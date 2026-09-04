---
source_file: "Fluchs_Profil_Wasser.pdf"
source_sha256: 8f966823b95a8480156ce46072f1b9ec58dbe74ff5836dc3269f58833329b290
source_bytes: 1869923
pages: 104
tables: 45
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T19:08:35+00:00"
text_coverage_percent: 99.894
appended_source_lines: 85
restored_hyphens: 10
extraction_status: warn
warnings:
  - "10 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): GesamtReferenzarchitektur -> Gesamt-Referenzarchitektur, GrundschutzBausteine -> Grundschutz-Bausteine, GrundschutzProfil -> Grundschutz-Profil, ICSNetze -> ICS-Netze, ICSSecurity -> ICS-Security"
  - "Der Textlayer der Quelle enthaelt 541 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
  - "85 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

## IT-Grundschutz-Pilotprofil bzw.

## IT-Grundschutz-Profil für die Wasserwirtschaft

- Freie Version -

Erstellt im Rahmen einer Masterarbeit beim

## Bundesamt für Sicherheit in der Informationstechnik

Von: Sarah Fluchs Datum: 18. Juni 2017 Betreuer: Dipl.-Inf. Holger Schildt, Verena Lang M.Sc. Bundesamt für Sicherheit in der Informationstechnik 1. Prüferin: Prof. Dr.-Ing. Ulrike Meyer Research Group IT-Security, RWTH Aachen 2. Prüfer: Prof. Dr.-Ing. Ulrich Epple Lehrstuhl für Prozessleittechnik, RWTH Aachen Das vorliegende Dokument enthält das IT-Grundschutz-Profil als Anhang zur Masterarbeit

<!-- page: 2 -->

## 'Erstellung eines IT-Grundschutz-Profils für ein Referenzunternehmen mit automatisierter Prozesssteuerung' .

Das Profil beinhaltet das Hauptprofil sowie das Unterprofil AR (Architektur).

Anhänge für die Nutzung des Profils als

In diesem Dokument sind nur die frei verfügbaren Pilotprofil enthalten.

Ein zusätzlicher Anhang (verlängerter Anhang B) für die Nutzung des Profils zur Anwendung auf Institutionen der Wasserwirtschaft unterliegt einer Sperrklausel und ist kostenpflichtig erhältlich.

<!-- page: 3 -->

## IT-Grundschutz-Pilotprofil bzw.

## IT-Grundschutz-Profil für die Wasserwirtschaft

- Hauptprofil -

Erstellt im Rahmen einer Masterarbeit beim

## Bundesamt für Sicherheit in der Informationstechnik

Von: Sarah Fluchs Datum: 18. Juni 2017 Betreuer: Dipl.-Inf. Holger Schildt, Verena Lang M.Sc. Bundesamt für Sicherheit in der Informationstechnik 1. Prüferin: Prof. Dr.-Ing. Ulrike Meyer Research Group IT-Security, RWTH Aachen 2. Prüfer: Prof. Dr.-Ing. Ulrich Epple Lehrstuhl für Prozessleittechnik, RWTH Aachen

<!-- page: 4 -->

## Inhaltsverzeichnis

| Vorbemerkungen .................................................................................................   | Vorbemerkungen .................................................................................................                                                          | 6                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 1                                                                                                                  | Formale Aspekte .......................................................................................                                                                   | 8                                                                                                     |
| 1.1                                                                                                                | Titel .............................................................................................................                                                       | 8                                                                                                     |
| 1.2                                                                                                                | Autor und Verantwortliche/r .........................................................................                                                                     | 8                                                                                                     |
| 1.3                                                                                                                | Versionsstand und Revisionszyklus                                                                                                                                         | ............................................................ 8                                        |
| 1.4                                                                                                                | Vertraulichkeit                                                                                                                                                           | ............................................................................................. 8       |
| 1.5                                                                                                                | Status der BSI-Anerkennung                                                                                                                                                | ...................................................................... 8                              |
| 2                                                                                                                  | Management Summary .............................................................................                                                                          | 9                                                                                                     |
| 2.1                                                                                                                | Zielgruppe                                                                                                                                                                | ................................................................................................... 9 |
| 2.2                                                                                                                | Zielsetzung .................................................................................................                                                             | 9                                                                                                     |
| 2.3                                                                                                                | Inhalte .........................................................................................................                                                         | 9                                                                                                     |
| 3                                                                                                                  | Anwendung des IT-Grundschutz-Profils                                                                                                                                      | ............................................... 11                                                    |
| 3.1                                                                                                                | Begriffsklärung zum IT-Grundschutz und IT-Grundschutz-Profil ................                                                                                             | 11                                                                                                    |
| 3.2                                                                                                                | Anwendungsfälle.......................................................................................                                                                    | 12                                                                                                    |
| 3.3                                                                                                                | Hauptprofil und Unterprofile ......................................................................                                                                       | 12                                                                                                    |
| 3.4                                                                                                                | Vorgehensweise                                                                                                                                                            | ....................................................................................... 15            |
| 3.5                                                                                                                | Integration in das Gesamtsicherheitskonzept ............................................                                                                                  | 18                                                                                                    |
| 4                                                                                                                  | Geltungsbereich ......................................................................................                                                                    | 19                                                                                                    |
| 4.1                                                                                                                | Zielgruppe (Referenzinstitution) ................................................................                                                                         | 19                                                                                                    |
| 4.2                                                                                                                | Rahmenbedingungen ................................................................................                                                                        | 19                                                                                                    |
| 4.2.1                                                                                                              | Regulierung der Wasserwirtschaft                                                                                                                                          | ............................................................ 19                                       |
| 4.2.2                                                                                                              | Schutz kritischer Infrastrukturen ................................................................                                                                        | 19                                                                                                    |
| 4.2.3                                                                                                              | Regelwerke der Branchenverbände                                                                                                                                           | .......................................................... 20                                         |
| 4.3                                                                                                                | Zugrundeliegende IT-Grundschutz-Vorgehensweise und angestrebtes Schutzniveau ............................................................................................ | 21                                                                                                    |
| 4.4                                                                                                                | ISO 27001-Kompatibilität ..........................................................................                                                                       | 21                                                                                                    |
| 5                                                                                                                  | Abgrenzung des Informationsverbunds ................................................                                                                                      | 22                                                                                                    |
| 5.1                                                                                                                | Organisationsstruktur ................................................................................                                                                    | 22                                                                                                    |
| 5.2                                                                                                                | Geschäftsprozesse und Anlagen ..............................................................                                                                              | 23                                                                                                    |
| 5.3                                                                                                                | Schutzbedarf der Anlagen .........................................................................                                                                        | 24                                                                                                    |
| 5.4                                                                                                                | ICS-Netzstruktur .......................................................................................                                                                  | 26                                                                                                    |

<!-- page: 5 -->

| 6                                 | Generische Referenzarchitektur ............................................................                                                                                                | 29                                                                                                    |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 6.1                               | Generische Zielobjektliste .........................................................................                                                                                       | 29                                                                                                    |
| 6.2                               | Generische Netzpläne                                                                                                                                                                       | .............................................................................. 32                     |
| 6.2.1                             | Legenden                                                                                                                                                                                   | .................................................................................................. 33 |
| 6.2.2                             | Netzpläne                                                                                                                                                                                  | ................................................................................................. 35  |
| 6.3                               | Schutzbedarf der anwendungsfallunabhängigen Zielobjekte .....................                                                                                                              | 39                                                                                                    |
| 7                                 | Anforderungen und Maßnahmen ...........................................................                                                                                                    | 40                                                                                                    |
| 7.1                               | Modellierung der anwendungsfallunabhängigen Zielobjekte .....................                                                                                                              | 40                                                                                                    |
| 7.2                               | Auswahl der Maßnahmen (Anforderungen) am Beispiel des Bausteins .................................................................................................................          | B 1.0 41                                                                                              |
| 7.3                               | Umsetzungsvorgaben ...............................................................................                                                                                         | 43                                                                                                    |
| 8                                 | Risikobehandlung ...................................................................................                                                                                       | 44                                                                                                    |
| 8.1                               | Integration und Realitätsabgleich der Gesamt-Referenzarchitektur ...........                                                                                                               | 44                                                                                                    |
| 8.2                               | Vorgehensweise bei Abweichungen..........................................................                                                                                                  | 45                                                                                                    |
| 8.3                               | Hilfestellungen zur ergänzenden Risikoanalyse ........................................                                                                                                     | 46                                                                                                    |
| 8.3.1                             | Gefährdungsübersicht ...............................................................................                                                                                       | 47                                                                                                    |
| 8.3.2                             | Nicht behandelte Gefährdungen und Restrisiko ........................................                                                                                                      | 49                                                                                                    |
| 8.3.3                             | Risikomatrix ..............................................................................................                                                                                | 51                                                                                                    |
| 9                                 | Anhang A .................................................................................................                                                                                 | 54                                                                                                    |
| 9.1                               | Glossar und Abkürzungsverzeichnis .........................................................                                                                                                | 54                                                                                                    |
| 9.2                               | Literaturverzeichnis ...................................................................................                                                                                   | 59                                                                                                    |
| 10                                | Anhang B (Pilotprofil) .............................................................................                                                                                       | 62                                                                                                    |
| 10.1                              | Maßnahmenauswahltabellen ....................................................................                                                                                              | 62                                                                                                    |
| 10.1.1                            | Baustein B 1.0 ..........................................................................................                                                                                  | 62                                                                                                    |
| 10.2                              | Gefährdungstabellen .................................................................................                                                                                      | 63                                                                                                    |
| 10.2.1                            | Baustein B 1.0 ..........................................................................................                                                                                  | 63                                                                                                    |
| 10.3                              | Nicht berücksichtigte Gefährdungen .........................................................                                                                                               | 64                                                                                                    |
| 11                                | Anhang C (Pilotprofil) .............................................................................                                                                                       | 65                                                                                                    |
| 11.1                              | Allgemeine Methodik für die Profilerstellung ..............................................                                                                                                | 65                                                                                                    |
| 11.2                              | Methodik zur Berücksichtigung von Variationen in der Referenzarchitektur ................................................................................................................. | 67                                                                                                    |
| 11.3                              | Orientierungshilfe für die Zuordnung von Maßnahmentypen zu den Unterprofilen .............................................................................................                 | 69                                                                                                    |
| 11.3.1 Hauptprofil (Organisation) |                                                                                                                                                                                            | ......................................................................... 70 70                       |
| 11.3.2                            | Unterprofil AR (Architektur) .......................................................................                                                                                       |                                                                                                       |
| 11.3.3 Unterprofil NM             | (Netzmanagement) ...........................................................                                                                                                               | 71                                                                                                    |
| 11.3.4                            | Unterprofil UA (Benutzerzugang)                                                                                                                                                            | .............................................................. 72                                     |
| 11.3.5                            | Unterprofil PA (Programmzugriff) ..............................................................                                                                                            | 72                                                                                                    |
| 11.3.6                            | Unterprofil PLC (SPS-Programmierung und -Wartung)                                                                                                                                          | ............................. 73                                                                      |

<!-- page: 6 -->

## Abbildungsverzeichnis

| Abb. 2.1: Vorgehensschritte bei der Anwendung des Profils ................................                                                                                                                                                |   10 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| Abb. 3.1: Legende zur Anwendung des IT-Grundschutz-Profils: Unterstützende Dokumente ........................................................................................                                                             |   15 |
| Abb. 3.2: Vorgehensweise für die Anwendung des IT-Grundschutz-Profils ..........                                                                                                                                                          |   16 |
| Abb. 5.1: Verteilte ICS-Netzstruktur .....................................................................                                                                                                                                |   27 |
| Abb. 5.2: Konzentrierte ICS-Netzstruktur .............................................................                                                                                                                                    |   27 |
| Abb. 5.3: Gemischte ICS-Netzstruktur .................................................................                                                                                                                                    |   28 |
| Abb. 6.1: Legende zu physischen Netzplänen: Komponenten, Einordnung der Komponenten in die Automatisierungspyramide und Verbindungen der Komponenten .................................................................................... |   33 |
| Abb. 6.2: Legende zu logischen Netzplänen: Anwendungen und Datenübermittlung ..........................................................................................................                                                   |   35 |
| Abb. 6.3: Physischer Netzplan der generischen Referenzarchitektur ...................                                                                                                                                                     |   36 |
| Abb. 6.4: Logischer Netzplan der generischen Referenzarchitektur .....................                                                                                                                                                    |   37 |
| Abb. 8.1: Vorgehensweise bei Abweichung der ICS-Anlagen des Profilanwenders von den im Profil wählbaren Referenzarchitekturen ...........................                                                                                 |   45 |
| Abb. 8.2: Allgemeine Risikomatrix (angelehnt an [BSI16c]) .................................                                                                                                                                               |   51 |
| Abb. 8.3: Risikomatrix für die Wasserwirtschaft (angelehnt an [B3S17b]) ............                                                                                                                                                      |   52 |
| Abb. 12.1: Methodik zur Erstellung eines IT-Grundschutz-Profils nach Vorbild des Pilotprofils ..........................................................................................                                                  |   66 |
| Abb. 12.2: Methodik für die Berücksichtigung von Variationsmöglichkeiten in der Referenzarchitektur anhand von Anwendungsfällen ..........................                                                                                |   68 |

<!-- page: 7 -->

## Tabellenverzeichnis

| Tab. 3.1: Verteilung der Inhalte auf das Hauptprofil und die Unterprofile..............                                                                                   | 13                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Tab. 3.2: Übersicht über alle Unterprofile (Anwendungsfallgruppen) und die darin enthaltenen Anwendungsfälle ............................................................ | 14                                                                                                                                 |
| Tab. 3.3: Aufbau der Zielobjekt-Maßnahmen-Tabelle                                                                                                                         | .......................................... 17                                                                                      |
| Tab. 5.1: Geschäftsprozesse in der Wasserversorgung .......................................                                                                               | 23                                                                                                                                 |
| Tab. 5.2: Geschäftsprozesse in der Abwasserbeseitigung ...................................                                                                                | 23                                                                                                                                 |
| Tab. 6.1: Generische Zielobjektliste .....................................................................                                                                | 30                                                                                                                                 |
| Tab. 6.2: Schutzbedarfstabelle für die anwendungsfallunabhängigen Zielobjekte                                                                                             | 39                                                                                                                                 |
| Tab. 7.1: Modellierungstabelle für die anwendungsfallunabhängigen Zielobjekte                                                                                             | 40                                                                                                                                 |
| Tab. 7.2: Maßnahmenauswahl für den Baustein B 1.0: Sicherheitsmanagement .                                                                                                | 42                                                                                                                                 |
| Tab. 7.3: Begründung der Nichtauswahl von Maßnahmen für den Baustein B 1.0                                                                                                | 43                                                                                                                                 |
| Tab. 8.1: Ergänzung von Gefährdungen in der Zielobjekt-Maßnahmen-Tabelle...                                                                                               | 47                                                                                                                                 |
| Tab. 8.2: Gefährdungstabelle für den Baustein B 1.0: Sicherheitsmanagement ...                                                                                            | 48                                                                                                                                 |
| Tab. 10.1: Maßnahmenauswahltabelle für den Baustein B 1.0: Sicherheitsmanagement ....................................................................                     | 62                                                                                                                                 |
| Tab. 10.2: Gefährdungstabelle für den Baustein B 1.0: Sicherheitsmanagement .                                                                                             | 63                                                                                                                                 |
| Tab. 10.3: Liste nicht berücksichtigter Gefährdungen 3.302                                                                                                                | für die Bausteine B 1.0 und B ................................................................................................. 64 |

<!-- page: 8 -->

## Vorbemerkungen

Das vorliegende IT-Grundschutz-Profil in der Version 1.0 ist im Rahmen einer Masterarbeit entstanden. Die Lektüre der Masterarbeit ist zur Verwendung des Profils nicht notwendig.

Bei Interesse können jedoch Überlegungen, Hintergründe und Entscheidungen, die während der Erstellung des IT-Grundschutz-Profils eine Rolle gespielt haben, in der Masterarbeit nachgelesen werden. Sie ist als Hintergrundlektüre zum vorliegenden IT-Grundschutz-Profil zu verstehen, trägt den Titel 'Erstellung eines IT-Grundschutz-Profils für ein Referenzunternehmen mit automatisierter Prozesssteuerung' und ist beim BSI frei erhältlich.

Das IT-Grundschutz-Profil ist mit 'IT-Grundschutz-Pilotprofil bzw. IT-Grundschutz-Profil für die Wasserwirtschaft' benannt. Der Grund für den doppelten Titel ist der doppelte Zweck des Profils:

Als IT-Grundschutz-Pilotprofil ist es frei erhältlich und soll als Blaupause für die Erstellung weiterer IT-Grundschutz-Profile dienen. Es enthält keine komplette Maßnahmenempfehlung (verkürzter Anhang B), sondern zeigt die Struktur und Grundideen eines Profils an einigen Beispielen auf. Dafür enthält das Pilotprofil einen zusätzlichen Anhang C mit Hilfestellungen und Methoden, um auf Basis des Pilotprofils Profile für weitere Anwendergruppen zu erstellen.

Das IT-Grundschutz-Profil für die Wasserwirtschaft besteht aus dem frei erhältlichen Pilotprofil und einem kostenpflichtigen Anhang (kompletter Anhang B). Es enthält Empfehlungen für eine Informationssicherheitskonzeption für Institutionen der Wasserwirtschaft und basiert auf dem branchenspezifischen Sicherheitsstandard Wasser / Abwasser (B3S WA) gemäß § 8a (2) BSIG [BSIG16].

Der B3S WA wurde von den Branchenverbänden DWA 1  und DVGW 2  zur Feststellung der Eignung beim BSI eingereicht. Nach seiner Genehmigung durch das BSI können durch die Anwendung des B3S WA auf den Sektor Wasser die Mindestanforderungen für IT-Sicherheit gemäß § 8a (1) BSIG erfüllt werden. Da sich der der B3S WA während der Niederschrift dieser Masterarbeit noch in der Prüfungsphase beim BSI befand, steht auch für das Profil für die Wasserwirtschaft die Genehmigung noch aus.

Das Profil besteht aus einem Hauptprofil und perspektivisch fünf Unterprofilen. Das Hauptprofil sowie das Unterprofil Architektur (AR) wurden im Rahmen der Masterarbeit erstellt.

Der IT-Grundschutz befand sich zur Zeit der Niederschrift der Masterarbeit im Umbruch. Das IT-Grundschutz-Profil ist ein Konzept des modernisierten IT-Grundschutzes; allerdings war der Modernisierungsprozess zum Zeitpunkt der Niederschrift noch nicht abgeschlossen. Wo möglich, werden Begrifflichkeiten, Konzepte und Inhalte des modernisierten IT-Grundschutzes verwendet. Jedoch muss das Profil die bisherigen, noch nicht modernisierten IT-Grundschutz-Bausteine zurückgreifen, um Maßnahmen zu empfehlen.

1  Deutsche Vereinigung für Wasserwirtschaft, Abwasser und Abfall

2  Deutscher Verein des Gas- und Wasserfachs

<!-- page: 9 -->

Sobald die modernisierten Bausteine zur Verfügung stellen, sollten die bisherigen Bausteine mit Hilfe von Migrationstabellen ersetzt werden. Damit geht auch eine Anpassung der Begrifflichkeiten einher: Statt Maßnahmen werden in den modernisierten Bausteinen Anforderungen empfohlen.

<!-- page: 10 -->

## 1 Formale Aspekte

## 1.1 Titel

Pilotprofil - Hauptprofil

bzw.

Leittechnische Netze in der Wasserversorgung und Abwasserbeseitigung ( Wasserwirtschaft )

- Hauptprofil

## 1.2 Autor und Verantwortliche/r

Sarah Fluchs, RWTH Aachen Holger Schildt, BSI

## 1.3 Versionsstand und Revisionszyklus

Version 1.0 vom 18.06.2017

## 1.4 Vertraulichkeit

Pilotprofil : Öffentlich, mit verkürztem Anhang B (Pilotprofil) und zusätzlichem Anhang C

Wasserwirtschaft

: Nicht öffentlich, mit vollständigem Anhang B (Wasserwirtschaft)

## 1.5 Status der BSI-Anerkennung

Anerkennung wird noch geprüft.

<!-- page: 11 -->

## 2 Management Summary

## 2.1 Zielgruppe

Dieses IT-Grundschutz-Profil richtet sich an Institutionen aller öffentlich-rechtlichen und privatrechtlichen Betriebsformen, die in der Wasserwirtschaft tätig sind. Unter dem Begriff Wasserwirtschaft werden in diesem Profil Institutionen zusammengefasst, die Dienstleistungen innerhalb der Wasserversorgung und der Abwasserbeseitigung erbringen.

## 2.2 Zielsetzung

Der Fokus dieses Profils liegt auf der Absicherung von industriellen Netzen, also der Prozessleittechnik und Automatisierungstechnik. Büro-Netze werden nur unter dem Gesichtspunkt der von ihnen ausgehenden Gefährdungen für die industriellen Netze berücksichtigt.

Es werden Maßnahmen zur Absicherung industrieller Netze empfohlen. Für Anlagen, die nach BSI-KritisV [KritisV16] zu den kritischen Infrastrukturen gehören, werden zusätzliche Maßnahmen gewählt.

Das Profil ist in ein Hauptprofil und mehrere Unterprofile gegliedert. Das vorliegende Hauptprofil enthält Informationen zur allgemeinen Vorgehensweise des Profils, zum Geltungsbereich und zur Risikobehandlung sowie Maßnahmenempfehlungen für Organisation und Management. Die Unterprofile dienen der individuellen Anpassung des Profils an die leittechnische Infrastruktur des Profilanwenders und enthalten jeweils Maßnahmenempfehlungen für einen Teilbereich des industriellen Netzes.

## 2.3 Inhalte

Abb. 2.1 gibt eine Übersicht über die Anwendung des Profils. Blau umrandete Schritte erfolgen mit Hilfe des Hauptprofils, grün umrandete sind in den Unterprofilen enthalten. Das vorliegende Hauptprofil erläutert die Auswahl der betrachteten Geschäftsprozesse und Anlagen (Schritt 1), die Schutzbedarfszuweisung für die Anlagen (2), die Auswahl der ICS-Netzstruktur (3) und die Integration und den Realitätsabgleich (6) nach Durcharbeiten aller Unterprofile. Es enthält zudem Informationssicherheitsempfehlungen (5), die Organisation und Management betreffen. Diese Empfehlungen sind von der Anpassung in den Unterprofilen unabhängig und gelten für jeden Profilanwender.

In Abschnitt 3 werden die einzelnen Schritte genauer erläutert.

<!-- page: 12 -->

Abb. 2.1: Vorgehensschritte bei der Anwendung des Profils

<!-- image -->

<!-- page: 13 -->

## 3 Anwendung des IT-Grundschutz-Profils

## 3.1 Begriffsklärung zum IT-Grundschutz und IT-Grundschutz-Profil

Die folgenden  und  weitere  für  das  vorliegende  Profil  relevante  Begriffsdefinitionen  sind  im Glossar (Anhang A, Abschnitt 9.1) gesammelt.

Institution:

Oberbegriff für Unternehmen und Behörden.

Geltungsbereich: Der Geltungsbereich des IT-Grundschutz-Profils legt die Zielgruppe fest. Dazu kann mittels einer Referenzinstitution eine typische Institution der Zielgruppe skizziert werden. Auch die Rahmenbedingungen sollten spezifiziert werden.

Informationsverbund: Es  muss  abgegrenzt  werden,  welche  Geschäftsprozesse  der  Zielgruppe das IT-Grundschutz-Profil betrachten soll. Der Informationsverbund bezeichnet die Gesamtheit von infrastrukturellen, organisatorischen, personellen und technischen Komponenten, die für die Ausführung dieser betrachteten Geschäftsprozesse nötig sind.

Referenzarchitektur: Eine  typische  Architektur  des  abgegrenzten  Informationsverbunds. Eine Referenzarchitektur besteht aus Zielobjekten und einem oder mehreren Netzplänen.

Zielobjekt: Zielobjekte sind die IT-Systeme, Infrastruktur, Anwendungen und Netzkomponenten, die zum Informationsverbund gehören und im Rahmen des Profils abgesichert werden sollen.

Modellierung: Modellierung ist die Zuordnung von mindestens einem IT-Grundschutz-Baustein zu jedem Zielobjekt. Da die Bausteine Anforderungen enthalten, impliziert die Modellierung eine Auswahl von Anforderungen für die Zielobjekte eines Informationsverbunds. Im Rahmen eines Profils müssen nicht alle Anforderungen eines Bausteins ausgewählt werden.

Maßnahme: Anforderungen werden durch Maßnahmen erfüllt. Im bisherigen IT-Grundschutz enthielten die Bausteine keine Anforderungen, sondern direkt Maßnahmen. Im modernisierten IT-Grundschutz können konkrete Maßnahmen zu den Anforderungen eines Bausteins in Umsetzungshinweisen gegeben sein.

Dieses Profil soll perspektivisch mit den Bausteinen des modernisierten IT-Grundschutzes arbeiten. Da zum Zeitpunkt der Profilerstellung jedoch die Überarbeitung der IT-Grundschutz-Bausteine noch nicht abgeschlossen war, werden beispielhaft alte Bausteine verwendet.

<!-- page: 14 -->

## 3.2 Anwendungsfälle

Das vorliegende Profil soll für alle Institutionen in der Wasserwirtschaft anwendbar sein (für eine genauere Definition des Geltungsbereichs siehe Abschnitt 4). Die ICS-Netze von Institutionen der Wasserwirtschaft sind relativ homogen. Dennoch gibt es im Detail Unterschiede, die Einfluss auf die Empfehlung geeigneter Sicherheitsanforderungen und -maßnahmen haben. Um einer möglichst breiten Palette von Anwenderinstitutionen gerecht zu werden, bietet dieses Profil die Möglichkeit der individuellen Anpassung.

Um diese Anpassung möglichst aufwandsarm und intuitiv zu gestalten, wird auf Anwendungsfälle  zurückgegriffen.  Anwendungsfälle  beschreiben  bestimmte  Einsatzszenarien  der  ICS-Netze. Für dieses Profil wurde auf Anwendungsfälle zurückgegriffen, die die American Wastewater Association (AWWA) entwickelt hat [AWWA14]. Sie gliedern sich in fünf Anwendungsfallgruppen, die nach dem Teilaspekt benannt sind, den sie behandeln. Die Anwendungsfälle in den Gruppen stellen Variationen dieser namensgebenden Aspekte dar:

- Architektur (Architecture, AR ),
- Netzmanagement (Network Management, NM ),
- Benutzerzugang (User Access, UA ),
- Programmzugriff (Program Access, PA ) und
- SPS-Programmierung und -Wartung (PLC Programming and Maintenance, PLC ).

## 3.3 Hauptprofil und Unterprofile

