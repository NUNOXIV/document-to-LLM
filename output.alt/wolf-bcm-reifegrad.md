---
source_file: "Wolf_BCM_Reifegrad.pdf"
source_sha256: b6f9f7cb917b154a51fa900346bdb3ff006e622007a37afef95cb28d46885697
source_bytes: 3726909
pages: 167
tables: 91
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T21:15:52+00:00"
text_coverage_percent: 99.99
appended_source_lines: 25
restored_hyphens: 9
extraction_status: warn
warnings:
  - "9 Tabellenzelle(n) beginnen mitten im Satz — moegliche Zellverschiebung, z. B. \"des Befugnisse in- und BAO notwendigen (beispielsweise Schul...\". Zeilen dieser Tabelle vor dem Zitat gegen die Quelle pruefen."
  - "9 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): 330xxReihe -> 330xx-Reihe, AssessmentKomponente -> Assessment-Komponente, AssessmentModells -> Assessment-Modells, AufbauBCMS -> Aufbau-BCMS, BCMReifegradmodelle -> BCM-Reifegradmodelle"
  - "Der Textlayer der Quelle enthaelt 1639 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
  - "25 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

## Erstellung eines Reifegradmodells für den BSI-Standard 200-4

## Masterarbeit

zur Erlangung des Grades Master of Science des Fachbereichs Wirtschaft der Technischen Hochschule Brandenburg

vorgelegt von: Victor Wolf geb. am 07. Mai 1994 in Berlin Studiengang Security Management

Betreuer: Prof. Dr. Heinz-Dieter Schmelling Zweitgutachter: Daniel Gilles (BSI)

Berlin, den 20. September 2021

<!-- page: 2 -->

## Inhaltsverzeichnis

| Abbildungsverzeichnis ...................................................................................     | Abbildungsverzeichnis ...................................................................................     | Abbildungsverzeichnis ...................................................................................     | III   |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------|
| Tabellenverzeichnis ......................................................................................... | Tabellenverzeichnis ......................................................................................... | Tabellenverzeichnis ......................................................................................... | V     |
| Abkürzungsverzeichnis .................................................................................       | Abkürzungsverzeichnis .................................................................................       | Abkürzungsverzeichnis .................................................................................       | VII   |
| 1                                                                                                             | Einleitung .............................................................................................      | Einleitung .............................................................................................      | 1     |
| 1.1                                                                                                           | Ausgangslage und Problemstellung ......................................................                       | Ausgangslage und Problemstellung ......................................................                       | 1     |
| 1.2                                                                                                           | Zielsetzung ............................................................................................      | Zielsetzung ............................................................................................      | 2     |
| 1.3                                                                                                           | Vorgehensweise und inhaltlicher Aufbau der Arbeit ..............................                              | Vorgehensweise und inhaltlicher Aufbau der Arbeit ..............................                              | 3     |
| 2                                                                                                             | Inhaltliche Grundlagen ........................................................................               | Inhaltliche Grundlagen ........................................................................               | 6     |
| 2.1                                                                                                           | Business Continuity Management .........................................................                      | Business Continuity Management .........................................................                      | 6     |
|                                                                                                               | 2.1.1                                                                                                         | Begriffsdefinitionen ...................................................................                      | 6     |
|                                                                                                               | 2.1.2                                                                                                         | Historische Entwicklung des BCMS ..........................................                                   | 8     |
|                                                                                                               | 2.1.3                                                                                                         | BCMS gemäß BSI-Standard 200-4 (CD) ................................                                           | 11    |
| 2.2                                                                                                           | Reifegradmodelle.................................................................................             | Reifegradmodelle.................................................................................             | 16    |
|                                                                                                               | 2.2.1                                                                                                         | Anwendungszweck .................................................................                             | 16    |
|                                                                                                               | 2.2.2                                                                                                         | Struktureller Aufbau ................................................................                         | 17    |
|                                                                                                               | 2.2.3                                                                                                         | Ausprägungen von Reifegradmodellen ...................................                                        | 19    |
|                                                                                                               | 2.2.4                                                                                                         | Vorgehensmodelle zur Entwicklung von Reifegradmodellen                                                        | .. 23 |
| 3                                                                                                             | Reifegradmodell für den BSI-Standard 200-4 ..................................                                 | Reifegradmodell für den BSI-Standard 200-4 ..................................                                 | 27    |
| 3.1                                                                                                           | Methodische Vorgehensweise .............................................................                      | Methodische Vorgehensweise .............................................................                      | 27    |
|                                                                                                               | 3.1.1                                                                                                         | Problemdefinition ....................................................................                        | 28    |
|                                                                                                               | 3.1.2                                                                                                         | Anforderungen an das Reifegradmodell..................................                                        | 29    |
|                                                                                                               | 3.1.3                                                                                                         | Bewertung bestehender BCM-Reifegradmodelle ....................                                               | 31    |
|                                                                                                               | 3.1.4                                                                                                         | Festlegung der Entwicklungsstrategie.....................................                                     | 36    |
|                                                                                                               | 3.1.5                                                                                                         | Diskussion und Auswahl der Modellbasis ...............................                                        | 37    |
| 3.2                                                                                                           | Entwicklung der Modellinhalte .............................................................                   | Entwicklung der Modellinhalte .............................................................                   | 41    |
|                                                                                                               | 3.2.1                                                                                                         | Das Prozess-Referenzmodell .................................................                                  | 41    |
|                                                                                                               | 3.2.2                                                                                                         | Der Bewertungsrahmen ..........................................................                               | 45    |
|                                                                                                               | 3.2.3                                                                                                         | Das Prozess-Assessment-Modell ...........................................                                     | 49    |
| 3.3                                                                                                           | Entwicklung des Erhebungstools (Prototyp) ......................................                              | Entwicklung des Erhebungstools (Prototyp) ......................................                              | 101   |
|                                                                                                               | 3.3.1                                                                                                         | Anwendungslogik ..................................................................                            | 102   |
|                                                                                                               | 3.3.2                                                                                                         | Datenmodell ..........................................................................                        | 103   |
|                                                                                                               | 3.3.3                                                                                                         | Erläuterung der Tabellenblätter .............................................                                 | 104   |

<!-- page: 3 -->

| 4                                                                                                          | Evaluation des Reifegradmodells ..................................................                         |   111 |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------|
| 4.1                                                                                                        | Zielsetzung, Vorgehensweise und Teilnehmer der Evaluation ..........                                       |   111 |
| 4.2                                                                                                        | Evaluationskriterien ...........................................................................           |   114 |
| 4.3                                                                                                        | Ergebnisse der Evaluation .................................................................                |   116 |
| 5                                                                                                          | Fazit ..................................................................................................   |   119 |
| 5.1                                                                                                        | Konsolidierung der Ergebnisse ..........................................................                   |   119 |
| 5.2                                                                                                        | Ausblick .............................................................................................     |   121 |
| Literaturverzeichnis ..................................................................................... | Literaturverzeichnis ..................................................................................... |   124 |
| Anhang I: Vergleich bestehender BCM-Reifegradmodelle .......................                               | Anhang I: Vergleich bestehender BCM-Reifegradmodelle .......................                               |   129 |
| Anhang II: Prozessbeschreibungen des PRM ...........................................                       | Anhang II: Prozessbeschreibungen des PRM ...........................................                       |   133 |
| Anhang III: Aufbau der Reifegradstufen (gemäß ISO/IEC 33020) .............                                 | Anhang III: Aufbau der Reifegradstufen (gemäß ISO/IEC 33020) .............                                 |   143 |
| Anhang IV: Excel-basiertes Erhebungstool ...............................................                   | Anhang IV: Excel-basiertes Erhebungstool ...............................................                   |   145 |
| Anhang V: Evaluationsbögen zur Bewertung des Reifegradmodells ...... 146                                   | Anhang V: Evaluationsbögen zur Bewertung des Reifegradmodells ...... 146                                   |       |

<!-- page: 4 -->

## Abbildungsverzeichnis

| Abbildung 1: Inhaltlicher Aufbau der Arbeit ........................................................   |
|--------------------------------------------------------------------------------------------------------|

<!-- page: 5 -->

| Abbildung 29: Auszug der Statements im Evaluationsbogen .........................                                       | 115                            |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| Abbildung 30: Gesamtübersicht der Evaluationsergebnisse                                                                 | .......................... 116 |
| Abbildung 31: Evaluationsergebnisse im direkten Vergleich ..........................                                    | 117                            |
| Abbildung 32: Durchschnittlicher Zustimmungsgrad (Mittelwert) der Evaluation                                            |                                |
| ....................................................................................................................... | 117                            |
| Abbildung 34: Vorlage des Evaluationsbogens, Teil II ...................................                                | 147                            |
| Abbildung 35: Evaluationsbogen Optimal Systems, Teil I ..............................                                   | 148                            |
| Abbildung 36: Evaluationsbogen Optimal Systems, Teil II .............................                                   | 149                            |
| Abbildung 37: Evaluationsbogen Vivantes, Teil I ............................................                            | 150                            |
| Abbildung 38: Evaluationsbogen Vivantes, Teil II ...........................................                            | 151                            |
| Abbildung 39: Evaluationsbogen Handelsunternehmen, Teil I .......................                                       | 152                            |
| Abbildung 40: Evaluationsbogen Handelsunternehmen, Teil II ......................                                       | 153                            |
| Abbildung 41: Evaluationsbogen Handelsunternehmen, Teil III .....................                                       | 154                            |
| Abbildung 42: Evaluationsbogen DKB Service GmbH, Teil I ..........................                                      | 155                            |
| Abbildung 43: Evaluationsbogen DKB Service GmbH, Teil II .........................                                      | 156                            |
| Abbildung 44: Evaluationsbogen BSI, Teil I ...................................................                          | 157                            |
| Abbildung 45: Evaluationsbogen BSI, Teil II...................................................                          | 158                            |

<!-- page: 6 -->

## Tabellenverzeichnis

| Tabelle 1: Typische Bestandteile eines Reifegradmodells ...............................                                                                                                  | Tabelle 1: Typische Bestandteile eines Reifegradmodells ...............................                                                                                                  | Tabelle 1: Typische Bestandteile eines Reifegradmodells ...............................                                                                                                  | Tabelle 1: Typische Bestandteile eines Reifegradmodells ...............................                                                                                                  | Tabelle 1: Typische Bestandteile eines Reifegradmodells ...............................                                                                                                  | Tabelle 1: Typische Bestandteile eines Reifegradmodells ...............................   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Tabelle 2: Prozesssteckbrief MP.1 ...................................................................                                                                                    | Tabelle 2: Prozesssteckbrief MP.1 ...................................................................                                                                                    | Tabelle 2: Prozesssteckbrief MP.1 ...................................................................                                                                                    | Tabelle 2: Prozesssteckbrief MP.1 ...................................................................                                                                                    | Tabelle 2: Prozesssteckbrief MP.1 ...................................................................                                                                                    | 44                                                                                        |
| Tabelle                                                                                                                                                                                  | 3:                                                                                                                                                                                       | Beschreibung                                                                                                                                                                             | der                                                                                                                                                                                      | zur Identifikation                                                                                                                                                                       | der                                                                                       |
| Reifegradstufen ................................................................................................                                                                         | Reifegradstufen ................................................................................................                                                                         | Reifegradstufen ................................................................................................                                                                         | Reifegradstufen ................................................................................................                                                                         | Reifegradstufen ................................................................................................                                                                         | 46                                                                                        |
| Tabelle 4: Prozessattribute gemäß ISO/IEC 33020 ..........................................                                                                                               | Tabelle 4: Prozessattribute gemäß ISO/IEC 33020 ..........................................                                                                                               | Tabelle 4: Prozessattribute gemäß ISO/IEC 33020 ..........................................                                                                                               | Tabelle 4: Prozessattribute gemäß ISO/IEC 33020 ..........................................                                                                                               | Tabelle 4: Prozessattribute gemäß ISO/IEC 33020 ..........................................                                                                                               | 47                                                                                        |
| Tabelle 5: Bewertungsskala gemäß ISO/IEC 33020 ........................................                                                                                                  | Tabelle 5: Bewertungsskala gemäß ISO/IEC 33020 ........................................                                                                                                  | Tabelle 5: Bewertungsskala gemäß ISO/IEC 33020 ........................................                                                                                                  | Tabelle 5: Bewertungsskala gemäß ISO/IEC 33020 ........................................                                                                                                  | Tabelle 5: Bewertungsskala gemäß ISO/IEC 33020 ........................................                                                                                                  | 47                                                                                        |
| Tabelle 6: Schematische Zusammensetzung der Zielniveaus..........................                                                                                                        | Tabelle 6: Schematische Zusammensetzung der Zielniveaus..........................                                                                                                        | Tabelle 6: Schematische Zusammensetzung der Zielniveaus..........................                                                                                                        | Tabelle 6: Schematische Zusammensetzung der Zielniveaus..........................                                                                                                        | Tabelle 6: Schematische Zusammensetzung der Zielniveaus..........................                                                                                                        | 49                                                                                        |
| Tabelle 7: MP.1: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 7: MP.1: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 7: MP.1: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 7: MP.1: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 7: MP.1: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | 53                                                                                        |
| Tabelle 8: MP.2: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 8: MP.2: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 8: MP.2: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 8: MP.2: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 8: MP.2: Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | 56                                                                                        |
| Tabelle 9: LP.1: Reifegradstufen und spezifische Fragestellungen ..................                                                                                                      | Tabelle 9: LP.1: Reifegradstufen und spezifische Fragestellungen ..................                                                                                                      | Tabelle 9: LP.1: Reifegradstufen und spezifische Fragestellungen ..................                                                                                                      | Tabelle 9: LP.1: Reifegradstufen und spezifische Fragestellungen ..................                                                                                                      | Tabelle 9: LP.1: Reifegradstufen und spezifische Fragestellungen ..................                                                                                                      | 60                                                                                        |
| Tabelle 10: LP.2: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 10: LP.2: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 10: LP.2: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 10: LP.2: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 10: LP.2: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | 64                                                                                        |
| Tabelle 11: LP.3: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 11: LP.3: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 11: LP.3: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 11: LP.3: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 11: LP.3: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | 67                                                                                        |
| Tabelle 12: LP.4 Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 12: LP.4 Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 12: LP.4 Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 12: LP.4 Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | Tabelle 12: LP.4 Reifegradstufen und spezifische Fragestellungen .................                                                                                                       | 70                                                                                        |
| Tabelle 13: LP.5: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 13: LP.5: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 13: LP.5: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 13: LP.5: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 13: LP.5: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | 74                                                                                        |
| Tabelle 14: LP.6: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 14: LP.6: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 14: LP.6: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 14: LP.6: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 14: LP.6: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | 77                                                                                        |
| Tabelle 15: LP.7: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 15: LP.7: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 15: LP.7: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 15: LP.7: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 15: LP.7: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | 81                                                                                        |
| Tabelle 16: LP.8: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 16: LP.8: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 16: LP.8: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 16: LP.8: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 16: LP.8: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | 85                                                                                        |
| Tabelle 17: LP.9: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 17: LP.9: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 17: LP.9: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 17: LP.9: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | Tabelle 17: LP.9: Reifegradstufen und spezifische Fragestellungen ................                                                                                                       | 88                                                                                        |
| Tabelle 18: SP.1: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | Tabelle 18: SP.1: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | Tabelle 18: SP.1: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | Tabelle 18: SP.1: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | Tabelle 18: SP.1: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | 92                                                                                        |
| Tabelle 19: SP.2: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | Tabelle 19: SP.2: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | Tabelle 19: SP.2: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | Tabelle 19: SP.2: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | Tabelle 19: SP.2: Reifegradstufen und spezifische Fragestellungen ...............                                                                                                        | 96                                                                                        |
| Tabelle 20: SP.3: Reifegradstufen und spezifische Fragestellungen .............                                                                                                          | Tabelle 20: SP.3: Reifegradstufen und spezifische Fragestellungen .............                                                                                                          | Tabelle 20: SP.3: Reifegradstufen und spezifische Fragestellungen .............                                                                                                          | Tabelle 20: SP.3: Reifegradstufen und spezifische Fragestellungen .............                                                                                                          | Tabelle 20: SP.3: Reifegradstufen und spezifische Fragestellungen .............                                                                                                          | 100                                                                                       |
| Tabelle 21: Optionen zur Erprobung des Reifegradmodels für den BSI-Standard                                                                                                              | Tabelle 21: Optionen zur Erprobung des Reifegradmodels für den BSI-Standard                                                                                                              | Tabelle 21: Optionen zur Erprobung des Reifegradmodels für den BSI-Standard                                                                                                              | Tabelle 21: Optionen zur Erprobung des Reifegradmodels für den BSI-Standard                                                                                                              | Tabelle 21: Optionen zur Erprobung des Reifegradmodels für den BSI-Standard                                                                                                              |                                                                                           |
| 200-4 ..............................................................................................................                                                                     | 200-4 ..............................................................................................................                                                                     | 200-4 ..............................................................................................................                                                                     | 200-4 ..............................................................................................................                                                                     | 200-4 ..............................................................................................................                                                                     | 113                                                                                       |
| Tabelle 22: Teilnehmer der Evaluation des Reifegradmodells .......................                                                                                                       | Tabelle 22: Teilnehmer der Evaluation des Reifegradmodells .......................                                                                                                       | Tabelle 22: Teilnehmer der Evaluation des Reifegradmodells .......................                                                                                                       | Tabelle 22: Teilnehmer der Evaluation des Reifegradmodells .......................                                                                                                       | Tabelle 22: Teilnehmer der Evaluation des Reifegradmodells .......................                                                                                                       | 114                                                                                       |
| Tabelle 23: Evaluationskriterien für das Reifegradmodell (basierend auf Anforderungen an das Reiferadmodell) ..........................................................                  | Tabelle 23: Evaluationskriterien für das Reifegradmodell (basierend auf Anforderungen an das Reiferadmodell) ..........................................................                  | Tabelle 23: Evaluationskriterien für das Reifegradmodell (basierend auf Anforderungen an das Reiferadmodell) ..........................................................                  | Tabelle 23: Evaluationskriterien für das Reifegradmodell (basierend auf Anforderungen an das Reiferadmodell) ..........................................................                  | Tabelle 23: Evaluationskriterien für das Reifegradmodell (basierend auf Anforderungen an das Reiferadmodell) ..........................................................                  | den 115                                                                                   |
| Tabelle 24: Tabellarische Darstellung der Evaluationsergebnisse .................                                                                                                        | Tabelle 24: Tabellarische Darstellung der Evaluationsergebnisse .................                                                                                                        | Tabelle 24: Tabellarische Darstellung der Evaluationsergebnisse .................                                                                                                        | Tabelle 24: Tabellarische Darstellung der Evaluationsergebnisse .................                                                                                                        | Tabelle 24: Tabellarische Darstellung der Evaluationsergebnisse .................                                                                                                        | 116                                                                                       |
| Tabelle 25: Detailbetrachtung BCM-Reifegradmodell Klawitter (1997) ..........                                                                                                            | Tabelle 25: Detailbetrachtung BCM-Reifegradmodell Klawitter (1997) ..........                                                                                                            | Tabelle 25: Detailbetrachtung BCM-Reifegradmodell Klawitter (1997) ..........                                                                                                            | Tabelle 25: Detailbetrachtung BCM-Reifegradmodell Klawitter (1997) ..........                                                                                                            | Tabelle 25: Detailbetrachtung BCM-Reifegradmodell Klawitter (1997) ..........                                                                                                            | 130                                                                                       |
| Tabelle 26: Detailbetrachtung BCM-Reifegradmodell Smit (2005) .................                                                                                                          | Tabelle 26: Detailbetrachtung BCM-Reifegradmodell Smit (2005) .................                                                                                                          | Tabelle 26: Detailbetrachtung BCM-Reifegradmodell Smit (2005) .................                                                                                                          | Tabelle 26: Detailbetrachtung BCM-Reifegradmodell Smit (2005) .................                                                                                                          | Tabelle 26: Detailbetrachtung BCM-Reifegradmodell Smit (2005) .................                                                                                                          | 131                                                                                       |
| Tabelle 27: Detailbetrachtung BCM-Reifegradmodell Randeree (2012) ........                                                                                                               | Tabelle 27: Detailbetrachtung BCM-Reifegradmodell Randeree (2012) ........                                                                                                               | Tabelle 27: Detailbetrachtung BCM-Reifegradmodell Randeree (2012) ........                                                                                                               | Tabelle 27: Detailbetrachtung BCM-Reifegradmodell Randeree (2012) ........                                                                                                               | Tabelle 27: Detailbetrachtung BCM-Reifegradmodell Randeree (2012) ........                                                                                                               | 132                                                                                       |
| Tabelle 28: Prozesssteckbrief MP.1 Initiierung, Planung und Steuerung BCMS ............................................................................................................. | Tabelle 28: Prozesssteckbrief MP.1 Initiierung, Planung und Steuerung BCMS ............................................................................................................. | Tabelle 28: Prozesssteckbrief MP.1 Initiierung, Planung und Steuerung BCMS ............................................................................................................. | Tabelle 28: Prozesssteckbrief MP.1 Initiierung, Planung und Steuerung BCMS ............................................................................................................. | Tabelle 28: Prozesssteckbrief MP.1 Initiierung, Planung und Steuerung BCMS ............................................................................................................. | des 133                                                                                   |
| Tabelle 29: Prozesssteckbrief MP.2 Managementreview ...............................                                                                                                      | Tabelle 29: Prozesssteckbrief MP.2 Managementreview ...............................                                                                                                      | Tabelle 29: Prozesssteckbrief MP.2 Managementreview ...............................                                                                                                      | Tabelle 29: Prozesssteckbrief MP.2 Managementreview ...............................                                                                                                      | Tabelle 29: Prozesssteckbrief MP.2 Managementreview ...............................                                                                                                      | 134                                                                                       |
| Tabelle 30: Prozesssteckbrief LP.1 Befähigung der Stabsstrukturen .............                                                                                                          | Tabelle 30: Prozesssteckbrief LP.1 Befähigung der Stabsstrukturen .............                                                                                                          | Tabelle 30: Prozesssteckbrief LP.1 Befähigung der Stabsstrukturen .............                                                                                                          | Tabelle 30: Prozesssteckbrief LP.1 Befähigung der Stabsstrukturen .............                                                                                                          | Tabelle 30: Prozesssteckbrief LP.1 Befähigung der Stabsstrukturen .............                                                                                                          | 134                                                                                       |
| Tabelle 31: Prozesssteckbrief LP.2 Meldung, Alarmierung, Erstreaktion .......                                                                                                            | Tabelle 31: Prozesssteckbrief LP.2 Meldung, Alarmierung, Erstreaktion .......                                                                                                            | Tabelle 31: Prozesssteckbrief LP.2 Meldung, Alarmierung, Erstreaktion .......                                                                                                            | Tabelle 31: Prozesssteckbrief LP.2 Meldung, Alarmierung, Erstreaktion .......                                                                                                            | Tabelle 31: Prozesssteckbrief LP.2 Meldung, Alarmierung, Erstreaktion .......                                                                                                            | 135                                                                                       |
| Tabelle 32: Prozesssteckbrief LP.3 Störbetrieb, Deeskalation und Bewältigung                                                                                                             | Tabelle 32: Prozesssteckbrief LP.3 Störbetrieb, Deeskalation und Bewältigung                                                                                                             | Tabelle 32: Prozesssteckbrief LP.3 Störbetrieb, Deeskalation und Bewältigung                                                                                                             | Tabelle 32: Prozesssteckbrief LP.3 Störbetrieb, Deeskalation und Bewältigung                                                                                                             | Tabelle 32: Prozesssteckbrief LP.3 Störbetrieb, Deeskalation und Bewältigung                                                                                                             |                                                                                           |

....................................................................................................................... 136

<!-- page: 7 -->

| Tabelle 33: Prozesssteckbrief LP.4 Business-Impact-Analyse .......................                                                                                                                  |   137 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| Tabelle 34: Prozesssteckbrief LP.5 BCM-Risikoanalyse und Soll-Ist-Vergleich ....................................................................................................................... |   138 |
| Tabelle 35: Prozesssteckbrief LP.6 Notfallplanung und Konzeption ..............                                                                                                                     |   139 |
| Tabelle 36: Prozesssteckbrief LP.7 Tests- und Übungen ...............................                                                                                                               |   139 |
| Tabelle 37: Prozesssteckbrief LP.8 Überprüfung und Berichterstattung ........                                                                                                                       |   140 |
| Tabelle 38: Prozesssteckbrief LP.9 Kontinuierliche Verbesserung ................                                                                                                                    |   141 |
| Tabelle 39: Prozesssteckbrief SP.1 Dokumentenlenkung ..............................                                                                                                                 |   141 |
| Tabelle 40: Prozesssteckbrief SP.2 BCM Aufbauorganisation .......................                                                                                                                   |   142 |
| Tabelle 41: Prozesssteckbrief SP.3 Schulung und Sensibilisierung ...............                                                                                                                    |   142 |
| Tabelle 42: Ableitung der Reifegrade in Abhängigkeit der Prozessattribute ...                                                                                                                       |   144 |

<!-- page: 8 -->

## Abkürzungsverzeichnis

Abkürzung

BAO

BCI

BCMS

BIA

BSI

bzw.

CD

CMMI

DRI

ER-Modell

etc.

GPG

GQM

HLS

HVB

ISMS

ISO

LP

MM

MP

PA

PAM

PDCA

PRM

RG

SP

SPICE

SPQS

u. a.

z. B.

Beschreibung

Besondere Aufbauorganisation

Business Continuity Institute

Business Continuity Management System

Business-Impact-Analyse

Bundesamt für Sicherheit in der Informationstechnik

beziehungsweise

Community Draft

Capability Maturity Model Integration

Disaster Recovery Institute

Entity-Relationship-Modell

et cetera

Good Practice Guidelines

Goal Question Metric

High Level Structure

Hochverfügbarkeits-Benchmark

Information Security Management System

International Organisation for Standardisation

Lifecycle-Prozess

Messmodell

Management-Prozess

Prozess-Attribut

Prozess-Assessment-Modell

Plan, Do, Check, Act

Prozess-Referenz-Modell

Reifegradstufe

Support-Prozess

Software Process Improvement and Capability Determination

Scope Process Quality Stages

unter anderem

zum Beispiel

<!-- page: 9 -->

## 1  Einleitung

## 1.1  Ausgangslage und Problemstellung

Jeder Vorfall - unabhängig seiner Art und Weise - hat das Potential, die Fortsetzung der Geschäftsfähigkeit einer Organisation zu beeinträchtigen. Organisationen, die in Bezug auf ihre Geschäftskontinuität ausreichende Vorsorgemaßnahmen treffen, können die Auswirkungen von Betriebsunterbrechungen auf ein akzeptables  Maß  reduzieren. 1   Die  Fähigkeit,  angemessen  auf  Vorfälle  und  Betriebsunterbrechungen reagieren zu können, wird jedoch nicht erst nach Eintritt eines Vorfalls aufgebaut. Vielmehr sind hierzu präventive und regelmäßig durchgeführte Prozesse notwendig, um eine angemessene Reaktion auf Vorfälle zu ermöglichen. 2  Die Implementierung eines Business Continuity Management System (BCMS) ist ein hilfreiches Präventionsinstrument, diese Prozesse zu steuern, zu analysieren und kontinuierlich zu verbessern. 3  Dies ermöglicht es, Geschäftsprozesse nach einer Störung auf einem akzeptablen Niveau aufrechtzuerhalten. Dem BCMS unterliegt - wie für Managementsysteme charakteristisch - ein kontinuierlicher Verbesserungsprozess. Dieser ermöglicht es, das Managementsystem kontinuierlich an die sich ändernden Rahmenbedingungen anzupassen und stetig zu verbessern.

Ein Prozess wird als eine Reihe von aufeinanderfolgenden Aktivitäten und Aufgaben für die Erreichung eines bestimmten Ziels definiert. 4  Prozesse gelten nach Randeree et al. (2012) als Dreh- und Angelpunkt für eine nachhaltige Verbesserung einer Organisation. Prozesse können unterschiedliche Entwicklungsstufen (Reifegrade) aufweisen. Die Reife eines Prozesses kann mit Hilfe von Reifegradmodellen ermittelt werden. 5  Reifegradmodelle gewinnen zunehmend an Bedeutung: Beispielsweise durch Vorgaben von Auftraggebern oder unternehmensweiten Richtlinien, die eine Erreichung bestimmter Zielreifegrade einzelner Unter-

nehmensteile fordern. 6

Um Organisationen eine praxisnahe Anleitung für den Aufbau eines BCMS zu liefern, hat das Bundesamt für Sicherheit in der Informationstechnik (BSI) im Januar 2021 den modernisierten BSI-Standard 200-4 im Community Draft (CD) veröffentlicht. Der BSI-Standard 200-4 löst somit den nunmehr veralteten BSI-Standard 100-4: Notfallmanagement ab. 7  Mithilfe von verschiedenen Startmodellen und eines praxisorientierten Ansatzes wird das Ziel verfolgt, Organisationen jeglicher Größe bei dem Aufbau und der kontinuierlichen Weiterentwicklung eines BCMS zu unterstützen. Um die Effektivität eines BCMS verbessern zu können, stehen Organisationen vor der Herausforderung, die Wirksamkeit und Effektivität des Managementsystems kontinuierlich zu überprüfen und Verbesserungen vorzunehmen. Reifegradmodelle könnten in einer solchen Situation als hilfreiches Instrument dienen, um die  derzeitige  Entwicklung  des  BCMS  einzuschätzen  und  zukünftige  Entwicklungspotentiale aufzuzeigen. 8, 9  Aufgrund der Aktualität des BSI-Standards 2004 ist derzeit kein geeignetes Reifegradmodell etabliert. Anwender des BSI-Standards 200-4 stehen demzufolge vor der Herausforderung, etablierte Strukturen an geänderte Rahmenbedingungen anzupassen, ohne dass ein passendes Hilfsmittel  existiert.  Ein  geeignetes  Reifegradmodell  für  den  BSI-Standard  200-4 könnte folglich  Anwender des BSI-Standards zukünftig dabei unterstützen,  ihr BCMS kontinuierlich und langfristig zu verbessern. 10

1  Vgl. Aleksandrova, V. et al., 2018, S. 14

2  Vgl. Venclova, K. et al., 2013, S. 895

3  Vgl. Aleksandrova, V. et al., 2018, S. 15

4  Vgl. Dayan, R. &amp; Evans, S., 2006, S. 72

5  Vgl. Randeree, et al., 2012, S. 473

6  Vg. Fritzsche, M. &amp; Keil, P., 2007, S. 95

<!-- page: 10 -->

## 1.2  Zielsetzung

Zentrales Ziel dieser Arbeit ist die Entwicklung eines Reifegradmodells für den BSI-Standard  200-4,  das  Anwender  bei  der  Identifikation  und  Bewertung  des Leistungsstands des BCMS unterstützt. Aus diesem übergreifenden Ziel leiten sich die folgenden Forschungsfragen der Thesis ab:

- Forschungsfrage 1: Was sind die zentralen Ziele und Fähigkeiten des BCMS auf Basis des BSI-Standards 200-4, und wie können diese in ein messbares Modell überführt werden?
- Forschungsfrage 2: Welche Rahmenbedingungen müssen bei der Entwicklung eines Reifegradmodells für den BSI-Standard 200-4 berücksichtigt werden?
- Forschungsfrage 3: In welchem Maße erfüllt das entwickelte Reifegradmodell die definierten Anforderungen?

7  Bundesamt für Sicherheit in der Informationstechnik, 2021

8  Vgl. Becker, P. et al., 2009, S. 249

9  Vgl. Lahrmann, G. &amp; Marx, F., 2010, S. 522

10  Vgl. Lahrmann, G. &amp; Marx, F. 2010, S. 522

<!-- page: 11 -->

Neben der Beantwortung der theoretischen Forschungsfragen wird die Ausarbeitung durch einen praktischen Anteil ergänzt. Ziel des Praxisanteils ist es, Anwendern ein hilfreiches Werkzeug bei der Umsetzung des BSI-Standards 200-4 zu liefern. Er beinhaltet die folgenden Aspekte:

- Beschreibung der systematischen Entwicklung des Reifegradmodells entlang eines erprobten Vorgehensmodells,
- Erstellung eines excel-basierten Erhebungstools zur Operationalisierung der Inhalte des Reifegradmodells sowie
- Durchführung von Experteninterviews zur Evaluation der praktischen Eignung des Reifegradmodells.

Die im Rahmen dieser Arbeit gewonnenen Erkenntnisse werden strukturiert aufbereitet.  Auf  Basis  der  Forschungsergebnisse  werden  zudem  Anknüpfungspunkte für zukünftige Arbeiten identifiziert.

## 1.3  Vorgehensweise und inhaltlicher Aufbau der Arbeit

Die Vorgehensweise zur Erstellung des Reifegradmodells ist in drei Phasen aufgeteilt. In der ersten Phase werden die Inhalte des Reifegradmodells konzipiert und entwickelt. Anschließend erfolgt die Erstellung des Erhebungstools. Dies soll den Transfer der theoretischen Inhalte in die praktische Anwendung ermöglichen. In Phase 3 wird das Reifegradmodell an ausgewählten Organisationen evaluiert und  hinsichtlich  der  Anwendbarkeit  bewertet.  Abbildung  1  visualisiert  das  geplante Vorgehensmodell der Abhandlung.

<!-- page: 12 -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 1: Inhaltlicher Aufbau der Arbeit

Inhaltlich gliedert sich die vorliegende Thesis in fünf Abschnitte. Abschnitt 1 widmet sich der Problemstellung sowie Zielsetzung der Arbeit. Inhaltlich wird deren Motivation  beschrieben,  das  Forschungsziel  definiert  sowie  die  Notwendigkeit des Reifegradmodells dargestellt. Abschnitt 2 widmet sich den inhaltlichen Grundlagen und Begrifflichkeiten, die für das Verständnis der Arbeit benötigt werden. Insbesondere beinhaltet dies die Beschreibung des BCMS und der inhaltlichen Ausgestaltung von Reifegradmodellen. Abschnitt 3 bildet den Kernbestandteil der Arbeit. Dieser Abschnitt beschreibt die Erstellung des Reifegradmodells für den BSI-Standard 200-4. Er teilt sich in die  Unterkapitel Methodische Vorgehensweise, Entwicklung der Modellinhalte, sowie Entwicklung des Erhebungstools auf. Hierzu werden zunächst die Problemstellung des Reifegradmodells analysiert sowie darauf aufbauend die zugrundeliegenden  Anforderungen  identifiziert.  Nachfolgend  werden  bereits  bestehende BCM-Reifegradmodelle analysiert und hinsichtlich ihrer praktischen Anwendbarkeit auf den BSI-Standard 200-4 bewertet. Zusätzlich wird ein geeignetes Basismodell für die inhaltliche Erstellung des Reifegradmodells ausgewählt und erläutert. Basierend auf der Vorgehensweise des ausgewählten Basismodells werden nachfolgend die Modellinhalte konzipiert. Schlussendlich wird ein excel-basiertes Erhebungstool erstellt, um die Modellinhalte zu operationalisieren.

<!-- page: 13 -->

In Abschnitt 4 erfolgt die Evaluation des Reifegradmodells. Hierzu wurden Experteninterviews mit ausgewählten Anwendern des BSI-Standards 200-4 unterschiedlicher Branchen durchgeführt. Abschnitt 5 fasst die Erkenntnisse der Thesis zusammen und liefert einen Ausblick für zukünftige Forschungen. Im Anhang befinden sich ergänzende Informationen für die Erhebung der einzel-

nen Reifegrade, ein detaillierter Vergleich bereits bestehender BCM-Reifegradmodelle sowie die ausgefüllten Evaluationsbögen.

<!-- page: 14 -->

## 2  Inhaltliche Grundlagen

## 2.1  Business Continuity Management

In diesem Abschnitt werden die grundlegenden Elemente eines BCMS beschrieben. Ziel des Abschnitts ist es,  das notwendige Verständnis für den methodischen Aufbau und den Betrieb eines BCMS zu schaffen sowie die elementaren Definitionen des Managementsystems zu erläutern.

## 2.1.1 Begriffsdefinitionen

## Business Continuity Management System:

Ein BCMS beschreibt den systematischen Aufbau sowie die kontinuierliche Verbesserung von präventiven und reaktiven Maßnahmen zur Aufrechterhaltung des Geschäftsbetriebs bei massiven Schadensereignissen. 11  Dies beinhaltet sowohl organisatorische,  technische  als  auch  personelle  Maßnahmen.  Hauptziel  des BCMS ist die Fortführung der kritischen Geschäftsprozesse nach Eintritt eines Schadensereignisses. Hierbei sollen die notwendigen Geschäftsaktivitäten auf einem  vorher  festgelegten  Niveau  fortgesetzt  sowie  in  einer  definierten  Zeitspanne wiederhergestellt werden. Wie jedes Managementsystem, verfolgt auch das BCMS eine zyklische und kontinuierliche Verbesserung. 12  In der Literatur existieren  weitere  Beschreibungen  eines  BCMS,  deren  jeweilige  Definition  jedoch den Rahmen der vorliegenden Arbeit sprengen würde.

## Kritische Geschäftsprozesse:

Geschäftsprozesse bestehen per Definition aus einer Menge logisch verknüpfter Einzeltätigkeiten, die ein bestimmtes betriebliches Ziel erreichen. 13  Kritische Geschäftsprozesse (oder auch: Fachverfahren) sind ebenjene Prozesse, die essenziell für den Bestand einer Institution und somit von besonderer Bedeutung für die Kernaufgaben der Organisation sind. 14  Kritische Geschäftsprozesse im Sinne des BCMS sind primär die zeitkritischen Geschäftsprozesse einer Institution. Ein Ausfall  eines  zeitkritischen  Geschäftsprozesses,  der  einen  zuvor  definierten Schwellwert  (die  maximale  Ausfallzeit)  überschreitet,  kann  mitunter  existenzbedrohend für eine Organisation werden. Ein tiefgreifendes Verständnis über die kritischen Geschäftsprozesse einer Organisation sowie deren angemessene Absicherung stellt sicher, dass das BCMS seinen Zweck erfüllt, und erhöht die Erfolgschancen im Schadensfall. 15

