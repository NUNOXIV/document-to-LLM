---
source_file: "Mindeststandard_Nutzung_externer_Cloud-Dienste_Version_2_1.pdf"
source_sha256: 5665e22bd1feac42cbcfc69898ae78c2971a8810beca5b14639b1910297d5a2d
source_bytes: 373380
pages: 18
tables: 3
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T20:34:29+00:00"
text_coverage_percent: 100.0
appended_source_lines: 1
restored_hyphens: 8
extraction_status: warn
warnings:
  - "8 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): C5Prüfbericht -> C5-Prüfbericht, CloudDienst -> Cloud-Dienst, CloudDienste -> Cloud-Dienste, CloudDiensteanbieter -> Cloud-Diensteanbieter, CloudDienstes -> Cloud-Dienstes"
  - "Der Textlayer der Quelle enthaelt 21 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
  - "1 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

<!-- image -->

## Mindeststandard des BSI zur Nutzung externer Cloud-Dienste

nach § 8 Absatz 1 Satz 1 BSIG - Version 2.1 vom 15.12.2022

<!-- image -->

<!-- page: 2 -->

## Änderungshistorie

|   Version | Datum      | Beschreibung                                                                                            |
|-----------|------------|---------------------------------------------------------------------------------------------------------|
|       1.0 | 24.04.2017 | Erstveröffentlichung                                                                                    |
|       2.0 | 07.07.2021 | Major Release - Zusammenführung der Mindeststandards zur Nutzung und Mitnutzung externer Cloud- Dienste |
|       2.1 | 15.12.2022 | Korrekturen, Ergänzungen und Begriffsanpassungen                                                        |

Tabelle 1: Versionsgeschichte des Mindeststandards. Eine ausführliche Änderungsübersicht zum Mindeststandard erhalten Sie unter: https://www.bsi.bund.de/dok/930566

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn

[E-Mail: mindeststandards@bsi.bund.de](mailto:mindeststandards@bsi.bund.de)

