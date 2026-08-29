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
import gs_struktur as GS  # noqa: E402
import index as IDX  # noqa: E402
import tracker as TR  # noqa: E402
import publish  # noqa: E402
import versioncheck as VC  # noqa: E402
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



def test_gs_struktur() -> None:
    """Mindmap-Hierarchie und Plakat-Legende zu einer Gliederung fuegen."""
    print("\ntest_gs_struktur")
    import xml.etree.ElementTree as ET

    mm = ET.fromstring(
        '<map><node TEXT="Wurzel">'
        '<node TEXT="APP (Anwendungen)">'
        '<node TEXT="APP.1.1 Office"><icon BUILTIN="full-2"/></node>'
        '<node TEXT="APP.1.9 Ohne Symbol"/>'
        "</node>"
        '<node><richcontent TYPE="NODE"><html><body><p>SYS.1.3 Linux</p>'
        "</body></html></richcontent><icon BUILTIN=\"full-1\"/></node>"
        "</node></map>")
    wurzel = mm.find("node")

    zeilen, ohne = [], []
    GS.gliederung(wurzel, 0, zeilen, ohne)
    check("Hierarchie eingerueckt", zeilen[1].startswith("- APP (") and
          zeilen[2].startswith("  - APP.1.1"), str(zeilen[:3]))
    check("Rang aus Symbol", "· **R2**" in zeilen[2], zeilen[2])
    check("richcontent gelesen", any("SYS.1.3 Linux" in z for z in zeilen), str(zeilen))
    check("Rang R1 erkannt", any("SYS.1.3 Linux · **R1**" in z for z in zeilen))
    # Ein rangloses Blatt ist auffaellig, ein Gruppenknoten nicht.
    check("rangloses Blatt gemeldet", ohne == ["APP.1.9 Ohne Symbol"], str(ohne))

    with tempfile.TemporaryDirectory() as tmp:
        plakat = Path(tmp) / "plakat.md"
        plakat.write_text(
            "> IT-Grundschutz-Kompendium 2023\n"
            "> : Zuerst umsetzen.\n> : Danach umsetzen.\n> : Zuletzt umsetzen.\n"
            "> Farben: neuer Baustein\n> Stand: Februar 2023\n", encoding="utf-8")
        erkl, fuss = GS.legende(plakat)
        check("drei Rangstufen erklaert", erkl == {1: "Zuerst umsetzen.",
                                                  2: "Danach umsetzen.",
                                                  3: "Zuletzt umsetzen."}, str(erkl))
        check("Fusszeilen erkannt", fuss == ["Farben: neuer Baustein",
                                             "Stand: Februar 2023"], str(fuss))



def test_versioncheck_historie() -> None:
    """Bewusst gefuehrte Altfassungen sind kein Mangel."""
    print("\ntest_versioncheck_historie")
    hist = VC.historisch()
    check("Historienregistry gelesen", isinstance(hist, dict) and hist, str(hist)[:80])
    check("OWASP 4.0 als historisch gefuehrt",
          any("owasp" in s for s in hist), str(list(hist)[:3]))
    check("Nachfolger benannt", all(v for v in hist.values()), str(hist))

    # Der Bericht darf eine Altfassung nicht als 'veraltet' zaehlen.
    f_hist = VC.Finding("alt", "Alt", "4.0", "4.2", "u", "historisch", "", "")
    f_alt = VC.Finding("x", "X", "1.0", "2.0", "u", "veraltet", "", "")
    text = VC.render([f_hist, f_alt])
    check("nur echte Veraltung gezaehlt", "veraltet: 1" in text, text[:200])
    check("historisch im Bericht benannt", "historisch" in text)