11  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 6-7

12  Vgl. Aleksandrova, V. et al., 2018, S. 14

13  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 10

14  Vgl. Kersten &amp; Klett, 2017, S. 134

<!-- page: 15 -->

## Business-Impact-Analyse (BIA):

Die  Analyse  von  Risiken  und  deren  Auswirkungen  auf  die  Geschäftstätigkeit (engl.: business ) sind ein wesentlicher Bestandteil des BCMS. 16  Um die tatsächlichen Auswirkungen eines Schadensereignisses abschätzen bzw. identifizieren zu können, wird ein Verständnis der Kernfunktionen bzw. der Kernprodukte einer Organisation benötigt. 17  Hierbei stehen primär die Auswirkungen (engl.: impact ) des Ausfalls eines kritischen Geschäftsprozesses im Fokus. Das Hauptziel einer Business-Impact-Analyse ist das Sammeln und Analysieren der notwendigen Informationen  zur  Identifikation  und  Priorisierung  (zeit-)kritischer  Geschäftsprozesse. Im Ergebnis der BIA werden alle kritischen Ressourcen und Geschäftsprozesse hinsichtlich ihrer Kritikalität bewertet. Da die Kontinuitätsstrategien des BCMS auf den Ergebnissen der BIA aufbauen, hängt der Erfolg des BCMS maßgeblich von deren Ergebnissen ab. 18

## PDCA Zyklus:

Der Plan-Do-Check-Act (PDCA)-Zyklus ist ein Modell, das bei der kontinuierlichen Verbesserung von Managementsystemen Verwendung findet. Ursprünglich wurde der Begriff des Modells durch Deming (1982) geprägt, weshalb es auch unter Deming-Zyklus bekannt ist. Deming war der Meinung, dass die regelmäßige Bewertung von Managementverfahren der Schlüssel für die Entwicklung eines erfolgreichen Unternehmens sei. 19  Der PDCA-Zyklus beschreibt den Prozess der kontinuierlichen Verbesserung durch regelmäßiges Planen, Einführen, Überprüfen und Verbessern.

15  Vgl. Torabi, S. et al., 2014, S. 309

16  Vgl. Dey, M., 2011, S. 230

17  Vgl. Torabi, S. et al., 2014, S. 311

18  Vgl. Torabi, S. et al., 2014, S. 309-310

19  Vgl. Johnson, C., 2002, S. 120

<!-- page: 16 -->

## 2.1.2 Historische Entwicklung des BCMS

Erste Anzeichen für eine strukturierte Planung und Umsetzung konkreter Handlungsabfolgen bei Stör- und Notfällen finden sich bereits in frühen Werken der Militärliteratur. 20   Verglichen mit anderen Managementdisziplinen ist das BCMS jedoch vergleichsweise neu. 21

Seit den 1970er Jahren änderte sich der Fokus der Kontinuitätsplanung von gesellschaftlichen und militärischen hin zu betrieblichen Aspekten. Dies ist insbesondere auf die zunehmende Nutzung und steigende Abhängigkeit von IT-Systemen zurückzuführen. Die ersten strukturierten Ansätze für die Kontinuitätsplanung begannen im amerikanischen Finanzsektor: Mit dem Disaster Recovery Management (DRM) wurden Risiken, die sich aus der Nutzung von IT-Systemen ergaben, strukturiert gesteuert. In der Konsequenz hatte das DRM einen starken technischen  Fokus  auf  die  Wiederherstellung  ausgefallener  IT-Systeme  und kann als Vorläufer des BCM betrachtet werden. 22  Im Laufe der Zeit hat sich das BCMS von einer reaktiven und technisch orientierten  Ad-hoc-Lösung zu einer international  standardisierten  Managementdisziplin entwickelt. Herbane (2010) teilt die historische Evolution des BCMS in vier Phasen ein (Abbildung 2). 23

<!-- image -->

Quelle: Eigene Darstellung in Anlehnung an Herbane, 2010

Abbildung 2: Phasen der historischen Entwicklung des BCMS

Die erste Entwicklungsphase des BCMS kennzeichnet sich durch  eine beginnende Gesetzgebung. Insbesondere im Finanz- und Gesundheitssektor werden Institutionen gesetzlich zu spezifischen Vorkehrungen für den Schutz wichtiger Unternehmensunterlagen verpflichtet.  Durch die  zunehmende Verbreitung der IT-Systeme wurden zu Beginn der 1970er Jahre immer mehr Unternehmensdaten elektronisch gespeichert und verarbeitet. Dies erforderte erste Ansätze von Prozessen zur Datensicherung und -wiederherstellung. Zu Beginn der 1980er Jahre wurden erstmalig konkrete Anforderungen gegenüber US-Banken an formale Notfallpläne und Testverfahren gestellt. 24 Die zweite Entwicklungsphase des BCMS charakterisiert Herbane als eine Phase der  zunehmenden  Standardisierung.  Charakteristisch  für  diese  Entwicklungsphase  war  insbesondere  die  Gründung  von  Organisationen  wie  Disaster Recovery Institute (DRI) 25  im Jahr 1988 oder Business Continuity Institute (BCI) im Jahr 1994. 26  Insbesondere durch die Veröffentlichung der ersten BCI Good Practice Guidelines wurden erste Ansätze zur Standardisierung des BCMS erkennbar. Die dritte Entwicklungsphase wurde insbesondere durch die verheerenden Auswirkungen der Terroranschläge vom 11. September 2001 geprägt. Dessen Auswirkungen,  die  über  die  bisher  betrachteten  Schadenszenarien  hinausgingen, veranlassten Organisationen zu einer Neubewertung der Bedrohungslage. Das BCMS wandelte sich somit von einer isoliert betrachteten Insellösung für technische Ausfälle zu einer durch das Top-Management wahrgenommenen Managementkompetenz. Die dritte Phase charakterisierte sich insbesondere durch eine starke Beschleunigung bei der Einführung neuer regulatorischen Vorgaben. Dieser  Trend  führte  international  zu  neuen  regulatorischen  Anforderungen. 27   Die vierte Entwicklungsphase des BCMS ist insbesondere durch eine zunehmende internationale Verbreitung gekennzeichnet. 28  Dies spiegelt sich beispielsweise in der  Harmonisierung  nationaler  Standards  durch  die  Einführung  internationaler Normen wider. Nationaler Vorreiter in der Standardisierung des BCMS war das Vereinigte Königreich mit dem British Standard 25999, der sich größtenteils aus den Inhalten des BCI GPG abgeleitet hat. Die internationale Norm ISO 22301, die im Jahr 2012 wesentlich zur internationalen Verbreitung beigetragen hat, basiert inhaltlich auf dem BS 25999 und löst diesen offiziell ab. 29   Abbildung 3 zeigt den historischen Verlauf der Entwicklung des BCMS anhand eines Zeitstrahls.

20  Beispielhaft zu nennen sind hier die klassischen Werke der Militärliteratur von Sun-Tzu oder Clausewitz.

21  Vgl. Klawitter, J., 2007, S. 4

22  Vgl. Hilles, A. 2010, S. 98

23  Vgl. Herbane, B. 2010, S. 979

<!-- page: 17 -->

24  Beispielhaft zu nennen ist hier das Office of Comptroller of Currency's Banking Circullar BC-

177 sowie der US Expedited Funds Availability Act.

25  Vgl. DRI International, 2021

26  Vgl. Business Continuity Institute, 2021

27  Vgl. Herbane, B. 2010, S. 987

28  Vgl. Herbane, B. 2010, S. 989

29  Vgl. Herbane, B. 2010, S. 990

<!-- page: 18 -->

<!-- image -->

Quelle: Eigene Darstellung in Anlehnung an Herbane, 2010

Abbildung 3: Zeitstrahl zur historischen Entwicklung des BCMS

Zusammenfassend lässt sich  konstatieren, dass das BCMS in den letzten 50 Jahren deutlich an Relevanz und inhaltlicher Reife gewonnen hat. Der zu Beginn starke technische Fokus loser Abläufe zur Datenwiederherstellung hat sich im Laufe der Zeit zu einem eigenständigen Managementsystem entwickelt. Die Relevanz und Aktualität des BCMS zeigt sich insbesondere in der zunehmenden Verbreitung von nationalen und internationalen Standards.

<!-- page: 19 -->

## 2.1.3 BCMS gemäß BSI-Standard 200-4 (CD)

Das BSI hat im Januar 2021 den aktualisierten BSI-Standard 200-4 für das BCM veröffentlicht. Durch die Modernisierung des Standards wird der im Jahr 2008 veröffentlichte BSI-Standard 100-4 abgelöst. Ziel der Modernisierung war es, Anwendern eine praxisnahe Anleitung für den Aufbau und die kontinuierliche Verbesserung eines BCMS zu liefern. 30  Zum gegenwärtigen Zeitpunkt gilt der BSIStandard 200-4 international als aktuellster und detailreichster Standard für das BCMS. 31   Im  folgenden  Abschnitt  wird  der  methodische  Ansatz  des  BSI-Standards 200-4 beschrieben. Dies soll ein Grundverständnis für die Inhalte des Standards und somit für das angestrebte Reifegradmodell geben. Ziel  des  BSI-Standard  200-4  ist  es,  Institutionen  unterschiedlicher  Branchen, Größe und Dimension eine Hilfestellung für den Aufbau und Betrieb eines BCMS zu  bieten.  Adressaten  des  Standards  sind  BCM-Verantwortliche  oder  interessierte Personen, die sich inhaltlich mit der Thematik des BCMS befassen. 32  Die Inhalte sowie die verwendeten Begrifflichkeiten werden durch den Standard nicht dogmatisch vorgegeben, sondern können individuell auf die jeweilige Institution angepasst werden. Neben einer Anleitung zur vollständigen Umsetzung eines BCMS bietet der Standard auch die Möglichkeit, punktuelle Lösungsansätze zu extrahieren. Um die Adressaten schrittweise bei der Einführung eines BCMS zu unterstützen, unterliegt dem BSI-Standard 200-4 ein Phasenmodell, das - konform zur internationalen Norm ISO 22301 - am PDCA-Zyklus angelehnt ist. 33 Der inhaltliche Aufbau des Standards ermöglicht Anwendern einen schrittweisen Aufbau eines BCMS. Ermöglicht wird dies durch die sogenannten Stufenmodelle. Mithilfe der Stufenmodelle Reaktiv-BCMS, Aufbau-BCMS und Standard-BCMS gibt der Standard hilfreiche Zwischenstufen vor, die Anwender beim schrittweisen Aufbau eines Standard-BCMS unterstützen. 34  Die jeweiligen Stufenmodelle unterscheiden sich in der zugrundeliegenden Methodik sowie im Prozessumfang. Sowohl das Reaktiv-BCMS als auch das Aufbau-BCMS sind dabei als vereinfachte Startmodelle für das Standard-BCMS zu verstehen (Abbildung 4).

.

30  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021

31  Vgl. Lehmann, M. &amp; Sowa, J., 2021, S. 30

32  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 6-8

33  Vgl. Lehmann, M. &amp; Sowa, J., 2021, S. 30

34  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 26-28

<!-- page: 20 -->

<!-- image -->

Quelle: BSI-Standard 200-4, 2021

Abbildung 4: BCMS-Stufenmodelle des BSI-Standards 200-4

Die verschiedenen Startmodelle unterscheiden sich neben dem Prozessumfang insbesondere im inhaltlichen Fokus. Beim Reaktiv-BCMS liegt dieser primär auf dem Aufbau notwendiger Reaktionsstrukturen für die Notfallbewältigung. Demnach werden Aspekte wie z.B. der Aufbau einer besonderen Aufbauorganisation (BAO) gegenüber Analyseprozessen wie der BIA oder der BCM-Risikoanalyse priorisiert. 35   Das  Aufbau-BCMS bietet Anwendern eine alternative Vorgehensweise.  Hierbei  werden  keine  inhaltlichen  Aspekte  priorisiert,  sondern  der  Geltungsbereich  von  vornherein  schlanker  gehalten  als  beim  vollständigen  Standard-BCMS. Durch eine sukzessive Erweiterung des Geltungsbereichs können Anwender das Aufbau-BCMS mit Hilfe des kontinuierlichen Verbesserungsprozesses zu einem Standard-BCMS ausbauen. 36

Weiterhin liegt dem BSI-Standard 200-4 ein prozessorientierter Ansatz zugrunde. Dies bedeutet, dass die einzelnen Abschnitte des Standards in die Phasen plan, do, check, act untergliedert sind. Diese Struktur ermöglicht es, die jeweiligen Teilaspekte  den  unterschiedlichen  Phasen  des  Managementsystem  zuzuordnen, und sind kompatibel zur ISO 22301. 37  Abbildung 5 zeigt den inhaltlichen Aufbau und die Zusammensetzung des BSI-Standard 200-4 am Beispiel des StandardBCMS. Die einzelnen Phasen des BSI-Standards 200-4 werden nachfolgend exponiert.

35  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 46

36  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 142

37  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 145

<!-- page: 21 -->

Quelle: BSI-Standard 200-4, 2021

<!-- image -->

Abbildung 5: Inhaltlicher Aufbau des Standard-BCMS

Plan-Phase: In dieser Phase werden die Rahmenbedingungen für das BCMS definiert. Dazu werden zunächst die relevanten Anforderungen der Organisation im Hinblick auf das BCMS analysiert. Dies ermöglicht es, einen Überblick über die relevanten Interessensgruppen sowie die benötigten Ressourcen für den Aufbau des BCMS zu erhalten. Zusätzlich werden die geltenden Bestimmungen der Dokumentenlenkung festgelegt sowie die Ziele und strategische Ausrichtung des BCMS in der BCM-Leitlinie dokumentiert. 38

Do-Phase: Die Do-Phase teilt sich inhaltlich in zwei Kernbestandteile auf:

- Aufbau und Befähigung der BAO sowie
- angemessene Absicherung der Geschäftsprozesse.

38  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 145

<!-- page: 22 -->

Zweck der BAO ist es, gesonderte Verantwortlichkeiten für eine  zielgerichtete und rasche Bewältigung von Notfällen festzulegen. Hierzu werden Stabsstrukturen zur Lenkung und Koordination der Notfallbewältigung aufgebaut. Diese ermöglichen eine zentrale und koordinierte Führung der Notfallbewältigung. 39  Um die Arbeitsfähigkeit des Notfallstabs zu gewährleisten, werden zudem organisatorische Voraussetzungen getroffen. Hierzu zählen die Ausstattung des Stabsraums, die Schulung und Befähigung der einzelnen Stabsmitglieder sowie die Definition von geeigneten Vorgaben für die Stabsarbeit. Um die BAO für eine angemessene Reaktion auf Notfälle zu befähigen, werden Prozesse zur Detektion, Alarmierung und Eskalation von Schadensereignissen benötigt. 40  Dies beinhaltet  die  Definition  von  Sofortmaßnahmen  zur unverzüglichen Reaktion auf Schadensfälle. Weiterhin werden allgemeine Handlungsanweisungen zur internen und externen Notfallkommunikation definiert. Durchdachte Kommunikationskanäle können im Notfall einen positiven Einfluss auf die Reaktionszeit haben und gelten somit als wesentlicher Erfolgsfaktor für die Notfallbewältigung. 41 Der zweite Kernbestandteil der Do-Phase ist die angemessene Absicherung der Geschäftsprozesse. Zur Identifikation der zeitkritischen Geschäftsprozesse werden hierzu BIA durchgeführt. 42  Aufbauend auf diesen Erkenntnissen wird ein Soll-Ist-Vergleich durchgeführt. Dessen Ziel ist es, die identifizierten Verfügbarkeitsanforderungen  mit  den  tatsächlich  erreichbaren  Wiederanlaufzeiten  einzelner Ressourcen abzugleichen.  Durch die darauffolgende BCM-Risikoanalyse  werden mögliche Ursachen für den Ausfall des Geschäftsbetriebs analysiert und bewertet.  Die  Erkenntnisse  dieser  Analysen  ermöglichen  es,  die  übergreifenden BC-Strategien an die Bedürfnisse der Organisation auszurichten sowie die notwendigen Pläne und Konzepte 43  für das BCMS zu erstellen. Check-Phase: Ziel  der  Check-Phase ist  es, den erreichten Umsetzungsstand des BCMS zu steuern und zu überwachen. Die Überprüfung der Leistungsfähigkeit des BCMS stellt einen wesentlichen Bestandteil des BCMS dar. Durch regelmäßiges Üben und Testen der aufgebauten Strukturen des BCMS wird sichergestellt, dass die entwickelten Pläne und Maßnahmen angemessen und wirksam

39  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 160-162

40  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 167

41  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 17

42  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 193

43  Insbesondere: Geschäftsfortführungsplanung, Notfallmaßnahmen, Notfallvorsorgekonzept und Notfallhandbuch.

<!-- page: 23 -->

sind. 44  Neben der Durchführung von Übungen und Tests ist die Leistungsüberprüfung  durch  geeignete  Kennzahlen  ebenfalls  ein  wesentliches  Element  zur Überwachung des Umsetzungsstands des BCMS. 45

Act-Phase: Die Act-Phase dient der kontinuierlichen Verbesserung des BCMS. Ziel  dieser  Phase  ist  die  Identifizierung  von  Korrekturbedarfen  und  Verbesserungsmöglichkeiten. Korrekturbedarfe können beispielsweise durch Abweichungen aus Audits, Tests und Übungen erhoben werden. Auf dieser Basis werden Verbesserungsmaßnahmen  definiert  sowie  deren  Umsetzung  überwacht  und nachgehalten. 46

44  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 252

45  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 278

46  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 286

<!-- page: 24 -->

## 2.2  Reifegradmodelle

Dieser Abschnitt schafft ein Verständnis der notwendigen Begrifflichkeiten von Reifegradmodellen. Nach einer kurzen Beschreibung des Anwendungszwecks werden der strukturelle Aufbau sowie die unterschiedlichen Ausprägungen von Reifegradmodellen  illustriert.  Weiterhin  werden  exemplarische  Vorgehensmodelle für die Entwicklung von Reifegradmodellen erläutert.

## 2.2.1 Anwendungszweck

Prozessoptimierung gilt als zentraler Bestandteil der Organisationsentwicklung. Die kontinuierliche Verbesserung von Geschäftsprozessen hat demzufolge einen hohen Stellenwert bei verantwortlichen Managern. 47  Um Geschäftsprozesse zielgerichtet zu optimieren, sind objektive Beurteilungen zu Beginn des Vorhabens eine bewährte Praxis. 48  Ziel einer solchen objektiven Beurteilung ist es, den derzeitigen Leistungsstand von Geschäftsprozessen zu analysieren. Ein Werkzeug für die Durchführung von objektiven Beurteilungen sind Reifegradmodelle. Diese ermöglichen es, mithilfe einer zugrundeliegenden Methodik systematische Entwicklungspfade zur Leistungssteigerung zu identifizieren. 49 Reifegradmodelle gibt es in unterschiedlichen Formen und Ausprägungen. Aufgrund der Vielzahl an Reifegradmodellen gibt es in der Literatur keine formelle Begriffsdefinition des Reifegradmodells. Grund dafür sind vor allem deren unterschiedlichen Untersuchungsbereiche. Beispielsweise gibt es Reifegradmodelle für Prozesse des IT-Managements, für die Softwareentwicklung oder für Produktentwicklungsprozesse. Trotz der unterschiedlichen Themenschwerpunkte gibt es insbesondere  im  Anwendungszweck  einige  Gemeinsamkeiten  zwischen  den existierenden Reifegradmodellen. Aus der Literatur lassen sich folgende Variationen des Anwendungszecks ableiten: 50

## Leistungsbewertung:

Reifegradmodelle zur Leistungsbewertung dienen der Analyse der derzeitigen Fähigkeiten  (Ist-Stand).  Unter  der  Berücksichtigung  spezifischer  Kriterien  wird der Status quo eines ausgewählten Themengebiets bewertet. Die Leistungsbewertung erfolgt weiterstgehend objektiv. Die Ergebnisse der Leistungsbewertung werden in der Regel an interne oder externe Stakeholder berichtet. Modelle, die ausschließlich zur Leistungsbewertung dienen, werden oftmals punktuell eingesetzt. 51, 52

47  Vgl. Poeppelbuss, J. &amp; Roeglinger, M., 2011, S. 1

48  Vgl. Bensiek, T., 2013, S. 20-21

49  Vgl. de Bruin, T. &amp; Freeze, R., 2005, S. 5-6

50  Vgl. Bensiek, T., 2013, S. 19

<!-- page: 25 -->

## Leistungssteigerung:

Reifegradmodelle zur Leistungssteigerung ermöglichen es, Entwicklungspotentiale zu erkennen und zu adressieren. Empfohlene Zielwerte ermöglichen es Anwendern - ausgehend vom Status quo -, den gewünschten Zielreifegrad zu erreichen. Hierzu werden Handlungsmaßnahmen abgeleitet, die eine strukturierte Leistungssteigerung ermöglichen. 53

## Leistungsvergleich:

Reifegradmodelle zum Leistungsvergleich ermöglichen einen Vergleich des Umsetzungsstands über die Grenzen der Organisation hinweg. Damit solch ein Vergleich aussagekräftig ist, benötigt diese Art von Reifegradmodell einen hohen Standardisierungsgrad.  Der  Vergleich  von  ähnlichen  Themenfeldern  unterschiedlicher Industrien oder Organisationen ermöglicht die Erstellung von internen oder externen Benchmarks. Der Untersuchungsbereich kann je nach Reifegradmodell variieren. So existieren Reifegradmodelle für die Untersuchung sowohl von Produkten als auch von Prozessen. 54   Ziel  des  Produktreifegradmanagements  ist  es,  den  Fortschritt  einer Produktentwicklung zu überwachen und zu kontrollieren. Das Produktreifegradmanagement ist Bestandteil des Projektmanagements und ermöglicht die Abnahme von vordefinierten Qualitätskriterien (Quality Gates) im Entwicklungsprozess. 55  Das Prozessreifegradmanagement fokussiert sich auf die Abläufe außerhalb  des  Produktlebenszyklus:  die  effektivere  Gestaltung  der  relevanten  Prozesse der Institution. 56  Der Fokus dieser Arbeit liegt auf dem Prozessreifegradmanagement. Das Produktreifegradmanagement wird demnach nicht weiter betrachtet.

## 2.2.2 Struktureller Aufbau

Reifegradmodelle gelten als eine spezielle Ausprägung von Referenzmodellen, die sich ausschließlich auf die systematische Verbesserung eines Betrachtungsbereichs fokussieren. Sie ermöglichen eine zielgerichtete Gestaltung von Orga-

51  Vgl. Poeppelbuss, J. &amp; Roeglinger, M., 2011, S. 5-6

52  Vgl. de Bruin, T. &amp; Freeze, R., 2005, S. 2-3

53  Vgl. Bensiek, T., 2013, S. 19

54  Vgl. Christiansen, S. &amp; Gausemeier, J., 2010, S. 347-348

55  Vgl. Angermeier, G., 2004

56  Vgl. Bensiek, T., 2013, S. 21

<!-- page: 26 -->

nisationen und besitzen in der Regel einen allgemeingültigen Empfehlungscharakter. 57   Reifegradmodelle  sind  folgerichtig  Referenzmodelle,  die  sich  ausschließlich  auf  die  systematische  Verbesserung  eines  Untersuchungsbereichs konzentrieren. 58  Obwohl im Laufe der Zeit verschiedene Reifegradmodelle - teilweise unterschiedlicher Qualität - entstanden sind, ist der charakteristische Aufbau der Modelle ähnlich. Im folgenden Abschnitt wird der strukturelle Aufbau von Reifegradmodellen beschreiben. Typischerweise sind Reifegradmodelle stufenförmig aufgebaut. Je Reifegradstufe, werden spezifische Anforderungen an die Erfüllung des jeweiligen Reifegrads gestellt. Ein Reifegrad wird erreicht, wenn zuvor festgelegte Kriterien für die Erreichung des Reifegrads nachweislich umgesetzt werden. Ein nächsthöherer Reifegrad kann demnach nur erreicht werden, wenn die vorherigen Stufen ebenfalls erfüllt worden sind. Ein Überspringen eines  Reifegrads  ist  normalerweise  nicht  möglich. 59   Standardmäßig  bestehen Reifegradmodelle aus den folgenden Bestandteilen: 60

|   # | Bestandteil                                | Beschreibung                                                                       |
|-----|--------------------------------------------|------------------------------------------------------------------------------------|
|     | Anzahl von Reifegradstufen (typischerweise | 1 Reifegradstufe • Definierte 3 bis 6 Stufen)                                      |
|   2 | Bezeichnung                                | • Bezeichnung je Reifegradstufe (z.B. 'initial', 'wiederholbar', 'definiert' etc.) |
|   3 | Beschreibung                               | • Generische Beschreibung der Eigenschaften des jeweiligen Reifegrads              |
|   4 | Prozessbereiche •                          | Anzahl an betrachteten Prozessbereichen (auch Dimensionen genannt)                 |
|   5 | Aktivitäten                                | • Aktivitäten, die den jeweiligen Prozessbereich charakterisieren                  |
|   6 | Aktivitäten je Rei- fegrad                 | • Beschreibung der Aktivitäten je Reifegrad                                        |

Quelle: Fraser et al., 2002

Tabelle 1: Typische Bestandteile eines Reifegradmodells

Um Reifegrade für einen Untersuchungsbereich erheben zu können, erfolgt die Betrachtung anhand von objektiven Kriterien. Zusätzlich ermöglicht die Analyse mehrerer Prozessbereiche einen umfassenden Blick auf den Betrachtungsbereich und beugt somit einer einseitigen Bewertung vor. 61

Zur Beschreibung des betrachteten Untersuchungsbereichs arbeiten Reifegradmodelle mit Handlungsfeldern. Diese kategorisieren den Untersuchungsbereich in übergeordnete Bereiche. Das Reifegradmodell Capability Maturity Model Integration (CMMI) kategorisiert den Untersuchungsbereich beispielsweise in Prozessbereiche,  wie  dem  Configuration  Management  oder  dem  Risikomanagement. Die Leistungsfähigkeit jedes Handlungsfelds wird mit Hilfe von Handlungselementen ermittelt. Diese sind Kriterien bzw. Attribute, die einen hohen Einfluss auf den Untersuchungsbereich haben. Die Handlungselemente werden bei der Erhebung  von  Reifegraden  mithilfe  von  spezifischen  Fragestellungen  abgefragt. 62

57  Vgl. Mettler, T., 2010, S. 33

58  Vgl. Mettler, T., 2010, S. 40

59  Vgl. Bensiek, T., 2013, S. 23

60  Vgl. Fraser, P. et al, 2002, S. 3

61  Vgl. Becker, J. et al., 2009, S. 5

<!-- page: 27 -->

## 2.2.3 Ausprägungen von Reifegradmodellen

Die  meisten  Reifegradmodelle  sind Standardwerke und somit gekennzeichnet durch allgemeingültige Empfehlungen. 63  Institutionen stehen daher vor der Herausforderung, ein geeignetes Reifegradmodell für den jeweiligen Anwendungszweck zu identifizieren. Ein Verständnis für den Anwendungszweck und die Bedürfnisse der Organisation sind bei der Auswahl und Anwendung von Reifegradmodellen infolgedessen unverzichtbar. Im Laufe der Zeit haben sich unterschiedliche Ausprägungen von Reifegradmodellen entwickelt. Übergreifend lässt sich die Struktur dieser Ausprägungen in folgende Modellarten kategorisieren: 64

- Rasterbasierte  Modelle (maturity  grids): Rasterbasierte  Reifegradmodelle sind die simpelste Form von Reifegradmodellen. Einfache textuelle Beschreibungen der Reifegradstufen zeigen den Fortschritt in einem Prozessbereich. Das Reifegradmodell unterliegt hierbei einem vorgegebenen Raster, bei dem die Aktivitäten je Reifegradstufe vordefiniert sind.
- Formal-strukturierte Modelle (CMM-like models): Bei dieser Kategorie von Reifegradmodellen erfolgt die Bewertung der Reifegrade mithilfe einer vorgegebenen formalisierten Struktur (Metamodell). Im Vergleich zum rasterbasierten Modell haben formal-strukturierte Modelle eine erhöhte Komplexität. Die Reifegrade sind durch Merkmale charakterisiert, die mithilfe von spezifischen Fragestellungen  erhoben  werden.  Zusätzlich  werden  unterschiedliche  Prozessbereiche (Dimensionen) betrachtet, was zu einer erhöhten Komplexität führt. Aufgrund dessen werden die Daten meist toolgestützt erhoben. 65
- Hybride Reifegradmodelle (hybrids ): Hybride Modelle sind eine Kombination der vorherigen Modellarten. Mithilfe von einfachen Fragestellungen wird die Erreichung von Zielen einer jeweiligen Reifegradstufe abgefragt. Hybride

62  Vgl. Christiansen &amp; Gausemeier, 2010, S. 344

63  Vgl. Becker, J. et al., 2009, S. 6

64  Vgl. Mettler, T., 2010, S. 44-45

65  Vgl. Fraser, P. et al., 2002, S. 4

<!-- page: 28 -->

Reifegradmodelle gehen somit über eine einfache textuelle Beschreibung der Reifegradstufen hinaus, unterliegen jedoch keiner formalisierten Struktur. 66

Die  unterschiedlichen  Ausprägungen  der  Reifegradmodelle  führen  zu  der  Erkenntnis, dass kein allgemeingültiges Reifegradmodell (one fits all) für alle Bedürfnisse unterschiedlicher Organisationen existiert. Anwender von Reifegradmodellen müssen sich demnach im Vorfeld über ihre Bedürfnisse und das angestrebte Ziel bewusst sein. Dies gilt insbesondere für das gewünschte Maß an Komplexität des Reifegradmodells. Ein Reifegradmodell, das die komplexe Realität  zu stark vereinfacht, liefert nicht genügend aussagekräftige Informationen, wohingegen ein zu komplexes Modell Anwender überfordern könnte. 67

66  Vgl. Kulkarni, U. &amp; St. Louis, R., 2003, S. 2544-2545

67  Vgl. de Bruin, T. &amp; Freeze, R., 2005, S. 4

<!-- page: 29 -->

Um Anwender bei der Auswahl eines geeigneten Reifegradmodells zu unterstützen, haben Christiansen und Gausemeier (2010) eine Konsistenzanalyse bestehender  Reifegradmodelle  durchgeführt. 68   Im  Ergebnis  dieser  Analyse  ist  ein Schema zur Kategorisierung von Reifegradmodellen entstanden. Folglich lassen sich Reifegradmodelle in fünf Klassen unterteilen, wobei jede Klasse spezifische Charakteristiken aufweist.

<!-- image -->

Quelle: Christiansen und Gausemeier, 2010

Abbildung 6: Visualisierung der Klassen von Reifegradmodellen mit eingetragenen Hauptunterscheidungsmerkmalen

Abbildung 6 visualisiert die definierten Klassen von Reifegradmodellen sowie die wesentlichen Hauptunterscheidungsmerkmale. Die grau hinterlegten Flächen in der Grafik symbolisieren die jeweilige Klasse eines Reifegradmodells. Jede dargestellte Kugel steht stellvertretend für ein Ausprägungsbündel, sprich eine Kombination  von  Merkmalsausprägungen. 69   Die  Hauptunterscheidungsmerkmale (Balken) verdeutlichen die grundlegenden Unterschiede zwischen den jeweiligen Klassen. So unterscheiden sich beispielsweise die Klasse 2 und die Klasse 4 im benötigten Schulungsaufwand für die Anwendung der Reifegradmodelle. Klasse 1 und Klasse 2 sind beispielsweise durch vorgegebene Maßnahmen innerhalb der jeweiligen Reifegradmodelle gekennzeichnet, während bei Reifegradmodellen der Klasse 4 und Klasse 5 die Handlungsmaßnahmen individuell gestaltet werden können. 70  Nachfolgend werden die fünf unterschiedlichen Klassen von Reifegradmodellen gemäß Christiansen und Gausemeier charakterisiert: 71

68  Vgl. Christiansen, S. &amp; Gausemeier, J., 2010, S. 346-348

69  Vgl. Christiansen, S. &amp; Gausemeier, J., 2010, S. 346

<!-- page: 30 -->

- Klasse 1 - Flexible Regelwerke: Regelwerke der Klasse 1 kennzeichnen sich dadurch, dass sie an die spezifischen Besonderheiten einer Organisation angepasst werden können. Sie eignen sich insbesondere für Organisationen, die ein Reifegradmodell einsetzen wollen, das an die Besonderheiten der Organisation angepasst werden kann. Die Einführung eines solchen Reifegradmodells ist mit hohem Aufwand (ca. 6-12 Monate) verbunden.
- Klasse 2 - Starre Regelwerke: Reifegradmodelle der Klasse 2 charakterisieren sich durch ein fest definiertes Regelwerk. Die Handlungsempfehlungen und Verbesserungsmaßnahmen des Modells orientieren sich meist an Best Practices und Industriestandards, eine Anpassung an organisatorische Begebenheiten ist daher nicht möglich. Reifegradmodelle der Klasse 2 eignen sich insbesondere  für  Organisationen,  die  einen  hohen  Standardisierungsgrad und/oder eine  Vergleichbarkeit  zu  anderen  Organisationen  anstreben.  Der hohe Standardisierungsgrad führt zu aufwändigen Auditierungen durch unabhängige Institutionen.
- Klasse  3  -  Methodische  Instrumentarien: Bei Reifegradmodellen  der Klasse 3 wird lediglich der methodische Rahmen vorgegeben. Inhaltlich können die Reifegradmodelle an die Besonderheiten der jeweiligen Organisation angepasst werden. Aufgrund des individuellen Charakters dieser Reifegradmodelle sind organisationsübergreifende Vergleiche in der Regel nicht möglich. Der Implementierungsaufwand dieser Art von Reifegradmodellen ist gering.
- Klasse 4 - Plakative Zustandsbewertung: Reifegradmodelle dieser Kategorie legen einen starken Fokus auf die Leistungsbewertung. Diese Reifegradmodelle wurden spezifisch konzipiert, was eine Anpassung an die organisatorischen Begebenheiten obsolet macht. Der Aufwand zur Durchführung bzw. Implementierung eines solchen Reifegradmodells ist gering. Da durch diese Art von Reifegradmodellen lediglich der derzeitige Ist-Zustand abgebildet  wird,  sind  in  der  Regel  keine  Maßnahmen  zur  Leistungssteigerung  in ihnen enthalten.
- Klasse 5 - Pragmatische Wirkkettenanalyse: Bei Reifegradmodellen der Klasse 5 werden primär Kennzahlen als Indikatoren verwendet. Da diese Art

70  Vgl. Christiansen, S. &amp; Gausemeier, J., 2010, S. 347

71  Vgl. Christiansen, S. &amp; Gausemeier, J., 2010, S. 347-348

<!-- page: 31 -->

von Reifegradmodellen auf Kennzahlensystemen aufbaut, wird in der Regel ein etabliertes Prozessmanagement vorausgesetzt. Grundsätzlich sind in diesen Reifegradmodellen keine Maßnahmen zur Leistungssteigerung enthalten. Ebenfalls sind diese nicht für unternehmensübergreifende Vergleiche geeignet.

Als wesentliche Erkenntnis kann an dieser Stelle festgehalten werden, dass eine Vielzahl an unterschiedlichen Ausprägungen von Reifegradmodellen existiert. Je nach  Anwendungszweck  und  Zielsetzung  eignen  sich  unterschiedliche  Reifegradmodelle. Die Vielzahl an möglichen Reifegradmodellen kann Anwender jedoch vor eine Herausforderung stellen. Ein klares Verständnis der Anforderungen und Begebenheiten der Institution ist demnach eine Grundvoraussetzung, um ein geeignetes Reifegradmodell auswählen zu können. Trotz der Vielzahl an Reifegradmodellen besteht die Möglichkeit, dass keines der Reifegradmodelle für den Einsatz geeignet ist. Neben einer Vielzahl von bereits bestehenden Reifegradmodellen finden sich in der Literatur ebenfalls verschiedene Ansätze zur strukturierten Entwicklung von neuen Reifegradmodellen. 72

## 2.2.4 Vorgehensmodelle zur Entwicklung von Reifegradmodellen

Vorgehensmodelle ermöglichen eine theoretisch fundierte Entwicklung von Reifegradmodellen. Eine transparente und nachvollziehbare Beschreibung der Vorgehensweise der Entwicklung eines Reifegradmodells hat einen positiven Einfluss auf die Zuverlässigkeit und Validität des Modells. 73  Für die Entwicklung von Reifegradmodellen existieren verschiedene Ansätze mit unterschiedlichen Herangehensweisen. 74  Gemeinsam haben diese Ansätze, dass sie eine Anzahl von Phasen und Aktivitäten aufweisen, die für die Entwicklung des Modells durchgeführt werden müssen. Zwei Vorgehensmodelle werden in der Literatur besonders häufig referenziert. 75  Da eine detaillierte Beschreibung der unterschiedlichen Ansätze den Umfang dieser Arbeit überschreiten würde, werden nachfolgend die Vorgehensmodelle von de Bruin et al. (2005) und Becker et al. (2009) kurz erläutert. Ausgewählt wurden diese beiden Vorgehensmodelle aufgrund ihrer weiten Verbreitung 76  und ihrer adaptierbaren bzw. unspezifischen Ausrichtung. 77

72  Vgl. Bas, M., 2021, S. 29-30

73  Vgl. Becker, J. et al., 2009, S. 249