Das IT-Grundschutz-Profil besteht aus einem Hauptprofil und fünf Unterprofilen. Ein Unterprofil umfasst jeweils eine der oben genannten Anwendungsfallgruppen. Tab. 3.1 gibt eine Übersicht über die Verteilung der Profilinhalte auf das Hauptprofil und die Unterprofile.

Die Unterprofile (UP) sind Teilprofile, die sich nur mit einem Aspekt des Informationsverbunds befassen. Innerhalb eines Unterprofils werden in Form von Anwendungsfällen Variationen dieses Aspekts vorgestellt. Die maßgeblichen Abschnitte der Unterprofile sind die Abschnitte UP6 und UP7: Der Anwender des Profils sucht in Abschnitt UP6 (Referenzarchitektur) die für ihn zutreffenden Anwendungsfälle aus (in der Regel mindestens einen pro Unterprofil) und erhält eine dazu passende spezifische Referenzarchitektur, bestehend aus einer spezifischen Zielobjektliste und einem spezifischen Netzplan. Im selben Abschnitt erfolgt - auf Basis der spezifischen Referenzarchitektur - die Schutzbedarfsfeststellung der einzelnen Zielobjekte. Abschnitt UP7 (Anforderungen und Maßnahmen) enthält die Modellierung der spezifischen Referenzarchitekturen mit IT-Grundschutz-Bausteinen und eine Liste der für den Anwendungsfall relevanten Anforderungen.

Im übergeordneten Hauptprofil (HP) finden sich alle Inhalte, die für jeden Profilanwender relevant sind. Es bereitet den Anwender auf die Anpassung des Profils an seine Anlagen vor und hilft ihm bei der anschließenden Überführung aller in den Unterprofilen ausgewählten Anwendungsfälle in ein vollständiges Sicherheitskonzept. Das Hauptprofil enthält dazu die Abschnitte 1 (Formale Aspekte), 2 (Management Summary), 3 (Anwendung des Profils), 4 (Geltungsbereich), 5 (Abgrenzung des Informationsverbunds) und 8 (Risikobehandlung). Außerdem wird im Abschnitt 6 (Referenzarchitektur) eine generische Referenzarchitektur, bestehend aus einer generischen Zielobjektliste und einem generischen Netzplan, gegeben, die die Grundlage für die Anwendungsfallauswahl darstellt.

<!-- page: 15 -->

Sicherheitsmaßnahmen, die Organisation und Management betreffen, werden im Hauptprofil behandelt, weil sie anwendungsfallunabhängig und architekturunabhängig sind und somit keine spezifischen Referenzarchitekturen erfordern. Konkret bedeutet dies, dass die Modellierung und die Auswahl geeigneter Maßnahmen für die Zielobjekte der Kategorie Organisation im Hauptprofil erfolgt, und zwar im Abschnitt 7 (Anforderungen und Maßnahmen).

Tab. 3.1: Verteilung der Inhalte auf das Hauptprofil und die Unterprofile

|      | Hauptprofil                                               |      |        | Unterprofile                              |
|------|-----------------------------------------------------------|------|--------|-------------------------------------------|
|    1 | Formale Aspekte                                           | UP1  |        | Formale Aspekte                           |
|    2 | Management Summary                                        | UP2  |        | Management Summary                        |
|    3 | Anwendung des Profils                                     |      |        |                                           |
|    4 | Geltungsbereich                                           |      |        |                                           |
|    5 | Abgrenzung des Informationsverbunds                       |      |        |                                           |
|    6 | Generische Referenzarchitektur                            | UP6  |        | Spezifische Referenzarchitektur           |
|  6.1 | Generische Zielobjektliste                                |      | UP6.1  | Spezifische Zielobjektlisten              |
|  6.2 | Generische Netzpläne                                      |      | UP6.2  | Spezifische Netzpläne                     |
|  6.3 | Schutzbedarf der anwendungsfallunabhängigen Ziel- objekte |      | UP6.3  | Schutzbedarf der spezifischen Zielobjekte |
|    7 | Anforderungen und Maßnahmen                               | UP7  |        | Anforderungen und Maßnahmen               |
|  7.1 | Modellierung der anwendungsfallunabhängigen Ziel- objekte |      | UP7.1  | Modellierung der spezifischen Zielobjekte |
|  7.2 | Auswahl der Anforderungen                                 |      | UP7.2  | Auswahl der Anforderungen                 |
|  7.3 | ggf. Umsetzungsvorgaben                                   |      | UP7.3  | ggf. Umsetzungsvorgaben                   |
|    8 | Risikobehandlung                                          |      |        |                                           |
|    9 | Anhang A                                                  | UP9  |        | Anhang A                                  |
|  9.1 | Glossar                                                   |      | UP9.1  | Glossar                                   |
|  9.2 | Literaturverzeichnis                                      |      | UP9.2  | Literaturverzeichnis                      |
|   10 | Anhang B                                                  | UP10 |        | Anhang B                                  |
| 10.1 | Maßnahmenauswahltabellen                                  |      | UP10.1 | Maßnahmenauswahltabellen                  |
| 10.2 | Gefährdungstabellen                                       |      | UP10.2 | Gefährdungstabellen                       |
| 10.3 | Nicht berücksichtigte Gefährdungen                        |      |        |                                           |

<!-- page: 16 -->

Eine Übersicht über alle Unterprofile und die Anwendungsfälle, die in den Unterprofilen zur Auswahl stehen, gibt Tab. 3.2. Zu jeder Anwendungsfallgruppe sind sowohl das Kürzel als auch die ursprüngliche (englischsprachige) AWWA-Bezeichnung als auch die deutsche, für die Unterprofiltitel verwendete Bezeichnung angegeben. Die Anwendungsfälle sind unter Verwendung des Kürzels ihres Unterprofils nummeriert.

Tab. 3.2: Übersicht über alle Unterprofile (Anwendungsfallgruppen) und die darin enthaltenen Anwendungsfälle

| Kürzel   | Unterprofil-Bezeichnung                                | AWWA-Bezeichnung                                       |
|----------|--------------------------------------------------------|--------------------------------------------------------|
| AR       | Architektur                                            | Architecture                                           |
| AR1      | Dediziertes ICS-Netz                                   | Dediziertes ICS-Netz                                   |
| AR2      | Gemeinsames WAN                                        | Gemeinsames WAN                                        |
| AR3      | Gemeinsames LAN                                        | Gemeinsames LAN                                        |
| NM       | Netzmanagement                                         | Network Management & System Support                    |
| NM1      | Lokales, individuelles Netzmanagement                  | Lokales, individuelles Netzmanagement                  |
| NM2      | Lokales, zentralisiertes Netzmanagement                | Lokales, zentralisiertes Netzmanagement                |
| NM3      | Fern-Netzmanagement                                    | Fern-Netzmanagement                                    |
| UA       | Benutzerzugang                                         | User Access                                            |
| UA1      | Systemzugriff vom Leitstand aus                        | Systemzugriff vom Leitstand aus                        |
| UA2      | Systemzugriff von der Anlage aus                       | Systemzugriff von der Anlage aus                       |
| UA3      | Fernzugriff                                            | Fernzugriff                                            |
| UA4      | Rein lesender Fernzugriff                              | Rein lesender Fernzugriff                              |
| UA5      | Rein lesender Fernzugriff im Webbrowser                | Rein lesender Fernzugriff im Webbrowser                |
| PA       | Programmzugriff                                        | Programm Access                                        |
| PA1      | Automatisiertes Senden von Nachrichten                 | Automatisiertes Senden von Nachrichten                 |
| PA2      | Interaktives Senden von Dateien                        | Interaktives Senden von Dateien                        |
| PA3      | Interaktives Empfangen von Dateien                     | Interaktives Empfangen von Dateien                     |
| PA4      | Automatisierte Software-Updates                        | Automatisierte Software-Updates                        |
| PA5      | Automatisierter Datenaustausch                         | Automatisierter Datenaustausch                         |
| PA6      | Automatisierter Datenaustausch für das Netzmanagement  | Automatisierter Datenaustausch für das Netzmanagement  |
| PLC      | SPS-Programmierung und -War- tung                      | PLC Programming and Maintenance                        |
| PLC1     | Lokale, individuelle SPS-Programmierung und -Wartung   | Lokale, individuelle SPS-Programmierung und -Wartung   |
| PLC2     | Lokale, zentralisierte SPS-Programmierung und -Wartung | Lokale, zentralisierte SPS-Programmierung und -Wartung |
| PLC3     | SPS-Fernprogrammierung und -Fernwartung                | SPS-Fernprogrammierung und -Fernwartung                |

<!-- page: 17 -->

## 3.4 Vorgehensweise

In Abb. 3.2 wird ein Fließbild gegeben, in dem die Vorgehensweise für die Anwendung des IT-Grundschutz-Profils dargestellt ist. Darin ist durch farbige Umrandung gekennzeichnet, ob der betreffende Anwendungsschritt mit Hilfe des Hauptprofils (blau) oder Unterprofils (grün) erfolgt.

Die Herkunft konkreter verwendeter Dokumente (Tabellen, Listen, Abbildungen oder Erklärungen) ist durch bunte Schriftfarbe gekennzeichnet. Außer Dokumenten aus dem Haupt- und Unterprofil werden auch solche aus dem IT-Grundschutz verwendet (orange). Einige Dokumente müssen vom Anwender selbst erstellt werden (grau). Dokumente mit Inhalten aus dem branchenspezifischen Sicherheitsstandard für die Wasserwirtschaft (B3S WA) sind mit einem roten [B3S WA] versehen - sie fallen unter die Sperrklausel und sind im Pilotprofil nur exemplarisch enthalten. Die vollständige Legende der farblichen Kennzeichnung ist in Abb. 3.1 gegeben.

Schritt erfolgt mit Hilfe des Hauptprofils.

Schritt erfolgt mit Hilfe der Unterprofile.

Dokument im Hauptprofil vorhanden.

Dokument im Unterprofil vorhanden.

Dokument im allgemeinen IT-Grundschutz vorhanden.

Dokument wird vom Profilanwender erstellt.

[B3S WA] = Dokument beinhaltet Informationen aus dem branchenspezifischen Sicherheitsstandard Wasser / Abwasser

Abb. 3.1: Legende zur Anwendung des IT-Grundschutz-Profils: Unterstützende Dokumente

Der  erste  Schritt  bei  der  Anwendung  des  IT-Grundschutz-Profils  ist  die  Auswahl  der Geschäftsprozesse und Anlagen der eigenen Institution, die durch das Profil abgedeckt werden sollen. Dabei hilft Abschnitt 5 des Hauptprofils.

Danach folgt im zweiten Schritt eine Schutzbedarfszuweisung für die betrachteten Anlagen. Diese wird im IT-Grundschutz-Profil in Analogie zur Unterscheidung zwischen KRITIS- und Nicht-KRITIS-Anlagen in der BSI-KritisV [KritisV16] vorgenommen. Genauere Erläuterungen gibt Abschnitt 5.3 des Hauptprofils.

Der dritte und vierte Schritt dienen der genaueren Erfassung der ICS-Anlagenstruktur der eigenen Institution in einer Referenzarchitektur. Dazu wird zunächst die grundlegende ICS-Netzstruktur ausgewählt, die der eigenen Anlage am nächsten kommt. Dies kann eine verteilte oder konzentrierte Struktur sein oder auch eine Mischung aus beiden. Die Beschreibung der ICS-Netzstrukturtypen erfolgt in Abschnitt 5.4 des Hauptprofils.

<!-- page: 18 -->

Abb. 3.2: Vorgehensweise für die Anwendung des IT-Grundschutz-Profils

<!-- image -->

Im vierten Schritt folgt die Auswahl der zutreffenden Anwendungsfälle für die eigene Institution, sodass die Details der Referenzarchitektur angepasst werden können. Die Anwendungsfälle sind in Unterprofile gruppiert, die jeweils einen Aspekt der Gesamtanlage abdecken. In der Regel sollte aus jedem Unterprofil mindestens ein Anwendungsfall ausgewählt werden. Dabei hilft Abschnitt UP6 der Unterprofile. Für jeden Anwendungsfall wird im Unterprofil eine Referenzarchitektur, bestehend aus einer Zielobjektliste und einem Netzplan gegeben. In der Schutzbedarfstabelle wird jedem Zielobjekt ein Schutzbedarf zugewiesen.

<!-- page: 19 -->

Im fünften Schritt folgt die Erfassung der Informationssicherheitsempfehlungen für die an die eigene Institution angepasste Referenzarchitektur: In jedem Unterprofil gibt es eine Modellierungstabelle, die den Zielobjekten passende IT-Grundschutz-Bausteine zuordnet. Maßnahmenauswahltabellen  geben für  jeden  Baustein  -  in  Abhängigkeit  von  Anwendungsfall  und Schutzbedarf - eine Auswahl der relevanten Anforderungen (bisheriger IT-Grundschutz: Maßnahmen) an.

Die Informationen des vierten und fünften Schritts sollten in einer Zielobjekt-Maßnahmen-Tabelle gesammelt werden. Am Ende der Profilanwendung enthält diese Tabelle in strukturierter Form alle relevanten Informationen für die Maßnahmenumsetzung und potenzielle Risikoanalysen. Ihr Aufbau ist in Tab. 3.3 erklärt.

Tab. 3.3: Aufbau der Zielobjekt-Maßnahmen-Tabelle

| Zielobjekt                                                                                                                                    | Anwendungsfall                                                                                                | Baustein                                                               | Anforderung (Maßnahme)                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 1) Aus den spezifi- schen Zielobjektlis- ten : Alle relevanten Zielobjekte 1b) Aus den Schutz- bedarfstabellen : Schutzbedarf der Zielobjekte | 1) Aus den spe- zifischen Ziel- objektliste n: Alle Anwen- dungsfälle, in denen die Ziel- objekte vor- kommen | 2) Aus den Modellie- rungstabellen : Bau- steine für die Zielob- jekte | 3) Aus den Maßnahmen- auswahltabellen : Maßnah- men, die für jeden Baustein (also jedes Zielobjekt) emp- fohlen sind |

Der sechste Schritt besteht aus einer Integration der Referenzarchitekturen aus den Unterprofilen und einem Realitätsabgleich. Dabei unterstützt Abschnitt 8.1 des Hauptprofils. Zuerst wird die Zielobjekt-Maßnahmen-Tabelle unter Berücksichtigung der anwendungsfallunabhängigen Zielobjekte aus dem Hauptprofil komplettiert. Mit Hilfe der anwendungsfallspezifischen Netzpläne wird ein Gesamt-Netzplan erstellt. Damit sind alle Voraussetzungen für den anschließenden Realitätsabgleich geschaffen, dessen Ziel eine Überprüfung ist: Sind alle relevanten  Zielobjekte  der  eigenen  ICS-Anlage  in  der  Zielobjekt-Maßnahmen-Tabelle  erfasst? Sind für alle Zielobjekte alle relevanten Gefährdungen berücksichtigt?

Ist dies nicht der Fall, muss das Profil ergänzt werden. Dies kann durch Modifikation eines bestehenden Anwendungsfalls oder Ergänzung eines neuen Anwendungsfalls erfolgen, falls der IT-Grundschutz passende Bausteine enthält. Decken die IT-Grundschutz-Bausteine die fehlenden Zielobjekte oder Gefährdungen nicht ab, kann eine ergänzende Risikoanalyse nach BSI-Standard 200-3 durchgeführt werden. Detaillierte Informationen zur Ergänzung des IT- Grundschutz-Profils enthält Abschnitt 8.2 des Hauptprofils. Abschnitt 0 gibt einige Hilfestellungen für den Fall, dass eine ergänzende Risikoanalyse erforderlich ist.

<!-- page: 20 -->

Der letzte Schritt gehört nicht mehr zur Anwendung des Profils im engeren Sinne. Er umfasst die (Auswahl und) Umsetzung von Maßnahmen, die die ermittelten Anforderungen erfüllen können. Dabei können die Umsetzungshinweise des BSI unterstützen; es können jedoch auch Umsetzungsvorgaben für einzelne Maßnahmen im Abschnitt UP7.3 des zugehörigen Unterprofils angegeben sein.

## 3.5 Integration in das Gesamtsicherheitskonzept

Die im Zuge des vorliegenden Profils ermittelten Anforderungen (Maßnahmen) sind in das Gesamtsicherheitskonzept zu integrieren und im Zuge der Realisierungsplanung umzusetzen.

<!-- page: 21 -->

## 4 Geltungsbereich

## 4.1 Zielgruppe (Referenzinstitution)

Dieses IT-Grundschutz-Profil richtet sich an Institutionen aller öffentlich-rechtlichen und privatrechtlichen Betriebsformen, die in der Wasserwirtschaft tätig sind. Unter dem Begriff Wasserwirtschaft werden in diesem Profil Institutionen zusammengefasst, die Dienstleistungen innerhalb der Branchen 'Öffentliche Wasserversorgung' und 'Öffentliche Abwasserbeseitigung' erbringen.

Der Fokus dieses Profils liegt dabei auf den industriellen Netzen, also der Prozessleittechnik und Automatisierungstechnik. Büro-Netze werden nur unter dem Gesichtspunkt der von ihnen ausgehenden Gefährdungen für die industriellen Netze berücksichtigt. In Abgrenzung zur in gewöhnlichen Büros üblichen Informationstechnik (IT oder Office-IT), wird die Informationstechnik in industriellen Netzen auch Operational Technology (OT) genannt.

## 4.2 Rahmenbedingungen

## 4.2.1  Regulierung der Wasserwirtschaft

Die Wasserversorgung und Abwasserbeseitigung gehören zu der grundlegenden Daseinsvorsorge eines Staates; daher unterliegen sie staatlichen Regulierungen. Die EU-Trinkwasserrichtlinie  (98/83/EG,  [TWRL98])  und  die  EU-Kommunalabwasserrichtlinie  (91/271/EWG, [AWRL91]) legen Mindeststandards zur Trinkwasserqualität und zur Abwasserreinigung fest. Mit  der  Trinkwasserverordnung (TrinkwV 2001, [TrinkwV01]) und der Abwasserverordnung (AbwV, [AbwV97]) sind sie in deutsches Recht umgesetzt. Die EU-Wasserrahmenrichtlinie (2000/60/EG, [WRRL00]) macht Zielvorgaben für die Qualität der Gewässer, die die Wasserwirtschaft als Quellen nutzt und in die sie die gereinigten Abwässer einleitet. Ihre Umsetzung in nationales Recht findet sich im Wasserhaushaltsgesetz (WHG, [WHG09]). Die Ausführung dieser Verordnungen liegt in der Verantwortung der Kommunen.

Dieses IT-Grundschutz-Profil berücksichtigt bei der Schutzbedarfsfeststellung die Rahmenbedingungen nach dem deutschem Recht, die in der TrinkwV, der AbwV und dem WHG festgelegt werden.

## 4.2.2  Schutz kritischer Infrastrukturen

Die Wasserversorgung und Abwasserbeseitigung zählen laut der Nationalen Strategie zum Schutz Kritischer Infrastrukturen (KRITIS-Strategie, [BMI09]) zu den kritischen Infrastrukturen (KRITIS). Seit Juli 2015 gilt das IT-Sicherheitsgesetz (IT-SiG, [IT-SiG15]), das KRITIS-Betreiber verpflichtet, ihre kritischen Dienstleistungen nach dem Stand der Technik angemessen abzusichern und dies mindestens alle zwei Jahre überprüfen zu lassen. Auch die Meldung von IT-Sicherheitsvorfällen schreibt das Gesetz vor.

<!-- page: 22 -->

Mitglieder einer KRITIS-Branche können gemäß § 8a (2) BSIG [BSIG16] selbst branchenspezifische IT-Sicherheitsstandards (B3S) entwickeln, um die vorgeschriebene Absicherung nach dem Stand der Technik für ihre Mitglieder zu erleichtern [BSI16a]. Das BSI kann dabei auf Anfrage beratend tätig sein.  Für die Wasserwirtschaft haben die Deutsche Vereinigung für Wasserwirtschaft, Abwasser und Abfall e.V. (DWA) und der Deutsche Verein des Gas- und Wasserfaches e.V. (DVGW) einen solchen B3S bereits entwickelt [B3S17b; B3S17a; B3S17c].

Dieses IT-Grundschutz-Profil soll die Absicherung nach Stand der Technik, wie im IT-SiG vorgeschrieben, erleichtern. Es basiert auf den Inhalten des B3S WA.

Die Vorgaben des IT-SiG gelten nur für Institutionen, die in der Verordnung zur Bestimmung kritischer Infrastrukturen (BSI-KritisV, [KritisV16]) festgelegte Schwellenwerte überschreiten. Für Wasserversorger liegt dieser Schwellenwert bei einer verarbeiteten Wassermenge von 22 m³/Jahr, für Abwasserbeseitiger bei einer Ausbaugroße von 500 000 Einwohnern bzw. Einwohnerwerten 3 . Die Mehrheit der Institutionen in der Wasserwirtschaft betreibt Anlagen, die deutlich kleiner sind.

Trotzdem soll dieses IT-Grundschutz-Profil sich gerade auch an diese kleineren Institutionen richten. Auch wenn diese bislang nicht gesetzlich zur IT-Sicherheit verpflichtet sind, so haben sie doch - wenn auch in kleineren Maßstäben - dieselben technischen Infrastrukturen und damit dieselben Probleme mit der Informationssicherheit.

## 4.2.3  Regelwerke der Branchenverbände

Die Interessen der Wasserwirtschaft werden durch mehrere Verbände repräsentiert. Dabei sind vor allem die DWA und der DVGW zu nennen. Beide Verbände geben Regelwerke heraus, in denen sie branchenweite Qualitäts- und Sicherheitsstandards definieren.

Der ebenfalls von der DWA und dem DVGW entwickelte B3S WA baut auf den bestehenden Regelwerken auf, indem er auf schon bestehende Regelungen verweist und in diesen Bereichen keine neuen Anforderungen definiert [B3S17b; B3S17c].

Das vorliegende IT-Grundschutz-Profil, das wiederum auf dem B3S WA aufbaut, übernimmt diese Vorgehensweise.

3  Der Einwohnerwert ist ein Vergleichswert für die in Abwässern enthaltenen Schmutzfrachten. Er ergibt sich aus Summe der Anzahl angeschlossener Einwohner und eines Vergleichswerts, mit dessen Hilfe sich die Schmutzfracht  gewerblicher Abwässer  in  Einwohnerzahlen  ausdrücken  lässt [DIN16323].

<!-- page: 23 -->

## 4.3 Zugrundeliegende IT-Grundschutz-Vorgehensweise und angestrebtes Schutzniveau

Grundlage für das vorliegende IT-Grundschutz-Profil ist die IT-Grundschutz-Vorgehensweise der Standardabsicherung. Jedoch werden nicht alle Maßnahmen (modernisiert: Basis- und Standard-Anforderungen) empfohlen, sondern eine für die Zielgruppe angemessene Auswahl getroffen.

Das Profil ist für zwei unterschiedliche Anwendergruppen konzipiert. Für Institutionen der Wasserwirtschaft, die nach den Kriterien der BSI-KritisV [KritisV16] zu den kritischen Infrastrukturen (KRITIS) gehören, sind mehr Maßnahmen empfohlen als für solche, die die Schwellwerte für die Zugehörigkeit zu den kritischen Infrastrukturen unterschreiten. Diese Unterscheidung zwischen  KRITIS-  und  Nicht-KRITIS-Anwendern  beruht  auf  unterschiedlichen  Schutzbedarfseinschätzungen für die beiden Anwendergruppen im Rahmen der Standardabsicherung. Aus diesem Grund wird sowohl für KRITIS-Institutionen als auch für Nicht-KRITIS-Institutionen ein Schutzniveau erreicht, das der Standardabsicherung entspricht.

Da zum Zeitpunkt der Konzeptionierung des vorliegenden Profils die Bausteine des modernisierten Grundschutzes noch nicht fertiggestellt waren, wurde die Vorgehensweise zwar an die der Standardabsicherung angenähert, jedoch mussten die Bausteine des bisherigen Grundschutzes verwendet werden. Bei diesen Bausteinen sind die Maßnahmen nicht in die Kategorien Basis, Standard und erhöhter Schutzbedarf eingeteilt, die für die Bewertung des Schutzniveaus nach der modernisierten Vorgehensweise erforderlich wären. Eine abschließende Beurteilung des erreichten Schutzniveaus nach dem modernisierten BSI-Standard 200-2 ist somit nicht möglich. Perspektivisch sollte bei der Migration zu den Anforderungen des modernisierten IT-Grundschutzes darauf geachtet werden, dass das Schutzniveau der Standardabsicherung erreicht wird.

## 4.4 ISO 27001-Kompatibilität

Das BSI hat ein 'Zertifizierungsschema für Informationssicherheit entwickelt, das die Anforderungen an Managementsysteme für die Informationssicherheit aus ISO/IEC 27001 berücksichtigt und als Prüfkataloge das IT-Grundschutz-Kompendium zugrunde legt.' Dies wird als ISO 27001-Zertifizierung auf Basis IT-Grundschutz bezeichnet [BSI17].

Die Zertifizierung ist möglich, wenn mindestens die IT-Grundschutz-Vorgehensweise 'Standardabsicherung' umgesetzt wird. Damit ist das vorliegende Profil, sofern die Migration zu den modernisierten IT-Grundschutz-Bausteinen erfolgt ist, ISO 27001-kompatibel.

<!-- page: 24 -->

## 5 Abgrenzung des Informationsverbunds

|   1 | Auswahl der betrachteten Geschäftsprozesse und Anlagen                         |
|-----|--------------------------------------------------------------------------------|
|   2 | Schutzbedarfszuweisung für die Anlagen                                         |
|   3 | Auswahl der ICS-Netzstruktur                                                   |
|   4 | Auswahl der zutreffenden Anwendungsfälle und Erfassung der Referenzarchitektur |
|   5 | Erfassung der Informationssicherheitsempfehlungen für die Anwendungsfälle      |
|   6 | Integration und Realitätsabgleich aller Referenzarchitekturen und Empfehlungen |
|   7 | Umsetzung von Maßnahmen                                                        |

## 5.1 Organisationsstruktur

In Deutschland sind nach Grundgesetz Art. 28 Abs. 2 die Kommunen für die Wasserversorgung und Abwasserbeseitigung verantwortlich. Diese Regelung ist der Grund dafür, dass die Mehrheit der Institutionen in der Wasserwirtschaft klein ist (unter 100 Beschäftigte) [Verdi15].

Die Betriebsformen sind vorwiegend öffentlich-rechtlich (Regiebetriebe, Eigenbetriebe, Anstalten öffentlichen Rechts); bei privatrechtlichen Betriebsformen (GmbH und AG) behalten Kommunen durch Anteilsbesitze und Stimmrechte die Handlungshoheit [BSI15].

Häufig sind Wasserversorgung und Abwasserbeseitigung nur eine von mehreren Dienstleistungen eines Betriebes, zum Beispiel bei den meisten Stadtwerken - in solchen Fällen sind die Mitarbeiter oft nicht klar der Wasserwirtschaft zuzuordnen [Verdi15].

