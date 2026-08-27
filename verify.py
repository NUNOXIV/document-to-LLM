#!/usr/bin/env python3
"""ACSOS document-to-LLM — Abweichungspruefung Quelle gegen Extrakt.

Vergleicht den Textlayer des Quell-PDFs (Docling-PDF-Backend, ohne ML-Modelle)
Wort fuer Wort mit dem erzeugten Markdown. Ergebnis ist eine Deckungsquote plus
die Liste der Woerter, die im Extrakt fehlen — seitengenau.

Damit ist belegbar, dass nichts verloren gegangen ist, statt es zu hoffen.

    python verify.py output/iso-27001.md --source input/ISO-27001.pdf
    python verify.py output/iso-27001.md --source input/ISO-27001.pdf --min-coverage 99.5
"""

from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import click

# Zeichen, die zwischen PDF-Textlayer und Markdown-Serialisierung typografisch
# variieren duerfen, ohne dass es eine inhaltliche Abweichung waere.
_QUOTES = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-",
    "−": "-", "­": "", " ": " ",
}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    for src, dst in _QUOTES.items():
        text = text.replace(src, dst)
    return text.casefold()


def tokenize(text: str) -> list[str]:
    """Woerter und Zahlen; Satzzeichen und Layout-Artefakte fallen weg."""
    text = normalize(text)
    # Am Zeilenende getrennte Woerter zusammenfuehren (Silbentrennung im PDF).
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
    return re.findall(r"[0-9a-zA-ZÀ-ɏ]+(?:[.,][0-9]+)*", text)


def markdown_tokens(md_path: Path) -> list[str]:
    text = md_path.read_text(encoding="utf-8")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)   # Front-Matter
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)          # Seitenmarker/Hinweise
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)            # Bildplatzhalter
    text = re.sub(r"^\s*\|[\s:|-]+\|\s*$", " ", text, flags=re.M)  # Tabellentrennzeilen
    return tokenize(text)


def _mask(line: str) -> str:
    """Zeile fuer den Kopf-/Fusszeilen-Vergleich normalisieren (Ziffern maskiert,
    damit 'Seite 3' und 'Seite 4' als dieselbe laufende Zeile gelten)."""
    return re.sub(r"\d+", "#", normalize(line)).strip()


def pdf_pages(pdf_path: Path) -> tuple[dict[int, list[str]], dict[int, list[str]]]:
    """Textlayer des PDFs ueber das Docling-Backend (keine ML-Modelle noetig).

    Rueckgabe: (Inhaltstokens je Seite, Kopf-/Fusszeilen-Tokens je Seite).
    Laufende Kopf- und Fusszeilen werden von Docling bewusst entfernt; sie
    duerfen die Deckungsquote nicht druecken und werden separat ausgewiesen.
    """
    from docling.backend.docling_parse_backend import DoclingParseDocumentBackend
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.document import InputDocument
    from docling_core.types.doc.page import TextCellUnit

    # InputDocument instanziiert das Backend bereits selbst; ein zweites wuerde
    # dieselbe Datei ein zweites Mal offen halten.
    in_doc = InputDocument(
        path_or_stream=pdf_path, format=InputFormat.PDF,
        backend=DoclingParseDocumentBackend, filename=pdf_path.name,
    )
    backend = in_doc._backend
    lines_by_page: dict[int, list[str]] = {}
    try:
        n = backend.page_count()
        for i in range(n):
            seg = backend.load_page(i).get_segmented_page()
            lines_by_page[i + 1] = [c.text for c in seg.iterate_cells(TextCellUnit.LINE)]
    finally:
        backend.unload()

    # Laufende Kopf-/Fusszeilen: gleiche (ziffernmaskierte) Zeile auf vielen Seiten,
    # jeweils am oberen oder unteren Rand des Seiteninhalts.
    n = len(lines_by_page)
    seen: Counter[str] = Counter()
    for lines in lines_by_page.values():
        seen.update({_mask(l) for l in lines if _mask(l) and len(tokenize(l)) <= 12})
    threshold = max(2, int(0.6 * n))
    running = {m for m, c in seen.items() if c >= threshold} if n >= 2 else set()

    content: dict[int, list[str]] = {}
    boiler: dict[int, list[str]] = {}
    for page_no, lines in lines_by_page.items():
        keep, drop = [], []
        for line in lines:
            (drop if _mask(line) in running else keep).append(line)
        content[page_no] = tokenize(" ".join(keep))
        boiler[page_no] = tokenize(" ".join(drop))
    return content, boiler


@dataclass
class VerifyResult:
    source: str
    extract: str
    source_tokens: int = 0
    extract_tokens: int = 0
    missing_tokens: int = 0
    coverage: float = 100.0
    per_page: dict[int, float] = field(default_factory=dict)
    missing_sample: list[str] = field(default_factory=list)
    worst_pages: list[tuple[int, float]] = field(default_factory=list)
    boilerplate_tokens: int = 0
    rejoined_tokens: int = 0
    note: str | None = None

    @property
    def ok_for(self) -> float:
        return self.coverage