74  Vgl. Hecht, S., 2013, S. 125

75  Vgl. Becker, J. et al., 2009, de Bruin, T. &amp; Freeze, R. 2005

76  U.a. in vergleichbaren Arbeiten von Bas, M., 2021; Bensiek, T., 2013; Mettler, T., 2010; Hecht, S., 2013.

77  Vgl. Hecht, S., 2013, S. 125-126

<!-- page: 32 -->

## Vorgehensmodell von de Bruin et al.:

Das von de Bruin et al. entwickelte Framework teilt die Entwicklung von Reifegradmodellen in sechs generische, aufeinander aufbauende Phasen ein (Abbildung 7). 78

Quelle: de Bruin et al., 2005

<!-- image -->

Abbildung 7: Vorgehensmodell zur Erstellung von Reifegradmodellen nach de Bruin et al.

Das Vorgehensmodell startet mit der Phase Scope, in der zunächst der inhaltliche Fokus des Reifegradmodells festgelegt wird. Hierzu werden der Umfang des Reifegradmodells definiert sowie die äußeren Grenzen des Modells abgesteckt. Neben dem inhaltlichen Fokus werden zusätzlich die Stakeholder des Reifegradmodells bestimmt. In der Design-Phase wird die Architektur des Reifegradmodells  bestimmt. 79   Neben  den  Adressaten  des  Reifegradmodells  wird  in  dieser Phase die Erhebungsmethode festgelegt. Diese kann je nach Anwendungsfall variieren und entweder eigenständig (Self-Assessment) oder durch externe Akteure (Third-Party-Assessment) durchgeführt werden. Der Fokus dieser Phase liegt insbesondere auf den Interessen der Stakeholder und wie diese sinnvoll berücksichtigt  werden  können. 80   Zusätzlich  werden  in  dieser  Phase  die  Art  und Weise der Berichterstattung  (Reporting)  zum  Zielpublikum  sowie  die  Betrachtungstiefe  des  Reifegradmodells  festgelegt.  Darauf  folgt  die  Phase  Populate. Diese beinhaltet die inhaltliche Erhebung und Befüllung des Reifegradmodells. Hierzu werden zunächst dessen Betrachtungsdomänen identifiziert. Diese können aus bekannten kritischen Erfolgsfaktoren des Untersuchungsbereichs abgeleitet werden. 81  Darüber hinaus wird in Phase 3 ein geeignetes Instrument zur Durchführung der Reifegradmessung erstellt. Eine toolgestützte Erhebung soll eine einheitliche statistische Erhebung ermöglichen und kann nach de Bruine et al.  die Vergleichbarkeit der Ergebnisse verbessern. 82  Die Erstellung des Erhebungstools sollte mithilfe von geeigneten Fragestellungen erfolgen. In Phase 4 erfolgt die Erprobung des Modells. Hierdurch wird sichergestellt, dass die theoretische Basis des Modells solide ist. Ziel ist es, das erstellte Reifegradmodell hinsichtlich der Relevanz und inhaltlichen Korrektheit zu überprüfen. Erprobungen können mithilfe von Fallstudien in Form von Pilotversuchen an ausgewählten Institutionen durchgeführt werden. 83  In Phase 5 wird das erstellte Reifegradmodell anderen Anwendern zur Verfügung gestellt. Dies dient der Verbesserung der Akzeptanz sowie der Standardisierung des Reifegradmodells. 84  Ziel ist es, eine Allgemeingültigkeit  des  Reifegradmodells  herzustellen.  Die  Bereitstellung  des Reifegradmodells an ein breites Publikum ermöglicht es weiteren Organisationen, das Reifegradmodell anzuwenden und kann maßgeblich zur Standardisierung und der allgemeinen Akzeptanz des Modells beitragen. 85  In Phase 6 erfolgt die kontinuierliche Anpassung des Reifegradmodells an aktuelle Entwicklungen und  sich  ändernde  Rahmenbedingungen. 86   Insbesondere  wenn  Reifegradmodelle  Handlungsempfehlungen  für  die  Erreichung  eines  nächsthöheren  Reifegrads ausgeben, müssen diese regelmäßig aktualisiert werden und dem Stand der Technik entsprechen. 87  Eine regelmäßige Aktualisierung sichert demnach die Relevanz des Reifegradmodells.

78  Vgl. de Bruin, T. et al., 2005, S. 2

79  Vgl. Bas, M., 2021, S. 33

80  Vgl. de Bruin, T. et al., 2005, S. 4

81  Vgl. de Bruin, T. et al., 2005, S. 5-6

82  Vgl. de Bruin, T. et al., 2005, S. 7

<!-- page: 33 -->

## Vorgehensmodell nach Becker et al.:

Das Vorgehensmodell von Becker et al. orientiert sich an den Gestaltungsprinzipien der Design Science Research Guidelines 88  und teilt die Entwicklung von Reifegradmodellen in acht aufeinander aufbauende Phasen ein. Das Vorgehensmodell startet mit der Problemdefinition. Hier werden der Bedarf und der angestrebte Nutzen des Reifegradmodells identifiziert. 89  Darauffolgend wird ein Vergleich mit existierenden Reifegradmodellen durchgeführt. Dieser soll die Notwendigkeit für das Reifegradmodell begründen und bildet die Grundlage für die Festlegung  einer  Entwicklungsstrategie.  Entwicklungsstrategien  können  beispielsweise die vollständige Neuentwicklung oder die Weiterentwicklung bestehender Reifegradmodelle sein. 90  Die iterative Reifegradmodellentwicklung gilt als zentrale Phase des Vorgehensmodells. In ihr erfolgt die inhaltliche Entwicklung des Reifegradmodells  in  mehreren  Iterationsstufen.  In  der  darauffolgenden  Phase Konzeption  von  Transfer  und  Evaluation werden wesentliche Entscheidungen über  die  adressatengerechte  Kommunikation  getroffen.  Die  darauffolgende Phase Implementierung der Transfermittel dient dazu, das Reifegradmodell auf der zuvor festgelegten Art und Weise bereitzustellen. 91  In der Phase der Durchführung der Evaluation wird analysiert, inwiefern das Reifegradmodell dem ursprünglich angestrebten Nutzen gerecht wird. Die letzte Phase ist abhängig von

83  Vgl. de Bruin, T. et al., 2005, S. 8-9

84  Vgl. Bas, M., 2021, S. 33

85  Vgl. de Bruin, T. et al., 2005, S. 8-9

86  Vgl. Bas, M., 2021, S. 33

87  Vgl. de Bruin, T. et al., 2005, S. 9

88  Vgl. Hevner, A., 2004, S. 83

89  Vgl. Becker, J. et al., 2009, S. 252

90  Vgl. Becker, J. et al., 2009, S. 255

91  Vgl. Becker, J. et al., 2009, S. 255

<!-- page: 34 -->

den Ergebnissen der Evaluation und kann entweder zu einer erneuten Modellversion, einer erneuten Evaluation (positiver Ausgang) oder zum Verwerfen des Reifegradmodells (negativer Ausgang) führen. 92

Im direkten Vergleich der beiden Vorgehensmodelle ist erkennbar, dass das Vorgehensmodell nach Becker et al. deutlich umfangreicher gestaltet ist als das Vorgehensmodell von de Bruin et al. Jedoch sind die jeweiligen Phasen des Vorgehensmodell nach Becker et al. nicht sehr spezifisch und wenig detailliert. Dies führt dazu, dass wenig konkrete Anhaltspunkte für die Konstruktion des Reifegradmodells abgeleitet werden können. 93  Das Vorgehensmodell von de Bruin et al. hingegen ist im direkten Vergleich eher generisch ausgelegt und zielt auf eine Veröffentlichung und langfristige Standardisierung des Reifegradmodells ab (insbesondere erkennbar durch die Phasen Deploy und Maintain). Jedoch können insbesondere für die Festlegung der Zielsetzung und des Adressatenbereichs hilfreiche Erkenntnisse aus dem Modell von de Bruine et al. entnommen werden. Die beschriebenen Vorgehensmodelle zur Entwicklung von Reifegradmodellen schlagen einen iterativen Entwicklungsprozess vor. 94  Zusätzlich zu den bestehenden Vorgehensmodellen zur Neuentwicklung von Reifegradmodellen existieren weitere Ansätze für die Erstellung von Reifegradmodellen. Diese beinhalten neben der Neuentwicklung weitere Strategien für die Entwicklung eines Reifegradmodells. Grundsätzlich wird hierbei in die folgenden Strategien unterschieden: 95, 96

- Weiterentwicklung bestehender Modelle,
- Kombination bestehender Modelle oder
- Übertragung von Inhalten bestehender Reifegradmodelle auf einen neuen Anwendungsbereich.

Nach Lahrmann/Marx (2010) gilt hierbei die Anpassung eines bestehenden Modells als eine gangbare Entwicklungsstrategie. 97  Auch aufgrund der Vielzahl an existierenden Reifegradmodellen gewinnt diese Strategie zunehmend an Relevanz. 98  Jedoch fehlt es bisher an methodisch fundierten Herangehensweisen zur Anpassung bestehender Reifegradmodelle. 99

92  Vgl. Becker, J. et al., 2009, S. 256

93  Vgl. Mettler, T. 2010, S. 134

94  Vgl. Lahrmann, G. &amp; Marx, F., 2010, S. 524

95  Vgl. Bas, M., 2021, S. 54

96  Vgl. Ahlemann, F. et al., 2005

97  Vgl. Lahrmann, G. &amp; Marx, F., 2010, S. 525

98  Vgl. Hecht, S., 2013, S. 139

99  Vgl. Hauck, J. et al., 2011, S. 44

<!-- page: 35 -->

## 3  Reifegradmodell für den BSI-Standard 200-4

## 3.1  Methodische Vorgehensweise

Die Konzeption des Reifegradmodells für den BSI-Standard 200-4 erfolgt in Anfang der Arbeit gerecht zu werden, wird das Vorgehensmodell leicht modifiziert. Implemenwerden in Anlehnung

lehnung an das Vorgehensmodell nach Becker et al. 100  Um dem geplanten UmDie ursprünglichen Phasen Konzeption von Transfer und Evaluation , tierung der Transfermittel und Durchführung der Evaluation an Hecht (2013) zu der übergreifenden Phase Evaluation konsolidiert. 101 Die erste Phase beinhaltet die Problemdefinition. Hierin werden der Bedarf für das Reifegradmodell für den BSI-Standard 200-4 analysiert sowie die Relevanz für  das  Modell identifiziert.  Weiterhin  werden  die  Ziele und  Zielgruppe für das Reifegradmodell festgelegt (Abschnitt 3.1.1). Im nächsten Abschnitt erfolgt die Anforderungserhebung (Abschnitt 3.1.2). Die identifizierten Anforderungen legen die Grundlage für die spätere Modellentwicklung, die Auswahl des zugrundeliegenden Basismodells sowie die Evaluation des Modells. Im darauffolgenden Abschnitt erfolgt ein Vergleich bestehender Modelle (Abschnitt 0) . In diesem Abschnitt  werden  bereits  bestehende  BCM-Reifegradmodelle  hinsichtlich  einer möglichen Anwendung für den BSI-Standard 200-4 analysiert. Dieser Schritt ist notwendig, um die Festlegung der Entwicklungsstrategie (Abschnitt  3.1.4)  sinnvoll  entscheiden  zu  können. 102   Zusätzlich  zur  ausgewählten Entwicklungsstrategie wird auf Basis der definierten Anforderungen ein geeignetes Basismodell diskutiert und ausgewählt (Abschnitt 3.1.5). Dieses dient als methodische Grundlage für die inhaltliche Erstellung des Reifegradmodells. In der Phase der inhaltlichen Modellentwicklung (Abschnitt 3.2) erfolgen die Erstellung des Prozessreferenzmodells (PRM) für den BSI-Standard 200-4 sowie die Erstellung des darauf aufbauenden Prozess-Assessmentmodells. Weiterhin erfolgt in der Phase der inhaltlichen Modellentwicklung die Erstellung eines excel-basierten Erhebungstools. In der Phase Evaluation (Abschnitt 4) werden die Inhalte des Reifegradmodells sowie das Erhebungstool gemeinsam mit Fachexperten und Anwendern des BSI-Standards 200-4 diskutiert. Auf Basis der definierten Anforderungen wird die praktische Eignung des Reifegradmodells bewertet. Abbildung 8 stellt die methodische Vorgehensweise zur Entwicklung des Reifegradmodells grafisch dar.

100  Vgl. Becker, J. et al., 2009, S. 254

101  Vgl. Hecht, S., 2013, S. 127-128

102  Vgl. Becker, J. et al., 2009, S. 256

<!-- page: 36 -->

Quelle: Eigene Darstellung, entwickelt in Anlehnung an Becker, J. et al., 2009 und Hecht, S., 2013

Abbildung 8: Methodische Vorgehensweise zur Entwicklung des Reifegradmodells für den BSIStandard 200-4

## 3.1.1 Problemdefinition

Die Entwicklung des Reifegradmodells startet mit der Problemdefinition. In dieser Phase werden der Fokus des Modells, die Adressaten und die Zielsetzung bestimmt. Zusätzlich wird der Bedarf für das Reifegradmodell exemplifiziert.

Fokus des Reifegradmodells ist der BSI-Standards 200-4. Es handelt sich demnach um ein domänenspezifisches Reifegradmodell. Die Adressaten des Reifegradmodells sind Anwender des BSI-Standards 200-4. Wesentlicher Treiber für die  Erstellung  des  Reifegradmodells  ist  die  Aktualisierung  des  BSI-Standards 200-4 und der damit verbundene Bedarf seitens der Anwender für ein Reifegradmodell. Die Erhebung von Reifegraden soll anhand Self-Assessments erfolgen und  ohne  externe  Unterstützung  realisierbar  sein.  Geplante  Interviewpartner bzw. Nutzer des Modells sind BC-Beauftragte sowie gegebenenfalls weitere Mitarbeiter der jeweiligen Organisation.

Die Analyse des Bedarfs ist ein wesentlicher Handlungsschritt bei der Erstellung von Reifegradmodellen. Dies ermöglicht, dass das Reifegradmodell nicht nur innovativen Charakter hat, sondern ist auch für die praktische Anwendung relevant. 103  Ein wesentlicher Punkt der Bedarfsanalyse ist der Entwicklungsstand des betrachteten Gestaltungsbereichs. 104  Im Kontext dieser Thesis handelt es sich hierbei um den BSI-Standard 200-4. Eine zentrale Annahme ist es, dass mit zunehmender Reife des Entwicklungsstands eines Gestaltungsbereichs die Unsicherheit bei Anwendern verringert wird. Abbildung 9 zeigt den Zusammenhang zwischen dem Entwicklungsstand eines Gestaltungsbereichs  und dem Bedarf nach einem Reifegradmodell.

103  Vgl. Becker, J. et al., 2009, S. 252

104  Vgl. Mettler, T., 2010, S. 45-46

<!-- page: 37 -->

<!-- image -->

Quelle: Mettler, T., 2010

Abbildung 9: Bedarf nach Reifegradmodellen in Abhängigkeit des Entwicklungsstands

Auf Basis dieser theoretischen Überlegung kann festgehalten werden, dass ein neuer bzw. aktualisierter Gestaltungsbereich für Unsicherheiten bei Anwendern sorgen kann. Diese Unsicherheiten können zu einem Bedarf nach einem geeigneten Reifegradmodell führen. Aufgrund der Aktualität des BSI-Standards 200-4 kann davon ausgegangen werden, dass der Entwicklungsstand des BCM nach dem aktualisierten Standard in vielen Institutionen noch nicht weit verbreitet ist. Dies wurde ebenfalls im Rahmen des ersten IT-Grundschutztags durch Nachfragen der Anwender nach einem Reifegradmodell ersichtlich. 105

## 3.1.2 Anforderungen an das Reifegradmodell

Im ersten Schritt der Modellentwicklung werden Anforderungen definiert, die das Reifegradmodell zu erfüllen hat. Diese dienen als Grundlage zu dessen Entwicklung.

- (A1) Urteilskraft: Das Reifegradmodell soll ein fundiertes Urteil über den Reifegrad des BCM gemäß BSI-Standard 200-4 in einer bestimmten Institution ermöglichen. Der Reifegrad muss anhand von messbaren und differenzierbaren Kriterien bestimmt werden können. Durch das Reifegradmodell soll ein ganzheitlicher Überblick über den Umsetzungsstand des BCMS entstehen. Eine ganzheitliche Abdeckung der Themenbereiche des BSI-Standards 2004 ist demzufolge eine Grundvoraussetzung.
- (A2) Verständlichkeit: Zweck des Reifegradmodells ist die Kommunikation des Reifegrads innerhalb einer Institution. Das Reifegradmodell soll demnach

105  Vgl. Youtube Präsenz der HiSolutions AG, 2021

<!-- page: 38 -->

- leicht verständlich und erklärbar sein, beispielsweise mithilfe von Visualisierungen. Es soll eine einfache und schnelle Leistungsbewertung ermöglichen. Die Bedienung des Modells soll einfach und ohne externe Unterstützung möglich sein. Zur Erhöhung der Akzeptanz muss die Struktur des Reifegradmodells nachvollziehbar dokumentiert sein.
- (A3) Anwendbarkeit: Das Reifegradmodell soll für alle Institutionen unabhängig  ihrer  Größe  und  Beschaffenheit  anwendbar  sein.  Das  zugrundeliegende Referenzwerk sollte demnach international anerkannt und akzeptiert sein.  Die  Methodik  des  Reifegradmodells soll  zudem auf anerkannten und verbreiteten Vorgehensweisen aufbauen.
- (A4) Empfehlungscharakter: Das Reifegradmodell soll Anwender dabei unterstützen, den neuen BSI-Standard 200-4 umzusetzen. Aus diesem Grund sollen mithilfe des Reifegradmodells spezifische Handlungsempfehlungen ermittelt werden.
- (A5) Vergleichbarkeit: Das Reifegradmodell soll organisationsübergreifende Vergleiche (Benchmarks) ermöglichen. Neben der Bewertung des Leistungsniveaus einzelner Institutionen sollen die Ergebnisse mit anderen Institutionen verglichen werden können. Die Ergebnisse der Reifegraderhebung müssen demnach eindeutig und reproduzierbar sein.

<!-- page: 39 -->

## 3.1.3 Bewertung bestehender BCM-Reifegradmodelle

In den letzten Jahren wurden bereits vereinzelt Reifegradmodelle für das BCM konzipiert. Im Rahmen des folgenden Abschnitts wird die Anwendbarkeit der bestehenden BCM-Reifegradmodelle auf den BSI-Standard 200-4 diskutiert.  Die Diskussion erfolgt auf Basis der Ergebnisse einer komparativen Analyse. 106  Bei bestehenden Reifegradmodellen für das BCM wird zwischen Reifegradmodellen und Self-Assessment-Erhebungsbögen unterschieden. Für die nachfolgende Bewertung wurden ausschließlich öffentlich verfügbare BCM-Reifegradmodelle berücksichtigt, die nachfolgend kurz erläutert werden:

- Business Continuity Maturity Model (Klawitter, 1997),
- BCM Maturity Model (Smit, 2005) sowie
- BCM Maturity Model (Randeree, 2012).

BCMM (Klawitter, 1997): Das BCMM wurde im Jahre 1997 durch Jerry Klawitter entwickelt. Klawitter war Manager in einer führenden Investmentbank und wollte mithilfe des Reifegradmodells ein Werkzeug entwickeln, mit dem sich der Zustand des BCMS in Institutionen bewerten lässt. 107  Primärerer Zweck des Tools war es, Stakeholdern und Investoren die Möglichkeit zu geben, sich über die Beschaffenheiten des BCMS von Institutionen zu informieren. Ebenfalls wurde das Reifegradmodell für die Erstellung von Benchmarks genutzt, das die Reife des BCMS zwischen Institutionen verschiedener Branchen vergleicht. 108  Das Reifegradmodell  besteht  aus  sechs  Reifegradstufen.  Diese  wurden  durch  Klawitter selbstständig definiert und basieren auf keinem standardisierten Referenzwerk. Die sechs Reifegradstufen gliedern sich wie folgt:

- Level 1: Self-Governed,
- Level 2: Supported Self-Governed,
- Level 3: Cooperatively-Governed,
- Level 4: Enterprise Awakening,
- Level 5: Planned Growth,
- Level 6: Synergistic.

Die Leistung und Effektivität des BCMS wird mithilfe von eigenständig definierten Domänen berechnet. Die Erhebung der Domänen erfolgte eigenständig auf der Basis von selbst definierten Schlüsselelementen des BCMS. 109  Die betrachteten Domänen des Reifegradmodells sind: 110

106  Haidzir, H. et al., 2018

107  Vgl. Haidzir, H. et al., 2018, S. 43

108  Vgl. Klawitter, J., 2007, S. 6

109  Vgl. Klawitter, J., 2007, S. 9-11

110  Sinngemäße Übersetzung, basierend auf Klawitter, J., 2007, S. 9-11.

<!-- page: 40 -->

- Führung des BCMS,
- Mitarbeiter-Awareness,
- BC-Programmstruktur,
- Durchdringung des Programms,
- Metriken,
- Ressourceneinsatz,
- externe Koordinierung,
- inhaltliche Betrachtung des BCMS.

BCM Maturity Model (Smit, 2005): Dieses Reifegradmodell wurde durch Naomi Smit im Rahmen einer Masterthesis erstellt. Ziel der Arbeit war es, dem Bedarf eines Instruments zur Reifegradmessung des BCMS gerecht zu werden. 111  Smits Reifegradmodell liegt die Annahme zugrunde, dass die Reife des BCMS sowohl durch die Prozessqualität als auch durch den Umfang (Scope) des Managementsystems bestimmt wird. 112  Zur Bewertung der Reifegrade wird das Modell in sogenannte Scope Process Quality Stages (SPQS) unterteilt. Der jeweilige Reifegrad wird durch das Maß an Abdeckung der SPQS ermittelt. Die Bewertung von SPQS erfolgt mithilfe von spezifischen Anforderungen. Hierzu wird jedes SPQS durch verschiedene Merkmale beschrieben. Für jedes Merkmal werden konkrete Zielvorgaben festgelegt. Jede Zielvorgabe wird in spezifische und messbare Anforderungen unterteilt. Abbildung 10 zeigt das Zusammenspiel von Merkmalen, Zielvorgaben und Anforderungen.

Quelle: Eigene Darstellung in Anlehnung an Smit, N., 2005

<!-- image -->

Abbildung 10: Struktureller Aufbau von SPQS gemäß Smit

Das Reifegradmodell ist nicht sektorspezifisch und kann für Organisationen unterschiedlicher Branchen verwendet werden. Die zu erreichenden Reifegradstufen des Modells gliedern sich wie folgt: 113

111  Vgl. Smit, N., 2005, S. 2

112  Vgl. Smit, N., 2005, S. 52

113  Vgl. Smit, N., 2005, S. 49-50

<!-- page: 41 -->

- Level 1: Initial: Ein Commitment durch das Management für das BCMS ist erkennbar. Es sind Verantwortlichkeiten und Vorgaben definiert.
- Level 2: Geplant: Die notwendigen Analysen des BCMS werden durchgeführt. Relevante BC-Pläne sind erstellt. Eine Vorgehensweise für das BCMS wurde festgelegt.
- Level 3: Implementiert: Maßnahmen werden nicht nur geplant, sondern auch durchgeführt. Die anfallenden Aufgaben sind Personen zugewiesen und werden umgesetzt.
- Level 4: Integriert: Der BCMS-Prozess ist implementiert und wird gelebt. Die Abläufe des BCMS sind werden verstanden und umgesetzt.
- Level 5: Gesteuert: Tests und Übungen für das BCMS werden regelmäßig durchgeführt. Das BCMS ist in den organisatorischen Abläufen der Organisation fest verankert.
- Level 6: Optimiert: Die Abläufe des BCMS sind fester Bestandteil der Organisationskultur und werden kontinuierlich verbessert. Das BCMS gilt als strategisches Instrument zur Steuerung der Organisation.

BCM Maturity Model (Randeere, 2012): Das BCM-Reifegradmodell von Randeree ist das aktuellste der betrachteten Reifegradmodelle und an der University of  Oxford  entwickelt.  Der  Fokus  dessen  Untersuchungsbereichs  lag  auf  dem Bankensektor der Vereinigten Arabischen Emirate. 114  Die Entwicklung des Modells erfolgte in zwei Stufen. Zunächst wurde eine Analyse bestehender BCM-Reifegradmodelle durchgeführt. In der zweiten Stufe wurde das entwickelte Modell  im  Rahmen von Fokusgruppen des  Bankensektors der vereinigten Arabischen Emirate validiert. Inhaltlich basiert das Reifegradmodell von Randeree auf einer High-Level-Struktur des prozessualen Ablaufs des BCMS. Dies wurde in sieben Schritte unterteilt. Zusätzlich wurden fünf relevante Themenbereiche (Domänen) identifiziert, die zur Erhebung der Reifegrade verwendet werden. Die sieben Stufen des BCMS-Prozesses werden den jeweiligen Themenbereichen zugeordnet (Abbildung 11). 115

114  Vgl. Randeree, K. et al., 2012, S. 472

115  Vgl. Randeree, K. et al., 2012, S. 479

<!-- page: 42 -->

Quelle: Eigene Darstellung in Anlehnung an Randeree, K., 2012 und Smit, N., 2005 Abbildung 11: Betrachtungsbereiche des Reifegradmodells von Randeree

<!-- image -->

In Anlehnung an das Reifegradmodell von Smit betrachtet Randeeres Reifegradmodell ebenfalls die Reifegradmessung mithilfe der zweidimensionalen Betrachtungsweise  (BCM-Prozessqualität  sowie BCM-Prozessumfang).  Die  Erhebung der Reifegrade erfolgt mithilfe der erläuterten SPQS-Methodik von Smit. 116 Eine wesentliche Anforderung des Reifegradmodells für den BSI-Standard 2004 ist eine vollständige Abdeckung der relevanten Inhalte. Um zu überprüfen, ob ein bereits bestehenden BCM-Reifegradmodell für die Anwendung auf den aktualisierten  BSI-Standard geeignet ist,  wurde ein inhaltlicher Vergleich durchgeführt. Hierzu wurden die Inhalte des BSI-Standards den Betrachtungsbereichen der vorgestellten Reifegradmodelle gegenübergestellt (Abbildung 12). Eine detaillierte Beschreibung des inhaltlichen Vergleichs befindet sich im Anhang I: Vergleich bestehender BCM-Reifegradmodelle.

116  Vgl. Randeree, K. et al., 2012, S. 480

<!-- page: 43 -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 12: Bewertung bestehender Reifegradmodelle hinsichtlich der Anwendbarkeit auf den BSI-Standard 200-4

Abbildung 12 zeigt, dass keines der betrachteten Modelle die Inhalte des BSI-Standards  200-4  vollständig  abdeckt.  Die  analysierten  Reifegradmodelle  sind zwar inhaltlich fundiert, entsprechen jedoch nicht den inhaltlichen Anforderungen des aktualisierten BSI-Standards. Dies ist primär auf die Aktualität und inhaltliche Detailtiefe des BSI-Standards zurückzuführen. Obwohl vereinzelt Anzeichen für einen hohen Abdeckungsgrad erkennbar sind (Abbildung 12), ist das inhaltliche Delta zu groß, um dies mit inhaltlichen Anpassungen der bestehenden Modelle zu schließen.

Der Vergleich bereits bestehender BCM-Reifegradmodelle hat gezeigt, dass keines der öffentlich verfügbaren Modelle für die Anwendung des BSI-Standards 200-4 geeignet ist. Gründe hierfür sind vor allem die fehlende Abdeckung der Inhalte des BSI-Standards 200-4 sowie der Fakt, dass den Modellen kein international anerkanntes Referenzwerk zur Reifegraderhebung zugrunde liegt. Hilfreiche Erkenntnisse liefert jedoch die Ausgestaltung der Reifegradmodelle. Es ist erkennbar, dass alle Modelle den Betrachtungsbereich des BCMS in verschiedene Domänen unterteilt haben. Klawitter hat zur logischen Gruppierung der Domänen kritische Erfolgsfaktoren (Corporate Competencies) gebildet. 117  Smit sowie  Randeree  haben  auf  Basis  verschiedener  Best-Practice-Standards  einen High-Level-Prozess des BCM gebildet und die einzelnen Teilschritte in Betrachtungsbereiche gruppiert (Abbildung 11). 118,   119  Die Bewertung der bestehenden Reifegradmodelle des BCM führt zu der Erkenntnis, dass keines der Modelle für eine Anwendung auf den BSI-Standard 200-4 geeignet ist. Es besteht somit der Bedarf, ein eigenständiges Reifegradmodell zu entwickeln.

117  Vgl. Klawitter, J., 2007, S. 9-11

118  Vgl. Smit, N., 2005, S. 56

119  Vgl. Randeree, K. et al., 2012, S. 479

<!-- page: 44 -->

## 3.1.4 Festlegung der Entwicklungsstrategie

Im folgenden Abschnitt wird die Entwicklungsstrategie des Reifegradmodells für den BSI-Standard 200-4 diskutiert und festgelegt. Dies erfolgt unter Berücksichtigung der definierten Anforderungen und Ergebnisse der komparativen Analyse bestehender BCM-Reifegradmodelle.

Ziel des Reifegradmodells für den BSI-Standard 200-4 ist es, Anwendern des Standards eine Hilfestellung für die Umsetzung der relevanten Anforderungen des Standards zu liefern. Eine wesentliche Anforderung, die an das Reifegradmodell gestellt wird, ist die vollständige Betrachtung der relevanten Themen des BSI-Standards  200-4.  Der  Vergleich  der  bestehenden  BCM-Reifegradmodelle hat gezeigt, dass keines der derzeit existierenden BCM-Reifegradmodelle die Inhalte des Standards vollständig abdeckt.

In Anlehnung an Hecht (2013) wird im Folgenden zwischen zwei zentralen Komponenten des Reifegradmodells unterschieden: 120  die Prozess-Komponente und die Assessment-Komponente. Die Prozess-Komponente bildet die inhaltliche Basis  des  Reifegradmodells (Was  wird  gemessen?) ,  während  die  Assessment-Komponente die Methodik zur Messung der Reifegrade beinhaltet (Wie wird gemessen?) . Die Entwicklungsstrategie teilt sich demnach in zwei Teilaspekte auf. Für den Anteil der Prozess-Komponente wird die Strategie der Neuentwicklung (auf Basis der Kombination bestehender Modelle) gewählt, für die Assessment-Komponente wird ein bestehendes Basismodell spezifiziert. Abbildung 13 visualisiert die ausgewählte Entwicklungsstrategie.

120  Vgl. Hecht, S., 2013, S. 143

<!-- page: 45 -->

Quelle: Eigene Darstellung in Anlehnung an Hecht, 2013

<!-- image -->

Abbildung 13: Visualisierung der geteilten Entwicklungsstrategie in Anlehnung an Hecht

Verschiedene vergleichbare Arbeiten empfehlen die Auswahl der ISO/IEC 330xx-Reihe (ehemals ISO/IEC 15504) als methodische Grundlage für eine geeignete Modellentwicklung und -anpassung.  121,   122  Auch die ISO/IEC 330xx-Reihe sieht eine  Aufteilung  des  Reifegradmodells  in  verschiedene  Modellkomponenten vor. 123  Die Diskussion und Auswahl des Basismodells werden im folgenden Abschnitt fortgesetzt.

## 3.1.5 Diskussion und Auswahl der Modellbasis

Zur inhaltlichen Erstellung des Reifegradmodells wird ein geeignetes Basismodell benötigt. Dessen Auswahl erfolgt unter der Berücksichtigung der definierten Anforderungen (siehe Abschnitt 3.1). Jedoch sind nicht alle Anforderungen für die Auswahl des Basismodells relevant. Nachfolgend werden die für die Auswahl des Basismodells eminenten Aspekte extrahiert. Basierend auf den definierten Anforderungen sollte das Basismodell:

- auf internationalen Standards basieren,
- vielseitig anerkannt,
- für Institutionen unterschiedlicher Größe und Beschaffenheit anwendbar sowie
- umfassend dokumentiert sein.

121  Vgl. Hecht, S., 2013, S. 139

122  Vgl. Hauck, J. et al., 2011, S. 52

123  Vgl. International Organisation for Standardisation, 2015, S. 4

<!-- page: 46 -->

Unter  der  Berücksichtigung  der  Anforderungen  erscheint  die  ISO/IEC-330xx-Reihe als ein mögliches Basismodell. Die Normreihe ISO/IEC 330xx ist ein umfangreiches Rahmenwerk für die Durchführung von Prozess-Assessments. Sie löste im Jahre 2015 die weit verbreitete ISO/IEC-Reihe 155xx ab, die die Grundlage für etablierte Reifegradmodelle lieferte. Ebenfalls wurde durch die Aktualisierung der Normenreihe der Anwendungsbereich erweitert. 124   Nachfolgend wird die Eignung der Normreihe für das Reifegradmodell für den BSI-Standard 200-4 diskutiert.

Die ISO/IEC 330xx wurde in vergleichbaren Arbeiten für die Erstellung eines Reifegradmodells  für  den  BSI-Standard  200-2  ebenfalls  als  Basismodell  ausgewählt. 125  Grund für die Auswahl war u.a. das umfassende methodische Vorgehen der Normreihe. Weitere Gründe, die für die Eignung als Basismodell sprechen, sind vor allem die internationale Standardisierung sowie die weite Verbreitung der Normenreihe. 126  Das lange Bestehen 127  sowie die kontinuierliche Weiterentwicklung der Normenreihe sprechen für eine hohe Reife des Referenzwerks. 128 Zudem ist die Normenreihe generisch aufgebaut und kann - verglichen mit anderen Modellen - ohne signifikanten Nachteil auf die jeweiligen Bedürfnisse angepasst werden. 129  Weitere Stärken der Normenreihe sind die Verständlichkeit und Allgemeingültigkeit des Modells.

Quelle: Eigene Darstellung

Abbildung 14: Erfüllungsgrad der extrahierten Anforderungen durch die ISO/IEC 330xx

Der Erfüllungsgrad der extrahierten Anforderungen  ist in Abbildung 14 dargestellt. In Anbetracht der hohen Anzahl an erfüllten Anforderungen werden die relevanten Teile der ISO/IEC 330xx als Basismodell für das Reifegradmodell ausgewählt. Der inhaltliche Aufbau der Normenreihe wird im Folgenden dargestellt. Die Normreihe ISO/IEC 330xx besteht insgesamt aus 18 Einzelnormen und stellt ein umfangreiches Rahmenwerk für die Durchführung von Prozess-Assessments bereit. 130  Für die Erstellung des Reifegradmodells sind insbesondere die Einzelnormen ISO/IEC 33001, ISO/IEC 33020 sowie die ISO/IEC 33004 relevant. Die ISO/IEC 33001 definiert das Rahmenwerk für die Messung der Prozessreife. Die ISO/IEC 33020 definiert generische Anforderungen (Prozessattribute), die zur Erreichung der  jeweiligen  Reifegradstufe  benötigt  werden.  Prozessattribute  sind demnach Merkmale eines Prozesses, anhand derer die Reife des Prozesses gemessen werden kann. Die ISO/IEC 33004 definiert Anforderungen an die Erstellung eines Prozess-Referenzmodells. Dieses bildet die inhaltlichen Aspekte des Reifegradmodells und  wird  benötigt,  um  die  Inhalte  des  BSI-Standards  200-4 messbar zu gestalten. Inhaltlich besteht die Normenreihe aus drei Schlüsselelementen:

124  Vgl. Lami, G. et al., 2014

125  Vgl. Bas, M., 2021, S. 54-55

126  Vgl. Salviano, C. &amp; Figueiredo, A., 2008, S. 177-178

127  Vgl. Schweigert, T. &amp; Phillip, M., 2018, S. 321

128  Vgl. Haufe, K., 2017, S. 135

129  Vgl. Haufe, K., 2017, S. 137

<!-- page: 47 -->

- einem Prozess-Referenzmodell (PRM),
- einem Prozess-Assessmentmodell (PAM) sowie
- einem Messmodell (MM).

Diese werden nachfolgend erläutert.

Prozess-Referenzmodell (PRM): Das  Prozess-Referenzmodell  bestimmt  das Anwendungsgebiet und den Betrachtungsumfang. Es besteht aus einer Reihe von miteinander zusammenhängen Prozessen. 131  Wie ein Prozess-Referenzmodell ausgestaltet werden soll, ist in der Norm ISO/IEC 33004 definiert. Eigenständige Prozesse sind im Rahmen dieser Norm nicht definiert. Daher wird für die Erstellung eines Reifegradmodells mindestens ein externes Prozess-Referenzmodell benötigt. 132

Prozess-Assessment-Modell: Das Prozess-Assessment-Modell ist das eigentliche Reifegradmodell. Es setzt sich aus dem Mess(Wie wird gemessen?) und Prozess-Referenzmodell (Was wird gemessen?) zusammen. Die beiden Dimensionen werden nachfolgend erläutert:

- Prozessdimension (x-Achse): Die Prozessdimension enthält alle betrachteten  Prozesse  des  zugrundeliegenden  Prozess-Referenzmodells.  Es  beschreibt demnach, was gemessen werden soll.  Die Anforderungen an das Prozess-Referenzmodell werden durch die ISO/IEC 33004 definiert.
- Reifegrad-Dimension (y-Achse): Die Reifegraddimension enthält die Indikatoren für die Fähigkeit der betrachteten Prozesse. Sie basiert auf dem zugrun-

130  Vgl. Bas, M., 2021, S. 56

131  Vgl. Del Carpio, A., 2018, S. 2

132  Vgl. Bas, M., 2021, S. 56

<!-- page: 48 -->

