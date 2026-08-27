#!/usr/bin/env python3
"""ACSOS document-to-LLM — Aufnahmeprotokoll aller Extrakte.

Liest die erzeugten Markdown-Dateien und schreibt eine Uebersicht: je Dokument
Wortdeckung, Seiten, Tabellen, Ueberschriften, entfernte Kopf-/Fusszeilen und
offene Warnungen. Bei jedem Lauf neu erzeugt, damit die Datei nie veraltet.

    python tracker.py --output output --to output/_TRACKER.md
    python tracker.py --output output --to ~/obsidian-vault/"document-to-LLM Tracker.md"
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import click


@dataclass
class Doc:
    slug: str
    source: str = ""
    pages: int = 0
    tables: int = 0
    headings: int = 0
    words: int = 0
    coverage: float | None = None
    boilerplate: int = 0
    appended: int = 0
    table_mode: str = ""
    status: str = "ok"
    ocr: bool = False
    converter: str = ""
    converted_at: str = ""
    sha256: str = ""
    warnings: list[str] = field(default_factory=list)
    framework: str = ""
    vault_notes: int = 0

    @property
    def verdict(self) -> str:
        if self.coverage is None:
            return "kein Textlayer"
        if self.coverage >= 100.0:
            return "vollstaendig"
        if self.coverage >= 99.5:
            return "Rest fehlt"
        return "unvollstaendig"


def read_doc(md: Path) -> Doc:
    text = md.read_text(encoding="utf-8")
    doc = Doc(slug=md.stem)
    m = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
    body = text[m.end():] if m else text
    if m:
        block = m.group(1)
        def val(key: str) -> str:
            km = re.search(rf"^{key}:\s*(.*)$", block, flags=re.M)
            return km.group(1).strip().strip('"') if km else ""
        doc.source = val("source_file")
        doc.sha256 = val("source_sha256")
        doc.pages = int(val("pages") or 0)
        doc.tables = int(val("tables") or 0)
        doc.converter = val("converter")
        doc.converted_at = val("converted_at")
        doc.table_mode = val("table_mode")
        doc.status = val("extraction_status") or "ok"
        doc.ocr = val("ocr").split("#")[0].strip() == "true"
        cov = val("text_coverage_percent")
        doc.coverage = float(cov) if cov else None
        doc.appended = int(val("appended_source_lines") or 0)
        doc.warnings = [w.strip().strip('"').replace('\\"', '"').replace("\\\\", "\\")
                        for w in re.findall(r"^\s+-\s+(.*)$", block, flags=re.M)]
    doc.headings = len(re.findall(r"^#{1,6}\s+\S", body, flags=re.M))
    doc.words = len(re.findall(r"[0-9A-Za-zÀ-ɏ]+", re.sub(r"<!--.*?-->", " ", body, flags=re.S)))
    return doc


def enrich_from_verify(doc: Doc, src_dir: Path) -> None:
    """Kopf-/Fusszeilenzahl aus der Quelle nachziehen, wenn die Quelle noch da ist."""
    if not doc.source:
        return
    src = src_dir / doc.source
    if not src.exists() or src.suffix.lower() != ".pdf":
        return
    try:
        from verify import pdf_pages

        _, boiler = pdf_pages(src)
        doc.boilerplate = sum(len(t) for t in boiler.values())
    except Exception:
        pass


def vault_counts(vault: Path | None) -> dict[str, int]:
    if not vault:
        return {}
    base = vault / "Normen (lizenziert)"
    if not base.is_dir():
        return {}
    return {p.name: len(list(p.glob("*.md"))) for p in base.iterdir() if p.is_dir()}


def block_for(doc: Doc) -> str:
    """Der Meldeblock je Dokument."""
    cov = f"{doc.coverage} %" if doc.coverage is not None else "nicht pruefbar"
    lines = [
        f"Wortdeckung:  {cov}" + (f"  ({doc.words} Woerter im Extrakt)" if doc.words else ""),
        f"Seiten:       {doc.pages or '—'}",
        f"Struktur:     {doc.tables} Tabellen, {doc.headings} Ueberschriften",
    ]
    if doc.boilerplate:
        lines.append(f"Entfernt:     {doc.boilerplate} Woerter Kopf-/Fusszeilen")
    if doc.appended:
        lines.append(f"Nachgetragen: {doc.appended} Quellzeile(n) ohne Zuordnung")
    if doc.ocr:
        lines.append("OCR:          aktiv")
    if doc.table_mode and doc.table_mode != "accurate":
        lines.append(f"Tabellen:     Modell {doc.table_mode} (ACCURATE brach ab)")
    return "\n".join(lines)


def render(docs: list[Doc], vault: Path | None) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    complete = [d for d in docs if d.coverage is not None and d.coverage >= 100.0]
    partial = [d for d in docs if d.coverage is not None and d.coverage < 100.0]
    unchecked = [d for d in docs if d.coverage is None]

    out = [
        "---",
        "type: tracker",
        'tags: ["grc/tracker", "grc/normtext"]',
        "generated-by: document-to-LLM",
        f"generated_at: {now}",
        f"documents: {len(docs)}",
        "---",
        "",
        "# Aufnahmeprotokoll der Normextraktion",
        "",
        f"Stand {now}. Erzeugt von `tracker.py`; jeder Lauf schreibt die Datei neu.",
        "",
        "## Bilanz",
        "",
        f"- **{len(complete)} von {len(docs)}** Dokumenten mit 100,0 % Wortdeckung",
        f"- {len(partial)} mit fehlendem Text" if partial else "- kein Dokument mit fehlendem Text",
        f"- {len(unchecked)} ohne pruefbaren Textlayer (Office-Format oder Scan)"
        if unchecked else "- alle Quellen hatten einen pruefbaren Textlayer",
        "",
        "## Uebersicht",
        "",
        "| Dokument | Seiten | Tabellen | Deckung | Befund | Warnungen |",
        "| --- | ---: | ---: | ---: | --- | ---: |",
    ]
    for d in sorted(docs, key=lambda x: x.slug):
        cov = f"{d.coverage} %" if d.coverage is not None else "—"
        out.append(f"| {d.slug} | {d.pages or '—'} | {d.tables} | {cov} | {d.verdict} "
                   f"| {len(d.warnings)} |")

    if vault:
        counts = vault_counts(vault)
        if counts:
            out += ["", "## Im Vault abgelegt", "",
                    "| Framework | Normtext-Notizen |", "| --- | ---: |"]
            for fw, n in sorted(counts.items()):
                out.append(f"| {fw} | {n} |")

    out += ["", "## Je Dokument", ""]
    for d in sorted(docs, key=lambda x: x.slug):
        out += [f"### {d.slug}", ""]
        if d.source:
            out.append(f"Quelle: `{d.source}`" + (f" · SHA-256 `{d.sha256[:16]}…`" if d.sha256 else ""))
            out.append("")
        out += ["```", block_for(d), "```", ""]
        if d.warnings:
            out.append("Offene Hinweise:")
            out += [f"- {w}" for w in d.warnings]
            out.append("")
    return "\n".join(out).rstrip() + "\n"


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("-o", "--output", "out_dir", default="output", show_default=True,
              type=click.Path(exists=True, file_okay=False),
              help="Ordner mit den Extrakten.")
@click.option("--input", "src_dir", default="input", show_default=True,
              type=click.Path(file_okay=False),
              help="Ordner mit den Quelldateien (fuer die Kopf-/Fusszeilenzahl).")
@click.option("--to", "targets", multiple=True,
              help="Zieldatei; mehrfach angebbar (z. B. Repo und Vault).")
@click.option("--vault", default=None, type=click.Path(file_okay=False),
              help="Vault-Wurzel, um die abgelegten Normtext-Notizen mitzuzaehlen.")
def main(out_dir: str, src_dir: str, targets: tuple[str, ...], vault: str | None) -> None:
    """Schreibt das Aufnahmeprotokoll aller Extrakte."""
    out = Path(out_dir)
    docs = []
    for md in sorted(out.glob("*.md")):
        if md.name.startswith("_"):
            continue
        doc = read_doc(md)
        enrich_from_verify(doc, Path(src_dir))
        docs.append(doc)
    if not docs:
        raise click.ClickException(f"Keine Extrakte in {out}/ gefunden.")

    text = render(docs, Path(vault).expanduser() if vault else None)
    written = []
    for t in (targets or (str(out / "_TRACKER.md"),)):
        target = Path(t).expanduser()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        written.append(str(target))
    ok = sum(1 for d in docs if d.coverage is not None and d.coverage >= 100.0)
    click.secho(f"{len(docs)} Dokumente, {ok} mit 100,0 % Deckung -> " + ", ".join(written),
                fg="green")


if __name__ == "__main__":
    main()