def test_fts5_query() -> None:
    """Alltagsschreibweisen duerfen nicht als FTS5-Syntax gelesen werden."""
    print("\ntest_fts5_query")
    q = IDX.fts5_query
    # Der Bindestrich im Wort war der Fehler: FTS5 las ihn als Spaltenfilter.
    check("Bindestrich gequotet", q("Mehrfaktor-Authentisierung Fernzugriff")
          == '"Mehrfaktor-Authentisierung" "Fernzugriff"', q("Mehrfaktor-Authentisierung Fernzugriff"))
    check("Punkte in IDs gequotet", q("OPS.1.1.3") == q("OPS.1.1.3"))
    check("Schraegstrich gequotet", '"IT/OT"' in q("IT/OT Netz") or q("IT/OT Netz") == "IT/OT Netz")
    # Ohne Sonderzeichen bleibt die Eingabe unangetastet.
    check("harmlose Eingabe unveraendert", q("Backup Konzept") == "Backup Konzept")
    # Bewusste FTS5-Syntax wird nicht entschaerft.
    check("Phrase bleibt", q('"genau so"') == '"genau so"')
    check("OR bleibt", q("Backup OR Sicherung") == "Backup OR Sicherung")
    check("NEAR bleibt", q("NEAR(Backup Test)") == "NEAR(Backup Test)")



def test_korpus_json() -> None:
    """Bestandsregister: ein verarbeitendes System darf nicht raten muessen."""
    print("\ntest_korpus_json")
    import json as J
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        (out / "a.docling.json").write_text("{}", encoding="utf-8")
        (out / "b.passthrough.json").write_text("{}", encoding="utf-8")
        docs = [TR.Doc(slug="a", source="a.pdf", coverage=100.0, pages=3),
                TR.Doc(slug="b", source="b.yml", coverage=100.0),
                TR.Doc(slug="c", source="c.pdf", coverage=99.0),
                TR.Doc(slug="scan", source="scan.pdf", coverage=None, ocr=True)]
        d = J.loads(TR.korpus_json(docs, out))
    check("alle Dokumente gelistet", d["documents_total"] == 4, str(d["documents_total"]))
    arten = {e["slug"]: e["struktur_art"] for e in d["documents"]}
    check("Docling erkannt", arten["a"] == "docling", str(arten))
    check("Passthrough erkannt", arten["b"] == "passthrough", str(arten))
    # Ohne Struktur-JSON darf nicht stillschweigend fehlen: es wird benannt.
    check("fehlende Struktur benannt", d["ohne_struktur_json"] == ["c", "scan"],
          str(d["ohne_struktur_json"]))
    check("kein Pfad erfunden", arten["c"] is None
          and d["documents"][2]["struktur_json"] is None)
    check("Befund mitgefuehrt", d["documents"][0]["befund"] == "vollstaendig",
          d["documents"][0]["befund"])
    # Ein Scan darf nicht wie ein woertlicher Extrakt aussehen: ein leeres
    # Deckungsfeld allein liesse sich als "unbekannt" lesen. Die Flags sagen
    # ausdruecklich, dass der Text geraten und nicht gelesen wurde.
    nach_slug = {e["slug"]: e for e in d["documents"]}
    check("Scan als nicht woertlich markiert",
          nach_slug["scan"]["woertlich"] is False and nach_slug["scan"]["ocr"] is True,
          str(nach_slug["scan"]))
    check("Extrakt mit Textlayer bleibt woertlich",
          nach_slug["a"]["woertlich"] is True and nach_slug["a"]["ocr"] is False,
          str(nach_slug["a"]))



def test_export_json() -> None:
    """Anforderungs-Export in der Form, die ein rechnendes System erwartet."""
    print("\ntest_export_json")
    import json as J
    g = publish.gruppe
    check("A.5.1 -> A.5", g("A.5.1") == "A.5", g("A.5.1"))
    check("APP.1.1.A1 -> APP.1.1", g("APP.1.1.A1") == "APP.1.1", g("APP.1.1.A1"))
    check("AM-01.01B -> AM-01", g("AM-01.01B") == "AM-01", g("AM-01.01B"))
    check("GC-01 -> GC", g("GC-01") == "GC", g("GC-01"))
    check("ohne Gliederung leer", g("PO") == "", g("PO"))

    treffer = {"A.5.1": publish.Section("A.5.1", "Policies", "Wortlaut.", 12)}
    d = J.loads(publish.export_json("iso27001-2022", "unbekannt",
                                    {"source_file": "n.pdf", "source_sha256": "ab"},
                                    treffer, ["A.5.2"]))
    check("Pflichtfelder vorhanden",
          set(d) >= {"frameworkId", "edition", "sourceFile", "sourceSha256",
                     "requirements", "missing"}, str(sorted(d)))
    r = d["requirements"][0]
    check("Anforderung vollstaendig",
          r == {"id": "A.5.1", "title": "Policies", "text": "Wortlaut.", "group": "A.5"}, str(r))
    # Nicht aufgeloeste IDs duerfen nicht als Anforderung ohne Wortlaut erscheinen.
    check("Luecke getrennt gefuehrt", d["missing"] == ["A.5.2"]
          and all(x["text"] for x in d["requirements"]), str(d["missing"]))
    check("keine Ausgabe erfunden", d["edition"] is None, str(d["edition"]))