deliegenden Messmodell. Die Indikatoren gelten für alle Prozesse gleichermaßen. 133  Das Messmodell wird durch die ISO/IEC 33001 und ISO/IEC 33020 definiert.

Abbildung 15 zeigt die inhaltliche Zusammensetzung des Prozess-Assessment-Modells.

<!-- image -->

Quelle: Eigene Darstellung in Anlehnung an Müller et al., 2016

Abbildung 15: Zusammensetzung des Prozess-Assessment-Modells

Messmodell: Das Messmodell  ist  ein  Schema  zur  Bewertung  eines  Prozesses, 134   und dient als Rahmenwerk für die Messung der Reife der betrachteten Prozesse. Die Anforderungen an die Ausgestaltung des Messmodells sind in der ISO/IEC 33003 definiert. Grundlegende Elemente des Messmodells sind:

- aufeinander aufbauende Reifegradstufen,
- eine messbare Ausprägung von Qualitätsmerkmalen eines Prozesses sowie
- eine Reihe von Punkten, die einem Qualitätsmerkmal zugeordnet werden.

Eine vollständige Auflistung der Reifegradstufen sowie der dazugehörigen Prozessattribute befindet sich im Anhang III: Aufbau der Reifegradstufen.

133  Vgl. Müller, M. et al., 2016, S. 6-7

134  Lami, G. et al., 2014, S. 51-52

<!-- page: 49 -->

## 3.2  Entwicklung der Modellinhalte

Der folgende Abschnitt befasst sich mit der inhaltlichen Ausgestaltung des Reifegradmodells. Die vorherigen Abschnitte haben gezeigt, dass ein Reifegradmodell aus einem Prozess-Referenzwerk, einem Bewertungsrahmen sowie einem oder mehreren Prozess-Assessment-Modellen besteht. 135  Die inhaltliche Ausgestaltung des Reifegradmodells ist entlang dieser Schlüsselelemente strukturiert.

## 3.2.1 Das Prozess-Referenzmodell

Um die Inhalte des BSI-Standards 200-4 in ein messbares Modell überführen zu können, wird ein Prozess-Referenzmodell benötigt. Der BSI-Standard 200-4 definiert Anforderungen an ein BCMS. Obwohl er prozessorientiert aufgebaut ist, ist ein eigenständiges PRM nicht vorhanden. Im Folgenden wird ein PRM, basierend auf  den  Anforderungen  des  BSI-Standards  200-4,  erstellt.  Hierzu  werden  zunächst die relevanten Prozesse des BSI-Standards 200-4 identifiziert. Die Struktur des PRM für den BSI-Standard 200-4 basiert auf der von Cortina et al. (2014) entwickelten High-Level-Structure (HLS) für Managementsysteme. 136  Basierend auf der HLS wurden die Prozesse des BSI-Standards 200-4 in Management-Prozesse (MP), Prozesse des BCMS Lifecycle (LP) sowie Support-Prozesse (SP) unterteilt. Das Ergebnis ist in Abbildung 16 visualisiert.

135  Vgl. International Organisation for Standardisation, 2015, S. 6

136  Vgl. Cortina, S. et al., 2014, S. 36-47

<!-- page: 50 -->

Quelle: Eigene Darstellung in Anlehnung an Cortina et al., 2014 Abbildung 16: High-Level-Struktur des PRM

Die  Prozesse  des  PRM  wurden  mithilfe  der  Statement-Tree-Methodik  identifiziert.  Hierzu  wurden  im  ersten  Schritt  die  relevanten  Anforderungen  des  BSI-Standards 200-4 erhoben und kategorisiert (muss, soll, kann). Im Anschluss wurden elementare Anforderungen identifiziert. Auf dieser Basis wurden Prozessbereiche definiert sowie eine spezifische Zielsetzung für jeden Prozessbereich festgelegt. Mithilfe einer Mindmap wurden Anforderungen mit ähnlicher Zielsetzung zusammengefasst. Abbildung 17 zeigt einen Auszug eines Statement Tree für den Prozess MP.1.

<!-- page: 51 -->

<!-- image -->

Quelle: Eigene Darstellung in Anlehnung an Cortina et al., 2014

Abbildung 17: Statement-Tree für den Prozess 'Initiierung, Planung und Steuerung'

Im nächsten Schritt wurden auf Basis der identifizierten Anforderungen Prozessbeschreibungen erstellt. Um konform zur ausgewählten Modellbasis zu sein, wurden diese entlang der Anforderungen der ISO/IEC 33004 erstellt. Die inhaltliche Beschreibung der Prozesse dient dabei primär als Grundlage zur Erhebung der jeweiligen Reifegradstufen und erhebt keinen Anspruch auf Vollständigkeit. Die Prozessbeschreibungen setzen sich wie folgt zusammen:

- Definition des Prozesszwecks: Der Zweck eines Prozesses setzt sich aus der Beschreibung des Ziels des Prozesses sowie konkreter Ergebnisse zusammen.
- Definition der Prozessergebnisse: Prozessergebnisse sind eine Detaillierung  des  Prozesszwecks. 137 Sie  spezifizieren,  was  durch  den  Prozess  erreicht werden soll.
- Arbeitsprodukte: Ein Prozessergebnis wird über Arbeitsprodukte definiert. Diese können die Herstellung eines Artefakts (z.B. ein Dokument), die signifikante Änderung des Zustands oder die Erfüllung von Anforderungen sein. 138 Zusammen mit Basispraktiken stellen sie Nachweise für die Erfüllung des Prozesszwecks dar.
- Basispraktiken: Diese  sind  modellhafte 139   Aktivitäten,  deren  Umsetzung Prozessergebnisse ermöglichen.

137  Vgl. Müller, M. et al., 2016, S. 8

138  Vgl. International Organisation for Standardisation, 2015, S. 3

139  Alle beschriebenen Aspekte des Prozess-Referenzmodells sind modellhaft zu verstehen. Sie erheben keinen Anspruch auf Vollständigkeit.

<!-- page: 52 -->

Tabelle 2 zeigt einen Auszug der Prozessbeschreibungen des PRM für den BSIStandard 200-4. Die vollständigen Prozessbeschreibungen befinden sich im Anhang II: Prozessbeschreibungen des PRM.

MP.1 Initiierung, Planung und Steuerung des BCMS

| Attribut             | Eigenschaft                                                                                                                                                                                                                                                                                                                                      |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck                | Festlegung der strategischen Rahmenbedingungen des BCMS sowie Anpassung des BCMS an die organisatorischen Begeben- heiten der Institution.                                                                                                                                                                                                       |
| Prozessergebnisse    | • Ziele und Rahmenbedingungen des BCMS sind festgelegt und kommuniziert. • Gründe für das BCMS sind identifiziert und dokumentiert. • Abzusichernder Zeitraum und Geltungsbereich des BCMS ist definiert. • Verantwortung der Institutionsleitung ist dokumentiert. • Vorgehensweise für das BCM wurde festgelegt.                               |
| Basispraktiken       | • Analyse der relevanten Anforderungen an das BCMS • Festlegung der strategischen Ziele des BCMS • Identifikation und Benennung der Stakeholder des BCMS • Erhebung der relevanten Schnittstellen zu weiteren Manage- mentsystemen • Erstellung und Freigabe der BCM-Leitlinie • Identifikation der zeitlichen Ressourcen des BCM-Beauftrag- ten |
| Arbeitsprodukte      | • BCM-Leitlinie • Selbstverpflichtung der Institutionsleitung • Festlegung der Vorgehensweise • Abgegrenzter Geltungsbereich des BCMS                                                                                                                                                                                                            |
| Referenzen BSI 200-4 | • 3.1.1 Zielsetzung • 3.1.2 Geltungsbereich • 3.1.3 Entscheidung für Vorgehensweise • 3.1.4 Übernahme der Verantwortung durch die Leitungsebene • 3.1.1.2 Abzusichernder Zeitraum durch ein BCM • 3.1.1.1 Motivation für den Aufbau eines BCMS                                                                                                   |

Quelle: Eigene Darstellung basierend auf ISO/IEC 33004

Tabelle 2: Prozesssteckbrief MP.1

<!-- page: 53 -->

## 3.2.2 Der Bewertungsrahmen

Um den Reifegrad eines Prozesses messen zu können, wird ein geeigneter Bewertungsrahmen benötigt. Für dieses Reifegradmodell wird der Bewertungsrahmen der ISO/IEC 33020 verwendet. Die Orientierung an die Norm ermöglicht es, das  Reifegradmodell  für  objektive,  wiederholbare  und  auf  Nachweisen  basierende Beurteilungen zu nutzen. 140  Die Messung der Prozessreife nach ISO/IEC 33020 erfolgt in sechs Stufen. Die Reifegradstufen sind durch die Norm vorgegeben und somit international bekannt und erprobt. Um die Beschreibung der Reifegradstufen praxisorientierter zu gestalten, werden diese mit Beschreibungen des Mindeststandards des BSI HV-Benchmark ergänzt. 141  Die Reifegradstufen des Reifegradmodells für den BSI-Standard 200-4 werden wie folgt definiert:

## Stufe 0: Unvollständig

Der Prozess wird nicht durchgeführt. Es liegen keine Nachweise für die Durchführung des Prozesses vor. Verantwortlichkeiten für die Durchführung des Prozesses sind nicht definiert.

## Stufe 1: Durchgeführt

Der Prozess wird situativ bzw. ad-hoc, ohne Planung und ohne spezifische Vorgaben, durchgeführt. Das Wissen liegt bei einzelnen Wissensträgern und ist nicht dokumentiert. Der Prozess erreicht zwar seine definierten Prozessergebnisse, diese werden jedoch nicht nach einer definierten Vorgehensweise erreicht. Verantwortlichkeiten für die Durchführung des Prozesses sind definiert. Der Handlungsbedarf und die Aufgaben für die Durchführung des Prozesses sind bekannt, werden jedoch ereignisgetrieben umgesetzt. Das Know-how und Expertenwissen in Bezug auf die Prozessdurchführung bündeln sich bei einzelnen Kompetenzträgern.

## Stufe 2: Wiederholbar

Durch festgelegte Ablaufmuster wird die Durchführung des Prozesses wiederholbar. Der Prozess wird gelegentlich durchgeführt. Die Durchführung ist nicht mehr von einzelnen Wissensträgern abhängig, sondern kann ebenfalls von fachnahen Mitarbeitern  durchgeführt  werden.  Abläufe  sind  jedoch  nicht  organisationsweit bekannt (Silostrukturen). Für die Durchführung des Prozesses existieren Dokumente und Vorgaben, die diesen Ablauf beschreiben und eingehalten werden.

140  Vgl. Gaulke, M., 2015, S. 201

141  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2018, S. 48

<!-- page: 54 -->

## Stufe 3: Standardisiert

Der Prozess ist vollständig dokumentiert und standardisiert. Zudem wird er regelmäßig gemäß definierter Vorgehensweise durchgeführt. Seine Verantwortlichkeiten und Abläufe sind organisationsweit bekannt. Der Ablauf des Prozesses entspricht den Anforderungen des BSI-Standards 200-4 (Standard-BCMS). Die Mitarbeiter  werden  hinsichtlich  der  Prozessdurchführung  regelmäßig  ausgebildet und besitzen nachweislich die erforderlichen Fähigkeiten.

## Stufe 4: Gesteuert

Für die Prozessdurchführung wurden konkrete Ziele definiert. Die Einhaltung der Zielvorgaben wird regelmäßig mithilfe von Kennzahlen kontrolliert und gesteuert. Die Einhaltung von Vorgaben für den Prozess wird regelmäßig überprüft und etwaige Abweichungen zeitnah korrigiert.

## Stufe 5: Optimierend

Der  Prozess  wird  kontinuierlich  verbessert.  Verbesserungsvorschläge  werden identifiziert und zeitnah umgesetzt. Der Prozess wird mithilfe von Tools unterstützt.

Um eine inhaltliche Trennschärfe zwischen den unterschiedlichen Reifegradstufen zu gewährleisten, wurden diese mit Schlüsselwörtern versehen. Diese werden nachfolgend erläutert:

| RG                        | Schlüsselwort                                                                             | Beschreibung                                                        |
|---------------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| 1                         | Situativ/ad-hoc durch externe                                                             | Der Prozess wird anlassbezogen durchgeführt und Trigger angestoßen. |
| 2 Gelegentlich            | Der fest definier- tes Intervall.                                                         | Prozess wird wiederholt durchgeführt, jedoch ohne                   |
| Regelmäßig                | Der Prozess wird in einem fest definierten Intervall durchgeführt.                        | 3                                                                   |
| Regelmäßig überprüft      | Die Einhaltung der fest definierten Intervalle wird mit Hilfe von Kenn- zahlen gesteuert. | 4                                                                   |
| Kontinuierlich verbessert | Der Prozess wird durch die durchführenden Mitarbeiter kontinuierlich verbessert.          | 5                                                                   |

Quelle: Eigene Darstellung

Tabelle 3: Beschreibung der Schlüsselwörter zur Identifikation der Reifegradstufen

Die Festlegung der erreichten Reifegradstufe erfolgt anhand von Prozessattributen. Diese sind jeder Reifegradstufe zugeordnet und beschreiben die benötigten Fähigkeiten für die jeweilige Reifegradstufe. Im Rahmen des Reifegrad-Assessments werden die Reifegrade des Prozesses mithilfe der Prozessattribute identifiziert. Die Prozessattribute sowie deren Zuordnung zu den Reifegradstufen sind in Tabelle 4 dargestellt.

<!-- page: 55 -->

| Reifegradstufe          | ID     | Prozessattributname                |
|-------------------------|--------|------------------------------------|
| Stufe 0: Unvollständig  |        |                                    |
| Stufe 1: Durchgeführt   | PA 1.1 | Prozessperformance                 |
| Stufe 2: Wiederholbar   | PA 2.1 | Management der Prozessdurchführung |
| Stufe 2: Wiederholbar   | PA 2.2 | Management der Arbeitsprodukte     |
| Stufe 3: Standardisiert | PA 3.1 | Prozessdefinition                  |
| Stufe 3: Standardisiert | PA 3.2 | Prozessumsetzung                   |
| Stufe 4: Gesteuert      | PA 4.1 | Prozessmessung                     |
| Stufe 4: Gesteuert      | PA 4.2 | Prozesskontrolle                   |
| Stufe 5: Optimierend    | PA 5.1 | Prozessinnovation                  |
| Stufe 5: Optimierend    | PA 5.2 | Kontinuierliche Verbesserung       |

Quelle: ISO/IEC 33020, 2014

Tabelle 4: Prozessattribute gemäß ISO/IEC 33020

Die Prozessattribute bilden die Bewertungsgrundlage zur Identifikation der Reifegrade. Gemäß ISO/IEC 33020 wird jedem Prozessattribut ein Wert auf einer vierstufigen Bewertungsskala zugewiesen (Tabelle 5). 142

| Bewertung               | Bedeutung       | Erreichung                                                                    | Beschreibung   |
|-------------------------|-----------------|-------------------------------------------------------------------------------|----------------|
| Nicht er- reicht        | 0 % bis 15 %    | Es gibt keinen Nachweis für die Erreichung des Prozessattributs.              | N              |
| Teilweise erreicht      | >15 % bis 50 %  | Es gibt einen Teilnachweis für die Errei- chung des Prozessattributs.         | P              |
| Größten- teils erreicht | >50 % bis 85 %  | Es gibt einen signifikanten Nachweis für die Erreichung des Prozessattributs. | L              |
| Vollständig erreicht    | >85 % bis 100 % | Es gibt einen vollständigen Nachweis für die Erreichung des Prozessattributs. | F              |

Quelle: ISO/IEC 33020, 2014

Tabelle 5: Bewertungsskala gemäß ISO/IEC 33020

Die Reifegradstufe 1 wird beispielsweise erreicht, wenn das Prozessattribut PA 1.1  größtenteils  erreicht  wurde  (Umsetzungsgrad  größer  als  50%).  Die  Erreichung  der  Reifegradstufe  1  ist  eine  wesentliche  Grundvoraussetzung  für  die nächsthöheren  Reifegradstufen.  Da  die  Reifegradstufen  kumulativ  aufgebaut sind, kann der nächsthöhere Reifegrad erst erreicht werden, wenn die Prozessattribute des vorherigen Reifegrads vollständig erreicht wurden (Umsetzungsgrad größer als 85%). Die Zusammensetzung der Reifegradstufen und der notwendigen Umsetzungsgrade sind im Anhang III: Aufbau der Reifegradstufen dargestellt.

142  Vgl. International Organisation for Standardisation, 2014, S. 7

<!-- page: 56 -->

Die eigentliche Zielvorstellung des Standards sieht vor, ein ganzheitlich gesteuertes BCMS zu betreiben (demnach mindestens Reifegradstufe 4). Dies wird u.a. durch die Erhebung von Kennzahlen im Rahmen eines  eigenständigen Querschnittsprozesses im BSI-Standard 200-4 gefordert. 143  Infolgedessen müssten - bei korrekter Umsetzung des BSI-Standards 200-4 - alle anderen Teilprozesse des Reifegradmodells mindestens Reifegradstufe 4 erreichen. Dies würde dazu führen, dass der LP.8: Überprüfung und Berichterstattung nur die Reifegradstufe 4 erreichen kann, wenn alle anderen Prozesse diese Reifegradstufe ebenfalls erreicht haben. Folgerichtig würde dies zu einer Abhängigkeit aller Prozesse des PRM und dem LP.8: Überprüfung und Berichterstattung führen, was die praktische Anwendung des Reifegradmodells verkomplizieren würde. Um das Reifegradmodell jedoch praxisorientiert zu gestalten, wurde sich im Rahmen der Erstellung des Modells darauf geeinigt, dass die Umsetzung der Reifegradstufe 3 den Anforderungen des BSI-Standards 200-4 entspricht.

Für das Reifegradmodell wurden schematische Zielniveaus definiert. Diese orientieren sich an den unterschiedlichen Startmodellen des BSI-Standards 200-4 (Reaktiv-BCMS  und  Standard-BCMS).  Da  das  Aufbau-BCMS  als  StandardBCMS mit eingeschränktem Prozessumfang 144  gilt, besteht hinsichtlich der Zielreifegrade der einzelnen Prozesse kein Unterschied. Das Zielniveau des Aufbau-BCMS wird daher nicht näher betrachtet. Die Soll-Reifegrade sind schematisch zu verstehen und dienen als Richtwert für die Reifegraderhebung. Basierend auf den Anforderungen des BSI-Standards 200-4 wurden für die Zusammensetzung der Soll-Reifegrade folgende Annahmen getroffen:

- Standard-BCMS: Das  Standard-BCMS  gilt  als  vollständig  umgesetztes BCMS. 145   Alle  Prozesse  des  Reifegradmodells  sollten  in  der  Konsequenz gleichmäßig auf einem höheren Reifegrad umgesetzt werden.
- Reaktiv-BCMS: Das Reaktiv-BCMS priorisiert Aspekte, die eine angemessene Notfallbewältigung fördern. 146   Demzufolge wird der Soll-Reifegrad für Prozesse der Notfallbewältigung höher angesetzt als für entfallene BCM-Prozess-Schritte des Standard-BCMS.

143  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 279-280

144  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 142

145  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 145

146  Vgl. Bundesamt für Sicherheit in der Informationstechnik, 2021, S. 46

<!-- page: 57 -->

Tabelle 6 zeigt die schematischen Soll-Reifegrade der unterschiedlichen BCMSStartmodelle des BSI-Standards 200-4.

| Prozesskürzel   | Reaktiv-BCMS   | Standard-BCMS   |
|-----------------|----------------|-----------------|
|                 | 3              | MP.1 2          |
| 1               | 3              | MP.2            |
| 3               | 3              | LP.1            |
|                 | 3 3            | LP.2            |
|                 | 3 3            | LP.3            |
|                 | 1,5 3          | LP.4            |
|                 | 0 3            | LP.5            |
|                 | 1 3            | LP.6            |
|                 | 1,5 3          | LP.7            |
|                 | 0,5 3          | LP.8            |
| 2               | 3              | LP.9            |
|                 | 1 3            | SP.1            |
| SP.2            | 1 3            |                 |
| SP.3            | 1 3            |                 |

Quelle: Eigene Darstellung

Tabelle 6: Schematische Zusammensetzung der Zielniveaus

## 3.2.3 Das Prozess-Assessment-Modell

Im Prozess-Assessment-Modell wird das PRM mit dem Bewertungsrahmen des zugrundeliegenden Basismodells kombiniert. Hierzu werden Reifegradstufen für die identifizierten Prozesse des PRM gebildet. Für diese Reifegradstufen werden die generischen Prozess-Attribute (PA) des Basismodells für den jeweiligen Prozess interpretiert. Die Prozesse des PRM (Abschnitt 3.2.1) werden demnach den generischen Prozessattributen (Abschnitt 3.2.2) zugeordnet. Zur späteren Erhebung der Reifegrade werden ausgehend von den Prozess-Attributen spezifische Fragestellungen erstellt. Diese werden, um ein zielorientiertes Messen zu ermöglichen, im Sinne der Goal-Question-Metric (GQM-)-Methode erstellt. Hierdurch werden basierend auf den definierten Zielen je Reifegrad (in diesem Fall: Prozess-Attribute)  spezifische  Fragestellungen  konkretisiert.  Dies  ermöglicht  die Operationalisierung der Messziele und eine spätere Bewertung, inwieweit diese erreicht wurden. 147

In  den  folgenden  Abschnitten  werden  die  Reifegradstufen  der  einzelnen  Prozesse detailliert zusammengefasst. Abbildung 18 zeigt das Schema zur Zusammensetzung der Reifegradstufen sowie der spezifischen Fragestellungen je Reifegradstufe.

147  Vgl. Müller, M. et al., 2016, S. 216-217

<!-- page: 58 -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 18: Schema zur Zusammensetzung der Reifegradstufen

## 3.2.3.1  MP.1 Initiierung, Planung und Steuerung des Managementsystems

Der Managementprozess MP.1 verfolgt das Ziel, die strategischen Rahmenbedingungen für das BCMS sowie die Anpassung an die organisatorischen Begebenheiten zu gewährleisten. Tabelle 7 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen.

<!-- page: 59 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Die Leitungsebene nimmt die Verantwortung für das BCMS wahr. • Die Verantwortung für das BCMS ist dokumentiert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | • Nimmt die Leitungsebene die Verantwortung für das BCMS wahr und ist dies dokumentiert?                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 2: Wiederholbar  | PA 2.1 : • Die Institutionsleitung definiert strategische Ziele für das BCMS. • Eine Vorgehensweise (Road- map) für zur nachhaltigen Etab- lierung des BCMS ist geplant. • Die Leitungsebene zeigt Inte- resse am BCMS und geht mit gutem Beispiel voran. • Die benötigten Ressourcen für das BCMS werden erhoben. • Die Anforderungen an das BCMS werden gelegentlich identifiziert und darauf aufbau- end Ziele abgeleitet. • Schnittstellen zu weiteren Ma- nagementsystemen werden identifiziert. PA 2.2: • Es existiert eine BCMS-Leitlinie. • Die BCMS-Leitlinie wird gele- gentlich aktualisiert. • Ziele und Vorgehensweise des BCMS werden gelegentlich eva- luiert und bei Bedarf angepasst. | • Definiert die Institutionsleitung strategische Ziele für das BCMS? Werden die Ziele und die Vorgehensweise gelegent- lich evaluiert und bei Bedarf an- gepasst? • Zeigt die Institutionsleitung Inte- resse für das BCMS und geht mit gutem Beispiel voran? • Ist die Vorgehensweise zur Etablierung des BCMS geplant (beispielsweise in einer Road- map)? • Werden benötigte Ressourcen für das BCMS und Schnittstel- len zu weiteren Management- systemen identifiziert? • Existiert eine Leitlinie für das BCMS, und wird diese gelegent- lich aktualisiert? |

<!-- page: 60 -->

| 3: Standardisiert   | PA 3.1: • Interessensgruppenanalyse für das BCMS wurde durchgeführt. • Stakeholder für das BCMS sind identifiziert. • Es finden regelmäßige Abstim- mungen mit allen relevanten Stakeholdern gemäß Interes- sensgruppenanalyse statt. • Die Wirksamkeit und Angemes- senheit des BCMS wird regel- mäßig überprüft. PA 3.2: • Der BCM-Beauftragte ist in den strategischen Planungsprozess für das BCMS eingebunden. • Anforderungen und Rahmenbe- dingungen an das BCMS wer- den regelmäßig auf Basis des BSI-Standards 200-4 erhoben und neubewertet. • Verbesserungspotentiale hin- sichtlich der Vorgehensweise werden identifiziert.   | • Wurde eine Interessensgrup- penanalyse durchgeführt und alle relevanten Stakeholder für das BCMS identifiziert? • Finden regelmäßige Abstim- mungen mit allen relevanten Stakeholdern statt? • Wird die Wirksamkeit und Ange- messenheit des BCMS regel- mäßig überprüft? • Ist der BCM-Beauftragte in den strategischen Planungsprozess für das BCMS eingebunden? • Werden Anforderungen und Rahmenbedingungen (auf Ba- sis des BSI-Standards 200-4) an das BCMS regelmäßig erho- ben und neubewertet? • Werden Verbesserungspotenti- ale zur Vorgehensweise des BCMS identifiziert?   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- page: 61 -->

| 4: Gesteuert   | PA 4.1: • Die Institutionsleitung besitzt ein gutes Verständnis über das BCMS. • Die strategischen Ziele des BCMS sind an den Zielen der In- stitution ausgerichtet. • Strategische Kennzahlen für das BCMS sind definiert. • Es finden regelmäßige Abstim- mungen mit der Institutionslei- tung über die Effektivität und Ef- fizienz des BCMS statt. PA 4.2: • Die Ressourcen für das BCMS entsprechen dem analysierten Bedarf. • Benötigte Ressourcen für not- wendige Projekte werden pro- aktiv geplant. • Bei Problemen (z.B. Ressour- cenmangel) leitet die Instituti- onsleitung adäquate Maßnah-   | • Besitzt die Institutionsleitung ein gutes Verständnis über das BCMS? • Sind die Ziele des BCMS an den strategischen Zielen oder Orga- nisation ausgerichtet? • Wurden strategische Kennzah- len für das BCMS definiert? • Finden regelmäßige Abstim- mungen mit der Institutionslei- tung über die Effektivität und Ef- fizienz des BCMS statt?   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5: Optimierend | PA 5.1: • Die Institutionsleitung beteiligt sich aktiv am BCMS, beispiels- weise durch die Teilnahme in Branchentagungen und Interes- sensverbänden. • Benötigte Ressourcen werden regelmäßig proaktiv geplant. PA 5.2: • Auf Basis von aktuellen Ent- wicklungen (z.B. Änderungen in Best Practices) werden Verbes- serungspotentiale für das BCMS identifiziert. • Verbesserungsvorschläge für das BCMS werden bewertet und umgesetzt.                                                                                                                                                                    | • Beteiligt sich die Institutionslei- tung aktiv am BCMS, beispiels- weise durch die Teilnahme an Branchentagungen und Interes- senverbänden? • Werden benötigte Ressourcen für das BCMS proaktiv geplant? • Werden basierend auf aktuellen Entwicklungen Verbesserungs- potentiale für das BCMS identi- fiziert, bewertet und umgesetzt?           |

Quelle: Eigene Darstellung

Tabelle 7: MP.1: Reifegradstufen und spezifische Fragestellungen

<!-- page: 62 -->

## 3.2.3.2  MP.2 Managementreview

Der Management-Prozess MP.2 verfolgt das Ziel, strategische Entscheidungen für die zukünftige Weiterentwicklung des BCMS zu treffen. Tabelle 8 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen.

<!-- page: 63 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • BCM-Managementreviews wer- den anlassbezogen (ad hoc) durchgeführt.                                                                                                                                                                                                                                                                                                                                                                                                            | • Werden BCM-Managementre- views anlassbezogen durchge- führt?                                                                                                                                                                                                                                                                                                                                               |
| 2: Wiederholbar  | PA 2.1: • Ziele für BCM-Managementre- views sind festgelegt. • Managementreviews werden gelegentlich durchgeführt. • Vorgehensweise für die Durch- führung von Managementre- views ist festgelegt. • Ansprechpartner für die Durch- führung von Managementre- views werden frühzeitig einge- bunden. PA 2.2: • Vorgehensweise für die Durch- führung von Managementre- views ist dokumentiert. • Es existieren Templates und Ar- beitshilfen für die Durchführung von Managementreviews. | • Werden BCM-Managementre- views gelegentlich durchge- führt? • Sind Ziele und Vorgehensweise für die Durchführung von BCM- Managementreviews festgelegt und dokumentiert? • Sind die benötigten Ansprech- partner für die Durchführung von BCM-Managementreviews bekannt, und werden diese früh- zeitig eingebunden? • Existieren Templates und Ar- beitshilfen für die Durchführung von Managementreviews? |

<!-- page: 64 -->

| 3: Standardisiert   | PA 3.1: • Die BCM-Managementreviews werden regelmäßig und in fest- gelegten Intervallen durchge- führt. • Die Vorgehensweise für die Durchführung von BCM-Ma- nagementreviews ist den betei- ligten Personen bekannt. PA 3.2: • Entscheidungen werden auf Ba- sis einer standardisierten Ent- scheidungsvorlage getroffen. • Auf Basis des BCM-Manage- mentreviews werden Entschei- dungen für das BCMS erhoben und dokumentiert.   | • Existiert eine Geschäftsordnung für den Notfallstab und benennt diese die Rolleninhaber des Stabs namentlich? • Wurden Aufgaben, Befugnisse und Kompetenzen der Rollen in- nerhalb der BAO festgelegt und dokumentiert? • Besitzen die Rollen der BAO nachweislich die notwendigen Kompetenzen (beispielsweise durch relevante Schulungen und Trainings)? • Sind die Mitarbeiter der BAO or- ganisationsweit bekannt und werden spezifisch für ihre jewei- lige Funktion im Stab ausgebil- det? • Wird der Stabsraum der BAO sowie die notwendigen Utensi- lien regelmäßig aktuell gehal- ten?   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4: Gesteuert        | PA 4.1: • Die regelmäßige Durchführung von BCM-Managementreviews wird mit Hilfe von Kennzahlen gesteuert. PA 4.2: • BCM-Managementreviews wer- den regelmäßig hinsichtlich der korrekten Durchführung über- prüft.                                                                                                                                                                                                                  | • Wird die regelmäßige Durchfüh- rung von BCM-Managementre- views mit Hilfe von Kennzahlen gesteuert? • Wird die korrekte Durchführung der BCM-Managementreviews regelmäßig überprüft?                                                                                                                                                                                                                                                                                                                                                                                                             |
| 5: Optimierend      | PA 5.1: • Die Durchführung von BCM-Ma- nagementreviews wird kontinu- ierlich verbessert. • Sollten BCM-Managementre- views nicht aussagekräftig sein, werden Verbesserungspotenti- ale identifiziert und umgesetzt.                                                                                                                                                                                                                 | • Wird die Durchführung von BCM-Managementreviews kon- tinuierlich verbessert? • Werden Verbesserungspotenti- ale für die Managementberichte (z.B. in Bezug auf Aussagekraft) identifiziert und umgesetzt?                                                                                                                                                                                                                                                                                                                                                                                         |

Quelle: Eigene Darstellung

Tabelle 8: MP.2: Reifegradstufen und spezifische Fragestellungen

<!-- page: 65 -->

## 3.2.3.3  LP.1 Befähigung der Stabsstrukturen

Der Lifecycle-Prozess LP.1 verfolgt das Ziel, angemessene Stabsstrukturen zur Notfallbewältigung aufzubauen. Tabelle 9 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen.

<!-- page: 66 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Eine besondere Aufbauorgani- sation (BAO) ist etabliert. • Rollen und Verantwortlichkeiten sind grob definiert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | • Existiert ein Notfall- oder Krisen- stab, und sind die Rollen und Verantwortlichkeiten für diesen zumindest grob definiert?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2: Wiederholbar  | PA 2.1: • Die Aufgaben und notwendige Befugnisse der Mitglieder der BAO sind identifiziert. • Es existieren rudimentäre Vor- gaben, Handlungsabläufe und Verhaltensmuster für die Stabs- arbeit. • Die Rollen sind durch geeig- nete Mitarbeiter besetzt. • Mitglieder der BAO werden auf die Wahrnehmung ihrer Rolle vorbereitet. • Arbeitsmittel für die Stabsarbeit sind beschafft (z.B. Krisen- stabsraum inklusive Ausstat- tung). • Rollen und Stabsmitglieder sind untereinander bekannt, die Weisungsbefugnis ist festge- legt. PA 2.2: • Verhaltensweisen für die Stabs- arbeit werden erhoben und sind dokumentiert. • Interessensgruppen für die Not- fallkommunikation sind bekannt. | • Wurden Aufgaben und notwen- dige Befugnisse für die Mitglie- der der BAO identifiziert? • Sind die definierten Rollen der BAO durch geeignete Mitarbei- ter besetzt, und werden diese auf die Wahrnehmung der Rolle vorbereitet? • Sind die Rollen der Stabsmit- glieder untereinander bekannt und ist die Weisungsbefugnis der Rollen festgelegt? • Existieren rudimentäre Vorga- ben, die die Handlungsabläufe und Verhaltensmuster für die Stabsarbeit vorgeben? • Wurden die notwendigen Ar- beitsmittel für die Stabsarbeit beschafft (z.B. Krisenstabsraum inklusive Ausstattung)? • Wurden Interessensgruppen für die Notfallkommunikation identi- fiziert |

<!-- page: 67 -->