[Internet: https://www.bsi.bund.de](https://www.bsi.bund.de/)

© Bundesamt für Sicherheit in der Informationstechnik 2022

<!-- page: 3 -->

## Vorwort

Risiken für die Cyber- und Informationssicherheit sind nicht zuletzt aufgrund der zunehmenden Komplexität und Vernetzung von IT-Systemen allgegenwärtig. Dadurch betreffen potenzielle Schwachstellen und Cyber-Angriffe in der Regel nicht nur einzelne Stellen.

Umso wichtiger ist die Vorgabe verbindlicher Sicherheitsanforderungen an die Informationstechnik des Bundes. So kann ein einheitliches Mindestsicherheitsniveau mit effektiven Maßnahmen zur Abwehr von Cyber-Angriffen innerhalb der heterogenen Behördenlandschaft etabliert werden.

Dazu legt das Bundesamt für Sicherheit in der Informationstechnik (BSI) Mindeststandards (MST) für die Sicherheit der Informationstechnik des Bundes 1  fest. Dies erfolgt auf der Grundlage des § 8 Absatz 1 BSIG im Benehmen mit den Ressorts. Als gesetzliche Vorgabe definieren Mindeststandards somit ein verbindliches Mindestniveau für die Informationssicherheit.

Bereits 2017 hat das Bundeskabinett mit dem Umsetzungsplan Bund 2017 (UP Bund 2017) eine Leitlinie für Informationssicherheit in der Bundesverwaltung in Kraft gesetzt. Damit wurde die Beachtung der Mindeststandards für den Bereich der Stellen des Bundes verbindlich. Durch das IT-Sicherheitsgesetz 2.0 wurde die Einhaltung der Mindeststandards des BSI auch gesetzlich geregelt. Die Umsetzungspflicht der Mindeststandards ergibt sich aus dem dadurch neu gefassten § 8 BSIG.

Die Mindeststandards richten sich primär an IT-Verantwortliche, IT-Sicherheitsbeauftragte (IT-SiBe), Informationssicherheitsbeauftragte (ISB), IT-Betriebspersonal und Beschaffungsstellen. Die Gesamtverantwortung für die Informationssicherheit und damit auch für die Einhaltung der Mindeststandards trägt gemäß UP Bund 2017 die Leitung der jeweiligen Einrichtung 1 .

IT-Systeme sind in der Regel komplex und in ihren individuellen Anwendungsbereichen durch die unterschiedlichsten (zusätzlichen) Rahmenbedingungen und Anforderungen gekennzeichnet. Daher können sich in der Praxis regelmäßig höhere Anforderungen an die Informationssicherheit ergeben, als sie in den Mindeststandards beschrieben werden. Aufbauend auf dem Mindestsicherheitsniveau sind diese individuellen Anforderungen in der Planung, der Etablierung und im Betrieb der IT-Systeme zusätzlich zu berücksichtigen, um dem jeweiligen Bedarf an Informationssicherheit zu genügen. Die Vorgehensweise dazu beschreiben die IT-Grundschutz-Standards des BSI.

Zur Sicherstellung der Effektivität und Effizienz in der Erstellung und Betreuung von Mindeststandards arbeitet das BSI nach einer standardisierten Vorgehensweise. Zur Qualitätssicherung durchläuft jeder Mindeststandard mehrere Prüfzyklen einschließlich des Konsultationsverfahrens mit der Bundesverwaltung. 2  Über die Beteiligung bei der Erarbeitung von Mindeststandards hinaus kann sich jede Einrichtung auch bei der Erschließung fachlicher Themenfelder für neue Mindeststandards einbringen oder im Hinblick auf Änderungsbedarf für bestehende Mindeststandards Kontakt mit dem BSI aufnehmen. Einhergehend mit der Erarbeitung von Mindeststandards berät das BSI die Einrichtungen auf Ersuchen bei der Umsetzung und Einhaltung der Mindeststandards.

1  Die von den Mindeststandards adressierten Stellen werden in § 8 Absatz 1 BSI-Gesetz (BSIG) definiert (siehe https://www.gesetze-im-internet.de/bsig\_2009/\_\_8.html). Zur besseren Lesbarkeit wird im weiteren Verlauf für alle dort genannten Stellen der Begriff 'Einrichtung' verwendet.

[2  Siehe FAQ zu den MST: https://www.bsi.bund.de/DE/Themen/OeffentlicheVerwaltung/Mindeststandards/FAQ\_MST/faq\_mst\_node.html](https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/FAQ_MST/faq_mst_node.html)

<!-- page: 4 -->

## Inhalt

| 1                                                                                                                                                                                                            | Beschreibung .......................................................................................................................................................................................... 5    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1                                                                                                                                                                                                          | Begriffsbestimmung und Abgrenzung ............................................................................................................................ 5                                             |
| 1.2                                                                                                                                                                                                          | Modalverben ................................................................................................................................................................................ 6               |
| 2                                                                                                                                                                                                            | Sicherheitsanforderungen ................................................................................................................................................................ 7                  |
| 2.1                                                                                                                                                                                                          | Planungsphase ............................................................................................................................................................................. 7                |
| 2.2                                                                                                                                                                                                          | Beschaffungsphase .................................................................................................................................................................... 9                     |
| 2.3                                                                                                                                                                                                          | Einsatzphase ............................................................................................................................................................................... 12              |
| 2.4                                                                                                                                                                                                          | Beendigungsphase ................................................................................................................................................................... 14                      |
| 2.5                                                                                                                                                                                                          | Sicherheitsanforderungen bei einer Mitnutzung ..................................................................................................... 14                                                       |
| Literaturverzeichnis..................................................................................................................................................................................... 16 | Literaturverzeichnis..................................................................................................................................................................................... 16 |
| Abkürzungsverzeichnis .............................................................................................................................................................................. 18      | Abkürzungsverzeichnis .............................................................................................................................................................................. 18      |

<!-- page: 5 -->

## 1 Beschreibung

Dieser Mindeststandard setzt Sicherheitsanforderungen an die Nutzung externer Cloud-Dienste.

## 1.1 Begriffsbestimmung und Abgrenzung

Zur Begriffsbestimmung nutzt dieser Mindeststandard die Definition für Cloud-Dienste des Cloud Computing Compliance Criteria Catalogue - C5:2020 (Kriterienkatalog Cloud Computing) 3 , die sich an die internationale Begriffsdefinition des ISO 17788 anlehnt. 4  Cloud Computing bezeichnet das dynamisch an den Bedarf angepasste Anbieten, Nutzen und Abrechnen von IT-Dienstleistungen über ein Netz. Angebot und Nutzung dieser Dienstleistungen ('Cloud-Dienste') erfolgen dabei ausschließlich über definierte technische Schnittstellen und Protokolle. Die Spannbreite der in diesem Rahmen angebotenen Cloud-Dienste umfasst das komplette Spektrum der Informationstechnik und beinhaltet unter anderem Infrastruktur (z. B. Rechenleistung, Speicherplatz), Plattformen und Anwendungen.

Externe Cloud-Dienste im Sinne dieses Mindeststandards sind Cloud-Dienste, die von Anbietern der Wirtschaft außerhalb der öffentlichen Verwaltung des Bundes erbracht werden. 5

Als Nutzung eines Cloud-Dienstes sind das Speichern und Verarbeiten von dienstlichen Daten durch einen externen Cloud-Dienst zu verstehen. Dieser kann durch eine oder mehrere Einrichtungen beauftragt werden. Regelungen für das Mitnutzen externer Cloud-Dienste durch Benutzende 6  einer Einrichtung sind in Kapitel 2.5 beschrieben. Von einer Mitnutzung wird ausgegangen, wenn eine Einrichtung den externen Cloud-Dienst nicht selbst beauftragt hat bzw. zwischen dieser Einrichtung und dem Cloud-Diensteanbieter kein unmittelbares Vertragsverhältnis besteht.

Werden keine dienstlichen Daten verarbeitet, können die Regelungen des Mindeststandards dennoch hilfreiche Empfehlungen enthalten und trotzdem angewendet werden (siehe NCD.2.1.03, Buchstabe e). 7

3  Im Weiteren mit 'C5' abgekürzt, vgl. (BSI 2020a).

4  Der Standard 'ISO/IEC 17788:2014 Information technology - Cloud computing - Overview and vocabulary' (ISO 2014) definiert Cloud Computing als Paradigma für die Ermöglichung über ein Netz auf einen skalierbaren und elastischen Pool von geteilten virtuellen oder physischen Ressourcen (Server, Plattform, Anwendung, Software, etc.) zuzugreifen und über ein Selbst-Service Portal zu bestellen und selbst zu administrieren. Ein Cloud-Service ist als über eine definierte Schnittstelle buchbare und über Cloud Computing angebotene Fähigkeiten ('capabilities') definiert. Cloud-Fähigkeiten werden nach Infrastruktur, Plattform und Anwendung unterschieden.

5  Hinweis: Private Cloud-Dienste der IT-Dienstleister des Bundes (z. B. Bundescloud) fallen somit nicht unter diese Bestimmung.

6  Analog Rolle 'Benutzer' nach IT-Grundschutz-Kompendium, (BSI 2022a): 'Ein Benutzer ist ein Mitarbeiter einer Institution, der informationstechnische Systeme im Rahmen der Erledigung seiner Aufgaben benutzt. IT-Benutzer und Benutzer sind hierbei als Synonyme zu betrachten, da heutzutage nahezu jeder Mitarbeiter eines Unternehmens bzw. einer Behörde informationstechnische Systeme während der Erledigung seiner Aufgaben verwendet.', Kap. Rollen, S. 27

7  Hinweis: Für eine Beschreibung, wie sich die Anforderungsnummerierung zusammensetzt, siehe FAQ zu den Mindeststandards (BSI 2019).

<!-- page: 6 -->

## 1.2 Modalverben

In Anlehnung an den IT-Grundschutz 8  werden die Sicherheitsanforderungen mit den Modalverben MUSS und SOLLTE sowie den zugehörigen Verneinungen formuliert. Darüber hinaus wird das Modalverb KANN für ausgewählte Prüfaspekte verwendet. Die hier genutzte Definition basiert auf RFC 2119 9  und DIN 820-2: 2018 10 .

## MUSS / DARF NUR

bedeutet, dass diese Anforderung zwingend zu erfüllen ist. Das von der Nichtumsetzung ausgehende Risiko kann im Rahmen einer Risikoanalyse nicht akzeptiert werden.

## DARF NICHT / DARF KEIN

bedeutet, dass etwas zwingend zu unterlassen ist. Das durch die Umsetzung entstehende Risiko kann im Rahmen einer Risikoanalyse nicht akzeptiert werden.

## SOLLTE

bedeutet, dass etwas umzusetzen ist, es sei denn, im Einzelfall sprechen gute Gründe gegen eine Umsetzung. Die Begründung muss dokumentiert und bei einem Audit auf ihre Stichhaltigkeit geprüft werden können.

## SOLLTE NICHT / SOLLTE KEIN

bedeutet, dass etwas zu unterlassen ist, es sei denn, es sprechen gute Gründe für eine Umsetzung. Die Begründung muss dokumentiert und bei einem Audit auf ihre Stichhaltigkeit geprüft werden können.

## KANN

bedeutet, dass die Umsetzung oder Nicht-Umsetzung optional ist und ohne Angabe von Gründen unterbleiben kann.

8  Vgl. BSI-Standard 200-2 (BSI 2017a), S. 18

9  Vgl. Key words for use in RFCs (IETF 1997)

10  Vgl. DIN-820-2: Gestaltung von Dokumenten (DIN 2018)

<!-- page: 7 -->

## 2 Sicherheitsanforderungen

Nachfolgende Sicherheitsanforderungen adressieren die Informationssicherheit entlang des gesamten Lebenszyklus und setzen auf den IT-Grundschutz-Baustein OPS.2.2 Cloud-Nutzung 11  auf.

## 2.1 Planungsphase

Grundlage der Informationssicherheit im Bereich Cloud Computing bilden nach dem IT-Grundschutz-Baustein OPS.2.2 Cloud-Nutzung

- die Strategie für die Cloud-Nutzung,
- die darauf basierende Sicherheitsrichtlinie sowie
- das jeweilige Sicherheitskonzept für den externen Cloud-Dienst.

Die nachfolgenden Sicherheitsanforderungen adressieren diese Dokumente entsprechend.

## NCD.2.1.01 Strategie für die Cloud-Nutzung

a) Die Einrichtung MUSS eine Strategie für die Cloud-Nutzung nach OPS.2.2.A1 Erstellung einer Strategie für die Cloud-Nutzung 12  erstellen.

b) Die Einrichtung MUSS in dieser Strategie für die Cloud-Nutzung festlegen, wie sie mit Risiken bei der Nutzung externer Cloud-Dienste umgeht. Hierzu MUSS eine Richtlinie zur Risikoanalyse erstellt werden. 13

c) Die Einrichtung MUSS prüfen, ob ein externer Cloud-Dienst grundsätzlich mit den in ihrer Strategie für die Cloud-Nutzung definierten Zielen, Chancen und Risiken vereinbar ist.  14  Die Einrichtung DARF einen externen Cloud-Dienst NUR nutzen, wenn dieser die in der Strategie für die Cloud-Nutzung definierten Ziele, Chancen und Risiken angemessen unterstützt.

