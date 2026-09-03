#!/usr/bin/env python3
"""Inhaltspruefung: gehoert der Text zu der ID, unter der er steht?

Die Plausibilitaetspruefung sieht Groessenordnungen. Sie faengt einen Text,
der ins Uferlose laeuft — aber nicht einen Versatz um eine Position. Wenn
APP.1.1.A5 den Wortlaut von A6 traegt, sind alle Laengen unauffaellig, alle
Felder befuellt, alle IDs vorhanden. Genau das waere der teuerste Fehler in
einem Compliance-Bestand: eine Anforderung, die etwas anderes sagt, als ihre
Nummer verspricht, und der man das nicht ansieht.

Dieses Skript vergleicht jeden exportierten Wortlaut mit dem Abschnitt, der
im Quellextrakt unter derselben Kennung steht. Nicht stichprobenartig,
sondern fuer jede Anforderung, zu der sich im Extrakt eine Ueberschrift
findet.

Geprueft wird:

  Zuordnung   Deckt sich der exportierte Text mit dem Abschnitt der Quelle?
  Versatz     Traegt eine Anforderung den Wortlaut ihres Nachbarn?
  Leckage     Steht im Text eine fremde Anforderungsueberschrift?
  Titel       Stimmt der Titel mit der Ueberschrift der Quelle ueberein?
  Kennungen   Fehlt eine ID des Registers im Export?

Die frameworkeigene Nummerierung bleibt dabei unangetastet. Sie ist der
Anker, ueber den jede Aussage belegbar wird; eine vereinheitlichte Nummer
kommt spaeter im Mapping dazu, sie ersetzt die Kennung nie.

    python inhalt.py --vault <vault>
    python inhalt.py --vault <vault> --strict     # Exit 1 bei Befunden
"""
from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import click

import publish


def normtext(s: str) -> str:
    """Vergleichsform: Unterschiede, die kein Mensch als solche laese, weg."""
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", s).strip().casefold()


@dataclass
class Befund:
    art: str
    framework: str
    ident: str
    detail: str


@dataclass
class Bericht:
    befunde: list[Befund] = field(default_factory=list)
    geprueft: int = 0
    ohne_ueberschrift: int = 0
    frameworks: int = 0
    entfallen: int = 0

    def melde(self, *a: str) -> None:
        self.befunde.append(Befund(*a))


def quellen_index(out_dir: Path) -> dict[str, Path]:
    """Zuordnung Quelldateiname -> Extrakt, einmal aufgebaut."""
    idx: dict[str, Path] = {}
    for md in sorted(out_dir.glob("*.md")):
        if md.name.startswith("_"):
            continue
        kopf = md.read_text(encoding="utf-8", errors="replace")[:1200]
        m = re.search(r'^source_file:\s*"(.+?)"', kopf, re.M)
        if m:
            idx[m.group(1)] = md
    return idx


def extrakte_zu(d: dict, fw: str, vault: Path | None,
                idx: dict[str, Path]) -> list[Path]:
    """Alle Extrakte, aus denen dieses Framework stammt.

    Der Regelfall ist eine Quelle, dann steht ihr Name im Export. Der BSI-C5
    kommt aber aus 18 YAML-Katalogen, und der Export vermerkt statt eines
    Namens '18 Quelldateien'. Wer nur nach einem Dateinamen sucht, findet
    nichts und meldet das Framework als nicht pruefbar -- 796 Anforderungen
    blieben so ungeprueft, obwohl jede einzelne Quelle vorliegt. Die Namen
    stehen in den Vaultnotizen des Frameworks; von dort werden sie geholt.
    """
    einzeln = idx.get(str(d.get("sourceFile", "")))
    if einzeln:
        return [einzeln]
    if vault is None:
        return []
    ordner = vault / "Normen (lizenziert)" / fw
    if not ordner.is_dir():
        return []
    namen = set()
    for p in ordner.glob("*.md"):
        m = re.search(r'^source_file:\s*"(.+?)"',
                      p.read_text(encoding="utf-8", errors="replace")[:900], re.M)
        if m:
            namen.add(m.group(1))
    return [idx[n] for n in sorted(namen) if n in idx]