Aufgrund dieser heterogenen Strukturen wird im vorliegenden IT-Grundschutz-Profil keine typische Organisationsstruktur vorgegeben. Es ist aber zu vermerken, dass die Informationssicherheit der prozessleittechnischen Infrastruktur in vielen Fällen eine Aufgabe ist, die nicht in einer einzigen Abteilung gelöst werden kann. Für die Etablierung eines Informationssicherheitskonzepts für industrielle IT sind sowohl IT-Sicherheits-Kenntnisse als auch Kenntnisse der prozessleittechnischen Systeme notwendig; des Weiteren gibt es Wechselwirkungen zwischen den Sicherheitskonzepten für die industrielle IT und die Office-IT. In dem wahrscheinlichen Fall, dass getrennte Abteilungen für die Office-IT und die Prozessleittechnik bestehen, ist demnach eine Zusammenarbeit ratsam.

<!-- page: 25 -->

## 5.2 Geschäftsprozesse und Anlagen

Die Auswahl der Geschäftsprozesse für dieses Profil orientiert sich an der Verordnung zur Bestimmung kritischer Infrastrukturen (BSI-KritisV, [KritisV16]). Die Begrifflichkeiten für Anlagen und Anlagenbestandteile werden für die Wasserversorgung der Norm DIN 4046 sowie für die Abwasserbeseitigung den Normen DIN 4045 und DIN EN 16323 entnommen [DIN4046; DIN4045; DIN16323].

Einen Überblick über die betrachteten Geschäftsprozesse und dafür notwendige Anlagen geben Tab. 5.1 und Tab. 5.2. Bei der Wasserversorgung sind die Geschäftsprozesse Gewinnung, Aufbereitung und Verteilung des Wassers relevant; bei der Abwasserbeseitigung die Siedlungsentwässerung sowie die Abwasserbehandlung und Gewässereinleitung.

Tab. 5.1: Geschäftsprozesse in der Wasserversorgung

| Geschäftsprozess   | Gewinnung                                   | Aufbereitung                                   | Verteilung                              |
|--------------------|---------------------------------------------|------------------------------------------------|-----------------------------------------|
| Anlage             | Gewinnungsanlage (Wasserwerk) mit Leitstand | Aufbereitungsanlage (Wasserwerk) mit Leitstand | Wasserverteilungs- system mit Leitstand |
| ICS-Netzstruktur   | konzentriert                                | konzentriert                                   | verteilt                                |

Tab. 5.2: Geschäftsprozesse in der Abwasserbeseitigung

| Geschäftsprozess   | Siedlungsentwässerung      | Abwasserbehandlung und Gewässereinleitung   |
|--------------------|----------------------------|---------------------------------------------|
| Anlage             | Kanalisation mit Leitstand | Kläranlage mit Leitstand                    |
| ICS-Netzstruktur   | verteilt                   | konzentriert                                |

Für die Gewinnung und Aufbereitung von Trinkwasser werden Gewinnungs- und Aufbereitungsanlagen verwendet. Der Begriff Wasserwerk kann für beide dieser Anlagen stehen. Die Abwasserbehandlung findet in Kläranlagen statt. All diesen Anlagen haben gemeinsam, dass sie - mitsamt Leitstand und Steuergeräten - in einem Gebäudekomplex konzentriert sind.

Wasserverteilungssysteme und die Kanalisation für die Siedlungsentwässerung bestehen aus Kanalnetzen mit Ventilen, Schiebern und Klappen, Pumpen und gegebenenfalls weiteren Kanalbauwerken wie Überläufen. Der Leitstand für diese Kanalnetze befindet sich in der Regel an einer zentralen Stelle, während die eigentlichen Kanäle und Kanalbauwerke und ihre Steuerungssysteme über eine größere Region verteilt sind. Größere Kanalbauwerke, zum Beispiel Pumpstationen, können jedoch auch einen eigenen Leitstand vor Ort haben. In diesem Fall sind sie als konzentrierte Anlagen zu betrachten.

Die Unterschiede in den ICS-Netzstrukturen von konzentrierten und verteilten Anlagen werden in Abschnitt 5.4 genauer beleuchtet.

<!-- page: 26 -->

## 5.3 Schutzbedarf der Anlagen

|   1 | Auswahl der betrachteten Geschäftsprozesse und Anlagen                         |
|-----|--------------------------------------------------------------------------------|
|   2 | Schutzbedarfszuweisung für die Anlagen                                         |
|   3 | Auswahl der ICS-Netzstruktur                                                   |
|   4 | Auswahl der zutreffenden Anwendungsfälle und Erfassung der Referenzarchitektur |
|   5 | Erfassung der Informationssicherheitsempfehlungen für die Anwendungsfälle      |
|   6 | Integration und Realitätsabgleich aller Referenzarchitekturen und Empfehlungen |
|   7 | Umsetzung von Maßnahmen                                                        |

Für die Auswahl geeigneter Maßnahmen muss jeder abzusichernden Anlage der Institution des Profilanwenders ein Schutzbedarf zugewiesen werden. Anlagen mit höherem Schutzbedarf werden im Verlauf der Profilanwendung zusätzliche Maßnahmen zugewiesen.

In diesem Profil werden die Schutzbedarfskategorien 'normal' und 'hoch' verwendet. In Anlehnung an den BSI-Standard 200-2 wird der Schutzbedarf bezüglich Schadenskategorien eingeschätzt [BSI17]. Da die Schadenskategorie 'Beeinträchtigung der Aufgabenerfüllung' als die relevanteste für Anlagen der Wasserwirtschaft angesehen wird, beschränkt sich die Betrachtung auf diese Kategorie.

Als quantitatives Kriterium für die Unterscheidung zwischen normalem und hohem Schutzbedarf wird die Anzahl der Personen herangezogen, die von einem Ausfall der betrachteten Anlage betroffen wären: Ab 500 000 betroffenen Personen fällt die Anlage unter die Schutzbedarfskategorie 'hoch'.

Die BSI-KritisV nutzt ebendiese Personenzahl als Grundlage für die Berechnung der Schwellenwerte für  kritische  Infrastrukturen  [KritisV16].  Daraus  ergeben  sich  nach  BSI-KritisV  die Schwellwerte von 22 Mio. m³ jährlich verarbeiteter Wassermenge für Anlagen der Trinkwasserversorgung  und  500  000  angeschlossene  Einwohner  für  Anlagen  der  Abwasserbeseitigung. Tab. 5.3 gibt eine Übersicht für die Zuordnung von Schutzbedarfskategorien für die Anlagen des Profilanwenders.

<!-- page: 27 -->

Tab. 5.3: Kriterien für die Zuweisung von Schutzbedarfskategorien

| Schutzbedarfs- kategorie                                                     | "Normal"                                                                                               | "Hoch" (=KRITIS)                                                                                       |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Kriterium für die Schadenskategorie "Beeinträchtigung der Aufgabenerfüllung" | Von einem Ausfall der An- lage sind weniger als 500 000 Per- sonen betroffen.                          | Von einem Ausfall der An- lage sind mindestens 500 000 Per- sonen betroffen.                           |
| Schwellenwerte nach BSI-KritisV                                              | Trinkwasser: < 22 Mio. m³/Jahr verarbei- tete Wassermenge Abwasser: < 500 000 angeschlossene Einwohner | Trinkwasser: ≥ 22 Mio. m³/Jahr verarbei- tete Wassermenge Abwasser: ≥ 500 000 angeschlossene Einwohner |

<!-- page: 28 -->

## 5.4 ICS-Netzstruktur

|   1 | Auswahl der betrachteten Geschäftsprozesse und Anlagen                         |
|-----|--------------------------------------------------------------------------------|
|   2 | Schutzbedarfszuweisung für die Anlagen                                         |
|   3 | Auswahl der ICS-Netzstruktur                                                   |
|   4 | Auswahl der zutreffenden Anwendungsfälle und Erfassung der Referenzarchitektur |
|   5 | Erfassung der Informationssicherheitsempfehlungen für die Anwendungsfälle      |
|   6 | Integration und Realitätsabgleich aller Referenzarchitekturen und Empfehlungen |
|   7 | Umsetzung von Maßnahmen                                                        |

Als Ausgangspunkt für die Anpassung des Profils an die Bedürfnisse der Anwenderinstitution wird  die  abzusichernde  Anlage  (oder  der  abzusichernde  Anlagenverbund)  einer  von  drei grundlegenden ICS-Netzstrukturen zugeordnet.

Die ICS-Infrastruktur für die in Abschnitt 5.2 genannten Anlagen der Wasserwirtschaft besteht stets aus Feldgeräten, Steuergeräten (Speicherprogrammierbare Steuerungen, SPS) und einem Leitstand. Als Leitstand wird in diesem Profil eine Räumlichkeit bezeichnet, von der aus der Eingriff in die Prozesssteuerung möglich ist. Leitstandskomponenten sind die Funktionseinheiten, die dies ermöglichen, also mindestens ein Human Machine Interface (HMI). In etwas weiterem Sinne können auch Engineering-Workstations oder Control Server darunter fallen.

Die Steuergeräte müssen echtzeitfähig mit den Sensoren und Aktoren und gegebenenfalls auch untereinander kommunizieren können.

Bezüglich der Verteilung der ICS-Komponenten lassen sich drei ICS-Netzstrukturtypen ableiten:

Die verteilte ICS-Netzstruktur (typischerweise bei Wasserverteilungssystemen und Kanalisation zu finden) zeichnet sich dadurch aus, dass die Feldgeräte und ihre zugehörigen Steuergeräte räumlich verteilt und mittels eines Wide Area Networks (WAN) mit dem  zentralen Leitstand verbunden sind. Eine grafische Darstellung findet sich in Abb. 5.1.

<!-- page: 29 -->

Abb. 5.1: Verteilte ICS-Netzstruktur

<!-- image -->

Bei der konzentrierten ICS-Netzstruktur (typischerweise für Wasserwerke, Kläranlagen und größere Kanalbauwerke verwendet) hingegen befinden sich die Feld- und Steuergeräte nah genug beim lokalen Leitstand, um in ein- und demselben Local Area Network (LAN) verbunden zu sein. Die konzentrierte Struktur ist in Abb. 5.2 dargestellt.

Abb. 5.2: Konzentrierte ICS-Netzstruktur

<!-- image -->

<!-- page: 30 -->

Bei Institutionen der Wasserwirtschaft, die größere Regionen bedienen, kann auch eine gemischte ICS-Netzstruktur vorliegen, der in Abb. 5.3 veranschaulicht ist und sowohl aus verteilten (links in Abb. 5.3) und konzentrierten (rechts) Anlagen besteht. Um alle verteilten und konzentrierten Anlagen einer Region vom zentralen Leitstand aus im Blick zu behalten, können die konzentrierten Anlagen zusätzlich noch über das WAN an den zentralen Leitstand angebunden sein. Diese Verbindung muss jedoch nicht zwangsläufig bedeuten, dass die Anlagen vom zentralen Leitstand aus steuerbar sind; sie können auch lediglich Überwachungsdaten liefern.

Abb. 5.3: Gemischte ICS-Netzstruktur

<!-- image -->

Der Schwerpunkt liegt im gesamten Profil und folglich bei der Darstellung der ICS-Netzstrukturen auf der OT. Office-IT-Komponenten (Mitarbeiter-Rechner, Drucker, Server etc.) werden nur dann berücksichtigt, wenn sie - wie in Abb. 5.1, Abb. 5.2 und Abb. 5.3 - Verbindungen zur OT besitzen.

Eine detailliertere Beschreibung der einzelnen Zielobjekte in sowie vollständige Netzpläne sind im folgenden Abschnitt 6 des vorliegenden Profils enthalten. Diese Netzpläne basieren auf der gemischten ICS-Netzstruktur, weil sie die allgemeinste ist. Der Profilanwender sollte dabei die Netzpläne an den für seine Anlagen am besten passenden grundlegenden ICS-Netzstruktur anpassen.

<!-- page: 31 -->

## 6 Generische Referenzarchitektur

Die generische Referenzarchitektur soll einen Überblick geben, um die Orientierung in den spezifischen Referenzarchitekturen der Unterprofile zu erleichtern, die jeweils nur einen Ausschnitt (und Variationen dieses Ausschnitts) der generischen Referenzarchitektur beleuchten.

Zu jeder Referenzarchitektur, generisch oder spezifisch, gehören

- eine Zielobjektliste sowie
- ein Netzplan (für die generische Referenzarchitektur: ein logischer und ein physischer Netzplan).

## 6.1 Generische Zielobjektliste

Die generische Zielobjektliste in Tab. 6.1 enthält eine vollständige Übersicht über alle Zielobjekte, die im vorliegenden Profil berücksichtigt werden. Jedem Zielobjekt ist eine kurze Beschreibung beigefügt.

Die Zielobjekte sind in sechs Kategorien unterteilt.

- Organisation (O) : Für die Informationssicherheit relevante Managementprozesse
- IT-Systeme (IT) : ICS-Hardware
- Anwendungen (A) : Software für die Erbringung der ICS-Prozesse
- Netzkomponenten (N) :  Hard- und Software für die Vernetzung und Kommunikation der IT-Systeme und Anwendungen
- Infrastruktur (IN) :  Physische  Orte,  an  denen  Hardwarekomponenten sich befinden können
- Sicherheit (S) :  Komponenten, die nicht in erster Linie der Erbringung der ICS-Prozesse, sondern der Informationssicherheit der übrigen Komponenten dienen

<!-- page: 32 -->

Tab. 6.1: Generische Zielobjektliste

| Nr.          | Zielobjekt               | Beschreibung                                                                                                                                                                                                                     |
|--------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Organisation | Organisation             | Organisation                                                                                                                                                                                                                     |
| O1           | Sicherheits- management  | Teil des Managements, das sich mit der Informationssicherheit be- fasst.                                                                                                                                                         |
| O2           | Notfallmanagement        | Stellt die Kontinuität des Betriebs in Notfällen sicher.                                                                                                                                                                         |
| IT-Systeme   | IT-Systeme               | IT-Systeme                                                                                                                                                                                                                       |
| IT1          | Feldgerät                | Sensor oder Aktor. Beispiele für Sensoren sind Druck- oder Durchflussmesser, Beispiele für Aktoren Pumpen oder Ventile.                                                                                                          |
| IT2          | SPS                      | Speicherprogrammierbare Steuerung. Spezialisierter Computer für die automatisierte Prozesssteuerung. Auch bekannt unter dem englischen Begriff PLC (Programmable Logic Controller).                                              |
| IT3          | HMI                      | Bedien- und Benutzeroberfläche für die Prozesssteuerung, insbe- sondere auch für die Koordination aller SPSen. Hier kann der ge- samte Prozess überwacht werden. Auch Eingriffe, beispielsweise Sollwertsetzungen, sind möglich. |
| IT4          | Historian                | Rechner bzw. Server, auf dem (vergangene) Prozessdaten archi- viert werden.                                                                                                                                                      |
| IT5          | Engineering- Workstation | Rechner, auf dem die Programme für die SPSen geschrieben wer- den. Dedizierte Rechner für diesen Zweck werden auch als Pro- grammiergerät (PG) bezeichnet.                                                                       |
| IT6          | Control Server           | Zentraler Speicherort für alle Daten und Programme, die eine Pro- zesssteuerung ermöglichen. Dient oft der Erfüllung von SCADA / PLS / DCS-Aufgaben.                                                                             |
| IT7          | Webserver                | Stellt ICS-Funktionen, etwa des HMI oder Historian, über das In- ternet (im Browser) zur Verfügung.                                                                                                                              |
| IT8          | Mobilgerät               | Laptop, Tablet oder Smartphone, das in verschiedenen Bereichen des ICS-Netzes für verschiedene Funktionen zum Einsatz kom- men kann. Beispiele sind Engineering- oder HMI-Funktionen und das Empfangen von Alarmen.              |
| IT9          | Externe Kompo- nente     | Ein Laptop oder Desktop-PC, der nicht zum ICS-Netz gehört. Ent- weder eine Office-Komponente oder ein PC eines ICS-Herstellers, der beispielsweise für Fernwartung genutzt werden kann.                                          |
| IT 10        | Office-IT-Kompo- nente   | Ein Desktop-PC, Laptop, Drucker oder eine sonstige Komponente zur Erfüllung von nicht-ICS-relevanten Aufgaben.                                                                                                                   |
| Anwendungen  | Anwendungen              | Anwendungen                                                                                                                                                                                                                      |
| A1           | Engineering- Software    | Softwareumgebung, mit der Programme für SPSen geschrieben und kompiliert werden können. Da die SPS-Programmiersprachen im Standard DIN IEC 61131-3 vereinheitlicht werden, sind die meisten Programme mit der Norm kompatibel.   |
| A2           | SPS-Programm             | Kompiliertes Programm, das zur Ausführung auf die SPS geladen wird.                                                                                                                                                              |
| A3           | HMI-Software             | Anwendung, die eine (meist grafische) Darstellung der aktuellen Prozessdaten bietet. Auch Bedienfunktionen, etwa für das Setzen von Sollwerten und das Bedienen von Aktoren, sind enthalten.                                     |
| A4           | Datenbank                | Anwendung zum Archivieren vergangener Prozessdaten.                                                                                                                                                                              |

<!-- page: 33 -->

| A5              | Webdienst                    | Anwendung, die ein IP-basiertes Netz nutzt, um Dienste auf Basis von HTTP, SMTP oder FTP anzubieten. Das wichtigste Protokoll für Webdienste ist SOAP. Eine Anwendung, die häufig als Web- dienst bereitgestellt wird, ist die HMI-Software.                                |
|-----------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A6              | Netzmanagement- Software     | Anwendung, die für die Überwachung und Konfiguration der Netze und Netzwerkgeräte verwendet wird. Beispiele sind das Protokoll SNMP oder der syslog-Standard.                                                                                                               |
| A7              | OPC                          | Standard für die Kommunikation zwischen Geräten unterscheidli- cher Hersteller. OPC-Server sind Anwendungen, die von ICS-Her- stellern angeboten werden, um ihr Gerät OPC-fähig zu machen. OPC-Clients sind Anwendungen, die den Zugriff auf einen OPC- Server ermöglichen. |
| A8              | Mail, SMS, Instant Messaging | Eine Anwendung für kurze, automatisierte Nachrichten, die von den Steuergeräten gesendete Alarme überträgt.                                                                                                                                                                 |
| A9              | Betriebssystem               | Windows, Unix-System oder Mac OS für PCs oder Laptops bzw. Firmware für eingebettete Systeme wie SPSen.                                                                                                                                                                     |
| Netzkomponenten | Netzkomponenten              | Netzkomponenten                                                                                                                                                                                                                                                             |
| N1              | Switch                       | Netzwerkgerät, das LAN-Teilnehmer zu einem LAN verbindet.                                                                                                                                                                                                                   |
| N2              | Router                       | Netzwerkgerät, das für die Verbindung eines LANs zu einem an- deren oder zu einem WAN zuständig ist.                                                                                                                                                                        |
| N3              | Modem                        | Netzwerkgerät, digitale Signale für ein analoges WAN-Übertra- gungsmedium umformt.                                                                                                                                                                                          |
| N4              | IT-Verkabelung               | Kabel zum Verbinden der einzelnen Geräte eines Netzes, bei- spielsweise Ethernet-Kabel.                                                                                                                                                                                     |
| N5              | Feldbus                      | Steht hier stellvertretend für alle Echtzeit-Kommunikationstechni- ken: Einheitssignale, klassische Feldbustechnik, Funk und Indust- rial Ethernet.                                                                                                                         |
| N6              | Fernwartung                  | WAN-Verbindung zum System eines ICS-Herstellers zum Zweck der Fernwartung.                                                                                                                                                                                                  |
| Infrastruktur   | Infrastruktur                | Infrastruktur                                                                                                                                                                                                                                                               |
| IN1             | Leitstand                    | Räumlichkeit, von der aus die Prozesssteuerung erfolgt. Darin be- findet sich in jedem Fall das HMI und möglicherweise Enginee- ring-Workstations, Historian und / oder ein Server.                                                                                         |
| IN2             | Büro                         | Räumlichkeit für Office-IT-Komponenten.                                                                                                                                                                                                                                     |
| IN3             | Serverraum                   | Räumlichkeit mit speziellen klimatischen und / oder zugangstech- nischen Bedingungen, in der Server und Großrechner ohne Be- dienschnittstelle untergebracht sind.                                                                                                          |
| IN4             | Schutzschrank                | Schaltschrank, in dem SPSen untergebracht und verschaltet wer- den.                                                                                                                                                                                                         |
| IN5             | Mobiler Arbeits- platz       | Arbeitsplatz eines Mobilgeräts.                                                                                                                                                                                                                                             |

<!-- page: 34 -->

| IN6        | Feld               | Steht für die Räumlichkeiten (oder den Ort ohne spezielle Räum- lichkeiten), in der die zu steuernden Maschinen, Feldgeräte und ggf. SPSen untergebracht sind. In der Automatisierungstechnik auch als Feld bekannt.   |
|------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sicherheit | Sicherheit         | Sicherheit                                                                                                                                                                                                             |
| S1         | Firewall           | Hard- oder Software, die Datenverkehr im Netz oder auf einem Host nach bestimmten Regeln filtert. Dazu gehören unter anderem Layer-3-Firewalls (Paketfilter) und Layer-7-Firewalls (Application Layer Gateways).       |
| S2         | VPN                | Umfasst die Soft- und Hardware für den Aufbau einer VPN-Verbin- dung, zum Beispiel VPN-Router, VPN-Gateways oder VPN-Ser- ver.                                                                                         |
| S3         | IDS / IPS          | Intrusion Detection System / Intrusion Prevention System.                                                                                                                                                              |
| S4         | Antiviren-Software | Software, die anhand von Signaturen bekannte Malware erkennt.                                                                                                                                                          |

## 6.2 Generische Netzpläne

Netzpläne sind ein wichtiges Werkzeug des vorliegenden Profils, weil sie das Zusammenspiel der Zielobjekte veranschaulichen. Abschnitt 6.2.1 führt in die für die Netzpläne verwendete Notation ein, die auch in allen Unterprofilen verwendet wird.

Die generischen Netzpläne passen höchstwahrscheinlich nicht optimal zur abzusichernden ICS-Anlage jedes Profilanwenders. Die Anpassung erfolgt in den Unterprofilen. Neben der Einführung in die Notation ist der zweite wichtige Zweck der generischen Netzpläne deswegen eine Orientierung, welche Variation der generischen Referenzarchitektur in welchem Unterprofil behandelt wird. Dazu finden sich Hinweise in Abschnitt 6.2.

Als dritter Zweck sollen die generischen Netzpläne eine Idee vermitteln, wie ein vollständiger Netzplan des ICS-Netzes aussehen kann - im Gegensatz zu den spezifischen Netzplänen der Unterprofile, die jeweils auf einen Aspekt reduziert sind und dazu auch physische und logische Netzplanelemente kombinieren.

Bezüglich der ICS-Netzstruktur (verteilt, konzentriert oder gemischt, siehe Abschnitt 5.4) liegt den generischen Netzplänen, aber auch allen Netzplänen in Unterprofilen, die Mischform (s. Abb. 5.3) zugrunde, in der sich die verteilte Netzstruktur auf der linken, die konzentrierte Netzstruktur auf der rechten Seite wiederfindet. Die grundlegende ICS-Netzstruktur sollte stets dem der eigenen Anlage am nächsten kommenden angepasst werden.

<!-- page: 35 -->

## 6.2.1  Legenden

Der physische Netzplan zeigt Komponenten und ihre Verbindungen, die Räumlichkeiten, in denen Komponenten verortet sind, und Netzwerkgeräte. In Abb. 6.1 ist die Legende für physischen Netzplänen zu sehen.

Abb. 6.1: Legende zu physischen Netzplänen: Komponenten, Einordnung der Komponenten in die Automatisierungspyramide und Verbindungen der Komponenten

<!-- image -->

- Rechteckige  Kästen  zeigen Komponenten an,  Linien  ihre Verbindungen .  Sowohl Komponenten (z.B. eine SPS) als auch Verbindungen (z.B. der Feldbus) können Zielobjekte repräsentieren.
- Soweit sich die Komponenten in die Automatisierungspyramide einordnen lassen, ist  dies farblich dargestellt. Dabei werden die oberen beiden Ebenen zur Unternehmensebene zusammengefasst und umfassen alle Office-IT-Komponenten (gelb), die Prozessleitebene umfasst alle im vorliegenden Profil als Prozessleitkomponenten zusammengefassten Komponenten (grün), die Steuerungsebene die SPSen (türkis) und die Feldebene Feldgeräte (blau).
- Externe Komponenten (grau) stellen in den Netzplänen alle Komponenten dar, die nicht fest zum ICS-Netz einer Institution gehören. Dies können Office-Komponenten, Komponenten anderer Institutionen (etwa für die Fernwartung) oder mobile Komponenten (Tablets oder Laptops) sein.
- Netzkomponenten sind schwarz dargestellt und nur im physischen Netzplan eingezeichnet.

<!-- page: 36 -->

- WAN-Verbindungen werden durch eine Wolke dargestellt. Dabei steht WAN in aller Regel für eine Internetverbindung über öffentliche Telefonleitungen oder Mobilfunk; ist aber generisch gehalten, um auch Standleitungen und nichtöffentliche Funkverbindungen abzudecken.
- LAN-Verbindungen sind durch Linien dargestellt. Schwarze und grüne Linien stehen für  Ethernet-Verbindungen.  Schwarze  Verbindungen  stehen  für  reine  Office-Netze, grüne Linien verbinden ICS-Komponenten. Türkise Verbindungen stehen für alle Formen von Echtzeitkommunikation: Industrial Ethernet, klassische Feldbusse oder Einheitssignale.
- Ist die Verbindungslinie grau und gepunktet, kennzeichnet sie eine temporäre Verbindung , zum Beispiel ein Fernwartungszugang zu einem externen PC oder eine LAN-Verbindung eines Mobilgeräts. Mehrere temporäre Verbindungen bestehen in der Regel nicht gleichzeitig, zum Beispiel kann ein mobiles Gerät nicht mit zwei (verteilten) SPSen gleichzeitig direkt verbunden sein.

In Abb. 6.2 ist die Legende für die Anwendungen und Datenübermittlung gegeben, die in logischen Netzpläne dargestellt werden.

- Anwendungen sind in einem weißen Feld unterhalb der Komponente dargestellt.
- Linien in Rottönen stellen die Datenübermittlung dar: Orangefarbene Linien stehen für  automatisierte Datenübermittlung, rote für interaktive Datenübermittlung. Ist eine Komponente oder Verbindung pinkfarben gekennzeichnet, steht dies für den Zugriff auf  die  Netzmanagementdaten  einer  Komponente  bzw.  auf  die  Konfiguration  einer (Netz)verbindung.
- Pfeile verdeutlichen die vorherrschende Richtung der Datenübermittlung : Ein Pfeil von einer Komponente A zu einer Komponente B bedeutet, dass Daten von einer Anwendung der Komponente A zur einer Anwendung der Komponente B übermittelt werden; B hat in diesem Fall also nur lesenden Zugriff auf A. Ein Pfeil von B nach A bedeutet dementsprechend eine Datenübermittlung von B nach A bzw. schreibenden Zugriff der Komponente B auf die Komponente A. Ein Pfeil in beide Richtungen kennzeichnet einen Datenaustausch zwischen beiden Komponenten.

