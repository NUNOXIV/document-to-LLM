#!/usr/bin/env python3
"""Fundstellen-Resolver: loest jede Fundstelle gegen den Primaertext auf.

Wozu
----
Die bestehenden Waechter pruefen Konsistenz: Schema, Kennungen, Laengen,
Versatz, Wortdeckung. Sie messen, ob die Maschine mit sich selbst
uebereinstimmt. Was sie nicht messen koennen: ob eine Fundstelle mit dem
Primaertext uebereinstimmt. Genau diese Ebene fehlte — und genau dort lagen
sechs von sieben dokumentierten Fehlern.

Dieser Resolver schliesst die Luecke. Er nimmt eine Ground-Truth-Datei
(fixtures/ground-truth/*.json) — einen Primaertext, den niemand aus dem
Ergebnis abgeleitet hat — und prueft, ob jede Fundstelle im Bestand
woertlich wiederzufinden ist.

Der Befund ist dreiwertig, nie zweiwertig:

    verifiziert    Kennung UND Woertlaut im Bestand aufgeloest.
    abweichend     Kennung da, Woertlaut nicht — der gefaehrliche Fall.
                   So sah der Zellversatz aus: Kennung stimmte, Text war der
                   der Nachbarzeile.
    unverifiziert  Nicht aufloesbar. Kein Fehlerurteil, sondern ein
                   Statuseingestaendnis: geprueft wurde es nicht.

"Unverifiziert" ist ausdruecklich erlaubt. Was nicht erlaubt ist, ist ein
ungeprueftes Ergebnis, das wie ein geprueftes aussieht.

Nutzung
-------
    python fundstellen.py --bestand output/muster-norm-zweispaltig.md
    python fundstellen.py --bestand export/iso27001-2022.json --strict
    python fundstellen.py --ground-truth fixtures/ground-truth --bestand output/ --json
"""
from __future__ import annotations

import difflib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import click

GT_STANDARD = Path("fixtures/ground-truth")

# Zeichen, die beim Setzen und beim Extrahieren wandern, ohne dass sich der
# Woertlaut aendert. Wer sie nicht angleicht, meldet Abweichungen, die keine
# sind — und wer zu viel angleicht (Kleinschreibung, Satzzeichen weg), meldet
# Uebereinstimmungen, die keine sind. Die Liste bleibt deshalb kurz.
ERSETZUNGEN = {
    "­": "",           # weiches Trennzeichen
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-",
    # Alle Anfuehrungszeichen auf dieselbe Form. Der Extrakt gibt „Wort" teils
    # als 'Wort' wieder — Typografie, kein Woertlaut. Wer das als Abweichung
    # meldet, verschuettet die echten Befunde unter Formalien.
    "‘": '"', "’": '"', "‚": '"', "'": '"',
    "“": '"', "”": '"', "„": '"', "»": '"', "«": '"',
    "‹": '"', "›": '"',
    " ": " ", " ": " ", " ": " ", " ": " ",
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl",
}


def normalisiere(text: str) -> str:
    """Vergleichsform: Unicode vereinheitlicht, Umbrueche zu Leerzeichen.

    Gross-/Kleinschreibung und Satzzeichen bleiben erhalten. Ein Resolver, der
    beides wegwirft, findet fast alles wieder und belegt fast nichts.
    """
    t = unicodedata.normalize("NFKC", text)
    for alt, neu in ERSETZUNGEN.items():
        t = t.replace(alt, neu)
    # Trennung am Zeilenende zusammenziehen: "Informations-\nsicherheit".
    t = re.sub(r"-\s*\n\s*", "", t)
    return re.sub(r"\s+", " ", t).strip()



# Wie viele Woerter den Ankerpunkt bilden. Kurz genug, um in einem knappen
# Absatz zu stehen, lang genug, um nicht zufaellig mehrfach vorzukommen.
ANKER = 6

# Wie viele Fundstellen des Ankers geprueft werden, bevor aufgegeben wird.
# Mehr als eine Handvoll ist Rechenzeit ohne Erkenntnis.
MAX_ANKER = 8


def wortfolge(text: str) -> list[str]:
    return text.split()


def _fehlende_woerter(s_woerter: list[str], fenster: str) -> tuple[int, list[str]]:
    sm = difflib.SequenceMatcher(None, s_woerter, wortfolge(fenster), autojunk=False)
    fehlend: list[str] = []
    einschuebe = 0
    for tag, a1, a2, _b1, _b2 in sm.get_opcodes():
        if tag == "insert":
            einschuebe += 1
        elif tag in ("delete", "replace"):
            fehlend += s_woerter[a1:a2]
    return einschuebe, fehlend


