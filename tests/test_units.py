#!/usr/bin/env python3
"""Unit-Tests fuer die Teile der Pipeline, die ohne ML-Modelle pruefbar sind:
Qualitaetsgates, Seitenmarker-Export, Zielnamen, Pipeline-Optionen und die
Abweichungspruefung. Laeuft mit `python tests/test_units.py`.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import extract  # noqa: E402
import publish  # noqa: E402
import verify as V  # noqa: E402

FIXTURE_PDF = Path(__file__).parent / "fixtures" / "Muster-Norm-Zweispaltig.pdf"
failures: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    print(("  ok   " if cond else "  FAIL ") + name + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        failures.append(name)


class FakeDoc:
    """Minimaler DoclingDocument-Ersatz fuer den seitenweisen Export."""

    def __init__(self, pages: dict[int, str]):
        self.pages = pages
        self.tables = []

    def export_to_markdown(self, page_no: int | None = None) -> str:
        if page_no is None:
            return "\n\n".join(self.pages[p] for p in sorted(self.pages))
        return self.pages[page_no]


class NoPageDoc(FakeDoc):
    def export_to_markdown(self, page_no: int | None = None) -> str:  # kein page_no
        if page_no is not None:
            raise TypeError("unexpected keyword argument 'page_no'")
        return "## Ohne Seiten\n\nText."


def test_page_markers() -> None:
    print("Seitenmarker")
    doc = FakeDoc({1: "## 4 Kontext\n\nText A.", 2: "## Anhang A\n\nText B."})
    md = extract.to_markdown(doc, with_page_markers=True)
    check("Marker Seite 1", "<!-- page: 1 -->" in md)
    check("Marker Seite 2", "<!-- page: 2 -->" in md)
    check("Reihenfolge", md.index("Text A.") < md.index("Text B."))
    check("Fallback ohne page_no", "Ohne Seiten" in extract.to_markdown(NoPageDoc({1: ""}), True))
    check("ohne Marker", "<!-- page:" not in extract.to_markdown(doc, False))


def test_quality_gates() -> None:
    print("Qualitaetsgates")
    try:
        extract.check_quality("---\na: 1\n---\n\n   \n", 2, True, False)
        check("leerer Extrakt bricht ab", False)
    except extract.ExtractionError:
        check("leerer Extrakt bricht ab", True)

    warn = extract.check_quality("# T\n\nx\n", 10, True, False)
    check("textarme Seiten gemeldet", any("Zeichen/Seite" in w for w in warn))
    check("OCR-Hinweis", any("--ocr on" in w for w in warn))

    flat = "Fliesstext ohne Gliederung. " * 40
    check("fehlende Ueberschriften gemeldet",
          any("Ueberschriften" in w for w in extract.check_quality(flat, 1, True, False)))

    broken = "# T\n\n| a | b |\n|---|---|\n| 1 | 2 | 3 |\n\n" + "Text. " * 60
    check("kaputte Tabelle gemeldet",
          any("Spaltenstruktur" in w for w in extract.check_quality(broken, 1, True, False)))

    good = "# T\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n" + "Text. " * 60
    check("intakte Tabelle ohne Warnung",
          not any("Spaltenstruktur" in w for w in extract.check_quality(good, 1, True, False)))

    check("Encoding-Fehler gemeldet",
          any("U+FFFD" in w for w in extract.check_quality("# T\n\nTe�xt " * 40, 1, True, False)))


def test_target_names() -> None:
    print("Zielnamen")
    claimed: dict[str, Path] = {}
    a = extract.target_name(Path("/in/ISO 27001.pdf"), claimed)
    b = extract.target_name(Path("/in/ISO 27001.docx"), claimed)
    check("Slug normalisiert", a == "iso-27001", a)
    check("keine Kollision", a != b and b == "iso-27001-docx", b)
    check("stabil bei Wiederholung", extract.target_name(Path("/in/ISO 27001.pdf"), claimed) == a)
    check("Umlaute", extract.slugify("Prüfung Änderung") == "pruefung-aenderung")


def test_pipeline_options() -> None:
    print("Docling-Pipelineoptionen")
    try:
        conv = extract.build_converter(ocr=True)
    except Exception as exc:  # ohne Modelle darf der Aufbau nicht scheitern
        check("Converter baubar", False, str(exc))
        return
    from docling.datamodel.base_models import InputFormat

    opts = conv.format_to_options[InputFormat.PDF].pipeline_options
    check("OCR gesetzt", opts.do_ocr is True)
    check("Tabellenstruktur an", opts.do_table_structure is True)
    check("Cell-Matching an", opts.table_structure_options.do_cell_matching is True)
    check("TableFormer ACCURATE", str(opts.table_structure_options.mode).upper().endswith("ACCURATE"),
          str(opts.table_structure_options.mode))
    check("OCR abschaltbar", extract.build_converter(ocr=False)
          .format_to_options[InputFormat.PDF].pipeline_options.do_ocr is False)


def test_verify() -> None:
    print("Abweichungspruefung")
    if not FIXTURE_PDF.exists():
        check("Fixture vorhanden", False, str(FIXTURE_PDF))
        return
    pages, boiler = V.pdf_pages(FIXTURE_PDF)
    check("Seiten gelesen", len(pages) == 2, str(len(pages)))
    check("Kopf-/Fusszeile erkannt", any("testzwecken" in t for t in boiler[1]))
    check("Kopfzeile nicht im Inhalt", not any("testzwecken" in t for t in pages[1]))

    with tempfile.TemporaryDirectory() as tmp:
        full = Path(tmp) / "full.md"
        full.write_text("---\nx: 1\n---\n" + "\n".join(" ".join(t) for t in pages.values()),
                        encoding="utf-8")
        r = V.verify(FIXTURE_PDF, full)
        check("vollstaendig = 100 %", r.coverage == 100.0, str(r.coverage))

        gap = Path(tmp) / "gap.md"
        gap.write_text(full.read_text(encoding="utf-8")
                       .replace("kryptographie", "").replace("schlüsselverwaltung", ""),
                       encoding="utf-8")
        rg = V.verify(FIXTURE_PDF, gap)
        check("Luecke erkannt", rg.coverage < 99.5, str(rg.coverage))
        check("fehlende Woerter benannt", "kryptographie" in rg.missing_sample)
        check("Seite lokalisiert", rg.per_page[2] < rg.per_page[1])

        onepage = Path(tmp) / "p2.md"
        onepage.write_text("---\nx: 1\n---\n" + " ".join(pages[2]), encoding="utf-8")
        r1 = V.verify(FIXTURE_PDF, onepage)
        check("fehlende Seite erkannt", r1.per_page[1] < 50, str(r1.per_page))

        joined = Path(tmp) / "join.md"
        joined.write_text(full.read_text(encoding="utf-8")
                          .replace("informationssicherheitsrichtlinie n",
                                   "informationssicherheitsrichtlinien"), encoding="utf-8")
        rj = V.verify(FIXTURE_PDF, joined)
        check("Umbruch-Zusammenfuehrung kein Fehlalarm", rj.coverage == 100.0, str(rj.coverage))


def test_repair() -> None:
    print("Nachtrag fuer nicht zugeordneten Text")
    if not FIXTURE_PDF.exists():
        check("Fixture vorhanden", False, str(FIXTURE_PDF))
        return
    pages, _ = V.pdf_pages(FIXTURE_PDF)
    with tempfile.TemporaryDirectory() as tmp:
        # Extrakt, dem der Tabellentext fehlt (wie ein verschluckter Zellrest)
        gap = Path(tmp) / "gap.md"
        gap.write_text("---\nx: 1\n---\n" + " ".join(pages[1]), encoding="utf-8")
        lines = V.unassigned_lines(FIXTURE_PDF, gap)
        check("fehlende Quellzeilen gefunden", bool(lines), str(len(lines)))
        check("Seitenzahl mitgeliefert", all(isinstance(p, int) for p, _ in lines))
        check("Zellinhalt enthalten",
              any("Schlüsselverwaltung" in text for _, text in lines))

        md = extract.appendix(lines)
        check("Nachtrag hat Ueberschrift", md.startswith("## Nachtrag"))
        check("Nachtrag mit Seitenmarker", "<!-- page: 2 -->" in md)
        check("Nachtrag als Zitat", "\n> " in md)

        # Nach dem Anhaengen muss die Deckung 100 % erreichen
        fixed = Path(tmp) / "fixed.md"
        fixed.write_text(gap.read_text(encoding="utf-8") + "\n\n" + md, encoding="utf-8")
        check("Deckung nach Nachtrag 100 %", V.verify(FIXTURE_PDF, fixed).coverage == 100.0,
              str(V.verify(FIXTURE_PDF, fixed).coverage))

        # Vollstaendiger Extrakt: kein Nachtrag noetig
        full = Path(tmp) / "full.md"
        full.write_text("---\nx: 1\n---\n" + "\n".join(" ".join(v) for v in pages.values()),
                        encoding="utf-8")
        check("kein Nachtrag bei vollstaendigem Extrakt", V.unassigned_lines(FIXTURE_PDF, full) == [])


def test_office_verify() -> None:
    print("Pruefung von Office-Formaten")
    import tempfile as tf
    from docx import Document as Docx
    from openpyxl import Workbook

    with tf.TemporaryDirectory() as tmp:
        xlsx = Path(tmp) / "controls.xlsx"
        wb = Workbook()
        ws = wb.active
        for row in [("Control", "Anforderung"),
                    ("A.8.24", "Regeln fuer Kryptographie und Schluesselverwaltung"),
                    ("A.8.25", "Regeln fuer sichere Entwicklung")]:
            ws.append(row)
        wb.save(xlsx)

        pages, _ = V.office_pages(xlsx)
        check("xlsx gelesen", bool(pages) and "schluesselverwaltung" in pages[1],
              str(list(pages)))

        full = Path(tmp) / "full.md"
        full.write_text("---\nx: 1\n---\n" + " ".join(pages[1]), encoding="utf-8")
        check("xlsx vollstaendig = 100 %", V.verify(xlsx, full).coverage == 100.0)

        gap = Path(tmp) / "gap.md"
        gap.write_text(full.read_text(encoding="utf-8").replace("schluesselverwaltung", ""),
                       encoding="utf-8")
        rg = V.verify(xlsx, gap)
        check("xlsx Luecke erkannt", rg.coverage < 100.0, str(rg.coverage))
        check("xlsx Nachtrag findet die Zelle",
              any("Schluesselverwaltung" in text for _, text in V.unassigned_lines(xlsx, gap)))

        docx = Path(tmp) / "policy.docx"
        d = Docx()
        d.add_paragraph("Die Organisation muss Kryptographie regeln.")
        d.save(docx)
        dpages, _ = V.office_pages(docx)
        check("docx gelesen", "kryptographie" in dpages[1], str(dpages))

    check("Tabellenkalkulation ohne Ueberschriften-Warnung",
          not any("Ueberschriften" in w for w in
                  extract.check_quality("| a | b |\n|---|---|\n| 1 | 2 |\n" + "Text " * 60,
                                        1, False, False, ".xlsx")))


def test_broken_ooxml_styles() -> None:
    """Web-Exporte schreiben `<fill />` ohne patternFill — openpyxl bricht ab.

    Geprueft wird, dass die Container-Normalisierung die Datei lesbar macht
    und dabei kein Zellinhalt verloren geht.
    """
    import re
    import tempfile as tf
    import zipfile
    from openpyxl import Workbook, load_workbook

    with tf.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        good = tmpdir / "good.xlsx"
        wb = Workbook()
        ws = wb.active
        ws.append(("Control", "Anforderung"))
        ws.append(("A.8.24", "Regeln fuer Kryptographie"))
        wb.save(good)

        # styles.xml gezielt beschaedigen: patternFill aus den fills entfernen
        broken = tmpdir / "broken.xlsx"
        with zipfile.ZipFile(good) as zin, \
                zipfile.ZipFile(broken, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename.endswith("styles.xml"):
                    text = data.decode("utf-8")
                    text = re.sub(r"<fill>.*?</fill>", "<fill />", text, flags=re.S)
                    data = text.encode("utf-8")
                zout.writestr(item, data)

        try:
            load_workbook(broken, read_only=True, data_only=True)
            check("defektes Stylesheet bricht openpyxl ab", False, "kein Fehler")
        except TypeError:
            check("defektes Stylesheet bricht openpyxl ab", True)

        outdir = tmpdir / "fix"
        outdir.mkdir()
        repaired = V.normalize_ooxml_styles(broken, outdir)
        check("Reparatur liefert eine Kopie", repaired is not None and repaired.exists())

        readable, _tmp = V.readable_office_source(broken)
        pages, _ = V.office_pages(broken)
        check("repariertes xlsx wird gelesen",
              bool(pages) and "kryptographie" in pages[1], str(pages))
        check("Original bleibt unveraendert", readable != broken)

        # An intakten Dateien darf nichts repariert werden.
        check("intakte Datei wird nicht angefasst",
              V.normalize_ooxml_styles(good, outdir) is None)


def test_text_passthrough() -> None:
    """Formate ohne Docling-Reader werden zeichengetreu uebernommen."""
    print("\ntest_text_passthrough")
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        # Inhalt mit Backticks, damit der Zaun wachsen muss, und mit CRLF.
        content = "a: 1\r\n```\r\nnoch ein: wert\r\n"
        src = d / "kriterien.yml"
        src.write_bytes(content.encode("utf-8"))

        body, lines = extract.passthrough_body(src)
        check("Zeilen gezaehlt", lines == 3, f"{lines}")
        check("Zaun waechst ueber Quell-Backticks", "````yaml" in body, body[:80])

        fence = "`" * 4
        inner = body.split(fence + "yaml\n", 1)[1].rsplit("\n" + fence, 1)[0]
        check("Inhalt zeichengetreu", inner == "a: 1\n```\nnoch ein: wert", repr(inner))

        # .yml gilt als unterstuetzt, laeuft aber nicht ueber Docling.
        check("Suffix unterstuetzt", ".yml" in extract.SUPPORTED_SUFFIXES)
        check("nicht im Docling-Pfad", ".yml" not in extract.DOCLING_SUFFIXES)
        # .mm (FreeMind-Mindmap) ist XML und laeuft ueber denselben Pfad.
        check("mm unterstuetzt", ".mm" in extract.SUPPORTED_SUFFIXES)
        check("mm als XML eingezaeunt", extract.TEXT_FENCE_LANG[".mm"] == "xml")

        out = d / "out"
        res = extract.convert_file(
            None, src, out, ocr_mode="auto", page_markers=True,
            write_json=False, force=True, claimed={}, do_verify=True,
            min_coverage=99.0, repair=True,
        )
        check("Konverter markiert", res.converter == "passthrough", res.converter)
        check("Deckung 100 %", res.text_coverage == 100.0, str(res.text_coverage))
        check("Warnung gesetzt", any("keinen Reader" in w for w in res.warnings))
        md = Path(res.output).read_text(encoding="utf-8")
        check("Front-Matter nennt Passthrough", "ACSOS Passthrough" in md)
        check("Quelltext im Extrakt", "noch ein: wert" in md)



def test_yaml_catalogue() -> None:
    """Maschinenlesbarer Katalog (BSI C5 als YAML) -> Anforderungsabschnitte."""
    print("\ntest_yaml_catalogue")

    flach = """<!-- irgendein Vorspann -->