d) Die Einrichtung MUSS vor der Nutzung eines externen Cloud-Dienstes eine Risikoanalyse gemäß der in NCD.2.1.01 b) festgelegten Richtlinie durchführen.

## NCD.2.1.02 Sicherheitsrichtlinie für externe Cloud-Dienste

a) Die Einrichtung MUSS eine Sicherheitsrichtlinie für externe Cloud-Dienste nach OPS.2.2.A2 Erstellung einer Sicherheitsrichtlinie für die Cloud-Nutzung 15 erstellen.

b) Die Einrichtung MUSS in dieser Sicherheitsrichtlinie mindestens die Umsetzung und Einhaltung der Basiskriterien nach dem Cloud Computing Compliance Criteria Catalogue - C5 (Kriterienkatalog Cloud Computing) als spezielle Sicherheitsanforderungen an den Cloud-Diensteanbieter festlegen. 16

c) Die Einrichtung MUSS die IT-Sicherheitsbeauftragten bei der Erstellung der Sicherheitsrichtlinie beteiligen und ebenfalls - sofern betroffen - die zuständigen Datenschutz- und Geheimschutzbeauftragten.

11  IT-Grundschutz-Kompendium, (BSI 2022a), OPS.2.2 Cloud-Nutzung

12  IT-Grundschutz-Kompendium, (BSI 2022a), OPS.2.2 Cloud-Nutzung

13 Siehe BSI-Standard 200-3, (BSI 2017b), S. 9f.

14  Hinweis: OPS.2.2.A1 Erstellung einer Strategie für die Cloud-Nutzung sieht die Erstellung einer Strategie für die Cloud-Nutzung vor. In dieser erfasst die Einrichtung ihre Ziele, Chancen und Risiken, die sie mit einer Cloud-Nutzung generell verbindet. Die Strategie für die Cloud-Nutzung nimmt daher eine zentrale Rolle für die Einrichtung ein. Sie wird benötigt, um die beabsichtigte Nutzung eines konkreten externen Cloud-Dienstes bewerten zu können.

15  IT-Grundschutz-Kompendium, (BSI 2022a), OPS.2.2 Cloud-Nutzung

16  Cloud Computing Compliance Criteria Catalogue - C5:2020 (Kriterienkatalog Cloud Computing), (BSI 2020a), S.1ff.

<!-- page: 8 -->

## NCD.2.1.03 Sicherheitskonzept für den externen Cloud-Dienst

a) Die Einrichtung MUSS ein Sicherheitskonzept für den externen Cloud-Dienst nach OPS.2.2.A7 Erstellung eines Sicherheitskonzeptes für die Cloud-Nutzung 17  erstellen.

b) Die Einrichtung MUSS in dem Sicherheitskonzept die aktuellen Veröffentlichungen des BSI zu CloudSicherheit berücksichtigen. 18

c) Die Einrichtung MUSS die IT-Sicherheitsbeauftragten bei der Erstellung des Sicherheitskonzeptes beteiligen und ebenfalls - sofern betroffen - die zuständigen Datenschutz- und Geheimschutzbeauftragten.

d) Die Einrichtung MUSS sämtliche dienstliche Daten identifizieren, die künftig in dem externen Cloud-Dienst verarbeitet werden sollen.

e) Kommt die Einrichtung zu dem Ergebnis, dass in dem externen Cloud-Dienst keine dienstlichen Daten 19 verarbeitet werden, handelt es sich nicht um eine Nutzung oder Mitnutzung externer Cloud-Dienste im Sinne dieses Mindeststandards. In diesen Fällen KANN die Einrichtung die Sicherheitsanforderungen des Mindeststandards umsetzen.

f) Die Einrichtung MUSS die identifizierten dienstlichen Daten den nachfolgenden Kategorien zuordnen:

- Kategorie 1 = Privat-, Dienst-, Betriebs- und Geschäftsgeheimnisse gemäß Strafgesetzbuch (StGB) §§ 203 und 353b
- Kategorie 2 = personenbezogene Daten gemäß Datenschutz-Grundverordnung (DSGVO) Art. 4 Nr. 1
- Kategorie 3 = Verschlusssachen gemäß Verschlusssachenanweisung - VSA 20
- Kategorie 4 = sonstige Daten (weder Kategorie 1, noch 2, noch 3)

g) Die Einrichtung KANN die identifizierten dienstlichen Daten den Kategorien 1, 2 und 3 gleichzeitig zuordnen.

h) Falls Daten den Kategorien 1, 2 oder 3 zugeordnet wurden: Die Einrichtung MUSS für die identifizierten dienstlichen Daten dieser Kategorien die Geheim- und Datenschutzaspekte 21  sowie Anforderungen hinsichtlich Privat-, Dienst, Betriebs- und Geschäftsgeheimnisse ermitteln und aus diesen ggf. entstehende weitere Anforderungen ableiten.

i) Die Einrichtung MUSS Risiken, die aus der künftigen Nutzung des externen Cloud-Dienstes entstehen können, umfassend ermitteln und bewerten. 22  Die Einrichtung MUSS die ermittelten Risiken gemäß der in der Strategie für die Cloud-Nutzung festgelegten Richtlinie zur Risikoanalyse bewerten.

ii) Die Einrichtung DARF den externen Cloud-Dienst NUR nutzen, wenn alle ermittelten Risiken gemäß der in der Strategie für die Cloud-Nutzung genannten Richtlinie zur Risikoanalyse wirksam vermieden oder hinreichend reduziert oder in Übereinstimmung mit den Risikoakzeptanzkriterien bei der Cloud-Nutzung getragen werden können.

17  IT-Grundschutz-Kompendium, (BSI 2022a), OPS.2.2 Cloud-Nutzung

18  Siehe Veröffentlichungen unter https://www.bsi.bund.de/cloud

19  Dienstliche Daten können gleichzeitig auch personenbezogene Daten sein. Für den Zweck dieses Mindeststandards sind jedoch nicht solche personenbezogenen Daten (wie Stammdaten, Nutzungsdaten), die für die Registrierung und Nutzung des Dienstes vom Cloud-Diensteanbieter erhoben oder verarbeitet werden, gemeint.

20  Allgemeine Verwaltungsvorschrift zum materiellen Geheimschutz (Verschlusssachenanweisung - VSA), (BMI 2018)

21  Hinsichtlich Datenschutzaspekte siehe insbesondere (AKTM 2014), S.1ff.

