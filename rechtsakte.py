#!/usr/bin/env python3
"""Importiert amtliche Rechtstexte als Ground Truth.

Warum das kein Widerspruch zur Regel "keine eigenen Parser" ist
--------------------------------------------------------------
Die Regel gilt PDFs: dort muss ein Parser aus Koordinaten und Schriftgroessen
erraten, was Ueberschrift, was Spalte und was Tabellenzelle ist — und rat
falsch. Hier wird nichts geraten. gesetze-im-internet.de liefert XML nach einer
veroeffentlichten DTD (gii-norm), in der jeder Paragraf ein Element mit
Bezeichnung, Titel und Text ist. Gelesen wird mit dem XML-Parser der
Standardbibliothek, nicht mit einem Regex ueber Fliesstext.

Warum ueberhaupt
----------------
Ein aus einem PDF gewonnener Export laesst sich nicht gegen dasselbe PDF
pruefen — das waere dieselbe Hand zweimal. Das amtliche XML ist die zweite,
unabhaengige Quelle: andere Herkunft, anderes Format, anderer Leseweg. Genau
das verlangt die Zwei-Quellen-Regel.

Rechtslage: amtliche Werke sind nach § 5 UrhG gemeinfrei. Dieser Primaertext
darf deshalb — anders als ISO- oder TISAX-Woertlaut — im Repository liegen.

Nutzung
-------
    python rechtsakte.py import input/BJNR12D0B0025.xml
    python rechtsakte.py import input/ --alle
    python rechtsakte.py liste
"""
from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import click

GT_ORDNER = Path("fixtures/ground-truth")
GII_BASIS = "https://www.gesetze-im-internet.de"

# Elemente, die im gii-XML eine sichtbare Grenze bilden: dort steht im Satz ein
# Leerzeichen, auch wenn im XML keins steht. Ohne diese Liste klebte die
# Aufzaehlungsmarke am Text -- aus "<DT>1.</DT><DD>Konzepte" wurde
# "1.Konzepte", und der Resolver meldete jeden solchen Absatz als Abweichung,
# obwohl der Extrakt richtig war. Ein Pruefmassstab, der selbst falsch
# zusammensetzt, erzeugt genau die Fehlalarme, die ihn unbrauchbar machen.
GRENZE = {"P", "DT", "DD", "LA", "table", "row", "entry", "Title", "Ident", "TOC"}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for brocken in iter(lambda: f.read(1 << 20), b""):
            h.update(brocken)
    return h.hexdigest()


def _roh(el: ET.Element) -> str:
    """Text eines Elements, mit Leerzeichen an den sichtbaren Elementgrenzen.

    Innerhalb eines Absatzes wird NICHT getrennt: Auszeichnungen wie <F> stehen
    mitten im Wort, ein Leerzeichen dort zerrisse es.
    """
    teile: list[str] = [el.text or ""]
    for kind in el:
        inhalt = _roh(kind)
        teile.append(f" {inhalt} " if kind.tag in GRENZE else inhalt)
        teile.append(kind.tail or "")
    return "".join(teile)


def blocktext(el: ET.Element) -> str:
    """Sichtbarer Text eines Blocks, Zwischenraum normalisiert.

    Bewusst nicht mehr: keine Nummerierung ergaenzt, keine Aufzaehlungszeichen
    erfunden, keine Reihenfolge geaendert. Was hier herauskommt, muss sich im
    Extrakt woertlich wiederfinden lassen — jede Verschoenerung waere ein
    Unterschied, der spaeter als Abweichung gemeldet wuerde.
    """
    return re.sub(r"\s+", " ", _roh(el)).strip()


def normtext(norm: ET.Element) -> str:
    content = norm.find("textdaten/text/Content")
    if content is None:
        return ""
    teile = [blocktext(kind) for kind in content]
    return "\n".join(t for t in teile if t)


@dataclass
class Rechtsakt:
    kurzname: str
    jurabk: str
    langue: str
    ausfertigung: str
    fundstelle: str
    stand: list[str]
    quelle: str
    datei: str
    sha256: str
    bytes: int
    fundstellen: list[dict]