```yaml
-
  id: 'GC-01'
  name: 'Angaben zum Recht'
  condition: 'Der Anbieter macht Angaben zu:\n\n1. dem anwendbaren Recht.'
  hint: 'Vgl. Abschnitt 1.2.'
```
"""
    got = publish.sections_from_yaml(flach, {"source_file": "GC.yml"})
    check("flache Form gefunden", "gc-01" in got, str(sorted(got)))
    sec = got.get("gc-01")
    check("Titel aus name", bool(sec) and sec.title == "Angaben zum Recht")
    check("Normtext woertlich", bool(sec) and "dem anwendbaren Recht." in sec.text)
    check("Hinweis getrennt", bool(sec) and "[!info] Hinweis der Quelle" in sec.text)
    check("Schluesselpfad statt Seite",
          bool(sec) and sec.page == 0 and sec.locator == "GC-01 in GC.yml")

    verschachtelt = """```yaml
-
  identifier: '01'
  name: 'Rahmenwerk'
  basic:
    -
      identifier: '01B'
      criterion: 'Ein Rahmenwerk ist dokumentiert.'
  additional_complement:
    -
      identifier: '01AC'
      criterion: 'Zusaetzlich werden Informationen beruecksichtigt.'
  information:
    -
      information_text: 'Assets sind Objekte im Verantwortungsbereich.'
```
"""
    got = publish.sections_from_yaml(verschachtelt, {"source_file": "AM.yml"})
    check("Unterkriterium Basic", "am-01.01b" in got, str(sorted(got)))
    check("Unterkriterium Complement", "am-01.01ac" in got)
    check("Kriterienbereich aus information", "am-01" in got)
    check("Gruppe aus Dateiname",
          got.get("am-01.01b") is not None
          and got["am-01.01b"].text.startswith("Ein Rahmenwerk"))
    check("Belegstelle nennt Zweig",
          got.get("am-01.01b") is not None
          and got["am-01.01b"].locator == "basic/01B in AM.yml")

    # Kein Katalog: Passthrough einer Konfigurationsdatei darf nichts liefern.
    check("Nicht-Katalog ergibt nichts",
          publish.sections_from_yaml("```yaml\nversion: '1.1.0'\n```\n",
                                     {"source_file": "Version-und-Lizenz.yml"}) == {})
    check("ohne YAML-Block nichts",
          publish.sections_from_yaml("# Ohne Block\n", {"source_file": "AM.yml"}) == {})

    # Nur ein Katalog darf das Fehlen einer ID belegen.
    check("Katalog nennt seine Gruppe",
          publish.yaml_catalogue_group(verschachtelt, {"source_file": "AM.yml"}) == "AM")
    check("PDF-Extrakt ist kein Katalog",
          publish.yaml_catalogue_group("## 4.1 Kontext\n\nText.\n",
                                       {"source_file": "norm.pdf"}) is None)
    note = publish.withdrawn_note("bsi-c5", "AM-01.02AC", {"source_file": "AM.yml"})
    check("Entfallen-Notiz kennzeichnet Status", "status: entfallen" in note)
    check("Entfallen-Notiz erfindet keinen Text", "> [!quote]" not in note)
    check("Entfallen-Notiz warnt vor Zitat", "Nicht als geltende Anforderung zitieren" in note)

    # Ueberholte Fassungen: Wortlaut bleibt, Geltung nicht.
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        src = d / "alt.md"
        src.write_text("# Alt\n\nAlter Wortlaut.\n", encoding="utf-8")
        vault = d / "vault"
        (vault / "GRC" / "Handbuch").mkdir(parents=True)
        m = {"source_file": "Alt.pdf", "source_sha256": "ab" * 32, "pages": "3"}
        note, full = publish.document_notes(src, vault, m, "Alter Wortlaut.",
                                            "Alte Fassung", "BSI", "Leitfaden",
                                            dry_run=False, superseded_by="neu-2026")
        txt = note.read_text(encoding="utf-8")
        check("Historie: Status gesetzt", "status: historisch" in txt)
        check("Historie: Nachfolger genannt", "superseded_by: neu-2026" in txt)
        check("Historie: warnt vor Zitat", "nicht als geltend zitieren" in txt)
        check("Historie: eigener Tag", "grc/historisch" in txt)
        check("Historie: Wortlaut bleibt", "Alter Wortlaut." in full.read_text(encoding="utf-8"))

        note2, _ = publish.document_notes(src, vault, m, "Alter Wortlaut.",
                                          "Normale Fassung", "BSI", "Leitfaden",
                                          dry_run=False)
        t2 = note2.read_text(encoding="utf-8")
        check("ohne Nachfolger keine Warnung", "status: historisch" not in t2)


def main() -> int:
    for fn in (test_page_markers, test_quality_gates, test_target_names,
               test_pipeline_options, test_verify, test_repair, test_office_verify,
               test_broken_ooxml_styles, test_text_passthrough,
               test_yaml_catalogue):
        fn()
    print()
    if failures:
        print(f"{len(failures)} Test(s) fehlgeschlagen: {', '.join(failures)}")
        return 1
    print("Alle Unit-Tests bestanden.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