<!-- page: 37 -->

Abb. 6.2: Legende zu logischen Netzplänen: Anwendungen und Datenübermittlung

<!-- image -->

## 6.2.2  Netzpläne

Abb. 6.3 und Abb. 6.4 zeigen Netzpläne der generischen Referenzarchitektur. Abb. 6.3 (physischer Netzplan) legt dabei den Schwerpunkt auf Hardware, Verbindungen und physische Verortung der Zielobjekte, Abb. 6.4 (logischer Netzplan) auf die logische Datenübermittlung zwischen Anwendungen.

Abb. 6.3 ist ein möglicher physischer Netzplan der generischen Referenzarchitektur, der die physische Verortung der generischen Zielobjekte sowie die Verbindungen zwischen den Zielobjekten darstellt.

<!-- page: 38 -->

Abb. 6.3: Physischer Netzplan der generischen Referenzarchitektur

<!-- image -->

Außer den Komponenten und Verbindungen zeigt der physische Netzplan die Räumlichkeiten, in denen Komponenten verortet sind. Auch Netzkomponenten werden aufgeführt. Software-Anwendungen werden im physischen Netzplan nicht abgebildet.

- Für  die  ICS-Komponenten  des  zentralen  Leitstands  (links)  ist  dabei  angenommen, dass HMI und Engineering-WS sich in einem abschließbaren Raum, Leitstand genannt, befinden.
- Historian und Server, die keine Bedienschnittstelle haben, sind im Netzplan nicht im Leitstand, sondern in einem separaten Serverraum verortet.
- Office-Komponenten für die Verwaltung auf zentraler Leitstands-Ebene haben nicht nur ein separates LAN (eigener Switch), sondern auch eigene Räumlichkeiten - sie sind im Netzplan als Büro gelb gekennzeichnet.
- Für den lokalen Leitstand (rechts) ist ein gemeinsames LAN für ICS- und Office-Komponenten angenommen. Auch haben Leitstands- und Office-Komponenten gemeinsame Räumlichkeiten (Büro = Leitstand).
- Steuer- und Feldgeräte, die echtzeitfähig miteinander kommunizieren, werden räumlich  der Anlage (blaugrün)  zugeordnet, zu der sie gehören. Dabei können mehrere SPSen, Sensoren und Aktoren zu ein- und derselben Anlage gehören; bei den verteilten Steuergeräten können aber auch räumliche Trennungen zwischen ihnen liegen.
- Externe Komponenten können über das WAN auf die ICS- oder Office-Netze zugreifen. Dasselbe gilt für Mobilgeräte , die jedoch auch direkte Schnittstellen zu einzelnen

<!-- page: 39 -->

Geräten, beispielsweise SPSen, besitzen können. Verbindungen zu externen und mobilen Geräten sind in der Regel temporär.

In Abb. 6.3 sind bezüglich zweier Aspekte Annahmen getroffen worden: Bezüglich der räumlichen Verordnung der Zielobjekte und bezüglich der gemeinsamen Nutzung der Netze durch Office- und ICS-Komponenten. Variationen dieser Aspekte werden in den Unterprofilen behandelt:

- Das Unterprofil Architektur (AR) enthält Anwendungsfälle, die sich mit der gemeinsamen Nutzung von Local Area Networks (LAN) und Wide Area Networks (WAN) durch Office-IT-Komponenten und ICS-Komponenten befassen.
- Das Unterprofil Benutzerzugang (UA) enthält Anwendungsfälle, die den physischen Zugang von Benutzern zur ICS-Anlage betrachten.

In Abb. 6.4, dem logischen Netzplan, werden die Software-Anwendungen auf der generischen Zielobjektliste dargestellt.

Abb. 6.4: Logischer Netzplan der generischen Referenzarchitektur

<!-- image -->

<!-- page: 40 -->

Zum logischen Netzplan sind einige Punkte zu beachten:

- In der Regel sind diese Anwendungen auf dedizierten Komponenten installiert.
- Office-Komponenten sind nicht dargestellt, da Office-Anwendungen nicht zum Geltungsbereich dieses Profils gehören. Wenn ICS-Anwendungen auf Office-Komponenten installiert sind, werden diese Office-Komponenten im logischen Netzplan als externe Komponente betrachtet.
- Wie auch auf dem Mobilgerät können auf externen Komponenten eine Vielfalt von möglichen  Anwendungen  installiert  sein,  darunter  HMI-Software,  Engineering-Software oder Netzmanagementsoftware. Dabei ist es sowohl beim externen PC als auch beim Mobilgerät möglich, dass eine, mehrere oder keine der genannten Anwendungen tatsächlich installiert sind.

Der Datenfluss zwischen den Anwendungen ist sehr vielfältig und zudem stark vom Anwendungsfall abhängig, weshalb er nicht im generischen logischen Netzplan, sondern nur für spezielle Anwendungsfälle in den spezifischen Netzplänen der Unterprofile dargestellt wird:

- Das Unterprofil Benutzerzugang (UA) enthält  Anwendungsfälle, die den Zugriff auf das HMI und die HMI-Software (HMI-SW) betrachten.
- Das  Unterprofil SPS-Programmierung und -Wartung (PLC) enthält  Anwendungsfälle, die die Programmierung und den Zugriff auf SPSen und ihre Programme betrachten, besonders mittels Engineering-Workstations (Engineering WS) und entsprechender Engineering-Software (Engineering-SW).
- Das Unterprofil Netzmanagement (NM) enthält Anwendungsfälle, die den Betrieb und die Konfiguration der einzelnen Zielobjekte, vor allem der Netzkomponenten, und der darauf installierten Software betrachten.
- Das  Unterprofil Programmzugriff  (PA) enthält  Anwendungsfälle,  die  die  automatisierte  oder  interaktive  Kommunikation  zwischen  verschiedenen  Anwendungen  betrachten.

<!-- page: 41 -->

## 6.3 Schutzbedarf der anwendungsfallunabhängigen Zielobjekte

Der Schutzbedarf für einzelne Zielobjekte wird im Rahmen dieses Profils wie folgt festgelegt:

- Grundsätzlich erben die Zielobjekte den Schutzbedarf von dem Geschäftsprozess, für dessen Erfüllung sie (bzw. die Anlage, zu der sie gehören) benötigt werden. Das bedeutet insbesondere, dass ihr Schutzbedarf nicht höher als der dieses Geschäftsprozesses (bzw. dieser Anlage) sein kann.
- Gehört der Geschäftsprozess zu keiner kritischen Infrastruktur, haben alle dazugehörigen Zielobjekte einen normalen Schutzbedarf. Die Schutzbedarfsfeststellung in Tab. 6.2 ist deswegen nur für kritische Infrastrukturen relevant.
- Bei Geschäftsprozessen einer kritischen Infrastruktur (mit hohem Schutzbedarf) können die Zielobjekte hohen oder normalen Schutzbedarf haben. Die Schutzbedarfszuweisung hängt von dem Anwendungsfall ab, in dem die Zielobjekte verwendet werden.
- Ist  in  einem  Anwendungsfall das Zielobjektes für die Erbringung des kritischen Geschäftsprozesses (oder den Schutz anderer Zielobjekte) besonders wichtig, erhält das Zielobjekt die Schutzbedarfskategorie 'hoch'.

Im Hauptprofil wird der Schutzbedarf nur für anwendungsfallunabhängige Zielobjekte festgelegt. Für alle weiteren Zielobjekte geschieht dies in den Unterprofilen.

Anwendungsfallunabhängige Zielobjekte dieses Profils sind solche, deren Einbindung in das ICS-Netz in den Unterprofilen nicht mehr variiert wird. Dies sind die Zielobjekte O1: Sicherheitsmanagement und O2: Notfallmanagement.

Die Schutzbedarfsfeststellung dieser Zielobjekte ist in  Tab. 6.2 abgebildet. Dabei steht ein weißes Feld für normalen, ein schwarzes für hohen Schutzbedarf. Das Zielobjekt O1 ist von grundlegender Wichtigkeit für die Etablierung, Aufrechterhaltung und Weiterentwicklung aller Maßnahmen zur Informationssicherheit im täglichen Betrieb und bekommt deswegen einen hohen Schutzbedarf zugewiesen. Das Zielobjekt O2 ist weniger relevant für den täglichen Betrieb; ein normaler Schutzbedarf ist deswegen ausreichend.

Tab. 6.2: Schutzbedarfstabelle für die anwendungsfallunabhängigen Zielobjekte

| Legende für den Schutzbedarf:   | Legende für den Schutzbedarf:   | normal   | hoch   |
|---------------------------------|---------------------------------|----------|--------|
| Nr.                             | Zielobjekt                      |          |        |
| Organisation                    | Organisation                    |          |        |
| O1                              | Sicherheitsmanagement           |          |        |
| O2                              | Notfallmanagement               |          |        |

<!-- page: 42 -->

## 7 Anforderungen und Maßnahmen

## 7.1 Modellierung der anwendungsfallunabhängigen Zielobjekte

Im Hauptprofil wird die Modellierung mit IT-Grundschutz-Bausteinen nur für die anwendungsfallunabhängige Zielobjekte O1 und O2 durchgeführt. Für alle weiteren Zielobjekte geschieht dies in den Unterprofilen.

Die Modellierung der beiden Organisations-Zielobjekte mit Bausteinen ist in Tab. 7.1 veranschaulicht. In den Zeilen finden sich die zu modellierenden Zielobjekte, in den Spalten die ausgewählten Bausteine. Wird ein Baustein für die Modellierung eines Zielobjekts verwendet, wird das entsprechende Feld eingefärbt. Ein Zielobjekt kann dabei durchaus durch mehrere Bausteine abgebildet werden.

Sowohl für das allgemein gehaltene Sicherheitsmanagement, also den Teil des Managements, der sich mit der Informationssicherheit einer Institution befasst, als auch für das etwas spezifischere Notfallmanagement, das die Kontinuität des Betriebs in Notfällen sicherstellen soll, gibt es explizit Bausteine im (bisherigen) IT-Grundschutz: Die Bausteine B 1.0: Sicherheitsmanagement sowie B 1.3: Notfallmanagement .

Um die Modellierung zu vervollständigen, wird für beide Zielobjekte zusätzlich der Baustein B 1.8: Behandlung von Sicherheitsvorfällen ausgewählt. Während sich Bausteine B 1.0 und B 1.3 eher mit dem übergeordneten Management befassen, beinhaltet dieser Baustein konkretere operative Maßnahmen.

Tab. 7.1: Modellierungstabelle für die anwendungsfallunabhängigen Zielobjekte

| Nr.          | Zielobjekt            | Modellierung mit Bausteinen   | Modellierung mit Bausteinen   | Modellierung mit Bausteinen               |
|--------------|-----------------------|-------------------------------|-------------------------------|-------------------------------------------|
|              |                       | B 1.0 Sicherheits- management | B 1.3 Notfall- management     | B 1.8 Behandlung von Sicherheitsvorfällen |
| Organisation | Organisation          |                               |                               |                                           |
| O1           | Sicherheitsmanagement |                               |                               |                                           |
| O2           | Notfallmanagement     |                               |                               |                                           |

<!-- page: 43 -->

## 7.2 Auswahl  der  Maßnahmen  (Anforderungen)  am  Beispiel  des Bausteins B 1.0

Jeder IT-Grundschutz-Baustein enthält eine Liste von Maßnahmen (modernisiert: Anforderungen). Nicht immer wurden alle dieser Maßnahmen für dieses Profil ausgewählt. Die Auswahl von Maßnahmen wird für jeden im Hauptprofil verwendeten Baustein durchgeführt. Die Maßnahmenauswahl für dieses Profil beruht auf dem branchenspezifischen Sicherheitsstandard Wasser / Abwasser (B3S WA) [B3S17a].

Bei einer Nichtauswahl einer Maßnahme sind folgende Szenarien möglich:

- Die Maßnahme (Anforderung) wird für die Zielgruppe des Profils insgesamt nicht ausgewählt. In diesem Fall sollte die Nichtauswahl begründet werden.
- Die Maßnahme (Anforderung) wird für die Zielgruppe des Profils ausgewählt, aber nicht für  diesen  Anwendungsfall.  Stattdessen  wird  sie  in  einem  anderen  Anwendungsfall ausgewählt. Dieser Anwendungsfall kann auch Teil eines anderen Unterprofils sein. Hierfür ist keine gesonderte Begründung notwendig.

Tab. 7.2 zeigt die Maßnahmenauswahl für den Baustein B 1.0: Sicherheitsmanagement. Die Maßnahmenauswahltabellen für die Bausteine B 1.3: Notfallmanagement und B 1.8: Behandlung von Sicherheitsvorfällen befinden sich im kostenpflichtigen Anhang B (Wasserwirtschaft).

In den Tabellenzeilen sind alle Maßnahmen des Bausteins aufgelistet. Es wird die Nummer der Maßnahme, ihr Titel sowie ihre Qualifizierungsstufe angegeben. Mögliche Qualifizierungsstufen sind A (Einstieg), B (Aufbau), C (Zertifikat), Z (zusätzlich) und W (Wissen). Nur die Stufen A bis C sind für eine Qualifizierung nach IT-Grundschutz bzw. ISO 27001 notwendig.

In den Tabellenspalten sind die Anwendungsfälle aufgeführt, für die mindestens eine Maßnahme des Bausteins ausgewählt wurde. Ein grün eingefärbtes Feld kennzeichnet die Auswahl der Maßnahme für den Anwendungsfall. Ist das Feld zusätzlich mit einem 'K' gekennzeichnet, wird die Maßnahme nur dann ausgewählt, wenn das mit dem Baustein modellierte Zielobjekt einen hohen Schutzbedarf hat, also die dazugehörige Anlage als kritische Infrastruktur (KRITIS) eingestuft ist.

<!-- page: 44 -->

Tab. 7.2: Maßnahmenauswahl für den Baustein B 1.0: Sicherheitsmanagement

| Maßnahmen des Bausteins B 1.0: Sicherheitsmanagement:   | Maßnahmen des Bausteins B 1.0: Sicherheitsmanagement:   | Maßnahmen des Bausteins B 1.0: Sicherheitsmanagement:                                                |    |
|---------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------------|----|
|                                                         | = Im Hauptprofil (HP) ausgewählt                        | = Im Hauptprofil (HP) ausgewählt                                                                     | HP |
| K M 2.192                                               | = A                                                     | Nur für KRITIS / hohen Schutzbedarf ausgewählt Erstellung einer Leitlinie zur Informationssicherheit |    |
| M 2.193                                                 | A                                                       | Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit                             |    |
| M 2.195                                                 | A                                                       | Erstellung eines Sicherheitskonzeptes                                                                |    |
| M 2.197                                                 | A                                                       | Integration der Mitarbeiter in den Sicherheitsprozess                                                |    |
| M 2.199                                                 | A                                                       | Aufrechterhaltung der Informationssicherheit                                                         |    |
| M 2.200                                                 | C                                                       | Management-Berichte zur Informationssicherheit                                                       | K  |
| M 2.201                                                 | C                                                       | Dokumentation des Sicherheitsprozesses                                                               | K  |
| M 2.335                                                 | A                                                       | Festlegung der Sicherheitsziele und -strategie                                                       |    |
| M 2.336                                                 | A                                                       | Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitungsebene                 |    |
| M 2.337                                                 | A                                                       | Integration der Informationssicherheit in organisationsweite Abläufe und Prozesse                    |    |
| M 2.338                                                 | Z                                                       | Erstellung von zielgruppengerechten Sicherheitsrichtlinien                                           |    |
| M 2.339                                                 | Z                                                       | Wirtschaftlicher Einsatz von Ressourcen für Informationssicherheit                                   |    |
| M 2.475                                                 | A                                                       | Vertragsgestaltung bei Bestellung eines externen IT-Sicherheitsbeauf- tragten                        |    |
| M 6.16                                                  | Z                                                       | Abschließen von Versicherungen                                                                       |    |

<!-- page: 45 -->

Es gibt vier mögliche Gründe für die Nichtauswahl von Maßnahmen durch den B3S WA, auf die im Folgenden durch Nennung der vorangestellten Kennziffer Bezug genommen wird:

1. Für  Zielgruppe  nicht relevant. Die  Maßnahme ist für  die  Zielgruppe  (Wasserwirtschaft) i.A. nicht relevant.
2.  Redundant zu anderen Regelwerken. Die  Maßnahme wurde bereits im Merkblatt zum B3S WA beschrieben bzw. wird durch andere Regelwerke von DWA / DVGW abgedeckt.
3. Qualifizierungsstufe Z. Die Maßnahme hat die Qualifizierungsstufe Z und ist somit für die Qualifizierung nach IT-Grundschutz oder ISO 27001 nicht notwendig; sie stellen Ergänzungen dar [BSI16b]. Diese Maßnahmen wurden i.A. nicht ausgewählt.
4.  Durch übergeordnete Maßnahme abgedeckt. Die Maßnahme ist ein Spezialfall einer übergeordneten Maßnahme, die ausgewählt wurde.

In Tab. 7.3 sind die Begründungen für alle nicht ausgewählten Maßnahmen des Bausteins B 1.0 im Einzelnen aufgeführt.

Tab. 7.3: Begründung der Nichtauswahl von Maßnahmen für den Baustein B 1.0

| Nicht ausgewählte Maßnahme                                                                | Begründung (Kennziffer)                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M 2.338 : Erstellung von zielgruppengerechten Sicherheitsrichtlinien                      | Qualifizierungsstufe Z (3)                                                                                                                                                                                                                  |
| M 2.339 : Wirtschaftlicher Einsatz von Ressour- cen für Informationssicherheit            | Qualifizierungsstufe Z (3)                                                                                                                                                                                                                  |
| M 2.475 : Vertragsgestaltung bei Bestellung ei- nes externen IT-Sicherheitsbeauftrag- ten | Für Zielgruppe nicht relevant (1) : Für die Zielgruppe der Wasserwirtschaft wird i.A. kein externer IT-Sicherheitsbeauftragter bestellt. Sollte dies im Einzelfall dennoch der Fall sein, sollte die Maßnahme zusätzlich ausgewählt werden. |
| M 6.16 : Abschließen von Versicherungen                                                   | Qualifizierungsstufe Z (3)                                                                                                                                                                                                                  |

## 7.3 Umsetzungsvorgaben

Die Umsetzung der Maßnahmen liegt im Ermessen der Profilanwender. Für einige Bausteine bietet zudem der IT-Grundschutz Umsetzungshinweise, die zu Rate gezogen werden können.

Bevor nun mit Abschnitt 8 des vorliegenden Hauptprofils fortgefahren wird, sollten die Abschnitte UP6 und UP7 aller Unterprofile zu Rate gezogen werden (siehe Vorgehensweise zur Profilanwendung in Abb. 3.2).

<!-- page: 46 -->

## 8 Risikobehandlung

<!-- image -->

## 8.1 Integration und Realitätsabgleich der Gesamt-Referenzarchitektur

Nach dem Durcharbeiten aller Unterprofile sollte die an die individuellen Gegebenheiten der Anwenderinstitution angepasste Zielobjekt-Maßnahmen-Tabelle (siehe Tab. 3.3) vorliegen. Auch  die  anwendungsfallunabhängigen  Organisations-Zielobjekte  des  Hauptprofils  sollten enthalten sein. Diese Tabelle ist das zentrale Ergebnis der Profilanwendung und enthält alle relevanten Informationen für eine eventuelle ergänzende Risikoanalyse und die Umsetzung der gewählten Maßnahmen.

Es sollte dann ein Gesamt-Netzplan erstellt werden. Dazu sind folgende Schritte durchzuführen:

1. Die grundlegende Netzplanstruktur an den ICS-Netzstrukturtyp anpassen.
2. Physische Aspekte der Netzpläne aller ausgewählten Anwendungsfälle zu einem physischen Netzplan vereinigen.
3. Anwendungsbezogene Aspekte der Netzpläne aller ausgewählten Anwendungsfälle zu einem logischen Netzplan vereinigen.

Um sicherzustellen, dass das Profil die Anwenderinstitution ausreichend abdeckt, sollte die Zielobjekt-Maßnahmen-Tabelle mit der tatsächlichen Situation der Anwenderinstitution verglichen werden:

1. Sind alle Assets der Institution als Zielobjekte erfasst?
2. Geben die Anwendungsfälle den Anlagenalltag hinreichend wieder?

Kommen in der Anwenderinstitution weder zusätzliche Anwendungsfälle noch zusätzliche Zielobjekte oder Gefährdungen vor, ist die Anwendung des IT-Grundschutz-Profils abgeschlossen und die Umsetzung der ausgewählten Anforderungen (Maßnahmen) kann beginnen. Anderenfalls helfen die folgenden Abschnitte 8.2 und ggf. 8.3 dabei, mit den Abweichungen umzugehen.

<!-- page: 47 -->

## 8.2 Vorgehensweise bei Abweichungen

Wenn der Realitätsabgleich Unterschiede zwischen den durch das Profil abgedeckten Referenzarchitektur und der Anwenderinstitution ergibt, muss eine Ergänzung stattfinden. Diese findet sich in der Vorgehensweise zur Profilanwendung in Schritt 6a, dessen Fließbild in Abb. 8.1 dargestellt wird. Die Legende entspricht der in Abb. 3.1 vorgestellten Legende für das Fließbild zur gesamten Profilanwendung (Abb. 3.2).

Abb. 8.1: Vorgehensweise bei Abweichung der ICS-Anlagen des Profilanwenders von den im Profil wählbaren Referenzarchitekturen

<!-- image -->

<!-- page: 48 -->

Das Vorgehen unterscheidet sich je nachdem, ob ein fehlender Anwendungsfall oder ein fehlendes Zielobjekt identifiziert wurde:

- Fehlt ein Anwendungsfall, kann er im am ehesten passenden Unterprofil ergänzt werden. Die Anwendungsfallergänzung kann aus einem völlig neuen Anwendungsfall bestehen; in den meisten Fällen sollte jedoch die Modifikation eines bestehenden Falles ausreichen. Sie kann darin bestehen, dem Anwendungsfall ein zusätzliches Zielobjekt  hinzuzufügen - dies zieht dann auch die Wahl passender IT-Grundschutz-Bausteine für die Modellierung und die Auswahl von nötigen Anforderungen aus die Bausteinen nach sich. Möglich sind aber auch die Modellierung eines Zielobjektes mit zusätzlichen Bausteinen oder die Auswahl von zusätzlichen Anforderungen aus bereits zur Modellierung verwendeten Bausteinen.
- Fehlt ein Zielobjekt, ist es ratsam, zunächst einen Blick ins IT-Grundschutz-Kompendium zu werfen: Gibt es für das fehlende Zielobjekt einen passenden Baustein?
- o Falls ja, kann der Baustein in den relevanten Anwendungsfällen in den Unterprofilen ergänzt werden - dies entspricht der bereits vorgestellten Vorgehensweise zur Anwendungsfallergänzung.
- o Hilft das IT-Grundschutz-Kompendium nicht weiter, muss für das fehlende Zielobjekt  oder  die  zusätzliche  Gefährdung  eine ergänzende  Risikoanalyse durchgeführt  werden,  um  eventuell  notwendige  zusätzliche  Maßnahmen  zu identifizieren. Dazu bietet der BSI-Standard 200-3 eine detaillierte Anleitung. Einige spezifische Hilfestellungen zur ergänzenden Risikoanalyse für die Anwender dieses Profils enthält Abschnitt 8.3.

In jedem Fall sollten zum Abschluss der Ergänzung die zusätzlichen Maßnahmen (modernisiert: Anforderungen) und ggf. zusätzlichen Zielobjekte, Anwendungsfälle oder Bausteine in der Zielobjekt-Maßnahmen-Tabelle ergänzt werden. Mit der nun vollständigen Liste kann zur Umsetzung der Anforderungen in konkrete Maßnahmen in Schritt 7 übergegangen werden. Dabei dient die im Profilverlauf erstellte Zielobjekt-Maßnahmen-Tabelle als individuell an den Profilanwender angepasste Leitlinie, die für jedes Zielobjekt alle umzusetzenden Maßnahmen enthält.

## 8.3 Hilfestellungen zur ergänzenden Risikoanalyse

Das Vorgehen zur ergänzenden Risikoanalyse ist im BSI-Standard 200-3 ausführlich beschreiben  [BSI16c].  Bevor  im  Rahmen  der  ergänzenden  Risikoanalyse  zusätzliche  Maßnahmen identifiziert werden können, sind einige Vorarbeiten erforderlich: Das Erstellen einer Gefährdungsübersicht, die Identifikation zusätzlicher Gefährdungen und die Einstufung von Gefährdungen in Risikostufen.

In den folgenden Abschnitten 8.3.1 bis 8.3.3 sind einige Hilfestellungen zu diesen Vorarbeiten gegeben.

<!-- page: 49 -->

## 8.3.1  Gefährdungsübersicht

Die Risikoanalyse soll die im bisherigen Verlauf ausgewählten Anforderungen (Maßnahmen) nur ergänzen. Sind für eine bestimmte Gefährdung bereits ausreichende Maßnahmen gewählt worden, muss sie in der Risikoanalyse nicht mehr berücksichtigt werden. Aus diesem Grund ist für eine ergänzende Risikoanalyse eine Übersicht über im Profil berücksichtigte Gefährdungen wichtig.

Zu diesem Zweck enthält das vorliegende Profil zu jedem verwendeten Baustein eine Gefährdungstabelle. In der Tabelle werden alle in der Maßnahmenauswahltabelle des Bausteins gewählten  Maßnahmen den Gefährdungen zuordnet, gegen die sie  wirken  sollen.  An  dieser Stelle wird - wie schon bei der Maßnahmenauswahl - beispielhaft die Tabelle für den Baustein B 1.0: Sicherheitsmanagement (Tab. 8.2) gezeigt. Die Tabellen der weiteren im Hauptprofil verwendeten Bausteine finden sich im kostenpflichtigen Anhang B (Wasserwirtschaft). Auch in  den  Unterprofilen  enthält  der  kostenpflichtige  Anhang  B (Wasserwirtschaft) eine Gefährdungstabelle für jeden im Unterprofil verwendeten Baustein.

Die Legende für die Gefährdungstabellen entspricht der für die Maßnahmenauswahltabellen. Nicht  ausgewählte  Maßnahmen wurden jedoch aus den Gefährdungstabellen entfernt und jede Maßnahme einer oder mehreren orangefarben hinterlegten Gefährdungen zugeordnet.