def lies_gii(pfad: Path) -> Rechtsakt:
    wurzel = ET.parse(pfad).getroot()
    normen = wurzel.findall("norm")
    if not normen:
        raise SystemExit(f"{pfad}: kein <norm>-Element — ist das gii-norm-XML?")

    kopf = normen[0].find("metadaten")
    jurabk = (kopf.findtext("jurabk") or "").strip()
    amtabk = (kopf.findtext("amtabk") or jurabk).strip()
    langue = (kopf.findtext("langue") or "").strip()
    ausfertigung = (kopf.findtext("ausfertigung-datum") or "").strip()
    periodikum = (kopf.findtext("fundstelle/periodikum") or "").strip()
    zitstelle = (kopf.findtext("fundstelle/zitstelle") or "").strip()
    stand = [f"{s.findtext('standtyp', '').strip()}: {s.findtext('standkommentar', '').strip()}"
             for s in kopf.findall("standangabe")]

    fundstellen: list[dict] = []
    gliederung = ""
    for norm in normen:
        md = norm.find("metadaten")
        if md is None:
            continue
        gl_bez = (md.findtext("gliederungseinheit/gliederungsbez") or "").strip()
        gl_titel = (md.findtext("gliederungseinheit/gliederungstitel") or "").strip()
        if gl_bez:
            gliederung = f"{gl_bez} {gl_titel}".strip()

        enbez = (md.findtext("enbez") or "").strip()
        titel = (md.findtext("titel") or "").strip()
        text = normtext(norm)

        # Nur echte Vorschriften. Die Inhaltsuebersicht wiederholt alle Titel
        # und wuerde jede Ueberschrift doppelt aufloesen lassen; Gliederungs-
        # knoten tragen keinen eigenen Text.
        if not enbez or enbez == "Inhaltsübersicht" or not text:
            continue

        fundstellen.append({
            "id": enbez,
            "art": "paragraf",
            "titel": titel,
            "text": text,
            # Ein ganzer Paragraf steht im Extrakt fast nie am Stueck: Seiten-
            # marken, Kopf- und Fusszeilen liegen dazwischen. Geprueft wird
            # deshalb je Absatz -- das ist auch die Ebene, in der zitiert wird
            # ("§ 30 Absatz 2"). Der Gesamttext bleibt fuer den Vergleich mit
            # Quellen, die keine Absaetze fuehren.
            "absaetze": [t for t in text.split("\n") if t],
            "gliederung": gliederung,
            "doknr": norm.get("doknr", ""),
        })

    kurz = re.sub(r"[^a-z0-9]+", "-", amtabk.lower()).strip("-")
    return Rechtsakt(
        kurzname=kurz,
        jurabk=jurabk,
        langue=langue,
        ausfertigung=ausfertigung,
        fundstelle=f"{periodikum} {zitstelle}".strip(),
        stand=stand,
        quelle=f"{GII_BASIS}/{kurz.replace('-', '_')}/",
        datei=pfad.name,
        sha256=sha256(pfad),
        bytes=pfad.stat().st_size,
        fundstellen=fundstellen,
    )


def als_ground_truth(a: Rechtsakt) -> dict:
    return {
        "quelle": f"{a.jurabk} — {a.langue}",
        "kurzname": a.kurzname,
        "herkunft": (
            f"Amtliches XML von gesetze-im-internet.de ({a.quelle}), Datei {a.datei}, "
            f"SHA-256 {a.sha256}, {a.bytes} Bytes. Amtliches Werk nach § 5 UrhG, "
            "gemeinfrei — deshalb darf dieser Primaertext im Repository liegen."
        ),
        "rolle": (
            "Zweite, unabhaengige Quelle im Sinne der Zwei-Quellen-Regel. Der Export "
            "dieses Rechtsakts stammt aus einem PDF; ihn gegen dasselbe PDF zu pruefen "
            "waere dieselbe Hand zweimal. Hier kommt der Woertlaut aus anderem Format, "
            "anderer Herkunft und anderem Leseweg."
        ),
        "amtliche_fundstelle": a.fundstelle,
        "ausfertigung": a.ausfertigung,
        "stand": a.stand,
        "importiert_am": date.today().isoformat(),
        "importiert_mit": "rechtsakte.py (xml.etree, gii-norm-DTD)",
        "fundstellen": a.fundstellen,
    }


@click.group()
def main() -> None:
    """Amtliche Rechtstexte als Pruefmassstab importieren."""


@main.command("import")
@click.argument("pfad", type=click.Path(exists=True, path_type=Path))
@click.option("--alle", is_flag=True, help="Ordner rekursiv nach *.xml durchsuchen.")
@click.option("--ziel", type=click.Path(path_type=Path), default=GT_ORDNER, show_default=True)
def importieren(pfad: Path, alle: bool, ziel: Path) -> None:
    """Liest gii-norm-XML und legt es als Ground Truth ab."""
    dateien = sorted(pfad.rglob("*.xml")) if (pfad.is_dir() or alle) else [pfad]
    if not dateien:
        raise SystemExit(f"Keine XML-Datei unter {pfad}")
    ziel.mkdir(parents=True, exist_ok=True)

    for datei in dateien:
        try:
            akt = lies_gii(datei)
        except (ET.ParseError, SystemExit) as fehler:
            print(f"[uebersprungen] {datei.name}: {fehler}")
            continue
        aus = ziel / f"{akt.kurzname}.json"
        aus.write_text(json.dumps(als_ground_truth(akt), ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
        print(f"{akt.jurabk}: {len(akt.fundstellen)} Fundstellen -> {aus} "
              f"(Stand {akt.ausfertigung}, {akt.fundstelle})")


@main.command("liste")
@click.option("--ziel", type=click.Path(path_type=Path), default=GT_ORDNER, show_default=True)
def liste(ziel: Path) -> None:
    """Zeigt, welche Primaertexte vorliegen — und mit welchem Stand."""
    if not ziel.exists():
        raise SystemExit(f"Kein Ground-Truth-Ordner: {ziel}")
    for datei in sorted(ziel.glob("*.json")):
        gt = json.loads(datei.read_text(encoding="utf-8"))
        stand = "; ".join(gt.get("stand", [])) or "—"
        print(f"{datei.stem:20} {len(gt.get('fundstellen', [])):4} Fundstellen  "
              f"{gt.get('ausfertigung', '—'):12} {stand[:70]}")


if __name__ == "__main__":
    main()