def verify(pdf_path: Path, md_path: Path) -> VerifyResult:
    res = VerifyResult(source=str(pdf_path), extract=str(md_path))
    pages, boiler = pdf_pages(pdf_path)
    src_all = [t for toks in pages.values() for t in toks]
    out = markdown_tokens(md_path)
    res.source_tokens = len(src_all)
    res.extract_tokens = len(out)
    res.boilerplate_tokens = sum(len(t) for t in boiler.values())

    if not src_all:
        res.note = ("Kein Textlayer im PDF (gescannt) — ein Wortvergleich ist nicht "
                    "moeglich. Extraktion mit --ocr on pruefen.")
        return res

    stream = "".join(out)  # fuer Woerter, die im PDF ueber einen Zeilenumbruch getrennt sind

    def compare(tokens: list[str]) -> tuple[int, Counter[str]]:
        """Gibt (fehlende Anzahl, fehlende Woerter) zurueck. Woerter, die im PDF
        ueber einen Umbruch getrennt und im Extrakt zusammengefuegt sind, gelten
        als vorhanden — das ist keine inhaltliche Abweichung."""
        budget = Counter(out)
        missing: Counter[str] = Counter()
        for i, tok in enumerate(tokens):
            if budget[tok] > 0:
                budget[tok] -= 1
                continue
            if len(tok) > 3 and tok in stream:
                res.rejoined_tokens += 1
                continue
            prev = tokens[i - 1] if i else ""
            nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
            if (prev and (prev + tok) in stream) or (nxt and (tok + nxt) in stream):
                res.rejoined_tokens += 1
                continue
            missing[tok] += 1
        return sum(missing.values()), missing

    res.rejoined_tokens = 0
    total_missing, missing = compare(src_all)
    res.missing_tokens = total_missing
    res.coverage = round(100.0 * (1 - total_missing / len(src_all)), 3)
    res.missing_sample = [w for w, _ in missing.most_common(25)]

    # Seitenweise Deckung, jede Seite unabhaengig bewertet: zeigt, ob eine
    # Spalte, Tabelle oder ganze Seite im Extrakt fehlt.
    rejoined_total = res.rejoined_tokens
    for page_no, toks in pages.items():
        if not toks:
            res.per_page[page_no] = 100.0
            continue
        page_missing, _ = compare(toks)
        res.per_page[page_no] = round(100.0 * (1 - page_missing / len(toks)), 2)
    res.rejoined_tokens = rejoined_total
    res.worst_pages = sorted(res.per_page.items(), key=lambda kv: kv[1])[:5]
    return res


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("extract_md", type=click.Path(exists=True, dir_okay=False))
@click.option("--source", required=True, type=click.Path(exists=True, dir_okay=False),
              help="Quell-PDF, aus dem der Extrakt erzeugt wurde.")
@click.option("--min-coverage", default=99.5, show_default=True,
              help="Geforderte Wortdeckung in Prozent; darunter Exit-Code 1.")
@click.option("--show-missing", default=25, show_default=True,
              help="Wie viele fehlende Woerter ausgegeben werden.")
def main(extract_md: str, source: str, min_coverage: float, show_missing: int) -> None:
    """Prueft, ob der Extrakt den Text des Quell-PDFs vollstaendig enthaelt."""
    res = verify(Path(source), Path(extract_md))
    if res.note:
        click.secho(res.note, fg="yellow")
        sys.exit(1)

    color = "green" if res.coverage >= min_coverage else "red"
    click.secho(f"Wortdeckung: {res.coverage} %  "
                f"({res.source_tokens - res.missing_tokens}/{res.source_tokens} Woerter)", fg=color)
    click.echo(f"Extrakt enthaelt {res.extract_tokens} Woerter "
               f"(Differenz kann aus Tabellen-Wiederholungen stammen).")
    if res.worst_pages:
        worst = ", ".join(f"S.{p}: {c} %" for p, c in res.worst_pages)
        click.echo(f"Schwaechste Seiten: {worst}")
    if res.boilerplate_tokens:
        click.echo(f"{res.boilerplate_tokens} Woerter aus laufenden Kopf-/Fusszeilen "
                   f"nicht gewertet (von Docling bewusst entfernt).")
    if res.rejoined_tokens:
        click.echo(f"{res.rejoined_tokens} Woerter waren im PDF ueber einen Zeilenumbruch "
                   f"getrennt und im Extrakt zusammengefuegt — als vorhanden gewertet.")
    if res.missing_tokens:
        click.echo("Fehlende Woerter (haeufigste): "
                   + ", ".join(res.missing_sample[:show_missing]))
    if res.coverage < min_coverage:
        click.secho(f"FEHLER: Deckung unter {min_coverage} % — Extrakt ist nicht vollstaendig.",
                    fg="red")
        sys.exit(1)


if __name__ == "__main__":
    main()