Durch orangefarben hinterlegte Felder am rechten Tabellenrand ist gekennzeichnet, in welchen Anwendungsfällen eine Gefährdung relevant ist (orange) und welche Maßnahmen dagegen ausgewählt wurden (grün). Wurden für eine Gefährdung nur für kritische Infrastrukturen (KRITIS) Gegenmaßnahmen gewählt, sind auch die orangefarbenen Felder zusätzlich mit einem 'K' gekennzeichnet.

Auf diese Weise lassen sich mit den Gefährdungstabellen die berücksichtigten Gefährdungen für die individuell ausgewählten Anwendungsfälle schnell erfassen, sodass mit der Identifikation zusätzlicher Gefährdungen begonnen werden kann.

Die Informationen über die Gefährdungen sollten auch in der Zielobjekt-Maßnahmen-Tabelle als zentrales Ergebnis der Profilanwendung dokumentiert werden (siehe Tab. 8.1: Ergänzung von Gefährdungen in der Zielobjekt-Maßnahmen-Tabelle).

Tab. 8.1: Ergänzung von Gefährdungen in der Zielobjekt-Maßnahmen-Tabelle

| Zielobjekt   | Anwendungs- fall   | Gefährdung                                                                                    | Baustein   | Anforderung (Maßnahme)   |
|--------------|--------------------|-----------------------------------------------------------------------------------------------|------------|--------------------------|
| …            | …                  | 4) Aus den Gefähr- dungstabellen : Ge- fährdungen, gegen die die empfohlenen Maßnahmen wirken | …          | …                        |

<!-- page: 50 -->

Tab. 8.2: Gefährdungstabelle für den Baustein B 1.0: Sicherheitsmanagement

| Gefährdungen des Bausteins B 1.0: Sicherheitsmanagement:   | Gefährdungen des Bausteins B 1.0: Sicherheitsmanagement:                             | HP   |
|------------------------------------------------------------|--------------------------------------------------------------------------------------|------|
|                                                            | = Gefährdung für das Hauptprofil (HP)                                                |      |
| K                                                          | = Gegenmaßnahme nur für KRITIS / hohen Schutzbedarf                                  |      |
| G 2.66                                                     | Unzureichendes Sicherheitsmanagement                                                 |      |
| M 2.192                                                    | Erstellung einer Leitlinie zur Informationssicherheit                                |      |
| M 2.193                                                    | Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit             |      |
| M 2.195                                                    | Erstellung eines Sicherheitskonzeptes                                                |      |
| M 2.197                                                    | Integration der Mitarbeiter in den Sicherheitsprozess                                |      |
| M 2.199                                                    | Aufrechterhaltung der Informationssicherheit                                         |      |
| M 2.200                                                    | Management-Berichte zur Informationssicherheit                                       | K    |
| M 2.201                                                    | Dokumentation des Sicherheitsprozesses                                               | K    |
| M 2.336                                                    | Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitungsebene |      |
| M 2.337                                                    | Integration der Informationssicherheit in organisationsweite Abläufe und Prozesse    |      |
| G 2.106                                                    | Störung der Geschäftsabläufe aufgrund von Sicherheitsvorfällen                       |      |
| M 2.335                                                    | Festlegung der Sicherheitsziele und -strategie                                       |      |

<!-- page: 51 -->

## 8.3.2  Nicht behandelte Gefährdungen und Restrisiko

Einige Gefährdungen werden durch vorliegende IT-Grundschutz-Profil explizit nicht behandelt. Diese Gefährdungen können anhand der Gründe für ihre Nichtbehandlung in folgende drei Kategorien unterteilt werden:

1. Die Gefährdungen fallen nicht in den Geltungsbereich des Profils beziehungsweise treffen auf die Zielgruppe des Profils nicht zu.
2. Die Gefährdungen fallen in den Geltungsbereich des Profils, werden jedoch bereits in anderen Regelwerken behandelt , deren Implementierung vorausgesetzt wird.
3. Die Gefährdungen fallen in den Geltungsbereich des Profils, gegen sie werden jedoch keine Maßnahmen unternommen. Stattdessen werden die damit verbundenen Risiken akzeptiert ( Restrisiko ).

Diese Gefährdungen aus den Kategorien 1 und 2 müssen auch in einer ergänzenden Risikoanalyse nicht berücksichtigt werden. Dazu zählen:

- Gefährdungen, die keine Auswirkungen auf die Erbringung der kritischen Dienstleistung haben. Die Einschränkung des Anlagenbetriebs ist die einzig relevante Schadenskategorie bei der Risikoeinstufung.
- Gefährdungen für die Vertraulichkeit von Daten. Datenschutz ist nicht Ziel des Profils.
- Gefährdungen, die den Zugang zu den (ab)wassertechnischen Anlagen, die Stromversorgung der (ab)wassertechnischen Anlagen und Planung, Bau, Betrieb und Instandhaltung der (ab)wassertechnischen Anlagen betreffen. Für diese Gefährdungen existieren bereits Richtlinien in anderen branchenspezifischen Regelwerken der Wasserwirtschaft. Für ICS-Anlagen, also die Automatisierungstechnik für die (ab)wassertechnischen Anlagen, werden diese Aspekte jedoch berücksichtigt [B3S17c; B3S17b].
- Gefährdungen, die aus mangelnder Qualifikation und Organisation von Mitarbeitern sowie mangelhaftem Risikomanagement entstehen. Auch diese Aspekte sind bereits im Regelwerk der DWA beziehungsweise des DVGW abgedeckt [B3S17c; B3S17b].

Gefährdungen der dritten Kategorie können in einer ergänzenden Risikoanalyse berücksichtigt werden, wenn der Profilanwender das mit ihnen verbundene Restrisiko nicht tragen möchte und Gegenmaßnahmen möglich sind.

Die Entscheidung, welche Gefährdungen für die Wasserwirtschaft relevant sind, hat für den B3S WA - genau wie die Auswahl der relevanten Maßnahmen - eine Befragung von Fachleuten ergeben [B3S17b]. Das Ergebnis ist für die im vorliegenden Profil außerhalb der Sperrklausel exemplarisch behandelten Bausteine:

- G 2.1: Fehlende oder unzureichende Regelungen und
- G 5.51: Missbrauch der Routing-Protokolle

Nach der Zusammenstellung aller nicht berücksichtigten Gefährdungen für die einzelnen Bausteine sollte geprüft werden, ob die Gefährdung durch eine ausgewählte Maßnahme in einem anderen Baustein innerhalb des Profils abgedeckt wird. Dies trifft auf Gefährdung G 2.1 zu, sodass als nicht berücksichtigte Gefährdung für die exemplarisch betrachteten Bausteine nur G 5.51 übrig bleibt.

<!-- page: 52 -->

Eine vollständige Liste der nicht berücksichtigten Gefährdungen unter Berücksichtigung aller Bausteine des Hauptprofils und des Unterprofils AR befindet sich im kostenpflichtigen Anhang B (Wasserwirtschaft). Sie sollte nach der Erstellung der anderen Unterprofile ergänzt werden.

Es sind Gefährdungen denkbar, die zur dritten Kategorie zählen, weil es keine (ausreichenden) Maßnahmen gegen sie gibt und die resultierenden Risiken deswegen akzeptiert werden müssen .  Auch solche Gefährdungen sollten im Profil benannt sein. Speziell für die Wasserwirtschaft sind im B3S WA keine solche Gefährdungen angegeben. Jedoch gibt es unabhängig von der Branche Gefährdungen, für die stets ein Restrisiko akzeptiert werden muss:

- Advanced Persistent Threats (APT), also elaborierte, zielgerichtete Angriffe. Sie können präventiv nicht völlig ausgeschlossen werden; ihre Auswirkungen jedoch durch eine schnelle Detektion und Reaktion abgemildert.
- Social Engineering, also das Ausnutzen einer Vertrauensbasis zu Mitarbeitern der zu schützenden Institution. Awareness-Training helfen, Mitarbeiter für solche Angriffe zu sensibilisieren, können sie jedoch nicht komplett ausschließen.

Für die ergänzende Risikoanalyse von ICS-Netzen sei zudem erwähnt, dass Safety-Mechanismen kein adäquater Ersatz für Security-Maßnahmen sind (und umgekehrt). Durch einen Angriff auf (oder ein Versagen von) ICS-Netzen können Safety-Mechanismen außer Kraft gesetzt werden. Aus diesem Grund sollten Safety-Mechanismen einerseits durch Security-Maßnahmen zusätzlich abgesichert werden, andererseits jedoch möglichst wenig auf die Security der ICS-Netze angewiesen sein [KL15].

<!-- page: 53 -->

## 8.3.3  Risikomatrix

Der nächste Schritt nach der Identifikation von Gefährdungen ist ihre Einstufung in Risikokategorien. Dafür wird im BSI-Standard 200-3 eine Risikomatrix verwendet, wie sie in Abb. 8.2 dargestellt ist.

Die Einstufung erfolgt in Abhängigkeit von Eintrittswahrscheinlichkeit und potenzieller Schadenshöhe einer Gefährdung. Gefährdungen mit einer hohen Eintrittswahrscheinlichkeit und einer hohen Schadenshöhe werden in der Risikomatrix rechts oben verordnet und bekommen somit ein hohes Risiko zugeordnet (rot). Mit sinkender Schadenshöhe und / oder Eintrittswahrscheinlichkeit sinkt auch die Risikoeinstufung zu mittlerem (gelb) oder niedrigem (grün) Risiko.

<!-- image -->

Eintrittswahrscheinlichkeit

Abb. 8.2: Allgemeine Risikomatrix (angelehnt an [BSI16c])

Der BSI-Standard 200-3 schlägt für die Risikoeinschätzung sowohl für die Eintrittswahrscheinlichkeit als auch für die Schadenshöhe Kategorien vor, die jedoch individuell an die eigene Institution angepasst werden sollten [BSI16c].

In Anlehnung an den B3S WA wird speziell für die Wasserwirtschaft die folgende Anpassung der Risikomatrixdimensionen vorgeschlagen (siehe Abb. 8.3) [B3S17b; B3S17c]:

<!-- page: 54 -->

Abb. 8.3: Risikomatrix für die Wasserwirtschaft (angelehnt an [B3S17b])

<!-- image -->

## · Eintrittswahrscheinlichkeit:

- o Sehr gering (seltener als einmal in fünf Jahren)
- o Gering (seltener als einmal in zwei Jahren)
- o Mittel (bis zu einmal im Jahr)
- o Hoch (bis zu dreimal im Jahr)
- o Sehr hoch (mehr als dreimal im Jahr)

## · Schadenshöhe = Grad der Einschränkung des Anlagenbetriebs:

- o Geringe Einschränkung (Anlage mindestens im Standardmodus betreibbar, geringe Einschränkung der Dienstleistungsqualität)
- o Spürbare  Einschränkung  (Anlage  mit  geringen  Einschränkungen  betreibbar, spürbare  Einschränkung  der  Dienstleitungsqualität  innerhalb  der  zulässigen Grenzen)
- o Deutliche Einschränkung (Anlage nicht mehr vollständig betreibbar, Dienstleistungsqualität ist merklich eingeschränkt, die Qualität liegt unterhalb der vorgegebenen Grenzen)
- o Erhebliche Einschränkung (Anlage nur noch teilweise betreibbar, Erbringung der Dienstleitung nur noch teilweise möglich, Qualität liegt erheblich unter den vorgegebenen Grenzen)
- o Totalausfall (Anlage nicht mehr betreibbar, Dienstleistung kann nicht mehr erbracht werden)

<!-- page: 55 -->

## · Risiko:

- o Rot (deutlich zu minderndes Risiko)
- o Gelb (einzugrenzendes Risiko)
- o Grün (akzeptables Risiko)

<!-- page: 56 -->

## 9 Anhang A

- 9.1 Glossar und Abkürzungsverzeichnis

| AV              | Antivirensoftware                                                                                                                                                                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AWWA            | American Water Works Association                                                                                                                                                                                                                                                |
| B3S             | Branchenspezifischer Sicherheitsstandard                                                                                                                                                                                                                                        |
| B3S WA          | Branchenspezifischer Sicherheitsstandard Wasser / Abwasser Vor dem Hintergrund des IT-Sicherheitsgesetzes von DWA und DVGW entworfener Informationssicherheitsstandard für die Wasser- wirtschaft.                                                                              |
| BSI             | Bundesamt für Sicherheit in der Informationstechnik                                                                                                                                                                                                                             |
| BSI-KritisV     | Verordnung zur Bestimmung Kritischer Infrastrukturen nach dem BSI- Gesetz Deutsches Gesetz, das festlegt, welche Anlagenbetreiber innerhalb der KRITIS-Branchen unter das IT-Sicherheitsgesetz fallen.                                                                          |
| DCS             | Distributed Control System                                                                                                                                                                                                                                                      |
| DVGW            | Deutscher Verein des Gas- und Wasserfachs                                                                                                                                                                                                                                       |
| DWA             | Deutsche Vereinigung für Wasserwirtschaft, Abwasser und Abfall                                                                                                                                                                                                                  |
| EWS             | Engineering-Workstation Rechner für die Erstellung und Kompilation der Programme für die Steuergeräte (SPSen). Dedizierte Rechner für diesen Zweck werden auch als Programmiergerät (PG) bezeichnet. Die kompilierten Pro- gramme werden anschließend auf die SPSen überspielt. |
| FW              | Firewall. Software (ggf. auf dediziertem Gerät), die anhand von Regeln den Datenverkehr im Netz filtert.                                                                                                                                                                        |
| Geltungsbereich | Der Geltungsbereich eines IT-Grundschutz-Profils definiert die Ziel- gruppe, an die sich das Profil wendet, und ihre Rahmenbedingungen.                                                                                                                                         |
| Historian       | Datenbank für die Archivierung von Prozessdaten                                                                                                                                                                                                                                 |
| HMI             | Human-Machine-Interface Bedienschnittstelle einer automatisierten Anlage. Das HMI ermöglicht sowohl die Überwachung als auch den manuellen Eingriff in den au- tomatisierten Prozess, etwa durch das Setzen von Sollwerten und das Bedienen von Aktoren.                        |

<!-- page: 57 -->

| HP                     | Hauptprofil                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HW                     | Hardware                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ICS                    | Industrial Control System: Systeme zur Fertigungs- und Prozessautomatisierung im industriellen Umfeld. Unter den Begriff fallen in diesem Profil alle technischen Sys- teme, die für die automatisierte Steuerung eines Prozesses und die menschliche Überwachung dieser automatisierten Steuerung zustän- dig sind.                                                                                                                                  |
| ICS-Security           | IT-Sicherheit für ICS: Befasst sich mit auf ICS-Geräten elektronisch gespeicherten Informationen. Das Ziel der ICS-Sicherheit ist jedoch nicht nur der Schutz der Informationen, sondern insbesondere auch des Prozesses und der Anlagen, die diese Informationen steuern. Wird in diesem Profil mit dem englischen Begriff Security verwendet, um sie von der Safety abzugrenzen, die in ICS-Netzen ebenfalls eine hohe Rolle spielt (siehe Safety). |
| IDS                    | Intrusion Detection System                                                                                                                                                                                                                                                                                                                                                                                                                            |
| IEC                    | International Electrotechnical Commission Internationale Normungsorganisation für Elektrotechnik und Elektro- nik                                                                                                                                                                                                                                                                                                                                     |
| Informationssicherheit | Schutz von Informationen jeglicher Art und Herkunft. Dabei können Informationen sowohl auf Papier, in Rechnersystemen oder auch in den Köpfen der Nutzer gespeichert sein [BSI08]                                                                                                                                                                                                                                                                     |
| Informationsverbund    | Der Informationsverbund definiert, welche Geschäftsprozesse im Rahmen eines IT-Grundschutz-Profils betrachtet werden und die Ge- samtheit von infrastrukturellen, organisatorischen, personellen und technischen Komponenten, die für die Ausführung der Geschäftspro- zesse nötig sind.                                                                                                                                                              |
| Institution            | Oberbegriff für Unternehmen und Behörden                                                                                                                                                                                                                                                                                                                                                                                                              |
| IP                     | Internet Protocol: Protokoll auf Schicht 3 des ISO/OSI-Referenzmodells, das für die In- ternet-Kommunikation verwendet wird.                                                                                                                                                                                                                                                                                                                          |
| IPS                    | Intrusion Prevention System                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ISO                    | International Organization for Standardization Internationale Normungsorganisation                                                                                                                                                                                                                                                                                                                                                                    |
| IT                     | Information Technology bzw. Informationstechnik. Oberbegriff für In- formations- und Datenverarbeitung durch technische Geräte, Dienste und Funktionen.                                                                                                                                                                                                                                                                                               |

<!-- page: 58 -->

| IT-Sicherheit                  | Schutz elektronisch gespeicherter Informationen und deren Verarbei- tung [BSI08]                                                                                                                                                                                                                                                                                                    |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IT-SiG                         | Gesetz zur Erhöhung der Sicherheit informationstechnischer Sys- teme, kurz: IT-Sicherheitsgesetz [IT-SiG15] Seit Juli 2015 geltendes deutsches Gesetz, das KRITIS-Betreiber dazu verpflichtet, ihre kritischen Dienstleistungen nach dem Stand der Technik angemessen abzusichern und dies mindestens alle zwei Jahre überprüfen zu lassen. Auch die Meldung von IT-Sicherheitsvor- |
| Konzentrierte Anlage           | Automatisierungstechnische Anlage mit konzentrierter ICS-Netzstruk- tur                                                                                                                                                                                                                                                                                                             |
| Konzentrierte ICS-Netzstruktur | Konzentrierte ICS-Netzstruktur                                                                                                                                                                                                                                                                                                                                                      |
| KRITIS                         | Kritische Infrastruktur nach IT-Sicherheitsgesetz bzw. BSI-Kritis-Ver- ordnung [IT-SiG15; KritisV16].                                                                                                                                                                                                                                                                               |
| LAN                            | Local Area Network: Rechner- oder Kommunikationsnetz, das sich in etwa über einen Ge- bäudekomplex ausdehnt.                                                                                                                                                                                                                                                                        |
| Leitstand                      | In diesem Profil bezeichnet der Leitstand die Räumlichkeit bzw. Funk- tionseinheit, in der mindestens Funktionen eines HMI, möglicher- weise aber weitere zur Prozessleitebene der Automatisierungspyra- mide gehörigen Funktionalitäten verortet sind (Engineering-Worksta- tion, Control Server, …)                                                                               |
| Modellierung                   | Im IT-Grundschutz die Zuordnung von mindestens einem IT-Grund- schutz-Baustein zu jedem Zielobjekt. Da Bausteine Anforderungen enthalten, impliziert die Modellierung eine Auswahl von Anforderun- gen für die Zielobjekte eines Informationsverbunds.                                                                                                                              |
| Office-IT                      | Oberbegriffe für Hard- und Software, die üblicherweise im Büro-Um- feld verwendet wird - etwa PCs, Laptops, Server und Drucker.                                                                                                                                                                                                                                                     |
| OS                             | Betriebssystem (Operating System)                                                                                                                                                                                                                                                                                                                                                   |
| OT                             | Operational Technology: Oberbegriff für ICS und weitere Automationslösungen, die nicht im industriellen Umfeld verortet sind, z.B. Gebäudeleittechnik oder Inter- net-of-Things-Geräte. Er wird vor allem zur Abgrenzung von der IT (Information Technology) verwendet                                                                                                              |

<!-- page: 59 -->

| PCS                        | Process Control System (deutsch: Prozessleitsystem, PLS)                                                                                                                                                                                                                                                                       |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PLC                        | Programmable Logic Controller (deutsch: Speicherprogrammierbare Steuerung, SPS) In diesem Profil als Oberbegriff für automatische Steuergeräte auf der Steuerungsebene der Automatisierungspyramide verwendet.                                                                                                                 |
| PLS                        | Prozessleitsystem (englisch: Process Control System, PCS)                                                                                                                                                                                                                                                                      |
| Referenzarchitektur        | Eine typische Architektur des Informationsverbunds einer Referenzin- stitution. Eine Referenzarchitektur besteht aus Zielobjekten und ei- nem oder mehreren Netzplänen.                                                                                                                                                        |
| Referenzinstitution        | Eine typische Institution der Branche oder Anwendergruppe, an die ein IT-Grundschutz-Profil sich wendet.                                                                                                                                                                                                                       |
| Safety                     | In der Automatisierungstechnik steht Safety meist für funktionaler Si- cherheit und hat zum Ziel, dass Maschinen oder Geräte funktionieren, ohne für ihre Umwelt gefährliche Zustände einzunehmen. Um dies sicherzustellen, sind spezielle Steuereinheiten aktiv, die gefährliche Maschinenzustände verhindern sollen [IEC15]. |
| SCADA                      | Supervisory Control and Data Acquisition                                                                                                                                                                                                                                                                                       |
| Security                   | siehe IT-Sicherheit                                                                                                                                                                                                                                                                                                            |
| SPS                        | Speicherprogrammierbare Steuerung (englisch: Programmable Logic Controller, PLC) In diesem Profil als Oberbegriff für automatische Steuergeräte auf der Steuerungsebene der Automatisierungspyramide verwendet.                                                                                                                |
| SW                         | Software                                                                                                                                                                                                                                                                                                                       |
| UP                         | Unterprofil                                                                                                                                                                                                                                                                                                                    |
| Verteilte Anlage           | Automatisierungstechnische Anlage mit verteilter ICS-Netzstruktur                                                                                                                                                                                                                                                              |
| Verteilte ICS-Netzstruktur | Verteilte ICS-Netzstruktur                                                                                                                                                                                                                                                                                                     |
|                            | In diesem Profil bedeutet eine verteilte ICS-Netzstruktur, dass die ICS-Steuerungskomponenten über einen größeren Bereich als den eines Gebäudekomplexes verteilt sind. Die Anlage hat einen zentra- len Leitstand, der mit den Steuerungskomponenten mittels WAN- Technik kommuniziert.                                       |
| VPN                        | Virtual Private Network: Logisches privates Netz auf Basis einer öffentlichen Netzinfrastruktur, das zusätzliche Authentisierungs- und Verschlüsselungstechnik, z.B. IPsec, verwendet.                                                                                                                                         |
| WAN                        | Wide Area Network: Rechner- oder Kommunikationsnetz, dessen Ausdehnung über einen                                                                                                                                                                                                                                              |

<!-- page: 60 -->

|                  | Gebäudekomplex hinausgeht. WANs können sich über die gesamte Welt ausdehnen. Ein Beispiel ist das Internet. In der Wasserwirtschaft wird für die Kommunikation über ein WAN häufig der Begriff Fern- wirktechnik verwendet.   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Wasserwirtschaft | In diesem Profil der Oberbegriff für Institutionen, die Dienstleistung innerhalb der Wasserversorgung und der Abwasserbeseitigung er- bringen.                                                                                |
| WS               | Workstation, zum Beispiel in 'Engineering-WS'                                                                                                                                                                                 |
| Zielobjekt       | Zielobjekte sind im IT-Grundschutz die IT-Systeme, Infrastruktur, An- wendungen und Netzkomponenten, die den Informationsverbund ausmachen und im Rahmen einer Sicherheitskonzeption abgesichert werden sollen.               |

<!-- page: 61 -->

## 9.2 Literaturverzeichnis

| [AbwV97]   | Verordnung über Anforderungen an das Einleiten von Abwasser in Gewässer (Abwasserverordnung - AbwV) (1997-03-21). URL www.gesetze-im-internet.de/bundesrecht/abwv/gesamt.pdf                                                                                                                                  |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AWRL91]   | Richtlinie 91/271/EWG über die Behandlung von kommunalem Abwasser. In: Amtsblatt der Europäischen Gemeinschaften (1991-05-21). URL eur-lex.europa.eu/LexUriServ/LexUri- Serv.do?uri=OJ:L:1991:135:0040:0052:DE:PDF                                                                                            |
| [AWWA14]   | American Water Works Association (AWWA): Process Control System Security Guidance for the Water Sector. 2014 (1). URL www.awwa.org/Portals/0/files/legreg/documents/AWWACybersecuri- tyguide.pdf Überprüfungsdatum 2017-02-07                                                                                 |
| [B3S17a]   | Deutsche Vereinigung für Wasserwirtschaft, Abwasser und Abfall (DWA) ; Deutscher Verein des Gas- und Wasserfaches (DVGW): Branchenspezifischer Sicherheitsstandard Wasser/Abwasser : IT-Sicherheits- leitfaden. 2017                                                                                          |
| [B3S17b]   | Deutsche Vereinigung für Wasserwirtschaft, Abwasser und Abfall (DWA) ; Deutscher Verein des Gas- und Wasserfaches (DVGW): Branchenspezifischer Sicherheitsstandard Wasser/Abwasser : Handbuch zum IT-Sicherheitsleitfaden. 2017                                                                               |
| [B3S17c]   | Deutsche Vereinigung für Wasserwirtschaft, Abwasser und Abfall (DWA) ; Deutscher Verein des Gas- und Wasserfaches (DVGW): M 1060 bzw. W 1060 (M) : IT-Sicherheit - Branchenstandard Wasser/Abwas- ser. 2017                                                                                                   |
| [BMI09]    | Bundesministerium des Innern (BMI): Nationale Strategie zum Schutz Kriti- scher Infrastrukturen (KRITIS-Strategie). 2009. URL www.bmi.bund.de/SharedDocs/Downloads/DE/Broschueren/2009/kri- tis.pdf;jsessionid=32AA6FEA813259E0BA0A82AACEB7325A.2_cid287?__ blob=publicationFile Überprüfungsdatum 2017-01-31 |
| [BSI08]    | Bundesamt für Sicherheit in der Informationstechnik (BSI): BSI-Standard 100-1 : Managementsysteme für Informationssicherheit ISMS. 2., überarb. Aufl. Köln : Bundesanzeiger-Verl., 2008 (Unternehmen und Wirt- schaft)                                                                                        |

<!-- page: 62 -->

