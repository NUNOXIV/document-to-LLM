#!/usr/bin/env python3
"""Erzeugt das Norm-aehnliche Test-PDF unter tests/fixtures/.

Bewusst schwierig: zweispaltiger Satz, Kopf- und Fusszeilen, Gliederungsnummern,
eine Control-Tabelle mit mehrzeiligen Zellen, Umlaute und ein Seitenumbruch
mitten im Fliesstext. Nur fuer Tests — nicht Teil der Laufzeit.

Der Woertlaut steht nicht mehr hier, sondern in fixtures/ground-truth/
muster-norm-99001.json. Das ist der Kern der Sache: dieselbe Datei ist Vorlage
fuer die Quelle und Sollwert fuer den Fundstellen-Resolver (fundstellen.py).
Stuende der Text zweimal, koennten Quelle und Pruefmassstab auseinanderlaufen
und die Pruefung waere eine Selbstbestaetigung.

    python tests/make_fixture.py [zielpfad.pdf]
"""
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, NextPageTemplate, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

import sys

DEFAULT_OUT = Path(__file__).parent / "fixtures" / "Muster-Norm-Zweispaltig.pdf"
GROUND_TRUTH = (Path(__file__).resolve().parents[1] / "fixtures" / "ground-truth"
                / "muster-norm-99001.json")


def ground_truth(pfad: Path = GROUND_TRUTH) -> dict:
    return json.loads(pfad.read_text(encoding="utf-8"))
ss = getSampleStyleSheet()
body = ParagraphStyle("body", parent=ss["BodyText"], fontSize=9, leading=12, alignment=TA_JUSTIFY)
h1 = ParagraphStyle("h1", parent=ss["Heading1"], fontSize=13, spaceAfter=6)
h2 = ParagraphStyle("h2", parent=ss["Heading2"], fontSize=11, spaceAfter=4)
h3 = ParagraphStyle("h3", parent=ss["Heading3"], fontSize=10, spaceAfter=4)


def decorate(canvas, doc, kopf="MUSTER-NORM 99001:2026-08 (Entwurf)",
             kopf_rechts="Vertraulich - nur zu Testzwecken"):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.drawString(20 * mm, A4[1] - 12 * mm, kopf)
    canvas.drawRightString(A4[0] - 20 * mm, A4[1] - 12 * mm, kopf_rechts)
    canvas.drawCentredString(A4[0] / 2, 12 * mm, f"Seite {doc.page}")
    canvas.restoreState()


def build(out: Path = DEFAULT_OUT, gt: dict | None = None) -> Path:
    gt = gt or ground_truth()
    fund = gt["fundstellen"]
    out.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(str(out), pagesize=A4,
                          leftMargin=20 * mm, rightMargin=20 * mm,
                          topMargin=20 * mm, bottomMargin=20 * mm)

    def schmuck(canvas, d):
        decorate(canvas, d, gt.get("kopfzeile", ""), gt.get("kopfzeile_rechts", ""))

    w = (doc.width - 8 * mm) / 2
    two = PageTemplate(id="two", onPage=schmuck, frames=[
        Frame(doc.leftMargin, doc.bottomMargin, w, doc.height, id="l"),
        Frame(doc.leftMargin + w + 8 * mm, doc.bottomMargin, w, doc.height, id="r"),
    ])
    one = PageTemplate(id="one", onPage=schmuck,
                       frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height)])
    doc.addPageTemplates([two, one])

    stil = {1: h1, 2: h2, 3: h3}
    cell = ParagraphStyle("cell", parent=body, fontSize=8, leading=10, alignment=0)

    def ueberschrift(f: dict):
        # "4.1 Verstehen ..." bzw. "Anhang A (normativ) ..." — die Kennung steht
        # vorn, damit der Resolver sie in der Ueberschrift wiederfindet.
        return Paragraph(f"{f['id']} {f['titel']}", stil.get(f.get("ebene", 2), h2))

    # Vor dem Anhang zweispaltig, ab dem Anhang einspaltig mit Control-Tabelle.
    # Die Tabelle steht geschlossen an der Stelle ihres ersten Controls.
    story: list = []
    tabelle_gesetzt = False
    for f in fund:
        if f["art"] == "control":
            if tabelle_gesetzt:
                continue
            controls = [c for c in fund if c["art"] == "control"]
            rows = [["Control", "Titel", "Attribut", "Anforderung"]]
            rows += [[c["id"], c["titel"], c.get("attribut", ""), c["text"]] for c in controls]
            data = [[Paragraph(c, cell) for c in row] for row in rows]
            # Titelspalte breit genug fuer das laengste Wort. Bei 45 mm brach
            # reportlab "Informationssicherheitsrichtlinien" ohne Trennstrich um,
            # der Textlayer der Quelle enthielt danach "...richtlinie n". Der
            # Extrakt gab das getreu wieder — die Abweichung sass in der Vorlage.
            # Gefunden hat sie der Fundstellen-Resolver, im ersten Lauf.
            table = Table(data, colWidths=[22 * mm, 54 * mm, 20 * mm, 74 * mm], repeatRows=1)
            table.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dddddd")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            story += [table, Spacer(1, 6 * mm)]
            tabelle_gesetzt = True
            continue
        if f["id"] == "Anhang A":
            story += [NextPageTemplate("one"), PageBreak()]
        story.append(ueberschrift(f))
        if f.get("text"):
            story.append(Paragraph(f["text"], body))

    doc.build(story)
    return out


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    print("geschrieben:", build(target))