| PA 3.1: • Es existiert eine Geschäftsord- nung für den Notfallstab (inklu- sive namentlicher Benennung der Rolleninhaber). • Die Aufgaben, Befugnisse und Kompetenzen der Rollen der                                                                                                                                                                                                                                                                                                                                                                                   | • Existiert eine Geschäftsordnung für den Notfallstab und benennt diese die Rolleninhaber Stabs namentlich? • Wurden Aufgaben, und Kompetenzen der Rollen nerhalb der BAO festgelegt dokumentiert? • Besitzen die Rollen der nachweislich die Kompetenzen durch relevante und Trainings)? • Sind die Mitarbeiter der BAO ganisationsweit bekannt werden spezifisch für ihre lige Funktion im Stab det?   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BAO wurden festgelegt. • Die Rollen der BAO besitzen nachweislich die notwendigen Kompetenzen, beispielsweise durch relevante Schulungen und Trainings. • Die Aufgaben, Befugnisse und Verantwortlichkeiten der Rollen der BAO sind festgelegt und do- kumentiert. PA 3.2: • Die Mitarbeiter der BAO sind or- ganisationsweit bekannt, not- wendige Befugnisse sind fest- gelegt. • Die Mitarbeiter der BAO werden regelmäßig geschult und spezi- fisch für ihre jeweilige Funktion im Stab ausgebildet. • Der Stabsraum sowie die not- wendigen Utensilien werden re- | des Befugnisse in- und BAO notwendigen (beispielsweise Schulungen or- und jewei- ausgebil-                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | • Wird der Stabsraum der sowie die notwendigen lien regelmäßig aktuell                                                                                                                                                                                                                                                                                                                                   |
| gelmäßig aktuell gehalten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | BAO                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Utensi- gehal-                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | ten?                                                                                                                                                                                                                                                                                                                                                                                                     |

<!-- page: 68 -->

| 4: Gesteuert   | PA 4.1: • Die Besetzung der BAO wird re- gelmäßig hinsichtlich der Ange- messenheit überprüft. • Vollständigkeit der Arbeitsmate- rialien zur Stabsarbeit wird re- gelmäßig geprüft. PA 4.2: • Die Aufgabenverteilung und Rollenbesetzung der BAO wer- den regelmäßig evaluiert. • Der Schulungsbedarf der Rolle- ninhaber wird regelmäßig evalu- iert. • Die Befähigung von Stabsstruk- turen ist Bestandteil des Übungsprogramms.   | • Wird die Besetzung der BAO re- gelmäßig hinsichtlich Angemes- senheit überprüft? • Wird die Aufgabenverteilung, die Rollenbesetzung und der Schulungsbedarf der Mitglieder der BAO regelmäßig überprüft? • Werden die Arbeitsmaterialien zur Stabsarbeit regelmäßig auf Vollständigkeit und Aktualität überprüft? • Wird der Schulungsbedarf der Rolleninhaber regelmäßig eva- luiert? • Wird die angemessene Befähi- gung von Stabsstrukturen im Rahmen von Übungen kontrol- liert?   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5: Optimierend | PA 5.1: • Mögliche Verbesserungspoten- tiale für die Stabsarbeit (z.B. Rollenverteilung, Ausstattung des Stabsraums, Stabsord- nung) werden identifiziert und bewertet.                                                                                                                                                                                                                                                               | • Werden regelmäßig mögliche Verbesserungspotentiale (z.B. Rollenverteilung, Ausstattung des Stabsraums, Stabsord- nung) für die Stabsarbeit identi- fiziert, bewertet und umgesetzt?                                                                                                                                                                                                                                                                                                    |

Quelle: Eigene Darstellung

Tabelle 9: LP.1: Reifegradstufen und spezifische Fragestellungen

<!-- page: 69 -->

## 3.2.3.4  LP.2 Meldung, Alarmierung und Erstreaktion

Der Lifecycle-Prozess LP.2 verfolgt das Ziel, Strukturen und Verfahren für eine angemessene Meldung, Alarmierung und Erstreaktion von Notfällen aufzubauen und aufrechtzuerhalten. Tabelle 10 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen.

<!-- page: 70 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Verantwortlichkeiten und Zu- ständigkeiten für Meldungen und Alarmierungen wurden be- nannt. • Sofortmaßnahmen nach Scha- denseintritt wurden rudimentär definiert.                                                                                                                                                                                                                                                                                                                    | • Wurden Verantwortlichkeiten und Zuständigkeiten für Mel- dungen und Alarmierungen be- nannt? • Existieren zumindest rudimen- täre Sofortmaßnahmen, die nach einem Schadenseintritt durchgeführt werden müssen?                                                                                                                                                                                                                                               |
| 2: Wiederholbar  | PA 2.1: • Meldungen, Alarmierungen und Erstreaktionen erfolgen nach ei- nem definierten Ablaufmuster. • Alarmierungsprozess ist defi- niert und visualisiert (z.B. im Rahmen eines Alarmierungs- konzepts). • Handlungsabläufe für Meldun- gen und Alarmierungen sind festgelegt. PA 2.2: • Relevante Rollen für den Alar- mierungsprozess sind identifi- ziert und im Alarmierungspro- zess verankert. • Beteiligte des Meldeprozesses werden hinsichtlich der gelten- den Vorgaben informiert. | • Existiert ein definiertes Ablauf- muster für Meldungen, Alarmie- rungen und Erstreaktionen? • Sind Handlungsabläufe für Mel- dungen und Alarmierungen fest- gelegt, und ist der Alarmie- rungsprozess visualisiert? • Wurden die relevanten Rollen für den Alarmierungsprozess identifiziert und im Alarmie- rungsprozess verankert? • Werden die beteiligten Rollen im Alarmierungsprozess gele- gentlich hinsichtlich der gelten- den Vorgaben informiert? |

<!-- page: 71 -->

| 3: Standardisiert   | PA 3.1: • Eine zentrale Meldestelle ist do- kumentiert und wurde organisa- tionsweit bekannt gemacht. • Handlungsabläufe in Bezug auf die Meldung, Alarmierung und Erstreaktion von Notfällen sind in Form von Vorgabedokumen- ten dokumentiert und entspre- chen den Anforderungen des BSI-Standards 200-4. • Der Meldeprozess ist mit betei- ligten Schnittstellen abgestimmt und bekanntgemacht worden. • Der Alarmierungsprozess sowie die dazugehörigen Eskalations- stufen sind mit Verantwortlichen des ISMS abgestimmt und wi- derspruchsfrei. PA 3.2: • Sofortmaßnahmen wurden an die Begebenheiten der Institu- tion angepasst und für spezifi- sche Notfallszenarien konkreti- siert. • Melde- und Alarmierungsver- fahren sind organisationsweit bekannt und erprobt. • Der Melde- und Alarmierungs- prozess entspricht den Vorga- ben des BSI-Standards 200-4. • Die BAO ist in Bezug auf die gel- tenden Vorgaben der Meldung, Alarmierung und Erstreaktion informiert. • Notfallmaßnahmen sowie As- pekte zur Meldung und Erstre- aktion werden regelmäßig er- probt.   | • Wurde eine zentrale Meldestelle eingerichtet, dokumentiert und organisationsweit bekannt ge- macht? • Sind die Handlungsabläufe für die Meldung, Alarmierung und Erstreaktion von Notfällen ent- sprechend den Anforderungen des BSI-Standards 200-4 doku- mentiert? • Wurde der Meldeprozess mit beteiligten Schnittstellen abge- stimmt und bekanntgemacht und entspricht dieser den Anfor- derungen des BSI-Standards 200-4? • Ist der Alarmierungsprozess (in- klusive Eskalationsstufen) mit den Verantwortlichen des ISMS abgestimmt und widerspruchs- frei? • Wurden die definierten Sofort- maßnahmen an die Begeben- heit der Institution angepasst und für spezifische Notfallsze- narien konkretisiert? • Sind die Melde- und Alarmie- rungsverfahren organisations- weit bekannt und werden diese regelmäßig erprobt?   |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- page: 72 -->

| 4: Gesteuert   | PA 4.1: • Die korrekte Durchführung von Meldungen und Alarmierungen wird regelmäßig überprüft, die Prüfgrundlage bilden die defi- nierten Handlungsanweisungen des Alarmierungskonzepts. • Ziele für die Durchführung des Melde- und Alarmierungspro- zesses sind definiert (z.B. Durchlaufzeit der Alarmierung). PA 4.2: • Der Melde- und Alarmierungs- prozess ist Bestandteil des Übungsumfangs und wird regel- mäßig erprobt. • Mögliche Abweichungen von Vorgaben im Alarmierungspro- zess werden identifiziert.   | • Wird die korrekte Durchführung (basierend auf den Inhalten des Alarmierungskonzepts) von Meldungen und Alarmierungen regelmäßig überprüft? Werden mögliche Abweichungen identi- fiziert und behoben? • Sind messbare Ziele für die Durchführung des Melde- und Alarmierungsprozesses defi- niert (z.B. Durchlaufzeit der Alarmierung)? • Ist der Melde- und Alarmie- rungsprozess Bestandteil des Übungsumfangs und wird die- ser regelmäßig erprobt?   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5: Optimierend | PA 5.1: • Für den Melde- und Alarmie- rungsprozess werden regelmä- ßig Verbesserungspotentiale identifiziert. • Die Alarmierung erfolgt mit der Unterstützung von Alarmie- rungstools. PA 5.2: • Die identifizierten Verbesse- rungspotentiale werden zeitnah umgesetzt. • Vorgaben und Handlungsan- weisungen werden regelmäßig hinsichtlich möglicher Verbes- serungspotentiale aktualisiert und angepasst.                                                                                                           | • Werden regelmäßig Verbesse- rungspotentiale für den Melde- und Alarmierungsprozess iden- tifiziert? Werden diese Verbes- serungspotentiale zeitnah um- gesetzt (z.B. durch Aktualisie- rung der relevanten Konzepte)? • Werden die Alarmierungen mit- hilfe von Alarmierungstools un- terstützt?                                                                                                                                                        |

Quelle: Eigene Darstellung

Tabelle 10: LP.2: Reifegradstufen und spezifische Fragestellungen

## 3.2.3.5  LP.3 Störbetrieb, Deeskalation und Bewältigung

Der Lifecycle-Prozess LP.3 verfolgt das Ziel, Strukturen und Verfahren für eine angemessene Rückführung in den Normalbetrieb nach einem Notfall aufzubauen und aufrechtzuerhalten. Tabelle 11 zeigt die Zusammensetzung der unterschiedlichen  Reifegradstufen  sowie  die  dazugehörigen  spezifischen  Fragestellungen des Prozesses.

<!-- page: 73 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Maßnahmen für die Rückfüh- rung in den Normalbetrieb nach einem Notfall wurden rudimen- tär definiert. • Verantwortlichkeiten und Zu- ständigkeiten für die Rückfüh- rung in den Normalbetrieb sind definiert.                                                                                                                                                                                                                                                                                                             | • Wurden Maßnahmen für eine geeignete Rückführung in den Normalbetrieb nach einem Not- fall rudimentär definiert? • Wurden Verantwortlichkeiten und Zuständigkeiten für eine Rückführung in den Normalbe- trieb definiert?                                                                                                                                                                                                               |
| 2: Wiederholbar  | PA 2.1: • Die Maßnahmen für eine Rück- führung in den Normalbetrieb wurden geplant und dokumen- tiert. • Ein Störbetriebsniveau wurde festgelegt und dokumentiert. • Die BAO wird hinsichtlich der Verfahren zur Rückführung in den Normalbetrieb geschult. • Eine Vorgehensweise für die Nachbereitung von Notfällen (Lessons Learned) wurde defi- niert. PA 2.2: • Kriterien für die Rückführung in den Normalbetrieb wurden fest- gelegt. • Es existiert eine Arbeitshilfe (Checkliste) für die Rückführung in den Normalbetrieb. | • Wurden Maßnahmen für die Rückführung in den Normalbe- trieb geplant und dokumentiert? Existiert eine Arbeitshilfe (Checkliste) für die Rückführung in den Normalbetrieb? • Wurden Kriterien für die Rück- führung in den Normalbetrieb definiert? • Wird die BAO hinsichtlich der Vorgehensweise zur Rückfüh- rung in den Normalbetrieb ge- schult? • Existiert eine Vorgehensweise zur Nachbereitung von Notfällen (Lessons Learned)? |

<!-- page: 74 -->

| 3: Standardisiert   | PA 3.1: • Das Notfallhandbuch enthält Verfahren für eine angemes- sene Rückführung in den Nor- malbetrieb. Diese werden regel- mäßig angepasst und doku- mentiert. • Nach einem Notfall werden re- gelmäßig Workshops und Ab- stimmungsrunden zur Identifika- tion von Verbesserungspotenti- alen durchgeführt. • Die Reihenfolge des Wiederan- laufs von Prozessen ist festge- legt und abgestimmt. • Die Kriterien für die Rückfüh- rung in den Normalbetrieb orien- tieren sich am BSI-Standard 200-4. PA 3.2: • Die Bewältigung von Notfällen wird regelmäßig ausgewertet. • Die Rückführung in den Normal- betrieb erfolgt anhand der defi- nierten Abläufe und festgeleg- ten Kriterien. • Die Bewältigung von Notfällen wird analysiert, hierzu wurden Bewertungskriterien für die Ana- lyse von Notfällen festgelegt.   | • Sind die Handlungsanweisun- gen für eine Rückführung in den Normalbetrieb im Notfallhand- buch dokumentiert? • Werden nach einer Notfallbe- wältigung regelmäßig Work- shops und Abstimmungsrunden zur Identifikation von Verbesse- rungspotentialen durchgeführt? • Entsprechen die Kriterien zur Rückführung in den Normalbe- trieb den Anforderungen des BSI-Standards 200-4? • Wird die Bewältigung von Not- fällen regelmäßig analysiert und ausgewertet (insbesondere hin- sichtlich der Einhaltung relevan- ter Vorgaben)?   |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- page: 75 -->

| 4: Gesteuert   | PA 4.1: • Die Bewältigung von Notfällen wird regelmäßig analysiert, um Verbesserungspotentiale zu identifizieren. • Die Einhaltung von Abläufen zur Notfallbewältigung wird regel- mäßig überprüft. • Die Kriterien zur Rückführung in den Normalbetrieb werden re- gelmäßig überprüft, Verbesse- rungspotentiale werden zeitnah eingearbeitet. PA 4.2: • Verbesserungspotentiale und Handlungsmaßnahmen in Be- zug auf die Notfallbewältigung werden erhoben, Konzepte wer-   | • Werden regelmäßig Verbesse- rungspotentiale für die Notfall- bewältigung identifiziert? Wer- den die Vorgaben und Abläufe auf Basis der identifizierten Ver- besserungspotentiale ange- passt? • Werden die Kriterien zur Rück- führung in den Normalbetrieb regelmäßig evaluiert?   |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5: Optimierend | PA 5.1: • Die Deeskalation und die Rück- führung in den Normalbetrieb werden kontinuierlich verbes- sert. • Erkenntnisse aus Übungen und Überprüfungen werden zeitnah eingearbeitet.                                                                                                                                                                                                                                                                                           | • Wird die Notfallbewältigung durch beteiligte Rollen kontinu- ierlich verbessert? Werden Er- kenntnisse aus Übungen und Überprüfungen für die Notfallbe- wältigung zeitnah eingearbei- tet?                                                                                           |

Quelle: Eigene Darstellung

Tabelle 11: LP.3: Reifegradstufen und spezifische Fragestellungen

## 3.2.3.6  LP.4 Business-Impact-Analyse

Der Lifecycle-Prozess LP.4 verfolgt das Ziel, eine regelmäßige Durchführung von Business-Impact-Analysen  zur  Identifikation  und  Bewertung  zeitkritischer  Geschäftsprozesse zu gewährleisten. Tabelle 12 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen des Prozesses.

<!-- page: 76 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Business-Impact-Analysen wer- den vereinzelt durchgeführt. • Verständnis über zeitkritische Geschäftsprozesse ist vorhan- den.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | • Werden vereinzelt Business- Impact-Analysen durchgeführt? • Existiert ein Verständnis über die zeitkritischen Geschäftspro- zesse der Organisation?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 2: Wiederholbar  | PA 2.1: • Parameter für die Durchführung von BIAs sind definiert (BIA-Pa- rameter, Zeithorizonte, Res- sourcenkategorien und Cluster). • Untragbarkeitsniveau wurde durch die Institutionsleitung festgelegt und dient als Grund- lage für die Durchführung von BIAs. • Die zu analysierenden Ge- schäftsprozesse werden nach- vollziehbar ausgewählt. • Ansprechpartner für die Durch- führung von BIAs sind bekannt. • BIA-Ansprechpartner werden im Vorfeld inhaltlich vorbereitet und verstehen die BIA-Methodik. PA 2.2: • Prozessabhängigkeiten (sowohl vor und nachgelagert) werden identifiziert. • Es existieren Vorgaben, in de- nen beschrieben wird, wie BIAs durchgeführt werden (z.B. BIA- Leitfaden). • Es existieren Templates für die Durchführung von BIAs. • Es existieren grobe/schemen- hafte Vorgaben für die Durch- führung von BIAs. | • Wurden die notwendigen Para- meter für die Durchführung von BIAs definiert? • Wurde das Untragbarkeitsni- veau durch die Institutionslei- tung festgelegt, und dient dies als Grundlage für die Durchfüh- rung von BIAs? • Werden die zu analysierenden Geschäftsprozesse nachvoll- ziehbar ausgewählt? • Sind die Ansprechpartner für die Durchführung von BIAs be- kannt, und werden diese inhalt- lich vorbereitet? • Werden Abhängigkeiten zu vor- und nachgelagerten Prozessen identifiziert? • Wurden grobe Vorgaben für die Durchführung von BIAs definiert (z.B. BIA-Leitfaden, Erhebungs- templates), und werden diese verwendet? • Existieren Templates für die Durchführung von BIAs? |

<!-- page: 77 -->

| 3: Standardisiert   | PA 3.1: • Für alle Geschäftsprozesse der Organisation werden regelmä- ßig BIAs nach einem definierten Verfahren durchgeführt und do- kumentiert. • Es existiert ein Rahmenwerk für die Durchführung von BIAs, das den Anforderungen des BSI- Standards 200-4 entspricht. • Es existiert eine Gesamtüber- sicht über alle zeitkritischen Ge- schäftsprozesse der Organisa- tion. • Die geltenden BIA-Parameter, Ressourcenkategorien und die Schadensbewertung sind den relevanten Ansprechpartnern bekannt und mit diesen abge- stimmt. PA 3.2: • Mitwirkende an einer BIA haben ein tiefgreifendes Verständnis über das Prozessmanagement der Organisation. • Die Vorgehensweise für die Durchführung von BIAs ist wohl- verstanden. • BIAs werden nach einer stan- dardisierten und abgestimmten Vorgehensweise durchgeführt.   | • Werden regelmäßig BIAs nach einer standardisierten Vorge- hensweise für alle Geschäfts- prozesse der Organisation durchgeführt? • Existiert ein Rahmenwerk (defi- niertes Verfahren) für die Durch- führung von BIAs, das den An- forderungen des BSI-Standards 200-4 entspricht? • Existiert eine Gesamtübersicht über alle identifizierten zeitkriti- schen Geschäftsprozesse der Organisation? • Sind die geltenden BIA-Para- meter den relevanten Ansprech- partnern bekannt und mit diesen abgestimmt? • Haben die relevanten An- sprechpartner ein tiefgreifendes Verständnis über das Prozess- management der Organisation?   |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- page: 78 -->

| 4: Gesteuert   | PA 4.1: • Es werden messbare Ziele für die Durchführung von BIAs defi- niert (z.B. jährliche Aktualisie- rung). • Die Durchführung von BIAs wird mithilfe von Kennzahlen über- prüft. • Die Einhaltung von Vorgehens- weisen zur Erstellung von BIAs wird regelmäßig überprüft. PA 4.2: • Abweichungen bei der Durch- führung von BIAs werden er- kannt. • Fehlerhafte oder unstimmige Vorgaben werden bei Bedarf   | • Wurden messbare Ziele für die Durchführung von BIAs identifi- ziert (z.B. Jährliche Aktualisie- rung) • Wird die regelmäßige Durchfüh- rung von BIAs mithilfe von Kennzahlen gesteuert? • Wird die korrekte Durchführung von BIAs regelmäßig überprüft und werden mögliche Abwei- chungen im Ablauf erkannt? • Werden fehlerhafte oder un- stimmige Vorgaben bei Bedarf angepasst?   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5: Optimierend | PA 5.1: • Die Methodik zur Durchführung von BIAs wird kontinuierlich ver- bessert. PA 5.2: • Mithilfe von GRC Tools werden für die Durchführung von BIAs Synergieeffekte (z.B. gemein- same Datengrundlage) zu an- deren Managementsystemen genutzt.                                                                                                                                                                | • Wird die BIA-Methodik kontinu- ierlich verbessert? • Wird die Durchführung von BIAs mithilfe von GRC Tools unter- stützt (Synergieeffekte zu weite- ren Managementsystemen durch gemeinsame Daten- grundlage)?                                                                                                                                                                       |

Quelle: Eigene Darstellung

Tabelle 12: LP.4 Reifegradstufen und spezifische Fragestellungen

<!-- page: 79 -->

## 3.2.3.7  LP.5 BCM-Risikoanalyse und Soll-Ist-Vergleich

Der Lifecycle-Prozess LP.5 verfolgt das Ziel, eine regelmäßige Durchführung von BCM-Risikoanalysen und Soll-Ist-Vergleichen zu gewährleisten. Tabelle 13 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen des Prozesses.

<!-- page: 80 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • BCM-Risikoanalysen werden vereinzelt durchgeführt. • Soll-Ist-Vergleiche werden an- lassbezogen durchgeführt. • Für die Durchführung von BCM Risikoanalysen wurde eine zu- ständige Person benannt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | • Werden BCM-Risikoanalysen anlassbezogen durchgeführt? • Werden vereinzelt Soll-Ist-Ver- gleiche durchgeführt? • Wurde für die Durchführung von Risikoanalysen und Soll-Ist-Ver- gleichen eine zuständige Per- son benannt?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2: Wiederholbar  | PA 2.1: • Eine geeignete Risikoanalyse- methodik ist identifiziert. • Das Risikoakzeptanzniveau wurde durch die Institutionslei- tung festgelegt. • BCM-Risikoanalysen werden nach einem definierten Prozess durchgeführt. • Parameter für die Durchführung von Risikoanalysen sind festge- legt (Schadensausmaß, Risiko- kategorien). • Verantwortlichkeiten und Zu- ständigkeiten für die Durchfüh- rung von BCM Risikoanalysen sind definiert, zugewiesen und kommuniziert. • Mitarbeiter besitzen ein Ver- ständnis über die Durchführung von BCM Risikoanalysen. PA 2.2: • Soll-Ist-Vergleiche der identifi- zierten Verfügbarkeitsanforde- rungen werden durchgeführt. • Ergebnisse der BCM Risikoana- lysen werden an die Leitungs- ebene berichtet. • Bei identifizierten Abweichun- gen im Soll-Ist-Vergleich wird das auftretende Risiko bewertet und angemessen behandelt. | • Wurde eine geeignete Risiko- analysemethodik für die Durch- führung von BCM-Risikoanaly- sen definiert? • Wurde ein Risikoakzeptanzni- veau durch die Institutionslei- tung festgelegt? • Werden BCM-Risikoanalysen nach einem definierten Prozess durchgeführt? • Wurden Parameter (Eintritts- wahrscheinlichkeit, Schadens- ausmaß, Risikokategorien) für die Durchführung von BCM-Ri- sikoanalysen festgelegt? • Sind Verantwortlichkeiten und Zuständigkeiten für die Durch- führung von BCM-Risikoanaly- sen definiert und zugewiesen? • Besitzen die verantwortlichen Mitarbeiter nachweislich ein Verständnis über die Durchfüh- rung von BCM-Risikoanalysen? • Werden gelegentlich Soll-Ist- Vergleiche der identifizierten Verfügbarkeitsanforderungen durchgeführt? • Werden die Ergebnisse der BCM-Risikoanalysen an die Lei- tungsebene berichtet? |

<!-- page: 81 -->

| 3: Standardisiert   | PA 3.1: • Die Durchführung von BCM-Ri- sikoanalysen orientiert sich an geltenden Standards des Risi- komanagements. • BCM-Risikoanalysen werden nach einer festgelegten Vorge- hensweise durchgeführt. • Die zuständigen Mitarbeiter werden regelmäßig hinsichtlich der Methodik der BCM-Risiko- analyse geschult. • Vorgaben und Templates für die Durchführung von BCM-Risiko- analysen sind organisationsweit etabliert. PA 3.2: • BCM-Risikoanalysen werden in regelmäßigen Intervallen durch- geführt. • Ergebnisse der BCM-Risiko- analysen werden inhaltlich be- wertet, Verbesserungspotenti- ale werden identifiziert.   | • Werden BCM-Risikoanalysen nach geltenden Standards durchgeführt? • Werden die Mitarbeiter regel- mäßig hinsichtlich der BCM-Ri- sikoanalysemethodik geschult? • Sind die zu verwendenden Vor- gaben und Templates für die Durchführung von BCM-Risiko- analysen organisationsweit etabliert? • Werden BCM-Risikoanalysen in regelmäßigen Intervallen durch- geführt? • Werden die Ergebnisse der BCM-Risikoanalysen regelmä- ßig inhaltlich bewertet und Ver- besserungspotentiale identifi- ziert? • Werden die identifizierten Risi- ken angemessen in den BC- Strategien berücksichtigt? • Werden Änderungsbedarfe, die sich durch den Soll-Ist-Ver- gleich ergeben, durch das   |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4: Gesteuert        | PA 4.1: • Messbare Ziele für die Durch- führung und Aktualisierung von BCM-Risikoanalysen sind defi- niert. • Kennzahlen für die Steuerung von BCM-Risiken sind definiert und werden kontrolliert. PA 4.2: • Identifizierte Risiken werden an- gemessen behandelt, Maßnah- men werden zeitnah umgesetzt. • Die Einhaltung der definierten Vorgehensweise für BCM-Risi- koanalysen wird regelmäßig kontrolliert.                                                                                                                                                                                                                   | tet? • Sind messbare Ziele für die re- gelmäßige Durchführung von BCM-Risikoanalysen definiert? • Wurden aussagekräftige Kenn- zahlen für die Steuerung von BCM-Risiken definiert und wer- den diese regelmäßig kontrol- liert? • Wird die Einhaltung der definier- ten Vorgehensweise für BCM- Risikoanalysen regelmäßig kon- trolliert?                                                                                                                                                                                                                                                                                                                                             |

<!-- page: 82 -->

| 5: Optimierend   | PA 5.1: • Die Methodik zur Durchführung von BCM-Risikoanalysen wird kontinuierlich verbessert. • Es werden Best Practices ange- wendet, um die Identifikation von BCM-Risiken zu optimieren. PA 5.2: • Die Durchführung von BCM-Ri- sikoanalysen erfolgt toolge- stützt.   | • Wird die Risikoanalysemethodik für die Durchführung von BCM- Risikoanalysen kontinuierlich verbessert? • Erfolgt die Durchführung von BCM-Risikoanalysen und die Kategorisierung von BCM-Risi- ken toolgestützt?   |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Quelle: Eigene Darstellung

Tabelle 13: LP.5: Reifegradstufen und spezifische Fragestellungen

## 3.2.3.8  LP.6 Notfallplanung und Konzeption

Der Lifecycle-Prozess LP.6 verfolgt das Ziel, durch eine strukturierte Planung und Konzeption der Notfallbewältigung eine angemessene Absicherung der zeitkritischen Geschäftsprozesse zu gewährleisten. Tabelle 14 zeigt die Zusammensetzung  der  unterschiedlichen  Reifegradstufen  sowie  die  dazugehörigen  spezifischen Fragestellungen des Prozesses.

<!-- page: 83 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Es existieren Geschäftsfortfüh- rungspläne, Wiederanlaufpläne und Wiederherstellungspläne für vereinzelte Geschäftspro- zesse. • Es existieren rudimentäre BC- Strategien.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | • Existieren Geschäftsfortfüh- rungspläne für vereinzelte Pro- zesse sowie Wiederanlaufpläne und Wiederherstellungspläne für vereinzelte Ressourcen? • Wurden BC-Strategien rudi- mentär definiert?                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2: Wiederholbar  | PA 2.1: • Die BC-Strategien sind an den Zielen der Organisation ausge- richtet. • Es existieren vereinzelte Notfall- pläne für die in der BIA identifi- zierten zeitkritischen Geschäfts- prozesse. • Die maximal mögliche Notbe- triebsdauer ist definiert. • Die Notfallpläne sind an der ma- ximal möglichen Notbetriebs- dauer ausgerichtet. • Es existieren Arbeitshil- fen/Templates für die Erstellung von Notfallplänen und BC-Plä- nen. PA 2.2: • Es existiert ein Notfallhandbuch, das die Geschäftsfortführungs- planung, die Wiederanlaufpla- nung und die Wiederherstel- lungspläne beinhaltet. • Die Erstellung von Notfallplänen für das Notfallhandbuch wird durch den BCMB gesteuert. | • Sind die BC-Strategien an den Zielen der Organisation ausge- richtet? • Existieren vereinzelte Notfall- pläne für die in der BIA identifi- zierten zeitkritischen Geschäfts- prozesse? • Wurde die maximal mögliche Notbetriebsdauer definiert und sind die Notfallpläne an dieser ausgerichtet? • Existieren Arbeitshilfen bzw. Templates für die Erstellung von Notfallplänen und BC-Plänen? • Wird die Erstellung von Notfall- plänen für das Notfallhandbuch durch den BCMB gesteuert? • Existiert ein Notfallhandbuch, das die Geschäftsfortführungs- planung, die Wiederanlaufpla- nung und die Wiederherstel- lungsplanung beinhaltet? |

<!-- page: 84 -->

| 3: Standardisiert   | PA 3.1: • Es existieren Notfallpläne für alle zeitkritischen Geschäftspro- zesse, die in der BIA identifiziert wurden. • Es existieren Dokumentenvorla- gen für Notfallpläne, Geschäfts- fortführungspläne, Wiederan- lauf und Wiederherstellungs- pläne. • BC-Strategie-Optionen für alle Ressourcenkategorien wurden definiert. • Die ausgewählten BC-Strate- gien sind durch die Institutions- leitung freigegeben. • Zuständigkeiten für die jeweili- gen BC-Strategien sind zuge- wiesen und kommuniziert. PA 3.2: • Notfallpläne, Wiederherstel- lungspläne und Wiederanlauf- pläne werden unter Verwen- dung einer standardisierten Vor- lage erstellt, die auf die spezifi- schen Bedarfe der Institution angepasst wurde. • Notfallpläne, Wiederherstel- lungspläne und Wiederanlauf- pläne sind Bestandteil des Not- fallhandbuchs und entsprechen den Anforderungen des BSI- Standards 200-4. • Die Erstellung von Notfallplä- nen, Wiederherstellungsplänen und Wiederanlaufplänen erfolgt in enger Abstimmung mit den Ressourcenverantwortlichen. • Die Ressourcenverantwortli- chen verfügen über das notwen- dige Wissen zur Erstellung von Notfallplänen. • Die Erstellung und Aktualisie- rung von Notfallplänen wird re- gelmäßig überprüft und aktuali- siert.   | • Existieren Dokumentenvorla- gen für Notfallpläne, Geschäfts- fortführungspläne und Wieder- herstellungspläne? • Wurden BC-Strategie-Optionen für alle Ressourcenkategorien definiert? Wurden die ausge- wählten BC-Strategien durch die Leitungsebene freigege- ben? • Sind Zuständigkeiten und Ver- antwortlichkeiten für die jeweili- gen BC-Strategien zugewiesen und kommuniziert? • Werden Notfallpläne, Wieder- herstellungspläne und Wieder- anlaufpläne unter Verwendung einer standardisierten Vorlage erstellt? Entsprechen diese den Anforderungen des BSI-Stan- dards 200-4? • Erfolgt die Erstellung von Not- fallplänen, Wiederherstellungs- plänen und Wiederanlaufplänen in enger Abstimmung mit den Ressourcenverantwortlichen? Verfügen diese über das not- wendige Wissen zur Erstellung von Notfallplänen? • Wird die Erstellung und Aktuali- sierung von Notfallplänen regel- mäßig überprüft (z.B. durch Do- kumentenaudits)? • Existieren Notfallpläne für alle zeitkritischen Geschäftspro- zesse die durch die BIA identifi- ziert wurden?   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- page: 85 -->

| 4: Gesteuert   | PA 4.1: • Das Notfallhandbuch sowie die darin enthaltenen Konzepte werden kontinuierlich fortge- schrieben. • Das Notfallhandbuch sowie die darin enthaltenen Pläne werden regelmäßig auf Vollständigkeit und inhaltliche Konsistenz ge- prüft. PA 4.2: • Das Notfallhandbuch wird regel- mäßig an Erkenntnisse aus Übungen und Überprüfungen angepasst. • Verbesserungsvorschläge für das Notfallhandbuch werden zeitnah eingearbeitet.   | • Wird das Notfallhandbuch und die darin enthaltenen Konzepte kontinuierlich fortgeschrieben? • Wird das Notfallhandbuch und die darin enthaltenen Konzepte regelmäßig auf Vollständigkeit und Aktualität geprüft? • Wird das Notfallhandbuch regel- mäßig an Erkenntnisse aus Übungen und Überprüfungen angepasst? Werden Verbesse- rungsvorschläge zeitnah einge- arbeitet?   |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5: Optimierend | PA 5.1: • Die Inhalte des Notfallhand- buchs sowie der dazugehörigen Konzepte werden kontinuierlich optimiert und fortgeschrieben. PA 5.2: • Die Erstellung, Ablage und Ak- tualisierung von Notfallkonzep- ten erfolgen toolgestützt.                                                                                                                                                                                                     | • Werden die Inhalte des Notfall- handbuchs und die dazugehöri- gen Konzepte kontinuierlich op- timiert und fortgeschrieben?                                                                                                                                                                                                                                                    |

Quelle: Eigene Darstellung

Tabelle 14: LP.6: Reifegradstufen und spezifische Fragestellungen

<!-- page: 86 -->

## 3.2.3.9  LP.7 Tests und Übungen

Der Lifecycle-Prozess LP.7 verfolgt das Ziel, eine strukturierte Planung von Tests und Übungen für das BCMS zu ermöglichen. Hierbei sollen die Handlungsabläufe und Pläne des BCMS regelmäßig kontrolliert werden. Tabelle 15 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen des Prozesses.

<!-- page: 87 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Übungen für das BCMS werden vereinzelt durchgeführt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | • Werden vereinzelt Übungen für das BCMS durchgeführt?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 2: Wiederholbar  | PA 2.1: • Es existieren Rahmenvorgaben (z.B. ein Übungskonzept) für die Durchführung von Übungen und Tests. • Übungen und Tests werden jährlich geplant und im Rahmen der Jahresübungsplanung do- kumentiert. • Es wurde eine verantwortliche Person zur Vorbereitung, Durchführung und Nachberei- tung von Übungen benannt. • Aufgaben, Verantwortlichkeiten und Befugnisse werden für jede Übung festgelegt. • Übungsteilnehmer werden auf ihre Rolle innerhalb der Übung vorbereitet. • Die Übungen basieren auf den Inhalten des Notfallhandbuchs. PA 2.2: • Es bestehen Austauschmög- lichkeiten zur Planung und Nachbereitung von Übungen und Tests. • Es bestehen Vorgaben zur Pro- tokollierung und Dokumentation von Übungsergebnissen. | • Existieren rudimentäre Rah- menvorgaben (Übungskonzept) für die Durchführung von Übun- gen und Tests? • Werden Übungen und Tests jährlich geplant und wird dies im Rahmen der Jahresübungspla- nung dokumentiert? • Wurde eine verantwortliche Per- son für die Vorbereitung, Durch- führung und Nachbereitung von Übungen benannt? • Werden Aufgaben, Verantwort- lichkeiten und Befugnisse für jede Übung festgelegt? Werden die Übungsteilnehmer auf ihre Rolle innerhalb der Übung vor- bereitet? • Sind die Übungsinhalte an den Inhalten des Notfallhandbuchs ausgerichtet? • Bestehen Austauschmöglich- keiten zur Planung und Nachbe- reitung von Übungen und Tests? • Existieren Vorgaben zur Proto- kollierung und Dokumentation von Übungsergebnissen? |

<!-- page: 88 -->

| 3: Standardisiert   | PA 3.1: • Ein Übungsrahmen für die über- greifenden Aspekte von Übun- gen ist definiert (Art und Weise der Übungen), spezifische Übungskonzepte werden für jede Übung erstellt und entspre- chen den Anforderungen des BSI-Standards 200-4. • Vorbereitung, Durchführung und Nachbereitung von Übun- gen ist standardisiert und erfolgt stets nach der gleichen Vorge- hensweise. • Die notwendigen Kompetenzen für jedes Übungsmitglied wur- den definiert. • Benötigte Ressourcen/Infra- struktur für Übungen wurden identifiziert. PA 3.2: • Übungen werden regelmäßig hinsichtlich des Übungserfolgs (Wirksamkeit und Zweckmäßig- keit) bewertet. • Abweichungen innerhalb des Übungsdurchlaufs werden do- kumentiert und analysiert. • Übungsablauf ist dokumentiert und orientiert sich an den Inhal- ten des BSI-Standards 200-4. • Nach jeder Übung werden   | • Wurde ein Übungsrahmen für die übergreifenden Aspekte von Übungen (z.B. Art und Weise der Übungen) abgestimmt und freigegeben? Entspricht dieser den Anforderungen des BSI- Standards 200-4? • Ist die Vorbereitung, Durchfüh- rung und Nachbereitung von Übungen standardisiert und er- folgt stets nach der gleichen Vorgehensweise? • Wurden die notwendigen Kom- petenzen für jedes Übungsmit- glied sowie die benötigte Infra- struktur für Übungen identifi- ziert? • Werden die Übungen regelmä- ßig hinsichtlich des Übungser- folgs (insbesondere Wirksam- keit und Zweckmäßigkeit) be- wertet? • Wird nach jeder Übung ein Übungsbericht angefertigt? Be- inhaltet dieser Abweichungen, die im Übungsdurchlauf identifi- ziert wurden?   |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4: Gesteuert        | PA 4.1: • Die planmäßige Durchführung (gemäß Übungsplanung) von Übungen wird mithilfe von Kennzahlen gesteuert. PA 4.2: • Erkenntnisse und Lessons Learned aus Übungen werden in das Rahmenkonzept eingear- beitet. • Abweichungen gegenüber der Jahresübungsplanung werden identifiziert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | • Wird die regelmäßige bzw. plan- mäßige Durchführung von Übungen mithilfe von Kennzah- len gesteuert? Werden Abwei- chungen gegenüber der Jahres- planung identifiziert? • Werden Erkenntnisse und Les- sons Learned aus Übungen in das Rahmenkonzept eingear- beitet?                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

<!-- page: 89 -->

| 5: Optimierend   | PA 5.1: • Die Durchführung von Übungen wird kontinuierlich verbessert. • Erkenntnisse und Verbesse- rungsmaßnahmen aus Übun- gen werden bewertet und umge- setzt. PA 5.2: • Übungsprotokolle vergangener Übungen werden evaluiert, be- vor Übungen geplant werden.   | • Werden Erkenntnisse und Ver- besserungsmaßnahmen aus Übungen bewertet und umge- setzt? • Wird die Durchführung von Übungen kontinuierlich verbes- sert?   |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|

Quelle: Eigene Darstellung

Tabelle 15: LP.7: Reifegradstufen und spezifische Fragestellungen

<!-- page: 90 -->

## 3.2.3.10 LP.8 Überprüfung und Berichterstattung

Der Lifecycle-Prozess LP.8 verfolgt das Ziel, die Wirksamkeit und Angemessenheit des BCMS regelmäßig zu überprüfen. Zusätzlich beinhaltet der Prozess eine regelmäßige Berichterstattung an die Institutionsleitung. Tabelle 16 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen des Prozesses.

<!-- page: 91 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Berichte an die Leitungsebene zum Umsetzungsstand des BCMS werden ad hoc erstellt. • Überprüfungen des BCMS fin- den anlassbezogen statt.                                                                                                                                                                                                                                                                                                                                                                                                                       | • Werden anlassbezogen Über- prüfungen für das BCMS durch- geführt? • Werden anlassbezogen Be- richte zum BCMS für die Lei- tungsebene erstellt?                                                                                                                                                                                                                                                                                                                                                        |
| 2: Wiederholbar  | PA 2.1: • Berichte an die Leitungsebene finden gelegentlich statt. • Der BCMB besitzt einen direk- ten Berichtweg. • Operative Kennzahlen für das BCMS sind definiert. • (Externe) Überprüfungen zur Identifizierung von Abweichun- gen im BCMS werden gelegent- lich durchgeführt. • Für die Durchführung von BCMS-Audits ist eine verant- wortliche Person benannt. PA 2.2: • Die Jahresplanung für die Durchführung von BCMS-Über- prüfungen (Revisionspro- gramm) ist rudimentär geplant. • BCM-Berichte werden gelegent- lich (ohne festgelegte Intervalle) erstellt | • Werden gelegentlich (ohne feste Intervalle) Berichte über das BCMS für die Leitungs- ebene erstellt? • Besitzt der BCM-Beauftragte ei- nen direkten Berichtsweg an die Leitungsebene? • Wurden operative Kennzahlen für das BCMS definiert? • Werden gelegentlich Überprü- fungen für das BCMS durchge- führt? Ist für die Durchführung von diesen Überprüfungen eine verantwortliche Person be- nannt? • Existiert eine rudimentäre Jah- resplanung für die Durchfüh- rung von BCMS-Überprüfun- gen? |

<!-- page: 92 -->

| 3: Standardisiert   | PA 3.1: • Berichte an die Leitungsebene finden regelmäßig statt, der Auf- bau des BCMS-Berichts ist standardisiert und entspricht den Anforderungen des BSI- Standards 200-4. • Es existieren abgestimmte und freigegebene Vorlagen/Templa- tes für die Erstellung von BCMS-Berichten, diese sind den verantwortlichen Personen zugänglich. • Es existiert ein abgestimmtes Revisionsprogramm, das den Anforderungen des BSI-Stan- dards 200-4 entspricht. PA 3.2: • Die Inhalte der Berichterstat- tung entsprechen vollständig den Anforderungen des BSI- Standards 200-4. • Die verantwortlichen Mitarbeiter besitzen nachweislich Kompe- tenzen in der Durchführung von   | • Finden regelmäßig (nach vorge- gebenem Intervall) Berichte an die Leitungsebene statt? • Ist der Aufbau des BCMS-Be- richts standardisiert und ent- spricht dieser den Anforderun- gen des BSI-Standards 200-4? • Existieren abgestimmte Vorga- ben und Templates für die Er- stellung von BCMS-Berichten? • Existiert ein abgestimmtes Revi- sionsprogramm, das den Anfor- derungen des BSI-Standards 200-4 entspricht? • Besitzen die Mitarbeiter nach- weislich Kompetenzen hinsicht- lich der Durchführung von Über- prüfungen?   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4: Gesteuert        | BCM-Überprüfungen PA 4.1: • Die Durchführung von BCMS- Audits wird mit Hilfe von Kenn- zahlen überprüft (z.B. terminge- rechte Umsetzung der Maßnah- men, Abdeckungsgrad der Au- ditierungen). PA 4.2: • Die Einhaltung von Berichtsin- tervallen wird mit Hilfe von Kennzahlen überprüft.                                                                                                                                                                                                                                                                                                                                                                                    | • Wird die regelmäßige Durchfüh- rung von BCMS-Überprüfungen mit Hilfe von Kennzahlen über- prüft (z.B. termingerechte Um- setzung der Maßnahmen, Ab- deckungsgrad der Überprüfun- gen)? • Wird die Einhaltung von Be- richtsintervallen mit Hilfe von Kennzahlen überprüft?                                                                                                                                                                                                                                                            |

<!-- page: 93 -->

| PA 5.1:                                                                                                                                                                                                                                                                                                                                                    | • Wird die Durchführung von BCMS-Überprüfungen kontinu- ierlich verbessert? • Führen BCMS-Überprüfungen zu einer Verbesserung der Kon- zepte, Maßnahmen und Pro- zesse des BCMS? • Wird die Planung, Durchführung und Nachbereitung von Über- prüfungen durch ein GRC Tool unterstützt, das Synergieeffekte zu weiteren Managementsyste-   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| • BCMS-Überprüfungen führen nachweislich zu einer Verbes- serung der Konzepte, Prozesse und Maßnahmen des BCMS. • Die Durchführung von BCMS- Überprüfungen wird kontinuier- lich verbessert. PA 5.2: • Die Planung und die Durchfüh- rung von BCMS-Überprüfungen wird durch ein GRC Tool unter- stützt, das Synergieeffekte zu weiteren Managementsystemen |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                            | men ermöglicht?                                                                                                                                                                                                                                                                                                                            |
| ermöglicht.                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                            |

Quelle: Eigene Darstellung

Tabelle 16: LP.8: Reifegradstufen und spezifische Fragestellungen

<!-- page: 94 -->

## 3.2.3.11 LP.9 Kontinuierliche Verbesserung

Der Lifecycle-Prozess LP.9 beinhaltet die Identifikation und Umsetzung von Korrekturbedarfen und Verbesserungsmöglichkeiten für das BCMS. Tabelle 17 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen des Prozesses.

<!-- page: 95 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Korrekturbedarfe und Verbes- serungspotentiale für das BCMS werden anlassbezogen erhoben.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | • Werden Korrekturbedarfe und Verbesserungspotentiale an- lassbezogen erhoben?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 2: Wiederholbar  | PA 2.1: • Die Vorgehensweise zur Identi- fikation von Verbesserungs- maßnahmen ist in Ansätzen vor- gegeben. • Eine verantwortliche Person für die kontinuierliche Verbesse- rung des BCMS wurde definiert, Beteiligte des BCMS engagie- ren sich aktiv an der kontinuier- lichen Verbesserung des BCMS. • Verbesserungsmaßnahmen werden gelegentlich identifiziert. PA 2.2: • Es existieren Arbeitshilfen und Templates für die Identifikation von Verbesserungspotentialen. • Austauschveranstaltungen zur Identifikation von Verbesse- rungspotentialen für das BCMS (z.B. Lessons Learned Veran- staltungen werden gelegentlich durchgeführt. | • Wurde eine Vorgehensweise zur Identifikation von Verbesse- rungspotentialen im Ansatz de- finiert? • Wurde eine verantwortliche Per- son für die kontinuierliche Ver- besserung des BCMS definiert? Beteiligen sich die BCMS-Ver- antwortlichen aktiv an der konti- nuierlichen Verbesserung des BCMS? • Werden Verbesserungsmaß- nahmen gelegentlich identifi- ziert? • Existieren Arbeitshilfen und Templates zur Identifikation von Verbesserungspotentialen? • Finden gelegentlich Austausch- veranstaltungen (z.B. Lessons Learned) zur Identifikation von Verbesserungspotentialen für das BCMS statt? |

<!-- page: 96 -->

| 3: Standardisiert   | PA 3.1: • Die Institutionsleitung wird aktiv und regelmäßig in den Verbes- serungsprozess für das BCMS eingebunden. • Die Identifikation und Bewer- tung von Verbesserungsmaß- nahmen erfolgt auf Basis der Anforderungen des BSI-Stan- dards 200-4. • Verbesserungsmaßnahmen für das BCMS werden dokumen- tiert, terminiert und priorisiert. PA 3.2: • Auf Basis der identifizierten Ver- besserungsmaßnahmen wer- den BCM-Maßnahmenpläne er- stellt. • Die Umsetzung der Maßnah- men des BCM-Maßnahmen- plans wird kontrolliert. • Verantwortlichkeiten für die Um- setzung von Verbesserungs-   | • Wird die Institutionsleitung aktiv in den Verbesserungsprozess für das BCMS eingebunden? • Erfolgt die Identifikation und Be- wertung von Verbesserungs- maßnahmen auf Basis der An- forderungen des BSI-Standards 200-4? • Werden Verbesserungsmaß- nahmen für das BCMS doku- mentiert, terminiert und priori- siert? • Werden BCM-Maßnahmen- pläne auf Basis der identifizier- ten Verbesserungsmaßnahmen erstellt? • Wird die Umsetzung der Maß- nahmen des BCM-Maßnah- menplans kontrolliert, und sind hierzu Verantwortlichkeiten fest- gelegt?   |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4: Gesteuert        | PA 4.1: • Die termingerechte Umsetzung von Verbesserungsmaßnah- men wird gesteuert und kontrol- liert. PA 4.2: • Erkenntnisse aus Übungen, Tests und Audits fließen in die kontinuierliche Verbesserung                                                                                                                                                                                                                                                                                                                                                                                            | • Wird die termingerechte Umset- zung von Verbesserungsmaß- nahmen gesteuert und kontrol- liert? • Fließen Erkenntnisse aus Übun- gen, Tests und Audits in die kontinuierliche Verbesserung des BCMS ein?                                                                                                                                                                                                                                                                                                                                                |
| 5: Optimierend      | PA 5.1: • Verbesserungsmaßnahmen für Konzepte, Prozesse und Ver- fahren des BCMS werden durch die verantwortlichen Mitarbeiter selbstständig erhoben und um- gesetzt.                                                                                                                                                                                                                                                                                                                                                                                                                              | • Werden Verbesserungsmaß- nahmen für Konzepte, Prozesse und Verfahren des BCMS durch die verantwortlichen Mitarbeiter selbstständig erhoben und um- gesetzt?                                                                                                                                                                                                                                                                                                                                                                                            |

Quelle: Eigene Darstellung

Tabelle 17: LP.9: Reifegradstufen und spezifische Fragestellungen

<!-- page: 97 -->

## 3.2.3.12 SP.1 Dokumentenlenkung

Der Support-Prozess SP.1 verfolgt das Ziel, eine angemessene Dokumentenlenkung für alle Dokumente des BCMS zu gewährleisten. Dies beinhaltet die Einhaltung  des  Dokumentenlebenszyklus  für  alle  Dokumente  im  BCMS.  Tabelle  18 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen des Prozesses.

<!-- page: 98 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Dokumenten-Lebenszyklus für die Dokumente des BCMS ist grob definiert. • BCMS-Dokumente werden an- lassbezogen aktualisiert.                                                                                                                                                                                                                                                                                                                                      | • Wurde der Dokumenten-Le- benszyklus für die Dokumente des BCMS grob definiert? • Werden die Dokumente des BCMS anlassbezogen aktuali- siert?                                                                                                                                                                                                                                  |
| 2: Wiederholbar  | PA 2.1: • Es existieren Vorgaben für die Ausgestaltung von BCMS-Do- kumenten (z.B. Dokumentenin- formationen, Schutzbedarfe etc.). • Die Vorgaben für die Ausgestal- tung von BCMS-Dokumenten entsprechen im Ansatz dem Do- kumentenlebenszyklus. • BCMS-Dokumente werden ge- legentlich aktualisiert. PA 2.2: • Die Dokumentenhierarchie für Dokumente des BCMS wurde definiert. • Verantwortlichkeiten für die un- terschiedlichen BCMS-Doku- mente werden identifiziert. | • Existieren Vorgaben für die Ausgestaltung von BCMS-Do- kumenten? • Entsprechen diese Vorgaben dem definierten Ansatz im Do- kumentenlebenszyklus? • Werden die Dokumente des BCMS gelegentlich aktualisiert? • Wurde eine Dokumentenhierar- chie für die Dokumente des BCMS definiert? • Wurden Verantwortlichkeiten für die unterschiedlichen BCMS- Dokumente identifiziert? |

<!-- page: 99 -->

| 3: Standardisiert   | PA 3.1: • Es existieren alle gemäß BSI- Standard 200-4 geforderten Do- kumente des BCMS. • Die BCMS-Dokumente werden regelmäßig (in definierten Inter- vallen) aktualisiert. • Die BCMS Dokumente entspre- chen vollständig den Vorgaben des Dokumentenlebenszyklus der Organisation, werden durch das Qualitätsmanagement ge- steuert und erfüllen die Anforde- rungen des BSI-Standards 200- 4. PA 3.2: • BCMS-Dokumente sind organi- sationsweit den relevanten Ziel- gruppen bekannt (beispiels- weise durch Veröffentlichung im Intranet). • Verantwortlichkeiten für die BCMS-Dokumente sind festge-   | • Existieren alle gemäß BSI-Stan- dard 200-4 geforderten Doku- mente des BCMS? • Werden die BCMS-Dokumente regelmäßig in fest definierten In- tervallen aktualisiert? • Entsprechen die BCMS-Doku- mente vollständig den Vorga- ben des Dokumentenlebens- zyklus der Organisation und werden diese durch das Quali- tätsmanagement gesteuert? • Sind die BCMS-Dokumente or- ganisationsweit den relevanten Zielgruppen bekannt? • Wurden Verantwortlichkeiten für die jeweiligen BCMS-Doku- mente festgelegt?   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4: Gesteuert        | legt und bekannt. PA 4.1: • Die Aktualisierung von BCMS- Dokumenten wird regelmäßig überprüft (beispielsweise in ei- ner Dokumentenmatrix). • Änderungsbedarf an BCMS-Do- kumenten wird zeitnah identifi- ziert, veraltete BCMS-Doku- mente werden durch neue Ver- sionen ersetzt. PA 4.2: • Notwendige Änderungen an BCMS-Dokumenten werden zeitnah eingearbeitet.                                                                                                                                                                                                                                          | • Wird die Aktualisierung von BCMS-Dokumenten regelmä- ßig geprüft (beispielsweise in ei- ner Dokumentenmatrix)? • Wird der Änderungsbedarf an BCMS-Dokumenten zeitnah identifiziert und werden notwen- dige Änderungen eingearbeitet? • Werden die Inhalte der BCMS- Dokumente regelmäßig mit den Anforderungen des BSI-Stan- dards 200-4 abgeglichen?                                                                                                                                                         |

<!-- page: 100 -->

| 5: Optimierend   | PA 5.1: • Die Inhalte der BCMS-Doku- mente werden regelmäßig mit den Anforderungen des BSI- Standards 200-4 abgeglichen. • Verbesserungspotentiale für BCMS-Dokumente werden identifiziert und eingearbeitet. PA 5.2: • Die Dokumentation und Ablage von BCMS Dokumenten erfolgt in einem zentral genutzten GRC Tool.   | • Werden die Inhalte der BCMS- Dokumente regelmäßig mit den Anforderungen des BSI-Stan- dards 200-4 abgeglichen? • Werden Verbesserungspotenti- ale für BCMS-Dokumente iden- tifiziert und eingearbeitet? • Erfolgen die Dokumentation und Ablage von BCMS-Dokumenten in einem zentral genutzten GRC Tool?   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Quelle: Eigene Darstellung

Tabelle 18: SP.1: Reifegradstufen und spezifische Fragestellungen

<!-- page: 101 -->

## 3.2.3.13 SP.2 BCM-Aufbauorganisation

Der Support-Prozess SP.2 verfolgt das Ziel, die Rollen und Zuständigkeiten für das BCMS festzulegen und bekanntzumachen. Tabelle 19 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen des Prozesses.

<!-- page: 102 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Einer Person wurde (ggf. infor- mell) die Verantwortung für das BCMS erteilt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | • Wurde (ggf. informell) einer Per- son die Verantwortung für das BCMS übertragen?                                                                                                                                                                                                                                                                                                                                                                             |
| 2: Wiederholbar  | PA 2.1: • Ein BCM-Beauftragter wurde benannt. • Der Ressourcenbedarf für das BCMS wurde identifiziert. • Erforderliche Rollen für die BCM Aufbauorganisation wurden identifiziert. • Es existieren dokumentierte Überlegungen für den Aufbau der BCM Organisation (z.B. grob definierte Aufgaben, Rol- lenbeschreibungen etc.). PA 2.2: • Berichtswege an die Leitungs- ebene sind festgelegt und wer- den gelegentlich wahrgenom- men. • Der BCM-Beauftragte besitzt nachweislich die notwendige fachliche Eignung (beispiels- weise durch Schulungen und Trainings). | • Wurde ein BCM-Beauftragter benannt und besitzt dieser nachweislich die notwendige fachliche Eignung (beispiels- weise durch Schulungen und Trainings)? • Wurden der Ressourcenbedarf und die erforderlichen Rollen für das BCMS identifiziert? • Existieren dokumentierte Über- legungen für den Aufbau der BCM-Organisation? • Sind die Berichtswege der BCM-Organisation an die Lei- tungsebene festgelegt und wer- den diese gelegentlich wahrge- nommen? |

<!-- page: 103 -->

| 3: Standardisiert   | PA 3.1: • Der BCM-Beauftragte ist formell bestellt und durch die Organisa- tionsleitung freigegeben. • Die Ressourcen der BCM-Auf- bauorganisation entsprechen dem identifizierten Bedarf und sind in einem Organisationskon- zept dokumentiert (ggf. Be- standteil des Notfallvorsorge- konzepts). • Allen Rollen (inklusive Vertreter) sind die dazugehörigen Aufga- ben, Verantwortlichkeiten und Befugnisse zugewiesen und im Geschäftsverteilungsplan doku- mentiert. PA 3.2: • Die gemäß BSI-Standard 200-4 geforderten Rollen der BCM Or- ganisation sind besetzt. • Alle Rollen der BCM-Organisa- tion werden für die Wahrneh- mung ihrer Rollen ausgebildet und besitzen die notwendige fachliche Eignung (Beispiels- weise durch Schulungen und Trainings).   | • Wurde ein BCM-Beauftragter durch die Institutionsleitung for- mell bestellt? • Entsprechen die Ressourcen der BCM-Organisation dem identifizierten Bedarf? • Sind die Rollen der BCM-Orga- nisation in einem Organisations- konzept dokumentiert (ggf. als Bestandteil des Notfallvorsorge- konzepts)? • Sind allen Rollen der BCM-Or- ganisation, die dazugehörigen Aufgaben, Verantwortlichkeiten und Befugnisse zugewiesen, und sind diese im Geschäftsver- teilungsplan dokumentiert? • Sind alle gemäß BSI-Standard 200-4 geforderten Rollen der BCM-Organisation besetzt und werden diese hinsichtlich der Wahrnehmung ihrer Rollen aus- gebildet?   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- page: 104 -->

| 4: Gesteuert   | PA 4.1: • Die Effizienz der BCM-Organi- sation wird mithilfe von Kenn- zahlen überprüft (z.B. Anzahl der Abstimmungen, Dauer der Entscheidungen). • Jedem Mitarbeiter der Organi- sation sind die Ansprechpartner für das BCMS bekannt (bei- spielsweise durch die Veröffent- lichung im Intranet). PA 4.2: • Die Aktualität und Angemessen- heit des BCM-Organisations- konzepts wird regelmäßig über- prüft. • Alle anfallenden Aufgaben der BCM-Organisation werden durch den BCMB gesteuert und verteilt.   | • Wird die Effizienz der BCM-Or- ganisation mithilfe von Kenn- zahlen überprüft (z.B. Anzahl der Abstimmungen, Dauer der Entscheidungen)? • Sind jedem Mitarbeiter der Or- ganisation die Ansprechpartner für das BCMS bekannt (bei- spielsweise durch die Veröffent- lichung im Intranet)? • Werden die Aktualität und An- gemessenheit des BCM-Orga- nisationskonzepts regelmäßig überprüft? • Werden die anfallenden Aufga- ben der BCM-Organisation durch den BCMB gesteuert und verteilt?   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5: Optimierend | PA 5.1: • Die BCM-Organisation wird re- gelmäßig an sich ändernde Rahmenbedingungen und An- forderungen angepasst. • Die Leitungsebene hinterfragt regelmäßig die Angemessen- heit der Aufbauorganisation für das BCMS; notwendige Opti- mierungsmaßnahmen werden zeitnah eingeleitet. PA 5.2: • Eine Matrix für die BCMS-Auf- bauorganisation wurde erstellt, und die Rollenzuweisung wurde derart realisiert, dass keine Inte- ressenskonflikte bestehen.                                                     | • Wird die BCM-Organisation re- gelmäßig an die sich ändernden Rahmenbedingungen ange- passt? • Hinterfragt die Leitungsebene regelmäßig die Angemessen- heit der Aufbauorganisation für das BCMS? Werden notwen- dige Optimierungsmaßnahmen zeitnah eingeleitet?                                                                                                                                                                                                                                |

Quelle: Eigene Darstellung

Tabelle 19: SP.2: Reifegradstufen und spezifische Fragestellungen

<!-- page: 105 -->

## 3.2.3.14 SP.3 Schulung und Sensibilisierung

Der Support-Prozess SP.3 verfolgt das Ziel, die Mitarbeiter der Institution in Bezug auf das BCMS angemessen zu schulen und zu sensibilisieren. Tabelle 20 zeigt die Zusammensetzung der unterschiedlichen Reifegradstufen sowie die dazugehörigen spezifischen Fragestellungen des Prozesses.

<!-- page: 106 -->

| Reifegradstufe   | Prozess-Attribute (PA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Spezifische Fragestellung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1: Durchgeführt  | PA 1.1: • Schulungs- und Sensibilisie- rungsmaßnahmen finden an- lassbezogen statt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | • Finden Schulungs- und Sensibi- lisierungsmaßnahmen anlass- bezogen statt?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 2: Wiederholbar  | PA 2.1: • Es existieren rudimentäre Über- legungen für die Ausgestaltung von Schulungs- und Sensibili- sierungsmaßnahmen für das BCMS. • Die Planung von einzelnen Schulungs- und Sensibilisie- rungsmaßnahmen erfolgt struk- turiert. • In der BCM-Organisation wurde ein Verantwortlicher für die Pla- nung von Schulungs- und Sen- sibilisierungsmaßnahmen be- nannt. • Schulungs- und Sensibilisie- rungsmaßnahmen finden gele- gentlich statt. PA 2.2: • Schulungsbedarf für die rele- vanten Rollen der BCM Organi- sation wurde identifiziert. • Mitarbeiter der BCM Organisa- tion werden gelegentlich für die Wahrnehmung ihrer Rolle ge- schult. • Mitarbeiter werden gelegentlich für BCM-relevante Inhalte sen- sibilisiert. | • Finden Schulungs- und Sensibi- lisierungsmaßnahmen gele- gentlich statt? • Existieren rudimentäre Überle- gungen für die Ausgestaltung von Schulungs- und Sensibili- sierungsmaßnahmen? Erfolgt die Planung dieser Maßnahmen strukturiert? • Wurde in der BCM-Organisation ein Verantwortlicher für die Pla- nung von Schulungs- und Sen- sibilisierungsmaßnahmen be- nannt? • Wurde der Schulungsbedarf für die relevanten Rollen der BCM- Organisation identifiziert? Wer- den die Mitarbeiter der BCM-Or- ganisation gelegentlich für die Wahrnehmung ihrer Rolle ge- schult? • Werden die Mitarbeiter in der In- stitution gelegentlich für BCM- relevante Inhalte sensibilisiert? |

<!-- page: 107 -->

| 3: Standardisiert   | PA 3.1: • Es existiert ein Schulungs- und Sensibilisierungskonzept für das BCMS, das die Anforderun- gen des BSI-Standards 200-4 erfüllt. • Alle Schulungs- und Sensibili- sierungsmaßnahmen werden gemäß den Inhalten des Schu- lungs- und Sensibilisierungs- konzepts geplant und regelmä- ßig durchgeführt. • Es existiert eine Jahres Schu- lungsplanung (Schulungs- und Sensibilisierungsprogramm). PA 3.2: • Alle Mitarbeiter der BCM-Orga- nisation werden entsprechend des Schulungsbedarfs in ihrer Rolle ausgebildet. • Die Inhalte der Schulungs- und Sensibilisierungsmaßnahmen entsprechen den Anforderun- gen des BSI-Standards 200-4. • Die Führungsebene fördert aktiv das Bewusstsein für das BCMS.   | • Existiert ein Schulungs- und Sensibilisierungskonzept (ggf. Bestandteil des Notfallvorsorge- konzepts), das die Anforderun- gen des BSI-Standards 200-4 erfüllt? • Werden alle Schulungs- und Sensibilisierungsmaßnahmen gemäß den Vorgaben des Schulungs- und Sensibilisie- rungskonzepts geplant und durchgeführt? • Existiert eine Jahres-Schu- lungsplanung? • Werden alle Mitarbeiter der BCM-Organisation entspre- chend des Schulungsbedarfs ausgebildet? • Entsprechen die Inhalte der Schulungs- und Sensibilisie- rungsmaßnahmen den Anforde- rungen des BSI-Standards 200- 4? • Fördert die Leitungsebene der Institution aktiv das Bewusst- sein für das BCMS?   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4: Gesteuert        | PA 4.1: • Das Schulungs- und Sensibili- sierungsprogramm wird jährlich geplant. • Die Einhaltung der Schulungs- und Sensibilisierungsplanung wird kontrolliert. PA 4.2: • Schulungs- und Sensibilisie- rungsmaßnahmen werden durch Kennzahlen gesteuert (z.B. Abdeckungsgrad und Ef- fektivität von Awareness Maß- nahmen). • Der Erfolg von Schulungs- und Sensibilisierungsmaßnahmen wird regelmäßig kontrolliert.                                                                                                                                                                                                                                                                                                   | • Wird das Schulungs- und Sensi- bilisierungsprogramm jährlich geplant (Jahresplanung)? • Wird die Einhaltung der Jahres- planung kontrolliert? • Werden Schulungs- und Sensi- bilisierungsmaßnahmen durch Kennzahlen gesteuert? • Wird der Erfolg von Schulungs- und Sensibilisierungsmaßnah- men kontrolliert?                                                                                                                                                                                                                                                                                                                                                               |

<!-- page: 108 -->

| 5: Optimierend   | PA 5.1: • Schulungs- und Sensibilisie- rungsmaßnahmen werden kon- tinuierlich an sich ändernde Rahmenbedingungen ange- passt. • Rückmeldungen durch Teilneh- mer sorgen für eine kontinuierli- che Optimierung von Schu- lungs- und Sensibilisierungs- maßnahmen.   | • Werden die Schulungs- und Sensibilisierungsmaßnahmen kontinuierlich an die sich än- dernden Rahmenbedingungen angepasst? • Werden die Schulungs- und Sensibilisierungsmaßnahmen auf Basis der Rückmeldung von Teilnehmern kontinuierlich opti- miert?   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Quelle: Eigene Darstellung

Tabelle 20: SP.3: Reifegradstufen und spezifische Fragestellungen

<!-- page: 109 -->

## 3.3  Entwicklung des Erhebungstools (Prototyp)

In den vorhergehenden Abschnitten der Arbeit wurden die Inhalte des Reifegradmodells für den BSI-Standard 200-4 konzipiert. Reifegradmodelle können jedoch mit der Zeit veralten und müssen kontinuierlich aktualisiert werden. 148  Durch die derzeitige CD-Version des BSI-Standards 200-4 ist dies insbesondere für dieses Reifegradmodell von Bedeutung. Zur Vereinfachung der Modellpflege wurde folglich  ein  excel-basiertes  Erhebungstool  erstellt.  Nachfolgend  werden  zunächst dessen  Anwendungslogik  sowie  das  zugrundeliegende  Datenmodell  erläutert. Mithilfe von Screenshots werden zudem die einzelnen Tabellenblätter detailliert exponiert.  Die Entwicklung des Erhebungstools erfolgte anhand von drei Teilschritten:

Schritt 1: Entwicklung des Grundgerüsts des Erhebungstools

Im ersten Schritt wurde das Grundgerüst des Erhebungstools skizziert. Ziel war es hierbei, dass dessen Struktur inhaltlich synchron zur Struktur Reifegradmodells aufgebaut ist.

Schritt 2: Festlegung der benötigten Funktionalitäten

Die Zusammensetzung der Reifegrade wurde durch das zugrundeliegende Basismodell vorgegeben. Im zweiten Schritt erfolgt daher die Festlegung der benötigten  Funktionalitäten.  Dies  beinhaltet  die  Hinterlegung der  notwendigen  Formeln zur Berechnung der jeweiligen Reifegrade anhand des vorgegebenen Basismodells.

Schritt 3: Befüllung der Inhalte

Im dritten Schritt wurde das Erhebungstool mit den erhobenen Inhalten des Reifegradmodells befüllt.

Der Entwicklung des Erhebungstools liegt die Prämisse zugrunde, dass:

- das Erhebungstool einfach zu bedienen und ohne externe Unterstützung ausfüllbar sowie
- das Erhebungstool für andere Reifegradmodelle wiederverwendbar ist.

148  Vgl. Bensiek, T., 2013, S. 112

<!-- page: 110 -->

## 3.3.1 Anwendungslogik

Im folgenden  Abschnitt  wird  der  logische  Ablauf  einer  Reifegraderhebung  mit Hilfe des excel-basierten Erhebungstools beschrieben. Das Erhebungstool lässt sich in drei logische Teilbereiche aufteilen:

- Erläuterungsbereich,
- Erhebungsbereich sowie
- Dashboard.

Der Erläuterungsbereich dient dazu, Anwendern die inhaltlichen Aspekte des Erhebungstools verständlich zu erläutern.  In  einzelnen  Tabellenblättern  erfolgen zunächst eine Einführung in das Thema (inklusive Darstellung des PRM) sowie eine Erläuterung der Ausfüllhinweise und der Erhebungsbögen. Im Erhebungsbereich erfolgt die Identifikation der Reifegrade anhand spezifischer Fragestellungen. Die einzelnen Erhebungsbögen sind separat strukturiert und lassen sich unabhängig voneinander ausfüllen. Das Dashboard visualisiert die Ergebnisse der Reifegraderhebung. Abbildung 19 visualisiert die Anwendungslogik des Erhebungstools anhand von drei Teilschritten.

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 19: Erläuterung der Anwendungslogik des Erhebungstools

<!-- page: 111 -->

## 3.3.2 Datenmodell

Im  Folgenden  wird  das  zugrundeliegende  Datenmodell  des  Erhebungstools schematisch  dargestellt  und  erläutert.  Das  Datenmodell  beinhaltet  14  Erhebungsbögen. Diese können je Prozess voneinander unabhängig ausgefüllt werden. Im Erhebungstool existieren daher zwei Entitätsklassen: die Erhebungsbögen (Anzahl = 14) sowie das Dashboard (Anzahl = 1). Die Erhebungsbögen beinhalten spezifische Fragestellungen, Antwortmöglichkeiten und einen Ist-Reifegrad je Prozess. Die ermittelten Ist-Reifegrade je Prozess werden im Dashboard konsolidiert und mit den Soll-Reifegraden abgeglichen. Abbildung 20 visualisiert das Datenmodell des Erhebungstools in einem vereinfachten Entity-Relationship (ER)-Modell.

Quelle: Eigene Darstellung

<!-- image -->

Abbildung 20: Vereinfachtes ER-Modell des Erhebungstools

Der Datenfluss des Erhebungstools findet auf zwei Ebenen statt:

- Prozess-Ebene sowie
- Prozess-Attribut-Ebene.

Wie bereits erläutert, existiert für jeden betrachteten Prozess ein eigener Erhebungsbogen. Die Ist-Reifegrade werden demnach für jeden Prozess einzeln ermittelt. Die Ermittlung der Reifegrade erfolgt - wie in Abschnitt 3.2.2 erläutert - durch PA. Für jedes PA werden spezifische Fragestellungen definiert. Die Antwortmöglichkeiten je spezifischer Fragestellung ergeben schlussendlich den Reifegrad je Prozess. Die Ergebnisse aller erhobenen Reifegrade werden im Dashboard  konsolidiert.  Abbildung  21  visualisiert  das  vereinfachte  Datenflussdiagramm des Erhebungstools.

Quelle: Eigene Darstellung

<!-- image -->

Abbildung 21: Vereinfachtes Datenflussdiagramm des Erhebungstools

<!-- page: 112 -->

## 3.3.3 Erläuterung der Tabellenblätter

Die Tabellenblätter des Erhebungstools unterteilen sich in erläuternde Tabellenblätter und Erhebungsbögen. Die erläuternden Tabellenblätter dienen der methodischen Beschreibung des Erhebungstools, der Visualisierung der Ergebnisse sowie der inhaltlichen Erläuterung des Reifegradmodells. Die Erhebungsbögen dienen der Identifikation der Reifegrade der einzelnen Teilprozesse anhand spezifischer  Fragestellungen.  Die  Struktur  der  Erhebungsbögen  orientiert  sich  an dem Prozess-Referenzmodell (PRM). Abbildung 22 zeigt das Deckblatt des Erhebungstools sowie die Struktur der einzelnen Tabellenblätter. Nachfolgend wird der Zweck der einzelnen Tabellenblätter näher erläutert.

Quelle: Eigene Darstellung

<!-- image -->

Abbildung 22: Deckblatt des Erhebungstools

Beim Start des Erhebungstools wird zunächst das Tabellenblatt Deckblatt angezeigt. Hier befinden sich der Titel und die Metadaten des Erhebungstools.

<!-- page: 113 -->

Im Tabellenblatt Einführung wird das zugrundeliegende Prozess-Referenzmodell erläutert und ein Überblick über die unterschiedlichen Prozessbereiche definiert (Abbildung 23).

Quelle: Eigene Darstellung

<!-- image -->

Abbildung 23: Tabellenblatt Einführung des Erhebungstools

Die  Management(Blau) ,  Lifecycle(Orange) und  Support-Prozesse (Grün) wurden hierbei in unterschiedlichen Farben markiert.

<!-- page: 114 -->

Das Tabellenblatt Dashboard liefert eine strukturierte Übersicht über die Ergebnisse der Reifegraderhebung in Form eines Spinnennetzdiagramms (Abbildung 24).

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 24: Tabellenblatt Dashboard des Erhebungstools

Zusätzlich wird dem Anwender die Möglichkeit gegeben, ein angestrebtes Zielniveau auszuwählen. Dieses orientiert sich an den Startmodellen des BSI-Standards 200-4 (Reaktiv-BCMS und Standard-BCMS). Die Zusammensetzung der Soll-Reifegrade ist in Abschnitt 3.2.2 detailliert erläutert. Je nach Auswahl ändern sich die jeweiligen Soll-Reifegrade im Spinnennetzdiagramm des Dashboards. Die Soll-Reifegrade sind schematisch zu verstehen und besitzen keine Verbindlichkeit hinsichtlich der vollständigen Umsetzung des Standards.

<!-- page: 115 -->

Das Tabellenblatt Ausfüllhinweise beschreibt die methodische Zusammensetzung von Reifegraden und erläutert dem Anwender das benötigte Hintergrundwissen.  Zusätzlich  werden  die  verwendeten  Schlüsselwörter  und  die  Antwortmöglichkeiten beschrieben (Abbildung 25).

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 25: Tabellenblatt Ausfüllhinweise des Erhebungstools

Das Tabellenblatt Erläuterung beschreibt den Aufbau der Erhebungsbögen. Es erläutert dem Anwender die Nutzung der einzelnen Erhebungsbögen. Zusätzlich werden hilfreiche Informationen mitgegeben, wie beispielsweise die Möglichkeit, sich im jeweiligen Erhebungsbogen zusätzliche Informationen anzeigen zu lassen (Abbildung 26).

<!-- page: 116 -->

Quelle: Eigene Darstellung

<!-- image -->

Abbildung 26: Tabellenblatt Erläuterung des Erhebungstools

Ab dem Tabellenblatt MP.1 beginnen die Erhebungsbögen (Abbildung 27). Jeder Teilprozess des Prozess-Referenzmodells hat ein eigenes Tabellenblatt und somit einen eigenen Erhebungsbogen. Insgesamt beinhaltet das Erhebungstool 14 Erhebungsbögen. Dies ermöglicht es dem Anwender, auch einzelne Prozesse zu betrachten.

Quelle: Eigene Darstellung

<!-- image -->

Abbildung 27: Erhebungsbögen des Erhebungstools am Beispiel des MP.1

<!-- page: 117 -->

Der Aufbau der Erhebungsbögen ist bewusst simpel gehalten, um Unklarheiten zu verhindern. Die Erhebungsbögen bestehen aus den folgenden Elementen:

- Prozesskürzel: Jeder Erhebungsbogen bezieht sich auf einen spezifischen Prozess des Prozess-Referenzwerks. Das jeweilige Kürzel sowie die dazugehörigen Informationen befinden sich im oberen Abschnitt der Erhebungsbögen. Um die Zuordnung zu erleichtern, ist das Prozesskürzel in der jeweils passenden Farbe (hier: blau) markiert.
- Reifegrad: Der ermittelte Reifegrad für den jeweiligen Prozess wird ebenfalls im oberen Abschnitt des Erhebungsbogens angezeigt. Er setzt sich aus den Antwortmöglichkeiten der spezifischen Fragestellungen zusammen.
- Kontrollfragen: Zu jedem Reifegrad werden spezifische Kontrollfragen gestellt.  Diese  basieren  auf  den  definierten  Prozess-Attributen  der  jeweiligen Reifegradstufe.
- Umsetzung: Um aussagekräftige Ergebnisse zu erhalten, sind die Antwortmöglichkeiten für die spezifischen Fragestellungen vordefiniert. Diese orientieren sich an den Vorgaben des Basismodells ISO/IEC 33020. Zusätzlich besteht die Möglichkeit, eine Frage mit 'nicht anwendbar' zu beantworten. Die Ergebnisse dieser Frage werden nicht gewertet, um das Endergebnis nicht zu verfälschen.
- Kommentar/Hinweis: Das Feld Kommentar/Hinweis ist ein Freitextfeld und ermöglicht dem Anwender, zusätzliche Kommentare zu dokumentieren (z.B. mögliche Umsetzungsmaßnahmen).

<!-- page: 118 -->

Weiterhin haben Anwender die Möglichkeit, sich im jeweiligen Erhebungsbogen zusätzliche Informationen, wie den Prozess-Steckbrief und die jeweiligen Prozess-Attribute der Reifegradstufe, anzeigen zu lassen. Abbildung 28 zeigt einen exemplarischen Prozesssteckbrief des Managementprozesses MP.1 .

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 28: Anzeigen von zusätzlichen Informationen am Beispiel des Erhebungsbogens MP.1

<!-- page: 119 -->

## 4  Evaluation des Reifegradmodells

## 4.1  Zielsetzung, Vorgehensweise und Teilnehmer der Evaluation

Der folgende Abschnitt beschreibt die Evaluation des Reifegradmodells für den BSI-Standard 200-4. Die Beurteilung soll einen Transfer der theoretischen Überlegungen in die Praxis ermöglichen und ist ein fester Bestandteil der Konzeption des Reifegradmodells. 149  Zudem ist die Evaluation des Reifegradmodells ein wesentlicher Aspekt zur Beantwortung der Forschungsfragen. Ihr Hauptziel ist es, zu  eruieren,  inwieweit  das  Reifegradmodell  Anwender  hinsichtlich  der  praktischen Umsetzung des BSI-Standards 200-4 unterstützt. Zusätzlich sollen durch die Bewertung Verbesserungspotentiale für das Reifegradmodell identifiziert wer-

den.

Die Evaluation wird anhand von semi-strukturierten Experteninterviews geführt. Nach Kühl et al. (2009) sollten Personen ein fachlich orientiertes Sonderwissen aufweisen können, um als Experte bezeichnet werden zu können. 150  Im Kontext dieser Arbeit werden folgende Kriterien für die Auswahl der Fachexperten definiert. Der Fachexperte:

- verfügt  über  mindestens  zwei  Jahre  Berufserfahrung  im  Themenfeld BCMS,
- arbeitet in einer Position,  die das Themenfeld BCMS verantwortet oder Schnittstellen zu diesem Thema hat,
- besitzt ein Verständnis über den BSI-Standard 200-4 und
- versteht sich als Anwender des BSI-Standards 200-4.

Den ausgewählten Fachexperten werden für die Durchführung der Evaluation zwei mögliche Optionen eingeräumt, die sich insbesondere im Zeitumfang unterscheiden. Da eine gemeinsame Erhebung mit einem Zeitumfang von bis zu 8 Stunden sehr ressourcenintensiv ist, ermöglicht die eigenständige Erhebung eine selbstständige Zeiteinteilung. Option 1 beinhaltet einen gemeinsamen Termin im Zeitumfang von 1 bis 2 Stunden. In dem Termin werden das Erhebungstool präsentiert und der grundlegende Ablauf der Anwendung erläutert. Im Nachgang des Termins wird das Erhebungstool zur eigenständigen Erhebung bereitgestellt. Option 2 beinhaltet eine gemeinsame Erhebung und Begutachtung des Reifegradmodells. Im Rahmen eines ganztägigen Workshops wird das Erhebungstool präsentiert und erläutert sowie gemeinsam zwischen Fachexperten und dem Autor erprobt. Die Option 1 birgt den Vorteil, dass das Erhebungstool in einem realistischen Anwendungsszenario erprobt wird. Sollte das Erhebungstool zukünftig offen zugänglich gemacht werden, ist die Option 1 demzufolge ein realistisches Anwendungsszenario.  Nachteil  dieser  Option  ist,  dass  Unklarheiten  im  Erhebungstool durch den Autor nicht erläutert werden können. Dies könnte beispielsweise zu einem falschen Verständnis einzelner Fragestellungen führen. Vorteile der Option 2 sind insbesondere, dass Unklarheiten im Rahmen des Termins direkt identifiziert und erläutert werden können. Nachteil der Option 2 ist, dass eine Erläuterung durch den Autor das Evaluationsergebnis beeinflussen könnte. Dies gilt insbesondere im Hinblick auf die Verständlichkeit des Erhebungstools (A2). Eine externe Unterstützung könnte einen positiven Einfluss auf die Verständlichkeit haben und somit das Stimmungsbild verzerren. Tabelle 21 zeigt die wesentlichen Merkmale der unterschiedlichen Optionen zur Erprobung des Reifegradmodells. Da das Erhebungstool unabhängig der ausgewählten Option in einem praktischen Umfeld erprobt wird,  sind die Ergebnisse vergleichbar. Festhalten lässt sich jedoch, dass Option 1 als das realistischere Anwendungsszenario gilt.

149  Vgl. Becker, J. et al., 2009, S. 258

150  Vgl. Kühl, S. et al., 2009, S. 33

<!-- page: 120 -->



<!-- page: 121 -->

| Options Art                   | Dauer des Ter- mins      | Ablauf des Termins                                                                                                                                                                   | Vor und Nachteile                                                                                                                                                                                                                                                                                       |
|-------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 - Eigen- ständige Erhebung  | Ca. 1 bis 2 Stunden      | • Vorstellung/Erläuterung der Methodik • Erläuterung des Erhe- bungstools • Bereitstellung des Erhe- bungstools inklusive des Evaluationsbogens                                      | Vorteil: • Erhebungstool wird aus tat- sächlicher Sicht der Anwender bewertet Nachteil: • Unklarheiten im Erhebungstool können nicht durch den Autor erläutert werden                                                                                                                                   |
| 2 - Ge- mein- same Er- hebung | Zwischen 4 und 8 Stunden | • Vorstellung/Erläuterung der Methodik • Erläuterung des Erhe- bungstools • Gemeinsame Erhebung der Reifegrade • Bereitstellung des Erhe- bungstools inklusive des Evaluationsbogens | Vorteil: • Fragestellungen können detail- liert erläutert werden • Unklarheiten können im Rah- men des Termins identifiziert werden Nachteil: • Erläuterung kann das Evalua- tionsergebnis beeinflussen (siehe Anforderung 2: Bedie- nung des Modells soll […] ohne externe Unterstützung möglich sein) |

Quelle: Eigene Darstellung

Tabelle 21: Optionen zur Erprobung des Reifegradmodels für den BSI-Standard 200-4 Im Anschluss an die gemeinsamen Termine mit den Fachexperten werden das Erhebungstool sowie der Bewertungsbogen zur Evaluation des Reifegradmodells bereitgestellt. Die Vorlage des Bewertungsbogens befindet sich im  Anhang V: Evaluationsbögen zur Bewertung des Reifegradmodells. Um einen möglichst objektiven Überblick über die Anwendbarkeit des Reifegradmodells zu erhalten, wurde Wert auf einen branchenübergreifenden Experten-

kreis gelegt. Die folgende Tabelle listet die Teilnehmer der Evaluation, die dazugehörige Branche sowie die Daten der durchgeführten Termine auf.

<!-- page: 122 -->

| Branche                                                | Organisation                                          | Fachexperte/n                                                                  | Option                 | Datum                                   |
|--------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------------------------------|------------------------|-----------------------------------------|
| IT (Softwareent- wicklung)                             | Optimal Sys- tems GmbH                                | Informationssi- cherheitsbeauf- tragter)                                       | Eigenständige Erhebung | 29. Juli 2021 von 11:00 bis 13:00 Uhr   |
| Gesundheit                                             | Vivantes - Netz- werk für Ge- sundheit GmbH           | Informationssi- cherheitsbeauf- tragter und Informationssi- cherheitsmana- ger | Gemeinsame Erhebung    | 02. August 2021 von 10:00 bis 14:30 Uhr |
| Handelsunter- nehmen, Schwerpunkt Lebensmittel- handel | [nicht öffentlich]                                    | Experte für Resilienz, BCM und Krisenma- nagement                              | Eigenständige Erhebung | 12. August 2021 von 10:30 bis 11:30 Uhr |
| Finanzen                                               | DKB Service GmbH                                      | /                                                                              | Eigenständige Erhebung | 19. August 2021 von 13:00 bis 15:00 Uhr |
| Öffentlicher Sektor                                    | Bundesamt für Sicherheit in der Informations- technik | Notfallbeauftrag- ter                                                          | Eigenständige Erhebung | 31. August 2021 von 09:00 bis 11:00 Uhr |

Quelle: Eigene Darstellung

Tabelle 22: Teilnehmer der Evaluation des Reifegradmodells

## 4.2  Evaluationskriterien

Um zu ermitteln, inwieweit das erstellte Reifegradmodell sowie das dazugehörige Erhebungstool Anwender bei der Umsetzung des BSI-Standards 200-4 unterstützen, wurden spezifische Evaluationskriterien definiert. Diese sollen es ermöglichen, den praktischen Nutzen des Reifegradmodells zu bestimmen. Die Grundlage für die Evaluationskriterien bilden die definierten Anforderungen an das Reifegradmodell (siehe Abschnitt 3.1.2). Dies ermöglicht eine Bewertung, inwieweit die definierten Anforderungen an das Reifegradmodell umgesetzt wurden. Die Evaluationskriterien des Reifegradmodells werden folglich wie folgt definiert:

<!-- page: 123 -->

| Anf.                 | Evaluationskriterium                                                                                                                                                                                                                                           | Definition   |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Urteilskraft         | • Das Reifegradmodell soll ein fundiertes Urteil über den Reifegrad des BCM gemäß BSI-Standard 200-4 in ei- ner bestimmten Institution ermöglichen. Durch das Rei- fegradmodell soll ein ganzheitlicher Überblick über den Umsetzungsstand des BCMS entstehen. | (A1)         |
| Verständlichkeit     | bar sein. Die Bedienung des Erhebungstools soll ohne                                                                                                                                                                                                           | (A2)         |
| Anwendbarkeit        | • Das Reifegradmodell soll für alle Institutionen unab- hängig ihrer Größe und Beschaffenheit anwendbar sein.                                                                                                                                                  | (A3)         |
| Empfehlungscharakter | spezifische Handlungsempfehlungen ermittelt werden                                                                                                                                                                                                             | (A4)         |

Quelle: Eigene Darstellung

Tabelle 23: Evaluationskriterien für das Reifegradmodell (basierend auf den Anforderungen an das Reiferadmodell)

Basierend auf den Evaluationskriterien für das Reifegradmodell wurden im Evaluationsbogen spezifische Aussagen zur Umsetzung der jeweiligen Anforderung aufgestellt (Abbildung 29).

Quelle: Eigene Darstellung

Abbildung 29: Auszug der Statements im Evaluationsbogen

Mithilfe  einer  5-Punkte-Likert-Skala 151   wurde  der  Grad  der  Zustimmung  des Fachexperten zur Umsetzung der jeweiligen Anforderung abgefragt. Zusätzlich wurde den Fachexperten die Möglichkeit für ein Freitextkommentar eingeräumt. Die vollständige Vorlage des Evaluationsbogens befindet sich im Anhang V: Evaluationsbögen zur Bewertung des Reifegradmodells.

151  Vgl. Bertram, D., 2006, S. 1

<!-- page: 124 -->

## 4.3  Ergebnisse der Evaluation

Ziel der Evaluation war es, die Anwendbarkeit des Reifegradmodells für den BSIStandard 200-4 in ausgewählten Organisationen zu verproben.  Im Folgenden werden die Rückmeldungen der Evaluation beschrieben und interpretiert. Zur Bewertung der Anwendbarkeit wird hierbei maßgeblich der Zustimmungsgrad (1 bis 5) hinsichtlich der ausgewählten Statements (S.) je Anforderung des Evaluationsbogens berücksichtigt. Abbildung 30 visualisiert detailliert das Gesamtergebnis der Rückmeldungen der Evaluationsteilnehmer. 152

Quelle: Eigene Darstellung

Abbildung 30: Gesamtübersicht der Evaluationsergebnisse

Abbildung  30  zeigt,  dass  die  Evaluationsteilnehmer  den  ausgewählten  Statements tendenziell zustimmen. Der Mittelwert aller Rückmeldungen beträgt 4,1. Im Gesamten stimmen alle Evaluationsteilnehmer demzufolge den ausgewählten Statements tendenziell zu. Tabelle 24 listet die Anzahl der Rückmeldungen je Zustimmungsgrad auf.

|   Wert | Zustimmungsgrad                   |   Anzahl |
|--------|-----------------------------------|----------|
|      5 | Stimme voll und ganz zu           |       12 |
|      4 | Stimme zu                         |       17 |
|      3 | Stimme weder zu noch lehne ich ab |        5 |
|      2 | Stimme nicht zu                   |        1 |
|      1 | Stimme überhaupt nicht zu         |        0 |

Quelle: Eigene Darstellung

Tabelle 24: Tabellarische Darstellung der Evaluationsergebnisse

152   Vgl.  Vorlage und Rückmeldung der Evaluationsbögen im Anhang V: Evaluationsbögen zur Bewertung des Reifegradmodells

<!-- page: 125 -->

Das folgende Balkendiagramm zeigt die Rückmeldungen je Anforderung der unterschiedlichen Evaluationsteilnehmer im Vergleich (Abbildung 31).

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 31: Evaluationsergebnisse im direkten Vergleich

Mit einem Mittelwert von 4,4 weist die Urteilskraft (A1) einen besonders hohen Zustimmungsgrad auf. Im direkten Vergleich zu den weiteren Anforderungen wird dieser daher am ehesten zugestimmt. Etwas weniger hoch wird die Anwendbarkeit (A3) mit 4,2 bewertet, dicht gefolgt von dem Empfehlungscharakter (A4) mit einem Wert von 4,1. Am schlechtesten bewertet, aber dennoch mit einer vergleichsweise hohen Bewertung ist die Verständlichkeit (A2) mit einem Mittelwert von 3,9. Der durchschnittliche Zustimmungsgrad je Anforderung ist in Abbildung 32 visualisiert.

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 32: Durchschnittlicher Zustimmungsgrad (Mittelwert) der Evaluation

<!-- page: 126 -->

Ergänzend zu den ausgewählten Statements im Evaluationsbogen wurde den Fachexperten die Möglichkeit eingeräumt, freie Anmerkungen zu ergänzen. Hierbei wurden vor allem die einfache Bedienung und die enthaltenen Erläuterungshinweise im Erhebungstool positiv hervorgehoben. 153  Jedoch  wurde auf die teilweise hohen Anforderungen zur Erlangung der Reifegradstufe 1 hingewiesen. 154 Weitere Kritikpunkte waren eine teilweise unklare bzw. nicht ausreichende Quellenangabe  im  Erhebungstool.  Als  Handlungsempfehlung  sollte  hierzu  -  dem Fachexperten nach zu urteilen - spezifischer herausgearbeitet werden, auf welchen Anforderungen die einzelnen Aussagen basieren. 155  Dies könnte ebenfalls den Empfehlungscharakter des Erhebungstools stärken. 156  Weiterhin wurde im Rahmen der Freitextanmerkungen auf die  granulare Analysetiefe des Modells hingewiesen. Nach Meinung des Fachexperten könnte dies 'ungeübte Anwender abschrecken' 157 . Zudem entspreche der Umfang des Modells nicht zwangsläufig einer 'schnellen [und] einfachen' 158  Reifegraderhebung. Weitere Anmerkungen nach zu urteilen lässt sich eine Reifegraderhebung mit Hilfe des Reifegradmodells effizient und ressourcenschonend durchführen. 159  Ebenfalls biete nach Meinung der Fachexperten der 'neutrale Aufbau' 160  einen sichtbaren Mehrwert für die evaluierte Organisation. Es sei jedoch aufgefallen, dass die Auswahlmöglichkeit 'Nicht anwendbar' 161  bei falscher Anwendung das Gesamtergebnis positiv verfälschen könnte.

153  Vgl. 'Evaluationsbogen Vivantes' im Anhang V

154  Vgl. 'Evaluationsbogen Vivantes' im Anhang V

155  Vgl. 'Evaluationsbogen Handelsunternehmen (nicht öffentlich)' im Anhang V

156  Vgl. 'Evaluationsbogen Handelsunternehmen (nicht öffentlich)' im Anhang V

157  Vgl. 'Evaluationsbogen Handelsunternehmen (nicht öffentlich)' im Anhang V

158  Vgl. 'Evaluationsbogen Handelsunternehmen (nicht öffentlich)' im Anhang V

159  Vgl. 'Evaluationsbogen DKB-Service' im Anhang V

160  Vgl. 'Evaluationsbogen DKB-Service' im Anhang V

161  Vgl. 'Evaluationsbogen DKB-Service' im Anhang V

<!-- page: 127 -->

## 5  Fazit

## 5.1  Konsolidierung der Ergebnisse

Die Aktualisierung des BSI-Standard 200-4 hat viele Neuerungen für Anwender des Standards mit sich gebracht. Zentrales Ziel dieser Arbeit war es, ein hilfreiches Instrument für Anwender im Umgang mit dem aktualisierten BSI-Standard zu erstellen. Zu Beginn der Thesis wurden die Ausgangslage, die Zielsetzung sowie die zugrundeliegende Problemstellung skizziert. Weiterhin erfolgte die Beschreibung der inhaltlichen Grundlagen, die für das Verständnis der Abhandlung von Bedeutung waren. Im Abschnitt 4 - dem Kernbestandteil der Arbeit - wurde das Reifegradmodell inhaltlich konzipiert. Nach der Auswahl einer geeigneten methodischen  Vorgehensweise  wurden  zunächst  konkrete  Anforderungen  an das Reifegradmodell definiert. In einer umfassenden Analyse bestehender BCM-Reifegradmodelle wurde festgestellt, dass keines der bestehenden Reifegradmodelle die Inhalte des BSI-Standards 200-4 adäquat abdeckt. Basierend auf einer kurzen Diskussion wurde ein geeignetes Basismodell ausgewählt und die Modellinhalte  entwickelt.  Zur  Entwicklung  der  Modellinhalte  gehört  die  Erstellung des PRM für den BSI-Standard 200-4, die Konzeption der unterschiedlichen Reifegradstufen des Reifegradmodells sowie die Entwicklung des Erhebungstools. Schlussendlich wurde im Rahmen einer Evaluation das Reifegradmodell an fünf ausgewählten  Organisationen  verprobt.  Ziel  der  Evaluation  war  es,  ein  Stimmungsbild über die praktische Anwendbarkeit des Reifegradmodells zu erhalten. Auf Basis der beschriebenen Ergebnisse der Ergebnisse der Arbeit werden nachfolgend die drei leitenden Forschungsfragen beantwortet:

Forschungsfrage 1: Was sind die zentralen Ziele und Fähigkeiten des BCMS auf der Basis des BSI-Standards 200-4, und wie können diese in ein messbares Modell überführt werden?

Zur Beantwortung dieser Forschungsfrage wurde zunächst das BCMS definiert und erläutert sowie der BSI-Standard 200-4 in der Entstehungsgeschichte des BCMS verortet. Zudem wurden der Aufbau und Anwendungszweck von Reifegradmodellen beschrieben. Als wesentliche Erkenntnis wurde festgestellt, dass sich Reifegradmodelle im Kontext des BCMS insbesondere für die Messung von Prozessen eignen. Um den BSI-Standard 200-4 demnach in ein messbares Modell überführen zu können, war ein PRM eine notwendige Grundvoraussetzung. Die zentralen Ziele und Fähigkeiten des BSI-Standards 200-4 wurden mithilfe der Statement-Tree-Methodik erhoben und unter Berücksichtigung des ausgewählten Basismodells in ein PRM überführt. Um die Struktur des Managementsystems angemessen abbilden zu können, wurde das PRM auf Grundlage der HLS für Managementsysteme konzipiert. Ein weiterer zentraler Beitrag zur Beantwortung der Forschungsfrage stellt die Identifikation und Strukturierung der Prozess-Attribute im PAM dar. Diese ermöglichen es, die zugrundeliegenden Inhalte des PRM entlang der inhaltlichen Anforderungen des ausgewählten Basismodells zu strukturieren.

<!-- page: 128 -->

Die Forschungsfrage 1 wurde somit durch die Identifikation von Zielen und Charakteristiken des BCMS und von Reifegradmodellen, der Erstellung des PRM unter Berücksichtigung der Statement-Tree-Methodik sowie der Ableitung der Reifegrade anhand des ausgewählten Basismodells beantwortet.

Forschungsfrage 2: Welche Rahmenbedingungen müssen bei der Entwicklung eines Reifegradmodells für den BSI-Standard 200-4 berücksichtigt werden?

Zur Beantwortung dieser Forschungsfrage wurden unterschiedliche Vorgehensmodelle zur Entwicklung von Reifegradmodellen beschrieben und bewertet. Auf Basis bestehender Vorgehensmodelle wurde eine geeignete methodische Vorgehensweise für den Kontext dieser Arbeit angepasst. Zusätzlich zu den theoretischen  Rahmenbedingungen  zur  Entwicklung  des  Reifegradmodells  wurden praktische Anforderungen definiert. Diese ermöglichten eine praxisnahe Erstellung des Reifegradmodells. Zur Bewertung einer möglichen Anpassung bereits bestehender BCM-Reifegradmodelle wurde ein komparativer Vergleich durchgeführt. Auf Basis der Erkenntnisse wurde eine geeignete Entwicklungsstrategie für das Reifegradmodell definiert und eine geeignete Modellbasis ausgewählt.

Die Forschungsfrage 2 wurde somit durch die Anpassung eines geeigneten Vorgehensmodells sowie die Ableitung geeigneter Anforderungen an das Reifegradmodell beantwortet. Die Ergebnisse der Forschungsfrage 2 sind zudem Grundlage für die dritte Forschungsfrage, die wie folgt lautet:

Forschungsfrage 3: In welchem Maße erfüllt das entwickelte Reifegradmodell die definierten Anforderungen?

Zur Beantwortung der Forschungsfrage erfolgte eine Evaluation des Reifegradmodells an fünf ausgewählten Organisationen unterschiedlicher Branchen. Zur Evaluation des Modells wurden Evaluationskriterien definiert. Als Evaluationskriterien dienten die in Forschungsfrage 2 definierten Anforderungen an das Reifegradmodell. Ziel der Evaluation war es, die praktische Anwendbarkeit des Reifegradmodells zu prüfen. Die Evaluation hat gezeigt, dass das Reifegradmodell die definierten Anforderungen größtenteils umgesetzt hat.

Zusammenfassend lässt sich konstatieren, dass die zentralen Annahmen der Arbeit bestätigt wurden. Die Evaluation des Reifegradmodells hat ergeben, dass die grundlegenden Anforderungen, die an das Reifegradmodell gestellt wurden, zu großen Teilen umgesetzt wurden. In Bezug auf die definierten Forschungsziele kann somit gesagt werden, dass diese grundsätzlich erreicht wurden und das Reifegradmodell eine hilfreiche Ergänzung zum BSI-Standard 200-4 ist. Die in vergleichbaren Arbeiten bereits identifizierte 'Gratwanderung' 162  zwischen den Vorstellungen des Autors und den Anforderungen der Anwender bei der Erstellung von Reifegradmodellen, kann im Rahmen dieser Arbeit als geglückt bezeichnet werden. Weder hinsichtlich der Detailtiefe noch der Breite des betrachteten Anwendungsbereichs wichen die Meinungen und Wünsche der Anwender stark vom derzeitigen Stand des Reifegradmodells ab. Dennoch konnten durch die Evaluation Verbesserungspotentiale für das Reifegradmodell identifiziert werden. So wurde in der praktischen Anwendung insbesondere das Delta zwischen den qualitativen Fragestellungen und den quantitativen Antwortmöglichkeiten ersichtlich. Insbesondere die fehlende Trennschärfe zwischen den Umsetzungsgraden 'in ein paar Fällen' und 'in den meisten Fällen' lässt Spielraum für Meinungen von Einzelpersonen und könnte hinderlich für eine objektive Reifegraderhebung sein.  Eine  Reifegradbeurteilung  im  Workshop-Charakter,  die  durch  mehrere Fachexperten durchgeführt wird, könnte dem entgegenwirken. Eine weitere Erkenntnis der Evaluation war es, dass die Anforderungen der Reifegradstufe 1 teils als relativ hoch angesehen wurden, was teilweise zu einem geringen Reifegrad geführt hat. Zurückzuführen ist dies auf den durch das Basismodell vorgegebenen kumulativen Aufbau der Reifegradstufen (siehe Anhang III: Aufbau der Reifegradstufen (gemäß ISO/IEC 33020)) sowie auf die vergleichsweise hohen Anforderungen des BSI-Standards 200-4. Eine genauere Ergänzung der zugrundeliegenden Quellen im Erhebungstool könnte zudem helfen, den Aufbau des Reifegradmodells transparenter zu gestalten. Zusätzlich ist zu betonen, dass das Reifegradmodell auf eine langfristige Nutzung abzielt. Ziel des Modells ist es, die Prozesse des BCMS nachhaltig zu verbessern. Erst durch eine langfristige Nutzung des Modells kann die Leistungsfähig des BCMS regelmäßig evaluiert und Verbesserungsmaßnahmen abgeleitet werden. Im Allgemeinen lassen die Ergebnisse der Evaluation auf eine hohe Nutzerakzeptanz schließen.

<!-- page: 129 -->

## 5.2  Ausblick

Die Entwicklung des Reifegradmodells für den BSI-Standard 200-4 sowie das damit einhergehende Erhebungstool schaffen eine konzeptionelle Grundlage für verschiedene Anschlusspunkte. Folgende Aspekte wären für mögliche Vertiefungen oder Erweiterungen des Reifegradmodells denkbar:

162  Vgl. Mettler, T., 2010, S.247

<!-- page: 130 -->

- Erweiterung des Evaluationskreises: Die Evaluation im Rahmen dieser Arbeit wurde insgesamt an fünf ausgewählten Organisationen durchgeführt. In intensiven bilateralen Terminen wurde das Reifegradmodell erläutert und den jeweiligen Fachexperten bereitgestellt. Um ein umfangreiches Bild über die praktische Einsetzbarkeit des Erhebungstools zu erlangen, könnte das Reifegradmodell im Rahmen einer Studie einer Vielzahl von Anwendern des BSI-Standards 200-4 zur Verfügung gestellt werden.
- Vertiefung  der  Evaluation: Zusätzlich  zur  bereits  erläuterten  Erweiterung des Evaluationskreises könnten die Evaluationen zukünftig vertieft werden. Dies könnte beispielsweise durch wiederholte Reifegraderhebungen mithilfe des Reifegradmodells über einen längeren Zeithorizont durchgeführt werden. Eine weitere Möglichkeit zur Vertiefung der Evaluation ist eine Analyse hinsichtlich eines optimalen Zielniveaus. Die zugrundeliegende Forschungsfrage könnte hierbei beispielsweise lauten, ab welcher Reifegradstufe ein optimales Kosten-Nutzen-Verhältnis eintritt.
- Professionalisierung  des  Erhebungstools: Das  Erhebungstool,  das  im Rahmen dieser Arbeit erstellt wurde, wurde lediglich zu Evaluationszwecken angefertigt. Wesentliche Funktionen, wie beispielsweise eine eigene Datenbank für historische Daten (z.B. vergangene Reifegrad-Erhebungen), sind in dem excel-basierten Erhebungstools nicht vorhanden. Die Evaluation hat gezeigt, dass eine grundsätzliche Akzeptanz für das Erhebungstool gegeben ist. In zukünftigen Arbeiten könnte das excel-basierte Erhebungstool professionalisiert werden, beispielsweise durch die Entwicklung einer eigenständigen Webanwendung. Diese könnte es zudem ermöglichen, das Reifegradmodell einer Vielzahl an Nutzern bereitzustellen.
- Erweiterung  der  Methodik  auf  weitere  Betrachtungsbereiche  des  ITGrundschutzes: Im Rahmen dieser Arbeit wurde ein Vorgehensmodell diskutiert und ausgewählt. Dieses wurde für die Bedürfnisse dieser Thesis konkretisiert. Um eine Wiederholbarkeit der Methodik zu gewährleisten, wurden die einzelnen Teilschritte zur Erstellung des Reifegradmodells detailliert dokumentiert. Auf Grundlage der vorliegenden Arbeit könnten Reifegradmodelle für weitere Standards des BSI (z.B. BSI-Standard 200-3) erstellt und erprobt werden.
- Detaillierung und Aktualisierung des Reifegradmodells: Das vorliegende Reifegradmodell basiert inhaltlich auf dem BSI-Standard 200-4 in der CD-Version vom Januar 2021. Zum Zeitpunkt der Erstellung der Arbeit befand sich der  BSI-Standard  200-4  demzufolge  im  Community  Draft  und  wurde  noch

<!-- page: 131 -->

nicht  final  publiziert.  Insbesondere  bei  der  Erstellung  des  Erhebungstools wurde Wert auf einen simplen und nachvollziehbaren Aufbau gelegt. Dies soll eine spätere Aktualisierung und Anpassung des Erhebungstools erleichtern. Im Rahmen von zukünftigen Arbeiten könnte das Reifegradmodell für den BSI-Standard 200-4 an geänderte Inhalte des Standards angepasst werden. Eine regelmäßige Aktualisierung sichert zudem die Relevanz des Reifegradmodells.

Schlussendlich bleibt festzuhalten, dass im Rahmen dieser Analyse eine mögliche  Herangehensweise  an  die  Erstellung  eines  Reifegradmodells  skizziert wurde. Die gewonnenen Erkenntnisse dieser Arbeit können sowohl methodisch (beispielsweise durch das Vorgehensmodell) als auch praktisch (beispielsweise durch das Erhebungstool) bei der Entwicklung neuer Reifegradmodelle verwendet werden.

<!-- page: 132 -->

## Literaturverzeichnis

Ahlemann, F., Schroeder, C. &amp; Teuteberg, F., 2005. Kompetenzund Reifegradmodelle für das Projektmanagement. Osnabrück: Universität Osnabrück.

Aleksandrova,  S.  V.,  Aleksandrov,  M.  N.  &amp;  Vasiliev,  V.  A.,  2018. Business Continuity Management System. St. Petersburg, IEEE, S. 14-17.

Angermeier, G., 2004. Projektmagazin. Taufkirchen. https://www.projektmagazin.de/glossarterm/quality-gate. Zugegriffen am 02. Juni 2021.

Barafort, B., Mesquida, A.-L. &amp; Mas, A., 2018. ISO 31000 - based integrated risk management process assessment model for IT organizations, Luxembourg: John Wiley &amp; Sons.

Basili,  V.,  Caldiera,  G.  &amp;  Rombach,  D.,  1994. The  Goal  Question  Metric Approach, Kaiserslautern: Universität Kaiserslautern.

Bas, M., 2021. Erstellung eines Reifegradmodells zum ITGrundschutz. Hagen: FernUniversität in Hagen.

Becker, J., Knackstedt, R. &amp; Poeppellbuß, J., 2009. Dokumentationsqualität von Reifegradmodellentwicklungen, Münster: Westfälische Wilhelms-Universität Münster.

Becker,  P.  D.  J.,  Knackstedt,  D.  R.  &amp;  Pöppelbuß,  J.,  2009.  Entwicklung  von Reifegradmodellen für das IT-Management - Vorgehensmodell und praktische Anwendung. Wirtschaftsinformatik , Nr. 3, S. 249-260.

Bensiek, T., 2013. Systematik zur reifegradbasierten Leistungsbewertung und - steigerung  von  Geschäftsprozessen  im  Mittelstand. Paderborn:  Universität Paderborn.

Bertram, D., 2006. Likert Scales. Calgary: CPSC 681 - Topic Report.

Bleck, F., Wittstruck, D. &amp; Teuteberg, F., 2011. Entwicklung und Validierung eines Reifegradmodells für das Sustainable Supply Chain Management. Tagungsband der Informatik (Band P192) , Juli.

Bundesamt für Sicherheit in der Informationstechnik, 2018. Mindeststandard des BSI  zur  Anwendung  des  HV-Benchmark  kompakt  4.0. Bonn:  Bundesamt  für Sicherheit in der Informationstechnik.

<!-- page: 133 -->

Bundesamt für Sicherheit in der Informationstechnik, 2021. BSI.Bund.de. Bonn. https://www.bsi.bund.de/DE/Service-

Navi/Presse/Pressemitteilungen/Presse2021/210118\_BSI-Standard-200-4.html. Zugegriffen am 13. Juni 2021

Bundesamt für Sicherheit in der Informationstechnik, 2021. BSI-Standard 200-4: Business  Continuity  Management. Bonn:  Bundesamt  für  Sicherheit  in  der Informationstechnik.

Business Continuity Institute, 2021. www.thebci.org. https://www.thebci.org/about-bci.html. Zugegriffen am 01. Juli 2021.

Christiansen, S.-K. &amp; Gausemeier, J., 2010. Klassifikation von Reifegradmodellen. Zeitschrift für wirtschaftlichen Fabrikbetrieb , S. 344-349.

Cortina,  S.,  Mayer,  N.,  Renault,  A.  &amp;  Barafort,  B.,  2014.  Towards  a  Process Assessment Model for Management System Standards. In: Software Process Improvement and Capability Determination. Switzerland: Springer International Publishing, S. 36-47.

Dayan,  R.  &amp;  Evans,  S.,  2006.  KM  your  way  to  CMMI. Journal  of  Knowledge Management, Vol. 10 Iss 1 , S. 69-80.

de Bruin, T. &amp; Freeze, R., 2005. Understanding the Main Phases of Developing a Maturity Assessment Model. Brisbane, s.n., S. 8-19.

Del Carpio, A. F., 2018. Visualizing  composition and behavior of the ISO/IEC 33000 assessment. s.l.:Computer Standards &amp; Interfaces.

Dey, D. M., 2011. Business Continuity Planning (BCP) Methodology - Essential for every business. Dubai, IEEE, S. 229-232.

DRI International, 2021. www.drii.org. https://drii.org/aboutus. Zugegriffen am 01. Juli 2021.

Fraser, P., Moultrie, J. &amp; Gregory, M., 2002. The use of maturity models / grids as a tool in assessing product development capability: a review. Cambridge, IEEE International.

Fritzsche,  M.  &amp;  Keil,  P.,  2007. Agilität  und  Prozessreife:  Erfüllbarkeit  der CMMIProzessgebiete  durch  agile  Methoden  am  Beispiel  von  XP. Software Engineering 2007 - Fachtagung des GI-Fachbereichs Softwaretechnik, Gesellschaft für Informatik e. V..

Gaulke, M., 2015. Das Instrument des Reifegrad-Assessments mit COBIT 5 im Revisionsalltag nutzen. Zeitschrift Interne Revision , 5, S. 200-207.

<!-- page: 134 -->

Haidzir,  H.  b.,  Othman,  S.  H.  &amp;  Mammi,  H.  K.,  2018.  Evaluation  of  Business Continuity Plan Maturity Level in Healthcare Organization. International Journal of Innovative Computing 8(1) , S. 33-42.

Hauck, J. C. R., Gresse von Wangenheim, C., Mc Caffery, F. &amp; Buglione, L., 2011. Proposing an ISO/IEC 15504-2 Compliant Method for Process Capability/Maturity Models Customization. Torre Canne, Springer Verlag, S. 4458.

Haufe,  D.  K.,  2017. Maturity  based  approach  for  ISMS  governance. Madric: Universidad Carlos III de Madrid.

Hecht, S., 2013. Ein Reifegradmodell für die Bewertung und Verbesserung von Fähigkeiten im ERP-Anwendungsmanagement. München: Springer Gabler.

Herbane, B., 2010. The evolution of business continuity management: A historical review of practices and drivers. Business History, Vol. 52 , Oktober, S. 978-1002.

Hevner,  A.,  2004.  Design  Science  in  Information  Systems  Research. MIS Quarterly Vol. 28 No. 1 , March, S. 75-105.

Hilles, A., 2010. The Definitive Handbook of Business Continuity Management. s.l.:John Wiley &amp; Sons.

International  Organisation  for  Standardisation,  2014. ISO/IEC  33020:2014. s.l.:International Organisation for Standardisation.

International  Organisation  for  Standardisation,  2015. ISO/IEC  33004:2015. s.l.:International Organisation for Standardisation.

Johnson, C. N., 2002. The Benefits of PDCA. Quality Progress (Bd. 35, Ausg. 5) , Mai, S. 120.

Jürjens, P. D. J., 2011. rgse.uni-koblenz.de. Koblenz. https://rgse.uni-koblenz.de/web/pages/teaching/ss11/mgse/Folien/V10\_Prozessqualitaet-\_Methodische\_Grundlagen\_des\_Software-Engineering.pdf. Zugegriffen  am 19. Juni 2021.

Kersten, H. &amp; Klett, G., 2017. Business Continuity und IT-Notfallmanagement. Wiesbaden: Springer Vieweg.

Klawitter, J., 2007. Business Continuity Maturity Model. New Jersey: Virtual Corp.

Kühl,  S.,  Strodtholz,  P.  &amp;  Taffertshofer,  A.,  2009. Handbuch  Methoden  der Organisationsforschung  -  Quantitative  und Qualitative  Methoden. Wiesbaden: GWV Fachverlage GmbH.

<!-- page: 135 -->

127

Kulkarni, U. &amp; St. Louis, R., 2003. Organizational Self Assessment of Knowledge Management Maturity. Tampa, AMCIS, S. 2542-2551. Lahrmann, G. &amp; Marx, F., 2010. Systematization of Maturity Model Extensions. St. Gallen, Springer Link, S. 522-525. Lami,  G.,  Fabbrini,  F.  &amp;  Buglione,  L.,  2014. An  ISO/IEC  33000-compliant Measurement  Framework  for  Software  Process  Sustainability  Assessment. Rotterdam, IWSM-MENSURA, S. 50-59. Lehmann, M. &amp; Sowa, J.-C., 2021. Business-Continuity-Management weitergedacht. &lt;KES&gt; , S. 30-32. Mettler,  T.,  2010. Supply  Management  im  Krankenhaus  -  Konstruktion  und Evaluation eines konfigurierbaren Reifegradmodells zur zielgerichteten Gestaltung. St. Gallen: Universität St. Gallen. Müller, M., Hörmann, D. K., Dittmann, L. &amp; Zimmer, J., 2016. Automotive SPICE in  der  Praxis  -  Interpretationshilfe  für  Anwender  und  Assessoren, Paderborn: dpunkt.verlag. Poeppelbuss, J. &amp; Roeglinger, M., 2011. What makes a useful maturity model? A framework of general design principles for maturity models and its demonstration in business process management. Helsinki, ECIS. Randeree, K., Mahal, A. &amp; Narwani, A., 2012. A business continuity management maturity  model  for  the  UAE  banking  sector. Business  Process  Management Journal , Juni, S. 472-492. Salviano,  C.  &amp;  Figueiredo,  A.,  2008. Unified  Basic  Concepts  for  Process Capability  Models. San  Francisco,  Centro  de  Pesquisas  Renato  Archer  - CenPRA, S. 173-178. Schweigert, T. &amp; Phillip, M., 2018. ISO 33020 Cornerstone or Pitfall of Process Improvement. In: EuroSPI 2018,. s.l.:Springer Nature Switzerland AG 2018, S. 318-328. Smit, N., 2005. Business Continuity Management - A Maturity Model. Rotterdam: Erasmus Universiteit Rotterdam. Torabi, S., Soufi, R. &amp; Sahebjamnia, N., 2014. A new framework for business impact analysis in business continuity management (with a case study). Teheran, University of Tehran, S. 309-323.

Venclova,  K.,  Urbancova,  H.  &amp;  Vostra  Vydrova,  H.,  2013.  Advantages  and Disadvantages  of  Business  Continuity  Management.  In: World  Academy  of Science,  Engineering  and  Technology  International  Journal  of  Industrial  and Systems Engineering Vol:7, No:4, 2013. s.l.:International Scholarly and Scientific Research &amp; Innovation, S. 895-899.

<!-- page: 136 -->

Youtube  Präsenz  der  HiSolutions  AG,  2021. 1.  IT-Grundschutz-Tag  -  BSI Standard 200-4 (ausgerichtet von der HiSolutions AG). Berlin. https://www.youtube.com/watch?v=\_S2yNZ06Zto&amp;list=PLEnTDCi\_wQ6LeliJGp ULuAdCvy3eFdKQK&amp;index=4. Zugegriffen am 13. August 2021.

<!-- page: 137 -->

## Anhang I: Vergleich bestehender BCM-Reifegradmodelle

## Klawitter (1997)

|   # | Abschnitt                                     | Prüfpunkt                                          | Berücksichtigt in                   | Votum     |
|-----|-----------------------------------------------|----------------------------------------------------|-------------------------------------|-----------|
|   1 | Initiierung des BCMS                          | Initiierung des BCMS                               | Zu finden in 'Lea- dership'         | Ja        |
|   2 | Analyse der erweiterten Rah- menbedingungen   | Planung des BCMS                                   | Zu finden in 'Lea- dership'         | Ja        |
|   3 | Dokumentation im Standard BCMS                | Planung des BCMS                                   | Zu finden in 'Lea- dership'         | Ja        |
|   4 | Leitlinie                                     | Planung des BCMS                                   | Zu finden in 'BC Program Structure' | Ja        |
|   5 | Aufbau der BAO                                | Aufbau und Befähi- gung der BAO                    | Teilweise über 'BC-Pläne'           | Teilweise |
|   6 | Detektion, Alarmierung und Eskalation         | Aufbau und Befähi- gung der BAO                    | Teilweise über 'BC-Pläne'           | Teilweise |
|   7 | Definition von Sofortmaß- nahmen              | Aufbau und Befähi- gung der BAO                    | Teilweise über 'BC-Pläne'           | Teilweise |
|   8 | Definition der Geschäftsord- nung des Stabes  | Aufbau und Befähi- gung der BAO                    | Teilweise über 'BC-Pläne'           | Teilweise |
|   9 | Herstellung der Fähigkeit zur Stabsarbeit     | Aufbau und Befähi- gung der BAO                    | Teilweise in 'Veran- kerung'        | Teilweise |
|  10 | Notfallkommunikation                          | Aufbau und Befähi- gung der BAO                    | Teilweise in 'Veran- kerung'        | Teilweise |
|  11 | Störbetrieb und Deeskalation                  | Aufbau und Befähi- gung der BAO                    | Teilweise in 'Veran- kerung'        | Teilweise |
|  12 | Analyse der Bewältigung                       | Aufbau und Befähi- gung der BAO                    | Zu finden in 'BC Program Content'   | Teilweise |
|  13 | Voranalyse                                    | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Zu finden in 'BC Program Content'   | Ja        |
|  14 | Business-Impact-Analyse                       | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Zu finden in 'BC Program Content'   | Ja        |
|  15 | Soll-Ist-Vergleich                            | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Zu finden in 'BC Program Content'   | Ja        |
|  16 | BCM-Risikoanalyse                             | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Zu finden in 'BC Program Content'   | Ja        |
|  17 | Business Continuity Strate- gien und Lösungen | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Zu finden in 'BC Program Content'   | Ja        |

<!-- page: 138 -->

Quelle: Eigene Darstellung

|   18 | Geschäftsfortführungspla- nung               | Angemessene Ab- sicherung der Ge- schäfts-prozesse   | Zu finden in 'BC Program Content'   | Ja   |
|------|----------------------------------------------|------------------------------------------------------|-------------------------------------|------|
|   19 | Wiederanlauf und Wieder- herstellungsplanung | Angemessene Ab- sicherung der Ge- schäfts-prozesse   | Zu finden in 'BC Program Content'   | Ja   |
|   20 | Üben und Testen                              | Überprüfung des BCMS                                 | Zu finden in 'Employee Awaren- ess' | Ja   |
|   21 | Leistungsüberprüfung und Berichterstattung   | Überprüfung des BCMS                                 | Zu finden in 'Metric'               | Ja   |
|   22 | Weiterentwicklung des BCMS                   | Korrektur und Ver- besserung                         | Zu finden in 'Metric'               | Ja   |

Tabelle 25: Detailbetrachtung BCM-Reifegradmodell Klawitter (1997)

## Smit (2005)

|   # | Abschnitt                                    | Prüfpunkt                       | Berücksichtigt in                                 | Votum     |
|-----|----------------------------------------------|---------------------------------|---------------------------------------------------|-----------|
|  23 | Initiierung des BCMS                         | Initiierung des BCMS            | Zu finden in 'BCM Policy'                         | Ja        |
|  24 | Analyse der erweiterten Rah- menbedingungen  | Planung des BCMS                | Zu finden in 'BCM Policy'                         | Ja        |
|  25 | Dokumentation im Standard BCMS               | Planung des BCMS                | Zu finden in 'BCM Policy'                         | Ja        |
|  26 | Leitlinie                                    | Planung des BCMS                | Zu finden in 'BCM Policy'                         | Ja        |
|  27 | Aufbau der BAO                               | Aufbau und Befähi- gung der BAO | Nein                                              | Teilweise |
|  28 | Detektion, Alarmierung und Eskalation        | Aufbau und Befähi- gung der BAO | Nein                                              | Teilweise |
|  29 | Definition von Sofortmaß- nahmen             | Aufbau und Befähi- gung der BAO | Ja in 'Development Plan'                          | Teilweise |
|  30 | Definition der Geschäftsord- nung des Stabes | Aufbau und Befähi- gung der BAO | Nein                                              | Teilweise |
|  31 | Herstellung der Fähigkeit zur Stabsarbeit    | Aufbau und Befähi- gung der BAO | Teilweise in 'Disas- ter Response Or- ganization' | Teilweise |
|  32 | Notfallkommunikation                         | Aufbau und Befähi- gung der BAO | Ja in 'Development Plan'                          | Teilweise |
|  33 | Störbetrieb und Deeskalation                 | Aufbau und Befähi- gung der BAO | Ja in 'Development Plan'                          | Teilweise |
|  34 | Analyse der Bewältigung                      | Aufbau und Befähi- gung der BAO | Ja in 'Analysis and determination ap- proach'     | Teilweise |

<!-- page: 139 -->

Quelle: Eigene Darstellung

|   35 | Voranalyse                                    | Angemessene Ab- sicherung der Ge- schäfts-prozesse   | Ja in 'Analysis and determination ap- proach'   | Ja        |
|------|-----------------------------------------------|------------------------------------------------------|-------------------------------------------------|-----------|
|   36 | Business-Impact-Analyse                       | Angemessene Ab- sicherung der Ge- schäfts-prozesse   | Ja in 'Analysis and determination ap- proach'   | Ja        |
|   37 | Soll-Ist-Vergleich                            | Angemessene Ab- sicherung der Ge- schäfts-prozesse   | Ja in 'Analysis and determination ap- proach'   | Ja        |
|   38 | BCM-Risikoanalyse                             | Angemessene Ab- sicherung der Ge- schäfts-prozesse   | Ja in 'Analysis and determination ap- proach'   | Ja        |
|   39 | Business Continuity Strate- gien und Lösungen | Angemessene Ab- sicherung der Ge- schäfts-prozesse   | Ja in 'Development Plan'                        | Ja        |
|   40 | Geschäftsfortführungspla- nung                | Angemessene Ab- sicherung der Ge- schäfts-prozesse   | Ja in 'Development Plan'                        | Ja        |
|   41 | Wiederanlauf und Wieder- herstellungsplanung  | Angemessene Ab- sicherung der Ge- schäfts-prozesse   | Ja in 'Development Plan'                        | Ja        |
|   42 | Üben und Testen                               | Überprüfung des BCMS                                 | Ja in 'Maintenance'                             | Teilweise |
|   43 | Leistungsüberprüfung und Berichterstattung    | Überprüfung des BCMS                                 | Nein                                            | Teilweise |
|   44 | Weiterentwicklung des BCMS                    | Korrektur und Ver- besserung                         | Nein                                            | Nein      |

Tabelle 26: Detailbetrachtung BCM-Reifegradmodell Smit (2005)

## Randeree (2012)

|   # | Abschnitt                                   | Prüfpunkt                       | Berücksichtigt in                | Votum     |
|-----|---------------------------------------------|---------------------------------|----------------------------------|-----------|
|  45 | Initiierung des BCMS                        | Initiierung des BCMS            | Ja in 'BCM Program Ma- nagement' | Ja        |
|  46 | Analyse der erweiterten Rah- menbedingungen | Planung des BCMS                | Ja in 'BCM Program Ma- nagement  | Ja        |
|  47 | Dokumentation im Standard BCMS              | Planung des BCMS                | Ja in 'BCM Program Ma- nagement  | Ja        |
|  48 | Leitlinie                                   | Planung des BCMS                | Ja in 'BCM Program Ma- nagement  | Ja        |
|  49 | Aufbau der BAO                              | Aufbau und Befähi- gung der BAO | Nein                             | Teilweise |

<!-- page: 140 -->

|   50 | Detektion, Alarmierung und Eskalation         | Aufbau und Befähi- gung der BAO                    | Nein                               | Teilweise   |
|------|-----------------------------------------------|----------------------------------------------------|------------------------------------|-------------|
|   51 | Definition von Sofortmaß- nahmen              | Aufbau und Befähi- gung der BAO                    | Ja in 'Development of the BC plan' | Teilweise   |
|   52 | Definition der Geschäftsord- nung des Stabes  | Aufbau und Befähi- gung der BAO                    | Ja in 'Development of the BC plan' | Teilweise   |
|   53 | Herstellung der Fähigkeit zur Stabsarbeit     | Aufbau und Befähi- gung der BAO                    | Ja in 'Development of the BC plan' | Teilweise   |
|   54 | Notfallkommunikation                          | Aufbau und Befähi- gung der BAO                    | Ja in 'Development of the BC plan' | Teilweise   |
|   55 | Störbetrieb und Deeskalation                  | Aufbau und Befähi- gung der BAO                    | Nein                               | Teilweise   |
|   56 | Analyse der Bewältigung                       | Aufbau und Befähi- gung der BAO                    | Nein                               | Teilweise   |
|   57 | Voranalyse                                    | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Ja in 'Planning and analysis'      | Ja          |
|   58 | Business-Impact-Analyse                       | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Ja in 'Planning and analysis'      | Ja          |
|   59 | Soll-Ist-Vergleich                            | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Ja in 'Planning and analysis'      | Ja          |
|   60 | BCM-Risikoanalyse                             | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Ja in 'Planning and analysis'      | Ja          |
|   61 | Business Continuity Strate- gien und Lösungen | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Ja in 'Planning and analysis'      | Ja          |
|   62 | Geschäftsfortführungs-pla- nung               | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Ja in 'Planning and analysis'      | Ja          |
|   63 | Wiederanlauf und Wieder- herstellungsplanung  | Angemessene Ab- sicherung der Ge- schäfts-prozesse | Ja in 'Implementa- tion'           | Ja          |
|   64 | Üben und Testen                               | Überprüfung des BCMS                               | Ja in 'Maintenaince'               | Teilweise   |
|   65 | Leistungsüberprüfung und Berichterstattung    | Überprüfung des BCMS                               | Nein                               | Teilweise   |
|   66 | Weiterentwicklung des BCMS                    | Korrektur und Ver- besserung                       | Nein                               | Nein        |

Quelle: Eigene Darstellung

Tabelle 27: Detailbetrachtung BCM-Reifegradmodell Randeree (2012)

<!-- page: 141 -->

## Anhang II: Prozessbeschreibungen des PRM

MP.1 Initiierung, Planung und Steuerung des BCMS

| Attribut Eigenschaft                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck Festlegung der strategischen Rahmenbedingungen des BCMS, so- wie Anpassung des BCMS an die organisatorischen Begebenheiten der Institution.                                                                                                                                 |
| Prozessergebnisse • Ziele und Rahmenbedingungen des BCMS sind festgelegt und kommuniziert • Gründe für das BCMS sind identifiziert und dokumentiert • Abzusichernder Zeitraum und Geltungsbereich des BCMS ist definiert • Verantwortung der Institutionsleitung ist dokumentiert |
| Basispraktiken • Erhebung der relevanten Schnittstellen zu weiteren Manage-                                                                                                                                                                                                       |
| Arbeitsprodukte • BCM-Leitlinie • Selbstverpflichtung der Institutionsleitung • Festlegung der Vorgehensweise • Abgegrenzter Geltungsbereich des BCMS Zielsetzung                                                                                                                 |
| Referenzen BSI 200-4 • 3.1.1 • 3.1.2 Geltungsbereich • 3.1.3 Entscheidung für Vorgehensweise • 3.1.4 Übernahme der Verantwortung durch die Leitungsebene • 3.1.1.2 Abzusichernder Zeitraum durch ein BCM • 3.1.1.1 Motivation für den Aufbau eines BCMS                           |

Quelle: Eigene Darstellung

Tabelle 28: Prozesssteckbrief MP.1 Initiierung, Planung und Steuerung des BCMS

MP.2 Managementreview

| Attribut          | Eigenschaft                                                                                                                                |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck             | Treffen von strategischen Entscheidungen hinsichtlich der zukünfti- gen Weiterentwicklung des BCMS durch die Institutionsleitung.          |
| Prozessergebnisse | • Das BCMS der Institution wird regelmäßig durch die Leitungs- ebene bewertet • Relevante Entscheidungen werden getroffen und dokumentiert |
| Basispraktiken    | • Organisation/Planung von regelmäßigen Evaluierungen des BCMS • Regelmäßige Evaluierung des BCMS in geplanten Abständen                   |

<!-- page: 142 -->

| Arbeitsprodukte      | • Entscheidungsvorlage • Dokumentierte Entscheidungen der Leitungsebene   |
|----------------------|---------------------------------------------------------------------------|
| Referenzen BSI 200-4 | • 6.12.3 Prüfung durch die Institutionsleitung (Managementbe- wertung)    |

Quelle: Eigene Darstellung

Tabelle 29: Prozesssteckbrief MP.2 Managementreview

## BCMS-Lifecycle-Prozesse (LP):

## LP.1 Befähigung der Stabsstrukturen

Quelle: Eigene Darstellung

| Attribut             | Eigenschaft                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck                | Aufbau und Befähigung angemessener Stabsstrukturen zur Notfall- bewältigung.                                                                                                                                                                                                                                                                                                                                                                                                              |
| Prozessergebnisse    | • Besondere Aufbauorganisation ist etabliert • Stabsstrukturen (inkl. Aufgaben und Zuständigkeiten) sind auf- gebaut und freigegeben • Notfallbewältigungsteams zur operativen Notfallbewältigung sind aufgebaut • Organisatorischen Aspekte der Stabsarbeit wurden definiert (Stabsraum, Vorgaben zur Protokollierung etc.) • Regelungen und Vorgaben für die interne und externe Notfall- kommunikation wurden definiert • Interessengruppen für die Notfallkommunikation sind bestimmt |
| Basispraktiken       | • Personelle Besetzung der definierten Rollen (inkl. Vertretungsre- gelung) • Festlegung der Entscheidungs- und Weisungsbefugnis der Rol- len der BAO • Dokumentation der Regelungen zur Stabsarbeit (z.B. Erreichbar- keit etc.) • Festlegung der organisatorischen Begebenheiten der Stabsar- beit (z.B. Stabsraum, Arbeitsanweisungen etc.)                                                                                                                                            |
| Arbeitsprodukte      | • Geschäftsordnung des Stabs (inklusive namentlicher Benen- nung der Rolleninhaber) • Interessensgruppen der Notfallkommunikation • Verhaltenskodex der Stabsarbeit                                                                                                                                                                                                                                                                                                                       |
| Referenzen BSI 200-4 | • 6.4.1 Aufbau der BAO • 6.4.1.5 Aufbau von Notfallbewältigungsteams                                                                                                                                                                                                                                                                                                                                                                                                                      |

Tabelle 30: Prozesssteckbrief LP.1 Befähigung der Stabsstrukturen

<!-- page: 143 -->

## LP.2 Meldung, Alarmierung, Erstreaktion

| Attribut             | Eigenschaft                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck                | Aufbau und Aufrechterhaltung von Strukturen für eine angemes- sene Meldung, Alarmierung und Erstreaktion von Notfällen.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Prozessergebnisse    | • Ablauf von Meldungen ist definiert, abgestimmt und dokumen- tiert • Eine zentrale Meldestelle ist eingerichtet und organisationsweit bekannt • Notwendige Sofortmaßnahmen zur Reaktion auf Notfälle sind festgelegt und bekanntgemacht • Zentrale Entscheidungsinstanz im Alarmierungsprozess ist be- stimmt und durch die Institutionsleitung freigegeben                                                                                                                                                                                                            |
| Basispraktiken       | • Erstellung von Handlungsanweisungen für die Meldung von Schadensereignissen mit Notfallpotenzial • Erhebung, Konzeption und Abstimmung von Meldewegen • Dokumentation der Meldewege im Notfallhandbuch • Identifikation relevanter Meldequellen der Institution • Festlegung einer zentralen Entscheidungsinstanz im Meldepro- zess • Abstimmung und Bekanntmachung des Meldeprozesses mit beteiligten Schnittstellen • Erhebung und Dokumentation von Sofortmaßnahmen für spezi- fische Notfallszenarien • Festlegung der Handlungsabläufe zum Ausrufen des Notfalls |
| Arbeitsprodukte      | • Visualisierter Melde- und Alarmierungsprozess (Ggf. Bestand- teil des Notfallhandbuchs) • Melde- und Alarmierungskonzept/Alarmierungsplan (Ggf. Be- standteil des Notfallhandbuchs) • Zentrale Meldestelle eingerichtet und Erreichbarkeit dokumen- tiert                                                                                                                                                                                                                                                                                                             |
| Referenzen BSI 200-4 | • 6.4.2.1 Detektion und Meldung • 6.4.2 Detektion, Alarmierung und Eskalation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

Quelle: Eigene Darstellung

Tabelle 31: Prozesssteckbrief LP.2 Meldung, Alarmierung, Erstreaktion

## LP.3 Störbetrieb, Deeskalation und Bewältigung

| Attribut          | Eigenschaft                                                                                                                                       |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck             | Aufbau und Aufrechterhaltung von Strukturen und Verfahren für eine angemessene Rückführung in den Normalbetrieb.                                  |
| Prozessergebnisse | • Maßnahmen für eine angemessene Rückführung in den Nor- malbetrieb sind definiert • Kriterien für die Deeskalation eines Notfalls sind definiert |

<!-- page: 144 -->

|                      | • Notfälle werden nach Bewältigung analysiert, Präventivmaß- nahmen abgeleitet und die Erkenntnisse an die Institutionslei- tung berichtet                                                                                                                                                                                                                                                                                                                                             |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basispraktiken       | • Festlegung des Störbetriebsniveaus • Festlegung von Prüfpunkten für eine angemessene Rückfüh- rung in den Normalbetrieb • Reihenfolge der anlaufenden Geschäftsprozesse wird festge- legt • Festlegung von Kriterien und Zuständigkeiten für die Deeskala- tion • Definition von Vorgaben für die Analyse von Notfällen • Durchführung von Workshops für die Analyse der Notfallbewäl- tigung • Erhebung von präventiven Verbesserungsmaßnahmen und Do- kumentation im Maßnahmenplan |
| Arbeitsprodukte      | • Checkliste für die Rückführung in den Normalbetrieb • Kriterien für die Deeskalation von Notfällen • Vorgaben für die Analyse von Notfällen                                                                                                                                                                                                                                                                                                                                          |
| Referenzen BSI 200-4 | • 6.4.7 Störbetrieb und Deeskalation • 6.4.8 Analyse der Bewältigung                                                                                                                                                                                                                                                                                                                                                                                                                   |

Quelle: Eigene Darstellung

Tabelle 32: Prozesssteckbrief LP.3 Störbetrieb, Deeskalation und Bewältigung

## LP.4 Business-Impact-Analyse

| Attribut          |
|-------------------|
| Zweck             |
| Prozessergebnisse |
| Basispraktiken    |
| Arbeitsprodukte   |

<!-- page: 145 -->

|                      | • Gesamtübersicht der zeitkritischen Geschäftsprozesse und Ressourcen   |
|----------------------|-------------------------------------------------------------------------|
| Referenzen BSI 200-4 | • 6.5 Business-Impact-Analyse                                           |

Quelle: Eigene Darstellung

Tabelle 33: Prozesssteckbrief LP.4 Business-Impact-Analyse

<!-- page: 146 -->

## LP.5 BCM-Risikoanalyse und Soll-Ist-Vergleich

| Attribut Eigenschaft                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck Durchführung von BCM-Risikoanalysen zur Identifikation und Be- wertung möglicher Ursachen für den Ausfall des Geschäftsbetriebs.                                                                     |
| Prozessergebnisse • BCM-Risikoanalyse für die zeitkritischen Geschäftsprozesse der Institution wurden durchgeführt • Soll-Ist-Vergleich wurde durchgeführt und durch die Institutions- leitung freigegeben |
| Basispraktiken • Durchführung der BCM-Risikoanalyse, Risikoeinschätzung je                                                                                                                                 |
| Arbeitsprodukte • Ressourcenübersicht                                                                                                                                                                      |
| Referenzen BSI 200-4 • 6.6 Soll-Ist-Vergleich • 6.7 BCM-Risikoanalyse                                                                                                                                      |

Quelle: Eigene Darstellung

Tabelle 34: Prozesssteckbrief LP.5 BCM-Risikoanalyse und Soll-Ist-Vergleich

## LP.6 Notfallplanung und Konzeption

| Attribut Eigenschaft                                                                               |
|----------------------------------------------------------------------------------------------------|
| Zweck Gewährleistung einer angemessenen schen Geschäftsprozesse Konzeption der Notfallbewältigung. |
| Prozessergebnisse • Geschäftsfortführungsplanung prozesse ist erstellt                             |
| Basispraktiken Pläne                                                                               |

<!-- page: 147 -->

|                      | • Festlegung von Sofortmaßnahmen • Festlegung von Maßnahmen für den Wiederanlauf • Dokumentation von Notfallteams im BCP • Erstellung notfallrelevanter Dokumente und Arbeitsmittel • Erstellung von Geschäftsfortführungsplänen • Erstellung von Wiederanlauf- und Wiederherstellungsplänen   |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Arbeitsprodukte      | • Dokumentation der BC-Strategien • BC-Pläne für ausgewählte kritische Geschäftsprozesse • Geschäftsfortführungspläne inklusive Notfallmaßnahmen • Wiederanlaufplanung (Inkl. Handlungsanweisungen für den Wiederanlauf der Ressourcen)                                                        |
| Referenzen BSI 200-4 | 6.8 Business-Continuity-Strategien und -Lösungen 6.9 Geschäftsfortführungsplanung 6.10 Wiederanlauf- und Wiederherstellungsplanung                                                                                                                                                             |

Quelle: Eigene Darstellung

Tabelle 35: Prozesssteckbrief LP.6 Notfallplanung und Konzeption

## LP.7 Tests- und Übungen

| Attribut             | Eigenschaft                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck                | Strukturierte Planung von Tests- und Übungen zur Überprüfung der Handlungsabläufe und Pläne des BCMS.                                                                                                                                                                                                                                                                                                                    |
| Prozessergebnisse    | • BCMS Übungen und Tests werden regelmäßig durchgeführt • Abgestimmtes Übungs- und Testprogramm ist erstellt • Jahresübungsplanung ist erstellt • Übungsbericht (inklusive Korrekturbedarfe und Verbesserungs- möglichkeiten) ist erstellt                                                                                                                                                                               |
| Basispraktiken       | • Planung, Vorbereitung, Durchführung und Nachbereitung von Übungen (Jahresübungsplanung) • Bestimmung von Rahmenbedingungen für die Durchführung von Übungen und Tests • Erstellung von Vorlagen/Hilfsmittel für die Durchführung von Übungen und Tests • Erstellung von Übungskonzepten • Dokumentation der Übungen und Tests (Übungsprotokoll und Übungsbericht) • Auswertung und Nachbereitung der Übungen und Tests |
| Arbeitsprodukte      | • Übungs- und Testprogramm (Jahresübungsplanung) • Übungsrahmen • Übungskonzept (je Übung) • Übungsberichte • Jahresübungsplanung                                                                                                                                                                                                                                                                                        |
| Referenzen BSI 200-4 | • 6.11 Üben und Testen                                                                                                                                                                                                                                                                                                                                                                                                   |

Quelle: Eigene Darstellung

Tabelle 36: Prozesssteckbrief LP.7 Tests- und Übungen

<!-- page: 148 -->

## LP.8 Überprüfung und Berichterstattung

| Attribut             | Eigenschaft                                                                                                                                                                                                                                                                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck                | Regelmäßige Überprüfung der Wirksamkeit und Angemessenheit des BCMS sowie Berichterstattung an die Institutionsleitung.                                                                                                                                                                                                                                 |
| Prozessergebnisse    | • Institutionsleitung ist über den aktuellen Stand des BCMS infor- miert • Wirksamkeit und Angemessenheit der Maßnahmen wird regel- mäßig überprüft • Kennzahlen für das BCMS sind definiert und werden gesteuert                                                                                                                                       |
| Basispraktiken       | • Auswahl und Erhebung von Kennzahlen und Zielwerten für das BCMS • Regelmäßige Analyse und Bewertung der Kennzahlen • Planung und regelmäßige Durchführung von Audits und Über- prüfungen für das BCMS • Identifikation und Analyse von Abweichungen und notwendigen Handlungsbedarf • Regelmäßige Erstellung von Berichten an die Institutionsleitung |
| Arbeitsprodukte      | • BCM Auditprogramm • BCM Kennzahlen • BCM Maßnahmenplan • BCM-Bericht für die Organisationsleitung (Managementbewer- tung)                                                                                                                                                                                                                             |
| Referenzen BSI 200-4 | • 6.12 Leistungsüberprüfung und Berichterstattung                                                                                                                                                                                                                                                                                                       |

Quelle: Eigene Darstellung

Tabelle 37: Prozesssteckbrief LP.8 Überprüfung und Berichterstattung

## LP.9 Kontinuierliche Verbesserung

| Attribut          | Eigenschaft                                                                                                                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck             | Identifikation und Umsetzung von Korrekturbedarfen und Verbesse- rungsmöglichkeiten für das BCMS.                                                                                                                  |
| Prozessergebnisse | zeitnah identifiziert • BCM-Maßnahmenplan ist durch die Institutionsleitung freigege-                                                                                                                              |
| Basispraktiken    | • Priorisierung und Terminierung der Korrektur- und Verbesse- rungsmaßnahmen • Festlegung von Verantwortlichkeiten für die Umsetzung der Korrektur- und Verbesserungsmaßnahmen • Erstellung des BCM-Maßnahmenplans |
| Arbeitsprodukte   | • BCM Maßnahmenplan                                                                                                                                                                                                |

<!-- page: 149 -->

|                      | • BCM-Bericht für die Organisationsleitung (Managementbewer- tung)   |
|----------------------|----------------------------------------------------------------------|
| Referenzen BSI 200-4 | • 6.13 Korrektur und Verbesserung des BCMS                           |

Quelle: Eigene Darstellung

Tabelle 38: Prozesssteckbrief LP.9 Kontinuierliche Verbesserung

## Support-Prozesse (SP):

## SP.1 Dokumentenlenkung

| Attribut             | Eigenschaft                                                                                                                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zweck                | Sicherstellung der Einhaltung des Dokumenten-Lebenszyklus für alle Dokumente im BCMS.                                                                                                                                       |
| Prozessergebnisse    | • Dokumentenlenkung für die Dokumente des BCMS ist festge- legt • Relevante Dokumente des BCMS werden regelmäßig aktuali- siert • Alle Dokumente des BCMS werden entsprechend den Vorga- ben der Dokumentenlenkung erstellt |
| Basispraktiken       | • Festlegung der relevanten Dokumenteninformationen für Doku- mente des BCMS • Regelmäßige Überprüfung und Aktualisierung der BCM-Doku- mente                                                                               |
| Arbeitsprodukte      | • Anforderungen an die Dokumentenlenkung                                                                                                                                                                                    |
| Referenzen BSI 200-4 | • 6.2 Dokumentation im Standard-BCMS                                                                                                                                                                                        |

Quelle: Eigene Darstellung

Tabelle 39: Prozesssteckbrief SP.1 Dokumentenlenkung

## SP.2 BCM Aufbauorganisation

| Attribut          | Eigenschaft                                                                              |
|-------------------|------------------------------------------------------------------------------------------|
| Zweck             | Festlegung und Bekanntmachung von Rollen und Verantwortlich- keiten für das BCMS.        |
| Prozessergebnisse | definiert und bekanntgegeben • Personen besitzen nachweislich notwendige Kompetenzen für |
| Basispraktiken    | keiten der BCM-Aufbauorganisation                                                        |

<!-- page: 150 -->

|                      | • Festlegung der Berichtswege an die Leitungsebene (insbeson- dere: direktes Vorspracherecht) • Ggf. Fachliche und persönliche Befähigung des BCMB-Beauf- tragten   |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Arbeitsprodukte      | • BCM-Organisationskonzept (Ggf. als Bestandteil des Vorsorge- konzept) • Geschäftsverteilungsplan • Aufgaben- und Stellenprofil der Mitarbeiter                    |
| Referenzen BSI 200-4 | • 3.1.5 Benennung des BCM-Beauftragten • 3.2.2 Definition der BCM-Aufbauorganisation • 3.2.4 Ressourcenplanung                                                      |

Quelle: Eigene Darstellung

Tabelle 40: Prozesssteckbrief SP.2 BCM Aufbauorganisation

## SP.3 Schulung und Sensibilisierung

| Attribut                                                    | Eigenschaft                                           |
|-------------------------------------------------------------|-------------------------------------------------------|
| Zweck Sensibilisierung                                      | Schulung und BCMS.                                    |
| Prozessergebnisse • Schulungsziele werden • Bewusstsein für |                                                       |
| Basispraktiken werden für                                   | • Schulungsziele • Bewusstsein                        |
| Arbeitsprodukte                                             | • BCM-Schulungskonzept • BCM-Sensibilisierungskonzept |
| Referenzen BSI                                              | 200-4 • 3.2.5 Schulung • 3.2.6 Sensibilisierung       |

Quelle: Eigene Darstellung

Tabelle 41: Prozesssteckbrief SP.3 Schulung und Sensibilisierung

<!-- page: 151 -->

## Anhang III: Aufbau der Reifegradstufen (gemäß ISO/IEC 33020)

| Reifegradstufe          | ID     | Bewertung zur Erreichung des Reifegrads                 |
|-------------------------|--------|---------------------------------------------------------|
| Stufe 0: Unvollständig  |        |                                                         |
| Stufe 1: Durchgeführt   | PA 1.1 | Größtenteils erreicht (L) oder vollständig erreicht (F) |
| Stufe 2: Wiederholbar   | PA 1.1 | Vollständig erreicht (F)                                |
| Stufe 2: Wiederholbar   | PA 2.1 | Größtenteils erreicht (L) oder vollständig erreicht (F) |
| Stufe 2: Wiederholbar   | PA 2.2 | Größtenteils erreicht (L) oder vollständig erreicht (F) |
| Stufe 3: Standardisiert | PA 1.1 | Vollständig erreicht (F)                                |
| Stufe 3: Standardisiert | PA 2.1 | Vollständig erreicht (F)                                |
| Stufe 3: Standardisiert | PA 2.2 | Vollständig erreicht (F)                                |
| Stufe 3: Standardisiert | PA 3.1 | Größtenteils erreicht (L) oder vollständig erreicht (F) |
| Stufe 3: Standardisiert | PA 3.2 | Größtenteils erreicht (L) oder vollständig erreicht (F) |
| Stufe 4: Gesteuert      | PA 1.1 | Vollständig erreicht (F)                                |
| Stufe 4: Gesteuert      | PA 2.1 | Vollständig erreicht (F)                                |
| Stufe 4: Gesteuert      | PA 2.2 | Vollständig erreicht (F)                                |
| Stufe 4: Gesteuert      | PA 3.1 | Vollständig erreicht (F)                                |
| Stufe 4: Gesteuert      | PA 3.2 | Vollständig erreicht (F)                                |
| Stufe 4: Gesteuert      | PA 4.1 | Größtenteils erreicht (L) oder vollständig erreicht (F) |
| Stufe 4: Gesteuert      | PA 4.2 | Größtenteils erreicht (L) oder vollständig erreicht (F) |
| Stufe 5: Optimierend    | PA 1.1 | Vollständig erreicht (F)                                |
| Stufe 5: Optimierend    | PA 2.1 | Vollständig erreicht (F)                                |
| Stufe 5: Optimierend    | PA 2.2 | Vollständig erreicht (F)                                |
| Stufe 5: Optimierend    | PA 3.1 | Vollständig erreicht (F)                                |
| Stufe 5: Optimierend    | PA 3.2 | Vollständig erreicht (F)                                |
| Stufe 5: Optimierend    | PA 4.1 | Vollständig erreicht (F)                                |
| Stufe 5: Optimierend    | PA 4.2 | Vollständig erreicht (F)                                |
| Stufe 5: Optimierend    | PA 5.1 | Größtenteils erreicht (L) oder vollständig erreicht (F) |

<!-- page: 152 -->

| Stufe 5: Optimierend   | PA 5.2   | Größtenteils erreicht (L) oder vollständig erreicht (F)   |
|------------------------|----------|-----------------------------------------------------------|

Quelle: ISO/IEC 33020

Tabelle 42: Ableitung der Reifegrade in Abhängigkeit der Prozessattribute

<!-- page: 153 -->

## Anhang IV: Excel-basiertes Erhebungstool

Das excel-basierte Erhebungstool ist dieser Arbeit als separates Dokument beiliegend:

- THB - Erhebungstool BSI-Standard 200-4.xlsx

<!-- page: 154 -->

## Anhang V: Evaluationsbögen zur Bewertung des Reifegradmodells

## Vorlage:

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 33: Vorlage des Evaluationsbogens, Teil I

<!-- page: 155 -->

<!-- image -->

<!-- image -->

<!-- page: 156 -->

## Evaluationsbogen Optimal Systems GmbH:

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 35: Evaluationsbogen Optimal Systems, Teil I

<!-- page: 157 -->

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 36: Evaluationsbogen Optimal Systems, Teil II

<!-- page: 158 -->

## Evaluationsbogen Vivantes - Netzwerk für Gesundheit GmbH:

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 37: Evaluationsbogen Vivantes, Teil I

<!-- page: 159 -->

<!-- image -->

Quelle: Eigene Darstellung

<!-- image -->

Abbildung 38: Evaluationsbogen Vivantes, Teil II

<!-- page: 160 -->

## Evaluationsbogen Handelsunternehmen (nicht öffentlich):

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 39: Evaluationsbogen Handelsunternehmen, Teil I

<!-- page: 161 -->

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 40: Evaluationsbogen Handelsunternehmen, Teil II

<!-- page: 162 -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 41: Evaluationsbogen Handelsunternehmen, Teil III

<!-- image -->

<!-- page: 163 -->

## Evaluationsbogen DKB-Service GmbH:

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 42: Evaluationsbogen DKB Service GmbH, Teil I

<!-- page: 164 -->

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 43: Evaluationsbogen DKB Service GmbH, Teil II

<!-- page: 165 -->

## Evaluationsbogen Bundesamt für Sicherheit in der Informationstechnik:

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 44: Evaluationsbogen BSI, Teil I

<!-- page: 166 -->

<!-- image -->

<!-- image -->

Quelle: Eigene Darstellung

Abbildung 45: Evaluationsbogen BSI, Teil II

<!-- page: 167 -->

## Ehrenwörtliche Erklärung

Hiermit versichere ich, dass ich die vorliegende Arbeit selbstständig verfasst und keine anderen als die angegebenen Quellen oder Hilfsmittel benutzt habe und dass die Arbeit in gleicher oder ähnlicher Form noch keiner anderen Prüfungsbehörde vorgelegt wurde.

Berlin, den 20. September 2021

<!-- image -->

(Victor Wolf)

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 1 -->

> Erstellung eines Reifegradmodells für den BSI-Standard 200-4

> zur Erlangung des Grades Master of Science

> vorgelegt von:

<!-- page: 2 -->

> Abkürzungsverzeichnis .................................................................................  VII

<!-- page: 5 -->

> Abbildung 29: Auszug der Statements im Evaluationsbogen ......................... 115

<!-- page: 7 -->

> VI

<!-- page: 8 -->

> BIA

<!-- page: 15 -->

> Business-Impact-Analyse (BIA):

> zesse. Im Ergebnis der BIA werden alle kritischen Ressourcen und Geschäfts-

<!-- page: 75 -->

> den daraufhin angepasst.

<!-- page: 81 -->

> Change-Management  bearbei-

<!-- page: 102 -->

> Einer Person wurde (ggf. infor-

<!-- page: 142 -->

> Identifikation aller Aufgaben, Rechte und Pflichten für die Rollen

<!-- page: 144 -->

> Einheitliches Festlegen der BIA Parameter und der Zeithori-

> Einheitliches Festlegen der Ressourcenkategorien und -Cluster

<!-- page: 146 -->

> Erstellung einer Gefährdungsgrundlage für die relevanten Res-

> Zielobjekt

> Identifikation von Risikobehandlungsoptionen

> Erstellung von BC-Plänen für BCM-Ausfallszenarien

<!-- page: 148 -->

> Korrektur- und Verbesserungsbedarfe für das BCMS werden

<!-- page: 149 -->

> Erhebung des Ressourcenbedarfs für das BCMS

> Benennung und Bekanntgabe eines BCM-Beauftragten als

> Hauptansprechpartner

<!-- page: 150 -->

> Schulungs- und Fähigkeitsbedarf wird regelmäßig identifiziert

> Schulungs- und Fähigkeitsbedarf wird regelmäßig identifiziert
