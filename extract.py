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
def build_converter(ocr: bool):
    """DocumentConverter mit Compliance-tauglichen Defaults.

    - TableFormer im ACCURATE-Modus: verschachtelte Control-Tabellen bleiben
      als Markdown-Tabellen erhalten statt zu Fliesstext zu zerfallen.
    - Cell-Matching an: Zellinhalte werden aus dem PDF-Textlayer uebernommen,
      nicht aus dem Modell rekonstruiert (keine erfundenen Zellwerte).
    """
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions

    opts = PdfPipelineOptions()
    opts.do_ocr = ocr
    opts.do_table_structure = True
    opts.table_structure_options.do_cell_matching = True
    try:
        from docling.datamodel.pipeline_options import TableFormerMode

        opts.table_structure_options.mode = TableFormerMode.ACCURATE
    except Exception:
        pass  # aeltere Docling-Version: Default-Modus ist ausreichend

    return DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )


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

    if "�" in body:
        warnings.append("Ersatzzeichen (U+FFFD) im Text — Encoding-/Font-Problem.")

    return warnings


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
        f"converted_at: {esc(datetime.now(timezone.utc).isoformat(timespec='seconds'))}",
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
    converter_for,
    src: Path,
    out_dir: Path,
    *,
    ocr_mode: str,
    write_json: bool,
    page_markers: bool,
    force: bool,
    claimed: dict[str, Path],
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
    doc = None

    for attempt in ("first", "ocr-retry"):
        conv = converter_for(ocr)
        try:
            doc = conv.convert(src).document
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

        res.pages = page_count(doc)
        md_body = to_markdown(doc, page_markers)
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
    res.tables = count_tables(doc, md_body)
    res.headings = len(re.findall(r"^#{1,6}\s+\S", md_body, flags=re.M))
    res.warnings = check_quality(md_body, res.pages, is_pdf, ocr)
    res.status = "warn" if res.warnings else "ok"

    out_dir.mkdir(parents=True, exist_ok=True)
    target.write_text(front_matter(src, res, ocr_mode) + md_body.rstrip() + "\n", encoding="utf-8")
    res.output = str(target)

    if write_json:
        jtarget = out_dir / f"{stem}.docling.json"
        jtarget.write_text(
            json.dumps(doc.export_to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
        )
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


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("inputs", nargs=-1, required=True, type=click.Path())
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
@click.option("--force", is_flag=True, help="Bereits konvertierte, unveraenderte Dokumente neu erzeugen.")
@click.option("--strict", is_flag=True, help="Exit-Code 1 auch bei Warnungen (fuer CI/Automation).")
def main(inputs, output_dir, ocr_mode, recursive, write_json, no_page_markers, force, strict):
    """Konvertiert Dokumente mit IBM Docling nach strukturiertem Markdown."""
    try:
        import docling  # noqa: F401
    except ImportError:
        raise click.ClickException(
            "Docling ist nicht installiert. Ausfuehren: pip install -r requirements.txt"
        )

    files = collect_inputs(tuple(inputs), recursive)
    if not files:
        raise click.ClickException("Keine unterstuetzten Dateien gefunden.")

    out_dir = Path(output_dir).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Converter werden pro OCR-Modus einmal gebaut und wiederverwendet
    # (Modell-Laden ist teuer).
    cache: dict[bool, object] = {}

    def converter_for(ocr: bool):
        if ocr not in cache:
            cache[ocr] = build_converter(ocr)
        return cache[ocr]

    click.echo(f"Docling {docling_version()} — {len(files)} Datei(en) -> {out_dir}/")
    claimed: dict[str, Path] = {}
    results: list[Result] = []
    for i, src in enumerate(files, 1):
        click.echo(f"[{i}/{len(files)}] {src.name}")
        try:
            res = convert_file(
                converter_for, src, out_dir,
                ocr_mode=ocr_mode, write_json=write_json,
                page_markers=not no_page_markers, force=force, claimed=claimed,
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
                    f"{res.headings} Ueberschriften, {res.duration_s}s)",
                    fg="green",
                )
            for w in res.warnings:
                click.secho(f"    WARNUNG: {w}", fg="yellow", err=True)
        results.append(res)

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
