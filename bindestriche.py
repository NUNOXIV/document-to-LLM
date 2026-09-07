#!/usr/bin/env python3
"""Setzt Bindestriche zurueck, die beim Konvertieren verlorengingen.

Der Befund
----------
Docling loest die Trennung am Zeilenende auf, indem es den Trennstrich
entfernt. Bei einem Wort, das der Umbruch getrennt hat, ist das richtig
("Informations-\\nsicherheit"). Bei einem Wort, das den Bindestrich selbst
traegt, ist es falsch: aus "IKT-\\nSystemen" wird "IKTSystemen" — ein Wort, das
in keiner Quelle steht und das keine Suche findet.

Warum es niemand gesehen hat: die Deckungspruefung entfernt denselben Strich
auch auf der Quellseite. Beide Seiten hiessen "iktsystemen", die Deckung blieb
100,0 %. Gefunden hat es der Abgleich gegen das amtliche Gesetzes-XML.

Die Regel
---------
Angefasst wird nur mit Beleg: ein Wort wird geaendert, wenn seine Form OHNE
Bindestrich im Textlayer der Quelle nicht vorkommt und die Form MIT Bindestrich
dort vorkommt. Damit bleibt echtes Binnenmajuskel ("OpenLDAP") unberuehrt — es
steht so in der Quelle.

Nutzung
-------
    python bindestriche.py                 # nur zaehlen, nichts aendern
    python bindestriche.py --reparieren    # Extrakte in output/ berichtigen
"""
from __future__ import annotations

import sys
from pathlib import Path

import click

import publish
import verify


def quelle_zu(meta: dict[str, str], eingang: Path) -> Path | None:
    """Findet die Quelldatei eines Extrakts ueber das Front-Matter."""
    name = (meta.get("source_file") or "").strip().strip('"')
    if not name.lower().endswith(".pdf"):
        return None
    treffer = [p for p in eingang.rglob("*.pdf") if p.name == name]
    return treffer[0] if treffer else None


def vermerke(kopf: str, anzahl: int, beispiele: str,
             feld: str = "restored_hyphens", hinweis: str = "") -> str:
    """Traegt den Befund ins Front-Matter ein — sichtbar, nicht stillschweigend."""
    zeilen = kopf.rstrip("\n").splitlines()
    hinweis = hinweis or (
        f"{anzahl} Wort(e) hatten einen Bindestrich der Quelle verloren und wurden "
        f"zurueckgesetzt (belegt durch den Textlayer): {beispiele}")
    ende = len(zeilen) - 1 if zeilen and zeilen[-1] == "---" else len(zeilen)
    neu = zeilen[:ende]
    neu = [z for z in neu if not z.startswith(f"{feld}:")]
    neu.append(f"{feld}: {anzahl}")
    if "warnings:" in neu:
        stelle = neu.index("warnings:") + 1
        neu.insert(stelle, f'  - "{hinweis}"')
    else:
        neu += ["warnings:", f'  - "{hinweis}"']
    return "\n".join(neu + ["---"]) + "\n"


@click.command()
@click.option("--output", type=click.Path(exists=True, path_type=Path), default=Path("output"),
              show_default=True, help="Ordner mit den Extrakten.")
@click.option("--input", "eingang", type=click.Path(exists=True, path_type=Path),
              default=Path("input"), show_default=True, help="Ordner mit den Quelldateien.")
@click.option("--reparieren", is_flag=True,
              help="Extrakte tatsaechlich aendern. Ohne diesen Schalter wird nur gezaehlt.")
@click.option("--strict", is_flag=True, help="Exit 1, wenn Befunde offen bleiben.")
def main(output: Path, eingang: Path, reparieren: bool, strict: bool) -> None:
    """Prueft alle PDF-Extrakte auf verlorene Bindestriche."""
    betroffen = worte = ohne_quelle = 0
    geprueft = 0
    for md in sorted(p for p in output.glob("*.md")
                     if not p.name.startswith("_") and not p.name.startswith(".")):
        roh = md.read_text(encoding="utf-8")
        meta, koerper = publish.split_front_matter(roh)
        quelle = quelle_zu(meta, eingang)
        if quelle is None:
            if (meta.get("source_file") or "").strip('"').lower().endswith(".pdf"):
                ohne_quelle += 1
            continue
        geprueft += 1
        try:
            # NICHT "roh" nennen: diese Variable haelt bereits den Markdown-Text.
            # Die Verwechslung hat den Kopf von 187 Extrakten aus dem PDF-Text
            # geschnitten statt aus dem Markdown -- ein einziger Name, 187
            # zerstoerte Dateien.
            quelltext = verify.quelltext(quelle)
        except Exception as fehler:
            print(f"  [nicht pruefbar] {md.name}: {fehler}")
            continue
        neu, treffer = verify.repariere_bindestriche(
            koerper, verify.quelle_kompakt(quelle, quelltext),
            verify.zusammenhaengende_quelle(quelle, quelltext))

        # Zweiter Durchgang mit dem zweiten Leser: wo pypdfium nur ein
        # unlesbares Zeichen liefert, liest das Docling-Backend die Trennung.
        # Nur dort, wo die Quelle selbst sagt, welche Form gemeint ist.
        trenn: dict[str, str] = {}
        if verify.unlesbar_im_wort(quelltext):
            try:
                neu, trenn = verify.repariere_trennungen(neu, verify.zweitleser_zeilen(quelle))
            except Exception as fehler:
                print(f"  [Zweitleser nicht verfuegbar] {md.name}: {fehler}")

        if not treffer and not trenn:
            continue
        betroffen += 1
        worte += len(treffer) + len(trenn)
        beispiele = ", ".join(f"{a} -> {b}" for a, b in sorted(treffer.items())[:3])
        b2 = ", ".join(f"{a} -> {b}" for a, b in sorted(trenn.items())[:3])
        print(f"  {md.name}: {len(treffer)} Bindestrich(e)"
              + (f" ({beispiele})" if treffer else "")
              + (f", {len(trenn)} Trennung(en) ueber den Zweitleser ({b2})" if trenn else ""))
        if reparieren:
            kopf = roh[:len(roh) - len(koerper)]
            ergebnis = kopf
            if treffer:
                ergebnis = vermerke(ergebnis, len(treffer), beispiele)
            if trenn:
                ergebnis = vermerke(
                    ergebnis, len(trenn), b2, feld="restored_splits",
                    hinweis=(f"{len(trenn)} Wort(e) hatten eine Trennung der Quelle verloren, "
                             f"weil der Textlayer dort ein unlesbares Zeichen fuehrt. Ein "
                             f"zweiter Leser (Docling-Backend) belegt die Trennstelle, die "
                             f"Quelle selbst die Form: {b2}"))
            ergebnis = ergebnis + neu
            if not ergebnis.startswith("---\n"):
                # Lieber nichts schreiben als eine Datei ohne Kopf. Genau das
                # ist passiert, und es faellt erst Stunden spaeter auf.
                print(f"  [nicht geschrieben] {md.name}: Kopf ginge verloren")
                continue
            md.write_text(ergebnis, encoding="utf-8")

    tat = "berichtigt" if reparieren else "gefunden (nichts geaendert)"
    print(f"\n{geprueft} PDF-Extrakte geprueft, {betroffen} betroffen, {worte} Wort(e) {tat}.")
    if ohne_quelle:
        print(f"{ohne_quelle} Extrakt(e) ohne auffindbare Quelldatei — dort nicht pruefbar.")
    if strict and (betroffen and not reparieren):
        sys.exit(1)


if __name__ == "__main__":
    main()