| [BSI15]     | Bundesamt für Sicherheit in der Informationstechnik (BSI): KRITIS Sektorstudie : Ernährung und Wasser. 2015. URL www.kritis.bund.de/SharedDocs/Downloads/Kritis/DE/Sektorstudie_ Ern%C3%A4hrung_Wasser.pdf?__blob=publicationFile Überprüfungsdatum 2017-02-07                                          |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BSI16a]    | Bundesamt für Sicherheit in der Informationstechnik (BSI): Das IT-Sicherheitsgesetz : Kritische Infrastrukturen schützen. 2016. URL www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/Bro- schueren/IT-Sicherheitsgesetz.pdf?__blob=publicationFile&v=5 Überprüfungsdatum 2017-02-02            |
| [BSI16b]    | Bundesamt für Sicherheit in der Informationstechnik (BSI): IT-Grundschutz-Kataloge: Standardwerk zur IT-Sicherheit : 15. Ergänzungslieferung 2016. Bonn : Bundesanzeiger Verlag, 2016                                                                                                                   |
| [BSI16c]    | Bundesamt für Sicherheit in der Informationstechnik (BSI): BSI-Standard 200-3 (Community Draft) : Risikoanalyse auf der Basis von IT- Grundschutz. 2016. URL www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT- Grundschutz-Modernisierung/BSI_Standard_200-3.pdf?__blob=publication- File&v=3 |
| [BSI17]     | Bundesamt für Sicherheit in der Informationstechnik (BSI): BSI-Standard 200-2 (Community Draft) : IT-Grundschutz-Methodik. 2017                                                                                                                                                                         |
| [BSIG16]    | Gesetz über das Bundesamt für Sicherheit in der Informationstechnik (2016) URL www.gesetze-im-internet.de/bsig_2009/BJNR282110009.html Überprüfungsdatum 2017-06-12                                                                                                                                     |
| [DIN16323]  | DIN EN 16232:2014-07 Wörterbuch für Begriffe der Abwassertechnik; Drei- sprachige Fassung EN 16232:2014                                                                                                                                                                                                 |
| [DIN4045]   | DIN 4045:2003-08 Abwassertechnik - Grundbegriffe                                                                                                                                                                                                                                                        |
| [DIN4046]   | DIN 4046:1983-09 Wasserversorgung: Begriffe                                                                                                                                                                                                                                                             |
| [IT-SiG15]  | Gesetz zur Erhöhung der Sicherheit informationstechnischer Systeme. In: Bundesgesetzblatt 2015 Teil I (2015-07-17), Nr. 31, S. 1324-1331. URL www.bgbl.de/xaver/bgbl/start.xav?startbk=Bundesanzeiger_ BGBl&jumpTo=bgbl115s1324.pdf Überprüfungsdatum 2017-02-02                                        |
| [KL15]      | KNAPP, Eric D. ; LANGILL, Joel Thomas: Industrial network security : Securing critical infrastructure networks for smart grid, SCADA, and other in- dustrial control systems. 2. ed. Amsterdam : Syngress Elsevier, 2015                                                                                |
| [KritisV16] | Verordnung zur Bestimmung Kritischer Infrastrukturen nach dem BSI-Gesetz. In: Bundesgesetzblatt 2016 Teil I (2016-04-22), Nr. 20, S. 958-969.                                                                                                                                                           |

<!-- page: 63 -->

URL www.bgbl.de/xaver/bgbl/start.xav?startbk=Bundesanzeiger\_ BGBl&amp;jumpTo=bgbl116s0958.pdf Überprüfungsdatum 2017-02-02

[TrinkwV01] Verordnung über die Qualität von Wasser für den menschlichen Gebrauch (Trinkwasserverordnung - TrinkwV 2001) (2001-05-21). URL www.gesetze-im-internet.de/bundesrecht/trinkwv\_2001/gesamt.pdf Über-

prüfungsdatum 2017-02-22 [TWRL98] Richtlinie 98/83/EG über die Qualität von Wasser für den menschlichen Gebrauch. In: Amtsblatt der Europäischen Gemeinschaften (1998-11-03). URL eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:1998:330:0032:0054:DE:PDF Überprüfungsdatum 2017-02-22 [Verdi15] Vereinte Dienstleistungsgewerkschaft (ver.di): ver.di-Branchenanalyse Wasserwirtschaft 2015. 2015. URL ver-und-entsorgung.verdi.de/branchen/wasserwirtschaft\_1/ ++co++598a98d8-2976-11e6-831e-52540077a3af Überprüfungsdatum 2017-02-21 [WHG09] Gesetz zur Ordnung des Wasserhaushalts (Wasserhaushaltsgesetz - WHG) (2009-07-31). URL www.gesetze-im-internet.de/bundesrecht/whg\_2009/gesamt.pdf Überprüfungsdatum 2017-02-22

[WRRL00] Richtlinie 2000/60/EG zur Schaffung eines Ordnungsrahmens für Maßnahmen der Gemeinschaft im Bereich der Wasserpolitik. In: Amtsblatt der Europäischen Gemeinschaften (2000-10-23). URL eur-lex.europa.eu/resource.html?uri=cellar:5c835afb-2ec6-4577-bdf8756d3d694eeb.0003.02/DOC\_1&amp;format=PDF Überprüfungsdatum 2017-02-22

<!-- page: 64 -->

## 10 Anhang B (Pilotprofil)

## 10.1  Maßnahmenauswahltabellen

## 10.1.1  Baustein B 1.0

Tab. 10.1: Maßnahmenauswahltabelle für den Baustein B 1.0: Sicherheitsmanagement

| Maßnahmen des Bausteins B 1.0: Sicherheitsmanagement:   | Maßnahmen des Bausteins B 1.0: Sicherheitsmanagement:                             | Maßnahmen des Bausteins B 1.0: Sicherheitsmanagement:                                |    |
|---------------------------------------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|----|
| K                                                       | = Im Hauptprofil (HP) ausgewählt = Nur für KRITIS / hohen Schutzbedarf ausgewählt | = Im Hauptprofil (HP) ausgewählt = Nur für KRITIS / hohen Schutzbedarf ausgewählt    | HP |
| M 2.192                                                 | A                                                                                 | Erstellung einer Leitlinie zur Informationssicherheit                                |    |
| M 2.193                                                 | A                                                                                 | Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit             |    |
| M 2.195                                                 | A                                                                                 | Erstellung eines Sicherheitskonzeptes                                                |    |
| M 2.197                                                 | A                                                                                 | Integration der Mitarbeiter in den Sicherheitsprozess                                |    |
| M 2.199                                                 | A                                                                                 | Aufrechterhaltung der Informationssicherheit                                         |    |
| M 2.200                                                 | C                                                                                 | Management-Berichte zur Informationssicherheit                                       | K  |
| M 2.201                                                 | C                                                                                 | Dokumentation des Sicherheitsprozesses                                               | K  |
| M 2.335                                                 | A                                                                                 | Festlegung der Sicherheitsziele und -strategie                                       |    |
| M 2.336                                                 | A                                                                                 | Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitungsebene |    |
| M 2.337                                                 | A                                                                                 | Integration der Informationssicherheit in organisationsweite Abläufe und Prozesse    |    |
| M 2.338                                                 | Z                                                                                 | Erstellung von zielgruppengerechten Sicherheitsrichtlinien                           |    |
| M 2.339                                                 | Z                                                                                 | Wirtschaftlicher Einsatz von Ressourcen für Informationssicherheit                   |    |
| M 2.475                                                 | A                                                                                 | Vertragsgestaltung bei Bestellung eines externen IT-Sicherheitsbeauf- tragten        |    |
| M 6.16                                                  | Z                                                                                 | Abschließen von Versicherungen                                                       |    |

<!-- page: 65 -->

## 10.2  Gefährdungstabellen

## 10.2.1  Baustein B 1.0

Tab. 10.2: Gefährdungstabelle für den Baustein B 1.0: Sicherheitsmanagement

| Gefährdungen des Bausteins B 1.0: Sicherheitsmanagement:   | Gefährdungen des Bausteins B 1.0: Sicherheitsmanagement:                             |    |
|------------------------------------------------------------|--------------------------------------------------------------------------------------|----|
|                                                            | = Gefährdung für das Hauptprofil (HP)                                                | HP |
| K                                                          | = Gegenmaßnahme nur für KRITIS / hohen Schutzbedarf                                  |    |
| G 2.66                                                     | Unzureichendes Sicherheitsmanagement                                                 |    |
| M 2.192                                                    | Erstellung einer Leitlinie zur Informationssicherheit                                |    |
| M 2.193                                                    | Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit             |    |
| M 2.195                                                    | Erstellung eines Sicherheitskonzeptes                                                |    |
| M 2.197                                                    | Integration der Mitarbeiter in den Sicherheitsprozess                                |    |
| M 2.199                                                    | Aufrechterhaltung der Informationssicherheit                                         |    |
| M 2.200                                                    | Management-Berichte zur Informationssicherheit                                       | K  |
| M 2.201                                                    | Dokumentation des Sicherheitsprozesses                                               | K  |
| M 2.336                                                    | Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitungsebene |    |
| M 2.337                                                    | Integration der Informationssicherheit in organisationsweite Abläufe und Prozesse    |    |
| G 2.106                                                    | Störung der Geschäftsabläufe aufgrund von Sicherheitsvorfällen                       |    |
| M 2.335                                                    | Festlegung der Sicherheitsziele und -strategie                                       |    |

<!-- page: 66 -->

## 10.3  Nicht berücksichtigte Gefährdungen

Tab. 10.3: Liste nicht berücksichtigter Gefährdungen für die Bausteine B 1.0 und B 3.302

| G 5.51   | Missbrauch der Routing-Protokolle   |
|----------|-------------------------------------|

<!-- page: 67 -->

## 11 Anhang C (Pilotprofil)

Der Anhang C enthält Hilfestellungen, um auf Basis des vorliegenden Pilotprofils ein IT-Grundschutz-Profil für eine weitere Anwendergruppe zu erstellen.

## 11.1  Allgemeine Methodik für die Profilerstellung

Abb. 11.1 zeigt die Methodik zur Erstellung eines neuen IT-Grundschutz-Profils nach Vorbild des Pilotprofils. Stellen, an denen Methoden des IT-Grundschutzes (IT-GS) angewendet werden, sind orangefarben markiert.

In Schritt 1 müssen die potenziellen Profilanwender ausgewählt werden. Die Zielgruppe kann eine ganze Branche oder nur Teilbereiche einer Branche enthalten; wichtig ist jedoch, dass sie so homogen wie möglich bezüglich aller Eingrenzungskriterien ist. Gute Eingrenzungskriterien können sich je nach Branche unterscheiden und sowohl organisatorischer als auch technischer Natur sein. Beispiele sind Unternehmensstruktur, Rahmenbedingungen, in der Branche übliche IT beziehungsweise OT oder Netzstrukturen. Am Ende dieses Schrittes sollte ein klar definierter Geltungsbereich stehen. Die Zielgruppe kann als eine Referenzinstitution beschrieben werden; auch sollten ihre Rahmenbedingungen (Gesetze, Richtlinien) genannt werden. Aus der Perspektive der IT-Grundschutz-Methodik sollten an dieser Stelle die Vorgehensweise nach Standard 200-2 und das angestrebte Schutzniveau ausgewählt werden.

Aus der eingegrenzten Referenzinstitution muss in Schritt 2 ein  konkreter Teilbereich von Geschäftsprozessen ausgewählt werden, die im Rahmen des Profils betrachtet werden sollen. Dazu müssen für die Geschäftsprozesse ggf. die relevanten Anlagen, in jedem Fall jedoch die IT-Grundstruktur erfasst werden ( Informationsverbund ). Die IT-Struktur des gewählten Teilbereichs sollte möglichst homogen innerhalb der Anwendergruppe sein - und nicht zu umfangreich. Vonseiten der IT-Grundschutz-Methodik werden die ausgewählten Geschäftsprozesse an dieser Stelle mit einem Schutzbedarf versehen. Zur Profilerstellung gehört deshalb auch  die  sinnvolle  Einteilung  von  Schutzbedarfskategorien.  Die  Schutzbedarfs-  und  Schadenskategorien des BSI-Standards 200-2 [BSI17] sind dafür ein guter Ausgangspunkt.

Der folgende Schritt 3 ist die weitere Konkretisierung des Informationsverbunds zu einer Referenzarchitektur .  Die  Referenzarchitektur,  bestehend  aus  einer  Zielobjektliste  und  einem Netzplan, stellt innerhalb des IT-Grundschutz-Profils das Pendant zu den abzusichernden Objekten einer konkreten Institution dar, die den IT-Grundschutz anwendet. In vielen Fällen wird es nicht möglich sein, eine einzelne Referenzarchitektur festzulegen, da sich die Architekturen selbst  innerhalb  sehr  homogener  Anwenderzielgruppen  stark  unterscheiden.  Der  nachfolgende Abschnitt 11.2 erläutert eine Methodik für die Erstellung einer Referenzarchitektur, die diesen Variationen gerecht wird.

<!-- page: 68 -->

Abb. 11.1: Methodik zur Erstellung eines IT-Grundschutz-Profils nach Vorbild des Pilotprofils

<!-- image -->

Die Referenzarchitektur ist aus IT-Grundschutz-Perspektive die Grundlage für die Modellierung mit IT-Grundschutz-Bausteinen (im Pilotprofil: Modellierungstabellen) und die Auswahl von  Maßnahmen  (im  Pilotprofil:  Maßnahmenauswahltabellen)  zur  Erstellung  eines  Sicherheitskonzepts. Die Nichtauswahl von Maßnahmen aus ausgewählten Bausteinen sollte begründet werden. Nicht berücksichtigte Gefährdungen sollten notiert werden, um als Hilfestellung für die ergänzende Risikoanalyse ins Profil einfließen zu können.

<!-- page: 69 -->

11 Anhang C (Pilotprofil)

67

Natürlich kann bei der Profilerstellung nicht ignoriert werden, dass es trotz aller Bemühungen Profilanwender geben wird, deren Institution mit den Referenzarchitekturen unzureichend abgebildet wird. Wenn das erstellte Profil von der IT/OT-Architektur einer Institution zu sehr abweicht,  müssen  Profilanwender  eine  ergänzende  Risikoanalyse  nach  BSI-Standard  200-3 durchführen. Für diese Fälle sollte das Profil den Anspruch haben, den Zusatzaufwand auf ein Minimum zu beschränken. Im abschließenden Schritt 4 sollte der Profilersteller deswegen Hinweise zur Risikobehandlung geben, die die Risikoanalyse erleichtern (im Pilotprofil: Abschnitt 8.3)  - beispielsweise sinnvolle Matrixdimensionen für die Risikomatrix oder Hinweise auf berücksichtigte Gefährdungen (im Pilotprofil: Gefährdungstabellen), nicht berücksichtigte oder gegebenenfalls zu berücksichtigende Gefährdungen. Für alle Profilanwender können zudem Literaturhinweise hilfreich sein.

## 11.2  Methodik zur Berücksichtigung von Variationen in der Referenzarchitektur

In den meisten Fällen wird es nicht möglich sein, einer Profilanwendergruppe mit einer einzigen Referenzarchitektur gerecht zu werden. Die in diesem Abschnitt vorgestellte Methodik bietet deswegen eine Möglichkeit an, mit Variationen in der Referenzarchitektur umzugehen. Die Vorgehensweise ist in Abb. 11.2 veranschaulicht. Die Grundidee für den Umgang mit Variationen ist die Aufteilung des Profils in ein Hauptprofil und mehrere Unterprofile. Jedes Unterprofil ist auf einen Aspekt der Referenzarchitektur fokussiert und bietet verschiedene Teilreferenzarchitekturen für Variationen an, sodass die zutreffenden Teilarchitekturen ausgewählt und zu einer Gesamt-Referenzarchitektur zusammengesetzt werden können. Um das umzusetzen, sollte der Profilersteller zunächst eine generische Referenzarchitektur erstellen. Dazu muss er alle denkbaren Zielobjekte auflisten, die in einer Referenzarchitektur eines Profilanwenders maximal enthalten sein könnten - damit erhält er in Schritt 3a die generische Zielobjektliste . Außerdem sollte ein generischer Netzplan erstellt werden, in dem möglichst viele der generischen Zielobjekte enthalten sind ( Schritt 3b ). Der Netzplan stellt die Konfiguration und Verbindungen der Zielobjekte dar. Da sich Variationsmöglichkeiten in Konfiguration und Verbindungen oft gegenseitig ausschließen, müssen bei der Erstellung des generischen Netzplans mit hoher Wahrscheinlichkeit einzelne Variationen ausgewählt werden. Auf welche Variationen die Wahl konkret fällt, ist an dieser Stelle von untergeordneter Bedeutung; sie sollten jedoch mitsamt ihrer nicht gewählten Alternativen klar benannt werden. Der Zweck des generischen Netzplans liegt darin, dem Profilanwender einen beispielhaften Netzplan des gesamten Netzes an die Hand zu geben. Im Gegensatz dazu werden die im weiteren Verlauf erarbeiteten spezifischen Netzpläne nur Teilaspekte des Gesamtnetzplans beinhalten.

<!-- page: 70 -->

Abb. 11.2: Methodik für die Berücksichtigung von Variationsmöglichkeiten in der Referenzarchitektur anhand von Anwendungsfällen

<!-- image -->

Nun müssen in Schritt 3c Variationsmöglichkeiten der Referenzarchitektur identifiziert und in Gruppen eingeteilt werden. An dieser Stelle wird deutlich, warum eine sorgfältige Auswahl eines homogenen Geltungsbereichs und eng abgegrenzten Informationsverbunds fundamental ist: Die Zahl der Variationsmöglichkeiten würde anderenfalls schnell unbeherrschbar.

Gemäß der Zielsetzung, dass der Profilanwender möglichst wenig Vorkenntnisse benötigen sollte (und entsprechend der Erfahrung, dass Netzpläne in Institutionen häufig nicht vorhanden sind),  sollten  die  Variationsmöglichkeiten so beschrieben werden, dass der Profilanwender leicht beantworten kann, welche Variante für seine Institution zutrifft. Sinnvoll sind Formulierungen wie 'Das System kann / hat…'. Dies resultiert in der Benennung von Anwendungsfällen , die - je nachdem, welcher Aspekt in den Anwendungsfallen variiert wird - zu Anwendungsfallgruppen (= Unterprofilen) zusammengefasst werden. Sinnvolle Beispiele finden sich im vorliegenden Pilotprofil (siehe Tab. 3.2).

<!-- page: 71 -->

Im letzten Schritt 3d muss der Profilersteller nun für jeden der Anwendungsfälle prüfen, welche Zielobjekte der generischen Liste für eine Anwendungsfallgruppe relevant sind ( spezifische Zielobjektlisten )  und für jeden Anwendungsfall einen Netzplan erstellen ( spezische Netzpläne ). Das Resultat sind spezifische Referenzarchitekturen, die die Referenzarchitektur des Profils für eine große Zahl von Profilanwendern möglichst passgenau machen sollten. Vonseiten des IT-Grundschutzes kann nun mit der Schutzbedarfsfeststellung der einzelnen Zielobjekte (für jeden Anwendungsfall!) und der Modellierung und Maßnahmenauswahl fortgefahren werden.

Bei der Bausteinmodellierung eines in Unterprofile gesplitteten Profils können Bausteine in mehreren Unterprofilen eingesetzt, aber jeweils nur ein Teil der Maßnahmen ausgewählt werden. Dabei gilt die Faustregel: Ein Zielobjekt sollte in einem Unterprofil nur dann mit seinem speziellen Baustein (also beispielsweise der Baustein 'SPS' für eine SPS) modelliert werden, wenn im Unterprofil spezifische Maßnahmen für dieses Zielobjekt ergriffen werden sollen.

Eine Orientierungshilfe für die Zuordnung von Maßnahmen zu den einzelnen Unterprofilen gibt der folgende Abschnitt 11.3.

## 11.3  Orientierungshilfe für die Zuordnung von Maßnahmentypen zu den Unterprofilen

Dieser Abschnitt soll eine Orientierung bieten, wie die Unterprofile gegeneinander abzugrenzen sind; konkret: Was für Maßnahmentypen für welche Zielobjekte in welches Unterprofil passen.

Werden Anwendungsfälle in Unterprofilen mit bestimmten Bausteinen modelliert, müssen nicht alle Maßnahmen (bzw. Anforderungen) der Bausteine ausgewählt werden. Bei einer Nichtauswahl einer Maßnahme sind folgende Szenarien möglich:

- Die Maßnahme (Anforderung) wird für die Zielgruppe des Profils insgesamt nicht ausgewählt. In diesem Fall sollte die Nichtauswahl begründet werden.
- Die Maßnahme (Anforderung) wird für die Zielgruppe des Profils ausgewählt, aber nicht für  diesen  Anwendungsfall.  Stattdessen  wird  sie  in  einem  anderen  Anwendungsfall ausgewählt. Hierfür ist keine gesonderte Begründung notwendig.

Aus diesem Grund ist es während der Profilerstellung sinnvoll, einen Überblick zu haben, welche Maßnahmentypen zu welchen Anwendungsfällen (und damit Unterprofilen) gehören. Im Folgenden werden dazu zum Hauptprofil sowie zu jedem Unterprofil Faustregeln für geeignete Maßnahmentypen gegeben. Dabei wird auch angegeben, auf welche Zielobjekte sich die Maßnahmen jedes Unterprofils konzentrieren sollten. Zur Veranschaulichung der Faustregeln dienen konkrete Maßnahmen als Beispiele; sie werden in drei Kategorien eingeteilt:

<!-- page: 72 -->

1. Komplexitätsreduktion
- a. Segmentierung
- b. Härtung
- c. Principle of Least Privilege (RBAC)
- d. Etablieren von Standards
2. Zugriffsschutz
- a. Schutz vor Zugriff auf Netze und Hosts
- b. Schutz vor Ausführung von Schadprogrammen
- c. Schutz vor Zugriff auf Daten
3.  Systemkenntnis
- a. Dokumentation und Baselining
- b. Beobachtung (Monitoring)

Bei der Lektüre der Orientierungshilfe ist zu beachten, dass mögliche Maßnahmen den passenden Unterprofilen zugeordnet werden. Dies soll eine Hilfestellung für Anwender des Pilotprofils sein, die auf Basis ähnlicher Anwendungsfallkategorien ein eigenes IT-Grundschutz-Profil für ihre Branche bzw. Zielgruppe erstellen möchten. Es wird explizit keine Aussage darüber getätigt, welche dieser Maßnahmen für ein konkretes IT-Grundschutz-Profil empfehlenswert sind. Auch erhebt die Übersicht keinen Anspruch auf Vollständigkeit; vielmehr soll sie die Zuordnung weiterer Maßnahmen zu den richtigen Unterprofilen erleichtern.

## 11.3.1  Hauptprofil (Organisation)

Das Hauptprofil enthält nur Maßnahmen, die für jede Institution, die das Profil anwendet, gelten - unabhängig von der Ausgestaltung ihres ICS-Netzes. Das sind Maßnahmen, die das Erstellen von Leitlinien, Konzepten, Strategien, Prozessen und Notfallkonzepten zur Aufrechterhaltung der Sicherheit und der Verteilung der Verantwortung umfassen.

## 11.3.2  Unterprofil AR (Architektur)

Für das Unterprofil AR sind alle Maßnahmen relevant, die mit dem grundlegenden Aufbau des ICS-Netzes und der Absicherung seiner Außengrenzen (Perimeter) zu tun hat. Faustregeln für geeignete Maßnahmen:

- Für Netzkomponenten und Sicherheitskomponenten: Spezifische Maßnahmen für einzelne Komponenten, vor allem für die Hardware, Anschaffung und grundlegende Implementierung der Komponenten. Maßnahmen, die Software und Betrieb der Komponenten betreffen, gehören eher ins Unterprofil NM.
- Für ICS-Komponenten: Keine spezifischen Maßnahmen. ICS-Komponenten sind nur insofern relevant, weil der Aufbau einer geeigneten Architektur sich an ihren Anforderungen orientiert (Netzsegmentierung!).

<!-- page: 73 -->

- Maßnahmen der Netzsicherheit ja, Sicherheitsmaßnahmen auf einzelnen Hosts eher nicht.

Konkret ist in der Kategorie der Komplexitätsreduktion die Netzsegmentierung eine mögliche Maßnahme. Für die Konfiguration von Routern und Switches kann die Entwicklung von Standards sinnvoll sein. Der Zugriffsschutz konzentriert sich vor allem auf Netzkomponenten an den Segmentgrenzen. Beispielsweise können dort Switch-Ports gesichert und Firewalls sowie Intrusion Detection / Prevention Systeme (IDS / IPS) eingerichtet werden. Bei WAN-Nutzung können weiterhin die Einrichtung eines DNS-Servers und die Nutzung von VPN-Verschlüsselung sinnvoll sein. Voreingestellte Passwörter auf Routern und Switches sollten geändert werden. Auch physischer Zugangsschutz gehört zu den möglichen Maßnahmen dieses Unterprofils. Hinsichtlich der Systemkenntnis

ist es wichtig, die Standardkonfigurationen von Routern und Switches zu kennen, um unbefugte Änderungen bemerken zu können.

## 11.3.3  Unterprofil NM (Netzmanagement)

Die Maßnahmen des Unterprofils NM betreffen - genau wie die des Unterprofils AR - eher Netzkomponenten als ICS-Komponenten. Im Unterschied zum Unterprofil AR geht es jedoch weniger um eine sichere Architektur und die Sicherung der Zonengrenzen, sondern um einen sicheren Betrieb der Netzkomponenten. Faustregeln für geeignete Maßnahmen:

- Komponentenübergreifend: Maßnahmen für Dokumentation der Netz- und Systemkonfiguration.
- Für Netz- und Sicherheitskomponenten: Spezifische Maßnahmen für Administration, Betrieb, Dokumentation, Notfallvorsorge und Updates.
- Bei der Maßnahmenauswahl steht nicht die Hardware, sondern Software und Prozesse im Fokus.

Komplexitätsreduktion kann erreicht werden, indem ein Netzmanagementsystem eingeführt wird (zum Beispiel auf Basis von SNMP) und die Netzkomponenten gehärtet werden (also alle nicht benötigten Anwendungen, Dienste und Protokolle eliminiert). Beim Zugriffsschutz spielen vor allem softwareseitige Maßnahmen eine Rolle: Die sichere Konfiguration von Routern, Switches und WLAN-Access Points, die Implementierung von Access Control Lists (ACL) auf Routern. Systemkenntnis ist für das Unterprofil NM besonders relevant: Für gutes Netzmanagement ist eine Dokumentation des Netzes sowie aller Geräte hilfreich, auch Baselines für die Konfigurationen sind sinnvoll, um Manipulationen erkennen zu können. Administratoren sollten ent-

sprechend geschult sein.

<!-- page: 74 -->

## 11.3.4  Unterprofil UA (Benutzerzugang)

Das Unterprofil UA umfasst solche Maßnahmen, die den Zugriff auf das ICS und insbesondere den vom ICS geführten Prozess schützen. Faustregeln für geeignete Maßnahmen:

- Das wichtigste zu schützende Zielobjekt dieses Unterprofils ist das HMI, da es direkten, manuellen Prozesszugriff erlaubt.
- Es geht um den Zugang von  Menschen (ggf. mit Geräten), weniger um den Zugriff durch Programme.
- Maßnahmen, die den physischen Zugang zur Anlage regeln, gehören hierher.
- Auch mobile Geräte und Datenträger können auf physischem Wege in die Anlage gelangen. Maßnahmen, um dies zu unterbinden, gehören in dieses Unterprofil.
- Der automatisierte Zugriff mittels SPSen wird im Unterprofil PLC abgedeckt; dafür sind hier keine Maßnahmen erforderlich.
- Maßnahmen, die den Zugriff auf das gesamte ICS-Netz erschweren, werden bereits im Unterprofil AR abgedeckt.