22  Hinweis: Es gilt, zu bewerten, inwiefern die mit dem betrachteten Cloud-Dienst im beabsichtigten Anwendungsfall verbundenen rechtlichen, technischen und organisatorischen Risiken mit der Strategie für die Cloud-Nutzung vereinbar sind.

<!-- page: 9 -->

i) Die Einrichtung MUSS prüfen, ob sie weiteren Anforderungen (z. B. aus Gesetzen, Verordnungen, Beschlüssen oder anderen Quellen) 23  unterliegt, die hinsichtlich der Cloud-Nutzung relevant sind. Diese Anforderungen MUSS die Einrichtung einhalten. Sie werden im Übrigen durch diesen Mindeststandard nicht berührt.

## NCD.2.1.04 Notfall- und Kontinuitätsmanagement

Mit Notfall- bzw. Kontinuitätsmanagement ist gemäß BSI-Standard 100-4 24  ein Managementsystem zur Aufrechterhaltung einer definierten Arbeitsfähigkeit einer Einrichtung gemeint. Es umfasst sowohl präventive als auch reaktive Maßnahmen, mit denen eine Einrichtung auf Notfälle und Krisensituationen reagiert. Es gilt im Weiteren die Begrifflichkeit des BSI-Standards 100-4. 25

a) Die Einrichtung MUSS bewerten, welche Bedeutung der externe Cloud-Dienst in Notfällen und Krisensituationen einnehmen würde. 26

b) Die Einrichtung MUSS prüfen, ob sie in Notfällen und Krisensituationen weiter auf den externen Cloud-Dienst zugreifen können muss. 27

c) Die Einrichtung MUSS die zuständigen Notfallbeauftragten entsprechend einbinden. Diese MÜSSEN prüfen, ob sich die Cloud-Nutzung auf Maßnahmen, die Notfällen und Krisensituationen präventiv und/oder reaktiv entgegenwirken, auswirkt und inwiefern diese Maßnahmen ggf. anzupassen sind. Die Einrichtung MUSS diese Änderungen vor der Cloud-Nutzung umsetzen. 28

## 2.2 Beschaffungsphase

Ziel des Beschaffungsprozesses, für den die Vorgaben des Vergaberechts einschlägig sind, ist die Auswahl eines geeigneten Cloud-Diensteanbieters. Hinsichtlich der Beschaffung externer Cloud-Dienste sollte die Einrichtung insbesondere die einschlägigen 'Ergänzenden Vertragsbedingungen für Cloudleistungen (EVBIT Cloud)' 29  beachten und nutzen.

## NCD.2.2.01 Umsetzung der Sicherheitsanforderungen

a) Die Einrichtung MUSS vor Vertragsabschluss bewerten, inwiefern der externe Cloud-Dienst die in ihrer Sicherheitsrichtlinie festgelegten Sicherheitsanforderungen (siehe NCD.2.1.02, Buchstabe a) erfüllt. 30

b) Die Einrichtung MUSS die Erfüllung dieser Sicherheitsanforderungen bereits in der Leistungsbeschreibung des externen Cloud-Dienstes einfordern. 31

c) Die Einrichtung MUSS die Angaben und Nachweise des Cloud-Diensteanbieters zu Buchstabe 0 hinsichtlich Inhalt, Aussagekraft, Nachvollziehbarkeit, Aktualität, nachteiliger Regelungen sowie Mitwirkungspflichten und Maßnahmen auswerten. Dazu SOLLTE der Leitfaden mit Checkliste zur Auswertung einer Berichterstattung nach BSI C5 32  verwendet werden.

23  Auf die geltenden Regelungen zur Verwendung einer Eigenerklärung und einer Vertragsklausel in Vergabeverfahren im Hinblick auf Risiken durch nicht offengelegte Informationsabflüsse an ausländische Sicherheitsbehörden wird in diesem Zusammenhang entsprechend verwiesen. (BMI 2014), S.1

24  BSI-Standard 100-4 - Notfallmanagement, (BSI 2008), S.1ff.

25  BSI-Standard 100-4 - Notfallmanagement, (BSI 2008), S.1ff.

26  Hinweis: Leitfragen für diese Prüfung können sein: Wie zeitkritisch sind die Geschäftsprozesse (bzw. Fachaufgaben), die den Cloud-Dienst in einem Notfall oder einer Krise benötigen? Zu welchem Grad wird der Cloud-Dienst in einem Notbetrieb benötigt?

27  Hinweis: Leitfragen für diese Prüfung können sein: Wird der Cloud-Dienst für einen im Notfallmanagement als zeitkritisch bewerteten Geschäftsprozess (bzw. Fachaufgabe) genutzt? Dient der Cloud-Dienst zur Etablierung und Aufrechterhaltung eines Notbetriebs? Ist der Cloud-Dienst für die Bewältigung eines Notfalls relevant?

28  Siehe OPS.2.2.A11 Erstellung eines Notfallkonzeptes für einen Cloud-Dienst, (BSI 2022a)

29  Vgl. EVB-IT Cloud, (BMI 2022)

30  Hinweis: Liegt ein C5-Prüfbericht vor, können diesem Informationen entnommen und der Bewertung zugrunde gelegt werden.

31  Siehe OPS.2.2.A8 Sorgfältige Auswahl eines Cloud-Diensteanbieters, (BSI 2022a)

<!-- page: 10 -->

d) Die Einrichtung MUSS sich die regelmäßige Vorlage von Sicherheitsnachweisen vom Cloud-Diensteanbieter zusichern lassen.

e) Diese Sicherheitsnachweise SOLLTEN mindestens

- die angemessene und wirksame Erfüllung der Basiskriterien nach C5 33 ,
- die aktuelle Dokumentation der Systembeschreibung 34 ,
- die Aktualität von vertraglich zugesicherten Zertifizierungen und Berichterstattungen sowie
- die ordnungsgemäße Durchführung von Datensicherungen und erprobten Rücksicherungen

umfassen und KÖNNEN vom Cloud-Diensteanbieter durch die regelmäßige Bereitstellung einer aktuellen C5-Berichterstattung vom Typ2 erbracht werden.

f) Die Einrichtung MUSS die Sicherheitsnachweise des Cloud-Diensteanbieters auswerten und eventuellen Unklarheiten und insbesondere darin ausgewiesene Abweichungen in geeigneter Form nachgehen. Hierbei MUSS die Einrichtung auch abwägen, ob und inwiefern ein Risiko entsteht und wie mit diesem umzugehen ist.

g) Insbesondere MÜSSEN Zertifikate, Prüfberichte und Nachweise den Zeitraum, in dem die Einrichtung den Cloud-Dienst nutzt, jeweils vollständig abdecken und DÜRFEN KEINE zeitlichen Lücken enthalten oder entstehen lassen. Dies MUSS die Einrichtung in ihre Sicherheitsanforderungen sowie demzufolge in die Leistungsbeschreibung aufnehmen.

h) Die Einrichtung MUSS sich die Einhaltung vorgesehener und vereinbarter Prozesse sowie die Durchführung von Audits, Sicherheitsprüfungen, Penetrationstests und Schwachstellenanalysen durch den Cloud-Diensteanbieter vertraglich zusichern lassen.

