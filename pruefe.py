#!/usr/bin/env python3
"""Plausibilitaetspruefung ueber den gesamten Bestand.

Die bisherigen Pruefungen fragten, ob etwas *da* ist: ein Feld befuellt, eine
ID vorhanden, keine Dublette. Das ist zu wenig. Der Grundschutz-Export war
nach diesen Massstaeben fehlerfrei und trotzdem unbrauchbar: jede Anforderung
trug im Median 54019 Zeichen statt der ueblichen paar hundert, weil die
Abschnittsgrenze nicht griff und jeder Eintrag den Rest des Dokuments
mitschleppte. Kein Feld fehlte, keine ID war doppelt, alles gruen.

Dieses Skript fragt stattdessen, ob die Werte *stimmen koennen*. Es kennt
keine richtigen Werte, aber es kennt Groessenordnungen: eine Anforderung ist
ein Absatz, kein Kapitel; eine Textseite traegt tausende Zeichen, keine zehn;
ein Extrakt ist so lang wie seine Quelle, nicht zwanzigmal so lang.

Auffaelligkeiten sind Hinweise, keine Urteile. Jeder Befund nennt die Zahl,
den Massstab und das betroffene Objekt, damit er nachpruefbar ist statt
geglaubt werden zu muessen.

    python pruefe.py                # ganzer Bestand
    python pruefe.py --strict       # Exit 1 bei Auffaelligkeiten (fuer CI)
"""
from __future__ import annotations

import json
import re
import statistics
from dataclasses import dataclass, field
from pathlib import Path

import click

# Groessenordnungen, keine Grenzwerte im normativen Sinn. Sie sind bewusst
# weit gesetzt: ein Fehlalarm kostet einen Blick, ein uebersehener Befund
# kostet das Vertrauen in den ganzen Bestand.
ANFORDERUNG_MEDIAN_MAX = 8_000     # Median je Framework
ANFORDERUNG_EINZEL_MAX = 150_000   # einzelne Anforderung
ZEICHEN_JE_SEITE_MIN = 80          # darunter: vermutlich Scan ohne Textlayer
EXTRAKT_UEBERHANG = 25.0           # Extrakt/Quelle, faengt Endlos-Abschnitte


@dataclass
class Befund:
    bereich: str
    objekt: str
    aussage: str
    zahl: str
    massstab: str


def bekannte_faelle() -> set[str]:
    """Slugs, deren Auffaelligkeit bereits geprueft und festgehalten ist.

    Ein dokumentierter Befund ist kein offener Befund. Wer ihn erneut als
    Auffaelligkeit meldet, erzeugt Laerm, und Laerm macht den naechsten echten
    Fund unsichtbar. Zugleich ist der Abgleich die Gegenprobe: findet die
    Pruefung etwas, das die Registry kennt, stimmen beide ueberein.
    """
    p = Path(__file__).parent / "mappings" / "vault-ausnahmen.json"
    if not p.exists():
        return set()
    d = json.loads(p.read_text(encoding="utf-8"))
    return {e.get("slug", "") for e in d.get("teilweise_erfasst", {}).get("eintraege", [])}


@dataclass
class Bericht:
    befunde: list[Befund] = field(default_factory=list)
    geprueft: dict[str, int] = field(default_factory=dict)

    def melde(self, *a: str) -> None:
        self.befunde.append(Befund(*a))


