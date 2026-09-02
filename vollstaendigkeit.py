#!/usr/bin/env python3
"""Prueft, ob JEDE Quelldatei einen Extrakt hat.

Die Luecke, die dieser Waechter schliesst
-----------------------------------------
Alle bisherigen Pruefungen sehen sich an, was da ist: Wortdeckung, Zellversatz,
Kennungen, Fundstellen. Keine einzige fragt, was FEHLT. Ein Dokument, das nie
eingespeist wurde, faellt deshalb durch jedes Netz -- es hat keinen Extrakt,
der auffallen koennte, und keinen Eintrag, der widerspraeche.

Gefunden wurde das nicht durch das Werkzeug, sondern weil der Bestand in einer
Uebersicht ausserhalb dieses Systems landete und dort sichtbar zu duenn war:
134 Dokumente fehlten, 468 statt 602. Vier PDFs lagen unkonvertiert in input/,
130 weitere steckten in zwei ZIP-Archiven, die nie ausgepackt wurden.

Deshalb prueft dieser Waechter gegen die QUELLE, nicht gegen den Bestand:
er laeuft ueber input/, schaut in Archive hinein und verlangt fuer jede
Datei einen Eintrag im Register.

Nutzung
-------
    python vollstaendigkeit.py                    # zaehlen und auflisten
    python vollstaendigkeit.py --strict           # Exit 1, wenn etwas fehlt
    python vollstaendigkeit.py --auspacken        # Archive nach input/ entpacken
"""
from __future__ import annotations

import json
import sys
import zipfile
from collections import Counter
from pathlib import Path

import click

# Formate, fuer die es einen Weg in den Bestand gibt. Alles andere wird
# ausgewiesen statt stillschweigend ignoriert -- eine Datei, die niemand
# verarbeiten kann, ist ein Befund und keine Randnotiz.
VERARBEITBAR = {".pdf", ".xlsx", ".xlsm", ".docx", ".pptx",
                ".yml", ".yaml", ".json", ".xml", ".md", ".txt", ".mm"}
ARCHIVE = {".zip"}


def register(korpus: Path) -> set[str]:
    if not korpus.exists():
        raise SystemExit(f"Bestandsregister fehlt: {korpus} — erst 'python index.py build'")
    return {d.get("source_file", "") for d in json.loads(korpus.read_text(encoding="utf-8"))["documents"]}


def archivinhalt(pfad: Path) -> list[str]:
    """Dateinamen im Archiv. Ordner und Metadateien zaehlen nicht."""
    try:
        with zipfile.ZipFile(pfad) as z:
            return [Path(n).name for n in z.namelist()
                    if not n.endswith("/") and not Path(n).name.startswith((".", "__"))]
    except zipfile.BadZipFile:
        return []


@click.command()
@click.option("--input", "eingang", type=click.Path(exists=True, path_type=Path),
              default=Path("input"), show_default=True)
@click.option("--korpus", type=click.Path(path_type=Path),
              default=Path("output/_KORPUS.json"), show_default=True)
@click.option("--auspacken", is_flag=True,
              help="Archive neben sich entpacken, damit ihr Inhalt eingelesen werden kann. "
                   "Schreibt nach input/ — ohne diesen Schalter wird nur gezaehlt.")
@click.option("--strict", is_flag=True, help="Exit 1, sobald eine Quelle ohne Extrakt bleibt.")
def main(eingang: Path, korpus: Path, auspacken: bool, strict: bool) -> None:
    """Vergleicht die Quellen mit dem Bestand und benennt jede Luecke."""
    erfasst = register(korpus)
    ohne_extrakt: list[tuple[str, Path]] = []
    unbekannt: list[Path] = []
    archive: list[tuple[Path, list[str]]] = []
    geprueft = 0

    for p in sorted(eingang.rglob("*")):
        if not p.is_file() or p.name == ".gitkeep":
            continue
        endung = p.suffix.lower()
        if endung in ARCHIVE:
            fehlend = [n for n in archivinhalt(p) if n not in erfasst]
            archive.append((p, fehlend))
            continue
        if endung not in VERARBEITBAR:
            unbekannt.append(p)
            continue
        geprueft += 1
        if p.name not in erfasst:
            ohne_extrakt.append((p.name, p))

    aus_archiven = sum(len(f) for _, f in archive)
    print(f"{geprueft} Quelldatei(en) geprueft, {len(erfasst)} im Bestand.\n")

    if ohne_extrakt:
        nach_typ = Counter(Path(n).suffix.lower() for n, _ in ohne_extrakt)
        print(f"{len(ohne_extrakt)} Quelle(n) ohne Extrakt {dict(nach_typ)}:")
        for name, p in ohne_extrakt[:40]:
            print(f"  {p.stat().st_size/1e6:8.2f} MB  {p}")
        if len(ohne_extrakt) > 40:
            print(f"  ... und {len(ohne_extrakt)-40} weitere")
        print()

    for p, fehlend in archive:
        if fehlend:
            print(f"Archiv nicht ausgepackt: {p} — {len(fehlend)} Datei(en) fehlen im Bestand")
            for n in fehlend[:3]:
                print(f"     {n}")
            if auspacken:
                ziel = p.with_suffix("")
                ziel.mkdir(exist_ok=True)
                with zipfile.ZipFile(p) as z:
                    z.extractall(ziel)
                print(f"     -> ausgepackt nach {ziel}/ — jetzt 'python extract.py {ziel} --recursive'")
    if archive:
        print()

    if unbekannt:
        print(f"{len(unbekannt)} Datei(en) in einem Format ohne Weg in den Bestand:")
        for p in unbekannt[:10]:
            print(f"  {p}")
        print()

    offen = len(ohne_extrakt) + aus_archiven
    if offen:
        print(f"BEFUND: {offen} Dokument(e) sind nicht im Bestand. "
              f"Vollstaendig waeren {len(erfasst) + offen}.")
    else:
        print("Jede Quelldatei hat einen Extrakt.")
    if strict and offen:
        sys.exit(1)


if __name__ == "__main__":
    main()
