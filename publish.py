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

import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import click
import yaml

LICENSED_DIR = "Normen (lizenziert)"


@dataclass
class Section:
    ident: str
    title: str
    text: str
    page: int
    # Belegstelle fuer Quellen ohne Seiten (maschinenlesbare Kataloge):
    # der Schluesselpfad, unter dem die Anforderung in der Datei steht.
    locator: str = ""


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


def norm_key(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().casefold()


def sections_from_headings(body: str) -> dict[str, Section]:
    """Nummerierte Abschnitte (4.1, 6.1.2 ...) aus den Docling-Ueberschriften."""
    out: dict[str, Section] = {}
    # Zwei Bauformen von Kennungen, und die zweite fehlte lange: numerische
    # ("4.1", "Artikel 32", "Annex A.8.24") und solche mit Buchstabenpraefix
    # ("APP.1.1.A1", "SYS.2.2.3.A5", "ORP.4.A9"), wie der BSI-Grundschutz sie
    # fuehrt. Ohne den zweiten Zweig wurde im Kompendium keine einzige
    # Ueberschrift erkannt; die Aufloesung fiel auf den Textanker zurueck, und
    # der findet kein Ende -- jede Anforderung schleppte den Rest des Dokuments
    # mit. Im Export waren das im Median 54019 Zeichen je Anforderung statt der
    # ueblichen paar hundert.
    kopfzeilen = list(re.finditer(
        r"^(#{1,6})\s+((?:Artikel|Article|Art\.?|Anhang|Annex)?\s*"
        # Der Buchstabenzweig steht VOR dem roemischen, und das ist keine
        # Kosmetik: "INF" beginnt mit "I", und "I" liegt in [0-9IVX]. Stuende
        # der roemische Zweig vorn, matchte er das blosse "I", brichts dort ab
        # und liefert die Kennung "I" statt "INF.1.A1". Betroffen waren INF,
        # IND und ISMS -- 49 Anforderungen, die dadurch ihre Abschnittsgrenze
        # verloren und den Rest des Dokuments mitschleppten.
        r"(?:[A-Z]{2,6}(?:\.[0-9]+)+(?:\.A[0-9]+)?"
        # Wortgrenze nach der Kennung: "## OPS.2.3A22 ..." (Druckfehler im
        # Kompendium) ist keine Ueberschrift der Gruppe OPS.2.3 -- sonst trug
        # der Baustein den Text der Anforderung A22.
        r"|[0-9IVX]+(?:[.\-][0-9A-Za-z]+)*)(?![A-Za-z0-9]))\s*[—–-]?\s*(.*)$", body, flags=re.M))
    # Strukturgrenzen: Ueberschriften ohne Kennung, die trotzdem einen
    # Abschnitt beenden -- Anhang, Kapitel, Abschnitt, Literatur und alles in
    # Versalien (KAPITEL IV, ALLGEMEINE BESTIMMUNGEN). Ohne sie lief ISO 42001
    # Klausel 10.2 bis ans Dokumentende und enthielt den ganzen Anhang A.
    # "## Control" oder "## Implementation guidance" sind KEINE Grenzen: sie
    # gliedern den Text einer Anforderung, sie beenden ihn nicht.
    grenzen = list(re.finditer(
        r"^#{1,6}\s+(?:(?:Annex|Anhang|Appendix|KAPITEL|Kapitel|CHAPTER|Chapter|TITEL|"
        r"ABSCHNITT|Abschnitt|Section|Bibliography|Literatur(?:verzeichnis)?|References)\b.*"
        r"|[A-ZÄÖÜ][A-ZÄÖÜ0-9 ,\-/()]{3,})\s*$", body, flags=re.M))
    # Amtsblattsatz: "Artikel 22" steht mal als Ueberschrift, mal als blosse
    # Zeile -- das Layoutmodell entscheidet das je Seite anders. Eine Zeile,
    # die nur aus der Artikelnummer besteht, ist eine Artikelgrenze, egal wie
    # sie ausgezeichnet ist. Ohne diese Regel trug Art.21 der DSGVO den Text
    # von Art.22 und Art.23 mit: volle Wortdeckung, falscher Inhalt.
    nackte = list(re.finditer(
        r"^((?:Artikel|Article|Art\.)\s+[0-9]+[a-z]?)\s*$", body, flags=re.M))
    heads = sorted(
        [(m.start(), m.end(), m.group(2), m.group(3)) for m in kopfzeilen]
        + [(m.start(), m.end(), m.group(1), "") for m in nackte]
        + [(m.start(), m.end(), None, "") for m in grenzen])
    for i, (h_start, h_end, roh_ident, titel) in enumerate(heads):
        if roh_ident is None:       # reine Strukturgrenze, kein Abschnitt
            continue
        end = heads[i + 1][0] if i + 1 < len(heads) else len(body)
        text = body[h_end:end]
        text = re.sub(r"<!--\s*page:\s*\d+\s*-->", "", text).strip()
        ident = norm_key(roh_ident)
        if ident in out:            # Wiederholte Kopfzeile o. ae.: laengeren Text behalten
            if len(text) <= len(out[ident].text):
                continue
        out[ident] = Section(ident, titel, text, page_at(body, h_start))

    # Oberklauseln ohne eigenen Text (z. B. 9.2, wenn alles in 9.2.1 und 9.2.2
    # steht) aus ihren Unterklauseln zusammensetzen, statt sie leer zu lassen.
    for ident, sec in list(out.items()):
        if sec.text.strip():
            continue
        kids = sorted(k for k in out if k.startswith(ident + ".") and out[k].text.strip())
        if not kids:
            continue
        parts = [f"### {k} {out[k].title}\n\n{out[k].text}".rstrip() for k in kids]
        out[ident] = Section(ident, sec.title, "\n\n".join(parts), sec.page or out[kids[0]].page)
    return out


def _yaml_block(body: str) -> str | None:
    """Der woertlich uebernommene YAML-Block eines Passthrough-Extrakts."""
    m = re.search(r"^```yaml\n(.*?)\n```", body, flags=re.S | re.M)
    return m.group(1) if m else None


def _c5_text(entry: dict) -> str:
    """Normativer Text eines C5-Eintrags, Hinweise davon getrennt.

    'criterion' bzw. 'condition' ist die Anforderung, 'hint' die Auslegungshilfe
    des BSI. Beides steht in der Notiz, aber erkennbar getrennt — sonst liest ein
    Agent den Hinweis als Anforderung.
    """
    parts = []
    for key in ("criterion", "condition"):
        v = entry.get(key)
        if isinstance(v, str) and v.strip():
            parts.append(v.strip())
    hint = entry.get("hint")
    if isinstance(hint, str) and hint.strip():
        parts.append("> [!info] Hinweis der Quelle\n"
                     + "\n".join("> " + z for z in hint.strip().splitlines()))
    return "\n\n".join(parts)


def yaml_catalogue_group(body: str, meta: dict[str, str]) -> str | None:
    """Kriterienbereich, den dieser Extrakt vollstaendig abdeckt — oder None.

    Nur bei einem maschinenlesbaren Katalog ist Abwesenheit einer ID eine
    Aussage: die Datei enthaelt den Bereich ganz. Aus einem PDF laesst sich das
    nicht schliessen, dort heisst eine fehlende ID meist, dass die Extraktion
    sie nicht gefunden hat.
    """
    if not sections_from_yaml(body, meta):
        return None
    group = Path(meta.get("source_file", "")).stem.upper()
    return group if re.fullmatch(r"[A-Z]{2,4}", group) else None


def sections_from_yaml(body: str, meta: dict[str, str]) -> dict[str, Section]:
    """Anforderungen aus einem maschinenlesbaren Katalog (BSI C5 als YAML).

    Der Passthrough-Pfad von extract.py legt solche Dateien woertlich in einem
    Codeblock ab, weil Docling keinen YAML-Reader mitbringt. Fuer die Ablage im
    Vault wird der Block hier mit PyYAML gelesen — kein selbst geschriebener
    Parser, der Zeichenbestand bleibt der der Quelle.

    Zwei Formen kommen vor:
      * flach          - [{id: 'GC-01', name, condition, hint}]
      * verschachtelt  - [{identifier: '01', name,
                           basic|additional_sharpen|additional_complement:
                             [{identifier: '01B', criterion}]}]
    Die Vault-IDs entstehen aus dem Dateinamen als Gruppe: GC-01, AM-01,
    AM-01.01B. Erfunden wird dabei nichts — Gruppe und Nummer stehen in der
    Quelle, nur zusammengesetzt werden sie hier.
    """
    block = _yaml_block(body)
    if block is None:
        return {}
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError:
        return {}                      # kein Katalog: die anderen Pfade greifen
    if not isinstance(data, list) or not data or not isinstance(data[0], dict):
        return {}

    src = meta.get("source_file", "")
    group = Path(src).stem.upper()
    if not re.fullmatch(r"[A-Z]{2,4}", group):
        return {}                      # kein Kriterienbereich (z. B. Version-und-Lizenz)

    out: dict[str, Section] = {}

    def add(ident: str, title: str, text: str, path: str) -> None:
        if text.strip():
            out[norm_key(ident)] = Section(ident, title, text, 0, f"{path} in {src}")

    for entry in data:
        if not isinstance(entry, dict):
            continue
        name = str(entry.get("name") or "").strip()

        flat_id = entry.get("id")
        if isinstance(flat_id, str) and flat_id.strip():
            ident = flat_id.strip()
            add(ident, name, _c5_text(entry), ident)
            continue

        crit = entry.get("identifier")
        if not isinstance(crit, str) or not crit.strip():
            continue
        crit_id = f"{group}-{crit.strip()}"

        for key in ("basic", "additional_sharpen", "additional_complement"):
            subs = entry.get(key)
            if not isinstance(subs, list):
                continue
            for sub in subs:
                if not isinstance(sub, dict):
                    continue
                sub_id = sub.get("identifier")
                if not isinstance(sub_id, str) or not sub_id.strip():
                    continue
                ident = f"{crit_id}.{sub_id.strip()}"
                add(ident, name, _c5_text(sub), f"{key}/{sub_id.strip()}")

        # Der Kriterienbereich selbst traegt keine eigene Anforderung, aber oft
        # erlaeuternde Informationen. Die gehoeren in seine Notiz; fehlen sie,
        # setzt main() ihn aus seinen Unterkriterien zusammen.
        infos = entry.get("information")
        texts = [str(i.get("information_text")).strip()
                 for i in infos if isinstance(i, dict) and i.get("information_text")] \
            if isinstance(infos, list) else []
        if texts:
            add(crit_id, name, "\n\n".join(texts), f"{crit.strip()}/information")

    return out


KENNUNG_IN_ZELLE = re.compile(r"^(A\.)?([0-9A-Z]+(?:[.\-][0-9A-Za-z]+)+)$")


def zeilen_kennung(zellen: list[str]) -> tuple[int, str] | None:
    """Position und Wert der Anforderungskennung in einer Tabellenzeile.

    Frueher wurde nur die erste Spalte betrachtet. Das traegt, solange die
    Tabelle mit der Kennung beginnt — die VDA-ISA tut das nicht: dort stehen
    davor eine leere Spalte und eine Referenzspalte, die in der Quelldatei
    #REF! enthaelt (ein kaputter Formelverweis der Arbeitsmappe selbst). Die
    Kennung sitzt in der vierten Zelle, der Kriterientext in der neunten bis
    zwoelften. Ohne diese Suche fiel das gesamte TISAX-Kapitel 8
    (Prototypenschutz, 23 Kriterien) auf Tabellenfuellzeichen zurueck: befuellt,
    aber ohne Inhalt — und damit schlimmer als leer, weil es wie Text aussieht.

    Gesucht wird nur in den ersten Zellen: weiter hinten stehen Datumsangaben
    und Versionsnummern, die wie Kennungen aussehen.
    """
    for i, z in enumerate(zellen[:4]):
        m = KENNUNG_IN_ZELLE.match(z)
        if m:
            # Die Kennung bleibt, wie sie in der Zelle steht. Frueher fiel das
            # "A." weg, und die Zeile A.5.1 (Policies) landete auch unter "5.1"
            # -- der Nummer der Klausel Leadership. 32 Anforderungen in zwei
            # ISO-Exporten trugen so den Text einer anderen Nummer.
            return i, m.group(0)
    return None


def zellmarke(texte: list[str]) -> str | None:
    """Das Wort, mit dem die Textzellen dieser Tabelle regulaer beginnen.

    ISO 27001 Anhang A leitet jede Control-Zelle mit "Control" ein. Wo eine
    Zelle nicht damit beginnt, ist ihr Anfang der Schwanz der vorigen Zeile:
    das Layoutmodell hat eine mehrzeilige Zelle an der Zeilengrenze getrennt.
    Die Marke wird nicht fest verdrahtet, sondern aus der Tabelle selbst
    gelesen -- beginnt die Mehrheit der Zellen mit demselben Wort, ist es die
    Marke; sonst gibt es keine, und es wird nichts verschoben.
    """
    erste = [t.split(None, 1)[0] for t in texte if t.split()]
    if len(erste) < 5:
        return None
    haeufig = Counter(erste).most_common(1)[0]
    return haeufig[0] if haeufig[1] >= 0.6 * len(erste) else None


def repariere_zellversatz(zeilen: list[tuple[str, str, str, int]]
                          ) -> list[tuple[str, str, str, int]]:
    """Text, der vor der Zellmarke steht, der vorigen Anforderung zurueckgeben.

    Beobachtet in ISO/IEC 27001 Anhang A: A.5.16 trug nur "Control", waehrend
    der zugehoerige Satz ("The full life cycle of identities shall be managed.")
    am Anfang der Zelle von A.5.17 stand -- und deren eigener Text erst
    dahinter. Neun von 94 Zeilen waren so verschoben. Laengen und Kennungen
    bleiben dabei unauffaellig; auffallen kann es nur, wer den Wortlaut gegen
    die Nummer haelt. Genau das ist der teuerste Fehler in einem
    Compliance-Bestand: eine Anforderung, die etwas anderes sagt, als ihre
    Nummer verspricht.

    Verschoben wird ausschliesslich der Teil vor der Marke, und nur, wenn es
    eine vorige Zeile gibt, an die er anschliesst. Verworfen wird nichts.
    """
    marke = zellmarke([z[2] for z in zeilen])
    if not marke:
        return zeilen
    ergebnis = [list(z) for z in zeilen]
    for i, (_, _, text, _) in enumerate(zeilen):
        if not text or text.startswith(marke) or marke not in text:
            continue
        kopf, _, rest = text.partition(marke)
        kopf = kopf.strip()
        if not kopf or i == 0:
            continue
        ergebnis[i][2] = (marke + rest).strip()
        vorher = ergebnis[i - 1][2]
        ergebnis[i - 1][2] = f"{vorher} {kopf}".strip() if vorher else kopf
    return [tuple(z) for z in ergebnis]


def sections_from_tables(body: str) -> dict[str, Section]:
    """Control-Tabellen (Anhang A): jede Zeile ist eine Anforderung."""
    zeilen: list[tuple[str, str, str, int]] = []
    for zeile in re.finditer(r"^\|(.+)\|\s*$", body, flags=re.M):
        roh = [c.strip() for c in zeile.group(1).split("|")]
        gefunden = zeilen_kennung([c for c in roh if c] or roh)
        if not gefunden:
            continue
        nicht_leer = [c for c in roh if c]
        pos, raw = gefunden
        rest = nicht_leer[pos + 1:]
        if not rest:
            continue
        text = "\n\n".join(rest[1:]) if len(rest) > 1 else ""
        zeilen.append((raw, rest[0], text, zeile.start()))

    out: dict[str, Section] = {}
    for raw, title, text, start in repariere_zellversatz(zeilen):
        # Ohne Praefix in der Zelle (Anhang-Tabellen, die "5.1" statt "A.5.1"
        # schreiben) auch unter der A.-Form ablegen; nie umgekehrt.
        schluessel = {norm_key(raw)}
        if not raw.upper().startswith("A."):
            schluessel.add(norm_key(f"A.{raw}"))
        for ident in schluessel:
            prev = out.get(ident)
            if prev and len(prev.text) >= len(text):
                continue
            out[ident] = Section(raw, title, text, page_at(body, start))
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
    # Steht der Treffer in einer Tabellenzeile, ist es eine Uebersicht
    # (Reifegradtabelle, Inhaltsverzeichnis), nicht der Abschnitt: TISAX-Gruppe
    # "1" trug so die Zeilen der Gruppen 2 bis 8 als Text.
    if body[body.rfind("\n", 0, anchor.start()) + 1:].lstrip().startswith("|"):
        return None
    rest = body[anchor.end():]
    nxt = re.search(r"(?m)^#{1,6}\s+[0-9]+(?:\.[0-9]+)*\s|(?<![\d.])[0-9]+\.[0-9]+\s+[A-Z]", rest)
    text = rest[: nxt.start()] if nxt else rest[:4000]
    text = re.sub(r"<!--\s*page:\s*\d+\s*-->", "", text).strip()
    return Section(ident, title, text, page_at(body, anchor.start())) if text else None


def id_variants(ident: str) -> list[str]:
    """Schreibweisen, unter denen eine Anforderungs-ID im Dokument stehen kann.

    Die Vault-IDs folgen je Framework eigenen Konventionen (Art.32, AnnexI.1.1,
    PO.1.1, APP.1.1.A1, 5.1). Hier werden daraus die Formen erzeugt, die in
    Ueberschriften oder in der ersten Tabellenspalte tatsaechlich auftauchen.
    """
    v = [ident]
    m = re.match(r"^Art\.?\s*([0-9]+)(?:\.([0-9]+))?$", ident, flags=re.I)
    if m:
        num = m.group(1)
        v += [f"Artikel {num}", f"Art. {num}", f"Art.{num}", f"Article {num}", num]
    m = re.match(r"^Annex([IVX]+)\.(.+)$", ident, flags=re.I)
    if m:
        v += [f"Anhang {m.group(1)} {m.group(2)}", f"Annex {m.group(1)} {m.group(2)}", m.group(2)]
    if "." in ident:
        v.append(ident.replace(".", " "))
    v.append(ident.removeprefix("A."))
    seen, out = set(), []
    for x in v:
        k = x.strip().casefold()
        if k and k not in seen:
            seen.add(k)
            out.append(x.strip())
    return out


def paragraph_of(text: str, marker: str) -> str:
    """Absatz (N) oder Buchstabenpunkt a) aus einem Artikeltext herausloesen.
    Die Gliederung stammt aus dem Dokument selbst, es wird nichts umformuliert."""
    if marker.isdigit():
        nxt_marker = str(int(marker) + 1)
        pats = (rf"^[-*\s]*\({marker}\)\s*", rf"^[-*\s]*\({nxt_marker}\)")
    else:
        nxt_marker = chr(ord(marker) + 1)
        pats = (rf"^[-*\s]*{marker}\)\s*", rf"^[-*\s]*{nxt_marker}\)")
    marks = list(re.finditer(pats[0], text, flags=re.M))
    if not marks:
        return ""
    start = marks[0].start()
    nxt = re.search(pats[1], text[start:], flags=re.M)
    return text[start: start + nxt.start()].strip() if nxt else text[start:].strip()


def sections_by_anchor(body: str, wanted: dict[str, str]) -> dict[str, Section]:
    """Anforderungen finden, die als ID am Zeilen-, Listen- oder Zellanfang
    stehen — etwa "GV.OC-01: ...", "- o PO.1.1: ..." oder "| ASI01: ... |".

    Der Abschnitt reicht bis zum naechsten so verankerten Treffer oder zur
    naechsten Ueberschrift. Es wird nur uebernommen, was im Dokument steht.
    """
    hits: list[tuple[int, int, str, str]] = []   # (start, textstart, id, variante)
    for ident in wanted:
        for variant in id_variants(ident):
            if len(variant) < 3 or variant.isdigit():
                continue                      # zu unspezifisch fuer einen Anker
            # Anker: Zeilenanfang, Listenpunkt oder Zellgrenze einer Tabelle —
            # in Norm-Tabellen steht die ID oft mitten in der Zeile hinter "|".
            # Nach der ID: Trennzeichen, Zeilenende oder ein Grossbuchstabe.
            # "Artikel 45 der Verordnung (EU) Nr. 909/2014 wird wie folgt
            # geaendert" ist ein Verweis in einem Aenderungsartikel, kein
            # Anker -- DORA Art.45 trug so den Text von Art.61.
            pat = re.compile(
                rf"(?:^|\|)[-*>\s]*(?:o\s+)?({re.escape(variant)})"
                rf"(?:\s*[:.)\]|–—-]|\s+(?=[A-ZÄÖÜ0-9(§])|\s*$)\s*",
                flags=re.M)
            for m in pat.finditer(body):
                hits.append((m.start(), m.end(), ident, variant))
    if not hits:
        return {}

    bounds = sorted({h[0] for h in hits})
    heads = [m.start() for m in re.finditer(r"^#{1,6}\s", body, flags=re.M)]
    out: dict[str, Section] = {}
    for start, tstart, ident, variant in sorted(hits):
        later = sorted([b for b in bounds if b > start] + [h for h in heads if h > start])
        end = later[0] if later else min(start + 4000, len(body))
        text = re.sub(r"<!--\s*page:\s*\d+\s*-->", "", body[tstart:end]).strip()

        # Steht die ID allein und der Titel folgt erst als eigene Ueberschrift
        # (so setzt der EU-Amtsblattsatz Artikelnummer und Artikelueberschrift),
        # gehoert der Abschnitt hinter dieser Ueberschrift dazu.
        if len(text) < 40 and end in heads and len(later) > 1:
            end = later[1]
            text = re.sub(r"<!--\s*page:\s*\d+\s*-->", "", body[tstart:end]).strip()
        if len(text) < 15:
            continue
        prev = out.get(ident)
        if prev and len(prev.text) >= len(text):
            continue
        title = wanted.get(ident) or ""
        out[ident] = Section(ident, title, text, page_at(body, start))
    return out


def load_crosswalk(framework: str) -> dict[str, str]:
    """Gepruefte Kreuzreferenz ID -> woertlicher Textanker, falls vorhanden.

    Noetig, wo die Nummerierung im Vault nicht der Reihenfolge des Dokuments
    folgt (CRA Anhang I). Die Datei liegt im Repository unter mappings/ und ist
    nachlesbar — eine Zuordnung nach Position waere hier schlicht falsch.
    """
    path = Path(__file__).parent / "mappings" / f"{framework}.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("anchors", {})


def section_at_anchor(body: str, ident: str, anchor: str, title: str) -> Section | None:
    """Abschnitt ab einem woertlichen Textstueck bis zum naechsten Listenpunkt."""
    # Der ganze Anker wird gesucht, nicht nur sein Anfang: im Amtsblattsatz
    # kommen Formulierungen wie "Produkte mit digitalen Elementen" hundertfach
    # vor, und ein zu kurzes Fenster trifft die falsche Stelle.
    words = re.sub(r"\s+", " ", anchor).split()
    m = re.search(r"\s+".join(re.escape(w) for w in words), body)
    if not m:
        return None
    line_start = body.rfind("\n", 0, m.start()) + 1
    rest = body[line_start:]
    nxt = re.search(r"(?m)^(?:-\s*(?:\([0-9]+\)|[a-z]\))|#{1,6}\s)", rest[1:])
    text = rest[: nxt.start() + 1] if nxt else rest[:3000]
    text = re.sub(r"<!--\s*page:\s*\d+\s*-->", "", text).strip()
    return Section(ident, title, text, page_at(body, line_start)) if text else None


def gruppe(ident: str) -> str:
    """Uebergeordnete Gliederungsebene einer Anforderungs-ID.

    A.5.1 -> A.5, APP.1.1.A1 -> APP.1.1, AM-01.01B -> AM-01, GC-01 -> GC.
    Abgeleitet aus der ID selbst, nicht geraten: die Konvention steckt in der
    Nummerierung des jeweiligen Frameworks.
    """
    if "." in ident:
        return ident.rsplit(".", 1)[0]
    if "-" in ident:
        return ident.split("-", 1)[0]
    return ""


def edition_aus_registry(slug: str) -> str | None:
    """Bezeichnung der Ausgabe aus versions.json — oder None.

    Erfunden wird nichts: steht das Dokument nicht in der Registry, bleibt das
    Feld leer, statt eine Ausgabe zu behaupten.
    """
    path = Path(__file__).parent / "versions.json"
    if not path.exists():
        return None
    eintrag = json.loads(path.read_text(encoding="utf-8")).get("documents", {}).get(slug)
    if not eintrag:
        return None
    titel, fassung = eintrag.get("titel", ""), eintrag.get("dokument_version", "")
    return f"{titel} {fassung}".strip() or None


def export_json(framework: str, slug: str, meta: dict[str, str],
                treffer: dict[str, Section], fehlend: list[str]) -> str:
    """Anforderungen als JSON, in der Form, die ein rechnendes System erwartet.

    Nicht aufgeloeste IDs stehen unter 'missing' statt mit leerem Text in
    'requirements': ein Verarbeiter soll eine Luecke als Luecke sehen und nicht
    als Anforderung ohne Wortlaut.
    """
    return json.dumps({
        "frameworkId": framework,
        "edition": edition_aus_registry(slug),
        "sourceFile": meta.get("source_file", ""),
        "sourceSha256": meta.get("source_sha256", ""),
        "requirements": [
            {"id": i, "title": treffer[i].title, "text": treffer[i].text,
             "group": gruppe(i)}
            for i in sorted(treffer)
        ],
        "missing": fehlend,
    }, ensure_ascii=False, indent=2) + "\n"


def abschnitte_zusammen(body: str, meta: dict[str, str]) -> dict[str, Section]:
    """Ueberschriften, Tabellenzeilen und YAML-Katalog zu einer Abschnittsliste.

    Eine Ueberschrift mit Text hat Vorrang. Tabellen und Katalog fuellen nur,
    was fehlt oder leer ist. Vorher galt update() in umgekehrter Richtung, und
    die Inhaltsverzeichnis-Tabelle ("| 10.1 | Continual improvement | 23 |")
    verdraengte das Kapitel 10.1 durch eine Zeile ohne Text.
    """
    found = sections_from_headings(body)
    for extra in (sections_from_tables(body), sections_from_yaml(body, meta)):
        for k, sec in extra.items():
            prev = found.get(k)
            if prev is None or not prev.text.strip():
                found[k] = sec
    return found


def aufgeloeste_abschnitte(body: str, meta: dict[str, str], wanted: dict[str, str],
                           framework: str) -> dict[str, Section]:
    """Je Anforderungs-ID den Abschnitt aus dem Extrakt — oder nichts.

    Die Reihenfolge der Versuche ist die Reihenfolge der Verlaesslichkeit:
    gepruefte Kreuzreferenz, Ueberschrift oder Tabellenzeile, Absatz aus einem
    Artikel, Textanker, Inline-Fund, zuletzt Zusammensetzung aus Unterpunkten.
    Was hier fehlt, steht nicht im Dokument — ergaenzt wird nichts.

    Herausgeloest aus main(), damit der JSON-Export dieselbe Aufloesung nutzt
    wie die Vault-Notizen und beide nicht auseinanderlaufen koennen.
    """
    found = abschnitte_zusammen(body, meta)
    anchored = sections_by_anchor(body, wanted)
    # Fuehrt das Dokument einen Anhang A mit eigener Nummerierung, sind "A.10"
    # und "10" zwei verschiedene Dinge: A.10 darf dann nicht auf Kapitel 10
    # zurueckfallen (ISO 42001: A.10 Third-party relationships vs 10 Improvement).
    hat_anhang_a = any(k.startswith("a.") for k in found)
    crosswalk = load_crosswalk(framework)
    out: dict[str, Section] = {}

    for ident in sorted(wanted):
        sec = None
        if ident in crosswalk:
            sec = section_at_anchor(body, ident, crosswalk[ident], wanted[ident])
            if sec:
                out[ident] = sec
                continue

        for variant in id_variants(ident):
            if hat_anhang_a and ident.startswith("A.") and variant == ident[2:]:
                continue
            sec = found.get(norm_key(variant))
            if sec and sec.text.strip():
                break
            sec = None

        # Absatz-IDs wie Art.20.1: Artikel holen, Absatz herausloesen.
        if sec is None:
            pm = re.match(r"^(.*)\.([0-9]+|[a-z])$", ident)
            if pm:
                for variant in id_variants(pm.group(1)):
                    parent = found.get(norm_key(variant)) or anchored.get(pm.group(1))
                    if parent and parent.text.strip():
                        para = paragraph_of(parent.text, pm.group(2))
                        if para:
                            sec = Section(ident, parent.title, para, parent.page)
                        break

        if sec is None or not sec.text.strip():
            sec = anchored.get(ident)
        if sec is None or not sec.text.strip():
            sec = inline_section(body, ident, wanted[ident])
        # Gruppen-IDs ohne eigenen Text (PO ueber PO.1.x, CIS-Kategorie 13 ueber
        # 13.1 ...) aus ihren Unterpunkten zusammensetzen. Eine Tabellenzeile,
        # die nur den Titel wiederholt ("A.10 | Third-party relationships"),
        # ist kein Text.
        if sec is None or not sec.text.strip() or norm_key(sec.text) == norm_key(sec.title or ""):
            kids = sorted(k for k in wanted
                          if k != ident and re.match(rf"^{re.escape(ident)}[.\-]", k))
            parts = []
            for k in kids:
                child = found.get(norm_key(k)) or anchored.get(k)
                if child and child.text.strip():
                    parts.append(f"### {k} {child.title}".rstrip() + f"\n\n{child.text}")
            if parts:
                first = found.get(norm_key(kids[0])) or anchored.get(kids[0])
                sec = Section(ident, wanted[ident], "\n\n".join(parts),
                              first.page if first else 0)

        if sec is None or not sec.text.strip():
            continue
        if not sec.title and wanted[ident]:
            sec = Section(ident, wanted[ident], sec.text, sec.page)
        out[ident] = sec

    return out


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


def vault_withdrawn(vault: Path, framework: str) -> set[str]:
    """IDs, die das Register selbst als withdrawn fuehrt.

    Sie bleiben Sollwert fuer den Export, wo das Dokument sie noch nennt (das
    Kompendium fuehrt 'ORP.1.A5 ENTFALLEN' als eigene Ueberschrift, und die
    Nummerierung bleibt so stabil). Fehlt eine solche ID aber im Dokument
    ganz (APP.2.2.A2 in der Edition 2023), ist das kein Verlust auf dem Weg
    in den Export — die Inhaltspruefung meldet sie deshalb getrennt.
    """
    folder = vault / "GRC" / "Frameworks" / framework
    if not folder.is_dir():
        return set()
    out: set[str] = set()
    for note in folder.glob("*.md"):
        meta, _ = split_front_matter(note.read_text(encoding="utf-8"))
        if meta.get("type") == "requirement" and meta.get("id") and (
                meta.get("kind") == "withdrawn" or meta.get("status") == "withdrawn"):
            out.add(meta["id"])
    return out


def yaml_wert(v: object) -> str:
    """Ein Wert als YAML-String, mit escapten Anfuehrungszeichen.

    Vorher stand diese Zeile dreimal als Lambda im Modul — und eine der drei
    Fassungen schrieb `.replace('"', '\\"')` ohne doppelten Backslash, ersetzte
    also ein Anfuehrungszeichen durch sich selbst. Ein Dateiname mit " haette
    dort das Front-Matter zerbrochen. Eine Fassung, eine Wahrheit.
    """
    return '"' + str(v).replace('"', '\\"') + '"'


def note_text(framework: str, ident: str, sec: Section, meta: dict[str, str]) -> str:
    return "\n".join([z for z in [
        "---",
        "type: normtext",
        f"framework: {framework}",
        f"id: {ident}",
        f"source_file: {yaml_wert(meta.get('source_file', ''))}",
        f"source_sha256: {meta.get('source_sha256', '')}",
        f"source_page: {sec.page}",
        (f"source_locator: {yaml_wert(sec.locator)}" if sec.locator else None),
        f"text_coverage_percent: {meta.get('text_coverage_percent', '')}",
        f'tags: ["grc/normtext", "grc/framework/{framework}"]',
        "generated-by: document-to-LLM",
        "---",
        "",
        f"# {ident} — {sec.title}".rstrip(" —"),
        "",
        (f"> [!quote] Normtext, Seite {sec.page} der Quelle" if sec.page
         else f"> [!quote] Normtext, Schluesselpfad {sec.locator}" if sec.locator
         else "> [!quote] Normtext"),
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
        # Der Konverter steht in der Kopfzeile des Extrakts. Bei Passthrough-Dateien
        # war Docling nicht beteiligt, "IBM Docling" davorzuschreiben waere falsch.
        f"Woertlich aus {meta.get('source_file', 'der Quelle')} extrahiert "
        f"({meta.get('converter', 'IBM Docling')}). Lizenzierter Text — "
        f"bleibt lokal, nicht versionieren.",
        "",
    ] if z is not None])


def withdrawn_note(framework: str, ident: str, meta: dict[str, str]) -> str:
    """Notiz fuer eine ID, die es in der aktuellen Fassung der Norm nicht gibt.

    Die Notiz erfindet keinen Text: sie haelt fest, dass die Anforderung in der
    vorliegenden — aktuellen — Fassung nicht vorkommt, und nennt die Quelle, aus
    der das hervorgeht. Eine leere Platzhalternotiz stehen zu lassen waere
    schlechter: sie sieht aus wie eine Luecke in der Extraktion.
    """
    src = meta.get("source_file", "der Quelle")
    return "\n".join([
        "---",
        "type: normtext",
        f"framework: {framework}",
        f"id: {ident}",
        "status: entfallen",
        f"source_file: {yaml_wert(src)}",
        f"source_sha256: {meta.get('source_sha256', '')}",
        f'tags: ["grc/normtext", "grc/framework/{framework}", "grc/entfallen"]',
        "generated-by: document-to-LLM",
        "---",
        "",
        f"# {ident} — entfallen",
        "",
        "> [!warning] In der aktuellen Fassung nicht enthalten",
        f"> Diese Anforderung kommt in {src} nicht vor. Der Katalog enthaelt den",
        "> Kriterienbereich vollstaendig. Woher die ID stammt, sagt die Quelle",
        "> nicht. Nicht als geltende Anforderung zitieren.",
        "",
        "---",
        "",
        f"Festgestellt beim Abgleich der Vault-IDs gegen {src} "
        f"({meta.get('converter', 'IBM Docling')}).",
        "",
    ])


def document_notes(md_path: Path, vault: Path, meta: dict[str, str], body: str,
                   titel: str, autor: str, art: str, dry_run: bool,
                   superseded_by: str = "", ablage: Path | None = None
                   ) -> tuple[Path, Path]:
    """Ein Dokument ohne Anforderungsraster ablegen: Volltext in den lizenzierten
    Ordner, Metadatennotiz nach GRC/Handbuch mit Embed darauf.

    Damit landet auch alles, was keine Norm ist — Leitfaden, Fachartikel,
    Handbuchkapitel, Behoerdenschreiben — im selben Bestand und nach denselben
    Regeln wie die Normen.

    Ist das Dokument von einer neueren Fassung abgeloest (`superseded_by`), wird
    es nicht verworfen, sondern als Historiendokument abgelegt: der Wortlaut
    bleibt nachlesbar, die Notiz sagt aber vorweg, dass er nicht mehr gilt, und
    nennt die geltende Fassung. Loeschen wuerde die Frage "was stand da frueher"
    unbeantwortbar machen.
    """
    deckung = str(meta.get('text_coverage_percent', '') or '').strip()
    slug = md_path.stem
    # Ohne --unterordner bleibt die Ablage der Vaultwurzel; mit ihm wandert
    # der gesamte erzeugte Bestand in einen eigenen Ordner. Das Register unter
    # GRC/Frameworks bleibt davon unberuehrt: es gehoert dem Nutzer, nicht
    # diesem Werkzeug.
    wurzel = ablage or vault
    full_dir = wurzel / LICENSED_DIR / "dokumente"
    full = full_dir / f"{slug} (Volltext).md"
    # Schraegstriche im Titel (z. B. "2003/361/EG") wuerden Unterordner anlegen.
    safe = re.sub(r"[/\\:]+", "-", titel).strip()
    note = wurzel / "GRC" / "Handbuch" / f"{safe} ({slug}).md"
    # Der Hinweis nennt den tatsaechlichen Pfad. Ein Verweis auf einen Ordner,
    # den es nicht gibt, ist schlechter als keiner: er laesst den Leser suchen.
    # Immer relativ zur Vaultwurzel, nie zur Ablage: mit Unterordner ergibt das
    # "Document to LLM/Normen (lizenziert)/dokumente/", ohne ihn schlicht
    # "Normen (lizenziert)/dokumente/". Eine Fallunterscheidung ueber 'ablage'
    # waere hier falsch, weil ablage auch ohne Unterordner gesetzt ist.
    volltext_pfad = f"{full_dir.relative_to(vault)}/"

    head = "\n".join([
        "---", "type: dokument-volltext", f"slug: {slug}",
        f"source_file: {yaml_wert(meta.get('source_file', ''))}",
        f"source_sha256: {meta.get('source_sha256', '')}",
        f"pages: {meta.get('pages', '')}",
        (f"text_coverage_percent: {deckung}" if deckung
         else "text_coverage_percent: null\ndeckung_pruefbar: false"),
        *(["status: historisch", f"superseded_by: {superseded_by}"] if superseded_by else []),
        ('tags: ["grc/dokument/volltext", "grc/historisch"]' if superseded_by
         else 'tags: ["grc/dokument/volltext"]'),
        "generated-by: document-to-LLM", "---", "",
    ])

    meta_note = "\n".join([
        "---", "type: document", f"slug: {slug}",
        f"work: {yaml_wert(titel)}", f"autor: {yaml_wert(autor)}", f"art: {yaml_wert(art)}",
        *(["status: historisch", f"superseded_by: {superseded_by}"] if superseded_by else []),
        f"source_file: {yaml_wert(meta.get('source_file', ''))}",
        f"source_sha256: {meta.get('source_sha256', '')}",
        f"pages: {meta.get('pages', '')}",
        (f"text_coverage_percent: {deckung}" if deckung
         else "text_coverage_percent: null\ndeckung_pruefbar: false"),
        f"converter: {yaml_wert(meta.get('converter', ''))}",
        "licensed: true",
        ('tags: ["grc/handbuch", "grc/dokument", "grc/historisch"]' if superseded_by
         else 'tags: ["grc/handbuch", "grc/dokument"]'),
        "generated-by: document-to-LLM", "---", "",
        f"# {titel}", "",
        f"*{autor} · {art}*" if autor or art else "",
        "",
        *(["> [!warning] Ueberholte Fassung — nicht als geltend zitieren",
           f"> Diese Fassung ist durch `{superseded_by}` abgeloest. Sie bleibt hier,",
           "> damit nachlesbar ist, was frueher galt: fuer Audits mit Stichtag in der",
           "> Vergangenheit, fuer Aenderungsnachweise und um Abweichungen zur neuen",
           "> Fassung belegen zu koennen. Fuer jede Aussage ueber den geltenden Stand",
           f"> ist `{superseded_by}` massgeblich.", ""] if superseded_by else []),
        *(["> [!info] Aufnahme",
           f"> Quelle `{meta.get('source_file', '')}`, {meta.get('pages', '?')} Seiten, "
           f"Wortdeckung {deckung} %. "
           f"Extrahiert mit {meta.get('converter', 'IBM Docling')}."] if deckung else
          ["> [!warning] Maschinell gelesen, nicht woertlich extrahiert",
           f"> Quelle `{meta.get('source_file', '')}`, {meta.get('pages', '?')} Seiten, "
           f"gelesen mit {meta.get('converter', 'IBM Docling')} und OCR.",
           "> Das PDF traegt keinen Textlayer. Der Text stammt damit aus der",
           "> Zeichenerkennung, nicht aus der Datei — er ist **erzeugt, nicht",
           "> extrahiert**. Eine Wortdeckung laesst sich nicht berechnen, weil es",
           "> nichts gibt, wogegen zu pruefen waere. Lesefehler sind moeglich und",
           "> faellen nicht auf. Fuer woertliche Zitate das Original heranziehen."]),
        "",
        "## Volltext",
        "",
        f"![[{slug} (Volltext)]]",
        "",
        "> [!info]- Kein Text zu sehen?",
        f"> Der Volltext liegt unter `{volltext_pfad}` — einem",
        "> Ordner ausserhalb der Versionierung. Auf diesem Rechner loest der",
        "> Verweis auf, im Repository bleibt er leer.",
        "",
    ])

    if not dry_run:
        full_dir.mkdir(parents=True, exist_ok=True)
        note.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(head + body.strip() + "\n", encoding="utf-8")
        note.write_text(meta_note, encoding="utf-8")
    return note, full


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("extract_md", type=click.Path(exists=True, dir_okay=False))
@click.option("--vault", required=True, type=click.Path(file_okay=False, exists=True),
              help="Wurzel des Obsidian-Vaults (der Ordner mit GRC/ und .obsidian/).")
@click.option("--framework", default=None,
              help="Framework-Slug wie im Vault, z. B. iso27001-2022.")
@click.option("--as-document", "as_document", is_flag=True,
              help="Dokument ohne Anforderungsraster ablegen (Leitfaden, Fachartikel, "
                   "Handbuchkapitel): Volltext plus Metadatennotiz unter GRC/Handbuch.")
@click.option("--titel", default=None, help="Titel der Dokumentnotiz (--as-document).")
@click.option("--autor", default="", help="Urheber (--as-document).")
@click.option("--art", default="Dokument", show_default=True,
              help="Art des Dokuments, z. B. Fachartikel, Leitfaden (--as-document).")
@click.option("--superseded-by", "superseded_by", default="",
              help="Slug der geltenden Fassung. Legt das Dokument als Historiendokument "
                   "ab: Wortlaut bleibt nachlesbar, die Notiz warnt vor dem Zitieren "
                   "als geltender Stand und nennt die Nachfolgefassung (--as-document).")
@click.option("--mark-withdrawn", "mark_withdrawn", is_flag=True,
              help="IDs, die der Katalog nicht kennt, als 'entfallen' festhalten. "
                   "Nur bei maschinenlesbaren Katalogen (YAML) moeglich, weil nur "
                   "dort das Fehlen einer ID eine Aussage ist.")
@click.option("--export-json", "export_ziel", default=None,
              help="Anforderungen zusaetzlich als JSON schreiben (frameworkId, edition, "
                   "sourceFile, sourceSha256, requirements[id,title,text,group]) — fuer "
                   "Systeme, die damit rechnen, ohne uebersetzen zu muessen.")
@click.option("--unterordner", default="",
              help="Unterordner im Vault, in den der erzeugte Bestand geschrieben "
                   "wird (z. B. 'Document to LLM'). Ohne Angabe liegt er in der "
                   "Vaultwurzel. Das Anforderungsregister unter GRC/Frameworks "
                   "wird immer aus der Wurzel gelesen — es gehoert dem Nutzer.")
@click.option("--dry-run", is_flag=True, help="Nur berichten, nichts schreiben.")
@click.option("--overwrite/--keep", default=True, show_default=True,
              help="Vorhandene Normtext-Notizen ersetzen oder stehen lassen.")
def main(extract_md: str, vault: str, framework: str | None, as_document: bool,
         unterordner: str,
         titel: str | None, autor: str, art: str, superseded_by: str,
         export_ziel: str | None, mark_withdrawn: bool, dry_run: bool,
         overwrite: bool) -> None:
    """Schreibt Normtext- oder Dokumentnotizen aus einem Extrakt in den Vault."""
    vault_path = Path(vault).expanduser()
    # Ablageort des erzeugten Bestands. Getrennt vom Vaultpfad gehalten, weil
    # gelesen und geschrieben an verschiedenen Stellen wird: das
    # Anforderungsregister liegt beim Nutzer, die Ausgabe dort, wo er sie haben
    # will. Ein gemeinsamer Pfad wuerde beides koppeln.
    ablage_path = vault_path / unterordner if unterordner else vault_path
    md_path = Path(extract_md)
    meta, body = split_front_matter(md_path.read_text(encoding="utf-8"))

    if as_document:
        name = titel or Path(meta.get("source_file", md_path.stem)).stem
        note, full = document_notes(md_path, vault_path, meta, body, name, autor, art,
                                    dry_run, superseded_by, ablage=ablage_path)
        click.secho(f"{'Historiendokument' if superseded_by else 'Dokument'} abgelegt"
                    f"{' (Probelauf)' if dry_run else ''}: {note.name}",
                    fg="yellow" if superseded_by else "green")
        if superseded_by:
            click.echo(f"Abgeloest durch: {superseded_by}")
        click.echo(f"Volltext: {full}")
        return

    if superseded_by:
        raise click.ClickException(
            "--superseded-by gilt nur mit --as-document. Eine ueberholte Fassung als "
            "Normtext abzulegen wuerde die geltenden Notizen ueberschreiben.")

    if not framework:
        raise click.ClickException("Entweder --framework oder --as-document angeben.")

    wanted = vault_ids(vault_path, framework)
    if not wanted:
        raise click.ClickException(f"Keine Anforderungsnotizen fuer {framework} im Vault gefunden.")

    aufgeloest = aufgeloeste_abschnitte(body, meta, wanted, framework)

    target_dir = ablage_path / LICENSED_DIR / framework
    written, missing, skipped = [], [], []
    for ident in sorted(wanted):
        sec = aufgeloest.get(ident)
        if sec is None:
            missing.append(ident)
            continue
        target = target_dir / f"{framework} {ident} (Normtext).md"
        if target.exists() and not overwrite:
            skipped.append(ident)
            continue
        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            target.write_text(note_text(framework, ident, sec, meta), encoding="utf-8")
        written.append(ident)

    withdrawn: list[str] = []
    if mark_withdrawn and missing:
        group = yaml_catalogue_group(body, meta)
        if not group:
            raise click.ClickException(
                "--mark-withdrawn nur bei maschinenlesbaren Katalogen: aus einem "
                "PDF laesst sich nicht schliessen, dass eine fehlende ID entfallen "
                "ist — sie kann auch nur nicht gefunden worden sein.")
        for ident in list(missing):
            if not ident.startswith(group + "-"):
                continue          # anderer Kriterienbereich: diese Datei sagt nichts
            target = target_dir / f"{framework} {ident} (Normtext).md"
            if target.exists() and not overwrite:
                continue
            if not dry_run:
                target_dir.mkdir(parents=True, exist_ok=True)
                target.write_text(withdrawn_note(framework, ident, meta), encoding="utf-8")
            withdrawn.append(ident)
            missing.remove(ident)

    if export_ziel:
        ep = Path(export_ziel).expanduser()
        ep.parent.mkdir(parents=True, exist_ok=True)
        ep.write_text(export_json(framework, md_path.stem, meta, aufgeloest,
                                  sorted(missing)), encoding="utf-8")
        click.echo(f"JSON-Export: {ep} ({len(aufgeloest)} Anforderungen, "
                   f"{len(missing)} ohne Wortlaut)")

    click.secho(f"{len(written)} von {len(wanted)} Anforderungen belegt"
                + (" (Probelauf, nichts geschrieben)" if dry_run else f" -> {target_dir}"),
                fg="green" if not missing else "yellow")
    if withdrawn:
        click.secho(f"{len(withdrawn)} als entfallen festgehalten (nicht in der aktuellen "
                    f"Fassung): " + ", ".join(withdrawn), fg="yellow")
    if skipped:
        click.echo(f"{len(skipped)} vorhandene Notizen unveraendert gelassen (--overwrite ersetzt sie).")
    if missing:
        click.secho(f"{len(missing)} ohne Normtext im Extrakt: "
                    + ", ".join(missing[:20]) + (" ..." if len(missing) > 20 else ""), fg="yellow")
        click.echo("Diese IDs stehen so nicht im Dokument — pruefen, ob der richtige "
                   "Normstand extrahiert wurde.")

    warn = (vault_path / ".gitignore")  # immer die Vaultwurzel, dort greift sie
    if warn.exists() and LICENSED_DIR not in warn.read_text(encoding="utf-8"):
        click.secho(f"ACHTUNG: '{LICENSED_DIR}/' steht nicht in der .gitignore des Vaults — "
                    f"lizenzierter Normtext koennte versioniert werden.", fg="red")


if __name__ == "__main__":
    main()