def enthalten_mit_einschueben(soll: str, voll: str) -> tuple[bool, int, list[str]]:
    """Steht der Woertlaut vollstaendig und in Reihenfolge im Bestand?

    Rueckgabe: (vollstaendig, Zahl der Einschuebe, fehlende Woerter).

    Warum nicht schlicht `soll in voll`: der Extrakt eines PDF traegt Material,
    das im Primaertext nicht vorkommt und mitten im Absatz steht — Seitenkopf,
    Fusszeile, ein eingeschobener Verweis ("Nichtamtliches Inhaltsverzeichnis").
    Der Extrakt gibt die Quelle damit korrekt wieder; die Ground Truth kennt
    diese Zutaten nur nicht.

    Was hier deshalb erlaubt ist: Einschuebe im Bestand. Was nicht erlaubt ist:
    ein Wort des Primaertexts, das fehlt oder ersetzt wurde. Genau diese
    Unterscheidung trennt Layoutrauschen von einer anderen Fassung.

    Geprueft werden ALLE Stellen, an denen der Anker vorkommt, und die beste
    gewinnt. Der erste Treffer ist naemlich regelmaessig der falsche: ein
    Gesetzesdruck fuehrt vorn ein Inhaltsverzeichnis mit denselben
    Ueberschriften. Wer dort stehenbleibt, meldet Woerter als fehlend, die
    zwanzig Seiten weiter unten stehen — so entstanden hier 13 Fehlalarme.
    """
    s_woerter = wortfolge(soll)
    if not s_woerter:
        return True, 0, []

    spanne = 3 * len(soll) + 2000
    anker = " ".join(s_woerter[:ANKER])
    stellen = [m.start() for m in re.finditer(re.escape(anker), voll)][:MAX_ANKER]
    if not stellen:
        ende_anker = " ".join(s_woerter[-ANKER:])
        stellen = [max(0, m.start() - spanne)
                   for m in re.finditer(re.escape(ende_anker), voll)][:MAX_ANKER]
    if not stellen:
        return False, 0, s_woerter[:ANKER]

    bestes: tuple[int, list[str]] | None = None
    for start in stellen:
        einschuebe, fehlend = _fehlende_woerter(s_woerter, voll[start:start + spanne])
        if bestes is None or len(fehlend) < len(bestes[1]):
            bestes = (einschuebe, fehlend)
        if not fehlend:
            break
    einschuebe, fehlend = bestes or (0, s_woerter)
    return (not fehlend), einschuebe, fehlend


@dataclass
class Befund:
    kennung: str
    art: str
    status: str            # verifiziert | abweichend | unverifiziert
    grund: str = ""
    quelle: str = ""
    fundort: str = ""


@dataclass
class Bericht:
    ground_truth: str
    bestand: str
    befunde: list[Befund] = field(default_factory=list)

    def zahl(self, status: str) -> int:
        return sum(1 for b in self.befunde if b.status == status)

    @property
    def quote(self) -> float:
        """Anteil verifizierter Fundstellen. Ohne Fundstellen keine Quote."""
        return round(100.0 * self.zahl("verifiziert") / len(self.befunde), 1) if self.befunde else 0.0


def bestandstext(pfad: Path) -> tuple[str, dict[str, str]]:
    """Liefert (Volltext, Kennung -> Text) fuer Markdown-Extrakt oder Export-JSON."""
    roh = pfad.read_text(encoding="utf-8")
    # Die <!-- page: N --> Marken und der ACSOS-Hinweis stammen von uns, nicht
    # aus der Quelle. Sie stehen mitten im Satz und wuerden jeden Absatz, den
    # sie durchschneiden, als Abweichung erscheinen lassen.
    roh = re.sub(r"<!--.*?-->", " ", roh, flags=re.S)
    if pfad.suffix.lower() == ".json":
        daten = json.loads(roh)
        if isinstance(daten, dict) and "requirements" in daten:
            je_kennung = {str(r.get("id", "")): " ".join(
                str(r.get(f, "")) for f in ("title", "text")) for r in daten["requirements"]}
            return normalisiere(" ".join(je_kennung.values())), {
                k: normalisiere(v) for k, v in je_kennung.items()}
        return normalisiere(roh), {}
    return normalisiere(roh), {}


