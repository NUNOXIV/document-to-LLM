#!/usr/bin/env python3
"""ACSOS document-to-LLM — Extrakte in den Obsidian-Vault einspielen.

Schreibt aus einem von extract.py erzeugten Markdown je Anforderung eine
Normtext-Notiz nach `Normen (lizenziert)/<framework>/<framework> <ID> (Normtext).md`.
Genau diese Dateien erwarten die Embeds in den Framework-Notizen des Vaults.

Welche IDs gebraucht werden, sagt der Vault selbst: gelesen wird das Feld `id`
aus den vorhandenen Notizen unter `GRC/Frameworks/<framework>/`. Es wird nichts
erfunden — gefunden oder nicht gefunden, und beides steht im Bericht.

Der Zielordner ist im Vault bewusst von der Versionierung ausgenommen:
lizenzierter Normtext bleibt lokal.

    python publish.py output/iso-iec-27001-2022.md \\
        --vault ~/obsidian-vault --framework iso27001-2022
    python publish.py output/iso-iec-27001-2022.md --vault ~/obsidian-vault \\
        --framework iso27001-2022 --dry-run
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import click

LICENSED_DIR = "Normen (lizenziert)"


@dataclass
class Section:
    ident: str
    title: str
    text: str
    page: int


def split_front_matter(md: str) -> tuple[dict[str, str], str]:
    m = re.match(r"\A---\n(.*?)\n---\n", md, flags=re.S)
    if not m:
        return {}, md
    meta = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([a-z0-9_]+):\s*(.*)$", line)
        if km:
            meta[km.group(1)] = km.group(2).strip().strip('"')
    return meta, md[m.end():]


def page_at(body: str, pos: int) -> int:
    """Seitenzahl aus dem letzten Seitenmarker vor dieser Position."""
    markers = [(m.start(), int(m.group(1)))
               for m in re.finditer(r"<!--\s*page:\s*(\d+)\s*-->", body[:pos])]
    return markers[-1][1] if markers else 0


def sections_from_headings(body: str) -> dict[str, Section]:
    """Nummerierte Abschnitte (4.1, 6.1.2 ...) aus den Docling-Ueberschriften."""
    out: dict[str, Section] = {}
    heads = list(re.finditer(r"^(#{1,6})\s+([0-9]+(?:\.[0-9]+)*)\s+(.*\S)\s*$", body, flags=re.M))
    for i, m in enumerate(heads):
        start = m.end()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        text = body[start:end]
        text = re.sub(r"<!--\s*page:\s*\d+\s*-->", "", text).strip()
        ident = m.group(2)
        if ident in out:            # Wiederholte Kopfzeile o. ae.: laengeren Text behalten
            if len(text) <= len(out[ident].text):
                continue
        out[ident] = Section(ident, m.group(3), text, page_at(body, m.start()))

    # Oberklauseln ohne eigenen Text (z. B. 9.2, wenn alles in 9.2.1 und 9.2.2
    # steht) aus ihren Unterklauseln zusammensetzen, statt sie leer zu lassen.
    for ident, sec in list(out.items()):
        if sec.text.strip():
            continue
        kids = sorted((k for k in out if k.startswith(ident + ".") and out[k].text.strip()),
                      key=lambda k: [int(x) for x in k.split(".")])
        if not kids:
            continue
        parts = [f"### {k} {out[k].title}\n\n{out[k].text}".rstrip() for k in kids]
        out[ident] = Section(ident, sec.title, "\n\n".join(parts), sec.page or out[kids[0]].page)
    return out


def sections_from_tables(body: str) -> dict[str, Section]:
    """Control-Tabellen (Anhang A): jede Zeile ist eine Anforderung."""
    out: dict[str, Section] = {}
    for m in re.finditer(r"^\|\s*(A\.)?([0-9]+\.[0-9]+(?:\.[0-9]+)*)\s*\|(.+)$", body, flags=re.M):
        cells = [c.strip() for c in m.group(3).split("|") if c.strip()]
        if not cells:
            continue
        title = cells[0]
        text = "\n\n".join(cells[1:]) if len(cells) > 1 else ""
        ident = f"A.{m.group(2)}"
        prev = out.get(ident)
        if prev and len(prev.text) >= len(text):
            continue
        out[ident] = Section(ident, title, text, page_at(body, m.start()))
    return out


def inline_section(body: str, ident: str, title: str) -> Section | None:
    """Letzter Ausweg fuer Klauseln, die das Layoutmodell nicht als Ueberschrift
    erkannt hat: die Stelle ueber ID *und* erwarteten Titel ankern (der Titel
    kommt aus der Vault-Notiz, wird also nicht geraten) und bis zur naechsten
    Gliederungsnummer lesen."""
    if not title:
        return None
    anchor = re.search(rf"(?<![\d.]){re.escape(ident)}\s+{re.escape(title)}\b", body)
    if not anchor:
        return None
    rest = body[anchor.end():]
    nxt = re.search(r"(?m)^#{1,6}\s+[0-9]+(?:\.[0-9]+)*\s|(?<![\d.])[0-9]+\.[0-9]+\s+[A-Z]", rest)
    text = rest[: nxt.start()] if nxt else rest[:4000]
    text = re.sub(r"<!--\s*page:\s*\d+\s*-->", "", text).strip()
    return Section(ident, title, text, page_at(body, anchor.start())) if text else None


def vault_ids(vault: Path, framework: str) -> dict[str, str]:
    """IDs und Titel der Anforderungsnotizen des Frameworks aus dem Vault."""
    folder = vault / "GRC" / "Frameworks" / framework
    if not folder.is_dir():
        raise click.ClickException(
            f"Framework-Ordner nicht gefunden: {folder}\n"
            f"Vorhanden: {', '.join(sorted(p.name for p in (vault / 'GRC' / 'Frameworks').iterdir()))}"
            if (vault / "GRC" / "Frameworks").is_dir() else f"Kein GRC/Frameworks in {vault}"
        )
    ids: dict[str, str] = {}
    for note in sorted(folder.glob("*.md")):
        meta, body = split_front_matter(note.read_text(encoding="utf-8"))
        if meta.get("type") != "requirement" or not meta.get("id"):
            continue
        title = ""
        h = re.search(r"^#\s+\S+\s+—\s+(.*\S)\s*$", body, flags=re.M)
        if h:
            title = h.group(1)
        ids[meta["id"]] = title
    return ids


def note_text(framework: str, ident: str, sec: Section, meta: dict[str, str]) -> str:
    esc = lambda v: '"' + str(v).replace('"', '\\"') + '"'
    return "\n".join([
        "---",
        "type: normtext",
        f"framework: {framework}",
        f"id: {ident}",
        f"source_file: {esc(meta.get('source_file', ''))}",
        f"source_sha256: {meta.get('source_sha256', '')}",
        f"source_page: {sec.page}",
        f"text_coverage_percent: {meta.get('text_coverage_percent', '')}",
        f'tags: ["grc/normtext", "grc/framework/{framework}"]',
        "generated-by: document-to-LLM",
        "---",
        "",
        f"# {ident} — {sec.title}".rstrip(" —"),
        "",
        f"> [!quote] Normtext, Seite {sec.page} der Quelle" if sec.page else "> [!quote] Normtext",
        "",
        sec.text,
        "",
        # Beginnt der Text mitten im Satz, ist beim Tabellenmodell ein Zellrest
        # verrutscht. Das gehoert in die Notiz, nicht nur ins Extraktionsprotokoll.
        ("> [!warning] Moegliche Zellverschiebung\n"
         "> Dieser Text beginnt mitten im Satz. Beim Extrahieren der Tabelle kann ein\n"
         "> Rest der vorherigen Anforderung hierher gerutscht sein. Vor dem Zitieren\n"
         f"> gegen Seite {sec.page} der Quelle pruefen."
         if sec.text.strip()[:1].islower() else ""),
        "",
        "---",
        "",
        f"Woertlich aus {meta.get('source_file', 'der Quelle')} extrahiert "
        f"(IBM Docling, {meta.get('converter', 'docling')}). Lizenzierter Text — "
        f"bleibt lokal, nicht versionieren.",
        "",
    ])


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("extract_md", type=click.Path(exists=True, dir_okay=False))
@click.option("--vault", required=True, type=click.Path(file_okay=False, exists=True),
              help="Wurzel des Obsidian-Vaults (der Ordner mit GRC/ und .obsidian/).")
@click.option("--framework", required=True,
              help="Framework-Slug wie im Vault, z. B. iso27001-2022.")
@click.option("--dry-run", is_flag=True, help="Nur berichten, nichts schreiben.")
@click.option("--overwrite/--keep", default=True, show_default=True,
              help="Vorhandene Normtext-Notizen ersetzen oder stehen lassen.")
def main(extract_md: str, vault: str, framework: str, dry_run: bool, overwrite: bool) -> None:
    """Schreibt Normtext-Notizen aus einem Extrakt in den Vault."""
    vault_path = Path(vault).expanduser()
    md_path = Path(extract_md)
    meta, body = split_front_matter(md_path.read_text(encoding="utf-8"))

    wanted = vault_ids(vault_path, framework)
    if not wanted:
        raise click.ClickException(f"Keine Anforderungsnotizen fuer {framework} im Vault gefunden.")

    found = sections_from_headings(body)
    found.update(sections_from_tables(body))

    target_dir = vault_path / LICENSED_DIR / framework
    written, missing, skipped = [], [], []

    for ident in sorted(wanted):
        sec = found.get(ident) or found.get(ident.removeprefix("A."))
        if sec is None or not sec.text.strip():
            sec = inline_section(body, ident, wanted[ident])
        if sec is None or not sec.text.strip():
            missing.append(ident)
            continue
        if not sec.title and wanted[ident]:
            sec = Section(ident, wanted[ident], sec.text, sec.page)
        target = target_dir / f"{framework} {ident} (Normtext).md"
        if target.exists() and not overwrite:
            skipped.append(ident)
            continue
        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            target.write_text(note_text(framework, ident, sec, meta), encoding="utf-8")
        written.append(ident)

    click.secho(f"{len(written)} von {len(wanted)} Anforderungen belegt"
                + (" (Probelauf, nichts geschrieben)" if dry_run else f" -> {target_dir}"),
                fg="green" if not missing else "yellow")
    if skipped:
        click.echo(f"{len(skipped)} vorhandene Notizen unveraendert gelassen (--overwrite ersetzt sie).")
    if missing:
        click.secho(f"{len(missing)} ohne Normtext im Extrakt: "
                    + ", ".join(missing[:20]) + (" ..." if len(missing) > 20 else ""), fg="yellow")
        click.echo("Diese IDs stehen so nicht im Dokument — pruefen, ob der richtige "
                   "Normstand extrahiert wurde.")

    warn = (vault_path / ".gitignore")
    if warn.exists() and LICENSED_DIR not in warn.read_text(encoding="utf-8"):
        click.secho(f"ACHTUNG: '{LICENSED_DIR}/' steht nicht in der .gitignore des Vaults — "
                    f"lizenzierter Normtext koennte versioniert werden.", fg="red")


if __name__ == "__main__":
    main()
