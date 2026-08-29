#!/usr/bin/env python3
"""ACSOS document-to-LLM — Retrieval-Layer ueber den Extraktions-Output.

Warum: Eine komplette Norm als ein Markdown-Blob im Kontextfenster senkt die
Praezision. Dieses Skript zerlegt die konvertierten Dokumente strukturerhaltend
in Chunks (Docling HierarchicalChunker bzw. Ueberschriftenpfad) und legt sie in
eine SQLite-FTS5-Datenbank. Agenten holen sich damit genau den Absatz, den sie
brauchen — mit Dokument, Ueberschriftenpfad und Seitenzahl als Beleg.

Beispiele:
    python index.py build --output output --db output/acsos.db
    python index.py search "Kryptographie Schluesselverwaltung" --db output/acsos.db
    python index.py show iso-27001 --heading "A.8"
"""

from __future__ import annotations

import json
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path

import click

SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
    slug          TEXT PRIMARY KEY,
    title         TEXT NOT NULL,
    source_file   TEXT,
    source_sha256 TEXT,
    pages         INTEGER,
    md_path       TEXT NOT NULL,
    indexed_at    TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE VIRTUAL TABLE IF NOT EXISTS chunks USING fts5(
    slug UNINDEXED,
    headings,
    page UNINDEXED,
    text,
    tokenize = 'unicode61 remove_diacritics 2'
);
"""


@dataclass
class Chunk:
    slug: str
    headings: str
    page: int
    text: str


# --------------------------------------------------------------------------
# Chunking
# --------------------------------------------------------------------------
def chunks_from_docling_json(slug: str, json_path: Path, chunker: str) -> list[Chunk]:
    """Bevorzugter Weg: Chunking auf dem verlustfreien DoclingDocument."""
    from docling_core.types.doc.document import DoclingDocument

    doc = DoclingDocument.model_validate_json(json_path.read_text(encoding="utf-8"))

    if chunker == "hybrid":
        from docling.chunking import HybridChunker

        chunk_iter = HybridChunker().chunk(dl_doc=doc)
    else:
        from docling_core.transforms.chunker import HierarchicalChunker

        chunk_iter = HierarchicalChunker().chunk(dl_doc=doc)

    out: list[Chunk] = []
    for ch in chunk_iter:
        meta = getattr(ch, "meta", None)
        headings = " > ".join(getattr(meta, "headings", None) or []) if meta else ""
        page = 0
        try:
            for item in (getattr(meta, "doc_items", None) or []):
                for prov in (getattr(item, "prov", None) or []):
                    page = prov.page_no
                    break
                if page:
                    break
        except Exception:
            page = 0
        text = (ch.text or "").strip()
        if text:
            out.append(Chunk(slug, headings, page, text))
    return out


def chunks_from_markdown(slug: str, md_path: Path) -> list[Chunk]:
    """Fallback ohne --json-Export: Schnitt an den von Docling erzeugten
    Markdown-Ueberschriften und Seitenmarkern. Es wird nichts interpretiert,
    nur an bereits vorhandenen Strukturgrenzen getrennt."""
    text = md_path.read_text(encoding="utf-8")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)

    stack: dict[int, str] = {}
    page = 0
    buf: list[str] = []
    headings_now = ""
    out: list[Chunk] = []

    def flush() -> None:
        body = "\n".join(buf).strip()
        if body:
            out.append(Chunk(slug, headings_now, page, body))
        buf.clear()

    for line in text.splitlines():
        m_page = re.match(r"^<!--\s*page:\s*(\d+)\s*-->\s*$", line)
        if m_page:
            page = int(m_page.group(1))
            continue
        m_head = re.match(r"^(#{1,6})\s+(.*\S)\s*$", line)
        if m_head:
            flush()
            level = len(m_head.group(1))
            stack = {k: v for k, v in stack.items() if k < level}
            stack[level] = m_head.group(2)
            headings_now = " > ".join(stack[k] for k in sorted(stack))
            continue
        buf.append(line)
    flush()

    # Sehr kleine Fragmente an den Vorgaenger anhaengen.
    merged: list[Chunk] = []
    for c in out:
        if merged and len(c.text) < 200 and merged[-1].headings == c.headings:
            merged[-1].text += "\n" + c.text
        else:
            merged.append(c)
    return merged


def read_front_matter(md_path: Path) -> dict[str, str]:
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        return {}
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([a-z0-9_]+):\s*(.*)$", line)
        if km:
            meta[km.group(1)] = km.group(2).strip().strip('"')
    return meta


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    """Volltext-Index ueber die von extract.py erzeugten Markdown-Dateien."""


@cli.command()
@click.option("-o", "--output", "out_dir", default="output", show_default=True,
              type=click.Path(exists=True, file_okay=False))
@click.option("--db", "db_path", default=None,
              help="Pfad zur SQLite-Datei (Default: <output>/acsos.db).")
@click.option("--chunker", type=click.Choice(["hierarchical", "hybrid", "markdown"]),
              default="hierarchical", show_default=True,
              help="hierarchical/hybrid nutzen die .docling.json (extract.py --json); "
                   "markdown arbeitet auf den .md-Dateien.")
def build(out_dir: str, db_path: str | None, chunker: str) -> None:
    """Index aus dem Output-Ordner (neu) aufbauen."""
    out = Path(out_dir)
    db_file = Path(db_path) if db_path else out / "acsos.db"
    md_files = sorted(p for p in out.glob("*.md") if not p.name.startswith("_"))
    if not md_files:
        raise click.ClickException(f"Keine Markdown-Dateien in {out}/ — zuerst extract.py laufen lassen.")

    conn = sqlite3.connect(db_file)
    conn.executescript(SCHEMA)
    conn.execute("DELETE FROM chunks")
    conn.execute("DELETE FROM documents")

    total = 0
    for md in md_files:
        slug = md.stem
        meta = read_front_matter(md)
        jpath = md.with_suffix("").with_suffix(".docling.json")
        if not jpath.exists():
            jpath = md.parent / f"{slug}.docling.json"

        if chunker in ("hierarchical", "hybrid") and jpath.exists():
            try:
                chunks = chunks_from_docling_json(slug, jpath, chunker)
            except Exception as exc:
                click.secho(f"  {slug}: Docling-Chunker nicht nutzbar ({exc}) — Markdown-Fallback",
                            fg="yellow", err=True)
                chunks = chunks_from_markdown(slug, md)
        else:
            if chunker != "markdown":
                click.secho(f"  {slug}: keine .docling.json — Markdown-Fallback "
                            f"(extract.py --json erzeugt sie)", fg="yellow", err=True)
            chunks = chunks_from_markdown(slug, md)

        conn.execute(
            "INSERT OR REPLACE INTO documents(slug,title,source_file,source_sha256,pages,md_path)"
            " VALUES (?,?,?,?,?,?)",
            (slug, meta.get("source_file", slug), meta.get("source_file"),
             meta.get("source_sha256"), int(meta.get("pages") or 0), str(md)),
        )
        conn.executemany(
            "INSERT INTO chunks(slug,headings,page,text) VALUES (?,?,?,?)",
            [(c.slug, c.headings, c.page, c.text) for c in chunks],
        )
        total += len(chunks)
        click.echo(f"  {slug}: {len(chunks)} Chunks")

    conn.commit()
    conn.close()
    click.secho(f"Index geschrieben: {db_file} ({len(md_files)} Dokumente, {total} Chunks)", fg="green")


# Zeichen, die FTS5 als Syntax liest. In deutschem Normtext stehen sie mitten
# im Wort ("Mehrfaktor-Authentisierung", "OPS.1.1.3", "IT/OT"), wo sie als
# Operator gemeint sind — mit dem Ergebnis "no such column: Authentisierung".
FTS5_SYNTAX = re.compile(r'[-+*:^(){}\[\]]')


def fts5_query(roh: str) -> str:
    """Suchbegriff so aufbereiten, dass alltaegliche Schreibweisen funktionieren.

    Wer FTS5-Syntax will, nutzt Anfuehrungszeichen, NEAR oder OR und bekommt die
    Eingabe unveraendert. Alles andere wird in Phrasen zerlegt und gequotet:
    ein Bindestrich im Wort ist dann Text, kein Ausschlussoperator.
    """
    if '"' in roh or re.search(r"\b(AND|OR|NOT|NEAR)\b", roh):
        return roh                      # bewusste FTS5-Syntax nicht anfassen
    begriffe = [w for w in roh.split() if w]
    if not any(FTS5_SYNTAX.search(w) for w in begriffe):
        return roh                      # nichts zu entschaerfen
    return " ".join('"' + w.replace('"', '') + '"' for w in begriffe)


@cli.command()
@click.argument("query")
@click.option("--db", "db_path", default="output/acsos.db", show_default=True)
@click.option("-n", "--limit", default=5, show_default=True)
@click.option("--doc", "slug", default=None, help="Auf ein Dokument (Slug) einschraenken.")
@click.option("--json", "as_json", is_flag=True, help="Ergebnis als JSON ausgeben.")
def search(query: str, db_path: str, limit: int, slug: str | None, as_json: bool) -> None:
    """Volltextsuche; gibt Treffer mit Dokument, Gliederung und Seite aus."""
    db_file = Path(db_path)
    if not db_file.exists():
        raise click.ClickException(f"Index fehlt: {db_file} — zuerst 'index.py build' ausfuehren.")
    conn = sqlite3.connect(db_file)
    sql = ("SELECT slug, headings, page, snippet(chunks,3,'**','**','…',40), text "
           "FROM chunks WHERE chunks MATCH ?")
    params: list = [fts5_query(query)]
    if slug:
        sql += " AND slug = ?"
        params.append(slug)
    sql += " ORDER BY rank LIMIT ?"
    params.append(limit)
    try:
        rows = conn.execute(sql, params).fetchall()
    except sqlite3.OperationalError as exc:
        raise click.ClickException(
            f"Ungueltige FTS5-Query: {exc}\n"
            "Fuer eine woertliche Suche den Begriff in Anfuehrungszeichen setzen.")
    conn.close()

    if as_json:
        click.echo(json.dumps(
            [{"doc": r[0], "headings": r[1], "page": r[2], "snippet": r[3], "text": r[4]} for r in rows],
            ensure_ascii=False, indent=2))
        return
    if not rows:
        click.echo("Keine Treffer.")
        return
    for doc, headings, page, snip, _ in rows:
        loc = f"{doc}" + (f" | {headings}" if headings else "") + (f" | S. {page}" if page else "")
        click.secho(loc, fg="cyan")
        click.echo(f"  {snip}\n")


@cli.command()
@click.argument("slug")
@click.option("--db", "db_path", default="output/acsos.db", show_default=True)
@click.option("--heading", default=None, help="Nur Abschnitte, deren Gliederungspfad diesen Text enthaelt.")
def show(slug: str, db_path: str, heading: str | None) -> None:
    """Abschnitte eines Dokuments vollstaendig ausgeben (fuer Zitate)."""
    db_file = Path(db_path)
    if not db_file.exists():
        raise click.ClickException(f"Index fehlt: {db_file} — zuerst 'index.py build' ausfuehren.")
    conn = sqlite3.connect(db_file)
    if heading:
        rows = conn.execute(
            "SELECT headings, page, text FROM chunks WHERE slug = ? AND headings LIKE ?",
            (slug, f"%{heading}%"),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT headings, page, text FROM chunks WHERE slug = ?", (slug,)
        ).fetchall()
    conn.close()
    if not rows:
        click.echo("Keine Abschnitte gefunden.")
        sys.exit(1)
    for headings, page, text in rows:
        click.secho(f"## {headings or slug}" + (f"  (S. {page})" if page else ""), fg="cyan")
        click.echo(text + "\n")


@cli.command(name="list")
@click.option("--db", "db_path", default="output/acsos.db", show_default=True)
def list_docs(db_path: str) -> None:
    """Indizierte Dokumente auflisten."""
    db_file = Path(db_path)
    if not db_file.exists():
        raise click.ClickException(f"Index fehlt: {db_file} — zuerst 'index.py build' ausfuehren.")
    conn = sqlite3.connect(db_file)
    rows = conn.execute(
        "SELECT d.slug, d.title, d.pages, (SELECT COUNT(*) FROM chunks c WHERE c.slug = d.slug)"
        " FROM documents d ORDER BY d.slug"
    ).fetchall()
    conn.close()
    for slug, title, pages, n in rows:
        click.echo(f"{slug:40s} {pages or '?':>4} S.  {n:>5} Chunks  {title}")


if __name__ == "__main__":
    cli()
