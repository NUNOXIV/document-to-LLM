#!/usr/bin/env python3
"""Erzeugt das Norm-aehnliche Test-PDF unter tests/fixtures/.

Bewusst schwierig: zweispaltiger Satz, Kopf- und Fusszeilen, Gliederungsnummern,
eine Control-Tabelle mit mehrzeiligen Zellen, Umlaute und ein Seitenumbruch
mitten im Fliesstext. Nur fuer Tests — nicht Teil der Laufzeit.

    python tests/make_fixture.py [zielpfad.pdf]
"""
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
ss = getSampleStyleSheet()
body = ParagraphStyle("body", parent=ss["BodyText"], fontSize=9, leading=12, alignment=TA_JUSTIFY)
h1 = ParagraphStyle("h1", parent=ss["Heading1"], fontSize=13, spaceAfter=6)
h2 = ParagraphStyle("h2", parent=ss["Heading2"], fontSize=11, spaceAfter=4)
h3 = ParagraphStyle("h3", parent=ss["Heading3"], fontSize=10, spaceAfter=4)


def decorate(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.drawString(20 * mm, A4[1] - 12 * mm, "MUSTER-NORM 99001:2026-08 (Entwurf)")
    canvas.drawRightString(A4[0] - 20 * mm, A4[1] - 12 * mm, "Vertraulich - nur zu Testzwecken")
    canvas.drawCentredString(A4[0] / 2, 12 * mm, f"Seite {doc.page}")
    canvas.restoreState()


def build(out: Path = DEFAULT_OUT) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(str(out), pagesize=A4,
                          leftMargin=20 * mm, rightMargin=20 * mm,
                          topMargin=20 * mm, bottomMargin=20 * mm)
    w = (doc.width - 8 * mm) / 2
    two = PageTemplate(id="two", onPage=decorate, frames=[
        Frame(doc.leftMargin, doc.bottomMargin, w, doc.height, id="l"),
        Frame(doc.leftMargin + w + 8 * mm, doc.bottomMargin, w, doc.height, id="r"),
    ])
    one = PageTemplate(id="one", onPage=decorate,
                       frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height)])
    doc.addPageTemplates([two, one])

    story = [
        Paragraph("4 Kontext der Organisation", h1),
        Paragraph("4.1 Verstehen der Organisation und ihres Kontextes", h2),
        Paragraph("Die Organisation muss externe und interne Themen bestimmen, die für ihren "
                  "Zweck relevant sind und die ihre Fähigkeit beeinflussen, die beabsichtigten "
                  "Ergebnisse ihres Informationssicherheitsmanagementsystems zu erreichen.", body),
        Paragraph("4.1.2 Dokumentierte Information", h3),
        Paragraph("Die Organisation muss dokumentierte Information über den Anwendungsbereich "
                  "aufrechterhalten. Der Anwendungsbereich muss die Schnittstellen und "
                  "Abhängigkeiten zwischen Tätigkeiten der Organisation und Tätigkeiten anderer "
                  "Organisationen berücksichtigen.", body),
        Paragraph("4.2 Verstehen der Erfordernisse und Erwartungen interessierter Parteien", h2),
        Paragraph("Die Organisation muss die interessierten Parteien bestimmen, die für das "
                  "Informationssicherheitsmanagementsystem relevant sind, sowie deren "
                  "Anforderungen, einschließlich gesetzlicher und vertraglicher Verpflichtungen.", body),
        Paragraph("5 Führung", h1),
        Paragraph("5.1 Führung und Verpflichtung", h2),
        Paragraph("Die oberste Leitung muss Führung und Verpflichtung in Bezug auf das "
                  "Informationssicherheitsmanagementsystem nachweisen, indem sie sicherstellt, "
                  "dass die Informationssicherheitspolitik und die Informationssicherheitsziele "
                  "festgelegt und mit der strategischen Ausrichtung der Organisation vereinbar sind.", body),
        NextPageTemplate("one"),
        PageBreak(),
        Paragraph("Anhang A (normativ) Referenzmaßnahmen", h1),
    ]

    rows = [["Control", "Titel", "Attribut", "Anforderung"],
            ["A.5.1", "Informationssicherheitsrichtlinien", "Präventiv",
             "Richtlinien für Informationssicherheit müssen definiert, von der Leitung genehmigt, "
             "veröffentlicht und den relevanten Beschäftigten kommuniziert werden."],
            ["A.8.24", "Verwendung von Kryptographie", "Präventiv",
             "Regeln für den wirksamen Einsatz von Kryptographie, einschließlich der "
             "Schlüsselverwaltung, müssen festgelegt und umgesetzt werden."],
            ["A.8.25", "Sicherer Entwicklungszyklus", "Präventiv",
             "Regeln für die sichere Entwicklung von Software und Systemen müssen festgelegt "
             "und auf Entwicklungen innerhalb der Organisation angewendet werden."],
            ["A.8.28", "Sicheres Programmieren", "Präventiv",
             "Grundsätze für sicheres Programmieren müssen auf die Softwareentwicklung "
             "angewendet werden."]]
    cell = ParagraphStyle("cell", parent=body, fontSize=8, leading=10, alignment=0)
    data = [[Paragraph(c, cell) for c in row] for row in rows]
    table = Table(data, colWidths=[22 * mm, 45 * mm, 20 * mm, 83 * mm], repeatRows=1)
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dddddd")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story += [table, Spacer(1, 6 * mm),
              Paragraph("Anhang B (informativ) Hinweise zur Anwendung", h1),
              Paragraph("Dieses Dokument ist frei erfunden und dient ausschließlich der "
                        "Regressionsprüfung der Extraktionspipeline. Ende der Beispielnorm.", body)]
    doc.build(story)
    return out


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    print("geschrieben:", build(target))
