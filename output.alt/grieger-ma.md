---
source_file: "Grieger_MA.pdf"
source_sha256: 55ecdf1b3552449ef134bf4732ae6a8e377231d67cf601e643739f8eceec7cbb
source_bytes: 1441235
pages: 199
tables: 116
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T19:19:38+00:00"
text_coverage_percent: 100.0
appended_source_lines: 83
restored_hyphens: 25
extraction_status: warn
warnings:
  - "6 Tabellenzelle(n) beginnen mitten im Satz — moegliche Zellverschiebung, z. B. \"bspw. private Schlüssel) führen zu einer Störung der sichere...\". Zeilen dieser Tabelle vor dem Zitat gegen die Quelle pruefen."
  - "25 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): 2700xReihe -> 2700x-Reihe, BergerGrabner -> Berger-Grabner, ComynWattiau -> Comyn-Wattiau, GSzertifiziert -> GS-zertifiziert, GovernmentGesetze -> Government-Gesetze"
  - "Der Textlayer der Quelle enthaelt 2248 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
  - "83 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

## Erstellung eines IT-Grundschutz-Profils für eine oberste Landesbehörde in der Bundesrepublik Deutschland

RAPHAEL GRIEGER

## MASTERARBEIT

eingereicht am Fachhochschul-Masterstudiengang

INFORMATION SECURITY MANAGEMENT

in Hagenberg

im Mai 2019

<!-- page: 2 -->

© Copyright 2019 Raphael Grieger

Alle Rechte vorbehalten

<!-- page: 3 -->

## Kurzzusammenfassung

Die  Computertechnologie  verbreitet  sich  kontinuierlich  im  privaten  wie  im  Behördenumfeld  und  sorgt  dort  unter  anderem  für  Effizienzsteigerungen  und  veränderte Kommunikationsprozesse. Neben unterschiedlichen Vorteilen, wie beschleunigten und nachvollziehbaren  Kommunikationswegen,  werden  dadurch  auch  Gefährdungen  für die IT-Infrastruktur einer Organisation geschaffen, die sich in der Einschränkung von Vertraulichkeit, Integrität und Verfügbarkeit von Informationen manifestieren können. Während die obersten Landesbehörden zum einen unterschiedlichen E-GovernmentGesetzen unterliegen, sind diese zugleich aufgrund der Leitlinie für die Informationssicherheit in der öffentlichen Verwaltung verpflichtet, ein Managementsystem für Informationssicherheit umzusetzen und Sicherheitskonzeptionen zu erstellen.

Um die Umsetzung dieser Verpflichtungen zu vereinfachen, wird in der vorliegenden Arbeit eine schematische Sicherheitskonzeption in einem IT-Grundschutz-Profil erstellt. Damit wird ein generischer Geschäftsprozess der obersten Landesbehörden abgesichert. Für eine bestmögliche Vergleichbarkeit zu einem ISMS nach der ISO 27001 wird eine Absicherung auf der Ebene der Standard-Absicherung des IT-Grundschutzes durchgeführt.  Zentrale  Forschungsfrage  ist  daher,  welche  Sicherheitsanforderungen eine ISMS-Schablone für eine oberste Landesbehörde zur Erstellung und Umsetzung einer schematischen Sicherheitskonzeption der Standard-Absicherung enthalten muss.

Zum Klären der Forschungsfrage wird auf eine Befragung der Informationssicherheitsbeauftragten von 15 Landesverwaltungen und auf die bestehende Verwaltungsliteratur  zurückgegriffen.  Auf  dieser  Basis  wird  das  IT-Grundschutz-Profil  erstellt  und durch Experteninterviews mit zwei Informationssicherheitsbeauftragten oberster Landesbehörden evaluiert.

Ergebnis der vorliegenden Arbeit ist ein IT-Grundschutz-Profil, welches den Geschäftsprozess der 'Beteiligung an der Normsetzung des Landes' generisch für eine oberste Landesbehörde, unabhängig der Ressortzugehörigkeit, auf der Ebene der Standard-Absicherung absichert. Die Evaluation bestätigt die Annahmen der Referenzarchitektur und die Sicherheitsanforderungen, sodass das IT-Grundschutz-Profil, soweit möglich, für eine tatsächliche Anwendung überprüft wurde.

<!-- page: 4 -->

## Abstract

Computer technology is continuously spreading in both the private and the public sector, where it increases efficiency and changes the ways of communication. While these changes have several advantages, they also pose new threats to the IT-infrastructure of an organization. These threats can manifest in damages to the property of confidentiality, integrity and availability of information. On the one hand, the state authorities of Germany are subject to different e-government laws, on the other hand they are required by the ' Leitlinie für die Informationssicherheit in der öffentlic hen Verwaltung' to implement an information security management system and to create security concepts.

In order to simplify the implementation process of these obligations, a schematic safety concept in form of an IT-Grundschutz-Profile is created. This concept covers a generic business process for the highest level of state authorities, the ministries. For the best possible comparability to an ISMS according to the ISO 27001, the ITGrundschutz-Profile covers the organisation at the standard protection level (Standard-Absicherung). The central research question is: Which safety requirements must be included by an ISMS template for a highest state authority for the preparation and implementation of a schematic security concept on the standard level?

As research methods, a survey of information security officers from 15 state administrations is conducted and existing literature regarding administrative science is reviewed. On this basis, the IT-Grundschutz-Profile is compiled and evaluated by two expert interviews with information security officers of the highest state authorities.

The result of this thesis is an IT-Grundschutz-Profile, which describes the generic business process of the "Participation in the norm setting of the state" for a highest state authority, independently of the department competency, on the standard level. An evaluation confirms the assumptions of the reference architecture and the security requirements. Thus, IT-Grundschutz-Profile has been verified as far as possible for further application in the highest state authorities.

<!-- page: 5 -->

## Inhaltsverzeichnis

| Erklärung                                                | Erklärung                                                                                                              | Erklärung                                                                                                              | iii   |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-------|
| Kurzzusammenfassung                                      | Kurzzusammenfassung                                                                                                    | Kurzzusammenfassung                                                                                                    | iv    |
| Abstract                                                 | Abstract                                                                                                               | Abstract                                                                                                               | v     |
| Abkürzungsverzeichnis                                    | Abkürzungsverzeichnis                                                                                                  | Abkürzungsverzeichnis                                                                                                  | ix    |
| Abbildungsverzeichnis                                    | Abbildungsverzeichnis                                                                                                  | Abbildungsverzeichnis                                                                                                  | x     |
| Tabellenverzeichnis                                      | Tabellenverzeichnis                                                                                                    | Tabellenverzeichnis                                                                                                    | xi    |
| Kapitel 1 Einleitung                                     | Kapitel 1 Einleitung                                                                                                   | Kapitel 1 Einleitung                                                                                                   | 1     |
| 1.1                                                      | Ziel der Masterarbeit ................................................................................................ | Ziel der Masterarbeit ................................................................................................ | 1     |
|                                                          | 1.1.1                                                                                                                  | Problemstellung ............................................................................................           | 2     |
|                                                          | 1.1.2                                                                                                                  | Lösungsansatz IT-Grundschutz-Profil .....................................................                              | 2     |
|                                                          | 1.1.3                                                                                                                  | Forschungsfragen .........................................................................................             | 3     |
| 1.2                                                      | Forschungsrichtung und Methodik .......................................................................                | Forschungsrichtung und Methodik .......................................................................                | 4     |
|                                                          | 1.2.1                                                                                                                  | Vorgaben aus der Literatur der Design Science ......................................                                   | 4     |
|                                                          | 1.2.2                                                                                                                  | Anwendung der Vorgaben auf die Forschungsarbeit ............................                                           | 5     |
| 1.3                                                      | Begriffsbestimmungen .............................................................................................     | Begriffsbestimmungen .............................................................................................     | 6     |
|                                                          | 1.3.1                                                                                                                  | Allgemeine Begrifflichkeiten ......................................................................                    | 6     |
|                                                          | 1.3.2                                                                                                                  | Standardspezifische Definitionen ............................................................                          | 10    |
| Kapitel 2 Behördliches Informationssicherheitsmanagement | Kapitel 2 Behördliches Informationssicherheitsmanagement                                                               | Kapitel 2 Behördliches Informationssicherheitsmanagement                                                               | 12    |
| 2.1                                                      | Informationssicherheit im Kontext deutscher Behörden ................................                                  | Informationssicherheit im Kontext deutscher Behörden ................................                                  | 12    |
|                                                          | 2.1.1                                                                                                                  | Allgemeine Gefährdungslage ...................................................................                         | 12    |
|                                                          | 2.1.2                                                                                                                  | Europäische Regelungen...........................................................................                      | 13    |
|                                                          | 2.1.3                                                                                                                  | Deutsche Regelungen ................................................................................                   | 15    |
| 2.2                                                      | Standardreihe ISO 2700x ......................................................................................         | Standardreihe ISO 2700x ......................................................................................         | 16    |
|                                                          | 2.2.1                                                                                                                  | Anwendungsbereich ..................................................................................                   | 16    |
|                                                          | 2.2.2                                                                                                                  | Struktur ........................................................................................................      | 17    |
|                                                          | 2.2.3                                                                                                                  | Umsetzung auf der Basis der ISO 27001 ...............................................                                  | 18    |
|                                                          | 2.2.4                                                                                                                  | Risikomanagement .....................................................................................                 | 20    |
|                                                          | 2.2.5                                                                                                                  | Branchenspezifische Standards ................................................................                         | 23    |
| 2.3                                                      | IT-Grundschutz ......................................................................................................  | IT-Grundschutz ......................................................................................................  | 23    |
|                                                          | 2.3.1 Anwendungsbereich ..................................................................................             | 2.3.1 Anwendungsbereich ..................................................................................             | 24    |

<!-- page: 6 -->

|                                                 | 2.3.2                                                                                                          | Struktur ........................................................................................................   | 24                                                                                                        |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
|                                                 | 2.3.3                                                                                                          | Umsetzung auf der Basis des IT-Grundschutz .....................................                                    | 25                                                                                                        |
|                                                 | 2.3.4                                                                                                          | Risikomanagement .....................................................................................              | 28                                                                                                        |
|                                                 | 2.3.5                                                                                                          | Branchenspezifische Standards ................................................................                      | 29                                                                                                        |
| 2.4                                             | IT-Grundschutz-Profile als Problemlösung .......................................................               | IT-Grundschutz-Profile als Problemlösung .......................................................                    | 31                                                                                                        |
| Kapitel 3                                       | Grundlagen für das IT-Grundschutz-Profil                                                                       | Grundlagen für das IT-Grundschutz-Profil                                                                            | 33                                                                                                        |
| 3.1                                             | Architektur einer obersten Landesbehörde ........................................................              | Architektur einer obersten Landesbehörde ........................................................                   | 34                                                                                                        |
|                                                 | 3.1.1                                                                                                          | Organisatorischer Aufbau.........................................................................                   | 37                                                                                                        |
|                                                 | 3.1.2                                                                                                          | Aufgaben und Geschäftsprozesse                                                                                      | ........................................................... 38                                            |
|                                                 | 3.1.3                                                                                                          | Digitalisierung und IT-Infrastruktur                                                                                | ....................................................... 41                                                |
| 3.2                                             | Befragung als anwenderbezogene Datenerhebung ...........................................                       | Befragung als anwenderbezogene Datenerhebung ...........................................                            | 42                                                                                                        |
|                                                 | 3.2.1                                                                                                          | Methodische Grundlage ............................................................................                  | 42                                                                                                        |
|                                                 | 3.2.2                                                                                                          | Fragebogenkonzeption..............................................................................                  | 43                                                                                                        |
|                                                 | 3.2.3                                                                                                          | Umsetzung des Fragebogens ...................................................................                       | 48                                                                                                        |
|                                                 | 3.2.4                                                                                                          | Auswertung der Ergebnisse......................................................................                     | 48                                                                                                        |
| 3.3                                             | Zusammenfassung der Erhebung ........................................................................          | Zusammenfassung der Erhebung ........................................................................               | 51                                                                                                        |
| Kapitel 4                                       | Konzeption des IT-Grundschutz-Profils                                                                          | Konzeption des IT-Grundschutz-Profils                                                                               | 53                                                                                                        |
| 4.1                                             | Methodik zur Entwicklung eines IT-Grundschutz-Profils ..............................                           | Methodik zur Entwicklung eines IT-Grundschutz-Profils ..............................                                | 53                                                                                                        |
| 4.2                                             | Feststellung des Informationsverbunds ..............................................................           | Feststellung des Informationsverbunds ..............................................................                | 54                                                                                                        |
|                                                 | 4.2.1                                                                                                          | Schutzbedarfskategorien                                                                                             | ........................................................................... 54                            |
|                                                 | 4.2.2                                                                                                          | Referenzarchitektur ...................................................................................             | 56                                                                                                        |
|                                                 | 4.2.3                                                                                                          | Netzplan                                                                                                            | ...................................................................................................... 76 |
| 4.3                                             | Modellierung des Informationsverbunds ............................................................             | Modellierung des Informationsverbunds ............................................................                  | 77                                                                                                        |
|                                                 | 4.3.1                                                                                                          | Absicherung der Zielobjekte ....................................................................                    | 77                                                                                                        |
|                                                 | 4.3.2                                                                                                          | Zusätzliche Anforderungen ......................................................................                    | 79                                                                                                        |
| 4.4                                             | Risikobetrachtung des Dateiservers .....................................................................       | Risikobetrachtung des Dateiservers .....................................................................            | 80                                                                                                        |
|                                                 | 4.4.1                                                                                                          | Risikokriterien .............................................................................................       | 81                                                                                                        |
|                                                 | 4.4.2                                                                                                          | Risikoanalyse ...............................................................................................       | 83                                                                                                        |
|                                                 | 4.4.3                                                                                                          | Risikobehandlung .......................................................................................            | 87                                                                                                        |
| 4.5                                             | Zusammenfassung des IT-Grundschutz-Profils ...............................................                     | Zusammenfassung des IT-Grundschutz-Profils ...............................................                          | 91                                                                                                        |
| Kapitel 5 Überprüfung des Forschungsgegenstands | Kapitel 5 Überprüfung des Forschungsgegenstands                                                                | Kapitel 5 Überprüfung des Forschungsgegenstands                                                                     | 93                                                                                                        |
| 5.1                                             | Vorgehen in der Evaluation ..................................................................................  | Vorgehen in der Evaluation ..................................................................................       | 93                                                                                                        |
| 5.2                                             | Konzeption der Experteninterviews ...................................................................          | Konzeption der Experteninterviews ...................................................................               | 96                                                                                                        |
| 5.3                                             | Durchführung der Experteninterviews .............................................................              | Durchführung der Experteninterviews .............................................................                   | 100                                                                                                       |
| 5.4                                             | Anforderungen aus der Befragung .....................................................................          | Anforderungen aus der Befragung .....................................................................               | 101                                                                                                       |
| 5.5                                             | Ergebnis der Evaluation ...................................................................................... | Ergebnis der Evaluation ......................................................................................      | 102                                                                                                       |
| Kapitel                                         | 6 Zusammenfassung                                                                                              | 6 Zusammenfassung                                                                                                   | 103                                                                                                       |
| 6.1                                             | Erstellungsprozess des IT-Grundschutz-Profils .............................................                    | Erstellungsprozess des IT-Grundschutz-Profils .............................................                         | 103                                                                                                       |
| 6.2                                             | Veröffentlichung und Weiterführung ................................................................            | Veröffentlichung und Weiterführung ................................................................                 | 104                                                                                                       |

<!-- page: 7 -->

| Literaturverzeichnis           | Literaturverzeichnis                                                                     |   105 |
|--------------------------------|------------------------------------------------------------------------------------------|-------|
| Anhang A Befragung             | Anhang A Befragung                                                                       |   111 |
| Anhang A.1                     | Verwendeter Fragebogen ................................................................. |   111 |
| Anhang A.2                     | Antworten auf den Fragenteil I ......................................................    |   117 |
| Anhang A.3                     | Antworten auf den Fragenteil II .....................................................    |   121 |
| Anhang B IT-Grundschutz-Profil | Anhang B IT-Grundschutz-Profil                                                           |   125 |
| Anhang C Experteninterviews    | Anhang C Experteninterviews                                                              |   170 |

<!-- page: 8 -->

## Abkürzungsverzeichnis

BKA

BSI

DIN

DMS

ECSO

ENISA

Eurostat

GGO

ISB

ISLL-Bund

ISMS

ISM

ISO

IT

IT-SG

KritisV

PKS

NIS

NIS-RL

NRW

SoA

VBS

VPN

Bundeskriminalamt

Bundesamt für Sicherheit in der Informationstechnik

Deutsches Institut für Normung

Dokumentenmanagementsystem

European Cyber Security Organisation

European Union Agency for Network and Information Security

Statistisches Amt der Europäischen Union

Gemeinsame Geschäftsordnung

Informationssicherheitsbeauftragte*r

Leitlinie für die Informationssicherheit in der öffentlichen Verwaltung 2018

Managementsystem für Informationssicherheit

Informationssicherheitsmanagement

International Organization for Standardization

Informationstechnik

IT-Sicherheitsgesetz

Verordnung  zur  Bestimmung  Kritischer  Infrastrukturen  nach  dem BSI-Gesetz

Polizeiliche Kriminalitätsstatistik

Netzwerks- und Informationssicherheit

Richtlinie (EU) 2016/1148 über Maßnahmen zur Gewährleistung eines hohen gemeinsamen Sicherheitsniveaus von Netz - und Informationssystemen in der Union

Nordrhein-Westfalen

Statement of Applicability

Vorgangsbearbeitungssystem

Virtuelles Privates Netzwerk

<!-- page: 9 -->

## Abbildungsverzeichnis

| Abbildung 2.1: Die Zusammenhänge in der Normenfamilie 27000 [23, S. 19] (Reproduktion) ......................................................................................................................... 17           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Abbildung 2.2: Plan-Do-Check-Act-Zyklus der ISO 2700x, reproduziert nach Römer und Piwinger [50] ..................................................................................................................... 20     |
| Abbildung 2.3: Risikomanagementprozess nach der ISO 31000:2018 [53, S. 9] (Reproduktion) ......................................................................................................................... 21         |
| Abbildung 2.4: Die Phasen des Informationssicherheitsprozesses [64, S. 15] (Reproduktion) ......................................................................................................................... 25        |
| Abbildung 2.5: Erstellung der Sicherheitskonzeption in der Standard -Absicherung [64, S. 76] (Reproduktion) .............................................................................................................. 27 |
| Abbildung 3.1: Verwaltungsaufbau der Landesverwaltung nach Bogumil und Jann [72,                                                                                                                                              |
| S. 88] (Reproduktion) .............................................................................................................. 36                                                                                       |
| Abbildung 3.2: Aufbau einer obersten Landesbehörde nach Schamburek [69, S. 60]                                                                                                                                                |
| (Reproduktion) ......................................................................................................................... 37                                                                                   |
| Abbildung 4.1: Netzplan der Referenzarchitektur (eigene Darstellung) ......................... 76                                                                                                                             |
| Abbildung 4.2: Risikomatrix einer obersten Landesbehörde (eigene Darstellung auf                                                                                                                                              |
| Basis des BSI Standards 200-3 [65, S. 27]) ........................................................................... 83                                                                                                     |
| Abbildung 5.1: Die hierarchischen Evaluationskriterien nach Prat, Comyn-Wattiau und                                                                                                                                           |
| Akoka                                                                                                                                                                                                                         |
| [98, S. 6] (Reproduktion) ............................................................................................ 95                                                                                                     |

<!-- page: 10 -->

## Tabellenverzeichnis

| Tabelle 2.1: Anforderungen an eine Organisation aus der ISO 27001 [48, S. 37]......... 19                                        |
|----------------------------------------------------------------------------------------------------------------------------------|
| Tabelle 4.1: Schutzbedarfskategorie Normal ....................................................................... 55            |
| Tabelle 4.2: Schutzbedarfskategorie Hoch .......................................................................... 56           |
| Tabelle 4.3: Schutzbedarfskategorie Sehr Hoch ................................................................. 56               |
| Tabelle 4.4: Zielobjekt PRO01 .............................................................................................. 58  |
| Tabelle 4.5: Zielobjekt APP01 ............................................................................................... 60 |
| Tabelle 4.6: Zielobjekt APP02 ............................................................................................... 60 |
| Tabelle 4.7: Zielobjekt APP03 ............................................................................................... 61 |
| Tabelle 4.8: Zielobjekt APP04 ............................................................................................... 62 |
| Tabelle 4.9: Zielobjekt APP05 ............................................................................................... 62 |
| Tabelle 4.10: Zielobjekt APP06 ............................................................................................. 63  |
| Tabelle 4.11: Zielobjekt APP07 ............................................................................................. 64  |
| Tabelle 4.12: Zielobjekt SYS01 .............................................................................................. 64 |
| Tabelle 4.13: Zielobjekt SYS02 .............................................................................................. 65 |
| Tabelle 4.14: Zielobjekt SYS03 .............................................................................................. 66 |
| Tabelle 4.15: Zielobjekt SYS04 .............................................................................................. 66 |
| Tabelle 4.16: Zielobjekt SYS05 .............................................................................................. 66 |
| Tabelle 4.17: Zielobjekt SYS06 .............................................................................................. 67 |
| Tabelle 4.18: Zielobjekt SYS07 .............................................................................................. 67 |
| Tabelle 4.19: Zielobjekt NET01 ............................................................................................ 68   |
| Tabelle 4.20: Zielobjekt NET02 ............................................................................................ 69   |
| Tabelle 4.21: Zielobjekt NET03 ............................................................................................ 69   |
| Tabelle 4.22: Zielobjekt NET04 ............................................................................................ 70   |
| Tabelle 4.23: Zielobjekt NET05 ............................................................................................ 71   |
| Tabelle 4.25: Zielobjekt NET07 ............................................................................................ 72   |
| Tabelle 4.24: Zielobjekt NET06 ............................................................................................ 71   |
| Tabelle 4.26: Zielobjekt NET08 ............................................................................................ 72   |
| Tabelle 4.27: Zielobjekt INF01 ............................................................................................. 73  |

<!-- page: 11 -->

| Tabelle 4.28: Zielobjekt INF02 ............................................................................................. 73                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tabelle 4.29: Zielobjekt INF03 ............................................................................................. 74                                                                              |
| Tabelle 4.30: Zielobjekt INF04 ............................................................................................. 74                                                                              |
| Tabelle 4.31: Zielobjekt INF05 ............................................................................................. 75                                                                              |
| Tabelle 4.32: Zielobjekt INF06 ............................................................................................. 75                                                                              |
| Tabelle 4.33: Modellierung der Referenzarchitektur .......................................................... 78                                                                                             |
| Tabelle 4.34: Anmerkungen zu der Modellierung des Informationsverbundes ............ 80                                                                                                                      |
| Tabelle 4.35: Zielobjekte für eine Risikoanalyse ................................................................. 81                                                                                        |
| Tabelle 4.36: Risikokriterium der Eintrittshäufigkeit ......................................................... 82                                                                                           |
| Tabelle 4.37: Risikokriterium der Schadenshöhe ................................................................ 82                                                                                           |
| Tabelle 4.38: Risikokategorien nach dem Standard 200-3 ................................................ 82                                                                                                   |
| Tabelle 4.39: Elementare Gefährdungen für den Dateiserver .......................................... 86                                                                                                      |
| Tabelle 4.40: Einschätzung der elementaren Gefährdungen für den Dateiserver ........ 87                                                                                                                      |
| Tabelle 4.41: Risikobehandlung der Gefährdungen des Dateiservers ............................. 91                                                                                                            |
| Tabelle 5.1: Gegenüberstellung der besonderen Anforderungen und der Berücksich- tigung im IT-Grundschutz-Profil ........................................................................................ 102 |

<!-- page: 12 -->

## Kapitel 1 Einleitung

Seit der Erfindung des ersten Computers im 20. Jahrhundert hat sich die Nutzung der Computertechnologie zu einem wesentlichen Wettbewerbsfaktor auf dem Weltmarkt entwickelt. Selbiges gilt für das damit zusammenhängende Internet, welches zunächst Universitäts-Netzwerke miteinander verband und mittlerweile als Kommunikationsverbindung in vielen Behörden, Unternehmen und Haushalten zu finden ist [1, S. 205-207].

Diese fortschreitende Vernetzung geht ebenfalls aus den Zahlen des Statistischen Amtes der Europäischen Union (Eurostat) hervor. Im Jahr 2007 hatten, laut Eurostat, durchschnittlich  55% der europäischen Haushalte einen Internetzugang. Zehn Jahre später sind nunmehr durchschnittlich 87% der Haushalte an das Internet angeschlossen [2]. Aus der Unternehmensperspektive verhält es sich ähnlich. Demnach hatten 77% der Wirtschaftsunternehmen in 2007 eine Breitbandverbindung zum Internet, im Jahr 2017 ist diese Zahl auf 96% gestiegen [3]. In diesem Zusammenhang argumentieren Berghaus, Kessler, Dmitriyev und Gómes, dass die zunehmende Digitalisierung der Geschäftsprozesse einen erfolgsentscheidenden Faktor für Unternehmen darstellt [4, S. 428-430].

Die deutschen Verwaltungen setzen sich ebenfalls mit der Digitalisierung auseinander. Nicht zuletzt die Bürger erwarten die digitale Abwicklung verschiedener behördlicher Interaktionen, besonders in den Bereichen Steuern/Finanzen, Meldewesen und Auto/Verkehr [5, S. 985-986]. Martini rechnet dazu auf hypothetischer Basis vor, dass in Deutschland durch Behördengänge jährlich etwa 6,2 Milliarden Euro an Verdienstausfall entstehen und fordert eine fortschreitende Digitalisierung der Verwaltung [6, S. 443-444].

Stember und Hesse betrachten den aktuellen Stand der Digitalisierung der Verwaltung bzw. des E-Governments in Deutschland als kritisch und hinter anderen Mitgliedsstaaten der Europäischen Union (EU) zurückliegend [7, S. 79-81]. Seitens des Bundesgesetzgebers und der meisten Bundesländer sind daher entsprechende E-Government-Gesetze für die Digitalisierung der Verwaltung verabschiedet worden [8, S. 167].

## 1.1 Ziel der Masterarbeit

Ausgehend von der fortschreitenden Digitalisierung entstehen in öffentlichen Verwaltungen neue Angriffsflächen und andere Risikopotenziale. Das folgende Unterkapitel stellt dar, weshalb Informationssicherheit insbesondere für oberste Landesbehörden relevant ist und welche Verpflichtungen für oberste Landesbehörden bestehen, ein Managementsystem für Informationssicherheit (ISMS) umzusetzen. Diese Verpflichtungen stellen die zentrale Problemstellung und Motivation dieser Masterarbeit dar.

<!-- page: 13 -->

Darauf aufbauend wird auf das Konzept der IT-Grundschutz-Profile eingegangen und es wird betrachtet, ob diese eine Lösung für die Problemstellung darstellen. Dies mündet in der Formulierung der zentralen Forschungsfragen für die vorliegende Arbeit.

## 1.1.1 Problemstellung

Mit einem ISMS kann eine Organisation die Sicherstellung von Informationssicherheit auf strategischer und organisatorischer Ebene umsetzen [9, S. 2]. Für eine Umsetzung eines ISMS gibt es indes unterschiedliche Gründe. So steht ein ISMS den Organisationen als technisch-organisatorische Maßnahme offen, die der Verordnung zur Bestimmung Kritischer Infrastrukturen nach dem BSI-Gesetz (KritisV) unterliegen und demnach zu Maßnahmen zur Absicherung ihrer IT-Infrastruktur verpflichtet sind [10, S. 810-811]. Andere Unternehmen entscheiden sich für ein ISMS, weil aus einer entsprechenden Zertifizierung des ISMS wirtschaftliche Vorteile zu erwarten sind [11].

Um ein gemeinsames Sicherheitsniveau in der Informationssicherheit zu etablieren, die Ebenen-übergreifende Kommunikation abzusichern und das Risiko der Kompromittierung der elektronischen Kommunikationskanäle zu senken, wurde für die Verwaltungen des Bundes und der Länder die Leitlinie für die Informationssicherheit in der öffentlichen Verwaltung im Jahr 2013 verabschiedet und 2018 aktualisiert [12]. Die Leitlinie in ihrer Fassung aus dem Jahr 2018 wird fortan als ISLL-Bund bezeichnet.

Die ISLL-Bund verpflichtet die Verwaltungen des Bundes und der Länder zu dem Betrieb eines ISMS [12, S. 11] auf der Grundlage des IT-Grundschutzes oder der ISO 2700x-Reihe [12, S. 9]. Dementsprechend sind davon die obersten Landesbehörden und die ihnen nachgeordneten Behörden betroffen.

Die obersten Landesbehörden stehen an der Spitze der Verwaltungshierarchie eines Landes und unterstehen, durch einen Minister als Behördenleitung, in der Regel direkt der Landesregierung [13, S. 50]. Aufgrund der ISLL-Bund sind diese verpflichtet ein ISMS  zu  betreiben,  entsprechende  Sicherheitskonzeptionen  zu  erstellen  und  ausreichende Ressourcen bereitzustellen [12, S. 9].

## 1.1.2 Lösungsansatz IT-Grundschutz-Profil

Das Bundesamt für Sicherheit in der Informationstechnik (BSI) hat im Rahmen der ISMS-Methodik des IT-Grundschutzes begonnen, sogenannte IT-Grundschutz-Profile zu etablieren. Ziel der IT-Grundschutz-Profile ist, den zeitlichen und personellen Aufwand bei der Erstellung der Sicherheitskonzeptionen in einem ISMS nach dem ITGrundschutz zu reduzieren [14].

IT-Grundschutz-Profile stellen eine ISMS-Schablone für Organisationen mit ähnlichen Anforderungen dar [15]. Ein IT-Grundschutz-Profil soll folgende Schritte des Sicherheitsprozesses beinhalten [16, S. 4]:

1. Die Festlegung des Anwendungsbereichs.

<!-- page: 14 -->

2. Die Durchführung einer allgemeinen Strukturanalyse.
3. Die Feststellung von Zielobjekten.
4. Eine Schutzbedarfsfeststellung der Zielobjekte.
5. Eine Auswahl von passenden IT-Grundschutz-Bausteinen (Modellierung).
6. Eine Beschreibung spezifischer Anforderungen und Maßnahmen.
7. Gegebenenfalls eine Risikoanalyse und -behandlung.

Im Detail wird auf diese Schritte der IT-Grundschutz-Methodik im Kapitel 2 der Masterarbeit eingegangen. Der IT-Grundschutz unterteilt die Erstellung der Sicherheitskonzeption in drei unterschiedliche Absicherungsgrade: Die Basis-Absicherung, die Kern-Absicherung und die Standard-Absicherung.

Für  die  schematische  Sicherheitskonzeption  eines  IT-Grundschutz-Profils  muss ebenfalls festgelegt werden, welcher dieser drei Absicherungsgrade erreicht werden soll. Da in der ISLL-Bund neben dem IT-Grundschutz auch die ISO 2700x-Reihe als ISMS-Methodik aufgeführt wird, wird das IT-Grundschutz-Profil auf Basis der Standard-Absicherung erstellt. Denn gemäß dem BSI ist ein ISMS basierend auf dem IT-Grundschutz ausschließlich in der Standard-Absicherung mit einem ISMS nach der ISO/IEC 27001:2013 (fortan ISO 27001) vergleichbar [17, S. 1].

Die Grundannahme für das IT-Grundschutz-Profil ist eine organisationsübergreifende Ähnlichkeit in Struktur und Aufgaben der obersten Landesbehörden, sodass die schematische Sicherheitskonzeption auf der Basis dieser Gemeinsamkeiten erstellt werden kann.

Die obersten Landesbehörden sind, wie oben erwähnt, als Teil der Landesverwaltung durch die ISLL-Bund zu dem Betrieb eines ISMS verpflichtet. Mit der schematischen  Sicherheitskonzeption  des  IT-Grundschutz-Profils  wird  die  Umsetzung  eines ISMS und die Erstellung der Sicherheitskonzeption auf der Basis des IT-Grundschutz vereinfacht. Ferner können sich Verwaltungen, die ein ISMS nach der ISO 27001 betreiben, an den Anforderungen aus dem IT-Grundschutz-Profil in einer Vollständigkeitsprüfung orientieren.

## 1.1.3 Forschungsfragen

Um die obersten Landesbehörden bei der Umsetzung des ISMS und der Erstellung einer Sicherheitskonzeption durch ein IT-Grundschutz-Profil zu unterstützen, bedarf es einer Informationsgrundlage für die Erstellung dieser Schablone.

Leitende  Forschungsfrage  ist: Welche  Sicherheitsanforderungen  muss  eine ISMS-Schablone  für  eine  oberste  Landesbehörde  zur  Erstellung  und  Umsetzung  einer  schematischen  Sicherheitskonzeption  der  Standard-Absicherung enthalten?

Darauf aufbauend lassen sich folgende Leitfragen feststellen, die für die Erstellung des IT-Grundschutz-Profils benötigt werden:

- Über  welche  gemeinsamen  Aufgaben  und  Geschäftsprozesse  verfügen  die obersten Landesbehörden?

<!-- page: 15 -->

- Welcher Geschäftsprozess könnte mit einem IT-Grundschutz-Profil betrachtet und abgesichert werden?
- Welche Informationen, Anwendungen, IT-Systeme, Netze und Infrastruktur sind üblicherweise vorzufinden und abzusichern?
- Welche Schutzbedarfe bestehen für diese Objekte?
- Wie stellt sich die Risikobereitschaft in einer obersten Landesbehörde dar?
- Gibt es zusätzliche Anforderungen für die Anwendung dieses schematischen ISMS auf eine oberste Landesbehörde?

Die  Masterarbeit  beschäftigt  sich  in  den  Folgekapiteln  mit  der  Klärung  dieser  Forschungsfragen und nutzt die so erhobenen Informationen für die Erstellung des ITGrundschutz-Profils.

## 1.2 Forschungsrichtung und Methodik

Vor der Erstellung der Forschungsarbeit ist methodisch einzugrenzen, ob diese in die Forschungsrichtung Verhaltensforschung oder Design Science einzuordnen ist. Ferner sind die dortigen Vorgehensweisen und Prozesse einzuhalten, um eine wissenschaftlich fundierte Ausarbeitung sicherzustellen.

Die Verhaltensforschung gliedert sich nach March und Smith in die Forschungsschritte ' Discovery ' und ' Justification ' , die anhand von Hypothesen versucht, die Realität zu erklären [18, S. 253]. In der Design Science soll dagegen ein wichtiges organisatorisches Problem mit einem sinnvollen Artefakt gelöst werden [19, S. 82].

Gemessen an diesen kurzen Darstellungen der beiden Forschungsrichtungen lässt sich die Erstellung eines IT-Grundschutz-Profils in den Forschungsbereich der Design Science einordnen. Das zu lösende Problem ist die Verpflichtung der obersten Landesbehörden, ein ISMS zu betreiben und eine Sicherheitskonzeption zu erstellen sowie umzusetzen. Das IT-Grundschutz-Profil dient als Artefakt, um dieses Problem durch eine Vereinfachung der Erstellung der Sicherheitskonzeption mindestens in Teilaspekten zu lösen.

## 1.2.1 Vorgaben aus der Literatur der Design Science

Grundlegender Teil des Design Science Forschungsprozesses ist ein Artefakt, welches in der Forschungsarbeit erstellt wird. Artefakte können nach Baskerville et al. in vier Formen vorliegen [20, S. 362]:

- Konstrukte, die  die  grundlegende  Sprache  zur  Beschreibung  der  Forschung und des Problems darstellen.
- Modelle, die eine Kombination aus mehreren Konstrukten sind, um tatsächliche Aufgaben, Situationen oder Artefakte zu beschreiben.
- Methoden, die die Durchführung mehrerer Aktivitäten zu der Erreichung eines Zieles enthalten.

<!-- page: 16 -->

- Instanziierungen, als praktisch umgesetzte Artefakte, welche Konstrukte, Modelle und Methoden verwenden, um Aufgaben zu erfüllen.

March und Smith unterteilen den Design Science Forschungsprozess in zwei Schritte: ' build ' und 'evaluate' [18, S. 259-262]. Peffers, Tuunanen, Rothenberger und Chatterjee beschreiben in einer jüngeren Ausarbeitung den Design Science Forschungsprozess in den nachfolgend aufgeführten sechs Schritten [21, S. 12-14]:

1. Der Forschungsprozess beginnt mit der Problemidentifizierung und Darstellung  der Problemrelevanz .  Ziel  ist  die  Nachvollziehbarkeit  der  Motivation und der Begründungen innerhalb der Forschungsarbeit.
2. Anschließend werden Ziele für  die Lösung in Form des Artefakts definiert. Mithilfe dessen wird das Ziel der Arbeit festgelegt und möglichst messbar gestaltet.
3. Es folgt die Erstellung und Entwicklung des Artefakts. Hier merken die Autoren an, dass, neben Konstrukten, Modellen, Methoden und Instanziierungen, jedes Objekt ein Artefakt sein könnte, sofern in dessen Entwicklung die Design Science Methodik eingeflossen ist.
4. Nach der Erstellung und Entwicklung des Artefakts folgt die Demonstration . Dadurch soll der Nutzen des Artefakts durch die Problemlösung, beispielsweise in einem Experiment oder einer Simulation, dargestellt werden.
5. Ebenso muss die Anwendbarkeit des Artefakts zur Problemlösung evaluiert werden. Unter anderem soll betrachtet werden, zu welchem Grad das Artefakt zur Problemlösung beiträgt. Sollte die Evaluation fehlschlagen, ist das Artefakt weiter zu verbessern.
6. Letztlich obliegt dem Forscher die Kommunikation des Problems, dessen Relevanz  und  des  Forschungsprozesses  mit  relevanten  Parteien  und  der  Forschungsgemeinschaft. Von der Kommunikation wird auch das Artefakt selbst umfasst.

## 1.2.2 Anwendung der Vorgaben auf die Forschungsarbeit

Mit dem IT-Grundschutz-Profil wird ein Artefakt erstellt. Gemäß der obigen Definitionen nach March und Smith ist dieses Artefakt als eine Methode einzuordnen. Winter argumentiert in diesem Zusammenhang, dass eine Unterscheidung  zwischen Modell und Methode zum Teil nicht möglich ist [22, S. 472]. Da es sich bei dem ITGrundschutz-Profil um eine umfangreiche Anwendung von Konstrukten und Modellen handelt, wird letztlich von einer Methode als Artefakt ausgegangen.

Nach der Darstellung des Design Science Forschungsprozesses von Peffers, Tuunanen, Rothenberger und Chaterjee orientiert diese Arbeit an deren Modell:

- Die Problemidentifizierung und -relevanz wird in Unterkapitel 1.1 und 2.1 dargestellt.

<!-- page: 17 -->

- Mit der Forschungsfrage aus Unterkapitel 1.1.3 und der Zielsetzung des ITGrundschutz-Profils in Kapitel 3 wird ebenso eine Zielsetzung für das Artefakt durchgeführt.
- Die Kapitel 2 und 3 dienen der Vorbereitung der Erstellung des IT-Grundschutz-Profil durch die Aggregierung von Wissen aus unterschiedlichen Quellen. In Kapitel 4 folgt darauf die Erstellung des Artefakts .
- In Kapitel 5 wird eine Evaluierung des Artefakts auf Basis von Experteninterviews durchgeführt.
- Während der Forschungsarbeit wird mit Ansprechpartnern aus dem BSI, den Landesverwaltungen und obersten Landesbehörden kommuniziert und eine praxisnahe Erstellung des Artefakts sichergestellt. Nach Fertigstellung des Artefakts wird dieses durch das BSI für eine übergreifende Anwendung, Kommentierung und Verbesserung veröffentlicht .

Damit werden fünf der sechs Prozessschritte in der vorliegenden Arbeit berücksichtigt. Eine Demonstration des Artefakts durch eine Implementierung findet aufgrund des zeitlichen und organisatorischen Umfangs in einer Organisation nicht statt.

## 1.3 Begriffsbestimmungen

Aufgrund  unterschiedlicher  Standards  und  Veröffentlichungen  wird  zum  Abschluss der Einleitung eine Definition der relevantesten Begriffe im Kontext der Masterarbeit vorgenommen. Quellen für die Definitionen sind das IT-Grundschutz-Kompendium des BSI, der Standard ISO/IEC 27000:2018 (fortan ISO 27000) der International Organization for Standardisation (ISO) und der ISO Guide 73. Nach einer Definition  der  Begriffe  in  diesem  Unterkapitel  werden  die  jeweils  ausgewählten  Begriffe nachfolgend angewendet.

## 1.3.1 Allgemeine Begrifflichkeiten

Es kommt in dem ISMS-Standard ISO 27000 sowie dem IT-Grundschutz zum Teil zu überschneidenden Definitionen. Zunächst wird daher auf überschneidende Begrifflichkeiten eingegangen.

## 1.3.1.1 Informationssicherheit

Der ISO Standard 27000 definiert unter Punkt 3.28 Informationssicherheit als:

'preservation of confidentiality, integrity and availability of information' [23, S. 4]

Gemäß den Anmerkungen zu dieser Definition können zusätzliche Schutzziele wie Authentizität, Zurechenbarkeit, Nicht-Abstreitbarkeit und Verlässlichkeit relevant sein. Das IT-Grundschutz-Kompendium gibt zur Informationssicherheit folgendes an:

'Informationssicherheit hat den Schutz von Informationen als Ziel. Dabei können Informationen sowohl auf Papier, in Rechnern oder auch in Köpfen gespeichert sein. Die Schutzziele oder auch Grundwerte der Informationssicherheit sind Vertraulichkeit, Integrität  und  Verfügbarkeit.  Viele  Anwender  ziehen  in  ihre  Betrachtungen  weitere Grundwerte mit ein.' [24, S. 63]

<!-- page: 18 -->

Wie die ISO beschränkt das BSI Informationssicherheit nach dem dortigen Verständnis auf die Schutzziele Vertraulichkeit, Integrität und Verfügbarkeit. Der Begriff der Informationssicherheit wird folglich im Sinne der ISO 27000 verstanden.

## 1.3.1.2 Informationssicherheitsmanagementsystem

Während der ISO Standard 27000 den Begriff des ISMS selbst nicht konkret definiert, liegt im IT-Grundschutz-Kompendium eine Definition vor. Dementsprechend wird ein Informationssicherheitsmanagementsystem wie folgt definiert:

' Die Planungs-, Lenkungs- und Kontrollaufgabe, die erforderlich ist, um einen durchdachten  und  wirksamen  Prozess  zur  Herstellung  von  Informationssicherheit  aufzubauen und kontinuierlich umzusetzen, wird als Informationssicherheitsmanagement bezeichnet. Dabei handelt es sich um einen kontinuierlichen Prozess, dessen Strategien und Konzepte ständig auf ihre Leistungsfähigkeit und Wirksamkeit zu überprüfen und bei Bedarf fortzuschreiben sind. ' [24, S. 63]

## 1.3.1.3 Vertraulichkeit

Die ISO 27000 definiert Vertraulichkeit als:

'property that information is not made available or disclosed to unauthorized individuals, entities, or processes' [23, S. 2]

Im IT-Grundschutz wird Vertraulichkeit wie folgt definiert:

'Vertraulichkeit ist der Schutz vor unbefugter Preisgabe von Informationen. Vertrauliche Daten und Informationen dürfen ausschließlich Befugten in der zulässigen Weise zugänglich sein. ' [24, S. 70]

Beide Definitionen haben ähnliche Inhalte, sodass letztlich die Definition des IT-Grundschutzes verwendet wird.

## 1.3.1.4 Integrität

Die ISO 27000 beschreibt Integrität als:

'property of accuracy and completeness' [23, S. 5]

Dem gegenüber steht die Definition des IT-Grundschutz-Kompendiums:

'Integrität bezeichnet die Sicherstellung der Korrektheit (Unversehrtheit) von Daten und der korrekten Funktionsweise von Systemen. Wenn der Begriff Integrität auf 'Daten' angewend et wird, drückt er aus, dass die Daten vollständig und unverändert sind. In der Informationstechnik wird er in der Regel aber weiter gefasst und auf 'Informationen' angewendet.' [24, S. 64]

<!-- page: 19 -->

Aufgrund der besseren Verständlichkeit wird auf die Definition des BSI zurückgegriffen.

## 1.3.1.5 Verfügbarkeit

Als letztes Schutzziel der Informationssicherheit (s. 1.3.1) wird auf die Verfügbarkeit eingegangen. Die ISO 27000 definiert diese als:

'property of being accessible and usable on demand by an authorized entity' [23, S. 2]

Dem gegenüber definiert das BSI die Verfügbarkeit als:

' Die Verfügbarkeit von Dienstleistungen, Funktionen eines IT-Systems, IT-Anwendungen oder IT-Netzen oder auch von Informationen ist vorhanden, wenn diese von den Anwendern stets wie vorgesehen genutzt werden können. ' [24, S. 70]

Aufgrund der besseren Verständlichkeit wird die Definition der ISO 27000 in dieser Masterarbeit angewendet.

## 1.3.1.6 Risiko

Eine zentrale Komponente eines ISMS nach der ISO 27001 ist das Risikomanagement [25, S. 42]. Die ISO definiert Risiko in dem Vokabular zum Risikomanagement (ISO Guide 73) als:

```
' [the] effect of uncertainty on objectives' [26, S. 1]
```

Eine Erläuterung zu dem Risikobegriff stammt dagegen aus der Definition des ITGrundschutz-Kompendiums:

' Risiko wird häufig definiert als die Kombination (also dem Produkt) aus der Häufigkeit, mit der ein Schaden auftritt und dem Ausmaß dieses Schadens. Der Schaden wird häufig als Differenz zwischen einem geplanten und ungeplanten Ergebnis dargestellt. Risiko ist eine spezielle Form der Unsicherheit oder besser Unwägbarkeit.

In der ISO wird Risiko auch als das Ergebnis von Unwägbarkeiten auf Zielobjekte definiert. In diesem Sinne wird daher auch von Konsequenzen statt von Schaden gesprochen,  wenn  Ereignisse  anders  eintreten  als  erwartet.  Hierbei  kann  eine Konsequenz negativ (Schaden) oder positiv (Chance) sein. Die obige Definition hat sich allerdings als gängiger in der Praxis durchgesetzt.

Im Unterschied zu 'Gefährdung' umfasst der Begriff 'Risiko' bereits eine Bewertung, inwieweit ein bestimmtes Schadensszenario im jeweils vorliegenden Fall relevant ist. ' [24, S. 66]

In diesem Fall wird der Risikobegriff des IT-Grundschutz-Kompendiums für diese Masterarbeit verwendet.

## 1.3.1.7 Risikomanagement

Auf dem Risikobegriff setzt das Risikomanagement auf. Der ISO Guide 73 definiert ein Risikomanagement als:

<!-- page: 20 -->

'coordinated activities to direct and control an organization with regard to risk' [24] [26, S. 2]

Im IT-Grundschutz wird hingegen unter Risikomanagement folgendes definiert:

' Als Risikomanagement werden alle Aktivitäten mit Bezug auf die strategische und operative Behandlung von Risiken bezeichnet, also alle Tätigkeiten, um Risiken für eine Institution zu identifizieren, zu steuern und zu kontrollieren.

Das strategische Risikomanagement beschreibt die wesentlichen Rahmenbedingungen, wie die Behandlung von Risiken innerhalb einer Institution, die Kultur zum Umgang mit Risiken und die Methodik ausgestaltet sind. Diese Grundsätze für die Behandlung von Risiken innerhalb eines ISMS müssen mit den Rahmenbedingungen des organisationsweiten Risikomanagements übereinstimmen bzw. aufeinander abgestimmt sein. ' [24, S. 67]

Hier wird ebenfalls der Begriff des Risikomanagements nach dem IT-Grundschutz aufgegriffen und fortan verwendet.

## 1.3.1.8 Anforderung

Beide ISMS-Methodiken stellen Anforderungen an das ISMS einer Organisation. Unter einer Anforderung (englisch: requirement) versteht die ISO 27000:

'need or expectation that is stated, generally implied or obligatory' [23, S. 7]

Der IT-Grundschutz verwendet in diesem Zusammenhang den Begriff der Sicherheitsanforderungen:

' Als Sicherheitsanforderung werden Anforderungen für den organisatorischen, personellen, infrastrukturellen und technischen Bereich bezeichnet, deren Erfüllung zur Erhöhung der Informationssicherheit notwendig ist bzw. dazu beiträgt. Eine Sicherheitsanforderung beschreibt also, was getan werden muss, um ein bestimmtes Niveau bezüglich der Informationssicherheit zu erreichen. Wie die Anforderungen im konkreten Fall erfüllt werden können, ist in entsprechenden Sicherheitsmaßnahmen beschrieben (siehe dort). Im englischen Sprachraum wird für Sicherheitsanforderungen häufig der Begriff 'control' verwendet.

Der IT-Grundschutz unterscheidet zwischen Basis-Anforderungen, Standard-Anforderungen und Anforderungen bei erhöhtem Schutzbedarf. Basis-Anforderungen sind fundamental und stets umzusetzen, sofern nicht gravierende Gründe dagegensprechen. Standard-Anforderungen sind für den normalen Schutzbedarf grundsätzlich umzusetzen, sofern sie nicht durch mindestens gleichwertige Alternativen oder die bewusste Akzeptanz des Restrisikos ersetzt werden. Anforderungen bei erhöhtem Schutzbedarf sind exemplarische Vorschläge, was bei entsprechendem Schutzbedarf zur Absicherung sinnvoll umzusetzen ist. ' [24, S. 68]

In dem Kontext der IT-Grundschutz-Profile wird bei der Begrifflichkeit Anforderung und Sicherheitsanforderung von der Interpretation des BSI ausgegangen.

<!-- page: 21 -->

## 1.3.2 Standardspezifische Definitionen

Neben den allgemein verwendeten Begrifflichkeiten beider ISMS-Methodiken, gibt es weitere Begriffe, die nur im Kontext einer Methodik verwendet werden. Da die ISO 2700x-Reihe im Kapitel 2 der Maserarbeit erläutert wird, werden die dort verwendeten Begriff in diesem Kapitel ebenfalls berücksichtigt. Maßgeblich relevant für die Masterarbeit sind indes Begrifflichkeiten des IT-Grundschutz ' .

## 1.3.2.1 Asset

Die ISO 27000 verwendet den Begriff des 'Assets' in Definitionen anderer Begriffe sowie im Standard 27001 für die Beschreibung des Vorgehens. Dennoch wird das Wort 'Asset' weder in der englischen noch in der deutschsprachigen Version der Standardreihe definiert.

Das BSI definiert ' Asset ' wie folgt:

' Als  Assets  werden  Bestände  von  Objekten  bezeichnet,  die  für  einen  bestimmten Zweck, besonders zur Erreichung von Geschäftszielen, benötigt werden. Der englische Begriff 'asset' wird häufig mit 'Wert' übersetzt. Wert ist allerdings im Deutschen ein mit vielen Bedeutungen belegter Begriff - von der gesellschaftlichen Bedeutung, die einer Sache zukommt, bis hin zur inneren Qualität eines Objekts. Im IT-Grundschutz wird der Begriff 'Assets' in der Bedeutung von 'werthaltigen bzw. wertvollen Zielobjekten' verwendet. ' [24, S. 59]

Auch wenn die ISO 27001 den Begriff 'Asset' wiederholt verwendet , wird auf diesen Begriff aufgrund der Ausrichtung der Masterarbeit am IT-Grundschutz nicht zurückgegriffen.

## 1.3.2.2 Informationsverbund

Mit dem IT-Grundschutz-Profil werden Geschäftsprozesse und Informationsverbünde abgedeckt [16, S. 9]. Bei Informationsverbünden handelt es sich im IT-Grundschutz um:

' Unter einem Informationsverbund ist die Gesamtheit von infrastrukturellen, organisatorischen, personellen und technischen Objekten zu verstehen, die der Aufgabenerfüllung  in  einem  bestimmten  Anwendungsbereich  der  Informationsverarbeitung  dienen. Ein Informationsverbund kann dabei als Ausprägung die gesamte Institution oder auch einzelne Bereiche, die durch organisatorische Strukturen (z. B. Abteilungen) oder gemeinsame Geschäftsprozesse bzw. Anwendungen (z. B. Personalinformationssystem) gegliedert sind, umfassen. ' [24, S. 63]

## 1.3.2.3 Zielobjekt

Während der Begriff des Assets eine zentrale Bedeutung in der ISO 2700x-Reihe hat, ist der Begriff des Zielobjekts ausschließlich im IT-Grundschutz zu finden:

Zielobjekte sind Teile des Informationsverbunds, denen im Rahmen der Modellierung ein oder mehrere Bausteine aus dem IT-Grundschutz-Kompendium zugeordnet werden können. Zielobjekte können dabei physische Objekte sein, wie beispielsweise Netze oder IT-Systeme. Häufig sind Zielobjekte jedoch logische Objekte, wie z. B. Organisationseinheiten, Anwendungen oder der gesamte Informationsverbund. [24, S. 71]

<!-- page: 22 -->

Der Begriff umfasst somit die Anteile des Informationsverbunds einer Organisation, die mit dem IT-Grundschutz-Kompendium abgebildet werden können. Die Definition des BSI wird im Zusammenhang der Masterarbeit erweitert und ebenfalls auf alle  identifizierbaren  Objekte  angewandt,  unabhängig  von  einem  bestehenden  ITGrundschutz-Baustein.

## 1.3.2.4 Geschäftsprozess

Der IT-Grundschutz sieht für die Feststellung der vorhandenen Informationen und die IT-Strukturanalyse einen prozessorientierten Ansatz vor, der für die Bestimmung der Schutzbedarfe Bedeutung hat [27, S. 62]. Das BSI definiert einen Geschäftsprozess wie folgt:

' Ein Geschäftsprozess ist eine Menge logisch verknüpfter Einzeltätigkeiten (Aufgaben, Arbeitsabläufe), die ausgeführt werden, um ein bestimmtes geschäftliches oder betriebliches Ziel zu erreichen. ' [24, S. 62]

## 1.3.2.5 IT-System

Auch wenn der Begriff der ' IT-Systeme ' verbreitet ist, so zum Beispiel in Gablers Lexikon für Unternehmensberatung [28], so umfasst dieser im Bereich des IT-Grundschutz eine bestimmte Art von Objekten:

'IT -Systeme sind technische Anlagen, die der Informationsverarbeitung dienen und eine abgeschlossene Funktionseinheit bilden. Typische IT-Systeme sind Server, Clients, Einzelplatz-Computer, Mobiltelefone, Router, Switches und Sicherheitsgateways. ' [24, S. 64]

## 1.3.2.6 Infrastruktur

Zuletzt wird auf den Begriff Infrastruktur eingegangen. Während dieser die gleiche Bedeutung wie der Begriff des Informationsverbunds zu haben scheint, unterscheiden sich diese Definitionen:

' Beim IT-Grundschutz werden unter Infrastruktur die für die Informationsverarbeitung und die IT genutzten Gebäude, Räume, Energieversorgung, Klimatisierung und die Verkabelung verstanden. Die IT-Systeme und Netzkoppelelemente gehören nicht dazu. ' [24, S. 63]

<!-- page: 23 -->

## Kapitel 2 Behördliches Informationssicherheitsmanagement

Wie in Kapitel 1 dargestellt, schreitet die Digitalisierung im privaten Umfeld wie in der Verwaltung und Wirtschaft kontinuierlich voran. Da die obersten Landesbehörden Betrachtungsgegenstand dieser Masterarbeit sind, wird zunächst auf deren allgemeine Gefährdungslage eingegangen. Zugleich gibt es Regelungen der EU und der Bundesrepublik Deutschland, um die Netz- und Informationssicherheit im europäischen und deutschen Raum zu erhöhen. Da diese Regelungen auch auf die obersten Landesbehörden zutreffen können, werden diese im Anschluss dargestellt.

Unter anderem verpflichten diese Regelungen ausgewählte Unternehmen und Behörden zu der Umsetzung eines ISMS. Um ein ISMS umzusetzen, stehen Organisationen unterschiedliche Standards mit Anforderungen, Handlungs- sowie Umsetzungsanweisungen zur  Verfügung. Da  in der ISLL-Bund  die  ISO  2700x-Reihe  und  der  ITGrundschutz als Mindeststandards aufgezählt werden [12, S. 9], werden diese ISMS-Methodiken im zweiten und dritten Unterkapitel erläutert.

## 2.1 Informationssicherheit im Kontext deutscher Behörden

In der Einleitung sind die zunehmende Digitalisierung und Vernetzung der Geschäftswelt dargestellt. Diese Entwicklung kann einerseits zu einer größeren wirtschaftlichen Leistungsfähigkeit und Effizienz von Behörden führen [29, S. 14-15], andererseits können sich daraus resultierende Gefährdungen und Schwachstellen in Form von Angriffen verwirklichen [30, S. 154].

Während zunächst auf diese Gefährdungslage eingegangen wird, werden zusätzlich die Maßnahmen dargestellt, die durch die EU und die Bundesrepublik Deutschland für die Erhöhung der Netz- und Informationssicherheit getroffen wurden.

## 2.1.1 Allgemeine Gefährdungslage

Das deutsche Bundeskriminalamt (BKA) führt die sogenannte Polizeiliche-Kriminalitätsstatistik (PKS), die eine Auswertung aller polizeilich erfassten Straftaten eines Jahres ermöglicht. Die Auswertung kann nach unterschiedlichen Kriterien erfolgen, in denen unter anderem gesondert die 'Computerkriminalität' als Kategorie von Straftaten erfasst wird. Seit der Einführung der Statistik im Jahr 1987 ist ein nahezu jährlicher Anstieg der in Deutschland erfassten Straftaten der Computerkriminalität festzustellen [31].

In diesem Zusammenhang gibt es unterschiedliche, mit der Digitalisierung und Vernetzung  verbundene,  Gefährdungs-  und  Schadensszenarien.  So  verschlüsselt  sogenannte Ransomware die Dateien der betroffenen Nutzer und fordert ein Lösegeld, um den ordnungsgemäßen Zugriff der Nutzer auf das Computersystem und die Dateien erneut freizugeben [32, S. 10-13]. Andere Schadsoftware versucht Bankdaten auszuspähen oder Rechenleistung für das Schaffen virtueller Währungen zu missbrauchen [33, S. 18-19].

<!-- page: 24 -->

Der  Bundesverband Informationswirtschaft,  Telekommunikation  und  neue  Medien e.V. gibt auf der Basis einer Befragung im Zusammenhang zum Wirtschaftsschutz an, dass insgesamt 68% der befragten Unternehmen in den vergangenen zwei Jahren Opfer von Datendiebstahl, Industriespionage oder Sabotage wurden. Eigener Angabe nach haben 47% der Befragten Schäden durch digitale Angriffe erlitten, was zu einem geschätzten Schaden von 43,4 Milliarden Euro in den Jahren 2016 und 2017 geführt hat [34, S. 14].

Auch öffentliche Verwaltungen sind als staatliche Institutionen das Ziel von verschiedenen Angriffen auf ihre IT-Infrastruktur. So sind diese das Ziel von allgemeinen Angriffen, die auf alle Computersysteme abzielen, unabhängig des Betreibers. Ein Beispiel dafür ist die Beeinträchtigung der Stadtverwaltung Burgdorf durch die Schadsoftware 'Emotet' [35]. Diese Schadsoftware zielt nicht ausschließlich auf Behörden ab, sondern betrifft ebenfalls Wirtschaftsunternehmen und verursachte in der Vergangenheit hohe Schäden [36].

Neben einem allgemeinen Gefährdungspotenzial gibt es ebenfalls gezielte Angriffe gegen öffentliche Institutionen. So kam es zu Denial-of-Service-Angriffen gegen die estländische Regierung und zu der unberechtigten Exfiltration von Daten aus den Netzwerken der EU [37, S. 290]. Als Beispiel für einen erfolgreichen Angriff auf eine öffentliche Institution Deutschlands dient der 2015 festgestellte Datenabfluss aus dem Netz des Deutschen Bundestages [38, S. 12]

In Deutschland ist die für IT- und Informationssicherheit zuständige, zentrale Behörde das BSI [38, S. 8]. Die Gefährdung von Behörden durch allgemeine und spezielle Angriffe, wird in einem Jahresbericht des BSI über das Jahr 2017 deutlich. In diesem stellt das BSI dar, dass monatlich ca. 52.000 E-Mails mit schadhaften Anhängen für die Bundesverwaltung abgefangen werden. Zusätzlich werden täglich ca. 5.100 Verbindungen von Behördenrechnern zu Servern mit Schadcode unterbunden [39, S. 8].

## 2.1.2 Europäische Regelungen

Um die Netzwerks- und Informationssicherheit (NIS) in der EU sicherzustellen und zu fördern, sind in den vergangenen 15 Jahren mehrere Maßnahmen durch die EU getroffen worden.

So wurde im Jahr 2004 die European Network and Information Security Agency (ENISA) geschaffen [37, S. 285]. Gemäß dem Beschluss 526/2013 vom 21.03.2014 des EU Parlaments und der EU Kommission ist gemäß Artikel 1 die Hauptaufgabe der ENISA, zu einem hohen Niveau der NIS beizutragen sowie das Bewusstsein für diese zu Stärken und eine entsprechende Kultur zu fördern. Konkret nennt die EU in Artikel 3 dieses Beschlusses mehrere Aufgaben, unter anderem:

<!-- page: 25 -->

1. Die Unterstützung und Beratung der EU in Sachen der Netzwerk- und Informationssicherheit sowie Analyse und Vorbereitung von diesbezüglichen Dokumenten.
2. Unterstützung der EU und seinen Mitgliedsstaaten durch fachliche Beratung, Übungen, Fortbildung und weiteren Maßnahmen.
3. Herstellung und Koordinierung von Kooperationen der Behörden und anderen relevanten Parteien im EU-Raum.
4. Unterstützung der Forschung, Entwicklung und Standardisierung auf dem Gebiet der Netzwerk- und Informationssicherheit.

Zusätzlich zu der ENISA wurde im Jahr 2017 die European Cyber Security Organisation (ECSO) gegründet. Auch diese hat koordinative Funktionen und umfasst mehr als 230  Mitglieder,  wie  das  BSI.  Neben  einer  Kommunikationsplattform  unterhält  die ECSO mehrere Arbeitsgruppen für die Weiterentwicklung der Cybersicherheit auf unterschiedlichen Gebieten [40, S. 221-222].

Als  NIS-spezifisches  Regelwerk  hat  die  EU  im  Jahr  2016  die  Richtlinie  (EU) 2016/1148 des Europäischen Parlaments und des Rates vom 6. Juli 2016 über Maßnahmen zur Gewährleistung eines hohen gemeinsamen Sicherheitsniveaus von Netz - und Informationssystemen in der Union (NIS-RL) beschlossen. Übergeordnetes Ziel der NIS-RL ist eine Vereinheitlichung der Informationssicherheitspolitiken in der EU. Aus diesem Grund enthält diese unterschiedliche Anforderungen, die die Mitgliedsstaaten in nationales Recht umsetzen müssen [41, S. 173-174]. Von Dürig und Fischer werden die Anforderungen wie folgt zusammengefasst [42, S. 209-210]:

1. Die Mitgliedsstaaten müssen eine nationale NIS-Strategie einführen.
2. Sie müssen sogenannte Computer-Emergency-Response-Teams (CSIRT) bilden, welche an einem länderübergreifenden CSIRT-Netzwerk beteiligt sind.
3. Es muss eine nationale Stelle benannt werden, die für die Aufgaben der NISRL verantwortlich ist.
4. Jeder Mitgliedsstaat  muss  eine  Stelle  benennen,  die  für  die  grenzüberschreitende Zusammenarbeit verantwortlich ist.
5. Die Betreiber wesentlicher Dienste werden durch die NIS-RL ebenfalls zum Umsetzen spezifischer Maßnahmen zur Absicherung ihrer Infrastruktur verpflichtet.

Zu Anforderung fünf nennt die NIS-Richtlinie insgesamt sieben Sektoren, in denen die Betreiber wesentlicher Dienste festzustellen sind [43, S. 28-29]:

1. Energie
2. Verkehr
3. Bankwesen
4. Finanzmarktinfrastrukturen
5. Gesundheitswesen

<!-- page: 26 -->

6. Trinkwasserlieferung und -versorgung
7. Digitale Infrastruktur

Letztlich müssen die Mitgliedsstaaten gemäß Artikel 5 Abs. 6 der NIS-RL eine Liste mit den Betreibern wesentlicher Dienste innerhalb ihres Hoheitsgebietes führen und diese mindestens alle zwei Jahre aktualisieren.

## 2.1.3 Deutsche Regelungen

Die Vorgaben der europäischen NIS-RL wurden zu großen Teilen bereits 2015 durch das deutsche IT-Sicherheitsgesetz (IT-SG) erfüllt. Mit dem Gesetz zu der Umsetzung der NIS-Richtlinie aus 2017 sind letztlich alle Vorgaben der NIS-RL vollständig umgesetzt [41, S. 161-162]. Aus diesen Gesetzen ergibt sich unter anderem, dass das BSI die zentrale Behörde für die Anforderungen der NIS-RL ist.

Neben den strategischen Folgen ergeben sich für die von dem IT-SG betroffenen Organisationen in Deutschland weitreichende Verpflichtungen [44, S. 20-21]. Wer zu den betroffenen Organisationen gehört, richtet sich nach der Branchenzugehörigkeit und Größe der Organisation, wobei die Vorgaben in der KritisV geregelt sind [41, S. 164]. Zum aktuellen Stand sind in der KritisV folgende Branchen erfasst:

1. Energieversorger aus dem Bereich der Strom-, Gas-, Kraftstoff-, Heizöl- und Fernwärmeversorgung (§2 KritisV).
2. Organisationen, befasst mit der Trinkwasserversorgung und Abwasserentsorgung (§3 KritisV).
3. Dienstleister im Bereich der Nahrungsversorgung (§4 KritisV).
4. Organisationen, die Dienste der Informations- und Telekommunikationstechnik, Sprach- und Datenübertragung sowie Datenspeicherung und -verarbeitung erbringen (§5 KritisV).

Öffentliche Verwaltungen sind nur von der NIS-RL und deren Regelungen betroffen, wenn sie die in der KritisV genannten Dienstleistungen in dem entsprechenden Umfang erbringen. Für alle weiteren Verwaltungen der Landesebene entstehen aus der NIS-RL und dem IT-SG keine Verpflichtungen.

Die Koordination von IT und Digitalisierung in der deutschen Verwaltungslandschaft obliegt seit 2010 dem IT-Planungsrat, einem bundesweiten Gremium der Verwaltungen des Bundes und der Länder [29, S. 21-23]. Unter anderem beschäftigt sich der IT-Planungsrat mit der Einführung von Standards und mit Sicherheitsanforderungen für den Datenaustausch in den Verwaltungen [7, S. 185-186].

Besondere Relevanz für die vorliegende Arbeit entfaltet die 2018 aktualisierte ISLL-Bund des IT-Planungsrates. Übergeordnetes Ziel der Leitlinie ist die Sicherstellung angemessener und dem Stand der Technik entsprechender Sicherheitsmaßnahmen zur Verhinderung von Sicherheitsvorfällen [12, S. 6]. Die ISLL-Bund enthält für die Verwaltungen des Bundes und der Länder zu diesem Zweck folgende Vorgaben:

<!-- page: 27 -->

- Die Einrichtungen von Bund und Ländern müssen ein angemessenes ISMS betreiben. Dies umfasst unter anderem die Erstellung und Umsetzung von Sicherheitskonzeptionen  für  Verwaltungsprozesse,  IT-Dienste,  Fachverfahren sowie Behörden und Einrichtungen [12, S. 11-12].
- Auf der Basis des IT-Grundschutz sind die Anschlussbedingungen an das Bundesnetz zu erfüllen, deren Einhaltung ist zu prüfen und diese sind fortzuschreiben [12, S. 13].
- Ebenen-übergreifende IT-Verfahren sind zu erfassen, zu beschreiben und auf ein einheitliches Sicherheitsniveau zu bringen [12, S. 14].
- Der VerwaltungsCERT-Verbund soll weiterentwickelt werden. Zudem Arbeiten Bund und Länder über gemeinsame technische Maßnahmen zur Abwehr von IT-Angriffen zusammen [12, S. 15].
- Letztlich sind die Verwaltungen angehalten, IT-Notfallmanagement-Prozesse auf Basis des IT-Grundschutzes zu etablieren [12, S. 16].

Demnach sind die obersten Landebehörden verpflichtet ein ISMS umzusetzen. Weiterhin muss das ISMS eine Sicherheitskonzeption beinhalten. Als Mindeststandards stehen der IT-Grundschutz und die ISO 2700x-Reihe zur Verfügung [12, S. 9].

## 2.2 Standardreihe ISO 2700x

Die 2700x-Reihe der ISO ist ein international anerkannter Standard [9, S. 5], der Anforderungen an die Planung, den Betrieb, die Kontrolle und die Verbesserung eines ISMS in einer Organisation stellt [45, S. 14]. Aufgrund der Kooperation zwischen dem deutschen Institut für Normung (DIN) und der ISO liegen die Dokumente der ISO 2700x-Reihe auch als Deutsche Normen vor, so z.B. die ISO 27001 in Form der DIN EN ISO/IEC 27001:2017.

## 2.2.1 Anwendungsbereich

Bereits aus dem Titel der ISO 27001 geht hervor, dass diese die Anforderungen an ein ISMS formuliert. In der übersetzten Fassung der DIN wird folgender Anwendungsbereich der ISO 27001 definiert:

' Diese Internationale Norm legt die Anforderungen für die Einrichtung, Umsetzung, Aufrechterhaltung und fortlaufende Verbesserung eines Informationssicherheitsmanagementsystems im Kontext der Organisation fest. Darüber hinaus beinhaltet diese Internationale Norm Anforderungen für die Beurteilung und Behandlung von Informationssicherheitsrisiken entsprechend den individuellen Bedürfnissen der Organisation. [ …]' [46, S. 6]

Ein ISMS nach der ISO 27001 lässt sich auf jegliche Organisation anwenden - auch wenn dies eine geringe Detailtiefe des Standards selbst bedingt. Das bedeutet, dass es jeder Organisation, unabhängig des Sektors, der Größe, des Standorts und der Struktur, möglich ist, auf Basis der ISO 27001 ein ISMS umzusetzen [47, S. 4].

<!-- page: 28 -->

## 2.2.2 Struktur

Die 2700x-Reihe ist eine Familie von Standards der ISO, die die Anforderungen an ein  ISMS,  die  Anforderungen  an  Zertifizierungsstellen,  zusätzliche  sektorspezifische Anforderungen und allgemeine Richtlinien für die Umsetzung eines ISMS formuliert [23, S. 18]. Grundlegende Norm dieser Familie ist die ISO/IEC 27000:2018, welche die allgemeinen Begrifflichkeiten und Ziele der Normenreihe erläutert. Wird auf die auf dort aufgeführte Übersicht zurückgegriffen (vgl. Abbildung 2.1), stellt sich die Normenfamilie wie folgt dar:

Abbildung 2.1: Die Zusammenhänge in der Normenfamilie 27000 [23, S. 19] (Reproduktion)

<!-- image -->

Abgesehen von den Begriffsbestimmungen ist für die Zertifizierung des ISMS einer Organisation der zentrale Standard die ISO 27001. Auf Basis der Vorgaben aus Kapitel 4-10 und dem Anhang A der ISO 27001 ist eine Zertifizierung möglich [48, S. 16]. Ein weiterer, zertifizierbarer Standard dieser Reihe ist die ISO/IEC 27006:2015, die verbindliche Anforderungen an akkreditierte Zertifizierungsstellen stellt [25, S. 12].

In der Nummerierung der Standards folgen auf die ISO 27001 die Normen 27002 bis 27005. Diese haben Richtliniencharakter und geben zusätzliche Hinweise und Umsetzungsunterstützung für die Inhalte und Vorgaben der ISO 27001 [45, S. 14]. Besonders ist hier die ISO/IEC 27002:2013 (fortan ISO 27002) zu beachten, die zu den Maßnahmen aus dem Anhang A der ISO 27001 genaue Beispiele und Umsetzungsmöglichkeiten aufzeigt.

Die ISO 27001 ist in insgesamt 10 Kapitel und einen Anhang aufgeteilt. Die ersten drei  Kapitel  enthalten  allgemeine  Informationen,  wie  den  Anwendungsbereich,  Begriffsbestimmungen (mit einem den Verweis auf die ISO 27000) und eine Erläuterung zu Referenzen. Konkrete Anforderungen an ein ISMS lassen sich aus den Kapiteln 4

<!-- page: 29 -->

bis 10 entnehmen [45, S. 23-24]. Die Überschriften dieser sechs Kapitel lauten in der deutschen Version der ISO 27001:

4. Kontext der Organisation , in dem die Aufgaben und Ziele der Organisation betrachtet und dokumentiert werden. Ebenso wird in diesem Kapitel gefordert, dass festgestellt wird, welche Parteien Anforderungen an die Organisation stellen und welchen Anwendungsbereich das ISMS umfasst.
5. Führung regelt die Verpflichtungen der Organisationsleitung, welches unter anderem die Übernahme der Gesamtverantwortung und die Bereitstellung benötigter Ressourcen umfasst. Zudem muss die Leitungsebene eine Sicherheitspolitik  verabschieden,  in  der  die  Informationssicherheitsziele,  die  Verpflichtung zum Umsatz der Politik und die Verpflichtung zur fortlaufenden Verbesserung dokumentiert sind.
6. Planung definiert den Umgang der Organisation mit Risiken. Neben den Prozessen und Richtlinien, wie Risikomanagement durchzuführen ist, werden in diesem Kapitel Maßnahmen zu der Bewältigung von Risiken festgelegt. Das Kapitel 6.2 erläutert festzulegende Informationssicherheitsziele und geht auf Verpflichtungen zu deren Erreichung ein.
7. Unterstützung befasst sich mit der Bereitstellung von benötigten Ressourcen, der Kommunikation und Dokumentation von Informationen. Es wird zusätzlich auf das Bewusstsein für Informationssicherheit eingegangen.
8. Betrieb enthält Vorgaben zu der Umsetzung und Steuerung des ISMS in der Organisation, der Risikobeurteilung und der Aktualisierung der Risikobehandlung.
9. Bewertung der Leistung fordert  von  der  Organisation  die  Kontrolle  des ISMS durch angemessene Maßnahmen und Metriken. Die Kontrolle muss über interne Audits des ISMS, welche geplant und umgesetzt werden muss, und eine jährlich stattfindende Managementbewertung ausgeübt werden.
10. Verbesserung ist das letzte Kapitel der ISO 27001 und regelt den Umgang mit Abweichungen, in dem das Vorgehen bei Korrekturen und deren Dokumentation geregelt wird. Zum anderen wird eine Organisation in diesem Kapitel verpflichtet, die Eignung, Angemessenheit und Wirksamkeit des ISMS fortlaufend zu verbessern.

## 2.2.3 Umsetzung auf der Basis der ISO 27001

Bei der Formulierung der Vorgaben, nach denen ein ISMS nach der ISO 27001 umzusetzen ist, wird auf das Vokabular der ISO 27000 verwiesen, die im Kapitel 0.2 folgende Begrifflichkeiten einführt [23, S. 5]:

1. Soll - Eine verpflichtende Vorgabe.
2. Sollte - Eine Empfehlung.
3. Darf - Eine Erlaubnis.

<!-- page: 30 -->

## 4. Kann - Eine Möglichkeit.

Mit diesen Leitworten versehen, gehen aus den Kapiteln der ISO 27001 Anforderungen an eine Organisation hervor, die von Kersten, Klett, Reuter und Schröder in der hier reproduzierten Tabelle 2.1 zusammengefasst werden:

Tabelle 2.1: Anforderungen an eine Organisation aus der ISO 27001 [48, S. 37]

| Abschnitt   | Gegenstand                                                                  |
|-------------|-----------------------------------------------------------------------------|
| 4.1-4.2     | Geschäftlichen Kontext ermitteln und aufbereiten                            |
| 4.3         | Scope des ISMS festlegen, Schnittstellen klären                             |
| 4.4         | ISMS umsetzen                                                               |
| 5.1         | Führung und Engagement: Etablieren                                          |
| 5.2         | Adäquate Leitlinie erstellen, in Kraft setzen                               |
| 5.3         | Organisation, Zuständigkeiten und Befugnisse festlegen, Rollen be- setzen   |
| 6.1         | Verfahren der Risikobeurteilung und -behandlung festlegen / doku- mentieren |
| 6.2         | Umsetzung planen                                                            |
| 7.1-7.3     | Leitungsaufgaben: Ressourcen, Kompetenzen, Kommunikation                    |
| 7.4         | 'Dokumentierte Informationen' planen                                        |
| 7.5         | Awareness-Programme planen                                                  |
| 8           | Risikobeurteilung und -behandlung durchführen, Maßnahmen umset- zen         |
| 9.1         | Überwachung, Messung und Auswertung aufsetzen                               |
| 9.2         | Interne Audits planen                                                       |
| 9.3         | Managementbewertung aufsetzen                                               |
| 10          | Prozess der kontinuierlichen Verbesserung einrichten                        |

Die Vorgaben aus den Kapiteln folgen einer chronologischen wie auch logischen Reihenfolge und bedienen sich dem sogenannten ' Deming-Zirkel ' , auch wenn dieser in dem Standard nicht wörtlich genannt wird. Dennoch lässt sich dieser in den 6 Kapitelüberschriften wiederfinden [49, S. 96]. Abbildung 2.2 zeigt eine schematische Darstellung  des  Deming-Zirkels,  auch  Plan-Do-Check-Act-Zyklus  (PDCA-Zyklus)  genannt, in Kombination mit den Inhalten der ISO 27001:

<!-- page: 31 -->

- Risikoanalyse

Abbildung 2.2: Plan-Do-Check-Act-Zyklus der ISO 2700x, reproduziert nach Römer und Piwinger [50]

<!-- image -->

Diese Abbildung setzt die Vorgaben der ISO 27001 in einen chronologischen und methodischen Zusammenhang und hebt hervor, dass die ISO 27001 Einführung und Umsetzung eines ISMS als kontinuierlichen Prozess betrachtet und entsprechende Anforderungen stellt. Besonders aufgrund dieser Betrachtungsweise, die sich nicht an vorgegebenen Strukturen der Organisation orientiert, wird die Methodik der ISO 27001 auch als prozessorientiert bezeichnet [25, S. 22-24].

## 2.2.4 Risikomanagement

Neben der iterativen Natur des ISMS-Prozesses hat das Risikomanagement eine zentrale Rolle in der Umsetzung eines ISMS nach der ISO 27001. Dieses wird als Anforderung im Rahmen der Umsetzung gefordert und beginnt in der Plan-Phase des Deming-Zirkels.

Anwendern der ISO 27001 stehen dazu gemäß der Umsetzungsempfehlung aus der ISO 27002 die Richtlinien aus dem Standard ISO/IEC 27005:2018 (fortan ISO 27005) zur Verfügung [51, S. 7]. Dieser Standard befasst sich ausschließlich mit IT-Risikomanagement und verweist in dem Risikomanagementprozess auf die ISO 31000:2018 [52, S. 3]. Die Begriffe Risiko und Risikomanagement sind in Kapitel 1 der vorliegenden Arbeit definiert. Die ISO 31000 betrachtet das Risikomanagement ebenfalls als einen wiederholenden Prozess, der in Abbildung 2.3 darstellt ist:

<!-- page: 32 -->

Abbildung 2.3: Risikomanagementprozess nach der ISO 31000:2018 [53, S. 9] (Reproduktion)

<!-- image -->

Ähnlich  dem  allgemeinen  Vorgehen  nach  der  ISO  27001  zum  Umsetzen  eines ISMS, wird zunächst der Kontext der Organisation festgestellt. Nicht abschließend aufgezählt  gehört  dazu  die  Festlegung  des  Anwendungsbereiches,  die  Bestimmung  der Ziele und Metriken, die angewandt werden sollen, sowie eine Festlegung der Bewertungskriterien und Maßstäbe [54, S. 49-52].

Nachdem allgemeine Informationen festgelegt sind, folgt das Risiko Assessment, die  Risikobeurteilung. Dieser Oberbegriff wird in Abbildung 2.3 in drei Prozessteile aufgeteilt. Gemäß Klipper beinhalten die drei Prozessteile der Risikobeurteilung folgende Aufgaben [55, S. 67-76]:

1. Die Risikoidentifikation befasst  sich  mit  der  systematischen  Feststellung wichtiger Werte in der Organisation. Für diese werden Bedrohungen und bereits  umgesetzte  Maßnahmen  ermittelt,  welche  zu  ihrem  Umsetzungsstand, Wirksamkeit und Richtigkeit geprüft werden. Unter Einbeziehung dieser Informationen  werden  die  Schwachstellen  für  die  Organisationswerte  betrachtet. Zuletzt werden mögliche Schadensauswirkungen festgestellt, wenn es zu einem Schadensfall gegenüber den festgestellten Werten kommt.

<!-- page: 33 -->

2. Die Risikoanalyse schätzt die festgestellten Risiken im Bezug zu ihrer Eintrittswahrscheinlichkeit  und/oder -frequenz  sowie  der Schadenshöhe. Dabei können Organisationen auf qualitative und quantitative Methoden sowie eine Mischform  derer  zurückgreifen.  Eine  Kombination  der  Wahrscheinlichkeit und Auswirkungen führt zu der Feststellung der Risikokategorie jedes Risikos.
3. Die Risikobewertung nutzt die zuvor erhobenen Daten und erstellt eine Priorisierung der Risiken. Anhand dieser wird entschieden, in welcher Reihenfolge die Risiken behandelt werden.

Nach der Durchführung der drei Teilprozesse der Risikobeurteilung liegt dem Anwender eine priorisierte Liste von Risiken für die Werte der Organisation vor. Im letzten Schritt des Risikomanagementprozesses müssen diese Risiken nun einer Risikobehandlung unterzogen werden. Dies bedeutet, dass für jedes Risiko eine von vier Behandlungsoptionen getroffen wird [54, S. 71]:

1. Mit einer Risikovermeidung gibt die Organisation das risikoursächliche Objekt auf, sodass das Risiko nicht mehr entstehen kann.
2. Mit einer Risikoreduktion werden Maßnahmen getroffen, die entweder Eintrittswahrscheinlichkeit oder -auswirkungen reduzieren.
3. Der Risikotransfer führt zu einer Weitergabe des Risikos an Dritte, wie Versicherer oder Dienstleister.
4. Bei einer Risikoübernahme wird das Risiko bewusst akzeptiert und übernommen.

Flankiert wird dieser zyklische Risikomanagementprozess von drei weiteren Maßnahmen [56, S. 266]:

1. Kommunikation umfasst die Mitteilung risikobezogener Informationen und die Beratung mit relevanten beteiligten Parteien. Es ist zu beachten, dass die Risikokommunikation  nicht  einseitig  verläuft,  sondern  in  beide  Richtungen stattfindet. Ziel der Risikokommunikation ist das Schaffen von Risikobewusstsein, Verständnis und risikobezogenem Fachwissen [55, S. 90-91].
2. Die Dokumentation ergänzt die Kommunikation durch die Erstellung von Berichten  über  das  Risikomanagement  und  deren  Prozesse.  Neben  einer Grundlage für Prüfungen durch das Management [47, S. 44], wird die Dokumentation des Risikomanagements für Entscheidungen und Unterstützung im Risikoprozess benötigt [53, S. 14-15].
3. Der Risikomanagementprozess und seine Teilprozesse sind im Rahmen des ISMS zu überwachen . Dazu können Metriken verwendet werden, die die Umsetzung und die Leistungsfähigkeit des Risikomanagements in Zahlen darstellen und dadurch die Kontrolle erleichtern [54, S. 75].

Eine Besonderheit der ISO 27001 gegenüber anderen Management-Standards, wie der ISO 22301:2013 [57, S. 224], ist die Forderung nach einem Statement of Applicability

<!-- page: 34 -->

(SoA) im Kapitel 6.1.3. Dieses enthält die Anforderung, dass die Ergebnisse der Informationssicherheitsrisikobeurteilung  und  -behandlung mit  den  vorgeschlagenen  Maßnahmen des Anhang A der ISO 27001 abgeglichen werden [46, S. 9-10].

Der Anhang A enthält 114 Anforderungen (engl. Controls), deren Umsetzung oder Auslassung gemäß Kapitel 6.1.3 d) in dem SoA dokumentiert werden müssen. Konkret muss das SoA begründen, welche Maßnahmen aus Anhang A bereits umgesetzt sind, umzusetzen sind und weshalb Maßnahmen nicht umgesetzt werden [48, S. 61-62].

## 2.2.5 Branchenspezifische Standards

Auf Basis der Darstellung von Brenner et al. [25, S. 11] und der Abbildung 2.1 werden folgende Standards zu den Hauptveröffentlichungen der ISO zu der Umsetzung eines ISMS gezählt:

1. Begriffsbestimmungen aus der ISO/IEC 27000:2016.
2. Anforderungen  an  ein  ISMS  und  Zertifizierungsstellen  aus  der  ISO/IEC 27001:2013 und ISO/IEC 27006:2015.
3. Allgemeine Leitfäden und Richtlinien zu der Umsetzung eines ISMS aus den Standards ISO/IEC 27002:2013, ISO/IEC 27003:2017, ISO/IEC 27004:2016, ISO/IEC 27005:2018.

Zusätzlich zu diesen Publikationen hat die ISO weitere Normen veröffentlicht, die bestimmte  Aspekte  des  Informationssicherheitsmanagements  (ISM)  oder  ausgewählte Branchen beleuchten. Grundlegender Standard dafür ist die ISO/IEC 27009:2016, die die Anforderungen an sektorspezifische ISMS stellt und darstellt, wie zusätzliche Anforderungen im Zusammenhang mit dem Anhang A der ISO 27001 umgesetzt werden können [58, S. 1].

So sind mit dem Stand der vorliegenden Arbeit mit der ISO/IEC 27011:2016 Richtlinien für ein ISMS eines Telekommunikationsdienstleisters veröffentlicht oder mit der ISO/IEC  27017:2015  zusätzliche  Vorgaben  für  Nutzer  und  Betreiber  von  CloudDiensten  formuliert.  Weiterhin  werden  beispielsweise  in  dem  ISO/IEC  Standard 27019:2017 zusätzliche Anforderungen für Energieunternehmen vorgestellt [45, S. 1516].

Für die öffentlichen Verwaltungen sind keine branchenspezifischen Vorgaben definiert oder ISO Standards veröffentlicht.

## 2.3 IT-Grundschutz

Alternativ zu der ISO 27001 können oberste Landesbehörden gemäß der ISLL-Bund ebenfalls auf den IT-Grundschutz zurückgreifen und sind in Fällen Ebenen-übergreifender IT-Verfahren dazu verpflichtet [12, S. 14].

Der IT-Grundschutz besteht aus den Standards 200-1 bis 200-3. Im Jahr 2017 sind diese Standards von dem BSI aktualisiert worden, vormals waren diese mit einer veränderten Methodik unter der Standard-Reihe 100-1 bis 100-3 bekannt [59, S. 89]. Obwohl die Standards von dem deutschen BSI veröffentlicht werden, sind diese auch in der englischen Sprache erhältlich. Die nun aktualisierten (mit der ISO 27001 kompatiblen [59, S. 90]) Standards behandeln, gemessen an der Überschrift, folgende Themen:

<!-- page: 35 -->

- BSI Standard 200-1: Managementsysteme für Informationssicherheit (ISMS)
- BSI Standard 200-2: IT-Grundschutz-Methodik
- BSI Standard 200-3: Risikoanalyse auf der Basis von IT-Grundschutz

## 2.3.1 Anwendungsbereich

Ähnlich der ISO 27001 soll auch die IT-Grundschutz Methodik unabhängig der Institutionsaufgabe und -größe verwendbar sein [60, S. 7]. Während bei der ISO 27001 kritisiert wird, dass diese nur allgemeine und wenige technische Anforderungen stellt [61,  S.  63-66],  setzt  die  IT-Grundschutz-Methodik auf sogenannte IT-Grundschutz-Bausteine, die die Sicherheitsanforderungen an das organisatorische ISMS und die IT-Infrastruktur der Organisation beinhalten.

## 2.3.2 Struktur

Die Standards, die das ISMS nach dem IT-Grundschutz beschreiben, gliedern sich in drei Teile. Auf deren Methodik aufbauend besteht zusätzlich das IT-GrundschutzKompendium, welches die zuvor erwähnten Sicherheitsanforderungen enthält.:

1. Der  BSI Standard  200-1 beschreibt  allgemeine  Anforderungen  an  ein ISMS [62, S. 54], das Vorgehen bei der Umsetzung eines ISMS und die relevanten Beteiligten, besonders die Organisationsführung [59, 89-90].
2. Der BSI Standard 200-2 betrachtet detailliert die IT-Grundschutz-Methodik [63, S. 26], die angewendet wird, um ein ISMS in der Organisation umzusetzen.
3. Im BSI Standard 200-3 wird anschließend auf die Risikoanalyse nach dem IT-Grundschutz eingegangen. Diese kann einzelne Zielobjekte, aber auch Geschäftsprozesse und Fachanwendungen, betrachten [27, S. 64].
4. Das IT-Grundschutz-Kompendium enthält  neben  allgemeinen  Informationen zu dem ISMS (und entsprechenden Referenzen zu den drei Standards), eine Liste von elementaren Gefährdungen und darauf aufbauenden IT-Grundschutz-Bausteinen,  die  Sicherheitsanforderungen  für  abzusichernde Zielobjekte [24, S. 31-32] beinhalten. Die IT-Grundschutz-Bausteine  betrachten neben  konkreten IT-Komponenten auch organisatorische Anteile des ISMS und stellen entsprechende Anforderungen.

Ergänzend gibt es weitere Publikationen des BSI. Ein Beispiel dafür ist der Standard 100-4, der sich mit Notfallmanagement beschäftigt. Im IT-Grundschutz-Kompendium wird der Standard 100-4 als Sicherheitsanforderung in zwei IT-Grundschutz-Bausteinen genannt, im Standard 200-2 wird das Notfallmanagement nach 100-4 in der Änderungshistorie erwähnt. Auch die Standards 200-1 und 200-3 erwähnen diesen Standard, gehen aber nicht weiter auf diesen und mögliche Zusammenhänge ein.

<!-- page: 36 -->

Aufgrund der Konzentration des Standards 100-4 auf das Notfallmanagement [60, S. 13] und fehlender Verweise der Standards 200-1 bis 200-3 auf diesen, wird der Standard 100-4 nicht zu dem Kern des ISMS nach der IT-Grundschutz-Methodik gezählt.

## 2.3.3 Umsetzung auf der Basis des IT-Grundschutz

Um ein ISMS nach der IT-Grundschutz-Methodik umzusetzen, wird methodisch zunächst auf den Standard 200-1 und anschließend auf den Standard 200-2 zurückgegriffen. In den Erläuterungen des Standards 200-1 wird ebenso ein zyklisches Prozessmodell des ISM beschrieben, in diesem Fall wörtlich der Plan-Do-Check-Act-Zyklus [60, S. 18]. Der Umsetzungsprozess wird im Standard 200-2 erläutert. Abbildung 2.4 stellt dar, in welche Phasen der Informationssicherheitsmanagementprozess unterteilt wird:

Abbildung 2.4: Die Phasen des Informationssicherheitsprozesses [64, S. 15] (Reproduktion)

<!-- image -->

<!-- page: 37 -->

Während der Standard 200-2 in den Kapiteln 3 bis 5 die allgemeinen organisatorischen Aufgaben der Initiierung, Organisation und Dokumentation des Informationssicherheitsprozesses beschreibt, unterscheidet der Standard 200-2 anschließend zwischen drei unterschiedlichen Vorgehensweisen der Sicherheitskonzeption. Diese stellen sich wie folgt dar [64, S. 28-29]:

1. Die Basis-Absicherung , die die Organisation grundlegend absichern und die größten Risiken senken soll.
2. Die Kern-Absicherung , die die zentralen und wichtigsten Geschäftsprozesse der Organisation betrachtet und absichert.
3. Die Standard-Absicherung ,  die mit einer Betrachtung aller relevante Infrastrukturanteile im Anwendungsbereich des ISMS zu einer umfassenden Sicherheitskonzeption führt.

Nach Goldschmidt und Krüsmann [59, 90] unterscheiden sich die Basis- und Kern-Absicherung wie folgt: Die Basis-Absicherung betrachtet die grundlegenden Geschäftsprozesse und sorgt für eine zeitnahe Umsetzung der wichtigsten Maßnahmen, um eine erste Absicherung vorzunehmen. Die Kern-Absicherung betrachtet dagegen nicht den gesamten Informationsverbund einer Organisation, sondern wichtige Prozesse, deren Fortbestand als besonders kritisch erachtet wird.

Die  Sicherheitskonzeption  der  Standard-Absicherung  betrachtet  die  vollständige Organisation und ihre Anteile im Rahmen des gesetzten  Anwendungsbereiches. Bei Zielobjekten, die den nachfolgend aufgeführten Kriterien entsprechen, muss gemäß der Standard-Absicherung eine Risikoanalyse durchgeführt werden. Die Standard-Absicherungsart wird vom BSI empfohlen [64, S. 30].

Die Standard-Absicherung umfasst folgende Prozessteile [64, S. 76-158]:

1. In der Strukturanalyse werden die Komponenten der Informationsverbundes erfasst und gebündelt dargestellt. Der Standard 200-2 schlägt die Unterteilung der Komponenten in die Gruppen Geschäftsprozesse, Anwendungen, IT-Systeme, Netze, ICS-Systeme, sonstiger Geräte und Räume vor. Das Ergebnis der Strukturanalyse sind die Objekte des Informationsverbunds, die im ISMS abgesichert werden.
2. Die Schutzbedarfsfeststellung erfasst, ausgehend von dem Geschäftsprozess und den verwendeten Informationen, die Schutzbedürftigkeit der zuvor festgestellten Objekte in ihren jeweiligen Gruppen. Dazu müssen durch die Organisation  im  Voraus  entsprechende  Einordnungskategorien,  genannt  Schutzbedarfskategorien, festgelegt werden.
3. In der Modellierung werden die festgestellten Objekte des Informationsverbundes mit den IT-Grundschutz-Bausteinen abgeglichen. Die entsprechenden IT-Grundschutz-Bausteine werden ausgewählt und aus den dort vorgegebenen Basis-, Standard- und erweiterten Sicherheitsanforderungen entsteht ein Entwicklungs- oder Prüfplan - je nach Stand des ISMS in der Organisation - mit umzusetzenden Sicherheitsmaßnahmen.

<!-- page: 38 -->

4. Der IT-Grundschutz-Check prüft anschließend, inwiefern die Sicherheitsanforderungen aus der Modellierung bereits umgesetzt sind. Dieser Soll-Ist-Vergleich kann als Grundlage dienen, um einen Umsetzungsplan für die weiteren Maßnahmen zu erstellen und so die verbleibenden Sicherheitsanforderungen zu erfüllen.
5. Die Risikoanalyse wird abschließend auf Objekte des Informationsverbunds angewendet, die in der Schutzbedarfsfeststellung als besonders schutzwürdig identifiziert werden. Die Risikoanalyse wird im IT-Grundschutz in die Prozessschritte Gefährdungsübersicht, Risikoeinstufung und Risikobehandlung eingestuft.

Eine schematische Darstellung des Erstellungsprozesses der Sicherheitskonzeption ist aus dem Standard 200-2 in Abbildung 2.5 reproduziert:

Abbildung 2.5: Erstellung der Sicherheitskonzeption in der Standard -Absicherung [64, S. 76] (Reproduktion)

<!-- image -->

Die IT-Grundschutz-Bausteine, die zur Modellierung verwendet werden, sind in zwei Gruppen aufgeteilt. Die Prozess-Bausteine betrachten das organisatorische ISMS. Die System-Bausteine beziehen sich ausschließlich auf die festgestellten Objekte des Informationsverbundes und sind daher abhängig von dem Aufbau der Organisation.

<!-- page: 39 -->

Der Inhalt der IT-Grundschutz-Bausteine ist vierteilig: Zunächst wird das Zielobjekt des Bausteins beschrieben und der Anwendungsbereich abgegrenzt. Anschließend wird auf die spezifischen Gefährdungen für diese Zielobjekt eingegangen, während am Ende jedes Bausteines alle relevanten elementaren Gefährdungen des Zielobjekts aufgelistet sind. Darauf aufbauend enthält jeder IT-Grundschutz-Baustein spezifische Sicherheitsanforderungen [64, S. 132-133].

Aus der Modellierung des Informationsverbundes mithilfe der IT-Grundschutz-Bausteine ergeben sich in der IT-Grundschutz-Methodik die Anforderungen, die im Rahmen des ISMS umgesetzt werden müssen. Diese Sicherheitsanforderungen gliedern sich in die Stufen Basis, Standard und Anforderungen für einen erhöhten Schutzbedarf.

Die Vorgaben der Anforderungen verwenden in diesem Zusammenhang die folgenden Begriffe [24, S. 33]:

1. MUSS / DARF NUR, für eine zwingend umzusetzende Maßnahme.
2. DARF NICHT / DARF KEIN, für eine absolute Unterlassung.
3. SOLLTE, für eine Maßnahme, die umgesetzt werden sollte, aber stichhaltig begründet und dokumentiert in bestimmten Fällen unterlassen werden kann.
4. SOLLTE NICHT / SOLLTE KEIN, für eine Unterlassung, die mit einer guten Begründung missachtet wird.

Die Anforderungen der IT-Grundschutz-Bausteine sind wie folgt strukturiert [64, S. 133-135]:

- Bei Anforderungen der Basis-Absicherung handelt es sich um zwingend umzusetzende Maßnahmen. Wird in der Basis-Absicherung modelliert, gelten die Basis-Anforderungen des gesamten Bausteins.
- Anforderungen der Standard-Absicherung sollten umgesetzt werden, mit einer dokumentierten Begründung kann dies unterlassen werden. In der StandardAbsicherung bauen die Anforderungen der Standard-Absicherung auf die Basis-Absicherung auf und SOLLTEN verwendet werden.
- Die Anforderungen für einen erhöhten Schutzbedarf verwenden in ihren Formulierungen ebenfalls die Begrifflichkeit SOLLTE, sind aber nicht automatisch bei einem hohen Schutzbedarf umzusetzen. Diese Anforderungen sind weiterführende Maßnahmen, die bei einem erhöhten Schutzbedarf zur Absicherung in Betrachtung gezogen werden können und haben einen Empfehlungscharakter.

## 2.3.4 Risikomanagement

Nach dem BSI Standard 200-2 ist in der Kern- und Standard-Absicherung eine Risikoanalyse  besonders  schutzbedürftiger  Zielobjekte  vorgesehen.  Die  Basis-Absicherung bedient sich ausschließlich den Basis-Anforderungen aus den IT-Grundschutz-Bausteinen und sieht keine Durchführung einer Risikoanalyse vor [65, S. 9-10].

<!-- page: 40 -->

Für die Durchführung einer Risikoanalyse nennt der BSI Standard 200-3 mehrere Voraussetzungen, die die Anwender vorab erfüllen sollen [65, S. 9-10]. So sollen mehrere organisatorische Maßnahmen, wie ein festgelegter Geltungsbereich, bereits getroffen worden sein. Zudem soll im Rahmen der Sicherheitskonzeption eine Schutzbedarfsfeststellung durchgeführt worden sein. Die Schutzbedarfsfeststellung betrachtet für die Geschäftsprozesse und Infrastrukturanteile im Anwendungsbereich des ISMS den jeweiligen  Schutzbedarf  in  Hinsicht  auf  die  Schutzziele  Vertraulichkeit,  Integrität  und Verfügbarkeit.

Es muss eine Risikoanalyse durchgeführt werden, wenn einer von drei Fällen zutrifft [60, S. 32]:

1. Das Zielobjekt fällt unter einen hohen oder sehr hohen Schutzbedarf.
2. Für das Zielobjekt besteht kein Baustein des IT-Grundschutz-Kompendiums.
3. Das Zielobjekt wird in außergewöhnlichen oder unüblichen Szenarien eingesetzt.

Bei einem normalen Schutzbedarf muss keine Risikoanalyse durchgeführt werden, da das BSI während der Erstellung der IT-Grundschutz-Bausteine das betreffende Zielobjekt unter dem Gesichtspunkt von insgesamt 47 elementaren Gefährdungen betrachtet und so eine Risikobehandlung bei einem normalen Schutzbedarf erstellt hat [60, S. 41]. Muss nun ein Zielobjekt zusätzlich durch eine Risikoanalyse überprüft werden, sieht die Risikoanalyse nach der IT-Grundschutz-Methodik folgendes Vorgehen vor [65, S. 7-8]:

1. Die Ermittlung möglicher Gefährdungen für das Zielobjekt.
2. Eine Einschätzung der dadurch entstehenden Risiken auf der Basis von Eintrittswahrscheinlichkeiten und -Auswirkungen.
3. Die Behandlung der festgestellten Risiken durch Vermeidung, Verschiebung, Reduzierung (z.B. über zusätzliche Baustein-Anforderungen) oder Übernahme.
4. Eine Konsolidierung der Ergebnisse mit den bereits vorgesehen Maßnahmen der Modellierung und eine Rückführung der Ergebnisse in den Sicherheitsprozess.

## 2.3.5 Branchenspezifische Standards

Außer  den  Standards  200-1  bis  200-3  und  dem  IT-Grundschutz-Kompendium existieren keine weiteren BSI-Standards als Richtlinien zu der Umsetzung eines ISMS. Es  gibt  Handreichungen, Merkblätter  und  anderes  Informations-  und  Hilfematerial, welches auf Internetseite des BSI zur Verfügung gestellt wird. Dies kommt, hiesiger Bewertung nach, nicht der Kodifikation eines BSI-Standards oder des Standards der ISO gleich. Das BSI stellt diese Dokumente auch nicht als beteiligungsfähige Community Drafts bereit.

Auf der sektorspezifischen Ebene gibt es technische Richtlinien, welche besondere Anforderungen im Bereich der Informationssicherheit definieren. Ein Beispiel hierzu ist die BSI-TR-03108, die Maßnahmen für den sicheren E-Mail Transport beschreibt [66, S. 37]. Branchenspezifische ISMS-Standards sind vom BSI nicht veröffentlicht.

<!-- page: 41 -->

Um dennoch die Umsetzung eines ISMS in unterschiedlichen Branchen zu erleichtern, werden auf Initiative des BSI IT-Grundschutz-Profile entwickelt, die eine ISMS-Schablone für Organisationen mit ähnlichen Anforderungen darstellen sollen [15]. Dabei  können  Anwender  des  IT-Grundschutzes  einer  Koordinationsgruppe,  beispielsweise einem Branchenverband, mit Unterstützung des BSI eine Schablone einer Sicherheitskonzeption erstellen.

Ein IT-Grundschutz-Profil bietet eine generische Sicherheitskonzeption, die von Organisationen gleicher Zugehörigkeit im Rahmen der Umsetzung des eigenen ISMS adaptiert werden können [67, S. 36]. Ein IT-Grundschutz-Profil gemäß der Strukturbeschreibung des BSI folgende Inhalte haben [16, S. 7-21]:

1. Management Summary
2. o Dient als Zusammenfassung des IT-Grundschutz-Profils und stellt die Zielgruppe sowie Zielsetzung dar.
2. Festlegung des Geltungsbereichs
4. o Dieser  Teil  des  IT-Grundschutz-Profils  dient  zur  Festlegung  Zielgruppe,  dem  Abdeckungsgrad  nach  dem  IT-Grundschutz,  der  ISO 27001 Kompatibilität und den Rahmenbedingungen.
3. Abgrenzung des Informationsverbunds
6. o Hier werden die Bestandteile des Informationsverbundes oder des Geschäftsprozesses  dargestellt  und  es  wird  abgegrenzt,  was  vom  ITGrundschutz-Profil nicht betrachtet wird.
4. Referenzarchitektur
8. o In der Referenzarchitektur wird festgelegt, welche Objekte durch das IT-Grundschutz-Profil betrachtet werden. Das BSI gibt an, dass im Idealfall  die  Objektgruppen  Infrastruktur,  Netze  und  Kommunikation, IT-Systeme sowie Geschäftsprozesse / Anwendungen betrachtet werden. Ähnliche Zielobjekte sollen dabei gruppiert werden.
5. Zu erfüllende Anforderungen und umzusetzende Maßnahmen
10. o Die  festgestellte  Referenzarchitektur  wird  mithilfe  der  IT-Grundschutz-Bausteine abgebildet und daraus ergeben sich die Anforderungen  der  Sicherheitskonzeption.  In  diesem  Zusammenhang  können Anforderungen je nach Zielrichtung des IT-Grundschutz-Profils auch konkretisiert oder gestrichen werden. Es können aber auch alle Anforderungen als relevant erachtet werden.
6. Restrisikobetrachtung / Risikobehandlung

<!-- page: 42 -->

- o In der Erstellung des IT-Grundschutz-Profils können zusätzliche Risiken und Sicherheitsanforderungen festgestellt werden, die hier aufgezählt werden. Auch Restrisiken müssen bewertet und dokumentiert werden.
7. Anwendungshinweise
- o In den Anwendungshinweisen kann den Anwendern beschrieben werden, wie mit dem IT-Grundschutz-Profil und den daraus folgenden Anforderungen umgegangen wird.
8. Unterstützende Informationen
- o In dem letzten Kapitel können Hinweise auf zusätzliche Literatur und andere IT-Grundschutz-Profile gegeben werden.

Im Bereich des IT-Grundschutzes wird üblicherweise die Begrifflichkeit des Informationsverbundes  als  Oberbegriff  für  den  betrachteten  Anwendungsbereich  verwendet (Definition siehe Kapitel 1.3.2.2). In den IT-Grundschutz-Profilen wird dagegen auf die Begrifflichkeit der Referenzarchitektur zurückgegriffen. Diese ist nicht im IT-Grundschutz-Kompendium definiert.  Aus  dem  Kontext  der  Strukturbeschreibung  der  ITGrundschutz-Profile ergibt sich, dass die Referenzarchitektur den generischen Informationsverbund beschreibt, der die Grundlage für die schematische Sicherheitskonzeption darstellt.

Wird das strukturelle Vorgehen des IT-Grundschutzes betrachtet, so sind die Inhalte der IT-Grundschutz-Profile in der Sicherheitskonzeption eines ISMS einzuordnen. Die Strukturbeschreibung hebt ebenfalls hervor, dass eines der Hauptziele der ITGrundschutz-Profile ist, die Erstellung der Sicherheitskonzeptionen zu erleichtern [16, S. 5].

## 2.4 IT-Grundschutz-Profile als Problemlösung

In der ISLL-Bund ist für den Betrieb des ISMS in obersten Landesbehörden nicht verbindlich  vorgegeben,  welche  ISMS-Methodik  anzuwenden  ist.  Bezüglich  der  anwendbaren ISMS-Methodiken wird festgehalten:

'Die Festlegung des Mindestsicherheitsstandards orientiert sich am IT -Grundschutz des BSI, dem IT-Grundschutz-Kompendium in der jeweils aktuellen Fassung sowie der ISO 2700x-Reihe.' [12, S. 9]

Eine Ausnahme stellen Ebenen-übergreifende Verfahren und Verbindungen dar. Wenn diese länderübergreifend betrieben werden, ist die Absicherung über den ITGrundschutz verbindlich [12, S. 14].

Beide ISMS-Methodiken sind in diesem Kapitel vorgestellt und in ihrem Vorgehen beschrieben.  Während  die  unterschiedlichen  Risikomanagementprozesse  dargestellt sind, besteht laut dem BSI eine ausreichende Deckungsgleichheit, um eine ISO 27001 Zertifizierung eines ISMS nach dem IT-Grundschutz zu ermöglichen [17, S. 1].

<!-- page: 43 -->

Die ISO und das BSI formulieren in gesonderten Standards zusätzliche Anforderungen an einzelne Branchen oder Einsatzbereiche der Informationstechnik. Eine sektorspezifische Norm, die sich auf die Anforderungen und das Umfeld von öffentlichen Verwaltungen im Bereich der Informationssicherheit bezieht, existiert nicht. Eine Anwendbarkeit von technischen Standards für oberste Landesbehörden kann in bestimmten Anwendungsfällen gegeben sein. So könnte eine oberste Landesbehörde die technische Richtlinie für die sichere E-Mail-Kommunikation anwenden.

Um die Umsetzung des ISMS und die Erstellung eines Sicherheitskonzeption in einer  obersten  Landesbehörde  zu  vereinfachen  und  zu  unterstützen,  wird  ein  ITGrundschutz-Profil erstellt. Mit dem IT-Grundschutz-Profil kann als anwenderorientierte Schablone auf die besonderen Anforderungen und Umstände einer Behörde im Bereich des ISM eingegangen werden. Zudem können sich die obersten Landesbehörden  bei  der  Erstellung  der  Sicherheitskonzeption  an  den  Vorgaben  des  IT-Grundschutz-Profils orientieren oder diese adaptieren.

Auf der Basis des IT-Grundschutz-Profils können sich die obersten Landesbehörden zusätzlich über weitere, vereinheitlichte Maßnahmen verständigen und mögliche Synergie- oder Kostensenkungseffekte hervorrufen. Dies ergänzt die Bestrebungen der ISLL-Bund, die ebenfalls diese Ziele verfolgt [12, S. 6-7].

Behörden, die bereits ein ISMS nach der ISO 27001 etabliert haben, können bei einem  ähnlichen  Anwendungsbereich  die  Sicherheitsanforderungen  aus  dem  ITGrundschutz-Profil als Grundlage für eine Vollständigkeitsprüfung verwenden.

<!-- page: 44 -->

## Kapitel 3 Grundlagen für das IT-Grundschutz-Profil

Nachdem  die  Forschungsfrage,  Problemstellung,  Rahmenbedingungen  sowie  die Grundlagen der IT-Grundschutz-Methodik dargelegt sind, wird weiteres Wissen über die Aufgaben und Anforderungen oberster Landesbehörden im Bereich der Informationssicherheit für ein IT-Grundschutz-Profil benötigt. In Anlehnung an die Forschungsfrage hat das IT-Grundschutz-Profil folgende Ziele:

- Das IT-Grundschutz-Profil soll den Informationsverbund einer obersten Landesbehörde  zur  Bewältigung  eines  generischen  Geschäftsprozesses darstellen.
- Dieser Geschäftsprozesses soll auf Basis der Standard-Absicherung abgesichert werden.
- In  dem  IT-Grundschutz-Profil  sollen  die  aktuellen  Anforderungen  der obersten  Landesbehörden  an  ein  ISMS  und  ein  IT-Grundschutz-Profil durch eine Zusammenarbeit und Kommunikation berücksichtigt werden.

Der Betrachtungsraum des IT-Grundschutz-Profils wird durch die Abgrenzung des Informationsverbundes festgelegt. Der im Informationsverbund betrachtete Geschäftsprozess wird anschließend abgesichert, wobei aus diesem die benötigten Informationen, Anwendungen sowie weitere Infrastrukturkomponenten - und deren Schutzbedürftigkeit - abgeleitet werden [64, S. 82-83].

Dass die obersten Landesbehörden als Teile der Landesverwaltung grundsätzlich organisatorisch selbstbestimmt sind [68, S. 30], stellt ein wesentliches Hindernis für die Feststellung eines gemeinsamen Geschäftsprozess dar. So gibt es keine bundesweit einheitliche Aufgabenverteilung der Ministerien, wie Schamburek am Beispiel einiger Innenministerien hervorhebt [69, S. 25-26]. Deshalb lässt sich kein generisches IT-Grundschutz-Profil für einen bestimmten Behördentypus, wie ein Innenministerium erstellen.

Stattdessen enthält das IT-Grundschutz-Profil eine schematische Sicherheitskonzeption eines Geschäftsprozesses einer obersten Landesbehörde unabhängig des Bundeslandes und der Ressortzugehörigkeit. Als Grundlage wird dazu ein allgemeiner Geschäftsprozess,  der  durch  möglichst  alle  obersten  Landesbehörden  wahrgenommen wird, für das IT-Grundschutz-Profil ermittelt und abgesichert.

Im ersten Unterkapitel wird zunächst auf Grundlage der Verwaltungsliteratur auf die Struktur der Landesverwaltungen sowie der obersten Landesbehörden und auf deren Aufgaben eingegangen. Ein weiteres Thema in Bezug auf diese Aufgaben ist die Digitalisierung der Verwaltung, auf welche ebenfalls in diesem Zusammenhang eingegangen wird.

Um die Annahmen der Fachliteratur mit Informationen aus der Verwaltungspraxis zu belegen, wird methodisch in der vorliegenden Arbeit zusätzlich auf eine Befragung als Erhebungsmethode zurückgegriffen. Diese wird im zweiten Unterkapitel konzipiert und in Form eines Fragebogens durchgeführt. Neben der Konzeption des Fragebogens wird auf dessen Umsetzung und Ergebnisse eingegangen. Im dritten Unterkapitel wird auf Basis der Literaturstudie und der Befragung ein generischer Geschäftsprozess entwickelt, den das IT-Grundschutz-Profil absichert.

<!-- page: 45 -->

## 3.1 Architektur einer obersten Landesbehörde

Die Fachliteratur der Verwaltungswissenschaft wird als erster Ausgangspunkt für die  Feststellung  der  Aufgaben und  Geschäftsprozesse der obersten Landesbehörden verwendet. Für die Feststellung dessen wird zunächst auf die Position der obersten Landesbehörden innerhalb der Landesverwaltungen und auf die Struktur der obersten Landesbehörden eingegangen. In den Verwaltungen des Bundes und der Länder gibt es unterschiedliche Verwaltungsebenen, die sich abstrakt in drei Schichten einordnen lassen [13, S. 44]:

1. Die Bundesverwaltung.
2. Die Landesverwaltungen.
3. Die Kommunalverwaltungen.

Einen Sonderfall zu den Ebenen 2 und 3 stellen die drei Stadtstaaten Bremen, Berlin und Hamburg dar. Zum einen sind in diesen Ländern die Verwaltungsapparate reduziert [70, S. 320], zum anderen wird die Landesregierung und ihr Verwaltungsunterbau anders bezeichnet. Gemäß den Landesverfassungen dieser drei Stadtstaaten besteht die Landesverwaltung, die mit der Kommunalverwaltung zusammengelegt ist [68, S. 32], aus den Senaten, denen jeweils die Senatoren als Behördenleiter vorstehen. Das Oberhaupt der Senatoren und der Regierung wird in diesen Ländern als regierender bzw. als erster Bürgermeister bezeichnet [71, S. 863].

Für die Verwaltung des Landes finden sich in den Landesverwaltungen unterschiedliche Institutionseben und -arten. Jede Institution hat unterschiedliche Aufgaben, wobei die Hierarchie von den obersten Landesbehörden als übergeordnete Verwaltungsebene ausgeht [72, S. 33]. Die untergeordneten Behörden werden in diesem Zusammenhang als nachgeordnete Behörden bezeichnet. Insgesamt kann so zwischen vier unterschiedliche Behördentypen in einer Landesverwaltung unterschieden werden:

1. Oberste Landesbehörden , als Senate und Ministerien an der Spitze der Verwaltungshierarchie, die unter anderem die nachgeordneten Verwaltungen beaufsichtigen [70, S. 633]
2. Obere Landesbehörden oder Landesoberbehörden , die den obersten Landesbehörden nachgeordnet sind, aber eine Zuständigkeit für das gesamte Land inne haben [13, S. 50].
3. Mittlere Landesbehörden oder Landesmittelbehörden ,  die  eine  verbindende,  kontrollierende  und  koordinierende  Funktion  zwischen  der obersten Verwaltungsebene und den unteren Landesbehörden innehaben. Sie sind nur für einen Teilbereich des Landes zuständig [68, S. 35].

<!-- page: 46 -->

4. Untere  Landesbehörden ,  die  bspw.  als  Finanz-  oder  Forstämter  ihre Aufgaben im Rahmen staatlicher Sonderverwaltungen wahrnehmen [72, S. 101].

Da nicht alle Länder diese Behördentypen nutzen, gibt es in Deutschland zwei unterschiedliche Verwaltungsorganisationen, in die sich die dreizehn Flächenländern unterteilen lassen [68, S. 71-72]:

1. Dreistufige Landesverwaltungen, die zwischen den landesweiten Behörden und den unteren Landesbehörden noch eigene regionalisierte mittler Behördenstrukturen aufweisen. Unter anderem ist dies Bayern, Nordrhein-Westfalen, Hessen oder Sachsen.
2. Zweistufige Landesverwaltungen, die zwischen den oberen Landesbehörden und den unteren Landesbehörden kein regionales Bindeglied aufweisen. Beispiele dafür sind Niedersachsen, Brandenburg oder Schleswig-Holstein.

Die Stadtstaaten lassen sich aufgrund der oben angeführten, verringerten Verwaltungsapparate hier nicht einordnen.

Um den Aufbau der Verwaltung eines Landes abzuschließen, wird hier mit Abbildung 3.1 die Gesamtdarstellung der Landesverwaltungen von Bogumil und Jann eingeführt. Diese haben die unterschiedlichen Verwaltungsebenen und -typen in einer Übersicht  grafisch  dargestellt,  woraus  deutlicher  hervorgeht,  wie  die  Landesverwaltungen strukturiert  sind.  Während Bogumil und Jann in der Originalabbildung ebenfalls die Bundesverwaltung dargestellt haben, wird in Abbildung 3.1 dagegen nur der relevante Teil der Landesverwaltung reproduziert:

<!-- page: 47 -->

Abbildung 3.1: Verwaltungsaufbau der Landesverwaltung nach Bogumil und Jann [72, S. 88] (Reproduktion)

<!-- image -->

<!-- page: 48 -->

## 3.1.1 Organisatorischer Aufbau

Nachdem die Position der obersten Landesbehörde in der Landesverwaltung dargestellt ist, wird nun auf die interne Struktur der Behörden eingegangen. Die Landesrechnungshöfe als faktische oberste Landesbehörden werden aufgrund einer anderen Aufgabenzuweisung [72, S. 131] nicht betrachtet, zudem sind diese ausdrücklich von der ISLL-Bund nicht umfasst [12, S. 5]. Diese Autonomie von der ISLL-Bund wird auf der faktischen Unabhängigkeit der Landesparlamente und der Rechnungshöfe von der restlichen Verwaltung begründet sein So legt beispielsweise Artikel 70 der Niedersächsischen Verfassung fest, dass die Mitglieder des Rechnungshofes richterliche Unabhängigkeit besitzen.

Die Leitung der obersten Landesbehörde obliegt einem Minister oder Senator als Teil der Landesregierung [72, S. 96]. Dem Minister steht in der Regel eine Stabsorganisation zur Seite, sein Vertreter ist ein Staatssekretär. Die Steuerung und Verwaltung der Behörde wird üblicherweise  in  einer  Zentralabteilung  wahrgenommen,  die fachliche Aufgabenwahrnehmung findet in den Referaten, den Abteilungen untergeordnet, statt [69, S. 16-20].

Abbildung 3.2 stellt den üblichen Aufbau einer obersten Landesbehörde dar, reproduziert von der Abbildung und den Schilderungen Schambureks:

Abbildung 3.2: Aufbau einer obersten Landesbehörde nach Schamburek [69, S. 60] (Reproduktion)

<!-- image -->

<!-- page: 49 -->

Da der Verwaltungsaufbau den Ländern selbst obliegt [72, S. 96], ist hier festzuhalten, dass einzelne oberste Landesbehörden oder ganze Bundesländer eine andere Struktur und Organisationsbezeichnung verwenden können. Als Grundlage für die hiesige Erstellung des IT-Grundschutz-Profils wird von dieser Struktur ausgegangen.

## 3.1.2 Aufgaben und Geschäftsprozesse

Der  Begriff  Geschäftsprozess  orientiert  sich  an  der  Definition  des  IT-Grundschutz-Kompendiums, da auch diese Methodik angewendet wird:

Ein Geschäftsprozess ist eine Menge logisch verknüpfter Einzeltätigkeiten (Aufgaben, Arbeitsabläufe), die ausgeführt werden, um ein bestimmtes geschäftliches oder betriebliches Ziel zu erreichen . [24, S. 63]

Um auf die Geschäftsprozesse der obersten Landesbehörden zu schließen, werden bei der Betrachtung der Literatur zunächst die Aufgaben der Behörden auf abstrakter Ebene betrachtet.

## 3.1.2.1 Aufgabenzuweisungen aus den gemeinsamen Geschäftsordnungen

Die Aufgabenwahrnehmung in den obersten Landesbehörden findet in den Referaten statt, welche in Abteilungen zusammengefasst werden [72, S. 143]. Die Aufgabenverteilung wird gewöhnlich in einem Geschäftsverteilungsplan festgehalten. Aus den Geschäftsverteilungsplänen gehen die Zuständigkeiten der Organisationseinheiten sowie die Funktionen hervor [73].

Für die Bestimmung einer allgemeinen Aufgabe oder eines allgemeinen Geschäftsprozesses bieten die Geschäftsverteilungspläne keine Ausgangsbasis, da diese die Zuständigkeiten in einer Behörde isoliert betrachten. Eine Analyse der gesamtdeutschen Geschäftsverteilungspläne  wird  aufgrund  des  Umfangs  durch  die  Gesamtzahl  der obersten Landesbehörden nicht in Betracht gezogen.

Dagegen ist auf der Landesebene die Aufgabenverteilung zwischen den Ministerien und Senate ebenfalls reglementiert. Um eine Zusammenarbeit zwischen den obersten Landesbehörden zu koordinieren und zu strukturieren, gibt es in jedem Bundesland zur interministeriellen Verfahrensregelung [74, S. 325] eine gemeinsame Geschäftsordnung (GGO). Eine Auswertung dieser sechszehn GGO'en ergibt, dass dort in der Regel keine Aufgaben und Prozesse konkret beschrieben werden.

Eine Ausnahme bildet hier die GGO des Landes Niedersachsen, die in § 13 der Gemeinsamen Geschäftsordnung der Landesregierung und der Ministerien in Niedersachsen folgendes bestimmt:

'Die Ministerien sollen sich auf gesetzgeberische und allgemein lenkende Aufgaben sowie auf Aufgaben der Aufsicht, Planung und Erfolgskontrolle beschränken. Vorbehaltlich gesetzlicher Regelungen sind Vollzugsaufgaben und die Bearbeitung von Einzelfällen nachgeordneten Behörden vorbehalten.' [75, S. 10]

Die GGO des Landes Nordrhein-Westfalen (NRW) definiert ebenfalls in § 2 der GGO NRW die Aufgaben der Ministerien:

<!-- page: 50 -->

'Die Ministerien nehmen Aufgaben wahr, die der Erfüllung oder Unterstützung von Regierungsfunktionen  dienen.  Dazu  zählen  insbesondere  die  strategische  Gestaltung und Koordination von Politikfeldern, die Realisierung von politischen Zielen, Schwerpunkten und Programmen, die Beteiligung an Gesetzgebungsverfahren sowie die Wahrnehmung von Steuerungs- und Aufsichtsfunktionen gegenüber dem nachgeordneten Geschäftsbereich. Die Ausrichtung auf ministerielle Kernaufgaben ist durch ständige Aufgabenkritik sicherzustellen. Operative Aufgaben und die Bearbeitung von Einzelfällen sind in der Regel den Dienststellen des Geschäftsbe reichs vorbehalten.' [76, S. 1]

Weitere Aufgabenzuweisungen sind in den verbleibenden 14 GGO'en nicht vorhanden.

## 3.1.2.2 Aufgaben aus landesbezogener Fachliteratur

Die Fachliteratur der Verwaltungswissenschaft befasst sich ebenfalls mit den Aufgaben und Geschäftsprozessen einer obersten Landesbehörde. Es ist zwischen landesspezifischen und allgemeinen Werken aus der Verwaltungswissenschaft zu unterscheiden. Bei einem Rückgriff auf die landesspezifische Fachliteratur stellen die Autoren Träger und Priebus bezogen auf Sachsen-Anhalt folgendes fest:

'Der Einbringung von Gesetzesinitiativen gehen überdies schon vor deren Diskussion im Kabinett zum Teil langwierige Gespräche zwischen dem jeweils federführenden Ministerium und den übrigen Ministerien voran. Besonders zeitaufwändig sind Projekte, die von hoher politischer Bedeutung für die Regierung sind. Grundsätzlich ist zu jedem Gesetz die Zustimmung des Finanz- sowie des Justizministeriums einzuholen; häufig auch die des Innenministeriums. ' [77, S. 132]

## Des Weiteren schildern sie:

' Dies erklärt sich zum einen daraus, dass neben der originären Landesgesetzgebung auch die Ausführungsbestimmungen für viele Bundesgesetze formuliert werden müssen, was ohne eine entsprechende Ministerialbürokratie nicht zu leisten wäre. Zum anderen sind diese Gesetze, von den Ministerialbürokratien als Spitzen der Landesverwaltung auszuführen; beziehungsweise deren Ausführung ist zu überwachen. Überdies gibt es, wenn man das Beispiel des Wirtschaftsministeriums aufgreift, Bereiche, in denen - auch auf Bundesebene - nicht immer die Formulierung von Gesetzen im Vordergrund steht. Vielmehr geht es hier häufig um die Konzipierung von Fördermaßnahmen (zum Beispiel Landesprogrammen zur Stärkung regionaler Wirtschaftszentren), die der ministeriellen Entwicklung und Koordinierung bedürfe n.' [77, S. 133]

Als weiteres Beispiel werden die Autoren Nentwig und Werwath herangezogen. In ihrem Buch zu der Politik und dem Regieren in Niedersachsen unterscheiden die Autoren zwischen den folgenden Aufgaben [78, S. 266-270]:

- Die konzentrierte Rechts- und Fachaufsicht über die nachgeordneten Behörden, in der Praxis durch Verordnungen und Erlasse.

<!-- page: 51 -->

- Die Unterstützung der Hausleitung (gemeint ist der Minister) für eine angemessene politische Handlungsfähigkeit.
- Die zum Teil weisungsgebundene Mitarbeit an Gesetzen.
- In den Stabsorganisationen die Organisation, Pressearbeit sowie strategische Planung und Koordinierung.

## 3.1.2.3 Aufgaben aus allgemeiner Fachliteratur

Nun wird auf Fachliteratur zurückgegriffen, die sich auf die gesamtdeutsche Verwaltung bezieht. Bogumil und Jann nennen in ihrem Lehrbuch zu einer Einführung in die Verwaltungswissenschaft drei Aufgaben, die einer obersten Landesbehörde zuzuordnen sind [72, S. 154]:

- Unterstützung  der  Regierungstätigkeit  durch  den  Entwurf  von  Gesetzen, Rechtsverordnungen und Verwaltungsvorschriften.
- Politische Unterstützung des Ministers durch die Beantwortung parlamentarischer Anfragen und die Vorbereitung von Reden.
- Steuerung und Überwachung des Gesetzesvollzugs durch die nachgeordneten Behörden.

Becker stellt in seinem Lehrbuch zu der öffentlichen Verwaltung insgesamt vier Aufgaben fest [70, S. 633]:

- Die Vorbereitung von Gesetzen.
- Die Planung der Umsetzung von Gesetzen.
- Der Vollzug der Gesetze als oberste Verwaltungsbehörde.
- Die Aufsicht über nachgeordnete Behörden.

## 3.1.2.4 Gesamtbetrachtung der Aufgaben

Aus diesen drei Quellen werden die Aufgaben der obersten Landesbehörden zusammengefasst. Abstrakt formuliert sind dies:

- Das Erlassen von Verordnungen, Erlassen und die Mitarbeit an Gesetzen.
- Die Ausführung von Bundes- und Landesgesetzen, sofern diese nicht an nachgeordnete Behörden delegiert ist.
- Die Aufsicht und Kontrolle der nachgeordneten Behörden.
- Die (politische) Unterstützung des Ministers durch Informationsbeschaffung und sonstige Tätigkeiten.
- Die  Selbstverwaltung  der  Behörde  durch  strategische  Planung,  Pressearbeit und Personalsachen.

<!-- page: 52 -->

## 3.1.3 Digitalisierung und IT-Infrastruktur

Um diese Aufgaben wahrzunehmen, stehen den Behörden Ressourcen in digitaler und analoger Form zur Verfügung. Dies ist relevant, da festgestellt werden muss, wo Informationstechnik für die Aufgabenbewältigung eingesetzt wird. Wenn die Aufgaben nicht digital wahrgenommen und umgesetzt werden, so sind diese zwar auch von einem ISMS umfasst, aber nicht durch die Absicherung der IT.

Aus der rechtlichen Perspektive besteht seit nahezu sechs Jahren das Gesetz zur Förderung der elektronischen Verwaltung, welches die Digitalisierung der Bundesverwaltung regelt [7, S. 192]. Komplementär gibt es mittlerweile in der Mehrheit der deutschen Bundesländer E-Government-Gesetze, wobei die auf Bundes- und Landesebene nicht einheitlichen Regelungen gemäß Beckermann gemeinsam folgende Ziele verfolgen [8, S. 169-172]:

- Eine Einführung digitaler Zugänge zu Behörden - neben einer persistenten physischen Möglichkeit.
- Eine Digitalisierung der Sachbearbeitung in der Verwaltung und des behördeninternen Schriftverkehrs.
- Die Präsentation der Behörden im Internet sowie die Publikation von amtlichen Mitteilungen und Gesetzen.
- Elektronischer Zahlungsverkehr im Umgang des Bürgers mit Behörden.

Praktisch nutzen alle 16 Landesverwaltungen einen zentralen IT-Dienstleister, der, häufig in der Gestalt einer Anstalt öffentlichen Rechts, die Verwaltung der Informationstechnik zu einem gewissen Grad übernimmt [29, S. 100-101]. Trotz dieser Regelung wird der aktuelle Stand in der Digitalisierung der Verwaltung kritisch betrachtet. Speyer merkt in seinem Beitrag an, dass die deutsche Verwaltung in Sachen Digitalisierung verglichen mit anderen Staaten, besonders in der EU, weit zurückliegt [6, S. 443-444]. Einer von Speyer zitierten EU-Studie aus 2016 zufolge, lag Deutschland in der Digitalisierung der Verwaltung auf Platz 18 der gesamten EU-Staaten.

Zu einem ähnlichen Schluss kommen auch Stember, Eixelsberger und Spichiger, die einen Vergleich zwischen Deutschland, der Schweiz und Österreich ziehen. Auch in dieser Vergleichsgruppe liegt die Digitalisierung der deutschen Verwaltung zurück und hat, neben einer niedrigen Dienstleistungsqualität für Bürger, auch mit schwindenden Personalressourcen in diesem Bereich zu kämpfen [7, S. 79-80].

Für das IT-Grundschutz-Profil folgt daraus, dass alle Bundesländer auf der Ebene der obersten Landesbehörden zentrale IT-Dienstleister verwenden. Der Grad der Auslagerung und die Anzahl der Dienstleister ist dagegen variabel [29, S. 101]. Die rechtlichen Regelungen gestalten sich nicht einheitlich, sodass diese nicht in dem IT-Grundschutz-Profil berücksichtigt werden.

<!-- page: 53 -->

## 3.2 Befragung als anwenderbezogene Datenerhebung

Neben der Fachliteratur wird in dem Rechercheprozess zu dem IT-GrundschutzProfil die Verwaltungspraxis berücksichtigt. Denn grundsätzlich ist durch das BSI vorgesehen,  dass  ein  IT-Grundschutz-Profil  durch  Gremien,  Anwendergruppen  einer Branche oder Vertreter eines Themenbereiches erstellt werden [67, S. 36-37]. Diese Anwender- bzw. Praxisorientierung wird in der Masterarbeit auf anderem Wege mit einer Befragung der Informationssicherheitsbeauftragten (ISB) der Landesverwaltungen aufgegriffen.

Das Ziel der Befragung ist, Wissen zu den gemeinsamen Gegebenheiten in obersten Landesbehörden zu generieren und als praxisorientiertes Instrument die Wirklichkeit des  aktuellen  Verwaltungshandelns  im  Bezug  zum  ISM  darzustellen.  Die  Befragung wird über einen Fragebogen durchgeführt, der den ISB von 15 Landesverwaltungen übersandt wird. Die Landesverwaltung Niedersachsen wird an dem Fragebogen aufgrund einer direkten Zusammenarbeit im Rahmen dieser Masterarbeit nicht beteiligt.

Der Fragebogen verfolgt zwei Ansätze: Zum einen soll Wissen bezüglich der verwendeten Geschäftsprozesse, Anwendungen und weiteren Teilen des ISMS in einer obersten Landesbehörde gewonnen werden. Zum anderen soll die Befragung mehrerer Teilnehmer eine statistische Auswertung ermöglichen, um so gemeinsame und divergierende Angaben zu berücksichtigen.

## 3.2.1 Methodische Grundlage

Das Methodenwissen im Bereich der Durchführung von Befragungen und der Erstellung von Fragebögen orientiert an Quellen aus der Sozialwissenschaft. Nach Berger-Grabner sucht die quantitative Sozialwissenschaft nach Wissensgewinnung durch Modelle und durch zahlenmäßig festgestellte Signifikanzen [79, S. 117]. Tragender Gedanke ist die Operationalisierung der Forschungsparameter, die sich in statistisch auswertbare Daten niederschlägt.

Dem gegenüber stehen laut Berger-Grabner die qualitativen Forschungsmethoden, die versuchen die Wirklichkeit zu beschreiben, zu interpretieren und zu verstehen. Dieser Forschungsansatz verfolgt damit nicht das Ziel, eine statistische Repräsentanz zu ermöglichen. Vielmehr geht es um das Ergründen von Zusammenhängen [79, S. 117-118].

Dieser Fragebogen versucht Elemente beider Forschungsrichtungen zu kombinieren. Es sollen statistisch relevante Daten erhoben werden, um Gemeinsamkeiten und nur einzeln auftretende Aussagen zu unterscheiden. Andererseits sollen die befragten Personen die Möglichkeit haben, frei ihre Antworten zu formulieren und Zusammenhänge zu erläutern. Ohne vorgegebene Antwortmöglichkeiten können so gegebenenfalls bislang nicht bekanntes Wissen und Zusammenhänge erfasst werden. So gibt es beispielsweise keine Wissensgrundlage zu besonderen Anforderungen der Verwaltung an das ISM oder zu Problemen bei der Umsetzung eines ISMS.

<!-- page: 54 -->

Damit wird mit dem Fragebogen ein qualitativer sowie quantitativer Ansatz verfolgt. In der Sozialwissenschaft wird dieser Ansatz mitunter als Mixed Methods bezeichnet,  da  zwei  eigentlich  getrennt  angewendete Forschungsmethoden miteinander  verbunden werden [80, S. 153-154]. Aus hiesiger Perspektive können die beiden folgenden Vorteile durch diese Kombination genutzt werden:

1. Die Reichweite der qualitativen Aussagen der Befragten kann durch die quantitative Erhebung abgegrenzt werden.
2. Vorher nicht bekannte Umstände können erfasst werden, gleichzeitig erschließt sich, ob dies gegebenenfalls nur ein Einzelphänomen ist.

Der qualitative Anteil wird über offene Fragen in den Fragebogen umgesetzt. Durch eine möglichst große Anzahl von befragten Personen wird der quantitative Anteil der Befragung hergestellt. Hier wird eine Kombination von einer klassischen quantitativen Methode (standardisierter Fragebogen) mit einer qualitativen Dimension angestrebt, die in dieser Form auch von Kelle genannt wird [80, S. 158]. Kuckartz bezeichnet dies als 'Transferdesign' [81, S. 87].

In der Unterscheidung zwischen der Dominanz einer Forschungsrichtung im Forschungsdesign [80, S. 160], ist hier eine Gleichwertigkeit der quantitativen und qualitativen Forschungsrichtung und Auswertungsgewichtung angestrebt. Dementsprechend soll die höchste Signifikanz von Antworten ausgehen, die gleichsam von mehreren Befragten gegeben wurden.

## 3.2.2 Fragebogenkonzeption

Der Fragebogen wird als exploratives Forschungsmittel verwendet und soll Wissen generieren, welches bislang nicht in diesem Kontext zur Verfügung steht. Letztlich bietet die Verwaltungsliteratur zwar einen theoretischen und abstrakten Blick auf die obersten Landesbehörden, inwiefern dieser die Wirklichkeit aus Sicht der ISB der Länder wiederspiegelt, ergibt sich jedoch nicht.

Unter Berücksichtigung dieser Rahmenbedingung wird der Fragebogen konzipiert. Der Prozess gliedert sich in vier Teilbereiche: Die Auswahl der zu befragenden Personen, die Ableitung der Fragen aus der Forschungsfrage, die Formulierung der Fragen und die Strukturierung des Fragebogens.

## 3.2.2.1 Zielgruppe

Vor der Fragestellung muss die Zielgruppe festgelegt werden, die mit dem Fragebogen erreicht werden soll. Die Teilnehmer aus der Zielgruppe sollen eine Expertise in dem Fachgebiet des ISM in Behörden besitzen und zugleich für eine Befragung erreichbar sein. In dieser Arbeit wird davon ausgegangen, dass als Hauptquelle der Expertise die berufliche Tätigkeit im ISM einer Behörde dient.

Aufgrund der Anforderung des Umsetzungsplans der Leitlinie für die Informationssicherheit in der öffentlichen Verwaltung aus 2013, dass jedes Land einen ISB der Landesverwaltung benennen muss [82, S. 3], verfügen jene nun über einen oder eine entsprechende ISB auf der Ebene der Landesverwaltung.

<!-- page: 55 -->

Über den IT-Planungsrat werden diese 15 ISB schriftlich befragt. Bei einer mündlichen Vorabfrage haben sich die Teilnehmer des IT-Planungsrates bereit erklärt, einen Fragebogen über den ISB der Landesverwaltung Niedersachsen anzunehmen und auf freiwilliger Basis zu beantworten.

Während die einzelnen ISB der obersten Landesbehörden ebenfalls als kompetente Ansprechpartner erscheinen, steht eine Kommunikationsplattform nur über den IT-Planungsrat zur Verfügung. Daher werden die 15 ISB der Landesverwaltungen als übergeordnete Koordinationsebene für den Fragebogen ausgewählt. Aus der koordinativen Tätigkeit des ISM in der gesamten Landesverwaltung ist ein tiefgehendes Wissen über die  Anforderungen der obersten Landesbehörden an ein ISMS und über deren Geschäftsprozesse sowie Aufgaben anzunehmen.

## 3.2.2.2 Ableitung der Fragen

Die Fragestellungen ergeben sich aus der Forschungsfrage sowie aus den Zielen der Befragung  hinsichtlich  der  Wissensgenerierung.  Um  relevante  Fragen  aus  der  Forschungsfrage herzuleiten, wird die Methodik von Kaiser für Experteninterviews angewandt [83, S. 55-60].

Gemäß Kaiser soll diese Herleitung der Fragen mehrere Stufen durchlaufen. Zunächst wird die zentrale Forschungsfrage betrachtet und es werden davon ausgehend die Analysedimensionen festgestellt. Darauf aufbauend ergeben sich zu jeder Analysedimension Fragenkomplexe, die bei Kaiser in die Formulierung der konkreten Interviewfrage münden. Zunächst wird die zentrale Forschungsfrage und die daraus entstehenden Analysedimensionen dargestellt:

- Welche Anforderungen muss ein IT-Grundschutz-Profil für eine oberste Landesbehörde beinhalten?
- o Aktueller Stand des ISMS in den Landesverwaltungen
- o Informationsverbund
- o Risikobetrachtung
- o Zusätzliche Anforderungen an ein ISMS

Anschließend werden aus den Analysedimensionen die entstehenden Fragenkomplexe betrachtet:

- Aktueller Stand des ISMS in den Landesverwaltungen
- o Gründe für die Umsetzung des ISMS
- o Verankerung von ISM in der Behördenstruktur
- o ISMS-Methodik
- o Stand der Umsetzung
- o Besonderheiten bei der Umsetzung
- Informationsverbund
- o Geschäftsprozesse

<!-- page: 56 -->

- o Anwendungen
- o IT-Systeme
- o Kommunikationsverbindungen
- o Gebäude und Räume
- Risikobetrachtung
- o Risikoneigung
- o Quantifizierung des Risikos
- o Schutzbedarfskategorien
- o Schutzbedarfe
- o Risikoanalyse
- Zusätzliche Anforderungen an ein ISMS
- o Betrachtete Geschäftsprozesse
- o Betrachtete Zielobjekte
- o Besonderheiten für Behörden

Nach Anwendung der Methodik ergeben sich insgesamt 18 Fragenkomplexe, die von dieser Befragung umfasst werden können. Daraus ableitbare Fragen werden in einem nachfolgenden Unterkapitel dargestellt, während zunächst auf die Struktur des Fragebogens eingegangen wird.

## 3.2.2.3 Struktur des Fragebogens

Der Fragebogen muss für die Befragten logisch strukturiert sein [84, S. 146]. An den Anmerkungen von Klöckner und Friedrichs zu der Gestaltung von Fragebögen orientiert [85, S. 675-684], wird der Fragebogen in folgende Bereiche aufgeteilt:

1. Anschreiben und Fragen zu der befragten Person.
2. Fragen zu der Behörde, in der oder die Befragte tätig ist.
3. Fragen an den Erfahrungsschatz der befragten Person bezogen auf ISM.
4. Raum für eigene Anmerkungen.
5. Abschluss.

Das Anschreiben beschreibt das Ziel der Masterarbeit und des IT-Grundschutz-Profils. Hier wird hervorgehoben, dass das IT-Grundschutz-Profil die obersten Landesbehörden als betroffene Organe mit einbeziehen und diesen einen Mehrwert bieten soll. Das Anschreiben enthält zudem Fragen zu der Person und Tätigkeit der Befragten. Dies dient unter anderem der Nachvollziehbarkeit, ob tatsächlich die vorausgesetzte Expertise vorliegt.

Im ersten Hauptteil werden den Befragten zunächst Fragen zu einer Behörde gestellt, in der diese tätig sind oder die diese gut kennen. Dadurch wird mit den Antworten Bezug auf die Realität in den obersten Landesbehörden hergestellt. Da die Zielgruppe aktuell nicht in einer obersten Landesbehörde tätig ist, sollen die Befragten eine oberste Landesbehörde auswählen, für die die vorgelegten Fragen beantwortet werden.

<!-- page: 57 -->

Im zweiten Hauptteil wird auf das Wissen der Befragten als Experten für behördliche Informationssicherheit zurückgegriffen. Damit wird eine Übersicht erlangt, welche generischen Geschäftsprozesse bestehen und wo beispielsweise Probleme bei der Umsetzung des ISMS für eine oberste Landesbehörde entstehen können.

In den Anmerkungen und dem Schluss des Fragebogens bekommen die Teilnehmer die Möglichkeit, noch weitere Antworten und Anmerkungen zu geben. Zuletzt wird der  Fragebogen durch  Angaben zu dem Vorgehen, den Zusende- und Anonymisierungsmöglichkeiten und der Antwortfrist beendet.

## 3.2.2.4 Fragestellungen

Ausgehend von den Fragekomplexen aus Unterkapitel 3.2.2.2 und der Strukturierung aus Unterkapitel 3.2.2.3 werden nun die Fragen dargestellt, die im Rahmen des Fragebogens gestellt werden. Die hier ausformulierten Fragen orientieren sich bestmöglich an den Grundsätzen von Porst in seinem Arbeitsbuch zu Fragebögen [84, S. 99100]. Bei den biografischen Fragen werden folgende Daten erhoben:

- Das Tagesdatum, an dem die Befragten das Dokument ausgefüllt haben.
- Den Namen der Person.
- Die Institution.
- Das Bundesland.
- Die aktuelle Tätigkeit.
- Eine freiwillige Angabe der Erreichbarkeit für Rückfragen.

An dieser Stelle wird gegenüber den Teilnehmern und Teilnehmerinnen hervorgehoben, dass die Daten in der Masterarbeit aus Datenschutzgründen nicht veröffentlicht werden. Nichtsdestotrotz müssen diese Daten erhoben werden, um auf die Kompetenz der Befragten und damit auf die Validität der Antworten schließen zu können.

Der erste Teil beginnt mit den Fragen zu dem ISMS einer obersten Landesbehörde, die die befragte Person frei wählen kann. Da im Vorfeld bekannt ist, dass alle Landesverwaltungen  den IT-Grundschutz anwenden, wird in der Fragebogenerstellung  auf eine Definition der gängigen Begriffe verzichtet. Diese sind im Glossar des IT-Grundschutz-Kompendiums definiert [24, S. 59-71].

Die Fragen im ersten Teil, zum ISMS einer Behörde, sind wie folgt formuliert:

1. Für welche Institution werden Sie die folgenden Fragen beantworten?
2. Der modernisierte IT-Grundschutz unterscheidet in dem Standard 200-2 sowie dem IT-Grundschutz-Kompendium zwischen der Basis-, Kern- und StandardAbsicherung als anzuwendende Methodik. Welche dieser drei Methodiken verwendet Ihre Institution oder wird sie in der Zukunft anwenden?

<!-- page: 58 -->

3. Wie weit ist das ISMS in der ausgewählten Institution umgesetzt (bspw. in Planung, teilweise oder vollständig)? Sollte das ISMS nur teilweise umgesetzt sein, bitte ich Sie die fehlenden Bereiche zu nennen.
4. Welcher Geltungs- beziehungsweise Anwendungsbereich wurde für das ISMS in Ihrer Institution formuliert?
5. Welche Anwendungen sind von Ihrer Behörde im Rahmen des ISMS erfasst worden?
6. Welche IT-Systeme wurden im Rahmen der Strukturanalyse festgestellt?
7. Wurden im Rahmen der Strukturanalyse Zielobjekte mit hohem oder sehr hohem Schutzbedarf festgestellt? Bitte zählen Sie diese auf.
8. Erbringen Dritte für Ihre Institution IT-Dienstleistungen? Bitte zählen Sie gegebenenfalls die ausgelagerten Zielobjekte (Anwendungen, Systeme, etc.) auf.
9. Wurden Zielobjekte mit hohem oder sehr hohem Schutzbedarf Dritte ausgelagert? Bitte zählen Sie diese gegebenenfalls auf.

Es handelt sich um neun offene Fragen, die von den Teilnehmern beantwortet werden sollen. Die Fragen sind hier fortlaufend nummeriert, sodass die Antworten in komprimierter Form in Anlage A.2 und A.3 dargestellt werden können. Im zweiten Teil werden weitere sechs Fragen an den Erfahrungsschatz der Befragten gerichtet:

10. Welche Geschäftsprozesse würden Sie für eine schematisch dargestellte oberste Landes-behörde als typisch ansehen? Wie sind diese definiert?
11. Welche Zielobjekte sind in einer obersten Landesbehörde Ihrer Einschätzung nach  als  besonders  schützenswert  anzusehen  (Schutzbedarf  hoch  oder  sehr hoch)?
12. Welches Schutzziel der Informationssicherheit (Vertraulichkeit, Integrität, Verfügbarkeit) ist das Wichtigste in einer obersten Landesbehörde? Bitte begründen Sie kurz.
13. Denken Sie die Schutzziele 'Nicht -Abstreitbarkeit ', 'Vertrauen', 'Nachvollziehbarkeit' oder 'Verlässlichkeit' sind relevant für die Informationssicherheit in einer obersten Landes-behörde? Bitte nennen Sie die relevant erscheinenden Schutzziele und begründen Sie kurz.
14. Können  Sie  Anforderungen  an  ein  IT-Grundschutz-Profil  für  eine  oberste Landes-behörde formulieren?
15. Gab oder gibt es bei der Umsetzung des ISMS Probleme in Ihrer Institution? Bitte erläutern Sie die, Ihrer Einschätzung nach, schwerwiegendsten Probleme.

In Anlage A.1 dieser Masterarbeit befindet sich der Fragebogen, der den Teilnehmern zur Beantwortung übersandt wurde. Persönliche Daten des Autors sind zur Wahrung der Privatsphäre entfernt.

<!-- page: 59 -->

## 3.2.3 Umsetzung des Fragebogens

Das Konzept des Fragebogens verfolgt unter  anderem das Ziel,  eine  möglichst hohe  Antwortrate  zu  erreichen.  Angelehnt  an  die  Ausführungen  von  Engel  und Schmidt zur Unit-Nonresponse [86, S. 333-341] werden dazu folgende Maßnahmen umgesetzt:

- Der Fragebogen wird vorab angekündigt und eine Bereitschaft zur Teilnahme wird abgefragt.
- Zu Beginn des Fragebogens wird der Nutzen für die Teilnehmer dargelegt (Unterstützung eines IT-Grundschutz-Profils als Mehrwert für alle obersten Landesverwaltungen).
- Der Umfang des Fragebogens wird auf zentrale Fragen reduziert, um die Abneigung der Antwort durch zu großen Zeitaufwand zu reduzieren.
- Es wird ein klarer Abgabezeitraum gesetzt und vor der Abgabe wird an die Befragung erinnert.
- Der Aufwand für die Befragten wird durch die digitale Umsetzung des Fragebogens weiter reduziert.

Der Fragebogen wird als ausfüllbares Textdokument digital an die Teilnehmer per EMail versendet. Die Teilnehmer haben dadurch die Möglichkeit, die Antwort an den Autor der Masterarbeit oder an den ISB der niedersächsischen Landesverwaltung zu senden. Als Antwortfrist wird den Teilnehmern ein Zeitraum von vier Wochen eingeräumt, eine Woche vor Fristablauf wird eine Erinnerung versandt.

Nach Ablauf der Frist gingen auf diesem Weg sechs Antworten ein. Dies entspricht einer Antwortquote von 40%. Die anonymisierten Antworten sind nummeriert im Anhang A.2 und A.3 der Masterarbeit angefügt. Die Kontaktdaten der Personen sowie die jeweilige Behörde aus der ersten Frage sind nicht dargestellt. Zusätzlich sind die Antworten in zufälliger Reihenfolge angeordnet, so dass eine Identifizierung einzelner Landesverwaltungen und Befragten vermieden wird.

## 3.2.4 Auswertung der Ergebnisse

Wie zuvor dargestellt ist das Ziel des Fragebogens, Gemeinsamkeiten zwischen den Ländern bezogen auf die Geschäftsprozesse, die verwendete IT und das behördliche ISM festzustellen. Deshalb besteht ein besonderer Fokus auf Fragen, in der es zu mehrheitlich gleichen oder ähnlichen Antworten gekommen ist. Es wird dennoch auf die Antworten aller Fragen eingegangen.

## 3.2.4.1 Allgemeine Angaben

Zunächst wird die berufliche Verteilung der Befragungsteilnehmer festgestellt. Es haben drei ISB der Landesverwaltungen geantwortet, zwei Antworten gingen von ISB aus  einer  obersten  Landesbehörde  ein.  Eine  Antwort stammt  von  einer  oder  einem Sachbearbeiter*in eines Fachreferats für Informationssicherheit.

<!-- page: 60 -->

Von einer Expertise aller Antwortenden wird aufgrund der beruflichen Tätigkeit in dem behördlichen ISMS ausgegangen, auch wenn nur drei der Antwortenden der ursprünglichen Zielgruppe angehören.

## 3.2.4.2 Rückmeldungen auf die Fragen des ersten Hauptteils

Bezogen  auf  die  betrachtete  Behörde,  haben  diese  in  vier  Fällen  eine  konkrete oberste Landesbehörde genannt. Zwei Personen haben die Folgeantworten auf die gesamte Landesverwaltung bezogen.

Bezüglich der Umsetzungsmethodik des ISMS sind fünf der betrachteten Organisationen mindestens in der langfristigen Planung auf eine Standard-Absicherung orientiert. Manche Organisationen setzen zuvor eine Basis- oder Kern-Absicherung um, eine befragte Person gibt an, dass die Absicherungsmethodik von der jeweiligen Stellung der Organisation abhänge. Ebenso befinden sich fünf der sechs mitgeteilten ISMS noch in Planung oder im Aufbau, nur eine Rückmeldung verweist auf eine vollständige Umsetzung.

Das ISMS umfasst mehrheitlich die gesamte Behörde, vier Personen haben entsprechendes zum Ausdruck gebracht. Die beiden weiteren Antworten zu dieser Frage beziehen sich nicht auf den Anwendungsbereich im Sinne der Frage, sondern auf das Vorgehen auf der Ebene der Landesverwaltung bzw. die festgelegte Methodik. Somit ist bei 100% der validen Antworten die gesamte Behörde von dem ISMS umfasst.

Die Fragen nach den Anwendungen und IT-Systemen wird von den Teilnehmern ohne Übereinstimmung beantwortet, selbiges gilt für festgestellte Schutzbedarfe.  Im Falle von konkret genannten Anwendungen oder IT-Systemen, die nicht einem ressortspezifischen Fachverfahren zuzuordnen sind, sind von den Befragten stets Produkte des Herstellers Microsoft genannt worden.

Bezüglich  der  Auslagerung  von  Zielobjekten  antworten  dagegen  alle  Befragten, dass ein IT-Dienstleister genutzt wird. Die Antworten unterscheiden sich hinsichtlich der tatsächlich ausgelagerten Behördenanteile. Ebenfalls scheint kein einheitliches Vorgehen im Umgang mit der Auslagerung von Zielobjekten hohen Schutzbedarfes zu bestehen, die Antworten auf die entsprechende Frage gestalten sich unterschiedlich.

## 3.2.4.3 Rückmeldungen auf die Fragen des zweiten Hauptteils

Die Teilnehmer der Befragung haben sich bezüglich eines generischen Geschäftsprozesses nicht einheitlich geäußert. Diese Frage ist unterschiedlich interpretiert worden, sodass äußerst unterschiedliche Arten von Geschäftsprozessen von den Teilnehmern genannt werden - abhängig des Verständnisses von einem Geschäftsprozess.

Betrachtet man die sechs Antworten gemäß der Definition eines Geschäftsprozesses nach dem IT-Grundschutz (vgl. Kapitel 1) lassen sich folgende Prozesse feststellen (jeweils eine Nennung):

- Gesetzgebungsverfahren
- Rechtssetzungsverfahren
- Daseinsvorsorge

<!-- page: 61 -->

- Aufrechterhaltung des Verwaltungsbetriebes

Obwohl der Begriff ' Zielobjekt ' in der IT-Grundschutz-Methodik einheitlich verwendet wird, sind zu der 12. Frage ebenfalls divergierende Antworten eingegangen. Zum Großteil haben die Befragten schützenswerte Geschäftsvorgänge wie die Personalbearbeitung oder geschäftskritische Verfahren angegeben. Eine befragte Person hat indes konkrete Zielobjekte benannt:

- Verzeichnisdienste
- Zentrale Anmelde- und Identifizierungsdienste
- Zentral geführte Register

Die Fragen zu der Gewichtung der Schutzziele Vertraulichkeit, Integrität und Verfügbarkeit sowie zu weiteren Schutzzielen haben zu keinen übereinstimmenden Aussagen geführt. Auch wenn die Teilnehmer jeweils nachvollziehbar darstellen, weshalb sie ein oder kein Sicherheitsziel bevorzugen, lässt sich kein Konsens ableiten.

Zu spezifischen Anforderungen für ein IT-Grundschutz-Profil haben alle Teilnehmer ausführliche Antworten eingetragen. Wie zuvor kommt es zu wenigen Übereinstimmungen, konkrete Anforderungen, die zusätzlich als eine Anforderung in einem ITGrundschutz-Baustein verwendet werden könnten, gehen daraus nicht hervor.

Als letzte Frage werden die Teilnehmer nach Problemen bei der Umsetzung eines IT-Grundschutz-Profils befragt. Hier kommt es zu folgenden Überschneidungen der Antworten:

- Drei von sechs Befragten geben an, dass nicht ausreichend Ressourcen für die Umsetzung von Informationssicherheit zur Verfügung gestellt werden.
- Vier von sechs Befragten bemängeln, dass auf der Führungsebene der Behörden der Informationssicherheit  kein  ausreichender  Stellenwert  zugemessen wird. Ein Teilnehmer gibt in diesem Zusammenhang an, dass alle weiteren Probleme aus dieser fehlenden Aufmerksamkeit entstammen.
- Nur eine befragte Person gibt an, dass es zu keinen Problemen bei der Umsetzung gekommen sei.

## 3.2.4.4 Schlussfolgerungen aus der Befragung

Aufgrund der geringen Beteiligung wird diese Befragung als nicht repräsentativ gewertet. Von den angeschriebenen 15 Landesverwaltungen sind 6 Antworten eingegangen. Zusätzlich sind die ISB der Landesverwaltungen die befragte Zielgruppe. Auch wenn die weiteren Teilnehmer eine Expertise auf diesem Wissensgebiet haben und berücksichtigt sind, gehören diese nicht zu der ursprünglichen Zielgruppe. Wird lediglich die Zielgruppe betrachtet, liegt eine Beteiligung von 20% vor.

Neben der fehlenden Repräsentanz durch die geringe Teilnahme, sind die Fragen, vermutlich aufgrund ihrer Offenheit, in unterschiedlicher Interpretation beantwortet worden.  Obwohl  bewusst  im  IT-Grundschutz  definierte  Terminologien  verwendet wurden, haben die Teilnehmer Begrifflichkeiten unterschiedlich gedeutet und entsprechend ihrer Interpretation geantwortet.

<!-- page: 62 -->

Daraus ergibt sich, dass sich ein begrenzter Umfang der Daten aus dieser Befragung für das IT-Grundschutz-Profil verwendet wird. Folgende Informationen aus der Befragung werden im Rahmen des IT-Grundschutz-Profils berücksichtigt:

- Die größten Hürden für die Umsetzung eines ISMS liegen für die Teilnehmer im Bereich der Ressourcenbereitstellung und ein geringer Stellenwert von Informationssicherheit für die Behördenleitung.
- Generisch betrachtet können die Geschäftsprozesse Gesetzgebungsverfahren, Rechtssetzungsverfahren, Daseinsvorsorge und die Aufrechterhaltung des Verwaltungsbetriebes in einer obersten Landesbehörde vorhanden sein.
- Die obersten Landesbehörden bzw. Landesverwaltungen nutzen zu einem gewissen Grad externe Dienstleister für ihre Infrastruktur.
- An Anwendungen könnten Verzeichnisdienste, zentrale Anmelde- und Identifizierungsdienste sowie zentral geführte Register vorhanden  sein. Diese Anwendungen  unterliegen  laut  der  befragten  Person  einem  besonders  hohem Schutzbedarf.
- Während den Landesverwaltungen unterschiedliche Produkte zur Aufgabenerfüllung zur Verfügung stehen, scheinen Produkte des Herstellers Microsoft bevorzugt zu werden.

## 3.3 Zusammenfassung der Erhebung

Die Ergebnisse der Literaturrecherche und der Befragung dienen als Grundlage für die Erstellung des IT-Grundschutz-Profils. Der Ausgangspunkt dessen sind die Aufgaben  und Geschäftsprozesse,  die  in  der  schematischen  Sicherheitskonzeption  abgesichert werden. Während in den Antworten zu dem Fragebogen keine einheitlichen Angaben zu den Aufgaben festzustellen sind, gehen aus der Literatur folgende Aufgaben hervor:

1. Das Erlassen von Verordnungen, Erlassen und die Mitarbeit an Gesetzen.
2. Die Ausführung von Bundes- und Landesgesetzen, sofern diese nicht an nachgeordnete Behörden delegiert ist.
3. Die Aufsicht und Kontrolle der nachgeordneten Behörden.
4. Die (politische) Unterstützung des Ministers durch Informationsbeschaffung und sonstige Tätigkeiten.
5. Die  Selbstverwaltung  der  Behörde  durch  strategische  Planung,  Pressearbeit und Personalsachen.

<!-- page: 63 -->

Die signifikanten Antworten aus der Befragung verhalten sich deckungsgleich zu den Punkten 1 und 5. Die Aufgaben werden durch die Landesverwaltungen unter der Zuhilfenahme von IT-Dienstleistern bewältigt. Aus der Literatur und der Befragung ergibt sich, dass der Grad der Auslagerung differiert.

Folgende Anforderungen und Probleme konnten für ein ISMS einer obersten Landesbehörde identifiziert werden, sodass diese in dem IT-Grundschutz-Profil berücksichtigt werden:

- Die größten Hürden für die Umsetzung eines ISMS lagen für die Teilnehmer im Bereich der Ressourcenbereitstellung und in dem geringen Stellenwert von Informationssicherheit für die Behördenleitung.
- An Anwendungen sind in einer Einzelnennung Verzeichnisdienste, zentrale Anmelde- und Identifizierungsdienste sowie zentral geführte Register vorhanden. Diese Anwendungen unterliegen laut der befragten Person einem besonders hohem Schutzbedarf.
- Während den Landesverwaltungen unterschiedliche Produkte zur Aufgabenerfüllung zur Verfügung stehen, werden bei den Befragten Produkte des Herstellers Microsoft bevorzugt.

<!-- page: 64 -->

## Kapitel 4 Konzeption des IT-Grundschutz-Profils

Auf der Basis der zuvor erhobenen Informationen wird nun das IT-Grundschutz-Profil für oberste Landesbehörden erstellt. Das erste Unterkapitel befasst sich dazu mit der Strukturbeschreibung des BSI zu den IT-Grundschutz-Profilen und legt das nachfolgende Vorgehen fest.

Das zweite Unterkapitel grenzt den Informationsverbund ab, stellt die Komponenten der Referenzarchitektur dar und unterzieht diese zugleich einer Schutzbedarfsfeststellung. Das dritte Unterkapitel widmet sich der Modellierung des Informationsverbundes mit den IT-Grundschutz-Bausteinen, während das vierte Unterkapitel das ITGrundschutz-Profil mit einer schematischen Risikoanalyse eines Zielobjekts abschließt.

## 4.1 Methodik zur Entwicklung eines IT-Grundschutz-Profils

Das Vorgehen zur Erstellung eines IT-Grundschutz-Profis ist durch das BSI in einer Strukturbeschreibung vorgegeben. Die Struktur eines IT-Grundschutz-Profils und deren Inhalte sind im zweiten Kapitel der Masterarbeit aufgeführt und wird nicht wiederholt. Das IT-Grundschutz-Profil ist demnach in der Sicherheitskonzeption des IT-Grundschutzes verortet und umfasst nicht das gesamte ISMS der Organisation [67, S. 36]. So muss jede Organisation beispielsweise selbst eine Informationssicherheitsleitlinie festlegen und nach deren Vorgaben handeln. Dies ist unter anderem eine Anforderung, die sich auch aus den IT-Grundschutz-Bausteinen ergibt [24, S. 127-128].

Obwohl in  der  Einleitung  zu  Strukturbeschreibung  der  IT-Grundschutz-Profile nach dem BSI erwähnt wird, dass das IT-Grundschutz-Profil eine Schutzbedarfsfeststellung und Risikoanalyse enthalten kann [16, S. 5], werden in den ausführlichen Erläuterungen keine weiteren Hinweise dazu gegeben. Ein eigenes Kapitel, in dem eine Schutzbedarfsfeststellung der Zielobjekte wie in dem Standard 200-2 durchgeführt wird [64, S. 104-132], ist nicht dargestellt. Ausführliche Erläuterungen zu einer Risikoanalyse sind ebenfalls nicht vorzufinden.

Da  die  obersten  Landesbehörden  in  der  ISLL-Bund,  neben  dem  Betrieb  eines ISMS, ausdrücklich zu der Erstellung und Umsetzung der Sicherheitskonzepte aufgefordert werden, wird das IT-Grundschutz-Profil um die Schutzbedarfsfeststellung und um eine schematische Risikoanalyse eines Zielobjekts mit hohem Schutzbedarf erweitert. Zum einen kann dies den obersten Landesbehörden eine zusätzliche Orientierung in der Erstellung der Sicherheitskonzeption, den festzustellenden Schutzbedarfen der Standard-Absicherung und der Risikoanalyse bieten. Zum anderen kann dieser umfangreichere Ansatz die Struktur der IT-Grundschutz-Profile durch ein evaluiertes Anwendungsbeispiel erweitern.

<!-- page: 65 -->

## 4.2 Feststellung des Informationsverbunds

Da die geforderte Management Summary eine Zusammenfassung des IT-Grundschutz-Profils ist und, hiesiger Einschätzung nach, keiner weiteren Erläuterung innerhalb der Masterarbeit bedarf, wird auf diese nicht weiter eingegangen. Für das Gesamtdokument des IT-Grundschutz-Profils (s. Anhang B) werden die zuvor und nachfolgend dargelegten Inhalte letztlich in eine zusammenhängende Textform überführt.

Folgend wird der Geltungsbereich definiert [14, S. 10]. Mit diesem wird abgegrenzt, welche Geschäftsprozesse und Organisationsanteile in der schematischen Sicherheitskonzeption betrachtet werden. Durch diese Abgrenzung wird der Betrachtungsbereich des Informationsverbunds festgelegt, dessen Referenzarchitektur abgesichert wird.

Obwohl ein vollständiges ISMS in der Basis- und Standard-Absicherung häufig die gesamte Organisation betrachtet [64, S. 30-31] und die obersten Landesbehörden gemäß der Befragung ebenfalls die gesamte Organisation betrachten, wird in diesem ITGrundschutz-Profil  nur  ein  Teilbereich  einer  obersten  Landesbehörde  abgesichert. Zum einen ist dadurch das IT-Grundschutz-Profil unabhängig der Behördenstruktur anwendbar, zum anderen wird mit der Beschränkung des Betrachtungsgegenstandes eine angemessene und granulare Absicherung sichergestellt.

Für die Festlegung des Geltungsbereiches wird die Aufgabenzusammenfassung des Kapitels 3.3 herangezogen. Ausgehend davon werden die Aufgaben des Erarbeitens von Verordnungen, Erlassen und die Mitarbeit an Gesetzen als Ausgangspunkt verwendet,  um  den  Anwendungsbereich  des  IT-Grundschutz-Profils  einzugrenzen.  Diese 'konzeptionellen' Aufgaben [69, S. 15] sind in der Fachliteratur, den Gemeinsamen Geschäftsordnungen und als eine Antwort der Befragung genannt.

Aufgrund dieser übergreifenden Übereinstimmung wird davon ausgegangen, dass diese drei Aufgaben durch alle obersten Landesbehörden wahrgenommen werden. Um einen  zentralen,  übergeordneten  Geschäftsprozess  im  IT-Grundschutz-Profil  zu  betrachten, werden diese drei Einzelaufgaben als die Beteiligung an der Normsetzung des Landes zusammengefasst. Der Geltungsbereich umfasst diesen Geschäftsprozess und die damit zusammenhängende Referenzarchitektur wird abgesichert.

Der  Strukturbeschreibung  folgend,  wird  nun  die  Referenzarchitektur  sowie  die Schutzbedarfe beschrieben. Die Schutzbedarfsfeststellung beispielhaft dargestellt und an jedem Zielobjekts angeführt. In dem Gesamtdokument des IT-Grundschutz-Profils wird ein eigenes Kapitel für die Schutzbedarfsfeststellung gebildet.

## 4.2.1 Schutzbedarfskategorien

Neben der Aufzählung der Zielobjekte wird unmittelbar eine Schutzbedarfsfeststellung durchgeführt. Diese basiert auf einer Gefahrenabschätzung ausgehend von den verarbeiteten Informationen. Bevor eine Schutzbedarfsfeststellung durchgeführt wird, müssen zunächst die Kategorien der Schutzbedarfe festgelegt werden [64, S. 104].

Auf eine Anfrage haben die Landesverwaltungen keine Sicherheitskonzeptionen einer obersten Landesbehörde auf der Ebene der Standard-Absicherung für eine Orientierung an den Schutzbedarfskategorien bereitgestellt. Aufgrund der fehlenden Datengrundlage, wird in der vorliegenden Arbeit der Vorschlag des BSI für dieses IT-Grundschutz-Profil verwendet. Die Schutzbedarfskategorien sind im Standard 200-2 wie folgt eingeteilt [64, S. 106-107]:

<!-- page: 66 -->

## Normaler Schutzbedarf

Tabelle 4.1: Schutzbedarfskategorie Normal

|   1. | Verstoß gegen Gesetze/ Vorschriften/Verträge                      | • Verstöße gegen Vorschriften und Gesetze mit ge- ringfügigen Konsequenzen. • Geringfügige Vertragsverletzungen mit maximal geringen Konventionalstrafen.                                              |
|------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   2. | Beeinträchtigung des in- formationellen Selbstbe- stimmungsrechts | • Es handelt sich um personenbezogene Daten, durch deren Verarbeitung der Betroffene in seiner gesellschaftlichen Stellung oder in seinen wirt- schaftlichen Verhältnissen beeinträchtigt werden kann. |
|   3. | Beeinträchtigung der persönlichen Unver- sehrtheit                | • Eine Beeinträchtigung erscheint nicht möglich.                                                                                                                                                       |
|   4. | Beeinträchtigung der Aufgabenerfüllung                            | • Die Beeinträchtigung würde von den Betroffenen als tolerabel eingeschätzt werden. • Die maximal tolerierbare Ausfallzeit liegt zwi- schen 24 und 72 Stunden.                                         |
|   5. | Negative Innen- oder Außenwirkung                                 | • Eine geringe bzw. nur interne Ansehens- oder Vertrauensbeeinträchtigung sind zu erwarten.                                                                                                            |
|   6. | Finanzielle Auswirkun- gen                                        | • Der finanzielle Schaden bleibt für die Institution tolerabel.                                                                                                                                        |

## Hoher Schutzbedarf

|   1. | Verstoß gegen Gesetze/ Vorschriften/Verträge                      | • Verstöße gegen Vorschriften und Gesetze mit er- heblichen Konsequenzen. • Vertragsverletzungen mit hohen Konventional- strafen.                                                                                  |
|------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   2. | Beeinträchtigung des in- formationellen Selbstbe- stimmungsrechts | • Es handelt sich um personenbezogene Daten, bei deren Verarbeitung der Betroffene in seiner ge- sellschaftlichen Stellung oder in seinen wirtschaft- lichen Verhältnissen erheblich beeinträchtigt wer- den kann. |
|   3. | Beeinträchtigung der persönlichen Unver- sehrtheit                | • Eine Beeinträchtigung der persönlichen Unver- sehrtheit kann nicht absolut ausgeschlossen wer- den.                                                                                                              |
|   4. | Beeinträchtigung der Aufgabenerfüllung                            | • Die Beeinträchtigung würde von einzelnen Be- troffenen als nicht tolerabel eingeschätzt. • Die maximal tolerierbare Ausfallzeitliegt zwischen drei und 24 Stunden.                                               |

<!-- page: 67 -->

Tabelle 4.2: Schutzbedarfskategorie Hoch

|   5. | Negative Innen- oder Außenwirkung   | • Eine breite Ansehens- oder Vertrauensbeeinträch- tigung ist zu erwarten.                    |
|------|-------------------------------------|-----------------------------------------------------------------------------------------------|
|   6. | Finanzielle Auswirkun- gen          | • Der Schaden bewirkt beachtliche finanzielle Ver- luste, ist jedoch nicht existenzbedrohend. |

## Sehr hoher Schutzbedarf

Tabelle 4.3: Schutzbedarfskategorie Sehr Hoch

|   1. | Verstoß gegen Gesetze/ Vorschriften/Verträge                      | • Fundamentaler Verstoß gegen Vorschriften und Gesetze. • Vertragsverletzungen, deren Haftungsschäden rui- nös sind.                                             |
|------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   2. | Beeinträchtigung des in- formationellen Selbstbe- stimmungsrechts | • Es handelt sich um personenbezogene Daten, bei deren Verarbeitung eine Gefahr für Leib und Le- ben oder die persönliche Freiheit des Betroffenen gegeben ist.  |
|   3. | Beeinträchtigung der persönlichen Unver- sehrtheit                | • Gravierende Beeinträchtigungen der persönlichen Unversehrtheit sind möglich. • Gefahr für Leib und Leben.                                                      |
|   4. | Beeinträchtigung der Aufgabenerfüllung                            | • Die Beeinträchtigung würde von allen Betroffenen als nicht tolerabel eingeschätzt werden. • Die maximal tolerierbare Ausfallzeit ist kleiner als drei Stunden. |
|   5. | Negative Innen- oder Außenwirkung                                 | • Eine landesweite bis bundesweite Ansehens- oder Vertrauensbeeinträchtigung, eventuell sogar exis- tenzgefährdender Art, ist denkbar.                           |
|   6. | Finanzielle Auswirkun- gen                                        | • Der finanzielle Schaden ist für die Institution exis- tenzbedrohend.                                                                                           |
|   7. | Sonstige Auswirkungen                                             | • Der Bestand des Staates oder wesentliche Teile dessen könnten gefährdet werden.                                                                                |

## 4.2.2 Referenzarchitektur

Nach der Festlegung der Schutzbedarfskategorien wird nun die Referenzarchitektur in Form der Zielobjekte dargestellt, die für den Geschäftsprozess der Beteiligung an der Normsetzung benötigt werden.

Orientiert an der Einteilung der IT-Grundschutz-Bausteine werden die Zielobjekte in die Kategorien Anwendungen, IT-Systeme, Netze und Kommunikation sowie räumliche Infrastruktur unterteilt. Für eine klare Identifikation wird jedes festgestellte Zielobjekt mit einer Identifikationsnummer versehen. Die Zielobjekte werden, wie in der Strukturbeschreibung gefordert [16, S. 12], gruppiert zusammengefasst. Zwischen unterschiedlichen Verwendungsarten wird nicht unterschieden.

Neben einer Definition des Zielobjekts, die abgewandelt in das IT-GrundschutzProfil übernommen wird, wird für jedes Zielobjekt die Schutzbedarfsfeststellung in einer tabellarischen Form durchgeführt. Die Schutzbedarfsfeststellung ergibt sich unter anderem aus dem Schutzbedarf des Geschäftsprozess und dessen Informationen [64, S. 110]. Zusätzlich werden weitere Effekte und Prinzipien beachtet [64, S. 108-109]:

<!-- page: 68 -->

- Das Vererbungsprinzip , welches dafür sorgt, dass sich der Schutzbedarf des Geschäftsprozesses und dessen Informationen auf die Zielobjekte überträgt, die mit diesen in Kontakt kommen.
- Das Maximumprinzip wird angewendet, wenn ein Zielobjekt mit mehreren anderen Objekten interagiert. Es gilt in diesem Fall der jeweils höchste vorzufindende Schutzbedarf.
- Der Kumulationseffekt ,  findet  ebenfalls  bei  der  Nutzung eines Zielobjekts durch andere Infrastrukturanteile statt. So kann es zu einem höheren Schutzbedarf kommen, weil mehrere kompensierbare Schäden durch die gemeinsame Plattform zu einem großen Schaden führen würden.
- Das Abhängigkeitsprinzip ,  tritt  auf,  wenn  ein  besonders  schützenswertes Zielobjekt von weniger schutzbedürftigen Objekten abhängt. Durch diese Abhängigkeit erhöht sich der Schutzbedarf der z.B. ursprünglich normal eingestuften Objekte.
- Der Verteilungseffekt kann dagegen für den Schutzbedarf des Objekts entlastend wirken. So wirken hohe Schutzbedarfe eines Zielobjekts nicht auf andere beteiligte Objekte, wenn diese nur unwesentliche Teilbereiche verwenden.

## 4.2.2.1 Betrachteter Geschäftsprozess

Die Beteiligung an der Normsetzung des Landes als Geschäftsprozess ist per Definition des BSI in Aufgaben und Arbeitsabläufe zu unterteilen (vgl. Kapitel 1.3.2.4). Der Prozess der Beteiligung an der Normsetzung ist ursprünglich aus drei Aufgaben der obersten Landesbehörden (vgl. Kapitel 3.3) abgeleitet:

1. Die Mitarbeit an Gesetzen.
2. Das Erlassen von Verordnungen.
3. Das Festsetzen von Erlassen.

Dazu wird von folgenden Arbeitsabläufen für die Erfüllung dieser Aufgaben ausgegangen:

- Die Kommunikation mit anderen Behörden, wie Kommunen und obersten Landesbehörden zur Abstimmung der Inhalte.
- Wahrnehmung interner Kommunikationswege für die Steuerung der Aufgabe und deren Bearbeitung im eigenen Bereich.
- Die  fachliche  Mitarbeit  an  den  verschiedenen  Normtypen,  unter  anderem durch die Erstellung von Gutachten, Stellungnahmen und Ausarbeitungen von Vorschlägen und Konzepten.

<!-- page: 69 -->

Diese Aufzählung der Aufgaben und Arbeitsabläufe dient als Basis der benötigten Zielobjekte. Nichtsdestotrotz wird kein Anspruch an eine vollständige Aufzählung erhoben. Der erste Teil der Referenzarchitektur, der Geschäftsprozess, stellt sich somit wie folgt dar:

Tabelle 4.4: Zielobjekt PRO01

| PRO01 Beteiligung an der Normsetzung des Landes   | PRO01 Beteiligung an der Normsetzung des Landes   | PRO01 Beteiligung an der Normsetzung des Landes                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                                        | Schutzbe- darf                                    | Begründung                                                                                                                                                                                                                                                                                                                                                                                            |
| Vertraulich- keit                                 | Normal                                            | Die verschiedenen Normsetzungsprozesse der obersten Landesbehörden (Beteiligung an Gesetzge- bung, Verordnungen und Erlasse) weisen keine her- ausragenden Anforderungen an die Vertraulichkeit auf. In den vergangenen Jahren haben sich stattdes- sen weitere Transparenztendenzen durchgesetzt [87, S. 165-166]. Bei einer unberechtigten Kenntnis- nahme kommt es zu überschaubaren Konsequenzen. |
| Integrität                                        | Normal                                            | Der Geschäftsprozess behandelt Informationen, de- ren unberechtigte Veränderung tolerierbare Beein- trächtigungen nach sich zieht.                                                                                                                                                                                                                                                                    |
| Verfügbar- keit                                   | Normal                                            | Der Geschäftsprozess behandelt Informationen, bei denen eine Einschränkung der Verfügbarkeit im to- lerierbaren Bereich liegt.                                                                                                                                                                                                                                                                        |

## 4.2.2.2 Anwendungen

Da sich nach der IT-Grundschutz-Methodik die Anwendungen aus dem betrachteten Geschäftsprozess ergeben und von diesen weitere Infrastrukturanteile ausgehen [64, S. 81-82], werden die Anwendungen zunächst dargestellt.

Um den Geschäftsprozess  umzusetzen,  wird  gemäß  den  wenigen  anwendbaren Antworten aus der Befragung hauptsächlich eine allgemein zur Verfügung stehende IT verwendet. Fachanwendungen sind, außer E-Akten-Systemen und ressortspezifischen Anwendungen, nicht bekannt geworden. Ein Teilnehmer hat dies als die Nutzung von 'Büro - IT' in einem typischen Geschäftsprozess bezeichnet (s. Anhang A2).

D er Begriff der 'Büro - IT' ist undefiniert und in keinem vorliegenden Lexikon verzeichnet. Die Autoren Fischer und Hofer verwenden den hier als gleichwertig eingeschätzten Begriff der 'Bürokommunikation' in einem Lexikon der Informatik. Dieser Begriff wird bei Fischer und Hofer mit folgenden IT-Produkten verbunden:

- Microsoft Exchange für die Erledigung der Bürokommunikation in Form von Telefax, Stimme, E-Mail, Terminen, Kontakten und Aufgaben [88, S. 566]
- mySAP.com, als erweiterte Funktion von SAP R3 [88, S. 597]
- Microsoft  Office  mit  den  Produkten  Outlook,  PowerPoint,  MS  Publisher, SharePoint, InfoPath, Visio und OneNote [88, S. 629]

<!-- page: 70 -->

- Open Office als Suite für Büro-Kommunikation [88, S. 635]
- Tabellenkalkulation [88, S. 888]
- Textverarbeitung [88, S. 901]

Dementsprechend werden diese Produkte bei der Bestimmung der Zielobjekte berücksichtig. Neben Produkten der Bürokommunikation könnten für die Wahrnehmung der Normsetzung ebenfalls Vorgangsbearbeitungssysteme (VBS) verwendet werden. Derzeit sind keine Behörden bekannt, die ein solches für diesen Geschäftsprozess einsetzen, weshalb nicht von der Nutzung eines Vorgangsbearbeitungssystems im Rahmen der Aufgabenerfüllung ausgegangen wird. Selbiges gilt für E-Akten- und Dokumentenmanagementsysteme.

Die Referenzarchitektur orientiert sich an diesen Grundanwendungen der Bürokommunikation und stellt die dafür benötigte Grundarchitektur bereit. Die Granularität der  Objektbeschreibungen  orientiert  sich  an  den  vorhandenen  Bausteinen  des  ITGrundschutz-Kompendiums. Eine technische Detailtiefe ist für diese Managementperspektive nicht vorgesehen und erscheint nicht zielführend.

Grundlage der Anwendungen auf Computersystemen ist zunächst das Betriebssystem:

'[Betriebssystem ist ein] Sammelbegriff für Programme, die den Betrieb eines Computers  erst  möglich machen […]. Sie steuern und überwachen das Zusammenspiel der Hardwarekomponenten im Rahmen der Auftrags-, Daten-, Arbeitsspeicher- und Programmverwaltung (bes. die Abwicklung einzelner Anwendungsprogramme, den Zugriff von Prozessen auf bestimmte Ressourcen) sowie der Systemsicherung (Fehlererkennung und -behebung). Das Betriebssystem macht ein Datenverarbeitungssystem erst bedienbar und beherrschbar.' [89, S. 14]

Aufgrund der hohen Verbreitung des Windows-Betriebssystems bei Desktop-PCs [90] und der Ergebnisse des Fragebogens wird von dem Windows 10 Betriebssystem für die Benutzer-Clients ausgegangen. Windows 10 ist die aktuelle Betriebssystemversion des Herstellers Microsoft und seit 2015 erhältlich [91], weshalb von dieser Version ausgegangen wird.

| APP01 Betriebssystem Windows 10   | APP01 Betriebssystem Windows 10   | APP01 Betriebssystem Windows 10                                                                                                                                                    |
|-----------------------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                        | Schutzbe- darf                    | Begründung                                                                                                                                                                         |
| Vertraulich- keit                 | Normal                            | Es wird über das Betriebssystem nur auf einen Ge- schäftsprozess mit einem normalen Schutzbedarf eingewirkt. Die unberechtigte Kenntnisnahme von Daten hat begrenzte Auswirkungen. |
| Integrität                        | Normal                            | Auf dem Betriebssystem findet eine Vererbung des normalen Schutzbedarfes des Geschäftsprozesses statt.                                                                             |

<!-- page: 71 -->

Tabelle 4.5: Zielobjekt APP01

| Verfügbar- keit   | Normal   | Über eine Internetverbindung oder entsprechend vorbereite Kopien kann die Software jederzeit neu zur Verfügung gestellt werden. Die Ausfallzeit ist im normalen Schutzbereich.   |
|-------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Für die Bearbeitung von Verfahren der Normsetzung müssen den Nutzern Anwendungen bereitgestellt werden, die es ermöglicht Texte zu verarbeiten und Tabellen sowie Präsentationen zu erstellen. Diese Anwendungen der Bürokommunikation werden von verschiedenen Herstellern angeboten.

Aufgrund der bereits festgestellten Tendenz zu dem Hersteller Microsoft wird das Software-Produkt Microsoft Office [88, S. 629], welches in mehreren Versionen erhältlich ist, als Zielobjekt für die Anwendungen der Bürokommunikation ausgewählt. Da Behörden zum Teil längere Umstellungszeiten in IT-Produkten in Kauf nehmen [92, S. 127-128], wird Microsoft Office 2016 als Teil des Informationsverbunds angenommen, auch wenn Microsoft Office 2019 bereits erhältlich ist.

Tabelle 4.6: Zielobjekt APP02

| APP02 Microsoft Office 2016   | APP02 Microsoft Office 2016   | APP02 Microsoft Office 2016                                                                                                                                                                                                            |
|-------------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                    | Schutzbe- darf                | Begründung                                                                                                                                                                                                                             |
| Vertraulich- keit             | Normal                        | Die Office-Anwendungen speichern lediglich tem- porär Daten zwischen und sind selbst nicht vertrau- lich zu behandeln. Es wird nur auf Informationen mit normalem Schutzbedarf zugegriffen.                                            |
| Integrität                    | Normal                        | Aufgrund der temporären Datenspeicherung bedarf Microsoft Office selbst keiner Absicherung der In- tegrität über den normalen Schutzbedarf hinaus.                                                                                     |
| Verfügbar- keit               | Normal                        | Über eine Internetverbindung oder entsprechend vorbereite Kopien kann die Software jederzeit neu zur Verfügung gestellt werden. Längere Ausfallzeiten sind dadurch unwahrscheinlich und hätten nur Aus- wirkungen im normalen Bereich. |

In der Verbindung mit der Bürokommunikation steht einer obersten Landesbehörde ebenfalls ein Dateiserver zur Verfügung.

'Ein Dateiserver ist […] ein Programmsystem, das alle Teilnehmenden mit Dateien versorgt.' [88, S. 806]

Dieser ermöglicht die zentrale und abgesicherte Speicherung von Daten auf einem Netzlaufwerk. Ein konkretes Produkt für einen Dateiserver ist nicht benannt worden.

<!-- page: 72 -->

Tabelle 4.7: Zielobjekt APP03

| APP03 Dateiserver   | APP03 Dateiserver   | APP03 Dateiserver                                                                                                                                                                                                                                                                                                                                                         |
|---------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel          | Schutzbe- darf      | Begründung                                                                                                                                                                                                                                                                                                                                                                |
| Vertraulich- keit   | Normal              | Auf dem Dateiserver werden Dokumente dauerhaft gespeichert und von berechtigten Personen abgeru- fen. Die dort abgelegten Dokumente enthalten In- formationen, deren unbefugte Kenntnisnahme die Institution und dritte Personen im tolerierbaren Maße schädigen können.                                                                                                  |
| Integrität          | Normal              | Die über den Dateiserver verwalteten Daten werden nur durch berechtigte Personen bearbeitet. Die mög- lichen Auswirkungen unberechtigter oder falscher Änderungen sind im normalen Schutzbereich.                                                                                                                                                                         |
| Verfügbar- keit     | Hoch                | Ohne die Dateiverwaltung und Kollaborationsmög- lichkeiten ist die Arbeitsfähigkeit der Behörde deut- lich eingeschränkt, eine längere Ausfallzeit als einen Tag ist nicht akzeptabel. Eine Ausfallzeit von unter einer Stunde ist dabei nicht einzuhalten, existenz- bedrohend ist ein Ausfall des Dateiservers ebenfalls nicht. Daher liegt ein hoher Schutzbedarf vor. |

Um gegebenenfalls  auf  die  öffentliche  Berichterstattung,  aber  auch  auf  behördliche Dienste auf der Basis von Webplattformen, zuzugreifen, wird ein Web-Browser benötigt.

'Der Browser ist ein Programm zur gr afischen Darstellung der Inhalte des World Wide Web (WWW), welches neben HTTP noch andere Dienste wie FTP unterstützt.' [89, S. 18]

Es wird der Web-Browser Firefox als nicht-kommerzielle Anwendung einer gemeinnützigen Organisation ausgewählt.

| APP04 Web-Browser Firefox   | APP04 Web-Browser Firefox   | APP04 Web-Browser Firefox                                                                                                                                         |
|-----------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                  | Schutzbe- darf              | Begründung                                                                                                                                                        |
| Vertraulich- keit           | Normal                      | Ein Web-Browser enthält selbst keine über den nor- malen Schutzbedarf hinausgehenden Informationen. Besonders schützenswerte Webanwendungen sind nicht vorhanden. |
| Integrität                  | Normal                      | Der Web-Browser speichert lediglich temporär Da- ten zwischen und Bedarf selbst keinem Schutz der Integrität über das normale Maß hinaus.                         |
| Verfügbar- keit             | Normal                      | Über eine Internetverbindung oder entsprechend vorbereite Kopien kann die Software jederzeit neu zur Verfügung gestellt werden. Ausfallzeiten sind                |

<!-- page: 73 -->

dadurch reduziert und im Eintrittsfalle von normalem Schutzbedarf.

Tabelle 4.8: Zielobjekt APP04

Eine zentrale Anwendung in der Benutzerverwaltung ist ein sogenannter Verzeichnisdienst. In der Befragung wurde dies unter anderem als besonders schützenswerte Komponente genannt.

'Ein Verzeichnisdienst stellt in einem Datennetz Informationen über beliebige Objekte in einer definierten Art zur Verfügung. Mit einem Objekt können zugehörige Attribute gespeichert werden, zum Beispiel zu einer Benutzerkennung Namen und Vornamen des Benutzers, die Personalnummer und der Rechnername. Diese Daten können dann gleichermaßen von verschiedenen Applikationen verwendet werden. Der Verzeichnisdienst und seine Daten werden i n der Regel von zentraler Stelle aus verwaltet.' [24, S. 387]

Dazu bietet Microsoft den Verzeichnisdienst Active Directory an, der hier verwendet wird.

Tabelle 4.9: Zielobjekt APP05

| APP05 Verzeichnisdienst Active Directory   | APP05 Verzeichnisdienst Active Directory   | APP05 Verzeichnisdienst Active Directory                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                                 | Schutzbe- darf                             | Begründung                                                                                                                                                                                                                                                                                                                                |
| Vertraulich- keit                          | Hoch                                       | Der Verzeichnisdienst speichert Daten und Berech- tigungen, die unter anderem für einen ordnungsge- mäßen Betrieb der IT und der Rechteverwaltung ver- antwortlich sind. Eine Verletzung der Vertraulichkeit kann Betriebsausfälle und einen wesentlichen Nach- teil für die Institution bedeuten, sodass ein hoher Schutzbedarf besteht. |
| Integrität                                 | Hoch                                       | Der Verzeichnisdienst ist verantwortlich für die si- chere Authentifizierung und Bereitstellung von Res- sourcen innerhalb der Behörde. Eine unberechtigte Veränderung kann unter anderem die Gesamtverfüg- barkeit des Informationsverbundes bedeutend ein- schränken, weshalb ein hoher Schutzbedarf besteht.                           |
| Verfügbar- keit                            | Hoch                                       | Sollte der Verzeichnisdienst nicht verfügbar sein, ist die gesamte Aufgabenwahrnehmung der Behörde gefährdet. Zugriffe auf Systeme, Dateien und andere Ressourcen sind nicht möglich. Dementsprechend ist eine Ausfallzeit von mehr als 24 Stunden nicht ak- zeptabel.                                                                    |

Neben der Kommunikation auf dem Postweg, Telefon und Telefax wird in der Referenzarchitektur die die E-Mail-Kommunikation verwendet. Diese definiert sich als:

<!-- page: 74 -->

'Eine E -Mail-Anwendung besteht aus einem Mailing Server, der die Nachrichten archiviert und den Versand steuert sowie einem client-seitigen Mailing-Programm zur Erstellung und zum Transfer von elektronischen Nachrichten.' [89, S. 62]

Zu  dem  Betrieb  eines  Mail-Servers  steht  dazu  die  Anwendung Microsoft Exchange zur  Verfügung, über  die unter anderem E-Mails, Kontakte und Termine bereitgestellt und verwaltet werden können. Als Mailing-Programm steht in Microsoft Office 2016 eine entsprechende Anwendung (Outlook) zu Verfügung.

Tabelle 4.10: Zielobjekt APP06

| APP06 Microsoft Exchange   | APP06 Microsoft Exchange   | APP06 Microsoft Exchange                                                                                                                                                                                           |
|----------------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                 | Schutzbe- darf             | Begründung                                                                                                                                                                                                         |
| Vertraulich- keit          | Normal                     | Microsoft Exchange ergänzt die Office Produkte als Kommunikations- und Planungsressource. Da In- formationen mit normalem Schutzbedarf verarbeitet werden, vererbt sich dieser Schutzbedarf auf dieses Zielobjekt. |
| Integrität                 | Normal                     | Da Informationen mit normalen Schutzbedarf verar- beitet werden, vererbt sich der normale Schutzbedarf des Geschäftsprozesses auf dieses Zielobjekt.                                                               |
| Verfügbar- keit            | Normal                     | Ein temporärer Ausfall von Microsoft-Exchange ist tolerierbar, dieser betrifft Informationen mit norma- lem Schutzbedarf. Andere Kommunikationsmittel stehen bei einem Ausfall gegebenenfalls zur Verfü- gung.     |

Zuletzt wird für eine authentische Übermittlung von Nachrichten und sichere Identifizierung von Sendern und Empfängern eine Public-Key Infrastruktur (PKI)  in  der Behörde verwendet. Eine PKI definiert sich als:

'Pauschale Bezeichnung für Mechanismen zur Aut hentisierung sich nicht vertrauter Subjekte  und  Objekte  sowie  für  ganze  Infrastrukturen  rund  um  die  asymmetrische Kryptografierung; zur Infrastruktur gehören die Algorithmen, die öffentlichen und privaten Schlüssel sowie ein authentisierter Schlüsseltausch mit Zertifikat und einer Zertifizierungsstelle, CA […].' [88, S. 713]

Über Signaturverfahren kann auf diesem Weg eine vertrauliche und authentisierte Kommunikation hergestellt werden.

| APP07: Public-Key Infrastruktur   | APP07: Public-Key Infrastruktur   | APP07: Public-Key Infrastruktur                                                               |
|-----------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------|
| Schutzziel                        | Schutzbe- darf                    | Begründung                                                                                    |
| Vertraulich- keit                 | Hoch                              | Unberechtigte Kenntnisnahmen von spezifischen Informationen der Public-Key Infrastruktur (wie |

<!-- page: 75 -->

Tabelle 4.11: Zielobjekt APP07

|                 |      | bspw. private Schlüssel) führen zu einer Störung der sicheren Kommunikation der Behörde. Daher liegt ein hoher Schutzbedarf vor.                                                                                                                                          |
|-----------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integrität      | Hoch | Nachrichten können unberechtigt von dritten Perso- nen als behördlich autorisiert dargestellt werden, sollte es zu einem Integritätsverlust kommen. Ferner können Datenfehler in der PKI zu unlesbaren Nach- richten führen. Daraus ergibt sich ein hoher Schutz- bedarf. |
| Verfügbar- keit | Hoch | Die Public-Key Infrastruktur dient zur verbindlichen Kommunikation und muss dazu nahezu störungsfrei zur Verfügung stehen. Es kann eine Ausfallzeit von bis zu einem Tag toleriert werden, woraus sich ein hoher Schutzbedarf ergibt.                                     |

## 4.2.2.3 IT-Systeme

Im Hintergrund der Anwendungen werden verschiedene Dienste und Hardwaregeräte betrieben, die eine angemessene Ausführung der Anwendungen ermöglichen oder zusätzliche Dienste bereitstellen.

Ein grundlegender Teil dieser Dienste sind Servermaschinen, die umgangssprachlich als Server bezeichnet werden. Bei einem Server handelt es sich um dezidierte, gesicherte und gehärtete Servermaschinen, die zentralisiert Dienstleistungsprogramme für die Nutzer bereitstellen [88, S. 806-807].

Neben der benötigten Hardware nutzt diese Server ebenfalls ein Betriebssystem, in diesem Fall Windows Server 2016 . Hier besteht ebenfalls bereits das Betriebssystem Windows Server 2019, welches aus den oben bereits aufgeführten Gründen nicht ausgewählt wird.

Tabelle 4.12: Zielobjekt SYS01

| SYS01 Windows-Server 2016   | SYS01 Windows-Server 2016   | SYS01 Windows-Server 2016                                                                                                                                                                                       |
|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                  | Schutzbe- darf              | Begründung                                                                                                                                                                                                      |
| Vertraulich- keit           | Hoch                        | Der Server bildet die Grundlage für dezidierte Ser- veranwendungen wie den Verzeichnisdienst, Micro- soft Exchange und den Dateiserver. Es vererbt sich ein hoher Schutzbedarf.                                 |
| Integrität                  | Hoch                        | Es besteht hoher Schutzbedarf durch den Verer- bungseffekt, der unter anderem durch den zum Dienstbetrieb benötigten Verzeichnisdienst eintritt. Zudem werden weitere Dienste über den Server be- reitgestellt. |
| Verfügbar- keit             | Hoch                        | Durch die Vererbung von dem Dateiserver und dem Verzeichnisdienst liegt ein hoher Schutzbedarf der Verfügbarkeit vor.                                                                                           |

<!-- page: 76 -->

Die Aufgabenwahrnehmung durch die Mitarbeiter der Behörde finden nicht auf dem Server selbst,  sondern  auf  einem Arbeitsplatz-PC statt,  der  als  Client  in  das  lokale Netzwerk eingebunden ist.

'[ Ein PC ist ein] Universalrechner auf Basis eines Mikroprozessors, der überwiegend auf die Nutzung durch genau eine Person zugeschnitten ist, die diesen für berufliche oder private Zwecke einsetzt […]. Der PC umfasst alle  notwendigen Komponenten eines  unabhängigen  Rechners  wie  Prozessor,  Speicher,  Peripheriespeicher,  Sichtgerät, Tastatur und Drucker sowie Anschlussmöglichkeiten an Rechnernetze'. [93, S. 525]

Der Arbeitsplatz-PC ist ein stationäres Gerät, welches nicht für den mobilen Betrieb ausgelegt ist.

Tabelle 4.13: Zielobjekt SYS02

| SYS02 Arbeitsplatz-PC   | SYS02 Arbeitsplatz-PC   | SYS02 Arbeitsplatz-PC                                                                                                                                                                                         |
|-------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel              | Schutzbe- darf          | Begründung                                                                                                                                                                                                    |
| Vertraulich- keit       | Normal                  | Von dem Arbeitsplatz-PC wird als Client über das Betriebssystem auf Daten zugegriffen, die einer nor- malen Vertraulichkeit unterliegen. Daher liegt ein normaler Schutzbedarf vor.                           |
| Integrität              | Normal                  | Über den Zugriff des Arbeitsplatz-PCs sind Verän- derungen der normal schutzbedürftigen Daten mög- lich. Da eine Verfälschung dieser Daten tolerierbar ist, besteht ein normaler Schutzbedarf der Integrität. |
| Verfügbar- keit         | Normal                  | Die benötigte Hardware kann als Ersatzteil eingela- gert und bei Bedarf zur Verfügung gestellt werden. Es liegt ein normaler Schutzbedarf vor.                                                                |

Neben den stationären Computern stehen in einer obersten Landesbehörde ebenfalls Mobile-PCs zur Verfügung. Diese ermöglichen mobiles Arbeiten und können gegebenenfalls für einen Einsatz in der Heimarbeit konfiguriert werden. Ein Mobiler-PC ist ein Arbeitsplatz-PC, optimiert als mobile Datenverarbeitungseinheit. Dieses Zielobjekt wird daher nicht zusätzlich definiert.

| SYS03 Mobiler-PC   | SYS03 Mobiler-PC   | SYS03 Mobiler-PC                                                                                                                                                                     |
|--------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel         | Schutzbe- darf     | Begründung                                                                                                                                                                           |
| Vertraulich- keit  | Normal             | Von dem Mobilen-PCs wird als Client über das Be- triebssystem auf Daten zugegriffen, die einer norma- len Vertraulichkeit unterliegen. Daher vererbt sich ein normaler Schutzbedarf. |
| Integrität         | Normal             | Der Mobile-PC hält nur Daten vor, die dem norma- len Schutzbedarf unterliegen.                                                                                                       |

<!-- page: 77 -->

Tabelle 4.14: Zielobjekt SYS03

| Verfügbar- keit   | Normal   | Der Mobile-PC fungiert als Client, die benötigte Hardware kann daher als Ersatzteil eingelagert und bei Bedarf zur Verfügung gestellt werden. Es liegt ein normaler Schutzbedarf vor.   |
|-------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Um die Telefon- und Telefaxdienste zur Kommunikation zu verwenden, werden entsprechende Hardwaregeräte benötigt. Bei einem Telefon handelt es sich um das Gerät zur Nutzung eines Fernsprechdienstes und bei dem Telefaxgerät um ein Endgerät zum Versand und Empfang von Telefaxen.

Tabelle 4.15: Zielobjekt SYS04

| SYS04 Telefon     | SYS04 Telefon   | SYS04 Telefon                                                                                                                                        |
|-------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel        | Schutzbe- darf  | Begründung                                                                                                                                           |
| Vertraulich- keit | Normal          | Da Informationen mit normalen Schutzbedarf verar- beitet werden, vererbt sich dieser Schutzbedarf des Geschäftsprozesses auch auf dieses Zielobjekt. |
| Integrität        | Normal          | Das Telefon benötigt keiner weiteren Absicherung und hält keine Daten über den normalen Schutzbe- reich hinaus vor.                                  |
| Verfügbar- keit   | Normal          | Das Telefon kann als Ersatzteil bereitgestellt und bei Bedarf zeitnah ersetzt werden. Der Schutzbedarf geht nicht über die Stufe ' normal ' hinaus.  |

Tabelle 4.16: Zielobjekt SYS05

| SYS05 Telefaxgerät   | SYS05 Telefaxgerät   | SYS05 Telefaxgerät                                                                                                                                   |
|----------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel           | Schutzbe- darf       | Begründung                                                                                                                                           |
| Vertraulich- keit    | Normal               | Da Informationen mit normalen Schutzbedarf verar- beitet werden, vererbt sich dieser Schutzbedarf des Geschäftsprozesses auch auf dieses Zielobjekt. |
| Integrität           | Normal               | Das Telefaxgerät benötigt keiner weiteren Absiche- rung und hält keine Daten über den normalen Schutzbereich hinaus vor.                             |
| Verfügbar- keit      | Normal               | Das Telefaxgerät wird als Ersatzteil bereitgestellt und bei Bedarf zeitnah ersetzt.                                                                  |

Eine Neuerung der vergangenen Jahre sind mobile Datenverarbeitungsgeräte, die unter anderem als Smartphones bezeichnet werden.

' Smartphones sind Mobiltelefone mit eingebauten E-Mail-Funktionen, Web-Browser, Terminverwaltung und spezifischen Applikationen für Mobile-Betriebssysteme. ' [88, S. 831]

<!-- page: 78 -->

Während es mit iOS und Android zwei dominante Betriebssystemgruppen gibt, wird aufgrund der Verbreitung [94] von einem Android-Betriebssystem ausgegangen.

Tabelle 4.17: Zielobjekt SYS06

| SYS06 Smartphones mit Android-Betriebssystem   | SYS06 Smartphones mit Android-Betriebssystem   | SYS06 Smartphones mit Android-Betriebssystem                                                                                                                                    |
|------------------------------------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                                     | Schutzbe- darf                                 | Begründung                                                                                                                                                                      |
| Vertraulich- keit                              | Normal                                         | Da Informationen mit normalen Schutzbedarf verar- beitet werden, vererbt sich der normale Schutzbedarf des Geschäftsprozesses auch auf dieses Zielobjekt.                       |
| Integrität                                     | Normal                                         | Smartphones und Tablets sind für die Behördenzwe- cke angepasst und enthalten im Rahmen des Ge- schäftsprozesses keine Daten, die besonders in der Integrität zu schützen sind. |
| Verfügbar- keit                                | Normal                                         | Das Vorhalten von entsprechenden Ersatzgeräten und die Verarbeitung normaler Informationen führt zu einem normalen Schutzbedarf.                                                |

Zuletzt werden die Ergebnisse der Textverarbeitung zum Teil in Papierform benötigt. Im Bereich von großen Organisationen bieten sich dazu Netzwerk-Multifunktionsgeräte an, die über eine hohe Leistungsfähigkeit und ein großes Einsatzspektrum verfügen.

Netzwerk-Multifunktionsgeräte  sind  Kombinationsgeräte  zur  Erstellung/Druck von Papierdokumenten [88, S. 265] und zur optischen Erfassung von Informationen, die als Kontrastmuster (Druckschrift, Handschrift, Rasterbild, Foto) vorliegen [88, S. 783].

Tabelle 4.18: Zielobjekt SYS07

| SYS07 Netzwerk-Multifunktionsgeräte   | SYS07 Netzwerk-Multifunktionsgeräte   | SYS07 Netzwerk-Multifunktionsgeräte                                                                                                                       |
|---------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                            | Schutzbe- darf                        | Begründung                                                                                                                                                |
| Vertraulich- keit                     | Normal                                | Da Informationen mit normalen Schutzbedarf verar- beitet werden, vererbt sich der normale Schutzbedarf des Geschäftsprozesses auch auf dieses Zielobjekt. |
| Integrität                            | Normal                                | Das Multifunktionsgerät ist vor unberechtigten Zu- griffen abgesichert. Integritätsverletzungen hätten nur Folgen im Rahmen des normalen Schutzbedarfs.   |
| Verfügbar- keit                       | Normal                                | Der Ausfall des Netzwerk-Multifunktionsgeräts ist in die normale Schutzbedarfskategorie einzuordnen.                                                      |

<!-- page: 79 -->

## 4.2.2.4 Netze- und Kommunikation

In diesem Teil des Informationsverbunds wird die zugrunde liegende Infrastruktur betrachtet, die die vorgenannten Anteile miteinander verbindet. Die Grundlage dieser Vernetzung innerhalb der Behörde ist die Gebäudeverkabelung :

'Multifunktionale, in der Realität aber vorwiegend für digitale Telefonie und Daten vorgesehene, Vollverkabelung ganzer Unternehmenskomplexe.' [88, S. 962]

In diesem Zusammenhang wird hier auch die elektrotechnische Verkabelung des Gebäudes für die Stromversorgung verstanden.

Tabelle 4.19: Zielobjekt NET01

| NET01 Gebäudeverkabelung   | NET01 Gebäudeverkabelung   | NET01 Gebäudeverkabelung                                                                                                                                                          |
|----------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                 | Schutzbe- darf             | Begründung                                                                                                                                                                        |
| Vertraulich- keit          | Hoch                       | Es wird eine hohe Vertraulichkeit durch den Trans- port von Daten der PKI und des Verzeichnisdienstes vererbt.                                                                    |
| Integrität                 | Hoch                       | Da Informationen mit hohem Schutzbedarf über die Gebäudeverkabelung transportiert werden, liegt ein hoher Schutzbedarf vor.                                                       |
| Verfügbar- keit            | Normal                     | Eine Reparatur der Verkabelung bei einer Einschrän- kung kann zeitnah erfolgen und über das Vorhalten von entsprechenden Ersatzteilen und Leitungsplä- nen sichergestellt werden. |

Zur internen Verteilung der Daten wird ein Switch verwendet. Ein Switch definiert sich als:

' Vermittlungsgerät  auf  OSI-Schicht  2  zur  Weiterleitung  von  Rahmen  in  LANs; [Switches]  besorgen  Direktverbindungen  unter  Verwendung  der MAC-Adresse, sie streuen die zu verteilenden Daten also nicht wie Hubs an alle Clients, sondern kanalisieren den Leitungsverkehr .' [88, S. 878-879]

Ohne eine Verbindung zu dem Switch ist faktisch kein Zugriff auf das Netzwerk der Behörde - und damit auf die Serverressourcen - möglich.

| NET02 Switch      | NET02 Switch   | NET02 Switch                                                                                                                                                                                      |
|-------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel        | Schutzbe- darf | Begründung                                                                                                                                                                                        |
| Vertraulich- keit | Hoch           | Ähnlich der Gebäudeverkabelung werden über den Switch besonders schützenswerte Daten der PKI und des Verzeichnisdienstes koordiniert. Daraus ent- steht ein hoher Schutzbedarf für dieses Objekt. |

<!-- page: 80 -->

Tabelle 4.20: Zielobjekt NET02

| Integrität      | Hoch   | Auch besonders schützenswerte Datenverarbei- tungsprozesse werden über die Gebäudeverkabelung durchgeführt und durch den Switch im Netzwerk verteilt. Dieser erbt den hohen Schutzbedarf.           |
|-----------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Verfügbar- keit | Normal | Ein Ersatzgerät wird vorgehalten und notfalls ausge- tauscht. Konfigurationen lassen sich auf Datenträ- gern separat vorhalten und aufspielen. Die Verfüg- barkeit liegt daher im normalen Bereich. |

Die Steuerung zu Kommunikationsverbindungen außerhalb der Organisation wird über einen Router hergestellt.

'Intelligenter Brückenrechner auf der Vermittlungsschicht (3) von OSI zwischen kompatiblen, aber nicht unbedingt gleichartigen Netzwerken (Unterschiede auf Schichten 1 oder 2) zu deren gegenseitiger Integration, zur Optimierung der Datenwege und neuerdings zur Komprimierung der Daten vor dem Transfer; ein R. begrenzt die Kollisionsund die Broadcast-Domäne; R. sind vor allem Paketleitsysteme, arbeiten mit logischen Adressen (IP) und sind deshalb flexibler als Bridges.' [88, S. 766]

In diesem Zusammenhang wird der Router für die Verbindung in das Internet und, abhängig von der Netzwerkstruktur, in die DMZ (Demilitarisierte Zone) verwendet.

Tabelle 4.21: Zielobjekt NET03

| NET03 Router      | NET03 Router   | NET03 Router                                                                                                                                  |
|-------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel        | Schutzbe- darf | Begründung                                                                                                                                    |
| Vertraulich- keit | Normal         | Eine Steuerung vertraulicher Informationen in das Internet ist nicht vorgesehen, sodass ein normaler Schutzbedarf besteht.                    |
| Integrität        | Normal         | Über den Router werden nur Informationen geleitet, die einem normalen Schutzbedarf unterliegen.                                               |
| Verfügbar- keit   | Normal         | Ersatzgeräte werden vorgehalten und notfalls ausge- tauscht. Konfigurationen lassen sich auf Datenträ- gern separat vorhalten und aufspielen. |

Die Kontrolle und Filterung des Netzwerksverkehrs obliegen der Firewall . Diese definiert sich wie folgt:

' Hard- oder Software, die zwischen Rechner oder lokale Netzwerke und öffentliche Netze geschaltet wird, um den Zugriff auf Rechner von außen durch unbefugte Dritte zu verhindern und so interne Daten zu schützen. Auf einzelnen Rechnern installierte Firewalls, die mit dem Internet verbunden sind, werden Personal Firewall genannt. ' [89, S. 70]

<!-- page: 81 -->

Die Firewall ist durch die Filter- und Einschränkungsmöglichkeiten des unberechtigten Netzwerkverkehrs an externe Ressourcen ein zentraler Bestandteil der Sicherheitsarchitektur.

Tabelle 4.22: Zielobjekt NET04

| NET04 Firewall    | NET04 Firewall   | NET04 Firewall                                                                                                                                                                                                                                                                |
|-------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel        | Schutzbe- darf   | Begründung                                                                                                                                                                                                                                                                    |
| Vertraulich- keit | Hoch             | Die Firewall-Regeln müssen vertraulich behandelt werden, da sonst potenzielle Angreifer Möglichkei- ten für eine System-Kompromittierung ausspähen können. Ein darauf basierender Angriff kann die Ar- beitsfähigkeit der Behörde entschieden beeinträchti- gen.              |
| Integrität        | Hoch             | Die Firewall-Regeln dürfen auf keinen Fall unbe- rechtigt verändert werden. Entsprechende Eingriffe oder falsche Daten gefährden die Handlungsfähig- keit der Behörde außerordentlich, weshalb ein hoher Schutzbedarf entsteht.                                               |
| Verfügbar- keit   | Hoch             | Die Firewall schützt jederzeit das Behördennetz ge- gen unberechtigte Zugriffe und andere sicherheitsre- levante Interaktionen. Eine Ausfallzeit von 24 Stun- den ist nicht tolerabel, da in diesem Falle jegliche be- troffene Außenverbindungen unterbrochen werden müssen. |

Zwingend für die externe Kommunikation wird der Internet-Zugang benötigt. Neben Webplattformen und Recherchen wird die Internetverbindung, über eine Netzanbindung eines Providers, für die Erbringung weiterer, netzwerkbezogener Dienste benötigt.

| NET05 Internet-Zugang   | NET05 Internet-Zugang   | NET05 Internet-Zugang                                                                                                                                                           |
|-------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel              | Schutzbe- darf          | Begründung                                                                                                                                                                      |
| Vertraulich- keit       | Normal                  | Vertrauliche Informationen werden durch den Ge- schäftsprozess nicht verursacht, weshalb auch die Steuerung zu einem Internet-Provider von norma- lem Schutzbedarf ist.         |
| Integrität              | Normal                  | Der Internetzugang ist durch entsprechende Proto- kolle und Maßnahmen ausreichend abgesichert. Über diesen werden nur Informationen des norma- len Schutzbedarfs transportiert. |
| Verfügbar- keit         | Normal                  | Ein Ausfall der Internetverbindung ist für 24 Stun- den tolerierbar, die Aufgabenwahrnehmung wird dadurch nur im angemessenen Maße eingeschränkt.                               |

<!-- page: 82 -->

## Tabelle 4.23: Zielobjekt NET05

Für die interne und externe Kommunikation werden Telefax- und Telefondienste benötigt.

'[Telefon als]  Fernsprechdienst; b enutzt wird das klassische und analoge, weltweite Telefonnetz […]; die weltweit geführten Auslandgespräche haben zwischen 1999 und 2001 um 20% zugenommen; Ende 2001 machte die analoge Telefonie 94% der geführten Ferngespräche aus[…], das Web Phoning, brach te es auf 6%; Tendenz allerdings stark steigend.' [87, S. 896]

In diesem Zusammenhang wird Voice-over-IP als Protokoll verwendet:

'Mittlerweile eingebürgerte  Bezeichnung  für  die  Sprachband -Telefonie  im  TCP/IPNetz bzw. Internet.' [87, S. 977]

Bei dem Telefaxdienst handelt es um:

'Fernkopierdienst in der Telekommunikation […].' [87, S. 896]

Die Bereitstellung dieser Dienste findet in der Behörde durch einen zentralen Serverdienst statt.

| NET06 Telefondienst   | NET06 Telefondienst   | NET06 Telefondienst                                                                                                                                                          |
|-----------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel            | Schutzbe- darf        | Begründung                                                                                                                                                                   |
| Vertraulich- keit     | Normal                | Da Informationen mit normalen Schutzbedarf verar- beitet werden, vererbt sich der normale Schutzbedarf des Geschäftsprozesses auf dieses Zielobjekt.                         |
| Integrität            | Normal                | Es werden Informationen mit normalen Schutzbe- darf verarbeitet, für die Integrität vererbt sich der normale Schutzbedarf des Geschäftsprozesses auch auf dieses Zielobjekt. |
| Verfügbar- keit       | Normal                | Neben einer telefonischen Erreichbarkeit bestehen weitere Kommunikationskanäle für die Aufgaben- wahrnehmung.                                                                |

Tabelle 4.24: Zielobjekt NET06

| NET07 Telefaxdienst   | NET07 Telefaxdienst   | NET07 Telefaxdienst                                                                                                                                                          |
|-----------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel            | Schutzbe- darf        | Begründung                                                                                                                                                                   |
| Vertraulich- keit     | Normal                | Da Informationen mit normalen Schutzbedarf verar- beitet werden, vererbt sich hier ein normaler Schutz- bedarf.                                                              |
| Integrität            | Normal                | Es werden Informationen mit normalen Schutzbe- darf verarbeitet, für die Integrität vererbt sich der normale Schutzbedarf des Geschäftsprozesses auch auf dieses Zielobjekt. |

<!-- page: 83 -->

Tabelle 4.25: Zielobjekt NET07

| Verfügbar- keit   | Normal   | Neben einer Erreichbarkeit per Telefax bestehen weitere Kommunikationskanäle für die Aufgaben- wahrnehmung und verbindliche Kommunikation der Behörde.   |
|-------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|

Für einen externen Zugriff auf die Netzinfrastruktur und Daten wird zur sicheren Kommunikation ein abgesicherter Zugang in Form eines virtuellen privaten Netzwerkes (VPN) benötigt.

' [D]urch strenge Authentisierung, Autorisierung und Verschlüsselung gesicherte und deshalb vertrauliche Koppelung zweier geschlossener Netzwerke über eine öffentliche und unsichere Netzwerkinfrastruktur; Beispiel: für ein gesichertes Extranet werden VPN benötigt.' [88, S. 970]

Der Anwendungsfall einer VPN-Verbindung ist der Fernzugriff für die Heim- und Telearbeit.

Tabelle 4.26: Zielobjekt NET08

| NET08 Abgesicherter Netzwerk-Zugang über ein VPN   | NET08 Abgesicherter Netzwerk-Zugang über ein VPN   | NET08 Abgesicherter Netzwerk-Zugang über ein VPN                                                                                                                                                                                                   |
|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                                         | Schutzbe- darf                                     | Begründung                                                                                                                                                                                                                                         |
| Vertraulich- keit                                  | Normal                                             | Unberechtigte Kenntnisnahmen können bei diesem Zielobjekt zu Beeinträchtigungen führen, bei denen gemäß des normalen Schutzbedarfes keine schwer- wiegende Folge eintreten sollte. Administrative Pro- zesse sind von der VPN-Verbindung getrennt. |
| Integrität                                         | Normal                                             | Unberechtigte Veränderungen können bei diesem Zielobjekt zu Beeinträchtigungen führen, die auf- grund des normalen Schutzbedarfes des zugrunde liegenden Geschäftsprozesses Folgen im Rahmen des normalen Schutzbedarfs haben.                     |
| Verfügbar- keit                                    | Normal                                             | Ein Ausfall des externen Netzwerkzugriffes ist für 24 Stunden tolerierbar, die Aufgabenwahrnehmung wird dadurch im angemessenen Maße eingeschränkt                                                                                                 |

## 4.2.2.5 Räume

Als letzte Betrachtungsebene wird in der Feststellung des Informationsverbunds die Gebäudeinfrastruktur betrachtet. Es wird zwischen den Gebäuden, sofern es unterschiedliche Gebäudetypen gibt, und den Raumtypen unterschieden.

Zunächst gibt es die Kategorisierung des allgemeinen Gebäudes , in dem die Behörde ihren Sitz hat. Alle nachfolgenden Räume sind Teil dieses Gebäudes, was den hohen Schutzbedarf verursacht.

<!-- page: 84 -->

Tabelle 4.27: Zielobjekt INF01

| INF01 Allgemeines Gebäude   | INF01 Allgemeines Gebäude   | INF01 Allgemeines Gebäude                                                                                                                                                          |
|-----------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                  | Schutzbe- darf              | Begründung                                                                                                                                                                         |
| Vertraulich- keit           | Hoch                        | Es gilt das Vererbungsprinzip. In dem allgemeinen Gebäude befindet sich auch der Serverraum. Zudem muss eine Akkumulation der Schutzbedarfe in Be- tracht gezogen werden.          |
| Integrität                  | Hoch                        | In dem Gebäude werden grundsätzlich alle Informa- tionen verarbeitet und es fungiert als Server- und Ser- verdienststandort. Es kommt zu einer Vererbung des hohen Schutzbedarfes. |
| Verfügbar- keit             | Hoch                        | In dem Gebäude werden grundsätzlich alle Informa- tionen verarbeitet und es fungiert als Serverstandort. Daher kommt es zu einer Vererbung des hohen Schutzbedarfes.               |

In dem Gebäude sind unterschiedliche Räumlichkeiten vorhanden. Der Büroraum ist der Arbeitsplatz der Mitarbeiter, ausgestattet mit einem stationären Telefon und einem Arbeitsplatz- oder Mobilen-PC. Hier werden die Aufgaben und Tätigkeiten für den Geschäftsprozess wahrgenommen.

Tabelle 4.28: Zielobjekt INF02

| INF02 Büroraum    | INF02 Büroraum   | INF02 Büroraum                                                                                                                                                                                           |
|-------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel        | Schutzbe- darf   | Begründung                                                                                                                                                                                               |
| Vertraulich- keit | Normal           | Im Büroraum werden durch Mitarbeiter Daten mit normalem Schutzbedarf verarbeitet und mitunter in Papierform aufbewahrt.                                                                                  |
| Integrität        | Normal           | Normal eingestufte Arbeitsprozesse werden in den Büroräumen als Arbeitsplatz durchgeführt. Daher hat dieser einen normalen Schutzbedarf.                                                                 |
| Verfügbar- keit   | Normal           | Ohne zur Verfügung stehende Büroräumlichkeiten besteht keine Möglichkeit zur Aufgabenwahrneh- mung. Allerdings ist eine dadurch verursachte Stö- rung des Geschäftsprozesses im tolerierbaren Be- reich. |

Der Serverraum, auch als Rechenzentrum bezeichnet, fungiert als zentraler Raum für die Servermaschinen. Ein Rechenzentrum lässt sich definieren als:

'Zentrale datenverarbeitende und -speichernde Infrastruktur bei zentralisierten, betrieblichen IT-Lösungen oder ITDienstleistern.' [88, S. 737]

Dieser Raum enthält die Serverinfrastruktur und muss entsprechend abgesichert werden, durch die Zentralität entsteht ein hoher Schutzbedarf.

<!-- page: 85 -->

Tabelle 4.29: Zielobjekt INF03

| INF03 Serverraum   | INF03 Serverraum   | INF03 Serverraum                                                                                                                                                                                                                                    |
|--------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel         | Schutzbe- darf     | Begründung                                                                                                                                                                                                                                          |
| Vertraulich- keit  | Hoch               | Physischer Standort des Servers bzw. der Server, da- her kommt der Vererbungs- sowie der Kumulations- effekt zum Tragen. Von hier aus werden wesentliche Dienste bereitgestellt.                                                                    |
| Integrität         | Hoch               | Vererbung des Schutzbedarfes von den dort betrie- benen Servermaschinen und den darauf betriebenen Diensten wie dem Verzeichnisdienst.                                                                                                              |
| Verfügbar- keit    | Hoch               | Der Serverraum ist der zentrale Raum, der für die Er- bringung der IT-Dienste im Dienstgebäude verant- wortlich ist. Es kommt zu einer Vererbung des ho- hen Schutzbedarfes von den dort betriebenen Ser- vern und den darauf betriebenen Diensten. |

Für Besuche,  Fortbildungen  und  Präsentationen  verfügt  die  oberste  Landesbehörde ebenfalls  über  einen Präsentations- und Besprechungsraum. Diese  Räumlichkeit dient besonders zur Besprechung mit mehreren (auch externen) Personen, weshalb dort kein Zugriff auf sensitive Daten möglich ist. Gleichzeitig sollen dort vertraulich geführte Gespräche nicht mit- oder abgehört werden können.

Tabelle 4.30 : Zielobjekt INF04

| INF04 Präsentations- und Besprechungsraum   | INF04 Präsentations- und Besprechungsraum   | INF04 Präsentations- und Besprechungsraum                                                                                                                                                                             |
|---------------------------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                                  | Schutzbe- darf                              | Begründung                                                                                                                                                                                                            |
| Vertraulich- keit                           | Normal                                      | Es werden hier keine besonders schützenswerten Daten verarbeitet und es stehen nur eingeschränkte IT-Ressourcen zur Verfügung.                                                                                        |
| Integrität                                  | Normal                                      | Im Präsentations- und Besprechungsraum stehen nur eingeschränkte IT-Ressourcen zur Verfügung. Falsche und/oder unberechtigt veränderte Informa- tionen haben nur Auswirkungen in der normalen Schutzbedarfskategorie. |
| Verfügbar- keit                             | Normal                                      | Es sind keine besonderen Schutzbedarfe des Präsen- tations- und Besprechungsraums hinsichtlich der Verfügbarkeit erkennbar.                                                                                           |

Die Mitarbeiter der Behörde können einen häuslichen Arbeitsplatz einrichten, der die Aufgabenwahrnehmung über einen Fernzugriff ermöglicht. Dieser Raum ist in den privaten Wohnbereich von Mitarbeitern integriert und über das VPN wird ein sicherer Zugriff auf das Behördennetzwerk sichergestellt.

<!-- page: 86 -->

Tabelle 4.31: Zielobjekt INF05

| INF05 Häuslicher Arbeitsplatz   | INF05 Häuslicher Arbeitsplatz   | INF05 Häuslicher Arbeitsplatz                                                                                                                                       |
|---------------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schutzziel                      | Schutzbe- darf                  | Begründung                                                                                                                                                          |
| Vertraulich- keit               | Normal                          | Gemäß des Vererbungsprinzips ist von einer norma- len Vertraulichkeit der Daten auszugehen, die an ei- nem häuslichen Arbeitsplatz verarbeitet werden.              |
| Integrität                      | Normal                          | Der häusliche Arbeitsplatz hat im Rahmen des Ge- schäftsprozesses Zugriff auf Schutzbedarfe im nor- malen Bereich. Dementsprechend gestaltet sich der Schutzbedarf. |
| Verfügbar- keit                 | Normal                          | Es sind keine Schutzbedarfe des häuslichen Arbeits- platzes über das normale Maß hinaus hinsichtlich der Verfügbarkeit erkennbar.                                   |

Eine weitere Räumlichkeit ist der Drucker- und Kopierraum .  Dieser ist mit einem Netzwerk-Multifunktionsgerät  ausgestattetet,  welches  zentral  für  Büroaufgaben  wie Scans, Ausdrucke, Kopien und dergleichen vorgesehen ist. Dort sammeln sich, zumindest temporär, Daten und Unterlagen an, so dass sich dieser Raum in seiner Art und Nutzung von einem normalen Büroraum unterscheidet.

Tabelle 4.32: Zielobjekt INF06

| INF06 Drucker- und Kopierraum   | INF06 Drucker- und Kopierraum   | INF06 Drucker- und Kopierraum                                                                                         |
|---------------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Schutzziel                      | Schutzbe- darf                  | Begründung                                                                                                            |
| Vertraulich- keit               | Normal                          | Vererbung von dem Netzwerk-Multifunktionsgerät auf dem Schutzbedarf 'Normal'.                                         |
| Integrität                      | Normal                          | Es findet eine Vererbung des normalen Schutzbe- darfs vom Geschäftsprozess sowie von dem Multi- funktionsgerät statt. |
| Verfügbar- keit                 | Normal                          | Der Schutzbedarf des Drucker- und Kopierraums ist im normalen Bereich.                                                |

<!-- page: 87 -->

## 4.2.3 Netzplan

Teil des IT-Grundschutz-Profils kann ein Netzplan sein, der auf abstrakter Ebene die Zielobjekte des Informationsverbunds in einen Zusammenhang setzt [16, S. 13]. Für eine klare Struktur des Netzplans sind die Kürzel der Zielobjekte hier, soweit möglich, dargestellt. Auf die Hervorhebung der Netztrennung von Systemen mit hohem Schutzbedarf wird in der schematischen Darstellung verzichtet. Abbildung 4.1 stellt in dem Netzplan die Referenzarchitektur einer obersten Landesbehörde dar:

Abbildung 4.1: Netzplan der Referenzarchitektur (eigene Darstellung)

<!-- image -->

<!-- page: 88 -->

## 4.3 Modellierung des Informationsverbunds

In dem vorherigen Kapitel sind die abzusichernden Zielobjekte aufgezählt, auf deren  Basis  nun  die  IT-Grundschutz-Bausteine  ausgewählt  werden.  Zunächst  werden dazu die gesamten Zielobjekte und entsprechenden IT-Grundschutz-Bausteine aufgezählt.

Dies stellt dar, welche Zielobjekte durch den IT-Grundschutz bereits abgebildet sind und welche gegebenenfalls aufgrund eines fehlenden IT-Grundschutz-Bausteins einer Risikoanalyse unterzogen werden müssen. Anschließend werden die ausgewählten IT-Grundschutz-Bausteine separat in ihren jeweiligen Gruppen aufgezählt und es werden relevante Anforderungen für die Anwendung in den obersten Landesbehörden aufgeführt.

## 4.3.1 Absicherung der Zielobjekte

Die allgemeinen Prozess-Bausteine werden für eine bessere Verständlichkeit auf der Ebene des Informationsverbundes bzw. des Geschäftsprozesses aufgelistet, da eine Anwendung dieser auf die gesamte Referenzarchitektur stattfindet. Diese IT-Grundschutz-Bausteine sind anhand ihrer Relevanz für die obersten Landesbehörden ausgewählt.

Da eine Basis- und Standard-Absicherung die Erfüllung der entsprechenden Anforderungen auf der Ebene der Basis- und Standard-Anforderungen voraussetzt [64, S. 133-134], werden diese beiden Anforderungsgruppen mit dieser Nennung in die Sicherheitsanforderungen des IT-Grundschutz-Profils aufgenommen. Eine Reproduktion der einzelnen  Anforderungen  findet  nicht  statt,  diese  lassen  sich  indes  dem  IT-Grundschutz-Kompendium entnehmen.

Für eine vollständige Sicherheitskonzeption auf der Basis der Standard-Absicherung  MÜSSEN  die  Basis-Anforderungen  der  nachfolgend  aufgezählten  IT-Grundschutz-Bausteine erfüllt werden. Ebenso SOLLEN die Standard-Anforderungen umgesetzt werden, wobei es organisatorische Gründe für eine ausbleibende Umsetzung geben kann. Die Verwendung dieser Begriffe orientiert sich an der in Kapitel 2.3.3 dargelegten Nutzung im IT-Grundschutz.

| Anwendungen   | Anwendungen                                                        | Anwendungen                                                                                                                                                                                                                              |
|---------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID            | Zielobjekt                                                         | Bausteine                                                                                                                                                                                                                                |
| PRO01         | Allgemeiner Informations- verbund / Beteiligung an der Normsetzung | ISMS.1; OPS.1.1.2; OPS.1.1.3; OPS.1.1.4; OPS.1.1.5; OPS1.1.6; OPS.1.2.2; OPS.1.2.3; OPS.1.2.4; OPS.2.4 ORP.1; ORP.2; ORP.3; ORP.4; ORP.5 CON.1; CON.3; CON.4; CON.6; DER.1; DER.2.1; DER.2.2; DER.2.3; DER.3.1 DER.3.2; DER.4 SYS.3.2.2; |

<!-- page: 89 -->

Tabelle 4.33: Modellierung der Referenzarchitektur

| APP01                   | Betriebssystem Windows 10                   | SYS.2.1; SYS.2.2.3                  |
|-------------------------|---------------------------------------------|-------------------------------------|
| APP02                   | Microsoft Office 2016                       | APP.1.1                             |
| APP03                   | Dateiserver                                 | APP.3.3                             |
| APP04                   | Web-Browser Firefox                         | APP.1.2                             |
| APP05                   | Verzeichnisdienst Active Directory          | APP.2.1, APP.2.2                    |
| APP06                   | Microsoft Exchange                          | APP.5.1; APP.5.2                    |
| APP07                   | Public-Key Infrastruktur                    | Kein spezieller Baustein vorhanden. |
| IT-Systeme              | IT-Systeme                                  | IT-Systeme                          |
| SYS01                   | Windows-Server 2016                         | SYS.1.1; SYS.1.2.3 (in Erstellung)  |
| SYS02                   | Arbeitsplatz-PC                             | SYS.2.1; SYS.2.2.3                  |
| SYS03                   | Mobiler-PC                                  | SYS.2.1; SYS.3.1; SYS.2.2.3         |
| SYS04                   | Telefon                                     | NET.4.1                             |
| SYS05                   | Telefaxgerät                                | NET.4.3                             |
| SYS06                   | Smartphones mit And- roid-Betriebssystem    | APP.1.4; SYS.3.2.1; SYS.3.2.4       |
| SYS07                   | Netzwerk-Multifunkti- onsgerät              | SYS.4.1                             |
| Netzwerkkomponenten     | Netzwerkkomponenten                         | Netzwerkkomponenten                 |
| NET01                   | Gebäudeverkabelung                          | NET.1.1                             |
| NET02                   | Switch                                      |                                     |
| NET03                   | Router                                      | NET.3.1                             |
| NET04                   | Firewall                                    | NET.3.2                             |
| NET05                   | Internet-Zugang                             | NET.1.1                             |
| NET06                   | Telefondienst                               | NET.4.2                             |
| NET07                   | Telefaxdienst                               | NET.4.3                             |
| NET08                   | Abgesicherter Netzwerk- Zugang über ein VPN | NET.3.3                             |
| Räumliche Infrastruktur | Räumliche Infrastruktur                     | Räumliche Infrastruktur             |
| INF01                   | Allgemeines Gebäude                         | INF.1; INF.3; INF.4                 |
| INF02                   | Büroraum                                    | INF.7                               |
| INF03                   | Serverraum                                  | INF.2                               |
| INF04                   | Präsentations- und Be- sprechungsraum       | INF.10                              |
| INF05                   | Häuslicher Arbeitsplatz                     | INF.8                               |
| INF06                   | Drucker- und Kopier- raum                   | Kein spezieller Baustein vorhanden. |

<!-- page: 90 -->

## 4.3.2 Zusätzliche Anforderungen

Aus der Modellierung ergeben sich die Anforderungen an die Sicherheitskonzeption der Standard-Absicherung. Dazu sollen die Anmerkungen der ISB der obersten Landesbehörden ebenfalls berücksichtigt werden. Das IT-Grundschutz-Profil wurde während der Erstellung dazu den ISB von vier obersten Landesbehörden vorgelegt, die sich als Ansprechpartner bereiterklärt haben.

Die aus der Fachliteratur und den Angaben der ISB entstammenden Anmerkungen werden in dem IT-Grundschutz-Profil berücksichtigt und sind anzuwenden. Dazu wird neben dem Bezug der Anmerkung ebenfalls dargestellt, woher die Modifikation der Anforderungen stammt.

| Anforde- rung   | Titel                                                  | Anmerkung                                                                                                                                                            | Begründung                                                                                                                                                                                     | Quelle                                                                                                                                                   |
|-----------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ISMS.1.A10      | Erstel- lung ei- nes Si- cher- heitskon- zepts         | Die Anforde- rung MUSS um- gesetzt werden.                                                                                                                           | Gemäß der ISLL-Bund müssen die Ver- waltungen des Bundes und der Länder Sicher- heitskonzeptio- nen erstellen.                                                                                 | ISLL-Bund                                                                                                                                                |
| ISMS.1.A12      | Manage- ment-Be- richte zur Informa- tionssi- cherheit | Die Anforde- rung MUSS um- gesetzt werden.                                                                                                                           | Diese Anforde- rungen stellen die erfolgreiche Umsetzung des ISMS in der Be- hörde sicher.                                                                                                     | Expertenbeitrag                                                                                                                                          |
| ORP.4.A8        | Regelung des Pass- wortge- brauchs                     | Passwörter DÜRFEN NICHT im Klartext elektro- nisch gespei- chert werden. Stattdessen SOLLTE ein Prüfsummenver- fahren nach dem Stand der Tech- nik verwendet werden. | Im Klartext ab- gespeicherte Be- nutzer-Pass- wort-Kombina- tionen können intern zu einem Missbrauch füh- ren oder bei ei- nem Datenab- fluss dem An- greifer weitere Möglichkeiten einräumen. | Ein entsprechen- des Sicherungs- vorgehen wird in der ISO 27002:2013 [51, S. 27], der NIST SP 800-63B [95, S. 15] und der PCI DSS [96, S. 72] empfohlen. |
| CON.2.1.1       | Einlei- tung / Standard- Daten- schutz- modell         | Der Baustein CON.2 ist nicht anzuwenden.                                                                                                                             | Für die Verwal- tungsbehörden gilt bereits das bundesweit etablierte Stan- dard-Daten- schutzmodell                                                                                            | IT-Grundschutz Kompendium, Baustein CON.2 - Datenschutz.                                                                                                 |

<!-- page: 91 -->

Tabelle 4.34: Anmerkungen zu der Modellierung des Informationsverbundes

| (SDM) und die entsprechende Datenschutzge- setzgebung. Da- her wird der Baustein hier als redundant be- trachtet.   |
|---------------------------------------------------------------------------------------------------------------------|

## 4.4 Risikobetrachtung des Dateiservers

Da die Modellierung des Informationsverbunds durchgeführt ist, ist nun im Rahmen der Standard-Absicherung auf Basis der Schutzbedarfsfeststellung eine Risikobetrachtung durchzuführen [65, S. 9-10].

Gemäß dem BSI Standard 200-3, der sich mit der Risikoanalyse befasst, sind von einer Risikobetrachtung mehrere Gruppen an Zielobjekten betroffen [65, S. 6]:

1. Zielobjekte mit einem hohem und sehr hohen Schutzbedarf.
2. Zielobjekte, für die bislang kein IT-Grundschutz-Baustein besteht.
3. Zielobjekte, die außerhalb ihrer üblichen Einsatzszenarien angewendet werden.

Anhand dieser Kriterien handelt es sich in Referenzarchitektur um 10 Zielobjekte, die einer Risikobetrachtung unterzogen werden müssen:

| ID    | Was                                  | Vertraulich- keit   | Integri- tät   | Verfügbar- keit   |
|-------|--------------------------------------|---------------------|----------------|-------------------|
| APP03 | Dateiserver                          | Normal              | Normal         | Hoch              |
| APP05 | Verzeichnisdienst Active Di- rectory | Hoch                | Hoch           | Hoch              |
| APP07 | Public-Key Infrastruktur             | Hoch                | Hoch           | Hoch              |
| SYS01 | Windows-Server 2016                  | Hoch                | Hoch           | Hoch              |
| NET01 | Gebäudeverkabelung                   | Hoch                | Hoch           | Normal            |
| NET02 | Switch                               | Hoch                | Hoch           | Normal            |
| NET06 | Firewall                             | Hoch                | Hoch           | Hoch              |
| INF01 | Allgemeines Gebäude                  | Hoch                | Hoch           | Hoch              |

<!-- page: 92 -->

Tabelle 4.35: Zielobjekte für eine Risikoanalyse

| INF03   | Serverraum              | Hoch                                       | Hoch                                       | Hoch                                       |
|---------|-------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|
| INF06   | Drucker- und Kopierraum | Kein IT-Grundschutz Baustein vorhan- den . | Kein IT-Grundschutz Baustein vorhan- den . | Kein IT-Grundschutz Baustein vorhan- den . |

In diesem Unterkapitel wird eines dieser 10 Zielobjekte nach den Vorgaben des BSI Standards 200-3 einer Risikobetrachtung und -behandlung unterzogen. Diese Risikobetrachtung behandelt eine schematisch existierende Organisation, sodass kein tatsächlich existierendes Zielobjekt in seiner Konfiguration und Nutzung einer Risikoanalyse unterzogen wird.

Dementsprechend orientieren sich die festgestellten Risiken nicht an tatsächlichen Gegebenheiten und können so keinen verbindlichen Charakter für die obersten Landesbehörden entwickeln - gemäß den Grundannahmen der ISO 31000:2018 ist die Risikoanalyse durch jede Organisation auf ihren spezifischen internen und externen Kontext anzuwenden [53, S. 3].

Ausgehend davon soll durch eine Organisation keine generische Risikoanalyse genutzt werden, um eine individuelle Betrachtung der eigenen Infrastruktur zu vermeiden. Diese Risikoanalyse hat einen exemplarischen Charakter, kann aber in ihrer Struktur und Formulierung als Leitfaden dienen. So wird neben den Risikokriterien, bei denen ein Rückgriff auf den BSI Standard 200-3 stattfindet, auch eine generische Risikomatrix dargestellt.

Durch die zentrale Rolle des Dateiservers in der Datenaufbewahrung, -verwaltung und Kollaboration wird dieses Zielobjekt der schematischen Risikobetrachtung unterzogen. Dadurch können sich weitere Anforderungen als Risikobehandlung ergeben, um die festgestellten Risiken zu verringern.

## 4.4.1 Risikokriterien

Vor der Risikoanalyse müssen zunächst die Rahmenbedingungen der Behörde in Bezug auf Risiken festgelegt werden. Als Grundlage der Risikobetrachtung dient zunächst die Festlegung von Risikokriterien, aus deren Perspektive die Risiken für das jeweilige Zielobjekt eingeordnet werden [55, S. 63-64].

Ähnlich der Schutzbedarfskategorien wird auf die vorgeschlagene Risikokriterien seitens des BSI zurückgegriffen und damit der semi-qualitative Ansatz verfolgt. Die Risikokriterien für die Eintrittshäufigkeit und Schadenshöhe, die hier angewendet werden, gestalten sich im Standard 200-3 wie folgt [65, S. 26-27]:

| Eintrittshäufigkeit   | Beschreibung                                                                     |
|-----------------------|----------------------------------------------------------------------------------|
| selten                | Ereignis könnte nach heutigem Kenntnisstand höchstens alle fünf Jahre eintreten. |
| mittel                | Ereignis tritt einmal alle fünf Jahre bis einmal im Jahr ein.                    |
| häufig                | Ereignis tritt einmal im Jahr bis einmal pro Monat ein.                          |

<!-- page: 93 -->

Tabelle 4.36: Risikokriterium der Eintrittshäufigkeit

| sehr häufig   | Ereignis tritt mehrmals im Monat ein.   |
|---------------|-----------------------------------------|

Tabelle 4.37: Risikokriterium der Schadenshöhe

| Schadenshöhe/Scha- densauswirkungen   | Beschreibung                                                                                      |
|---------------------------------------|---------------------------------------------------------------------------------------------------|
| vernachlässigbar                      | Die Schadensauswirkungen sind gering und können ver- nachlässigt werden.                          |
| begrenzt                              | Die Schadensauswirkungen sind begrenzt und überschau- bar.                                        |
| beträchtlich                          | Die Schadensauswirkungen können beträchtlich sein.                                                |
| existenzbedrohend                     | Die Schadensauswirkungen können ein existenziell be- drohliches, katastrophales Ausmaß erreichen. |

Wenn diese Risikokriterien in einen Zusammenhang zueinander gesetzt werden, ergibt sich daraus die Risikokategorie jeder Gefährdung. Aus dieser leitet sich ab, welche Risiken vordringlich behandelt werden müssen [97, S. 16].

Dazu bietet es sich an, eine Risikomatrix zu erstellen, die die Eintrittswahrscheinlichkeit und -auswirkungen einer Gefährdung anhand des Risikoappetits der Organisation in entsprechende Risikokategorien einordnet [54, S. 21-22]. Nachdem bereits die Risikokriterien aus dem IT-Grundschutz entnommen sind, wird ebenfalls auf die Risikokategorien des Standards 200-3 zurückgegriffen:

Tabelle 4.38: Risikokategorien nach dem Standard 200-3

| Risikokategorien nach dem Standard 200-3 [65, S. 28]:   | Risikokategorien nach dem Standard 200-3 [65, S. 28]:                                                                                                                                                                                     |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gering                                                  | Die bereits umgesetzten oder zumindest im Sicherheitskonzept vorgese- henen Sicherheitsmaßnahmen bieten einen ausreichenden Schutz. In der Praxis ist es üblich, geringe Risiken zu akzeptieren und die Gefährdung dennoch zu beobachten. |
| mittel                                                  | Die bereits umgesetzten oder zumindest im Sicherheitskonzept vorgese- henen Sicherheitsmaßnahmen reichen möglicherweise nicht aus. In ab- sehbarer Zeit sollten Maßnahmen geplant und umgesetzt werden.                                   |
| hoch                                                    | Die bereits umgesetzten oder zumindest im Sicherheitskonzept vorgese- henen Sicherheitsmaßnahmen bieten keinen ausreichenden Schutz vor der jeweiligen Gefährdung.                                                                        |
| sehr hoch                                               | Die bereits umgesetzten oder zumindest im Sicherheitskonzept vorgese- henen Sicherheitsmaßnahmen bieten keinen ausreichenden Schutz vor der jeweiligen Gefährdung. In der Praxis werden sehr hohe Risiken selten akzeptiert.              |

<!-- page: 94 -->

In diesem Zusammenhang muss durch die Verantwortungsträger bedacht werden, dass es sich bei einer obersten Landesbehörde um eine zentrale Institution eines Landes handelt, die weitreichende Entscheidungen auf Landesebene treffen kann und in diversen Gremien tätig ist.

Daher wird für die hier dargestellte Behörde von einer geringen Risikobereitschaft ausgegangen. Angelehnt an die Vorgaben aus dem Standard 200-3 wird in Abbildung 4.2 eine risikoaverse Risikomatrix dargestellt. Diese berücksichtigt den niedrigen Risikoappetit einer obersten Landesbehörde, weshalb ein kleiner Bereich der Risiken als gering und mittel eingeschätzt wird und gegebenenfalls für viele Schadenseintrittswahrscheinlichkeiten und -auswirkungen ein hoher Handlungsbedarf entsteht.

Abbildung 4.2: Risikomatrix einer obersten Landesbehörde (eigene Darstellung auf Basis des BSI Standards 200-3 [65, S. 27])

<!-- image -->

## 4.4.2 Risikoanalyse

Nachdem die Rahmenbedingungen für die Einschätzung und Behandlung von Risiken festgelegt sind, folgt nun die Risikoanalyse des Dateiservers. Dazu wird eine dreiteilige Struktur verwendet, die in die elementaren Gefährdungen nach dem IT-Grundschutz-Baustein, die Risikoidentifikation und -Einschätzung sowie die Risikobehandlung aufgeteilt ist.

## 4.4.2.1 Feststellung der elementaren Gefährdungen

In dem Risikoprozess des Standards 200-3 ist vorgesehen, dass zunächst die elementaren Gefährdungen für das Zielobjekt betrachtet werden [65, S. 16]. Ausgehend von dem Baustein APP.3.3 bestehen nach dem IT-Grundschutz-Kompendium mehrere elementare Gefährdungen für den Dateiserver [24, S. 431-432]. Neben der Aufzählung der Zielobjekte sieht der Standard 200-3 vor, dass zu jeder Gefährdung eine Relevanzfeststellung erfolgt. Für eine umfassende Darstellung in dieser Beispiel-Risikoanalyse werden alle Risiken betrachtet.

<!-- page: 95 -->

Es bleibt zu beachten, dass es weitere elementare Gefährdungen gibt, die auf übergeordnete Objekte wirken [24, S. 40]. Diese Gefahren werden auf der Ebene des jeweiligen Zielobjekts (z.B. Gebäude oder Serverraum) erfasst, im erforderlichen Rahmen abgesichert und werden hier nicht wiederholt. In Tabelle 4.39 sind die elementaren Gefahren für den Dateiserver nach dem IT-Grundschutz-Baustein APP.3.3 aufgeführt:

| Ge- fähr- dung   | Titel                                                 | Schutz- ziel   | Beispiel                                                                                                                                                                             |
|------------------|-------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.14           | Ausspähen von Informationen (Spionage)                | C              | Unberechtigte Personen könnten Zugriff auf die abgelegten Daten erhalten und diese für Ihre Zwecke missbrauchen.                                                                     |
| G 0.16           | Diebstahl von Geräten, Da- tenträgern oder Dokumenten | C, A           | Aus dem Serverraum oder einem anderen Aufstellort für den Dateiserver könnten Fest- platten mit sensiblen Daten entnommen wer- den.                                                  |
| G 0.18           | Fehlplanung o- der fehlende Anpassung                 | C, I, A        | Der Dateiserver und das darunterliegende Ser- ver-Betriebssystem könnten falsch konfigu- riert sein und so bspw. schnell überlasten oder unberechtigte Zugriffe zulassen.            |
| G 0.19           | Offenlegung schützenswer- ter Informatio- nen         | C              | Durch einen berechtigten Benutzer wird die Zugriffsberechtigung falsch eingerichtet und ein unbestimmter Teilnehmerkreis kann die schützenswerten Informationen zur Kenntnis nehmen. |
| G 0.21           | Manipulation von Hard- o- der Software                | C, I, A        | Über Schwachstellen könnte der Dateiserver manipuliert werden und so unberechtigte Zu- griffe ermöglichen.                                                                           |
| G 0.22           | Manipulation von Informati- onen                      | I              | Durch Fehler in den Berechtigungen o.ä. könnten Nutzer wesentliche Informationen manipulieren.                                                                                       |
| G 0.23           | Unbefugtes Eindringen in IT-Systeme                   | C, I           | Jemand könnte sich unberechtigt Zugang zum Dateiserver über fremde Zugangsdaten ver- schaffen.                                                                                       |
| G 0.25           | Ausfall von Geräten oder Systemen                     | A              | Hardwarefehler, die zum Teil schon in der Produktion entstehen, können zum zeitweili- gen Ausfall des Dateiservers führen.                                                           |

<!-- page: 96 -->

| Ge- fähr- dung   | Titel                                           | Schutz- ziel   | Beispiel                                                                                                                                                                              |
|------------------|-------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.26           | Fehlfunktion von Geräten o- der Systemen        | C, I, A        | Unvorhergesehene Konflikte in den Konfigu- rationseinstellungen mit anderen IT-Systemen könnten zu einem Ausfall führen.                                                              |
| G 0.27           | Ressourcen- mangel                              | A              | Es kommt zu Verzögerungen und Ausfällen bei Zugriffen auf den Dateiserver, weil dieser nicht mit ausreichen Kapazitäten versorgt ist.                                                 |
| G 0.28           | Software- Schwachstellen oder -Fehler           | C, I, A        | Der Dateiserver könnte z.T. unbekannte Si- cherheitslücken beinhalten, die die Verletzun- gen der Sicherheitsziele ermöglichen.                                                       |
| G 0.30           | Unberechtigte Nutzung von Geräten und Systemen  | C, I, A        | Unberechtigte Personen könnten Zugriff auf Administrationskonten erhalten und auf die- sem Wege Zugriffe auf den Dateiserver unter- binden oder Daten entwenden.                      |
| G 0.31           | Fehlerhafte Nutzung von Geräten und Systemen    | C, I, A        | Durch berechtigte Nutzer und Administrato- ren könnte der Dateiserver so verändert wer- den, dass es zu einem Ausfall kommt oder das Daten falsch preisgegeben bzw. verändert werden. |
| G 0.32           | Missbrauch von Berechti- gungen                 | C, I, A        | Unberechtigt zugeteilte Berechtigungen könn- ten von den jeweiligen Mitarbeitern verwendet werden, um nicht für Sie bestimmte Daten zu verwenden.                                     |
| G 0.39           | Schadpro- gramme                                | C, I, A        | Eine Infektion des Dateiservers mit einem Schadprogramm könnte die Sicherstellung der Sicherheitsziele gefährden.                                                                     |
| G 0.40           | Verhinderung von Diensten (Denial of Ser- vice) | A              | Der Dateiserver könnte durch eine Vielzahl von missbräuchlich veranlassten Anfragen keine Zugriffe mehr verarbeiten und nicht mehr zur Verfügung stehen.                              |
| G 0.43           | Einspielen von Nachrichten                      | C, I           | Ein Angreifer könnte die Netzwerkverbindun- gen des Dateiservers nutzen, um dort vorlie- gende Daten zu lesen, zu verändern oder un- brauchbar zu machen.                             |
| G 0.44           | Unbefugtes Eindringen in Räumlichkei- ten       | C, I, A        | Unberechtigte Personen könnten zu dem Standort des Servers vordringen                                                                                                                 |

<!-- page: 97 -->

Tabelle 4.39: Elementare Gefährdungen für den Dateiserver

| Ge- fähr- dung   | Titel                                                  | Schutz- ziel   | Beispiel                                                                                                                          |
|------------------|--------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| G 0.45           | Datenverlust                                           | A              | Durch einen Serverausfall und invalide Daten- sicherungen könnten Daten unwiederbringli- chen verloren gehen.                     |
| G 0.46           | Integritätsver- lust schützens- werter Infor- mationen | I              | Falsche Konfigurationen seitens des Dateiser- vers könnten einem Angreifer ermöglichen di- verse Daten unberechtigt zu verändern. |

## 4.4.2.2 Risikobewertung

Um eine umfassende Betrachtung zu gewährleisten, müssen die festgestellten elementaren Gefährdungen nun in einen Kontext mit den tatsächlichen Risiken gesetzt werden, die von diesen ausgehen. Dazu wird für jede Gefährdung die Eintrittshäufigkeit und die Schadensauswirkung geschätzt [65, S. 26-27]. Grundlage dafür sind die oben angeführten Kategorien.

| Ge- fähr- dung   | Titel                                                   | Schutz- ziel   | Eintritts- häufig- keit   | Auswir- kungen              | Risiko- katego- rie   |
|------------------|---------------------------------------------------------|----------------|---------------------------|-----------------------------|-----------------------|
| G 0.14           | Ausspähen von Infor- mationen (Spionage)                | C              | Mittel                    | Begrenzt                    | Gering                |
| G 0.16           | Diebstahl von Gerä- ten, Datenträgern o- der Dokumenten | C, A           | Mittel bis häufig         | Beträchtlich                | Sehr Hoch             |
| G 0.18           | Fehlplanung oder feh- lende Anpassung                   | C, I, A        | Mittel                    | Begrenzt bis be- trächtlich | Hoch                  |
| G 0.19           | Offenlegung schüt- zenswerter Informati- onen           | C              | Selten                    | Begrenzt                    | Gering                |
| G 0.21           | Manipulation von Hard- oder Software                    | C, I, A        | Selten                    | Beträchtlich                | Mittel                |
| G 0.22           | Manipulation von In- formationen                        | I              | Selten                    | Begrenzt                    | Gering                |
| G 0.23           | Unbefugtes Eindrin- gen in IT-Systeme                   | C, I           | Selten                    | Beträchtlich                | Hoch                  |

<!-- page: 98 -->

Tabelle 4.40: Einschätzung der elementaren Gefährdungen für den Dateiserver

| Ge- fähr- dung   | Titel                                              | Schutz- ziel   | Eintritts- häufig- keit   | Auswir- kungen   | Risiko- katego- rie   |
|------------------|----------------------------------------------------|----------------|---------------------------|------------------|-----------------------|
| G 0.25           | Ausfall von Geräten oder Systemen                  | A              | Mittel                    | Beträchtlich     | Hoch                  |
| G 0.26           | Fehlfunktion von Ge- räten oder Systemen           | C, I, A        | Mittel                    | Beträchtlich     | Hoch                  |
| G 0.27           | Ressourcenmangel                                   | A              | Häufig                    | Beträchtlich     | Sehr Hoch             |
| G 0.28           | Software-Schachstel- len oder -Fehler              | C, I, A        | Selten                    | Beträchtlich     | Mittel                |
| G 0.30           | Unberechtigte Nut- zung von Geräten und Systemen   | C, I           | Selten                    | Beträchtlich     | Mittel                |
| G 0.31           | Fehlerhafte Nutzung von Geräten und Sys- temen     | C, I, A        | Häufig                    | Begrenzt         | Hoch                  |
| G 0.32           | Missbrauch von Be- rechtigungen                    | C, I           | Häufig                    | Begrenzt         | Hoch                  |
| G 0.39           | Schadprogramme                                     | C, I, A        | Mittel                    | Beträchtlich     | Sehr Hoch             |
| G 0.40           | Verhinderung von Diensten (Denial of Service)      | A              | Mittel                    | Beträchtlich     | Hoch                  |
| G 0.43           | Einspielen von Nach- richten                       | I              | Selten                    | Begrenzt         | Gering                |
| G 0.44           | Unbefugtes Eindrin- gen in Räumlichkeiten          | C, I           | Mittel                    | Begrenzt         | Gering                |
| G 0.45           | Datenverlust                                       | A              | Mittel                    | Beträchtlich     | Hoch                  |
| G 0.46           | Integritätsverlust schützenswerter In- formationen | I              | Selten                    | Begrenzt         | Gering                |

## 4.4.3 Risikobehandlung

Ausgehend von den Risiken, die von den elementaren Gefährdungen ausgehen, werden nun Anforderungen aus verschiedenen IT-Grundschutz-Bausteinen aufgeführt, die die jeweilige Gefährdung im Rahmen der Risikoreduktion verringern. Es wird vorwiegend das Schutzziel Verfügbarkeit abgesichert, da für dieses ein hoher Schutzbedarf vorliegt. Die weiteren Schutzziele Integrität und Vertraulichkeit werden aufgrund des normalen Schutzbedarfes nicht prioritär betrachtet.

<!-- page: 99 -->

Bei den Anforderungen werden in Tabelle 4.41 zur Übersichtlichkeit nur die zusätzlichen Anforderungen für den erhöhten Schutzbedarf genannt. Zusätzlich werden die Basis- und Standard-Anforderungen vorausgesetzt.

Grundsätzlich soll die die Akzeptanz eines Risiko soll nur bei einer geringen Einstufung stattfinden [65, S. 35]. Die ISLL-Bund hält in diesem Zusammenhang fest, dass ein Sicherheitsniveau angestrebt wird, in dem keine hohen Risiken akzeptiert werden [12, S. 6]. Dementsprechend sollten weiterführende Maßnahmen bei mittleren bis sehr hohen Risikostufen getroffen werden.

| Ge- fähr- dung   | Titel                                                   | Schutz- ziel   | Ri- siko   | Maßnahmen zur Risikobe- handlung                                                                                                                                                       |
|------------------|---------------------------------------------------------|----------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.14           | Ausspähen von Informationen (Spionage)                  | C              | Ge- ring   | Anforderungen der Bausteine OPR.2 und ORP.4, sowie: • ORP.4.A21 (Mehr-Faktor-Au- thentisierung) • ORP.2.A13 (Sicherheitsüber- prüfung) • ORP.5.A10 (Klassifizierung von Informationen) |
| G 0.16           | Diebstahl von Geräten, Daten- trägern oder Do- kumenten | C, A           | Sehr Hoch  | Anforderungen der Bausteine DER.1, OPS.1.2.3, INF.1, INF.2 sowie: • CON.1.A10 (Entwicklung ei- nes Kryptokonzepts) • INF.1.A22 (Sichere Türen und Fenster)                             |
| G 0.18           | Fehlplanung o- der fehlende An- passung                 | C, I, A        | Hoch       | Anforderungen der Bausteine OPS.1.1.2, OPS.1.1.3, OPS.1.1.6, DER.1 sowie: • DER.1.A16 (Einsatz von De- tektionssystemen nach Schutzbedarfsanforderungen)                               |
| G 0.19           | Offenlegung schützenswerter Informationen               | C              | Ge- ring   | Anforderungen der Bausteine ORP.1, ORP.3 sowie: • ORP.5.A10 (Klassifizierung von Informationen)                                                                                        |

<!-- page: 100 -->

| Ge- fähr- dung   | Titel                                    | Schutz- ziel   | Ri- siko   | Maßnahmen zur Risikobe- handlung                                                                                                                       |
|------------------|------------------------------------------|----------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  |                                          |                |            | • CON.6.A9 (Auswahl geeigne- ter Verfahren zur Löschung oder Vernichtung von Daten- trägern bei erhöhtem Schutz- bedarf)                               |
| G 0.21           | Manipulation von Hard- oder Software     | C, I, A        | Mittel     | Anforderungen der Bausteine OPS.1.1.2, OPS.1.1.3, OPS.1.16 sowie: • CON.1.A16 (Physische Absi- cherung von Kryptomodulen)                              |
| G 0.22           | Manipulation von Informatio- nen         | I              | Ge- ring   | Anforderungen der Bausteine ORP.4., OPS.1.1.2, OPS.1.1.6, SYS.1.1, APP.3.3.                                                                            |
| G 0.23           | Unbefugtes Ein- dringen in IT- Systeme   | C, I           | Hoch       | Anforderungen der Bausteine ORP.4, OPS.1.2.4, DER.1, DER.2.1 sowie: • ORP.4.A21 (Mehr-Faktor-Au- thentisierung)                                        |
| G 0.25           | Ausfall von Ge- räten oder Syste- men    | A              | Hoch       | Anwendung der Standard-Maß- nahmen und Akzeptanz des Rest- risikos)                                                                                    |
| G 0.26           | Fehlfunktion von Geräten o- der Systemen | C, I, A        | Hoch       | Anforderungen des Bausteins OPS.1.1.2, OPS.1.1.3, OPS.1.1.5, DER.1, DER.2.1, DER.2.3 sowie: • CON.1.A14 (Schulung von Benutzern und Administrato- ren) |
| G 0.27           | Ressourcenman- gel                       | A              | Sehr Hoch  | Anforderungen der Bausteine OPS.1.1.2, SYS.1.1, APP.3.3 so- wie: • CON.5.A13 (Entwicklung ei- nes Redundanzkonzeptes für Anwendungen)                  |
| G 0.28           | Software- Schachstellen oder -Fehler     | C, I, A        | Mittel     | Anforderungen der Bausteine OPS.1.1.2, OPS.1.1.3, OPS.1.1.5, DER.1, DER.2.1, DER.2.3, APP.3.3.                                                         |

<!-- page: 101 -->

| Ge- fähr- dung   | Titel                                              | Schutz- ziel   | Ri- siko   | Maßnahmen zur Risikobe- handlung                                                                                                                                                                                                        |
|------------------|----------------------------------------------------|----------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.30           | Unberechtigte Nutzung von Geräten und Sys- temen   | C, I           | Mittel     | Anforderungen der Bausteine OPR.4, OPS.1.1.2, DER.1 sowie: • ORP.4.A21 (Mehr-Faktor-Au- thentisierung)                                                                                                                                  |
| G 0.31           | Fehlerhafte Nut- zung von Gerä- ten und Syste- men | C, I, A        | Hoch       | Anforderungen der Bausteine ORP.2, OPS.1.1.2 sowie: • OPS.1.1.2.A17 (IT-Administ- ration im Vier-Augen-Prinzip)                                                                                                                         |
| G 0.32           | Missbrauch von Berechtigungen                      | C, I           | Hoch       | Anforderungen der Bausteine ORP.2, ORP.4, OPS.1.1.2 sowie: • ORP.5.A10 (Klassifizierung von Informationen) • OPS.1.1.2.A14 (Sicherheits- überprüfung von Administra- toren) • OPS.1.1.2.A17 (IT-Administ- ration im Vier-Augen-Prinzip) |
| G 0.39           | Schadpro- gramme                                   | C, I, A        | Sehr Hoch  | Anforderungen der Bausteine OPS.1.1.4, DER.1, DER.2.1, DER.2.3 sowie: • ORP.3.A9 (Spezielle Schulung von exponierten Personen und Institutionen) • DER.1.A16 (Einsatz von De- tektionssystemen nach Schutzbedarfsanforderungen)         |
| G 0.40           | Verhinderung von Diensten (Denial of Ser- vice)    | A              | Hoch       | Anforderungen der Bausteine CON.5, DER.1, DER.2.1, SYS.1.1, APP3.3 sowie: • CON.5.A13 (Entwicklung ei- nes Redundanzkonzeptes für Anwendungen)                                                                                          |
| G 0.43           | Einspielen von Nachrichten                         | I              | Ge- ring   | Anforderungen der Bausteine CON.1, OPS.1.1.5, SYS.1.1, APP.3.3, INF.4 sowie: • CON.1.A10 (Entwicklung ei- nes Kryptokonzepts)                                                                                                           |

<!-- page: 102 -->

Tabelle 4.41: Risikobehandlung der Gefährdungen des Dateiservers

| Ge- fähr- dung   | Titel                                            | Schutz- ziel   | Ri- siko   | Maßnahmen zur Risikobe- handlung                                                                                                                                                                           |
|------------------|--------------------------------------------------|----------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.44           | Unbefugtes Ein- dringen in Räumlichkeiten        | C, I           | Ge- ring   | Anforderungen der Bausteine INF.1, INF.2 sowie: • INF.2.A24 (Einsatz von Vi- deoüberwachungsanlagen)                                                                                                       |
| G 0.45           | Datenverlust                                     | A              | Hoch       | Anforderungen der Bausteine CON.3, CON.5, OPS.1.1.6, DER.2.1, DER.4 sowie: • CON.1.A14 (Schulung von Benutzern und Administrato- ren) • CON.5.A13 (Entwicklung ei- nes Redundanzkonzeptes für Anwendungen) |
| G 0.46           | Integritätsverlust schützenswerter Informationen | I              | Ge- ring   | Anforderungen der Bausteine CON.1, OPS.1.1.5, SYS.1.1, APP.3.3.                                                                                                                                            |

## 4.5 Zusammenfassung des IT-Grundschutz-Profils

Aus den vier Unterkapiteln ergeben sich folgende Informationen für das IT-Grundschutz-Profil einer obersten Landesbehörde:

- Der abgegrenzte Informationsverbund und der betrachtete Geschäftsprozess.
- Die Referenzarchitektur und Zielobjekte, die verwendet werden.
- Die Sicherheitsanforderungen der Sicherheitskonzeption für die Geschäftsprozess der Beteiligung an der Normsetzung des Landes.
- Die Schutzbedarfskategorien sowie Schutzbedarfe der Zielobjekte.
- Die Risikokategorien und eine Risikoanalyse des Dateiservers.

Das IT-Grundschutz-Profil wird als Gesamtdokument aus diesen Informationen gebildet. Das Gesamtdokument wird dazu in folgende Kapitel untergliedert:

1. Management Summary
2. Geltungsbereich
3. Betrachteter Informationsverbund
4. Referenzarchitektur
5. Modellierung des Informationsverbunds

<!-- page: 103 -->

6. Schutzbedarfe
7. Risikobetrachtung
8. Anwendungshinweise
9. Literatur

Die Inhalte dieser 9 Kapitel bestehen aus den hier dargestellten und hergeleiteten Informationen. Das Gesamtdokument des IT-Grundschutz-Profils für oberste Landesbehörden ist in seiner vollständigen Form in Anhang C abgebildet. Einige Inhalte sind dort für eine besser lesbare Form komprimiert dargestellt und, wo erforderlich, umformuliert.

<!-- page: 104 -->

## Kapitel 5 Überprüfung des Forschungsgegenstands

Mit der Erstellung des IT-Grundschutz-Profils ist der methodische 'build' -Anteil nach March und Smith abgeschlossen. Zusätzlich muss das Artefakt gemäß den Anforderungen aus der Design Science Forschung, hier repräsentiert durch Prat, Comyn-Wattiau und Akoka [98, S. 2] sowie Ahmed und Sundaram [99, S. 1-2], evaluiert werden.

Das erste Unterkapitel befasst sich zunächst mit den Methoden zur Evaluation eines Artefakts. Das zweite Unterkapitel befasst sich mit der Konzeption und Durchführung der Experteninterviews, die als geeignetste Methode für die Evaluation angesehen werden. Im dritten Unterkapitel werden die Ergebnisse der Experteninterviews dargestellt.  Zuletzt  wird  im  vierten  Unterkapitel  als  weitere Evaluationsdimension  auf  die Anforderungen der Befragung eingegangen und die Gesamtergebnisse der Evaluation werden zusammengefasst.

## 5.1 Vorgehen in der Evaluation

In der Design Science wird durch mehrere Autoren gefordert, dass eine Evaluierung  der  erstellten  Artefakte  durchzuführen  ist.  Während  beispielsweise  March  und Smith vorgeben, dass eine Evaluation nötig ist [18, S. 254], bleibt offen, welche Methodiken dafür zur Verfügung stehen. Unabhängig der Methodik fordern diese zu der Evaluation eines Modells folgendes:

'Models are evaluated in terms of their fidelity with real world phenomena, completeness, level of detail, robustness, and internal consistency.' [18, S. 261]

Einschlägige  Methoden  für  die  Evaluation  von  IT-Artefakten  werden  von  Hevner, March, Park und Ram vorgeschlagen [19, S. 86]:

- Beobachtung
- a. Eine Fallstudie, die das Artefakt im Unternehmensumfeld betrachtet.
- b. Eine Feldstudie des Artefakts in der Anwendung bei mehreren Projekten.
- Analyse
- a. Die Überprüfung der statischen Eigenschaften des Artefakts.
- b. Die Überprüfung der dynamischen Eigenschaften des Artefakts.
- c. Die Betrachtung des Artefakts im Kontext der technischen Architektur.
- d. Die Darstellung der optimalen Attribute des Artefakts.
- Experiment
- a. Die Untersuchung des Artefakts in einem kontrollierten Umfeld.

<!-- page: 105 -->

- b. Die Umsetzung des Artefakts mit Testdaten.
- Test
- a. Testen des Artefakts auf funktionale Weise, sodass das Ergebnis auf Fehler überprüft wird.
- b. Strukturelles Testen des Artefakts, indem ein Teil des Artefakts implementiert und überprüft wird.
- Deskriptiv
- a. Durchführung einer überzeugenden Argumentation auf der Basis von Literatur und logischen Argumenten.
- b. Szenarien-basierte Beschreibung des Artefakts, um den Anwendungsfall darzustellen.

Einige Methodiken sind aufgrund ihrer Art und ihres Umfangs nicht für die Überprüfung des hiesigen Artefakts geeignet. So lässt sich beispielsweise ein ISMS als organisationsumfassendes Regelungsmodell nicht in dem zeitlichen Umfang einer Masterarbeit in einer Feldstudie evaluieren.

Folgende  Evaluations-Methoden  werden  als  anwendbar  auf  dieses  IT-Grundschutz-Profil angesehen:

- Analyse des Artefakts hinsichtlich der vier oben aufgeführten Qualitäten.
- Simulation des Artefakts als Experiment.
- Strukturelle Tests des Artefakts.
- Argumentative und Szenarien-basierte Deskription.

Als strategisch orientiertes Artefakt wird die Analyse des Artefakts als Evaluationsmethodik ausgewählt. Während Hevner, March, Park und Ram die Analyse der Architektur für Informationssysteme vorgesehen haben, wird dieser Analyseansatz in abgewandelter Form auf die Architektur des IT-Grundschutz-Profils und dessen Anwendbarkeit auf eine oberste Landesbehörde angewendet.

Eine Evaluation kann unterschiedliche Kriterien umfassen, die von Prat, Comyn-Wattiau und Akoka zusammengefasst werden [98, S. 6]. Die in Abbildung 5.1 dargestellten Evaluationskriterien decken sich mit den oben genannten Evaluationskriterien für Modelle von Hevner und March, sind aber von größerem Umfang und Granularität.

<!-- page: 106 -->

Abbildung 5.1: Die hierarchischen Evaluationskriterien nach Prat, Comyn-Wattiau und Akoka [98, S. 6] (Reproduktion)

<!-- image -->

<!-- page: 107 -->

Die  Architekturanalyse  wird  in  Form  von  Experteninterviews  durchgeführt.  Es wird auf etabliertes Wissen der ISB der obersten Landesbehörden zurückgegriffen, um die Annahmen des IT-Grundschutz-Profils mit den Gegebenheiten der obersten Landesbehörden abzugleichen und Übereinstimmungen oder Widersprüche festzustellen.

Eine persönliche Befragung von Experten ermöglicht, dass Fragen bei Missverständnissen konkretisiert und verbindliche Aussagen erreicht werden können. Zudem werden, anders als in der schriftlichen Befragung, die Experteninterviews auf der Ebene der ISB der obersten Landesbehörden stattfinden. So wird aus dem betrachteten Behördentypus Wissen erhoben und die Infrastruktur abgefragt.

Werden die oben eingeführten Kriterien betrachtet, werde folgende in den Experteninterviews berücksichtigt:

- In Hinsicht des Ziels soll die Validität und Allgemeingültigkeit des Artefakts für den hiesigen Anwendungsbereich überprüft werden.
- In Bezug auf die organisationale Umgebung wird die Anpassung an die Organisation betrachtet.

Insgesamt  werden  mit  den  Experteninterviews  drei  Evaluationskriterien  überprüft. Eine Evaluation aller Kriterien mithilfe von Experteninterviews scheint indes nicht umsetzbar. Ein Experte oder eine Expertin könnte nicht in einem angemessenen Zeitrahmen für eine ausführliche Betrachtung jedes Kriteriums befragt werden. Es ist zudem anzunehmen, dass bei anderen Methoden wie Experimenten oder Simulationen ebenfalls nicht alle Evaluationskriterien überprüft werden können.

Diese Eingrenzung scheint auch in anderen Forschungsprojekten vorzuliegen. Prat, Comyn-Wattiau und Akoka haben in ihrer Ausarbeitung zu den Evaluationskriterien in der Auswertung mehrerer wissenschaftlicher Beiträge festgestellt, dass nur ein Bruchteil aller vorgeschlagenen Kriterien evaluiert wird [98, S. 9-10].

## 5.2 Konzeption der Experteninterviews

Von der methodischen Erläuterung ausgehend, werden folgende Ziele durch die Evaluation verfolgt:

- Überprüfung  der  Annahmen  des  IT-Grundschutz-Profils  in  Bezug  auf  die Struktur der obersten Landesbehörden.
- Überprüfung, ob die Gemeinsamkeiten der obersten Landesbehörden angemessen erfasst sind.
- Darstellung, ob existierende oberste Landesbehörden in einem Vergleich mit dem IT-Grundschutz-Profil realistisch dargestellt sind.

Um diese Ziele mit den evaluierenden Experteninterviews zu erreichen, werden diese auf  der  Basis  einschlägiger  Fachliteratur  vorbereitet  und  durchgeführt.  Nach  einer schriftlichen Anfrage stehen für die Experteninterview die ISB zweier oberster Landesbehörden unterschiedlicher Landesverwaltungen zur Verfügung.

<!-- page: 108 -->

Für die Vorbereitung der Interviews wird zunächst nach der Anleitung von Kaiser aus dem Bereich der Politikwissenschaft ein Interviewleitfaden erstellt. Ein Interviewleitfaden erfüllt drei Funktionen [83, S. 52-55]:

1. Die Strukturierung des Interviews hinsichtlich der zu stellenden Fragen, der Reihenfolge der Fragen und der Nachvollziehbarkeit für den Interviewten.
2. Es sollen für den Gesprächspartner Hintergrundinformationen und weitere  Rahmenbedingungen  wie  Anonymisierungsmöglichkeiten  bekannt sein.
3. Zuletzt soll für den Gesprächspartner ersichtlich werden, dass der Interviewende ein fachlich angemessener Ansprechpartner ist.

Da das Gesamtdokument des IT-Grundschutz-Profils einen Umfang von mehr als 30 Seiten hat, werden in dem Interview bevorzugt Fragen gestellt, die die Grundannahmen überprüfen. Soweit möglich wird auf die repetitive Abfrage von Zielobjekten und ITGrundschutz-Bausteinen verzichtet. In geringem Umfang werden dennoch ausgewählte Zielobjekte aus allen Objektgruppen abgefragt.

Es ist folgender Interviewablauf vorgesehen:

1. Begrüßung  und  Vorstellung  des  Interviewers,  der  Masterarbeit,  des  Interviewzwecks und der Interviewstruktur.
2. Fragen zur Person, mit Einholung des Einverständnisses zu dem Interview, der akustischen Dokumentation des Interviews und der anonymisierten Veröffentlichungen, persönliche Daten des Befragten, berufliche Laufbahn und aktuelle Tätigkeit.
3. Fragen zur Behörde, in der der Experte als ISB tätig ist oder war. Es wird insbesondere auf die ISMS-Methodik, die Organisation des ISMS sowie den Umfang des ISMS eingegangen.
4. Fragen zum IT-Grundschutz Profil unter Einbeziehung des Geschäftsprozesses der Beteiligung an der Normsetzung, den allgemeinen Zielobjekten zur Bewältigung des Prozesses, den Schutzbedarfen von ausgewählten Zielobjekten, der Art der Risikobetrachtung in der Behörde und der Wahrnehmung des Outsourcings.
5. Zuletzt die Möglichkeit für weitere Bemerkungen.

Um den Experten die Möglichkeit zu geben, sich auf organisationsspezifische Fragen vorzubereiten, werden auszugsweise Fragen aus dem Interviewleitfaden übersendet. Für einen Gesprächsumfang von einer Stunde sind dazu folgende Fragen vorgesehen:

- Welche Geschäftsprozesse und Anwendungen werden von dem ISMS Ihrer Behörde umfasst?
- Wie weit ist das ISMS in der Behörde umgesetzt?
- Ist eine externe Auditierung / Zertifizierung des ISMS vorgesehen?

<!-- page: 109 -->

- Gibt es Geschäftsprozesse oder Infrastrukturanteile, welche üblicherweise an externe Dienstleister ausgelagert werden? Wenn ja, welche?
- Umfasst die Tätigkeit Ihrer Behörde auch die Beteiligung an der Normsetzung des Landes, beispielsweise durch die Mitarbeit an Gesetzen und Verordnungen?
- Welche  Anwendungen  und  IT-Systeme  werden  für  die  Beteiligung  an  der Normsetzung des Landes Ihrer Meinung nach  in  einer  obersten  Landesbehörde üblicherweise benötigt?
- Können Sie die Nutzung folgender Zielobjekte zu diesem Geschäftsprozess bestätigen oder ablehnen?
- o Betriebssystem Windows 10
- o Dateiserver
- o Active Directory
- o Microsoft Exchange
- o Windows Server 2016
- o Gebäudeverkabelung
- o Firewall
- o Signatur-Dienst
- o Serverraum
- Hat Ihre Behörde eine Schutzbedarfsfeststellung nach dem IT-Grundschutz oder Vergleichbares im Rahmen der Umsetzung des ISMS durchgeführt?
- Wie wurden die Schutzbedarfskategorien definiert?
- Wie hoch würden Sie den Schutzbedarf bezüglich Vertraulichkeit, Integrität und Verfügbarkeit für den Geschäftsprozess der Beteiligung an der Normsetzung des Landes einschätzen?
- Wie schätzen Sie in Bezug auf die Beteiligung an der Normsetzung des Landes den Schutzbedarf hinsichtlich Vertraulichkeit, Integrität und Verfügbarkeit folgender Zielobjekte:
- o Betriebssystem Windows 10
- o Dateiserver
- o Active Directory
- o Microsoft Exchange
- o Windows Server 2016
- o Gebäudeverkabelung
- o Firewall

<!-- page: 110 -->

- o Signatur-Dienst
- o Serverraum
- Wurden diese Zielobjekte durch Ihre Behörde im Rahmen des ISMS betrachtet? Wenn ja, welche Schutzbedarfe wurden festgestellt?
- Wie schätzen Sie den Risikoappetit Ihrer Behörde bzw. einer obersten Landesbehörde ein?
- Welche Gründe können Sie für eine erhöhte oder eine niedrige Risikobereitschaft identifizieren?
- Wie sind die Risikoeintrittswahrscheinlichkeiten und  -auswirkungen in Ihrer betrachteten Behörde operationalisiert?

Dazu werden zusätzliche Fragen behandelt, die aufgrund einer Betrachtung des Erfahrungswissens der Experten nicht vorab zu Verfügung gestellt werden:

- Sind Sie mit der akustischen Aufnahme und anschließenden Verschriftung dieses Interviews einverstanden?
- Sind Sie einverstanden, dass das Interview in anonymisierter Form in der Masterarbeit veröffentlicht wird?
- Bitte nennen Sie ihren höchsten akademischen Bildungsabschluss.
- Bitte stellen Sie Ihre bisherigen Tätigkeiten seit dem Abschluss Ihrer akademischen Laufbahn dar.
- Was ist Ihre aktuelle Funktion in ihrer Behörde?
- Welche Methodik zu der Umsetzung eines ISMS wendet Ihre Behörde an?
- Wird in den anderen obersten Landesbehörden Ihrer Landesverwaltung die gleiche Methodik angewandt?
- Wo ist der oder die Informationssicherheitsbeauftragte in Ihrer Behörde angesiedelt?
- Wie viele Personen sind direkt mit der Aufgabe des Informationssicherheitsmanagements betraut?
- Wer zählt zu dem erweiterten Kreis der Beteiligten im Zusammenhang mit dem ISMS?
- Welche Geschäftsprozesse und Anwendungen werden von dem ISMS Ihrer Behörde umfasst?
- Welche weiteren generischen Geschäftsprozesse könnten Sie für eine oberste Landesbehörde, unabhängig des Ressorts, formulieren?
- Wenn ja, welches waren Schutzbedarfe?

<!-- page: 111 -->

Insgesamt handelt es sich um 28 Fragen, die im Rahmen des Experteninterviews erfasst werden.  Davon  sind  5  Fragen  von  biografischer  Natur,  um  die  Expertise  des  Gesprächspartners festzustellen. Die weiteren Fragen befassen sich mit dem ISMS der jeweiligen Behörde und mit den Erfahrungen der Experten als ISB.

## 5.3 Durchführung der Experteninterviews

Das  Ziel  der  Evaluation  ist  die  Feststellung  der  Anwendbarkeit  des  IT-Grundschutz-Profils auf die Sicherheitskonzeption einer obersten Landesbehörde. Um diese zu prüfen, bieten sich unterschiedliche Fragen an, die in dem Experteninterview gestellt werden. Die konkreten Fragen sind für diese Interviews im Unterkapitel 5.2 aufgelistet, werden im Gespräch zum Teil aber nicht zwangsweise in diesem Wortlaut gestellt.

Die erste befragte Person ist derzeit als ISB für eine oberste Landesbehörde tätig. Die zweite Person war ISB einer obersten Landesbehörde, ist nun allerdings in das organisatorische ISM der Landesverwaltung gewechselt. Für das Interview werden beide Personen durch den Verfasser dieser Masterarbeit aufgesucht und im März und April 2019 persönlich befragt.

Die Interviews werden im Dialog geführt und akustisch aufgezeichnet. Anschließend wird eine Transkription der Aufzeichnungen durchgeführt, die auf Wunsch der Interviewpartner anonymisiert ist. Aus der Transkription ergibt sich so weder die Behörde noch der Interviewpartner. Zudem sind die Transkripte im Nachhinein den jeweiligen Behörden vorgelegt und von diesen freigegeben worden. Die anonymisierten Transkripte befinden sich im Anhang C dieser Masterarbeit.

Aus den Interviews lassen sich folgende Feststellungen für Validität der Annahmen des IT-Grundschutz-Profils und für dessen Anwendbarkeit treffen:

- Beide Gesprächspartner haben die Anwendung des generischen Geschäftsprozesses der Beteiligung an der Normsetzung bestätigt.
- Ebenso sind Teile  der  IT-Infrastruktur  an  externe  Dienstleister  ausgelagert, wobei der konkrete Grad der Auslagerung nicht benannt werden konnte.
- Zur Wahrnehmung des Geschäftsprozesses nennen die Gesprächsteilnehmer allgemeine Büroanwendungen wie Word und Excel sowie als darunter liegende IT-Systeme den allgemeinen Server, Clients und das Windows Betriebssystem.
- Die Auswahl der 9 Zielobjekte wird durch beide Gesprächspartner bestätigt. Selbiges gilt für die Auswahl der Produkte des Herstellers Microsoft bei einem Anteil dieser Zielobjekte.
- Der Schutzbedarf der abgefragten Zielobjekte wird von einem Experten bestätigt. Die interviewte Expertin hat aufgrund der Sicherheitsrelevanz der Angaben  nur  den  Schutzbedarf  des  Geschäftsprozesses  und  nicht  der  einzelnen Zielobjekte eingeschätzt. Für diesen nimmt sie einen normalen Schutzbedarf bezüglich der drei Schutzziele Vertraulichkeit, Integrität und Verfügbarkeit an.

<!-- page: 112 -->

Die Schutzbedarfe der einzelnen Zielobjekte und des Geschäftsprozesses decken sich mit den Annahmen des IT-Grundschutz-Profils.

## 5.4 Anforderungen aus der Befragung

Neben der formellen Evaluation durch die Experteninterviews ist im Kontext der vorliegenden Arbeit eine weitere Evaluationsdimension aufgetreten, über die die methodische  wie  fachliche  Vollständigkeit  betrachtet  werden  kann.  So  sind  durch  die schriftliche Befragung der ISB spezifische Anforderungen festgestellt worden, deren Berücksichtigung im IT-Grundschutz-Profil nun geprüft wird.

Die in Kapitel 3.2 durchgeführte Befragung hat eine Wissensbasis geschaffen, die der Erstellung des IT-Grundschutz-Profils dient. Nach der Erstellung des Artefakts ist nun nachzuvollziehen, ob diese spezifischen Anforderungen im IT-Grundschutz-Profil tatsächlich berücksichtigt sind.

| Anforderung                                                                                                                                                                                                                                  | Berücksichti- gung                                                                   | Begründung                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Die größten Hürden für die Umsetzung eines ISMS in ei- ner obersten Landesbehörde liegen für die Teilnehmer im Bereich der Ressourcenbereit- stellung und ein geringer Stel- lenwert von Informationssi- cherheit für die Behördenlei- tung. | Anwendung der Anforderung ISMS.1.A4 im IT- Grundschutz- Profil.                      | Die Anforderung A4 fordert verpflichtend von der Lei- tungsebene, dass der ISB mit ausreichend Ressourcen aus- zustatten ist. Wenn ein geringer Stellenwert für das ISM bei der Leitungs- ebene vorliegt, lässt sich dieser nicht mit Hilfe von ver- pflichtenden Maßnahmen her- |
| Generisch betrachtet können die Geschäftsprozesse Ge- setzgebungsverfahren • Rechtssetzungsverfah- ren • Daseinsvorsorge und • die Aufrechterhaltung des Verwaltungsbetrie- bes in einer obersten Landesbe- hörde vorhanden sein.            | Absicherung des Geschäftsprozes- ses der Beteiligung an der Normsetzung des Landes . | stellen. Einer der genannten Ge- schäftsprozesse wird explizit im IT-Grundschutz-Profil ab- gesichert. Die weiteren Nen- nungen sind aufgrund des Umfangs der Masterarbeit nicht betrachtet.                                                                                     |
| Die obersten Landesbehör- den bzw. Landesverwaltun- gen nutzen externe Dienst- leister für ihre Infrastruktur                                                                                                                                | Auswahl des Bau- steins OPS.2.1 (Outsourcing für Kunden)                             | Das IT-Grundschutz-Profil betrachtet den Informations- verbund bewusst ohne die Einbeziehung der Auslage- rung aufgrund unterschiedli- cher Auslagerungsmodelle.                                                                                                                 |

<!-- page: 113 -->

Tabelle 5.1: Gegenüberstellung der besonderen Anforderungen und der Berücksichtigung im IT-Grundschutz-Profil

| Anforderung                                                                                                                                                                                                                                | Berücksichti- gung                                                                                    | Begründung                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                            |                                                                                                       | Um einer möglichen Auslage- rung Rechnung zu tragen, wird der Baustein OPS.2.1 in der Sicherheitskonzeption ver- wendet.                                                     |
| An Anwendungen könnten Verzeichnisdienste, zentrale Anmelde- und Identifizie- rungsdienste sowie zentral ge- führte Register vorhanden sein. Diese Anwendungen unterliegen laut der befragten Person einem besonders ho- hem Schutzbedarf. | Absicherung des Zielobjektes Ac- tive Directory                                                       | Die Anwendung Active Di- rectory umfasst die genannten Funktionen. Zudem ist das Zielobjekt mit dem Schutzbe- darf ' hoch ' in Bezug zu den drei Schutzzielen identifiziert. |
| Während den Landesverwal- tungen unterschiedliche Pro- dukte zur Aufgabenerfüllung zur Verfügung stehen, schei- nen Produkte des Herstellers Microsoft bevorzugt zu wer- den.                                                              | Verwendung der Zielobjekte Windows 10, Windows Server 2016, Microsoft Office 2016, Ac- tive Directory | Bei der Auswahl der Zielob- jekte sind in Abwägungssitua- tionen Produkte des Herstel- lers Microsoft bevorzugt und über entsprechende Bausteine modelliert.                 |

Die festgestellten besonderen Anforderungen werden, soweit möglich, berücksichtigt. Weitere Anforderungen und Anmerkungen wurden im Erstellungsprozess durch die beteiligten Ansprechpartner ergänzt, welche mit entsprechender Quellenangabe als zusätzliche Anforderung in der Sicherheitskonzeption enthalten sind.

## 5.5 Ergebnis der Evaluation

Es bleibt festzuhalten, dass die Evaluation auf Basis der Experteninterviews die Annahmen des IT-Grundschutz-Profils für die Beteiligung an der Normsetzung des Landes bestätigt hat. Während die Vollständigkeit der angenommenen Zielobjekte nicht über eine ausführliche Abfrage im Experteninterview evaluiert wird, sind stattdessen ausgewählte Zielobjekte und deren Schutzbedarf geprüft worden. Es konnten keine Widersprüche festgestellt werden. Eine Gegenüberstellung der Anforderungen aus der Befragung ergibt, dass die dortigen Anmerkungen weitestgehend im IT-Grundschutz-Profil aufgenommen wurden.

Diese Feststellungen dienen der Bestätigung des IT-Grundschutz-Profils und der Grundannahmen. Eine induktive Anwendung der Erkenntnisse auf alle obersten Landesbehörden ist, ähnlich dem Fragebogen, nicht auf dieser Datenbasis möglich.

<!-- page: 114 -->

## Kapitel 6 Zusammenfassung

Im Folgenden werden die Ergebnisse der vorliegenden Arbeit und des daraus entstehenden Artefakts zusammengefasst. Es wird zunächst auf das Vorgehen zur Erstellung des  IT-Grundschutz-Profils  und dessen  Evaluation  eingegangen.  Anschließend  wird beschrieben, inwiefern das IT-Grundschutz-Profil veröffentlicht und weiterentwickelt werden kann.

## 6.1 Erstellungsprozess des IT-Grundschutz-Profils

Unter Anwendung der IT-Grundschutz-Methodik des BSI, des Fragebogens und der Literaturrecherche ist das IT-Grundschutz-Profil als Design Science Artefakt erstellt worden. Neben diesen Quellen wird im Kapitel 2 auf Maßnahmen zur Erhöhung der Netz- und Informationssicherheit in Europa und Deutschland, die Methodiken der ISO 2700x-Reihe sowie des IT-Grundschutz eingegangen. In Kapitel 3 sind die spezifischen Wissensanteile und deren Erhebung, die für die Erstellung des IT-Grundschutz-Profils genutzt sind, dargelegt. Das 4. Kapitel enthält die Konzeption des IT-Grundschutz-Profils, welches im 5. Kapitel erfolgreich evaluiert wird.

Das IT-Grundschutz-Profil betrachtet eine oberste Landesbehörde bei der Erfüllung des generischen Geschäftsprozesses der Beteiligung an der Normsetzung des Landes . Für diesen Geschäftsprozess ist eine Schablone der Sicherheitskonzeption entwickelt worden, die entsprechende Sicherheitsanforderungen zur Absicherung aufführt. Mithilfe dessen können die obersten Landesbehörden die Sicherheitskonzeption bezogen auf die Beteiligung an der Normsetzung des Landes vereinfacht umsetzen und so ihren Verpflichtungen nach der ISLL-Bund nachkommen.

Es ist hervorzuheben, dass, neben den Fragebögen, von Beginn der Masterarbeit an mit den Landesverwaltungen und obersten Landesbehörden kontinuierlich zu dem IT-Grundschutz-Profil kommuniziert wird. Dafür stehen insgesamt fünf Ansprechpartner verschiedener oberster Landesbehörden und Landesverwaltungen zur Verfügung. Zusätzlich ist das IT-Grundschutz-Profil ebenso dem BSI für eine fachliche Einsichtnahme und Kommentierung mehrfach übersandt und nach Kommentierungen verändert worden.

Das IT-Grundschutz-Profil ist neben den Darstellungen des Kapitels 4 in komprimierter Form in Anhang C dieser Masterarbeit zusammengefasst. Eine Evaluation ausgewählter  Anteile  des  IT-Grundschutz-Profils  führt  abschließend  zu  dem  Ergebnis, dass das Artefakt die Gegebenheiten in den obersten Landesbehörden, soweit in diesem Rahmen überprüfbar, berücksichtigt und darstellt.

Mit dem IT-Grundschutz-Profil und den darin enthaltenen Sicherheitsanforderungen  wird  zugleich  die  zentrale  Forschungsfrage  beantwortet.  Die  Leitfragen  werden durch die angewandten Forschungsmethoden der Befragung, Literaturrecherche und Experteninterviews sowie der kontinuierlichen Kommunikation mit Ansprechpartnern ebenfalls beantwortet. Unter anderem bildet dies einen Teil der Informationen ab, die die Grundlage für das IT-Grundschutz-Profil und damit für die Beantwortung der Forschungsfrage darstellen.

<!-- page: 115 -->

## 6.2 Veröffentlichung und Weiterführung

Mit dieser Masterarbeit endet die Bearbeitungsphase für das IT-Grundschutz-Profil. Dieses wird dem BSI zur Verfügung gestellt und nach einer Prüfung veröffentlicht. Dies erfüllt abschließend die Forderung der Kommunikation der Forschungsergebnisse von Peffers, Tuunanen, Rothenberger und Chatterjee, wie auch von Hevner, March, Park und Ram.

Die Einsichtnahme in das IT-Grundschutz-Profil ist durch die Veröffentlichung des BSI für jede oberste Landesbehörde möglich. Zukünftig können die obersten Landesbehörden in der Umsetzung neuer Sicherheitskonzeptionen diese Schablone entsprechend berücksichtigen und anwenden. Zudem können Behörden mit bestehenden Sicherheitskonzeptionen  das  IT-Grundschutz-Profil  als  Prüfungsmodell  verwenden, um die eigenen Feststellungen auf Vollständigkeit und Validität zu prüfen.

Für die kontinuierliche Pflege des IT-Grundschutz-Profils könnte, wie vom BSI in der Strukturvorgabe vorgesehen, ein Gremium der Landesverwaltungen die Verantwortung übernehmen und so für eine angemessene Aktualität sorgen. Erfahrungswerte aus der Anwendung des ISMS in einer obersten Landesbehörde und aus der Anwendung des IT-Grundschutz-Profils können so in eine Verbesserung des Artefakts einfließen.

<!-- page: 116 -->

## Literaturverzeichnis

- [1] T. Braun, 'Geschichte und Entwicklung des Internets', Informatik Spektrum , Jg. 33, Nr. 2, S. 201 - 207, 2010.
- [2] Eurostat, 'Digital economy and society statistics - households and individuals', Eurostat, Jun. 2018. [Online] Verfügbar unter: https://ec.europa.eu/eurostat/statstics-explained/index.php?title=Digital\_economy\_and\_society\_statistics-housholds\_and\_indivuduals&amp;oldid=496187. Zugriff am: 25. Februar 2019.
- [3] Eurostat, 'Enterprises with broadband access: % of enter prises with at least 10 persons employed in the given NACE sectors. NACE Rev 2 since 2009 (break in series in 2009)', Eurostat, Dez. 2018. [Online] Verfügbar unter: https://ec.europa.eu/eurostat/tgm/table.do?tab=table&amp;init=1&amp;plugin=1&amp;language=en&amp;pcode=tin00090. Zugriff am: 25. Februar 2019.
- [4] G. Berghaus, R. Kessler, V. Dmitriyev und J. M. Gómez, 'Ermittlung der Digitalisierungspotenziale von nicht-digitalen Geschäftsprozessen', HMD Praxis der Wirtschaftsinformatik , 2018.
- [5] B. W. Wirtz und P. Daiser, 'E - Government' in Handbuch Staat , R. Voigt, Hg., Wiesbaden: Springer Fachmedien Wiesbaden, 2018, S. 981 - 995.
- [6] M. Martini, 'Transformation der Verwaltung durch Digitalisierung', DÖV (Die Öffentliche Verwaltung) , Jg. 11, S. 443 - 455, 2017.
- [7] J. Stember, W. Eixelsberger und A. Spichiger, Wirkungen von E-Government: Impulse für eine wirkungsgesteuerte und technikinduzierte Verwaltungsreform . Wiesbaden: Springer Gabler, 2018.
- [8] B. Beckermann, 'E -Government-Gesetzgebung im Vergleich', Verwaltung &amp; Management , Jg. 24, Nr. 4, S. 167 - 176, 2018.
- [9] A. Asosheh, P. Hajinazari und H. Khodkari, 'A practical implementation of ISMS' in 2013 7th International Conference on e-Commerce in Developing Countries: with Focus on e-Security (ECDC): 17 - 18 April 2013, Kish Island, Iran , Kish Island, Iran, 2013, S. 1 - 17.
- [10]  D.- K. Kipker und D. Pfeil, 'IT - Sicherheitsgesetz in Theorie und Praxis', Datenschutz und Datensicherheit , Jg. 40, Nr. 12, S. 810 - 814, 2016.
- [11] J. K. Deane, D. M. Goldberg, T. R. Rakes und L. P. Rees, 'The effect of information security certification announcements on the market value of the firm', Information Technology and Management , Jg. 29, S. 157 - 172, 2019.
- [12] Leitlinie für die Informationssicherheit in der öffentlichen Verwaltung -2018 - , 2018.
- [13]  K. Möltgen-Sicking und T. Winter, Verwaltung und Verwaltungswissenschaft: Eine praxisorientierte Einführung . Wiesbaden: Springer VS, 2018.
- [14]  Bundesamt für Sicherheit in der Informationstechnik, IT-Grundschutz-Profile. [Online] Verfügbar unter: https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzProfile/itgrundschutzProfile.html. Zugriff am: 30. Januar 2019.

<!-- page: 117 -->

- [15]  Bundesamt für Sicherheit in der Informationstechnik, Kernpunkte der Modernisierung. [Online] Verfügbar unter: https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzAbout/IT-Grundschutz-Modernisierung/Kernpunkte/itgrundschutz\_Kernpunkte.html. Zugriff am: 30. Januar 2019.
- [16]  Bundesamt für Sicherheit in der In formationstechnik, 'IT -Grundschutz-Profile: - Strukturbeschreibung - ', Bundesamt für Sicherheit in der Informationstechnik (BSI), Bonn, Sep. 2018.
- [17] Bundesamt für Sicherheit in der Informationstechnik, 'Zuordnung ISO/IEC 27001 sowie ISO/IEC 27002 zum modernisierten ITGrundschutz', Bundesamt für Sicherheit in der Informationstechnik (BSI), Bonn, 2018.
- [18] S. T. March und G. F. Smith, 'Design and natural science research on information technology', Decision Support Systems , Jg. 15, Nr. 4, S. 251 - 266, 1995.
- [20] R. Baskerville, A. Baiyere, S. Gergor, A. Hevner und M. Rossi, 'Design Science Research Co ntributions: Finding a Balance between Artifact and Theory', JAIS , Jg. 19, Nr. 5, S. 358 - 376, 2018.
- [19] Alan R. Hevner, Salvatore T. March, Jinsoo Park und Sudha Ram, 'Design Science in Information Systems Research', MIS Quarterly , Nr. 28, S. 75 - 105, 2004.
- [21] K. Peffers, T. Tuunanen, M. A. Rothenberger und S. Chatterjee, 'A Design Science Research Methodology for Information Systems Research', Journal of Management Information Systems , Jg. 24, Nr. 3, S. 45 - 77, 2007.
- [22] R. Winter, 'Design science research in Europe', European Journal of Information Systems , Jg. 17, Nr. 5, S. 470 - 475, 2008.
- [23] ISO/IEC 27000:2018 , 2018.
- [24]  Bundesanzeiger Verlag GmbH; Deutschland, IT-Grundschutz-Kompendium: 2. Edition 2019 . Köln: Bundesanzeiger Verlag, 2019.
- [25]  M. Brenner et al., Praxisbuch ISO/IEC 27001: Management der Informationssicherheit und Vorbereitung auf die Zertifizierung, 2. Aufl. München: Hanser, 2017.
- [26] Guide 73 , 2009.
- [27] F. Rustmeyer, 'Der neue IT - Grundschutz in der Praxis', &lt;kes&gt; - Die Zeitschrift für Informations-Sicherheit , Jg. 3, S. 62 - 65, 2018.
- [28]  R.-D. Reineke und F. Bock, Gabler Lexikon Unternehmensberatung, 1. Aufl. Wiesbaden: Gabler Verlag / Springer Fachmedien Wiesbaden GmbH Wiesbaden, 2007.
- [29]  R. Heuermann, M. Tomenendal und C. Bressem, Hg., Digitalisierung in Bund, Ländern und Gemeinden: IT-Organisation, Management und Empfehlungen . Berlin, Germany: Springer Gabler, 2018.
- [30]  B. W. Wirtz u nd J. C. Weyerer, 'Cyberangriffe und Datensicherheit in öffentlichen Netzwerken und Dateninfrastrukturen in Deutschland', Verwaltung &amp; Management , Jg. 23, Nr. 3, S. 154 - 159, 2017.
- [31] Bundeskriminalamt, 'Polizeiliche Kriminalitätsstatistik: Grundtabelle - ohne Tatortverteilung ab 1987', Feb. 2019. [Online] Verfügbar unter: https://www.bka.de/DE/AktuelleInformationen/StatistikenLagebilder/PolizeilicheKriminalstatistik/PKS2018/Zeitreihen/zeitreihenFaelle.html?nn=108686. Zugriff am: 22. April 2019.

<!-- page: 118 -->

- [32]  Bundeskriminalamt, Bundeslagebild Cybercrime 2017. [Online] Verfügbar unter: https://www.bka.de/SharedDocs/Downloads/DE/Publikationen/JahresberichteUndLagebilder/Cybercrime/cybercrimeBundeslagebild2017.html;jsessionid=B66516459919E1D617F90854F4BBD185.live2301?nn=28110. Zugriff am: 5. Februar 2019.
- [33] Europol, 'INTERNET ORGANISED CRIME THREAT ASSESSMENT (IOCTA) 2018', Den Haag, 2019.
- [34]  Bundesverband Informationswirtschaft, Telekommunikation und neue Medien e.V., Spionage, Sabotage und Datendiebstahl - Wirtschaftsschutz im digitalen Zeitalter: Studienbericht 2018. [Online] Verfügbar unter: https://www.bitkom.org/Bitkom/Publikationen/Wirtschaftsschutzstudie-2018.html. Zugriff am: 5. Februar 2019.
- [35]  J. Schmidt, Achtung Dynamit-Phishing: Gefährliche Trojaner-Welle Emotet legt ganze Firmen lahm. [Online] Verfügbar unter: https://www.heise.de/security/meldung/Achtung-Dynamit-Phishing-Gefaehrliche-Trojaner-Welle-legt-ganze-Firmen-lahm-4241424.html. Zugriff am: 22. April 2019.
- [36]  J. Dege, Trojaner-Angriff im Burgdorfer Rathaus - LKA ermittelt. [Online] Verfügbar unter: http://www.haz.de/Umland/Burgdorf/Trojaner-Emotet-legt-Stadtverwaltung-lahm-Landeskriminalamt-ermittelt-im-Rathaus-von-Burgdorf. Zugriff am: 22. April 2018.
- [37] G. Christou, 'The collective securit isation of cyberspace in the European Union', West European Politics , Jg. 42, Nr. 2, S. 278 - 301, 2019.
- [38]  M. Schallbruch und I. Skierka, Cybersecurity in Germany, 1. Aufl. Cham: Springer International Publishing, 2018.
- [39]  Bundesamt für Sicherheit in de r Informationstechnik, 'Die Lage der IT -Sicherheit in Deutschland 2017'.
- [40] M. Sparenberg und N. Pohlmann, 'Cybersecurity made in EU', Datenschutz und Datensicherheit , Jg. 42, Nr. 4, S. 220 - 223, 2018.
- [41] T. Wischmeyer, 'Informationssicherheitsrecht: IT -Sicherheitsgesetz und NIS-Richtlinie als Bausteine eines Ordnungsrechts für die Informationsgesellschaft', Die Verwaltung , Jg. 50, Nr. 2, S. 155 - 188, 2017.
- [42] M. Dürig und M. Fischer, 'Cybersicherheit in Kritischen Infrastrukturen', Datenschutz und Datensicherheit , Jg. 42, Nr. 4, S. 209 - 213, 2018.
- [43] RICHTLINIE (EU) 2016/1148 DES EUROPÄISCHEN PARLAMENTS UND DES RATES vom 6. Juli 2016 über Maßnahmen zur Gewährleistung eines hohen gemeinsamen Sicherheitsniveaus von Netz- und Informationssystemen in der Union , 2016.
- [44]  A. Sowa, Management der Informationssicherheit: Kontrolle und Optimierung . Wiesbaden: Springer Fachmedien Wiesbaden; Imprint: Springer Vieweg, 2017.
- [45]  T. Humphreys, Implementing the ISO/IEC 27001 ISMS standard . Boston: Artech House, 2016.
- [46] ISO/IEC 27001:2013 , 2013.

<!-- page: 119 -->

- [47]  H. Kersten, G. Klett, J. Reuter und K.-W. Schröder, IT-Sicherheitsmanagement nach der neuen ISO 27001: ISMS, Risiken, Kennziffern, Controls . Wiesbaden: Springer Vieweg, 2016.
- [48]  H. Kersten, J. Reuter und K.-W. Schröder, IT-Sicherheitsmanagement nach ISO 27001 und Grundschutz: Der Weg zur Zertifizierung, 4. Aufl. Wiesbaden: Springer Vieweg, 2013.
- [49]  K.-R. Müller, Handbuch Unternehmenssicherheit: Umfassendes Sicherheits-, Kontinuitätsund Risikomanagement mit System, 3. Aufl. Wiesbaden: Springer Vieweg, 2015.
- [50] M. Römer und B. Piwinger, 'Informationssicherheit 2013', Düsseldorf, 2013. [Online] Verfügbar unter: https://www.atkearney.de/documents/856314/1214728/BIP\_Informationssicher-heit\_2013.pdf/5396cbc3-1d93-4f3f-9ee8-359fb67a1e85. Zugriff am: 5. März 2019.
- [51] ISO/IEC 27002:2013 , 2013.
- [52] ISO/IEC 27005:2018 , 2018.
- [53] ISO 31000:2018 , 2018.
- [54]  H.-P. Königs, IT-Risikomanagement mit System: Praxisorientiertes Management von Informationssicherheits-, IT- und Cyber-Risiken, 5. Aufl. Wiesbaden: Springer Vieweg, 2017.
- [55]  S. Klipper, Information Security Risk Management: Risikomanagement mit ISO/IEC 27001, 27005 und 31010, 2. Aufl. Wiesbaden: Springer -Vieweg, 2015.
- [56] V. Agrawal, 'A Framework for the Information Classification in ISO 27005 Standard' in 2017 IEEE 4th International Conference on Cyber Security and Cloud Computing (CSCloud) , New York, NY, USA, Jun. 2017 - Jun. 2017, S. 264 - 269.
- [57]  H. Kersten und G. Klett, Business Continuity und IT-Notfallmanagement . Wiesbaden: Springer Fachmedien Wiesbaden, 2017.
- [58] ISO/IEC 27009:2016 , 27009, 2016.
- [59] T. Goldschmidt und S. Krüsmann, 'IT - Grundschutz 2.0', &lt;kes&gt; - Die Zeitschrift für Informations-Sicherheit , Jg. 5, 89-94, 2017.
- [60] BSI-Standard 200-1 , 2017.
- [61]  F. Stetter und S. Heukrodt-Bauer, 'IT -Grundschutzkataloge des BSI - Last oder Mehrwert?', Wirtschaftsinformatik &amp; Management , Jg. 9, Nr. 4, S. 62 - 66, 2017.
- [62] H. Schildt, 'Der neue IT -Grundschutz: Modernisierung erfolgreich abgeschlossen', &lt;kes&gt; - Die Zeitschrift für Informations-Sicherheit , Jg. 6, S. 53 - 54, 2017.
- [63] A. Essoh und B. Klein, 'Migration auf den modernisierten IT -Grundschutz: Anleitung für einen r eibungslosen Übergang', &lt;kes&gt; - Die Zeitschrift für Informations-Sicherheit , Jg. 2, S. 25 - 26, 2018.
- [64] BSI-Standard 200-2 , 2017.
- [65] BSI-Standard 200-3 , 2017.
- [66] H. Kreutzmann, 'Sektorspezifische ISMS -Standards und -Normen - eine Aktualisierung', &lt;kes&gt; - Die Zeitschrift für Informations-Sicherheit , Jg. 3, S. 36 - 38, 2017.
- [67] H. Schildt und I. Münch, 'Schablonen für die Informationssicherheit', &lt;kes&gt; - Die Zeitschrift für Informations-Sicherheit , Jg. 4, S. 36 - 40, 2016.

<!-- page: 120 -->

- [68]  F. Grotz, A. Götz, M. Lewandowsky und H. Wehrkamp, Verwaltungsstrukturreformen in den deutschen Ländern: Die Entwicklung der staatlichen Kernverwaltung im Ländervergleich . Wiesbaden: Springer VS, 2017.
- [69] D. Schamburek, 'Die Ansiedlung von Aufgaben in der Aufbauorganisation deutscher Landesministerialverwaltungen'. Dissertation, 2016.
- [70]  B. Becker, Öffentliche Verwaltung: Lehrbuch für Wissenschaft und Praxis . Percha am Starnberger See: Schulz, 1989.
- [71]  S. Bröchler und H.- J. Lauth, 'Regierungen (Bund und Länder)' in Handbuch Staat , R. Voigt, Hg., Wiesbaden: Springer Fachmedien Wiesbaden, 2018, S. 857 - 871.
- [72]  J. Bogumil und W. Jann, Verwaltung und Verwaltungswissenschaft in Deutschland: Einführung in die Verwaltungswissenschaft, 2. Aufl. Wiesbaden: VS Verlag für Sozialwissenschaften, 2009.
- [73]  B. Krems, Stichwort "Geschäftsverteilungsplan" im Online-Verwaltungslexikon. [Online] Verfügbar unter: https://olev.de/g.htm#Geschaeftsverteilungsplan. Zugriff am: 9. Mai 2019.
- [74]  R. Koch, Hg., New Public Service: Öffentlicher Dienst als Motor der Staats- und Verwaltungsmodernisierung, 2. Aufl. Wiesbaden: Springer Fachmedien, 2011.
- [75] Gemeinsame Geschäftsordnung der Landesregierung und der Ministerien in Niedersachsen: GGO , 2004.
- [76] Gemeinsame Geschäftsordnung für die Ministerien des Landes Nordrhein-Westfalen: GGO , 2014.
- [77]  H. Träger und S. Priebus, Politik und Regieren in Sachsen-Anhalt . Wiesbaden: Imprint Springer VS, 2017.
- [78]  T. Nentwig und C. Werwath, Hg., Politik und Regieren in Niedersachsen . Wiesbaden: Springer VS, 2016.
- [79]  D. Berger-Grabner, Wissenschaftliches Arbeiten in den Wirtschafts- und Sozialwissenschaften: Hilfreiche Tipps und praktische Beispiele, 3. Aufl. Wiesbaden: Springer Gabler, 2016.
- [80] U. Kelle, 'Mixed Methods' in Handbuch Methoden der empirischen Sozialforschung , N. Baur und J. Blasius, Hg., Wiesbaden: Springer Fachmedien Wiesbaden, 2014, S. 153 - 166.
- [81]  U. Kuckartz, Mixed Methods: Methodologie, Forschungsdesigns und Analyseverfahren . Wiesbaden: Springer VS, 2014.
- [82] Leitlinie für die Informationssicherheit in der öffentlichen Verwaltung - Umsetzungsplan - , 2013.
- [83]  R. Kaiser, Qualitative Experteninterviews . Wiesbaden: Springer Fachmedien Wiesbaden, 2014.
- [84]  R. Porst, Fragebogen: Ein Arbeitsbuch, 4. Aufl. Wiesbaden: Springer Fachmedien Wiesbaden, 2014.
- [85] J. Klöckner und J. Friedrichs, 'Gesamtgestaltung des Fragebogens' in Handbuch Methoden der empirischen Sozialforschung , N. Baur und J. Blasius, Hg., Wiesbaden: Springer Fachmedien Wiesbaden, 2014, S. 675 - 699.

<!-- page: 121 -->

- [86]  U. Enge l und B. O. Schmidt, 'Unit - und Item-Nonresponse' in Handbuch Methoden der empirischen Sozialforschung , N. Baur und J. Blasius, Hg., Wiesbaden: Springer Fachmedien Wiesbaden, 2014, S. 331 - 348.
- [87] M. Herr, C. E. Müller, B. Engewald und J. Ziekow, 'Transpa renzgesetzgebung in Deutschland in der Bewährung: Erfahrungen einer Gesetzesevaluation', DÖV (Die Öffentliche Verwaltung) , Jg. 5, S. 165 - 168, 2018.
- [88]  P. Fischer und P. Hofer, Lexikon der Informatik, 15. Aufl. Berlin, Heidelberg: Springer-Verlag Berlin Heidelberg, 2011.
- [89]  S. Brich und C. Hasenbalg, Kompakt-Lexikon Wirtschaftsinformatik: 1.500 Begriffe nachschlagen, verstehen, anwenden . Wiesbaden: Springer Gabler, 2013.
- [90]  StatCounter, Global Market Share Held by Operating Systems for Desktop Pcs, from January 2013 to January 2019. [Online] Verfügbar unter: www.statista.com/statistics/218089/global-market-share-of-windows-7. Zugriff am: 15. Februar 2019.
- [91]  T. Myerson, Hello World: Windows 10 Available on July 29. [Online] Verfügbar unter: https://blogs.windows.com/windowsexperience/2015/06/01/hello-worldwindows-10-available-on-july-29/. Zugriff am: 25. April 2019.
- [92] H. Lemke, 'IT -Einsatz in der öffentlichen Verwaltung: Sachstand, Herausforderungen, Perspektiven', Die Verwaltung , Jg. 46, Nr. 1, S. 123 - 134, 2013.
- [93]  M. Broy und O. Spaniol, VDI-Lexikon Informatik und Kommunikationstechnik . Berlin, Heidelberg: Springer, 1999.
- [94]  Kantar, Share of The Leading Smartphone Operating Systems in The Sales Volume of Smartphones in Germany from January 2012 to September 2018. [Online] Verfügbar unter: www.statista.com/statistics/461959/smartphone-os-sales-volume-share-germany. Zugriff am: 15. Februar 2019.
- [95] NIST Special Publication 800-63B , 2017.
- [96] Data Security Standard , 2018.
- [97] M. Knoll, 'IT -Ris ikomanagement im Zeitalter der Digitalisierung', HMD Praxis der Wirtschaftsinformatik , Jg. 54, Nr. 1, S. 4 - 20, 2017.
- [98]  N. Prat, I. Comyn-Wattiau und J. Akoka, 'ARTIFACT EVALUATION IN INFORMATION SYSTEMS DESIGN-SCIENCE RESEARCH - A HOLISTIC VIEW', PACIS 2014 Proceedings , 2014.
- [99] M. D. Ahmed und D. Sundaram, 'Design Science Research Methodology: An Artefact-Centric Creati on and Evaluation Approach', ACIS 2011 Proceedings , 2011.

<!-- page: 122 -->

## Anhang A Befragung

## Anhang A.1 Verwendeter Fragebogen

## BEFRAGUNG DER INFORMATIONSSICHERHEITSBEAUFTRAGTEN DER LANDESVERWALTUNGEN DEUTSCHLANDS

Erstellt im Rahmen des Masterstudiengangs INFORMATION SECURITY MANAGEMENT der Fachhochschule Hagenberg

ERSTELLER: RAPHAEL GRIEGER MATRIKEL-NR. S1710771007

13. November 2018

<!-- page: 123 -->

## VORWORT

Dieser Fragebogen ist Teil der Entwicklung eines IT-Grundschutz-Profils für oberste Landesbehörden, wie ein Innen- oder Finanzministerium. Ziel ist die schematische Darstellung des Informationsverbundes einer obersten Landesbehörde und damit die vereinfachte Einführung der Standard-Absicherung in einer solchen Institution. Nach der Entwicklung  des  IT-Grundschutz-Profils  soll  das  Ergebnis  letztlich  auf  eine  ausgewählte oberste Landesbehörde angewandt werden.

Bereits in der Ausarbeitung des Profils soll das Wissen der gängigen Praxis berücksichtigt und mit einbezogen werden. Aufgrund Ihrer Tätigkeit als Informationssicherheitsbeauftragte/r der Landesverwaltungen und dem damit verbundenen Erfahrungsschatz, wurden Sie daher für diese Befragung ausgewählt.

Bitte geben Sie zunächst allgemeine Informationen zu Ihrer Person, Tätigkeit und Institution an. Diese Daten werden nur statistisch berücksichtigt und ggf. für Rückfragen verwendet. Eine Veröffentlichung findet nicht statt.

| Datum       | Bitte geben Sie das Datum ein.                                                 | Name             | Bitte geben Sie Ihren vollständi- gen Namen ein.                                                             |
|-------------|--------------------------------------------------------------------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Institution | Bitte geben Sie Ihre Insti- tution ein.                                        | Bundes- land     | Bitte geben Sie das Bundesland Ihrer Institution ein.                                                        |
| Tätigkeit   | Bitte geben Sie die Tätig- keit an, die Sie in Ihrer In- stitution wahrnehmen. | Erreich- barkeit | Bitte geben Sie für Rückfragen Ihre Erreichbarkeiten ein (Telefon und E-Mail. Diese Angabe ist frei- willig. |

Auf der Folgeseite werden anschließend die Fragen aufgeführt. Diese sind offen formuliert und freitextlich zu beantworten. Ich bitte Sie daher um möglichst vollständige und wahrheitsgemäße Angaben. Da Ihre Antworten einen variablen Umfang haben werden, empfehle ich Ihnen den Fragebogen elektronisch auszufüllen.

Aus Gründen der Transparenz wird die Befragung in der Masterarbeit anonymisiert veröffentlicht. Um Rückschlüsse auf einzelne Institutionen zu vermeiden, werden die Antworten dabei nicht im Kontext der einzelnen Fragebögen, sondern lediglich zusammengefasst dargestellt.

Ich bitte Sie um eine Beantwortung bis zum 15.11.2018 und danke Ihnen im Voraus für Ihre Teilnahme.

<!-- page: 124 -->

## FRAGEBOGEN

## I. Das ISMS in einer obersten Landesbehörde

Beantworten Sie zunächst einige Fragen zu dem ISMS einer obersten Landesbehörde Ihrer Wahl, deren Informationsverbund sie gut kennen. Beziehen Sie Ihre Antworten bitte nur auf die ausgewählte oberste Landesbehörde.

- Für welche Institution werden Sie die folgenden Fragen beantworten? Bitte geben Sie hier die Antwort auf die Frage ein.
- Der modernisierte IT-Grundschutz unterscheidet in dem Standard 200-2 sowie dem IT-Grundschutz-Kompendium zwischen der Basis-, Kern- und StandardAbsicherung als anzuwendende Methodik. Welche dieser drei Methodiken verwendet Ihre Institution oder wird sie in der Zukunft anwenden?

Bitte geben Sie hier die Antwort auf die Frage ein.

- Wie weit ist das ISMS in der ausgewählten Institution umgesetzt (bspw. in Planung, teilweise oder vollständig)? Sollte das ISMS nur teilweise umgesetzt sein, bitte ich Sie die fehlenden Bereiche zu nennen.

Bitte geben Sie hier die Antwort auf die Frage ein.

- Welcher Geltungs- beziehungsweise Anwendungsbereich wurde für das ISMS in Ihrer Institution formuliert?

Bitte geben Sie hier die Antwort auf die Frage ein.

- Welche Anwendungen sind von Ihrer Behörde im Rahmen des ISMS erfasst worden?

Bitte geben Sie hier die Antwort auf die Frage ein.

- Welche IT-Systeme wurden im Rahmen der Strukturanalyse festgestellt? Bitte geben Sie hier die Antwort auf die Frage ein.
- Wurden im Rahmen der Strukturanalyse Zielobjekte mit hohem oder sehr hohem Schutzbedarf festgestellt? Bitte zählen Sie diese auf.

Bitte geben Sie hier die Antwort auf die Frage ein.

- Erbringen Dritte für Ihre Institution IT-Dienstleistungen? Bitte zählen Sie gegebenenfalls die ausgelagerten Zielobjekte (Anwendungen, Systeme, etc.) auf.

Bitte geben Sie hier die Antwort auf die Frage ein.

- Wurden Zielobjekte mit hohem oder sehr hohem Schutzbedarf Dritte ausgelagert? Bitte zählen Sie diese gegebenenfalls auf.

Bitte geben Sie hier die Antwort auf die Frage ein.

<!-- page: 125 -->

## II. Expertenerfahrungen und Einschätzungen

Nun bitte ich Sie um Ihre persönliche Einschätzung als Expertin oder Experten für Informationssicherheit.

- Welche Geschäftsprozesse würden Sie für eine schematisch dargestellte oberste Landes-behörde als typisch ansehen? Wie sind diese definiert?

Bitte geben Sie hier die Antwort auf die Frage ein.

- Welche Zielobjekte sind in einer obersten Landesbehörde Ihrer Einschätzung nach  als  besonders  schützenswert  anzusehen  (Schutzbedarf  hoch  oder  sehr hoch)?

Bitte geben Sie hier die Antwort auf die Frage ein.

- Welches Schutzziel der Informationssicherheit (Vertraulichkeit, Integrität, Verfügbarkeit) ist das Wichtigste in einer obersten Landesbehörde? Bitte begründen Sie kurz.

Bitte geben Sie hier die Antwort auf die Frage ein.

- Denken Sie die Schutzziele 'Nicht - Abstreitbarkeit', 'Vertrauen', 'Nachvollziehbarkeit' oder 'Verlässlichkeit' sind relevant für die Informationssicherheit in einer obersten Landesbehörde? Bitte nennen Sie die relevant erscheinenden Schutzziele und begründen Sie kurz.

Bitte geben Sie hier die Antwort auf die Frage ein.

- Können  Sie  Anforderungen  an  ein  IT-Grundschutz-Profil  für  eine  oberste Landes-behörde formulieren?

Bitte geben Sie hier die Antwort auf die Frage ein.

- Gab oder gibt es bei der Umsetzung des ISMS Probleme in Ihrer Institution? Bitte erläutern Sie die Ihrer Einschätzung nach schwerwiegendsten Probleme.

Bitte geben Sie hier die Antwort auf die Frage ein.

<!-- page: 126 -->

## III. Abschluss

- ·
- Gibt es Ihrerseits noch weitere Anmerkungen? Bitte geben Sie bei Bedarf hier die Antwort auf die Frage ein.

<!-- page: 127 -->

## ABSCHLUSS

Bitte speichern Sie das ausgefüllte Dokument ab oder exportieren Sie dieses als PDF-Datei. Die Datei (und damit den ausgefüllten Fragebogen) können Sie mir auf zwei Wegen zukommen lassen:

Zum einen besteht die Möglichkeit, die Antwort Herrn Köhler (CISO der Niedersächsischen Landesverwaltung) zuzusenden. Dieser wird die Datei an mich weiterleiten.

Zum anderen können Sie mir den Fragebogen auch direkt zusenden. Meine private Kontaktadresse ist:

## Raphael Grieger

(Die persönliche Anschrift wurde zur Wahrung der Privatsphäre entfernt)

Bei einer Übersendung an meine private Erreichbarkeit empfehle ich Ihnen zur Wahrung der Vertraulichkeit und Integrität der Informationen eine Verschlüsselung der Datei.

Dazu erscheint die Übermittlung in Form einer passwortgeschützten PDF-Datei oder eines verschlüsselten Archivs am geeignetsten. Sollten Sie sich dazu entscheiden, bitte ich  Sie  um  gesonderte Übermittlung des Passworts. Alternativ sind auch andere geschützte Übermittlungsmethoden möglich, ich bitte Sie mich in diesem Fall ebenfalls zu kontaktieren.

Das entwickelte IT-Grundschutz-Profil wird voraussichtlich im Jahr 2019 durch das Bundesamt  für  Sicherheit  in  der  Informationstechnik  zunächst  als  'Community Draft' veröffentlicht werden. Dort erhalten Sie di e Möglichkeit, dass Profil einzusehen und bei Bedarf weiter zu verbessern. Sollten Sie bereits vorab Interesse an einer Beteiligung bei diesem Entwurf haben, können Sie dies in den Anmerkungen angeben. Ich werde Sie diesbezüglich gesondert kontaktieren.

Zum Abschluss des Fragebogens möchte ich Ihnen nun herzlich für die Teilnahme an dieser Befragung danken! Vielen Dank, dass Sie sich die Zeit genommen haben, um die Entwicklung des IT-Grundschutz-Profils zu unterstützen.

Raphael Grieger

<!-- page: 128 -->

## Anhang A.2 Antworten auf den Fragenteil I

Nachfolgend sind die Antworten der Teilnehmer der Befragung zu dem IT-Grundschutz-Profil dargestellt. Die Antworten sind zufällig angeordnet, um, wie den Teilnehmern zugesichert, Rückschlüsse auf eine konkrete Behörde zu vermeiden. Ebenfalls sind die Antworten angepasst, sodass die Nennung eines Bundeslandes nicht vorhanden ist. Zuletzt sind Schreibfehler der Antworten korrigiert worden.

Die erste Frage enthält die Angabe der Befragten, für welche konkrete Behörde geantwortet wird. Aus Anonymisierungsgründen wird die erste Frage hier nicht aufgeführt.

## Das ISMS in einer obersten Landesbehörde

Beantworten Sie zunächst einige Fragen zu dem ISMS einer obersten Landesbehörde Ihrer Wahl, deren Informationsverbund sie gut kennen. Beziehen Sie Ihre Antworten bitte nur auf die ausgewählte oberste Landesbehörde.

Frage 2: Der modernisierte IT-Grundschutz unterscheidet in dem Standard 200-2 sowie dem IT-Grundschutz-Kompendium zwischen der Basis-, Kern- und Standard-Absicherung als anzuwendende Methodik. Welche dieser drei Methodiken verwendet

Ihre Institution oder wird sie in der Zukunft anwenden?

## Antworten

Geplant ist die Umsetzung gemäß Standard-Absicherung.

Zunächst ist eine Kern-Absicherung geplant. Darauf aufbauend sind Basis- und, in einem dritten Schritt, Standard-Absicherung geplant

Momentan wird im MI ein Informationssicherheitskonzept für eine Basisabsicherung erarbeitet. Nach Fertigstellung und Umsetzung der dafür noch notwendigen Maßnahmen ist die konzeptionelle Vorbereitung und Umsetzung einer Standardabsicherung geplant.

Es soll in Zukunft eine Standardabsicherung erreicht werden.

Wir beabsichtigen, die Kern- und Standard-Absicherung vorzunehmen. Momentan haben wir noch die Beschreibungen nach den ,altem Standard' durchgeführt.

Alle drei Varianten, je nach Organisation insbesondere auch Rechtsform der jeweiligen Organisation.

Beispiel: Einer Dienststelle mit autarker IT und entsprechendem Auftrag (Angebote am Markt als GmbH), neben der Tätigkeit für die Verwaltung) haben wir den Standard ISIS12 'auferlegt'. Inhaltlich entspric ht das der BASIS Absicherung.

Einer Dienststelle (Ressort), welche auf dem Weg zum Grundschutz ist, dies aber nicht unverzüglich leisten kann, empfehlen wir die Kernabsicherung. Identifizieren von IT gestützten Geschäftsprozessen von besonderer Bedeutung (Daseinsvorsorge, politisch, hohe Betroffenheit in der Bevölkerung, medial wirksam).

Die Standard Absicherung erwarten wir von den für uns tätigen IT Dienstleistern. Diese Standards (GS-zertifiziert) sollen in eine möglichst maximale 'Weite' in die Dienststellen hinein reichen, so dass die Dienststellen eine Differenzbetrachtung anstellen müssen.

<!-- page: 129 -->

Frage 3: Wie weit ist das ISMS in der ausgewählten Institution umgesetzt (bspw. in Planung, teilweise oder vollständig)? Sollte das ISMS nur teilweise umgesetzt sein, bitte ich Sie die fehlenden Bereiche zu nennen.

| Antworten                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ISMS ist in der gesamten Landesverwaltung umgesetzt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Größtenteils in Planung bzw. in Vorbereitung - Umsetzungsbeginn in Kürze.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Das ISMS ist vor allem über die Ressorts etabliert. Fast vollständig sind die Sicher- heitsmanagements Teil der IT Abteilungen. Das vorwiegend organisatorische ISMS hat derzeit einen Reifegrad von: TEILWEISE. Es fehlen vor allem konzeptionelle Umsetzungen in den Ressorts. Die zugeordneten Bereiche der Ressorts werden ungenügend adressiert. Die Verantwortung des Mana- gements wird nicht wahrgenommen, bestenfalls delegiert. Technische Maßnahmen sind derzeit nicht umgesetzt. Rechtliche Voraussetzungen fehlen. Ressourcen fehlen. Diese Standards (GS- zertifiziert) sollen in eine möglichst maximale 'Weite' in die Dienststellen hinein reichen, so dass die Dienststellen eine Differenzbetrachtung an- stellen müssen. |
| In Planung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Das ISMS befindet sich im Aufbau. Eine Informationssicherheitsleitlinie wurde er- arbeitet und in Kraft gesetzt. Im nächsten Schritt erfolgt die Bildung eines ISM- Teams im Hause. Innerhalb eines zu erarbeitenden Basissicherheitskonzepts wurden bisher die umzu- setzenden Prozessbausteine festgelegt.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Das ISMS ist nur rudimentär aufgebaut. Die Informationssicherheitsleitlinie ist zwar lange schon erstellt, wurde aber formell nicht verabschiedet. Es fehlt ein Risiko- und Notfallmanagement. Ein systematischer, vollständiger Überblick über Verfahrens- verbünde, deren Modellierung, vorhandene Schutzbedarfsfeststellungen und durch- geführte Basis-Sicherheitschecks soll 2019 erstellt werden.                                                                                                                                                                                                                                                                                                                                      |

Frage 4: Welcher Geltungs- beziehungsweise Anwendungsbereich wurde für das ISMS in Ihrer Institution formuliert?

| Antworten                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Das ISMS gilt für das Ministerium für Inneres und Sport.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Die gesamte Dienststelle                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Das ISMS ist mit einem Senatsbeschluss (Kabinettsbeschluss) landesweit auf Grund- schutzbasis festgelegt. Der kommunale Bereich hat entsprechend gehandelt.                                                                                                                                                                                                                                                                                                              |
| Leitlinie: Ministerium sowie nachgeordneter Geschäftsbereich. Die Verwaltungs- zweige im nachgeordneten Bereich setzen das ISMS jeweils eigenständig um.                                                                                                                                                                                                                                                                                                                 |
| Der Geltungsbereich ist in der Informationssicherheitsleitlinie und in der Einsetzungsverfügung des ISB beschrieben und bezieht sich auf das Ministerium und auf den nachgeordneten Bereich.                                                                                                                                                                                                                                                                             |
| Die Informationssicherheits-Leitlinie (IS-LL) ist beschlossen. Sie gilt für alle Dienst- stellen, Organe der Rechtspflege sowie den sonstigen öffentlichen Stellen des Landes, soweit diese im staatlichen Auftrag tätig werden. Für andere Stellen und Einrichtun- gen des Landes (z. B. Rechnungshof) gilt die Leitlinie und die daraus folgenden Vor- gaben nach Maßgabe gesondert abzuschließender Vereinbarungen für die gemein- same Nutzung der IT-Infrastruktur. |

<!-- page: 130 -->

Frage 5:  Welche Anwendungen sind von Ihrer Behörde im Rahmen des ISMS erfasst worden?

## Antworten

Geplant: alle Fachverfahren, Basis-IT-Dienste (wie bspw. Exchange, AD, usw.).

Die Erfassung der Anwendungen steht noch aus. Es ist vorgesehen, die Erfassung referatsweise zu erarbeiten.

Fehlanzeige, ggf. telefonische Nachfrage bei mir.

Ein  vorhandenes  IT-Architekturmanagement  mit  Übersicht  alle  Fachverfahren wurde  vom  ISMS  mitverwendet.  Das  Architekturmanagement  wurde  aufgegeben und das entsprechende Verzeichnis abgekündigt. Somit beginnt das ISMS derzeit, die Erfassung von Neuem (geplant für 2019).

1. Zentrale Infrastrukturen.

2. Mit den Geschäftskritische Anwendungen des Landes ist begonnen worden.

Bisher wurden neben Exchange und Outlook auch die Anwendung Qchess erfasst. Die Erfassung ist aber noch nicht abgeschlossen.

Die  Anwendungen  Domea  und  Landwirtschaftliche  Betriebsdatenbank  werden ebenfalls erfasst, werden aber nicht vom Ministerium betreut.

Frage 6: Welche IT-Systeme wurden im Rahmen der Strukturanalyse festgestellt?

| Antworten                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bisher wurden Allgemeiner Server, SAN-Systeme, Laptop, Drucker- und Kopierge- räte, Windows-Server 2008, Allgemeiner Client, Core-Switch betrachtet. Die Aufzäh- lung ist aber nicht abschließend, da die Strukturanalyse noch nicht abgeschlossen ist. |
| Da das Unterstützungstool (HiScout), welches als Landeslizenz beschafft wurde, noch nicht genutzt werden kann, steht keine aktuelle Strukturanalyse zur Verfügung. Dieses soll abgewartet werden, um Doppelarbeit zu vermeiden.                         |
| Ein Großteil der IT-Systeme wurde vom IT-Dienstleister des Landes im Rahmen vertraglicher Leitungen (Security-SLAs) erfasst und dokumentiert. Siehe 5.                                                                                                  |
| Typischerweise Standard-Arbeitsplatz; mobile Geräte (Notebook, Smartphones, Tablets); Server                                                                                                                                                            |
| IT-Systeme der RZ² Infrastruktur (z.B. Server, Datenbanken, Webserver, Netzinfra- struktur.)                                                                                                                                                            |

Frage 7: Wurden im Rahmen der Strukturanalyse Zielobjekte mit hohem oder sehr hohem Schutzbedarf festgestellt? Bitte zählen Sie diese auf.

## Antworten

Aufgrund des aktuellen Projektstatus noch keine Antwort möglich.

Ja,  einige  Fachverfahren  (IT-Verbünde)  und  zentrale  Infrastrukturen  (z.B.  AD, SCCM, HIM-Workflow.)

Die Ressorts oder Dienststellen haben vereinzelt die Schutzbedarfe ihrer Systeme erhoben, hohe und sehr hohe Schutzbedarfe wurden identifiziert. Aufzählung?  Siehe 5.

<!-- page: 131 -->

Im Bereich der Landespolizei sicherlich. Dort ist ein eigenes Sicherheitsmanagement etabliert. Die Übersicht ist dem ISMS des Ministeriums in der Gesamtheit nicht bekannt. Eine Aufzählung der Verfahren möchte ich über den Fragebogen nicht abgeben.

Siehe Frage 6.

Bisher noch nicht, die Strukturanalyse ist aber noch nicht abgeschlossen.

Frage 8: Erbringen Dritte für Ihre Institution IT-Dienstleistungen? Bitte zählen Sie gegebenenfalls die ausgelagerten Zielobjekte (Anwendungen, Systeme, etc.) auf.

## Antworten

Dataport  ist  der  zentrale  Dienstleister  für  Schleswig-Holstein,  Hamburg,  Bremen und Sachsen-Anhalt. Eine Gesamtübersicht der ausgelagerten Zielobjekte liegt mir nicht vor. Ein Zugriff auf die Haushaltplandaten ist möglich, aus Kapazitätsgründen ist eine Auswertung bislang nicht erfolgt.

Serverbetrieb durch das staatliche Rechenzentrum; Anwendungsentwicklung (Webund Rich-Clientanwendungen) teilweise im Auftrag durch Dritte.

Als zentraler Dienstleister für das Land erbringt Dataport IT-Dienstleistungen für das MI.

Die IT des Landes ist überwiegend auf den IT Dienstleister Dataport (und seine Subcontracter) verlagert worden. Insbesondere trifft das Netzinfrastruktur (100%),

Telefonie (ca. 100%), Rechenzentrum (20%), Clientmanagement (50%). Des Weite-

ren arbeiten

-

nicht zentral gesteuerte (CIO)- IT-Dienstleister für Dienststellen und

Ressorts  im  Binnenverhältnis  (Clientmanagement,  Gebäude  Infrastruktur  Betrieb,

Anwendungsbetrieb, Serverbetrieb, UHD).

Ausgelagert  an  den  Landesbetrieb  sind  die  Anwendungen  Domea  und Landwirtschaftliche Betriebsdatenbank, da der Betrieb bereits nach ISO 27001 auf der Basis von IT-Grundschutz zertifiziert ist

Ja, das Land hat Anteile an einem externen Dienstleister, der den größten Teil der Leistungen erbringt. 2/3 der Arbeitsplätze sind full managed. Das RZ und Teile der Netze sind BSI zertifiziert.

Frage 9: Wurden Zielobjekte mit hohem oder sehr hohem Schutzbedarf Dritte ausgelagert? Bitte zählen Sie diese gegebenenfalls auf.

| Antworten                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nein.                                                                                                                                                                                                                                           |
| Aus dem Polizeibereich ist eine Auslagerung einen Dienstleister erfolgt.                                                                                                                                                                        |
| Siehe Frage 6.                                                                                                                                                                                                                                  |
| Aufgrund des aktuellen Projektstatus noch keine Antwort möglich. Allerdings gilt: Outsourcing sowie Cloud-Dienste sollten aus Sicht des Landes-CIO ab hohem Schutzbedarf aus grundsätzlichen Erwägungen nicht mehr in Anspruch genommen werden. |
| Siehe Frage 8.                                                                                                                                                                                                                                  |
| Das erklärte- und im Großem durchgeführte Ziel war und ist es, genau diese Verfah- ren auf die gesicherten Infrastrukturen des zentralen IT Dienstleisters (AöR) zu über- tragen.                                                               |

<!-- page: 132 -->

Verfahren des Ordnungswesens, Justizbereich, Polizei, Finanzen (Haushalt und Steuern), Gesundheitswesen.

## Anhang A.3 Antworten auf den Fragenteil II

Nun bitte ich Sie um Ihre persönliche Einschätzung als Expertin oder Experten für Informationssicherheit.

Frage 10: Welche Geschäftsprozesse würden Sie für eine schematisch dargestellte oberste Landesbehörde als typisch ansehen? Wie sind diese definiert?

## Antworten

Bürokommunikation und Vorgangsbearbeitung. Für die Finanzministerien: IT-Unterstützung für Haushaltsaufstellung und -vollzug

Jeweils die Kernprozesse jeden Ressorts, die zentrale Infrastruktur und der Grundschutzkonforme RZ-Betrieb. Eine Aufzählung würde eine Ressort-Abfrage bedingen und wegen des zeitlichen Aufwandes nicht durchgeführt werden.

1. Daseinsvorsorge und Innere Sicherheit (KRITIS).
2. Hohe Betroffenheit bei Bürgern und der Wirtschaft.
3. Aufrechterhaltung des Verwaltungsbetriebes

Exchange und E-Mail, E-Akte-System, Fachanwendungen

1. Gesetzgebungsverfahren
2. Rechtsetzungsverfahren

Ich orientiere mich an einer Zusammenstellung aus IT-Grundschutzkompendium, ISO 2700x und COBIT 5. Übersicht der Geschäftsprozesse, die durch das ISMS zu steuern sind, lege ich als Anhang bei.

Frage 11: Welche Zielobjekte sind in einer obersten Landesbehörde Ihrer Einschätzung nach als besonders schützenswert anzusehen (Schutzbedarf hoch oder sehr hoch)?

## Antworten

Da bisher noch keine Objekte mit hohem oder sehr hohem Schutzbedarf ermittelt wurden, ist eine Antwort auf diese Frage nicht möglich.

Geschäftskritische Verfahren aller Ressorts.

Besonderes Augenmerk sollte auf den gesamten Komplex 'Datensicherung' gelegt werden, was allerdings nicht gleichbedeutend mit hohem Schutzbedarf ist.

Unklar.

Personalbearbeitung bzw. - Verwaltung; Kabinettsangelegenheiten; Kassenaufgaben (Staatsoberkasse und Staatshauptkasse); Haushaltsaufstellung; Steuerverwaltung (Bereich Finanzämter und Elster).

Generell alle Dienste, die im Querschnitt eingesetzt werden und aggregierte Daten halten: Verzeichnisdienste, zentrale Anmelde- und Identifizierungsdienste und dergleichen, sowie zentral geführte Register. Zahlungsverfahren fallen ebenso in diesen Bereich. Die Verfahren der traditionellen Sicherheitsbehörden zählen ebenso dazu.

<!-- page: 133 -->

Frage 12: Welches Schutzziel der Informationssicherheit (Vertraulichkeit, Integrität, Verfügbarkeit) ist das Wichtigste in einer obersten Landesbehörde? Bitte begründen Sie kurz.

| Antworten                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vertraulichkeit. Da in den obersten Landesbehörden ständig mit vertraulichen und streng vertrauli- chen Informationen gearbeitet wird, ist die Vertraulichkeit das Wichtigste Schutzziel. Wenn vertrauliche Informationen aus einer obersten Landesbehörde an die Öffent- lichkeit gelangen, ist das Ansehen der Behörde sehr stark beschädigt.                                                                                         |
| Diese Schutzziele stehen gleichberechtigt nebeneinander, eine 'Wichtung' brächte keine Vorteile                                                                                                                                                                                                                                                                                                                                         |
| Die obersten Landesbehörden stehen häufig in einer Gewährleistungspflicht, nicht so sehr in der Durchführungsverpflichtung. Daher tendiere ich dazu, die Integrität als das wichtigste Ziel anzusehen.                                                                                                                                                                                                                                  |
| Je nach Einzelfall variiert die Wichtigkeit. Im Folgenden sind jeweils Beispiele aufge- führt:                                                                                                                                                                                                                                                                                                                                          |
| Für die telefonische Erreichbarkeit der Notfallnummern (110,112) ist Verfügbarkeit das Wichtigste.                                                                                                                                                                                                                                                                                                                                      |
| Für Sozialsysteme mit jugendlichen Straf- und Psychologiedaten ist die Vertraulich- keit vorrangig.                                                                                                                                                                                                                                                                                                                                     |
| Beim Active Directory sind alle drei Schutzziele gleichrangig. Für eine oberste Landesbehörde sind die Schutzziele Vertraulichkeit und Integrität als am wichtigsten einzuschätzen. Das Vertrauen des Bürgers beruht auch auf die ordnungsgemäße Verarbeitung und die Richtigkeit der Daten.                                                                                                                                            |
| gig im Binnenverhältnis einzuschätzen. Die Verfügbarkeit gewinnt erst wieder an Be- deutung im Digitalisierungskontext und der rund um die Uhr zur Verfügung gestell- ten Dienstleistungen. In dieser Pauschalität: Alle drei Schutzziele sind gleichwertig. Nuancen ergeben bei konkreten Verfahren: Beim Kassenverfahren stehen beispielsweise Integrität Verfügbarkeit (Liquidität!) im Vordergrund, bei der Personalbewirtschaftung |
| sich und hinge- gen Vertraulichkeit und Integrität.                                                                                                                                                                                                                                                                                                                                                                                     |

Frage 13: Denken Sie die Schutzziele 'Nicht - Abstreitbarkeit', 'Vertrauen', 'Nachvollziehbarkeit' oder 'Verlässlichkeit' sind relevant für die Informationssicherheit in einer obersten Landesbehörde? Bitte nennen Sie die relevant erscheinenden Schutzziele und begründen Sie kurz.

| Antworten                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mit Ausnahme von Vertrauen sind die anderen Schutzziele aus den drei originalen Schutzzielen der Informationssicherheit abzuleiten. Daher sind sie relevant. Nicht-Abstreitbarkeit und Verlässlichkeit sind Teilmengen der Integrität und der Verfügbarkeit. Nachvollziehbarkeit wird durch zentrale Protokollierung erreicht. Wir halten Schutzziele, die sich aus den 3 originären InformationsSchutzzielen ablei- ten lassen für Betrachtungswürdig. Alle anderen Datenschutz-Schutzziele lassen wir außen vor. |
| Da die Staatsministerien im Allgemeinen nur sehr wenige Vollzugsaufgaben haben, sind Vertrauen und Verlässlichkeit wohl in den Vordergrund zu stellen. In diesen                                                                                                                                                                                                                                                                                                                                                   |

<!-- page: 134 -->

Schutzzielen spiegelt sich die hergebrachte Vertrauensstellung zwischen Bürger und Verwaltung, die vom Ministerium in besonderer Weise ausgefüllt werden muss (Prinzip der Ministerverantwortung).

Das ist im Rahmen einer Fragebogenabfrage für mich nicht spontan zu beantworten. Häufig sind Schutzziele zerlegbar in einzelne Bestandteile, so könnte man

Verlässlichkeit als Mischung zwischen Verfügbarkeit und Integrität auffassen. Die Datenschutzziele der Transparenz, Intervenierbarkeit und Nicht-Verkettbarkeit halte ich auch im Bereich der Informationssicherheit relevant, zumal das ISMS gehalten ist, auch Datenschutzanforderungen umzusetzen.

Alle genannten Ziele sind für eine oberste Landesbehörde relevant, sowohl die Datenschutzziele als auch das Management und Revisionsziele.

Im Kontext der Digitalisierung und dem Austausch von Daten zwischen Behörden und Bürgern/Wirtschaft sind Nicht-Abstreibarkeit und Vertrauen wichtig.

Im Kontext der IT Systemstabilität sind Anforderungen wie Widerstandsfähigkeit (Verlässlichkeit), Nachvollziehbarkeit (Revisionsfähigkeit) von großer Bedeutung.

Diese Schutzziele sind aus meiner Sicht alle relevant für eine Behörde, die erfolgreich ein ISMS betreiben möchte. Denn jede Behörde hat das Ziel integer und bürgerfreundlich zu arbeiten, natürlich auch eine oberste Landesbehörde.

Die  Schutzziele  'Vertraulichkeit',  'Integrität'  und  'Verfügbarkeit'  sind  ausreichend. Sie decken die oben genannten Schutzziele weitestgehend mit ab

Frage 14: Können Sie Anforderungen an ein IT-Grundschutz-Profil für eine oberste Landesbehörde formulieren?

## Antworten

Es sollte alle Bausteine beinhalten, die für die Implementierung der Informationssicherheit in einem IT-Verbund notwendig sind, welcher die Geschäftsprozesse beinhaltet, die typischerweise in einer obersten Landesbehörde abgewickelt werden

Im Polizeibereich wird im Rahmen einer Arbeitsgruppe ein solches Grundschutzprofil

zurzeit erarbeitet. An einer Erstellung eines entsprechenden Profils für eine oberste Landesbehörde habe ich Interesse. Anforderungen kann ich spontan nicht nennen.

Aufgrund des aktuellen Projektstatus noch keine Antwort möglich. Besonderheiten eines Ministeriums sind möglicherweise ein hoher Anteil bzw. Bedeutung mobiler Geräte (Laptops, Tablets, Smartphones), überproportional hohe Anforderungen an Verfügbarkeit (nicht im Sinne einer Abwägung, wie bei Nr. 3) und der geringe Einsatz von Fachanwendungen (dafür Bürokommunikation, eAkte). Schwerpunkte für den IT-Grundschutz finden sich eher im Clientbereich (soweit Server bei einem staatlichen Dienstleister zentralisiert sind).

Die Punkte Sicherheitsmanagement, Personal und Organisation, Gebäude, Datensicherheit, IT-Administration, Patch- und Änderungsmanagement, Schutz vor Schadprogrammen,  allgemeine  Office-Programme  und  Fachanwendungen  können  beispielhaft aufgezählt werden. Ein Anspruch auf Vollständigkeit besteht nicht, da auch 6/8 landesweit bzw. Ministerien übergreifend Anforderungen definiert werden. Dieser Prozess ist noch nicht abgeschlossen.

Als Grundstruktur schlagen wir folgendes vor:

- Festlegung des Anwendungsbereichs,
- Durchführung einer verallgemeinerten Strukturanalyse,

<!-- page: 135 -->

- Schutzbedarfsfeststellung und Modellierung für diesen Bereich,

- Auswahl und Anpassung von umzusetzenden IT-Grundschutz-Bausteinen

- Beschreibung spezifischer Sicherheitsanforderungen und -Maßnahmen.

Zudem gehören sämtliche Bausteine dazu, die von den geschäftskritischen Verfahren zu nutzen sind.

Das  größte  Augenmerk  bei  einem  Grundschutzprofil  für  eine  oberste  Landesbehörde sollte dem Compliance Management (System) gegeben werden. Compliance, Datenschutz und Informationssicherheit  lassen sich  in  einem  Managementsystem kombinieren und nutzen viele gleiche Daten und Prozesse.

IT- Betrieb für die kommende Digitalisierung bei zunehmender Virtualisierung sind nicht länger Kernaufgabengebiete von Behörden oder Verwaltungen. Diese Kompetenz ist zunehmend auch nicht wirtschaftlich in Behörden oder eigens geschaffenen IT-Behörden darstellbar.

Das Outsourcing mit Compliance Management sind demnach die zu gestaltenden Bereiche eines Verwaltungsprofils.

## Frage 15: Gab oder gibt es bei der Umsetzung des ISMS Probleme in Ihrer Institution? Bitte erläutern Sie die Ihrer Einschätzung nach schwerwiegendsten Probleme.

## Antworten

1. Awareness der Führungskräfte für Informationssicherheit ist kaum vorhanden und wenn es vorhanden ist, dann sind falsche Vorstellungen weit verbreitet. Die oder der ISB werden nicht als Berater auf Augenhöhe der Verwaltungsspitze akzeptiert.

2. Informationssicherheit ist in der Organisation häufig noch im IT-Management angesiedelt und hat somit keine unabhängige Position zur Prüfung und Beratung.

3. Die Ressourcenausstattung ist unzureichend.

4. Die Steuerung des IT-Bereichs (und damit auch der Informationssicherheit) durch Dienstleister wird durch zunehmendes Outsourcing begünstigt. Damit werden Probleme nicht gelöst, sondern 'wegdelegiert'."

Personalaufwand und - bedarf für die Umsetzung des Projekts.

Die Organisatorischen Maßnahmen in den Ressorts (Besetzung der Rolle des behördlichen  Informationssicherheitsbeauftragten)  mit  ausreichenden  Kapazitäten stellt immer noch die größte Herausforderung dar. Zudem sehen einige Ressortleitungen den Stellenwert der Informationssicherheit als viel zu gering an.

Das schwerwiegendste Problem des ISMS, ist die fehlende Aufmerksamkeit für das Thema im C-Level. Politisch uninteressant wird dem Thema auf keiner Verwaltungsebene Aufmerksamkeit zu Teil.

Andere Probleme sind ausschließlich Folgewirkungen.

Bis jetzt sind noch keine Probleme aufgetreten.

Größte anfängliche Herausforderung ist die Überzeugung der Stakeholder. Das erfolgt  durch unterschiedliche zielgruppenorientierte Informations- und Sensibilisierungsmaßnahmen. Dabei ist zu berücksichtigen, dass die Implementierung der Informationssicherheit ein langwieriger Prozess ist. Ziel muss es sein, Informationssicherheit zu einem selbstverständlichen Element jeglichen Handelns zu verankern.

<!-- page: 136 -->

## Anhang B IT-Grundschutz-Profil

## IT-Grundschutz-Profil für die obersten Landesbehörden Deutschlands

Autor:

Institution:

Veröffentlichungsstatus:

Version:

Datum:

Raphael Grieger

FH Hagenberg

Final

1.0

31.05.2019

<!-- page: 137 -->

## Inhaltsverzeichnis

| Kapitel 1                                          | Management Summary                                 |   1 |                                                    |
|----------------------------------------------------|----------------------------------------------------|-----|----------------------------------------------------|
| Kapitel 2                                          | Geltungsbereich                                    |   2 |                                                    |
| Kapitel 3                                          | Betrachteter Informationsverbund                   |   3 |                                                    |
| Kapitel 4                                          | Referenzarchitektur                                |   4 |                                                    |
| 4.1                                                | Geschäftsprozesse                                  |   4 |                                                    |
| 4.2                                                | Anwendungen                                        |   4 |                                                    |
| 4.3                                                | IT-Systeme                                         |   5 |                                                    |
| 4.4                                                | Netze- und Kommunikation                           |   5 |                                                    |
| 4.5                                                | Räumliche Infrastruktur                            |   5 |                                                    |
| 4.6                                                | Netzplan                                           |   7 |                                                    |
| Kapitel 5                                          | Modellierung des Informationsverbunds              |   8 |                                                    |
| 5.1                                                | Kreuzreferenztabelle                               |   8 |                                                    |
| 5.2                                                | Prozess-Bausteine                                  |   9 |                                                    |
|                                                    | 5.2.1 Schicht ISMS                                 |   9 |                                                    |
|                                                    | 5.2.2 Schicht ORP                                  |   9 |                                                    |
|                                                    | 5.2.3 Schicht CON                                  |  10 |                                                    |
|                                                    | 5.2.4 Schicht OPS                                  |  10 |                                                    |
|                                                    | 5.2.5 Schicht DER                                  |  10 |                                                    |
| 5.3                                                | System Bausteine                                   |  11 |                                                    |
|                                                    | 5.3.1 Schicht APP                                  |  11 |                                                    |
|                                                    | 5.3.2 Schicht SYS                                  |  11 |                                                    |
|                                                    | 5.3.3 Schicht NET                                  |  12 |                                                    |
|                                                    | Schicht INF                                        |  12 |                                                    |
| Kapitel 6 Schutzbedarfe                            | Kapitel 6 Schutzbedarfe                            |  13 | Kapitel 6 Schutzbedarfe                            |
| 6.1                                                | Schutzbedarfskategorien                            |  13 |                                                    |
| 6.2 Schutzbedarfsfeststellung                      | 6.2 Schutzbedarfsfeststellung                      |  14 |                                                    |
|                                                    | 6.2.1 Schutzziel Vertraulichkeit                   |  14 |                                                    |
|                                                    | 6.2.2 Schutzziel Integrität                        |  16 |                                                    |
|                                                    | 6.2.3 Schutzziel Verfügbarkeit                     |  18 |                                                    |
| 6.3                                                | Zielobjekte für die Risikoanalyse                  |  21 |                                                    |
| Kapitel 7 Risikobetrachtung relevanter Zielobjekte | Kapitel 7 Risikobetrachtung relevanter Zielobjekte |  22 | Kapitel 7 Risikobetrachtung relevanter Zielobjekte |
| 7.1 Risikokriterien                                | 7.1 Risikokriterien                                |  22 | 7.1 Risikokriterien                                |
| 7.2 Risikoappetit einer obersten Landesbehörde     | 7.2 Risikoappetit einer obersten Landesbehörde     |  22 | 7.2 Risikoappetit einer obersten Landesbehörde     |
|                                                    | 7.2.1 Risikomatrix                                 |  23 |                                                    |
|                                                    | 7.2.2 Bewertungskategorien der                     |  23 |                                                    |
|                                                    | Risikoanalyse                                      |  24 |                                                    |

24

<!-- page: 138 -->

| 7.3.1     | Gefährdungen für den Dateiserver             |   25 |
|-----------|----------------------------------------------|------|
| 7.3.2     | Risikoeinschätzung und Risikobewertung       |   26 |
| 7.3.3     | Risikobehandlung                             |   27 |
| Kapitel 8 | Anwendungshinweise                           |   31 |
| 8.1       | Andere IT-Grundschutz-Profile                |   31 |
| 8.2       | Internationale ISMS-Standards                |   31 |
| 8.3       | Weiterentwicklung des IT-Grundschutz-Profils |   31 |
| Kapitel 9 | Literatur                                    |   32 |

<!-- page: 139 -->

## Kapitel 1 Management Summary

Dieses IT-Grundschutz-Profil bildet die Anforderungen einer Sicherheitskonzeption einer obersten Landesbehörde in Deutschland für die Absicherung des Geschäftsprozesses der 'Beteiligung an der Normsetzung des Landes' nach der Standard -Absicherung ab. Dazu wird die für den Geschäftsprozess benötigte Referenzarchitektur dargestellt und mit den IT-Grundschutz-Bausteinen modelliert. Zudem werden die Schutzbedarfe der Zielobjekte aufgelistet und es wird eine schematische Risikoanalyse und - behandlung des Dateiservers  angefertigt. Neben den Anforderungen der IT-Grundschutz-Bausteine werden Anmerkungen von Verantwortlichen für Informationssicherheit aufgeführt, die spezifisches Wissen aus diesem Anwendungsbereich der Informationssicherheit widerspiegeln.

Durch diese schematische Sicherheitskonzeption wird die Umsetzung einer Standard-Absicherung der Beteiligung an der Normsetzung des Landes durch die Vorauswahl passender IT-Grundschutz-Bausteine vereinfacht. Nach der Modellierung wird zudem eine  Risikoanalyse  des  Dateiservers  aufgrund  eines  erhöhten  Schutzbedarfes durchgeführt. Diese Risikoanalyse führt zu der Feststellung zusätzlicher Maßnahmen, um dem erhöhten Schutzbedarf des Zielobjektes gerecht zu werden.

Die  Anwender  dieses  IT-Grundschutz-Profils  können  die  festgestellten  Zielobjekte, Schutzbedarfe und Anforderungen als Grundlage für ihre Sicherheitskonzeption verwenden und individuell auf ihre Organisation anpassen. Die Landesrechnungshöfe als oberste Landesbehörden werden aufgrund divergierender Aufgaben und der gesetzlichen Unabhängigkeit von dem IT-Grundschutz-Profil nicht umfasst.

<!-- page: 140 -->

## Kapitel 2 Geltungsbereich

Gemeinhin stellen die obersten Landesbehörden einen zentralen Teil der Landesverwaltungen  dar  und  werden  als  Ministerien,  Senate  oder  Staatskanzleien  bezeichnet. Diese Behörden bilden in den Ländern, unter der Leitung des Ministerpräsidenten und der jeweiligen Minister*innen, die höchste Verwaltungsebene [1, S.50].

Für  die  Absicherung  ihres  Informationsverbundes  sollen  die  Verwaltungen  des Bundes und der Länder, gemäß der Leitlinie für die Informationssicherheit in der öffentlichen Verwaltung vom 06.12.2018 (ISLL-Bund) ein Informationssicherheitsmanagementsystem (ISMS) betreiben und dort insbesondere eine Sicherheitskonzeption erstellen und umsetzen. Dazu wird in der ISLL-Bund die ISO 2700x-Reihe sowie der ITGrundschutz als Mindeststandard definiert. Ausgenommen sind die Landesrechnungshöfe, die Landesdatenschutzbeauftragten und die Verwaltungen der Landtage. Daher werden  diese  Institutionen  von  dem  IT-Grundschutz-Profil  nicht  betrachtet,  auch wenn die Landesrechnungshöfe im weiteren Sinne zu den obersten Landesbehörden gezählt werden [2, S. 96].

Dieses IT-Grundschutz-Profil wendet die Methodik der Standard-Absicherung gemäß dem BSI-Standard 200-2 an, um die Umsetzung eines ISMS in einer obersten Landesbehörde  durch  ein  schematische  Sicherheitskonzeption  zu  unterstützen.  Wie  im Standard 200-2 angeführt, und vom Bundesamt für Sicherheit in der Informationstechnik (BSI) in einer Referenztabelle weiter konkretisiert [3], ist die Standard-Absicherung des IT-Grundschutzes kompatibel zu dem ISO/IEC Standard 27001:2013. Dies trifft daher auch auf die Umsetzung dieses IT-Grundschutz-Profils zu, sofern für die Institution ein entsprechender Anwendungsbereich des ISMS definiert ist und organisationsspezifische Anpassungen getroffen wurden. Weiterhin kann über die Anwendung dieses IT-Grundschutz-Profils der Verpflichtung nach dem Betrieb eines ISMS und der Umsetzung der Sicherheitskonzeption nach der ISLL-Bund nachgekommen werden.

Dieses IT-Grundschutz-Profil verwendet stets die Begrifflichkeiten des IT-Grundschutzes. Selbiges gilt für methodische Angaben, wie die Verwendung der Worte MUSS und SOLL im Bezug zu einer Sicherheitsanforderung. Eine umfassende Begriffsdefinition befindet sich im Glossar des aktuellen IT-Grundschutz-Kompendiums.

<!-- page: 141 -->

## Kapitel 3 Betrachteter Informationsverbund

Die Zuständigkeiten und Geschäftsbereiche der obersten Landesbehörden weichen auf Grund unterschiedlicher politischer Konstellationen und der grundsätzlichen Souveränität der Länder [4, S. 35] voneinander ab. Daher wird in diesem IT-Grundschutz-Profil keine tiefergehende Definition der Geschäftsprozesse vorgenommen, sondern es wird ein  allgemein  formulierter  Geschäftsprozess  betrachtet,  der  aus  den  Aufgaben  der obersten Landesbehörden hergeleitet wird. Abstrakt formuliert nehmen die obersten Landesbehörden folgende Aufgaben wahr:

1. Das Erlassen von Verordnungen, Erlassen und die Mitarbeit an Gesetzen.
2. Die Ausführung von Bundes- und Landesgesetzen, sofern diese nicht an nachgeordnete Behörden delegiert ist.
3. Die (politische) Unterstützung des Ministers oder der Ministerin durch Informationsbeschaffung und sonstige Tätigkeiten.
4. Die  Selbstverwaltung  der  Behörde  durch  strategische  Planung,  Pressearbeit und Personalsachen.
5. Die Aufsicht über nachgeordnete Behörden.
6. Die Wahrnehmung von sonstigen Aufgaben, wie Beantwortung von parlamentarischen Anfragen, Koordination von ressortübergreifenden Aufgaben sowie Öffentlichkeitsarbeit.

Insbesondere aus der ersten Aufgabengruppe wird der generische Geschäftsprozess der Beteiligung an der Normsetzung des Landes generiert und in einer Standard-Absicherung betrachtet. Dieser Geschäftsprozess umfasst, nicht abschließend aufgezählt, folgende Tätigkeiten:

- Die Kommunikation mit anderen Behörden, wie Kommunen und obersten Landesbehörden,  zur  Abstimmung  der  Inhalte  in  Gesetzgebungs-,  Verordnungs- und Erlassverfahren.
- Wahrnehmung interner Kommunikationswege für die Steuerung der Aufgaben und Tätigkeiten sowie deren Bearbeitung im eigenen Bereich.
- Die  fachliche  Mitarbeit  an  den  verschiedenen  Normtypen,  unter  anderem durch die Erstellung von Gutachten und Stellungnahmen sowie die Ausarbeitung von Vorschlägen und Konzepten.

In den Folgekapiteln werden die für diesen Geschäftsprozess benötigten Zielobjekte in einer Referenzarchitektur aufgeführt, mit den IT-Grundschutz-Bausteinen modelliert und einer Schutzbedarfsfeststellung unterzogen. Zunächst wird der Informationsverbund in Form der Zielobjekte für diesen Geschäftsprozess dargestellt. Dabei ist zu bedenken,  dass  alle  Landesverwaltungen  Anteile  der  IT-Infrastruktur  an  externe  IT- Dienstleister ausgelagert haben [5, S. 101]. In diesem IT-Grundschutz-Profil wird aufgrund  unterschiedlicher  Auslagerungsmodelle  grundsätzlich  von  keiner  Auslagerung ausgegangen. Wenn relevante Zielobjekte der Sicherheitskonzeption ausgelagert sind, müssen die entsprechenden Verantwortlichen die Anforderungen der Sicherheitskonzeption angepasst umsetzen. Weiteres dazu lässt sich dem IT-Grundschutz-Baustein OPS.2.1 (Outsourcing für Kunden) entnehmen.

<!-- page: 142 -->

Grundsätzlich  werden  andere  Aufgaben  einer  obersten  Landesbehörde  ähnliche IT-Ressourcen benötigen und indirekt mit abgebildet sein. Dem Umfang dieser Ausarbeitung ist es geschuldet, dass an dieser Stelle nicht weiter auf diesen Umstand eingegangen wird. Bei Erstellung der Sicherheitskonzeption besteht allerdings für jeden Anwender die Prüfungsmöglichkeit, ob weitere Geschäftsprozesse so bereits abgedeckt werden oder ohne großen Mehraufwand abgedeckt werden können. Eine Risikoanalyse ist im Kontext der eigenen Organisation stets durchzuführen und wird hier nur beispielhaft für das Zielobjekt des Dateiservers aufgeführt.

<!-- page: 143 -->

## Kapitel 4 Referenzarchitektur

Bei  der  Darstellung  der  Referenzarchitektur  wird  davon  ausgegangen,  dass  von  den obersten Landesbe hörden für diese 'konzeptionelle' Arbeit [6, S. 15] entweder Anwendungen der Bürokommunikation oder ein Vorgangsbearbeitungs- bzw. Dokumentenmanagementsystem  (VBS;  DMS)  genutzt  werden.  In  diesem  IT-Grundschutz-Profil werden die Anwendungen der Bürokommunikation als zentrale Komponente zur Aufgabenerfüllung angenommen. Zusätzlich dazu werden in der Referenzarchitektur die Zielobjekte festgestellt, die zum Betrieb der Anwendungen der Bürokommunikation, der Nutzerverwaltung und der Aufgabenwahrnehmung benötigt werden.

Die Beschreibungen der Zielobjekte sind weitestgehend dem Lexikon der Informatik von Fischer [7] entnommen und sind nur im Bedarfsfall durch den Autor angepasst. Zum  Teil  enthält  diese  Aufzählung  konkrete  Soft-  oder  Hardwareprodukte  (bspw. Windows 10 und Microsoft Exchange). Diese wurden aufgrund ihrer aktuellen Verbreitung in der heutigen IT-Landschaft, insbesondere in den öffentlichen Verwaltungen, ausgewählt (siehe u.a. [8 - 10]) und sind über die IT-Grundschutz-Bausteine modelliert.

## 4.1 Geschäftsprozesse

| ID    | Was                                           | Beschreibung                                                                                                                                        |
|-------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| PRO01 | Beteiligung an der Normset- zung des Lan- des | Die oberste Landesbehörde beteiligt sich an dem lan- desinternen Gesetzgebungsprozess, dem Erlassen von Verordnungen und dem fertigen von Erlassen. |

## 4.2 Anwendungen

| ID    | Was                         | Beschreibung                                                                                                                                                                                                                                                                                                |
|-------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APP01 | Betriebssys- tem Windows 10 | Für den Betrieb eines komplexen Rechners notwendiges Programm zur Verwaltung seiner Betriebsmittel, zur Da- tenkommunikation mit der Peripherie, als Verbindungs- glied zwischen Anwender und Applikation. Hier ein weit verbreitetes Produkt der Fa. Microsoft für den Privat- und Geschäftskundenbereich. |
| APP02 | Microsoft Office 2016       | Anwendungen für Textverarbeitung, E-Mail-Client, Er- stellen von Präsentationen, Tabellenkalkulationen.                                                                                                                                                                                                     |
| APP03 | Dateiserver                 | Ein zentral auf einer Servermaschine ausgeführtes Pro- grammsystem, das alle Teilnehmenden mit Dateien ver- sorgt und als Kollaborationsplattform dienen kann.                                                                                                                                              |
| APP04 | Web-Brow- ser Firefox       | Eine die HTML interpretierende Client-Applikation zum Durchsuchen und Präsentieren ausgewählter Bereiche wie FTP, Usenet und des World Wide Web.                                                                                                                                                            |

<!-- page: 144 -->

| APP05   | Verzeichnis- dienst Active Directory   | Zentrale, einheitliche Datenbank über sämtliche mensch- lichen und maschinellen Ressourcen einer vernetzten Ar- beitsumgebung sowie von Metadaten der ganzen IT einer Unternehmung: Namen, Adressen, Telefonnummern, Geräteparameter, Zugriffsrechte, Datenbeschreibungen, Spezifikationen, Routing-Informationen. Ziele eines Verzeichnisdienstes sind u. a. Single Sign-on- Lösungen, die unternehmensweite zentrale Pflege, die ein- heitliche Notation, ein vereinheitlichter Workflow, die mobile Datenverarbeitung oder die automatische Konfi- guration von Komponenten durch Herauslesen von In- formationen.   |
|---------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APP06   | Microsoft Exchange                     | Client/Server-Lösung zur Erledigung der Bürokommuni- kation (Telefax, Stimme, E-Mail, Termine, Kontaktadres- sen, Aufgaben) in einem Arbeitskollektiv unter zentraler Verwaltung. Der Server heißt Exchange, der Client (bei Microsoft) Outlook.                                                                                                                                                                                                                                                                                                                                                                        |
| APP07   | Public-Key Infrastruktur               | Zuständig für die authentische Übermittlung von Nach- richten und sichere Identifizierung von Sendern und Empfängern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## 4.3 IT-Systeme

| ID    | Was                                     | Beschreibung                                                                                                                                                                              |
|-------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYS01 | Windows-Ser- ver 2016                   | Eine dezidierte, gesicherte und gehärtete Serverma- schine, die zentralisiert Dienstleistungsprogramme für die Nutzer der Netzinfrastruktur bereitstellt.                                 |
| SYS02 | Arbeitsplatz- PC                        | Ein stationäre Datenverarbeitungseinheit, bestehend aus Prozessor, Primärspeicher, Netzwerkanbindung so- wie Ein-/Ausgabeeinheit.                                                         |
| SYS03 | Mobiler-PC                              | Eine mobile Datenverarbeitungseinheit, siehe auch Arbeits platz-PC.                                                                                                                       |
| SYS04 | Telefon                                 | Hardwaregerät zur Nutzung eines Fernsprechdienstes über das Telekommunikationsnetz                                                                                                        |
| SYS05 | Telefaxgerät                            | Endgerät zum Versand und Empfang von Telefaxen.                                                                                                                                           |
| SYS06 | Smartphones mit Android- Betriebssystem | Mobiltelefone mit eingebauten E-Mail-Funktionen, Web-Browser, Terminverwaltung und spezifischen Ap- plikationen für Mobile-Betriebssysteme.                                               |
| SYS07 | Netzwerk-Mul- tifunktionsgerät          | Kombinationsgerät, zur Erstellung von Papierdoku- menten und zur optischen Erfassung von Informatio- nen, die als Kontrastmuster (Druckschrift, Handschrift, Rasterbild, Foto) vorliegen. |

<!-- page: 145 -->

## 4.4 Netze- und Kommunikation

| ID    | Was                                           | Beschreibung                                                                                                                                                                                                                                                                                           |
|-------|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NET01 | Gebäudeverka- belung                          | Multifunktionale, vorwiegend für digitale Telefonie und Daten vorgesehene, Vollverkabelung des Behör- dengebäudes. Unter anderem zur Herstellung einer LAN-Verbindung.                                                                                                                                 |
| NET02 | Switch                                        | Vermittlungsgerät zur Weiterleitung von Daten in LAN unter der Herstellung von Direktverbindungen unter Verwendung der MAC-Adresse.                                                                                                                                                                    |
| NET03 | Router                                        | Intelligenter Brückenrechner auf der Vermittlungs- schicht (3) von OSI zwischen kompatiblen, aber nicht unbedingt gleichartigen Netzwerken (Unterschiede auf Schichten 1 oder 2) zu deren gegenseitiger In- tegration, zur Optimierung der Datenwege und zur Komprimierung der Daten vor dem Transfer. |
| NET04 | Firewall                                      | Oberbegriff für Sicherheitskonzepte, welche den Da- tenverkehr zwischen zwei TCP/IP Netzen mithören oder filtern.                                                                                                                                                                                      |
| NET05 | Internet-Zugang                               | Anbindung der Behörde an das Internet über eine Netzanbindung eines Providers.                                                                                                                                                                                                                         |
| NET06 | Telefondienst                                 | Fernsprechdienst über das Telekommunikationsnetz, i.d.R. unter der Nutzung von Voice-over-IP.                                                                                                                                                                                                          |
| NET07 | Telefaxdienst                                 | Fernkopierdienst in der Telekommunikation.                                                                                                                                                                                                                                                             |
| NET08 | Abgesicherter Netz-werk-Zu- gang über ein VPN | Durch strenge Authentisierung, Autorisierung und Verschlüsselung gesicherte und deshalb vertrauliche Koppelung zweier geschlossener Netzwerke über eine öffentliche und unsichere Netzwerkinfrastruktur.                                                                                               |

## 4.5 Räumliche Infrastruktur

| ID    | Was                                   | Beschreibung                                                                                                                                              |
|-------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| INF01 | Allgemeines Ge- bäude                 | Ein oder mehrere Dienstgebäude der Behörde.                                                                                                               |
| INF02 | Büroraum                              | Arbeitsplatz der Mitarbeiter der Behörde, ausgestattet mit einem stationären Telefon und einem Client-PC.                                                 |
| INF03 | Serverraum                            | Gesondert ausgerüsteter und abgesicherter Raum in- nerhalb des Gebäudes, der die Serverinfrastruktur ent- hält und über ein entsprechendes Klima verfügt. |
| INF04 | Präsentations- und Bespre- chungsraum | Räumlichkeit zur Besprechung mit mehreren (auch ex- ternen) Personen.                                                                                     |
| INF05 | Häuslicher Ar- beitsplatz             | Arbeitsplatz im privaten Bereich von Mitarbeitern, der über einen VPN-Zugriff in das Behördennetzwerk ver- fügt.                                          |
| INF06 | Drucker- und Kopierraum               | Mit einem Multifunktionsgerät ausgestatteter Raum, der Büroaufgaben wie Scans, Ausdrucke, Kopien und dergleichen vorgesehen ist.                          |

<!-- page: 146 -->

## 4.6 Netzplan

Die  zuvor  aufgelistete  Netzinfrastruktur  einer  obersten  Landesbehörde  ist  nun schematisch übersichtsweise dargestellt. Aufgrund unterschiedlicher Auslagerungsmodelle wird auf die Darstellung von ausgelagerten Anteilen des Informationsverbundes verzichtet. Für eine klare Struktur des Netzplans sind die Kürzel der Zielobjekte hier; soweit möglich, dargestellt. Auf die Hervorhebung der Netztrennung von Systemen mit hohem Schutzbedarf wird in der schematischen Darstellung verzichtet.

Abbildung 1: Netzplan des Informationsverbundes (eigene Darstellung)

<!-- image -->

<!-- page: 147 -->

## Kapitel 5 Modellierung des Informationsverbunds

In der Referenzarchitektur der obersten Landesbehörde werden die nachfolgenden ITGrundschutz-Bausteine für eine Standard-Absicherung empfohlen. Zunächst werden die IT-Grundschutz-Bausteine zu den festgestellten Zielobjekten in einer Kreuzreferenztabelle dargestellt.  Daraus ergibt  sich  in  einer  Kurzübersicht,  welche  IT-Grundschutz-Bausteine  verwendet  werden  und  welches  Zielobjekt  über  einen  IT-Grundschutz-Baustein abgesichert ist.

Anschließend werden die verwendeten IT-Grundschutz-Bausteine gruppiert nach dem IT-Grundschutz-Kompendium aufgezählt. Sofern vorhanden werden Anmerkungen zu bestimmten Bausteinen oder Anforderungen auf der Basis von Expertenmeinungen oder der Fachliteratur unter der jeweiligen Gruppe dargestellt. Neben den Anmerkungen  dieser  Ausarbeitung  können  zudem  die  Anmerkungen  des  IT-Grundschutz-Profils für Kommunalverwaltungen beachtet werden.

## 5.1 Kreuzreferenztabelle

In dieser Kreuzreferenztabelle ist dargestellt, welche unter Kapitel 4 aufgezählten Zielobjekte einem IT-Grundschutz-Baustein zugeordnet werden können. Dadurch kann ermittelt  werden,  ob  die  Absicherung  umfänglich  stattfindet.  Zudem  ist  dieser  Teilschritt vorbereitend für die Risikoanalyse, da diese zwangsweise Zielobjekte berücksichtigt, denen kein IT-Grundschutz-Baustein zugeordnet ist.

Kreuzreferenztabelle zwischen Zielobjekten und IT-Grundschutz-Bausteinen

| Anwendungen   | Anwendungen                                                        | Anwendungen                                                                                                                                                                                                                              |
|---------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID            | Zielobjekt                                                         | Bausteine                                                                                                                                                                                                                                |
| PRO01         | Allgemeiner Informati- onsverbund / Beteiligung an der Normsetzung | ISMS.1; OPS.1.1.2; OPS.1.1.3; OPS.1.1.4; OPS.1.1.5; OPS1.1.6; OPS.1.2.2; OPS.1.2.3; OPS.1.2.4; OPS.2.4 ORP.1; ORP.2; ORP.3; ORP.4; ORP.5 CON.1; CON.3; CON.4; CON.6; DER.1; DER.2.1; DER.2.2; DER.2.3; DER.3.1 DER.3.2; DER.4 SYS.3.2.2; |
| ID            | Zielobjekt                                                         | Bausteine                                                                                                                                                                                                                                |
| APP01         | Betriebssystem Windows 10                                          | SYS.2.1; SYS.2.2.3                                                                                                                                                                                                                       |
| APP02         | Microsoft Office 2016                                              | APP.1.1                                                                                                                                                                                                                                  |
| APP03         | Dateiserver                                                        | APP.3.3                                                                                                                                                                                                                                  |
| APP04         | Web-Browser Firefox                                                | APP.1.2                                                                                                                                                                                                                                  |

<!-- page: 148 -->

| APP05                   | Verzeichnisdienst Active Directory          | APP.2.1, APP.2.2                    |
|-------------------------|---------------------------------------------|-------------------------------------|
| APP06                   | Microsoft Exchange                          | APP.5.1; APP.5.2                    |
| APP07                   | Public-Key Infrastruktur                    | Kein spezieller Baustein vorhanden. |
| IT-Systeme              | IT-Systeme                                  | IT-Systeme                          |
| SYS01                   | Windows-Server 2016                         | SYS.1.1; SYS.1.2.3 (in Erstellung)  |
| SYS02                   | Arbeitsplatz-PC                             | SYS.2.1; SYS.2.2.3                  |
| SYS03                   | Mobiler-PC                                  | SYS.2.1; SYS.3.1; SYS.2.2.3         |
| SYS04                   | Telefon                                     | NET.4.1                             |
| SYS05                   | Telefaxgerät                                | NET.4.3                             |
| SYS06                   | Smartphones mit And- roid-Betriebssystem    | APP.1.4; SYS.3.2.1; SYS.3.2.4       |
| SYS07                   | Netzwerk-Multifunkti- onsgerät              | SYS.4.1                             |
| Netzwerkkomponenten     | Netzwerkkomponenten                         | Netzwerkkomponenten                 |
| NET01                   | Gebäudeverkabelung                          | NET.1.1                             |
| NET02                   | Switch                                      | NET.3.1                             |
| NET03                   | Router                                      |                                     |
| NET04                   | Firewall                                    | NET.3.2                             |
| NET05                   | Internet-Zugang                             | NET.1.1                             |
| NET06                   | Telefondienst                               | NET.4.2                             |
| NET07                   | Telefaxdienst                               | NET.4.3                             |
| NET08                   | Abgesicherter Netzwerk- Zugang über ein VPN | NET.3.3                             |
| Räumliche Infrastruktur | Räumliche Infrastruktur                     | Räumliche Infrastruktur             |
| INF01                   | Allgemeines Gebäude                         | INF.1; INF.3; INF.4                 |
| INF02                   | Büroraum                                    | INF.7                               |
| INF03                   | Serverraum                                  | INF.2                               |
| INF04                   | Präsentations- und Be- sprechungsraum       | INF.10                              |
| INF05                   | Häuslicher Arbeitsplatz                     | INF.8                               |
| INF06                   | Drucker- und Kopier- raum                   | Kein spezieller Baustein vorhanden. |

## 5.2 Prozess-Bausteine

## 5.2.1 Schicht ISMS

Die Basis-Anforderungen des Bausteins ISMS.1 MÜSSEN umgesetzt werden. Zusätzlich dazu SOLLTEN die Vorgaben der Standard-Absicherung dieses Bausteins umgesetzt werden. Wenn von der Umsetzung einer optionalen Anforderung abgesehen wird, so ist dies hinreichend zu begründen und entsprechend zu dokumentieren.

<!-- page: 149 -->

Zu den Anforderungen bestehen folgende Anmerkungen:

| Anforde- rung   | Titel                                             | Anmerkung                                    | Begründung                                                                                                   | Quelle              |
|-----------------|---------------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------|
| ISMS.1.A10      | Erstellung eine Sicher- heitskonzep- tion         | Die Anfor- derung MUSS um- gesetzt wer- den. | Gemäß der ISLL-Bund müssen die Verwaltun- gen des Bundes und der Länder Sicherheitskon- zeptionen erstellen. | ISLL- Bund          |
| ISMS.1.A12      | Management- Berichte zur Informati- onssicherheit | Die Anfor- derung MUSS um- gesetzt wer- den. | Diese Anforderungen stellen die erfolgreiche Umsetzung des ISMS in der Behörde sicher.                       | Exper- tenbei- trag |

## 5.2.2 Schicht ORP

Die Basis-Anforderungen der Bausteine ORP.1-ORP.5 MÜSSEN umgesetzt werden. Zusätzlich dazu SOLLTEN die Vorgaben der Standard-Absicherung dieser Bausteine umgesetzt werden. Wenn von der Umsetzung einer optionalen Anforderung abgesehen wird, so ist dies hinreichend zu begründen und entsprechend zu dokumentieren.

Folgende Anmerkungen bestehen zu den Anforderungen der Bausteine ORP.1 - ORP.5:

| Anforde- rung   | Titel                                | Anmerkung                                                                                                                                                            | Begründung                                                                                                                                                                                                                                        | Quelle                                                                                                                                                       |
|-----------------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ORP.4.A8        | Rege- lung des Pass- wortge- brauchs | Passwörter DÜRFEN NICHT im Klartext elektro- nisch gespeichert werden. Statt- dessen SOLLTE ein Prüfsum- menverfahren nach dem Stand der Technik ver- wendet werden. | Im Klartext abge- speicherte Benut- zer-Passwort- kombinationen können intern zu einem Missbrauch führen oder bei ei- nem Datenabfluss dem Angreifer weitere Möglich- keiten des Miss- brauchs unter dem Eindruck legiti- men Handelns einräumen. | Ein entsprechen- des Sicherungs- vorgehen wird in der ISO/IEC 27002:2013 [11, S. 27], der NIST SP 800-63B [12, S. 15] und der PCI DSS [13, S. 72] empfohlen. |

<!-- page: 150 -->

## 5.2.3 Schicht CON

Die Basis-Anforderungen der Bausteine CON.1, CON3, CON.4 und CON.6 MÜSSEN umgesetzt werden. Zusätzlich dazu SOLLTEN die Vorgaben der Standard-Absicherung dieser Bausteine umgesetzt werden. Wenn von der Umsetzung einer optionalen Anforderung abgesehen wird, so ist dies hinreichend zu begründen und entsprechend zu dokumentieren.

Folgende Anmerkungen bestehen zu den Anforderungen der Bausteine CON.1 - CON.7:

| Anforde- rung   | Titel                                       | Anmerkung                                  | Begründung                                                                                                                                                                                                            | Quelle                                                         |
|-----------------|---------------------------------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| CON.2.1.1       | Einleitung / Standard-Da- tenschutzmo- dell | Der Baustein CON.2 ist nicht anzuwen- den. | Für die Verwal- tungsbehörden gilt bereits das bundesweit etablierte Stan- dard-Daten- schutzmodell (SDM) und die entsprechende Datenschutzge- setzgebung. Da- her wird der Baustein hier als redundant be- trachtet. | IT-Grund- schutz Kom- pendium, Baustein CON.2 - Da- tenschutz. |

## 5.2.4 Schicht OPS

Die  Basis-Anforderungen  der  Bausteine  OPS.1.1.2-OPS1.1.6,  OPS.1.2.2,  OPS.1.2.3, OPS.1.2.4 und OPS.2.4 MÜSSEN umgesetzt werden. Zusätzlich dazu SOLLTEN die Vorgaben der Standard-Absicherung dieser Bausteine umgesetzt werden. Wenn von der Umsetzung einer optionalen Anforderung abgesehen wird, so ist dies hinreichend zu begründen und entsprechend zu dokumentieren.

Folgende Anmerkungen bestehen zu den Anforderungen der Bausteine OPS.1.1.2 - OPS.4:

Keine .

## 5.2.5 Schicht DER

Die Basis-Anforderungen der Bausteine DER.1,  DER.2.1, DER.2.2, DER.2.3, DER.3.1, DER.3.2 und DER.4 MÜSSEN umgesetzt werden. Zusätzlich dazu SOLLTEN  die  Vorgaben  der  Standard-Absicherung  dieser  Bausteine  umgesetzt  werden. Wenn von der Umsetzung einer optionalen Anforderung abgesehen wird, so ist dies hinreichend zu begründen und entsprechend zu dokumentieren.

<!-- page: 151 -->

Folgende Anmerkungen bestehen zu den Anforderungen der Bausteine DER.1 - DER.4:

Keine.

## 5.3 System-Bausteine

## 5.3.1 Schicht APP

Die  Basis-Anforderungen  der  nachfolgend  aufgezählten  Bausteine  der  Schicht  APP MÜSSEN umgesetzt werden. Zusätzlich dazu SOLLTEN die Vorgaben der StandardAbsicherung dieser Bausteine umgesetzt werden. Wenn von der Umsetzung einer optionalen Anforderung abgesehen wird, so ist dies hinreichend zu begründen und entsprechend zu dokumentieren.

Folgende Bausteine werden aufgrund der Referenzarchitektur angewandt:

- APP.1.1 - Office Produkte
- APP.1.2 - Web-Browser
- APP.1.4 - Mobile Anwendungen
- APP.2.1 - Allgemeiner Verzeichnisdienst
- APP.2.2 - Active Directory
- APP.3.3 - Dateiserver
- APP.5.1 - Allgemeine Groupware
- APP.5.2 - Microsoft Exchange und Outlook

Folgende Anmerkungen bestehen zu den Anforderungen der Schicht APP:

Keine .

## 5.3.2 Schicht SYS

Die  Basis-Anforderungen  der  nachfolgend  aufgezählten  Bausteine  der  Schicht  SYS MÜSSEN umgesetzt werden. Zusätzlich dazu SOLLTEN die Vorgaben der StandardAbsicherung dieser Bausteine umgesetzt werden. Wenn von der Umsetzung einer optionalen Anforderung abgesehen wird, so ist dies hinreichend zu begründen und entsprechend zu dokumentieren.

Folgende Bausteine werden aufgrund der Referenzarchitektur angewandt:

- SYS.1.1 - Allgemeiner Server
- SYS.1.2.3 - Windows Server 2016 (in Erstellung)
- SYS.1.8 - Speicherlösungen
- SYS.2.1 - Allgemeiner Client

<!-- page: 152 -->

- SYS.2.2.3 - Clients unter Windows 10
- SYS.3.1 - Laptops
- SYS.3.2.1 - Allgemeine Smartphones und Tablets
- SYS.3.2.2 - Mobile Device Management
- SYS.3.2.4 - Android
- SYS.3.3 - Mobiltelefon
- SYS.3.4 - Mobile Datenträger
- SYS.4.1 - Drucker, Kopierer und Multifunktionsgeräte

Folgende Anmerkungen bestehen zu den Anforderungen der Schicht SYS:

Keine.

## 5.3.3 Schicht NET

Die Basis-Anforderungen der nachfolgend aufgezählten Bausteine der Schicht NET MÜSSEN umgesetzt werden. Zusätzlich dazu SOLLTEN die Vorgaben der StandardAbsicherung dieser Bausteine umgesetzt werden. Wenn von der Umsetzung einer optionalen Anforderung abgesehen wird, so ist dies hinreichend zu begründen und entsprechend zu dokumentieren.

Folgende Bausteine werden aufgrund der Referenzarchitektur angewandt:

- NET.1.1 - Netzarchitektur und -design
- NET.1.2 - Netzmanagement
- NET.3.1 - Router und Switches
- NET.3.2 - Firewall
- NET.3.3 - VPN
- NET.4.1 - Telekommunikationsanlagen
- NET.4.2 - VoIP
- NET.4.3 - Telefaxgeräte und Telefaxserver

Folgende Anmerkungen bestehen zu den Anforderungen der Schicht NET:

Keine.

<!-- page: 153 -->

## 5.3.4 Schicht INF

Die  Basis-Anforderungen  der  nachfolgend  aufgezählten  Bausteine  der  Schicht  INF MÜSSEN umgesetzt werden. Zusätzlich dazu SOLLTEN die Vorgaben der StandardAbsicherung dieser Bausteine umgesetzt werden. Wenn von der Umsetzung einer optionalen Anforderung abgesehen wird, so ist dies hinreichend zu begründen und entsprechend zu dokumentieren.

Folgende Bausteine werden aufgrund der Referenzarchitektur angewandt:

- INF.1 - Allgemeines Gebäude
- INF.2 - Rechenzentrum sowie Serverraum
- INF.3 - Elektrotechnische Verkabelung
- INF.4 - IT-Verkabelung
- INF.7 - Büroarbeitsplatz
- INF.8 - Häuslicher Arbeitsplatz
- INF.10 - Besprechungs-, Veranstaltungs- und Schulungsräume

Folgende Anmerkungen bestehen zu den Anforderungen der Schicht SYS:

Keine.

<!-- page: 154 -->

## Kapitel 6 Schutzbedarfe

## 6.1 Schutzbedarfskategorien

Folgende Schutzbedarfskategorien werden für eine erste Schutzbedarfsfeststellung im Rahmen der Standard-Absicherung aus dem BSI-Standard 200-2 herangezogen [14, S. 106-107]:

## Normaler Schutzbedarf

|   7. | Verstoß gegen Ge- setze/ Vorschrif- ten/Verträge                | • Verstöße gegen Vorschriften und Gesetze mit ge- ringfügigen Konsequenzen. • Geringfügige Vertragsverletzungen mit maximal ge- ringen Konventionalstrafen.                                            |
|------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   8. | Beeinträchtigung des informationellen Selbstbestimmungs- rechts | • Es handelt sich um personenbezogene Daten, durch deren Verarbeitung der Betroffene in seiner gesell- schaftlichen Stellung oder in seinen wirtschaftlichen Verhältnissen beeinträchtigt werden kann. |
|   9. | Beeinträchtigung der persönlichen Unver- sehrtheit              | • Eine Beeinträchtigung erscheint nicht möglich.                                                                                                                                                       |
|  10. | Beeinträchtigung der Aufgabenerfüllung                          | • Die Beeinträchtigung würde von den Betroffenen als tolerabel eingeschätzt werden. • Die maximal tolerierbare Ausfallzeit liegt zwischen 24 und 72 Stunden.                                           |
|  11. | Negative Innen- oder Außenwirkung                               | • Eine geringe bzw. nur interne Ansehens- oder Ver- trauensbeeinträchtigung sind zu erwarten.                                                                                                          |
|  12. | Finanzielle Auswir- kungen                                      | • Der finanzielle Schaden bleibt für die Institution to- lerabel.                                                                                                                                      |

## Hoher Schutzbedarf

|   7. | Verstoß gegen Ge- setze/Vorschrif- ten/Verträge                 | • Verstöße gegen Vorschriften und Gesetze mit er- heblichen Konsequenzen. • Vertragsverletzungen mit hohen Konventionalstra- fen.                                                                              |
|------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   8. | Beeinträchtigung des informationellen Selbstbestimmungs- rechts | • Es handelt sich um personenbezogene Daten, bei deren Verarbeitung der Betroffene in seiner gesell- schaftlichen Stellung oder in seinen wirtschaftlichen Verhältnissen erheblich beeinträchtigt werden kann. |
|   9. | Beeinträchtigung der persönlichen Unver- sehrtheit              | • Eine Beeinträchtigung der persönlichen Unversehrt- heit kann nicht absolut ausgeschlossen werden.                                                                                                            |
|  10. | Beeinträchtigung der Aufgabenerfüllung                          | • Die Beeinträchtigung würde von einzelnen Be- troffenen als nicht tolerabel eingeschätzt. • Die maximal tolerierbare Ausfallzeitliegt zwischen drei und 24 Stunden.                                           |

<!-- page: 155 -->

|   11. | Negative Innen- oder Außenwirkung   | • Eine breite Ansehens- oder Vertrauensbeeinträchti- gung ist zu erwarten.                    |
|-------|-------------------------------------|-----------------------------------------------------------------------------------------------|
|   12. | Finanzielle Auswirkun- gen          | • Der Schaden bewirkt beachtliche finanzielle Ver- luste, ist jedoch nicht existenzbedrohend. |

## Sehr hoher Schutzbedarf

|   8. | Verstoß gegen Gesetze/ Vorschriften/Verträge                      | • Fundamentaler Verstoß gegen Vorschriften und Gesetze. • Vertragsverletzungen, deren Haftungsschäden rui- nös sind.                                             |
|------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   9. | Beeinträchtigung des in- formationellen Selbstbe- stimmungsrechts | • Es handelt sich um personenbezogene Daten, bei deren Verarbeitung eine Gefahr für Leib und Le- ben oder die persönliche Freiheit des Betroffenen gegeben ist.  |
|  10. | Beeinträchtigung der persönlichen Unver- sehrtheit                | • Gravierende Beeinträchtigungen der persönlichen Unversehrtheit sind möglich. • Gefahr für Leib und Leben.                                                      |
|  11. | Beeinträchtigung der Aufgabenerfüllung                            | • Die Beeinträchtigung würde von allen Betroffenen als nicht tolerabel eingeschätzt werden. • Die maximal tolerierbare Ausfallzeit ist kleiner als drei Stunden. |
|  12. | Negative Innen- oder Außenwirkung                                 | • Eine landesweite bis bundesweite Ansehens- oder Vertrauensbeeinträchtigung, eventuell sogar exis- tenzgefährdender Art, ist denkbar.                           |
|  13. | Finanzielle Auswirkun- gen                                        | • Der finanzielle Schaden ist für die Institution exis- tenzbedrohend.                                                                                           |
|  14. | Sonstige Auswirkungen                                             | • Der Bestand des Staates oder wesentliche Teile dessen könnten gefährdet werden.                                                                                |

## 6.2 Schutzbedarfsfeststellung

Nun werden die Schutzbedarfe der Zielobjekte bei der Umsetzung der Basis- und Standard-Anforderungen eingeschätzt und kurz kommentiert. Es wird dabei gemäß dem Standard 200-2 von dem Geschäftsprozess auf die Informationen, Anwendungen und den  weiteren  Informationsverbund  abgeleitet.  Für  die  Anwender  dieses  IT-Grundschutz-Profils ist zu beachten, dass es sich bei der Beteiligung an der Normsetzung des Landes um einen Geschäftsprozess handelt, der für gewöhnlich keine herausragenden Anforderungen an Vertraulichkeit, Integrität und Verfügbarkeit hat. Im Gegenteil, im Rahmen von Transparenzoffensiven wird dieser Geschäftsprozess in einigen Bundesländern zum größtmöglichen Teil öffentlich gehandhabt - was sich hier auf die Anforderungen der Vertraulichkeit auswirkt.

<!-- page: 156 -->

## 6.2.1 Schutzziel Vertraulichkeit

| ID    | Was                                           | Ver- trau- lich- keit   | Kommentar                                                                                                                                                                                                                                                                                                                                                                                         |
|-------|-----------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRO01 | Beteiligung an der Normset- zung des Lan- des | Nor- mal                | Die verschiedenen Normsetzungsprozesse der obersten Landesbehörden (Beteiligung an Ge- setzgebung, Verordnungen und Erlasse) weisen keine herausragenden Anforderungen an die Vertraulichkeit auf. In den vergangenen Jahren haben sich stattdessen weitere Transparenzten- denzen durchgesetzt [15, S. 165-166]. Bei einer unberechtigten Kenntnisnahme kommt es zu überschaubaren Konsequenzen. |
| ID    | Was                                           | Ver- trau- lich- keit   | Kommentar                                                                                                                                                                                                                                                                                                                                                                                         |
| APP01 | Betriebssys- tem Windows 10                   | Nor- mal                | Es wird über das Betriebssystem nur auf einen Geschäftsprozess mit einem normalen Schutz- bedarf eingewirkt. Die unberechtigte Kenntnis- nahme von Daten hat begrenzte Auswirkun- gen.                                                                                                                                                                                                            |
| APP02 | Microsoft Office 2016                         | Nor- mal                | Die Office-Anwendungen speichern lediglich temporär Daten zwischen und sind selbst nicht vertraulich zu behandeln. Es wird nur auf In- formationen mit normalem Schutzbedarf zuge- griffen.                                                                                                                                                                                                       |
| APP03 | Dateiserver                                   | Nor- mal                | Auf dem Dateiserver werden Dokumente dau- erhaft gespeichert und von berechtigten Perso- nen abgerufen. Die dort abgelegten Doku- mente enthalten Informationen, deren unbe- fugte Kenntnisnahme die Institution und dritte Personen im tolerierbaren Maße schädigen können.                                                                                                                      |
| APP04 | Web-Browser Firefox                           | Nor- mal                | Ein Web-Browser enthält selbst keine über den normalen Schutzbedarf hinausgehenden Infor- mationen. Besonders schützenswerte Weban- wendungen sind nicht vorhanden.                                                                                                                                                                                                                               |
| APP05 | Verzeichnis- dienst Active Directory          | Hoch                    | Der Verzeichnisdienst speichert Daten und Be- rechtigungen, die unter anderem für einen ord- nungsgemäßen Betrieb der IT und der Rechte- verwaltung verantwortlich sind. Eine Verlet- zung der Vertraulichkeit kann Betriebsausfälle und einen wesentlichen Nachteil für die Institu- tion bedeuten, sodass ein hoher Schutzbedarf besteht.                                                       |

<!-- page: 157 -->

| APP06   | Microsoft Exchange                        | Nor- mal              | Microsoft Exchange ergänzt die Office Pro- dukte als Kommunikations- und Planungsres- source. Da Informationen mit normalem Schutzbedarf verarbeitet werden, vererbt sich dieser Schutzbedarf auf dieses Zielobjekt.               |
|---------|-------------------------------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APP07   | Public-Key Infrastruktur                  | Hoch                  | Unberechtigte Kenntnisnahmen von spezifi- schen Informationen der Public-Key Infra- struktur (wie bspw. private Schlüssel) führen zu einer Störung der sicheren Kommunikation der Behörde. Daher liegt ein hoher Schutzbedarf vor. |
| ID      | Was                                       | Ver- trau- lich- keit | Kommentar                                                                                                                                                                                                                          |
| SYS01   | Windows- Server 2016                      | Hoch                  | Der Server bildet die Grundlage für dezidierte Serveranwendungen wie den Verzeichnisdienst, Microsoft Exchange und den Dateiserver. Es vererbt sich ein hoher Schutzbedarf.                                                        |
| SYS02   | Arbeitsplatz- PC                          | Nor- mal              | Von dem Arbeitsplatz-PC wird als Client über das Betriebssystem auf Daten zugegriffen, die einer normalen Vertraulichkeit unterliegen. Da- her liegt ein normaler Schutzbedarf vor.                                                |
| SYS03   | Mobile-PCs                                | Nor- mal              | Von dem Mobilen-PCs wird als Client über das Betriebssystem auf Daten zugegriffen, die einer normalen Vertraulichkeit unterliegen. Daher vererbt sich ein normaler Schutzbedarf.                                                   |
| SYS04   | Telefon                                   | Nor- mal              | Da Informationen mit normalen Schutzbedarf verarbeitet werden, vererbt sich dieser Schutz- bedarf des Geschäftsprozesses auf dieses Ziel- objekt.                                                                                  |
| SYS05   | Telefaxgerät                              | Nor- mal              | Da Informationen mit normalen Schutzbedarf verarbeitet werden, vererbt sich der normale Schutzbedarf des Geschäftsprozesses auf dieses Zielobjekt.                                                                                 |
| SYS06   | Smartphones mit Android- Betriebssys- tem | Nor- mal              | Da Informationen mit normalen Schutzbedarf verarbeitet werden, vererbt sich der normale Schutzbedarf des Geschäftsprozesses auf dieses Zielobjekt.                                                                                 |
| SYS07   | Netzwerk- Multifunkti- onsgerät           | Nor- mal              | Da Informationen mit normalen Schutzbedarf verarbeitet werden, vererbt sich der normale Schutzbedarf des Geschäftsprozesses auf dieses Zielobjekt.                                                                                 |
| ID      | Was                                       | Ver- trau- lich- keit | Kommentar                                                                                                                                                                                                                          |

<!-- page: 158 -->

| NET01   | Gebäudever- kabelung                        | Hoch                  | Es wird eine hohe Vertraulichkeit durch den Transport von Daten der PKI und des Ver- zeichnisdienstes vererbt.                                                                                                                                                       |
|---------|---------------------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NET02   | Switch                                      | Hoch                  | Ähnlich der Gebäudeverkabelung werden über den Switch besonders schützenswerte Daten der PKI und des Verzeichnisdienstes koordi- niert. Daraus entsteht ein hoher Schutzbedarf für dieses Objekt.                                                                    |
| NET03   | Router                                      | Nor- mal              | Eine Steuerung vertraulicher Informationen in das Internet ist nicht vorgesehen, sodass ein normaler Schutzbedarf besteht.                                                                                                                                           |
| NET04   | Firewall                                    | Hoch                  | Die Firewall-Regeln müssen vertraulich behan- delt werden, da sonst potenzielle Angreifer Möglichkeiten für eine System-Kompromittie- rung ausspähen können. Ein darauf basierender Angriff kann die Arbeitsfähigkeit der Behörde entschieden beeinträchtigen.       |
| NET05   | Internet-Zu- gang                           | Nor- mal              | Vertrauliche Informationen werden durch den Geschäftsprozess nicht verursacht, weshalb auch die Steuerung zu einem Internet-Provider von normalem Schutzbedarf ist.                                                                                                  |
| NET06   | Telefondienst                               | Nor- mal              | Da Informationen mit normalen Schutzbedarf verarbeitet werden, vererbt sich der normale Schutzbedarf des Geschäftsprozesses auch auf dieses Zielobjekt.                                                                                                              |
| NET07   | Telefaxdienst                               | Nor- mal              | Da Informationen mit normalen Schutzbedarf verarbeitet werden, vererbt sich hier ein norma-                                                                                                                                                                          |
| NET08   | Abgesicherter Netzwerk- Zugang über ein VPN | Nor- mal              | ler Schutzbedarf. Unberechtigte Kenntnisnahmen können bei diesem Zielobjekt zu Beeinträchtigungen füh- ren, bei denen gemäß des normalen Schutzbe- darfes keine schwerwiegende Folge eintreten sollte. Administrative Prozesse sind von der VPN-Verbindung getrennt. |
| ID      | Was                                         | Ver- trau- lich- keit | Kommentar                                                                                                                                                                                                                                                            |
| INF01   | Allgemeines Gebäude                         | Hoch                  | Es gilt das Vererbungsprinzip. In dem allgemei- nen Gebäude befindet sich auch der Server- raum. Zudem muss eine Akkumulation der Schutzbedarfe in Betracht gezogen werden. Es entsteht ein hoher Schutzbedarf.                                                      |
| INF02   | Büroraum                                    | Nor- mal              | Im Büroraum werden durch Mitarbeiter Daten normalem Schutzbedarf verarbeitet und mitun- ter in Papierform aufbewahrt.                                                                                                                                                |
| INF03   | Serverraum                                  | Hoch                  | Physischer Standort des Servers bzw. der Ser- ver, daher kommt der Vererbungs- sowie der                                                                                                                                                                             |

<!-- page: 159 -->

|       |                                           |          | Kumulationseffekt zum Tragen. Von hier aus werden wesentliche Dienste bereitgestellt.                                                                  |
|-------|-------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| INF04 | Präsentati- ons- und Be- sprechungs- raum | Nor- mal | Es werden hier keine besonders schützenswer- ten Daten verarbeitet und es stehen nur einge- schränkte IT-Ressourcen zur Verfügung.                     |
| INF05 | Häuslicher Arbeitsplatz                   | Nor- mal | Gemäß des Vererbungsprinzips ist von einer normalen Vertraulichkeit der Daten auszuge- hen, die an einem häuslichen Arbeitsplatz ver- arbeitet werden. |
| INF06 | Drucker- und Kopierraum                   | Nor- mal | Vererbung von dem Netzwerk-Multifunktions- gerät auf dem Schutzbedarf ' N ormal'.                                                                      |

## 6.2.2 Schutzziel Integrität

| ID    | Was                                           | Integri- tät   | Kommentar                                                                                                                                                                                                                                                                                                       |
|-------|-----------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRO01 | Beteiligung an der Normset- zung des Lan- des | Normal         | Der Geschäftsprozess behandelt Informati- onen, deren unberechtigte Veränderung to- lerierbare Beeinträchtigungen nach sich zieht.                                                                                                                                                                              |
| ID    | Was                                           | Integri- tät   | Kommentar                                                                                                                                                                                                                                                                                                       |
| APP01 | Betriebssys- tem Windows 10                   | Normal         | Auf dem Betriebssystem findet eine Verer- bung des normalen Schutzbedarfes des Ge- schäftsprozesses statt.                                                                                                                                                                                                      |
| APP02 | Microsoft Office 2016                         | Normal         | Aufgrund der temporären Datenspeiche- rung bedarf die Anwendung selbst keiner Absicherung der Integrität über den norma- len Schutzbedarf hinaus.                                                                                                                                                               |
| APP03 | Dateiserver                                   | Normal         | Die über den Dateiserver verwalteten Daten sollten nur durch berechtigte Personen bear- beitet werden. Die möglichen Auswirkungen unberechtigter oder falscher Änderungen sind im normalen Schutzbereich.                                                                                                       |
| APP04 | Web-Browser Firefox                           | Normal         | Der Web-Browser speichert lediglich tem- porär Daten zwischen und Bedarf selbst kei- nem Schutz der Integrität über das normale Maß hinaus.                                                                                                                                                                     |
| APP05 | Verzeichnis- dienst Active Directory          | Hoch           | Der Verzeichnisdienst ist verantwortlich für die sichere Authentifizierung und Bereitstel- lung von Ressourcen innerhalb der Be- hörde. Eine unberechtigte Veränderung kann unter anderem die Gesamtverfügbar- keit des Informationsverbundes bedeutend einschränken, weshalb ein hoher Schutzbe- darf besteht. |

<!-- page: 160 -->

| APP06   | Microsoft Exchange                        | Normal       | Da Informationen mit normalen Schutzbe- darf verarbeitet werden, vererbt sich der normale Schutzbedarf des Geschäftsprozes- ses auf dieses Zielobjekt.                                                                                                                        |
|---------|-------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APP07   | Public-Key Infrastruktur                  | Hoch         | Nachrichten können unberechtigt von drit- ten Personen als behördlich autorisiert dar- gestellt werden, sollte es zu einem Integri- tätsverlust kommen. Ferner können Daten- fehler in der PKI zu unlesbaren Nachrich- ten führen. Daraus ergibt sich ein hoher Schutzbedarf. |
| ID      | Was                                       | Integri- tät | Kommentar                                                                                                                                                                                                                                                                     |
| SYS01   | Windows- Server 2016                      | Hoch         | Es besteht hoher Schutzbedarf durch den Vererbungseffekt, der unter anderem durch den zum Dienstbetrieb benötigten Verzeich- nisdienst eintritt. Zudem werden weitere Dienste über den Server bereitgestellt.                                                                 |
| SYS02   | Arbeitsplatz- PC                          | Normal       | Über den Zugriff des Arbeitsplatz-PCs sind Veränderungen der normal schutzbedürfti- gen Daten möglich. Da eine Verfälschung dieser Daten tolerierbar ist, besteht ein nor- maler Schutzbedarf der Integrität.                                                                 |
| SYS03   | Mobiler-PC                                | Normal       | Der Mobile-PC hält selbst nur Daten vor, deren Veränderung dem normalen Schutz- bedarf unterliegt.                                                                                                                                                                            |
| SYS04   | Telefon                                   | Normal       | Das Telefon benötigt keiner weiteren Absi- cherung und hält keine Daten über den nor- malen Schutzbereich hinaus vor.                                                                                                                                                         |
| SYS05   | Telefaxgerät                              | Normal       | Das Telefaxgerät benötigt keiner weiteren Absicherung und hält keine Daten über den normalen Schutzbereich hinaus vor.                                                                                                                                                        |
| SYS06   | Smartphones mit Android- Betriebssys- tem | Normal       | Smartphones und Tablets sind für die Be- hördenzwecke angepasst und enthalten im Rahmen des Geschäftsprozesses keine Da- ten, die besonders in der Integrität zu schüt- zen sind.                                                                                             |
| SYS07   | Netzwerk- Multifunkti- onsgerät           | Normal       | Das Multifunktionsgerät ist vor unberech- tigten Zugriffen abgesichert sein und Integ- ritätsverletzungen hätten nur Folgen im Rahmen des normalen Schutzbedarfs.                                                                                                             |
| ID      | Was                                       | Integri- tät | Kommentar                                                                                                                                                                                                                                                                     |
| NET01   | Gebäudever- kabelung                      | Hoch         | Da Informationen mit hohem Schutzbedarf über die Gebäudeverkabelung transportiert werden, liegt ein hoher Schutzbedarf vor.                                                                                                                                                   |
| NET02   | Switch                                    | Hoch         | Auch besonders schützenswerte Datenver- arbeitungsprozesse werden über die Gebäu- deverkabelung durchgeführt und durch den                                                                                                                                                    |

<!-- page: 161 -->

|       |                                             |              | Switch im Netzwerk verteilt. Dieser erbt den hohen Schutzbedarf.                                                                                                                                                                    |
|-------|---------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NET03 | Router                                      | Normal       | Über den Router werden nur Informationen geleitet, die einem normalen Schutzbedarf unterliegen.                                                                                                                                     |
| NET04 | Firewall                                    | Hoch         | Die Firewall-Regeln dürfen auf keinen Fall unberechtigt verändert werden. Entspre- chende Eingriffe oder falsche Daten gefähr- den die Handlungsfähigkeit der Behörde au- ßerordentlich, weshalb ein hoher Schutzbe- darf entsteht. |
| NET05 | Internet-Zu- gang                           | Normal       | Der Internetzugang ist durch entsprechende Protokolle und Maßnahmen ausreichend ab- gesichert. Über diesen werden nur Informa- tionen des normalen Schutzbedarfs trans- portiert.                                                   |
| NET06 | Telefondienst                               | Normal       | Es werden Informationen mit normalen Schutzbedarf verarbeitet, für die Integrität vererbt sich der normale Schutzbedarf des Geschäftsprozesses auch auf dieses Zielob- jekt.                                                        |
| NET07 | Telefaxdienst                               | Normal       | Es werden Informationen mit normalen Schutzbedarf verarbeitet, für die Integrität vererbt sich der normale Schutzbedarf des Geschäftsprozesses auch auf dieses Zielob- jekt.                                                        |
| NET08 | Abgesicherter Netzwerk- Zugang über ein VPN | Normal       | Unberechtigte Veränderungen können bei diesem Zielobjekt zu Beeinträchtigungen führen, die aufgrund des normalen Schutz- bedarfes keine schwerwiegenden Folgen ha- ben.                                                             |
| ID    | Was                                         | Integri- tät | Kommentar                                                                                                                                                                                                                           |
| INF01 | Allgemeines Gebäude                         | Hoch         | In dem Gebäude werden grundsätzlich alle Informationen verarbeitet und es fungiert als Server- und Serverdienststandort. Es kommt zu einer Vererbung des hohen Schutzbedarfes.                                                      |
| INF02 | Büroraum                                    | Normal       | Normal eingestufte Arbeitsprozesse werden in den Büroräumen als Arbeitsplatz durch- geführt. Daher hat dieser einen normalen Schutzbedarf.                                                                                          |
| INF03 | Serverraum                                  | Hoch         | Vererbung des Schutzbedarfes von den dort betriebenen Servermaschinen und den da- rauf betriebenen Diensten wie dem Ver- zeichnisdienst.                                                                                            |

<!-- page: 162 -->

| INF04   | Präsentati- ons- und Be- sprechungs- raum   | Normal   | Im Präsentations- und Besprechungsraum stehen nur eingeschränkte IT-Ressourcen zur Verfügung, falsche und/oder unberech- tigt veränderte Informationen haben nur Auswirkungen in der normalen Schutzbe- darfskategorie.   |
|---------|---------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INF05   | Häuslicher Arbeitsplatz                     | Normal   | Der häusliche Arbeitsplatz hat im Rahmen des Geschäftsprozesses Zugriff auf Schutz- bedarfe im normalen Bereich. Dementspre- chend gestaltet sich der Schutzbedarf.                                                       |
| INF06   | Drucker- und Kopierraum                     | Normal   | Es findet eine Vererbung des normalen Schutzbedarfs vom Geschäftsprozess sowie von dem Multifunktionsgerät statt.                                                                                                         |

## 6.2.3 Schutzziel Verfügbarkeit

| ID    | Was                                          | Verfüg- barkeit   | Kommentar                                                                                                                                                                                                                                                                                                                                                                   |
|-------|----------------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRO01 | Beteiligung an der Norm- setzung des Lan-des | Normal            | Der Geschäftsprozess behandelt Informa- tionen, bei denen eine Einschränkung der Verfügbarkeit im tolerierbaren Bereich liegt.                                                                                                                                                                                                                                              |
| ID    | Was                                          | Verfüg- barkeit   | Kommentar                                                                                                                                                                                                                                                                                                                                                                   |
| APP01 | Betriebssys- tem Windows 10                  | Normal            | Über eine Internetverbindung oder ent- sprechend vorbereite Kopien kann die Software jederzeit neu zur Verfügung ge- stellt werden. Die Ausfallzeit ist im norma- len Schutzbereich                                                                                                                                                                                         |
| APP02 | Microsoft Office 2016                        | Normal            | Über eine Internetverbindung oder ent- sprechend vorbereite Kopien kann die Software jederzeit neu zur Verfügung ge- stellt werden. Längere Ausfallzeiten sind dadurch unwahrscheinlich und hätten nur Auswirkungen im normalen Bereich.                                                                                                                                    |
| APP03 | Dateiserver                                  | Hoch              | Ohne die Dateiverwaltung und Kollabora- tionsmöglichkeiten ist die Arbeitsfähigkeit der Behörde deutlich eingeschränkt, eine längere Ausfallzeit als einen Tag ist nicht akzeptabel. Eine Ausfallzeit von unter ei- ner Stunde ist dabei nicht einzuhalten, exis- tenzbedrohend ist ein Ausfall des Dateiser- vers ebenfalls nicht. Daher liegt ein hoher Schutzbedarf vor. |
| APP04 | Web-Browser Firefox                          | Normal            | Über eine Internetverbindung oder ent- sprechend vorbereite Kopien kann die Software jederzeit neu zur Verfügung ge- stellt werden. Ausfallzeiten sind dadurch                                                                                                                                                                                                              |

<!-- page: 163 -->

|       |                                           |                 | reduziert und im Eintrittsfalle im normalen schutzbedarf.                                                                                                                                                                                                                |
|-------|-------------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APP05 | Verzeichnis- dienst Active Directory      | Hoch            | Sollte der Verzeichnisdienst nicht verfüg- bar sein, ist die gesamte Aufgabenwahrneh- mung der Behörde gefährdet. Zugriffe auf Systeme, Dateien und andere Ressourcen sind nicht möglich. Dementsprechend ist eine Ausfallzeit von mehr als 24 Stunden nicht akzeptabel. |
| APP06 | Microsoft Exchange                        | Normal          | Ein temporärer Ausfall von Microsoft- Exchange ist tolerierbar, dieser betrifft In- formationen mit normalem Schutzbedarf. Andere Kommunikationsmittel stehen bei einem Ausfall gegebenenfalls zur Verfü- gung.                                                          |
| APP07 | Public-Key Infrastruktur                  | Hoch            | Die Public-Key Infrastruktur dient zur ver- bindlichen Kommunikation und muss dazu nahezu störungsfrei zur Verfügung stehen. Es kann eine Ausfallzeit von bis zu einem Tag toleriert werden, woraus sich ein hoher Schutzbedarf ergibt.                                  |
| ID    | Was                                       | Verfüg- barkeit | Kommentar                                                                                                                                                                                                                                                                |
| SYS01 | Windows- Server 2016                      | Hoch            | Durch die Vererbung von dem Dateiserver und dem Verzeichnisdienst liegt ein hoher Schutzbedarf der Verfügbarkeit vor.                                                                                                                                                    |
| SYS02 | Arbeitsplatz- PC                          | Normal          | Die benötigte Hardware kann als Ersatzteil eingelagert und bei Bedarf zur Verfügung gestellt werden. Es liegt ein normaler Schutzbedarf vor.                                                                                                                             |
| SYS03 | Mobiler-PC                                | Normal          | Der Mobile-PC fungiert als Client, die be- nötigte Hardware kann daher als Ersatzteil eingelagert und bei Bedarf zur Verfügung gestellt werden. Es liegt ein normaler Schutzbedarf vor.                                                                                  |
| SYS04 | Telefon                                   | Normal          | Das Telefon kann als Ersatzteil bereitge- stellt und bei Bedarf zeitnah ersetzt wer- den. Der Schutzbedarf geht nicht über die Stufe ' normal ' hinaus.                                                                                                                  |
| SYS05 | Telefaxgerät                              | Normal          | Das Telefaxgerät wird als Ersatzteil bereit- gestellt und bei Bedarf zeitnah ersetzt.                                                                                                                                                                                    |
| SYS06 | Smartphones mit Android- Betriebssys- tem | Normal          | Das Vorhalten von entsprechenden Ersatz- geräten und die Verarbeitung normaler In- formationen führt zu einem normalen Schutzbedarf.                                                                                                                                     |
| SYS07 | Netzwerk- multifunkti- onsgerät           | Normal          | Der Ausfall des Netzwerk-Multifunktions- geräts ist in die normale Schutzbedarfskate- gorie einzuordnen.                                                                                                                                                                 |

<!-- page: 164 -->

| ID    | Was                              | Verfüg- barkeit   | Kommentar                                                                                                                                                                                                                                                                 |
|-------|----------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NET01 | Gebäudever- kabelung             | Normal            | Eine Reparatur der Verkabelung bei einer Einschränkung kann zeitnah erfolgen und über das Vorhalten von entsprechenden Ersatzteilen und Leitungsplänen sicherge- stellt werden.                                                                                           |
| NET02 | Switch                           | Normal            | Ein Ersatzgerät wird vorgehalten und not- falls ausgetauscht. Konfigurationen lassen sich auf Datenträgern separat vorhalten und aufspielen. Die Verfügbarkeit liegt da- her im normalen Bereich.                                                                         |
| NET03 | Router                           | Normal            | Ersatzgeräte werden vorgehalten und not- falls ausgetauscht. Konfigurationen lassen sich auf Datenträgern separat vorhalten und aufspielen.                                                                                                                               |
| NET04 | Firewall                         | Hoch              | Die Firewall schützt jederzeit das Behör- dennetz gegen unberechtigte Zugriffe und andere sicherheitsrelevante Interaktionen. Eine Ausfallzeit von 24 Stunden ist nicht tolerabel, da in diesem Falle jegliche be- troffene Außenverbindungen unterbrochen werden müssen. |
| NET05 | Internet-Zu- gang                | Normal            | Ein Ausfall der Internetverbindung ist für 24 Stunden tolerierbar, die Aufgabenwahr- nehmung wird dadurch nur im angemesse- nen Maße eingeschränkt.                                                                                                                       |
| NET06 | Telefondienst                    | Normal            | Neben einer telefonischen Erreichbarkeit bestehen weitere Kommunikationskanäle für die Aufgabenwahrnehmung.                                                                                                                                                               |
| NET07 | Telefaxdienst                    | Normal            | Neben einer Erreichbarkeit per Telefax be- stehen weitere Kommunikationskanäle für die Aufgabenwahrnehmung und verbindli- che Kommunikation der Behörde.                                                                                                                  |
| NET08 | Autonomer Netzwerk- Zugang (VPN) | Normal            | Ein Ausfall der externen Netzwerkzugrif- fes ist für 24 Stunden tolerierbar, die Auf- gabenwahrnehmung wird dadurch im an- gemessenen Maße eingeschränkt                                                                                                                  |
| ID    | Was                              | Verfüg- barkeit   | Kommentar                                                                                                                                                                                                                                                                 |
| INF01 | Allgemeines Gebäude              | Hoch              | In dem Gebäude werden grundsätzlich alle Informationen verarbeitet und es fungiert als Serverstandort. Daher kommt es zu ei- ner Vererbung des hohen Schutzbedarfes.                                                                                                      |
| INF02 | Büroraum                         | Normal            | Ohne zur Verfügung stehende Büroräum- lichkeiten besteht keine Möglichkeit zur Aufgabenwahrnehmung. Allerdings ist eine dadurch verursachte Störung des Ge- schäftsprozesses im tolerierbaren Bereich.                                                                    |

<!-- page: 165 -->

| INF03   | Serverraum                                | Hoch   | Der Serverraum ist der zentrale Raum, der für die Erbringung der IT-Dienste im Dienstgebäude verantwortlich ist. Es kommt zu einer Vererbung des Schutzbe- darfes von den dort betriebenen Servern und den darauf betriebenen Diensten.   |
|---------|-------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INF04   | Präsentati- ons- und Be- sprechungs- raum | Normal | Es sind keine besonderen Schutzbedarfe des Präsentations- und Besprechungsraum hinsichtlich der Verfügbarkeit erkennbar.                                                                                                                  |
| INF05   | Häuslicher Arbeitsplatz                   | Normal | Es sind keine Schutzbedarfe des häuslichen Arbeitsplatzes über das normale Maß hin- aus hinsichtlich der Verfügbarkeit erkenn- bar.                                                                                                       |
| INF06   | Drucker- und Kopierraum                   | Normal | Der Schutzbedarf des Drucker- und Ko- pierraums ist im normalen Bereich.                                                                                                                                                                  |

<!-- page: 166 -->

## 6.3 Zielobjekte für die Risikoanalyse

## Übersichtstabelle von Zielobjekten, die in einer Risikoanalyse berücksichtigt werden müssen

| ID    | Was                                  | Vertraulich- keit                 | Integ- rität                      | Verfügbar- keit                   |
|-------|--------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| APP03 | Dateiserver                          | Normal                            | Normal                            | Hoch                              |
| APP05 | Verzeichnisdienst Active Di- rectory | Hoch                              | Hoch                              | Hoch                              |
| APP07 | Public-Key Infrastruktur             | Hoch                              | Hoch                              | Hoch                              |
| SYS01 | Windows-Server 2016                  | Hoch                              | Hoch                              | Hoch                              |
| NET01 | Gebäudeverkabelung                   | Hoch                              | Hoch                              | Normal                            |
| NET02 | Switch                               | Hoch                              | Hoch                              | Normal                            |
| NET06 | Firewall                             | Hoch                              | Hoch                              | Hoch                              |
| INF01 | Allgemeines Gebäude                  | Hoch                              | Hoch                              | Hoch                              |
| INF03 | Serverraum                           | Hoch                              | Hoch                              | Hoch                              |
| INF06 | Drucker- und Kopierraum              | Kein IT-Grundschutz-Baustein vor- | Kein IT-Grundschutz-Baustein vor- | Kein IT-Grundschutz-Baustein vor- |

<!-- page: 167 -->

## Kapitel 7 Risikobetrachtung relevanter Zielobjekte

## 7.1 Risikokriterien

Wie zuvor dargestellt, gibt es in der Referenzarchitektur einer obersten Landesbehörde neun Zielobjekte mit hohem Schutzbedarf und ein Zielobjekt ohne spezifischen ITGrundschutz-Baustein. Gemäß der IT-Grundschutz-Methodik müssen diese einer Risikoanalyse unterzogen werden. Aufgrund des Umfanges findet dabei im Rahmen dieser Ausarbeitung nur die Analyse eines Zielobjektes statt. Bei dem Zielobjekt handelt es sich um den Dateiserver. Dieser wurde ausgewählt, da er eine zentrale Bedeutung in dem betrachteten Geschäftsprozess hat und über einen erhöhten Schutzbedarf im Bereich der Verfügbarkeit verfügt.

Diese Risikobetrachtung behandelt eine schematisch existierende Organisation, so dass kein existierendes Zielobjekt in seiner tatsächlichen Konfiguration und Nutzung einer Risikoanalyse unterzogen wird. Dementsprechend orientieren sich die festgestellten Risiken nicht an tatsächlichen Gegebenheiten und können so keinen verbindlichen Charakter für die obersten Landesbehörden entwickeln - gemäß den Grundannahmen der ISO 31000:2018 ist die Risikoanalyse durch jede Organisation auf ihren spezifischen internen und externen Kontext anzuwenden [16, S. 3].

Ausgehend davon soll durch eine Organisation keine generische Risikoanalyse genutzt werden, um eine individuelle Betrachtung der eigenen Infrastruktur zu vermeiden. Diese Risikoanalyse hat somit exemplarischen Charakter, kann aber in ihrer Struktur und Formulierung als Leitfaden dienen. So wird neben den Risikokriterien, bei denen ein Rückgriff auf den BSI Standard 200-3 stattfindet, auch eine generische Risikomatrix dargestellt. Bezüglich der Risikokriterien wird auf die allgemeine Empfehlung des Standards 200-3 zurückgegriffen [17, S. 26-27]:

| Eintrittshäufigkeit   | Beschreibung                                                                     |
|-----------------------|----------------------------------------------------------------------------------|
| selten                | Ereignis könnte nach heutigem Kenntnisstand höchstens alle fünf Jahre eintreten. |
| mittel                | Ereignis tritt einmal alle fünf Jahre bis einmal im Jahr ein.                    |
| häufig                | Ereignis tritt einmal im Jahr bis ein- mal pro Monat ein.                        |
| sehr häufig           | Ereignis tritt mehrmals im Monat ein.                                            |

<!-- page: 168 -->

| Schadenshöhe/Schadensauswirkungen   | Beschreibung                                                                                      |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| vernachlässigbar                    | Die Schadensauswirkungen sind ge- ring und können vernachlässigt wer- den.                        |
| begrenzt                            | Die Schadensauswirkungen sind be- grenzt und überschaubar.                                        |
| beträchtlich                        | Die Schadensauswirkungen können beträchtlich sein.                                                |
| existenzbedrohend                   | Die Schadensauswirkungen können ein existenziell bedrohliches, kata- strophales Ausmaß erreichen. |

## 7.2 Risikoappetit einer obersten Landesbehörde

Der Risikoappetit der Behörde beschreibt die Motivation der Institution, Risiken einzugehen. Grundsätzlich steht es dabei jeder Behörde im Rahmen gesetzlicher und politischer Vorgaben und Verpflichtungen frei, den eigenen Risikoappetit festzulegen und Risiken nach eigenem Ermessen in Kauf zu nehmen.

Nichtsdestotrotz sollte in diesem Zusammenhang durch die Verantwortungsträger bedacht werden, dass es sich bei einer obersten Landesbehörde um eine zentrale Institution eines Landes handelt, die weitreichende Entscheidungen auf Landes- und über den Bundesrat - auch auf Bundesebene treffen kann. Daher wird für die hier dargestellte Behörde von einem geringen Risikoappetit ausgegangen.

## 7.2.1 Risikomatrix

Da es sich um eine Behörde handelt, wird von einer niedrigen Risikoaffinität ausgegangen, da das Eingehen von Risiken keine Vorteile bei einer Institution ohne Gewinnerzielungsabsicht bedeutet. Der Risikoappetit einer obersten Landesbehörde kann in einer Risikomatrix wie folgt dargestellt werden:

<!-- page: 169 -->

<!-- image -->

Eintrittshäufigkeit

Abbildung 2: Risikomatrix einer obersten Landesbehörde (eigene Darstellung auf Basis des BSI-Standards 200-3 [17, S. 27])

## 7.2.2 Bewertungskategorien der Risiken

| Risikokategorien nach Standard 200-3 [17, S. 28]   | Risikokategorien nach Standard 200-3 [17, S. 28]                                                                                                                                                                                              |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gering                                             | Die bereits umgesetzten oder zumindest im Sicherheitskonzept vorgesehe- nen Sicherheitsmaßnahmen bieten einen ausreichenden Schutz. In der Pra- xis ist es üblich, geringe Risiken zu akzeptieren und die Gefährdung den- noch zu beobachten. |
| mittel                                             | Die bereits umgesetzten oder zumindest im Sicherheitskonzept vorgesehe- nen Sicherheitsmaßnahmen reichen möglicherweise nicht aus. In absehba- rer Zeit sollten Maßnahmen geplant und umgesetzt werden.                                       |
| hoch                                               | Die bereits umgesetzten oder zumindest im Sicherheitskonzept vorgesehe- nen Sicherheitsmaßnahmen bieten keinen ausreichenden Schutz vor der je- weiligen Gefährdung.                                                                          |
| sehr hoch                                          | Die bereits umgesetzten oder zumindest im Sicherheitskonzept vorgesehe- nen Sicherheitsmaßnahmen bieten keinen ausreichenden Schutz vor der je- weiligen Gefährdung. In der Praxis werden sehr hohe Risiken selten akzep- tiert.              |

## 7.3 Risikoanalyse

Nachdem die Rahmenbedingungen für die Einschätzung und Behandlung von Risiken festgelegt sind, folgt nun die Risikoanalyse für schutzbedürftige Zielobjekte aus dem Informationsverbund der obersten Landesbehörde. In diesem IT-Grundschutz-Profil wurden mehrere schutzbedürftige Zielobjekte festgestellt, von denen hier Dateiserver betrachtet wird. Dazu ist in diesem Dokument eine dreiteilige Kapitelstruktur angelegt, die auf die Gefährdungsfeststellung, die Risikoidentifikation und -Einschätzung sowie die Risikobehandlung aufgeteilt ist.

<!-- page: 170 -->

Erweiterungen des IT-Grundschutz-Profils können diese Struktur aufgreifen und so weitere Zielobjekte einer Risikoanalyse unterziehen.

## 7.3.1 Gefährdungen für den Dateiserver

Folgende Gefährdungen bestehen für den Dateiserver [18, APP.3.3 S. 8]

| Ge- fähr- dung   | Titel                                                 | Schutz- ziel   | Beispiel                                                                                                                                                                            |
|------------------|-------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.14           | Ausspähen von In- formationen (Spio- nage)            | C              | Unberechtigte Personen könnten Zu- griff auf die abgelegten Daten erhalten und diese für Ihre Zwecke missbrau- chen.                                                                |
| G 0.16           | Diebstahl von Ge- räten, Datenträgern oder Dokumenten | C, A           | Aus dem Serverraum oder einem ande- ren Aufstellort für den Dateiserver könnten Festplatten mit sensiblen Da- ten entnommen werden.                                                 |
| G 0.18           | Fehlplanung oder fehlende Anpassung                   | C, I, A        | Der Dateiserver und das darunterlie- gende Server-Betriebssystem könnten falsch konfiguriert sein und so bspw. schnell überlasten oder unberechtigte Zugriffe zulassen.             |
| G 0.19           | Offenlegung schüt- zenswerter Infor- mationen         | C              | Durch einen berechtigten Benutzer wird die Zugriffsberechtigung falsch eingerichtet und ein unbestimmter Teil- nehmerkreis kann schützenswerte In- formationen zur Kenntnis nehmen. |
| G 0.21           | Manipulation von Hard- oder Soft- ware                | C, I, A        | Über Schwachstellen könnte der Datei- server manipuliert werden und so unbe- rechtigte Zugriffe ermöglichen.                                                                        |
| G 0.22           | Manipulation von Informationen                        | I              | Durch Fehler in den Berechtigungen o.ä. könnten Nutzer wesentliche Infor- mationen manipulieren.                                                                                    |
| G 0.23           | Unbefugtes Ein- dringen in IT-Sys- teme               | C, I           | Jemand könnte sich unberechtigt zum Dateiserver über fremde Zugangsdaten verschaffen.                                                                                               |

<!-- page: 171 -->

| Ge- fähr- dung   | Titel                                                                    | Schutz- ziel   | Beispiel                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.25           | Ausfall von Geräten oder Systemen                                        | A              | Hardwarefehler, die zum Teil schon in der Produktion entstehen, können zum zeitweiligen Ausfall des Dateiservers führen.                                                            |
| G 0.26           | Fehlfunktion von Geräten oder Syste- men                                 | C, I, A        | Unvorhergesehene Konflikte in den Konfigurationseinstellungen mit ande- ren IT-Systemen könnten zu einem Ausfall führen.                                                            |
| G 0.27           | Ressourcenmangel                                                         | A              | Es könnte zu Verzögerungen und Aus- fällen bei Zugriffen auf den Dateiserver kommen, weil dieser nicht mit ausrei- chen Kapazitäten versorgt ist.                                   |
| G 0.28           | Software-Schwach- stellen oder -Fehler                                   | C, I, A        | Der Dateiserver könnte z.T. unbe- kannte Sicherheitslücken beinhalten, die die Verletzungen der Sicherheitsziele ermöglichen.                                                       |
| G 0.30           | Unberechtigte Nut- zung oder Admi- nistration von Gerä- ten und Systemen | C, I, A        | Unberechtigte Personen könnten Zu- griff auf Administrationskonten erhal- ten und auf diesem Wege Zugriffe auf den Dateiserver unterbinden oder Da- ten entwenden.                  |
| G 0.31           | Fehlerhafte Nut- zung oder Admi- nistration von Gerä- ten und Systemen   | C, I, A        | Durch berechtigte Nutzer und Admi- nistratoren könnte der Dateiserver so verändert werden, dass es zu einem Ausfall kommt oder das Daten falsch preisgegeben bzw. verändert werden. |
| G 0.32           | Missbrauch von Be- rechtigungen                                          | C, I, A        | Unberechtigt zugeteilte Berechtigungen könnten von den jeweiligen Mitarbei- tern verwendet werden, um nicht für diese bestimmte Daten zu verwenden.                                 |
| G 0.39           | Schadprogramme                                                           | C, I, A        | Eine Infektion des Dateiservers mit ei- nem Schadprogramm könnte die Si- cherstellung der Sicherheitsziele gefähr- den.                                                             |
| G 0.40           | Verhinderung von Diensten (Denial of Service)                            | A              | Der Dateiserver könnte durch eine Vielzahl von missbräuchlich veranlass- ten Anfragen keine Zugriffe mehr ver- arbeiten und nicht mehr zur Verfügung stehen.                        |

<!-- page: 172 -->

| Ge- fähr- dung   | Titel                                              | Schutz- ziel   | Beispiel                                                                                                                                                |
|------------------|----------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.43           | Einspielen von Nachrichten                         | C, I           | Ein Angreifer könnte die Netzwerkver- bindungen des Dateiservers nutzen, um dort vorliegende Daten zu lesen, zu verändern oder unbrauchbar zu ma- chen. |
| G 0.44           | Unbefugtes Ein- dringen in Räum- lichkeiten        | C, I, A        | Unberechtigte Personen könnten zu dem Standort des Servers vordringen                                                                                   |
| G 0.45           | Datenverlust                                       | A              | Durch einen Serverausfall und invalide Datensicherungen könnten Daten un- wiederbringlichen verloren gehen.                                             |
| G 0.46           | Integritätsverlust schützenswerter In- formationen | I              | Falsche Konfigurationen seitens des Dateiservers könnten einem Angreifer ermöglichen diverse Daten unberech- tigt zu verändern.                         |

## 7.3.2 Risikoeinschätzung und Risikobewertung

Folgend ist das geschätzte Risiko einer obersten Landesbehörde zu den Gefährdungen eines Dateiserver ohne Etablierung eines ISMS. Dabei ist zu beachten, dass jede Institution unterschiedliche Risiken aufgrund der bereits bestehenden Sicherheitsmaßnahmen tragen wird und diese Risiken daher im Rahmen der eigenen Organisation betrachten muss.

Risikoeinschätzung und -Bewertung für den Dateiserver

| Ge- fähr- dung   | Titel                                                 | Schutz- ziel   | Eintritts- häufig- keit   | Auswir- kungen              | Risiko    |
|------------------|-------------------------------------------------------|----------------|---------------------------|-----------------------------|-----------|
| G 0.14           | Ausspähen von Infor- mationen (Spionage)              | C              | Mittel                    | Begrenzt                    | Gering    |
| G 0.16           | Diebstahl von Geräten, Datenträgern oder Do- kumenten | C, A           | Mittel bis häufig         | Beträchtlich                | Sehr Hoch |
| G 0.18           | Fehlplanung oder feh- lende Anpassung                 | C, I, A        | Mittel                    | Begrenzt bis be- trächtlich | Hoch      |
| G 0.19           | Offenlegung schüt- zenswerter Informatio- nen         | C              | Selten                    | Begrenzt                    | Gering    |

<!-- page: 173 -->

| Ge- fähr- dung   | Titel                                            | Schutz- ziel   | Eintritts- häufig- keit   | Auswir- kungen   | Risiko    |
|------------------|--------------------------------------------------|----------------|---------------------------|------------------|-----------|
| G 0.21           | Manipulation von Hard- oder Software             | C, I, A        | Selten                    | Beträchtlich     | Mittel    |
| G 0.22           | Manipulation von In- formationen                 | I              | Selten                    | Begrenzt         | Gering    |
| G 0.23           | Unbefugtes Eindringen in IT-Systeme              | C, I           | Selten                    | Beträchtlich     | Hoch      |
| G 0.25           | Ausfall von Geräten o- der Systemen              | A              | Mittel                    | Beträchtlich     | Hoch      |
| G 0.26           | Fehlfunktion von Ge- räten oder Systemen         | C, I, A        | Mittel                    | Beträchtlich     | Hoch      |
| G 0.27           | Ressourcenmangel                                 | A              | Häufig                    | Beträchtlich     | Sehr Hoch |
| G 0.28           | Software-Schachstellen oder -Fehler              | C, I, A        | Selten                    | Beträchtlich     | Mittel    |
| G 0.30           | Unberechtigte Nut- zung von Geräten und Systemen | C, I           | Selten                    | Beträchtlich     | Mittel    |
| G 0.31           | Fehlerhafte Nutzung von Geräten und Sys- temen   | C, I, A        | Häufig                    | Begrenzt         | Hoch      |
| G 0.32           | Missbrauch von Be- rechtigungen                  | C, I           | Häufig                    | Begrenzt         | Hoch      |
| G 0.39           | Schadprogramme                                   | C, I, A        | Mittel                    | Beträchtlich     | Sehr Hoch |
| G 0.40           | Verhinderung von Diensten (Denial of Service)    | A              | Mittel                    | Beträchtlich     | Hoch      |
| G 0.43           | Einspielen von Nach- richten                     | I              | Selten                    | Begrenzt         | Gering    |
| G 0.44           | Unbefugtes Eindringen in Räumlichkeiten          | C, I           | Mittel                    | Begrenzt         | Gering    |
| G 0.45           | Datenverlust                                     | A              | Mittel                    | Beträchtlich     | Hoch      |

<!-- page: 174 -->

| Ge- fähr- dung   | Titel                                              | Schutz- ziel   | Eintritts- häufig- keit   | Auswir- kungen   | Risiko   |
|------------------|----------------------------------------------------|----------------|---------------------------|------------------|----------|
| G 0.46           | Integritätsverlust schützenswerter Infor- mationen | I              | Selten                    | Begrenzt         | Gering   |

## 7.3.3 Risikobehandlung

Aufgrund des erhöhten Schutzbedarfes der Verfügbarkeit sind insbesondere zusätzliche Anforderungen zur Risikoreduktion zu etablieren. Durch den Anspruch an eine hohe Verfügbarkeit des Zielobjekts kommen dabei andere Risikobehandlungen wie eine Risikovermeidung oder ein Risikotransfer nur zum Teil in Frage. In diesem IT-Grundschutz-Profil  wird  daher  zunächst  eine  Risikobehandlung  auf  der  Basis  zusätzlicher Maßnahmen vorgenommen.

In der zusätzlichen Absicherung werden im Sinne der Übersichtlichkeit nur optionale Anforderungen für den erhöhten Schutzbedarf genannt und auf die grundlegenden Bausteine verwiesen. Die zusätzlichen Anforderungen sind in diesem Falle gemäß der Risikohöhe  anzuwenden.  Dementsprechend  genießen  sehr  hohe  Risiken  eine  die höchste Priorität, für geringe Risiken steht dagegen offen, ob eine Risikoakzeptanz stattfindet.

## Gefährdungen und deren Risikobehandlung

| Ge- fähr- dung   | Titel                                                   | Schutz- ziel   | Ri- siko   | Maßnahmen zur Risikobe- handlung                                                                                                                                                       |
|------------------|---------------------------------------------------------|----------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.14           | Ausspähen von Informationen (Spionage)                  | C              | Ge- ring   | Anforderungen der Bausteine OPR.2 und ORP.4, sowie: • ORP.4.A21 (Mehr-Faktor-Au- thentisierung) • ORP.2.A13 (Sicherheitsüber- prüfung) • ORP.5.A10 (Klassifizierung von Informationen) |
| G 0.16           | Diebstahl von Geräten, Daten- trägern oder Do- kumenten | C, A           | Sehr Hoch  | Anforderungen der Bausteine DER.1, OPS.1.2.3, INF.1, INF.2 sowie: • CON.1.A10 (Entwicklung ei- nes Kryptokonzepts) • INF.1.A22 (Sichere Türen und Fenster)                             |

<!-- page: 175 -->

| Ge- fähr- dung   | Titel                                     | Schutz- ziel   | Ri- siko   | Maßnahmen zur Risikobe- handlung                                                                                                                                                                                         |
|------------------|-------------------------------------------|----------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.18           | Fehlplanung o- der fehlende An- passung   | C, I, A        | Hoch       | Anforderungen der Bausteine OPS.1.1.2, OPS.1.1.3, OPS.1.1.6, DER.1 sowie: • DER.1.A16 (Einsatz von De- tektionssystemen nach Schutzbedarfsanforderungen)                                                                 |
| G 0.19           | Offenlegung schützenswerter Informationen | C              | Ge- ring   | Anforderungen der Bausteine ORP.1, ORP.3 sowie: • ORP.5.A10 (Klassifizierung von Informationen) • CON.6.A9 (Auswahl geeigne- ter Verfahren zur Löschung oder Vernichtung von Daten- trägern bei erhöhtem Schutz- bedarf) |
| G 0.21           | Manipulation von Hard- oder Software      | C, I, A        | Mittel     | Anforderungen der Bausteine OPS.1.1.2, OPS.1.1.3, OPS.1.16 sowie: • CON.1.A16 (Physische Absi- cherung von Kryptomodulen)                                                                                                |
| G 0.22           | Manipulation von Informatio- nen          | I              | Ge- ring   | Anforderungen der Bausteine ORP.4., OPS.1.1.2, OPS.1.1.6, SYS.1.1, APP.3.3.                                                                                                                                              |
| G 0.23           | Unbefugtes Ein- dringen in IT- Systeme    | C, I           | Hoch       | Anforderungen der Bausteine ORP.4, OPS.1.2.4, DER.1, DER.2.1 sowie: • ORP.4.A21 (Mehr-Faktor-Au- thentisierung)                                                                                                          |
| G 0.25           | Ausfall von Ge- räten oder Syste- men     | A              | Hoch       | Anwendung der Standard-Maß- nahmen und Akzeptanz des Rest- risikos).                                                                                                                                                     |
| G 0.26           | Fehlfunktion von Geräten o- der Systemen  | C, I, A        | Hoch       | Anforderungen des Bausteins OPS.1.1.2, OPS.1.1.3, OPS.1.1.5, DER.1, DER.2.1, DER.2.3 sowie: • CON.1.A14 (Schulung von Benutzern und Administrato- ren)                                                                   |

<!-- page: 176 -->

| Ge- fähr- dung   | Titel                                                              | Schutz- ziel   | Ri- siko   | Maßnahmen zur Risikobe- handlung                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------|----------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.27           | Ressourcenman- gel                                                 | A              | Sehr Hoch  | Anforderungen der Bausteine OPS.1.1.2, SYS.1.1, APP.3.3 so- wie: • CON.5.A13 (Entwicklung ei- nes Redundanzkonzeptes für Anwendungen)                                                                                                   |
| G 0.28           | Software- Schachstellen oder -Fehler                               | C, I, A        | Mittel     | Anforderungen der Bausteine OPS.1.1.2, OPS.1.1.3, OPS.1.1.5, DER.1, DER.2.1, DER.2.3, APP.3.3.                                                                                                                                          |
| G 0.30           | Unberechtigte Nutzung oder Administration von Geräten und Systemen | C, I           | Mittel     | Anforderungen der Bausteine OPR.4, OPS.1.1.2, DER.1 sowie: • ORP.4.A21 (Mehr-Faktor-Au- thentisierung)                                                                                                                                  |
| G 0.31           | Fehlerhafte Nut- zung von Gerä- ten und Syste- men                 | C, I, A        | Hoch       | Anforderungen der Bausteine ORP.2, OPS.1.1.2 sowie: • OPS.1.1.2.A17 (IT-Administ- ration im Vier-Augen-Prinzip)                                                                                                                         |
| G 0.32           | Missbrauch von Berechtigungen                                      | C, I           | Hoch       | Anforderungen der Bausteine ORP.2, ORP.4, OPS.1.1.2 sowie: • ORP.5.A10 (Klassifizierung von Informationen) • OPS.1.1.2.A14 (Sicherheits- überprüfung von Administra- toren) • OPS.1.1.2.A17 (IT-Administ- ration im Vier-Augen-Prinzip) |
| G 0.39           | Schadpro- gramme                                                   | C, I, A        | Sehr Hoch  | Anforderungen der Bausteine OPS.1.1.4, DER.1, DER.2.1, DER.2.3 sowie: • ORP.3.A9 (Spezielle Schulung von exponierten Personen und Institutionen) • DER.1.A16 (Einsatz von De- tektionssystemen nach Schutzbedarfsanforderungen)         |

<!-- page: 177 -->

| Ge- fähr- dung   | Titel                                            | Schutz- ziel   | Ri- siko   | Maßnahmen zur Risikobe- handlung                                                                                                                                                                           |
|------------------|--------------------------------------------------|----------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.40           | Verhinderung von Diensten (Denial of Ser- vice)  | A              | Hoch       | Anforderungen der Bausteine CON.5, DER.1, DER.2.1, SYS.1.1, APP3.3 sowie: • CON.5.A13 (Entwicklung ei- nes Redundanzkonzeptes für Anwendungen)                                                             |
| G 0.43           | Einspielen von Nachrichten                       | I              | Ge- ring   | Anforderungen der Bausteine CON.1, OPS.1.1.5, SYS.1.1, APP.3.3, INF.4 sowie: • CON.1.A10 (Entwicklung ei- nes Kryptokonzepts)                                                                              |
| G 0.44           | Unbefugtes Ein- dringen in Räumlichkeiten        | C, I           | Ge- ring   | Anforderungen der Bausteine INF.1, INF.2 sowie: • INF.2.A24 (Einsatz von Vi- deoüberwachungsanlagen)                                                                                                       |
| G 0.45           | Datenverlust                                     | A              | Hoch       | Anforderungen der Bausteine CON.3, CON.5, OPS.1.1.6, DER.2.1, DER.4 sowie: • CON.1.A14 (Schulung von Benutzern und Administrato- ren) • CON.5.A13 (Entwicklung ei- nes Redundanzkonzeptes für Anwendungen) |
| G 0.46           | Integritätsverlust schützenswerter Informationen | I              | Ge- ring   | Anforderungen der Bausteine CON.1, OPS.1.1.5, SYS.1.1, APP.3.3.                                                                                                                                            |

<!-- page: 178 -->

## Kapitel 8 Anwendungshinweise

## 8.1 Andere IT-Grundschutz-Profile

Neben den Anforderungen und Anmerkungen dieses IT-Grundschutz-Profils können die  Anwender  ebenfalls  auf  das  IT-Grundschutz-Profil  der  Basis-Absicherung  für Kommunalverwaltungen zurückgreifen. Während eine Kommunalverwaltung über andere Aufgaben und Geschäftsprozesse verfügt, werden diese, abgesehen von spezifischen Fachverfahren, üblicherweise über ähnliche Anwendungen und IT-Systeme bewältigt. Diesem IT-Grundschutz-Profil lassen sich daher nützliche Hinweise bezüglich der hier empfohlenen Anforderungen entnehmen.

Zudem werden weitere IT-Grundschutz-Profile über das BSI veröffentlicht, deren Ansätze und Kommentare auch für das ISMS einer obersten Landesbehörde von Vorteil sein können.

## 8.2 Internationale ISMS-Standards

Neben Publikationen des BSI können zur Umsetzung eines ISMS andere ISMS-Standards  herangezogen  werden.  Dazu  empfiehlt  sich  insbesondere  der  ISO  Standard 27001:2013 sowie der Standard 27002:2013 als Handlungsanleitung zu der ISMS-Umsetzung nach der ISO 27001.

Die Anmerkungen in diesen Dokumenten können für die Anwender der StandardAbsicherung relevant sein, da diese sich das ISMS nach der Standard-Absicherung auch über die ISO 27001:2013 zertifizieren lassen können.

Aus dem gleichen Normenbereich können bei entsprechendem Interesse die Standards 27003:2010 (Leitfaden zu der Umsetzung des ISMS), 27004:2012 (Messbarkeit des ISMS) und 27005:2018 (Informationssicherheits-Risikomanagement) ebenfalls berücksichtigt werden. Allerdings sollte vor einer Anschaffung bedacht werden, dass die Umsetzung der Standard-Absicherung nach IT-Grundschutz die dort formulierten Anforderungen erfüllt.

## 8.3 Weiterentwicklung des IT-Grundschutz-Profils

Wie das BSI bereits in seinen Publikationen und Veranstaltungen zu dem IT-Grundschutz hervorhebt, profitieren die IT-Grundschutz-Profile besonders durch Beteiligung der betroffenen Institutionen und den dortigen Erfahrungen.

Auch wenn dieses IT-Grundschutz-Profil unter Rücksprache mit mehreren Verantwortlichen der obersten Landesbehörden erstellt wurde, sind zukünftig Verbesserungen zu erwarten. Erst durch die Rückmeldung und Beteiligung von Anwendern können zuvor unbekannte Fehler verbessert und das Profil so effizienter gestaltet werden.

Ebenso besteht die Möglichkeit, auf Basis dieses IT-Grundschutz-Profils weitere Profile für spezielle Landesbehörden zu generieren. Diese Profile wären in diesem Fall in  der  Lage,  besondere Fachverfahren einer bestimmten Behörde aufzunehmen und ggf. einen individuellen Baustein dafür abzubilden. Dies würde sich insbesondere bei Ebenen-übergreifenden Fachverfahren anbieten, die  gemeinsamen  Sicherheitsbestrebungen unterliegen.

<!-- page: 179 -->



<!-- page: 180 -->

## Kapitel 9 Literatur

- [1] K.  Möltgen-Sicking  und T.  Winter, Verwaltung  und  Verwaltungswissenschaft: Eine praxisorientierte Einführung . Wiesbaden: Springer VS, 2018.
- [2] J. Bogumil und W. Jann, Verwaltung und Verwaltungswissenschaft in Deutschland: Einführung in die Verwaltungswissenschaft , 2. Aufl. Wiesbaden: VS Verlag für Sozialwissenschaften, 2009.
- [3] Bundesamt für Sicherheit in de r Informationstechnik, 'Zuordnung ISO/IEC  27001  sowie  ISO/IEC  27002  zum  modernisierten  ITGrundschutz', Bundesamt für Sicherheit in der Informationstechnik (BSI), Bonn, 2018.
- [4] T. Nentwig und C. Werwath, Hg., Politik und Regieren in Niedersachsen . Wiesbaden: Springer VS, 2016.
- [5] R. Heuermann, M. Tomenendal und C. Bressem, Hg., Digitalisierung in Bund, Ländern  und  Gemeinden:  IT-Organisation,  Management  und  Empfehlungen .  Berlin,  Germany: Springer Gabler, 2018.
- [6] D. Schamburek, 'Die Ansiedlung von Aufgab en in der Aufbauorganisation deutscher Landesministerialverwaltungen'. Dissertation, 2016.
- [7] P. Fischer und P. Hofer, Lexikon der Informatik , 15. Aufl. Berlin, Heidelberg: Springer-Verlag Berlin Heidelberg, 2011.
- [8] StatCounter, Global Market Share Held by Operating Systems for Desktop Pcs, from January  2013  to  January  2019 .  [Online]  Verfügbar  unter:  www.statista.com/statistics/218089/global-market-share-of-windows-7. Zugriff am: Feb. 15 2019.
- [9] ITCandor, Share of the global server market by operating system in the first half of 2018 .  [Online]  Verfügbar  unter:  https://www.statista.com/statistics/915085/global-server-share-by-os. Zugriff am: Feb. 15 2019.
- [10] Kantar, Share of The Leading Smartphone Operating Systems in The Sales Volume of Smartphones in Germany from January 2012 to September 2018 . [Online] Verfügbar unter: www.statista.com/statistics/461959/smartphone-os-sales-volume-share-germany. Zugriff am: Feb. 15 2019.
- [11] ISO/IEC 27002:2013 , 2013.
- [12] NIST Special Publication 800-63B , 2017.
- [13] Data Security Standard , 2018.
- [14] BSI-Standard 200-2 , 2017.
- [15] M. Herr, C. E. Müller, B. Engewald und J. Ziekow, 'Transparenzgesetzgebung in Deutschland in der Bewährung: Erfahrungen einer Gesetzesevaluation', DÖV (Die Öffentliche Verwaltung) , Jg. 5, S. 165 - 168, 2018.
- [16] ISO 31000:2018 , 2018.
- [17] BSI-Standard 200-3, 2017.
- [18] Bundesanzeiger Verlag GmbH; Deutschland, IT-Grundschutz-Kompendium: 2. Edition 2019 . Köln: Bundesanzeiger Verlag, 2019.

<!-- page: 181 -->

## Anhang C Experteninterviews

In den beiden folgenden Anhängen sind die beiden Experteninterviews im Rahmen der Evaluierung des IT-Grundschutz-Profils aufgeführt. Die Interviews sind im März und April 2019 durchgeführt worden und sind auf Nachfrage bei den befragten Experten anonymisiert. Die persönlich geführten Interviews sind akustisch aufgenommen und anschließend transkribiert worden.

Die Anonymisierung umfasst die Behörde, für die geantwortet wurden, den Namen der Person (hier ersetzt durch einen anderen Namen) und das Bundesland. Auf diesem Wege sollen Rückschlüsse vermieden werden, um welche Person und oberste Landesbehörde es sich handelt. Grund dafür ist die Sicherheitsrelevanz der Angaben für die betreffende Behörde.

## Interview I:

Experteninterview  im  Rahmen  der  Masterarbeit  'Erstellung  eines  IT -Grundschutz-Profils für die oberste Landesbehörden' am 28.03.2019

Anwesend sind Herr Meyer und Herr Grieger

Grieger : Guten Tag Herr Meyer, mein Name ist Raphael Grieger und ich schreibe derzeit eine Masterarbeit im Studiengang Information Security Management. Die Masterarbeit hat folgende Forschungsfragen:

- Welche Anforderungen muss ein IT-Grundschutz-Profil für eine oberste Landesbehörde zur Umsetzung einer Standard-Absicherung enthalten?
- Über welche gemeinsamen Geschäftsprozesse verfügen oberste Landesbehörden?
- Welcher dieser  Geschäftsprozesse  könnte  mit  einem  IT-Grundschutz-Profil generisch betrachtet und mit der IT-Grundschutz-Methodik abgesichert werden?
- Wie stellt sich die Risikobereitschaft in einer obersten Landesbehörde dar?
- Welche Schutzbedarfe bestehen für die betrachteten Zielobjekte?
- Gibt es zusätzliche Anforderungen für die Anwendung dieses schematischen ISMS auf eine oberste Landesbehörde?

Nun zu dem Interview an sich. Dort habe ich eine grobe Struktur vorgesehen, der wir im Interview folgen werden. Zunächst einmal eine Vorstellung meiner Person und der Masterarbeit  als  Einführung,  was  ich  ja  eben  getan  habe.  Anschließend  möchte  ich Ihnen einige Fragen zu Ihrer Person stellen, dass sich für den nachfolgenden Leser ergibt, wer vor mir saß und woher sich Ihre Expertise ergibt. Dann möchte ich Fragen zu der Behörde stellen, in der sie arbeiten oder gearbeitet haben. Daran anschließen werde ich Fragen bezogen auf das IT-Grundschutz-Profil stellen, um rückzukoppeln, ob die Annahmen die dort getroffen wurden realistisch sind. Abschließend bleibt die Möglichkeit für Bemerkungen.

<!-- page: 182 -->

Meyer : Sehr gut.

Grieger : Zunächst als allgemeine Frage, ob Sie mit der akustischen Aufnahme des Interviews einverstanden sind?

Meyer : Ja.

Grieger : Und zusätzlich haben sie ja bereits im Vorfeld mitgeteilt, dass gegebenenfalls nach dem Interview geprüft werden muss, ob Ihre Angaben zu Ihrer Behörde veröffentlichungsfähig sind. Ich würde versuchen, die Fragen zu dem IT-Grundschutz-Profil als Einschätzungsfragen Ihrerseits zu formulieren. Im Zweifelsfalle könnten dann die Anteile Ihrer Aussage, die sich auf Ihre Behörde beziehen, herausgenommen werden.

Meyer : Eventuell bietet es sich an, dass ich das Interview nach der Transkription bei der Behörde einreiche und diese eine Veröffentlichung prüfen kann.

Grieger : Ok, dann machen wir das so und ich lasse Ihnen die Transkription zur Prüfung nach der Fertig-stellung zukommen. Um zur ersten Frage überzugehen: Welches ist ihr akademischer Bildungsabschluss?

Meyer : Ich bin promoviert.

Grieger : Was waren denn ihre beruflichen Tätigkeiten seit dem Abschluss ihrer akademischen Laufbahn?

Meyer : Im wesentlichen IT-Projektmanagement und dann Informationssicherheitsmanagement.

Grieger : Im Bereich von Behörden oder auch außerhalb der öffentlichen Verwaltung? Meyer : In Behörden.

Grieger : Und ihre aktuelle Tätigkeit?

Meyer : Strategisches Informationssicherheitsmanagement.

Grieger : Auf welcher Ebene?

Meyer : Auf Landesebene. Für die Landesverwaltung.

<!-- page: 183 -->

Grieger : Im Vorfeld habe ich erfahren, dass sie auch als Informationssicherheitsbeauftragter einer obersten Landesbehörde tätig waren?

Meyer : Genau.

Grieger : Dann würde ich mich bei den weiteren Fragen, die sich auf eine oberste Landesbehörde beziehen, auf ihre Tätigkeit dort beziehen.

Meyer : Ja.

Grieger :  Diesbezüglich  wüsste  ich  zunächst  gerne,  welche  ISMS-Methodik  ihre  Behörde angewendet hat.

Meyer : Das ISMS basiert auf der Informationssicherheitsleitlinie und den Informationssicherheitsrichtlinien des Landes, die die Mindeststandards für ein ISMS und die Aufbau- und Ablauforganisation im ISMS definieren. Diese bilden die Grundlage.

Grieger : Wenn sie die Methodik zwischen der ISO 27001 und dem IT-Grundschutz einordnen müssten, wo würde sich diese Leitlinie und Richtlinie orientieren?

Meyer : Grundsätzlich eher an der ISO 27000, wobei auch Elemente des BSI vorhanden sind, wenn es um Gefährdungsanalyse beispielsweise geht.

Grieger :  Gilt  diese  Informationssicherheitsleitlinie und -Richtlinie  für  alle  Behörden der  Landesverwaltung gleichermaßen? Findet also überall dort die gleiche Methodik Anwendung?

Meyer : Ja, diese orientieren sich alle an einer ähnlichen Methodik. Allerdings mit Einschränkungen. Die obersten Landesbehörden orientieren sich alle daran, es gibt Teilbereiche, die in der Regel im nachgeordneten Bereich liegen, die aufgrund externer Anforderungen den BSI IT-Grundschutz anwenden und zertifizieren müssen.

Grieger : Welche Anforderungen wären dies?

Meyer : In der Regel Vorgaben aus dem Bereich der EU-Zahlstellen, die aufgrund einer EU-Vorgabe eine BSI-Zertifizierung benötigen. Wenn EU-Zahlungsverkehr besteht, wie beispielsweise in verschiedenen Förderungen. Dies ist aber gewöhnlich im nachgeordneten Bereich angesiedelt.

Grieger : Wo ist der Informationssicherheitsbeauftrage in der Behördenstruktur ihrer Behörde angesiedelt?

<!-- page: 184 -->

Meyer : In der Behörde in dem Referat für IT und E-Government. Also in der Linie. Gleichwohl, mit direktem Vortragsrecht bei der Behördenleitung.

Grieger : Also integriert in den allgemeinen Arbeitsablauf der Behörde und nicht separat davon?

Meyer : Genau.

Grieger : Wie würden sie die Begrifflichkeit 'in der Linie' definieren?

Meyer : Das ist ein spezielles Problemfeld. Die Aufgaben eines Beauftragten werden aus der Informationssicherheitsleitlinie hergeleitet. Dies sind prüfende und initiierende Aufgaben sowie beratende Aufgaben gegenüber der Behördenleitung. Diese finden unabhängig von der Position in der Hierarchie einer Behörde statt. Gleichwohl hat man in der Informationssicherheit auch immer Tätigkeiten, die operativ sind. Das wären dann die Linienaufgaben. Zwischen diesen Aufgaben zu unterscheiden fällt schwer und ist in der Praxis fast unmöglich.

Grieger : Wie viele Personen sind selbst mit der Aufgabe des Informationssicherheitsmanagements in der obersten Landesbehörde betraut?

Meyer : Eine.

Grieger : Welcher Personenkreis wird davon betroffen?

Meyer : Die oberste Landesbehörde hat etwa 400 Beschäftigte.

Grieger : Wer zählt zu dem erweiterten Kreis der Beteiligten im Bereich der Informationssicherheit?

Meyer : Die Behördenleitung natürlich, der Staatssekretär vertritt die Behördenleitung in diesem Bereich, übernimmt die Verantwortung und trifft die Entscheidungen. Und der Leiter der Abteilung 1, Innere Dienste, dort ist das Referat für IT und E-Government angesiedelt. Die Referatsleiter sind dort ebenfalls mit eingebunden. Die Abteilungsleiter sind in der Regel mit monatlichen Gesprächen eingebunden, wo strategische Weiterentwicklungen besprochen werden.

Grieger :  Welchen Anwendungsbereich umfasst das ISMS in ihrer Behörde? Welche Geschäftsprozesse und Anwendungen wurden davon umfasst?

Meyer : Die Betrachtungsweise der behördlichen Vorgänge als Geschäftsprozesse bildet sich erst langsam. Es ist also nicht die die Grundlage, auf der das ISMS basiert. Viel eher orientiert sich das ISMS an organisatorischen Zuständigkeiten, also fachlichen Zuständigkeiten und an bestehenden Infrastrukturen wie Fachverfahren und Services. Diese Fachverfahren stellen dann einen Teil dieser ganzen Sicherheitskonzeption dar.

<!-- page: 185 -->

Grieger : Um es konkret zu formulieren, was wäre ein Teil, der in dem ISMS konkret betrachtet wird?

Meyer : Die ganze Infrastruktur ist ein Teil des ISMS und als Fachverfahren gibt es im Wesentlichen An-wendungen, die vom Ministerium selbst verwaltet werden.

Grieger : Gibt es denn konkrete Anteile der Infrastruktur und Anwendungen, die ausdrücklich nicht betrachtet werden?

Meyer : Ausgeklammert sind Fachverfahren die wir nicht selbst betreiben, sondern die wir die wir als Leistungs-Empfänger lediglich anwenden. Das Risiko dieser Verfahren und Services wird von den Bereitstellern getragen. Zusätzlich wird das Risiko für die IT-Infrastruktur als Ganzes vom IT-Dienstleister des Landes getragen.

Grieger : Inwieweit ist das ISMS, zu dem Zeitpunkt als sie in der Behörde gearbeitet haben, umgesetzt gewesen?

Meyer : Ich würde es als teilweise umgesetzt bezeichnen. Es gibt nicht zu allen Fachverfahren abgeschlossene Sicherheitskonzeptionen. Die Infrastruktur ist ebenfalls nicht in allen Bereichen durch eine Sicherheitskonzeption untersucht. Ich würde sagen, der Reifegrad ist im mittleren Bereich.

Grieger : Ist vorgesehen, dass eine externe Auditierung oder Zertifizierung stattfindet?

Meyer : Dies ist derzeit nicht vorgesehen. Das wäre auch etwas, was behördenübergreifend etabliert wer-den sollte. Da das Land nicht klar dem IT-Grundschutz folgt, müsste es eine Zertifizierung nach der ISO 27001 sein. Da wurden bislang noch keine Überlegungen angestellt, dass man so etwas anstrebt.

Grieger : Wenn sie ihre Behörde als Ganzes generisch betrachten, wird die Tätigkeit der Beteiligung an der Normsetzung des Landes dort wahrgenommen? Also unabhängig der jeweiligen Ressorts?

Meyer : Ja.

Grieger : In welcher Form?

Meyer :  Als  oberste  Landesbehörde,  wo  Gesetzgebung  initiiert  wird  oder  in  Beteiligungsverfahren beteiligt wird.

<!-- page: 186 -->

Grieger : Aber generell werden auch Verordnungen von ihrer Behörde vorbereitet?

Meyer : Ja, Verordnungen und Erlasse.

Grieger : Können sie sich weitere generische Geschäftsprozesse vorstellen, die in ihrer Behörde durchgeführt werden?

Meyer : Also grundsätzlich ist Personalmanagement etwas, was in diese Richtung geht. Man könnte es an den Aufgaben orientieren. An der Gewerbeaufsicht hängen ganz konkrete Geschäftsprozesse, die in der Regel den nachgeordneten Behörden obliegen.

Grieger : Dieser Geschäftsprozess ist aber auch sehr abhängig von der Zuständigkeit des Ressorts. Wenn sie dies auf der Landesverwaltungsebene betrachten würden, wäre es die Normsetzung und das Personal-management. Gäbe es dort noch weitere Ansätze?

Meyer : Vielleicht noch organisatorische Fragen, aber das ist vielleicht auch zu kleinteilig. Kabinettsbefassungen sind noch ein solcher Geschäftsprozess. Alles was im Kabinett beschlossen wird, wird vorher einer wohldefinierten, formalen Beteiligung in den einzelnen Ressorts zugeführt. Da gibt es sehr gut definierte Abläufe, die auch mit Zeitfaktoren versehen sind. Dort ließen sich Geschäftsprozesse finden. Anderer Punkt sind parlamentarische Anfragen, die als kleine und große Anfragen aus dem Parlament kommen. Auch hier sehe ich ganz deutlich solche Geschäftsprozesse.

Grieger . Was würde man denn für den Geschäftsprozess der Normsetzung ihrer Einschätzung nach für Anwendungen und IT-Systeme benötigen?

Meyer : Also die Infrastruktur die man ohnehin benötigt, um so ein Netz zu betreiben. Und klassische Büro-Anwendungen. Darüber hinaus gibt es wenige gesonderte Anwendungen, die in der Regel der Aufgabenverfolgung dienen. Ansonsten Word, Excel, was eine typische Büroausstattung anbelangt.

Grieger : Ich habe einige IT-Infrastrukturanteile vorbereitet, die im IT-GrundschutzProfil beinhaltet sind. Ich würde sie um Stellungnahme bitten, ob diese Anteile in einer obersten Landesbehörde vorkommen.

Meyer : Gut.

Grieger : Dann bitte ich Sie einmal um Ablehnung oder Zustimmung, ob das Betriebssystem Windows 10 als Client-Betriebssystem vorkommt.

<!-- page: 187 -->

Meyer : Teilweise Zustimmung. Derzeit wird Windows 8.1 umgesetzt, ein Wechsel wird derzeit vorbereitet und wird in den nächsten 12 Monaten stattfinden.

Grieger : Nutzen sie eine Infrastruktur um Daten zentral und abgesichert zu speichern? Dies würde ich als Dateiserver, gegebenenfalls mit der konkreten Software Samba, bezeichnen.

Meyer : Da müsste ich raten. Einen Dateiserver gibt es, ob Samba oder Windows Komponenten verwendet werden ist mir nicht genau bekannt.

Grieger : Wird Active Directory genutzt?

Meyer : Ja, als eine zentrale Komponente.

Grieger : Wie steht es um Microsoft Exchange?

Meyer : Wird ebenfalls genutzt.

Grieger : Welches Server Betriebssystem wird verwendet?

Meyer : Server mit Microsoft Betriebssystem, allerdings nicht ausschließlich. Bei Microsoft Servern wird auch nicht ausschließlich die 2016-ner Version verwendet. Es ist gemischt. Dazu muss gesagt werden, dass ich nicht genau weiß, welche IT-Systeme der IT-Dienstleister für die Dienste der obersten Landesbehörde verwendet.

Grieger : Allgemein haben sie ja erwähnt, dass es in dem Gebäude eine eigene Infrastruktur gibt. Daher würde ich davon ausgehen, dass damit hier die Verkabelung auch gemeint ist?

Meyer : Genau.

Grieger : Gibt es denn eine Firewall in der Behörde?

Meyer : Bei dem zentralen IT-Dienstleister.

Grieger : Gibt es eventuelle noch eine gesonderte Firewall unter der Administration der obersten Landes-behörde?

Meyer : Nein.

Grieger : Nutzt ihre Behörde einen Signatur-Dienst, um authentische E-Mails oder vergleichbares zu gewährleisten?

<!-- page: 188 -->

Meyer : Ja, es gibt eine PKI.

Grieger : Können sie den Umfang der PKI beschreiben? Wird die gesamte Landesverwaltung davon um-fasst?

Meyer :  Die  PKI  ist  beim  zentralen  IT-Dienstleister  angesiedelt  und  erstreckt  sich grundsätzlich auf die Landesverwaltung. Allerdings wird nicht für jeden Arbeitsplatz ein Zertifikat ausgerollt, sondern bedarfs-orientiert eingerichtet.

Grieger :  Und  zuletzt,  ob  Serverräume  in  der  obersten  Landesbehörde  vorzufinden sind.

Meyer : Ja, sind sie. Ja, sind Sie. Im Sinne eines Zwischendings zwischen einem Verteilerschrank und einem Rechenzentrum. Die Server, die zentrale Verfahren und Dienstleistungen hosten, die sind im Rechenzentrum des IT-Dienstleisters. In dem Serverraum in der Behörde befinden sich aktive und passive Komponenten des Netzwerkes sowie einzelne vorgelagerte Services, wie der Print-Dienst.

Grieger : Im Wesentlichen handelt es sich also um eine Teilauslagerung?

Meyer :  Nein,  eher  um  eine  vollständige.  Der  Betrieb  obliegt  dem  Dienstleister,  der richtet nur Hardware vor Ort ein.

Grieger : Hat denn in ihrer Behörde eine Schutzbedarfsfeststellung bezüglich Integrität, Vertraulichkeit und Verfügbarkeit stattgefunden?

Meyer : Nicht voll umfänglich, aber wesentlich.

Grieger : Eine Schutzbedarfsfeststellung nach dem IT-Grundschutz oder nach der ISO 27000?

Meyer : Eine Mischung, was dem niedersächsischen Weg geschuldet ist. Für die Schutzbedarfsfeststellung gibt das BSI ja Anhaltspunkte für die Schutzbedarfskategorien und die Schutzbedarfe dazu. Die wurden im Wesentlichen als Grundlage verwendet und für die behördenweite Einstufung der Schutzbedarfe angepasst. Die Risikoermittlung die dann darauf folgt, die erfolgt nach der Informationssicherheitsrichtlinie des Landes zum Umgang mit Risiken.

Grieger : Wie würden sie persönlich den Schutzbedarf der Beteiligung an der Normsetzung des Landes einschätzen?

Meyer : Normal.

<!-- page: 189 -->

Grieger : Warum?

Meyer : Weil die einzelnen Schutzziele nach diesen Kategorien keinen erhöhten Schutzbedarf erkennen lassen. Die Verfügbarkeit ist im normalen Bereich. Von einer erhöhten Verfügbarkeit sprechen wir, wenn die Ausfallzeit von maximal einem Tag tolerierbar ist. Bei der Normsetzung ist eine Ausfallzeit von bis zu einem Tag tolerierbar. Integrität ist im normalen Bereich, es ist kompensierbar, wenn Integritätsverletzungen stattfinden. Und die Gründe der Vertraulichkeit liegen auch im normalen Bereich.

Grieger : Nun würde ich zu der zweiten Aufzählungsfrage kommen und zwar möchte ich Sie um eine Ein-schätzung hinsichtlich der Schutzbedarfe der zuvor genannten IT-Infrastrukturanteile.  Dies  muss  nicht  100%  richtig  sein,  einige  Faktoren  wie  Vererbungsprozess oder ähnliches sind vermutlich in einer Interviewsituation nicht ohne weiteres zu überblicken. Angenommen, Ihre Behörde würde Windows 10 verwenden, wie würden sie den Schutzbedarf einschätzen?

Meyer : Dazu muss man sagen, dass das Thema viel diskutiert wird. Meine Auffassung dazu ist, dass diese klassischen Infrastrukturkomponenten für einen hohen Schutzbedarf  konzipiert  werden  sollen,  da  diese  in  unterschiedlichen  Situationen  auftauchen. Dies gilt auch für die Bereiche Client, Exchange, und Active Directory.

Grieger : Also nehmen sie für die drei Schutzziele jeweils einen hohen Schutzbedarf an?

Meyer : Das ist schwierig. Nach der jetzigen Konzeption werden unterschiedliche Typen von Arbeitssituationen konzipiert, auf die Schutzbedarfe dann ausgelegt werden. Ich kann für die einzelnen Schutzziele zwar raten, aber ich könnte diese ad-hoc nicht zuverlässig einordnen.

Grieger : Ok, dann bleiben wir bei den allgemeinen, schutzzielunabhägigen, Stellungnahmen. Wie schätzen sie den Schutzbereich des Dateiservers?

Meyer :  Ebenfalls hoch. Bei Active Directory müsste man gegebenenfalls unterscheiden, ob es sich um die normalen Benutzerzugänge oder die des Administrators handelt. Aber dies wäre erst mit dem Dienstleister zu klären.

Grieger : Ok. Bei Microsoft Exchange?

Meyer : Entsprechend auch ein hoher Schutzbedarf. Bei allen wäre ich mir auch sicher, dass es sich um einen hohen Schutzbedarf handelt. Nur bei der Gebäudeverkabelung bin ich mir unsicher, ob dort so eine direkte Übertragung der Schutzbedarfes stattfindet.

Grieger : Bei einem Serverraum erkennen sie einen hohen oder sehr hohen Schutzbedarf?

<!-- page: 190 -->

Meyer :  Einen  hohen.  Die  einschlägige  Verordnung  des  Landes  sieht  vor,  dass  der Schutzbedarf abhängig ist von den Anwendungen, die darüber laufen. Das wären in diesem Fall nur Anwendungen mit hohem Schutzbedarf.

Grieger :  Hat ihre Behörde diese aufgezählten Zielobjekte im Rahmen der Schutzbedarfskonzeption betrachtet?

Meyer : Dadurch, dass diese nicht in unserem Zuständigkeitsbereich liegen, nein. Außer die Gebäudeverkabelung.

Grieger : Welcher Schutzbedarf wurde angenommen?

Meyer : Normal bis hoch.

Grieger :  Als  letzten  Fragekomplex würde ich auf den Umgang mit Risiken in einer Behörde eingehen. Wie würden sie die Risikobereitschaft einer Behörde einschätzen?

Meyer : Das ist eine schwierige Frage. Grundsätzlich gibt es Risikobereitschaft auf der psychologischen Basis, dass ja noch nie was passiert ist. Ein Risikobewusstsein könnte dort größer sein, wo es bereits einen Vorfall gab. Der Risikoappetit meiner obersten Landesbehörde würde ich als kleiner schätzen. In der Informationssicherheitsleitlinie wird die Ausprägung der Risikomatrix nicht explizit vorgegeben. Diese wird im ISMS der Behörden jeweils festgelegt. Die dortigen Empfehlungen gehen aber von einem geringen Risikoappetit aus.

Grieger : Gibt es bestimmte andere Gründe, die sie für eine erhöhte oder niedrige Risikobereitschaft in einer obersten Landesbehörde identifizieren können?

Meyer : Grundsätzlich gibt es unterschiedliche Strategien, wie sehr man Veränderungen zulässt. Oberste Landesbehörden scheinen etwas weniger Veränderungsbereit, was umgekehrt zu einer Risikobereitschaft führt. Dies mag auch eher unbewusst stattfinden.

Grieger : Inwiefern wurden denn in ihrer Behörde die Risikoeintrittswahrscheinlichkeiten und -auswirkungen operationalisiert? Wurde dort quantitativ auf einen monetären Schaden geschaut oder wie wurde diese durchgeführt?

Meyer : Quantitativ ist das schwierig, weil fast immer die Zahlen fehlen. Daher sehe ich das eher qualitativ.

Grieger : Wie stehen sie zu einer semi-qualitativen Form, beispielweise orientiert an harten Grenzen?

<!-- page: 191 -->

Meyer : Es gibt harte Grenzen, besonders im finanziellen Bereich und im Bereich von Verfügbarkeitseinschränkungen. Da kann man mit diesem Grenzen arbeiten. Ja.

Grieger : Ich hätte dann keine weiteren Fragen mehr. Grundsätzlich würde mich allerdings auch interessieren, ob sie noch Anmerkungen zu dem IT-Grundschutz-Profil hätten. Gibt es beispielsweise Besonderheiten, die ein IT-Grundschutz-Profil berücksichtigen sollte, um einen besonderen Mehrwehrt für die oberste Landesbehörde zu haben?

Meyer : Ich bin mir nicht ganz sicher ob sich dies in einem IT-Grundschutz-Profil angemessen darstellen lässt. Aber in der Risikoanalyse sind politische Risiken eine besondere Kategorie, die sich schwer schätzen lassen. Zudem lässt sich mit dem Blick auf die Organisation schwer feststellen, wo in der Organisation besonders solche Risiken verortet sind.

Grieger : Haben sie sonst noch weitere Anmerkungen zu dem IT-Grundschutz-Profil, der Forschungsfrage oder anderen Anteilen des Interviews?

Meyer : Grundsätzlich finde ich die Idee gut mit dem Geschäftsprozess der Normsetzung. Wie bereits erwähnt, sehe ich dort noch weitere Geschäftsprozesse, die man ähnlich behandeln könnte. Mich würde interessieren, ob man bei dem Schutzbedarf dieses Geschäftsprozess auch zu anderen Auffassungen gelangen kann und beispielsweise einen hohen Schutzbedarf erkennt. Das führt zu der Sub-Frage der Subjektivität solcher Schutzbedarfsfeststellungen, die einem im Informationssicherheitsmanagement immer wieder begegnet. Insofern bin ich über die Aussagen anderer Experten gespannt.

Grieger : Dann danke ich Ihnen für dieses Interview.

Meyer : Gern geschehen.

## Interview II:

Experteninterview  im  Rahmen  der  Masterarbeit  'Erstellung  eines IT-Grundschutz-Profils für die oberste Landesbehörden' am 15.04.2019

Anwesend sind Frau Mayer und Herr Grieger

Grieger : Guten Tag Frau Mayer, ich werde nun mit dem Interview beginnen. Das Interview ist mehrere Teile gegliedert, die ich Ihnen kurz darstellen möchte. Zunächst werde ich mich die Masterarbeit und den Zweck des Experteninterviews vorstellen. Anschließend werde ich Ihnen einige Fragen zu Ihrer Person stellen, damit für den Leser, selbst wenn es anonymisiert ist, daraus hervorgeht, mit wem ich gesprochen habe. Zudem muss ihre Expertise auch aus dem Interview hervorgehen.

Dann werde ich im dritten Teil Fragen zu ihrer Behörde stellen, dazu hatte ich ihnen im Voraus einige Fragen bereits zur Verfügung gestellt. Dann werde ich Fragen zu dem IT-Grundschutz-Profil stellen. Es wird dabei zwangsweise zu Überschneidungen zu ihrer Behörde kommen, da es mir darum geht, mit dem IT-Grundschutz-Profil die Verwaltungswirklichkeit abzubilden. Es ist ja das klare Ziel der Masterarbeit und des ITGrundschutz-Profils etwas zu schaffen, was einen Mehrwert für die Behörden darstellt, die davon betroffen sind. Es soll sich also um keine rein theoretische Arbeit handeln, sondern es soll möglichst viel Rückkopplung mit der Praxis stattfinden. Am Ende würde ich ihnen noch die Möglichkeit geben, weitere Anmerkungen zu machen und ansonsten das Interview beenden.

<!-- page: 192 -->

Zu der Masterarbeit: In der Masterarbeit geht es um die Erstellung eines IT-Grundschutz-Profils, dazu habe ich sechs Kapitel vorgesehen. Eine Einleitung, den Stand der Wissenschaft, im dritten Teil geht es um den Fragebogen, mit dem erhoben werden sollte, wie die Verwaltungswirklichkeit in Deutschland ist. Auf Basis der Literatur und des Fragebogens habe ich anschließend ein IT-Grundschutz-Profil erstellt, unter Anleitung des BSI, welches dann evaluiert wird.

Die Masterarbeit bewegt sich im Bereich der Design Science, die nicht wie die Verhaltensforschung eine Hypothese belegt oder wiederlegt. In der Design Science wird eine Problemstellung gelöst. Hier ist die Problematik, dass die Verwaltungen des Bundes und der Länder nach der gemeinsamen Informationssicherheitsleitlinie ein ISMS etablieren sollen und, dass dies mit einem IT-Grundschutz-Profil vereinfacht werden könnte. Ich möchte daher in der Evaluation nach der Erstellung des IT-Grundschutz-Profils ein paar Grundannahmen, die ich dort getroffen habe, validieren. Daher das Experteninterview.

Ich möchte zunächst mit der Frage beginnen, ob sie mit der akustischen Aufzeichnung einverstanden sind.

Mayer : Bin ich, ja.

Grieger : Im Vorfeld haben wir über die Veröffentlichung gesprochen, das wäre zuvor abzustimmen mit ihrer Behörde. Wenn diese der anonymisierten Version nicht zustimmen, dann würde gegebenenfalls nur in der Masterarbeit ein Vermerk sein, dass ein Interview durchgeführt wurde, aber der Veröffentlichung in der Masterarbeit nicht zugestimmt wurde.

Mayer : Gut, das muss ich wie gesagt abklären. Zum einen würde ich das mit dem CISOTeam abklären, zum anderen dem Leiter der IT zu Kenntnis geben, damit auch dieser sagen kann, ob das Interview Informationen enthält, die nicht veröffentlicht werden dürfen.

Grieger : Was ist ihr akademischer Bildungsabschluss?

<!-- page: 193 -->

Mayer : Ich bin Diplom-Verwaltungswirtin.

Grieger : Gleichzusetzen mit einem heutigen Bachelor oder einem heutigen Master?

Mayer : Mit einem Bachelor.

Grieger : Alles klar. Was waren ihre Tätigkeiten seit ihrem letzten Bildungsabschluss?

Mayer : Ich habe in verschiedenen Verwaltungszweigen gearbeitet und bin jetzt seit zwei Jahren in der Informationssicherheit tätig. Ich habe keine IT-Ausbildung und auch vorher nicht in der IT gearbeitet.

Grieger : Was ist ihre aktuelle Funktion in ihrer Behörde?

Mayer : Ich bin die Informationssicherheitsbeauftragte.

Grieger : In der Landesverwaltung oder der obersten Landesbehörde?

Mayer : In der obersten Landesbehörde.

Grieger : Welche Methodik wendet denn die Behörde an, die sie hier vertreten?

Mayer : Den IT-Grundschutz.

Grieger : Ok, und wird in den anderen obersten Landesbehörden der Landesverwaltung die gleiche Methodik angewendet oder eine andere?

Mayer : Die gleiche.

Grieger : Ist das einheitlich von der Landesverwaltung vorgegeben?

Mayer :  Ja,  nach  der Leitlinie  des IT-Planungsrats wurde vom Kabinett beschlossen, dass einheitlich der IT-Grundschutz in der Landesverwaltung umgesetzt wird.

Grieger :  Wo  ist  der  Informationssicherheitsbeauftragte  in  ihrer  obersten  Landesbehörde angesiedelt?

Mayer : In der Linienorganisation. Das hat vor allem praktische Gründe. Nichtsdestotrotz wurde dennoch immer wieder betont, dass auch das direkte Vortragsrecht bei der Leitung des Hauses besteht.

Grieger : Wie viele Personen sind in ihrer Behörde mit dem Thema Informationssicherheit befasst?

<!-- page: 194 -->

Mayer : Neben mir eine weitere Person.

Grieger

: Also zwei Stellen?

Mayer : Nicht ganz Vollzeit, grundsätzlich aber ja.

Grieger : Wer zählt zu dem erweiterten Kreis der Beteiligten im Bereich der Informationssicherheit? Also neben der Behördenleitung und ihnen beispielsweise?

Mayer : Das ist hier noch nicht genau definiert. Ich würde auf jeden Fall den Leiter des inneren Dienstes und den Leiter der IT hinzuzählen. Im gewissen Umfang auch den Datenschutzbeauftragen, das ist aktuell noch nicht abschließend geklärt.

Grieger :  Welche Geschäftsprozesse wurden von dem ISMS ihrer Behörde umfasst? Wie wurde der Anwendungsbereich geschnitten?

Mayer : Es gibt hier viele Fachverfahren, die übergreifend modelliert sind. Alles im Einzelnen ist noch nicht identifiziert.

Grieger : Der Anwendungsbereich umfasst also die gesamte Behörde oder werden auch manche Teile ausdrücklich nicht betrachtet?

Mayer : Es wird die ganze Behörde betrachtet.

Grieger : Wie weit würden sie die Umsetzung des ISMS bezeichnen?

Mayer : Teilweise.

Grieger : Ist eine Zertifizierung der Behörde vorgesehen?

Mayer : Die Zertifizierung der Behörde auf Basis des IT-Grundschutzes ist nicht geplant.

Grieger : In dem IT-Grundschutz-Profil wurde ein generischer Geschäftsprozess betrachtet,  den  ich  im  Rahmen  des  Interviews  überprüfen  möchte.  Daher  wüsste  ich gerne, ob die Tätigkeit ihrer Behörde auch die Beteiligung an der Normsetzung umfasst?

Mayer : Ja.

Grieger : Welche Aufgaben sehen sie da in diesem Bereich, wenn sie diesen Oberbegriff betrachten?

<!-- page: 195 -->

Mayer : Jedes Gesetz, das vom Kabinett beschlossen wird, wird in allen Ministerien auf Fachebene abgestimmt. Jedes Ministerium gibt also eine Stellungnahme ab, wenn ein Gesetz beschlossen wird.

Grieger : Gibt es auch weitere Bereiche der Normsetzung?

Mayer : Es gibt auch Bereiche, in denen wir die Federführung haben und wo wir die Gesetze in die Wege leiten.

Grieger : Der Themenbereich der Erlasse und Verordnungen wird auch wahrgenommen?

Mayer : Ja.

Grieger : Es handelte sich ja hier um einen generischen Oberbegriff für eine Aufgabe der Behörde. Können sie noch weitere Aufgaben auf einem ähnlichen Abstraktionslevel nennen, die eine Behörde beschreiben?

Mayer : Verstehen sie auch Verwaltungsvorschriften unter der Normsetzung?

Grieger : Würde ich jetzt auch darunter definieren.

Mayer : Dann würden mir so ad-hoc keine weiteren Aufgaben einfallen.

Grieger : Wie sieht das aus mit der Auslagerung von Infrastrukturanteilen aus der Behörde? Nutzen Sie einen IT-Dienstleister? Wenn ja, was wurde dort ausgelagert.

Mayer :  Teile  sind  aus  Kapazitätsgründen  an  einen  öffentlichen  IT-Dienstleister  des Landes ausgelagert. Dieser nimmt für die gesamte Landesverwaltung Aufgaben wahr. Den Grad der Auslagerung kann ich Ihnen nicht nennen.

Grieger : Welche Anwendungen und IT-Systeme werden ihrer Meinung nach benötigt, um den Geschäftsprozess der Normsetzung in einer obersten Landesbehörde wahrzunehmen?

Mayer :  Die allgemeinen IT-Systeme werden. Wir haben auch Fachverfahren, die für die Normsetzung aber nicht benötigt werden.

Grieger : Welche Systeme würden sie benennen, wenn sie sie aufzählen müssten?

Mayer : Allgemeine Server, Clients, Windows-Betriebssystem.

<!-- page: 196 -->

Grieger :  Und Anwendungen für die Sachbearbeitung? Nutzen sie beispielsweise ein Vorgangsbearbeitungssystem?

Mayer : Ja, wir nutzen ein elektronisches Aktensystem für die Bearbeitung.

Grieger : Ich habe eine Aufzählung vorbereitet, in der es um verschiedene Zielobjekte geht. Ich habe diese Liste ihnen vorab zur Verfügung gestellt und ich bitte sie nun jeweils zu den Objekten anzugeben, ob sie diese in einer obersten Landesbehörde für den Geschäftsprozess der Normsetzung benötigen.

Mayer

: Ok.

Grieger

: Nutzen sie das Windows Betriebssystem?

Mayer : Ja.

Grieger

Mayer

: Welche Version?

: Das sind Informationen, die ich nicht weitergeben kann.

Grieger

: Wird ein Dateiserver verwendet?

Mayer : Ja.

Grieger

: Active Directory?

Mayer : Ja.

Grieger

: Microsoft Exchange?

Mayer : Ja.

Grieger : Wird Windows ebenfalls als Server-Betriebssystem genutzt. Sie müssen keine konkrete Version nennen.

Mayer : Ja, das wird genutzt.

Grieger : Wird zu der Vernetzung der Systeme die Gebäudeverkabelung benutzt oder drahtlose Verbindungen?

Mayer : In der Regel wird die Gebäudeverkabelung verwendet, es gibt auch ein drahtloses Netzwerk.

<!-- page: 197 -->

Grieger

: Firewall?

Mayer : Ja.

Grieger

: Und ein Signatur-Dienst, also eine Public Key Infrastruktur?

Mayer

: Ich glaube nicht, dass so etwas vorhanden ist.

Grieger

: Ein Serverraum?

Mayer : Ja.

Grieger

: In der obersten Landesbehörde oder ausgelagert?

Mayer

: Auch in der obersten Landesbehörde.

Grieger :  Wurde  eine  Schutzbedarfsfeststellung  für  die  Zielobjekte  in  ihrer  Behörde durchgeführt?

Mayer : Bis jetzt nicht, wir befinden uns in der Bearbeitung und diese ist noch nicht fertiggestellt.

Grieger : Haben sie denn Schutzbedarfskategorien festgelegt?

Mayer : Ja, die üblichen?

Grieger : Die des BSI oder auf welche beziehen sie sich?

Mayer : Wir haben die vorgegebenen vom BSI verwendet.

Grieger : Wie würden sie den Schutzbedarf der Normsetzung bezogen auf Vertraulichkeit, Integrität und Verfügbarkeit einschätzen?

Mayer : Das kommt darauf an, dass lässt sich schwer generalisieren. Es gibt Bereiche, wo es um sensible Dinge geht, wo der Schutzbedarf hoch ist. Bei uns würde ich von einem sehr hohen Schutzbedarf nicht ausgehen.

Grieger : Wo würden sie denn in diesem Gebiet von einem hohen Schutzbedarf sprechen?

Mayer : Ich würde sagen, vor allem, wenn personenbezogene Daten betroffen sind.

<!-- page: 198 -->

Grieger : Ausgehend davon hätte ich gerne ihre Einschätzung bezüglich der Schutzbedarfe der zuvor angesprochenen Zielobjekte. Mir ist bewusst, dass sie ad-hoc manche Effekte wie Vererbung und Kumulationseffekte nicht überblicken können. Dennoch würde ich sie um eine Einschätzung bitten. Wie würden sie bei einem Betriebssystem die Schutzbedarfe Vertraulichkeit, Integrität und Verfügbarkeit einschätzen?

Mayer : Die Vertraulichkeit kann hoch sein, es ist aber generell schwierig da Aussagen zu treffen, da sich unsere Umsetzung dort noch nicht befindet.

Grieger : Das würde sich das auch bei den anderen Zielobjekten wiederholen?

Mayer : Ja.

Grieger : Dann würde ich nochmal auf den Geschäftsprozess zurückkommen. Wie würden sie die Vertraulichkeit des Geschäftsprozesses der Beteiligung an der Normsetzung einschätzen?

Mayer : Normal bis hoch. Es ist schwierig, dass so zu sagen.

Grieger : Grundsätzlich gibt es ja zunehmende Transparenzprozesse, besonders bei Gesetzesvorhaben. Sehen sie die Vertraulichkeit eher sinken, wenn immer weiter Transparenz geschaffen wird?

Mayer : Ja.

Grieger : Wie sehen sie das im Bereich der Integrität.

Mayer : Da würde ich den Schutzbedarf eher hoch ansetzen.

Grieger : Und bezüglich der Verfügbarkeit?

Mayer : Ein normaler Schutzbedarf.

Grieger : Wie schätzen sie denn den Risikoappetit ihrer Behörde ein?

Mayer : Ich würde sagen gering bis mittel. Es kommt darauf an. Es gibt Bereiche, da ist sicherlich auch ein mittlerer Risikoappetit vorhanden. Wenn es irgendwo zu aufwändig wird gewisse Dinge umzusetzen, da wird in der Behörde eher das Risiko eingegangen.

Grieger : Was wären denn weitere Gründe für diesen mittleren Risikoappetit?

Mayer : Es gibt den ein oder anderen Punkt, wo die Eintrittswahrscheinlichkeit nicht sehr hoch ist, wo aber das Risiko auch nicht mehr nur gering ist. Die Einführung der Schutzmechanismen wäre aber so umfangreich, dass man eher bereit ist das Risiko in Kauf zu nehmen.

<!-- page: 199 -->

Grieger : Wird das Risiko dann durch die Verantwortlichen bewusst in Kauf genommen?

Mayer : Ja.

Grieger : Gibt es in ihrer Behörde eine Operationalisierung der Eintrittswahrscheinlichkeiten und -auswirkungen?

Mayer : Bislang nicht, nein.

Grieger : Wird dort dann zukünftig ein qualitativer oder quantitativer Ansatz verfolgt?

Mayer :  Da wir uns in der Umsetzung befinden, kann ich das noch nicht zuverlässig sagen.

Grieger :  Haben Sie noch Anmerkungen zu dem IT-Grundschutz-Profil und diesem Interview?

Mayer

: Nein.

Grieger

: Dann danke ich Ihnen für dieses Interview.

Mayer

: Gerne.

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 5 -->

> ix

> xi

> 1.1

> 1.2

> 2.1

> 2.2

<!-- page: 6 -->

> vii

<!-- page: 7 -->

> viii

<!-- page: 11 -->

> xii

<!-- page: 28 -->

> 2703x

> 2703x

> Vocabulary standard

> Guidelines standards

> Sector-specific guidelines

> TR 27008

> TR 27016

> Control-specific guidelines

> 2703x

> 2704x

<!-- page: 31 -->

> Strategieentwicklung

> Realisierungsplan

> Notfallpläne

> Schulungen/Sensibilisierung

> Fehlerbehebung

<!-- page: 32 -->

> Scope, Context, Criteria

> Identification

> Risk Treatment

> Identification

> Identification

> Communication& Consultation

> Monitoring & Review

> Recording & Reporting

<!-- page: 36 -->

> Fortentwicklung des ISMS

> OrganisationdesInformationssicherheitsprozesses

<!-- page: 38 -->

> Analyse des Ist-Zustands

<!-- page: 47 -->

> Landesministerien

> Landesumweltamt

> Landesämter für

> Denkmalpflege

> Landeshauptkasse

> Landesforstdirektionen

> Oberbergämter

> Regierungspräsidien

> Ämter für Forstwirtschaft

> Ämter für Arbeitsschutz

> Kreise

> Kreisfreie Städte

> Landesmedienanstalten

> und Rundfunkanstalten

> Fachhochschulen und

> Universitäten

> Handwerkskammern

<!-- page: 48 -->

> Referat Z.1

> Referat Z.2

<!-- page: 83 -->

> kes

<!-- page: 87 -->

> Projektor

<!-- page: 94 -->

> lichtlich

<!-- page: 106 -->

> Konsistenz

> Benutzbarkeit

> Ethik

> Nebeneffekte

> Organisationelle

> Konsistenz

> Nebeneffekte

> Konsistenz

> Nebeneffekte

> Einfachheit

> Klarheit

> Stil

> Einheitlichkeit

> Korrespondenz zu

> Phänomentreue

> Efffizenz

> Volllständigkeit

> Konsistenz

> Genauigkeit

> Evolution

> Robustheit

> Lernfähigkeit

<!-- page: 133 -->

> Die Verfügbarkeit ist bei einer 8x5 Verwaltung (oberste Landesbehörde) als nachran-

<!-- page: 138 -->

> cxxvii

<!-- page: 146 -->

> Projektor

<!-- page: 169 -->

> lichtlich