def pruefe_fundstelle(f: dict, voll: str, je_kennung: dict[str, str], quelle: str) -> Befund:
    kennung = str(f.get("id", "")).strip()
    art = f.get("art", "")
    soll_text = normalisiere(str(f.get("text", "")))
    soll_titel = normalisiere(str(f.get("titel", "")))

    # Der Export ordnet Text einer Kennung zu — dann wird genau dort geprueft,
    # nicht irgendwo im Dokument. Sonst deckte der Nachbarabschnitt den Versatz.
    if je_kennung:
        if kennung not in je_kennung:
            return Befund(kennung, art, "unverifiziert",
                          "Kennung im Bestand nicht vorhanden", quelle)
        eintrag = je_kennung[kennung]
        if soll_text and soll_text not in eintrag:
            return Befund(kennung, art, "abweichend",
                          "Kennung vorhanden, Woertlaut des Primaertexts steht nicht darunter",
                          quelle, f"id={kennung}")
        if not soll_text and soll_titel and soll_titel not in eintrag:
            return Befund(kennung, art, "abweichend",
                          "Titel weicht vom Primaertext ab", quelle, f"id={kennung}")
        return Befund(kennung, art, "verifiziert", "", quelle, f"id={kennung}")

    # Freier Text (Markdown-Extrakt): Kennung und Woertlaut muessen beide da
    # sein, und der Woertlaut muss vollstaendig sein.
    if kennung and normalisiere(kennung) not in voll:
        return Befund(kennung, art, "unverifiziert", "Kennung im Extrakt nicht gefunden", quelle)
    if soll_titel and soll_titel not in voll:
        return Befund(kennung, art, "abweichend", "Titel nicht woertlich im Extrakt", quelle)

    # Fuehrt die Ground Truth Absaetze, wird je Absatz geprueft. Ein ganzer
    # Paragraf steht im Extrakt fast nie zusammenhaengend: Seitenmarken, Kopf-
    # und Fusszeilen liegen dazwischen. Wer trotzdem am Stueck vergleicht,
    # meldet jeden laengeren Paragrafen als Abweichung -- und nach dem dritten
    # Fehlalarm liest niemand mehr hin.
    absaetze = [normalisiere(a) for a in f.get("absaetze", []) if normalisiere(a)]
    if absaetze:
        offen: list[tuple[str, list[str]]] = []
        einschuebe = 0
        for a in absaetze:
            if a in voll:
                continue
            ok, n, fehlt = enthalten_mit_einschueben(a, voll)
            einschuebe += n
            if not ok:
                offen.append((a, fehlt))
        ort = f"{kennung} ({len(absaetze)} Absaetze)"
        if offen:
            a, fehlt = offen[0]
            return Befund(kennung, art, "abweichend",
                          f"{len(offen)} von {len(absaetze)} Absaetzen weichen ab; "
                          f"im ersten fehlen {len(fehlt)} Woerter: "
                          f"\u201e{' '.join(fehlt)[:110]}\u201c "
                          f"(Absatzanfang: \u201e{a[:60]}...\u201c)",
                          quelle, ort)
        grund = (f"vollstaendig, im Extrakt durch {einschuebe} Einschub/Einschuebe getrennt"
                 if einschuebe else "")
        return Befund(kennung, art, "verifiziert", grund, quelle, ort)

    if soll_text and soll_text not in voll:
        return Befund(kennung, art, "abweichend", "Woertlaut nicht vollstaendig im Extrakt", quelle)
    if not soll_text and not soll_titel:
        return Befund(kennung, art, "unverifiziert", "Ground Truth nennt keinen Woertlaut", quelle)
    return Befund(kennung, art, "verifiziert", "", quelle)


def loese_auf(gt: dict, bestand: Path) -> Bericht:
    voll, je_kennung = bestandstext(bestand)
    b = Bericht(gt.get("kurzname", gt.get("quelle", "?")), str(bestand))
    for f in gt.get("fundstellen", []):
        b.befunde.append(pruefe_fundstelle(f, voll, je_kennung, b.ground_truth))
    return b


def gt_dateien(pfad: Path) -> list[Path]:
    return sorted(pfad.glob("*.json")) if pfad.is_dir() else [pfad]