def main() -> int:
    for fn in (test_page_markers, test_quality_gates, test_target_names,
               test_pipeline_options, test_verify, test_repair, test_office_verify,
               test_broken_ooxml_styles, test_text_passthrough,
               test_yaml_catalogue, test_gs_struktur,
               test_versioncheck_historie, test_fts5_query, test_korpus_json, test_export_json):
        fn()
    print()
    if failures:
        print(f"{len(failures)} Test(s) fehlgeschlagen: {', '.join(failures)}")
        return 1
    print("Alle Unit-Tests bestanden.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


def test_document_note_ohne_pruefbare_deckung(tmp_path: Path) -> None:
    """Ein Scan ohne Textlayer darf nicht wie ein geprueftes Dokument aussehen.

    Frueher stand in der Notiz "Wortdeckung — %": das liest sich wie ein
    Formatierungsfehler, nicht wie eine Aussage. Genau hier muss aber stehen,
    dass der Text aus der Zeichenerkennung stammt und niemand ihn gegen ein
    Original gehalten hat — sonst wandert OCR-Text als belegter Wortlaut in
    ein Audit.
    """
    import publish

    vault = tmp_path / "vault"
    (vault / "GRC" / "Handbuch").mkdir(parents=True)
    (vault / publish.LICENSED_DIR / "dokumente").mkdir(parents=True)
    md = tmp_path / "scan-ohne-textlayer.md"
    md.write_text("# Titel\n\nText aus OCR.\n", encoding="utf-8")

    meta = {"source_file": "Scan.pdf", "source_sha256": "abc", "pages": "14",
            "text_coverage_percent": "", "converter": "IBM Docling 2.123.0"}
    note, _ = publish.document_notes(md, vault, meta, "Text aus OCR.",
                                     "Titel", "Autor", "Foliensatz", False)
    t = note.read_text(encoding="utf-8")
    assert "Wortdeckung —" not in t, "kein Strich als Scheinwert"
    assert "Maschinell gelesen" in t, "Warnhinweis fehlt"
    assert "laesst sich nicht berechnen" in t
    assert "text_coverage_percent: null" in t
    assert "deckung_pruefbar: false" in t
    assert "erzeugt, nicht" in t and "extrahiert" in t

    meta["text_coverage_percent"] = "100.0"
    note2, _ = publish.document_notes(md, vault, meta, "Text.",
                                      "Titel2", "Autor", "Fachbuch", False)
    t2 = note2.read_text(encoding="utf-8")
    assert "Wortdeckung 100.0 %" in t2
    assert "deckung_pruefbar" not in t2


def test_deckung_braucht_tragfaehige_grundlage(tmp_path: Path) -> None:
    """Eine Deckungszahl gegen zwei Woerter ist kein Befund, sondern Zufall.

    Beobachtet an einem 291-Seiten-Scan: dessen Textlayer enthielt zwei
    Streuzeichen aus einer Kopfzeile. Der Vergleich fand beide im Extrakt
    wieder und meldete 100,0 % — fuer ein Dokument, dessen 195773 Woerter
    saemtlich aus der Zeichenerkennung stammten. Im Tracker haette es als
    "vollstaendig" gestanden, im Korpusregister als woertlich.

    Die alte Schutzklausel griff nur bei einer voellig leeren Grundlage.
    """
    import verify as V

    class Fake:
        def __init__(self, ref: int, ext: int) -> None:
            self.ref, self.ext = ref, ext

    def lauf(ref_woerter: int, ext_woerter: int) -> V.VerifyResult:
        md = tmp_path / f"e{ref_woerter}-{ext_woerter}.md"
        md.write_text(" ".join(f"wort{i}" for i in range(ext_woerter)), encoding="utf-8")
        quelle = tmp_path / f"q{ref_woerter}-{ext_woerter}.pdf"
        quelle.write_bytes(b"%PDF-1.4\n")
        seiten = {1: [f"wort{i}" for i in range(ref_woerter)]}
        echt = V.source_pages
        V.source_pages = lambda p: (seiten, {})
        try:
            return V.verify(quelle, md)
        finally:
            V.source_pages = echt

    duenn = lauf(2, 5000)
    assert duenn.coverage is None, "keine Zahl ohne tragfaehige Grundlage"
    assert "zu duenn" in (duenn.note or ""), duenn.note

    # Gegenprobe: ein kleines Dokument ist nicht verdaechtig, nur weil es klein
    # ist. Sonst faellt jede winzige Tabelle faelschlich in denselben Zweig.
    klein = lauf(30, 30)
    assert klein.coverage == 100.0, str(klein.coverage)
    assert not klein.note

    gesund = lauf(4800, 5000)
    assert gesund.coverage is not None and gesund.coverage > 90.0

    # Office-Formate bleiben aussen vor. Ein XLSX mit verbundenen Zellen
    # blaeht den Extrakt durch reine Wiederholung auf -- A3_Modellierung
    # kommt auf 4995 Quellwoerter gegen 114056 Extraktwoerter, ein
    # Verhaeltnis von 4,4 %, ohne dass ein einziges Wort ungeprueft waere.
    # Der Schutz gilt dem OCR-Fall, und OCR gibt es nur bei PDFs.
    md = tmp_path / "tabelle.md"
    md.write_text(" ".join(f"wort{i%20}" for i in range(5000)), encoding="utf-8")
    xlsx = tmp_path / "tabelle.xlsx"
    xlsx.write_bytes(b"PK\x03\x04")
    echt = V.source_pages
    V.source_pages = lambda p: ({1: [f"wort{i%20}" for i in range(200)]}, {})
    try:
        office = V.verify(xlsx, md)
    finally:
        V.source_pages = echt
    assert office.coverage == 100.0, str(office.coverage)
    assert not office.note, office.note


def test_tracker_befund_trennt_duenn_von_fehlend() -> None:
    """Ein zu duenner Textlayer ist nicht dasselbe wie gar keiner.

    Beide fuehren zu 'keine Deckungszahl', aber nur der zweite Fall ist
    offensichtlich. Der erste gab sich vorher als volle Deckung aus und
    gehoert deshalb im Protokoll beim Namen genannt, statt unter dem
    harmloseren Befund mitzulaufen.
    """
    import tracker as TR

    duenn = TR.Doc(slug="scan", coverage=None,
                   warnings=["Textlayer zu duenn fuer einen Wortvergleich: 2 "
                             "Referenzwoerter gegen 195773 Woerter im Extrakt."])
    leer = TR.Doc(slug="bild", coverage=None,
                  warnings=["Kein Textlayer im PDF (gescannt)"])
    voll = TR.Doc(slug="ok", coverage=100.0)

    assert duenn.verdict == "Textlayer zu duenn", duenn.verdict
    assert leer.verdict == "kein Textlayer", leer.verdict
    assert voll.verdict == "vollstaendig", voll.verdict

    # Dritter Fall: Markdown-Quelle. Kein zweiter Leser, also keine
    # Gegenprobe -- aber ein Textlayer fehlt hier nicht, es gibt schlicht
    # nur Text. "kein Textlayer" waere eine Falschaussage.
    md_quelle = TR.Doc(slug="md", coverage=None, warnings=[])
    assert md_quelle.verdict == "nicht gegengeprueft (Format)", md_quelle.verdict


def test_tracker_vault_luecken() -> None:
    """Fehlende Anforderungen im Vault-Geruest gehoeren ins Protokoll.

    Sie sind kein Extraktionsfehler: der Wortlaut liegt vor, nur das Raster
    kennt die ID nicht. Genau deshalb faellt so etwas sonst niemandem auf —
    eine Abdeckungsanalyse gegen ein unvollstaendiges Raster meldet keine
    Luecke, sie hat die Anforderung nie gesehen.
    """
    import tracker as TR

    g = TR.vault_gaps()
    assert g.get("offen_nach_korrektur"), "Registry ist leer"
    for e in g["offen_nach_korrektur"]:
        assert e.get("id") and e.get("befund"), str(e)
    assert g.get("hinweis") and g.get("ursache") and g.get("lehre")
    # Der Eintrag haelt eine Korrektur fest: der frueher gemeldete Mangel am
    # Vault existierte nicht, verglichen wurde gegen die falsche Menge. Das
    # gehoert benannt, nicht stillschweigend ersetzt.
    assert "KORREKTUR" in g["hinweis"]


def test_export_laengen_plausibel(tmp_path: Path) -> None:
    """Ein befuelltes Feld ist noch kein richtiges Feld.

    Der Grundschutz-Export trug im Median 54019 Zeichen je Anforderung statt
    der ueblichen paar hundert: die Ueberschriftenerkennung kannte keine
    Kennungen mit Buchstabenpraefix (APP.1.1.A1), fiel auf den Textanker
    zurueck, und der findet kein Ende — jede Anforderung schleppte den Rest
    des Dokuments mit. Die damalige Pruefung sah nur nach, ob ein Text da ist,
    ob IDs fehlen und ob welche doppelt sind. Alles gruen, alles falsch.

    Deshalb prueft dieser Test die Verteilung, nicht die Anwesenheit.
    """
    import publish

    body = "\n".join([
        "## APP.1.1.A1 Erste Anforderung (B)", "",
        "Die Institution MUSS das eine tun.", "",
        "## APP.1.1.A2 Zweite Anforderung (S)", "",
        "Die Institution SOLLTE das andere tun.", "",
        "## SYS.2.2.3.A7 Dritte Anforderung (H)", "",
        "Die Institution KANN das dritte tun.", "",
    ])
    s = publish.sections_from_headings(body)
    for ident in ("app.1.1.a1", "app.1.1.a2", "sys.2.2.3.a7"):
        assert ident in s, f"{ident} nicht erkannt — Buchstabenpraefix faellt durch"

    # INF, IND und ISMS beginnen mit Buchstaben, die auch roemische Ziffern
    # sind. Stand der roemische Zweig im Regex vorn, matchte er das blosse "I"
    # und lieferte die Kennung "I" statt "INF.1.A1" -- 49 Anforderungen
    # verloren dadurch ihre Abschnittsgrenze, waehrend der Median gesund
    # aussah. Ein Test nur mit APP und SYS haette das durchgelassen.
    roem = "\n".join([
        "## INF.1.A1 Planung der Gebaeudeabsicherung (B)", "",
        "Die Institution MUSS planen.", "",
        "## IND.2.1.A3 Nutzung sicherer Protokolle (S)", "",
        "Die Institution SOLLTE sichere Protokolle nutzen.", "",
        "## ISMS.1.A6 Integration in Ablaeufe (B)", "",
        "Die Institution MUSS integrieren.", "",
        "## X Nachfolgende Ueberschrift", "", "Ende.", "",
    ])
    sr = publish.sections_from_headings(roem)
    for ident in ("inf.1.a1", "ind.2.1.a3", "isms.1.a6"):
        assert ident in sr, f"{ident} nicht erkannt — roemischer Zweig greift zu frueh"
        assert len(sr[ident].text) < 120, \
            f"{ident} laeuft ueber seine Grenze hinaus: {len(sr[ident].text)}"
    assert "I" not in sr, "blosses 'I' als Kennung erkannt"

    # Die entscheidende Zusicherung: ein Abschnitt endet an der naechsten
    # Ueberschrift. Ohne sie sieht der Export vollstaendig aus und ist es nicht.
    assert "das andere" not in s["app.1.1.a1"].text, \
        "Abschnitt laeuft in die naechste Anforderung hinein"
    assert "das dritte" not in s["app.1.1.a2"].text
    laengen = [len(s[i].text) for i in ("app.1.1.a1", "app.1.1.a2", "sys.2.2.3.a7")]
    assert max(laengen) < 200, f"unplausibel lang: {laengen}"