i) Die Einrichtung MUSS ermittelte Risiken, die nicht bereits durch Basiskriterien nach C5 abgedeckt sind, über zusätzliche Anforderungen, die vom Cloud-Diensteanbieter zu erfüllen sind, abdecken oder diese Risiken transferieren oder akzeptieren, und MUSS dies entsprechend dokumentieren.

i) Die Einrichtung MUSS die weiteren Anforderungen nach NCD.2.1.03, Buchstabe i, in ihre Sicherheitsanforderungen aufnehmen. Soweit die Einrichtung diese weiteren Anforderungen nur gemeinsam mit dem Cloud-Diensteanbieter erfüllen kann, MUSS die Einrichtung diese in die Leistungsbeschreibung bzw. in das Vertragsverhältnis mit dem Cloud-Diensteanbieter aufnehmen.

ii) Für die zusätzlichen Anforderungen MUSS die Einrichtung mit dem Cloud-Diensteanbieter vereinbaren, dass dieser regelmäßig geeignete Nachweise ihrer angemessenen und wirksamen Umsetzung vorlegt. Falls die Anforderungen nur gemeinsam erfüllt werden können, erstrecken sich die Nachweise nur auf den Anteil, der vom Cloud-Diensteanbieter umgesetzt wird.

32  Hinweis: Der Auswertungsleitfaden gibt eine Struktur vor, die dabei unterstützt, einen C5-Prüfbericht systematisch auszuwerten. Diese Auswertung beinhaltet, die Sicherheitsmaßnahmen (Kontrollen) des Cloud-Diensteanbieters inklusive der zugehörigen Prüfergebnisse sowie der auf Cloud-Nutzendenseite einzurichtenden Kontrollen aufzunehmen. In Verbindung mit den aufseiten der Einrichtung eingerichteten Kontrollen sowie weiterer, vom individuellen Anwendungsfall abhängenden Informationen lassen sich die mit der Nutzung des betrachteten Cloud-Dienstes verbundenen Risiken identifizieren und bewerten. Siehe 'Leitfaden mit Checkliste zur Auswertung einer Berichterstattung nach BSI C5', (BSI 2020b).

33  Hinweis: Die im C5 festgelegten Übergangsfristen für neue Versionen sind zu beachten.

34 Hinweis: Im Falle einer 'direkten Prüfung' (vgl. C5, (BSI 2020a), Kap. 3.4.3.2, S.23f.) enthält der Bericht keine vom Cloud-Diensteanbieter angefertigte Systembeschreibung, sondern eine vom Prüfenden im Rahmen der Prüfung angefertigte Systembeschreibung.

<!-- page: 11 -->

j) Die Einrichtung SOLLTE sich eigene Prüfrechte vertraglich zusichern lassen.

i) Die Einrichtung MUSS die Prüfrechte so ausgestalten, dass die Einrichtung ihre weiteren Anforderungen (z. B. aus Gesetzen, Verordnungen, Beschlüssen oder anderen Quellen) erfüllt.

ii) Die Einrichtung MUSS die Prüfrechte so ausgestalten, dass sie nach Art und Umfang eine Bewertung des vom Cloud-Diensteanbieter für den betrachteten Cloud-Dienst gebotenen Informationssicherheitsniveaus ermöglichen und die Einrichtung selbst oder Dritte in ihrem Auftrag (z. B. andere Stellen, externe IT-Revision, Wirtschaftsprüfende) die Prüfrechte wahrnehmen können.

iii) Sofern der Cloud-Diensteanbieter keinen Prüfbericht nach C5 vorlegen kann, MUSS sich die Einrichtung vom Cloud-Diensteanbieter dazu berechtigen lassen, die Prüfung nach C5 durch Dritte selbst beauftragen zu können.

iv) Aufgrund der Ergebnisse aus der Datenkategorisierung und Risikoanalyse KANN die Einrichtung in begründeten Fällen auf eigene Prüfrechte verzichten, soweit weitere Anforderungen (z. B. aus Gesetzen, Verordnungen, Beschlüssen oder anderen Quellen) nicht entgegenstehen.

## NCD.2.2.02 Umgang mit Unterauftragnehmern und anderen externen Dritten

a) Die Einrichtung MUSS sich vom Cloud-Diensteanbieter vollständig benennen lassen, welche seiner Unterauftragnehmer gemäß C5 als Subdienstleistungsunternehmen 35  anzusehen sind und auf welche Art und in welchem Umfang er diese in die Bereitstellung des Cloud-Dienstes einbezieht. 36

b) Die Einrichtung MUSS mit dem Cloud-Diensteanbieter vereinbaren, dass er der Einrichtung beabsichtigte Änderungen an vertraglichen Vereinbarungen mit Subdienstleistungsunternehmen, die in die Bereitstellung des Cloud-Dienstes involviert sind, unverzüglich schriftlich oder per E-Mail mitteilt.

i) Diese Mitteilung SOLLTE zeitlich vor Umsetzung der Änderung erfolgen.

ii) Der Cloud-Diensteanbieter MUSS der Einrichtung insbesondere mitteilen, wenn er bestehende Vertragsverhältnisse beendet oder neue Vertragsverhältnisse mit Subdienstleistungsunternehmen eingeht. Vertragsverhältnisse in diesem Sinne schließen alle mitgeltenden Dokumente und Regelungen, wie z. B. Leistungsscheine, Dienstgütevereinbarungen oder Allgemeine Geschäfts- und Einkaufsbedingungen ein.

c) Diese Mitteilungen KANN der Cloud-Diensteanbieter z. B. über Internetportale oder PushBenachrichtigungen bereitstellen, wenn die Einrichtung diese Anforderungen als erfüllt ansieht.

d) Falls der Cloud-Diensteanbieter Subdienstleistungsunternehmen einbezieht oder anderweitig wesentliche Teile der Entwicklung oder Bereitstellung des Cloud-Dienstes an Unterauftragnehmer auslagert, MUSS sich die Einrichtung vom Cloud-Diensteanbieter zusichern lassen, dass

- die Subdienstleistungsunternehmen und Unterauftragnehmer die zwischen der Einrichtung und dem Cloud-Diensteanbieter vertraglich festgelegten Vorgaben ebenfalls erfüllen und
- sich die Prüfrechte, die der Cloud-Diensteanbieter der Einrichtung zugesichert hat, auch auf die Subdienstleistungsunternehmen und Unterauftragnehmer des Cloud-Diensteanbieters beziehen.

## NCD.2.2.03 Gerichtsbarkeit

a) Die Einrichtung SOLLTE zur Absicherung der Verfügbarkeit als Teil der Informationssicherheit Vereinbarungen ausschließlich nach deutschem Recht und deutschem Gerichtsstand und ohne obligatorisch vorab zu betreibende Schlichtungsverfahren abschließen.

35  Kriterienkatalog Cloud Computing (C5:2020), (BSI 2020a), Kap. 3.4.5, S.25f.

36  Siehe OPS.2.2.A9 Vertragsgestaltung mit dem Cloud-Diensteanbieter, (BSI 2022a)

<!-- page: 12 -->

b) Die Einrichtung MUSS berücksichtigen, dass bei gegebenenfalls notwendigem Rechtsschutz beziehungsweise Eilrechtsschutz Zeitverluste eintreten können, insbesondere durch eine Einarbeitung in fremde Rechtsordnungen oder ein Auftreten vor entfernt gelegenen Gerichten.