def pruefe_export(ordner: Path, b: Bericht) -> None:
    """Anforderungen: ein Absatz, kein Kapitel."""
    n = 0
    for f in sorted(ordner.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        reqs = d.get("requirements", [])
        if not reqs:
            b.melde("Export", d.get("frameworkId", f.stem),
                    "keine Anforderungen", "0", "> 0")
            continue
        n += len(reqs)
        laengen = [len(r.get("text", "")) for r in reqs]
        med = statistics.median(laengen)
        fw = d.get("frameworkId", f.stem)
        if med > ANFORDERUNG_MEDIAN_MAX:
            b.melde("Export", fw,
                    "Anforderungen im Median zu lang — Abschnittsgrenze greift "
                    "vermutlich nicht, jeder Eintrag traegt Fremdtext",
                    f"{med:.0f} Zeichen", f"<= {ANFORDERUNG_MEDIAN_MAX}")
        for r, lg in zip(reqs, laengen):
            if lg > ANFORDERUNG_EINZEL_MAX:
                b.melde("Export", f"{fw} {r.get('id', '?')}",
                        "einzelne Anforderung unplausibel lang",
                        f"{lg} Zeichen", f"<= {ANFORDERUNG_EINZEL_MAX}")
        leer = [r.get("id") for r in reqs if not r.get("text", "").strip()]
        if leer:
            b.melde("Export", fw, "Anforderungen ohne Wortlaut",
                    f"{len(leer)} ({', '.join(map(str, leer[:5]))})", "0")
        doppelt = len(reqs) - len({r.get("id") for r in reqs})
        if doppelt:
            b.melde("Export", fw, "doppelte IDs", str(doppelt), "0")
    b.geprueft["Anforderungen"] = n


def pruefe_korpus(register: Path, b: Bericht) -> None:
    """Extrakte: so lang wie ihre Quelle, und ihre Kennzeichnung stimmig."""
    if not register.exists():
        return
    docs = json.loads(register.read_text(encoding="utf-8")).get("documents", [])
    b.geprueft["Dokumente"] = len(docs)
    for d in docs:
        slug = d.get("slug", "?")
        seiten, woerter = d.get("pages") or 0, d.get("words") or 0
        md = Path(d.get("markdown", ""))

        # Ein Dokument ohne Deckung muss als solches gekennzeichnet sein --
        # sonst wandert maschinell gelesener Text als belegter Wortlaut weiter.
        if d.get("text_coverage_percent") is None and d.get("woertlich") is not False:
            b.melde("Korpus", slug,
                    "keine Deckungszahl, aber nicht als 'nicht woertlich' markiert",
                    str(d.get("woertlich")), "false")
        if d.get("ocr") and d.get("woertlich"):
            b.melde("Korpus", slug, "als OCR und zugleich als woertlich gefuehrt",
                    "ocr=true, woertlich=true", "sich ausschliessend")

        if seiten and woerter:
            je_seite = woerter * 6 / seiten     # grob Zeichen je Seite
            if je_seite < ZEICHEN_JE_SEITE_MIN and d.get("text_coverage_percent") is not None:
                b.melde("Korpus", slug,
                        "sehr wenig Text je Seite, aber als geprueft gefuehrt — "
                        "Inhalt steckt vermutlich in Bildern",
                        f"{je_seite:.0f} Zeichen/Seite",
                        f">= {ZEICHEN_JE_SEITE_MIN}")
        # Nur fuer PDFs: dort ist eine Seite eine Seite. Bei XLSX/PPTX ist sie
        # ein Blatt bzw. eine Folie und darf legitim riesig sein --
        # A3_Modellierung verbindet Zellen ueber 45 Spalten, Docling schreibt
        # den Wert in jede, aus 210 kB Quelle werden 8,6 MB Markdown. Reine
        # Wiederholung, kein Fehler. Ein Massstab, der das anschlaegt, erzeugt
        # Laerm und macht die echten Befunde unsichtbar.
        ist_pdf = str(d.get("source_file", "")).lower().endswith(".pdf")
        if md.exists() and seiten and ist_pdf:
            je_seite_md = md.stat().st_size / seiten
            if je_seite_md > EXTRAKT_UEBERHANG * 1000:
                b.melde("Korpus", slug,
                        "Extrakt je Seite unplausibel gross — Wiederholung "
                        "oder Endlos-Abschnitt",
                        f"{je_seite_md/1000:.1f} kB/Seite",
                        f"<= {EXTRAKT_UEBERHANG} kB")
            # Jede Seite der Quelle muss im Extrakt eine Marke haben. Fehlt
            # eine, ist ihr Inhalt entweder verloren oder einer Nachbarseite
            # zugeschlagen -- beides unsichtbar fuer Laenge und Deckung, weil
            # die Woerter ja da sind, nur nicht dort, wo das Zitat sie sucht.
            marken = {int(m) for m in re.findall(
                r"<!-- page: (\d+) -->", md.read_text(encoding="utf-8", errors="replace"))}
            fehlend = sorted(set(range(1, seiten + 1)) - marken)
            if fehlend:
                b.melde("Korpus", slug,
                        "Seiten ohne Marke im Extrakt — Zitate mit Seitenzahl sind "
                        "dort nicht belegbar",
                        f"{len(fehlend)} von {seiten} Seiten, z. B. {fehlend[:5]}",
                        "0")


def pruefe_vault(vault: Path, b: Bericht) -> None:
    """Normtext-Notizen: dieselbe Groessenordnung wie der Export."""
    wurzel = vault / "Normen (lizenziert)"
    if not wurzel.exists():
        return
    n = 0
    for fw_dir in sorted(p for p in wurzel.iterdir() if p.is_dir()):
        if fw_dir.name == "dokumente":
            continue
        groessen = []
        for p in fw_dir.glob("*(Normtext).md"):
            groessen.append(p.stat().st_size)
        if not groessen:
            continue
        n += len(groessen)
        med = statistics.median(groessen)
        if med > ANFORDERUNG_MEDIAN_MAX * 2:   # Notiz traegt Frontmatter dazu
            b.melde("Vault", fw_dir.name,
                    "Normtext-Notizen im Median zu gross — vermutlich derselbe "
                    "Abschnittsfehler wie im Export",
                    f"{med:.0f} Bytes", f"<= {ANFORDERUNG_MEDIAN_MAX * 2}")
    b.geprueft["Normtext-Notizen"] = n


@click.command()
@click.option("--export", "export_dir", type=click.Path(file_okay=False, path_type=Path),
              default=Path("export"), show_default=True)
@click.option("--korpus", type=click.Path(dir_okay=False, path_type=Path),
              default=Path("output/_KORPUS.json"), show_default=True)
@click.option("--vault", type=click.Path(file_okay=False, path_type=Path),
              default=None, help="Vaultwurzel; ohne Angabe wird der Vault uebersprungen.")
@click.option("--strict", is_flag=True, help="Exit 1, wenn Auffaelligkeiten bleiben.")
def main(export_dir: Path, korpus: Path, vault: Path | None, strict: bool) -> None:
    """Prueft, ob die Werte im Bestand stimmen koennen — nicht, ob sie da sind."""
    b = Bericht()
    bekannt = bekannte_faelle()
    if export_dir.exists():
        pruefe_export(export_dir, b)
    pruefe_korpus(korpus, b)
    if vault:
        pruefe_vault(vault, b)

    schon_bekannt = [f for f in b.befunde if f.objekt in bekannt]
    b.befunde = [f for f in b.befunde if f.objekt not in bekannt]

    umfang = ", ".join(f"{v} {k}" for k, v in b.geprueft.items() if v)
    click.echo(f"Geprueft: {umfang or 'nichts gefunden'}")
    for f in schon_bekannt:
        click.secho(f"Bekannt und festgehalten: {f.objekt} ({f.zahl}) — "
                    f"siehe 'teilweise_erfasst' in mappings/vault-ausnahmen.json",
                    fg="cyan")
    if not b.befunde:
        click.secho("Keine offenen Auffaelligkeiten.", fg="green")
        return
    click.secho(f"\n{len(b.befunde)} Auffaelligkeit(en):", fg="yellow")
    for f in b.befunde:
        click.echo(f"  [{f.bereich}] {f.objekt}")
        click.echo(f"      {f.aussage}")
        click.echo(f"      gemessen {f.zahl}, erwartet {f.massstab}")
    if strict:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
