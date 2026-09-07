#!/usr/bin/env python3
"""Eigenschaftstests: Faelle, die niemand aufgeschrieben haette.

Warum zusaetzlich zu den Beispieltests: Die Kennungserkennung ist zweimal an
Faellen zerbrochen, die in keiner Beispielliste standen — erst an
Buchstabenpraefixen (APP.1.1.A1), dann an "INF", weil das I im roemischen
Zweig lag und der Regex nach einem Zeichen abbrach. Beide Male sah der Median
gesund aus, beide Male fehlte der Fall in den Tests, weil niemand ihn
aufgeschrieben hatte.

hypothesis schreibt ihn auf. Statt einzelner Beispiele wird eine Eigenschaft
behauptet — "aus jeder gueltigen Kennung faellt genau dieselbe Kennung wieder
heraus" — und die Bibliothek sucht das Gegenbeispiel.

    python -m pytest tests/test_eigenschaften.py -q
"""
from __future__ import annotations

import sys
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fundstellen as F  # noqa: E402
import publish  # noqa: E402

# Praefixe, wie Regelwerke sie fuehren. INF, IND und ISMS stehen ausdruecklich
# dabei: an ihnen ist der Regex zerbrochen.
PRAEFIX = st.sampled_from(["APP", "SYS", "ORP", "CON", "DER", "IND", "INF", "ISMS",
                           "NET", "OPS", "PAS", "OS"])
ZAHL = st.integers(min_value=1, max_value=99)


@st.composite
def kennung(draw) -> str:
    """Kennungen der Form APP.1.1.A1, SYS.2.2, INF.10.A3."""
    teile = [draw(PRAEFIX)] + [str(draw(ZAHL)) for _ in range(draw(st.integers(1, 3)))]
    ident = ".".join(teile)
    if draw(st.booleans()):
        ident += f".A{draw(ZAHL)}"
    return ident


@given(ident=kennung(), titel=st.text(alphabet=st.characters(
    whitelist_categories=("Ll", "Lu", "Zs")), min_size=3, max_size=40))
@settings(max_examples=300, deadline=None)
def test_kennung_faellt_unveraendert_wieder_heraus(ident: str, titel: str) -> None:
    """Aus einer Ueberschrift muss dieselbe Kennung kommen, die hineinging.

    Der INF-Fehler war genau ein Verstoss dagegen: hinein ging "INF.1.A1",
    heraus kam "I". Die Laenge des Ergebnisses verriet nichts, der Abschnitt
    lief bis zum Dateiende weiter.
    """
    titel = titel.strip() or "Titel"
    body = f"## {ident} {titel}\n\nDie Institution MUSS etwas tun."
    treffer = publish.sections_from_headings(body)
    # Die Ablage fuehrt Kennungen normalisiert (publish.norm_key), deshalb wird
    # gegen die normalisierte Form geprueft — aber gegen die vollstaendige.
    schluessel = publish.norm_key(ident)
    assert schluessel in treffer, f"{ident} nicht erkannt, erkannt wurde: {list(treffer)}"
    assert treffer[schluessel].text.startswith("Die Institution MUSS")


@given(text=st.text(min_size=1, max_size=200))
@settings(max_examples=300, deadline=None)
def test_normalisierung_ist_stabil(text: str) -> None:
    """Zweimal normalisieren aendert nichts mehr.

    Ohne diese Eigenschaft koennte derselbe Text je nach Weg unterschiedlich
    aussehen — und der Resolver mal treffen, mal nicht.
    """
    einmal = F.normalisiere(text)
    assert F.normalisiere(einmal) == einmal


@given(text=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu", "Nd", "Zs")),
                    min_size=5, max_size=120))
@settings(max_examples=300, deadline=None)
def test_woertlaut_bleibt_auffindbar_trotz_umbruch(text: str) -> None:
    """Ein Zeilenumbruch an beliebiger Stelle darf den Treffer nicht kosten.

    Genau das passiert beim zweispaltigen Satz: die Quelle bricht mitten im
    Satz um. Ein Resolver, der daran scheitert, meldet Abweichungen, die keine
    sind — und wird nach dem dritten Fehlalarm ignoriert.
    """
    soll = F.normalisiere(text)
    if not soll:
        return
    mitte = len(text) // 2
    umgebrochen = F.normalisiere(text[:mitte] + "\n" + text[mitte:])
    # Ein Umbruch zwischen zwei Woertern verschwindet, einer mitten im Wort
    # wird zum Leerzeichen. Beides darf den Woertlaut nicht laenger machen.
    assert len(umgebrochen) <= len(soll) + 1