# Begleitdateien der Extraktion, die keinen fortlaufenden Normtext enthalten.
# Auch *.docling.json bleibt draussen: dort steht derselbe Text, aber in
# Einzelelemente zerlegt und JSON-escaped. Ein Satz, der ueber zwei Elemente
# laeuft, waere dort nie woertlich zu finden -- der Resolver meldete eine
# Abweichung, die keine ist. Als Kandidat
# wuerden sie die Zuordnung verwaessern und im Zweifel als "einzige Datei"
# durchgehen -- ein Bericht ueber das Manifest saehe aus wie einer ueber den Text.
KEINE_BESTANDSDATEI = {"manifest.json", "korpus.json"}


def bestand_dateien(pfad: Path) -> list[Path]:
    if pfad.is_dir():
        return sorted(p for p in [*pfad.glob("*.md"), *pfad.glob("*.json")]
                      if p.name not in KEINE_BESTANDSDATEI
                      and not p.name.endswith(".docling.json"))
    return [pfad]


def passend(gt: dict, kandidaten: list[Path]) -> list[Path]:
    """Bestandsdateien, die zu dieser Ground Truth gehoeren.

    Die Zuordnung steht in der Ground Truth selbst (`bestand_muster`), nicht in
    einer Regel. Der erste Anlauf riet ueber den Wortstamm des Kurznamens: aus
    "bsi-kritisv" wurde "bsi", und der Resolver pruefte die Verordnung gegen
    "bsi-benutzerdefinierte-bausteine.md" — ein voellig fremdes Dokument, 22
    Fundstellen "unverifiziert", der Befund wertlos.

    Ohne Muster wird der vollstaendige Kurzname verlangt. Findet sich nichts,
    wird nichts geprueft, und genau das steht im Bericht: ein leerer Lauf darf
    nicht gruen aussehen.
    """
    muster = [str(m).lower() for m in gt.get("bestand_muster", [])]
    if not muster:
        kurz = str(gt.get("kurzname", "")).lower()
        muster = [kurz] if kurz else []
    return [k for k in kandidaten if any(m in k.name.lower() for m in muster)]


@click.command()
@click.option("--ground-truth", "gt_pfad", type=click.Path(path_type=Path),
              default=GT_STANDARD, show_default=True,
              help="Datei oder Ordner mit Primaertexten.")
@click.option("--bestand", type=click.Path(exists=True, path_type=Path), required=True,
              help="Extrakt (.md), Export (.json) oder ein Ordner davon.")
@click.option("--json", "als_json", is_flag=True, help="Maschinenlesbarer Bericht.")
@click.option("--strict", is_flag=True,
              help="Exit 1, sobald eine Fundstelle abweicht oder unverifiziert bleibt.")
def main(gt_pfad: Path, bestand: Path, als_json: bool, strict: bool) -> None:
    """Prueft Fundstellen gegen den Primaertext, nicht gegen sich selbst."""
    if not gt_pfad.exists():
        raise SystemExit(f"Ground Truth fehlt: {gt_pfad}")
    kandidaten = bestand_dateien(bestand)
    berichte: list[Bericht] = []
    ohne_bestand: list[str] = []

    for datei in gt_dateien(gt_pfad):
        gt = json.loads(datei.read_text(encoding="utf-8"))
        ziele = passend(gt, kandidaten)
        if not ziele:
            ohne_bestand.append(gt.get("kurzname", datei.name))
            continue
        for ziel in ziele:
            berichte.append(loese_auf(gt, ziel))

    if als_json:
        print(json.dumps({
            "berichte": [{"ground_truth": b.ground_truth, "bestand": b.bestand,
                          "quote": b.quote,
                          "befunde": [vars(x) for x in b.befunde]} for b in berichte],
            "ohne_bestand": ohne_bestand,
        }, ensure_ascii=False, indent=2))
    else:
        for b in berichte:
            print(f"\n{b.ground_truth} gegen {b.bestand}")
            print(f"  {b.zahl('verifiziert')} verifiziert, {b.zahl('abweichend')} abweichend, "
                  f"{b.zahl('unverifiziert')} unverifiziert — Quote {b.quote} %")
            for x in b.befunde:
                if x.status != "verifiziert":
                    print(f"  [{x.status}] {x.kennung or '(ohne Kennung)'}: {x.grund}")
        for k in ohne_bestand:
            print(f"\n[unverifiziert] {k}: keine Bestandsdatei zugeordnet — nicht geprueft.")

    offen = sum(b.zahl("abweichend") + b.zahl("unverifiziert") for b in berichte) + len(ohne_bestand)
    if strict and offen:
        sys.exit(1)


if __name__ == "__main__":
    main()