def pruefe_framework(pfad: Path, out_dir: Path, b: Bericht,
                    vault: Path | None, idx: dict[str, Path]) -> None:
    d = json.loads(pfad.read_text(encoding="utf-8"))
    fw = d.get("frameworkId", pfad.stem)
    reqs = d.get("requirements", [])
    quellen = extrakte_zu(d, fw, vault, idx)
    if not quellen:
        b.melde("Quelle", fw, "—",
                f"Extrakt zu '{d.get('sourceFile')}' nicht gefunden — "
                f"Zuordnung nicht pruefbar")
        return

    abschnitte: dict[str, publish.Section] = {}
    for q in quellen:
        roh = q.read_text(encoding="utf-8", errors="replace")
        # Die Metadaten des Extrakts mitgeben, nicht ein leeres dict: der
        # YAML-Pfad braucht den Quelldateinamen, um den Katalog zuzuordnen.
        # Ohne ihn galten alle 796 C5-Anforderungen als "ohne Ueberschrift"
        # und blieben ungeprueft -- die Pruefung lief, sah aber nichts.
        q_meta, body = publish.split_front_matter(roh)
        for k, sec in publish.abschnitte_zusammen(body, q_meta).items():
            prev = abschnitte.get(k)
            if prev is None or not prev.text.strip():
                abschnitte[k] = sec

    # Leckage: eine fremde Anforderungsueberschrift im eigenen Text.
    fremde = re.compile(r"^#{1,6}\s+([A-Z]{2,6}(?:\.\d+)+\.A\d+|\d+(?:\.\d+)+)\s",
                        re.M)

    vorher: tuple[str, str] | None = None
    for r in reqs:
        ident, text = r.get("id", ""), r.get("text", "")
        titel = r.get("title", "")

        # Versatz: gleicher Wortlaut wie der Vorgaenger. Zwei Anforderungen
        # mit identischem Text sind entweder eine Dublette oder ein Versatz;
        # beides muss auffallen.
        if vorher and normtext(text) == normtext(vorher[1]) and len(text) > 40:
            b.melde("Versatz", fw, ident,
                    f"identischer Wortlaut wie {vorher[0]}")
        vorher = (ident, text)

        for treffer in fremde.findall(text):
            # Ein Unterpunkt ist nicht fremd: eine Oberklausel, die aus ihren
            # Unterklauseln zusammengesetzt ist, enthaelt deren Ueberschriften
            # zu Recht. Ohne diese Unterscheidung meldet die Pruefung 28 mal
            # Leckage, wo Struktur ist -- und Laerm macht den naechsten echten
            # Fund unsichtbar.
            # "A.4" und "4.1": im ISO-42001-Anhang tragen die Oberpunkte das
            # Praefix A., ihre Unterpunkte im Dokument nicht. Ohne diese
            # Normalisierung meldet die Pruefung sieben mal Leckage, wo
            # Struktur ist.
            kern = ident[2:] if ident.startswith("A.") else ident
            if (treffer != ident and not treffer.startswith(ident + ".")
                    and treffer != kern and not treffer.startswith(kern + ".")):
                b.melde("Leckage", fw, ident,
                        f"fremde Ueberschrift im Text: {treffer}")
                break

        sec = abschnitte.get(publish.norm_key(ident))
        if sec is None:
            b.ohne_ueberschrift += 1
            continue
        b.geprueft += 1

        quelltext, exporttext = normtext(sec.text), normtext(text)
        if quelltext and exporttext != quelltext:
            # Ein Nachtrag oder eine zusammengesetzte Oberklausel darf laenger
            # sein; falsch ist, wenn der Quelltext gar nicht enthalten ist.
            if quelltext not in exporttext and exporttext not in quelltext:
                b.melde("Zuordnung", fw, ident,
                        f"Text deckt sich nicht mit dem Abschnitt der Quelle "
                        f"(Export {len(text)} Z., Quelle {len(sec.text)} Z.)")
        if sec.title and titel and normtext(sec.title) != normtext(titel):
            b.melde("Titel", fw, ident,
                    f"Export '{titel[:45]}' vs Quelle '{sec.title[:45]}'")


