---
source_file: "ISMS-in-Kritischen-Infrastrukturen-und-NIS2-OpenKRITIS.pdf"
source_sha256: b547d5faa4ac3dd00f88d1ba7efb7819cae51a9fe6826eaae34a487187cc36af
source_bytes: 521343
pages: 8
tables: 5
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-27T18:10:05+00:00"
text_coverage_percent: 100.0
appended_source_lines: 3
extraction_status: warn
warnings:
  - "3 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
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

## ISMS in KRITIS und NIS2

<!-- image -->

<!-- page: 2 -->

- [Cybersecurity in KRITIS und NIS2](https://www.openkritis.de/massnahmen/)
- [ISMS](https://www.openkritis.de/massnahmen/information_security_management-isms-kritis.html)
- [BCMS](https://www.openkritis.de/massnahmen/business_continuity_management-bcms-kritis.html)
- [Risikomanagement](https://www.openkritis.de/massnahmen/kritis_risiko_management_assets.html)
- [Leitung](https://www.openkritis.de/massnahmen/kritis_organisation_management.html)
- [Personal](https://www.openkritis.de/massnahmen/personalsicherheit_schulungen_kritis-nis2.html)
- [Supply Chain](https://www.openkritis.de/massnahmen/lieferanten_supply-chain_sicherheit-kritis-nis2.html)
- [Vorfälle](https://www.openkritis.de/massnahmen/vorfallsmanagement.html)
- [Angriffserkennung](https://www.openkritis.de/massnahmen/orientierungshilfe_angriffserkennung_oh_sza.html)
- [IT-Sicherheit](https://www.openkritis.de/massnahmen/it-sicherheit.html)
- [Standards](https://www.openkritis.de/massnahmen/kritis-security-standards.html)

<!-- page: 3 -->

<!-- image -->

Betreiber und Einrichtungen müssen nach KRITIS und NIS2 ihre Anlagen und Dienstleistungen im Unternehmen durch ein ISMS, einem Management-System für Informations­ - sicherheit, schützen. Das ISMS verankert Verantwortung und Prozesse für das Management von Cybersecurity, um damit Risiken im Betrieb und in den erbrachten Dienstleistungen zu mindern.

1. ISMS Governance
2. Richtlinien und Vorgaben
3. Audits und Prüfungen

NIS2 macht umfangreiche Vorgaben für das Sicherheitsmanagement bei regulierten Unternehmen. Die folgende Ausarbeitung führt ISMS-Kernkomponenten anhand der NIS2Anforderungen für Einrichtungen, sowie der alten KRITIS-Anforderungen von RUN-KdA aus. Als Orientierung sind die Anforderungen der Durchführungsverordnung DVO (EU)

<!-- page: 4 -->

| Bereich     | Anforderung                                                                                  | NIS2 BSIG                    | RUN KdA        |
|-------------|----------------------------------------------------------------------------------------------|------------------------------|----------------|
| ISMS        | Management-System: Governance für Informationssicherheit                                     | NS.1 NS.5 NS.37              | 1-3 (1,17,3,4) |
| Richtlinien | Normatives Regelwerk für Informationssicherheit                                              | NS.5                         | 2-4 (2,65-67)  |
| Audits      | Selbstüberprüfung des ISMS zur Überwachung und externe Audits für Compliance und Regulatorik | NS.5 NS.18 NS.39 NS.40 NS.42 | 2-5 (85-89)    |

## Sicherheitsmanagement

## ISMS

Für die wirksame Behandlung von Cyberrisiken bei Einrichtungen und Betreibern ist ein Management-System für Informationssicherheit (ISMS) notwendig, das den Geltungs­ bereich bzw. die ganze Einrichtung (Legaleinheit) abdeckt und dort notwendige Maßnahmen der Informationssicherheit steuert.

| Anforderung                                 | NIS2 DVO-EU       | ISO 27001 2022   | RUN KdA   |
|---------------------------------------------|-------------------|------------------|-----------|
| Managementsystem für Informationssicherheit | 1.1.1 7.1         | 4.1-10.2         | 1 (1)     |
| Zuständigkeiten und Verantwortungen         | 1.2.1 1.2.2 1.2.4 | 4.3 A.5.3 A.5.4  | 2/3 (3)   |
| Funktionstrennung                           | 1.2.5             | A.5.3            | 2 (4)     |
| Verantwortung Geschäftsleitung              | NS.37             | 5.1 A.5.31       | 2 (17)    |
| Geltungsbereich                             | NS.4              | 4.3              |           |

## Rollen

Im ISMS haben verschiedene Rollen definierte Aufgaben im Geltungsbereich, u.a.:

- CISO , ISO , ISB : Leitung ISMS und Verantwortung für Vorgaben der Informationssicherheit
- IT-Leiter/CTO : Verantwortung für Umsetzung der Vorgaben und von Maßnahmen im IT/OT-Betrieb
- Fachbereiche : Umsetzung der ISMS-Vorgaben in Prozessen und Bereichen
- Asset-Verantwortliche : Schutz der eigenen Assets durch Umsetzung von Maßnahmen
- Geschäftsleitung : Unterstützung und Freigabe der ISMS-Ziele, Ressourcen

## Verantwortlichkeiten

<!-- page: 5 -->

Die Verantwortungen der einzelnen Rollen für Informationssicherheit müssen verbindlich festgelegt werden - eindeutig (RACI-'A' und 'R') und getrennt in Vorgaben, Umsetzung und Kontrolle (Funktionstrennung). Mögliche Orte für die Festlegungen durch das ISMS sind:

1. Rollenbeschreibungen
2. RACI-Matrizen
3. Prozessbeschreibungen
4. Funktionsbeschreibungen
5. Ernennungsurkunden

## Prozesse

Mit Prozessen steuert das ISMS die Informationssicherheit in der IT der KRITIS-Anlagen, u.a.:

- ISMS-Steuerung : Betrieb des Management-Systems - Ausübung von Governance
- Risikoanalyse : Analyse der Informationssicherheit von Assets und der IT, Durchführung der Schutzbedarfsfeststellung (SBF), Feststellung von Risiken
- Risikobehandlung : Entscheidung und Auswahl von Optionen in der Risikobehandlung (RBH) - Definition von Maßnahmen für Informations- und IT-Sicherheit der Assets und IT
- Reporting : Meldewesen innerhalb des Betreibers zur KRITIS-Anlage zum Stand des ISMS
- ISMS-Überprüfung : Eigener Prozess zur Überprüfung im ISMS, siehe interne Audits
- ISMS-Verbesserung : Kontinuierliche Verbesserung im ISMS - PDCA-Zyklus

## Standards

Die KRITIS-Regulierung schreibt keine verbindlichen Cybersecurity Standards für Kritische Infrastrukturen vor, Betreiber können die Umsetzung frei entscheiden. Einige bekannte Standards zum Aufbau eines ISMS umfassen ISO 27001 aber auch NIS2 und die Durchführungsverordnung.

Von der Wahl­ freiheit gibt es Ausnahmen in bestimmten Branchen, die besonders reguliert sind und/oder einen Branchen­ standard umsetzen müssen.

## Nachweise

Artefakte als Nachweis für ein laufendes und funktionierendes Management-System sind u.a.:

1. Protokolle
2. Entscheidungen
3. Risikoeinschätzungen
4. Getroffene Maßnahmen

up

## Richtlinien und Vorgaben

Die Sicherheitsziele des ISMS müssen in einer zentralen Leitlinie (Policy) zur Informationssicherheit verankert werden, mit den Zielen des Unternehmens, dem regulatorischen Rahmen und der Bedrohungslage. Basierend auf der Leitlinie dokumentiert das ISMS in seinen weiteren Richtlinien die Anforderungen an Informationssicherheit im Geltungsbereich.

<!-- page: 6 -->

| Anforderung                                                    | NIS2 DVO-EU   | ISO 27001 2022   | RUN KdA   |
|----------------------------------------------------------------|---------------|------------------|-----------|
|                                                                | 6.2           | 6.2              |           |
| Strategische Vorgaben und Verantwortung                        | 1.1.1 1.1.2   | A.5.1 A.5.2      | 2 (2)     |
| Festlegung notwendiger Kompetenzen (Betrieb und IT-Sicherheit) | -             | A.5.1 A.5.2      | 2 (65)    |
| Überprüfung und Freigabe von Richtlinien und Anweisungen       | viele         | A.5.1            | 4/2 (66)  |
| Abweichungen von bestehenden Richtlinien und Anweisungen       | -             | A.5.1            | 3/4 (67)  |

## Rahmenwerk

Die normativen Vorgaben zur Informationssicherheit legt das ISMS in seinem Rahmenwerk fest - in strategischen Richtlinien und operativen Anweisungen (Policies und Procedures). Das Rahmenwerk muss im Geltungsbereich gültig sein und die relevanten Themen abdecken - und jährlich überprüft und durch die Leitung freigegeben werden.

## Abweichungen

Ausnahmen von Vorgaben der Informationssicherheit und abweichende Umsetzungen müssen von autorisierten Gremien freigegeben und dokumentiert werden. Die Risiken dieser Ausnahmen vom Vorgabenwerk und Gründe für die Abweichungen müssen dokumentiert und regelmäßig überprüft werden.

## Nachweise

Nachweise für effektive Vorgaben und Richtlinien im ISMS sind u.a.:

1. Aktuelle Richtlinien
2. Freigaben
3. Revisionhistorien
4. Änderungen
5. Entscheidungen

## up

## Audits und Prüfungen

Das ISMS muss regelmäßig Audits im Geltungsbereich durchführen oder veranlassen, um die Compliance von Prozessen und IT und das Management mit Risiken zu überprüfen. Dies dient einerseits der Compliance mit ISMS-Vorgaben, Einhaltung regulatorischer Vorgaben aber auch kontinuierlichen Verbesserung und Weiterentwicklung des ISMS (KVP).

| Anforderung                                        | NIS2        | ISO 27001     | RUN    |
|----------------------------------------------------|-------------|---------------|--------|
|                                                    | DVO-EU      | 2022          | KdA    |
| Compliance und Informieren der Unternehmensleitung | 2.2.1 2.2.2 | A.5.31 A.5.36 | 2 (85) |

<!-- page: 7 -->

|                                                       | 7.1 7.2     | 9.2                  | 4/5 (86)   |
|-------------------------------------------------------|-------------|----------------------|------------|
| Interne Überprüfungen der Compliance von IT-Prozessen | 7.3         | A.5.36               |            |
| Interne IT- Prüfungen                                 | 2.3.1       | A.5.36 A.8.34        | 4/5/3 (87) |
| Planung externer Audits                               | 2.3.1       | A.5.35 A.5.36 A.8.34 | 3 (88)     |
| Durchführung externer Audits                          | 2.3.2 NS.39 | A.5.36 A.8.34        | 4/5 (89)   |
| Behördliche Audits, Nachfragen                        | 2.3.3 NS.40 | A.5.5 A.5.31         |            |
|                                                       | NS.42       | A.5.28 A.5.37        |            |

## Arten von Audits

Informationssicherheit kann durch das ISMS mit Audits überprüft werden - und sollte zu effektiven Verbesserungen führen.

- Compliance-Prüfungen : Überprüfung der Richtlinien-Konformität von IT-Prozessen
- Schwachstellen-Scans : Technische Scans und Tests der IT-Systeme auf Schwachstellen
- IT-Prüfungen : Überprüfung der Richtlinien-Konformität der IT-Systeme
- Externe Audits : Unabhängige Überprüfung von Prozessen der Systemen durch Dritte

## Nachweise

Nachweise für funktionierende interne Audits zur Verbesserung des ISMS sind u.a.:

1. Prüfberichte
2. Prüfpläne
3. Festgelegte Maßnahmen
4. Durchgeführte Maßnahmen

up

## Integration im Unternehmen

Das ISMS muss für eine nachhaltige Verbesserung der Informationssicherheit im Betrieb mit weiteren Management-Systemen beim regulierten Unternehmen vernetzt sein.

- Personalsicherheit: Vorgaben für HR-Security und Kontrollen in Personalprozessen.
- Lieferanten und Sicherheit: Vorgaben für Sicherheit bei Lieferanten, Dienstleistern und im Einkauf

<!-- page: 8 -->

up

## Weitere Informationen

## Literatur

1. KRITIS-FAQ: Nutzung eines bestehenden ISO 27001-Zertifikats als Bestandteil eines Nachweises gemäß § 8a Absatz 3 BSIG, Bundesamt für Sicherheit in der Informationstechnik, o.D.
2. IT-Grundschutz-Baustein (200-1): ISMS.1: Sicherheitsmanagement, Bundesamt für Sicherheit in der Informationstechnik, Februar 2023
3. Framework for Improving Critical Infrastructure Cybersecurity, NIST - National Institute of Standards and Technology, Version 1.1, April 2018

## Quellen

1. [Konkretisierung der Anforderungen an die gemäß § 8a Absatz 1 BSIG umzusetzenden Maßnahmen, Bundesamt für Sicherheit in der Informationstechnik, Version 1.0, 28.2.2020](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Kritis/Konkretisierung_Anforderungen_Massnahmen_KRITIS.pdf)
2. [Gesetz über das Bundesamt für Sicherheit in der Informationstechnik und die Sicherheit in der Informationstechnik von Einrichtungen, BSI-Gesetz vom 2. Dezember 2025](https://www.gesetze-im-internet.de/bsig_2025/)
3. Reife- und Umsetzungsgradbewertung (RUN) im Rahmen der Nachweisprüfung, Bundesamt für Sicherheit in der Informationstechnik, 09.01.2025
4. Mapping von Anforderungen aus der Konkretisierung der KRITIS-Anforderungen auf RUN-Umsetzungsgrade, Bundesamt für Sicherheit in der Informationstechnik, 09.01.2025
5. ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection - Information security management systems - Requirements
6. [OpenKRITIS](https://www.openkritis.de/)
7. [Cybersecurity in KRITIS und NIS2](https://www.openkritis.de/massnahmen/)
8. [ISMS](https://www.openkritis.de/massnahmen/information_security_management-isms-kritis.html)
9. up

OpenKRITIS ∙ Die gemeinnützige Informationsplattform für NIS2-Einrichtungen und Kritische Infrastrukturen. 50670 Köln ∙ info@openkritis.de ∙ ISSN 2748-565X

Paul Weissmann ist der Herausgeber von OpenKRITIS und publiziert seit 1999 das PA-RISC-Referenzwerk, und Insel Westberlin. OpenKRITIS hat keinen Anspruch auf Vollständigkeit oder Korrektheit und stellt keine Rechtsberatung dar.

Copyright © 2021-2026 ∙ Impressum ∙ Datenschutz ∙ Über uns und Kontakt

- Risiko-Management: Meldung von Risiken und Maßnahmen an das Unternehmens-Risiko-Management, Abgleich von Methoden und Definitionen
- Asset-Management: Abgleich von Asset-Informationen der Assets in Scope der Anlage
- BCM: Austausch von Risiken und Maßnahmen, gemeinsame Risikobehandlung und Pläne
- IT-Betrieb und IT-Sicherheit: Definition und Begleitung der Maßnahmen-Umsetzung im Betrieb; Austausch zu operativen Risiken und Bedrohungen
- IT-Notfallmanagement: Behandlungsoption für Maßnahmen zur Ausfallsicherheit; gemeinsame Sicht auf IT-Assets und deren Risiken
- Leitung: Abgleich Geltungsbereich ISMS und Geltungsbereich KRITIS; Definition der IT-Systeme und Prozesse im Scope; Zusammenarbeit im Meldewesen

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 4 -->

> aufgeführt.

<!-- page: 7 -->

> 2.3.4

> 9.2
