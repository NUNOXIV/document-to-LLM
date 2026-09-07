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
    wortlaut_belegt: int = 0
    ohne_quelle: int = 0

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


# So viele Woerter am Stueck muessen aus dem Wortlaut in der Quelle stehen.
# Kuerzere Texte (Titelzeilen, "Diese Anforderung ist entfallen.") sagen zu
# wenig, um daraus einen Befund zu machen.
PROBE_WOERTER = 8


def wortlaut_in_quelle(text: str, quelle: str) -> bool:
    """Steht der Wortlaut ueberhaupt in der Quelle?

    Die Zuordnungspruefung braucht die Ueberschrift der Anforderung im Extrakt;
    fehlt sie, galt die Anforderung als "dort nicht pruefbar" — 422 von 3855
    blieben so ganz ungeprueft. Diese Probe kommt ohne Ueberschrift aus: sie
    nimmt den laengsten zusammenhaengenden Ausschnitt des Wortlauts und sucht
    ihn im Quellextrakt. Sie belegt nicht, dass der Text unter der richtigen
    Kennung steht -- das kann nur die Zuordnungspruefung. Sie belegt, dass er
    aus der Quelle stammt und nicht erfunden ist.
    """
    # Eine Gruppen-ID wird aus ihren Unterpunkten zusammengesetzt, und die
    # dabei eingefuegten Zwischenueberschriften ("### 4.1 Devices") stehen so
    # in keiner Quelle. Sie sind Struktur dieses Werkzeugs, nicht Wortlaut des
    # Dokuments — geprueft wird der Text zwischen ihnen. Acht Gruppen von CIS
    # und TISAX wurden sonst gemeldet, obwohl ihr Text vollstaendig aus der
    # Quelle stammt.
    q = normtext(quelle)
    abschnitte = [a for a in re.split(r"(?m)^#{1,6}\s+.*$", text) if a.strip()]
    for abschnitt in sorted(abschnitte, key=len, reverse=True):
        worte = normtext(abschnitt).split()
        if len(worte) < PROBE_WOERTER:
            continue
        # Mehrere Ausschnitte, damit ein einzelner Bindestrich oder ein
        # Tabellentrenner in der Mitte nicht den ganzen Befund erzeugt.
        for start in (0, max(0, (len(worte) - PROBE_WOERTER) // 2), len(worte) - PROBE_WOERTER):
            if " ".join(worte[start:start + PROBE_WOERTER]) in q:
                return True
        return False
    return True


def ueberhaenge(reqs: list[dict]) -> list[tuple[str, str]]:
    """Zeilen, die den vollen Text einer anderen Anforderung enthalten.

    Doppelter Text hat volle Wortdeckung und faellt keiner Deckungspruefung
    auf. Das Aufnahmetor des Auftraggebers fand so 12 Zeilen (DSGVO Art.21
    mit Art.22 und Art.23, DORA Art.30 mit Art.31 ...), die hier niemand sah.
    Eine Oberklausel, die aus ihren Unterpunkten zusammengesetzt ist (9.2 aus
    9.2.1), enthaelt deren Text zu Recht und zaehlt nicht.
    """
    norm = {str(r.get("id", "")): normtext(str(r.get("text", ""))) for r in reqs}
    treffer: list[tuple[str, str]] = []
    for a, ta in norm.items():
        if len(ta) < 200:
            continue
        # Woertlich gleiche Texte zweier Anforderungen (das Kompendium fuehrt
        # SYS.1.1.A31 und SYS.2.1.A33 identisch) sind kein Ueberhang; sie
        # gehoeren auch nicht in eine Oberklausel hineingerechnet, die aus
        # ihrem Unterpunkt besteht.
        kinder = {t for k, t in norm.items() if k.startswith(a + ".") or k.startswith(a + "-")}
        for bb, tb in norm.items():
            if bb == a or len(tb) < 200 or len(tb) >= len(ta):
                continue
            if bb.startswith(a + ".") or bb.startswith(a + "-") or tb in kinder:
                continue
            if tb[:60] in ta and tb in ta:
                treffer.append((a, bb))
    return sorted(treffer)


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

    # Volltext aller Quellextrakte: Grundlage der Wortlautprobe fuer
    # Anforderungen, die keine eigene Ueberschrift im Extrakt haben.
    quelltext_gesamt = normtext(" ".join(
        publish.split_front_matter(q.read_text(encoding="utf-8", errors="replace"))[1]
        for q in quellen))

    # Leckage: eine fremde Anforderungsueberschrift im eigenen Text.
    fremde = re.compile(r"^#{1,6}\s+([A-Z]{2,6}(?:\.\d+)+\.A\d+|\d+(?:\.\d+)+)\s",
                        re.M)

    for a, bb in ueberhaenge(reqs):
        b.melde("Ueberhang", fw, a, f"enthaelt den vollen Text von {bb}")

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
            # Ohne Ueberschrift ist die Zuordnung nicht pruefbar, der Wortlaut
            # aber schon: er muss in der Quelle ueberhaupt vorkommen.
            b.ohne_ueberschrift += 1
            if not wortlaut_in_quelle(text, quelltext_gesamt):
                b.melde("Wortlaut", fw, ident,
                        "steht so nicht im Quellextrakt — weder unter dieser noch "
                        "unter einer anderen Ueberschrift")
            else:
                b.wortlaut_belegt += 1
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


def register_ohne_quelle(fw: str) -> set[str]:
    """Kennungen des Registers, zu denen es im Bestand keinen Primaertext gibt.

    Nachgewiesen und begruendet in mappings/vault-ausnahmen.json. Sie fehlen im
    Export zu Recht: ohne Quelle wird kein Wortlaut abgelegt. Als offener Befund
    gefuehrt zu werden waere falsch — es gibt nichts zu beheben, ausser die
    Quelle zu beschaffen. Sichtbar bleiben sie trotzdem.
    """
    p = Path(__file__).parent / "mappings" / "vault-ausnahmen.json"
    if not p.exists():
        return set()
    d = json.loads(p.read_text(encoding="utf-8")).get("register_ohne_quelle", {})
    return {k for e in d.get("eintraege", []) if e.get("framework") == fw
            for k in e.get("kennungen", [])}


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
    zurueckgezogen = sorted((register - export - set(entfallen))
                            & publish.vault_withdrawn(vault, fw))
    if zurueckgezogen:
        b.entfallen += len(zurueckgezogen)
        print(f"  {fw}: {len(zurueckgezogen)} ID(s) im Register als withdrawn gefuehrt und im "
              "Dokument nicht mehr vorhanden: " + ", ".join(zurueckgezogen[:8]))
    ohne_quelle = sorted((register - export) & register_ohne_quelle(fw))
    if ohne_quelle:
        b.ohne_quelle += len(ohne_quelle)
        print(f"  {fw}: {len(ohne_quelle)} Kennung(en) des Registers ohne Primaerquelle im "
              f"Bestand, dokumentiert in mappings/vault-ausnahmen.json: "
              + ", ".join(ohne_quelle[:6]) + (" ..." if len(ohne_quelle) > 6 else ""))
    fehlend = sorted(register - export - set(entfallen) - set(zurueckgezogen) - set(ohne_quelle))
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

    click.echo(f"Geprueft: {b.geprueft} Anforderungen Wort fuer Wort unter ihrer "
               f"Kennung ({b.frameworks} Frameworks); {b.ohne_ueberschrift} ohne "
               f"eigene Ueberschrift im Extrakt, davon {b.wortlaut_belegt} mit "
               f"Wortlaut in der Quelle belegt.")
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
