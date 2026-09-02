---
source_file: "Identifikation-von-KRITIS-und-NIS2-Einrichtungen-OpenKRITIS.pdf"
source_sha256: 7f3f8c30162c578c132223a9d89aac8e973e5cb5385655ab6478b963dee38cb2
source_bytes: 497025
pages: 9
tables: 9
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T20:23:38+00:00"
text_coverage_percent: 100.0
restored_hyphens: 4
extraction_status: warn
warnings:
  - "2 Tabellenzelle(n) beginnen mitten im Satz — moegliche Zellverschiebung, z. B. \"kritische Dienstleistung ✓...\". Zeilen dieser Tabelle vor dem Zitat gegen die Quelle pruefen."
  - "4 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): KRITISBetreiber -> KRITIS-Betreiber, KRITISSektor -> KRITIS-Sektor, NIS2Umsetzung -> NIS2-Umsetzung, oderverknüpft -> oder-verknüpft"
  - "Der Textlayer der Quelle enthaelt 3 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

- [OpenKRITIS](https://www.openkritis.de/)
- [NIS2](https://www.openkritis.de/it-sicherheitsgesetz/)
- [Europa](https://www.openkritis.de/eu/)
- [Betreiber](https://www.openkritis.de/betreiber/)
- [Security](https://www.openkritis.de/massnahmen/)
- [School](https://www.openkritis.de/school/)

## Identifikation Betreiber

<!-- image -->

<!-- page: 2 -->

- [Regulierte Unternehmen](https://www.openkritis.de/betreiber/)
- [Identifikation](https://www.openkritis.de/betreiber/identifikation-kritische-infrastruktur.html)
- [Registrierung](https://www.openkritis.de/betreiber/registrierung-kritis-anlagen.html)
- [Meldepflicht](https://www.openkritis.de/betreiber/meldepflichten-bsig.html)
- [Geltungsbereich](https://www.openkritis.de/betreiber/geltungsbereich-kritis.html)
- [Betriebsführer](https://www.openkritis.de/betreiber/betriebsfuehrer-bnetza.html)
- [Komponenten](https://www.openkritis.de/betreiber/kritische-komponenten.html)
- [Prüfungen](https://www.openkritis.de/pruefung/)
- [Reifegrade](https://www.openkritis.de/betreiber/reifegrade-kritis-nis2-run.html)
- [Bußgelder](https://www.openkritis.de/betreiber/bussgelder-kritis-bsig.html)

<!-- page: 3 -->

<!-- image -->

<!-- page: 4 -->

Unternehmen sind für die Identifikation von KRITIS-Anlagen und Feststellung der Betroffenheit als NIS2-Einrichtung selbst verantwortlich. Kritische Anlagen und Schwellenwerte sind in der KRITIS-Verordnung definiert (deutsche KRITIS-Methodik). Für NIS2 relevante Einrichtungen, Sektoren und Unternehmens­ größen sind wiederum im Gesetz definiert (NIS2-Umsetzung).

1. Identifikation
2. KRITIS und kritische Anlagen
3. NIS2 und Einrichtungen

Mit der NIS2-Umsetzung und dem KRITIS-Dachgesetz verändert sich die Betroffenheit von Unternehmen und die Selbst-Identifikation: Neben kritischen Anlagen mit Schwellenwerten kommen mittlere und größe Unternehmen als Einrichtungen dazu. Diese NIS2-Einrichtungen identifizieren sich über ihre Unternehmens­ größe anhand von Mitarbeitern und Umsatz.

## Identifikation

## Betreiber und Einrichtungen

Erbringen Unternehmen mit eigenen Anlagen in KRITIS-Sektoren kritische Dienstleistungen über KRITIS-Schwellenwerten (über 500 Tsd. Personen), werden sie KRITIS-Betreiber. Ist ein Unternehmen in NIS2-Sektoren tätig und überschreitet NIS2-Unternehmensgrößen, wird es als ganzes Unternehmen zur NIS2-Einrichtung.

## Methode

Die Identifikation der Betroffenheit für KRITIS und NIS2 ist ähnlich und beginnt bei Sektoren.

| #                                                 | Parameter                                         | Betreiber (KRITIS)                                | Einrichtung (NIS2)                                                 |
|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|--------------------------------------------------------------------|
| 1.                                                | Sektor und                                        | KRITIS-Sektor ✓                                   | NIS2-Sektor ✓                                                      |
|                                                   | Dienstleistung                                    | kritische Dienstleistung ✓                        | NIS2-Einrichtungsart ✓                                             |
| 2.                                                | Geographie                                        | Wertschöpfung in Deutschland ✓                    | Legaleinheiten in Deutschland ✓                                    |
| 3. Scope                                          |                                                   | Wertschöpfung in KRITIS-Anlagen ✓                 | Wertschöpfung in Legaleinheiten ✓                                  |
| 4. Schwellenwerte Anlage ≥ KRITIS-Schwellenwerten | 4. Schwellenwerte Anlage ≥ KRITIS-Schwellenwerten | 4. Schwellenwerte Anlage ≥ KRITIS-Schwellenwerten | ✓ Unternehmen > Mitarbeiter ✓ oder Unternehmen > Umsatz + Bilanz ✓ |
| 5. Zeitraum                                       | 5. Zeitraum                                       | Pro Kalenderjahr oder Stichtag ✓                  | noch offen                                                         |
| ∑ Betroffenheit                                   | ∑ Betroffenheit                                   | Wenn 1+2+3+4+5 ✓ dann KRITIS                      | Wenn 1+2+3+4+5 ✓ dann Einrichtung                                  |
| 7. Registrierung                                  | 7. Registrierung                                  | Unmittelbar nach Betroffenheit                    | Drei Monate nach Betroffenheit                                     |
| 8. Pflichten                                      | 8. Pflichten                                      | Direkt nach Registrierung                         | Direkt nach Registrierung                                          |
| 9. Prüfungen                                      | 9. Prüfungen                                      | Alle drei Jahre                                   | Stichproben durch BSI                                              |

## Konsequenzen

Es gibt mehrere Möglichkeiten für Unternehmen, betroffen zu sein:

1. Das Unternehmen betreibt in KRITIS-Sektoren eine kritische Anlage über definierten KRITIS-Schwellenwerten und identifiziert (KRITIS) diese.
2. Die Legaleinheit wird zum Betreiber kritischer Anlagen
3. Das Unternehmen muss im Geltungsbereich der kritischen Anlage KRITIS-Pflichten umsetzen

<!-- page: 5 -->

up

## KRITIS und kritische Anlagen

Das folgende Beispiel der KRITIS-Betroffenheit beschreibt einen Konzern, der als Gesundheits­ versorger Krankenhäuser betreibt und dabei die KRITIS-Betroffenheit seiner Häuser prüft.

## Identifikation

## Infrastrukturen

Zur Einordnung: das BSI-Gesetz definiert Kritische Infrastrukturen bis 2025 als:

'Einrichtungen, Anlagen oder Teile davon, die [den KRITIS-Sektoren] angehören und von hoher Bedeutung für das Funktionieren des Gemeinwesens sind, weil durch ihren Ausfall oder ihre Beeinträchtigung erhebliche Versorgungsengpässe oder Gefährdungen für die öffentliche Sicherheit eintreten würden.'

## Anlagen und Betreiber

Anlagen sind im KRITIS-Dachgesetz §2 (2) definiert als:

' Betriebsstätte, sonstige ortsfeste Installation, Maschine, Gerät, sonstige ortsveränderliche technische Installation oder Software und IT-Dienste; für Software und IT-Dienste, die nicht unmittelbar der Steuerung, Überwachung oder Unterstützung physischer Prozesse der Erbringung kritischer Dienstleistungen dienen, gelten ausschließlich die Vorgaben des BSIGesetzes;'

Die genauen Anlagentypen sind in der KRITIS-Verordnung definiert.

Die Betreiber kritischer Anlagen sind im KRITIS-Dachgesetz §2 (1) definiert als:

' natürliche oder juristische Person oder eine rechtlich unselbständige Organisationseinheit einer Gebietskörperschaft, die unter Berücksichtigung der rechtlichen, wirtschaftlichen und tatsächlichen Umstände bestimmenden Einfluss auf eine oder mehrere kritische Anlagen ausübt; abweichend hiervon hat im Sektor Finanzwesen bestimmenden Einfluss auf eine kritische Anlage, wer die tatsächliche Sachherrschaft ausübt, wobei die rechtlichen und wirtschaftlichen Umstände insoweit unberücksichtigt bleiben;'

## Sektor und Dienstleistung

KRITIS-Anlagen erbringen kritische Dienstleistungen in den KRITIS-Sektoren zur Versorgung der Bevölkerung. Kritische Infrastrukturen, also KRITIS-Anlagen, befinden sich immer in KRITIS-Sektoren - die Betreiber selbst können auch in anderen Sektoren tätig sein.

- Das Unternehmen muss zusätzlich KRITIS-Dachgesetz-Pflichten umsetzen
- Die Legaleinheit wird automatisch auch besonders wichtige Einrichtung
- Das Unternehmen muss in der Legaleinheit NIS2-Pflichten umsetzen
2. Das Unternehmen bietet in NIS2-Sektoren Dienstleistungen an und überschreitet dabei NIS2-Unternehmensgrößen und identifiziert (NIS2) die Legaleinheit.
- Die Legaleinheit wird zur regulierten NIS2-Einrichtung (besonders wichtig oder wichtig)
- Das Unternehmen muss in der Legaleinheit NIS2-Pflichten umsetzen

<!-- page: 6 -->

Alle Dienstleistungen und Sektoren sind in der KRITIS-Verordnung definiert.

Beispiel : Der Gesundheitskonzern erbringt eine kritische Dienstleistung in einem KRITIS-Sektor.

| Unternehmen KRITIS-Sektor     | Kritische Dienstleistung             | KritisV   |
|-------------------------------|--------------------------------------|-----------|
| Gesundheitskonzern Gesundheit | stationäre medizinische Versorgung ✓ | §6 (1) 1. |

## Geographie

Die Wertschöpfung der kritischen Dienstleistung muss in Anlagen in Deutschland stattfinden. Der Betreiber kann international sein - wichtig ist der Standort der Anlagen auf Bundesgebiet.

Beispiel : Der Konzern erbringt die Dienstleistung in Deutschland in zwei Krankenhäusern.

| Unternehmen   | Dienstleistung                                                | Standort der Anlagen                                          |
|---------------|---------------------------------------------------------------|---------------------------------------------------------------|
|               | Stationäre medizinische Versorgung Krankenhäuser europaweit ✗ | Stationäre medizinische Versorgung Krankenhäuser europaweit ✗ |
| Konzern       | (HQ)                                                          | Krankenhäuser Deutschland ✓                                   |
|               | Verwaltung                                                    | HQ International ✗                                            |

## Anlagen

Die kritische Dienstleistung muss in Anlagen erbracht werden, die in der umfangreichen Liste der KRITIS-Anlagen der KritisV definiert sind. Die Anlagen sind spezifisch pro KRITIS-Sektor definiert und umfassen Betriebsstätten, Standorte oder sonstige ortsfeste Einrichtungen .

Beispiel : Krankenhäuser sind im Sektor Gesundheit als Anlage 1.1 definiert

| Anlage              | Standort              | KRITIS-Anlage     | KritisV         |
|---------------------|-----------------------|-------------------|-----------------|
| Krankenhaus Berlin, | Deutschland           | 1.1 Krankenhaus ✓ | Anhang 5, 1. a) |
| Krankenhaus         | Hangelar, Deutschland | 1.1 Krankenhaus ✓ | Anhang 5, 1. a) |

up

## Kritische Infrastruktur

## Schwellenwerte

Anlagen, die Schwellenwerte überschreiten, werden zur KRITIS-Anlage. Die Schwellenwerte leiten sich (meist) aus der für die Versorgung von 500.000 Personen benötigten Leistung oder Kapazität pro Jahr ab. Betreiber müssen die Leistung der eigenen KRITIS-Anlagen feststellen und Schwellenwerte erkennen, die KRITIS-Verordnung definiert sind.

Beispiel : Der Schwellenwert für die Anlagen 1.1 'Krankenhäuser' ist 30 Tsd. Fälle pro Jahr. In 2023 hatte das Krankenhaus Berlin 40 Tsd. vollstationäre Fälle (= KRITIS), Hangelar 20 Tsd. (≠ KRITIS).

| Anlage   | Leistung   | Schwellenwert   | KritisV   |
|----------|------------|-----------------|-----------|

<!-- page: 7 -->

| Krankenhaus Berlin 40 Tsd. Fälle ✓   | 30 Tsd. vollstationäre Fallzahl pro Jahr   | Anhang 5, Teil 3 1.1   |
|--------------------------------------|--------------------------------------------|------------------------|
| Krankenhaus Hangelar 20 Tsd. Fälle ✗ | 30 Tsd. vollstationäre Fallzahl pro Jahr   | Anhang 5, Teil 3 1.1   |

## Zeitraum

Die Schwellenwerte müssen in einem Kalenderjahr überschritten und (meist) zum 31. März des Folgejahrs ermittelt werden. Bei einigen Anlagen gibt es in der KritisV auch abweichende Stichtage und Fristen, die Daten sind bei den einzelnen KRITIS-Sektoren aufgelistet.

Beispiel : Der Betreiber ermittelt den Schwellenwert des Krankenhauses Berlin vor der Frist und meldet die Anlage fristgerecht. Das Krankenhaus Hangelar wird zu spät ermittelt, bleibt jedoch 2019 unter dem Schwellenwert und ist damit nicht KRITIS.

Anlage Leistung Festgestellt KRITIS-Meldung

Krankenhaus Berlin 40 Tsd. Fälle/2019 10. Februar 2020 ✓ 1. April 2020 ✓

Krankenhaus Hangelar 20 Tsd. Fälle/2019 30. April 2020 ✗

## Konsequenzen

Treffen auf eine Anlage alle fünf Kriterien oben zu, ist diese wahrscheinlich KRITIS und muss als Kritische Infrastruktur beim BSI registriert werden. Der Betreiber wird zum KRITIS-Betreiber mit diversen Pflichten für Cybersecurity ab Registrierung.

Mit den Informationen aus der Identifikation wird nach der Registrierung der Geltungsbereich der KRITIS-Anlage definiert. Dieser beschreibt die Grenzen der Anlage im Unternehmen des KRITIS-Betreibers mit den zur Anlage gehörenden Prozesse, IT und OT.

Ein Betreiber kritischer Anlagen wird automatisch auch besonders wichtige Einrichtung in der betreibenden Legaleinheit und erbt dort NIS2-Pflichten.

up

## NIS2 und Einrichtungen

Das folgende Beispiel der NIS2-Betroffenheit beschreibt einen Verband, der u.a. ein Unternehmen der Abfallbewirtschaftung betreibt und dafür die NIS2-Betroffenheit seiner Unternehmen prüft.

## Identifikation Unternehmen

Mit der NIS2-Umsetzung werden Tausende Unternehmen in Deutschland als neue Einrichtung betroffen sein. Diese Einrichtungen sind in NIS2 mit separaten Wirtschafts­ sektoren und bestimmten Unternehmens­ größe definiert. Die Identifikation als Einrichtung in NIS2 bezieht sich rein auf Sektor und Dienstleistung sowie Unternehmens­ kennzahlen - nicht auf Anlagen.

Die Vorgaben und Definitionen dazu sind im NIS2-Umsetzungsgesetz (BSIG) beschrieben. Betreiber kritischer Anlagen werden automatisch auch besonders wichtige Einrichtung.

## Sektor und Dienstleistung

keine NIS2-Einrichtungen erbringen Dienstleistungen in separaten NIS2-Sektoren zur Versorgung der Allgemeinheit. Unternehmen können auch in anderen Sektoren tätig sein, das Erbringen von NIS2-Dienstleistungen in einem der NIS2-Sektoren ist ausschlaggebend.

<!-- page: 8 -->

Alle Dienstleistungen und Sektoren sind in der NIS2-Umsetzung im Gesetz (BSIG) definiert.

Beispiel : Der Verband erbringt mehrere Dienstleistungen in mehreren Sektoren.

| Dienstleistung      | NIS2-Sektor    | Einrichtungsart                         | Gesetz         |
|---------------------|----------------|-----------------------------------------|----------------|
| Abwasserbeseitigung | Abwasser ✓     | 1 Abwasser behandeln ✓                  | Anlage 1 5.2.1 |
| Entsorgungsbetrieb  | Entsorgung ✓ 2 | Unternehmen der Abfallbewirtschaftung ✓ | Anlage 2 2.1.1 |
| Schwimmbad          | - ✗            | (Hallenbad) ✗                           | -              |

## Legaleinheiten und Geographie

Die Wertschöpfung der kritischen Dienstleistung muss in Deutschland stattfinden. Der Betreiber kann international sein - wichtig ist die Erbringung der Dienstleistung auf Bundesgebiet.

Für NIS2-Einrichtungen ist die Legaleinheit von erbrachten Dienstleistungen entscheidend. In der Regel werden die Legaleinheiten (Gesellschaften, Anstalten oder Körperschaften), die die regulierten Dienstleistungen erbringen, zur regulierten Einrichtung.

Beispiel : Der Verband erbringt Dienstleistungen europaweit und ist dabei in verschiedene Legaleinheiten für den Betrieb aufgeteilt.

* - wird (wahrscheinlich) in anderen EU-Ländern reguliert

| Legaleinheit                                                                      | Standort                                                                          | Einrichtungsart NIS2                                                              |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Abfall ACME GmbH                                                                  | Altenkirchen, Deutschland ✓ Unternehmen Abfallbewirtschaftung ✓                   | Altenkirchen, Deutschland ✓ Unternehmen Abfallbewirtschaftung ✓                   |
| Recycling ACME GmbH Hachenburg, Deutschland ✓ Unternehmen Abfallbewirtschaftung ✓ | Recycling ACME GmbH Hachenburg, Deutschland ✓ Unternehmen Abfallbewirtschaftung ✓ | Recycling ACME GmbH Hachenburg, Deutschland ✓ Unternehmen Abfallbewirtschaftung ✓ |
| Wasser ACME GmbH                                                                  | Altenkirchen, Deutschland ✓ Abwasser behandeln ✓                                  | Altenkirchen, Deutschland ✓ Abwasser behandeln ✓                                  |
| Hallenbad ACME GmbH Hachenburg, Deutschland ✓ - ✗                                 | Hallenbad ACME GmbH Hachenburg, Deutschland ✓ - ✗                                 | Hallenbad ACME GmbH Hachenburg, Deutschland ✓ - ✗                                 |
| Recycling ACME B.V.                                                               | Holland ✗                                                                         | Unternehmen Abfallbewirtschaftung ( ✓ )*                                          |

up

## Betroffene Einrichtung

## Größe

Ist ein Unternehmen mit Legaleinheiten in den NIS2-Sektoren tätig und überschreitet die Werte für Mitarbeiter oder Umsatz und Bilanz, wird es zur regulierten Einrichtung.

Beispiel : Die einzelnen ACME-Unternehmen haben eigene Mitarbeiter (FTE) und Umsatz (EUR) durch Gebühren. Die NIS2-Grenzen für mittlere und Großunternehmen liegen an.

Die Kriterien sind oder-verknüpft: (Mitarbeiter) oder (Umsatz und Bilanz).

| Legaleinheit     | Größe                                       | NIS2-Grenze   | Einrichtung   |
|------------------|---------------------------------------------|---------------|---------------|
| Abfall ACME GmbH | 45 FTE ✗ 11 Mio Umsatz ✓ ≥ 50 FTE ≥ 10 Mio. | EUR           | Wichtig       |

<!-- page: 9 -->

```
Recycling ACME GmbH 15 FTE ✗ 5 Mio Umsatz ✗ ≥ 50 FTE ≥ 10 Mio. EUR - Wasser ACME GmbH 250 FTE ✓ 33 Mio Umsatz ✗ ≥ 250 FTE ≥ 50 Mio. EUR Besonders wichtig
```

## Zeitraum

Die Unternehmensgröße muss wahrscheinlich pro Kalenderjahr festgestellt und dann zum 31. März des Folgejahrs gemeldet werden - dies ist jedoch noch nicht im Gesetz definiert.

## Konsequenzen

Treffen auf ein Unternehmen alle NIS2-Kriterien zu (Sektor, Dienstleistung, Legaleinheit in Deutschland, Größe), ist das Unternehmen wahrscheinlich eine NIS2-Einrichtung und muss sich beim BSI registrieren. Die Einrichtung hat diverse Pflichten für Cybersecurity ab Registrierung.

Legaleinheit Sektor Größe Reguliert als

Abfall ACME GmbH Entsorgung 11 Mio Umsatz Wichtige Einrichtung

Wasser ACME GmbH Abwasser 250 FTE

Besonders wichtige Einrichtung

up

## Weitere Informationen

## Quellen

1. NIS-2-Betroffenheitsprüfung, Bundesamt für Sicherheit in der Informationstechnik, o.D.
2. [Verordnung zur Bestimmung kritischer Anlagen nach dem BSI-Gesetz (BSI-Kritisverordnung - BSI-KritisV) von 2016, geändert 2025](https://www.gesetze-im-internet.de/bsi-kritisv/BJNR095800016.html)
3. [Gesetz über das Bundesamt für Sicherheit in der Informationstechnik und die Sicherheit in der Informationstechnik von Einrichtungen, BSI-Gesetz vom 2. Dezember 2025](https://www.gesetze-im-internet.de/bsig_2025/)
4. [OpenKRITIS](https://www.openkritis.de/)
5. [Regulierte Unternehmen](https://www.openkritis.de/betreiber/)
6. [Identifikation](https://www.openkritis.de/betreiber/identifikation-kritische-infrastruktur.html)
7. up

OpenKRITIS ∙ Die gemeinnützige Informationsplattform für NIS2-Einrichtungen und Kritische Infrastrukturen. 50670 Köln ∙ info@openkritis.de ∙ ISSN 2748-565X

Paul Weissmann ist der Herausgeber von OpenKRITIS und publiziert seit 1999 das PA-RISC-Referenzwerk, und Insel Westberlin. OpenKRITIS hat keinen Anspruch auf Vollständigkeit oder Korrektheit und stellt keine Rechtsberatung dar.

Copyright © 2021-2026 ∙ Impressum ∙ Datenschutz ∙ Über uns und Kontakt