Die Komplexitätsreduktion umfasst ähnliche Maßnahmen wie für SPSen: Es können Maßnahmen ergriffen werden, die der Härtung des HMI-Systems und die ausschließliche Nutzung freigegebener Hard- und Software bewirken. Zudem sind Maßnahmen zur Klärung von Verantwortlichkeiten  (und  Vertretungen)  und  Nutzerrechten  sinnvoll  (RBAC,  Least  Privilege). Auch Regeln zum Gebrauch von Passwörtern sind denkbar.

Der Zugriffsschutz ähnelt ebenfalls dem der SPS-Programmierung, nur dass diesmal das HMI das Zielobjekt ist: Passwortschutz, gesichertes Login, Schutz vor Schadprogrammen, geeignete Regeln für Mobilgeräte, mobile Datenträger und Fremdpersonen gehören zu den klassischen Maßnahmen. Auch beim HMI ist ein Fernzugriff, oft über das Internet, verbreitet, sodass Maßnahmen wie Firewalls, VPN und Schutz vor Inhalten aus dem Internet angebracht seinen können.

Das HMI als Bedienschnittstelle des Prozesses muss fehlerfrei und vorhersehbar funktionieren, weshalb Systemkenntnis wichtig ist: Dazu gehört, Veränderungen am System stets zu dokumentieren und Handbücher bereitzuhalten. Das Personal, dass das HMI bedient, sollte geschult sein. Auch Datensicherung kann eine Maßnahme sein, die in dieses Unterprofil passt.

## 11.3.5  Unterprofil PA (Programmzugriff)

Das Unterprofil PA beschäftigt sich mit den ICS-Komponenten und insbesondere mit deren Software. Faustregeln für sinnvolle Maßnahmen sind

- Für IT-System-Komponenten: Maßnahmen, die die Software aller IT-Systeme betreffen, insbesondere Historian und Webserver.
- Ausgenommen sind Maßnahmen zum Programmieren von SPSen und für den Zugriff auf den Prozess (HMI), für die es eigene Unterprofile gibt (PLC, UA).
- Komponentenübergreifend: Maßnahmen, die den Zugriff auf Software regeln.

<!-- page: 75 -->

73

Zur Komplexitätsreduktion ist auch hier der Einsatz eines Netzmanagementsystems möglich. Es ist zudem sinnvoll, Nutzer in Gruppen einzuteilen, um ihnen nur die nötigen Zugriffsrechte für die Ausführung Rollen zuweisen zu können (RBAC, Principle of Least Privilege). Auch Maßnahmen zur Zugriffskontrolle konzentrieren sich auf Anwendungen. Dazu können Layer-7-Firewalls gehören, aber auch Zugriffskontrollen für einzelne Anwendungen, etwa den Historian. Der Einsatz von Virenschutzprogrammen mitsamt regelmäßiger Patches gehören ebenfalls zu den Maßnahmen des Unterprofils PA. Da die echtzeitkritischen Anwendungen nicht Teil des Unterprofils sind, spricht wenig gegen den Einsatz konventionelle Virenschutzprogramme. Zur Verbesserung der Systemkenntnis

kann das Sammeln und Auswerten von Log-Dateien sinnvoll sein. Eine Datensicherung, vor allem bei Datenbanken wie dem Historian, ist ratsam. Die Nutzerrollen und ihre Rechte können dokumentiert werden.

## 11.3.6  Unterprofil PLC (SPS-Programmierung und -Wartung)

In diesem Unterprofil dreht sich alles um den Zugriff auf die SPSen. Da sie direkt auf den zu leitenden Prozess einwirken, sollte der Zugang zu SPSen besonders geschützt sein. Faustregeln:

- Für ICS-Komponenten: Maßnahmen, die den Zugriff auf und die Integrität von (Daten auf) SPSen und Engineering-Workstations betreffen.
- Komponentenübergreifend: Besonders Maßnahmen für Mobilgeräte wie zum Beispiel Laptops, die auf SPSen zugreifen können und für die Kommunikation von SPSen mit externen Komponenten.

Die Komplexitätsreduktion spielt dabei insofern eine Rolle, als dass SPSen gehärtet werden sollten; dazu kann auch die Einschränkung der Benutzerumgebung gehören. Auch Standards können sinnvoll sein: Der Passwortgebrauch kann Regeln unterliegen um Missbrauch zu vermeiden. Es kann Standards geben, die die Freigabe von Hard- und Software regeln und die Nutzung aller anderen Komponenten untersagen. Zugriffsschutz ist aus oben genanntem Grund für die SPSen fundamental: Von Bildschirmsperren über Passwortschutz bis hin zu lokalen Firewalls und VPN bei Fernzugriff sind viele Maßnahmen denkbar. Die Ausführung von Schadprogrammen sollte unterbunden werden; sei es durch Virenschutzprogramme oder Whitelisting. Ein großes Risiko stellen Mobilgeräte und mobile Datenträger dar, die mit den SPSen verbunden werden; aus diesem Grund können für solche Geräte verschärfte Zugriffsschutzmaßnahmen ergriffen werden. Fremdpersonen sollten keine Möglichkeit bekommen, unbeaufsichtigt auf SPSen zuzugreifen. Die Systemkenntnis spielt vor allem zur Vermeidung von Sicherheitsrisiken durch Bedienfehler eine Rolle. Eine mögliche Maßnahme ist die Schulung von Personal, die mit SPSen arbeiten. Das umfasst auch eine Schärfung des Bewusstseins für Auffälligkeiten, die auf sicherheitsrelevante Vorfälle hinweisen (Security Awareness). Eine Datensicherung ist ratsam.

<!-- page: 76 -->



<!-- page: 77 -->

## IT-Grundschutz-Pilotprofil bzw. IT-Grundschutz-Profil für die Wasserwirtschaft

## - Unterprofil AR (Architektur) -

Erstellt im Rahmen einer Masterarbeit beim

## Bundesamt für Sicherheit in der Informationstechnik

Von: Sarah Fluchs Datum: 18. Juni 2017 Betreuer: Dipl.-Inf. Holger Schildt Bundesamt für Sicherheit in der Informationstechnik 1. Prüferin: Prof. Dr.-Ing. Ulrike Meyer Research Group IT-Security, RWTH Aachen 2. Prüfer: Prof. Dr.-Ing. Ulrich Epple Lehrstuhl für Prozessleittechnik, RWTH Aachen

<!-- page: 78 -->

## Inhaltsverzeichnis

| Vorbemerkungen .................................................................................................          | Vorbemerkungen .................................................................................................                                                                  | Vorbemerkungen .................................................................................................   |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| UP1                                                                                                                       | Formale Aspekte .......................................................................................                                                                           | 6                                                                                                                  |
| UP1.1 Titel ............................................................................................................. | UP1.1 Titel .............................................................................................................                                                         | 6                                                                                                                  |
| UP1.2 Autor und Verantwortliche/r .........................................................................               | UP1.2 Autor und Verantwortliche/r .........................................................................                                                                       | 6                                                                                                                  |
| UP1.3 Versionsstand und Revisionszyklus                                                                                   | UP1.3 Versionsstand und Revisionszyklus                                                                                                                                           | ............................................................ 6                                                     |
| UP1.4 Vertraulichkeit                                                                                                     | UP1.4 Vertraulichkeit                                                                                                                                                             | ............................................................................................. 6                    |
| UP1.5 Status der BSI-Anerkennung                                                                                          | UP1.5 Status der BSI-Anerkennung                                                                                                                                                  | ...................................................................... 6                                           |
| UP2                                                                                                                       | Management Summary .............................................................................                                                                                  | 7                                                                                                                  |
| UP2.1 Zielgruppe ...................................................................................................      | UP2.1 Zielgruppe ...................................................................................................                                                              | 7                                                                                                                  |
| UP2.2 Zielsetzung .................................................................................................       | UP2.2 Zielsetzung .................................................................................................                                                               | 7                                                                                                                  |
| UP2.3 Inhalte .........................................................................................................   | UP2.3 Inhalte .........................................................................................................                                                           | 7                                                                                                                  |
| UP6                                                                                                                       | Spezifische Referenzarchitektur ..............................................................                                                                                    | 9                                                                                                                  |
| UP6.1 Spezifische Zielobjektliste ...........................................................................             | UP6.1 Spezifische Zielobjektliste ...........................................................................                                                                     | 9                                                                                                                  |
| UP6.2 Spezifische Netzpläne ..............................................................................                | UP6.2 Spezifische Netzpläne ..............................................................................                                                                        | 11                                                                                                                 |
| UP6.2.1 Anwendungsfall AR1: Dediziertes ICS-Netz .........................................                                | UP6.2.1 Anwendungsfall AR1: Dediziertes ICS-Netz .........................................                                                                                        | 11                                                                                                                 |
| UP6.2.2                                                                                                                   | Anwendungsfall AR2: Gemeinsames WAN ..........................................                                                                                                    | 12                                                                                                                 |
| UP6.2.3 Anwendungsfall                                                                                                    | AR3: Gemeinsames                                                                                                                                                                  | LAN ........................................... 13                                                                 |
| UP6.3 Schutzbedarf der spezifischen Zielobjekte ................................................                          | UP6.3 Schutzbedarf der spezifischen Zielobjekte ................................................                                                                                  | 14                                                                                                                 |
| UP7                                                                                                                       | Anforderungen und Maßnahmen ...........................................................                                                                                           | 15                                                                                                                 |
| UP7.1 Modellierung .............................................................................................          | UP7.1 Modellierung .............................................................................................                                                                  | 15                                                                                                                 |
| UP7.2                                                                                                                     | Auswahl der Maßnahmen (Anforderungen) am Beispiel des Bausteins B 3.302 ......................................................................................................... | 17                                                                                                                 |
| UP7.3 Umsetzungsvorgaben ...............................................................................                  | UP7.3 Umsetzungsvorgaben ...............................................................................                                                                          | 20                                                                                                                 |
| UP9                                                                                                                       | Anhang A .................................................................................................                                                                        | 24                                                                                                                 |
| UP9.1 Glossar .....................................................................................................       | UP9.1 Glossar .....................................................................................................                                                               | 24                                                                                                                 |
| UP10 Anhang                                                                                                               | B (Pilotprofil)                                                                                                                                                                   | ............................................................................. 25                                   |
| UP10.1 Maßnahmenauswahltabellen ................................................................                          | UP10.1 Maßnahmenauswahltabellen ................................................................                                                                                  | 25                                                                                                                 |
| UP10.1.1 Baustein B 3.302 .................................................................................               | UP10.1.1 Baustein B 3.302 .................................................................................                                                                       |                                                                                                                    |
|                                                                                                                           |                                                                                                                                                                                   | 25                                                                                                                 |
| UP10.2                                                                                                                    | Gefährdungstabellen                                                                                                                                                               | ............................................................................ 27                                    |
| UP10.2.1                                                                                                                  | Baustein B 3.302 .................................................................................                                                                                | 27                                                                                                                 |

<!-- page: 79 -->

## Abbildungsverzeichnis

| Abb. 2.1:                                                                           | Vorgehensschritte bei der Anwendung des Profils .................................. 8       |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Abb. 6.1: Netzplan des Anwendungsfalls AR1: Dediziertes ICS-Netz .................. | 11                                                                                         |
| Abb. 6.2: Netzplan des Anwendungsfalls AR2: Gemeinsames WAN ...................     | 12                                                                                         |
| Abb. 6.3: Netzplan des Anwendungsfalls AR3: Gemeinsames LAN .....................   | 13                                                                                         |
| Abb. 7.1: Legende zu den Netzplänen: Zonen, Sicherheitskomponenten                  | Netzkomponenten und ................................................................... 21 |
| Abb. 7.2: Segmentierter Netzplan für den                                            | Anwendungsfall AR1 .......................... 23                                           |
| Abb. 7.3: Segmentierter Netzplan für die                                            | Anwendungsfälle AR2 und AR3 ........... 23                                                 |

<!-- page: 80 -->

## Tabellenverzeichnis

| Tab. 6.1: Spezifische Zielobjektliste der Anwendungsfallgruppe AR ....................   | 10                                                                                                                               |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Tab. 6.2: Schutzbedarfstabelle für die Zielobjekte der Anwendungsfallgruppe AR           | 14                                                                                                                               |
| Tab. 7.1: Modellierungstabelle für die Zielobjekte der Anwendungsfallgruppe AR           | 16                                                                                                                               |
| Tab. 7.2: Maßnahmenauswahl für den Baustein                                              | B 3.302: Router und Switches .. 18                                                                                               |
| Tab. 7.3: Begründung der Nichtauswahl von                                                | Maßnahmen für den Baustein B 3.302                                                                                               |
|                                                                                          | .......................................................................................................... 19                    |
| Tab. 10.1: Maßnahmenauswahltabelle für Switches                                          | den Baustein B 3.302: Router und ............................................................................................ 25 |

<!-- page: 81 -->

## Vorbemerkungen

Das vorliegende Unterprofil ist als Teil der Version 1.0 des 'IT-Grundschutz-Pilotprofils bzw. IT-Grundschutz-Profils für die Wasserwirtschaft' im Rahmen einer Masterarbeit entstanden. Vor der Lektüre wird dringend das Lesen des zugehörigen Hauptprofils empfohlen, das ebenfalls beim BSI frei erhältlich ist.

<!-- page: 82 -->

## UP1 Formale Aspekte

## UP1.1 Titel

Pilotprofil - Unterprofil Architektur ( AR )

bzw.

Leittechnische Netze in der Wasserversorgung und Abwasserbeseitigung ( Wasserwirtschaft )

- Unterprofil Architektur ( AR )

## UP1.2 Autor und Verantwortliche/r

Sarah Fluchs, RWTH Aachen

Holger Schildt, BSI

## UP1.3 Versionsstand und Revisionszyklus

Version 1.0 vom 18.06.2017

## UP1.4 Vertraulichkeit

Pilotprofil : Öffentlich, mit verkürztem Anhang B (Pilotprofil) und zusätzlichem Anhang C

Wasserwirtschaft : Nicht öffentlich, mit vollständigem Anhang B (Wasserwirtschaft)

## UP1.5 Status der BSI-Anerkennung

Anerkennung wird noch geprüft.

<!-- page: 83 -->

## UP2 Management Summary

## UP2.1 Zielgruppe

Siehe Hauptprofil.

## UP2.2 Zielsetzung

Das Profil ist in ein Hauptprofil und mehrere Unterprofile gegliedert. Die Unterprofile dienen der individuellen Anpassung des Profils an die leittechnische Infrastruktur des Profilanwenders und enthalten jeweils Maßnahmenempfehlungen für einen Teilbereich des industriellen Netzes (ICS-Netz). Das vorliegende Unterprofil AR befasst sich mit der grundlegenden Architektur des ICS-Netzes, insbesondere mit seinen Verbindungen zum Office-Netz. Die Anpassung erfolgt durch Auswahl zutreffender Anwendungsfälle. Dieses Unterprofil enthält Maßnahmenempfehlungen für die Anwendungsfälle

- AR1: Dediziertes ICS-Netz,
- AR2: Gemeinsames WAN,
- AR3: Gemeinsames LAN.

## UP2.3 Inhalte

Abb. 2.1 gibt eine Übersicht über die Anwendung des Profils. Blau umrandete Schritte erfolgen mit Hilfe des Hauptprofils, grün umrandete sind in den Unterprofilen enthalten. Das vorliegende Unterprofil empfiehlt Maßnahmen, die die Architektur des ICS-Netzes betreffen. Dazu werden zuerst die zur Auswahl stehenden Anwendungsfälle beschrieben (Schritt 4) und dann passende Informationssicherheitsempfehlungen gegeben (5). Für einzelne Maßnahmen werden Umsetzungsvorgaben gemacht (7).

Für  eine  genauere  Beschreibung  der  Vorgehensweise  zur  Profilanwendung  wird  auf  das Hauptprofil verwiesen.

<!-- page: 84 -->

Abb. 2.1: Vorgehensschritte bei der Anwendung des Profils

<!-- image -->

<!-- page: 85 -->

## UP6 Spezifische Referenzarchitektur

<!-- image -->

Die spezifische Referenzarchitektur beinhaltet

- die spezifische Zielobjektliste mit allen Objekten der generischen Zielobjektliste, die für die Anwendungsfallgruppe des Unterprofils relevant sind sowie
- Netzpläne, die die einzelnen Anwendungsfälle veranschaulichen.

Für eine genauere Beschreibung der spezifischen Zielobjekte sowie allgemeine Informationen und eine Legende zu den Netzplänen wird auf das Hauptprofil verwiesen.

## UP6.1 Spezifische Zielobjektliste

Die Anwendungsfallgruppe AR beschäftigt sich mit der Netzstruktur der ICS- und der Office-IT-Komponenten. Da es in dieser Anwendungsfallgruppe um die Netzarchitektur geht, stehen die Netzkomponenten mitsamt zugehöriger Sicherheitskomponenten im Vordergrund.

ICS-Komponenten werden in der spezifischen Zielobjektliste in Tab. 6.1 mit aufgeführt; sie sind aber für die spätere Anforderungsauswahl nur unter dem Aspekt ihrer Platzierung im Netz relevant. Externe Komponenten sind bezüglich ihrer Stellung in der Architektur wie Office-IT-Komponenten zu behandeln und deswegen nicht explizit erwähnt. Mobilgeräte sind in der Architektur nicht fest verankert; ihre Einbindung hängt von der Art ihrer Verwendung ab - deswegen werden auch sie in der Anwendungsfallgruppe AR nicht betrachtet.

<!-- page: 86 -->

Tab. 6.1: Spezifische Zielobjektliste der Anwendungsfallgruppe AR

| Nr.             | Zielobjekt              |
|-----------------|-------------------------|
| IT-Systeme      | IT-Systeme              |
| IT1             | Feldgerät               |
| IT2             | SPS                     |
| IT3             | HMI                     |
| IT4             | Historian               |
| IT5             | Engineering-Workstation |
| IT6             | Control Server          |
| IT7             | Webserver               |
| IT10            | Office-IT-Komponente    |
| Netzkomponenten | Netzkomponenten         |
| N1              | Switch                  |
| N2              | Router                  |
| N3              | Modem                   |
| N4              | IT-Verkabelung          |
| N5              | Feldbus                 |
| N6              | Fernwartung             |
| Sicherheit      | Sicherheit              |
| S1              | Firewall                |
| S2              | VPN                     |
| S3              | IDS / IPS               |

<!-- page: 87 -->

## UP6.2 Spezifische Netzpläne

## UP6.2.1 Anwendungsfall AR1: Dediziertes ICS-Netz

Der Anwendungsfall AR1: Dediziertes ICS-Netz (siehe Abb. 6.1) beschreibt eine Architektur, in  der  Office-IT  und  ICS-Komponenten  vollständig getrennt sind.  In  diesem  Fall  haben  die Office-Komponenten keinerlei Auswirkungen auf das ICS-Netz und sind deswegen nicht Teil der Referenzarchitektur. Dies gilt sowohl für die verteilte ICS-Netzstruktur (linke Hälfte der Abb. 6.1) mit einem zentralen Leitstand (bestehend aus HMI und ggf. Engineering-WS), der über ein WAN mit dem Feld verbunden ist, als auch für die konzentrierte ICS-Netzstruktur (rechte Hälfte der Abb. 6.1) mit lokalem Leitstand im selben LAN wie die Feldgeräte.

Abb. 6.1: Netzplan des Anwendungsfalls AR1: Dediziertes ICS-Netz

<!-- image -->

<!-- page: 88 -->

## UP6.2.2 Anwendungsfall AR2: Gemeinsames WAN

Der Anwendungsfall AR2: Gemeinsames WAN (Abb. 6.2) zeigt eine Architektur, bei der das WAN, das die Kommunikation zwischen dem zentralen Leitstand und den verteilten SPSen sowohl zwischen dem zentralen und den lokalen Leitständen ermöglicht, von Office-IT-Komponenten und ICS-Komponenten gemeinsam genutzt wird. Wie beim Fall AR1 gilt dies für Office-IT-Komponenten sowohl auf Ebene des zentralen als auch der lokalen Leitstände. Die LANs sind jedoch weiterhin getrennt: Separate Switches bilden das ICS- und das Office-LAN.

Abb. 6.2: Netzplan des Anwendungsfalls AR2: Gemeinsames WAN

<!-- image -->

<!-- page: 89 -->

## UP6.2.3 Anwendungsfall AR3: Gemeinsames LAN

Der dritte Anwendungsfall, AR3: Gemeinsames LAN (Abb. 6.3), stellt noch eine Steigerung der gemeinsamen Netznutzung dar. Nun wird nicht nur das WAN, sondern auch die lokalen Netze auf zentraler und lokaler Ebene gemeinsam von ICS- und Office-IT-Komponenten genutzt. Das bedeutet, dass die Komponenten an ein- und demselben Switch und somit in derselben Kollisionsdomäne hängen.

Abb. 6.3: Netzplan des Anwendungsfalls AR3: Gemeinsames LAN

<!-- image -->

<!-- page: 90 -->

## UP6.3 Schutzbedarf der spezifischen Zielobjekte

Tab. 6.2 zeigt die Schutzbedarfszuweisung der spezifischen Zielobjekte für alle drei Anwendungsfälle. Dabei steht ein weißes Feld für normalen, ein schwarzes für hohen Schutzbedarf. Weitere Informationen zu Schutzbedarfskategorien und Kriterien für die Kategorieneinteilung finden sich im Hauptprofil.

Tab. 6.2: Schutzbedarfstabelle für die Zielobjekte der Anwendungsfallgruppe AR

| Legende für den Schutzbedarf:   | Legende für den Schutzbedarf:   | normal   | normal   | hoch   |
|---------------------------------|---------------------------------|----------|----------|--------|
| Anwendungsfall:                 | Anwendungsfall:                 | AR1      | AR2      | AR3    |
| Nr.                             | Zielobjekt                      |          |          |        |
| IT-Systeme                      | IT-Systeme                      |          |          |        |
| IT1                             | Feldgerät                       |          |          |        |
| IT2                             | SPS                             |          |          |        |
| IT3                             | HMI                             |          |          |        |
| IT4                             | Historian                       |          |          |        |
| IT5                             | Engineering-Workstation         |          |          |        |
| IT6                             | Control Server                  |          |          |        |
| IT7                             | Webserver                       |          |          |        |
| IT10                            | Office-IT-Komponente            |          |          |        |
| Netzkomponenten                 | Netzkomponenten                 |          |          |        |
| N1                              | Switch                          |          |          |        |
| N2                              | Router                          |          |          |        |
| N3                              | Modem                           |          |          |        |
| N4                              | IT-Verkabelung                  |          |          |        |
| N5                              | Feldbus                         |          |          |        |
| N6                              | Fernwartung                     |          |          |        |
| Sicherheit                      | Sicherheit                      |          |          |        |
| S1                              | Firewall                        |          |          |        |
| S2                              | VPN                             |          |          |        |
| S3                              | IDS / IPS                       |          |          |        |

Die Komponenten, die den Zugang zum ICS-Netz erlauben, namentlich Router und Switches, haben unabhängig vom Anwendungsfall einen hohen Schutzbedarf. Sie sind elementar sowohl für die Aufrechterhaltung der Kommunikation zwischen einzelnen ICS-Komponenten als auch für den Zugang zum ICS-Netz und damit für den Schutz von ICS-Komponenten.

Beim Anwendungsfall AR2: Gemeinsames WAN ist eine Anbindung nach außen vorhanden. In diesem Fall erhöht sich der Schutzbedarf für die kritischsten ICS-Komponenten. Als kritischste Komponenten werden die echtzeitrelevanten Komponenten und solche, die direkten Zugriff auf den Prozess ermöglichen, gewertet. Dies umfasst die Zielobjekte Feldgerät, SPS, HMI, Engineering-Workstation und Control Server sowie den Feldbus. Router und Switches unterliegen ohnehin hohem Schutzbedarf.

<!-- page: 91 -->

## UP7 Anforderungen und Maßnahmen

<!-- image -->

## UP7.1 Modellierung

Die Modellierung der für die Anwendungsfallgruppe AR relevanten spezifischen Zielobjekte mit Bausteinen ist in Tab. 7.1 veranschaulicht. In den Zeilen finden sich die zu modellierenden Zielobjekte, in den Spalten die ausgewählten Bausteine. Wird ein Baustein für die Modellierung eines Zielobjekts verwendet, wird das entsprechende Feld eingefärbt. Ein Zielobjekt kann dabei durchaus durch mehrere Bausteine abgebildet werden.

Für die Anwendungsfallgruppe sind Maßnahmen für die Netzkomponenten und die Sicherheitskomponenten vorrangig. Diese Komponenten wurden deswegen mit den für sie spezifischen Bausteinen B 3.302: Router und Switches , B 3.301: Firewall , B 4.4: VPN und B 5.18: DNS-Server modelliert, um spezifische Maßnahmen auswählen zu können.

Die IT-System-Komponenten, darunter insbesondere alle ICS-Komponenten, sind im Unterprofil AR nur insofern relevant, dass der Aufbau einer geeigneten Architektur sich an ihren Anforderungen orientiert. Sie werden deshalb von den komponentenübergreifenden Bausteinen B 4.1: Lokale Netze und B 1.9: Hard- und Softwaremanagement modelliert (so wie die Netz- und Sicherheitskomponenten auch), jedoch nicht mit spezifischen Bausteinen. Dies erfolgt in anderen Unterprofilen, in denen spezifische Maßnahmen für die IT-Systeme empfohlen werden.

<!-- page: 92 -->

Tab. 7.1: Modellierungstabelle für die Zielobjekte der Anwendungsfallgruppe AR

| Nr.             | Zielobjekt           | Modellierung mit Bausteinen   | Modellierung mit Bausteinen      | Modellierung mit Bausteinen   | Modellierung mit Bausteinen   | Modellierung mit Bausteinen   | Modellierung mit Bausteinen   |
|-----------------|----------------------|-------------------------------|----------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
| Nr.             | Zielobjekt           | B 4.1 Lokale Netze            | B 1.9 Hard-/Software- management | B 3.302 Router und Switches   | B 3.301 Firewall              | B 4.4 VPN                     | B 5.18 DNS- Server            |
| IT-Systeme      | IT-Systeme           |                               |                                  |                               |                               |                               |                               |
| IT1             | Feldgerät            |                               |                                  |                               |                               |                               |                               |
| IT2             | SPS                  |                               |                                  |                               |                               |                               |                               |
| IT3             | HMI                  |                               |                                  |                               |                               |                               |                               |
| IT4             | Historian            |                               |                                  |                               |                               |                               |                               |
| IT5             | Engineering-WS       |                               |                                  |                               |                               |                               |                               |
| IT6             | Control Server       |                               |                                  |                               |                               |                               |                               |
| IT7             | Webserver            |                               |                                  |                               |                               |                               |                               |
| IT8             | Mobilgerät           |                               |                                  |                               |                               |                               |                               |
| IT9             | Externe Komponente   |                               |                                  |                               |                               |                               |                               |
| IT10            | Office-IT-Komponente |                               |                                  |                               |                               |                               |                               |
| Netzkomponenten | Netzkomponenten      |                               |                                  |                               |                               |                               |                               |
| N1              | Switch               |                               |                                  |                               |                               |                               |                               |
| N2              | Router               |                               |                                  |                               |                               |                               |                               |
| N3              | Modem                |                               |                                  |                               |                               |                               |                               |
| N4              | IT-Verkabelung       |                               |                                  |                               |                               |                               |                               |
| N5              | Feldbus              |                               |                                  |                               |                               |                               |                               |
| N6              | Fernwartung          |                               |                                  |                               |                               |                               |                               |
| Sicherheit      | Sicherheit           |                               |                                  |                               |                               |                               |                               |
| S1              | Firewall             |                               |                                  |                               |                               |                               |                               |
| S2              | VPN                  |                               |                                  |                               |                               |                               |                               |
| S3              | IDS / IPS            |                               |                                  |                               |                               |                               |                               |

