---
source_file: "Vorfallsmanagement-in-NIS2-und-KRITIS-OpenKRITIS.pdf"
source_sha256: f80dc82d3a3fb73916a9a535792c92518a38d423b034095697f5b26e7fd9132c
source_bytes: 320735
pages: 7
tables: 4
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-27T18:17:05+00:00"
text_coverage_percent: 100.0
appended_source_lines: 5
extraction_status: warn
warnings:
  - "5 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
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

<!-- image -->

<!-- page: 2 -->

## Vorfälle in NIS2 und KRITIS

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

<!-- image -->

Einrichtungen und Betreiber müssen Ereignisse, die zu Vorfällen, Störungen und Sicherheitsvorfällen führen können erkennen, behandeln und teilweise an Aufsichtsbehörden melden. Dazu sind durchgängige Prozesse für Vorfallsmanagement und Security Incident Management mit begleitenden Vorgaben und

<!-- page: 3 -->

## Abläfen notwendig.

- Vorfallsmanagement
- Definition
- Meldepflichten
- [Angriffserkennung](https://www.openkritis.de/massnahmen/orientierungshilfe_angriffserkennung_oh_sza.html)

NIS2 und das KRITIS-Dachgesetz vertiefen die Vorgaben zur Behandlung von Vorfällen bei regulierten Einrichtungen und Betreibern. Die folgende Ausarbeitung führt ISMS-Kernkomponenten anhand der NIS2-Anforderungen für Einrichtungen, sowie der alten KRITIS-Anforderungen von RUN-KdA aus. Als Orientierung sind die Anforderungen der Durchführungsverordnung DVO (EU) aufgeführt.

| Bereich                                                                                          | Anforderung                                                                                      | NIS2 BSIG   | KRITIS DachG   | RUN KdA       |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------|----------------|---------------|
| Vorfallsmanagement Prozesse und Vorgaben für das Incident Management von Vorfällen und Notfällen | Vorfallsmanagement Prozesse und Vorgaben für das Incident Management von Vorfällen und Notfällen | NS.6        | DG.12          | ? (77-82)     |
| Definition                                                                                       | Festlegungen zu den Kriterien meldepflichtiger Vorfälle an Aufsichtsbehörden                     | NS.6        | DG.12          | ? (77)        |
| Meldepflichten                                                                                   | Meldeweg und Pflichten für Vorfallsmeldungen an Behörden                                         | DG.23       | NS.31 DG.24    | 2/3 (97,100)  |
| Angriffserkennung                                                                                | Konkrete Vorgaben BSI Angriffserkennung bei Betreibern                                           | NS.30       |                | 3-5 (101-135) |

## Vorfallsmanagement

## Incident Management

Für die Behandlung von Sicherheitsvorfällen in Kritischen Infrastrukturen sind bei Einrichtungen und Betreibern klare Verantwortlichkeiten und Abläufe notwendig. Dazu muss ein geregeltes Incident Management mit Rollen und Prozessen für die Behandlung von Vorfällen definiert und betrieben werden.

| Anforderung                                                   | NIS2 DVO-EU   | KRITIS DachG   | ISO 27001 2022   | RUN KdA   |
|---------------------------------------------------------------|---------------|----------------|------------------|-----------|
| Verantwortlichkeiten und Vorgehensmodell                      | 3.1.1         | DG.12          | A.5.24           | 3 (77)    |
| Bearbeitung von Sicherheitsvorfällen                          | 3.5.1 3.5.2   | DG.12          | A.5.25 A.5.26    | 3 (78)    |
| Dokumentation und Berichterstattung über Sicherheitsvorfälle  | 3.3.1         | DG.12          | A.5.28           | 3 (79)    |
| Verpflichtung der Nutzer zur Meldung von Sicherheitsvorfällen | 3.3.1 3.3.2   | DG.12          | A.6.8            | 3 (81)    |

<!-- page: 4 -->

Auswertung und Lernprozess

## Rollen

Rollen und Aufgaben für Vorfälle müssen im Geltungsbereich festgelegt werden. Die Rollen können Teil vom CERT, CSIRT, SOC oder auch in der Security oder Flächenorganisation beim Betreiber sein.

- Leiter Vorfälle : Governance für und Leitung der Vorfallserkennung und -behandlung
- Vorfallsbehandlung : Reaktionsteam zur operativen Bewältigung von Vorfällen
- Notfallmanagement : Reaktives BCM zur Behandlung von Notfällen
- Störungsmanagement : Behandlung von betrieblichen Störungen

## NIS2 und KRITIS-Dachgesetz

Geregeltes Vorfallsmanagement ist sowohl in NIS2 (BSIG) für Einrichtungen und im KRITIS-Dachgesetz für Betreiber verpflichtend. Das Vorfallsmanagement nach NIS2 wird üblicherweise in Security Incident Management mit Fokus auf Sicherheitsvorfälle aus der Cybersecurity sein.

Im KRITIS-Dachgesetz ist ebenfalls Vorfallsmanagement gefordert, aber mehr für die Behandlungen von Notfällen und Beeinträchtigungen der kritischen Dienstleistung.

## Prozesse

Für den Umgang mit Störungen und Vorfällen müssen zentrale Prozesse im Betrieb der Einrichtungen Anlagen definiert werden, u.a.:

- Detektion : Störungen, Angriffe und Vorfälle müssen anhand von Logs, Mustern und Indikatoren im Betrieb erkannt und festgestellt werden
- Reaktion : Erkannte Vorfälle müssen von Fachpersonal klassifizert und behandelt, und die weitere Bewältigung eingeleitet werden (zum Incident-/Notfall-/Krisen-Management)
- Meldungen : Festgestellte V orfälle und Störungen müssen dokumentiert und gemeldet werden, falls diese meldepflichtig sind (ggf. über die Meldeorganisation)
- Auswertung : Vorfälle und Bewältigung müssen für Lessons Learned ausgewertet werden

## Nachweise

Artefakte als Nachweis für funktionierende Governance für Vorfälle sind u.a.:

1. Erkannte Angriffe
2. Bewältigte Vorfälle

<!-- formula-not-decoded -->

<!-- page: 5 -->

3. Tickets
4. Lessons Learned

up

## Definition

Für die Behandlung und Meldung von Vorfällen ist eine durchgängige Einstufung von Ereignissen und meldepflichten Vorfällen an Aufsichtsbehörden essentiell. Detektierte oder gemeldete Ereignissen müssen nach Regeln und Definitionen in Sicherheitsvorfälle und meldepflichtige Störungen hochgestuft werden können - was dann die Meldepflicht nach sich zieht.

| Anforderung                                                                                                 | NIS2   | KRITIS        | ISO 27001    | RUN    |
|-------------------------------------------------------------------------------------------------------------|--------|---------------|--------------|--------|
|                                                                                                             | DVO-EU | DachG         | 2022         | KdA    |
| Definition meldepflichtiger Vorfälle: schwerwiegende Sicherheitsvorfälle und schwerwiegende Störungen 3.4.2 | DG.23  | A.5.25 A.5.28 | A.6.8 A.8.15 | 3 (77) |

## Festlegung Kriterien

Die Kriterien für Sicherheitsvorfälle (NIS2) und Störungen/Vorfälle (KRITIS-Dachgesetz) sollten so klar, eindeutig und handelbar wie möglich definiert und zugänglich in Aufnahmebögen und Handouts für das Vorfallspersonal dokumentiert werden.

Wenn möglich, sollten die Kriterien mit der Leitung abgestimmt und freigegeben werden, und anschließend weitflächig im Rahmen der Vorfallsprozesse kommuniziert werden.

## NIS2

Einrichtungen nach NIS2 müssen erhebliche Sicherheitsvorfälle an die Aufsichtsbehörden melden. Dazu ist eine Definition der Erheblichkeit essentiell, die nach dem BSIG sehr verkürzt ist. Der EU Implementing Act, die Durchführungsverordnung kann hier als Orientierung dienen:

- Finanzieller Verlust von mehr als 500 Tsd. EUR oder 5 Prozent des Jahresumsatzes
- Abfluss von Geschäftsgeheimnissen
- Tod oder schwere Schädigung der Gesundheit einer natürlichen Person
- Unbefugter Zugriff auf Netz- und Informationssysteme → schwerwiegende Betriebsstörungen
- Wiederholte Sicherheitsvorfälle

## KRITIS-Dachgesetz

<!-- page: 6 -->

Das KRITIS-Dachgesetz definiert eine Art von meldepflichtigem Vorfall: 'ein Ereignis, das die Erbringung einer kritischen Dienstleistung erheblich beeinträchtigt oder beeinträchtigen könnte.' Ausgenommen davon sind Sicherheitsvorfälle nach NIS2 und Vorfälle nach TKG.

## up

## Meldewesen zu Behörden

Nach der Erkennung und parallel zur Behandlung von Vorfällen müssen bestimmte meldepflichtige Vorfälle an Aufsichtsbehörden gemeldet werden.

| Anforderung                                 | NIS2 DVO-EU   | KRITIS DachG   | ISO 27001 2022   | RUN KdA   |
|---------------------------------------------|---------------|----------------|------------------|-----------|
| Einrichtung einer Kontaktstelle             |               | DG.1           | A.5.5 A.5.31     | 3 (100)   |
| Meldepflicht erhebliche Sicherheitsvorfälle | NS.31         |                | A.5.5 A.5.31     |           |
| Meldepflicht erhebliche Störungen           |               | DG.23          | A.5.5 A.5.31     |           |
| Folgeinformationen                          | NS.31         | DG.23          | A.5.28 A.5.31    |           |

## Meldepflichten NIS2

Regulierte Einrichtungen und Betreiber kritischer Anlagen müssen nach NIS2 erhebliche Sicherheitsvorfälle an das BSI melden - innerhalb von 24 Stunden mit abgestuften Folge- und Abschlussmeldungen. Die Fristen und Inhalte der Meldung sind im Gesetz (BSIG) umfangreich vorgegeben - und müssen im BSI-Portal gemeldet werden.

## Meldepflichten KRITIS-Dachgesetz

Betreiber kritischer Anlagen müssen Vorfälle (erhebliche Störungen) nach dem KRITIS-Dachgesetz über die vom BSI und BBK für NIS2 eingerichtete gemeinsame Meldestelle melden - in sehr kurzen Fristen, innerhalb von 24 Stunden, und mit stufenweisen Folgemeldungen.

## Kontaktstelle

Bei Betreibern kritischer Anlagen muss eine 'jederzeit erreichbare' Kontaktstelle für das BSI eingerichtet und registriert werden. Sie nimmt eigehende Meldungen und Fragen von beiden Seiten an.

<!-- page: 7 -->

## Nachweise

Artefakte als Nachweis für ein funktionierendes Meldewesen sind u.a.:

1. Gemeldete Vorfälle
2. Dokumentierte Vorfälle
3. Quittierungen

up

## Weitere Informationen

## Quellen

1. Gesetz über das Bundesamt für Sicherheit in der Informationstechnik und die Sicherheit in der Informationstechnik von Einrichtungen, BSI-Gesetz vom 2. Dezember 2025
2. [Dachgesetz zur Stärkung der physischen Resilienz kritischer Anlagen, KRITIS-Dachgesetz vom 11. März 2026 (BGBl. 2026 I Nr. 66)](https://www.gesetze-im-internet.de/kritisdachg/index.html)
3. Reife- und Umsetzungsgradbewertung (RUN) im Rahmen der Nachweisprüfung, Bundesamt für Sicherheit in der Informationstechnik, 09.01.2025
4. Mapping von Anforderungen aus der Konkretisierung der KRITIS-Anforderungen auf RUN-Umsetzungsgrade, Bundesamt für Sicherheit in der Informationstechnik, 09.01.2025
5. ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection - Information security management systems - Requirements
6. [OpenKRITIS](https://www.openkritis.de/)
7. [Cybersecurity in KRITIS und NIS2](https://www.openkritis.de/massnahmen/)
8. [Vorfallsmanagement](https://www.openkritis.de/massnahmen/vorfallsmanagement.html)
9. up

OpenKRITIS ∙ Die gemeinnützige Informationsplattform für NIS2-Einrichtungen und Kritische Infrastrukturen. 50670 Köln ∙ info@openkritis.de ∙ ISSN 2748-565X

Paul Weissmann ist der Herausgeber von OpenKRITIS und publiziert seit 1999 das PA-RISC-Referenzwerk, und Insel Westberlin. OpenKRITIS hat keinen Anspruch auf Vollständigkeit oder Korrektheit und stellt keine Rechtsberatung dar.

Copyright © 2021-2026 ∙ Impressum ∙ Datenschutz ∙ Über uns und Kontakt

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 3 -->

> ? (77-82)

<!-- page: 4 -->

> 3.6.1

> 3.6.2

> A.5.27

<!-- page: 5 -->

> 3.4.1