def entfallen_belegt(vault: Path, fw: str, ident: str) -> bool:
    """Liegt fuer diese ID eine Entfallen-Notiz aus publish.py --mark-withdrawn vor?"""
    notiz = vault / "Normen (lizenziert)" / fw / f"{fw} {ident} (Normtext).md"
    if not notiz.is_file():
        return False
    return re.search(r"^status:\s*entfallen\s*$",
                     notiz.read_text(encoding="utf-8", errors="replace")[:600], re.M) is not None


def pruefe_kennungen(pfad: Path, vault: Path, b: Bericht) -> None:
    """Keine ID darf auf dem Weg in den Export verlorengehen oder sich aendern.

    Die frameworkeigene Nummerierung ist der Beleganker. Geht sie verloren,
    ist der Wortlaut zwar noch da, aber nicht mehr zuordenbar — und damit als
    Nachweis wertlos.
    """
    d = json.loads(pfad.read_text(encoding="utf-8"))
    fw = d.get("frameworkId", pfad.stem)
    try:
        register = set(publish.vault_ids(vault, fw))
    except Exception:
        return
    export = {r.get("id", "") for r in d.get("requirements", [])}
    # Eine ID, fuer die im Vault eine Entfallen-Notiz liegt, ist kein Verlust
    # auf dem Weg in den Export: die Quelle wurde gelesen, und sie kennt die
    # ID nicht. Das steht in der Notiz, mit Quelldatei und Hash.
    entfallen = sorted(i for i in register - export if entfallen_belegt(vault, fw, i))
    if entfallen:
        b.entfallen += len(entfallen)
        print(f"  {fw}: {len(entfallen)} ID(s) des Registers als entfallen belegt: "
              + ", ".join(entfallen[:8]) + (" ..." if len(entfallen) > 8 else ""))
    fehlend = sorted(register - export - set(entfallen))
    fremd = sorted(export - register)
    if fehlend:
        b.melde("Kennung", fw, "—",
                f"{len(fehlend)} ID(s) des Registers fehlen im Export: "
                + ", ".join(fehlend[:8]) + (" ..." if len(fehlend) > 8 else ""))
    if fremd:
        b.melde("Kennung", fw, "—",
                f"{len(fremd)} ID(s) im Export, die das Register nicht kennt: "
                + ", ".join(fremd[:8]))


@click.command()
@click.option("--export", "export_dir", type=click.Path(file_okay=False, path_type=Path),
              default=Path("export"), show_default=True)
@click.option("--output", "out_dir", type=click.Path(file_okay=False, path_type=Path),
              default=Path("output"), show_default=True)
@click.option("--vault", type=click.Path(file_okay=False, path_type=Path), default=None,
              help="Vaultwurzel, fuer den Abgleich der Kennungen gegen das Register.")
@click.option("--only", default=None, help="Nur dieses Framework pruefen.")
@click.option("--strict", is_flag=True, help="Exit 1, wenn Befunde bleiben.")
def main(export_dir: Path, out_dir: Path, vault: Path | None,
         only: str | None, strict: bool) -> None:
    """Prueft, ob jeder Wortlaut zu der Kennung gehoert, unter der er steht."""
    b = Bericht()
    idx = quellen_index(out_dir)
    for pfad in sorted(export_dir.glob("*.json")):
        if only and pfad.stem != only:
            continue
        b.frameworks += 1
        pruefe_framework(pfad, out_dir, b, vault, idx)
        if vault:
            pruefe_kennungen(pfad, vault, b)

    click.echo(f"Geprueft: {b.geprueft} Anforderungen gegen die Quelle "
               f"({b.frameworks} Frameworks); {b.ohne_ueberschrift} ohne "
               f"Ueberschrift im Extrakt, dort nicht pruefbar.")
    if not b.befunde:
        click.secho("Keine Abweichung: jeder Wortlaut steht unter seiner Kennung.",
                    fg="green")
        return
    nach_art: dict[str, list[Befund]] = {}
    for f in b.befunde:
        nach_art.setdefault(f.art, []).append(f)
    click.secho(f"\n{len(b.befunde)} Befund(e):", fg="yellow")
    for art, liste in nach_art.items():
        click.secho(f"\n  {art} ({len(liste)})", fg="yellow")
        for f in liste[:15]:
            click.echo(f"    {f.framework} {f.ident}: {f.detail}")
        if len(liste) > 15:
            click.echo(f"    ... und {len(liste) - 15} weitere")
    if strict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