<!-- page: 93 -->

## UP7.2 Auswahl der Maßnahmen (Anforderungen) am Beispiel des Bausteins B 3.302

Tab. 7.2 zeigt die Maßnahmenauswahl für den Baustein B 3.302: Router und Switches. Weitere Informationen zur Maßnahmenauswahl finden sich im Hautprofil. Die Maßnahmenauswahltabellen für die anderen in diesem Unterprofil zur Modellierung verwendeten Bausteine sind im kostenpflichtigen Anhang B (Wasserwirtschaft).

In den Tabellenzeilen sind alle Maßnahmen des Bausteins aufgelistet. Es wird die Nummer der Maßnahme, ihr Titel sowie ihre Qualifizierungsstufe angegeben. Mögliche Qualifizierungsstufen sind A (Einstieg), B (Aufbau), C (Zertifikat), Z (zusätzlich) und W (Wissen). Nur die Stufen A bis C sind für eine Qualifizierung nach IT-Grundschutz bzw. ISO 27001 notwendig.

In den Tabellenspalten sind die Anwendungsfälle aufgeführt, für die mindestens eine Maßnahme des Bausteins ausgewählt wurde. Ein grün eingefärbtes Feld kennzeichnet die Auswahl der Maßnahme für den Anwendungsfall. Ist das Feld zusätzlich mit einem 'K' gekennzeichnet, wird die Maßnahme nur dann ausgewählt, wenn das mit dem Baustein modellierte Zielobjekt einen hohen Schutzbedarf hat, also die dazugehörige Anlage als kritische Infrastruktur (KRITIS) eingestuft ist.

<!-- page: 94 -->

Tab. 7.2: Maßnahmenauswahl für den Baustein B 3.302: Router und Switches

| Maßnahmen des Bausteins   | Maßnahmen des Bausteins                                                                                 | Maßnahmen des Bausteins                                                                                 | Anwendungsfälle:   | Anwendungsfälle:   | Anwendungsfälle:   | Anwendungsfälle:   | Anwendungsfälle:   |
|---------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| K                         | Router und Switches: = In einem Unterprofil ausgewählt = Nur für KRITIS / hohen Schutzbedarf ausgewählt | Router und Switches: = In einem Unterprofil ausgewählt = Nur für KRITIS / hohen Schutzbedarf ausgewählt | AR 1               | AR 2,3             | NM 1               | NM 2               | NM 3               |
| M 1.43                    | A                                                                                                       | Gesicherte Aufstellung aktiver Netzkomponenten                                                          |                    |                    |                    |                    |                    |
| M 2.276                   | Z                                                                                                       | Funktionsweise eines Routers                                                                            |                    |                    |                    |                    |                    |
| M 2.277                   | Z                                                                                                       | Funktionsweise eines Switches                                                                           |                    |                    |                    |                    |                    |
| M 2.278                   | Z                                                                                                       | Typ. Einsatzszenarien v. Routern/Switches                                                               |                    |                    |                    |                    |                    |
| M 2.279                   | A                                                                                                       | Erstellung einer Sicherheitsrichtlinie für Router und Switches                                          |                    |                    |                    |                    |                    |
| M 2.280                   | C                                                                                                       | Kriterien für die Beschaffung und geeignete Auswahl von Routern und Switches                            | K                  | K                  |                    |                    |                    |
| M 2.281                   | A                                                                                                       | Dokumentation der Systemkonfiguration von Routern und Switches                                          |                    |                    |                    |                    |                    |
| M 2.282                   | A                                                                                                       | Regelmäßige Kontrolle von Routern und Switches                                                          |                    |                    |                    |                    |                    |
| M 2.283                   | B                                                                                                       | Software-Pflege auf Routern und Switches                                                                |                    |                    | K                  | K                  | K                  |
| M 2.284                   | C                                                                                                       | Sichere Außerbetriebnahme von Routern und Switches                                                      |                    |                    | K                  | K                  | K                  |
| M 3.38                    | B                                                                                                       | Administratorenschulung für Router und Switches                                                         |                    |                    | K                  | K                  | K                  |
| M 4.201                   | A                                                                                                       | Sichere lokale Grundkonfiguration von Routern und Switches                                              |                    |                    |                    |                    |                    |
| M 4.202                   | A                                                                                                       | Sichere Netz-Grundkonfiguration von Routern und Swit- ches                                              |                    |                    |                    |                    |                    |
| M 4.203                   | A                                                                                                       | Konfigurations-Checkliste für Router und Switches                                                       |                    |                    |                    |                    |                    |
| M 4.204                   | C                                                                                                       | Sichere Administration von Routern und Switches                                                         |                    |                    | K                  | K                  | K                  |
| M 4.205                   | C                                                                                                       | Protokollierung bei Routern und Switches                                                                |                    |                    | K                  | K                  | K                  |
| M 4.206                   | C                                                                                                       | Sicherung von Switch-Ports                                                                              | K                  | K                  |                    |                    |                    |
| M 5.111                   | C                                                                                                       | Einrichtung von Access Control Lists auf Routern                                                        |                    |                    | K                  | K                  | K                  |
| M 5.112                   | C                                                                                                       | Sicherheitsaspekte von Routing-Protokollen                                                              |                    |                    |                    |                    |                    |
| M 6.91                    | C                                                                                                       | Datensicherung und Recovery bei Routern und Swit- ches                                                  | K                  | K                  |                    |                    |                    |
| M 6.92                    | C                                                                                                       | Notfallvorsorge bei Routern und Switches                                                                |                    |                    | K                  | K                  | K                  |

<!-- page: 95 -->

Es gibt vier mögliche Gründe für die Nichtauswahl von Maßnahmen durch den B3S, auf die im Folgenden durch Nennung der vorangestellten Kennziffer Bezug genommen wird:

1. Für  Zielgruppe  nicht relevant. Die  Maßnahme ist für  die  Zielgruppe  (Wasserwirtschaft) i.A. nicht relevant.
2.  Redundant zu anderen Regelwerken. Die  Maßnahme wurde bereits im Merkblatt zum B3S beschrieben bzw. wird durch andere Regelwerke von DWA / DVGW abgedeckt.
3. Qualifizierungsstufe Z. Die Maßnahme hat die Qualifizierungsstufe Z und ist somit für die Qualifizierung nach IT-Grundschutz oder ISO 27001 nicht notwendig; sie stellen Ergänzungen dar [BSI16]. Diese Maßnahmen wurden i.A. nicht ausgewählt.
4.  Durch übergeordnete Maßnahme abgedeckt. Die Maßnahme ist ein Spezialfall einer übergeordneten Maßnahme, die ausgewählt wurde.

In Tab. 7.3 sind die Begründungen für alle nicht ausgewählten Maßnahmen des Bausteins B 3.302 im Einzelnen aufgeführt.

Tab. 7.3: Begründung der Nichtauswahl von Maßnahmen für den Baustein B 3.302

| Nicht ausgewählte Maßnahme                                               | Begründung (Kennziffer)                                                                                                             |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| M 2.276 : Funktionsweise eines Routers                                   | Qualifizierungsstufe Z (3)                                                                                                          |
| M 2.277 : Funktionsweise eines Switches                                  | Qualifizierungsstufe Z (3)                                                                                                          |
| M 2.278 : Typische Einsatzszenarien von Rou- tern und Switches           | Qualifizierungsstufe Z (3)                                                                                                          |
| M 2.279 : Erstellung einer Sicherheitsrichtlinie für Router und Switches | Durch übergeordnete Maßnahme abgedeckt (4) : M 2.192: Erstellung einer Leitlinie zur Informations- sicherheit (Baustein B 1.0)      |
| M 4.201 : Sichere lokale Grundkonfiguration von Routern und Switches     | Durch übergeordnete Maßnahme abgedeckt (4) : M 4.202: Sichere Netz-Grundkonfiguration von Rou- tern und Switches (Baustein B 3.302) |
| M 5.112 : Sicherheitsaspekte von Routing-Pro- tokollen                   | Durch übergeordnete Maßnahme abgedeckt (4) : M 5.39: Sicherer Einsatz der Protokolle und Dienste (Baustein B 3.301)                 |

<!-- page: 96 -->

## UP7.3 Umsetzungsvorgaben

<!-- image -->

|   1 | Auswahl der betrachteten Geschäftsprozesse und Anlagen                         |
|-----|--------------------------------------------------------------------------------|
|   2 | Schutzbedarfszuweisung für die Anlagen                                         |
|   3 | Auswahl der ICS-Netzstruktur                                                   |
|   4 | Auswahl der zutreffenden Anwendungsfälle und Erfassung der Referenzarchitektur |
|   5 | Erfassung der Informationssicherheitsempfehlungen für die Anwendungsfälle      |
|   6 | Integration und Realitätsabgleich aller Referenzarchitekturen und Empfehlungen |
|   7 | Umsetzung von Maßnahmen                                                        |

Für alle Maßnahmen außer den explizit erwähnten liegt die Umsetzung im Ermessen des Profilanwenders. Für einige Bausteine bietet zudem der IT-Grundschutz Umsetzungshinweise, die zu Rate gezogen werden können.

## UP7.3.1 Maßnahmen M 2.204, M 5.61, M 5.77

Die Maßnahmen M 2.204: Verhinderung ungesicherter Netzzugänge , M 5.61: Geeignete physische Segmentierung und M 5.77: Bildung von Teilnetzen betreffen die Aufteilung der Architektur in Zonen und die Sicherung der Zonenübergänge. Diese Umsetzungsvorgabe enthält einen Vorschlag für die Netzsegmentierung und die Absicherung der Perimeter für die Referenzarchitektur der Anwendungsfallgruppe AR.

Zur Veranschaulichung werden segmentierte Netzpläne gegeben. Die Netzpläne können als Basis für die Architektur des Gesamt-Netzplans (siehe Hauptprofil) dienen.

Abb. 7.1 enthält eine Legende zu den segmentierten Netzplänen. In Abb. 7.2 und Abb. 7.3 sind die segmentierten Netzpläne für die Anwendungsfälle AR1 sowie AR2 und AR3 zu sehen.

<!-- page: 97 -->

Abb. 7.1: Legende zu den Netzplänen: Zonen, Netzkomponenten und Sicherheitskomponenten

<!-- image -->

Die für die Segmentierung vorgeschlagenen Zonen orientieren sich an der Purdue Enterprise Reference Architecture (PERA) und dem Buch 'Industrial Network Security' von Eric D. Knapp und Joel Thomas Langill [Wil94; KL15]. Für jede Zone ist in den segmentierten Netzplänen ein eigenes Subnetz (mit eigenem Switch) eingeführt worden. Die Subnetze eines LANs werden von einem zentralen Router bedient.

Zur Absicherung der Zonengrenzen ist jede Zone mit einer Maßnahme zur Zugangskontrolle (Access Control, AC) gesichert, mindestens einer Firewall. WAN-Kommunikation erfolgt ausschließlich über eine verschlüsselte VPN-Verbindung. Die Umsetzung der Zugangskontrollen und der VPN-Verbindung werden jedoch in eigenen Maßnahmen behandelt und sind nicht Teil dieser Umsetzungsvorgabe.

Die rot eingefärbte maximal kritische Zone umfasst alle ICS-Komponenten, die direkt mit dem zu führenden Prozess interagieren (Feldgeräte, SPS) oder direkten Zugriff auf die Prozessführung haben (HMI). Diese Zone ist echtzeitkritisch. Der Control Server und die Engineering Workstations können auch noch zur Zone mit der höchsten Kritikalität gezählt werden, da auch sie schreibenden Zugriff auf SPSen besitzen können. Da sie jedoch weniger echtzeitkritisch sind, ist es auch möglich, die kritische Zone weiter zu unterteilen und Control Server und Engineering-WS einer semi-kritischen Zone (orange) zuzuordnen. Zudem ist noch anzumerken, dass die kritische Zone auch horizontal weiter unterteilt werden sollte, wenn es voneinander unabhängige Steuereinheiten gibt. Dies ist mit einer eigenen Zone für eine weitere verteilte SPS mit ihren Feldgeräten in den segmentierten Netzplänen angedeutet.

Office-IT-Komponenten sind im ICS-Umfeld nicht echtzeitkritisch. Vom Blickwinkel der ICS-Security aus sind sie externe Komponenten, die für einen Schutz der ICS-Komponenten nicht besonders geschützt  werden müssen.  Deswegen  werden  sie  als minimal  kritische Zone (grün) eingestuft.

<!-- page: 98 -->

ICS-Komponenten wie Historian und Web Server haben nur lesenden Zugriff auf prozessnahe Komponenten, weshalb sie weniger kritisch sind als die anderen Komponenten. Sie werden in die gelb markierte demilitarisierte Zone (DMZ) eingeordnet. Eine DMZ ist eine gute Lösung, um kontrollierten Zugriff auf ICS-Komponenten aus dem Office-Netz zu ermöglichen.

<!-- page: 99 -->

Abb. 7.2: Segmentierter Netzplan für den Anwendungsfall AR1

<!-- image -->

Abb. 7.3: Segmentierter Netzplan für die Anwendungsfälle AR2 und AR3

<!-- image -->

<!-- page: 100 -->

## UP9 Anhang A

## UP9.1 Glossar

Siehe Hauptprofil.

## UP9.2 Literaturverzeichnis

- [BSI16] Bundesamt für Sicherheit in der Informationstechnik (BSI): IT-Grundschutz-Kataloge: Standardwerk zur IT-Sicherheit : 15. Ergänzungslieferung 2016. Bonn : Bundesanzeiger Verlag, 2016
- [KL15] KNAPP, Eric D. ; LANGILL, Joel Thomas: Industrial network security : Securing critical infrastructure networks for smart grid, SCADA, and other industrial control systems. 2. ed. Amsterdam : Syngress Elsevier, 2015
- [Wil94] WILLIAMS, Theodore J.: The Purdue enterprise reference architecture. In: Computers in Industry 24 (1994), 2-3, S. 141-158

<!-- page: 101 -->

## UP10 Anhang B (Pilotprofil)

## UP10.1  Maßnahmenauswahltabellen

## UP10.1.1 Baustein B 3.302

Tab. 10.1: Maßnahmenauswahltabelle für den Baustein B 3.302: Router und Switches

| Maßnahmen des Bausteins   | Maßnahmen des Bausteins                                                                                 | Maßnahmen des Bausteins                                                                                 | Anwendungsfälle:   | Anwendungsfälle:   | Anwendungsfälle:   | Anwendungsfälle:   | Anwendungsfälle:   |
|---------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| K                         | Router und Switches: = In einem Unterprofil ausgewählt = Nur für KRITIS / hohen Schutzbedarf ausgewählt | Router und Switches: = In einem Unterprofil ausgewählt = Nur für KRITIS / hohen Schutzbedarf ausgewählt | AR 1               | AR 2,3             | NM 1               | NM 2               | NM 3               |
| M 1.43                    | A                                                                                                       | Gesicherte Aufstellung aktiver Netzkomponenten                                                          |                    |                    |                    |                    |                    |
| M 2.276                   | Z                                                                                                       | Funktionsweise eines Routers                                                                            |                    |                    |                    |                    |                    |
| M 2.277                   | Z                                                                                                       | Funktionsweise eines Switches                                                                           |                    |                    |                    |                    |                    |
| M 2.278                   | Z                                                                                                       | Typ. Einsatzszenarien v. Routern/Switches                                                               |                    |                    |                    |                    |                    |
| M 2.279                   | A                                                                                                       | Erstellung einer Sicherheitsrichtlinie für Router und Switches                                          |                    |                    |                    |                    |                    |
| M 2.280                   | C                                                                                                       | Kriterien für die Beschaffung und geeignete Auswahl von Routern und Switches                            | K                  | K                  |                    |                    |                    |
| M 2.281                   | A                                                                                                       | Dokumentation der Systemkonfiguration von Routern und Switches                                          |                    |                    |                    |                    |                    |
| M 2.282                   | A                                                                                                       | Regelmäßige Kontrolle von Routern und Switches                                                          |                    |                    |                    |                    |                    |
| M 2.283                   | B                                                                                                       | Software-Pflege auf Routern und Switches                                                                |                    |                    | K                  | K                  | K                  |
| M 2.284                   | C                                                                                                       | Sichere Außerbetriebnahme von Routern und Switches                                                      |                    |                    | K                  | K                  | K                  |
| M 3.38                    | B                                                                                                       | Administratorenschulung für Router und Switches                                                         |                    |                    | K                  | K                  | K                  |
| M 4.201                   | A                                                                                                       | Sichere lokale Grundkonfiguration von Routern und Switches                                              |                    |                    |                    |                    |                    |
| M 4.202                   | A                                                                                                       | Sichere Netz-Grundkonfiguration von Routern und Swit- ches                                              |                    |                    |                    |                    |                    |
| M 4.203                   | A                                                                                                       | Konfigurations-Checkliste für Router und Switches                                                       |                    |                    |                    |                    |                    |
| M 4.204                   | C                                                                                                       | Sichere Administration von Routern und Switches                                                         |                    |                    | K                  | K                  | K                  |
| M 4.205                   | C                                                                                                       | Protokollierung bei Routern und Switches                                                                |                    |                    | K                  | K                  | K                  |
| M 4.206                   | C                                                                                                       | Sicherung von Switch-Ports                                                                              | K                  | K                  |                    |                    |                    |

<!-- page: 102 -->

| M 5.111   | C   | Einrichtung von Access Control Lists auf Routern       |    | K   | K   | K   |
|-----------|-----|--------------------------------------------------------|----|-----|-----|-----|
| M 5.112   | C   | Sicherheitsaspekte von Routing-Protokollen             |    |     |     |     |
| M 6.91    | C   | Datensicherung und Recovery bei Routern und Swit- ches | K  |     |     |     |
| M 6.92    | C   | Notfallvorsorge bei Routern und Switches               |    | K   | K   | K   |

<!-- page: 103 -->

## UP10.2  Gefährdungstabellen

## UP10.2.1 Baustein B 3.302

Tab. 10.2: Gefährdungstabelle für den Baustein B 3.302: Router und Switches

| Gefährdungen des Bausteins    | Gefährdungen des Bausteins                                                   | Anwendungsfälle:   | Anwendungsfälle:   | Anwendungsfälle:   | Anwendungsfälle:   | Anwendungsfälle:   |
|-------------------------------|------------------------------------------------------------------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| B 3.302: Router und Switches: | = Gegenmaßnahme nur für KRITIS / hohen Schutzbed.                            |                    | AR 2,3             | NM 1               | NM 2               | NM 3               |
| K                             | = Gefährdung in einem Unterprofil                                            | AR 1               |                    |                    |                    |                    |
| G 2.3                         | Fehlende, ungeeignete, inkompatible Betriebsmittel                           | K                  | K                  |                    |                    |                    |
| M 2.280                       | Kriterien für die Beschaffung und geeignete Auswahl von Routern und Switches | K                  | K                  |                    |                    |                    |
| G 2.4                         | Unzureichende Kontrolle der Sicherheitsmaßnahmen                             |                    |                    |                    |                    |                    |
| M 2.282                       | Regelmäßige Kontrolle von Routern und Switches                               |                    |                    |                    |                    |                    |
| G 2.22                        | Fehlende oder unzureichende Auswertung von Proto- kolldaten                  |                    |                    |                    | K                  | K                  |
| M 4.205                       | Protokollierung bei Routern und Switches                                     |                    |                    |                    | K                  | K                  |
| G 2.27                        | Fehlende oder unzureichende Dokumentation                                    |                    |                    |                    |                    |                    |
| M 2.281                       | Dokumentation der Systemkonfiguration von Routern und Switches               |                    |                    |                    |                    |                    |
| G 2.44                        | Inkompatible aktive Netzkomponenten                                          |                    |                    |                    |                    | K                  |
| M 2.283                       | Software-Pflege auf Routern und Switches                                     |                    |                    |                    |                    | K                  |
| G 2.54                        | Vertraulichkeitsverlust durch Restinformationen                              |                    |                    |                    | K                  | K                  |
| M 2.284                       | Sichere Außerbetriebnahme von Routern und Switches                           |                    |                    |                    | K                  | K                  |
| G 3.64                        | Fehlerhafte Konfiguration von Routern und Switches                           |                    |                    | K                  | K                  | K                  |
| M 3.38                        | Administratorenschulung für Router und Switches                              |                    |                    | K                  | K                  | K                  |
| M 4.202                       | Sichere Netz-Grundkonfiguration von Routern und Swit- ches                   |                    |                    |                    |                    |                    |
| M 4.203                       | Konfigurations-Checkliste für Router und Switches                            |                    |                    |                    |                    |                    |
| G 3.65                        | Fehlerhafte Administration von Routern und Switches                          | K                  | K                  | K                  | K                  | K                  |
| M 4.204                       | Sichere Administration von Routern und Switches                              |                    |                    |                    | K                  | K                  |

<!-- page: 104 -->

| M 5.111   | Einrichtung von Access Control Lists auf Routern       |    |    |    |    | K   |
|-----------|--------------------------------------------------------|----|----|----|----|-----|
| M 6.91    | Datensicherung und Recovery bei Routern und Swit- ches | K  | K  |    |    |     |
| M 6.92    | Notfallvorsorge bei Routern und Switches               |    |    | K  | K  | K   |
| G 5.4     | Diebstahl                                              |    |    |    |    |     |
| M 1.43    | Gesicherte Aufstellung aktiver Netzkomponenten         |    |    |    |    |     |
| G 5.66    | Unberechtigter Anschluss von IT-Systemen an ein Netz   |    | K  |    |    |     |
| M 4.206   | Sicherung von Switch-Ports                             |    | K  |    |    |     |

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 4 -->

> II

> ICS-Netzstruktur ....................................................................................... 26

<!-- page: 5 -->

> III

> Nicht berücksichtigte Gefährdungen ......................................................... 64

> Unterprofil PLC (SPS-Programmierung und -Wartung) ............................. 73

<!-- page: 6 -->

> IV

> Abb. 5.1: Verteilte ICS-Netzstruktur ..................................................................... 27

> Abb. 5.3: Gemischte ICS-Netzstruktur ................................................................. 28

> Abb. 6.3: Physischer Netzplan der generischen Referenzarchitektur ................... 36

> Abb. 8.3: Risikomatrix für die Wasserwirtschaft (angelehnt an [B3S17b]) ............ 52

> Pilotprofils  .......................................................................................... 66

> Referenzarchitektur anhand von Anwendungsfällen .......................... 68

<!-- page: 7 -->

> Tab. 6.1: Generische Zielobjektliste  ..................................................................... 30

> Tab. 7.2: Maßnahmenauswahl für den Baustein B 1.0: Sicherheitsmanagement  . 42

> Tab. 8.2: Gefährdungstabelle für den Baustein B 1.0: Sicherheitsmanagement  ... 48

<!-- page: 8 -->

> 6    0 Vorbemerkungen

<!-- page: 14 -->

> SPS-Programmierung und -Wartung

<!-- page: 16 -->

> Gemeinsames WAN

> SPS-Programmierung und -War-

> Lokale, individuelle SPS-Programmierung und -Wartung

> Lokale, zentralisierte SPS-Programmierung und -Wartung

<!-- page: 18 -->

> aus jedem Unterprofil. Anlegen der Zielobjekt-Maßnahmen-Tabelle:

> Gesamt-Netzplan der ganzen Anlage

> → Sind alle realen Zielobjekte und Anwendungsfälle erfasst?

> branchenspezifischen Hilfen

> 6a

<!-- page: 28 -->

> einheiten, die dies ermöglichen, also mindestens ein Human Machine Interface (HMI). In etwas

> ergeräte räumlich verteilt und mittels eines Wide Area Networks (WAN) mit dem  zentralen

<!-- page: 29 -->

> WAN

<!-- page: 30 -->

> die konzentrierten Anlagen zusätzlich noch über das WAN an den zentralen Leitstand ange-

<!-- page: 32 -->

> IT3  HMI

> Stellt ICS-Funktionen, etwa des HMI oder Historian, über das In-

> men kann. Beispiele sind Engineering- oder HMI-Funktionen und

> A1

> HMI-Software

<!-- page: 34 -->

> VPN

> Umfasst die Soft- und Hardware für den Aufbau einer VPN-Verbin-

> dung, zum Beispiel VPN-Router, VPN-Gateways oder VPN-Ser-

> IDS / IPS

<!-- page: 35 -->

> Standleitung, nichtöffentlicher Funk

<!-- page: 36 -->

> 34    6 Generische Referenzarchitektur

<!-- page: 37 -->

> A1

> B1

> A1

> B1

> A1

> B1

> B1

> B1

> Anwendung B1

> Anwendung B1

<!-- page: 38 -->

> VPN | Modem | Router | FW

> VPN | Modem | Router | FW

<!-- page: 40 -->

> 38    6 Generische Referenzarchitektur

<!-- page: 47 -->

> Neuen Anwendungsfall hinzufügen

> Neues Zielobjekt hinzufügen

<!-- page: 52 -->

> 50    8 Risikobehandlung

<!-- page: 58 -->

> 56    9 Anhang A

<!-- page: 68 -->

> Konkretisieren des Informationsverbunds

> Hilfestellung Anwender mit abweichender

<!-- page: 69 -->

> Schritt 3a

> Schritt 3b

<!-- page: 70 -->

> Schritt 3c

> Modellierung und Maßnahmenauswahl für die spezifischen RA

> Auflistung aller denkbaren Zielobjekte für

> der Zielobjekte miteinander verknüpft sind

> beteiligten, variierenden Zielobjekte und

> Verknüpfungen

> Referenzarchitektur (RA) mit Variationsmöglichkeiten

<!-- page: 73 -->

> Konfiguration von Routern, Switches und WLAN-Access Points, die Implementierung von Ac-

<!-- page: 78 -->

> II

<!-- page: 79 -->

> III

<!-- page: 80 -->

> IV

<!-- page: 97 -->

> (Access Control, AC) gesichert, mindestens einer Firewall. WAN-Kommunikation erfolgt aus-

> AC

> Unkritische Zone

<!-- page: 99 -->

> AC

> AC

> AC

> AC

> AC

> AC

> AC

> AC

> AC