c) Die Einrichtung MUSS beim Verhandeln des Vertrages sicherstellen, dass sie handlungsfähig bleibt und ihre Forderungen effektiv durchsetzen kann.

## NCD.2.2.04 Lokation der Datenverarbeitung

a) Die Einrichtung MUSS prüfen, ob die dienstlichen Daten an den vertraglich zugesicherten Lokationen verarbeitet werden dürfen. Hierzu MUSS die Einrichtung die Ergebnisse der Datenkategorisierung und der Risikoanalyse, das mögliche Risiko eines fremdstaatlichen Zugriffs (z. B. durch Nachrichtendienste oder Ermittlungsbehörden) sowie weitere Anforderungen (z. B. aus Gesetzen, Verordnungen, Beschlüssen oder anderen Quellen) bewerten.

b) Die Einrichtung MUSS sämtliche Lokationen, an denen der Cloud-Diensteanbieter mit dem Cloud-Dienst dienstliche Daten speichert und verarbeitet, vertraglich festlegen. Dabei MUSS die Einrichtung auch Datensicherungen berücksichtigen, da diese ggf. an Drittlokationen durchgeführt werden. 37

## NCD.2.2.05 Meldepflicht sicherheitsrelevanter Vorfälle

a) Die Einrichtung MUSS die Pflichten des Cloud-Diensteanbieters, sicherheitsrelevante Vorfälle (sowie ggf. andere Vorfälle) gegenüber der Einrichtung zu melden, vertraglich regeln.

i) Die Einrichtung MUSS beim Festlegen von Vertragsstrafen und Haftungsfragen auf ein angemessenes Verhältnis zum ermittelten Schutzbedarf der mit dem Cloud-Dienst verarbeiteten dienstlichen Daten achten.

ii) Beim Festlegen von Vertragsstrafen und Haftungsregelungen sind die aus rechtlicher Sicht zulässigen Grenzen zu berücksichtigen. Die Einrichtung SOLLTE bei der Ansetzung von Vertragsstrafen 5% des Auftragsvolumens nicht unterschreiten.

## NCD.2.2.06 Beendigung des Vertragsverhältnisses

a) Die Einrichtung MUSS dem Anwendungsfall angemessene Kündigungsfristen festlegen. 38

b) Soweit rechtlich möglich, MUSS die Einrichtung kurzfristige einseitige Kündigungs- oder Zurückbehaltungsrechte an den Leistungen zu Lasten der Einrichtung ausschließen.

## NCD.2.2.07 Regelung der Datenrückgabe und Datenlöschung

a) Die Einrichtung MUSS mit dem Cloud-Diensteanbieter vertraglich regeln, wie dieser die mit dem Cloud-Dienst verarbeiteten dienstlichen Daten nach Beendigung der Nutzung an die Einrichtung übergibt (z. B. Fristen, Datenformat, Datenträger, Protokolle).

b) Die Einrichtung MUSS mit dem Cloud-Diensteanbieter vertraglich regeln, welche Maßnahmen dieser zur Löschung der dienstlichen Daten durchführt. Dabei MUSS die Einrichtung sicherstellen, dass die Maßnahmen dem zuvor ermittelten Schutzbedarf entsprechen. 39

## 2.3 Einsatzphase

Die Mindestanforderungen an den Einsatz von externen Cloud-Diensten regeln, wie die vertraglich zugesicherten Leistungen überwacht und überprüft werden.

37  Siehe OPS.2.2.A9 Vertragsgestaltung mit dem Cloud-Diensteanbieter, (BSI 2022a)

38  Siehe OPS.2.2.A9 Vertragsgestaltung mit dem Cloud-Diensteanbieter und OPS.2.2.A14 Geordnete Beendigung eines Cloud-Nutzungs-Verhältnisses, (BSI 2022a)

39  Siehe OPS.2.2.A9 Vertragsgestaltung mit dem Cloud-Diensteanbieter, (BSI 2022a)

<!-- page: 13 -->

## NCD.2.3.01 Einbindung in das ISMS

a) Die Einrichtung MUSS den externen Cloud-Dienst in ihr eigenes Informationssicherheitsmanagementsystem (ISMS) einbinden. 40

b) Die Einrichtung MUSS die im C5-Bericht genannten korrespondierenden Kontrollen für Cloud-Kunden 41 in ihrem ISMS einrichten. Die Einrichtung SOLLTE darüber hinaus die im C5 beschriebenen korrespondierenden Kriterien für Kunden berücksichtigen.

## NCD.2.3.02 Auswertung von Sicherheitsnachweisen

a) Die Einrichtung MUSS die Nachweise und sonstige Berichte des Cloud-Diensteanbieters auswerten. 4243

- i) Diese DÜRFEN über den Nutzungszeitraum KEINE zeitlichen Lücken enthalten.
2. ii) Ergeben sich aus der Auswertung Unklarheiten, MUSS die Einrichtung diesen nachgehen.

b) Die Einrichtung MUSS prüfen, ob festgestellten Unklarheiten durch Wahrnehmung der zugesicherten Prüf- und Kontrollrechte nachzugehen ist.

## NCD.2.3.03 Prüfung der Leistungsfähigkeit

a) Die Einrichtung MUSS mindestens jährlich die Leistungsfähigkeiten ihrer eigenen IT-Infrastruktur, wie Performance der Netzanbindung und -verbindungen, vor dem Hintergrund der Nutzung des Cloud-Dienstes beurteilen.

b) Die Einrichtung MUSS ggf. auftretende Abweichungen bewerten und auf diese durch geeignete Anpassungen an der eigenen IT-Infrastruktur und Netzanbindung reagieren.

c) Die Einrichtung MUSS mindestens jährlich die Leistungsfähigkeiten des Cloud-Diensteanbieters und des Cloud-Dienstes sowie der Netzverbindung zum Cloud-Diensteanbieter beurteilen. 4445

## NCD.2.3.04 Informationspflichten

a) Die Einrichtung MUSS nachhalten, dass der Cloud-Diensteanbieter seinen vertraglichen Informationspflichten stets nachkommt. Dies gilt insbesondere bei

- einer Eingliederung des Cloud-Diensteanbieters in ein anderes Unternehmen oder einen anderen Konzern oder in sonstigen Fällen des Wechsels des wirtschaftlichen Eigentums an ihm,
- einem Austausch von Unterauftragnehmern oder Dritten (siehe hierzu auch NCD.2.2.02).

40  Siehe OPS.2.2.A12 Aufrechterhaltung der Informationssicherheit im laufenden Cloud-Nutzungs-Betrieb, (BSI 2022a)

41  Hinweis: Der C5 führt in Version 2020 mit den korrespondierenden Kriterien für Kunden bestimmte Mitwirkungspflichten des Cloud-Kunden ein. Der C5 hält Cloud-Diensteanbieter dazu an, diese Mitwirkungspflichten, abhängig von der Art des Cloud-Dienstes, zu definieren und in den C5-Prüfbericht als korrespondierende Kontrollen für Cloud-Kunden aufzunehmen. Es liegt im Verantwortungsbereich des Cloud-Kunden und damit der Einrichtung, den Mitwirkungspflichten entsprechende Kontrollen zu gestalten, einzurichten und durchzuführen. Dies ist entscheidend für die Aufrechterhaltung der Informationssicherheit eines Cloud-Dienstes. Siehe C5, (BSI 2020a), S.15

