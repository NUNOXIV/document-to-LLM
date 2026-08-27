#!/usr/bin/env python3
"""ACSOS document-to-LLM — verlaessliche Norm-/Regulatorik-Extraktion.

Konvertiert GRC-Dokumente (PDF, DOCX, XLSX, PPTX, HTML) mit IBM Docling in
strukturiertes, LLM-lesbares Markdown.

Grundsatz: Die Extraktion macht ausschliesslich Docling. Dieses Skript baut
keinen eigenen Parser, es steuert die Pipeline, sichert Provenienz (Hash,
Seitenzahlen, Versionen) und prueft das Ergebnis auf Strukturverlust.

Beispiele:
    python extract.py input/ISO-27001.pdf
    python extract.py input/ --recursive --ocr auto
    python extract.py input/BSI.pdf -o output --json --force
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path

import click

# --------------------------------------------------------------------------
# Von Docling unterstuetzte Eingabeformate (Dateiendungen).
# --------------------------------------------------------------------------
SUPPORTED_SUFFIXES = {
    ".pdf", ".docx", ".xlsx", ".pptx", ".html", ".htm",
    ".md", ".adoc", ".asciidoc", ".csv", ".png", ".jpg", ".jpeg", ".tiff", ".bmp",
}

# Ab wie wenig Zeichen pro Seite ein PDF als "vermutlich gescannt" gilt.
LOW_TEXT_CHARS_PER_PAGE = 120


class ExtractionError(RuntimeError):
    """Konvertierung ist fehlgeschlagen oder das Ergebnis ist unbrauchbar."""


@dataclass
class Result:
    source: str
    source_sha256: str
    source_bytes: int
    output: str | None = None
    json_output: str | None = None
    pages: int = 0
    characters: int = 0
    headings: int = 0
    tables: int = 0
    ocr_used: bool = False
    table_mode: str = "accurate"
    docling_status: str = "success"
    failed_pages: list[int] = field(default_factory=list)
    text_coverage: float | None = None   # Wortdeckung Quelle -> Extrakt (nur PDF)
    repaired_lines: int = 0              # als Nachtrag ergaenzte Quellzeilen
    duration_s: float = 0.0
    status: str = "ok"          # ok | warn | error | skipped
    warnings: list[str] = field(default_factory=list)
    error: str | None = None


# --------------------------------------------------------------------------
# Hilfsfunktionen
# --------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def slugify(name: str) -> str:
    """Dateiname -> stabiler, zitierfaehiger Slug (ASCII, klein, mit Bindestrich)."""
    trans = {"ä": "ae", "ö": "oe", "ü": "ue", "Ä": "ae", "Ö": "oe", "Ü": "ue", "ß": "ss"}
    for src, dst in trans.items():
        name = name.replace(src, dst)
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    return re.sub(r"-{2,}", "-", name).strip("-") or "dokument"


def docling_version() -> str:
    try:
        from importlib.metadata import version

        return version("docling")
    except Exception:  # pragma: no cover - nur Metadaten
        return "unbekannt"


def collect_inputs(paths: tuple[str, ...], recursive: bool) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        p = Path(raw).expanduser()
        if p.is_dir():
            it = p.rglob("*") if recursive else p.glob("*")
            files.extend(
                f for f in sorted(it)
                if f.is_file() and f.suffix.lower() in SUPPORTED_SUFFIXES
            )
        elif p.is_file():
            files.append(p)
        else:
            raise click.BadParameter(f"Pfad nicht gefunden: {p}")
    # Duplikate (gleicher realer Pfad) entfernen, Reihenfolge beibehalten.
    seen: set[Path] = set()
    unique: list[Path] = []
    for f in files:
        rp = f.resolve()
        if rp not in seen:
            seen.add(rp)
            unique.append(f)
    return unique


# --------------------------------------------------------------------------
# Docling-Pipeline
# --------------------------------------------------------------------------
def build_converter(ocr: bool, models_dir: Path | None = None, table_mode: str = "accurate"):
    """DocumentConverter mit Compliance-tauglichen Defaults.

    - TableFormer im ACCURATE-Modus: verschachtelte Control-Tabellen bleiben
      als Markdown-Tabellen erhalten statt zu Fliesstext zu zerfallen.
    - Cell-Matching an: Zellinhalte werden aus dem PDF-Textlayer uebernommen,
      nicht aus dem Modell rekonstruiert (keine erfundenen Zellwerte).

    ACCURATE ist der Standard. Faellt eine Seite damit aus (das Modell bringt auf
    manchen Systemen einzelne Seiten zum Absturz), wiederholt convert_file den
    Lauf mit FAST und vermerkt das im Extrakt.
    """
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions

    opts = PdfPipelineOptions()
    if models_dir is not None:
        # Vorab geladene Docling-Checkpoints (air-gapped Betrieb, kein HF-Zugriff).
        opts.artifacts_path = str(models_dir)
    opts.do_ocr = ocr
    opts.do_table_structure = True
    opts.table_structure_options.do_cell_matching = True
    try:
        from docling.datamodel.pipeline_options import TableFormerMode

        opts.table_structure_options.mode = (
            TableFormerMode.ACCURATE if table_mode == "accurate" else TableFormerMode.FAST
        )
    except Exception:
        pass  # aeltere Docling-Version: Default-Modus ist ausreichend

    return DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )


# --------------------------------------------------------------------------
# Konvertierung im eigenen Prozess
# --------------------------------------------------------------------------
# Das Tabellenmodell bringt auf manchen Systemen den Prozess per Speicherzugriffs-
# fehler zum Absturz (Signal 11). In einem Batch wuerde das alle noch offenen
# Dokumente mitreissen. Deshalb laeuft die eigentliche Konvertierung in einem
# Worker-Prozess: stirbt er, verliert nur dieses eine Dokument seinen Versuch.
def _worker(src_str: str, ocr: bool, models: str | None, table_mode: str,
            page_markers: bool, want_json: bool) -> dict:
    src = Path(src_str)
    conv = build_converter(ocr, Path(models) if models else None, table_mode)
    result = conv.convert(src, raises_on_error=False)
    doc = result.document
    md = to_markdown(doc, page_markers)
    return {
        "markdown": md,
        "pages": page_count(doc),
        "tables": count_tables(doc, md),
        "status": str(getattr(result.status, "name", result.status)).lower(),
        "failed_pages": sorted({e.page_no for e in (result.errors or [])
                                if e.page_no is not None}),
        "errors": [e.error_message for e in (result.errors or [])][:3],
        "json": doc.export_to_dict() if want_json else None,
    }


class _Runner:
    """Haelt einen Worker-Prozess, damit die Modelle nicht je Dokument neu
    geladen werden, und ersetzt ihn, wenn er abgestuerzt ist."""

    def __init__(self) -> None:
        self._pool = None

    def _get(self):
        if self._pool is None:
            from concurrent.futures import ProcessPoolExecutor

            self._pool = ProcessPoolExecutor(max_workers=1)
        return self._pool

    def reset(self) -> None:
        if self._pool is not None:
            self._pool.shutdown(wait=False, cancel_futures=True)
        self._pool = None

    def run(self, *args) -> dict:
        """Fuehrt eine Konvertierung aus. Stirbt der Worker, wird das als
        ExtractionError sichtbar — der Batch laeuft weiter."""
        from concurrent.futures.process import BrokenProcessPool

        try:
            return self._get().submit(_worker, *args).result()
        except BrokenProcessPool as exc:
            self.reset()
            raise ExtractionError(
                "Konvertierungsprozess abgestuerzt (Speicherzugriffsfehler im "
                "Docling-Modell)"
            ) from exc


def page_count(doc) -> int:
    try:
        return len(doc.pages)
    except Exception:
        return 0


def to_markdown(doc, with_page_markers: bool) -> str:
    """Markdown-Export via Docling.

    Mit Seitenmarkern wird pro Seite exportiert, damit jede Aussage im Output
    auf eine Seitenzahl der Quelle zurueckfuehrbar ist (Zitierfaehigkeit).
    Faellt auf den Gesamtexport zurueck, wenn die Docling-Version keinen
    seitenweisen Export unterstuetzt.
    """
    total = page_count(doc)
    if with_page_markers and total:
        try:
            parts: list[str] = []
            for page_no in range(1, total + 1):
                chunk = doc.export_to_markdown(page_no=page_no)
                parts.append(f"<!-- page: {page_no} -->\n\n{chunk.strip()}\n")
            body = "\n".join(parts)
            if body.replace("<!-- page:", "").strip(" -0123456789>\n<!"):
                return body
        except TypeError:
            pass  # kein page_no-Parameter in dieser Version
        except Exception:
            pass
    return doc.export_to_markdown()


def count_tables(doc, markdown: str) -> int:
    try:
        return len(doc.tables)
    except Exception:
        return sum(1 for line in markdown.splitlines() if re.match(r"^\s*\|\s*-{3,}", line))


# --------------------------------------------------------------------------
# Qualitaetspruefung des Outputs
# --------------------------------------------------------------------------
def check_quality(md: str, pages: int, is_pdf: bool, ocr: bool) -> list[str]:
    warnings: list[str] = []
    body = re.sub(r"^---\n.*?\n---\n", "", md, flags=re.S)
    text = body.strip()

    if not text:
        raise ExtractionError("Leerer Markdown-Output — Konvertierung unbrauchbar.")

    if is_pdf and pages:
        per_page = len(text) / pages
        if per_page < LOW_TEXT_CHARS_PER_PAGE and not ocr:
            warnings.append(
                f"Nur {per_page:.0f} Zeichen/Seite — vermutlich gescanntes PDF. "
                f"Erneut mit --ocr on ausfuehren."
            )
        elif per_page < LOW_TEXT_CHARS_PER_PAGE:
            warnings.append(
                f"Nur {per_page:.0f} Zeichen/Seite trotz OCR — Quelle pruefen."
            )

    headings = len(re.findall(r"^#{1,6}\s+\S", body, flags=re.M))
    if headings == 0:
        warnings.append(
            "Keine Ueberschriften erkannt — Gliederung (z. B. 4.1, A.5.1) ging "
            "moeglicherweise verloren. Fuer Zitate Seitenmarker nutzen."
        )

    # Tabellenkonsistenz: gleiche Spaltenzahl je Block, Trennzeile vorhanden.
    block: list[str] = []
    broken = 0
    for line in body.splitlines() + [""]:
        if line.lstrip().startswith("|"):
            block.append(line)
            continue
        if block:
            widths = {row.count("|") for row in block}
            has_sep = any(re.match(r"^\s*\|[\s:|-]+\|\s*$", r) for r in block)
            if len(widths) > 1 or not has_sep:
                broken += 1
            block = []
    if broken:
        warnings.append(
            f"{broken} Tabellenblock/-bloecke mit inkonsistenter Spaltenstruktur — "
            f"vor Zitat aus Tabellen gegen die Quelle pruefen."
        )

    # Zellverschiebung: rutscht der Rest einer Zelle in die naechste Zeile
    # (kommt an Seitenumbruechen in fortgesetzten Tabellen vor), beginnt der
    # Zellinhalt mitten im Satz. Fuer Normtabellen ist das gefaehrlich, weil die
    # Anforderung dann beim falschen Control steht.
    spilled: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or re.match(r"^\|[\s:|-]+\|$", stripped):
            continue
        for cell in [c.strip() for c in stripped.strip("|").split("|")]:
            # Inhaltsverzeichnisse mit Punktfuehrung sind keine Verschiebung.
            if re.search(r"\.{5,}", cell):
                continue
            if len(cell) > 25 and cell[:1].islower() and " " in cell:
                spilled.append(cell[:60])
                break
    if spilled:
        warnings.append(
            f"{len(spilled)} Tabellenzelle(n) beginnen mitten im Satz — moegliche "
            f"Zellverschiebung, z. B. \"{spilled[0]}...\". Zeilen dieser Tabelle vor "
            f"dem Zitat gegen die Quelle pruefen."
        )

    if "�" in body:
        warnings.append("Ersatzzeichen (U+FFFD) im Text — Encoding-/Font-Problem.")

    return warnings


def appendix(lines: list[tuple[int, str]]) -> str:
    """Nachtrag mit Quelltext, den kein Docling-Element aufgenommen hat."""
    out = [
        "## Nachtrag: nicht zugeordneter Quelltext",
        "",
        "<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- "
        "oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, "
        "damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, "
        "Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite "
        "angeben und den Zusammenhang in der Quelle pruefen. -->",
        "",
    ]
    current = None
    for page_no, text in lines:
        if page_no != current:
            out.append(f"<!-- page: {page_no} -->")
            out.append("")
            current = page_no
        out.append(f"> {text}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def front_matter(src: Path, res: Result, ocr_mode: str) -> str:
    def esc(v: str) -> str:
        return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'

    lines = [
        "---",
        f"source_file: {esc(src.name)}",
        f"source_sha256: {res.source_sha256}",
        f"source_bytes: {res.source_bytes}",
        f"pages: {res.pages}",
        f"tables: {res.tables}",
        f"converter: {esc('IBM Docling ' + docling_version())}",
        f"ocr: {str(res.ocr_used).lower()} # mode={ocr_mode}",
        f"table_mode: {res.table_mode}",
        f"docling_status: {res.docling_status}",
        f"converted_at: {esc(datetime.now(timezone.utc).isoformat(timespec='seconds'))}",
    ]
    if res.text_coverage is not None:
        lines.append(f"text_coverage_percent: {res.text_coverage}")
    if res.repaired_lines:
        lines.append(f"appended_source_lines: {res.repaired_lines}")
    lines += [
        "extraction_status: " + res.status,
    ]
    if res.warnings:
        lines.append("warnings:")
        lines.extend(f"  - {esc(w)}" for w in res.warnings)
    lines.append("---")
    lines.append("")
    lines.append(
        "<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. "
        "Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl "
        "aus den <!-- page: N --> Markern belegen. -->"
    )
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Konvertierung einer Datei
# --------------------------------------------------------------------------
def target_name(src: Path, claimed: dict[str, Path]) -> str:
    """Stabiler Zielname; bei gleichem Stem in mehreren Formaten wird das
    Quellformat angehaengt (ISO.pdf und ISO.docx duerfen sich nicht ueberschreiben)."""
    base = slugify(src.stem)
    owner = claimed.get(base)
    if owner is None or owner == src.resolve():
        claimed[base] = src.resolve()
        return base
    name = f"{base}-{src.suffix.lstrip('.').lower()}"
    claimed.setdefault(name, src.resolve())
    return name


def convert_file(
    runner: "_Runner",
    src: Path,
    out_dir: Path,
    *,
    ocr_mode: str,
    write_json: bool,
    page_markers: bool,
    force: bool,
    claimed: dict[str, Path],
    do_verify: bool,
    min_coverage: float,
    repair: bool,
    mdir_ref: tuple[Path | None, ...] = (None,),
) -> Result:
    started = time.perf_counter()
    res = Result(
        source=str(src),
        source_sha256=sha256_of(src),
        source_bytes=src.stat().st_size,
    )
    stem = target_name(src, claimed)
    target = out_dir / f"{stem}.md"

    if target.exists() and not force:
        existing = target.read_text(encoding="utf-8", errors="replace")
        if res.source_sha256 in existing:
            res.status = "skipped"
            res.output = str(target)
            res.duration_s = round(time.perf_counter() - started, 2)
            return res

    is_pdf = src.suffix.lower() == ".pdf"
    ocr = ocr_mode == "on"
    table_mode = "accurate"
    mdir = mdir_ref[0]
    res_json = None

    def run(mode: str, use_ocr: bool) -> dict:
        return runner.run(str(src), use_ocr, str(mdir) if mdir else None, mode,
                          page_markers, write_json)

    for attempt in ("first", "ocr-retry"):
        try:
            try:
                out = run(table_mode, ocr)
            except ExtractionError:
                # Absturz mit ACCURATE: derselbe Lauf mit FAST hat gute Chancen.
                click.echo("    Konvertierung abgestuerzt — wiederhole mit "
                           "TableFormer FAST", err=True)
                table_mode = "fast"
                out = run(table_mode, ocr)
            failed = out["failed_pages"]
            status = out["status"]

            # Seitenfehler mit ACCURATE: erst denselben Modus wiederholen (der
            # Fehler ist sporadisch), dann erst auf FAST wechseln — FAST liefert
            # grobere Tabellen und ist die schlechtere Wahl.
            if (failed or status != "success") and table_mode == "accurate":
                click.echo("    Seitenfehler mit TableFormer ACCURATE — zweiter Versuch",
                           err=True)
                try:
                    retry = run("accurate", ocr)
                except ExtractionError:
                    retry = None
                if retry and not retry["failed_pages"] and retry["status"] == "success":
                    out, failed, status = retry, retry["failed_pages"], retry["status"]
                else:
                    click.echo("    erneut fehlgeschlagen — wiederhole mit FAST", err=True)
                    table_mode = "fast"
                    out = run(table_mode, ocr)
                    failed, status = out["failed_pages"], out["status"]

            res.table_mode = table_mode
            res.docling_status = status
            res.failed_pages = failed
            if status in ("failure", "skipped"):
                raise ExtractionError(
                    f"Docling meldet Status {status}: {'; '.join(out['errors'])}")
        except ExtractionError:
            raise
        except Exception as exc:
            detail = str(exc)
            if any(t in detail for t in ("403", "huggingface", "Forbidden", "Connection", "resolve")):
                raise ExtractionError(
                    f"Docling-Modelle nicht verfuegbar ({detail}). Die Layout-/Tabellenmodelle "
                    f"werden beim ersten PDF-Lauf von huggingface.co geladen. In Umgebungen ohne "
                    f"HF-Zugriff einmalig vorab holen: 'docling-tools models download' und den "
                    f"Cache ueber HF_HOME bereitstellen."
                ) from exc
            raise ExtractionError(f"Docling-Konvertierung fehlgeschlagen: {exc}") from exc

        res.pages = out["pages"]
        md_body = out["markdown"]
        res_json = out["json"]
        plain = md_body.strip()

        # Automatischer OCR-Fallback bei Textarmut (nur einmal).
        needs_ocr = (
            is_pdf
            and ocr_mode == "auto"
            and attempt == "first"
            and res.pages
            and len(plain) / res.pages < LOW_TEXT_CHARS_PER_PAGE
        )
        if needs_ocr:
            click.echo("    textarm — wiederhole mit OCR", err=True)
            ocr = True
            continue
        break

    res.ocr_used = ocr
    res.characters = len(md_body)
    res.tables = out["tables"]
    res.headings = len(re.findall(r"^#{1,6}\s+\S", md_body, flags=re.M))
    res.warnings = check_quality(md_body, res.pages, is_pdf, ocr)
    if res.failed_pages:
        res.warnings.insert(0, (
            f"Docling konnte {len(res.failed_pages)} Seite(n) nicht verarbeiten: "
            f"{', '.join(str(p) for p in res.failed_pages)}. Inhalt dieser Seiten fehlt."
        ))
    if res.table_mode != "accurate":
        res.warnings.append(
            "Tabellenmodell auf FAST zurueckgefallen (ACCURATE brach ab). "
            "Tabellenstruktur ist etwas grober; Zellinhalte stammen weiterhin aus dem Textlayer."
        )
    res.status = "warn" if res.warnings else "ok"

    # Abweichungspruefung: enthaelt der Extrakt den Text der Quelle vollstaendig?
    if is_pdf and do_verify:
        try:
            from verify import verify as verify_extract

            tmp = out_dir / f".{stem}.tmp.md"
            out_dir.mkdir(parents=True, exist_ok=True)
            tmp.write_text(md_body, encoding="utf-8")
            try:
                vres = verify_extract(src, tmp)
            finally:
                tmp.unlink(missing_ok=True)
            if vres.note:
                res.warnings.append(vres.note)
            else:
                res.text_coverage = vres.coverage

                # Fehlt Quelltext (typisch: ein Zellrest, den das Tabellenmodell
                # verschluckt), wird er woertlich als markierter Nachtrag
                # angehaengt. Lieber unstrukturiert vorhanden als still verloren.
                if repair and vres.coverage < 100.0:
                    from verify import unassigned_lines

                    tmp2 = out_dir / f".{stem}.tmp2.md"
                    tmp2.write_text(md_body, encoding="utf-8")
                    try:
                        extra = unassigned_lines(src, tmp2)
                    finally:
                        tmp2.unlink(missing_ok=True)
                    if extra:
                        md_body = md_body.rstrip() + "\n\n" + appendix(extra)
                        res.repaired_lines = len(extra)
                        tmp3 = out_dir / f".{stem}.tmp3.md"
                        tmp3.write_text(md_body, encoding="utf-8")
                        try:
                            vres = verify_extract(src, tmp3)
                        finally:
                            tmp3.unlink(missing_ok=True)
                        res.text_coverage = vres.coverage
                        res.warnings.append(
                            f"{len(extra)} Quellzeile(n) wurden vom Layout-/Tabellenmodell "
                            f"keinem Element zugeordnet und stehen woertlich im Abschnitt "
                            f"'Nachtrag: nicht zugeordneter Quelltext' — dort ohne "
                            f"Tabellenstruktur."
                        )

                if vres.coverage < min_coverage:
                    worst = ", ".join(f"S.{p}: {c} %" for p, c in vres.worst_pages[:3])
                    res.warnings.append(
                        f"Wortdeckung nur {vres.coverage} % (gefordert {min_coverage} %). "
                        f"Schwaechste Seiten: {worst}. Fehlend u. a.: "
                        f"{', '.join(vres.missing_sample[:8])}"
                    )
        except Exception as exc:
            res.warnings.append(f"Abweichungspruefung nicht durchfuehrbar: {exc}")
        res.status = "warn" if res.warnings else "ok"

    out_dir.mkdir(parents=True, exist_ok=True)
    target.write_text(front_matter(src, res, ocr_mode) + md_body.rstrip() + "\n", encoding="utf-8")
    res.output = str(target)

    if write_json and res_json is not None:
        jtarget = out_dir / f"{stem}.docling.json"
        jtarget.write_text(json.dumps(res_json, ensure_ascii=False, indent=2), encoding="utf-8")
        res.json_output = str(jtarget)

    res.duration_s = round(time.perf_counter() - started, 2)
    return res


def write_manifest(out_dir: Path, results: list[Result]) -> Path:
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "converter": f"IBM Docling {docling_version()}",
        "tool": "ACSOS document-to-LLM/extract.py",
        "documents": [asdict(r) for r in results],
    }
    path = out_dir / "manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def run_doctor(models_dir: Path | None) -> int:
    """Preflight: laeuft der PDF-Pfad in dieser Umgebung wirklich?"""
    click.echo(f"Docling:        {docling_version()}")
    fixture = Path(__file__).parent / "tests" / "fixtures" / "Muster-Norm-Zweispaltig.pdf"
    if not fixture.exists():
        click.secho("Test-PDF fehlt (tests/fixtures) — Pruefung nicht moeglich.", fg="yellow")
        return 1

    try:
        from verify import pdf_pages

        pages, _ = pdf_pages(fixture)
        click.secho(f"PDF-Textlayer:  ok ({len(pages)} Seiten gelesen)", fg="green")
    except Exception as exc:
        click.secho(f"PDF-Textlayer:  FEHLER — {exc}", fg="red")
        return 1

    click.echo("PDF-Modelle:    lade Layout-/Tabellenmodell ...")
    try:
        conv = build_converter(False, models_dir)
        doc = conv.convert(fixture).document
        md = doc.export_to_markdown()
    except Exception as exc:
        click.secho(f"PDF-Modelle:    FEHLER — {exc}", fg="red")
        click.echo(
            "\nDie Layout- und Tabellenmodelle kommen von huggingface.co. Ist der Host\n"
            "gesperrt, einmalig auf einer Maschine mit Zugriff holen und mitgeben:\n"
            "  docling-tools models download -o ./docling-models\n"
            "  python extract.py datei.pdf --models-dir ./docling-models\n"
            "  (oder ACSOS_DOCLING_MODELS=./docling-models setzen)"
        )
        return 1

    ok_table = "| A.8.24" in md or "A.8.24" in md
    click.secho(f"PDF-Modelle:    ok ({len(md)} Zeichen, Tabelle erkannt: {ok_table})", fg="green")
    click.secho("Bereit fuer PDF-Extraktion.", fg="green")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("inputs", nargs=-1, type=click.Path())
@click.option("-o", "--output", "output_dir", default="output", show_default=True,
              type=click.Path(file_okay=False), help="Zielordner fuer die Markdown-Dateien.")
@click.option("--ocr", "ocr_mode", type=click.Choice(["auto", "on", "off"]), default="auto",
              show_default=True,
              help="auto = OCR nur bei textarmen PDFs nachziehen; on = immer; off = nie.")
@click.option("-r", "--recursive", is_flag=True, help="Ordner rekursiv einlesen.")
@click.option("--json", "write_json", is_flag=True,
              help="Zusaetzlich das verlustfreie DoclingDocument als JSON ablegen (Basis fuer index.py).")
@click.option("--no-page-markers", is_flag=True,
              help="Ohne <!-- page: N --> Marker exportieren (nicht empfohlen: Zitate werden unbelegbar).")
@click.option("--verify/--no-verify", "do_verify", default=True, show_default=True,
              help="PDF-Extrakte gegen den Textlayer der Quelle pruefen (Wortdeckung).")
@click.option("--min-coverage", default=99.5, show_default=True,
              help="Geforderte Wortdeckung in Prozent; darunter Warnung (mit --strict Exit 1).")
@click.option("--repair/--no-repair", "repair", default=True, show_default=True,
              help="Fehlenden Quelltext woertlich als Nachtrag anhaengen, statt ihn zu verlieren.")
@click.option("--models-dir", "models_dir", default=None, type=click.Path(file_okay=False),
              envvar="ACSOS_DOCLING_MODELS", show_envvar=True,
              help="Ordner mit vorab geladenen Docling-Modellen (fuer Umgebungen ohne "
                   "Zugriff auf huggingface.co). Einmalig erzeugen mit: "
                   "docling-tools models download -o <ordner>")
@click.option("--doctor", is_flag=True,
              help="Nur pruefen, ob Docling und die PDF-Modelle einsatzbereit sind.")
@click.option("--force", is_flag=True, help="Bereits konvertierte, unveraenderte Dokumente neu erzeugen.")
@click.option("--strict", is_flag=True, help="Exit-Code 1 auch bei Warnungen (fuer CI/Automation).")
def main(inputs, output_dir, ocr_mode, recursive, write_json, no_page_markers,
         do_verify, min_coverage, repair, models_dir, doctor, force, strict):
    """Konvertiert Dokumente mit IBM Docling nach strukturiertem Markdown."""
    try:
        import docling  # noqa: F401
    except ImportError:
        raise click.ClickException(
            "Docling ist nicht installiert. Ausfuehren: pip install -r requirements.txt"
        )

    mdir = Path(models_dir).expanduser() if models_dir else None

    if doctor:
        sys.exit(run_doctor(mdir))

    if not inputs:
        raise click.ClickException("Keine Eingabedatei angegeben (oder --doctor nutzen).")

    files = collect_inputs(tuple(inputs), recursive)
    if not files:
        raise click.ClickException("Keine unterstuetzten Dateien gefunden.")

    out_dir = Path(output_dir).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Ein Worker-Prozess fuer den ganzen Batch: die Modelle werden einmal
    # geladen, ein Absturz kostet nur das laufende Dokument.
    runner = _Runner()

    click.echo(f"Docling {docling_version()} — {len(files)} Datei(en) -> {out_dir}/")
    claimed: dict[str, Path] = {}
    results: list[Result] = []
    for i, src in enumerate(files, 1):
        click.echo(f"[{i}/{len(files)}] {src.name}")
        try:
            res = convert_file(
                runner, src, out_dir,
                ocr_mode=ocr_mode, write_json=write_json,
                page_markers=not no_page_markers, force=force, claimed=claimed,
                do_verify=do_verify, min_coverage=min_coverage, repair=repair,
                mdir_ref=(mdir,),
            )
        except ExtractionError as exc:
            res = Result(
                source=str(src), source_sha256=sha256_of(src),
                source_bytes=src.stat().st_size, status="error", error=str(exc),
            )
            click.secho(f"    FEHLER: {exc}", fg="red", err=True)
        except Exception as exc:  # unerwartet: Batch nicht abbrechen
            res = Result(
                source=str(src), source_sha256=sha256_of(src),
                source_bytes=src.stat().st_size, status="error",
                error=f"{type(exc).__name__}: {exc}",
            )
            click.secho(f"    FEHLER: {res.error}", fg="red", err=True)
        else:
            if res.status == "skipped":
                click.echo("    unveraendert — uebersprungen (--force erzwingt neu)")
            else:
                click.secho(
                    f"    -> {Path(res.output).name} "
                    f"({res.pages} S., {res.characters} Z., {res.tables} Tab., "
                    f"{res.headings} Ueberschriften"
                    + (f", Deckung {res.text_coverage} %" if res.text_coverage is not None else "")
                    + f", {res.duration_s}s)",
                    fg="green",
                )
            for w in res.warnings:
                click.secho(f"    WARNUNG: {w}", fg="yellow", err=True)
        results.append(res)

    runner.reset()
    manifest = write_manifest(out_dir, results)
    errors = [r for r in results if r.status == "error"]
    warns = [r for r in results if r.status == "warn"]
    click.echo(
        f"\nFertig: {len(results) - len(errors)} ok, {len(warns)} mit Warnung, "
        f"{len(errors)} Fehler. Manifest: {manifest}"
    )
    if errors or (strict and warns):
        sys.exit(1)


if __name__ == "__main__":
    main()
