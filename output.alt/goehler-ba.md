---
source_file: "Goehler_BA.pdf"
source_sha256: 54d8a037a1d7defd3245b95a4ca02063d12cf8f642faba7bced740c7fc5b5796
source_bytes: 517869
pages: 196
tables: 18
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T19:13:38+00:00"
text_coverage_percent: 100.0
appended_source_lines: 5
restored_hyphens: 11
extraction_status: warn
warnings:
  - "11 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): CloudLösung -> Cloud-Lösung, ExchangeSysteme -> Exchange-Systeme, IPAdressen -> IP-Adressen, ITGrundschutz -> IT-Grundschutz, ITGrundschutzes -> IT-Grundschutzes"
  - "Der Textlayer der Quelle enthaelt 679 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
  - "5 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

## Bachelorarbeit

Vergleich von Leitfäden der Privatwirtschaft und staatlichen Einrichtungen zur organisierten Gestaltung der IT-Sicherheit in kleinen und mittleren Unternehmen

Gutachter: Verena Lang

Heiko Krumm Florian Göhler April 2018

Technische Universität Dortmund

Fakultät für Informatik Lehrstuhl IV

http://ls4-www.cs.tu-dortmund.de In Kooperation mit: Bundesamt für Sicherheit in der Informationstechnik

<!-- page: 2 -->



<!-- page: 3 -->

## Inhaltsverzeichnis

| 1 Einleitung                                                          |   1 |
|-----------------------------------------------------------------------|-----|
| 1.1 Motivation und Hintergrund . . . . . . . . . . . . . . . . .      |   1 |
| 1.2 Aufbau der Arbeit . . . . . . . . . . . . . . . . . . . . . .     |   1 |
| 2 Vorstellung der Richtlinien und Herausgeber                         |   3 |
| 2.1 Das Bundesamt für Sicherheit in der Informationstechnik           |   3 |
| 2.2 Der IT-Grundschutz . . . . . . . . . . . . . . . . . . . . .      |   3 |
| 2.3 VdS Schadenverhütung GmbH . . . . . . . . . . . . . . .           |   4 |
| 2.4 VdS 3473 . . . . . . . . . . . . . . . . . . . . . . . . . . .    |   4 |
| 3 ISMS - Sicherheitsmanagement                                        |   7 |
| 3.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . . . . .   |   7 |
| 3.2 ISMS.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . .    |   7 |
| 3.3 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |  10 |
| 4 ORP - Organisation und Personal                                     |  13 |
| 4.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . . . . .   |  13 |
| 4.2 ORP.1 - Organisation . . . . . . . . . . . . . . . . . . . .      |  13 |
| 4.3 ORP.2 - Personal . . . . . . . . . . . . . . . . . . . . . . .    |  16 |
| 4.4 ORP.3 - Sensibilisierung und Schulung . . . . . . . . . .         |  18 |
| 4.5 ORP.4 - Identitäts- und Berechtigungsmanagement . . .             |  20 |
| 4.6 ORP.5 - Compliance Management . . . . . . . . . . . . .           |  22 |
| 4.7 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |  23 |
| 5 CON - Konzeption und Vorgehensweise                                 |  25 |
| 5.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . . . . .   |  25 |
| 5.2 CON.1 - Kryptokonzept . . . . . . . . . . . . . . . . . . .       |  25 |
| 5.3 CON.2 - Datenschutz . . . . . . . . . . . . . . . . . . . .       |  26 |
| 5.4 CON.3 - Datensicherheit . . . . . . . . . . . . . . . . . .       |  26 |
| 5.6 CON.5 - Entwicklung und Einsatz von Fachanwendungen               |  29 |
| 5.7 CON.6 - Löschen und Vernichten . . . . . . . . . . . . . .        |  31 |

<!-- page: 4 -->

| 5.8 CON.7 - Informationssicherheit auf Auslandsreisen . . . .         | . .   |   31 |
|-----------------------------------------------------------------------|-------|------|
| 5.9 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . .   |   35 |
| 6 OPS - Betrieb                                                       |       |   37 |
| 6.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . .   |   37 |
| 6.2 OPS.1.1.2 - Ordnungsgemäße IT-Administration . . . . .            | . .   |   37 |
| 6.3 OPS.1.1.3 - Patch-und Änderungsmanagement . . . . .               | . .   |   40 |
| 6.4 OPS.1.1.4 - Schutz vor Schadprogrammen . . . . . . . .            | . .   |   41 |
| 6.5 OPS.1.1.5 - Protokollierung . . . . . . . . . . . . . . . . .     | . .   |   43 |
| 6.6 OPS.1.1.6 - Software-Tests und -Freigaben . . . . . . . .         | . .   |   45 |
| 6.7 OPS.1.2.2 - Archivierung . . . . . . . . . . . . . . . . . .      | . .   |   46 |
| 6.8 OPS.1.2.3 - Informations- und Datenträgeraustausch . .            | . .   |   48 |
| 6.9 OPS.1.2.4 - Telearbeit . . . . . . . . . . . . . . . . . . . .    | . .   |   50 |
| 6.10 OPS.2.1 - Outsourcing für Kunden . . . . . . . . . . . .         | . .   |   52 |
| 6.11 OPS.2.4 - Fernwartung . . . . . . . . . . . . . . . . . . .      | . .   |   53 |
| 6.12 OPS.3.1 - Outsourcing für Dienstleister . . . . . . . . . .      | . .   |   54 |
| 6.13 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . .   |   55 |
| 7 DER - Detektion und Reaktion                                        |       |   57 |
| 7.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . .   |   57 |
| 7.2 DER.1 - Detektion von sicherheitsrelevanten Ereignissen           | . .   |   57 |
| 7.3 DER.2.1 - Behandlung von Sicherheitsvorfällen . . . . . .         | . .   |   58 |
| 7.4 DER.2.2 - Vorsorge für die IT-Forensik . . . . . . . . . . .      | . .   |   61 |
| 7.5 DER.2.3 - Bereinigung weitreichender Sicherheitsvorfälle          | . .   |   62 |
| 7.6 DER.3.1 - Audits und Revisionen . . . . . . . . . . . . . .       | . .   |   64 |
| 7.7 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . .   |   65 |
| 8 APP - Anwendungen                                                   |       |      |
|                                                                       |       |   67 |
| 8.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . .   |   67 |
| 8.2 APP.1.1 - Office-Produkte . . . . . . . . . . . . . . . . . .     | . .   |   67 |
| 8.3 APP.1.2 - Web-Browser . . . . . . . . . . . . . . . . . . .       | . .   |   69 |
| 8.4 APP.2.1 - Allgemeiner Verzeichnisdienst . . . . . . . . . .       | . .   |   70 |
| 8.5 APP.2.2 - Active Directory . . . . . . . . . . . . . . . . . .    | . .   |   72 |
| 8.6 APP.3.1 - Webanwendungen . . . . . . . . . . . . . . . .          | . .   |   75 |
| 8.7 APP.3.2 - Webserver . . . . . . . . . . . . . . . . . . . . .     | . .   |   78 |
| 8.8 APP.3.3 - Fileserver . . . . . . . . . . . . . . . . . . . . .    | . .   |   80 |
| 8.9 APP.3.4 - Samba . . . . . . . . . . . . . . . . . . . . . . .     | . .   |   82 |
| 8.10 APP.3.6 - DNS-Server . . . . . . . . . . . . . . . . . . .       | . .   |   83 |
| 8.11 APP.4.3 - Relationale Datenbanksysteme . . . . . . . .           | . .   |   86 |
| 8.12 APP.5.1 - Allgemeine Groupware . . . . . . . . . . . . .         | . .   |   89 |

<!-- page: 5 -->

| 8.13 APP.5.2 - Microsoft Exchange und Outlook . . . . . .                                                           | . 90        |
|---------------------------------------------------------------------------------------------------------------------|-------------|
| 8.14 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                    | . 91        |
| 9 SYS - IT-Systeme                                                                                                  | 93          |
| 9.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . . .                                                     | . 93        |
| 9.2 SYS.1.1 - Allgemeiner Server . . . . . . . . . . . . . .                                                        | . 93        |
| 9.3 SYS.1.2.2 - Windows Server 2012 . . . . . . . . . . .                                                           | . 97        |
| 9.4 SYS.1.3: Server unter Unix . . . . . . . . . . . . . . .                                                        | . 98        |
| 9.5 SYS.1.5 - Virtualisierung . . . . . . . . . . . . . . . .                                                       | . 99        |
| 9.6 SYS.1.8 - Speicherlösungen . . . . . . . . . . . . . .                                                          | . 102       |
| 9.7 SYS.2.1 - Allgemeiner Client . . . . . . . . . . . . . .                                                        | . 104       |
| 9.8 SYS.2.2.2: Clients unter Windows 8.1 . . . . . . . . .                                                          | . 106       |
| 9.9 SYS.2.2.3: Clients unter Windows 10 . . . . . . . . .                                                           | . 107       |
| 9.10 SYS.2.3 - Clients unter Unix . . . . . . . . . . . . . .                                                       | . 109       |
| 9.11 SYS.3.1 - Laptops . . . . . . . . . . . . . . . . . . .                                                        | . 111       |
| 9.12 SYS.3.2.1 - Allgemeine Smartphones und Tablets . .                                                             | . 113       |
| 9.13 SYS.3.2.2: Mobile Device Management (MDM) . . .                                                                | . 116       |
| 9.14 SYS.3.2.3 - iOS (for Enterprise) . . . . . . . . . . . .                                                       | . 116       |
| 9.15 SYS.3.2.4 - Android . . . . . . . . . . . . . . . . . .                                                        | . 118       |
| 9.16 SYS.3.4 - Mobile Datenträger . . . . . . . . . . . . .                                                         | . 119       |
| 9.17 SYS.4.1 - Drucker, Kopierer und Multifunktionsgeräte                                                           | . 120       |
| 9.18 SYS.4.4 - Allgemeines IoT-Gerät . . . . . . . . . . .                                                          | . 121       |
| 9.19 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                    | . 122       |
| 10 IND - Industrielle IT                                                                                            | 125         |
| 10.1 Übersicht . . . . . . . . . .                                                                                  | . 125       |
| . . . . . . . . . . . . . .                                                                                         | . 125       |
| 10.2 IND.1 - Betriebs- und Steuerungstechnik . . . . . . . 10.3 IND.2.1 - Allgemeine ICS-Komponente . . . . . . . . | . 127       |
| 10.4 IND.2.3 - Sensoren und Aktoren . . . . . . . . . . . .                                                         | . 128       |
| 10.5 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                    | . 129       |
| 11 NET - Netze und Kommunikation                                                                                    | 131         |
| 11.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . .                                                      | . 131       |
| 11.2 NET.1.1 - Netzarchitektur und -design . . . . . . . .                                                          | . 131       |
| 11.3 NET.1.2 - Netzmanagement . . . . . . . . . . . . . .                                                           | . 135       |
| 11.4 NET.2.1 - WLAN-Betrieb . . . . . . . . . . . . . . . .                                                         |             |
| 11.5 NET.2.2 - WLAN-Nutzung . . . . . . . . . . . . . .                                                             | . 138 . 140 |
| . 11.6 NET.3.1 - Router und Switches . . . . . . . . . . . .                                                        | . 142       |
| 11.7 NET.3.2 - Firewall . . . . . . . . . . . . . . . . . . . .                                                     |             |
|                                                                                                                     | . 145       |
| 11.8 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                    | . 149       |

<!-- page: 6 -->

| 12 INF - Infrastruktur                                                    | 151     |
|---------------------------------------------------------------------------|---------|
| 12.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . . 151 |
| 12.2 INF.1 - Allgemeines Gebäude . . . . . . . . . . . . . . . . . .      | . . 151 |
| 12.3 INF.2 - Rechenzentrum sowie Serverraum . . . . . . . . . . .         | . . 153 |
| 12.4 INF.3 - Elektrotechnische Verkabelung . . . . . . . . . . . . .      | . . 156 |
| 12.5 INF.4 - IT-Verkabelung . . . . . . . . . . . . . . . . . . . . . .   | . . 157 |
| 12.6 INF.7 - Büroarbeitsplatz . . . . . . . . . . . . . . . . . . . . .   | . . 158 |
| 12.7 INF.8 - Häuslicher Arbeitsplatz . . . . . . . . . . . . . . . . .    | . . 158 |
| 12.8 INF.9: Mobiler Arbeitsplatz . . . . . . . . . . . . . . . . . . . .  | . . 159 |
| 12.9 INF.10 - Besprechungs-, Veranstaltungs- und Schulungsräume           | . . 161 |
| 12.10 Fazit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . 162 |
| 13 Fazit                                                                  | 163     |
| 13.1 Analyse der Ergebnisse . . . . . . . . . . . . . . . . . . . . .     | . . 163 |
| 13.2 Schlussfolgerungen für das Sicherheitsniveau . . . . . . . . .       | . . 164 |
| 13.3 Vergleich zu ISO 27001 . . . . . . . . . . . . . . . . . . . . .     | . . 166 |
| 13.4 Überlegungen zur Anwendbarkeit . . . . . . . . . . . . . . . .       | . . 166 |
| 13.5 Notwendige Ergänzungen in VdS 3473 . . . . . . . . . . . . .         | . . 167 |
| 14 Danksagungen                                                           | 169     |
| A Weitere                                                                 |         |
| Informationen                                                             | 171     |
| A.1 Übersichtstabelle . . . . . . . . . . . . . . . . . . . . . . . . .   | . . 172 |
| A.2 Anteil der erfüllten Anforderungen . . . . . . . . . . . . . . . .    | . . 186 |
| Literaturverzeichnis                                                      | 188     |
| Erklärung                                                                 | 188     |

<!-- page: 7 -->

## Kapitel 1

## Einleitung

## 1.1 Motivation und Hintergrund

Für die meisten Unternehmen in Deutschland sind IT-Systeme ein wesentlicher Bestandteil der täglichen Betriebsabläufe. Selbst kleinere Unternehmen, deren Geschäftsfelder nicht unmittelbar auf Computer angewiesen sind, benötigen oft IT-Systeme um ihre Verwaltungsangelegenheiten zu organisieren. Von großer Bedeutung ist dabei natürlich, dass die vorhandenen IT-Systeme sicher und zuverlässig funktionieren.

Während es für große Unternehmen oft möglich ist ganze Abteilungen von Mitarbeitern für den sicheren Betrieb von Informationssystemen bereitzustellen, können kleinere und mittlere Unternehmen (KMU) dies oft nicht leisten. Problematisch dabei ist, dass besonders mittelgroße Unternehmen durch IT-Sicherheitsvorfälle bedroht sind [7].

Um den Gefahren durch 'Cyber-Angriffe' zu begegnen gibt es verschiedene Standards, Richtlinien und Leitfäden, die Unternehmen dabei helfen sollen IT-Sicherheit in ihre Betriebsabläufe zu integrieren. Herausgegeben werden solche Anleitungen u. a. von internationalen Organisationen, Branchenverbänden und Behörden. Obwohl die Herausgeber dieser Regelwerke im Wesentlichen die gleichen Ziele verfolgen, gibt es zwischen den verschiedenen Ansätzen teils große Unterschiede. Zwei Beispiele für solche Standards sind das 'IT-Grundschutz-Kompendium' des Bundesamtes für Sicherheit in der Informationstechnik [6] und 'VdS 3473' [9], von der VdS Schadenverhütung GmbH. Beide Standards sind für KMU geeignet, jedoch unterscheidet sich der Umfang beider Werke erheblich. Ziel dieser Arbeit ist zu beurteilen ob deren Sicherheitsniveau vergleichbar ist, trotz der großen Unterschiede zwischen den Standards.

## 1.2 Aufbau der Arbeit

Der Hauptteil dieser Arbeit beschäftigt sich mit dem direkten Vergleich der 'Basis-Anforderungen' des IT-Grundschutzes mit den 'MUSS '-Vorgaben von VdS 3473. Dabei wird jede Anforderung des IT-Grundschutzes kurz beschrieben. Anschließend stelle ich mögliche Entsprechungen in VdS 3473 dar und diskutiere die Unterschiede zwischen den jeweiligen Vorgaben, falls diese vorhanden sind.

<!-- page: 8 -->

Bei der Betrachtung der Unterschiede ordne ich jede Anforderung des IT-Grundschutzes in eine von 3 Gruppen ein. Die 1. Gruppe enthält Anforderungen, die vollständig oder nur mit minimalen Abweichungen von VdS 3473 erfüllt wird. In die 2. Gruppe ordne ich Anforderungen ein, die nur teilweise oder mit deutlichen Unterschieden von VdS 3473 abgedeckt werden. Anforderungen des IT-Grundschutzes, die gar nicht von VdS 3473 abgedeckt werden oder bei denen es erhebliche Unterschiede gibt, ordne ich in die 3. Gruppe ein. Die so getroffenen Einordnungen werden, in Form eines Ampel-Farbsystems, als Tabelle in Anhang (1) dargestellt. Im Hauptteil ergibt sich die Einordnung aus der Beschreibung der Unterschiede bzw. Entsprechungen in VdS 3473.

Die Bewertung der Unterschiede orientiert sich an deren Einfluss auf das Sicherheitsniveau. Sollte eine Anforderung nicht offensichtlich eingeordnet werden können, werden die Kriterien, die zur Einordnung geführt haben, besonders hervorgehoben.

Nach jeder Bausteingruppe ziehe ich ein Zwischenfazit. Damit soll der Vergleich des Sicherheitsniveaus, bezogen auf den jeweiligen Anwendungsbereich, ermöglicht werden. Außerdem kann die Einordnung des Gesamtergebnisses so auf den Teilergebnissen aufbauen.

<!-- page: 9 -->

## Kapitel 2

## Vorstellung der Richtlinien und Herausgeber

## 2.1 Das Bundesamt für Sicherheit in der Informationstechnik

1991 wurde das Bundesamt für Sicherheit in der Informationstechnik (BSI) als Behörde des Bundes gegründet und dem Bundesministerium des Inneren unterstellt. Grundlage für die Arbeit des BSI ist das BSI-Gesetz, aus welchem auch die Aufgaben des BSI hervorgehen. Unter anderem muss das BSI Behörden in Fragen der Informationssicherheit beraten, Informationen über aktuelle IT-Gefahren bewerten und IT-Systeme zertifizieren.[1]

## 2.2 Der IT-Grundschutz

Der IT-Grundschutz wird seit etwa 20 Jahren als Regelwerk zur Gestaltung der Informationssicherheit in Behörden und Unternehmen genutzt. Im Jahr 2017 wurden die bisherigen Grundschutzkataloge grundlegend überarbeitet und als neues 'IT-GrundschutzKompendium' im Februar 2018 veröffentlicht. Eine Vorabversion war bereits während der Überarbeitung verfügbar.

Das IT-Grundschutz-Kompendium ist in Form von Bausteinen strukturiert, welche wiederum in Gruppen zusammen gefasst sind. Jede Gruppe ist einem Teilbereich der Informationssicherheit gewidmet, z. B. gibt es eine Gruppe für Softwareanwendungen und eine weitere Gruppe für IT-Systeme. Die einzelnen Bausteine befassen sich mit einem Teilbereich ihrer jeweiligen Gruppe. Es gibt bspw. einen Baustein für Client-Systeme mit Windows-Betriebssystem und einen anderen Baustein für Systeme mit Unix-Betriebssystem.

Ein Baustein besteht aus einer einleitenden Beschreibung, aus welcher der Zweck und die Ziele des Bausteins hervorgehen. Daran schließt eine Benennung von möglichen Gefahren an, die durch mangelnde Sicherheit in dem jeweils betrachteten Bereich entstehen können. Der wesentliche Teil eines Bausteins besteht aus einer Reihe von Sicherheitsanforderungen. Diese sind in drei Gruppen eingeteilt. Im Bereich der Basisanforderungen finden sich Vorgaben, welche ein Unternehmen unbedingt umsetzten muss um ein grundlegendes Schutzniveau zu erreichen. Die weitergehenden Standardanforderungen können nach den Basis-Anforderungen umgesetzt werden, damit das Sicherheitsniveau weiter ausgebaut wird. Mit Umsetzung der Standardanforderungen entspricht die Informationssicherheit dem aktuellen Stand der Technik. Die letzte Gruppe der Anforderungen ist bei erhöhtem Schutzbedarf umzusetzen, also bei IT-Systemen, die für ein Unternehmen von erheblicher Bedeutung sind.

<!-- page: 10 -->

Im Rahmen dieser Arbeit werde ich nur die Basisanforderungen der Bausteine vergleichen. Insgesamt besteht der IT-Grundschutz aus ca. 70 Bausteinen und weit über 400 Basisanforderungen, von denen die meisten in dieser Arbeit betrachtet werden.

Neben dem Grundschutz-Kompendium, welches in dieser Arbeit betrachtet wird, gibt es noch weitere Standards im IT-Grundschutz, die bei der Organisation der Informationssicherheit nützlich sind.

## 2.3 VdS Schadenverhütung GmbH

Die VdS Schadenverhütung GmbH ist ein Tochterunternehmen des Gesamtverband der Deutschen Versicherungswirtschaft e.V. (GDV). In ihrer heutigen Form existiert sie seit 1997. Vorgängerunternehmen, die im Laufe der Zeit umgewandelt wurden, gab es jedoch schon zu Beginn des 20. Jahrhunderts.

Das Unternehmensziel der VdS ist, ihrem Namen entsprechend, den in Deutschland ansässigen Unternehmen dabei zu helfen Schäden zu vermeiden. Dabei ist die VdS, anders als das BSI, jedoch nicht ausschließlich auf den Bereich der Informationssicherheit beschränkt. Neben dem Schutz vor 'Cyber-Gefahren' hat die VdS auch die Aufgabe Unternehmen in den Bereichen Brandschutz, Umweltschutz oder Einbruchsschutz zu beraten und zu zertifizieren.[8]

## 2.4 VdS 3473

Um insbesondere kleinen und mittleren Unternehmen einen organisierten Schutz vor Gefahren für die Informationssicherheit zu ermöglichen hat die VdS die Richtlinie 'VdS 3473 - Cyber-Security für kleine und mittlere Unternehmen (KMU)' erstellt. Wie der IT-Grundschutz wird diese regelmäßig weiter entwickelt. Mit ihren 38 Seiten ist VdS 3473 jedoch erheblich weniger umfangreich als das IT-Grundschutz-Kompendium.

Der Aufbau von VdS 3473 unterscheidet sich von dem des Grundschutz-Kompendiums. Einzelne Bereiche des Informationssicherheitsmanagements sind in Kapiteln angeordnet, welche kurz in das Teilgebiet einführen. Die eigentlichen Anforderungen sind dann, ggf. weiter untergliedert, beschrieben. Die VdS unterscheidet zwischen zwei Arten von Vorgaben: 'MUSS'- und 'SOLLTE'-Anforderungen. Erstere müssen von Unternehmen vorrangig umgesetzt werden. Sie sind vergleichbar mit den Basisanforderungen des BSI. Die SOLLTE-Anforderungen entsprechen den Standardanforderungen des IT-Grundschutzes. Die VdS sieht außerdem die Identifikation von kritischen IT-Systemen vor, für die es besondere Anforderungen gibt. Dies ist mit den Anforderungen für erhöhten Schutzbedarf des IT-Grundschutz vergleichbar.

<!-- page: 11 -->

VdS 3473 nimmt an einigen Stellen Bezug auf den IT-Grundschutz des BSI sowie auf vergleichbare Standards und verzichtet auf eigene Zusatzwerke, die bei der Umsetzung der Anforderungen helfen sollen.

<!-- page: 12 -->



<!-- page: 13 -->

## Kapitel 3

## ISMS - Sicherheitsmanagement

## 3.1 Übersicht

Die erste Bausteingruppe des IT- Grundschutz Kompendiums ist die 'ISMS'- Gruppe. Sie besteht nur aus einem Baustein (ISMS.1) und bildet den Grundstein für die Integration der Informationssicherheit in die Strukturen von Unternehmen und Behörden.

## 3.2 ISMS.1

ISMS.1 regelt unter anderem die Verantwortlichkeiten für die Informationssicherheit innerhalb von Organisationen.

## 3.2.1 ISMS.1.A1

Die erste Anforderung, die das BSI im Rahmen der Basisabsicherung stellt, richtet sich an die Leitungsebene einer Organisation. Diese muss die Gesamtverantwortung für die Informationssicherheit übernehmen, die nötigen Prozesse initiieren und regelmäßig überprüfen. Außerdem fordert der Baustein, dass die Leitungsebene Informationssicherheit vorlebt, weitere Zuständigkeiten im Bezug auf Informationssicherheit benennt und entsprechende Mitarbeiter angemessen ausstattet.

## Entsprechungen in VdS 3473

Auch die VdS sieht die Gesamtverantwortung für die Informationssicherheit und den Sicherheitsprozess bei der jeweiligen Organisationsleitung. Diese muss nach den Vorgaben der VdS 3473 ebenfalls die nötigen Ressourcen zur Verfügung stellen und Informationssicherheit in allen Bereichen des Unternehmens integrieren. Ensprechende Vorgaben finden sich in Abschnitt 4.2 von VdS 3473.

<!-- page: 14 -->

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen

## 3.2.2 ISMS.1.A2 und ISMS.1.A3

Umeinen geordneten Ablauf für den Informationssicherheitsprozess zu ermöglichen, fordert das BSI die Festlegung von Sicherheitszielen und einer Sicherheitsstrategie sowie die Erstellung von konzeptionellen Vorgaben und das Schaffen eines organisatorischen Rahmens, welcher die Umsetzung dieser Ziele ermöglicht. Die Leitung einer Organisation verantwortet diese Vorgaben und muss diese regelmäßig überprüfen. Das Ergebnis dieser Anforderung ist zu dokumentieren und wird zu einem Teil der Informationssicherheitsleitlinie, welche allen Mitarbeitern bekanntgegeben werden muss.

## Entsprechungen in VdS 3473

Eine, den Anforderungen des BSI nahe kommende, Vorgabe findet sich auch in den Vorgaben der VdS: die Leitungsebene ist verpflichtet zum 'Einbetten der Informationssicherheit in die Strukturen, Hierarchien und Arbeitsabläufe des Unternehmens' [9, Punkt 4.2.5]. Dazu gehört ebenfalls das Beschließen einer Informationssicherheitsleitlinie in der die Sicherheitsziele festgehalten werden. Die Ziele im Bezug auf Informationssicherheit müssen, wie im IT-Grundschutz, regelmäßig überprüft werden.

## Unterschiede

Das BSI fordert in der Basisabsicherung nicht das die Leitlinie zur Informationssicherheit regelmäßig aktualisiert wird, dies ist als 'SOLLTE'- Anforderung erst in der Standardabsicherung vorgesehen. Bei der VdS ist dies jedoch als 'MUSS'-Anforderung jährlich vorgesehen.

## 3.2.3 ISMS.1.A4 und ISMS.1.A5

Eine wichtige Rolle in der Informationssicherheit nimmt der Informationssicherheitsbeauftragte (ISB) ein, welcher von der Leitungsebene benannt werden muss. Der ISB muss den Sicherheitsprozess koordinieren und dafür angemessen ausgestattet und qualifiziert sein. Er muss der Leitungsebene direkt berichten können und bei Veränderungen in den IT-Systemen der Organisation einbezogen werden. Sollte der ISB durch einen externen Dienstleister gestellt werden, müssen die Aufgaben, Rechte und Pflichten, sowie die Vertraulichkeit und die Beendigung der Beauftragung vertraglich geregelt sein.

<!-- page: 15 -->

## Entsprechungen in VdS 3473

Auch die VdS fordert, dass ein ISB von der Leitungsebene benannt wird. Zu seinen Aufgaben gehört ebenfalls das Steuern des Sicherheitsprozesses. Er muss bei allen wesentlichen Veränderungen im Bereich der Informationsverarbeitung eingebunden werden. In Abschnitt 7.1 von VdS 3473 wird eine Eignung von Mitarbeitern vorgeschrieben.

## Unterschiede

Zum Bestellen eines externen ISB finden sich in VdS 3473 keine Angaben.

## 3.2.4 ISMS.1.A6

In einem Unternehmen muss eine 'übergreifende' Organisationsstruktur für Informationssicherheit geschaffen werden. Dafür müssen Rollen definiert werden, die für die Erfüllung der Sicherheitsziele zuständig sind. Diese müssen mit geeigneten Mitarbeitern besetzt und ausreichend Ressourcen ausgestattet sein. Dieses beinhaltet auch eine Vertretungsregelung. Es muss ebenfalls festgelegt werden, welche Rolle zu welcher Zeit und in welchem Umfang mit Informationen versorgt wird. Diese Vorgaben müssen regelmäßig auf Aktualität geprüft werden.

## Entsprechungen in VdS 3473

Bereits im Abschnitt zu ISMS.1.A1 wurde diskutiert, dass die Leitungsebene einer Organisation die Gesamtverantwortung für die Informationssicherheit trägt. In VdS 3473 ist als 'MUSS'- Anforderung ebenfalls festgelegt, dass die Leitungsebene 'Informationssicherheit' in alle Bereiche des Unternehmens integrieren muss [9, Abschnitt 4.2].

Die VdS sieht das Bestellen eines Informationssicherheitsteams vor, was den zu definierenden Rollen im BSI- Baustein entspricht.

## Unterschiede

Während das BSI abstrakt von 'Rollen' spricht, welche definiert werden müssen, geht die VdS einen Schritt weiter und benennt explizit einige Rollen, die in einem Team arbeiten und den ISB unterstützen sollen. Dabei werden auch einige Aufgaben explizit an andere Verantwortliche abgegeben.

Auf Seiten des BSI-Bausteins wird darüber hinaus eine eindeutige Festlegung von Informationswegen und Vertretungen verlangt, was in VdS 3473 nicht gefordert ist.

<!-- page: 16 -->

## 3.2.5 ISMS.1.A7 und ISMS.1.A8

Die Basisabsicherung sieht als Nächstes vor, dass für die gesamte Informationsverarbeitung Sicherheitsmaßnahmen festgelegt werden. Diese müssen Mitarbeitern bekannt sein und von diesen umgesetzt werden, sofern sie deren Arbeitsplatz betreffen. Mitarbeiter müssen in den Sicherheitsprozess einbezogen werden und die Möglichkeit haben diesen aktiv mit zu gestalten. Allen Mitarbeitern muss bekannt sein, wie sie SicherheitsWerkzeuge und -Richtlinien anwenden müssen.

## Entsprechungen in VdS 3473

Die VdS sieht die Erstellung von Sicherheitsrichtlinien vor, in denen konkrete Maßnahmen benannt werden müssen [9, Abschnitt 6]. Außerdem werden an vielen Stellen der VdS 3474 konkrete Maßnahmen für die Informationssicherheit verlangt. Laut der VdS müssen Mitarbeiter, die für sie relevanten Sicherheitsleitlinien kennen. Das Personal wird von der VdS in Abschnitt 4.4 in den Sicherheitsprozess eingebunden.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 3.2.6 ISMS.1.A9

Die Informationssicherheit muss in alte sowie neue Geschäftsprozesse einfließen und der ISB muss an für ihn relevanten Entscheidungen beteiligt werden.

## Entsprechungen in VdS 3473

Die VdS sieht die Verantwortung für die Integration in die Geschäftsprozesse bei der Leitung eines Unternehmens (Abschnitt 4.2) und verlangt ebenfalls das der ISB an Entscheidungen, die seine Aufgabe betreffen, beteiligt wird (z.B. 4.9).

## Unterschiede

In diesem Bereich finden sich keine Unterschiede zwischen dem BSI-Baustein und der Richtlinie der VdS, die das Sicherheitsniveau beeinflussen würden.

## 3.3 Fazit

Von den 9 Anforderungen in diesem Baustein werden 7 ganz oder nur mit minimalen Abweichungen erfüllt. Nur jeweils eine Anforderung wird nur zum Teil bzw. gar nicht erfüllt. Insgesamt sind die Anforderungen der beiden Richtlinien an die Organisation der Informationssicherheit also vergleichbar. Auf Seiten der VdS sollten aber Anforderungen bezüglich externer ISBs und Vertretungsregelungen ergänzt werden. Besonders die fehlenden Vertretungsregelungen könnten bei unerwartetem Ausfall eines Mitarbeiters zu Problemen führen.

<!-- page: 17 -->



<!-- page: 18 -->



<!-- page: 19 -->

## Kapitel 4

## ORP - Organisation und Personal

## 4.1 Übersicht

Die zweite Bausteingruppe des IT-Grundschutz-Kompendiums beschäftigt sich mit Organisation und Personal. Sie wird mit 'ORP' abgekürzt und umfasst 5 Bausteine. Im ersten Baustein der Gruppe wird definiert wie die Informationssicherheit in die Organisation eines Unternehmens integriert werden kann. ORP .1 legt somit den Rahmen für die Umsetzung der weiteren Bausteine fest.

## 4.2 ORP.1 - Organisation

Im ersten Baustein der Gruppe wird definiert wie 'Informationssicherheit' in die Organisation eines Unternehmens integriert werden kann. ORP .1 legt somit den Rahmen für die Umsetzung der weiteren Bausteine fest.

## 4.2.1 ORP.1.A1

Als erste Anforderung sieht der Baustein vor, dass die Aufgaben, die sicherheitsrelevant sind, mit klaren Verantwortlichkeiten versehen werden. Außerdem sollen die jeweiligen Befugnisse klar geregelt werden. Die Regelungen müssen alle Bertriebsaspekte umfassen und allen Mitarbeitern bekannt gemacht werden. Es muss festgelegt werden, welche Informationen mit wem ausgetauscht werden dürfen und wie diese dabei zu schützen sind. Eine regelmäßige Überarbeitung dieser Regeln ist ebenfalls vorgesehen. Diese Anforderung muss von der Leitung der jeweiligen Institution erfüllt werden.

## Entsprechungen in VdS 3473

In der Richtlinie der VdS wird die Organisation der Informationssicherheit in Abschnitt 4 geregelt. In Abschnitt 4.1 wird, ähnlich wie im BSI-Baustein, gefordert, dass Verantwortlichkeiten im IT-Sicherheitsprozess geregelt werden. Ebenfalls sind die Befugnisse der betreffenden Personen zu regeln. Vom Personal wird in Punkt 4.8 verlangt, dass es die Regeln für die Informationssicherheit einhält, entsprechend muss es über die Regelungen informiert sein. In Abschnitt 4.2 wird das 'Top Management' für den IT- Sicherheitsprozess verantwortlich gemacht. Das regelmäßige Überprüfen der festgelegten Regeln ist bereits in der Einleitung zu Abschnitt 4 gefordert.

<!-- page: 20 -->

## Unterschiede

Zwischen den Anforderungen des BSI und denen der VdS gibt es in diesem Bereich nur einen Unterschied: im Bereich 'Organisation' wird von der VdS nicht gefordert, dass festgelegt wird mit wem Informationen ausgetauscht werden dürfen. In allen übrigen Aspekten entsprechen die Anforderungen der VdS denen des BSI, sodass es nur eine geringfügige Abweichung gibt.

## 4.2.2 ORP.1.A2

Als zweite Anforderung verlangt der Baustein, dass für alle Geschäftsprozesse, Anwendungen und IT-Komponenten festgelegt wird, wer für deren Sicherheit verantwortlich ist. Alle Mitarbeiter müssen über diese Information verfügen, insbesondere muss ihnen eine eventuelle eigene Verantwortlichkeit bekannt sein.

## Entsprechungen in VdS 3473

In Punkt 4.1 und 4.1.1 wird von der VdS verlangt, dass für alle Ressourcen eine Verantwortlichkeit benannt wird. Ebenfalls muss das Personal (Punkt 4.8) über Regelungen informiert sein, welche es betreffen.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen des BSI und denen der VdS.

## 4.2.3 ORP.1.A3

In dieser Anforderung wird verlangt, dass Mitarbeiter dazu angehalten werden, betriebsfremde Personen nicht alleine zu lassen.

## Entsprechungen in VdS 3473

Es gibt keine explizite Entsprechung in der Richtlinie der VdS.

<!-- page: 21 -->

## 4.2.4 ORP.1.A4

In dieser Anforderung wird verlangt, dass alle Aufgaben in einer Organisation klar definiert und abgegrenzt sind. Insbesondere muss eine Funktionstrennung erfolgen: Mitarbeiter mit operativen Aufgaben dürfen nicht gleichzeitig mit der Kontrolle ihrer Aufgaben beauftragt sein.

## Entsprechungen in VdS 3473

Die VdS widmet den Abschnitt 4.1.2 der Funktionstrennung. Dort wird analog zum BSI verlangt, dass widersprechende Aufgaben nicht der gleichen Person zugeordnet werden. Darüber hinaus regelt die VdS ebenfalls wie vorzugehen ist, wenn eine Funktionstrennung nicht möglich ist.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 4.2.5 ORP.1.A5

In der letzten Basis-Anforderung dieses Bausteins wird das Berechtigungsmanagement geregelt. Das BSI verlangt mit dieser Anforderung, dass Personen nur die Zugangs/Zugriffsrechte haben, die sie zur Erfüllung ihrer Aufgaben benötigen. Außerdem muss das Verfahren für die Vergabe und die Dokumentation dieser Berechtigungen geregelt sein.

## Entsprechungen in VdS 3473

In Kapitel 15 wird das Verfahren für die Vergabe von Zugangs-/Zugriffsrechten definiert. Entsprechend den Anforderungen des BSI wird vorgeschrieben, dass nur notwendige Zugriffe erlaubt sind. Auch ein Vergabeverfahren und eine entsprechende Dokumentation sind vorgesehen.

## Unterschiede

Es gibt keine Abweichungen zwischen den Anforderungen der IT-Grundschutzes und denen der VdS 3473.

<!-- page: 22 -->

## 4.3 ORP.2 - Personal

Dieser Baustein regelt wie mit Personal im Bezug auf Sicherheitsfragen umgegangen werden muss. Dabei werden alle Aspekte, von der Einstellung bis zum Abgang eines Mitarbeiters, geregelt.

## 4.3.1 ORP.2.A1

Der Baustein beginnt bei der Einarbeitung neuer Mitarbeiter. Diese müssen in ihre Aufgaben, die Regeln und Umgangsformen in der Einrichtung eingewiesen werden. Dabei müssen auch die Regelungen zur Informationssicherheit, sowie deren Auswirkungen und Veränderungen berücksichtigt werden. Neue Mitarbeiter sollen explizit darauf hingewiesen werden, dass sie sich an Vorschriften und Gesetze halten müssen. Grundsätzlich müssen alle Informationen, die Mitarbeitern währen ihrer Arbeitszeit bekannt werden, vertraulich behandelt werden.

## Entsprechungen in VdS 3473

In Abschnitt 7 der VdS 3473 wird der Umgang mit Personal im Bezug auf Informationssicherheit geregelt. Die VdS fordert, genau so wie das BSI, dass neue Mitarbeiter in bestehende Regeln zur Informationssicherheit eingewiesen werden.

## Unterschiede

Die VdS verlangt nicht, dass Mitarbeiter explizit auf die Einhaltung von Gesetzen hingewiesen werden. Die Vorgaben der VdS weichen in diesem Punkt also merklich von denen des BSI ab. Es sind verschiedene Situationen denkbar, in denen einem Mitarbeiter nicht bewusst ist, dass eine Handlung gegen ein Gesetz verstößt. Ein Beispiel könnten externe Mitarbeiter aus anderen Staaten sein.

## 4.3.2 ORP.2.A2

In der zweiten Anforderung des Baustein wird das Weggehen eines Mitarbeiters geregelt. Wenn ein Mitarbeiter das Unternehmen verlässt, muss dessen Nachfolger rechtzeitig eingearbeitet werden, falls möglich durch den abgehenden Mitarbeiter. Sollte dies nicht möglich sein, muss der abgehende Mitarbeiter eine Dokumentation über seinen Arbeitsbereich anfertigen.

Dem Mitarbeiter müssen alle Zugangs- und Zugriffsrechte entzogen werden, gegebenenfalls müssen Ablauf- und Alarmpläne angepasst werden. Allen relevanten Stellen in der Institution muss der Abgang des Mitarbeiters bekannt gemacht werden.

<!-- page: 23 -->

## Entsprechungen in VdS 3473

Die VdS verlangt, dass es ein Verfahren für den Abgang eines Mitarbeiters geben muss (Abschnitt 7.3). Ebenfalls müssen Stellen über das Ausscheiden des Mitarbeiters informiert werden, sofern dies erforderlich ist. Das Anpassen von Zugangsrechten ist vorgeschrieben.

## Unterschiede

Die VdS macht keine Angaben zu den weiteren Aspekten eines Mitarbeiterwechsels, etwa der Dokumentation bisheriger Arbeiten. Die Anforderungen des BSI sind deutlich genauer.

## 4.3.3 ORP.2.A3

In Anforderung 3 des Bausteins werden Vorgaben für die Benennung von Vertretern gemacht. Regelungen für die Vertretung von Mitarbeitern müssen von Vorgesetzten getroffen werden. Die Regelungen müssen frühzeitig und eindeutig festgelegt werden. Ein zur Vertretung benannter Mitarbeiter muss über die entsprechenden Aufgaben informiert sein und für deren Erfüllung geeignet sein. Sollte kein eigener Mitarbeiter in Frage kommen, muss frühzeitig über das Einsetzen von externen Kräften nachgedacht werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in der Richtlinie der VdS.

## 4.3.4 ORP.2.A4

Beim Einsatz von Fremdpersonal in der Institution muss dieses ebenfalls auf das Einhalten von Gesetzen und Vorschriften hingewiesen werden. Sollte es sich um einen kurzzeitigen Einsatz handeln, kann das Personal so behandelt werden wie Besucher. Insbesondere muss es in sensiblen Bereichen beaufsichtigt werden.

Bei einer längerfristigen Beschäftigung von Fremdpersonal muss dieses, genau wie eigene Mitarbeiter, in seine Aufgaben eingewiesen werden. Analog zu internen Mitarbeitern gelten die Anforderungen aus ORP .2.A2/A3.

## Entsprechungen in VdS 3473

Regelungen für den Einsatz von Fremdpersonal sind in Abschnitt 6.4 der VdS 3474 zu finden. Dort wird verlangt, dass analog zu den Regelungen für Mitarbeiter auch Regeln für Auftragnehmer geschaffen werden.

<!-- page: 24 -->

## Unterschiede

Die VdS verzichtet auf eine Vertretungsregelung für Fremdpersonen. Durch die umfangreichen und konkreten Anforderungen, die in Abschnitt 6.4 aufgeführt sind, entsprechen die erforderlichen Maßnahmen für Fremdpersonal aber im Wesentlichen denen des BSI.

## 4.3.5 ORP.2.A5

In dieser Anforderung wird verlangt, dass Fremdpersonal eine Vertraulichkeitsvereinbarung unterzeichnen muss, welche den Umgang mit allen Informationen der Institution regelt.

## Entsprechungen in VdS 3473

In Punkt 6.4.6 wird verlangt, dass für Fremdpersonen der Umgang mit Informationen geregelt wird.

## Unterschiede

Die VdS macht in ihrer Anforderung genauere Angaben, welche Maßnahmen durch eine Regelung umgesetzt werden müssen. Das BSI hält diesen Punkt eher abstrakt. In diesem Punkt sind die Anforderungen der VdS genauer als die des BSI.

## 4.4 ORP.3 - Sensibilisierung und Schulung

Ein wichtiger Aspekt im Rahmen des Informationssicherheitsprozesses ist die Schulung und Sensibilisierung der Mitarbeiter. Anforderungen an einen organisierten Prozess dafür werden in Baustein 3 aus der ORP-Gruppe definiert.

## 4.4.1 ORP.3.A1

In dieser Anforderung wird festgelegt, dass die oberste Leitungsebene für Informationssicherheit sensibilisiert werden muss. Maßnahmen zur Sensibilisierung müssen von ihr unterstützt werden. Alle Vorgesetzten müssen Sicherheitsregeln einhalten, damit sie als Vorbild angesehen werden. Vorgesetzte müssen ihre Mitarbeiter auf die Einhaltung von Regelungen hinweisen.

## Entsprechungen in VdS 3473

Auch die VdS erkennt die Verantwortung des 'Top-Managements' bei der Informationssicherheit [9, Abschnitt 4.2]. Dieses muss die Informationssicherheit in alle Betriebsabläufe integrieren. Gemäß Abschnitt 8.2 muss Personal in Fragen der Informationssicherheit geschult werden.

<!-- page: 25 -->

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen der VdS und denen des BSI.

## 4.4.2 ORP.3.A2

Jede Institution muss einen Ansprechpartner haben, welcher Fragen zur Informationssicherheit beantworten kann. Alle Mitarbeiter müssen diesen kennen.

## Entsprechungen in VdS 3473

Der ISB soll gem. 4.3.10 als zentraler Ansprechpartner für Informationssicherheit zur Verfügung stehen.

## Unterschiede

Das BSI beschränkt die Rolle des Ansprechpartners nicht auf den ISB. Da jedoch in beiden Anforderungen ein Ansprechpartner gefordert wird, gibt es keinen Unterschied im Bezug auf das Sicherheitsniveau.

## 4.4.3 ORP.3.A3

In der letzten Basis-Anforderung des Bausteins wird gefordert, dass alle internen und externen Mitarbeiter im Umgang mit IT-Komponenten aus ihrem Arbeitsbereich unterwiesen werden. Dies muss in einer Richtlinie geregelt sein.

## Entsprechungen in VdS 3473

In der VdS Richtlinie wird in Abschnitt 6 eine Informationssicherheitsrichtlinie gefordert. In dieser müssen bedarfsgerecht Regelungen für die jeweilige Institution getroffen werden. Neben Regelungen für Mitarbeiter müssen dort auch Regeln für Fremdpersonal getroffen werden. Diese Regelungen müssen den jeweiligen Mitarbeitern bekannt gemacht werden.

## Unterschiede

Die Anforderungen unterscheiden sich nicht.

<!-- page: 26 -->

## 4.5 ORP.4 - Identitäts- und Berechtigungsmanagement

Mitarbeiter einer Institution dürfen nur auf Informationen und IT - Systeme zugreifen, wenn sie diese für ihre Arbeit benötigen. Außerdem muss sichergestellt sein, dass die Identität eines Mitarbeiters stets bekannt ist. Anforderungen, welche sich mit Regelungen für den Zugang zu Systemen und Informationen befassen, werden im Baustein ORP .4 behandelt.

## 4.5.1 ORP.4.A1 bis A3

Für das Anlegen von Benutzern und Benutzergruppen muss es eindeutige Regelungen geben. Das Anlegen von Benutzern und Gruppen darf nur mit gesonderten Administrationsrollen durchgeführt werden.

Die Berechtigungen, welche ein Nutzer hat, dürfen nur so weit gehen, wie es zur Erfüllung seiner Aufgaben nötig ist. Falls diese nicht mehr benötigt werden, müssen sie geändert werden. Rechte, welche weiter gehen als in der Institution üblich, müssen besonders begründet werden.

Die vergebenen Benutzerrechte müssen dokumentiert sein, die Dokumentation muss vor fremden Zugriff geschützt werden und regelmäßig auf Aktualität geprüft werden.

## Entsprechungen in VdS 3473

In Abschnitt 15.1 der VdS 3473 wird ein Verfahren gefordert, welches das Anlegen von Benutzern regelt. Im Wesentlichen werden dort analoge Anforderungen zu denen des BSI gestellt.

## Unterschiede

Die VdS verlangt nicht, dass Nutzer nur mit gesonderten Administrationsrollen angelegt werden dürfen. Im Wesentlichen sind die Anforderungen jedoch erfüllt.

## 4.5.2 ORP.4.A4

In dieser Anforderung wird das Prinzip der Funktionstrennung auf den IT-Einsatz übertragen. Relevante Aufgaben und Funktionen im Bereich des IT-Einsatzes müssen definiert werden. Sollten diese nicht miteinander vereinbar sein, müssen sie getrennt werden.

## Entsprechungen in VdS 3473

Die VdS regelt die Einhaltung der Funktionstrennung in Abschnitt 4.1.2. Ähnlich wie beim BSI müssen entgegenstehende Aufgaben von verschiedenen Personen wahrgenommen werden.

<!-- page: 27 -->

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 4.5.3 ORP.4.A5 bis A7

In diesen 3 Anforderungen wird verlangt, dass geregelt werden muss, welche Zutrittsberechtigungen (zu Räumen), Zugangsberechtigungen (zu IT-Systemen) und Zugriffsberechtigungen (zu Informationen) an welche Personen vergeben werden, bzw. diesen entzogen werden. Falls z.B. Chipkarten verwendet werden, muss deren Ausgabe/Einzug dokumentiert werden.

## Entsprechungen in VdS 3473

Die Vergabe von Zugangs- und Zugriffsrechten wird in Abschnitt 15.1 der VdS 3473 geregelt. Die dortigen Anforderungen sehen ebenfalls eine Dokumentation vor.

## Unterschiede

Die VdS regelt nicht den Zutritt zu Räumen und verzichtet auf explizite Angaben zu Zugangssystemen (z.B. Chipkarten).

## 4.5.4 ORP.4.A8 und A9

Die 8. Anforderung dieses Bausteins regelt den Umgang mit Passwörtern in einer Institution. Das BSI sieht vor, dass verbindlich geregelt wird, welche Passwörter als sicher gelten, dass diese geheim gehalten werden müssen und dass Standardzugänge zu ändern sind.

## Entsprechungen in VdS 3473

In Punkt 10.3.7 der VdS Richtlinie wird auf die Authentifizierung von Anwendern eingegangen. Dort wird verlangt, dass keine 'trivialen' Verfahren zur Identifikation von Nutzern angewendet werden. In Abschnitt 10.2.1 wird ebenfalls das deaktivieren von Standardzugängen gefordert.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

<!-- page: 28 -->

## 4.6 ORP.5 - Compliance Management

Der Baustein ORP .5 soll dabei helfen aus der Menge von Gesetzen, Verträgen, Richtlinien und internen Vorgaben Anforderungen die an Informationssicherheit abzuleiten.

## 4.6.1 ORP.5.A1

In einem Unternehmen muss eine Dokumentation existieren, aus welcher alle für die Informationssicherheit relevanten Vorgaben hervorgehen. Diese Vorgaben können z.B. durch Gesetze oder Verträge begründet sein. Die Dokumentation muss stets aktuell gehalten werden. Die ermittelten Anforderungen müssen bei der Planung aller Geschäftsprozesse berücksichtigt werden.

## Entsprechungen in VdS 3473

Die VdS sieht eine Anforderung, welche der des BSI entspricht, in der Basisabsicherung nicht vor. In Abschnitt 6.1 wird eine äquivalente Anforderung nur als 'SOLLTE'- Anforderung definiert.

## 4.6.2 ORP.5.A2

Führungskräfte, welche die Institution rechtlich vertreten, sind für die Einhaltung von rechtlichen Vorgaben verantwortlich. Die Verantwortlichkeiten müssen klar geregelt sein. Es müssen Maßnahmen definiert werden, welche Verstöße zu vermeiden helfen. Sollte es dennoch zu Verstößen kommen muss sachgerechte Abhilfe geschaffen werden.

## Entsprechungen in VdS 3473

Die Leitungsebene ist nach Punkt 4.2.5 dafür verantwortlich, dass Informationssicherheit in alle Bereiche der Institution eingebracht wird.

## Unterschiede

Die VdS regelt nicht explizit die Verantwortlichkeit für das Einhalten von rechtlichen Vorgaben. Dafür gibt es nur die o.g. implizite Regelung. Entsprechend ist auch kein Vorgehen bei Verstößen geregelt.

## 4.6.3 ORP.5.A3

Mitarbeiter müssen den rechtlichen Rahmen ihrer Tätigkeit kennen. Außerdem müssen ihnen alle relevanten rechtlichen Vorgaben bekannt gemacht werden.

<!-- page: 29 -->

## Entsprechungen in VdS 3473

Es gibt keine unmittelbare Entsprechung in den Regeln der VdS Richtlinie.

## 4.7 Fazit

Die 25 Anforderungen dieser Gruppe werden zum größten Teil (17 Anforderungen) von VdS 3473 erfüllt. Nur 8 Anforderungen werden nicht oder nur teilweise erfüllt. Auffällig ist, dass die Unterschiede in diesem Bereich meistens absolut sind: Eine Anforderung ist entweder erfüllt oder nicht. Von den 8 unzureichend erfüllten Anforderungen sind 7 gar nicht erfüllt, nur eine ist teilweise erfüllt. Die meisten Unterschiede betreffen den physikalischen Zutritt zu Räumen und die Einhaltung rechtlicher Vorgaben. In diesen Bereichen sind die Anforderungen des IT-Grundschutzes deutlich umfangreicher als jene der VdS.

<!-- page: 30 -->



<!-- page: 31 -->

## Kapitel 5

## CON - Konzeption und Vorgehensweise

## 5.1 Übersicht

Die CON-Reihe regelt den Aufbau von Konzepten zum Umgang mit Daten. Dabei wird neben Themen wie Kryptographie und Datenschutz auch das Entwickeln von individuellen Fachanwendungen berücksichtigt. Insgesamt umfasst die Gruppe 7 Bausteine.

## 5.2 CON.1 - Kryptokonzept

Im ersten Baustein dieser Gruppe geht es um ein einheitliches Konzept zur Anwendung von Kryptographie für eine Institution.

## 5.2.1 CON.1.A1

In der ersten Anforderung wird der Einsatz von geeigneten und ausreichend geprüften Kryptographiealgorithmen vorausgesetzt. Die gewählten Algorithmen dürfen keine Sicherheitslücken enthalten. Die Länge der Schlüssel muss aktuellen Empfehlungen folgen.

## Entsprechungen in VdS 3473

Die Abschnitte 6.3.3 und 6.4.3 fordern, dass Nutzer und externe Dienstleister nicht eigenmächtig auf Verschlüsselung zurückgreifen. Nur ein vom Unternehmen gewähltes Verfahren ist zu gestatten.

<!-- page: 32 -->

## Unterschiede

Es gibt keine expliziten Anforderungen an kryptographische Verfahren. Die Vorgaben des IT-Grundschutzes sind deutlich umfangreicher und werden von VdS 3473 nicht erfüllt.

## 5.2.2 CON.1.A2

Auf kryptographische Schlüssel in Datensicherungen dürfen Unbefugte keinen Zugriff haben. Schlüssel, welche über einen langen Zeitraum hinweg eingesetzt werden, dürfen nicht in regulären IT -Systemen gespeichert werden. Auch nach längerer Zeit muss noch auf verschlüsselte Daten zugegriffen werden können.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der VdS-Richtlinie.

## 5.3 CON.2 - Datenschutz

Der Baustein CON.2 verbindet den Datenschutz mit der Informationssicherheit. 'Datenschutz' bezieht sich dabei auf den rechtlichen Datenschutz im Sinne des Bundesdatenschutzgesetzes. Der Baustein hat in der Basisabsicherung nur eine einzige Anforderung.

## 5.3.1 CON.2.A1

In der einzigen Anforderung, die der Baustein an die Basisabsicherung stellt, wird gefordert, dass eine Institution prüfen muss, ob sie das 'Standard-Datenschutzmodell' anwenden sollte. Falls sich gegen die Anwendung entschieden wird muss dies begründet werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der VdS Richtlinie.

## 5.4 CON.3 - Datensicherheit

In CON.3 geht es um die Datensicherheit. 'Datensicherheit' bedeutet hier, den Verlust von Daten zu vermeiden.

Methodik: Abweichend von der üblichen Arbeitsweise werde ich in diesem Kapitel zunächst alle Anforderungen des BSI zusammen fassen. Danach wird auf (mögliche) Entsprechungen bzw. Unterschiede in der VdS 3474 eingegangen.

<!-- page: 33 -->

## 5.4.1 CON.3.A1

Zunächst muss ein Unternehmen ermitteln welche Systeme und Anwendungen in welchem Umfang Änderungen an ihren Daten vornehmen. Außerdem muss erkannt werden, welchen Stellenwert z.B. die Verfügbarkeit und die Integrität der Daten hat.

Die Ergebnisse müssen dokumentiert und beim Datensicherungskonzept berücksichtigt werden.

## 5.4.2 CON.3.A2

Für alle IT -Systeme und Datenarten muss festgelegt werden, wie oft und zu welchen Zeitpunkten Sicherungen der Daten vorgenommen werden. Dazu gehört auch auf welchen Medien die Sicherung erfolgt, wie die Daten transportiert werden und wie die Aufbewahrung der Daten geregelt ist. Die jeweiligen Verantwortlichkeiten müssen dokumentiert werden.

## 5.4.3 CON.3.A3

Falls es rechtliche Anforderungen an die Datensicherung gibt, müssen diese berücksichtigt werden.

## 5.4.4 CON.3.A4

Die Institution muss festlegen welche Anforderungen sie mindestens an eine Datensicherung stellt. Das 'Mindestdatensicherungskonzept' muss dabei auch auf Wiederherstellung sowie eingesetzte Hard- und Software eingehen.

## 5.4.5 CON.3.A5

Datensicherungen müssen regelmäßig durchgeführt werden. Die Sicherungen müssen mindestens die Daten umfassen, die nicht auf anderem Wege wiederbeschafft werden könnten. Sicherungen müssen vor ungewolltem Zugriff geschützt werden und regelmäßig getestet werden.

## Entsprechungen in VdS 3473

Die VdS regelt die Datensicherung in Kapitel 16 ihrer Richtlinie. In den 'SOLLTE'-Anforderungen verweist sie dabei auf 'anerkannte Standards', unter anderem den IT-Grundschutz des BSI. Im Falle einer Standard-Absicherung ('SOLLTE' wird erfüllt) wären die Anforderungen an die Datensicherheit also identisch, wenn das Vorgehen nach IT-Grundschutz gewählt wird.

<!-- page: 34 -->

In der Basis-Absicherung (nur 'MUSS' wird erfüllt), muss ein Verfahren entwickelt werden, aus dem hervorgeht, dass gesicherte Daten geschützt (vor unerlaubter Einsichtnahme, Verlust, Beschädigung) transportiert und aufbewahrt werden müssen. Außerdem muss sichergestellt sein, dass gesicherte Daten in einem anderen Brandabschnitt gelagert werden als die Systeme, von denen sie stammen. Bei der Archivierung von Daten müssen rechtliche Vorgaben berücksichtigt werden.

Daten müssen so gesichert werden, dass der letzte wiederherstellbare Zustand nicht älter als 24 Stunden ist. Sicherungen müssen nach jeder Änderung im Sicherungsverfahren und einmal im Jahr getestet werden. Die Datensicherung muss auch die Steuersoftware von aktiven Netzkomponenten umfassen.

## Unterschiede

Auch in der Basisabsicherung sind die konzeptionellen Vorgaben des BSI und der VdS sehr ähnlich. Es werden ähnliche Rahmenbedingungen berücksichtigt und vergleichbare Vorgaben gemacht. Einen erheblichen Unterschied gibt es nur bei Anforderung 4: für diese gibt es keine Entsprechung in VdS 3473.

## 5.5 CON.4 - Auswahl und Einsatz von Standardsoftware

Dieser Baustein soll dabei helfen Standardsoftware auf sicherem Wege zu beschaffen und deren Einsatz zu Planen. Das Ziel liegt dabei darin die Informationen, die mit der gewählten Software verarbeitet werden, zu schützen.

## 5.5.1 CON.4.A1 und A2

Bei der Installation von Software muss sichergestellt werden, dass diese unverändert ist. Nur berechtigte Mitarbeiter dürfen Zugang zu Installationsprogrammen haben. Die Programme zur Installation müssen auf schädliche Software geprüft werden.

Für die Installation der gewählten Standardsoftware muss es Anweisungen geben. Dabei sind gewählte Konfigurationsparameter zu berücksichtigen.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der Richtlinie der VdS.

## 5.5.2 CON.4.A3

Die Anweisungen für die Installation von Software müssen umgesetzt werden. Abweichungen davon müssen genehmigt werden. Installationen müssen vom IT-Betrieb durchgeführt werden. Es dürfen nur notwendige Programme installiert werden. Bei der Konfiguration von Software sind die Sicherheitsrichtlinien zu berücksichtigen. Nicht benötigte Anwendungen müssen deinstalliert oder abgeschaltet werden.

<!-- page: 35 -->

## Entsprechungen in VdS 3473

Es gibt keinen Abschnitt in der VdS Richtlinie welche sich mit der Installation von Software beschäftigt.

## 5.6 CON.5 - Entwicklung und Einsatz von Fachanwendungen

Oft müssen in einer Institution komplexe Anwendungen betrieben werden, welche besonders auf einen Fachbereich zugeschnitten sind. Die dabei zu berücksichtigen Sicherheitsanforderungen sind im Baustein CON.5 genannt.

## 5.6.1 CON.5.A1

Bei Fachanwendungen müssen notwendige Sicherheitsfunktionen berücksichtigt werden. Diese müssen sich an den Daten orientieren, die mit der Anwendung verarbeitet werden. Sicherheitsfunktionen müssen dokumentiert werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der Richtlinie der VdS.

## 5.6.2 CON.5.A2

Bei wesentlichen Änderungen an einer Software oder dem Einsatz einer neuen Software muss ein Test- und Freigabeverfahren existieren. Das Verfahren muss verschiedene Ebenen, wie z.B. die fachliche Ebene, die Informationssicherheitsebene oder den Bereich Datenschutz, berücksichtigen.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der Richtlinie der VdS.

## 5.6.3 CON.5.A3

Für Fachanwendungen muss es eine Installationsanweisung geben. Diese muss umgesetzt werden. Bei Änderungen an der Software muss die Anweisung aktualisiert werden.

<!-- page: 36 -->

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der Richtlinie der VdS.

## 5.6.4 CON.5.A4

Mitarbeitern muss die Nutzung einer Anwendung erläutert werden, dabei müssen Sicherheitsfunktionen berücksichtigt werden.

## Entsprechungen in VdS 3473

Die VdS nennt in Abschnitt 8 Anforderungen an die Schulung von Mitarbeitern. Dabei wird wird der Schwerpunkt auf Informationssicherheit gelegt, weniger auf das Anwenden einer Software. Sofern bei der Sensibilisierung der Mitarbeiter auch die Sicherheitsfunktionen der benutzten Anwendungen behandelt werden, sind die Anforderungen vergleichbar.

## 5.6.5 CON.5.A5

Nur berechtigte Nutzer dürfen Zugang zu Fachanwendungen haben. Protokolle müssen regelmäßig geprüft und den Vorgaben entsprechend gespeichert werden. Mit Herstellern von Anwendungen müssen Verträge vereinbart werden, die beinhalten, dass Sicherheitsupdates zeitnah zur Verfügung gestellt werden. Updates müssen im Vorfeld getestet werden.

## Entsprechungen in VdS 3473

In Abschnitt 10 werden Regeln für IT-Systeme genannt. Unter anderem müssen Sicherheitsupdates getestet und und zeitnah eingespielt werden. Protokolle sind, falls nicht anders vorgeschrieben, mindestens 6 Monate aufzubewahren. In Kapitel 15 wird außerdem festgelegt, dass Mitarbeiter nur die Zugriffsrechte haben dürfen, die sie für ihre Arbeit benötigen.

## Unterschiede

Die Bereitstellung von Sicherheitsupdates muss laut IT-Grundschutz vertraglich mit dem Hersteller vereinbart werden. VdS 3473 sieht eine solche Vereinbarung nicht vor. Diese Anforderung ist jedoch besonders wichtig, falls Software langfristig eingesetzt werden soll.

<!-- page: 37 -->

## 5.7 CON.6 - Löschen und Vernichten

Daten müssen in vielen Fällen nicht nur sicher gespeichert werden, auch die sichere Vernichtung von vertraulichen Daten kann von großer Bedeutung sein. Vorgaben wie das sichere löschen von Daten in einem Unternehmen geregelt werden kann macht der Baustein CON.6.

## 5.7.1 CON.6.A1

Das Löschen und Vernichten von Informationen muss geregelt sein. Je nach Organisationseinheit kann es dafür andere Voraussetzungen geben, die berücksichtigt werden müssen. Der Standort von Entsorgungsanlagen muss festgelegt werden.

Die Verantwortlichkeiten und Kommunikationswege müssen bereits frühzeitig festgelegt werden, auch für externen Dienstleistern.

## Entsprechungen in VdS 3473

Die VdS legt fest, dass bei der Ausmusterung eines IT-Systems, gespeicherte Daten sicher entfernt werden müssen (10.2.2).

## Unterschiede

Das BSI macht umfangreiche Vorgaben für das Vernichten von Informationen. In der Richtlinie der VdS gibt es jedoch keine konkreten Angaben zum Löschen von Informationen.

## 5.7.2 CON.6.A2

Vertrauliche Informationen müssen sicher entsorgt werden. Für diesen Zweck muss es gesicherte Entsorgungseinrichtungen geben. Zu den Einrichtungen dürfen nur berechtigte Personen Zugang haben. Beim Einsatz externer Dienstleister muss der Entsorgungsvorgang nachvollziehbar sein.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der Richtlinie der VdS.

## 5.8 CON.7 - Informationssicherheit auf Auslandsreisen

Der Baustein gibt Anforderungen vor, welche erfüllt sein müssen, wenn Informationen auf Auslandsreisen mitgenommen werden.

<!-- page: 38 -->

## 5.8.1 CON.7.A1

Es muss eine Sicherheitsrichtlinie geben, welche sich mit den Anforderungen und Maßnahmen auf Auslandsreisen beschäftigt. Dabei müssen tragbare IT-Systeme berücksichtigt werden. Die erarbeiteten Maßnahmen müssen entsprechenden Mitarbeitern bekannt gegeben werden.

## Entsprechungen in VdS 3473

Die VdS legt in Kapitel 6 fest, dass die Sicherheitsrichtlinie einer Einrichtung bei Bedarf angepasst werden muss. Dies ist für den Fall 'Auslandsreise' denkbar. In Abschnitt 8.2.1 wird gefordert, dass Mitarbeiter zielgruppenorientiert geschult werden müssen.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen des BSI und denen der VdS.

## 5.8.2 CON.7.A2

Anwender müssen im Umgang mit IT-Systemen geschult werden und in der Lage sein sich bei Auffälligkeiten geeignete Beratung zu suchen. Mitarbeiter sollen angehalten werden Verlust und Diebstahl zu vermeiden.

## Entsprechungen in VdS 3473

In Abschnitt 8.2.1 wird gefordert, dass Mitarbeiter zielgruppenorientiert geschult werden müssen.

## Unterschiede

Sofern Mitarbeiter, die ins Ausland vereisen, gesondert auf die dabei auftretenden Gefahren hingewiesen werden, ist die Anforderung der VdS mit der Anforderung des BSI vergleichbar.

## 5.8.3 CON.7.A3

Vor einer Auslandsreise müssen die rechtlichen Rahmenbedingungen im Zielland geprüft werden. Diese müssen dem Mitarbeiter so vermittelt werden, dass ein ausreichender Schutz für unternehmensbezogene Daten gegeben ist. Außerdem sollen die klimatischen Bedingungen geprüft werden. Nötige Schutzmaßnahmen für Mitarbeiter und Technik müssen ermittelt werden.

<!-- page: 39 -->

## Entsprechungen in VdS 3473

Neben der in Anforderung 2 genannten Schulungspflicht gibt es keine weiteren Entsprechungen in VdS 3474.

## Unterschiede

Die VdS verzichtet darauf explizite Anforderungen an Maßnahmen auf Auslandsreisen zu stellen. Es werden keine technischen und keine auf den Mitarbeiter bezogenen Schutzmaßnahmen gefordert.

## 5.8.4 CON.7.A4 bis A8

Bei der Arbeit mit mobilen Geräten muss auf ausreichenden Sichtschutz geachtet werden. Eine Schutzfolie muss den gesamten Bildschirm des Gerätes bedecken.

Geräte müssen mit einer Bildschirmsperre ausgestattet sein. Der Verlust eines IT-Systems oder Datenträgers muss zeitnah gemeldet werden. Die Meldewege müssen festgelegt werden.

Der entfernte Zugang zu internen Netzen der Institution muss ausreichend gesichert und verschlüsselt sein. Nur berechtigte Nutzer dürfen Zugang dazu erhalten. Mobile IT-Systeme müssen über eine restriktiv eingestellte Firewall verfügen.

Bei der Verwendung von öffentlichen WLANs muss ein VPN verwendet werden.

## Entsprechungen in VdS 3473

In Abschnitt 11.4.3 legt die VdS fest, dass der entfernte Zugriff auf interne Daten gesichert werden muss. Der Nutzer darf nur Zugang zu Systemen haben, die er auch benötigt. Abschnitt 10.4.3 regelt den Verlust von IT-Systemen. Der Zugang zu IT-Systemen muss gem. 19.3.7 durch geeignete Anmeldeverfahren gesichert sein.

## Unterschiede

Die VdS macht keine Vorgaben zur Verwendung von Sichtschutzfolien. Die weiteren Anforderungen des BSI werden jedoch durch VdS 3473 erfüllt.

## 5.8.5 CON.7.A9

Mobile Datenträger müssen auf Schadsoftware geprüft werden. Bei der Weitergabe von Datenträgern muss sichergestellt werden, dass keine vertrauliche Daten drauf enthalten sind. Nach Verwendung und vor Weitergabe eines Datenträgers, muss dieser mit einem festgelegten Verfahren überschrieben werden.

<!-- page: 40 -->

## Entsprechungen in VdS 3473

Die VdS legt fest, dass Mitarbeiter die Gefahren mobiler Datenträger kennen und entsprechende Gegenmaßnahmen ergreifen. Die Weitergabe von Datenträgern an unberechtigte wird untersagt. Diese Anforderungen werden in Abschnitt 12.1 der VdS 3473 genannt.

## Unterschiede

Es gibt keine nennenswerten Unterschiede im Sicherheitsniveau der Anforderungen.

## 5.8.6 CON.7.A10

Vertrauliche Informationen müssen vor Beginn einer Reise den Richtlinien der Institution entsprechend geschützt werden.

## Entsprechungen in VdS 3473

Es gibt keine explizite Entsprechung für mobile Datenträger auf Reisen. Jedoch wird in Punkt 12.1.1 und 12.1.2 allgemein gefordert, dass geregelt werden muss welche Informationen auf mobilen Datenträgern gespeichert werden dürfen und das die Informationen entsprechend geschützt werden müssen.

## Unterschiede

Es gibt keinen Unterschied im Sicherheitsniveau.

## 5.8.7 CON.7.A11

Diese Anforderung enthält nur 'SOLLTE' Anforderungen. Sie wird deshalb im Rahmen der Basisabsicherung nicht betrachtet.

## 5.8.8 CON.7.A12

Vertrauliche Informationen dürfen im Ausland nicht öffentlich entsorgt werden. Ist eine angemessene Entsorgung nicht möglich, muss die entsprechende Information einbehalten werden und nach der Rückreise vernichtet werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

<!-- page: 41 -->

## 5.9 Fazit

In der CON-Gruppe findet sich eine große Zahl von Anforderungen, die nicht von VdS 3473 erfüllt werden. Von 29 Anforderungen werden nur 13 erfüllt. 2 weitere werden zum Teil erfüllt. Ganze 14 Anforderungen werden nicht erfüllt.

Der größte Teil nicht erfüllter Anforderungen findet sich in den Bausteinen CON.4 und CON.5. Die VdS macht in ihrer Richtlinie keine Vorgaben zu Software, was auch noch beim Vergleich von anderen Bausteinen zu beobachten ist. Der Bereich Kryptographie wird von der VdS quasi gar nicht behandelt. Die Anforderungen des IT-Grundschutzes sind im Bereich 'Konzepte' erheblich umfangreicher als die Vorgaben der VdS.

<!-- page: 42 -->

36 KAPITEL 5. CON - KONZEPTION UND VORGEHENSWEISE

<!-- page: 43 -->

## Kapitel 6

## OPS - Betrieb

## 6.1 Übersicht

In der Gruppe 'OPS' befinden sich die Bausteine, welche sich mit dem Betrieb von IT-Systemen beschäftigen. Der Schwerpunkt wird dabei auf Anforderungen an den administrativen Betrieb gelegt. Entsprechend befassen sich 8 der 11 Bausteine in der OPS-Gruppe mit diesem Thema.

## 6.2 OPS.1.1.2 - Ordnungsgemäße IT-Administration

OPS.1.1.2 ist der erste Baustein in der Gruppe und regelt grundsätzliche Anforderungen an die Administration von IT-Systemen, etwa die Auswahl des entsprechenden Personals oder Vertretungsregelungen.

## 6.2.1 OPS.1.1.2.A1

Die erste Anforderung dieses Bausteins beschäftigt sich mit dem zur Administration eingesetzten Personal. Dieses muss alle Qualifikationen haben, die zur Erfüllung der administrativen Aufgaben erforderlich sind. Das Personal und die entsprechenden Vertreter müssen ausreichend Zeit für Fortbildungen haben.

Administratoren müssen, neben Kenntnissen in der Sprache, in der Dokumentationen im Unternehmen verfasst werden, gute Kenntnisse in Englisch haben.

Eine Person darf nicht zwei Rollen mit widersprechenden Interessen erfüllen. Ein Administrator darf also nicht mit seiner eigenen Kontrolle beauftragt sein.

Die Anforderungen gelten auch wenn die Aufgaben an einen Dritten ausgelagert werden.

<!-- page: 44 -->

## Entsprechungen in VdS 3473

Analog zu den Anforderungen des BSI wird in Punkt 7.1 von der VdS gefordert, dass das Personal über die notwendigen Qualifikationen verfügt.

In Punkt 8 wird gefordert, dass zumindest auf Informationssicherheit bezogen, regelmäßig das Wissen der Mitarbeiter gefördert wird.

Die vom BSI geforderte Funktionstrennung findet sich bei der VdS in Punkt 4.1.2. Gemäß Punkt 4.10 gelten die Anforderungen auch für externe Dienstleister.

## Unterschiede

Die Anforderungen des BSI sind deutlicher als die der VdS. Es finden sich z.B. keine direkten Aussagen zu den Sprachfähigkeiten eines Administrators in VdS 3473. Da man notwendige Sprachkenntnisse jedoch als Anforderung gem. Punkt 7.1 ansehen kann, sollte das Fehlen dieser expliziten Anforderungen das Sicherheitsniveau nicht beeinflussen.

Anders ist die fehlende Anforderung zu Vertretern von Administratoren in VdS 3473 zu bewerten. Eine nicht geregelte Vertretung kann die Sicherheit negativ beeinflussen.

## 6.2.2 OPS.1.1.2.A2

Für Mitarbeiter mit administrativen Aufgaben muss es benannte Vertretungen geben. Diese müssen Zugriff auf die Systeme haben, die sie in Vertretung betreuen müssen.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in der Richtlinie.

## Unterschiede

Im Gegensatz zur Anforderung des IT-Grundschutzes, wird in Punkt 4.6 von VdS 3473 gefordert, dass '[. . . ] Verantwortlichkeiten eines Administrators [...] mindestens einem Mitarbeiter zugewiesen werden' [9, S. 13].

In dieser Form lässt die Anforderung also zu, dass es nur einen einzigen Administrator gibt, für welchen dann kein Ersatz besteht.

## 6.2.3 OPS.1.1.2.A3

Administratoren müssen nach ihrer Einstellung in die Systeme eingewiesen werden, die sie betreuen sollen. Ihnen müssen auch alle relevanten Sicherheitsvorgaben bekannt gemacht werden und sie müssen auf die Einhaltung relevanter Gesetze hingewiesen werden.

<!-- page: 45 -->

## Entsprechungen in VdS 3473

In den Punkten 7.1 und 7.2 regelt die VdS die Einstellung von Personal. Insbesondere in Punkt 7.2 wird gefordert, dass den Mitarbeitern Sicherheitsverfahren bekannt gemacht werden.

## Unterschiede

Die VdS verzichtet darauf, dass Administratoren explizit darauf hingewiesen werden, dass sie sich an Gesetzte halten müssen. Die Anforderung ist auf Seite von der VdS 3473 nicht so weitreichend wie die Vorgaben des BSI.

## 6.2.4 OPS.1.1.2.A4

Wenn ein Administrator nicht länger in seiner Funktion bei der Organisation beschäftigt ist, müssen alle ihm bekannten Zugangsdaten geändert werden. Außerdem müssen Dritte und eigene Mitarbeiter darüber informiert werden, dass sich ihr Ansprechpartner für die Aufgaben des ehemaligen Mitarbeiters geändert hat.

Die Anforderungen gelten auch für Mitarbeiter externer Dienstleister.

## Entsprechungen in VdS 3473

In Punkt 7.3. der VdS 3473 werden analoge Anforderungen aufgeführt. In Verbindung mit Punkt 4.10 gelten diese Anforderungen auch für Mitarbeiter externer Dienstleister.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 6.2.5 OPS.1.1.2.A5

Administratoren müssen für Ihre Aufgaben gesonderte administrative Zugänge haben, die nur so weit gehen, wie es ihre Aufgaben erfordern.

Mit diesen Zugängen dürfen lediglich Aufgaben ausgeführt werden, welche ohne administrative Rechte nicht erfüllbar sind. Alle anderen Tätigkeiten müssen mit regulären, persönlichen Zugängen durchgeführt werden.

<!-- page: 46 -->

## Entsprechungen in VdS 3473

In Punkt 15.1.2 wird festgelegt, dass ein administrativer Zugang nur dann vergeben wird, wenn dieser zur Erfüllung von Aufgaben benötigt wird. Außerdem wird im gleichen Abschnitt bestimmt, dass Zugänge nur so weit gehen dürfen wie es zur Erfüllung der Aufgaben notwendig ist.

## Unterschiede

Die VdS legt nicht fest, dass administrative Zugänge nur für die Aufgaben eingesetzt werden dürfen, für die sie erforderlich sind. Das Durchführen von regulären Aufgaben mit Administratorkonten wäre also möglich. Dadurch wird das Sicherheitsniveau negativ beeinflusst.

## 6.2.6 OPS.1.1.2.A6

Administratorzugänge müssen sicher authentifiziert werden. Die ggf. verwendeten Passwörter dürfen nicht in anderen Teilen der IT-Infrastruktur verwendet werden. Der entfernte, administrative Zugriff auf ein System muss mit sicheren Protokollen erfolgen. Anmeldungen auf IT-Systemen müssen protokolliert werden.

## Entsprechungen in VdS 3473

Die VdS fordert in Punkt 10.3.7, dass Zugänge geeignet authentifiziert werden. Anmeldungen müssen gem. Punkt 10.3.3 protokolliert werden.

## Unterschiede

In der VdS 3474 gibt es keine Regelungen für den administrativen Fernzugriff auf Systeme. Es gibt zwar eine allgemeine Vorgabe für Fernzugriffe (Punkt 11.4.3), diese bezieht sich jedoch nur auf den Zugriff aus fremden Netzen.

## 6.3 OPS.1.1.3 - Patch-und Änderungsmanagement

IT-Systeme müssen oft verändert werden. Dies kann z.B. durch das Aktualisieren ('patchen') einer Software passieren. Der Baustein OPS.1.1.3 beinhaltet Anforderungen um solche und ähnliche Änderungen sicher zu gestalten.

<!-- page: 47 -->

## 6.3.1 OPS.1.1.3.A1

Bei der Veränderung von IT-Systemen müssen Sicherheitsaspekte berücksichtigt werden. Änderungen müssen getestet und dokumentiert werden. Während der Durchführung einer Änderung muss es eine Rückfallebene für die betroffenen Systeme geben. Das Sicherheitsniveau darf während einer Veränderung nicht beeinträchtigt werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen.

## 6.3.2 OPS.1.1.3.A2

Alle Unternehmensbereiche müssen einen Verantwortlichen für das Änderungsmanagement haben. Die Verantwortlichkeiten müssen in Konzepten geplant sein. Die mit den Aufgaben beauftragten Mitarbeiter müssen in Begrifflichkeiten der Informationssicherheit, Kryptographie und des Patch- und Änderungsmanagements geschult sein.

## Entsprechungen in VdS 3473

In der Richtlinie der VdS gibt es keine Entsprechungen für die Anforderungen des BSI.

## 6.3.3 OPS.1.1.3.A3

Es muss geregelt werden ob und wie Auto-Update Funkionen sicher eingesetzt werden können.

## Entsprechungen in VdS 3473

Es gibt keine entsprechenden Anforderungen in der VdS 3473.

## 6.4 OPS.1.1.4 - Schutz vor Schadprogrammen

Ein wichtiger Bereich der Informationssicherheit ist der Schutz vor der Ausführung von ungewollten Programmen. Im 3. Baustein der OPS-Gruppe werden Anforderungen gestellt, welche der Gefahr von Schadprogrammen begegnen sollen.

## 6.4.1 OPS.1.1.4.A1

In der Organisation muss es ein Konzept geben, aus dem hervorgeht welche IT-Systeme vor Schadsoftware geschützt werden müssen und wie dieser Schutz umgesetzt werden muss.

<!-- page: 48 -->

## Entsprechungen in VdS 3473

In der VdS 3473 ist in Punkt 10.3.5 geregelt, dass alle IT-Systeme vor Schadsoftware geschützt werden müssen. Außerdem muss jedes System täglich und vollständig auf Schadsoftware untersucht werden.

## Unterschiede

Die Anforderungen der VdS liegen hier über denen des BSI. Während das BSI Systeme zulässt, welche nicht vor Schadsoftware geschützt werden, ist ein solcher Schutz bei der VdS unbedingt erforderlich.

## 6.4.2 OPS.1.1.4.A2

Sollten auf einem IT-System Schutzmechnismen gegen Schadsoftware existieren, etwa im Betriebssystem oder in anderer Software, müssen diese oder ein vergleichbarer Ersatz genutzt werden.

## Entsprechungen in VdS 3473

Die VdS verlangt explizit das Maßnahmen zum Schutz gegen Schadsoftware eingesetzt werden (siehe Entsprechungen zu OPS.1.1.4.A1).

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 6.4.3 OPS.1.1.4.A3 bis A5

Auf Endgeräten, Gateways und Systemen, die dem Austausch von Daten dienen, muss eine Software für den Schutz gegen Schadprogramme vorhanden sein. Diese muss aus dem Enterprise-Bereich kommen und über Herstellerunterstützung verfügen. Die Software muss geeignet konfiguriert werden.

Beim Einsatz von Onlinediensten müssen Sicherheits- und Geheimhaltungsaspekte berücksichtigt werden.

## Entsprechungen in VdS 3473

Ähnlich wie das BSI fordert die VdS den Einsatz von 'geeigneter Software' zur Abwehr von Schadprogrammen.

<!-- page: 49 -->

## Unterschiede

Das BSI stellt genauere Anforderungen an die zu verwendende Software, die bei der VdS nicht genannt werden. Die Anforderungen sind damit nur teilweise von VdS 3473 abgedeckt.

## 6.4.4 OPS.1.1.4.A6

Die Datenbanken der Programme zur Abwehr von Schadsoftware müssen den Empfehlungen des Herstellers entsprechend aktualisiert werden. Nach einem Update muss die Konfiguration überprüft werden.

## Entsprechungen in VdS 3473

Die VdS gibt in Punkt 10.3.5 ihrer Richtlinie an, dass eine Software zur Abwehr von Schadprogrammen täglich aktualisiert werden muss.

## Unterschiede

Die VdS fordert nicht dass die Konfiguration nach einem Update geprüft wird.

## 6.4.5 OPS.1.1.4.A7

Benutzer müssen regelmäßig über die Gefahren durch Schadprogramme informiert werden.

## Entsprechungen in VdS 3473

Die VdS fordert in Punkt 8.2, dass Mitarbeiter regelmäßig geschult werden. Entsprechend sind die Anforderungen des BSI und der VdS auf dem gleichen Sicherheitsniveau.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 6.5 OPS.1.1.5 - Protokollierung

Dieser Baustein macht Vorgaben zu Protokollierungen von sicherheitsrelevanten Ereignissen.

<!-- page: 50 -->

## 6.5.1 OPS.1.1.5.A1 und A2

Es muss eine eigene Sicherheitsrichtlinie geben, welche festlegt unter welchen Umständen und auf welche Weise ein Ereignis protokolliert werden soll.

Die Richtlinie muss vom ISB in Zusammenarbeit mit den jeweiligen Fachverantwortlichen erstellt und regelmäßig aktualisiert werden. Mitarbeiter, die mit der Protokollierung beauftragt sind, müssen die Richtlinie kennen.

Alle Punkte müssen dokumentiert werden. Für die Systeme, welche in der Richtlinie erfasst werden, muss es Verantwortliche geben. Die Verantwortlichen müssen die Einhaltung der Protokollrichtlinie sicherstellen.

## Entsprechungen in VdS 3473

Die VdS fordert nicht explizit, dass es eine Richtlinie zur Protokollierung geben muss. Das Speichern von Protokollen wird jedoch in Punkt 10.3.3 vorgeschrieben, somit sind die Anforderungen im Wesentlichen vergleichbar mit denen des BSI.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 6.5.2 OPS.1.1.5.A3

Alle Systeme müssen Sicherheitsrelevante Ereignisse protokollieren. Falls die in Anforderung (1) genannten Systeme über eine Funktion zur Protokollierung verfügen, muss diese genutzt werden. Dabei sind die Angaben von Herstellern zu berücksichtigen. Falls keine geeignete Funktion verfügbar ist, müssen weitere Systeme zur Protokollierung eingesetzt werden.

Ob die Protokollierung funktioniert muss in Stichproben regelmäßig geprüft werden, das Intervall muss in der Richtlinie gem. Anforderung (1) definiert werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der VdS 3473.

## 6.5.3 OPS.1.1.5.A4

Die Uhren von Systemen zur Protokollierung müssen synchron eingestellt sein.

## Entsprechungen in VdS 3473

In Punkt 10.3.3 wird als Anforderung festgelegt, dass Uhren synchron sein müssen.

<!-- page: 51 -->

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 6.6 OPS.1.1.6 - Software-Tests und -Freigaben

Der 5. Baustein in der OPS-Gruppe behandelt Anforderungen an Sicherheitsaspekte, welche bei der von einem Unternehmen eingesetzten Software berücksichtigt werden müssen. Dabei geht es insbesondere um das Testen einer Software und die Freigabe für den Gebrauch innerhalb des Unternehmens. 'Testen' bezieht sich dabei jedoch nicht auf die Tests, die man im Rahmen der Softwareentwicklung durchführt, sondern auf das Testen der Funktionen der Software.

In der Richtlinie der VdS gibt es keine Anforderungen an das Testen von Software. Aus diesem Grund verzichte ich in diesem Kapitel, abweichend von der üblichen Methodik, auf die Diskussion von Entsprechungen bzw. Unterschieden zur VdS 3473. Das Sicherheitsniveau der VdS 3473 liegt, dem zu Folge, unter dem des IT-Grundschutz-Kompendiums. Alle in diesem Baustein gemachten Anforderungen gelten als nicht erfüllt.

## 6.6.1 OPS.1.1.6.A1

Vor dem Testen einer Software müssen die nötigen Rahmenbedingungen geschaffen werden. Dabei müssen die jeweiligen Gegebenheiten in der Organisation berücksichtigt werden. Insbesondere müssen die ausgewählten Testfälle repräsentativ sein.

## 6.6.2 OPS.1.1.6.A12

Funktionale Softwaretests müssen durchgeführt werden und dürfen den Produktivbetrieb nicht stören.

## 6.6.3 OPS.1.1.6.A3

Die Ergebnisse von Softwaretest müssen dokumentiert und ausgewertet werden.

## 6.6.4 OPS.1.1.6.A4

Die jeweilige Organisationseinheit muss Software nach erfolgreichem Test freigeben und dies dokumentieren. Dabei ist die korrekte Durchführung der Tests zu berücksichtigen.

## 6.6.5 OPS.1.1.6.A5

Software muss auch nicht-funktional getestet werden.

<!-- page: 52 -->

## 6.7 OPS.1.2.2 - Archivierung

Um die Archivierung von Dokumenten langfristig und sicher zu gewährleisten gibt es die Anforderungen im Baustein OPS.1.2.2.

Auf Seiten der VdS gibt es ebenfalls ein eigenes Kapitel zur Archivierung und Sicherung von Daten. In Abschnitt 16 der VdS 3473 wird dabei sogar, in Form einer 'SOLLTE'- Anforderung, auf den IT-Grundschutz des BSI verwiesen.

Da sich diese Arbeit mit den Maßnahmen der Basissicherung beschäftigt ('MUSS'), kann dieser Punkt jedoch nicht berücksichtigt werden. Stattdessen werden die Anforderungen betrachtet, die im Kapitel 16 als Basismaßnahmen genannt werden.

## 6.7.1 OPS.1.2.2.A1

Zu Beginn der Planung der Archivierung müssen alle technischen, rechtlichen und organisatorischen Einflussfaktoren ermittelt und berücksichtigt werden.

## Entsprechungen in VdS 3473

In Punkt 16.2 der VdS 3473 wird als Anforderung definiert, dass ein Unternehmen prüfen muss, welche Daten archiviert werden müssen. Dabei werden u.a. rechtliche Aspekte berücksichtigt.

## Unterschiede

Die Anforderungen der VdS sind zwar nicht so weitreichend formuliert wie die des BSI, sie sind aber auf das Sicherheitsniveau bezogen vergleichbar.

## 6.7.2 OPS.1.2.2.A2

Die Ziele der Archivierung müssen in einem Konzept beschrieben werden. Das Konzept muss aktuell gehalten werden. Relevante Regelungen und Verantwortlichkeiten müssen berücksichtigt werden.

Das Management muss am Prozess beteiligt werden.

## Entsprechungen in VdS 3473

Punkt 16.3 der Richtlinie legt fest, dass ein Verfahren existieren muss, das eine Datenarchivierung beschreibt. Dabei müssen rechtliche Vorgaben beachtet werden.

Die regelmäßige Aktualisierung des Archivsystems ergibt sich aus Punkt 16.4.

Das Management muss gem. Punkt 4.2.5 die Informationssicherheit in allen Unternehmensteilen vorantreiben. Somit auch die Archivierung.

<!-- page: 53 -->

## Unterschiede

Das BSI legt, wie auch in Anforderung (1), einen größeren Wert auf allgemeinere Konzepte. Inhaltlich liegen die Anforderungen in beiden Werken aber nahe beieinander.

## 6.7.3 OPS.1.2.2.A3

Zu Archivsystemen dürfen nur berechtigte Personen Zugang haben. Die Medien, auf denen eine Archivierung durchgeführt wird, müssen geeignet aufbewahrt werden.

## Entsprechungen in VdS 3473

Punkt 16.3 von VdS 3473 stellt äquivalente Anforderungen an die Datenarchivierung.

## Unterschiede

Es gibt keine Unterschiede, die das Sicherheitsniveau beeinflussen.

## 6.7.4 OPS.1.2.2.A4

Daten im Archiv müssen auffindbar sein. Angaben zu einem Index müssen im Konzept erfasst werden.

## Entsprechungen in VdS 3473

Zur Auffindbarkeit von Daten wird auf Seite der VdS keine Anforderung gestellt.

## 6.7.5 OPS.1.2.2.A5

Die Daten, die im Archiv gespeichert werden, müssen weiterhin nutzbar sein. Das heißt Datenformat und genutzte Anwendungen müssen kompatibel sein, Zeitstempel und kryptographische Verfahren müssen dem Stand der Technik entsprechen.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der VdS 3473.

## 6.7.6 OPS.1.2.2.A6 bis A8

Die Datenbank mit dem Index des Archiv muss vor unberechtigten Veränderungen geschützt sein. Je nach Größe des Archivs muss es Sicherungen der Datenbank geben, diese müssen wiederherstellbar sein. Das Archiv selbst muss auch regelmäßig gesichert werden.

<!-- page: 54 -->

Zugriffe auf Archive müssen protokolliert werden.

## Entsprechungen in VdS 3473

In Punkt 10.3.3 legt die VdS fest, dass Zugriffe auf IT-Systeme protokolliert werden müssen. Dies gilt entsprechend auch für Archivsysteme.

Punkt 16.5.1 schreibt die Wiederherstellbarkeit der Archive vor. Punkt 16.3 den Schutz vor unberechtigter Veränderung.

## Unterschiede

Die VdS erwähnt nicht explizit welche Maßnahmen für den Index von Archiven durchgeführt werden müssen. Bezogen auf die Archive selbst sind die Anforderungen aber vergleichbar.

## 6.7.7 OPS.1.2.2.A9

Dokumente müssen in einem geeignetem Format gespeichert sein. Das Format muss die Eigenschaften des Dokuments auch nach langer Zeit originalgetreu wiedergeben.

## Entsprechungen in VdS 3473

Es gibt keine Angaben zu Datenformaten in VdS 3473.

## 6.8 OPS.1.2.3 - Informations- und Datenträgeraustausch

Dieser Baustein hat das Ziel den Austausch von Informationen, zwischen verschiedenen Personen und zwischen unterschiedlichen IT-Systemen, abzusichern.

## 6.8.1 OPS.1.2.3.A1

Innerhalb einer Organisation muss definiert werden welche Kommunikationspartner eine bestimmte Information austauschen dürfen.

## Entsprechungen in VdS 3473

Eine Vorgabe für den Austausch von Informationen im Allgemeinen gibt es nicht.

<!-- page: 55 -->

## 6.8.2 OPS.1.2.3.A2 und A3

Bei auszutauschenden Informationen muss bestimmt werden ob und wie diese bei der Übertagung zu schützen sind und mit wem sie geteilt werden dürfen. Mitarbeiter müssen entsprechend geschult werden.

## Entsprechungen in VdS 3473

In Abschnitt 9.2 wird verlangt, dass allgemein ermittelt wird, welche Informationen des Unternehmens besonders geschützt werden müssen.

Das Sensibilisieren von Mitarbeitern ist in Abschnitt 8.2 beschrieben.

## Unterschiede

Das BSI betrachtet in seinen Vorgaben besonders das Austauschen von Informationen. In der Richtlinie der VdS gibt es dazu keine allgemeinen Vorgaben, es wird nur auf die Übertragung von digitalen Informationen eingegangen. Die Anforderungen (2) und (3) des Bausteines werden durch die VdS 3473 nicht erfüllt.

## 6.8.3 OPS.1.2.3.A4

Digitale Informationen müssen sowohl vor, als auch nach dem Versenden auf Schadsoftware überprüft werden. Die dafür eingesetzte Software muss dem Stand der Technik entsprechen.

## Entsprechungen in VdS 3473

Abschnitt 12.1 verlangt, dass bei Einsatz mobiler Datenträger auch Maßnahmen zum Schutz vor Schadsoftware ergriffen werden.

## Unterschiede

Die VdS verlangt nicht explizit, dass Informationen vor und nach dem Versenden auf schädliche Software untersucht werden. Anders als das BSI, sieht die VdS nicht unbedingt vor, dass es einen Echtzeitschutz vor Schadsoftware geben muss. Dies ist in Punkt 10.3.5 lediglich als 'SOLLTE'-Bestimmung aufgeführt. Damit liegt das Sicherheitsniveau auf Seiten des BSI höher und die Anforderung wird nicht von VdS 3473 abgedeckt.

## 6.8.4 OPS.1.2.3.A5

Es muss einen Meldeweg für verlorengegangene Datenträger geben. Das Verlust eines Datenträgers ist umgehend zu melden.

<!-- page: 56 -->

## Entsprechungen in VdS 3473

Punkt 12.2.3 sieht vor, dass Nutzer den Verlust eines kritischen Datenträgers umgehend zu melden haben.

## Unterschiede

Die VdS beschränkt sich bei Verlustmeldungen auf 'kritische' Datenträger, also jene auf denen kritische Informationen gespeichert werden. 'Kritisch' ist eine Information gem. 9.2 genau dann wenn ihr Verlust, ihre Veränderung oder ihr bekannt werden zu 'katastrophalen' Schäden führen kann.

Es ist denkbar, dass der Verlust einer Information keine 'katastrophalen' Folgen für ein Unternehmen hat, aber dennoch schwerwiegend ist. Der Verlust solcher Datenträger muss jedoch nicht gemeldet werden. Die Anforderungen des BSI sehen dies jedoch vor und sind entsprechend höher als die der VdS. Die Anforderung ist somit nur zum Teil erfüllt.

## 6.9 OPS.1.2.4 - Telearbeit

Unter 'Telearbeit' versteht das BSI alle Tätigkeiten, die ausschließlich außerhalb der Räumlichkeiten eines Unternehmens stattfinden. Dabei kann es sich sowohl um die Arbeit von Zuhause aus handeln, als auch um Arbeiten, die vom Standort eines Kunden oder einer Nebenniederlassung aus erfolgen.

## 6.9.1 OPS.1.2.4.A1

Alle Aspekte der Telearbeit müssen geregelt werden. Die betroffenen Mitarbeiter sind über die relevanten Vorgaben zu informieren. Für jeden Telearbeiter muss es einen Vertreter geben.

## Entsprechungen in VdS 3473

Es gibt keine gesonderten Vorgaben für die Telearbeit.

## 6.9.2 OPS.1.2.4.A2

Alle Sicherheitsaspekte der Telearbeit müssen geregelt sein. Zugriffe auf interne Systeme der Organisation müssen auf die Bereiche beschränkt werden, die zur Erfüllung der Aufgaben erforderlich sind.

Für die Telearbeit eingesetzte Systeme dürfen nur für die vorgesehenen Arbeiten eingesetzt werden, alle anderen Zugriffe müssen blockiert werden.

<!-- page: 57 -->

## Entsprechungen in VdS 3473

Punkt 11.4.2.3 schreibt vor, dass bei Fernzugriffen auf Systeme des Unternehmens nur die unbedingt nötigen Zugriffe erlaubt sind. Punkt 10.3.7 schreibt vor, dass der Zugriff auf Systeme des Unternehmens vor unberechtigten Personen geschützt wird.

## Unterschiede

Es gibt keine wesentliche Unterschiede zwischen den Anforderungen.

## 6.9.3 OPS.1.2.4.A3

Die Verbindung von Tele-Systemen zu den internen Systemen einer Organisation muss gesichert erfolgen. Das bedeutet, dass Informationen bei der Übertragung vertraulich bleiben und nicht verändert werden.

## Entsprechungen in VdS 3473

Die VdS stellt äquivalente Anforderungen in Punkt 11.4.3.1 ihrer Richtlinie auf.

## Unterschiede

Die Anforderungen unterscheiden sich nicht.

## 6.9.4 OPS.1.2.4.A4

Die bei der Telearbeit verarbeiteten Daten müssen regelmäßig und geeignet gesichert werden. Für die Sicherung sollte der Telearbeiter möglichst wenige Arbeitsschritte unternehmen müssen.

## Entsprechungen in VdS 3473

Punkt 11.4.1.2 schreibt vor, dass die Verantwortung für die Datensicherheit definiert werden muss.

## Unterschiede

Die VdS macht keine konkreten Vorgaben zur Sicherung der Daten, nur die Verantwortung muss definiert werden. Auf Seiten des BSI gibt es darüber hinausgehend Anforderungen an die Umsetzung.

<!-- page: 58 -->

## 6.9.5 OPS.1.2.4.A5

Telearbeiter müssen auf die besonderen Gefahren im Bezug auf Informationssicherheit hingewiesen werden, die bei der Telearbeit auftreten können.

## Entsprechungen in VdS 3473

In Abschnitt 8.2 schreibt die VdS vor, dass Mitarbeiter zielgruppenorientiert über Gefahren aufgeklärt werden.

## Unterschiede

Es gibt keine Unterschiede in den Anforderungen, die das Sicherheitsniveau beeinflussen.

## 6.10 OPS.2.1 - Outsourcing für Kunden

Das Auslagern von Teilen der eigenen IT-Systeme ist bereits in vielen Organisationen üblich. Der Baustein OPS.2.1 regelt die dabei zu beachtenden Aspekte der Informationssicherheit. Im Bereich der Basisabsicherung gibt es dabei nur eine einzige Anforderung.

## 6.10.1 OPS.2.1.A1

Beide, an einem Outsourcing-Vorhaben beteiligten Parteien, müssen einen, mit dem IT-Grundschutz vergleichbaren, Standard zur Informationssicherheit umsetzen und dessen Einhaltung vertraglich vereinbaren. Outsourcing-Vorhaben müssen geplant werden, dabei sind Sicherheitsvorgaben zu beachten.

## Entsprechungen in VdS 3473

In Kapitel 14 der VdS-Richtlinie gibt es umfangreiche Vorgaben für ein Outsourcing. Analog zu den Anforderungen des BSI muss es eine umfangreiche Planung für das Outsourcing geben. Darüber hinaus muss der Dienstleister vertraglich verpflichtet werden die betrieblichen, gesetzlichen oder vertraglichen Sicherheitsanforderungen des auslagernden Unternehmens zu erfüllen.

Für Systeme, welche vom Unternehmen als 'kritisch' eingestuft werden, gibt es noch weitergehende Regelungen, wie z.B. das Überwachen der vereinbarten Leistung.

<!-- page: 59 -->

## Unterschiede

Die Anforderungen der VdS und des BSI sind, im Bereich der Basisabsicherung, vergleichbar.

## 6.11 OPS.2.4 - Fernwartung

Baustein OPS.2.4 definiert Anforderungen, welche die Sicherheit bei der Fernwartung von IT-Systemen gewährleisten sollen.

## 6.11.1 OPS.2.4.A1

Das Unternehmen muss definieren wie der Einsatz von Fernwartung zu erfolgen hat. Dabei sind die Protokolle, die verwendet werden sollen, zu berücksichtigen. Auch deren Absicherung und die Überprüfung der Sicherheit müssen festgelegt werden.

## Entsprechungen in VdS 3473

Eine Regelung für den Fernzugriff gibt es für externe Dienstleister in Punkt 6.4.3 der VdS 3473.

## Unterschiede

Die VdS macht keine allgemeinen Vorgaben für den Fernzugriff. Eine entsprechende Regel gibt es nur für externe Dienstleister, jedoch nicht für eigene Mitarbeiter. Die Anforderung ist somit nicht erfüllt.

## 6.11.2 OPS.2.4.A2

Eine Fernwartung muss immer durch die Organisation gestartet werden. Betroffene Nutzer müssen dem Vorgang zustimmen.

## Entsprechungen in VdS 3473

Es gibt keine äquivalenten Vorgaben.

## 6.11.3 OPS.2.4.A3 und A4

Zugänge für die Fernwartung dürfen nur für den vorgesehen Zweck verwendet werden. Verbindungen müssen nach Beendigung der Wartung getrennt werden. Notwendige Prots für die Fernwartung müssen ständig verfügbar sein.

<!-- page: 60 -->

Verbindungen für die Fernwartung müssen in den Firewall-Regelungen beachtet werden. Bestehende Regelungen dürfen dabei nicht umgangen werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der VdS 3474.

## 6.11.4 OPS.2.4.A5

Es muss geregelt werden ob Onlinedienste für die Fernwartung verwendet werden dürfen.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen.

## 6.12 OPS.3.1 - Outsourcing für Dienstleister

Parallel zum Baustein OPS.2.1 ('Outsourcing für Kunden') regelt der Baustein OPS.3.1 die Anforderungen, die an einen Dienstleister für Outsourcing gestellt werden. In der Basisabsicherung hat OPS.3.1 ebenfalls nur eine einzige Anforderung.

## 6.12.1 OPS.3.1.A1

Es muss ein grobes Konzept zur angebotenen Dienstleistung geben. Dabei müssen auch Anforderungen an das Sicherheitsniveau des Kunden berücksichtigt werden.

## Entsprechungen in VdS 3473

Es gibt keine Regelungen, die sich an Dienstleister für Outsourcing richten.

## Unterschiede

Der IT-Grundschutz richtet sich auch an größere Unternehmen und ist wesentlich Umfangreicher. Aus diesem Grund deckt er auch Bereiche für Outsourcing-Dienstleister ab. Da solche Unternehmen aber auch im Mittelstand zu finden sind, fehlt hier eine Anforderung in VdS 3473.

<!-- page: 61 -->

## 6.13 Fazit

Wie bereits bei der Bausteingruppe CON festgestellt wurde, zeigt sich auch in der OPS-Gruppe, dass VdS 3473 bei technischen Anforderungen, insbesondere im Bezug auf Software, erheblich zurückliegt.

Zu beobachten ist, dass die Unterschiede zwischen VdS 3473 und IT-Grundschutz hauptsächlich darauf zurückzuführen sind, dass bestimmte Bereiche in VdS 3473 nicht order nur indirekt thematisiert werden. So sind von den 51 Basisanforderungen in dieser Baustein-Gruppe nur 16 erfüllt. 10 werden mit deutlichen, negativen Abweichungen erfüllt. Ganze 25 Anforderungen fehlen völlig. Ein großer Teil dieser nicht erfüllten Anforderungen liegt im Bereich der Software-Tests und Fernwartung.

Hervorzuheben ist aber auch, dass es 2 Anforderungen (OPS.1.1.4.A1 und OPS.2.1.A1) seitens des IT-Grundschutzes gibt, die von VdS 3473, zumindest teilweise, übertroffen werden.

<!-- page: 62 -->



<!-- page: 63 -->

## Kapitel 7

## DER - Detektion und Reaktion

## 7.1 Übersicht

Die Bausteine der Gruppe DER behandeln das Erkennen von Sicherheitsvorfällen und die Reaktion auf erkannte Ereignisse. Die Gruppe besteht aus 7 Bausteinen.

Der Baustein 3.2 ('IS-Revision für Bundesbehörden') richtet sich dabei jedoch explizit an Behörden des Bundes. Da das Ziel dieser Arbeit ein Vergleich des Sicherheitsniveaus des IT-Grundschutzes mit der VdS 3473 im Bezug auf kleine und mittlere Unternehmen ist, wird dieser Baustein nicht diskutiert werden.

DER.4 ist ein Baustein, der keine Basis-Anforderungen enthält. Aus diesem Grund kann er im Rahmen dieser Arbeit ebenfalls nicht behandelt werden.

## 7.2 DER.1 - Detektion von sicherheitsrelevanten Ereignissen

Der erste Baustein in dieser Gruppe zeigt auf wie eine Organisation vorgehen muss, um sicherheitsrelevante Ereignisse zu erkennen.

## 7.2.1 DER.1.A1

Es muss eine gesonderte Richtlinie geben, welche regelt wie innerhalb der Organisation die Erkennung von Sicherheitsvorfällen organisiert ist. Die dafür zuständigen Mitarbeiter müssen die Richtlinie kennen.

Änderungen an der Richtlinie, sowie deren Einhaltung, müssen vom ISB überwacht und dokumentiert werden.

<!-- page: 64 -->

## Entsprechungen in VdS 3473

Abschnitt 18.1 in der VdS-Richtlinie schreibt vor, dass es eine zusätzliche Richtlinie geben muss, die den Umgang mit Sicherheitsereignissen regelt. Dabei wird u. a. festgelegt, dass jeder Mitarbeiter (potenzielle) Sicherheitsvorfälle an den ISB melden muss.

## Unterschiede

Die Richtlinie, die das BSI fordert, ist im Bezug auf das Erkennen von Ereignissen eher allgemein gehalten und lässt weitgehende Freiheiten bei der Umsetzung.

Im Gegensatz dazu ist die Richtlinie, welche von der VdS gefordert wird, auf den gesamten Bereich 'Sicherheitsvorfälle' bezogen und macht nur eine Vorgabe zur Erkennung von Vorfällen: 'Jeder Mitarbeiter meldet mögliche Sicherheitsvorfälle an den ISB'.

Es ist denkbar, dass eine Richtlinie, welche nach den Anforderungen des IT-Grundschutzes erstellt wurde, eine ähnliche Vorgabe macht. Bezogen auf das Sicherheitsniveau sind die Unterschiede zwischen den beiden Anforderungen damit nicht von Bedeutung.

## 7.2.2 DER.1.A2

Beim Einsatz von Systemen zur Detektion und beim Auswerten von Protokolldaten müssen alle relevanten Vorschriften, insbesondere jene des Datenschutzes, eingehalten werden.

## Entsprechungen in VdS 3473

In der VdS 3473 gibt es keinen Abschnitt, welcher den Anforderungen des BSI entspricht.

## 7.3 DER.2.1 - Behandlung von Sicherheitsvorfällen

## 7.3.1 Übersicht

Nachdem der erste Baustein dieser Gruppe die Erkennung von Sicherheitsvorfällen beschrieben hat, macht der zweite Baustein Vorgaben zur Reaktion auf erkannte Ereignisse.

## 7.3.2 DER.2.1.A1

Der Begriff 'Sicherheitsvorfall' muss definiert sein. Es muss eine enge Abgrenzung zu täglichen Störungen geben. Mitarbeiter müssen die Definition des Begriffes kennen.

<!-- page: 65 -->

## Entsprechungen in VdS 3473

In Abschnitt 18.1 wird vorgeschrieben, dass der Begriff 'Sicherheitsvorfall' in der Richtlinie für Sicherheitsereignisse definiert wird. Die relevanten Richtlinien müssen den Mitarbeitern bekannt gemacht werden.

## Unterschiede

Es gibt keine relevanten Unterschiede zwischen den Anforderungen.

## 7.3.3 DER.2.1.A2

Es muss eine Richtlinie zum Umgang mit Sicherheitsvorfällen geben. Darin muss bestimmt werden wie bei welcher Art von Vorfall zu verfahren ist. Die Richtlinie muss allen Mitarbeitern bekannt sein.

## Entsprechungen in VdS 3473

Abschnitt 18.3 von VdS 3473 beschreibt das Vorgehen bei einem Sicherheitsvorfall.

## Unterschiede

Die VdS verzichtet auf eine eigene Richtlinie, welche nur den Umgang mit erfolgten Ereignissen beschreibt. Das Vorgehen nach dem Eintreten eines Sicherheitsvorfalles ist jedoch konkret in Abschnitt 18.3 beschrieben. Somit gibt es keine Unterschiede, die das Sicherheitsniveau beeinflussen.

## 7.3.4 DER.2.1.A3

Allen Mitarbeitern müssen ihre Aufgaben im Falle eines Sicherheitsvorfalls bekannt sein. Es muss geregelt sein wer Entscheidungen, etwa für eine forensische Untersuchung, treffen darf und nach welchen Umständen sich diese Entscheidungen richten muss.

## Entsprechungen in VdS 3473

In Abschnitt 18.1 wird festgelegt, dass Sicherheitsvorfälle immer vom ISB in Zusammenarbeit mit den Fachverantwortlichen und Administratoren untersucht werden. Dabei müssen gemäß Abschnitt 18.3 auch Beweise gesichert werden.

<!-- page: 66 -->

## Unterschiede

Die Vorgaben der VdS sind hier deutlich konkreter und lassen weniger Freiheiten bei der Umsetzung als die des BSI. Im Wesentlichen sind sie Anforderungen aber vergleichbar.

## 7.3.5 DER.2.1.A4

Bei einem Sicherheitsvorfall müssen alle relevanten Stellen informiert werden. Dabei sind u.a. auch der Datenschutzbeauftragte oder zuständige Behörden zu berücksichtigen.

## Entsprechungen in VdS 3473

Meldungen von Sicherheitsvorfällen erfolgen grundsätzlich an den ISB. Abschnitt 18.1 regelt weiterhin, dass ein Unternehmen festlegen muss welche weiteren internen und externen Stellen über einen Sicherheitsvorfall unterrichtet werden müssen.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 7.3.6 DER.2.1.A5

Die Verantwortlichen müssen nach einem Sicherheitsvorfall die Ursachen und Probleme erkennen und beheben. Dabei muss ggf. auf interne und externe Experten zurückgegriffen werden, mit denen sicher zu kommunizieren ist.

## Entsprechungen in VdS 3473

In Abschnitt 18.3 macht die VdS konkrete Vorgaben wie nach einem Sicherheitsvorfall zu verfahren ist. Diese Anforderungen entsprechen im Wesentlichen der Anforderung (5) dieses Bausteins.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 7.3.7 DER.2.1.A6

Von einem Vorfall betroffene Systeme müssen vom Netz getrennt werden. Daten, die zur Behebung der Ursache notwendig, sind müssen gesichert werden. Datensicherungen müssen dahingehend überprüft werden, ob sie auch vom Vorfall betroffen waren. Die Betroffenen Systeme müssen in einen sicheren Zustand zurückgeführt werden. Passwörter müssen vor erneuter Betriebsaufnahme geändert werden. Die Systeme müssen auf weitere Angriffe überwacht werden.

<!-- page: 67 -->

## Entsprechungen in VdS 3473

In Abschnitt 18.3 wird das grobe Vorgehen nach einem Sicherheitsereignis beschrieben.

## Unterschiede

Die VdS beschreibt zwar das Rahmenvorgehen für das Wiederherstellen des Betriebs, ist dabei aber nicht so detailliert wie das BSI. Das Benennen von eindeutigen technischen Maßnahmen, wie etwa das Zurückspielen der Originaldaten von schreibgeschützten Datenträgern, fehlt in VdS 3473.

## 7.4 DER.2.2 - Vorsorge für die IT-Forensik

Baustein DER.2.2 zeigt mit welchen vorbeugenden Maßnahmen ein Unternehmen forensische Untersuchungen nach einem Sicherheitsvorfall erleichtern kann. Dazu gibt es 3 Anforderungen, welche in der Basisabsicherung umgesetzt werden müssen.

## 7.4.1 DER.2.2.A1

Wenn Daten zu forensischen Zwecken verarbeitet werden, müssen alle rechtlichen Vorgaben berücksichtigt werden. Auch interne Vereinbarungen mit Mitarbeitern dürfen nur in Einzelfällen übergangen werden. Dabei müssen die für den Datenschutz zuständigen Mitarbeiter sowie der Betriebsrat einbezogen werden.

## Entsprechungen in VdS 3473

In der VdS 3473 gibt es keine Vorgaben zur Vorbereitung forensischer Maßnahmen. Da der IT-Grundschutz auch für größere Unternehmen geeignet ist, sind die Anforderungen hier deutlich umfangreicher.

## 7.4.2 DER.2.2.A2

Es muss einen Leitfaden geben, aus dem hervorgeht welche Erstmaßnahmen nach einem Sicherheitsvorfall durchgeführt werden müssen. Das Ziel ist dabei möglichst wenige Beweise zu zerstören.

<!-- page: 68 -->

## Entsprechungen in VdS 3473

Die VdS legt in Punkt 18.3.3 fest, dass ein Schaden durch 'Sofortmaßnahmen' eingedämmt werden muss. Im Punkt 5 des selben Abschnittes wird das Sichern von Beweismitteln festgeschrieben.

## Unterschiede

Zwar legt die VdS explizit fest, dass Sofortmaßnahmen ergriffen werden müssen, berücksichtigt dabei aber nicht, dass eine spätere forensische Analyse durch versehentliche Zerstörung von Spuren erschwert werden könnte.

## 7.4.3 DER.2.2.A3

Eine Organisation muss über eine Vorauswahl an forensischen Dienstleistern verfügen, falls sie über keine eigenen Mitarbeiter für Forensik verfügt.

## Entsprechungen in VdS 3473

In VdS 3473 gibt es keine vergleichbare Vorgabe.

## 7.5 DER.2.3 - Bereinigung weitreichender Sicherheitsvorfälle

In diesem Baustein geht es darum den Regelbetrieb, nach einem größeren Sicherheitsvorfall, wiederaufnehmen zu können.

## 7.5.1 DER.2.3.A1

Nach einem größerem Sicherheitsvorfall muss ein Leitungsgremium alle zur Wiederherstellung notwendigen Maßnahmen planen und überwachen. Die zuständigen Personen müssen die dazu notwendigen Rechte haben.

## Entsprechungen in VdS 3473

Es gibt keine Anforderung in VdS 3473, die der Anforderung des BSI entspricht.

## Unterschiede

Die VdS schreibt die Zuständigkeit für die Reaktion nach einem Sicherheitsvorfall (Abschnitt 18.3) keiner Personengruppe konkret zu, somit ist eine Leitungsgruppe nicht vorgesehen.

<!-- page: 69 -->

## 7.5.2 DER.2.3.A2

Das Leitungsgremium aus Anforderung (1) muss eine Strategie für die Bereinigung von betroffenen IT-Systemen festlegen. Dabei muss unter anderem entschieden werden ob Systeme neu aufgesetzt oder nur bereinigt werden. Bereinigte Systeme müssen auf weitere Kommunikation mit Angreifern überwacht werden.

## Entsprechungen in VdS 3473

In VdS 3473 wird in Punkt 18.3.6 festgelegt, dass Schäden nach einem Sicherheitsvorfall behoben werden müssen.

## Unterschiede

Die VdS beschränkt sich darauf, dass Schäden behoben werden müssen. Genauere Angaben zur Abarbeitung des Vorfalls werden nicht gemacht. Somit liegen die Anforderungen der VdS deutlich unter denen des BSI.

## 7.5.3 DER.2.3.A3 und A4

Vom Vorfall betroffene Netzbereiche müssen von allen anderen Netzen, insbesondere vom Internet, getrennt werden. Dieses muss gleichzeitig für alle betroffenen Bereiche geschehen, im Zweifelsfall für jeden Netzabschnitt, der betroffen sein könnte.

Besteht die Möglichkeit, dass Zugangsdaten oder kryptographische Schlüssel kompromitiert wurden, müssen diese geändert werden.

## Entsprechungen in VdS 3473

Die VdS schreibt in Abschnitt 18.3 ihrer Richtlinie vor, dass 'Sofortmaßnahmen' nach einem Sicherheitsvorfall ergriffen werden müssen.

## Unterschiede

Wie in Anforderung (2) dieses Bausteins, macht die VdS keine näheren Angaben dazu wie nach einem Sicherheitsvorfall auf technischer Ebene verfahren werden muss. Hier sind die Anforderungen des BSI wesentlich umfangreicher. Besonders in kleineren Unternehmen könnte eine solche Verfahrensanweisung hilfreich sein, falls es dort keine Mitarbeiter gibt, die über das nötige Wissen verfügen. Auch der Verweis auf einen externen Dienstleister fehlt in den Vorgaben der VdS. Angaben zu Zugangsdaten fehlen ebenfalls. Wesentliche Teile der Anforderungen werden von VdS 3473 nicht abgedeckt.

<!-- page: 70 -->

## 7.5.4 DER.2.3.A5 und A6

Mögliche technische Schwachstellen, die den Angriff ermöglicht haben, müssen behoben werden. Im Falle von menschlichem Versagen muss mit Hilfe von organisatorischen oder anderen Maßnahmen Abhilfe geschaffen werden.

Die Betroffenen Systeme müssen in den Produktivbetrieb zurückgeführt werden. Dazu müssen eventuell vorhandene Analysesysteme entfernt werden.

## Entsprechungen in VdS 3473

Die VdS fordert in Abschnitt 18.3, dass entstandene Schäden behoben werden müssen und dass die normalen Geschäftsprozesse wiederaufgenommen werden. Außerdem müssen Ursachen beseitigt werden.

## Unterschiede

Die allgemeinen Vorgaben des IT-Grundschutzes und der VdS 3473 sind vergleichbar. Das BSI macht jedoch auch Anforderungen, die deutlich genauer beschrieben sind, so dass Anforderung (5) und (6) nur zum Teil erfüllt sind.

## 7.6 DER.3.1 - Audits und Revisionen

Im letzten betrachteten Baustein der DER-Reihe geht es um das Durchführen von Audits. Damit wird das Ziel verfolgt, dass die bestehenden Prozesse zur Informationssicherheit weiter optimiert werden. Der Baustein umfasst in der Basisabsicherung 4 Anforderungen.

Anders als beim sonstigen Vorgehen werde ich die Anforderungen dieses Bausteines vollständig zusammenfassen, da es keine einzelnen Abschnitte in der Richtlinie der VdS gibt, die zum Vergleich herangezogen werden können.

## 7.6.1 DER.3.1.A1 bis A4

In einer Einrichtung muss es einen Mitarbeiter geben, der für die Organisation von Audits verantwortlich ist. Dieser muss die Bearbeitung der jeweiligen Ergebnisse überwachen. Es ist darauf zu achten dass kein Interessenkonflikt entsteht.

Bei einem Audit/einer Revision muss das genaue Ziel definiert und die zuständigen Ansprechpartner informiert werden.

Ein Audit hat das Ziel zu prüfen ob die Anforderungen aller relevanten Regelungen erfüllt werden. Dabei sind aktive Eingriffe in die zu prüfenden Systeme nicht gestattet. Die Revision hat das Ziel zu prüfen ob die Anforderungen korrekt umgesetzt werden.

Die jeweiligen Ergebnisse müssen dokumentiert werden.

<!-- page: 71 -->

## Entsprechungen in VdS 3473

In der VdS 3473 gibt es keine Anforderungen zur Durchführung von Audits. Zwar ist an verschiedenen Stellen vorgeschrieben, dass Sicherheitsrichtlinien auf Aktualität geprüft werden müssen, es gibt aber keine Vorgaben dafür, dass auch die Erfüllung der vorgeschriebenen Anforderungen geprüft wird. Auch für kleine und mittlere Unternehmen ist es sinnvoll, dass die Umsetzung von Anforderungen untersucht wird. Hier sind die Anforderungen des IT-Grundschutzes deutlich umfangreicher und werden von VdS 3473 nicht abgedeckt.

## 7.7 Fazit

Der Vergleich der DER-Bausteine mit VdS 3473 bestätigt die bisherigen Ergebnisse. In organisatorischen Bereichen, in denen Anforderungen auch mit weitgefassten, allgemeinen Vorgaben umgesetzt werden können, liegen die Sicherheitsniveaus beider Regelwerke nahe beieinander. Baustein DER.2.1 wird beispielsweise (fast) vollständig von VdS 3473 abgedeckt. Bei technischen Anforderungen oder detaillierten Vorgaben liegt VdS 3473 aber auch hier hinter dem IT-Grundschutz zurück. Von 21 Anforderungen in dieser Gruppe werden nur 11 erfüllt, 6 davon mit deutlichen Abweichungen. 10 Anforderungen sind gar nicht durch VdS 3473 abgedeckt.

<!-- page: 72 -->



<!-- page: 73 -->

## Kapitel 8

## APP - Anwendungen

## 8.1 Übersicht

Die APP-Gruppe stellt Sicherheitsanforderungen an die Software, die ein Unternehmen verwendet. Dabei behandelt jeder Baustein einen bestimmten Typ von Programmen.

## 8.2 APP.1.1 - Office-Produkte

Der Baustein APP .1.1 stellt Sicherheitsanforderungen an Office-Produkte.

## 8.2.1 APP.1.1.A1

Office-Produkte müssen bei der Installation unverändert sein. Updates dürfen nur aus sicheren Quellen bezogen werden. Es muss sichergestellt werden, dass auch Updates unverändert installiert werden.

## Entsprechungen in VdS 3473

Die VdS beschreibt in Punk 10.3.1 der VdS 3473, dass Updates nur nach einem implementierten Verfahren installiert werden dürfen.

## Unterschiede

Die VdS sieht zwar Verfahren für den Umgang mit Updates vor, macht jedoch keine weiteren Angaben auf technischer Ebene. Die Anforderungen des BSI sind somit deutlich genauer.

<!-- page: 74 -->

## 8.2.2 APP.1.1.A2

Aktive Inhalte (etwa Makros) dürfen nicht automatisch ausgeführt werden. Sollte die Ausführung erforderlich sein muss sichergestellt sein, dass die Inhalte nur von vertrauenswürdigen Quellen stammen.

Die Mitarbeiter müssen im Bezug auf die besonderen Gefahren von aktiven Inhalten geschult werden.

## Entsprechungen in VdS 3473

Mitarbeiter müssen, nach den Vorgaben in Abschnitt 8.2 der VdS 3473, über Gefahren für die Informationssicherheit aufgeklärt werden.

## Unterschiede

Die VdS macht keine Angaben zu aktiven Inhalten. Da diese besonders gefährlich sein können ist die Anforderung als nicht erfüllt zu betrachten.

## 8.2.3 APP.1.1.A3

Dokumente aus fremden Quellen müssen auf Schadsoftware untersucht werden. Es dürfen in einem Unternehmen nur notwendige und unproblematische Dateiformate eingesetzt werden. Anwender müssten im Umgang mit Dokumenten aus fremden Quellen geschult werden.

## Entsprechungen in VdS 3473

Mitarbeiter müssen, nach den Vorgaben in Abschnitt 8.2 der VdS 3473, über Gefahren für die Informationssicherheit aufgeklärt werden.

## Unterschiede

Die VdS macht keine Vorgaben zu Dateiformaten oder zum Umgang mit Dokumenten aus fremden Quellen.

## 8.2.4 APP.1.1.A4

Der ISB und der IT-Betrieb müssen regelmäßig über aktuelle Sicherheitslücken in OfficeProdukten informieren.

<!-- page: 75 -->

## Entsprechungen in VdS 3473

Es gibt keine Anforderungen, die denen des BSI entsprechen.

## 8.3 APP.1.2 - Web-Browser

Web-Browser gehören mit Sicherheit zu den am meisten genutzten Programmen. Dabei bieten sie jedoch auch eine große Angriffsfläche. Dieser Baustein enthält Anforderungen, mit denen Gefahren durch Angriffe auf Web-Browser abgewendet werden sollen.

## 8.3.1 APP.1.2.A1

Bei den im Unternehmen eingesetzten Webbrowsern muss ein Sandboxing-Verfahren angewendet werden. Das bedeutet, dass jeder Prozess (Jede aufgerufene Webseite, alle Plugins) des Browsers nur auf seine eigenen Speicherbereiche zugreifen kann.

## Entsprechungen in VdS 3473

Es gibt keine Anforderungen, die denen des BSI entsprechen.

## 8.3.2 APP.1.2.A2

Der Webbrowser muss eine sichere Version von TLS ('Transport Layer Security', eine verschlüsselte Übertragung der Inhalte) unterstützen. Ebenfalls muss HSTS unterstützt werden. HSTS steht für 'HTTP Strict Transport Security', oft auch als 'Certificate Pinning' bezeichnet.

## Entsprechungen in VdS 3473

Es gibt keine Anforderungen, die denen des BSI entsprechen.

## 8.3.3 APP.1.2.A3

Der verwendete Webbrowser muss eine Liste mit vertrauenswürdigen WurzelzertifikatAusstellern haben und unternehmenseigenen Zertifikaten vertrauen. Insbesondere müssen Extended-Validation-Zertifikate unterstützt werden.

Änderungen an den Zertifikaten, denen der Browser vertraut, dürfen nur mit Administratorrechten durchgeführt werden. Zertifikate müssen im Browser widerrufen werden können.

Der Browser muss die Gültigkeit von Zertifikaten überprüfen.

<!-- page: 76 -->

Es muss für den Benutzer leicht erkennbar sein, ob die Kommunikation des Browsers verschlüsselt ist oder nicht. Sollte ein Zertifikat fehlerhaft oder ungültig sein darf die Verbindung nur nach ausdrücklicher Bestätigung durch den Nutzer erfolgen.

## Entsprechungen in VdS 3473

Es gibt keine Anforderungen, die denen des BSI entsprechen.

## 8.3.4 APP.1.2.A4

Es muss möglich sein die Version des Browsers sowie die aller Plugins anzuzeigen. Updates müssen umgehend installiert werden. Sollte für eine schwerwiegende Schwachstelle kein Update verfügbar sein müssen zeitnah andere Maßnahmen ergriffen werden.

## Entsprechungen in VdS 3473

Die VdS sieht in Punkt 10.3.1 ihrer Richtlinie vor, dass Updates nach einem vorgegebenen Verfahren installiert werden.

## Unterschiede

Die VdS macht keine besondere Angabe zu Webbrowsern. Es gibt nur eine allgemeine Vorgabe zum Umgang mit Updates. Die Anforderung ist somit im Wesentlichen nicht erfüllt.

## 8.4 APP.2.1 - Allgemeiner Verzeichnisdienst

Ein Verzeichnisdienst stellt Informationen über eine bestimmte Art von Objekten zur Verfügung. Beispiele dafür sind Adressbücher oder ein Verzeichnis der Benutzerkonten aller Mitarbeiter. Da ein solcher Datensatz bei unberechtigtem Zugriff eine große Gefahr bedeuten kann, macht der Baustein APP .2.1 Vorgaben, wie ein sicherer Betrieb eines solchen Dienstes möglich ist.

## 8.4.1 APP.2.1.A1

Es muss eine gesonderte Sicherheitsrichtlinie für Verzeichnisdienste geben.

## Entsprechungen in VdS 3473

Laut Abschnitt 6.5 der VdS 3473 muss der ISB den Bedarf für weitere Informationssicherheitsrichtlinien ermitteln.

<!-- page: 77 -->

## Unterschiede

Die VdS stellt keine expliziten Anforderungen an Verzeichnisdienste auf.

## 8.4.2 APP.2.1.A2

Es muss, abhängig von der beabsichtigten Nutzung des Verzeichnisdienstes, ein Modell für die geplanten Objektklassen erstellt werden. Dabei müssen Personalvertretung und Datenschutzbeauftragter einbezogen werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der VdS 3473.

## 8.4.3 APP.2.1.A3

Die Administration und das Verwalten der eigentlichen Daten muss getrennt erfolgen. Die Zugriffsrechte müssen nach der in Anforderung (1) erstellten Richtlinie vergeben werden. Nach Zusammenführung mehrerer Verzeichnisbäume muss die neue Situation entsprechend geprüft werden.

## Entsprechungen in VdS 3473

In Punk 15.1.2 der VdS 3473 wird bestimmt, dass Nutzer nur den administrativen Zugriff bekommen dürfen, den sie für ihre Aufgaben benötigen.

## Unterschiede

Die VdS stellt keine gesonderten Anforderungen an Verzeichnisdienste. Somit wird auch nicht verlangt, dass die Verwaltung eines solchen Dienstes von der Administration getrennt ist. Ein Administrator, der gleichzeitig Verwalter ist, kann so in die Situation kommen, dass er Verwaltungsaufgaben mit administrativen Rechten durchführt.

## 8.4.4 APP.2.1.A4

Die Zugriffsrechte für einen Verzeichnisdienst müssen bereits während der Installation eingerichtet werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der VdS 3473.

<!-- page: 78 -->

## 8.4.5 APP.2.1.A5

Verzeichnisdienste müssen sowohl auf dem Server als auch auf dem Client sicher konfiguriert sein. Administrative Zugänge müssen geschützt sein.

## Entsprechungen in VdS 3473

Die VdS schreibt in Punkt 10.3.8 vor, dass Nutzer keine administrativen Zugriffsrechte haben dürfen.

## Unterschiede

Zu Servern und Clients für Verzeichnisdienste gibt es keine näheren Vorgaben. Die Anforderung wird damit nicht von VdS 3473 abgedeckt.

## 8.4.6 APP.2.1.A6

Während des Betriebs muss der Verzeichnisdienst durchgehend sicher sein. Nur Administratoren dürfen Zugang zu den entsprechenden Werkzeugen haben.

## Entsprechungen in VdS 3473

Die VdS schreibt in Punkt 10.3.8 vor, dass Nutzer keine administrativen Zugriffsrechte haben dürfen.

## Unterschiede

Zum Betrieb von Verzeichnisdiensten gibt es keine Vorgaben, die Anforderung wird nicht von VdS 3473 erfüllt.

## 8.5 APP.2.2 - Active Directory

Active Directory ist ein Verzeichnisdienst von Microsoft. Er erfasst Informationen über Benutzer und IT-Systeme. Die in diesem Baustein gemachten Anforderungen sollen den sicheren Betrieb eines solchen Dienstes ermöglichen.

## 8.5.1 APP.2.2.A1 und A2

Wie bei allgemeinen Verzeichnisdiensten auch, muss ein geeignetes Datenmodell erstellt werden. Die Berechtigungen der Nutzer müssen rollen-basiert geplant werden. Dabei müssen administrative Rechte möglichst restriktiv vergeben sein. Es darf in großen Domänen nicht zu Überschneidungen von Dienst- und Datenverwaltung kommen.

<!-- page: 79 -->

## Entsprechungen in VdS 3473

Die VdS hat in Abschnitt 4.1.2 die Funktionstrennung definiert. Widersprechende Aufgaben dürfen nicht von einer Person durchgeführt werden.

## Unterschiede

Die VdS mach keine expliziten Angaben zu Activ Directory. Es wird nur allgemein eine Trennung von widersprechenden Verantwortlichkeiten verlangt.

## 8.5.2 APP.2.2.A3

Es muss ein Konzept für die Erstellung von Gruppenrichtlinien unter Windows geben. Dieses Konzept muss Mehrfachüberdeckungen vermeiden. Aus der Dokumentation müssen Ausnahmen hervorgehen. Die Parameter der Gruppenrichtlinien müssen sicher vorgegeben sein.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in der VdS 3473.

## 8.5.3 APP.2.2.A4

Administratoren müssen mit den Sicherheitsaspekten von Activ Directory vertraut sein.

## Entsprechungen in VdS 3473

In Abschnitt 7.1 verlangt VdS 3473, dass Mitarbeiter für ihre Aufgaben die nötige Eignung haben.

## Unterschiede

Die VdS verlangt nicht explizit, dass ein Administrator über die Sicherheit von Activ Directory Bescheid weiß. Die Anforderungen des IT-Grundschutzes sind hier genauer.

## 8.5.4 APP.2.2.A5

Built-in-Accounts müssen über komplexe Passwörter verfügen und dürfen nur als Notfallkonten verwendet werden. Administrator Konten müssen Mitglieder der 'Protected Users' Gruppe sein.

Alle Domänen-Controller müssen auf Betriebssystemebene mit restriktiven Zugriffsrechten versehen sein.

<!-- page: 80 -->

Der Wiederherstellungsmodus von Activ Directory muss mit einem sicheren Passwort geschützt sein.

Die Gruppe 'Jeder' darf nur über eingeschränkte Rechte verfügen.

Domänen-Controller müssen vor unberechtigtem Neustarten geschützt sein.

Richtlinien für Domänen-Controller müssen sichere Einstellungen für Authentifizierung und Überwachung beinhalten.

## Entsprechungen in VdS 3473

Die VdS schreibt in Punkt 10.3.8 vor, dass Nutzer keine administrativen Zugriffsrechte haben dürfen.

## Unterschiede

Die VdS macht nur allgemeine Angaben zu Administrator-Zugängen. Es gibt keine Anforderungen, welche sich auf die übrigen Aspekte von Activ Directory beziehen. Die Anforderung wird nicht von VdS 3473 erfüllt.

## 8.5.5 APP.2.2.A6

Alle im Activ Directory vorhandenen Vertrauensbeziehungen müssen regelmäßig geprüft werden. Administratoren auf Domänen-Controllern dürfen nur die Rechte haben, die sie für ihre Aufgaben benötigen. Es sollte möglichst keine Mitglieder in der Gruppe 'Domänenadministratoren' geben. Ungenutzte Konten müssen deaktiviert werden.

## Entsprechungen in VdS 3473

VdS 3473 schreibt in Abschnitt 15.1 vor, dass nur die Zugriffsrechte genehmigt werden, die zur Erfüllung der Aufgaben erforderlich sind.

## Unterschiede

Die VdS macht keine auf Activ Directory bezogenen Vorgaben. Außer dem restriktiven Umgang mit Administrator-Rechten sind die Anforderungen des BSI nicht von VdS 3473 abgedeckt.

## 8.5.6 APP.2.2.A7

Administrator-Konten dürfen nicht für die reguläre Arbeit verwendet werden. Solche Zugänge dürfen nur auf ihren jeweiligen Systemen eingesetzt werden, d. h. ein ServerAdministrator darf sich nicht auf einem Arbeitsplatz-Rechner anmelden.

<!-- page: 81 -->

Benutzeraccounts müssen eindeutig einer Person zugeordnet sein.

Es muss so wenig Administratoren wie möglich geben, ihre Zugänge müssen geeignet gesichert sein. Dienste-Administratoren müssen die einzigen sein, die andere Dienste-Administrator-Konten bearbeiten dürfen.

Die (Domänen-) Administrator-Gruppe muss Besitzer des Domänen-Stammobjektes sein.

## Entsprechungen in VdS 3473

Neben den in A5 und A6 bereits genannten Einschränkungen für Administrator-Konten gibt es keine weiteren Entsprechungen in VdS 3473.

## 8.6 APP.3.1 - Webanwendungen

Webanwendungen sind Programme, welche nicht auf dem Rechner eines Benutzer ausgeführt werden. Sie werden mittels eines Webbrowsers von einem Server geladen und müssen deswegen nicht auf dem Rechner des Benutzers installiert sein.

Dieser Baustein stellt 7 Anforderungen auf, um Webanwendungen sicher zu Betreiben.

## 8.6.1 APP.3.1.A1

Für die Benutzung einer Webanwendung muss es eine geeignete Authentifikation geben. Dabei muss auf etablierte Standards zurückgegriffen werden. Passwortdateien müssen ausreichend geschützt werden. Die Benutzer müssen gezwungen werden ein sicheres Passwort zu wählen. Falls Zugangsdaten auf dem Client gespeichert werden, muss der Benutzer dem zustimmen und vorher auf die daraus entstehenden Gefahren hingewiesen werden. Die Webanwendung muss Grenzwerte für fehlgeschlagene Anmeldeversuche haben. Die Benutzer müssen darüber informiert werden wenn ihr Passwort zurückgesetzt wurde.

Bei kritischen Aktionen muss der Nutzer sich noch einmal authentifizieren. Falls mehrere Methoden zur Authentifizierung verwendet werden müssen alle das gleiche Sicherheitsniveau haben.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

<!-- page: 82 -->

## 8.6.2 APP.3.1.A2

Anwender dürfen nur Aktionen durchführen zu denen sie berechtigt sind. Die Zugriffsrechte müssen restriktiv vergeben werden. Die Verantwortlichen müssen Änderungen an Zugriffsrechten prüfen und dokumentieren. Wenn die Webanwendung nicht selbst über ein System für Zugriffsrechte verfügt, muss dafür auf ein zusätzliches System zurückgegriffen werden.

Die Autorisierungskomponente muss alle Teile der Webanwendung abdecken und server-seitig Arbeiten.

## Entsprechungen in VdS 3473

Die VdS regelt in Abschnitt 15.1, dass Anwender nur die für ihre Arbeit notwendigen Berechtigungen erhalten. Außerdem müssen vergebene Zugriffsrechte dokumentiert werden.

## Unterschiede

Die VdS macht nur allgemeine Angaben zu Zugriffsrechten. Für Webanwendungen gibt es keine gesonderten Anforderungen. Der IT-Grundschutz stellt genauere Anforderungen auf.

## 8.6.3 APP.3.1.A3

Session-IDs müssen zufällig erzeugt werden und geschützt sein. Falls möglich muss dies von einem ggf. verwendeten Framework umgesetzt werden. Dafür muss das Framework sicher konfiguriert sein.

Nutzer müssen die Möglichkeit haben eine Session explizit zu beenden. Bei Anmeldung eines Nutzers muss eine neue Session erzeugt werden, auch wenn noch eine alte vorhanden ist. Die Dauer einer Session muss beschränkt werden. Nach Ende einer Session müssen alle Sitzungsdaten vom Client und vom Server gelöscht werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 8.6.4 APP.3.1.A4

Die Webanwendung darf nur vorgesehene Daten einbinden. Upload-Funktionen dürfen nur notwendige Datei-Typen und -Pfade akzeptieren. Die Zugriffs- und Ausführungsrechte müssen restriktiv gesetzt werden.

<!-- page: 83 -->

Benutzer müssen informiert werden wenn sie auf nicht vertrauenswürdige Webseiten weitergeleitet werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 8.6.5 APP.3.1.A5

Ereignisse mit Sicherheitsbezug müssen protokolliert werden. Zugriff auf entsprechende Daten dürfen nur befugte Personen haben. Schadcode in Protokolldateien darf von Auswertungsprogrammen nicht ausgeführt werden.

## Entsprechungen in VdS 3473

Die VdS beschreibt in Punkt 10.3.3 der VdS 3473 dass Sicherheitsereignisse protokolliert werden müssen.

## Unterschiede

Die VdS macht keine Vorgaben zum Zugriff auf Protokolldaten und fordert nicht, dass Schadcode nicht von Auswertungssoftware ausgeführt wird. Die Anforderungen des IT-Grundschutzes sind umfangreicher.

## 8.6.6 APP.3.1.A6

Administratoren müssen sich regelmäßig über Schwachstellen informieren. Sicherheitsupdates müssen kurzfristig installiert werden. Die Updates müssen dabei aus vertrauenswürdigen Quellen stammen und getestet werden. Eine Wiederherstellung des alten Zustandes muss möglich sein.

## Entsprechungen in VdS 3473

Die VdS verlangt, dass Sicherheitsupdates des Herstellers getestet und installiert werden (Punk 10.3.1). In Abschnitt 8.1 gibt es eine Anforderung, die ähnlich der Vorgabe des BSI, verlangt, dass regelmäßig Informationen über aktuelle Gefährdungen eingeholt werden.

## Unterschiede

Die VdS verzichtet darauf, dass nach einem Update der vorherige Zustand wiederhergestellt werden kann.

<!-- page: 84 -->

## 8.6.7 APP.3.1.A7

Webanwendungen müssen vor automatischen Zugriffen geschützt sein. Die Funktionsfähigkeit der Anwendung für legitime Benutzer muss berücksichtigt werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 8.7 APP.3.2 - Webserver

Die Anforderungen im Baustein APP .3.2 sollen den sicheren Betrieb eines Webservers gewährleisten.

## 8.7.1 APP.3.2.A1

Ein Webserver muss sicher konfiguriert werden. Unter anderem muss das Benutzerkonto, mit dem der Prozess des Webservers ausgeführt, wird minimale Rechte haben. Falls möglich muss der Webserver in einer Sandbox betrieben werden. Nicht benötigte Funktionen müssen abgeschaltet werden.

## Entsprechungen in VdS 3473

Für Webserver gibt es keine Anforderungen in VdS 3473.

## 8.7.2 APP.3.2.A2

Scripte, Konfigurationsdateien und andere Daten dürfen nicht unberechtigt gelesen oder verändert werden.

Der Webserver darf nur auf Daten in dem dafür vorgesehenen Verzeichnisbaum zugreifen. Verzeichnisse dürfen nicht aufgelistet werden und unveränderliche Daten müssen schreibgeschützt sein. Falls vertrauliche Daten verarbeitet werden, müssen diese verschlüsselt übertragen und gespeichert werden.

## Entsprechungen in VdS 3473

Für Webserver gibt es keine Anforderungen in VdS 3473.

<!-- page: 85 -->

## 8.7.3 APP.3.2.A3

Dateien, die mit einem Webserver veröffentlicht werden, müssen auf Schadsoftware geprüft werden. Unnötige Informationen müssen von Dokumenten entfernt werden. Abrufbare Dateien müssen auf einer eigenen Partition gespeichert sein.

Datei-Uploads müssen mit einer Maximalgröße versehen sein. Der Benutzer darf den Ablageort einer Datei nicht beeinflussen können, dieser muss zufällig sein.

## Entsprechungen in VdS 3473

Für Webserver gibt es keine Anforderungen in VdS 3473

## 8.7.4 APP.3.2.A4

Ein Webserver muss Protokolle über erfolgreiche und fehlgeschlagene Zugriffe führen. Allgemeine Fehlermeldungen müssen ebenfalls gespeichert werden.

## Entsprechungen in VdS 3473

Die VdS schreibt in Punk 10.3.3 vor, dass jedes IT-System (also auch Webserver) Fehler und Sicherheitsereignisse speichern muss. Die Anforderungen der VdS sind hier also mit denen des BSI vergleichbar.

## Unterschiede

Es gibt keine Unterschiede.

## 8.7.5 APP.3.2.A5

Falls sich Clients am Webserver anmelden muss dafür eine verschlüsselte Verbindung genutzt werden. Die auf dem Server genutzten Passwortdateien müssen kryptographisch gesichert und vor unberechtigtem Zugriff geschützt sein.

## Entsprechungen in VdS 3473

Es gibt keine Anforderungen, die denen des BSI entsprechen.

## 8.7.6 APP.3.2.A6

Die verantwortlichen Mitarbeiter müssen sich regelmäßig über Schwachstellen in der Server-Software informieren. Sicherheitsupdates müssen kurzfristig installiert werden.

<!-- page: 86 -->

Die Updates müssen dabei aus vertrauenswürdigen Quellen stammen und getestet werden. Eine Wiederherstellung des alten Zustandes muss möglich sein.

## Entsprechungen in VdS 3473

Die VdS verlangt, dass Sicherheitsupdates des Herstellers getestet und installiert werden (Punk 10.3.1). In Abschnitt 8.1 gibt es eine Anforderung, die ähnlich der Vorgabe des BSI, verlangt, dass regelmäßig Informationen über aktuelle Gefährdungen eingeholt werden.

## Unterschiede

Die VdS verzichtet darauf, dass nach einem Update der vorherige Zustand wiederhergestellt werden kann.

## 8.7.7 APP.3.2.A7

Bei der Verbreitung von Inhalten Dritter müssen rechtliche Vorgaben beachtet werden.

## Entsprechungen in VdS 3473

Es gibt keine äquivalenten Anforderungen in VdS 3473.

## 8.8 APP.3.3 - Fileserver

Fileserver sind IT-Systeme, die dazu dienen Dateien mit anderen Benutzern und IT-Systemen auszutauschen. Um diese sicher betreiben zu können gibt es die Anforderungen in Baustein APP .3.3

## 8.8.1 APP.3.3.A1

Filesever dürfen nur an Orten betrieben werden, zu denen nur Berechtigte Zugang haben. Die Umgebung und die Stromversorgung muss für den Betrieb von Servern geeignet sein.

## Entsprechungen in VdS 3473

Es gibt keine Anforderungen in VdS 3473, die denen des BSI entsprechen.

<!-- page: 87 -->

## 8.8.2 APP.3.3.A2

Es muss geprüft werden ob ein RAID-System verwendet werden soll. Falls dies der Fall ist, muss das System dem Stand der Technik entsprechen und die Einzelheiten müssen definiert sein.

## Entsprechungen in VdS 3473

Es gibt keine Vergleichbaren Anforderungen in VdS 3473.

## 8.8.3 APP.3.3.A3

Abhängig vom Betriebssystem muss der Fileserver vor Schadsoftware geschützt werden. Die auf dem Server freigegebenen Dateien müssen regelmäßig auf Schadsoftware untersucht werden, dabei müssen auch Echtzeit-Scans zum Einsatz kommen. Auch komprimierte Daten müssen geprüft werden.

Daten müssen vor dem Speichern auf dem Server von der Antivirensoftware geprüft werden. Die eingesetzte Software muss aktuell gehalten werden. Nutzer dürfen keine Änderungen an der Antivirensoftware vornehmen.

## Entsprechungen in VdS 3473

Die VdS schreibt vor, dass jedes IT-System über einen Schutz vor Schadsoftware verfügen muss. Jedes System muss täglich auf Schadprogramme untersucht werden. Die eingesetzte Software muss täglich nach Updates suchen.

## Unterschiede

Die VdS hat keine Anforderungen, welche auf die Besonderheiten von Fileservern eingeht. Ein Echtzeitschutz ist bei der VdS nur als 'SOLLTE'-Anforderung vorhanden. Die Anforderungen des BSI sind genauer auf den Bereich 'Fileserver' zugeschnitten.

## 8.8.4 APP.3.3.A4

Daten auf Fileservern müssen regelmäßig gesichert werden. Details müssen in einem Konzept festgehalten werden. In jedem Fall muss eine Sicherung nach der Installation von Software oder Änderungen an der Konfiguration erfolgen. Die Sicherungen müssen jeder Zeit wiederherstellbar sein.

<!-- page: 88 -->

## Entsprechungen in VdS 3473

In Kapitel 16 fordert die VdS, dass es eine Informationssicherheitsrichtlinie für die Datensicherung geben muss. In Punk 16.5.2 wird für Server festgelegt, dass diese gesichert werden müssen.

## Unterschiede

Die VdS sieht vor, dass Sicherungen nicht länger als 24 Stunden auseinander liegen dürfen. Das BSI macht keine genauen Angaben zu einer Zeitspanne. Auf Seiten des IT-Grundschutzes wird jedoch explizit eine Sicherung im Rahmen einer Änderung am System verlangt, was sich in VdS 3473 nicht findet.

## 8.8.5 APP.3.3.A5

Die Rechte für den Dateizugriff auf dem Fileserver müssen restriktiv vergeben werden. Systemverzeichnisse dürfen nicht für Unbefugte freigegeben werden.

Die bestehenden Zugriffsrechte müssen regelmäßig geprüft werden. Vorgänge zum Ändern von Zugriffsrechten müssen definiert sein. Änderungen müssen dokumentiert werden.

## Entsprechungen in VdS 3473

Die VdS schreibt in Abschnitt 15.1 vor, dass Anwender nur die Rechte haben dürfen, die sie zum Erfüllen ihrer Aufgaben benötigen. Änderungen müssen dokumentiert werden.

## Unterschiede

Die VdS macht keine Angaben zu Zugriffsrechten auf Dateiservern. Die Anforderungen des BSI sind umfangreicher.

## 8.9 APP.3.4 - Samba

Samba ist eine Software mit der Active Directory Funktionen genutzt werden können. Auch Filesver-Funktionen werden von Samba zur Verfügung gestellt. Dieser Baustein regelt in 2 Basisanforderungen wie ein Samba-Server sicher betrieben werden kann.

<!-- page: 89 -->

## 8.9.1 APP.3.4.A1

Die Einführung eines Samba-Servers muss vorbereitet werden. Dabei müssen die Aufgaben des Server definiert werden. Für den Einsatz in besonderen Betriebsarten (z. B. als Cluster) müssen umfangreiche Vorplanungen und Tests durchgeführt werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Anforderungen in VdS 3473.

## 8.9.2 APP.3.4.A2

Ein Samba-Server muss sicher konfiguriert werden. Die Zugriffsrechte für jeden Benutzer müssen angepasst werden. Nur berechtigte Nutzer dürfen den Dienst nutzen.

Der Server darf nur Verbindungen von sicheren Netzen und Rechnern annehmen. Es darf keine zusätzliche Software wie 'SWAT' (eine Weboberfläche zur Konfiguration von Samba) eingesetzt werden.

## Entsprechungen in VdS 3473

VdS 3473 sieht in Abschnitt 15 vor, dass Nutzer nur auf die Dinge zugreifen dürfen, die sie für ihre Aufgaben benötigen.

## Unterschiede

Die VdS macht, neben den Anforderungen für die Zugriffsrechte, keine weiteren Angaben zu Samba-Servern. Die Anforderungen des BSI sind umfangreicher.

## 8.10 APP.3.6 - DNS-Server

In diesem Baustein werden Anforderungen für den sicheren Betrieb von DNS-Server gestellt. DNS-Server haben die Aufgabe Hostnamen (z. B. www.tu-dortmund.de) in IP-Adressen umzuwandeln. Da viele Anwendungen ihren Datenverkehr nicht direkt über IP-Adressen abwickeln, sondern dafür Hostnamen verwenden, sind DNS-Server besonders wichtig.

## 8.10.1 APP.3.6.A1

Der Einsatzes eines DNS-Server muss geplant werden. Dabei sind u. a. die zu schützenden DNS-Informationen zu berücksichtigen. Die Ergebnisse der Planung müssen dokumentiert werden.

<!-- page: 90 -->

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Anforderungen VdS 3473.

## 8.10.2 APP.3.6.A2

Für jeden (externen) Advertising-DNS-Server muss es mindestens einen zusätzlichen Secondary-DNS-Server geben.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Anforderungen VdS 3473.

## 8.10.3 APP.3.6.A3

Interne und externe DNS-Anfragen müssen getrennt werden. Interne DNS-Resolver dürfen nur die Internen DNS-Server verwenden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Anforderungen VdS 3473.

## 8.10.4 APP.3.6.A4

Resolving-DNS-Server dürfen nur Anfragen aus dem internen Netz beantworten. Beim Versenden von Anfragen muss er zufällige Source Ports verwenden. Es dürfen keine Anfragen an Server gesendet werden, die falsche Informationen liefern. Advertising-Server müssen Anfragen aus dem Internet der Reihe nach behandeln.

Zonentransfers zwischen primären und sekundären Servern müssen funktionieren und dürfen nur zwischen den dafür vorgesehenen Servern erfolgen. Der DNS-Server darf seine Version nicht bekannt geben.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Anforderungen VdS 3473.

## 8.10.5 APP.3.6.A5

Die zuständigen Mitarbeiter müssen sich regelmäßig über Sicherheitslücken informieren. Updates müssen kurzfristig getestet und eingespielt werden. Falls eine Schwachstelle nicht per Update geschlossen werden kann, müssen andere Maßnahmen ergriffen werden.

<!-- page: 91 -->

## Entsprechungen in VdS 3473

Die VdS verlangt, dass Sicherheitsupdates des Herstellers getestet und installiert werden (Punk 10.3.1). In Abschnitt 8.1 gibt es eine Anforderung, die wie die Vorgabe des BSI verlangt, dass regelmäßig Informationen über aktuelle Gefährdungen eingeholt werden.

Sollte eine Sicherheitslücke nicht geschlossen werden können, muss der Netzwerkverkehr beschränkt werden [9, Punk 10.3.2].

## Unterschiede

In VdS 3473 wird das Sichern von Konfigurationsdateien vor Updates nicht angefordert. Außerdem ist, im Falle von nicht behobenen Sicherheitslücken, nur eine Beschränkung des Netzverkehrs vorgesehen. Es sind Situationen denkbar in denen diese Maßnahme jedoch nicht ausreicht.

## 8.10.6 APP.3.6.A6

Nur legitime IT-Systeme dürfen bestimme Domain-Informationen ändern.

## Entsprechungen in VdS 3473

Es gibt keine Anforderungen in VdS 3473, die denen des BSI entsprechen.

## 8.10.7 APP.3.6.A7

DNS-Server müssen laufend auf Störungen oder Ausfall überwacht werden. Dabei sind Auslastung und Leistung der Server zu berücksichtigen. Sicherheitsereignisse müssen protokolliert werden.

## Entsprechungen in VdS 3473

Die VdS schreibt vor, dass alle IT-Systeme Sicherheitsereignisse protokollieren müssen.

## Unterschiede

Die VdS verlangt nicht, dass (DNS-) Server durchgehend überwacht werden.

## 8.10.8 APP.3.6.A8

Alle Domains, die ein Unternehmen verwendet, müssen rechtzeitig verlängert werden. Dafür muss ein Mitarbeiter zuständig sein. Falls dieses ein externer Dienstleister durchführt, muss sichergestellt sein, dass nur das Unternehmen die Kontrolle über die Domains hat.

<!-- page: 92 -->

## Entsprechungen in VdS 3473

Es gibt keine Anforderung zu Domains in VdS 3473.

## 8.10.9 APP.3.6.A9

Ein Notfallplan für DNS-Server muss in die bereits bestehenden Notfallpläne integriert werden. Im Datensicherungskonzept müssen auch Zonenkonfigurationen berücksichtigt werden. Der Notfallplan muss auch den Wiederanlauf regeln.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 8.11 APP.4.3 - Relationale Datenbanksysteme

Datenbanksysteme sind die Basis für viele Anwendungen. In ihnen werden oft große Datenmengen gespeichert. Die 9 Anforderungen des Bausteins APP .4.3 sollen helfen Datenbanken sicher zu betreiben.

## 8.11.1 APP.4.3.A1

Es muss eine Informationssicherheitsrichtlinie für Datenbank-Systeme geben. Diese muss allen Mitarbeitern, die mit Datenbanken arbeiten, bekannt sein. Alle Änderungen an der Richtlinie müssen dokumentiert und mit dem ISB abgestimmt sein. Die Richtlinie muss regelmäßig auf Aktualität geprüft werden.

## Entsprechungen in VdS 3473

Die VdS macht keine Angaben zu Datenbank-Systemen.

## 8.11.2 APP.4.3.A2

Die Installationsdaten für Datenbankmanagementsysteme (DBMS) müssen aus sicheren Quellen stammen. Updates müssen vor Inbetriebnahme installiert werden.

## Entsprechungen in VdS 3473

Die VdS macht keine Angaben zu Datenbank-Systemen.

<!-- page: 93 -->

## 8.11.3 APP.4.3.A3

DBMS müssen nach ihrer Installation gehärtet (best möglich gesichert) werden. Dafür muss eine Checkliste erstellt und abgearbeitet werden. Insbesondere muss sichergestellt werden, dass alle Passwörter geändert und sicher gespeichert werden. Die Basishärtung muss regelmäßig geprüft werden.

## Entsprechungen in VdS 3473

Die VdS macht keine Angaben zu Datenbank-Systemen.

## 8.11.4 APP.4.3.A4

Datenbanken müssen nach einem geregelten Prozess angelegt werden. Das Anlegen ist zusammen mit Informationen zur Datenbank zu dokumentieren.

## Entsprechungen in VdS 3473

Die VdS macht keine Angaben zu Datenbank-Systemen.

## 8.11.5 APP.4.3.A5

Das Konzept zum Umgang mit Benutzern und Rollen aus ORP .4 muss auf Datenbanken erweitert werden.

Es muss einen Prozess geben, welcher das Anlegen, Löschen usw. von Benutzern regelt. Berechtigungen müssen so restriktiv wie möglich sein. Bestehende Berechtigungen müssen regelmäßig geprüft werden.

## Entsprechungen in VdS 3473

Die VdS behandelt den Umgang mit Benutzerrechten in Kapitel 15 von VdS 3473. Die dort genannten Anforderungen entsprechen im Wesentlichen denen des BSI.

## Unterschiede

Die Anforderungen der VdS sind zwar nicht besonders auf Datenbanken bezogen, können aber auf diese angewendet werden. Somit gibt es keine wesentlichen Unterschiede zwischen den Anforderungen des BSI und denen der VdS.

<!-- page: 94 -->

## 8.11.6 APP.4.3.A6

DBMS-Passwörter müssen den Vorgaben des Unternehmens entsprechen. Bei Verdacht auf einen Sicherheitsvorfall müssen alle Passwörter geändert werden.

## Entsprechungen in VdS 3473

Es gibt keine Anforderungen in VdS 3473, die denen des BSI entsprechen.

## 8.11.7 APP.4.3.A7

Sicherheitsupdates müssen schnell getestet und eingespielt werden. Vorher muss das Datenbank-System gesichert werden.

Es muss eine Rolle geben, die regelmäßig Informationen zu Sicherheitslücken von Datenbank-Systemen einholt. Nach Möglichkeit müssen DBMS-Updates an den Update-Zyklus des Herstellers angepasst werden.

## Entsprechungen in VdS 3473

Die VdS verlangt, dass Sicherheitsupdates des Herstellers getestet und installiert werden (Punk 10.3.1). In Abschnitt 8.1 gibt es eine Anforderung, die ähnlich der Vorgabe des BSI verlangt, dass regelmäßig Informationen über aktuelle Gefährdungen eingeholt werden.

## Unterschiede

Die VdS verlangt nicht, dass der Update-Zyklus von DBM-Systemen an den des Herstellers angepasst wird.

## 8.11.8 APP.4.3.A8

Sicherheitsereignisse bei Datenbanksystemen müssen protokolliert werden.

## Entsprechungen in VdS 3473

Die VdS schreibt in Abschnitt 10.3 vor, dass jedes IT-System Sicherheitsvorfälle protokollieren muss.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

<!-- page: 95 -->

## 8.11.9 APP.4.3.A9

Datenbanken müssen regelmäßig gesichert werden, insbesondere vor dem Erstellen einer neuen Datenbank.

## Entsprechungen in VdS 3473

Die VdS regelt das Sichern von Daten in Kapitel 16.

## Unterschiede

In den Anforderungen der VdS wird nicht gesondert auf Datenbanken eingegangen. Daher ist auch keine Sicherung vor dem Erstellen einer neuen Datenbank vorgesehen.

## 8.12 APP.5.1 - Allgemeine Groupware

Groupware erleichtert die Zusammenarbeit von Menschen. Eine solche Software wird häufig auf einem Server betrieben und stellt Funktionen wie Adressbücher, Kalender oder Projektmanagement zur Verfügung. Der Baustein APP .5.1 beschreibt 5 Basisanforderungen um eine Groupware sicher zu betreiben.

## 8.12.1 APP.5.1.A1

Groupware-Systeme müssen sicher installiert werden. Besonders Passwörter müssen sicher gewählt werden. Unbenutzte Komponenten müssen deaktiviert werden.

## Entsprechungen in VdS 3473

Es gibt keine Vorgaben für Groupware in VdS 3473.

## 8.12.2 APP.5.1.A2

Benutzerkonten müssen eine sichere Voreinstellung haben. Benutzer dürfen die Konfiguration nicht selbst ändern. Passwörter müssen sicher gespeichert werden. Übertragene Dateien müssen eine Maximalgröße haben und auf Schadsoftware untersucht werden. Es muss Regelungen für die Weiterleitung von E-Mails geben.

## Entsprechungen in VdS 3473

Es gibt keine Vorgaben für Groupware in VdS 3473.

<!-- page: 96 -->

## 8.12.3 APP.5.1.A3

Alle Sicherheitsupdates müssen installiert werden. Denial-of-Service Angriffe müssen verhindert werden. Daten müssen sicher übertragen werden. Auf das System dürfen nur berechtigte Nutzer Zugriff haben.

## Entsprechungen in VdS 3473

Es gibt keine Vorgaben für Groupware in VdS 3473

## 8.12.4 APP.5.1.A4

Daten von Groupware-Systemen müssen regelmäßig gesichert werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 8.13 APP.5.2 - Microsoft Exchange und Outlook

Microsoft Exchange ist eine Groupware-Software, welche meistens in mittleren und großen Unternehmen zum Einsatz kommt. Im letzten Baustein der APP-Gruppe gibt es Anforderungen, mit denen die allgemeinen Vorgaben aus APP .5.1 im Bezug auf Exchange-Systeme erweitert werden.

## 8.13.1 APP.5.2.A1 und A2

Der Einsatz der Exchange- und Outlook-Software muss umfangreich geplant werden. Dabei sind u. a. die E-Mail-Infrastruktur, verwendete Protokolle und vorgesehene Systeme zu berücksichtigen. Es muss festgelegt sein ob die Systeme lokal betrieben werden oder eine 'Could '-Lösung eingesetzt wird.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen.

## 8.13.2 APP.5.2.A3

Für die beteiligten Systeme muss es ein Berechtigungskonzept geben. Rechte müssen möglichst minimal gehalten werden.

<!-- page: 97 -->

## Entsprechungen in VdS 3473

Die VdS macht vergleichbare Anforderungen in Abschnitt 15.1 ihrer Richtlinie.

## Unterschiede

Die Anforderungen der VdS sind nicht direkt auf Exchange bezogen, sondern gelten allgemein für alle IT -Systeme. Im Wesentlichen ist die Anforderung aber erfüllt.

## 8.13.3 APP.5.2.A4

Benutzerprofile für den Zugriff auf Exchangedaten müssen serverseitig arbeiten. Die Dateien im Exchange-Verzeichnis dürfen nur für Administratoren zugänglich sein.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen.

## 8.13.4 APP.5.2.A5

Exchange-Systeme müssen regelmäßig und vor Änderungen gesichert werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen.

## 8.14 Fazit

Von den 79 Anforderungen der APP-Reihe werden von VdS 3473 lediglich 7 vollständig bzw. ohne große Unterschiede erfüllt. Bei 15 Anforderungen gibt es deutliche Abweichungen von den Vorgaben des BSI. Ganze 48 Anforderungen werden entweder gar nicht erfüllt oder es gibt erhebliche Unterschiede zwischen den Anforderungen.

Besonders in der hier betrachteten APP-Reihe macht sich der deutlich größere Umfang des IT-Grundschutzes bemerkbar. Das BSI stellt wesentlich genauere Anforderungen auf, diese gehen zum Teil sogar auf einzelne Aspekte der Konfiguration von Systemen und Anwendungen ein.

Erneut ist zu beobachten, dass VdS 3473 kein Kapitel enthält, welches sich mit den Besonderheiten von bestimmten Software-Systemen beschäftigt. Aus den allgemeinen Anforderungen für IT-Systeme lassen sich zwar 26 (Teil-) Anforderungen für einzelne Software-Produkte ableiten, insgesamt bestätigt der Vergleich der Anforderungen in dieser Baustein-Gruppe aber die großen Schutzlücken im Bereich von Anwendungen und technischen Details in VdS 3473.

<!-- page: 98 -->



<!-- page: 99 -->

## Kapitel 9

## SYS - IT-Systeme

## 9.1 Übersicht

Nachdem die APP-Gruppe Anforderungen für verschiedene Anwendungen gestellt hat, werden in der SYS-Gruppe Anforderungen für verschiedene IT-Systeme beschrieben.

## 9.2 SYS.1.1 - Allgemeiner Server

Der 1. Baustein in dieser Gruppe stellt Anforderungen an die Sicherheit von Servern auf. Server sind hier IT-Systeme, die anderen IT-Systemen Dienste anbieten.

## 9.2.1 SYS.1.1.A1

Server müssen in Räumen betrieben werden, zu denen nur Berechtigte Zugang haben. Server dürfen nicht als Arbeitsplatzrechner eingesetzt werden. Systeme mit Sicherungsfunktion müssen getrennt von den Systemen aufgestellt sein, die sie sichern sollen.

## Entsprechungen in VdS 3473

Punkt 16.3.2 von VdS 3473 schreibt vor, dass Sicherungssysteme in anderen Brandabschnitten sein müssen, als die Systeme, die sie sichern sollen.

Abschnitt 13.1 sieht vor, dass Server vor unberechtigtem Zugang zu schützen sind.

## Unterschiede

Die VdS verbietet nicht, dass Server auch als Arbeitsplatzrechner genutzt werden.

<!-- page: 100 -->

## 9.2.2 SYS.1.1.A2

Zur Nutzung eines Server ist eine Anmeldung erforderlich. Falls Passwörter verwendet werden müssen, diese sicher sein.

## Entsprechungen in VdS 3473

Punk 10.3.7 von VdS 3473 sieht eine geeignete Anmeldung an nicht öffentlichen IT-Systemen vor.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 9.2.3 SYS.1.1.A3

Nutzer dürfen auf Dateien des Servers nur zugreifen, wenn sie diese für ihre Arbeit benötigen. Zugriffsarten müssen an die erforderlichen Arbeiten angepasst werden (etwa keine Schreibrechte für ausführbare Dateien).

## Entsprechungen in VdS 3473

VdS 3473 sieht in Abschnitt 15.1 vor, dass nur notwendige Zugriffsrechte vergeben werden dürfen.

## Unterschiede

Die VdS macht keine Angaben zu Arten des Zugriffs, die Anforderung wird nur zum Teil erfüllt.

## 9.2.4 SYS.1.1.A4

Administratorkonten dürfen nur für entsprechende Aufgaben benutzt werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 9.2.5 SYS.1.1.A5

Administrationsaufgaben müssen mit sicheren Methoden und Protokollen durchgeführt werden.

<!-- page: 101 -->

## Entsprechungen in VdS 3473

Es gibt keine Vorgaben, die sich mit den Methoden der Administration beschäftigen.

## 9.2.6 SYS.1.1.A6

Auf Servern dürfen nur benötigte Dienste und Benutzerkennungen aktiv sein. Standardzugangsdaten müssen geändert werden.

## Entsprechungen in VdS 3473

Punkt 10.2.1 sieht vor, dass voreingestellte Zugangsdaten geändert werden müssen.

## Unterschiede

Die VdS sieht das Deaktivieren von nicht notwendigen Diensten gem. Punkt 10.5.3 nur bei kritischen IT -Systemen vor. Die Anforderung des BSI, ungenutzte Dienste auf allen Servern abzuschalten, ist damit nicht erfüllt. Die Anforderung des BSI wird also nur teilweise abgedeckt.

## 9.2.7 SYS.1.1.A7

Administratoren müssen sich regelmäßig über aktuelle Sicherheitslücken informieren. Erkannte Lücken müssen schellst möglich geschlossen werden. Updates dürfen nur von sicheren Quellen installiert werden.

## Entsprechungen in VdS 3473

In Punkt 10.3.1 von VdS 3473 wird das Installieren von Hersteller-Updates vorgeschrieben. Falls Sicherheitslücken nicht geschlossen werden können, muss der Netzwerkverkehr zu den betroffenen Systemen auf das notwendige Minimum beschränkt werden.

## Unterschiede

Obwohl die Anforderungen der VdS und des BSI beide dem gleichen Zweck dienen, ist die Anforderung des BSI hier weitgehender. Bei nicht geschlossenen Sicherheitslücken müssen 'geeignete Maßnahmen zum Schutz des Systems getroffen werden'. Die VdS sieht nur eine Beschränkung des Netzwerkverkehrs vor.

Die Anforderung von VdS 3473 ist zwar auf den ersten Blick genauer, kann aber in vielen Fällen nicht ausreichend sein. Es ist denkbar, dass auch Sicherheitslücken auftreten können, die trotz eines minimalen Datenverkehrs ausgenutzt werden können. Die Anforderung des IT-Grundschutzes ist somit nur zum Teil erfüllt.

<!-- page: 102 -->

## 9.2.8 SYS.1.1.A8

Vor Änderungen am System und in regelmäßigen Abständen müssen Sicherungen durchgeführt werden.

## Entsprechungen in VdS 3473

VdS 3473 beschreibt Anforderungen an die Datensicherung in Kapitel 16. Abschnitt 5 dieses Kapitels sieht vor, dass Sicherungen nicht älter als 24 Stunden sein dürfen und eine vollständige Wiederherstellung des Servers ermöglichen müssen.

## Unterschiede

In VdS 3473 wird nicht gefordert, dass Sicherungen vor einer Änderung im System durchgeführt werden. Die Anforderung wird damit nicht vollständig von VdS 3473 abgedeckt.

## 9.2.9 SYS.1.1.A9

Falls auf dem Server Antivirensoftware eingesetzt werden muss, ist es notwendig, dass diese u. a. über Echtzeitscans verfügt. Die Datenbanken der Software müssen regelmäßig aktualisiert werden. Das Untersuchen von komprimierten und verschlüsselten Daten muss möglich sein.

## Entsprechungen in VdS 3473

VdS 3473 sieht in Punkt 10.3.5 vor, dass alle Systeme einen Schutz vor Schadsoftware haben müssen.

## Unterschiede

Die VdS macht keine Angaben zu komprimierten oder verschlüsselten Dateien. Echtzeitschutz ist nur in einer 'SOLLTE'-Anforderung vorgesehen. Die Anforderungen des BSI werden somit nicht vollständig erfüllt.

## 9.2.10 SYS.1.1.A10

Es müssen Vorgaben für die Protokollierung auf Servern gemacht werden. Sicherheitsereignisse müssen immer aufgezeichnet werden. Welche Ereignisse dazu zählen wird in der Anforderung genau aufgeführt.

<!-- page: 103 -->

## Entsprechungen in VdS 3473

Die VdS verlangt ebenfalls, dass sicherheitsrelevante Ereignisse festgehalten werden.

## Unterschiede

Die Anforderungen weichen im Wesentlichen nicht voneinander ab.

## 9.3 SYS.1.2.2 - Windows Server 2012

Dieser Baustein erweitert die Anforderungen von SYS.1.1 um, die Besonderheiten die beim Einsatz von Windowsservern mit der Version 'Windows Server 2012' zu beachten sind.

## 9.3.1 SYS.1.2.2.A1

Der Einsatz von Windows Server 2012 muss umfangreich geplant werden. Dabei sind Hardwareanforderungen und der geplante Zweck des Server zu beachten. Microsoft-Konten dürfen nur eingerichtet werden, wenn sie benötigt werden.

## Entsprechungen in VdS 3473

Die VdS macht keine Angaben zu bestimmten Betriebssystemen.

## 9.3.2 SYS.1.2.2.A2

Installationsmedien für das Betriebssystem müssen aus einer sicheren Quellen stammen. Die Server-Core Variante ist zu bevorzugen. Während der Installation muss der Server auf den aktuellen Patch-Level gebracht werden.

## Entsprechungen in VdS 3473

Die VdS macht keine Angaben zu bestimmten Betriebssystemen.

## 9.3.3 SYS.1.2.2.A3

Lokale Adminstrationskonten müssen einzigartige, sichere Passwörter haben. Verantwortliche Administratoren müssen über die Sicherheitsaspekte des Betriebssystems Bescheid wissen. Webbrowser auf Windows Servern dürfen nicht im Internet benutzt werden.

<!-- page: 104 -->

## Entsprechungen in VdS 3473

Die VdS macht keine Angaben zu bestimmten Betriebssystemen.

## 9.4 SYS.1.3: Server unter Unix

Dieser Baustein erweitert die in SYS.1.1 gemachten Anforderungen um die besonderen Maßnahmen, die bei der Absicherung eines Unix-Servers zu beachten sind.

## 9.4.1 SYS.1.3.A1

Benutzer müssen sich zur Nutzung des Servers anmelden. Bei entfernten Anmeldungen müssen verschlüsselte Verbindungen genutzt werden. Nutzerkonten dürfen nur für den vorgesehenen Zweck verwendet werden.

## Entsprechungen in VdS 3473

VdS 3473 sieht vor, dass der Zugriff auf IT-Systeme durch Anmeldeverfahren gesichert wird (10.3.7).

## Unterschiede

Außer dem Schutz vor unberechtigter Nutzung gibt es keine weiteren Entsprechungen in VdS 3473, die zu den Anforderungen des BSI äquivalent sind. Die Anforderungen werden von VdS 3473 also nur teilweise umgesetzt.

## 9.4.2 SYS.1.3.A2

Jede Nutzer- und Gruppen-ID darf nur einmal verwendet werden. Jeder Benutzer muss Mitglied einer Gruppe sein, alle Gruppen müssen in der entsprechenden Datei aufgeführt sein. Nutzer dürfen nur Mitglied in Gruppen sein, wenn dies unbedingt nötig ist.

## Entsprechungen in VdS 3473

Es gibt keine Vorgaben zu Besonderheiten von Unix-Systemen in VdS 3473.

## 9.4.3 SYS.1.3.A3

Wechsellaufwerke dürfen nicht automatisch eingebunden werden.

<!-- page: 105 -->

## Entsprechungen in VdS 3473

Es gibt keine Vorgaben zu Besonderheiten von Unix-Systemen in VdS 3473.

## 9.4.4 SYS.1.3.A4

Im Kernel müssen Schutzmechanismen für Anwendungen aktiviert sein.

## Entsprechungen in VdS 3473

Es gibt keine Vorgaben zu Besonderheiten von Unix-Systemen in VdS 3473.

## 9.4.5 SYS.1.3.A5

Software muss vor der Installation auf Integrität geprüft werden. Vorbereitende Arbeiten der Installation dürfen nicht mit administrativen Rechten durchgeführt werden.

## Entsprechungen in VdS 3473

Es gibt keine Vorgaben zu Besonderheiten von Unix-Systemen in VdS 3473.

## 9.5 SYS.1.5 - Virtualisierung

IT-Systeme werden immer öfter als virtuelles System betrieben. Dabei stellt ein IT-System seine Rechenleistung zur Verfügung, um dann andere Systeme auf seiner Hardware auszuführen. Dieser Baustein beschreibt in 7 Anforderungen wie virtuelle Systeme (als Gäste bezeichnet) und die dazugehörigen realen Systeme (Hosts) abgesichert werden müssen um die Basisanforderungen des IT-Grundschutzes zu erfüllen.

## 9.5.1 SYS.1.5.A1

Software auf dem Host-System muss regelmäßig aktualisiert werden und zeitnah mit Sicherheitsupdates versorgt werden. Updates sind auf einem Testsystem zu prüfen.

## Entsprechungen in VdS 3473

In Punkt 10.3.1 werden Anforderungen gestellt, die äquivalent zu denen des BSI sind.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

<!-- page: 106 -->

## 9.5.2 SYS.1.5.A2

Zuständige Administratoren müssen wissen welchen Einfluss die Virtualisierung auf den IT-Betrieb hat. Zugriffsrechte für virtuelle Systeme müssen minimal sein.

Notwendige Netzwerkverbindungen für virtuelle Systeme müssen verfügbar sein. Anforderungen an Datenschutz und Leistung sowie an die Isolation von Systemen müssen beachtet werden.

## Entsprechungen in VdS 3473

In Abschnitt 15.1 von VdS 3473 wird vorgeschrieben, dass Zugriffsrechte so minimal wie möglich sein müssen.

## Unterschiede

Es gibt keine Anforderungen zu virtuellen Systemen in VdS 3473. Außer den Angaben zu Zugriffsberechtigungen, gibt es somit nur eine teilweise Abdeckung der Anforderungen des IT-Grundschutzes. Hier zeigt sich erneut der deutlich größere Umfang des Grundschutz-Kompendiums.

## 9.5.3 SYS.1.5.A3

Gast-Systeme dürfen nicht auf physische Geräte des Host-Systems zugreifen. Ausnahmen hiervon dürfen nur für unbedingt nötige Zeitabschnitte gemacht werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Anforderungen in VdS 3473.

## 9.5.4 SYS.1.5.A4

Sicherheitsmaßnahmen dürfen nicht durch virtuelle Systeme umgangen werden können.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Anforderungen in VdS 3473.

## 9.5.5 SYS.1.5.A5

Administrations-Schnittstellen für virtuelle Systeme dürfen nur von berechtigten Nutzern verwendet werden. Bei Verwendung von unverschlüsselten Verbindungen, für die Administration von virtuellen Systemen, muss ein eigenes Administrations-Netz verwendet werden.

<!-- page: 107 -->

## Entsprechungen in VdS 3473

In Punkt 10.3.7 von VdS 3473 wird beschrieben, dass Zugänge zu IT-Systemen ausreichend authentifiziert werden müssen.

Die Anforderungen in Punkt 11.4.3 besagen, dass der Zugriff auf IT-Systeme über weniger vertrauenswürdige Netze gesichert erfolgen muss.

## Unterschiede

Die Anforderungen der VdS beziehen sich zwar nicht explizit auf virtuelle Systeme, können aber für deren Absicherung herangezogen werden.

Wenn das eigene Unternehmens-Netz für die Administration wenig vertrauenswürdig ist, sieht VdS 3473 vor, dass gesicherte Verbindungen genutzt werden müssen. Die fehlende Anforderung eines eigenen Administrations-Netzes für unverschlüsselte Verbindungen wird dadurch ausgeglichen. Insgesamt ist die Anforderung des BSI durch VdS 3473 abgedeckt.

## 9.5.6 SYS.1.5.A6

Der Betriebszustand von virtuellen Systemen muss ständig überwacht werden. Bei unzureichender Leistung muss Abhilfe geschaffen werden.

## Entsprechungen in VdS 3473

Es gibt keine entsprechenden Anforderungen in VdS 3473.

## 9.5.7 SYS.1.5.A7

Die Zeit aller produktiv eingesetzten Systeme muss synchron sein.

## Entsprechungen in VdS 3473

Eine identische Anforderung der VdS findet sich in Punkt 10.3.3 der Richtlinie VdS 3473.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

<!-- page: 108 -->

## 9.6 SYS.1.8 - Speicherlösungen

Dieser Baustein beschäftigt sich mit IT-Systemen deren hauptsächlicher Zweck es ist Dateien für andere Systeme zu speichern. Dazu werden 5 Anforderungen beschrieben.

## 9.6.1 SYS.1.8.A1

Speicher-Systeme müssen in gesicherten Räumen stehen. Die Umgebung muss den Vorgaben des Herstellers entsprechen. Die Stromversorgung muss sicher sein.

## Entsprechungen in VdS 3473

In Abschnitt 13.1 wird vorgeschrieben, dass Server gegen unberechtigten Zugang geschützt werden müssen.

## Unterschiede

Angaben zur Stromversorgung oder Umgebung macht die VdS erst im Rahmen einer 'SOLLTE ' -Anforderung. Damit wird die Anforderung des BSI nur zum Teil erfüllt.

## 9.6.2 SYS.1.8.A2

Speichersysteme müssen vor ihrem Einsatz auf einen aktuellen Patch-Level gebracht und konfiguriert werden.

Ungenutzte Zugangsdaten und Schnittstellen müssen deaktiviert, Standardpasswörter geändert werden.

## Entsprechungen in VdS 3473

VdS 3473 fordert in Punkt 10.3.1, dass Sicherheitsupdates zeitnah installiert werden. Punkt 10.2.1 besagt, dass voreingestellte Zugangsdaten geändert werden müssen. Die Abschaltung von ungenutzten Schnittstellen ist in Punkt 11.4.1 beschrieben.

## Unterschiede

Die Anforderungen des BSI werden im Wesentlichen von VdS 3473 abgedeckt.

## 9.6.3 SYS.1.8.A3

Benutzerkonten müssen auf Speichersystemen mit minimalen Rechten angelegt werden.

<!-- page: 109 -->

## Entsprechungen in VdS 3473

Abschnitt 15.1 sieht vor, dass Nutzer nur die Rechte haben, die zur Erfüllung ihrer Aufgaben notwendig sind.

## Unterschiede

Die Anforderungen haben keine wesentlichen Unterschiede.

## 9.6.4 SYS.1.8.A4

Administrations-Zugänge müssen gesichert sein. Der administrative Zugriff darf nur aus vertrauenswürdigen Netzen geschehen.

## Entsprechungen in VdS 3473

In Punkt 10.3.8 wird in VdS 3473 vorgeschrieben, dass Nutzer keine administrativen Tätigkeiten ausüben dürfen.

Der Zugriff auf IT-Systeme darf, bei nicht vertrauenswürdigen Netzen, nur verschlüsselt erfolgen (11.4.3).

## Unterschiede

Die Anforderungen haben keine wesentlichen Unterschiede.

## 9.6.5 SYS.1.8.A5

Speichersysteme müssen Informationen protokollieren, die zur Behebung von Problemen erforderlich sind.

## Entsprechungen in VdS 3473

In Punkt 10.3.3 sieht VdS 3473 vor, dass IT-Systeme Fehler protokollieren.

## Unterschiede

Die Anforderungen haben keine wesentlichen Unterschiede.

<!-- page: 110 -->

## 9.7 SYS.2.1 - Allgemeiner Client

Baustein SYS.2.1 beschäftigt sich mit der Absicherung von Clients, unabhängig von ihrem Betriebssystem. Spezifische Anforderungen zu einzelnen Betriebssysteme werden in den Bausteinen SYS.2.2.2 und SYS.2.2.3 gestellt.

## 9.7.1 SYS.2.1.A1

Vor der Verwendung eines Client-Systems muss sich ein Benutzer sicher authentifizieren.

## Entsprechungen in VdS 3473

Eine äquivalente Anforderung wird in Punkt 10.7.3 von VdS 3473 aufgestellt.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 9.7.2 SYS.2.1.A2

Administrative Aufgaben dürfen nur von berechtigten Personen vorgenommen werden. Das alltägliche Arbeiten mit Administrator-Rechten ist nicht gestattet.

## Entsprechungen in VdS 3473

VdS 3473 sieht in Punkt 10.3.8 vor, dass Nutzer keine administrativen Tätigkeiten ausüben dürfen.

## Unterschiede

Die VdS sieht nicht vor, dass administrative Konten nicht für tägliche Arbeiten benutzt werden. Die Anforderungen des BSi wird nur teilweise erfüllt.

## 9.7.3 SYS.2.1.A3

Updates müssen regelmäßig eingespielt werden.

## Entsprechungen in VdS 3473

Eine äquivalente Anforderung ist in 10.3.1 von VdS 3473 aufgeführt.

<!-- page: 111 -->

## Unterschiede

Die Anforderungen unterscheiden sich nicht.

## 9.7.4 SYS.2.1.A4

Es muss ein Konzept zur Datensicherung geben. Daten, die nicht anderweitig wiederbeschafft werden können, müssen von einem Client gesichert werden. Der Sicherungsvorgang muss regelmäßig geprüft werden.

## Entsprechungen in VdS 3473

VdS 3473 sieht ebenfalls ein Konzept zur Datensicherung vor. Ein Testen des Verfahrens wird einmal pro Jahr verlangt.

## Unterschiede

Die Anforderungen unterschieden sich nicht.

## 9.7.5 SYS.2.1.A5

Client-Systeme müssen über eine Bildschirmsperre verfügen. Zu deren Deaktivierung muss sich der Anwender authentifizieren.

## Entsprechungen in VdS 3473

Punkt 10.3.7 der VdS-Richtlinie sieht in Satz (3) vor, dass Sitzungen beendet oder gesperrt werden wenn der Nutzer eine bestimmte Zeit inaktiv war.

## Unterschiede

Die Anforderung wird im Wesentlichen von VdS 3473 abgedeckt.

## 9.7.6 SYS.2.1.A6

Der Einsatz von Antivirensoftware muss geprüft werden. Wird eine solche Software verwendet muss diese einen Echtzeit-Scan haben, sich regelmäßig aktualisieren und darf vom Anwender nicht verändert werden können.

<!-- page: 112 -->

## Entsprechungen in VdS 3473

Ein Schutz vor Schadsoftware wird in Punkt 10.3.5 vorgeschrieben. Punkt 10.3.8 sieht vor, dass Anwender keine administrativen Tätigkeiten durchführen dürfen. Dazu können auch Änderungen an der Virenschutz-Software gezählt werden.

## Unterschiede

Echtzeit-Scans werden von der VdS als 'SOLLTE ' -Anforderung definiert und sind damit nicht in der Basisabsicherung enthalten.

## 9.7.7 SYS.2.1.A7

Sicherheitsereignisse müssen protokolliert werden.

## Entsprechungen in VdS 3473

Eine entsprechende Anforderung ist in Punkt 10.3.3. zu finden.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 9.7.8 SYS.2.1.A8

Der Startvorgang eines Client-Systems muss gesichert sein. Starten von Wechselmedien darf nur für Administratoren möglich sein.

## Entsprechungen in VdS 3473

Eine entsprechende Anforderung ist in Punkt 10.3.6. zu finden.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 9.8 SYS.2.2.2: Clients unter Windows 8.1

Dieser Baustein erweitert die allgemeinen Anforderungen von SYS.2.1 um die Besonderheiten, welche bei der Absicherung von Clients mit Windows 8.1-Betriebssystem beachtet werden müssen.

<!-- page: 113 -->

## 9.8.1 SYS.2.2.2.A1

Die Version des Betriebssystems, die verwendet werden soll, muss für den geplanten Einsatzzweck geeignet sein.

## Entsprechungen in VdS 3473

Es gibt keine gesonderten Anforderungen zu Windowsbetriebssystemen in VdS 3473.

## 9.8.2 SYS.2.2.2.A2

Es muss geprüft werden ob, neben den üblichen Verfahren, auch neuere Anmeldewege erlaubt sind, etwa die Anmeldung ber PIN.

## Entsprechungen in VdS 3473

VdS 3473 beschreibt in Punkt 10.3.7 dass geeignete Anmeldeverfahren eingesetzt werden müssen.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 9.8.3 SYS.2.2.2.A3

Es muss ein Schutz vor Schadsoftware vorhanden sein.

## Entsprechungen in VdS 3473

Wie im Vergleich von SYS.2.1.A6 beschrieben, wird der Schutz vor Schadsoftware auch in VdS 3473 gefordert.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 9.9 SYS.2.2.3: Clients unter Windows 10

Nachdem der vorherige Baustein die Anforderungen an Client-Systeme um Windows 8.1-spezifische Anforderungen ergänzt hat, werden in diesem Baustein Anforderungen für Version 10 des Windows-Betriebssystems gemacht.

<!-- page: 114 -->

## 9.9.1 SYS.2.2.3.A1

Es muss festgelegt werden welche Cloud-Dienste von Microsoft verwendet werden dürfen.

## Entsprechungen in VdS 3473

In Abschnitt 14.1 von VdS 3473 wird angefordert, dass alle Verwendungen von CloudSystemen vom Management genehmigt werden müssen.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 9.9.2 SYS.2.2.3.A2

Die Beschaffung des Betriebssystems muss an die geplanten Anforderungen angepasst werden.

## Entsprechungen in VdS 3473

Es gibt keine Vorgaben in VdS 3473, die sich mit der Beschaffung von Betriebssystemen beschäftigen.

## 9.9.3 SYS.2.2.3.A3

Es muss ein umfangreiches Patch-Management für Windows 10-Systeme geben. Darin müssen Kriterien für die Verteilung von Updates, Tests und Abbruchpunkte genannt werden.

## Entsprechungen in VdS 3473

VdS 3473 macht in Punkt 10.3.1 Anforderungen zu Sicherheitsupdates.

## Unterschiede

Es gibt zwar Anforderungen zum Installieren von Updates, diese beziehen sich aber nur auf Sicherheitsupdates und nicht auf allgemeine Änderungen an der Software. Das in VdS 3473 beschriebene Vorgehen ist auch nicht so detailreich, wie das des IT-Grundschutzes. Die Anforderung des BSI wird somit nicht von VdS 3473 abgedeckt, es gibt erhebliche Abweichungen.

<!-- page: 115 -->

## 9.9.4 SYS.2.2.3.A4

Windows 10 versendet umfangreiche Telemetrie-Daten von IT-Systemen an Server von Microsoft. Es müssen Maßnahmen ergriffen werden um dies zu verhindern.

## Entsprechungen in VdS 3473

Es gibt keine Anforderung in VdS 3473, die sich explizit mit Windows 10 beschäftigt. Die Anforderung wird nicht abgedeckt.

## 9.9.5 SYS.2.2.3.A5

Windows 10-Systeme müssen vor Schadsoftware geschützt werden.

## Entsprechungen in VdS 3473

Wie im Vergleich von SYS.2.1.A6 beschrieben, wird der Schutz vor Schadsoftware auch in VdS 3473 gefordert.

## Unterschiede

Es gibt keine Unterschiede in den Anforderungen.

## 9.9.6 SYS.2.2.3.A6

Anmeldungen an Clients dürfen nur mit Benutzerkonten aus einem lokalen Verzeichnisdienst möglich sein. Das Verwenden von Microsoft-Konten ist unzulässig.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

## 9.10 SYS.2.3 - Clients unter Unix

Die Anforderungen für allgemeine Clients werden in diesem Baustein erweitert, damit auch die Besonderheiten von Unix-Clients abgedeckt sind.

## 9.10.1 SYS.2.3.A1

Benutzer müssen sich vor Anmeldung authentifizieren. Administratoren dürfen das RootKonto (Ein Konto mit höchsten Berechtigungen) nicht für die alltägliche Arbeit benutzen.

<!-- page: 116 -->

## Entsprechungen in VdS 3473

Eine geeignete Authentifizierung wird in Punkt 10.3.7 von VdS 3473 verlangt.

## Unterschiede

Es gibt keine Anforderung, aus der hervorgeht, dass ein Administrator keine alltäglichen Arbeiten mit einem Administrator Konto durchführen darf.

## 9.10.2 SYS.2.3.A2

Es muss eine Distribution (Eine Distribution ist eine Version eines Unix-Betriebssystems) gewählt werden, die für den geplanten Einsatzzweck geeignet ist. Unnötige Software muss entfernt werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

## 9.10.3 SYS.2.3.A3

Es muss eine Distribution (Eine Distribution ist eine Version eines Unix-Betriebssystems) gewählt werden die für den geplanten Einsatzzweck geeignet ist. Unnötige Software muss entfernt werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

## Unterschiede

Es gibt keine Unterschiede in den Anforderungen.

## 9.10.4 SYS.2.3.A4

Verantwortliche müssen regelmäßig Informationen zu Schwachstellen einholen. Sicherheitsupdates müssen zeitnah installiert werden. Falls es für eine Sicherheitslücke keinen Patch gibt, muss mit anderen Maßnahmen Abhilfe geschaffen werden. Nach UpdateInstallationen müssen die Clients neu gestartet werden, oder das Kernel-Livepatching muss aktiviert sein.

<!-- page: 117 -->

## Entsprechungen in VdS 3473

Abschnitt 8.1 sieht vor, dass regelmäßig Informationen zu aktuellen Gefährdungen eingeholt werden. Das einspielen von Sicherheitsupdates wird in Punkt 10.3.1 vorgeschrieben.

## Unterschiede

In VdS 3473 sind keine Unix-spezifischen Besonderheiten berücksichtigt. Die Anforderung wird damit nur zum Teil abgedeckt.

## 9.10.5 SYS.2.3.A5

Ein Unix-Client darf nur mit notwendigen Anwendungen ausgestattet sein. Nicht benötigte Software muss entfernt werden. Vor der Installation einer Software ist deren Echtheit zu prüfen. Vorbereitende Maßnahmen für Installationen dürfen nicht mit Root-Rechten ausgeführt werden.

## Entsprechungen in VdS 3473

Für diese Unix-spezifischen Anforderungen gibt es keine Entsprechungen in VdS 3473.

## 9.11 SYS.3.1 - Laptops

Bisher wurden IT-Systeme als ortsfeste Objekte betrachtet. Mobile Geräte, hier Laptops, sind jedoch besonderen Gefahren ausgesetzt. In diesem Baustein werden Anforderungen gestellt, die sich damit beschäftigen, diesen besonderen Gefahren zu begegnen.

## 9.11.1 SYS.3.1.A1

Der Umgang mit mobilen IT-Systemen muss geregelt werden. Dabei sind auch Verhaltensregeln für die Nutzer von Laptops aufzustellen. Den Nutzern müssen diese Regeln bekannt gemacht werden.

## Entsprechungen in VdS 3473

VdS 3473 schreibt in Abschnitt 8.2 vor, dass Mitarbeiter generell in Bezug auf sie betreffende Gefahren sensibilisiert werden müssen. Abschnitt 19.4 stellt weitere Regeln für mobile IT-Systeme auf. In einer Informationssicherheitsrichtlinie muss der Umgang mit mobilen Systemen geregelt werden.

<!-- page: 118 -->

## Unterschiede

Die Anforderungen von VdS 3473 und IT-Grundschutz sind im Wesentlichen vergleichbar.

## 9.11.2 SYS.3.1.A2

Laptops müssen vor unberechtigter Nutzung geschützt werden. Die Einhaltung dieser Vorgabe muss überprüft werden.

## Entsprechungen in VdS 3473

Auch die VdS sieht einen Zugriffsschutz für IT-Systeme vor (Punkt 10.3.7).

## Unterschiede

In VdS 3473 wird nicht verlangt, dass die Einhaltung der Maßnahmen geprüft wird.

## 9.11.3 SYS.3.1.A3

Auf jedem Laptop muss eine Firewall installiert sein. Diese darf nur nötigen Netzverkehr passieren lassen. Benutzer dürfen keine Warnmeldungen erhalten, die sie nicht verstehen können.

## Entsprechungen in VdS 3473

Das Einschränken des Netzwerkverkehrs auf das Nötigste wird für kritische IT-Systeme in Punkt 10.5.3 gefordert.

## Unterschiede

Die Anforderung des IT-Grundschutzes gilt für alle Laptops. Die VdS sieht diese Maßnahmen erst bei kritischen Systemen vor, so dass eine Abdeckung der BSI-Anforderung durch VdS 3473 nicht gegeben ist.

## 9.11.4 SYS.3.1.A4

Auf Laptops müssen, abhängig vom Betriebssystem, Antiviren-Programme eingesetzt werden. Diese müssen dem Nutzer vertraut sein. Die Software muss stets auf dem aktuellen Stand gehalten werden. Anwender dürfen keine Änderungen an deren Einstellungen vornehmen. Sollte eine Infektion mit Schadprogrammen erkannt werden, muss das Gerät geeignet untersucht werden.

<!-- page: 119 -->

## Entsprechungen in VdS 3473

Punkt 10.3.8 verbietet administrative Arbeiten durch Benutzer. Punkt 10.3.5 sieht einen Schutz vor Schadsoftware für jedes IT-System vor.

## Unterschiede

Die VdS macht keine Angaben zum Vorgehen nach einer Vireninfektion.

## 9.11.5 SYS.3.1.A5

Auch auf Laptops müssen Datensicherungen durchgeführt werden. Diese muss möglichst automatisiert erfolgen.

## Entsprechungen in VdS 3473

In der Informationssicherheitsrichtlinie für mobile IT-Systeme (Punkt 10.4.1) muss auch die Datensicherung geregelt werden. Dies wird in Punkt 16.4.3 noch einmal um ein von Administratoren vorgegebenes Verfahren erweitert.

## Unterschiede

Die VdS macht keine Angaben zur Automatisierung der Datensicherung. Da viele Anwender solche Maßnahmen als 'lästig ' empfingen, besteht die Gefahr, dass eine manuelle Datensicherung nicht ausreichend oft ausgeführt wird. Die Anforderung wird daher nur zum Teil von VdS 3473 umgesetzt.

## 9.12 SYS.3.2.1 - Allgemeine Smartphones und Tablets

Die Bedeutung von Smartphones und Tablets hat in den letzten Jahren stark zugenommen, auch beim Einsatz in Unternehmen. Der Baustein 3.2.1 in der SYS-Reihe beschreibt Vorgaben, mit denen diese Geräte, unabhängig vom verwendeten Betriebssystem, abgesichert werden können.

## 9.12.1 SYS.3.2.1.A1

Der Umgang mit Smartphones und Tablets im Unternehmen muss geregelt werden.

## Entsprechungen in VdS 3473

In VdS3473 können die allgemeinen Vorgaben für mobile IT-Systeme herangezogen werden. Sie sind in Abschnitt 10.4 zu finden.

<!-- page: 120 -->

## Unterschiede

Die Anforderungen unterscheiden sich nicht.

## 9.12.2 SYS.3.2.1.A2

Die Nutzung von Cloud-Diensten muss geregelt werden. Nutzer müssen regelmäßig in diesem Bereich geschult werden.

## Entsprechungen in VdS 3473

Abschnitt 8.2 sieht die zielgruppenorientierte Schulung von Mitarbeitern vor. In Kapitel 14 macht die VdS umfangreiche Vorgaben zur Nutzung von Cloud-Lösungen.

## Unterschiede

Die Anforderungen der VdS an Cloud-Lösungen gehen deutlich über die des BSI hinaus. Bereits in der Basisabsicherung werden Dinge wie Vertragsgestaltung und ähnliches geregelt.

## 9.12.3 SYS.3.2.1.A3

Es muss eine dokumentierte, sichere Grundkonfiguration geben. Eine eventuell genutzte Mobile-Device-Management-Lösung muss bei Übergabe des Gerätes installiert sein.

## Entsprechungen in VdS 3473

Es gibt keine Anforderungen in VdS 3473, die ähnlich detailliert sind. Die Anforderung wird somit nicht abgedeckt.

## 9.12.4 SYS.3.2.1.A4

Geräte müssen über automatische Bildschirmsperren verfügen. Auf dem Sperrbildschirm dürfen keine vertraulichen Informationen erscheinen.

Nach mehreren fehlgeschlagenen Versuchen, die Sperre zu deaktivieren, muss sich das Gerät in den Werkszustand zurücksetzten.

## Entsprechungen in VdS 3473

Die VdS gibt in Punkt 10.3.7 vor, dass IT-Systeme über geeignete AuthentifizierungsMechanismen verfügen müssen.

<!-- page: 121 -->

## Unterschiede

VdS 3473 enthält keine Smartphone-/Tablet-speziefischen Anforderungen, etwa zum automatischen Zurücksetzten.

## 9.12.5 SYS.3.2.1.A5

Updates müssen, nachdem sie getestet wurden, automatisch installiert werden. Der Hersteller der Gräte muss auch nach längerer Zeit Updates bereitstellen, darauf ist bei der Anschaffung zu achten.

## Entsprechungen in VdS 3473

Für Sicherheitsupdates macht VdS in Punkt 10.3.1 vergleichbare Vorgaben.

## Unterschiede

Es gibt keine Vorgabe zur langfristigen Versorgung mit Updates durch Hersteller.

## 9.12.6 SYS.3.2.1.A6

Anwendungen dürfen nur auf notwendige Daten und Schnittstellen zugreifen. Dies gilt insbesondere für Kamera und Mikrofon.

## Entsprechungen in VdS 3473

In VdS 3473 gibt es keine Anforderungen, die denen des IT-Grundschutzes entsprechen.

## 9.12.7 SYS.3.2.1.A7

Sicherheitsereignisse oder der Verlust eines Gerätes müssen sofort gemeldet werden. Geeignete Gegenmaßnehmen müssen eingeleitet werden.

## Entsprechungen in VdS 3473

Äquivalente Anforderungen macht die VdS in Punkt 10.4.3 sowie in Abschnitt 18.2 und 18.3.

## Unterschiede

Es gibt keine Unterschiede in den Anforderungen.

<!-- page: 122 -->

## 9.12.8 SYS.3.2.1.A8

Anwendungen dürfen nicht aus fremden Märkten oder von Dateien installiert werden.

## Entsprechungen in VdS 3473

Für diese Anforderung gibt es keine Entsprechung in VdS 3473.

## 9.13 SYS.3.2.2: Mobile Device Management (MDM)

Ein MDM ermöglicht die Verwaltung einer großen Zahl von mobilen Geräten. Die Administration wird durch den Einsatz eines MDM-Systems erleichtert.

Dieser Baustein beschreibt Anforderungen, die beim Verwenden einer MDM-Lösung zu beachten sind.

Dabei werden unter anderem Vorgaben zur Planung von MDM-Systemen (Cloud-Lösung, eigener Betrieb, etc.) gemacht, wie auch zur Konfiguration der Geräte und zum Protokollieren von Ereignissen.

In VdS 3473 gibt es keine Angaben zu MDM-Systemen. Es finden sich auch keine Anforderungen, mit denen die Vorgaben des BSI wenigstens zum Teil abgedeckt werden (Ausnahme ist SYS.3.2.2.A6). Aus diesem Grund wird auf eine Betrachtung der Einzelnen Anforderungen dieses Bausteines verzichtet und auf die Tabelle in Anhang 2 verwiesen.

## 9.14 SYS.3.2.3 - iOS (for Enterprise)

Die Anforderungen dieses Bausteins beschreiben genauere Maßnahmen, die bei der Verwendung von iOS-Geräten umgesetzt werden müssen.

## 9.14.1 SYS.3.2.3.A1

Grundsätzlich muss ein MDM-System zur Verwaltung der Geräte eingesetzt werden. Es muss eine Strategie für die Auswahl geeigneter Geräte und Fremdanwendungen geben.

## Entsprechungen in VdS 3473

Für diese Anforderung gibt es keine Entsprechung in VdS 3473.

## 9.14.2 SYS.3.2.3.A2

Es muss eine Festlegung geben, ob die Cloud-Dienste des Herstellers verwendet werden.

<!-- page: 123 -->

## Entsprechungen in VdS 3473

Die VdS regelt die Verwendung von Cloud-Diensten umfangreich in Kapitel 14.

## Unterschiede

Das BSI legt nur fest, dass über die Verwendung von Cloud-Diensten entschieden werden muss. Es gibt keine weiteren Details dazu.

In VdS 3473 werden, im Gegensatz zu den Vorgaben des IT-Grundschutzes, bereits in der Basis-Absicherung umfangreiche Maßnahmen für Verträge und Ähnliches beschrieben.

## 9.14.3 SYS.3.2.3.A3

Abhängig vom Schutzbedarf muss ein geeigneter Gerätecode verwendet werden.

## Entsprechungen in VdS 3473

Die Vorgaben von Punkt 10.3.7 in VdS 3473 sehen eine geeignete Authentifizierung für nichtöffentliche Systeme vor.

## Unterschiede

Die Maßnahmen von VdS 3473 beziehen sich zwar nicht direkt auf iOS-Geräte, dienen aber im Wesentlichen dem gleichen Zweck wie die Vorgaben des IT-Grundschutzes.

## 9.14.4 SYS.3.2.3.A4 und A5

Je nach Schutzbedarf muss sich ein Gerät nach einer festgelegten Zeit sperren.

## Entsprechungen in VdS 3473

Punkt 10.3.7 sieht das Beenden oder Sperren von inaktiven Sitzungen vor. Diese Anforderung kann auch auf mobile Geräte angewendet werden.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 9.14.5 SYS.3.2.3.A6

Nach einer festgelegten Anzahl von fehlgeschlagenen Anmeldeversuchen muss das Gerät zurückgesetzt werden.

<!-- page: 124 -->

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 9.14.6 SYS.3.2.3.A7

Benutzer dürfen Konfigurationen nicht selbstständig verändern.

## Entsprechungen in VdS 3473

Eine denkbare Entsprechung ist Punkt 10.3.8. In diesem wird festgelegt, dass Nutzer keine administrativen Arbeiten durchführen dürfen.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 9.14.7 SYS.3.2.3.A8

Aktualisierungen des Betriebssystems müssen getestet und zeitnah eingespielt werden. Nicht mehr unterstützte Geräte müssen ausgemustert werden.

## Entsprechungen in VdS 3473

Punkt 10.3.1 sieht ein, zum BSI ähnliches, Verfahren vor, nach dem mit Updates umgegangen werden muss.

## Unterschiede

Es gibt keine Vorgabe zum Aussortieren von nicht mehr unterstützten Geräten.

## 9.15 SYS.3.2.4 - Android

Dieser Baustein nennt besondere Maßnahmen zum Schutz von Android-Geräten. In der Basis-Absicherung gibt es nur eine Anforderung, die umgesetzt werden muss.

## 9.15.1 SYS.3.2.4.A1

Bei den verwendeten Geräten muss sichergestellt sein, dass sie regelmäßig mit Updates versorgt werden.

<!-- page: 125 -->

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 9.16 SYS.3.4 - Mobile Datenträger

In diesem Baustein werden Anforderungen zur Sicherheit von mobilen Datenträgern beschrieben. Zu den mobilen Datenträgern zählen unter anderem USB-Sticks, CDs oder Magnetbänder.

## 9.16.1 SYS.3.4.A1

Mitarbeiter müssen in Bezug auf mobile Datenträger sensibilisiert werden.

## Entsprechungen in VdS 3473

Eine äquivalente Anforderung gibt es in Abschnitt 8.2.

## Unterschiede

Es gibt keine wesentlichen Unterschiede.

## 9.16.2 SYS.3.4.A2

Es muss Meldewege für den Verlust eines Datenträgers geben. Verluste müssen umgehend gemeldet werden.

## Entsprechungen in VdS 3473

Die VdS behandelt mobile Datenträger in Kapitel 12 ihrer Richtlinie. In Unterpunkt 12.2.3 wird vorgeschrieben, dass der Verlust kritischer, mobiler Datenträger zu melden ist.

## Unterschiede

Die VdS verlangt eine Meldung nur für kritische Datenträger. Die Anforderung des BSI ist damit nur zum Teil erfüllt.

## 9.16.3 SYS.3.4.A3

Es muss eine Sicherheitskopie von einzigartigen Daten auf mobilen Datenträgern geben.

<!-- page: 126 -->

## Entsprechungen in VdS 3473

Eine Anforderung, die sich explizit auf die in dieser Anforderung beschriebene Situation bezieht, gibt es in VdS 3473 nicht.

## 9.17 SYS.4.1 - Drucker, Kopierer und Multifunktionsgeräte

Besonders in größeren Verwaltungsbereichen gibt es oft zentrale Drucker und Kopierer, die von einer Vielzahl von Arbeitsplätzen aus verwendet werden. In diesem Baustein werden Anforderungen beschreiben, welche dabei helfen sollen die Verwendung solcher Systeme sicher zu gestalten.

## 9.17.1 SYS.4.1.A1

Vor dem Einsatz von Geräten muss deren Verwendung geplant werden. Unter anderem muss der Ort der Aufstellung und der Zugriff geregelt werden.

## Entsprechungen in VdS 3473

In VdS 3473 gibt es keine Maßnahmen, die auf diese spezifischen Anforderungen angewendet werden können.

## 9.17.2 SYS.4.1.A2

Geräte müssen an geeigneten Orten und vor unbefugtem Zugang geschützt aufgestellt werden. Benutzer müssen dahingehend geschult werden, dass sie keine vertraulichen Dokumente in Druckern liegen lassen.

## Entsprechungen in VdS 3473

Die Sensibilisierung in von Mitarbeitern wird in Abschnitt 8.2 behandelt.

## Unterschiede

Es gibt keine Angaben zur Aufstellung von Geräten.

## 9.17.3 SYS.4.1.A3

Geräte müssen regelmäßig aktualisiert werden. Falls es keine Updates für Sicherheitslücken gibt, muss andere Abhilfe geschaffen werden.

<!-- page: 127 -->

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473, die sich auf Drucker und ähnliche Geräte beziehen.

## 9.18 SYS.4.4 - Allgemeines IoT-Gerät

Der letzte Baustein in der SYS-Gruppe beschäftigt sich mit sogenannten 'Internet of Things'-Geräten (IoT-Geräte). Dabei handelt es sich um Geräte, welche klassischer Weise nicht vernetzt sind. Bekannte Beispiele dafür sind z. B. über das Netz gesteuerte Lampen. Die potenziell große Anzahl solcher Geräte und deren z. T. unzureichende Sicherheit stellt besondere Anforderungen an die Informationssicherheit in einem Unternehmen.

## 9.18.1 SYS.4.4.A1

IoT-Geräte müssen mit Updates versorgt werden. Die Geräte dürfen keine festen Zugangsdaten haben und über eine Funktion zur Authentifizierung verfügen.

## Entsprechungen in VdS 3473

In Punkt 10.3.7 wird festgelegt, dass Systeme über eine Authentifizierung verfügen müssen.

## Unterschiede

Es gibt in VdS 3473 keine weiteren Anforderungen an IoT-Geräte. Insbesondere fehlen Vorgaben zu festen Zugangsdaten und Herstellerupdates für IoT-Geräte.

## 9.18.2 SYS.4.4.A2

Bevor ein IoT-Gerät genutzt werden kann, muss es eine sichere Authentifizierung der Benutzer geben.

## Entsprechungen in VdS 3473

In Punkt 10.3.7 wird eine sichere Authentifizierung für den Zugriff auf Systeme gefordert.

## Unterschiede

Es gibt keine wesentlichen Unterschiede.

<!-- page: 128 -->

## 9.18.3 SYS.4.4.A3

IoT-Geräte müssen regelmäßig aktualisiert werden. Falls Sicherheitslücken bekannt sind müssen diese geschlossen werden.

## Entsprechungen in VdS 3473

Eine ähnliche Anforderung ist in wird in Punkt 10.3.1 von VdS 3473 beschrieben.

## Unterschiede

Es gibt keine wesentlichen Unterschiede.

## 9.18.4 SYS.4.4.A4

Falls es keine regelmäßige Wartung von IoT-Geräte gibt müssen Autoupdate-Funktionen genutzt werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

## 9.18.5 SYS.4.4.A5

Der Netzwerkverkehr von IoT-Geräten muss minimiert werden. Dazu werden detaillierte Vorgaben gemacht.

## Entsprechungen in VdS 3473

In VdS 3473 gibt es eine Vorgabe zum Beschränken des Netzwerkverkehrs nur für bestimmte Geräte. Viele IoT-Geräte dürften jedoch nicht zu diesen gehören, die Anforderung ist also nicht abgedeckt.

## 9.19 Fazit

In diesem Kapitel wurden 93 Anforderungen verglichen. Der Anteil der von VdS 3473 abgedeckten Anforderungen (33) ist fast gleich dem der nicht erfüllten Anforderungen (38). Es gibt außerdem 22 teilweise erfüllte Anforderungen.

Anders als in der APP-Gruppe, welche ähnlich umfangreich wie die SYS-Gruppe ist, kann die VdS durch ihre sehr allgemein formulierten Anforderungen einen großen Teil der IT-Grundschutz-Vorgaben erfüllen. Eine Anforderung ist sogar weitgehender als die Vorgaben des BSI.

<!-- page: 129 -->

Insgesamt zeigt sich aber auch in dieser Bausteingruppe, dass die meisten Anforderungen nicht von VdS 3473 abgedeckt werden, sobald es um technische Einzelheiten bzw. spezifische Maßnahmen für bestimmte Systeme geht.

<!-- page: 130 -->



<!-- page: 131 -->

## Kapitel 10

## IND - Industrielle IT

## 10.1 Übersicht

Speziell für IT -Systeme in Industrieanlagen gibt es die IND-Gruppe. Mit ihren 5 Bausteinen stellt sie gesonderte Anforderungen an die IT-Sicherheit in entsprechenden Anlagen.

Baustein IND.2.2 beschäftigt sich mit einer Sonderform der in IND.2.1 betrachteten Steuerungssysteme. Da der Baustein keine Basisanforderungen hat, wird er im Rahmen dieser Arbeit nicht betrachtet.

Obwohl Baustein IND.2.4 2 Anforderungen an die Basisabsicherung stellt, wird auch dieser Baustein nicht betrachtet. Grund dafür ist, dass es sich bei allen Punkten, die der Baustein in seinen beiden Anforderungen stellt, um 'SOLLTE'-Anforderungen handelt.

## 10.2 IND.1 - Betriebs- und Steuerungstechnik

Der erste Baustein der Gruppe stellt, ähnlich wie der ISMS-Baustein, allgemeine Anforderungen an die Organisation der Informationssicherheit in sog. operativen Anlagen.

## 10.2.1 IND.1.A1

Für die Betriebstechnik muss es entweder ein eigenes ISMS geben, oder dieses muss im ISMS für das Gesamtunternehmen enthalten sein. Verantwortlichkeiten müssen für den Betriebstechnik-Bereich explizit genannt werden. Verantwortlich für den Sicherheitsprozess ist, wie auch beim 'normalen' ISMS, die Leitungsebene.

## Entsprechungen in VdS 3473

In Abschnitt 4.2 verlangt die VdS, dass die Leitungsebene eines Unternehmens die Informationssicherheit in allen Bereichen Unternehmensbereichen vorantreibt.

<!-- page: 132 -->

## Unterschiede

Die VdS hat keine gesonderten Anforderungen an die Informationssicherheit in Betriebsanlagen. IT-Systeme in Betriebsanlagen müssen dem entsprechend wie alle anderen Systeme behandelt werden. Da Informationssicherheit alle Bereiche eines Unternehmens betreffen muss, ist die Anforderung durch VdS 3473 erfüllt.

## 10.2.2 IND.1.A2

Personal, das Umgang mit IT-Systemen aus dem Betriebsbereich hat, muss regelmäßig in Bezug auf Informationssicherheit geschult werden.

## Entsprechungen in VdS 3473

Die VdS sieht vor, dass Mitarbeiter regelmäßig entsprechend ihrer Zielgruppe, geschult werden (Abschnitt 8.2).

## Unterschiede

Die Anforderungen unterscheiden sich nicht.

## 10.2.3 IND.1.A3

Für Betriebs-IT-Systeme muss es ein Konzept zum Schutz vor Schadsoftware geben. Sollte Schutzsoftware verwendet werden, muss auf entsprechende Unterstützung der Hersteller geachtet werden oder geeigneter Ersatz umgesetzt werden.

Eingesetzte Virenschutz-Software muss stets aktuell gehalten werden, Signaturen dürfen jedoch nicht unmittelbar aus dem Internet bezogen werden, die Verbindungen müssen über sichere Proxyserver erfolgen.

## Entsprechungen in VdS 3473

Laut VdS müssen alle IT-Systeme mit einem Schutz vor Schadprogrammen versehen sein (Punkt 10.3.5).

## Unterschiede

Die VdS macht aber keine gesonderten Angaben zum Umgang mit Produktionsanlagen. Die Anforderungen des BSI sind hier also deutlich umfangreicher und werden nur zum Teil von VdS 3473 abgedeckt.

<!-- page: 133 -->

## 10.3 IND.2.1 - Allgemeine ICS-Komponente

Baustein 2 der IND-Reihe stellt Anforderungen an sogenannte 'Industrial Control Systems' (ICS). Darunter versteht man IT-Systeme, mit denen Maschinen oder andere Anlagen gesteuert werden.

Der Baustein zeigt Anforderungen auf, mit denen ICS unabhängig von ihrem Hersteller abgesichert werden müssen.

## 10.3.1 IND.2.1.A1

Nur befugte Mitarbeiter dürfen auf die Konfiguration von ICS zugreifen. Standard-Zugangsdaten müssen geändert werden, die neuen Zugangsdaten müssen sicher dokumentiert werden.

## Entsprechungen in VdS 3473

Laut Abschnitt 10.3.8 dürfen administrative Tätigkeiten nur von berechtigten Nutzern durchgeführt werden.

## Unterschiede

Da die VdS keine besonderen Anforderungen an ICS stellt, sind die Vorgaben des BSI im Vergleich deutlich umfangreicher. Die VdS deckt diese nur zum Teil ab.

## 10.3.2 IND.2.1.A2

Bei Durchführung von Wartungsarbeiten müssen sichere Übertragungsprotokolle verwendet werden.

## 10.3.3 Entsprechungen in VdS 3473

Es gibt keine Anforderung, die grundsätzlich eine gesicherte Übertragung von Zugangsdaten fordert.

## 10.3.4 IND.2.1.A3

Sicherheitsrelevante Ereignisse müssen protokolliert werden. Die Dauer, die Art und der Zugang zu den Protokollen müssen geregelt sein.

<!-- page: 134 -->

## Entsprechungen in VdS 3473

Die VdS schreibt in Punkt 10.3.3 ihrer Richtlinie allgemein vor, dass Ereignisse, welche für die Sicherheit relevant sind, für 6 Monate aufgezeichnet werden.

## Unterschiede

Zwar sind die Anforderungen der VdS nicht explizit auf ICS bezogen, sie gelten aber für alle IT -Systeme eines Unternehmens und somit auf für ICS. Die Anforderungen unterscheiden sich in diesem Punkt also nicht besonders voneinander.

## 10.3.5 IND.2.1.A4 bis A6

In ICS müssen alle ungenutzten Funktionen und Benutzernoten deaktiviert werden. ICS müssen von der sonstigen IT getrennt sein.

## Entsprechungen in VdS 3473

Die VdS verlangt in Punkt 10.5.3, dass auf kritischen Systemen alle Netzwerkdienste abgeschaltet werden, sofern diese nicht benötigt werden. Abschnitt 15.2 stellt eine solche Anforderung auch im Bezug auch Nutzerkonten auf.

In Punkt 11.4.2 stellt die VdS die Anforderung auf, dass eine '[. . . ] Segmentierung der Netzwerke [. . . ] geprüft werden [muss]'.

## Unterschiede

Die VdS verlangt das Deaktivieren von ungenutzten Funktionen nur im Bezug auf Netzwerkdienste und nur bei kritischen Systemen. Gleiches gilt für Benutzerkonten. Die Trennung der Netzwerke von Betriebsanlagen und sonstiger IT muss lediglich geprüft werden und ist nicht zwingend vorgesehen.

Die Anforderungen des IT-Grundschutzes sind auch hier deutlich genauer gefasst und lassen sich direkt in konkrete Maßnahmen umsetzen.

## 10.4 IND.2.3 - Sensoren und Aktoren

Dieser Baustein hat das Ziel 'intelligente Sensoren' abzusichern. Dabei sollen die gestellten Anforderungen möglichst unabhängig von einem konkreten Hersteller umsetzbar sein.

In der Basisabsicherung hat der Baustein nur eine Anforderung.

<!-- page: 135 -->

## 10.4.1 IND.2.3.A1

Sensoren müssen für die Umgebung, in der sie genutzt werden sollen, geeignet sein. Außerdem müssen sie geeignet installiert werden.

## Entsprechungen in VdS 3473

Die VdS hat keine vergleichbaren Anforderungen in ihrer Richtlinie. Wie bei den meisten anderen Bausteinen aus der IND-Reihe, ist der IT-Grundschutz auch hier viel umfangreicher.

## 10.5 Fazit

Es zeigt sich, dass der IT-Grundschutz wesentlich mehr Bereiche abdeckt als VdS 3473. Auch im Mittelstand gibt es eine große Zahl von Unternehmen mit Produktionsanlagen. Besondere Sicherheitsvorgaben für diese sind in VdS 3473 nicht vorhanden. Die allgemeinen Vorgaben, die für alle IT-Systeme gelten, reichen hier nicht aus um ein Sicherheitsniveau zu erreichen, das mit dem IT-Grundschutz vergleichbar wäre.

Von 10 Anforderungen werden nur 3 erfüllt. 5 werden nur zum Teil erfüllt, ohne dabei auf Besonderheiten von Industrieanlagen einzugehen. 2 Anforderungen sind gar nicht erfüllt.

<!-- page: 136 -->



<!-- page: 137 -->

## Kapitel 11

## NET - Netze und Kommunikation

## 11.1 Übersicht

Fast jedes IT-System ist durch Netze mit anderen Systemen verbunden. Netze sind in vielen Unternehmen ein wichtiger Teil der IT-Infrastruktur und müssen entsprechend geschützt werden. Die Bausteine in der NET-Gruppe stellen aus diesem Grund Anforderungen an die Sicherheit von Netzen.

## 11.2 NET.1.1 - Netzarchitektur und -design

Der erste Baustein der Gruppe beschreibt Anforderungen, die noch vor dem Betrieb eines Netzes umgesetzt werden müssen. Bereits bei der Planung des späteren Netzes müssen Sicherheitsaspekte berücksichtigt werden, damit das Netz selbst möglichst wenig Angriffsfläche bietet.

## 11.2.1 NET.1.1.A1

Es muss eine eigene Sicherheitsrichtlinie für Netze geben. Darin muss u. a. beschrieben werden, welche Kommunikationswege (z. B. WLAN), Protokolle und Sicherheitszonen im Netz genutzt werden. Die Richtlinie muss allen betroffenen Mitarbeitern bekannt sein.

## Entsprechungen in VdS 3473

Die VdS macht zwar Angaben über die Dokumentation eines Netzes, es gibt jedoch keine Vorgabe, welche die Erstellung einer eigenen Informationssicherheitsrichtlinie für Netze fordert.

<!-- page: 138 -->

## 11.2.2 NET.1.1.A2

Das Netz muss dokumentiert sein. In der Dokumentation muss ein Netzplan enthalten sein, aus welchem auch die logische Organisation des Netzes hervorgeht.

## Entsprechungen in VdS 3473

Abschnitt 11.1 von VdS 3473 regelt die Dokumentation eines Netzes. Die dort gemachten Anforderungen entsprechen im Wesentlichen denen des BSI.

## Unterschiede

Es gibt keine Unterschiede.

## 11.2.3 NET.1.1.A3

Mit Hilfe der in Anforderung (1) erstellten Sicherheitsrichtlinie muss eine Anforderungsspezifikation für das Netz erstellt werden.

## Entsprechungen in VdS 3473

Da die VdS keine explizite Erstellung einer Sicherheitsrichtlinie vorsieht, kann auch keine weitere Spezifikation von Anforderungen vorgenommen werden. Die Anforderung wird entsprechend nicht von VdS 3473 abgedeckt.

## 11.2.4 NET.1.1.A4

Ein Unternehmensnetz muss in 3 Bereiche aufgeteilt werden: internes Netz, demilitarisierte Zone und äußeres Netz (mit Internetanbindung). Die Bereiche müssen jeweils durch eine Firewall getrennt sein, welche nur ausdrücklich erlaubten Datenverkehr passieren lässt.

## Entsprechungen in VdS 3473

In Abschnitt 11.3 wird vorgeschrieben, dass geprüft werden muss wo Netzübergänge zu weniger vertrauenswürdigen Netzen vorhanden sind und wie diese geschützt werden müssen. In Punkt 11.4.2 wird gefordert, dass eine Segmentierung des Netzes geprüft werden muss.

<!-- page: 139 -->

## Unterschiede

Die VdS verzichtet darauf genaue Maßnahmen zu fordern. Auf Seiten des IT-Grundschutz wird recht genau beschrieben wie Netzübergänge zu sichern sind. Auch eine Segmentierung des Netzes ist zwingend vorgesehen, während die VdS nur verlangt dass diese zu Prüfen ist.

## 11.2.5 NET.1.1.A5

Clients und Server müssen in verschiedenen Netzsegmenten sein, die durch Firewalls geschützt werden. Netzwerke, in denen häufig unbekannte Geräte aktiv sind ('Gastnetze '), müssen in einem eigenem Segment sein.

## Entsprechungen in VdS 3473

In VdS 3473 sind keine so genauen technischen Anforderungen beschrieben.

## 11.2.6 NET.1.1.A6

In einem Netzsegment dürfen nur Geräte mit einem ähnlichen Sicherheitsbedarf vorhanden sein.

## Entsprechungen in VdS 3473

Eine solche Vorgabe gibt es in VdS 3473 nicht.

## 11.2.7 NET.1.1.A7

Vertrauliche Informationen müssen innerhalb eines sicheren Netzsegmentes oder über sichere Protokolle ausgetauscht werden.

## Entsprechungen in VdS 3473

Zur Erfüllung dieser Anforderung kann Punkt 11.4.3 herangezogen werden. Dieser beschreibt in Unterpunkt (1), dass Informationen beim Transport durch weniger sichere Netze geschützt werden müssen.

## Unterschiede

Es gibt keine wesentlichen Unterschiede.

<!-- page: 140 -->

## 11.2.8 NET.1.1.A8

Der Verkehr zum Internet muss gem. Anforderung (4) gestaltet sein. Die Firewalls dürfen dabei nur den unbedingt notwendigen Datenverkehr zulassen.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbar genaue Anforderung in VdS 3473.

## 11.2.9 NET.1.1.A9

Für jedes Netz muss die Vertrauenswürdigkeit bestimmt werden. Netze, welche nicht vertrauenswürdig sind, müssen wie das Internet behandelt werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbar genaue Anforderung in VdS 3473.

## 11.2.10 NET.1.1.A10

Eingehender Zugriff darf nur auf Systeme erfolgen, die mit einer Firewall in einer DMZ abgetrennt sind.

## Entsprechungen in VdS 3473

Es gibt keine ähnlich genaue Anforderung in VdS 3473.

## 11.2.11 NET.1.1.A11

Der Zugriff auf interne Netzbereiche muss über sichere Wege (z. B. VPN) erfolgen.

## Entsprechungen in VdS 3473

Punkt 11.4.3 stellt vergleichbare Anforderungen auf.

## Unterschiede

Es gibt keine wesentlichen Unterschiede.

## 11.2.12 NET.1.1.A12

Ausgehender Datenverkehr muss über einen Proxy geleitet werden. Der Proxy-Server darf nicht im internen Netzsegment sein.

<!-- page: 141 -->

## 11.3. NET.1.2 - NETZMANAGEMENT

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

## 11.2.13 NET.1.1.A13

Bei der Implementierung eines Netzes muss die in Anforderung (1) erstellte Richtlinie beachtet werden. Außerdem muss berücksichtigt werden wie das Netz mit dem Internet verbunden wird, wie die Administration geregelt ist und welche Protokolle zulässig sind.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

## 11.2.14 NET.1.1.A14

Das geplante Netz muss fachgerecht umgesetzt werden. Diese Umsetzung ist bei der Abnahme zu prüfen.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

## 11.2.15 NET.1.1.A15

Es muss regelmäßig geprüft werden, ob das Netz den Anforderungen entspricht.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

## 11.3 NET.1.2 - Netzmanagement

Nachdem sich der erste Baustein dieser Gruppe mit dem Planen von Netzen beschäftigt hat, widmet sich der zweite Baustein dem Verwalten des Netzes. Dabei werden Anforderungen an verschiedene Aspekte der Administration gestellt.

## 11.3.1 NET.1.2.A1

Für die Verwaltung eines Netzes muss u. a. festgelegt werden welche Protokolle verwendet werden, wie zentrale Managementserver angesprochen werden oder wie Protokolle weiter verarbeitet werden.

<!-- page: 142 -->

## Entsprechungen in VdS 3473

Es gibt keine Abschnitte in VdS 3473, die sich mit der Verwaltung eines Netzes befassen und vergleichbare Anforderungen stellen.

## 11.3.2 NET.1.2.A2

Ausgehend von der in Anforderung (1) gemachten Planung müssen spezifische Anforderungen für alle Netzmanagementprozesse erstellt werden.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 11.3.3 NET.1.2.A3

Es muss ein eigenes Berechtigungskonzept für das Netzmanagement geben.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 11.3.4 NET.1.2.A4

Der Zugriff auf Netzmanagementsysteme muss geeignet gesichert sein.

## Entsprechungen in VdS 3473

In Punkt 10.3.7 von VdS 3473 wird vorgeschrieben, dass der Zugriff auf alle IT-Systeme geeignet gesichert werden muss.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 11.3.5 NET.1.2.5

Verantwortliche Mitarbeiter müssen sich regelmäßig über Sicherheitsprobleme in der eingesetzten Netzmanagementsoftware informieren. Updates für die Software müssen kurzfristig installiert werden.

<!-- page: 143 -->

## Entsprechungen in VdS 3473

Das Installieren von Sicherheitsupdates wird in Punkt 10.3.1 vorgeschrieben. In Abschnitt 8.1 wird eine Anforderung beschrieben, aus welcher hervorgeht, dass regelmäßig Informationen über aktuelle Entwicklungen im Bereich Informationssicherheit eingeholt werden müssen.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 11.3.6 NET.1.2.6

Systeme zur Netzverwaltung müssen regelmäßig gesichert werden. Dabei müssen deren spezifischen Daten berücksichtigt werden.

## Entsprechungen in VdS 3473

Bezogen auf aktive Netzkomponenten macht die VdS äquivalente Anforderungen in Punkt 16.5.3.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 11.3.7 NET.1.2.7

Netzmanagementsysteme müssen Sicherheitsereignisse protokollieren.

## Entsprechungen in VdS 3473

Eine äquivalente Anforderung wird in Punkt 10.3.3 beschrieben.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 11.3.8 NET.1.2.8

Alle Netzmanagementsysteme müssen auf die selbe Uhrzeit eingestellt sein.

<!-- page: 144 -->

## Entsprechungen in VdS 3473

Eine äquivalente Anforderung wird in Punkt 10.3.3 beschrieben.

## Unterschiede

Es gibt keine Unterschiede zwischen den Anforderungen.

## 11.3.9 NET.1.2.9

Die Kommunikation des Netzmanagements muss entweder über sichere Protokolle oder über ein eigenes Netz erfolgen.

## Entsprechungen in VdS 3473

Es gibt keine entsprechende Anforderung in VdS 3473.

## 11.3.10 NET.1.2.10

Bei der Verwendung von SNMP (Simple Network Management Protocol) muss entweder eine sichere Version verwendet werden oder es muss auf anderem Wege Abhilfe geschaffen werden.

## Entsprechungen in VdS 3473

Es gibt keine entsprechende Anforderung in VdS 3473.

## 11.4 NET.2.1 - WLAN-Betrieb

Dieser Baustein beschreibt Anforderungen, durch deren Umsetzung ein Unternehmen sicher WLANs einsetzen kann.

## 11.4.1 NET.

Vor dem Einsatz von WLAN im Unternehmen muss geplant werden in welchen Bereichen WLAN eingesetzt werden soll und für welche Zwecke es genutzt werden darf. Auch die Zuständigkeiten müssen definiert werden.

## Entsprechungen in VdS 3473

Es gibt keine Anforderung in VdS 3473, die sich mit der Planung des WLAN-Einsatzes beschäftigt.

<!-- page: 145 -->

## 11.4.2 NET.2.1.A2

Bei der Planung des WLAN-Einsatzes müssen andere Geräte berücksichtigt werden, wenn diese Strahlen im Frequenzbereich des WLAN abgeben. Außerdem dürfen nur Geräte mit sicheren WLAN-Standards bei der Planung berücksichtigt werden.

## Entsprechungen in VdS 3473

Es gibt keine Anforderung in VdS 3473, die sich mit der Planung des WLAN-Einsatzes beschäftigt.

## 11.4.3 NET.2.1.A3

WLAN-Verkehr muss mindestens mit dem Standard 'WPA2 ' gesichert werden. Falls dabei auf Passworte zurückgegriffen wird, müssen diese mindestens 20 Zeichen lang sein.

## Entsprechungen in VdS 3473

Es gibt keine ähnlichen Anforderungen in VdS 3473.

## 11.4.4 NET.2.1.A4

Zugangspunkte müssen vor fremden Zugang geschützt werden. Die Funkwellen sollten sich möglichst nur in Bereichen ausbreiten können in denen dies gewünscht ist. Bei Einsatz von WLAN im Außenbereich muss auf geeignete Wetterschutzmaßnahmen geachtet werden.

## Entsprechungen in VdS 3473

Abschnitt 13.1 sieht vor, dass aktive Netzkomponenten gegen unberechtigten Zugang geschützt werden müssen.

## Unterschiede

Die VdS deckt durch ihre eher allgemein gehaltene Anforderung nur einen Teil der Anforderungen des BSI ab. Angaben zu Witterungsschutz oder Funkwellenausbreitung fehlen hier.

<!-- page: 146 -->

## 11.4.5 NET.2.1.A5

WLAN-Zugangspunkte müssen unmittelbar nach Inbetriebnahme sicher konfiguriert werden.

## Entsprechungen in VdS 3473

Es gibt keine entsprechende Anforderung in VdS 3473.

## 11.4.6 NET.2.1.A6

Sollte ein Client seine WLAN-Schnittstelle längere Zeit nicht benötigen, muss die Schnittstelle deaktiviert werden. Außerdem darf eine WLAN-Schnittstelle nicht genutzt werden um getrennte Netze zu verbinden, wenn dies nicht vorgesehen ist.

## Entsprechungen in VdS 3473

Es gibt keine entsprechende Anforderung in VdS 3473.

## 11.4.7 NET.2.1.A7

Beim Aufbau eines Distributions Systems muss entschieden werden ob dieses physisch oder logisch getrennt wird.

## Entsprechungen in VdS 3473

Es gibt keine entsprechende Anforderung in VdS 3473.

## 11.4.8 NET.2.1.A8

Bei Sicherheitsvorfällen mit WLAN-Geräten sind spezielle Maßnahmen umzusetzen.

## Entsprechungen in VdS 3473

VdS 3473 macht keine gesonderten Angaben zu Vorfällen mit WLAN-Geräten.

## 11.5 NET.2.2 - WLAN-Nutzung

Dieser Baustein richtet sich an die Benutzer von WLAN-Geräten. Unter Anderem werden Vorgaben für die Schulung der Mitarbeiter gestellt.

<!-- page: 147 -->

## 11.5.1 NET.2.2.A1

Es muss eine Benutzerrichtlinie für den Umgang mit WLAN geben. Unter anderem muss dort beschrieben werden wie Sicherheitsmaßnahmen umgesetzt und eingehalten werden müssen. Außerdem muss festgelegt sein, welche Informationen ein Anwender über WLAN übertragen darf.

## Entsprechungen in VdS 3473

Die VdS sieht zwar vor, dass der ISB den Bedarf für weitere Informationssicherheitsrichtlinien prüfen muss, es wird aber keine konkrete Angabe für WLANs gemacht. Die Anforderung des BSI wird somit nicht (ausreichend) von VdS 3473 abgedeckt.

## 11.5.2 NET.2.2.A2

Nutzer müssen über die speziellen Besonderheiten bei der WLAN-Nutzung aufgeklärt werden. Ihnen müssen außerdem die entsprechenden Richtlinien bekannt gemacht werden.

## Entsprechungen in VdS 3473

Die Sensibilisierung des Personals wird in Abschnitt 8.2 von VdS 3473 beschrieben.

## Unterschiede

Da die VdS keine gesonderte Richtlinie für den WLAN-Einsatz vorsieht, kann diese auch nicht den Mitarbeitern bekannt gemacht werden. Die Anforderung wird also nur teilweise abgedeckt. Außerdem sind die Anforderungen der VdS in diesem Punkt sehr allgemein gehalten, die Vorgaben des BSI sind deutlich umfangreicher.

## 11.5.3 NET.2.2.A3

Bei der Verwendung von fremden WLANs müssen dem Benutzer die Sicherheitsanforderungen bekannt sein. Der Zugriff auf vertrauliche Daten muss über ein VPN erfolgen.

## Entsprechungen in VdS 3473

Zur Abdeckung dieser Anforderung kann Punkt 11.4.3 herangezogen werden. Dort wird festgelegt, dass der Zugriff auf vertrauliche Daten des Unternehmens über nicht vertrauenswürdige Netze gesichert werden muss.

<!-- page: 148 -->

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 11.6 NET.3.1 - Router und Switches

Router und Switches sind die grundlegenden Bestandteile eines Netzes. Dieser Baustein beschreibt die Anforderungen um diese sicher betreiben zu können.

## 11.6.1 NET.3.1.A1

Router und Switches müssen vor Inbetriebnahme von einem berechtigtem Mitarbeiter sicher konfiguriert werden. Auf dem Gerät dürfen nur notwendige Dienste, Protokolle sowie Schnittstellen aktiv sein. Zugriffsrechte müssen auf das Notwendige beschränkt und mit sicheren Passworten versehen sein.

## Entsprechungen in VdS 3473

VdS 3473 sieht in Punkt 10.3.8 vor, dass Benutzer keine administrativen Arbeiten durchführen dürfen. In Punkt 10.3.7 wird vorgeschrieben, dass der Zugriff auf IT-Systeme geeignet gesichert sein muss. Außerdem dürfen gem. Abschnitt 15.1 nur unbedingt notwendige Rechte an Benutzer vergeben werden.

## Unterschiede

Die VdS sieht nicht vor, dass auf Routern und Switches nur notwendige Dienste aktiv sind.

## 11.6.2 NET.3.1.A2

Administratoren müssen sich regelmäßig über aktuelle Sicherheitslücken informieren. Erkannte Lücken müssen schnellst möglich geschlossen werden. Updates dürfen nur von sicheren Quellen installiert werden. Falls keine Sicherheitsupdates verfügbar sind muss andere Abhilfe geschaffen werden.

## Entsprechungen in VdS 3473

Herstellerupdates müssen gemäß Punkt 10.3.1 zeitnah installiert werden. Falls Sicherheitslücken nicht geschlossen werden können, muss der Netzwerkverkehr zu den betroffenen Systemen auf das notwendige Minimum beschränkt werden.

<!-- page: 149 -->

## Unterschiede

Die VdS sieht bei unbehandelten Sicherheitslücken nur eine Beschränkung des Netzverkehrs vor. Es sind jedoch Situationen denkbar, in denen diese Maßnahme nicht ausreichend ist. Die Anforderungen des BSI sind in diesem Punkt weitgehender.

## 11.6.3 NET.3.1.A3

Zugriffsrechte für Router und Switches dürfen nur nach dem Minimalprinzip vergeben werden. Alltägliche Arbeiten dürfen nicht mit erhöhten Rechten ausgeführt werden.

## Entsprechungen in VdS 3473

Auch VdS 3473 sieht eine minimale Rechtevergabe vor. Diese ist in Abschnitt 15.1 beschrieben.

## Unterschiede

Die VdS sieht nicht vor, dass Administratorzugänge nur für administrative Aufgaben genutzt werden.

## 11.6.4 NET.3.1.A4

Administrationszugänge müssen auf den Zugriff durch festgelegte IP-Adressen beschränkt werden. Falls keine sicheren Protokolle für die Administration verwendet werden können, muss ein Administrationsnetz verwendet werden. Der Zugang zu physischen Schnittstellen für die Administration muss gesichert sein.

## Entsprechungen in VdS 3473

In VdS 3473 gibt es keine Anforderungen, die ausreichend geeignet sind, um die Vorgaben des BSI abzudecken.

## 11.6.5 NET.3.1.A5

Es muss ein Schutz vor Fragmentierungsangriffen auf IP-Ebene in Routern und Switches vorhanden sein.

## Entsprechungen in VdS 3473

Für diese Anforderung gibt es keine Entsprechung in VdS 3473.

<!-- page: 150 -->

## 11.6.6 NET.3.1.A6

Der Zugriff auf Router und Switches muss für Administratoren auch bei einem totalen Netzausfall möglich sein.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 11.6.7 NET.3.1.A7

Geräte müssen Änderungen an der Konfiguration, fehlgeschlagene Login-Versuche sowie systembezogene Ereignisse protokollieren.

## Entsprechungen in VdS 3473

Eine vergleichbare Anforderung wird in Punkt 10.3.3 beschrieben.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 11.6.8 NET.3.1.A8

Konfigurationsdaten von Routern und Switches müssen gesichert werden.

## Entsprechungen in VdS 3473

Punkt 16.5.3 stellt eine äquivalente Anforderung auf.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 11.6.9 NET.3.1.A9

Die Aufgaben eines Routers/Switches müssen dokumentiert sein.

## Entsprechungen in VdS 3473

Abschnitt 10.1 sieht vor, dass der Einsatzzweck eines IT-Systems dokumentiert wird. Die Anforderungen sind also identisch.

<!-- page: 151 -->

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 11.7 NET.3.2 - Firewall

Dieser Baustein enthält Anforderungen, die speziell für den sicheren Betrieb von Firewalls gedacht sind.

## 11.7.1 NET.3.2.A1

Für den Einsatz von Firewalls muss eine eigene Informationssicherheitsrichtlinie existieren. Diese muss allen betroffenen Mitarbeitern bekannt sein, ihre Umsetzung muss regelmäßig geprüft werden.

## Entsprechungen in VdS 3473

Die VdS sieht keine eigene Informationssicherheitsrichtlinie für den Bereich 'Firewalls' vor.

## 11.7.2 NET.3.2.A2

Der Datenverkehr zwischen Netzen muss durch eine Firewall geregelt werden. Diese darf keine unzulässigen Verbindungen akzeptieren. Verbindungen von außen in das interne Netz sind grundsätzlich unzulässig. Für die Erstellung und Änderung von Firewall-Regeln muss es festgelegte Verantwortlichkeiten geben. Alle Schritte müssen dokumentiert werden.

## Entsprechungen in VdS 3473

Abschnitt 11.3 macht Angaben zur Dokumentation von Sicherheitseinstellungen auf Netzübergangspunkten.

## Unterschiede

Außer der Dokumentationspflicht, gibt es in VdS 3473 keine weiteren Vorgaben für den Umgang mit Firewalls. Die Anforderungen des BSI sind somit nur zum Teil erfüllt.

## 11.7.3 NET.3.2.A3

Nach den in Anforderung Zwei definierten Regeln müssen Einstellungen an Paketfiltern vorgenommen werden. Protokolle sollten möglichst restriktiv gefiltert werden.

<!-- page: 152 -->

## Entsprechungen in VdS 3473

Es gibt keine Entsprechungen in VdS 3473.

## 11.7.4 NET.3.2.A4

Eine Firewall muss sicher konfiguriert werden. Insbesondere müssen ungenutzte Funktionen deaktiviert werden. Die Konfiguration darf nur durch berechtigte Mitarbeiter erfolgen. Alle Einstellungen müssen dokumentiert sein.

## Entsprechungen in VdS 3473

Die VdS verbietet in Punkt 10.3.8 dass Benutzer administrative Aufgaben durchführen können.

## Unterschiede

Außer den Vorgaben für administrative Aufgaben, gibt es keine weiteren Anforderungen in VdS 3473, die sich auf Firewalls beziehen.

## 11.7.5 NET.3.2.A5

Benutzerrechte auf Firewalls müssen restriktiv vergeben werden. Nur wenn diese unbedingt nötig sind dürfen sie gewährt und verwendet werden.

## Entsprechungen in VdS 3473

In Abschnitt 15.1 wird das Vergeben von Rechten auf das Nötigste beschränkt.

## Unterschiede

## 11.7.6 NET.3.2.A6

Diese Anforderung ist, im Wesentlichen, identisch mit Anforderung NET.3.1.A4. Es wird darum auf die dortigen Ergebnisse verwiesen.

## 11.7.7 NET.3.2.A7

Diese Anforderung ist, im Wesentlichen, identisch mit Anforderung NET.3.1.A6. Es wird darum auf die dortigen Ergebnisse verwiesen.

<!-- page: 153 -->

## 11.7.8 NET.3.2.A8

Grundsätzlich muss eine Firewall dynamisches Routing verhindern.

## Entsprechungen in VdS 3473

Es gibt keine Entsprechung in VdS 3473.

## 11.7.9 NET.3.2.A9

Firewalls müssen sicherheitsrelevante Ereignisse sowie Fehlermeldungen protokollieren.

## Entsprechungen in VdS 3473

Punkt 10.3.3 macht vergleichbare Anforderungen.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 11.7.10 NET.3.2.A10

Der Paketfilter muss Fragmentierungsangriffe abwehren.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 11.7.11 NET.3.2.A11

Verantwortliche Mitarbeiter müssen sich regelmäßig über Sicherheitslücken in Firewalls informieren. Updates müssen zeitnah eingespielt werden.

## Entsprechungen in VdS 3473

Das Installieren von Sicherheitsupdates wird in Punkt 10.3.1 vorgeschrieben. In Abschnitt 8.1 wird eine Anforderung beschrieben, aus welcher hervorgeht, dass regelmäßig Informationen über aktuelle Entwicklungen im Bereich Informationssicherheit eingeholt werden müssen.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

<!-- page: 154 -->

## 11.7.12 NET.3.2.A12

Das Vorgehen bei einem registrierten Angriff muss definiert sein.

## Entsprechungen in VdS 3473

Die VdS beschreibt das Vorgehen bei Sicherheitsvorfällen in den Abschnitten 17.1 und 17.2. Das dort beschriebene Vorgehen deckt die Anforderungen des BSI ab.

## 11.7.13 Unterschiede

Es gibt keine wesentlichen Unterschiede in den Anforderungen.

## 11.7.14 NET.3.2.A13

Die Konfiguration von Firewalls muss regelmäßig und bei Änderungen gesichert werden.

## Entsprechungen in VdS 3473

Eine vergleichbare Anforderung ist in Punkt 16.5.3 beschrieben.

## Unterschiede

Es gibt keine wesentlichen Unterschiede zwischen den Anforderungen.

## 11.7.15 NET.3.2.A14

Die Aufgaben einer Firewall und deren Konfiguration sowie Änderungen der Konfiguration müssen (automatisch) dokumentiert werden. Die Dokumentation muss vor unbefugter Einsicht geschützt sein.

## Entsprechungen in VdS 3473

Abschnitt 10.1 beschreibt das Dokumentieren des Einsatzzwecks eines IT-Systems.

## Unterschiede

Die VdS sieht keine automatische Protokollierung von Konfigurationsänderungen vor. Auch muss die Konfiguration nicht explizit vor fremden Zugriff geschützt werden. Da es sich bei den Einstellungen einer Firewall um besonders kritische Informationen handelt, erscheinen die Vorgaben der VdS hier nicht genau genug. Die Anforderung wird nur zum Teil abgedeckt.

<!-- page: 155 -->

## 11.7.16 NET.3.2.A15

Bei der Beschaffung einer Firewall sind die Vorgaben der Informationssicherheitsrichtlinie aus Anforderung (1) zu beachten. Insbesondere müssen die zusätzlichen Besonderheiten von IPv6 berücksichtigt werden.

## Entsprechungen in VdS 3473

Für die Beschaffung einer Firewall gibt es keine Vorgaben in VdS 3473.

## 11.8 Fazit

In dieser Bausteingruppe wurden 60 Anforderungen vergleichen. Die meisten dieser Anforderungen werden von VdS 3473 nicht abgedeckt (34 Anforderungen). Damit zeigt sich erneut, dass der IT-Grundschutz deutlich umfangreicher und genauer ist. Bei den meisten der nicht abgedeckten Anforderungen handelt es sich um technische Details. Da VdS 3473 jedoch eher allgemein gehalten ist, finden sich entsprechend wenige technische Vorgaben. Der größte Teil der verbleibenden Anforderungen wird von VdS 3473 erfüllt (16 Anforderungen). Dies sind meistens organisatorische oder sehr allgemein gehaltene Vorgaben.

Wie bei den vorherigen Bausteingruppen finden sich nur wenige Anforderungen (10), die nur teilweise erfüllt sind. Bei diesen Anforderungen handelt es sich meistens um Vorgaben, bei denen es einen allgemeinen Teil gibt, der auch von VdS 3473 abgedeckt wird. Oft sind damit aber auch weitergehende Anforderungen verbunden, die dann nicht mehr erfüllt werden.

<!-- page: 156 -->



<!-- page: 157 -->

## Kapitel 12

## INF - Infrastruktur

## 12.1 Übersicht

Die letzte Gruppe des IT-Grundschutz-Kompendiums beschäftigt sich mit der Infrastruktur, die nötig ist um IT-Systeme zu betreiben. Unter anderem gibt es in dieser Gruppe Anforderungen zu Verkabelung oder Gebäuden an sich.

## 12.2 INF.1 - Allgemeines Gebäude

Im ersten Baustein dieser Gruppe sind Anforderungen an ein Gebäude vorhanden, die erfüllt werden müssen damit der sichere Betrieb von IT-Systemen möglich ist.

## 12.2.1 INF.1.A1

Abhängig von der Verwendung des Gebäudes und dem Schutzbedarf müssen die verschiedenen Sicherheitsmaßnahmen aus den Bereichen Brandschutz, Zutritt, Umwelt und Informationssicherheit aufeinander abgestimmt werden.

## Entsprechungen in VdS 3473

In VdS 3473 gibt keine Anforderungen an die Sicherheit von Gebäuden.

## 12.2.2 INF.1.A2

Ein Unternehmen muss regelmäßig prüfen ob die vorhandenen Stromkreise noch den Anforderungen entsprechen.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

<!-- page: 158 -->

## 12.2.3 INF.1.A3

Alle Brandschutzvorgaben müssen eingehalten werden. Für die IT-Systeme muss es ein eigenes Brandschutzkonzept geben. Eine Person im Unternehmen muss als Brandschutzbeauftragter fungieren.

## Entsprechungen in VdS 3473

Die VdS macht zum Thema Brandschutz nur eine Randvorgabe in Punkt 17.3.1: Datensicherungen müssen in anderen Brandabschnitten gelagert werden als die Originaldaten. Eine allgemeine Aussage zum Thema Brandschutz gibt es jedoch nicht. Die Anforderung wird nicht von VdS 3473 abgedeckt.

## 12.2.4 INF.1.A4

In Gebäuden muss es ein Rauchmeldesystem geben, welches einen Alarm auslösen kann. Das System sowie die Fluchtwege müssen regelmäßig überprüft werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.2.5 INF.1.A5

Es muss eine ausreichende Anzahl an Feuerlöschern im Gebäude vorhanden sein.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.2.6 INF.1.A6

Mitarbeiter müssen angewiesen werden nach außen führende Türen und Fenster bei verlassen eines Raumes zu schließen. Die Einhaltung dieser Vorgabe muss regelmäßig geprüft werden. Brandschutztüren dürfen nicht dauerhaft offen gehalten werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

<!-- page: 159 -->

## 12.2.7 INF.1.A7

Falls erforderlich, muss es eine Zutrittskontrolle zu Gebäuden geben. Diese muss regelmäßig überprüft werden und darf nur Personen Zutritt gewähren die diesen unbedingt benötigen.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.2.8 INF.1.A8

In besonders schutzbedürftigen Bereichen muss ein Rauchverbot verhängt werden. Raucherzonen dürfen die Zutrittsregeln nicht beeinträchtigen.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.3 INF.2 - Rechenzentrum sowie Serverraum

Dieser Baustein erweitert die allgemeinen Regeln aus INF.1 um weitere Vorgaben, welche sind dem besonderen Schutzbedarf von Serverräumen und Rechenzentren widmen.

## 12.3.1 INF.2.A1

Bei der Planung eines Rechenzentrums müssen Sicherheitsaspekte berücksichtigt werden. Unter anderem muss es verschiedene Sicherheitsbereiche geben, welche z. B. die IT von der Logistik trennen. Versorgungsleitungen (z. B. für Wasser oder Gas) sollten möglichst nicht in der Nähe von IT-Systemen verlaufen.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.3.2 INF.2.A2

Im Gebäude müssen geeignete Brandabschnitte vorhanden sein. Diese müssen die Ausbreitung von Rauch verhindern.

<!-- page: 160 -->

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.3.3 INF.2.A3

Wichtige Systeme müssen mit einer unterbrechungsfreien Stromversorgung (USV) ausgestattet sein, diese muss regelmäßig geprüft werden. Ein System darf nicht mit anderen Systemen über leitende Verbindungen verbunden sein, wenn es mit einer USV betreiben wird.

## Entsprechungen in VdS 3473

Die VdS sieht einen Schutz vor fehlerhafter Stromversorgung gem. Abschnitt 13.3 für Kritische Systeme vor.

## Unterschiede

Die Vorgaben des IT-Grundschutzes sind genauer formuliert und weitreichender als die der VdS. Im Wesentlichen erfüllen beide Anforderungen aber den gleichen Zweck.

## 12.3.4 INF.2.A4

Ein Rechenzentrum muss auf einfachem Wege vollständig von allen Spannungsquellen getrennt werden können. Die Abschalteinrichtung muss vor unabsichtlicher Benutzung geschützt werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.3.5 INF.2.A5

Die Temperatur und Luftfeuchtigkeit in Serverräumen und Rechenzentren muss in den vom Hersteller eines IT-Systems vorgegebenen Grenzwerten liegen und regelmäßig überprüft werden. Sollte es zu Abweichungen kommen müssen die Werte dieser beiden Parameter für eine angemessene Zeit aufgezeichnet werden.

## Entsprechungen in VdS 3473

VdS 3473 sieht einen Schutz vor falschen Umgebungsbegingungen nur für kritische Systeme vor (Abschnitt 13.3). Die Anforderung wird daher nicht erfüllt.

<!-- page: 161 -->

## 12.3.6 INF.2.A6

Rechenzentren müssen vor unberechtigtem Zutritt geschützt werden. Mitarbeiter dürfen nur Bereiche betreten wenn dies für ihre Arbeit erforderlich ist. Fremdpersonal muss während des Aufenthalts begleitet werden. Für alle Zutrittswege muss es eine geeignete Überwachung geben. Die Einhaltung dieser Maßnahmen muss überwacht werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.3.7 INF.2.A7

Türen und Fenster zu Rechenzentren müssen stets verschlossen gehalten werden, wobei Fenster möglichst nicht vorhanden sein sollten. Türen und Fenster müssen ausreichenden Schutz vor Einbruchsversuchen bieten. Alle baulichen Komponenten eines Rechenzentrums müssen ein einheitliches Sicherheitsniveau haben.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.3.8 INF.2.A8

Alle Flächen in einem Rechenzentrum müssen mit einer Brandmeldeanlage ausgestattet sein, welche Alarme angemessen weiterleitet und regelmäßig geprüft wird. Brandabschnitte in denen ein Rechenzentrum liegt müssen frei von besonderen Brandlasten sein.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.3.9 INF.2.A9

Rechenzentren müssen eine geeignete Brandbekämpfungsanlage haben. Handfeuerlöscher müssen gut erreichbar sein und regelmäßig geprüft werden. Alle Mitarbeiter müssen wissen wie ein Feuerlöscher verwendet wird.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

<!-- page: 162 -->

## 12.3.10 INF.2.A10

Technische Anlagen und Leitungen durch Brandwände müssen regelmäßig geprüft werden. Die Ergebnisse der Prüfung müssen dokumentiert werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.3.11 INF.2.A11

Störungen müssen automatisch überwacht werden und als Alarm schnell an die Verantwortlichen Mitarbeiter weitergeleitet werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.4 INF.3 - Elektrotechnische Verkabelung

Elektrische Leitungen müssen geschützt werden um Störungen und Ausfällen entgegenzuwirken. Anforderungen dazu finden sich in diesem Baustein.

## 12.4.1 INF.3.A1

Kabel müssen entsprechend des Einsatzzwecks, der Umgebung und der rechtlichen Vorgaben ausgewählt werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.4.2 INF.3.A2

Kabelstrecken müssen ausreichend Platz bieten, auch für spätere Erweiterungen. Mögliche Gefahrenquellen müssen umgangen werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

<!-- page: 163 -->

## 12.4.3 INF.3.A3

Die Installation von Kabeln muss Fach- und Normgerecht erfolgen. Der Auftraggeber muss dies bei allen Schritten der Verlegung überprüfen. Eine Beschädigung der Kabel darf nicht durch normale Nutzung des Gebäudes möglich sein.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.5 INF.4 - IT-Verkabelung

Die Anforderungen dieses Baustein haben das Ziel, Datenleitungen so zu sichern, dass diese nicht abgehört werden können.

## 12.5.1 INF.4.A1

Neben den Umgebungsbedingungen müssen bei Datenleitungen auch Aspekte wie Übertagungsrate und die Entfernung zum Ziel berücksichtigt werden. Die Kabel müssen geeignet ausgewählt werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.5.2 INF.4.A2

Kabelstrecken müssen ausreichend Platz bieten, auch für spätere Erweiterungen. Mögliche Gefahrenquellen müssen umgangen werden.

## Entsprechungen in VdS 3473

In Abschnitt 13.2 schreibt VdS 3473 vor, dass Datenleitungen durch bautechnische Maßnahmen vor Schäden geschützt werden müssen.

## Unterschiede

Die VdS macht kein Angaben zu Kabelkanälen und ähnlichem.

<!-- page: 164 -->

## 12.5.3 INF.4.A3

Die Installation von Kabeln muss Fach- und Normgerecht erfolgen. Der Auftraggeber muss dies bei allen Schritten der Verlegung überprüfen. Eine Beschädigung der Kabel darf nicht durch normale Nutzung des Gebäudes möglich sein. Darüber hinaus müssen Datenkabel getrennt von Stromleitungen verlegt sein.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.6 INF.7 - Büroarbeitsplatz

Die Anforderungen in diesem Baustein sollen Informationen schützen die in Büroräumen verarbeitet werden.

## 12.6.1 INF.7.A1

Büroräume müssen für die Tätigkeit geeignet sein, insbesondere müssen rechtliche Vorgaben eingehalten werden. Falls es in einem Büroraum Publikumsverkehr gibt, darf dieser nicht in einem Sicherheitsbereich liegen.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.6.2 INF.7.A2

Beim verlassen von Büroräumen müssen alle Fenster und Türen geschlossen sein. Brandschutztüren müssen ebenfalls geschlossen gehalten werden.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.7 INF.8 - Häuslicher Arbeitsplatz

Dieser Baustein beschreibt wie man eine sichere Infrastruktur an einem Heimarbeitsplatz betreiben kann.

<!-- page: 165 -->

## 12.7.1 INF.8.A1

Vertrauliche Informationen dürfen an Heimarbeitsplätzen nicht für unbefugte zugänglich sein, es muss eine entsprechende Anzahl von abschließbaren Schränken (o. ä.) vorhanden sein.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.7.2 INF.8.A2

Das Unternehmen muss regeln welche Informationen an einem Heimarbeitsplatz verarbeitet werden dürfen. Die Informationen müssen gesichert transportiert werden.

## Entsprechungen in VdS 3473

Die VdS macht in Kapitel 12 Vorgaben für mobile Datenträger die denen des BSI entsprechen.

## Unterschiede

In VdS 3473 werden nur Datenträger betrachtet. Die Anforderung des IT-Grundschutzes bezieht sich jedoch auch auf Dokumente in Papierform. VdS 3473 deckt damit nur einen Teil der Anforderung ab.

## 12.7.3 INF.8.A3

Es muss sichergestellt werden, dass an Heimarbeitsplätzen kein unbefugter Zutritt zu Unternehmensdaten und -IT erfolgen kann. Mitarbeitern sind entsprechende Anweisungen zu geben, deren Einhaltung regelmäßig zu prüfen ist.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.8 INF.9: Mobiler Arbeitsplatz

Dieser Baustein soll es ermöglichen mobile Arbeitsplätze ähnlich sicher zu betreiben wie einen Arbeitsplatz in einem Büro.

<!-- page: 166 -->

## 12.8.1 INF.9.A1

Das Unternehmen muss regeln unter welchen Bedingungen eine Umgebung als mobiler Arbeitsplatz genutzt werden kann und welche Informationen an einem solchen verarbeitet werden dürfen.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbare Anforderung in VdS 3473.

## 12.8.2 INF.9.A2

Es muss festgelegt werden welche Informationen unterwegs bearbeitet werden dürfen und wie diese dabei zu schützen sind. Außerdem muss der Zugriff mit mobilen Systemen auf interne Informationen geregelt werden. Darüber hinaus muss geregelt sein welche Systeme, von wem mobil genutzt werden dürfen. Entsprechende Vorgänge müssen dokumentiert werden. Für betroffene Mitarbeiter muss es Schulungen geben.

## Entsprechungen in VdS 3473

In VdS 3473 ist gibt es regeln für den Umgang mit mobilen IT-Systemen. Diese sind in Abschnitt 10.4 zu finden und entsprechen im Wesentlichen den Vorgaben des BSI. Das zielgruppengerechte sensibilisieren von Mitarbeitern wird in Abschnitt 8.2 beschrieben.

## Unterschiede

Zwischen den Anforderungen gibt es keine wesentlichen Unterschiede.

## 12.8.3 INF.9.A3

Mitarbeitern müssen die Regeln bekannt gemacht werden, die verhindern das unbefugte Zugang zu vertraulichen Informationen bekommen. Unter anderem müssen Zugänge zu Räumen geschossen werden und Clients bei verlassen des Raumes gesperrt werden.

## Entsprechungen in VdS 3473

Punkt 10.3.7 sieht vor, dass ungenutzte Clients gesperrt werden müssen.

<!-- page: 167 -->

## Unterschiede

Außer den Angaben zu Client-Systemen gibt es keine Vorgaben in VdS 373, die denen des BSI gerecht werden. Da die meisten Vorgaben des BSI nicht von VdS 3473 abgedeckt werden, ist diese Anforderung nicht erfüllt.

## 12.8.4 INF.9.A4

Bei der Verarbeitung von Informationen auf fremden IT-Systemen müssen Mitarbeiter besondere Maßnahmen ergreifen. Unter anderem müssen temporäre Daten gelöscht werden.

## Entsprechungen in VdS 3473

VdS 3473 betrachtet keine fremden IT-Systeme.

## 12.9 INF.10 - Besprechungs-, Veranstaltungs- und Schulungsräume

In den Räumen, denen dieser Baustein gewidmet ist, werden oft IT-Systeme betrieben und Besucher erwartet. Diese Kombination erfordert einige besondere Vorsichtsmaßnahmen, die in den Anforderungen dieses Bausteins beschrieben sind.

## 12.9.1 INF.10.A1

Geräte die in den Räumen betrieben werden müssen ausreichend vor Diebstahl geschützt werden. Außerdem muss definiert werden welche IT-Systeme Besucher benutzten dürfen und wer für die Administration verantwortlich ist.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Vorgaben in VdS 3473.

## 12.9.2 INF.10.A2

Besucher müssen beaufsichtigt werden, wenn sie sich außerhalb von 'Besucherräumen' aufhalten.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Vorgaben in VdS 3473.

<!-- page: 168 -->

## 12.9.3 INF.10.A3

Zugänge zu Besucherräumen müssen geschlossen gehalten werden, sobald die Räume verlassen werden. Des gilt insbesondere für Feuerschutztüren.

## Entsprechungen in VdS 3473

Es gibt keine vergleichbaren Vorgaben in VdS 3473.

## 12.10 Fazit

In dieser Bausteingruppe zeigt sich besonders deutlich der größere Umfang des IT-Grundschutzes. Es gibt lediglich 2 Anforderungen die von VdS 3473 abgedeckt sind, 3 sind teilweise erfüllt. Mit 32 Anforderungen ist der größte Teil der BSI Vorgaben nicht erfüllt. Die erheblichen Differenzen zwischen den beiden Regelwerken können darauf zurückgeführt werden, dass es in VdS 3473 keine Vorgaben zu Infrastruktur gibt. Die Richtlinie der VdS bezieht sich nur auf unmittelbare Aspekte der Informationssicherheit und lässt Nebenbereiche außen vor.

Der IT-Grundschutz hingegen betrachtet, u. a. wegen seiner Eignung für große Unternehmen, auch Bereiche die nicht unmittelbar mit IT-Systemen zu tun haben, aber einen Einfluss auf die Sicherheit von Informationen haben können.

<!-- page: 169 -->

## Kapitel 13

## Fazit

## 13.1 Analyse der Ergebnisse

Bei einer abschließenden Betrachtung der Ergebnisse, bestätigt sich das Bild, dass sich bereits beim Vergleich der einzelnen Bausteingruppen ergeben hat. Mehr als die Hälfte (52 %) der Basisanforderungen des IT-Grundschutzes werden nicht von VdS 3473 erfüllt. Eine vollständige Abdeckung der BSI-Vorgaben durch VdS 3473 ist nur bei 30 % der Anforderungen gegeben. Bei 18 % der Anforderungen ist eine teilweise Abdeckung gegeben.

Die Anteile der nicht, teilweise und ganz erfüllten Anforderungen lassen sich auf die Unterschiede in den Ansätzen des BSI und der VdS zurückführen. Mit seinem Bausteinprinzip hat das BSI zum Teil sehr genaue, technische Vorgaben gemacht, die sich auf eine einzelne Art von IT-Systemen bzw. auf einen speziellen Bereich der Informationssicherheit beziehen (etwa Vorgaben zur Rechtevergabe auf Unix-Systemen). Diese detaillierten Anforderungen machen einen großen Teil der Basisanforderungen im IT-Grundschutz-Kompendium aus. VdS 3473 ist dem entgegenstehend jedoch sehr allgemein formuliert. Es gibt nur wenige genaue, technische Vorgaben. Die meisten Basisanforderungen können dementsprechend nicht von VdS 3473 abgedeckt werden.

Dazu kommt, dass die VdS einige Bereiche in ihrer Richtlinie gar nicht betrachtet. Der IT-Grundschutz macht bspw. umfangreiche Vorgaben zu Software, verschiedenen Arten von IT-Systemen und zur umliegenden Infrastruktur. Diese Bereiche werden in VdS 3473 (fast) nicht betrachtet, so dass selbst allgemeine Anforderungen dazu fehlen.

Die Anteile der zweitgrößten Gruppe, die Gruppe der vollständig erfüllten Anforderungen, ist zu einem großen Teil auf die allgemeinen Vorgaben der VdS zurückzuführen. Während das BSI z. B. IT-Systeme nach Betriebssystemen getrennt betrachtet, spricht die VdS von IT-Systemen im Allgemeinen. Damit werden mit einer Vorgabe viele einzelne Anforderungen des IT-Grundschutzes abgedeckt, jedoch nur solange es sich dabei um eher oberflächliche Aspekte handelt. Außerdem macht die VdS viele Vorgaben zur Organisation des Informationssicherheitsmanagements und kann die meisten Anforderungen des BSI aus diesem Bereich erfüllen.

<!-- page: 170 -->

Den kleinsten Anteil haben die teilweise erfüllten Anforderungen. Aufgrund der Unterschiede, die in diesem Abschnitt diskutiert wurden, gibt es nur wenige Anforderungen, bei denen es zu einer Abweichung kommen kann. Dabei handelt es sich oft um Anforderungen des IT-Grundschutzes, die einen allgemeinen oder organisatorischen Aspekt mit genaueren Vorgaben verbinden. VdS 3473 deckt den allgemeinen Teil der Anforderung ab, jedoch nicht den genaueren Teil. Würden diese Vorgaben des IT-Grundschutzes in einzelne Anforderungen aufgeteilt werden, würde der Anteil der teilweise erfüllten Anforderungen, zu Gunsten der beiden anderen Gruppen, noch kleiner werden. Die noch verbleibenden Anforderungen in dieser Gruppe wären dann Vorgaben, bei denen VdS und BSI zwar das gleiche Ziel haben, die Vorgaben der VdS jedoch weniger weit gehen. Beispielhaft dafür sind die Anforderungen für Virenschutz-Software: Das BSI sieht vor, dass eine solche Software einen Echtzeitschutz und einen 'On-Demand-Scan' haben muss. Die VdS sieht dies in der Basisabsicherung nicht vor, sondern spricht nur allgemein von einem Schutz vor Schadsoftware. Dies ist u. a. in APP .3.3.A3 der Fall.

Es sei noch angemerkt, dass es eine 4. Gruppe von Anforderungen gibt. Diese Gruppe macht einen sehr kleinen Anteil aus, soll aber nicht unerwähnt bleiben. Beim Vergleich der einzelnen Anforderungen fanden sich einige wenige Vorgaben, bei denen die Anforderungen des BSI hinter denen der VdS zurückliegen. In der Tabelle in Anhang (1) sind solche Anforderungen mit einem Kommentar versehen, in der Grafik in Anhang (2) wurden sie jedoch nicht gesondert erfasst.

## 13.2 Schlussfolgerungen für das Sicherheitsniveau

Die hier dargestellten Ergebnisse zeigen eindeutig, dass die Schutzanforderungen, und damit das Sicherheitsniveau, auf Seiten des IT-Grundschutzes höher liegen. Überraschend ist jedoch, dass VdS 3473 immerhin 30 % der Anforderungen des BSI abdecken kann, obwohl die Richtlinie der VdS nur ca. 5% des Umfangs des IT-Grundschutzes hat. Trotzdem gibt es in VdS 3473 erhebliche Defizite.

Nach Ansicht des BSI sind die Basis-Anforderungen des IT-Grundschutzes Maßnahmen, welche zeitnah umgesetzt werden müssen, damit ein Unternehmen ein Mindestmaß an Informationssicherheit gewährleisten kann. Ein ausreichendes Schutzniveau ist alleine dadurch jedoch nicht gegeben. Erst mit Umsetzung der weiterführenden Standardanforderungen ist ein Sicherheitsniveau erreicht, das dem Stand der Technik entspricht [6, S. 4].

Obwohl die VdS ihre Richtlinie als Mindestanforderung an Informationssicherheit betrachtet [9, S. 6], erfüllt VdS 3473 bereits die Basisanforderungen des IT-Grundschutzes nur zu etwa 30%. Darüber hinausgehend gibt es keine weiteren VdS-Richtlinien zur Steigerung des Sicherheitsniveaus. Aus diesem Grund ist es wahrscheinlich, dass die Standardanforderungen des BSI zu einem noch geringeren Anteil erfüllt werden als die Basisanforderungen. Die alleinige Umsetzung von VdS 3473 in einem Unternehmen ist daher nicht ausreichend um ein Sicherheitsniveau zu erreichen, das dem Stand der Technik entspricht.

<!-- page: 171 -->

## 13.2.1 Implizite Erfüllung von Anforderungen

Es ist denkbar, dass aus den allgemeinen Anforderungen der VdS, die fehlenden Details implizit abgeleitet werden. Ein Ansatz dafür ist bspw. die in Kapitel 7 (Personal) gemachte Vorgabe, dass Mitarbeiter für ihre Aufgaben geeignet sein müssen. Angewendet auf einen Administrator könnte diese Vorgabe so interpretiert werden, dass der Administrator in der Lage sein muss verschiedene IT-Systeme sicher zu konfigurieren und z. B. wissen muss wie er die Rechte auf einem Unix-System vergeben muss, damit dieses sicher ist. Die genaueren Anforderungen des BSI wären dann erfüllt.

Bei genauerer Betrachtung erweist sich dieser Ansatz jedoch als unzureichend. Natürlich muss ein Mitarbeiter eine grundsätzliche Eignung für eine Aufgaben haben, es erscheint jedoch unwahrscheinlich, dass einem Mitarbeiter jeder Zeit alle Details seiner Arbeit bewusst sind. Besonders bei Tätigkeiten, welche eher selten ausgeübt werden (etwa Neuinstallation eines Servers in einem kleinen Unternehmen), besteht die Gefahr, dass der verantwortliche Mitarbeiter eine sicherheitsrelevante Einstellung übersieht.

Ein solches Szenario erscheint glaubhaft. Eine Studie des BSI [3] im Bereich der kleinen und mittleren Unternehmen ergab, dass die häufigste Ursache für einen Sicherheitsvorfall menschliches Versagen ist [3, S. 86f].

Eine aktuellere Umfrage aus dem Jahr 2015, bei welcher 220 Einrichtungen befragt wurden, zeigt ein vergleichbares Bild auf. 120 der befragten Unternehmen gaben an, dass unabsichtliches Fehlverhalten von Mitarbeitern zum Erfolg eines 'Cyber-Angriffs' geführt hat. Etwa 70 Befragte nennen als weiteren Grund für erfolgreiche Angriffe die falsche Konfiguration von Systemen [4, S. 16].

Ähnliche Ergebnisse finden sich auch im Bereich von sog. 'Kritischen Infrastrukturen' [5, S.10].

Das Risiko eines Schadens durch ein fehlerhaft konfiguriertes Systems oder einen menschlichen Fehler ist also verhältnismäßig groß. Genaue Vorgaben, welche weniger Raumfür Fehler lassen, könnten ein geeignetes Mittel sein der Gefahr durch menschliche Fehler zu begegnen. In VdS 3473 fehlt es jedoch besonders an solchen Anforderungen. Eine indirekte Ableitung solcher Vorgaben ist nicht ausreichend um den 'Faktor Mensch' zu berücksichtigen.

<!-- page: 172 -->

## 13.3 Vergleich zu ISO 27001

ISO 27001 ist ein internationaler Standard für Informationssicherheitsmanagement. Er wird häufig als Vergleichswerk für Standards aus dem Bereich Informationssicherheit herangezogen und ist international anerkannt. Mit einem Umfang von etwa 90 Seiten, ist er fast drei mal so umfangreich wie VdS 3473, hat jedoch nur etwa 12% des Umfangs des IT-Grundschutzes.

Bei einer sehr oberflächlichen Betrachtung der Inhalte von ISO 27001 ergaben sich einige Abweichungen zu VdS 3473. Inwieweit diese sich auf die Vergleichbarkeit des Sicherheitsniveaus auswirken, kann zum jetzigen Zeitpunkt jedoch nicht abschließend beurteilt werden und bedarf weiterer Untersuchungen.

## 13.4 Überlegungen zur Anwendbarkeit

Die Unterschiede im Umfang des IT-Grundschutz-Kompendiums und VdS 3473 wirken sich möglicherweise nicht nur auf das Sicherheitsniveau aus. Es ist wahrscheinlich, dass sich die beiden Richtlinien unterschiedlich leicht oder schwer umsetzen lassen. Dazu möchte ich in diesem Abschnitt einige Überlegungen anstellen.

Beim IT-Grundschutz handelt es sich um ein sehr umfangreiches Werk. Neben dem IT-Grundschutz-Kompendium gibt es viele weiterführende Standards und Umsetzungshinweise. Der große Umfang könnte bei einem ersten Einstieg in das Thema 'Informationssicherheit' eher abschreckend wirken und die Orientierung erschweren.

Das BSI hat diesen Umstand jedoch erkannt und mit dem 'Leitfaden zur Basis-Absicherung nach IT-Grundschutz' [2] eine kompakte Anleitung für den Einstieg in die Informationssicherheit erstellt. Dieser Leitfaden kann, begleitend zum IT-Grundschutz-Kompendium, vergleichsweise einfach in das Themengebiet einführt und so die anfängliche Orientierung erleichtert.

VdS 3473 ist durch den geringen Umfang deutlich zugänglicher. Problematisch sind jedoch die in dieser Arbeit festgestellten Defizite. Insbesondere für unerfahrene Verantwortliche wird es schwierig sein, die fehlenden Aspekte zu berücksichtigen, wenn nicht auf weitere Literatur zurückgegriffen wird.

Aufgrund des Baustein-Prinzips eignet sich der IT-Grundschutz gut als 'Nachschlagewerk'. Verantwortliche in einem Unternehmen können einen relevanten Baustein heraussuchen und erhalten so direkt alle Informationen, die für den entsprechenden Bereich wichtig sind. Nicht benötigte Informationen können so auch übersprungen werden.

Ein 'themenbezogenes Nachschlagen' ist in begrenztem Maße auch mit VdS 3473 möglich. Allerdings bauen die einzelnen Bereiche stärker aufeinander auf, als es beim IT-Grundschutz der Fall ist. Im IT-Grundschutz gibt es bspw. einen Baustein zu Laptops. In VdS 3473 müssen für Laptops zunächst die allgemeinen Anforderungen für IT-Systeme umgesetzt werden und danach die zusätzlichen Anforderungen für mobile Systeme. Falls ein Themenbereich Vorgaben aus verschiedenen Kapiteln berücksichtigen muss, ist das gezielte Nachschlagen eher schwierig.

<!-- page: 173 -->

Inwieweit sich der Umfang und der Aufbau von Sicherheitsstandards tatsächlich auf die Umsetzbarkeit in kleinen und mittleren Unternehmen auswirkt und ob die Motivation zur Einführung eines ISMS vom Umfang der Standards beeinflusst wird, kann ohne weitere Forschung nicht eindeutig festgestellt werden. Diese Fragestellung könnte in einer Studie (möglicherweise im Rahmen einer Masterarbeit) weiter untersucht werden.

## 13.5 Notwendige Ergänzungen in VdS 3473

Der in dieser Arbeit durchgeführte Vergleich hat eine erhebliche Zahl von nicht erfüllten Anforderungen in VdS 3473 gefunden. Damit VdS 3473 ein ähnliches Sicherheitsniveau bekommt wie das IT-Grundschutz-Kompendium, müssen die fehlenden Anforderungen ergänzt werden.

Der VdS stehen dabei zwei Wege offen. Zum einen könnten die fehlenden Anforderungen im Text von VdS 3473 ergänzt werden. Dabei wäre es jedoch nicht erforderlich jede Vorgabe des BSI zu übernehmen. Aufgrund der Baustein-orientierten Konzeption des IT-Grundschutzes sind viele Anforderungen in mehreren Bausteinen vorhanden, ggf. mit minimalen Abweichungen. Beispiele dafür sind die Vorgaben zur Verlegung von Kabeln (INF.3.A3 und INF.4.A3). Würde die VdS ihre Richtlinie mit allgemeinen Vorgaben zur Verlegung von Kabeln erweitern, bei denen sowohl Strom- als auch Datenleitungen behandelt werden, wäre das Sicherheitsniveau von VdS 3473 in diesem Punkt identisch mit dem des BSI. Ähnlich müsste mit Anforderungen zu verschiedenen IT-Systemen und Software verfahren werden.

Der Umfang von VdS 3473 würde auf diesem Weg zwar deutlich zunehmen, aber bei weitem nicht so groß werden wie der des IT-Grundschutzes. Dies liegt auch daran, dass die VdS nicht so umfangreich in die einzelnen Themen einführt wie das BSI.

Ein zweiter Ansatz würde darin bestehen, den grundsätzlichen Aufbau von VdS 3473 beizubehalten. Statt technische Anforderungen zu ergänzen könnten alle Bereiche nur durch allgemeine Rahmenvorgaben beschrieben werden. Dadurch würden schon große Teile der IT -Grundschutz-Vorgaben abgedeckt werden, sofern auch Themen wie Software und IT-Systeme berücksichtigt werden. Die detaillierten Vorgaben, die zum großen Teil in VdS 3473 fehlen, könnten dann in einem weiteren Leitfaden beschrieben werden. Diese Ergänzung würde in etwa den Umsetzungshinweisen des BSI entsprechen, jedoch auch deutlich weniger umfangreich sein.

<!-- page: 174 -->



<!-- page: 175 -->

## Kapitel 14

## Danksagungen

Ich bedanke mich bei Frau Verena Lang (BSI) und Herrn Professor Heiko Krumm (TU Dortmund) dafür, dass Sie sich bereit erklärt haben diese Arbeit zu Betreuen und zu Bewerten.

Den Herren Birger Klein (BSI) und Alex Essoh (BSI) danke ich für Ihre Anmerkungen zu meiner Arbeit und Ihre Hinweise zu weiterführender Literatur.

<!-- page: 176 -->



<!-- page: 177 -->

## Anhang A Weitere Informationen

<!-- page: 178 -->

## A.1 Übersichtstabelle

Diese Tabelle stellt die Unterschiede zwischen IT-Grundschutz und VdS 3473 in übersichtlicher Form da.

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                                                      |
|------------------------------|----------------------------|------------------------------------------------------------------------------------------------|
| ISMS.1.A1                    | Erfüllt                    |                                                                                                |
| ISMS.1.A2                    | Erfüllt                    |                                                                                                |
| ISMS.1.A3                    | Erfüllt                    |                                                                                                |
| ISMS.1.A4                    | Erfüllt                    |                                                                                                |
| ISMS.1.A5                    | Nicht erfüllt              |                                                                                                |
| ISMS.1.A6                    | Teilweise Erfüllt          | Keine Vertretungsregelung in VdS 3473. Dafür aber genaue Benennung von Ver- antwortlichkeiten. |
| ISMS.1.A7                    | Erfüllt                    |                                                                                                |
| ISMS.1.A8                    | Erfüllt                    |                                                                                                |
| ISMS.1.A9                    | Erfüllt                    |                                                                                                |
| ORP.1.A1                     | Erfüllt                    |                                                                                                |
| ORP.1.A2                     | Erfüllt                    |                                                                                                |
| ORP.1.A3                     | Nicht erfüllt              |                                                                                                |
| ORP.1.A4                     | Erfüllt                    |                                                                                                |
| ORP.1.A5                     | Erfüllt                    |                                                                                                |
| ORP.2.A1                     | Erfüllt                    |                                                                                                |
| ORP.2.A2                     | Teilweise Erfüllt          | Umfang der nötigen Maßnahmen im IT- GS größer                                                  |
| ORP.2.A3                     | Nicht erfüllt              |                                                                                                |
| ORP.2.A4                     | Erfüllt                    |                                                                                                |
| ORP.2.A5                     | Erfüllt                    | VdS Anforderungen sind genauer.                                                                |
| ORP.3.A1                     | Erfüllt                    |                                                                                                |
| ORP.3.A2                     | Erfüllt                    |                                                                                                |
| ORP.3.A3                     | Erfüllt                    |                                                                                                |
| ORP.4.A1                     | Erfüllt                    |                                                                                                |
| ORP.4.A2                     | Erfüllt                    |                                                                                                |
| ORP.4.A3                     | Erfüllt                    |                                                                                                |
| ORP.4.A4                     | Erfüllt                    |                                                                                                |
| ORP.4.A5                     | Nicht erfüllt              |                                                                                                |

<!-- page: 179 -->

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                  |
|------------------------------|----------------------------|------------------------------------------------------------|
| ORP.4.A6                     | Nicht erfüllt              |                                                            |
| ORP.4.A7                     | Erfüllt                    |                                                            |
| ORP.4.A8                     | Erfüllt                    |                                                            |
| ORP.4.A9                     | Erfüllt                    |                                                            |
| ORP.5.A1                     | Nicht erfüllt              |                                                            |
| ORP.5.A2                     | Nicht erfüllt              |                                                            |
| ORP.5.A3                     | Nicht erfüllt              |                                                            |
| CON.1.A1                     | Nicht erfüllt              |                                                            |
| CON.1.A2                     | Nicht erfüllt              |                                                            |
| CON.2.A1                     | Nicht erfüllt              |                                                            |
| CON.3.A1                     | Erfüllt                    |                                                            |
| CON.3.A2                     | Erfüllt                    |                                                            |
| CON.3.A3                     | Erfüllt                    |                                                            |
| CON.3.A4                     | Nicht erfüllt              |                                                            |
| CON.3.A5                     | Erfüllt                    |                                                            |
| CON.4.A1                     | Nicht erfüllt              |                                                            |
| CON.4.A2                     | Nicht erfüllt              |                                                            |
| CON.4.A3                     | Nicht erfüllt              |                                                            |
| CON.5.A1                     | Nicht erfüllt              |                                                            |
| CON.5.A2                     | Nicht erfüllt              |                                                            |
| CON.5.A3                     | Nicht erfüllt              |                                                            |
| CON.5.A4                     | Erfüllt                    |                                                            |
| CON.5.A5                     | Teilweise Erfüllt          | Keine vertraglichen Vereinbarung von Si- cherheitsupdates. |
| CON.6.A1                     | Teilweise Erfüllt          | Keine Angabe zum sicheren Vernichten von Informationen.    |
| CON.6.A2                     | Nicht erfüllt              |                                                            |
| CON.7.A1                     | Erfüllt                    |                                                            |
| CON.7.A2                     | Erfüllt                    |                                                            |
| CON.7.A3                     | Nicht erfüllt              |                                                            |
| CON.7.A4                     | Nicht erfüllt              |                                                            |
| CON.7.A5                     | Erfüllt                    |                                                            |

<!-- page: 180 -->

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                                   |
|------------------------------|----------------------------|-----------------------------------------------------------------------------|
| CON.7.A6                     | Erfüllt                    |                                                                             |
| CON.7.A7                     | Erfüllt                    |                                                                             |
| CON.7.A8                     | Erfüllt                    |                                                                             |
| CON.7.A9                     | Erfüllt                    |                                                                             |
| CON.7.A10                    | Erfüllt                    |                                                                             |
| CON.7.A12                    | Nicht erfüllt              |                                                                             |
| OPS.1.1.2.A1                 | Teilweise Erfüllt          | Keine Vertretung von Administratoren er- forderlich.                        |
| OPS.1.1.2.A2                 | Nicht erfüllt              |                                                                             |
| OPS.1.1.2.A3                 | Teilweise Erfüllt          | Keine Aufforderung sich an Gesetzte zu halten.                              |
| OPS.1.1.2.A4                 | Erfüllt                    |                                                                             |
| OPS.1.1.2.A5                 | Teilweise Erfüllt          | Verbot der Nutzung von Administrations- konten nicht in VdS 3473 enthalten. |
| OPS.1.1.2.A6                 | Nicht erfüllt              |                                                                             |
| OPS.1.1.3.A1                 | Nicht erfüllt              |                                                                             |
| OPS.1.1.3.A2                 | Nicht erfüllt              |                                                                             |
| OPS.1.1.3.A3                 | Nicht erfüllt              |                                                                             |
| OPS.1.1.4.A1                 | Erfüllt                    |                                                                             |
| OPS.1.1.4.A2                 | Erfüllt                    |                                                                             |
| OPS.1.1.4.A3                 | Teilweise Erfüllt          | Keine genauen Vorgaben zu Virenschutz- software.                            |
| OPS.1.1.4.A4                 | Teilweise Erfüllt          | Keine genauen Vorgaben zu Virenschutz- software.                            |
| OPS.1.1.4.A5                 | Teilweise Erfüllt          | Keine genauen Vorgaben zu Virenschutz- software.                            |
| OPS.1.1.4.A6                 | Teilweise Erfüllt          | Konfigurationen müssen nach Updates nicht überprüft werden.                 |
| OPS.1.1.4.A7                 | Erfüllt                    |                                                                             |
| OPS.1.1.5.A1                 | Erfüllt                    |                                                                             |
| OPS.1.1.5.A2                 | Erfüllt                    |                                                                             |
| OPS.1.1.5.A3                 | Nicht erfüllt              |                                                                             |
| OPS.1.1.5.A4                 | Erfüllt                    |                                                                             |
| OPS.1.1.6.A1                 | Nicht erfüllt              |                                                                             |
| OPS.1.1.6.A3                 | Nicht erfüllt              |                                                                             |
| OPS.1.1.6.A4                 | Nicht erfüllt              |                                                                             |
| OPS.1.1.6.A5                 | Nicht erfüllt              |                                                                             |

<!-- page: 181 -->

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                             |
|------------------------------|----------------------------|-------------------------------------------------------|
| OPS.1.2.2.A1                 | Erfüllt                    |                                                       |
| OPS.1.2.2.A2                 | Erfüllt                    |                                                       |
| OPS.1.2.2.A3                 | Erfüllt                    |                                                       |
| OPS.1.2.2.A4                 | Nicht erfüllt              |                                                       |
| OPS.1.2.2.A5                 | Nicht erfüllt              |                                                       |
| OPS.1.2.2.A6                 | Nicht erfüllt              |                                                       |
| OPS.1.2.2.A7                 | Erfüllt                    |                                                       |
| OPS.1.2.2.A8                 | Erfüllt                    |                                                       |
| OPS.1.2.2.A9                 | Nicht erfüllt              |                                                       |
| OPS.1.2.3.A1                 | Nicht erfüllt              |                                                       |
| OPS.1.2.3.A2                 | Nicht erfüllt              |                                                       |
| OPS.1.2.3.A3                 | Teilweise Erfüllt          | Kein Betrachtung von 'Informationen' im Allgemienen.  |
| OPS.1.2.3.A4                 | Nicht erfüllt              |                                                       |
| OPS.1.2.3.A5                 | Teilweise Erfüllt          | Verlustmeldungen nur bei 'kritischen' Da- tenträgern. |
| OPS.1.2.4.A1                 | Nicht erfüllt              |                                                       |
| OPS.1.2.4.A2                 | Erfüllt                    |                                                       |
| OPS.1.2.4.A3                 | Erfüllt                    |                                                       |
| OPS.1.2.4.A4                 | Teilweise Erfüllt          | Keine genauen Angaben zur Datensiche- rung.           |
| OPS.1.2.4.A5                 | Erfüllt                    |                                                       |
| OPS.2.1.A1                   | Erfüllt                    |                                                       |
| OPS.2.4.A1                   | Nicht erfüllt              |                                                       |
| OPS.2.4.A2                   | Nicht erfüllt              |                                                       |
| OPS.2.4.A3                   | Nicht erfüllt              |                                                       |
| OPS.2.4.A4                   | Nicht erfüllt              |                                                       |
| OPS.2.4.A5                   | Nicht erfüllt              |                                                       |
| OPS.3.1.A1                   | Nicht erfüllt              |                                                       |
| DER.2.1.A1                   | Erfüllt                    |                                                       |
| DER.2.1.A2                   | Erfüllt                    |                                                       |
| DER.2.1.A3                   | Erfüllt                    |                                                       |
| DER.2.1.A4                   | Erfüllt                    |                                                       |

<!-- page: 182 -->

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                            |
|------------------------------|----------------------------|------------------------------------------------------|
| DER.2.1.A5                   | Erfüllt                    |                                                      |
| DER.2.1.A6                   | Teilweise Erfüllt          | Keine Benennung von genauen techni- schen Maßnahmen. |
| DER.2.2.A1                   | Nicht erfüllt              |                                                      |
| DER.2.2.A2                   | Teilweise Erfüllt          | Keine berücksichtigung einer forensichen Analyse     |
| DER.2.2.A3                   | Nicht erfüllt              |                                                      |
| DER.2.3.A1                   | Nicht erfüllt              |                                                      |
| DER.2.3.A2                   | Teilweise Erfüllt          | Keine genaue beschreibung des Vorge- hens.           |
| DER.2.3.A3                   | Nicht erfüllt              |                                                      |
| DER.2.3.A4                   | Nicht erfüllt              |                                                      |
| DER.2.3.A5                   | Teilweise Erfüllt          | Keine genaue Beschreibung des Vorge- hens.           |
| DER.2.3.A6                   | Teilweise Erfüllt          | Keine genaue Beschreibung des Vorge- hens.           |
| DER.3.1.A1                   | Nicht erfüllt              |                                                      |
| DER.3.1.A2                   | Nicht erfüllt              |                                                      |
| DER.3.1.A3                   | Nicht erfüllt              |                                                      |
| DER.3.1.A4                   | Nicht erfüllt              |                                                      |
| APP.1.1.A1                   | Teilweise Erfüllt          | Keine technischen Vorgaben.                          |
| APP.1.1.A2                   | Nicht erfüllt              |                                                      |
| APP.1.1.A3                   | Nicht erfüllt              |                                                      |
| APP.1.1.A4                   | Nicht erfüllt              |                                                      |
| APP.1.2.A1                   | Nicht erfüllt              |                                                      |
| APP.1.2.A2                   | Nicht erfüllt              |                                                      |
| APP.1.2.A3                   | Nicht erfüllt              |                                                      |
| APP.1.2.A4                   | Nicht erfüllt              |                                                      |
| APP.2.1.A1                   | Nicht erfüllt              |                                                      |
| APP.2.1.A2                   | Nicht erfüllt              |                                                      |
| APP.2.1.A3                   | Teilweise Erfüllt          | Keine Abgrenzung von Administrations- aufgaben       |
| APP.2.1.A4                   | Nicht erfüllt              |                                                      |
| APP.2.1.A5                   | Nicht erfüllt              |                                                      |
| APP.2.1.A6                   | Nicht erfüllt              |                                                      |
| APP.2.2.A1                   | Teilweise Erfüllt          | Keine expliziten Vorgaben für Active Di- rectory.    |

<!-- page: 183 -->

## A.1. ÜBERSICHTSTABELLE

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                                                                             |
|------------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------|
| APP.2.2.A2                   | Teilweise Erfüllt          | Keine expliziten Vorgaben für Active Di- rectory.                                                                     |
| APP.2.2.A3                   | Nicht erfüllt              |                                                                                                                       |
| APP.2.2.A4                   | Teilweise Erfüllt          | Keine genaue Anforderung zu Active Di- rectory.                                                                       |
| APP.2.2.A5                   | Nicht erfüllt              |                                                                                                                       |
| APP.2.2.A6                   | Teilweise Erfüllt          | Keine expliziten Vorgaben für Active Di- rectory.                                                                     |
| APP.2.2.A7                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.1.A1                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.1.A2                   | Teilweise Erfüllt          | Keine Vorgaben für Webanwendungen.                                                                                    |
| APP.3.1.A3                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.1.A4                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.1.A5                   | Teilweise Erfüllt          | Technische Anforderungen und Zu- grifssregelungen fehlen.                                                             |
| APP.3.1.A6                   | Erfüllt                    |                                                                                                                       |
| APP.3.1.A7                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.2.A1                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.2.A2                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.2.A3                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.2.A4                   | Erfüllt                    |                                                                                                                       |
| APP.3.2.A5                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.2.A6                   | Erfüllt                    |                                                                                                                       |
| APP.3.2.A7                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.3.A1                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.3.A2                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.3.A3                   | Teilweise Erfüllt          | Keine genauen Anforderungen für File- server, kein Echtzeitschutz.                                                    |
| APP.3.3.A4                   | Teilweise Erfüllt          | Genaue Vorgabe für das Interval einer Si- cherung in VdS 3473. Dafür jedoch keine Sicherung vor einer Systemänderung. |
| APP.3.3.A5                   | Teilweise Erfüllt          | Keine Angaben zu Zugriffsrechten auf Dateiservern.                                                                    |
| APP.3.4.A1                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.4.A2                   | Teilweise Erfüllt          | Keine Angaben für Samba-Server.                                                                                       |
| APP.3.6.A1                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.6.A2                   | Nicht erfüllt              |                                                                                                                       |
| APP.3.6.A3                   | Nicht erfüllt              |                                                                                                                       |

<!-- page: 184 -->

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                    |
|------------------------------|----------------------------|--------------------------------------------------------------|
| APP.3.6.A4                   | Nicht erfüllt              | Nicht erfüllt                                                |
| APP.3.6.A5                   | Teilweise Erfüllt          | Keine Sicherung von Konfigurationsda- ten.                   |
| APP.3.6.A6                   | Nicht erfüllt              | Nicht erfüllt                                                |
| APP.3.6.A7                   | Teilweise Erfüllt          | Keine Überwachung von DNS-Servern                            |
| APP.3.6.A8                   | Nicht erfüllt              |                                                              |
| APP.3.6.A9                   | Nicht erfüllt              |                                                              |
| APP.4.3.A1                   | Nicht erfüllt              |                                                              |
| APP.4.3.A2                   | Nicht erfüllt              |                                                              |
| APP.4.3.A3                   | Nicht erfüllt              |                                                              |
| APP.4.3.A4                   | Nicht erfüllt              |                                                              |
| APP.4.3.A5                   | Erfüllt                    |                                                              |
| APP.4.3.A6                   | Nicht erfüllt              |                                                              |
| APP.4.3.A7                   | Erfüllt                    |                                                              |
| APP.4.3.A8                   | Erfüllt                    |                                                              |
| APP.4.3.A9                   | Teilweise Erfüllt          | Keine Sicherung von Datenbanken vor dem anlegen einer neuen. |
| APP.5.1.A1                   | Nicht erfüllt              |                                                              |
| APP.5.1.A2                   | Nicht erfüllt              |                                                              |
| APP.5.1.A3                   | Nicht erfüllt              |                                                              |
| APP.5.1.A4                   | Nicht erfüllt              |                                                              |
| APP.5.2.A1                   | Nicht erfüllt              |                                                              |
| APP.5.2.A2                   | Nicht erfüllt              |                                                              |
| APP.5.2.A3                   | Erfüllt                    |                                                              |
| APP.5.2.A4                   | Nicht erfüllt              |                                                              |
| APP.5.2.A5                   | Nicht erfüllt              |                                                              |
| SYS.1.1.A1                   | Teilweise Erfüllt          | Kein Verbot der Nutzung von Servern als Arbeitsplatzrechner. |
| SYS.1.1.A2                   | Erfüllt                    |                                                              |
| SYS.1.1.A3                   | Teilweise Erfüllt          | Keine Angabe zu Zugriffsarten.                               |
| SYS.1.1.A4                   | Nicht erfüllt              |                                                              |
| SYS.1.1.A5                   | Nicht erfüllt              |                                                              |
| SYS.1.1.A6                   | Teilweise Erfüllt          | Kein Abschalten unbenutzter Dienste.                         |

<!-- page: 185 -->

## A.1. ÜBERSICHTSTABELLE

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                                      |
|------------------------------|----------------------------|--------------------------------------------------------------------------------|
| SYS.1.1.A7                   | Teilweise Erfüllt          | Anforderungen sind nicht so weitgehend wie die des BSI.                        |
| SYS.1.1.A8                   | Teilweise Erfüllt          | Keine Sicherung vor Änderungen am Sy- stem.                                    |
| SYS.1.1.A9                   | Teilweise Erfüllt          | Keine so genauen Vorgaben wie beim BSI, kein Echtzeitschutz.                   |
| SYS.1.1.A10                  | Erfüllt                    |                                                                                |
| SYS.1.2.2.A1                 | Nicht erfüllt              |                                                                                |
| SYS.1.2.2.A2                 | Nicht erfüllt              |                                                                                |
| SYS.1.2.2.A3                 | Nicht erfüllt              |                                                                                |
| SYS.1.3.A1                   | Teilweise Erfüllt          | Keine technischen Anforderungen.                                               |
| SYS.1.3.A2                   | Nicht erfüllt              |                                                                                |
| SYS.1.3.A3                   | Nicht erfüllt              |                                                                                |
| SYS.1.3.A4                   | Nicht erfüllt              |                                                                                |
| SYS.1.3.A5                   | Nicht erfüllt              |                                                                                |
| SYS.1.5.A1                   | Erfüllt                    |                                                                                |
| SYS.1.5.A2                   | Teilweise Erfüllt          | Keine Angaben zu virtuellen Systemen.                                          |
| SYS.1.5.A3                   | Nicht erfüllt              |                                                                                |
| SYS.1.5.A4                   | Nicht erfüllt              |                                                                                |
| SYS.1.5.A5                   | Erfüllt                    |                                                                                |
| SYS.1.5.A6                   | Nicht erfüllt              |                                                                                |
| SYS.1.5.A7                   | Erfüllt                    |                                                                                |
| SYS.1.8.A1                   | Teilweise Erfüllt          | Keine Angaben zu Stromversorgung o. ä.                                         |
| SYS.1.8.A2                   | Erfüllt                    |                                                                                |
| SYS.1.8.A3                   | Erfüllt                    |                                                                                |
| SYS.1.8.A4                   | Erfüllt                    |                                                                                |
| SYS.1.8.A5                   | Erfüllt                    |                                                                                |
| SYS.2.1.A1                   | Erfüllt                    |                                                                                |
| SYS.2.1.A2                   | Teilweise Erfüllt          | Kein Verbot der Nutzung von administra- tiven Konten für alltägliche Aufgaben. |
| SYS.2.1.A3                   | Erfüllt                    |                                                                                |
| SYS.2.1.A4                   | Erfüllt                    |                                                                                |
| SYS.2.1.A5                   | Erfüllt                    |                                                                                |
| SYS.2.1.A6                   | Teilweise Erfüllt          | Keine Echtzeit-Scans.                                                          |

<!-- page: 186 -->

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                                     |
|------------------------------|----------------------------|-------------------------------------------------------------------------------|
| SYS.2.1.A7                   | Erfüllt                    |                                                                               |
| SYS.2.1.A8                   | Erfüllt                    |                                                                               |
| SYS.2.2.2.A1                 | Nicht erfüllt              |                                                                               |
| SYS.2.2.2.A2                 | Erfüllt                    |                                                                               |
| SYS.2.2.2.A3                 | Erfüllt                    |                                                                               |
| SYS.2.2.3.A1                 | Erfüllt                    |                                                                               |
| SYS.2.2.3.A2                 | Nicht erfüllt              |                                                                               |
| SYS.2.2.3.A3                 | Nicht erfüllt              |                                                                               |
| SYS.2.2.3.A4                 | Nicht erfüllt              |                                                                               |
| SYS.2.2.3.A5                 | Erfüllt                    |                                                                               |
| SYS.2.2.3.A6                 | Nicht erfüllt              |                                                                               |
| SYS.2.3.A1                   | Teilweise Erfüllt          | Kein Verbot der Nutzung von Administra- tionskonten für alltägliche Aufgaben. |
| SYS.2.3.A2                   | Nicht erfüllt              |                                                                               |
| SYS.2.3.A3                   | Nicht erfüllt              |                                                                               |
| SYS.2.3.A4                   | Teilweise Erfüllt          | Besonderheiten von UNIX werden nicht berücksichtigt.                          |
| SYS.2.3.A5                   | Nicht erfüllt              |                                                                               |
| SYS.3.1.A1                   | Erfüllt                    |                                                                               |
| SYS.3.1.A2                   | Teilweise Erfüllt          | Keine Überprüfung ob Maßnahmen ein- gehalten werden.                          |
| SYS.3.1.A3                   | Nicht erfüllt              |                                                                               |
| SYS.3.1.A4                   | Teilweise Erfüllt          | Keine Angaben zum Vorgehen nach Vi- rusinfektion.                             |
| SYS.3.1.A5                   | Teilweise Erfüllt          | Keine automatische Datensicherung.                                            |
| SYS.3.2.1.A1                 | Erfüllt                    |                                                                               |
| SYS.3.2.1.A2                 | Erfüllt                    | Die Anforderungen der VdS sind höher.                                         |
| SYS.3.2.1.A3                 | Nicht erfüllt              |                                                                               |
| SYS.3.2.1.A4                 | Teilweise Erfüllt          | Keine Anforderungen für die Besonder- heiten von Smartphones und Tablets.     |
| SYS.3.2.1.A5                 | Teilweise Erfüllt          | Keine langfristige Versorgung mit Upda- tes durch Hersteller.                 |
| SYS.3.2.1.A6                 | Nicht erfüllt              |                                                                               |
| SYS.3.2.1.A7                 | Erfüllt                    |                                                                               |
| SYS.3.2.1.A8                 | Nicht erfüllt              |                                                                               |
| SYS.3.2.2.A1                 | Nicht erfüllt              |                                                                               |

<!-- page: 187 -->

## A.1. ÜBERSICHTSTABELLE

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                    |
|------------------------------|----------------------------|--------------------------------------------------------------|
| SYS.3.2.2.A2                 | Nicht erfüllt              |                                                              |
| SYS.3.2.2.A3                 | Nicht erfüllt              |                                                              |
| SYS.3.2.2.A4                 | Nicht erfüllt              |                                                              |
| SYS.3.2.2.A5                 | Nicht erfüllt              |                                                              |
| SYS.3.2.2.A6                 | Erfüllt                    |                                                              |
| SYS.3.2.3.A1                 | Nicht erfüllt              |                                                              |
| SYS.3.2.3.A2                 | Erfüllt                    | Anforderungen der VdS sind umfangrei- cher.                  |
| SYS.3.2.3.A3                 | Erfüllt                    |                                                              |
| SYS.3.2.3.A4                 | Erfüllt                    |                                                              |
| SYS.3.2.3.A5                 | Erfüllt                    |                                                              |
| SYS.3.2.3.A6                 | Nicht erfüllt              |                                                              |
| SYS.3.2.3.A7                 | Erfüllt                    |                                                              |
| SYS.3.2.3.A8                 | Teilweise Erfüllt          | Eine Vorgabe zum Ausmustern alter Ge- räte.                  |
| SYS.3.2.4.A1                 | Nicht erfüllt              |                                                              |
| SYS.3.4.A1                   | Erfüllt                    |                                                              |
| SYS.3.4.A2                   | Teilweise Erfüllt          | Nur der Verlust kritischer Datenträger muss gemeldet werden. |
| SYS.3.4.A3                   | Nicht erfüllt              |                                                              |
| SYS.4.1.A1                   | Nicht erfüllt              |                                                              |
| SYS.4.1.A2                   | Teilweise Erfüllt          | Angaben zur Aufstellung von Geräten fehlen.                  |
| SYS.4.1.A3                   | Nicht erfüllt              |                                                              |
| SYS.4.4.A1                   | Teilweise Erfüllt          | Keine weiteren Vorgaben zu IoT-Geräten.                      |
| SYS.4.4.A2                   | Erfüllt                    |                                                              |
| SYS.4.4.A3                   | Erfüllt                    |                                                              |
| SYS.4.4.A4                   | Nicht erfüllt              |                                                              |
| SYS.4.4.A5                   | Nicht erfüllt              |                                                              |
| IND.1.A1                     | Erfüllt                    |                                                              |
| IND.1.A2                     | Erfüllt                    |                                                              |
| IND.1.A3                     | Teilweise Erfüllt          | Keine Vorgaben zu Produktionsanlagen.                        |
| IND.2.1.A1                   | Teilweise Erfüllt          | Keine besonderen Vorgaben für Indu- strieanlagen.            |
| IND.2.1.A2                   | Nicht erfüllt              |                                                              |

<!-- page: 188 -->

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                        |
|------------------------------|----------------------------|------------------------------------------------------------------|
| IND.2.1.A3                   | Erfüllt                    |                                                                  |
| IND.2.1.A4                   | Teilweise Erfüllt          | Vergleichbare Anforderungen erst für kri- tische Systeme.        |
| IND.2.1.A5                   | Teilweise Erfüllt          | Vergleichbare Anforderungen erst für kri- tische Systeme.        |
| IND.2.1.A6                   | Teilweise Erfüllt          | Vergleichbare Anforderungen erst für kri- tische Systeme.        |
| IND.2.3.A1                   | Nicht erfüllt              |                                                                  |
| NET.1.1.A1                   | Nicht erfüllt              |                                                                  |
| NET.1.1.A2                   | Erfüllt                    |                                                                  |
| NET.1.1.A3                   | Nicht erfüllt              |                                                                  |
| NET.1.1.A4                   | Teilweise Erfüllt          | Keine technischen Anforderungen, keine Segmentierung des Netzes. |
| NET.1.1.A5                   | Nicht erfüllt              |                                                                  |
| NET.1.1.A6                   | Nicht erfüllt              |                                                                  |
| NET.1.1.A7                   | Erfüllt                    |                                                                  |
| NET.1.1.A8                   | Nicht erfüllt              |                                                                  |
| NET.1.1.A9                   | Nicht erfüllt              |                                                                  |
| NET.1.1.A10                  | Nicht erfüllt              |                                                                  |
| NET.1.1.A11                  | Erfüllt                    |                                                                  |
| NET.1.1.A12                  | Nicht erfüllt              |                                                                  |
| NET.1.1.A13                  | Nicht erfüllt              |                                                                  |
| NET.1.1.A14                  | Nicht erfüllt              |                                                                  |
| NET.1.1.A15                  | Nicht erfüllt              |                                                                  |
| NET.1.2.A1                   | Nicht erfüllt              |                                                                  |
| NET.1.2.A2                   | Nicht erfüllt              |                                                                  |
| NET.1.2.A3                   | Nicht erfüllt              |                                                                  |
| NET.1.2.A4                   | Erfüllt                    |                                                                  |
| NET.1.2.A5                   | Erfüllt                    |                                                                  |
| NET.1.2.A6                   | Erfüllt                    |                                                                  |
| NET.1.2.A7                   | Erfüllt                    |                                                                  |
| NET.1.2.A8                   | Erfüllt                    |                                                                  |
| NET.1.2.A9                   | Nicht erfüllt              |                                                                  |
| NET.1.2.A10                  | Nicht erfüllt              |                                                                  |

<!-- page: 189 -->

## A.1. ÜBERSICHTSTABELLE

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                                  |
|------------------------------|----------------------------|----------------------------------------------------------------------------|
| NET.2.1.A1                   | Nicht erfüllt              |                                                                            |
| NET.2.1.A2                   | Nicht erfüllt              |                                                                            |
| NET.2.1.A3                   | Nicht erfüllt              |                                                                            |
| NET.2.1.A4                   | Teilweise Erfüllt          | Keine Angaben zur Funkwellenausbrei- tung oder zum Witterungsschutz.       |
| NET.2.1.A5                   | Nicht erfüllt              |                                                                            |
| NET.2.1.A6                   | Nicht erfüllt              |                                                                            |
| NET.2.1.A7                   | Nicht erfüllt              |                                                                            |
| NET.2.1.A8                   | Nicht erfüllt              |                                                                            |
| NET.2.2.A1                   | Nicht erfüllt              |                                                                            |
| NET.2.2.A2                   | Teilweise Erfüllt          | Keine Angabe zu Sicherheitsrichtlinien für WLAN.                           |
| NET.2.2.A3                   | Erfüllt                    |                                                                            |
| NET.3.1.A1                   | Teilweise Erfüllt          | Keine Beschränkung auf notwendige Dienste.                                 |
| NET.3.1.A2                   | Teilweise Erfüllt          | Anforderungen sind nicht so weitgehend wie die des BSI.                    |
| NET.3.1.A3                   | Teilweise Erfüllt          | Kein Verbot der Nutzung von adminstrati- ven Zugängen für Alltagsarbeiten. |
| NET.3.1.A4                   | Nicht erfüllt              |                                                                            |
| NET.3.1.A5                   | Nicht erfüllt              |                                                                            |
| NET.3.1.A6                   | Nicht erfüllt              |                                                                            |
| NET.3.1.A7                   | Erfüllt                    |                                                                            |
| NET.3.1.A8                   | Erfüllt                    |                                                                            |
| NET.3.1.A9                   | Erfüllt                    |                                                                            |
| NET.3.2.A1                   | Nicht erfüllt              |                                                                            |
| NET.3.2.A2                   | Teilweise Erfüllt          | Keine Vorgaben auf technischer Ebene.                                      |
| NET.3.2.A3                   | Nicht erfüllt              |                                                                            |
| NET.3.2.A4                   | Teilweise Erfüllt          | Keine technischen Vorgaben.                                                |
| NET.3.2.A5                   | Teilweise Erfüllt          | Nutzung von administrativen Rechten für Alltagsaufgaben nicht verboten.    |
| NET.3.2.A6                   | Nicht erfüllt              |                                                                            |
| NET.3.2.A7                   | Nicht erfüllt              |                                                                            |
| NET.3.2.A8                   | Nicht erfüllt              |                                                                            |
| NET.3.2.A9                   | Erfüllt                    |                                                                            |
| NET.3.2.A10                  | Nicht erfüllt              |                                                                            |

<!-- page: 190 -->

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                                    |
|------------------------------|----------------------------|--------------------------------------------------------------|
| NET.3.2.A11                  | Erfüllt                    |                                                              |
| NET.3.2.A12                  | Erfüllt                    |                                                              |
| NET.3.2.A13                  | Erfüllt                    |                                                              |
| NET.3.2.A14                  | Teilweise Erfüllt          | Keine automatische Protokollierung von Änderungen.           |
| NET.3.2.A15                  | Nicht erfüllt              |                                                              |
| INF.1.A1                     | Nicht erfüllt              |                                                              |
| INF.1.A2                     | Nicht erfüllt              |                                                              |
| INF.1.A3                     | Nicht erfüllt              |                                                              |
| INF.1.A4                     | Nicht erfüllt              |                                                              |
| INF.1.A5                     | Nicht erfüllt              |                                                              |
| INF.1.A6                     | Nicht erfüllt              |                                                              |
| INF.1.A7                     | Nicht erfüllt              |                                                              |
| INF.1.A8                     | Nicht erfüllt              |                                                              |
| INF.2.A1                     | Nicht erfüllt              |                                                              |
| INF.2.A2                     | Nicht erfüllt              |                                                              |
| INF.2.A3                     | Erfüllt                    |                                                              |
| INF.2.A4                     | Nicht erfüllt              |                                                              |
| INF.2.A5                     | Nicht erfüllt              |                                                              |
| INF.2.A6                     | Nicht erfüllt              |                                                              |
| INF.2.A7                     | Nicht erfüllt              |                                                              |
| INF.2.A8                     | Nicht erfüllt              |                                                              |
| INF.2.A9                     | Nicht erfüllt              |                                                              |
| INF.2.A10                    | Nicht erfüllt              |                                                              |
| INF.2.A11                    | Nicht erfüllt              |                                                              |
| INF.3.A1                     | Nicht erfüllt              |                                                              |
| INF.3.A2                     | Nicht erfüllt              |                                                              |
| INF.3.A3                     | Nicht erfüllt              |                                                              |
| INF.4.A1                     | Nicht erfüllt              |                                                              |
| INF.4.A2                     | Teilweise Erfüllt          | Nur Angaben zum Schutz vor Schäden durch bauliche Maßnahmen. |
| INF.4.A3                     | Nicht erfüllt              |                                                              |

<!-- page: 191 -->

| Anforderung IT-Grundschutz   | Abdeckung durch VdS 3473   | Bemerkung                                  |
|------------------------------|----------------------------|--------------------------------------------|
| INF.7.A1                     | Nicht erfüllt              |                                            |
| INF.7.A2                     | Nicht erfüllt              |                                            |
| INF.8.A1                     | Nicht erfüllt              |                                            |
| INF.8.A2                     | Teilweise Erfüllt          | Keine Vorgaben für Dokumente auf Pa- pier. |
| INF.8.A3                     | Nicht erfüllt              |                                            |
| INF.9.A1                     | Nicht erfüllt              |                                            |
| INF.9.A2                     | Erfüllt                    |                                            |
| INF.9.A3                     | Nicht erfüllt              |                                            |
| INF.9.A4                     | Nicht erfüllt              |                                            |
| INF.10.A1                    | Nicht erfüllt              |                                            |
| INF.10.A2                    | Nicht erfüllt              |                                            |
| INF.10.A3                    | Nicht erfüllt              |                                            |

<!-- page: 192 -->

## A.2 Anteil der erfüllten Anforderungen

Dieses Diagramm zeigt die Anteile der erfüllten, teilweise erfüllten und nicht erfüllten Anforderungen.

<!-- image -->

<!-- page: 193 -->

## Literaturverzeichnis

- [1] BUNDESAMT FÜR SICHERHEIT IN DER INFORMATIONSTECHNIK (BSI): Historie des BSI . Webseite, abgerufen am 10.03.2018: https://www.bsi.bund. de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/IT\_Grundschutz\_ Kompendium\_Edition2018.pdf .
- [2] BUNDESAMT FÜR SICHERHEIT IN DER INFORMATIONSTECHNIK (BSI): Leitfaden zur Basis-Absicherung nach IT-Grundschutz . Verfügbar unter: https: //www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/Broschueren/ Leitfaden\_zur\_Basis-Absicherung.pdf?\_\_blob=publicationFile&amp;v=3 .
- [3] BUNDESAMT FÜR SICHERHEIT IN DER INFORMATIONSTECHNIK (BSI): Studie zur IT-Sicherheit in kleinen und mittleren Unternehmen . Studie, 2011. Verfügbar unter: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/ Studien/KMU/Studie\_IT-Sicherheit\_KMU.pdf .
- [4] BUNDESAMT FÜR SICHERHEIT IN DER INFORMATIONSTECHNIK (BSI): CyberSicherheits-Umfrage 2015 . Umfrage, Oktober 2015. Verfügbar unter: https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/ cybersicherheitslage/umfrage2015\_ergebnisse.pdf .
- [5] BUNDESAMT FÜR SICHERHEIT IN DER INFORMATIONSTECHNIK (BSI): Die Lage der IT-Sicherheit in Deutschland 2017 . Bericht, Bundesamt für Sicherheit in der Informationstechnik (BSI), August 2017. Verfügbar unter: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/ Lageberichte/Lagebericht2017.pdf .
- [6] BUNDESAMT FÜR SICHERHEIT IN DER INFORMATIONSTECHNIK (BSI): IT-Grundschutz-Kompendium 1. Edition 2018 . Bundesanzeiger Verlag GmbH, Februar 2018. Verfügbar unter: https://www.bsi.bund.de/SharedDocs/Downloads/ DE/BSI/Grundschutz/Kompendium/IT\_Grundschutz\_Kompendium\_Edition2018.pdf .
- [7] ENGEMANN, PHILIPP, DERK FISCHER, BJÖRN GOSDZIK, TOBIAS KOLLER und NIAL MOORE: Im Visier der Cyber-Gangster - So gefährdet ist die Informationssicher-

<!-- page: 194 -->

heit im deutschen Mittelstand . Studie, PricewaterhouseCoopers AG Wirtschaftsprüfungsgesellschaft (PwC), Februar 2017. Verfügbar unter: https://www.pwc.de/de/ mittelstand/assets/it-sicherheit-im-mittelstand-neu.pdf .

- [8] VDS SCHADENVERHÜTUNG GMBH: VdS - Unternehmen . Webseite, abgerufen am 10.03.2018: https://vds.de/de/unternehmen/ .
- [9] VDS SCHADENVERHÜTUNG GMBH: VdS-Richtlinien für die Informationssicherheit - VdS 3473 . VdS Schadenverhütung GmbH, Juli 2015. Verfügbar unter: https:// shop.vds.de/de/download/67b944842126c7b00c5031b16c44ae87 .

<!-- page: 195 -->

Hiermit versichere ich, dass ich die vorliegende Arbeit selbstständig verfasst habe und keine anderen als die angegebenen Quellen und Hilfsmittel verwendet sowie Zitate

kenntlich gemacht habe.

Dortmund, den 7. April 2018

Florian Göhler

<!-- page: 196 -->

190

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 1 -->

> ii

> Lehrstuhl IV

<!-- page: 3 -->

> i

<!-- page: 4 -->

> ii

<!-- page: 5 -->

> iii