42  Siehe OPS.2.2.A13 Nachweis einer ausreichenden Informationssicherheit bei der Cloud-Nutzung, (BSI 2022a)

43  Siehe 'Leitfaden mit Checkliste zur Auswertung einer Berichterstattung nach BSI C5', (BSI 2020b)

44  Siehe OPS.2.2.A12 Aufrechterhaltung der Informationssicherheit im laufenden Cloud-Nutzungs-Betrieb, (BSI 2022a)

45  Hinweis: Viele Cloud-Diensteanbieter stellen für die Beurteilung ihrer Leistungsfähigkeit geeignete Information kontinuierlich (bspw. in Portalen oder auf Webseiten) bereit. Einrichtungen können basierend auf diesen sowie ggf. weiteren, selbst erhobenen Informationen die Leistungsfähigkeit von Cloud-Diensteanbietern kontinuierlich überwachen. Eine in geeigneter Weise durchgeführte kontinuierliche Überwachung kann die Basis für die geforderte, mindestens jährlich durchzuführende Bewertung der Leistungsfähigkeit eines Cloud-Diensteanbieters sein, aber sie nicht vollständig ersetzen.

<!-- page: 14 -->

b) Die Einrichtung MUSS Meldungen des Cloud-Diensteanbieters über relevante Störungen und Cyber-Angriffe dokumentieren und auf diese gemäß der vereinbarten Mitwirkungspflichten nach NCD.2.2.01, Buchstabe c, reagieren.

## NCD.2.3.05 Multi-Faktor-Authentisierung

a) Bietet der externe Cloud-Dienst eine Multi-Faktor-Authentisierung für Anmeldungen von Benutzenden (Log-in) an, SOLLTE die Einrichtung diese nutzen.

b) Bietet der externe Cloud-Dienst eine Multi-Faktor-Authentisierung für Anmeldungen von Benutzenden mit privilegierten Rechten (Log-in), wie bspw. zur Administration, an, MUSS die Einrichtung diese nutzen. 46

## 2.4 Beendigungsphase

Mindestanforderungen an die Beendigung der Cloud-Nutzung adressieren die geordnete Beendigung des Vertragsverhältnisses. 47

## NCD.2.4.01 Datenrückgabe bei Beendigung

a) Die Einrichtung MUSS prüfen, ob der Cloud-Diensteanbieter alle dienstlichen Daten in der vereinbarten Form zurück übergeben hat. 48

b) Die Einrichtung MUSS die Übergabe dokumentieren.

## NCD.2.4.02 Datenlöschung bei Beendigung

a) Die Einrichtung MUSS sich vom Cloud-Diensteanbieter die gem. NCD.2.2.07 erfolgte Löschung aller dienstlichen Daten, einschließlich vorhandener Datensicherungen, bestätigen lassen. 49  Dies umfasst die

Bestätigung, dass die dienstlichen Daten gemäß der vertraglich vereinbarten Verfahren gelöscht wurden. b) Die Bestätigung nach Buchstabe a MUSS auch Daten und Datensicherungen bei möglichen Unterauftragnehmern (z. B. Subdienstleistungsunternehmen) und anderen externen Dritten umfassen.

c) Die Einrichtung MUSS die durch den Cloud-Diensteanbieter bestätigte Datenlöschung dokumentieren.

## 2.5 Sicherheitsanforderungen bei einer Mitnutzung

Nutzen die Benutzenden einer Einrichtung einen externen Cloud-Dienst, ohne dass zwischen dieser Einrichtung und dem Cloud-Diensteanbieter ein Vertragsverhältnis besteht, geht dieser Mindeststandard von einer sog. Mitnutzung aus. 50  Die nachfolgenden Sicherheitsanforderungen regeln die Mitnutzung externer Cloud-Dienste.

## NCD.2.5.01 Mitnutzung externer Cloud-Dienste

a) Die Einrichtung MUSS sicherstellen, dass die Mitnutzung mit der eigenen Strategie für die Cloud-Nutzung (siehe NCD.2.1.01) vereinbar ist.

b) Die Einrichtung MUSS die Sicherheitsanforderungen nach NCD.2.1.03, Buchstaben d bis i, umsetzen und einhalten.

c) Die Einrichtung MUSS ermitteln, an welchen Lokationen mit dem externen Cloud-Dienst dienstliche Daten verarbeitet werden. Dies schließt auch Datensicherungen sowie, sofern gegeben, Unterauftragnehmer und Subdienstleister des Cloud-Diensteanbieters ein.

i) Die Einrichtung MUSS bewerten, ob die dienstlichen Daten an diesen Lokationen verarbeitet werden dürfen.

46  Siehe ORP.4.A10 Schutz von Benutzerkennungen mit weitreichenden Berechtigungen, (BSI 2022a)

47  Siehe OPS.2.2.A14 Geordnete Beendigung eines Cloud-Nutzungsverhältnisses, (BSI 2022a)

48  Siehe OPS.2.2.A15 Sicherstellung der Portabilität von Cloud-Diensten, (BSI 2022a)

49  Hinweis: Neben Nutzdaten können auch Protokoll-/Transaktionsdaten zu löschen sein.

50  Hinweis: Ein Akzeptieren von Allgemeinen Geschäftsbedingungen (AGB) oder sonstigen Nutzungsbedingungen im Zuge einer Mitnutzung ist nicht als ein Vertragsverhältnis im Sinne dieses Mindeststandards anzusehen.

<!-- page: 15 -->

ii) Für diese Bewertung MUSS die Einrichtung insbesondere die Ergebnisse der Datenkategorisierung sowie, sofern gegeben, weitere Anforderungen (z. B. aus Gesetzen, Verordnungen, Beschlüssen oder anderen Quellen) heranziehen.

d) Die Einrichtung MUSS ermitteln, welche Rechte an den dienstlichen Daten dem Cloud-Diensteanbieter oder Dritten durch das Akzeptieren der vom Cloud-Diensteanbieter vorgegebenen Allgemeinen Geschäftsbedingungen (AGB), Datenschutzerklärung oder sonstigen Nutzungsbedingungen eingeräumt werden.

i) Die Einrichtung MUSS bewerten, ob diese Rechte mit den eigenen Sicherheitsanforderungen, die sie in der Sicherheitsrichtlinie und dem eigenen Sicherheitskonzept definiert hat, vereinbar sind.

ii) Die Einrichtung MUSS insbesondere die Nutzungsbedingungen und die Datenschutzerklärung des Cloud-Diensteanbieters auswerten.

e) Die Einrichtung MUSS bewerten, ob und wie die dienstlichen Daten im externen Cloud-Dienst verschlüsselt zu speichern sind. 51  Für die anschließende Bewertung SOLLTE die Einrichtung die identifizierten Risiken mit der eigenen Strategie für die Cloud-Nutzung (siehe NCD.2.1.01) abgleichen.

i) Die Einrichtung MUSS dann bewerten, ob die Verschlüsselung mit den Anforderungen aus den Ergebnissen der Datenkategorisierung vereinbar ist.

