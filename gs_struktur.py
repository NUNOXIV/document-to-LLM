#!/usr/bin/env python3
"""ACSOS document-to-LLM — Strukturuebersicht des IT-Grundschutz-Kompendiums.

Das BSI veroeffentlicht die Baustein-Struktur in zwei Dateien, die einander
brauchen:

  * GS_Struktur_Edition-2023.mm  — FreeMind-Mindmap mit der vollstaendigen
    Hierarchie und je Baustein einem Symbol full-1/2/3 fuer die empfohlene
    Umsetzungsreihenfolge.
  * GS_Struktur_Edition-2023.pdf — das Plakat. Es traegt die Legende, die
    erklaert, was full-1/2/3 bedeuten, dazu die Farblegende und den Stand.

Getrennt ist keine der beiden brauchbar: die Mindmap hat Symbole ohne
Erklaerung, das Plakat hat die Erklaerung ohne maschinenlesbare Struktur.
Dieses Skript fuegt beide zu einer navigierbaren Gliederung zusammen.

Das Ergebnis ist ABGELEITET, nicht extrahiert: es ordnet um und loest Symbole
in Klartext auf. Beide Quellen bleiben unveraendert im Bestand; die Notiz nennt
sie und sagt selbst, dass sie abgeleitet ist.

    python gs_struktur.py --output output --to output/_GS-STRUKTUR.md
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

import click

MINDMAP = "gs-struktur-edition-2023"
PLAKAT = "gs-struktur-edition-2023-pdf-clean"

# Die Symbole der Mindmap. Der Klartext stammt aus der Legende des Plakats und
# wird dort zur Laufzeit gelesen, nicht hier fest verdrahtet.
SYMBOL_RANG = {"full-1": 1, "full-2": 2, "full-3": 3}


def fenced_xml(md: Path) -> str:
    """Der woertlich uebernommene XML-Block eines Passthrough-Extrakts."""
    m = re.search(r"^```xml\n(.*?)\n```", md.read_text(encoding="utf-8"),
                  flags=re.S | re.M)
    if not m:
        raise click.ClickException(f"Kein XML-Block in {md}")
    return m.group(1)


def node_text(node: ET.Element) -> str:
    """Beschriftung eines Knotens: TEXT-Attribut oder eingebettetes HTML.

    FreeMind legt laengere Beschriftungen als richcontent ab. Beides kommt in
    dieser Datei vor, also beides lesen.
    """
    if node.get("TEXT"):
        return re.sub(r"\s+", " ", node.get("TEXT", "")).strip()
    for rich in node.findall("richcontent"):
        text = "".join(rich.itertext())
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            return text
    return ""


def node_rank(node: ET.Element) -> int | None:
    for icon in node.findall("icon"):
        rang = SYMBOL_RANG.get(icon.get("BUILTIN", ""))
        if rang:
            return rang
    return None


def legende(md: Path) -> tuple[dict[int, str], list[str]]:
    """Legende und Fusszeilen aus dem Plakat.

    Die drei Erklaerungen stehen dort als Zeilen, die mit ':' beginnen — das
    Symbol selbst ist eine Grafik und hat keinen Textlayer. Ihre Reihenfolge im
    Dokument ist die Reihenfolge R1, R2, R3.
    """
    text = md.read_text(encoding="utf-8")
    zeilen = [z[2:].strip() for z in text.splitlines() if z.startswith("> ")]
    erklaerungen = [z.lstrip(": ").strip() for z in zeilen if z.startswith(":")]
    fuss = [z for z in zeilen if z.startswith(("Farben", "Stand"))]
    return dict(zip((1, 2, 3), erklaerungen)), fuss


def gliederung(node: ET.Element, tiefe: int, out: list[str],
               ohne_rang: list[str]) -> None:
    text = node_text(node)
    kinder = node.findall("node")
    if text:
        rang = node_rank(node)
        marke = f" · **R{rang}**" if rang else ""
        out.append("  " * max(tiefe - 1, 0) + f"- {text}{marke}")
        # Ein Blatt ohne Rang ist entweder ein Baustein, dem die Quelle das
        # Symbol schuldig bleibt, oder eine Zwischenebene. Gruppenknoten haben
        # Kinder; ein rangloses Blatt ist auffaellig und gehoert benannt.
        if not kinder and rang is None:
            ohne_rang.append(text)
    for kind in kinder:
        gliederung(kind, tiefe + 1, out, ohne_rang)


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("-o", "--output", "out_dir", default="output", show_default=True,
              type=click.Path(exists=True, file_okay=False),
              help="Ordner mit den Extrakten.")
@click.option("--to", "ziele", multiple=True, default=("output/_GS-STRUKTUR.md",),
              show_default=True, help="Zieldatei; mehrfach angebbar.")
def main(out_dir: str, ziele: tuple[str, ...]) -> None:
    """Fuegt Mindmap und Plakat zu einer navigierbaren Gliederung zusammen."""
    ordner = Path(out_dir)
    mm_md, pdf_md = ordner / f"{MINDMAP}.md", ordner / f"{PLAKAT}.md"
    for p in (mm_md, pdf_md):
        if not p.exists():
            raise click.ClickException(f"Fehlt: {p}")

    wurzel = ET.fromstring(fenced_xml(mm_md)).find("node")
    if wurzel is None:
        raise click.ClickException("Mindmap ohne Wurzelknoten")
    erklaerung, fuss = legende(pdf_md)

    zeilen: list[str] = []
    ohne_rang: list[str] = []
    gliederung(wurzel, 0, zeilen, ohne_rang)
    bausteine = sum(1 for z in zeilen if "**R" in z)

    kopf = [
        "---", "type: struktur", "framework: bsi-grundschutz",
        'quellen: ["GS_Struktur_Edition-2023.mm", "GS_Struktur_Edition-2023.pdf"]',
        "abgeleitet: true",
        'tags: ["grc/struktur", "grc/framework/bsi-grundschutz"]',
        "generated-by: document-to-LLM", "---", "",
        "# IT-Grundschutz-Kompendium 2023 — Baustein-Struktur", "",
        "> [!info] Abgeleitete Darstellung",
        "> Diese Gliederung ist **zusammengesetzt**, nicht woertlich extrahiert: die",
        "> Hierarchie stammt aus `GS_Struktur_Edition-2023.mm`, die Bedeutung der",
        "> Rangstufen aus der Legende von `GS_Struktur_Edition-2023.pdf`. Getrennt",
        "> ist keine der beiden Quellen brauchbar — die Mindmap traegt Symbole ohne",
        "> Erklaerung, das Plakat die Erklaerung ohne maschinenlesbare Struktur.",
        "> Fuer woertliche Zitate die beiden Extrakte heranziehen.", "",
        f"**{bausteine} Bausteine** mit Rangstufe." + (f" {' · '.join(fuss)}" if fuss else ""),
        "", "## Umsetzungsreihenfolge", "",
    ]
    for rang in (1, 2, 3):
        if rang in erklaerung:
            kopf.append(f"- **R{rang}** — {erklaerung[rang]}")
    if ohne_rang:
        kopf += ["", "> [!warning] Ohne Rangstufe in der Quelle",
                 "> Diese Bausteine tragen in der Mindmap kein Symbol, obwohl sie",
                 "> Bausteine sind. Die Angabe fehlt in der Quelle, sie wurde hier",
                 "> nicht ergaenzt: " + ", ".join(f"`{b}`" for b in ohne_rang) + "."]
    kopf += ["", "## Gliederung", ""]

    inhalt = "\n".join(kopf + zeilen) + "\n"
    for ziel in ziele:
        p = Path(ziel).expanduser()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(inhalt, encoding="utf-8")
    click.secho(f"{bausteine} Bausteine, {len(zeilen)} Knoten -> "
                + ", ".join(str(Path(z).expanduser()) for z in ziele), fg="green")


if __name__ == "__main__":
    main()