ii) Ist die vom Cloud-Diensteanbieter eingesetzte Verschlüsselung nicht geeignet, MUSS die Einrichtung prüfen, ob Anforderungen an die Vertraulichkeit der Daten über eine clientseitige Verschlüsselung erfüllt werden können.

f) Die Einrichtung MUSS erheben, wie und wann Daten durch den Cloud-Anbieter gelöscht werden (z.B. Löschfristen). Die Einrichtung MUSS dann bewerten, ob dies mit den Anforderungen aus den Ergebnissen der Datenkategorisierung vereinbar ist.

g) Die Einrichtung MUSS ermitteln, ob für die Mitnutzung auf den eigenen Arbeitsplatzcomputern oder mobilen Endgeräten zusätzliche Softwareinstallationen erforderlich sind.

i) Die Einrichtung MUSS bewerten, ob die hierfür einzuräumenden Zugriffs- und Ausführungsrechte mit der eigenen Sicherheitsrichtlinie vereinbar sind und inwiefern gesonderte Lizenzen für die Mitnutzung eingeholt werden müssen.

ii) Ist ein Zugriff über mobile Endgeräte geplant, MUSS die Einrichtung diese zentral verwalten. Die Vorgaben des Mindeststandards Mobile Device Management sind zu beachten. 52

51  Siehe OPS.2.2.A17 Einsatz von Verschlüsselung bei Cloud-Nutzung, (BSI 2022a)

52  Vgl. Mindeststandard des BSI für Mobile Device Management, (BSI 2022b)

<!-- page: 16 -->

## Literaturverzeichnis

| AKTM (2014)   | Arbeitskreise Technik und Medien der Konferenz der Datenschutzbeauftragten des Bundes und der Länder sowie der Arbeitsgruppe Internationaler Datenverkehr des Düsseldorfer Kreises, Orientierungshilfe - Cloud Computing, Version 2.0, Oktober 2014, https://www.bfdi.bund.de/DE/Infothek/Orientierungshilfen/Artikel/OHCloudComputi ng.html     |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BMI (2014)    | Bundesministerium des Innern, Erlass zur Verwendung einer Eigenerklärung und einer Vertragsklausel in Vergabeverfahren im Hinblick auf Risiken durch nicht offengelegte Informationsabflüsse an ausländische Sicherheitsbehörden, O4 - 11032/23#14, Berlin 2014, https://www.bmi.bund.de/SharedDocs/kurzmeldungen/DE/2014/08/no-spy- erlass.html |
| BMI (2017)    | Bundesministerium des Innern und für Heimat: Umsetzungsplan Bund 2017 - Leitlinie für die Informationssicherheit in der Bundesverwaltung, https://www.bmi.bund.de/SharedDocs/downloads/DE/publikationen/themen/it- digitalpolitik/up-bund-2017.html                                                                                              |
| BMI (2018)    | Bundesministerium des Innern und für Heimat: Allgemeine Verwaltungsvorschrift zum materiellen Geheimschutz (Verschlusssachenanweisung - VSA), 10. August 2018, https://www.verwaltungsvorschriften-im- internet.de/bsvwvbund_10082018_SII554001196.htm                                                                                           |
| BMI (2022)    | Bundesministerium des Innern und für Heimat: Ergänzende Vertragsbedingungen für Cloudleistungen; Verweis unter: Aktuelle EVB-IT - EVB-IT Cloud, https://www.cio.bund.de/Web/DE/IT- Beschaffung/EVB-IT-und-BVB/Aktuelle_EVB-IT/aktuelle_evb_it_node.html                                                                                          |
| BSI (2008)    | Bundesamt für Sicherheit in der Informationstechnik: BSI-Standard 100-4 - Notfallmanagement, Version 1.0, https://www.bsi.bund.de/dok/128600                                                                                                                                                                                                     |
| BSI (2017a)   | Bundesamt für Sicherheit in der Informationstechnik: BSI-Standard 200-2 - IT- Grundschutz-Methodik, Version 1.0, https://www.bsi.bund.de/dok/128640                                                                                                                                                                                              |
| BSI (2017b)   | Bundesamt für Sicherheit in der Informationstechnik: BSI-Standard 200-3 - Risikoanalyse auf der Basis von IT-Grundschutz, Version 1.0, https://www.bsi.bund.de/dok/407502                                                                                                                                                                        |
| BSI (2019)    | Bundesamt für Sicherheit in der Informationstechnik: Mindeststandards - Antworten auf häufig gestellte Fragen zu den Mindeststandards, https://www.bsi.bund.de/dok/11916758                                                                                                                                                                      |
| BSI (2020a)   | Bundesamt für Sicherheit in der Informationstechnik: Cloud Computing Compliance Criteria Catalogue - C5:2020 (Kriterienkatalog Cloud Computing) - Stand Februar 2020, https://www.bsi.bund.de/dok/452204                                                                                                                                         |
| BSI (2020b)   | Bundesamt für Sicherheit in der Informationstechnik: Leitfaden mit Checkliste zur Auswertung einer Berichterstattung nach BSI C5, https://www.bsi.bund.de/dok/14020574                                                                                                                                                                           |
| BSI (2022a)   | Bundesamt für Sicherheit in der Informationstechnik: IT-Grundschutz-Kompendium, Edition 2022, https://www.bsi.bund.de/dok/128568                                                                                                                                                                                                                 |
| BSI (2022b)   | Bundesamt für Sicherheit in der Informationstechnik: Mindeststandard des BSI für Mobile Device Management, Version 2.0, https://www.bsi.bund.de/dok/453264                                                                                                                                                                                       |
| DIN (2018)    | Deutsches Institut für Normung e.V.: Normungsarbeit - Teil 2: Gestaltung von Dokumenten, DIN 820-2:2018-09                                                                                                                                                                                                                                       |
| IETF (1997)   | Internet Engineering Task Force: Key words for use in RFCs to Indicate Requirement Levels, RFC 2119, https://tools.ietf.org/html/rfc2119                                                                                                                                                                                                         |

<!-- page: 17 -->

ISO/IEC 17788:2014 Information technology - Cloud computing - Overview and

ISO (2014) vocabulary

<!-- page: 18 -->

## Abkürzungsverzeichnis

AGB

BMI

BSI

C5

DIN

DSGVO

EVB-IT

FAQ

IETF

ISB

ISMS

ISO/IEC

IT-SiBe

StGB

RFC

VSA

Allgemeine Geschäftsbedingungen

Bundesministerium des Innern und für Heimat

Bundesamt für Sicherheit in der Informationstechnik

Cloud Computing Compliance Criteria Catalogue (Kriterienkatalog Cloud Computing)

Deutsches Institut für Normung e.V.

Datenschutz-Grundverordnung

Ergänzende Vertragsbedingungen für die Beschaffung von Informationstechnik

Frequently Asked Questions

Internet Engineering Task Force

Informationssicherheitsbeauftragte

Informationssicherheitsmanagementsystem

International Organisation for Standardization / International Electrotechnical Commission

IT-Sicherheitsbeauftragte

Strafgesetzbuch

Request for Comments

Allgemeine Verwaltungsvorschrift zum materiellen Geheimschutz

(Verschlusssachenanweisung - VSA)

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 2 -->

> Tel.: +49 22899 9582-6262
