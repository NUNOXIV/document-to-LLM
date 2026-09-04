---
source_file: "Mindeststandard_ISMS_ITKB_V1_0a.pdf"
source_sha256: c44597c9e031a598b69d518a14dcb03f48de4e97cb0f3e605c7aefc38174c6bc
source_bytes: 590469
pages: 33
tables: 13
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T20:33:15+00:00"
text_coverage_percent: 100.0
restored_hyphens: 3
extraction_status: warn
warnings:
  - "4 Tabellenzelle(n) beginnen mitten im Satz — moegliche Zellverschiebung, z. B. \"negative Innen- und Außenwirkung...\". Zeilen dieser Tabelle vor dem Zitat gegen die Quelle pruefen."
  - "3 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): ISKErgebnisse -> ISK-Ergebnisse, ITDienstekonsolidierung -> IT-Dienstekonsolidierung, ITKonsolidierung -> IT-Konsolidierung"
  - "Der Textlayer der Quelle enthaelt 13 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

## Mindeststandard

Regelungsdokument für das Informationssicherheitsmanagementsystem in der IT-Konsolidierung Bund

Vorgabe nach § 8 Absatz 1 Satz 1 BSIG - Version 1.0a vom 0 4.07.2025

<!-- image -->

<!-- image -->

<!-- page: 2 -->

## Änderungshistorie

| Version   | Datum       | Beschreibung                                |
|-----------|-------------|---------------------------------------------|
| 1.0       | 0 4.12.2024 | Erste Veröffentlichung des Mindeststandards |
| 1.0a      | 04.07.2025  | Anpassung der Titelseite                    |

Tabelle 1: Versionsgeschichte des Regelungsdokuments für das Informationssicherheitsmanagementsystem in der IT-Konsolidierung Bund

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn

Tel.: +49 22899 9582-6262

[E-Mail: mindeststandards@bsi.bund.de](mailto:mindeststandards@bsi.bund.de)

Internet: https://www.bsi.bund.de

© Bundesamt für Sicherheit in der Informationstechnik 2024

<!-- page: 3 -->

## Vorwort

Das vorliegende Dokument beschreibt übergreifende Regelungen zur Zusammenarbeit in der IT-Konsolidierung Bund (Informationssicherheitsmanagementsystem). Die Verbindlichkeit dieser Regelungen ist dadurch gegeben, dass dieses Dokument eine Vorgabe nach § 8 BSIG ist. Im weiteren Verlauf wird für dieses Dokument der Begriff "Mindeststandard" verwendet.

Risiken für die Cyber- und Informationssicherheit sind nicht zuletzt aufgrund der zunehmenden Komplexität und Vernetzung von IT-Systemen allgegenwärtig. Dadurch betreffen potenzielle Schwachstellen und Cyberangriffe in der Regel nicht nur einzelne Stellen.

Umso wichtiger ist die Vorgabe verbindlicher Sicherheitsanforderungen an die Informationstechnik des Bundes. So kann ein einheitliches Mindestsicherheitsniveau mit effektiven Maßnahmen zur Abwehr von Cyberangriffen innerhalb der heterogenen Behördenlandschaft etabliert werden.

Dazu legt das Bundesamt für Sicherheit in der Informationstechnik (BSI) Mindeststandards (MST) für die Sicherheit der Informationstechnik des Bundes 1  fest. Dies erfolgt auf der Grundlage des § 8 Absatz 1 BSIG im Benehmen mit den Ressorts. Als gesetzliche Vorgabe definieren Mindeststandards somit ein verbindliches Mindestniveau für die Informationssicherheit.

Bereits 2017 hat das Bundeskabinett mit dem Umsetzungsplan Bund 2017 (UP Bund 2017) 2  eine Leitlinie für Informationssicherheit in der Bundesverwaltung in Kraft gesetzt. Damit wurde die Beachtung der Mindeststandards für den Bereich der Stellen des Bundes verbindlich. Durch das IT-Sicherheitsgesetz 2.0 wurde die Einhaltung der Mindeststandards des BSI auch gesetzlich geregelt. Die Umsetzungspflicht der Mindeststandards ergibt sich aus dem dadurch neu gefassten § 8 BSIG.

Die Mindeststandards richten sich primär an IT-Verantwortliche, IT-Sicherheitsbeauftragte (IT-SiBe), Informationssicherheitsbeauftragte (ISB), IT-Betriebspersonal und Beschaffungsstellen. Die Gesamtverantwortung für die Informationssicherheit und damit auch für die Einhaltung der Mindeststandards trägt gemäß UP Bund 2017 die Leitung der jeweiligen Einrichtung 1 .

IT-Systeme sind in der Regel komplex und in ihren individuellen Anwendungsbereichen durch die unterschiedlichsten (zusätzlichen) Rahmenbedingungen und Anforderungen gekennzeichnet. Daher können sich in der Praxis regelmäßig höhere Anforderungen an die Informationssicherheit ergeben, als sie in den Mindeststandards beschrieben werden. Aufbauend auf dem Mindestsicherheitsniveau sind diese individuellen Anforderungen in der Planung, der Etablierung und im Betrieb der IT-Systeme zusätzlich zu berücksichtigen, um dem jeweiligen Bedarf an Informationssicherheit zu genügen. Die Vorgehensweise dazu beschreiben die IT-Grundschutz-Standards des BSI.

Zur Sicherstellung der Effektivität und Effizienz in der Erstellung und Betreuung von Mindeststandards arbeitet das BSI nach einer standardisierten Vorgehensweise. Zur Qualitätssicherung durchläuft jeder Mindeststandard mehrere Prüfzyklen einschließlich des Konsultationsverfahrens mit der Bundesverwaltung. 3  Über die Beteiligung bei der Erarbeitung von Mindeststandards hinaus kann sich jede Einrichtung auch bei der Erschließung fachlicher Themenfelder für neue Mindeststandards einbringen oder im Hinblick auf Änderungsbedarf für bestehende Mindeststandards Kontakt mit dem BSI aufnehmen. Einhergehend mit der Erarbeitung von Mindeststandards berät das BSI die Einrichtungen auf Ersuchen bei der Umsetzung und Einhaltung der Mindeststandards.

1  Die von den Mindeststandards adressierten Stellen werden in § 8 Absatz 1 BSI-Gesetz (BSIG) definiert (siehe https://www.gesetze-im-internet.de/bsig\_2009/\_\_8.html). Zur besseren Lesbarkeit wird im weiteren Verlauf für alle dort genannten Stellen der Begriff 'Einrichtung' verwendet.

2  Vgl. UP Bund (BMI 2017)

[3  Siehe FAQ zu den MST: https://www.bsi.bund.de/dok/MST-FAQ (BSI 2024a)](https://www.bsi.bund.de/dok/MST-FAQ)

<!-- page: 4 -->

## Inhalt

| 1 Beschreibung .....................................................................................................................................................................................               | 1 Beschreibung .....................................................................................................................................................................................               | 1 Beschreibung .....................................................................................................................................................................................   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1                                                                                                                                                                                                                | Einleitung und Abgrenzung..............................................................................................................................................                                            | 5                                                                                                                                                                                                      |
| 1.1.1                                                                                                                                                                                                              | Geltungsbereich ................................................................................................................................................................                                   | 6                                                                                                                                                                                                      |
| 1.1.2                                                                                                                                                                                                              | Entscheidungs- und Durchführungsverantwortung ........................................................................................                                                                             | 6                                                                                                                                                                                                      |
| 1.1.3                                                                                                                                                                                                              | Zu konkretisierende Regelungsbereiche der Informationssicherheitsrichtlinie (Version 2.0)                                                                                                                          | ........ 7                                                                                                                                                                                             |
| 1.2                                                                                                                                                                                                                | Modalverben ...........................................................................................................................................................................                            | 8                                                                                                                                                                                                      |
| 2                                                                                                                                                                                                                  | Sicherheitsanforderungen ...........................................................................................................................................................                               | 9                                                                                                                                                                                                      |
| 2.1                                                                                                                                                                                                                | Einheitliche Schutzbedarfskategorien .........................................................................................................................                                                     | 9                                                                                                                                                                                                      |
| 2.2                                                                                                                                                                                                                | Kommunikation der Ergebnisse von Sicherheitskonzepten ............................................................................                                                                                 | 10                                                                                                                                                                                                     |
| 2.3                                                                                                                                                                                                                | Befugnisse der Dienstleister............................................................................................................................................                                           | 11                                                                                                                                                                                                     |
| 2.4                                                                                                                                                                                                                | Risikomanagement und Risikotransparenz .............................................................................................................                                                               | 12                                                                                                                                                                                                     |
| 2.5                                                                                                                                                                                                                | Prüfungen/Nachweispflichten ......................................................................................................................................                                                 | 15                                                                                                                                                                                                     |
| 2.6                                                                                                                                                                                                                | Vorfallmanagement ...........................................................................................................................................................                                      | 15                                                                                                                                                                                                     |
| 2.7                                                                                                                                                                                                                | Schwachstellenmanagement .........................................................................................................................................                                                 | 17                                                                                                                                                                                                     |
| 2.8                                                                                                                                                                                                                | Schnittstellen im ISMS ITKB ..........................................................................................................................................                                             | 17                                                                                                                                                                                                     |
| 2.9                                                                                                                                                                                                                | Leistungsbeziehung in der ITKB ...................................................................................................................................                                                 | 19                                                                                                                                                                                                     |
| Literaturverzeichnis ...............................................................................................................................................................................               | Literaturverzeichnis ...............................................................................................................................................................................               | 21                                                                                                                                                                                                     |
| Abkürzungsverzeichnis .........................................................................................................................................................................                    | Abkürzungsverzeichnis .........................................................................................................................................................................                    | 22                                                                                                                                                                                                     |
| Glossar .......................................................................................................................................................................................................... | Glossar .......................................................................................................................................................................................................... | 23                                                                                                                                                                                                     |
| Anhang 1: Einheitliche Schutzbedarfskategorien ITKB ..........................................................................................................                                                     | Anhang 1: Einheitliche Schutzbedarfskategorien ITKB ..........................................................................................................                                                     | 25                                                                                                                                                                                                     |
| Anhang 2: Adressaten der MST-Anforderungen ........................................................................................................................                                                | Anhang 2: Adressaten der MST-Anforderungen ........................................................................................................................                                                | 33                                                                                                                                                                                                     |

<!-- page: 5 -->

## 1 Beschreibung

Die Bundesregierung hat am 20. Mai 2015 mit Kabinettsbeschluss zum Grobkonzept zur IT-Konsolidierung Bund 4  beschlossen, ihre IT im ressortübergreifenden Großprojekt 'IT-Konsolidierung Bund (ITKB)' zu bündeln und zu standardisieren. Durch die Projekte der ITKB, die IT-Dienstekonsolidierung (DK) und die IT-Betriebskonsolidierung Bund (BKB), werden IT-Lösungen standardisiert und durch Dienstleister für Kundeneinrichtungen zentral erbracht. Dabei werden wesentliche Aufgaben und damit verbunden Teile der Verantwortung an die Dienstleister übertragen. Es ergeben sich dadurch neue Rahmenbedingungen zur Gewährleistung eines angemessenen Informationssicherheitsniveaus für die IT der Bundesverwaltung.

Der Umsetzungsplan Bund 2017 (UP Bund) 5  fordert als Informationssicherheitsleitlinie des Bundes die Verzahnung der Informationssicherheitsmanagementsysteme (ISMS) der Institutionen der ITKB, indem die grundsätzlichen Rahmenbedingungen an die Informationssicherheit hinsichtlich der IT-Konsolidierung des Bundes in einer entsprechenden 'Richtlinie zur Informationssicherheit der IT-Konsolidierung des Bundes' weiter konkretisiert werden.

Mit Beschluss Nr. 2023/09 vom 27.02.2023 verabschiedete das CIO Board die Informationssicherheitsrichtlinie IT-Konsolidierung Bund (ISR ITKB) in der Version 2.0 6 . Die darin definierten zusätzlich notwendigen Rechte und Pflichten der Institutionen der ITKB 7  werden in diesem Mindeststandard nach § 8 BSIG für das ISMS ITKB detailliert.

## 1.1 Einleitung und Abgrenzung

Der Mindeststandard für das Informationssicherheitsmanagementsystem in der IT-Konsolidierung Bund (MST ISMS ITKB) ist eine an der Praxis orientierte Hilfestellung zur Umsetzung der in der ISR ITKB festgelegten Anforderungen und macht diese Anforderungen für die Bundesverwaltung verbindlich.

Um die Praxistauglichkeit dieses Mindeststandards im Vorfeld zu untersuchen, wurde zunächst durch die AG Informationssicherheit (AG ISI) 8  ein sogenanntes 'vorläufiges Regelungsdokument' erstellt. Dieses vorläufige Regelungsdokument wurde mit der Arbeitsgruppe Informationssicherheitsmanagement (AG ISM) 9   abgestimmt. Die erarbeiteten Regelungen wurden dann im Rahmen von Pilotierungen mit Stellen des Bundes auf ihre Umsetzbarkeit in der Praxis geprüft.

Der MST ISMS ITKB trifft ausschließlich Regelungen für den Bereich Informationssicherheitsmanagement in der ITKB, etwaige andere bestehende Rechte und Pflichten (bspw. jene des Datenschutzes oder des Geheimschutzes) bleiben unberührt. Insbesondere bestehende Vereinbarungen zwischen Kundeneinrichtungen und Dienstleistern, die nicht den Geltungsbereich der ISR ITKB betreffen, bleiben von den Vorgaben dieser Richtlinie unberührt.

[4  Vgl. Grobkonzept zur IT-Konsolidierung Bund (BMI 2015)](https://www.cio.bund.de/SharedDocs/downloads/Webs/CIO/DE/cio-bund/steuerung-it-bund/grobkonzept-it-konsolidierung.html)

5  Vgl. UP Bund (BMI 2017)

[6  Vgl. Informationssicherheitsrichtlinie IT-Konsolidierung Bund, Version 2.0 (BSI 2023a)](https://www.bsi.bund.de/DE/Intern/Sicherheitsberatung/Bund/Dokumente/Publikationen/IT-Konsolidierung/Richtlinie_IT-Konsolidierung_Bund_V200.html)

7  Institutionen der ITKB sind die Projektleitungen der IT-Betriebskonsolidierung Bund und der IT-Dienstekonsolidierung, die Dienstleister und die Kundeneinrichtungen.

8  Mitglieder der AG ISI sind: BMI, BMF, ITZBund, BDBOS, BSI und ISB ITKB.

9  Mitglieder der AG ISM bestehen unter dem Vorsitz von BMI aus: Ressort-IT-Sicherheitsbeauftragten, BSI, ISB ITKB, BAköV, anlassbezogen CERT-Bund, dem Nationalem IT Lagezentrum und dem Nationalen Cyber-Abwehrzentrum.

<!-- page: 6 -->

## 1.1.1 Geltungsbereich

Der Geltungsbereich des vorliegenden MST ISMS ITKB entspricht dem Geltungsbereich der ISR ITKB 2.0 vom 27.02.2023 und umfasst, auch während Planung, Konzeption, Beschaffung, Umsetzung, Betrieb und Aussonderung:

- IT-Lösungen für die Bundesverwaltung, die im Rahmen der IT-Dienstekonsolidierung (DK) als Basis-, Querschnitts- oder Infrastruktur-Dienste (insbesondere in den Servicemodellen Platform as a Service (PaaS) oder Software as a Service (SaaS)) zentral bereitgestellt werden,
- IT-Lösungen für die Bundesverwaltung, die im Rahmen der IT-Betriebskonsolidierung Bund (BKB) auf den Betriebsplattformen des ITZBund (im Servicemodell Infrastructure as a Service(IaaS)) betrieben werden,
- Betriebsplattformen, auf denen die oben genannten IT-Lösungen betrieben werden, sowie
- zentrale Netze, die der Kommunikation zwischen den genannten Bestandteilen dienen.

Nicht Teil des Geltungsbereichs sind IT-Lösungen, die im bilateralen Verhältnis zwischen Kundeneinrichtungen und Dienstleistern betrieben werden (z. B. sogenannte 'vollkonsolidierte Behörden' 10 ), sowie nicht-konsolidierungsfähige IT-Lösungen, die Kundeneinrichtungen selbst außerhalb der Betriebsplattformen der ITKB betreiben.

Abbildung 1: Geltungsbereich der ISR ITKB (Quelle: BSI, 2023, Informationssicherheitsrichtlinie IT-Konsolidierung Bund v2.0)

<!-- image -->

## 1.1.2 Entscheidungs- und Durchführungsverantwortung

Die Entscheidungs- und Durchführungsverantwortung für die Umsetzung von Sicherheitsmaßnahmen zum Schutz der eigenen Geschäftsprozesse liegt bei der jeweiligen für den Geschäftsprozess zuständigen Institution der ITKB (Prozessverantwortlicher).

Die Entscheidungs- und Durchführungsverantwortung umfasst auch die Verantwortung für Risiken. Risiken aus dem Betrieb der IT muss der jeweilige Betreiber der betroffenen IT- Komponente verantworten;

10  Der Begriff "vollkonsolidierte Behörden" stammt aus dem Geschäftsbereich des BMF und bezeichnet Behörden, die bereits vollständig ihre IT vom ITZBund beziehen. Diese IT ist jedoch nicht Teil der ITKB, sondern ist individuell für die jeweilige Institution konzeptioniert.

<!-- page: 7 -->

andere Risiken muss der jeweilige Prozessverantwortliche verantworten. Dies bedeutet, der Betreiber bzw. Prozessverantwortliche muss über den Risikobehandlungsplan entscheiden und Restrisiken akzeptieren.

Hat eine Kundeneinrichtung den Betrieb einer IT-Komponente an einen Dienstleister ausgelagert, ist der Dienstleister der Betreiber dieser IT-Komponente und verantwortet die damit verbundenen Risiken. Betreibt eine Kundeneinrichtung eine IT-Komponente weiterhin selbst, ist sie selbst Betreiber und verantwortet die damit verbundenen Risiken. Im Kontext der ITKB wird der IT-Betrieb in Schichten aufgeteilt, um die Verantwortung eindeutig zuordnen zu können.

Die Kundeneinrichtungen tragen weiter die Entscheidungs- und Durchführungsverantwortung für die Umsetzung von Sicherheitsmaßnahmen für IT- Schichten, die sie selbst betreiben 11 . Um diese Sicherheitsmaßnahmen mit denen der Dienstleister in Einklang zu bringen bzw. Interdependenzen zu berücksichtigen, müssen die Kundeneinrichtungen die in diesem Mindeststandard festgelegten Pflichten sowie die jeweiligen Nutzungsbedingungen der Leistungen der ITKB einhalten.

Die Dienstleister tragen die Entscheidungs- und Durchführungsverantwortung für die Umsetzung von Sicherheitsmaßnahmen für IT-Schichten, die sie betreiben. 12  Hierfür müssen ihnen angemessene Befugnisse gegenüber den Kundeneinrichtungen eingeräumt werden, bspw. das Recht zur Erstellung von Nutzungsbedingungen für die Leistungen der ITKB, die Nachhaltung der Einhaltung dieser Nutzungsbedingungen sowie Möglichkeit auf Nicht-Einhaltung entsprechend reagieren zu können. Diese werden in diesem Mindeststandard festgelegt. 13  Die Dienstleister müssen die in diesem Mindeststandard festgelegten Pflichten einhalten.

Abbildung 2: Entscheidungs- und Durchführungsverantwortlichkeiten im Schichtenmodell des IT-Betriebs (Quelle: BSI, 2023, Informationssicherheitsrichtlinie IT-Konsolidierung Bund v2.0)

| Schichten / Servicemodell   | Infrastructure as a Service (IaaS)   | Platform as a Service (PaaS)   | Software as a Service (SaaS)   |
|-----------------------------|--------------------------------------|--------------------------------|--------------------------------|
| Anwendungen                 | Kundeneinrichtung                    | Kundeneinrichtung              | Dienstleister                  |
| Data                        | Kundeneinrichtung                    | Kundeneinrichtung              | Dienstleister                  |
| Runtime                     | Kundeneinrichtung                    | Dienstleister                  | Dienstleister                  |
| Middleware                  | Kundeneinrichtung                    | Dienstleister                  | Dienstleister                  |
| Betriebssystem              | Kundeneinrichtung                    | Dienstleister                  | Dienstleister                  |
| Virtualisierung             | Dienstleister                        | Dienstleister                  | Dienstleister                  |
| Server                      | Dienstleister                        | Dienstleister                  | Dienstleister                  |
| Speicher                    | Dienstleister                        | Dienstleister                  | Dienstleister                  |
| RZ-Netzwerk                 | Dienstleister                        | Dienstleister                  | Dienstleister                  |

## 1.1.3 Zu konkretisierende Regelungsbereiche der Informationssicherheitsrichtlinie (Version 2.0)

Mit dem Beschluss des CIO Boards (Beschluss Nr. 2023/09) wurde auch die Erstellung eines Mindeststandards nach § 8 BSIG, basierend auf der ISR ITKB 14 , vorgegeben. Dieser Mindeststandard konkretisiert die folgenden in der ISR ITKB vorgegebenen Regelungsbereiche:

- Einheitliche Schutzbedarfskategorien in der ITKB
- Kommunikation der Ergebnisse von Sicherheitskonzepten in der ITKB

11  Vgl. blau markierte Felder in Abbildung 2

12  Vgl. grün markierte Felder in Abbildung 2

13  Vgl. Kapitel 2, Sicherheitsanforderungen

[14  Vgl. Informationssicherheitsrichtlinie IT-Konsolidierung Bund, Version 2.0 (BSI 2023a)](https://www.bsi.bund.de/DE/Intern/Sicherheitsberatung/Bund/Dokumente/Publikationen/IT-Konsolidierung/Richtlinie_IT-Konsolidierung_Bund_V200.html)

<!-- page: 8 -->

- Risikomanagement und Risikotransparenz in der ITKB
- Prüfungen/Nachweispflichten in der ITKB
- Vorfallmanagement in der ITKB
- Schwachstellenmanagement in der ITKB
- Schnittstellen im Outsourcing-Kontext in der ITKB
- Befugnisse der Dienstleister

Detaillierte Angaben, welche Regelungen der ISR ITKB in den einzelnen Regelungsbereichen durch den Mindeststandard konkretisiert werden, werden den entsprechenden Sicherheitsanforderungen des Mindeststandards jeweils als einleitender Text vorangestellt.

## 1.2 Modalverben

In Anlehnung an den IT-Grundschutz 15  werden die Sicherheitsanforderungen mit den Modalverben MUSS und SOLLTE sowie den zugehörigen Verneinungen formuliert.. Die hier genutzte Definition basiert auf RFC 2119 16  und DIN 820-2: 2022 17 .

## MUSS / DARF NUR

bedeutet, dass diese Anforderung zwingend zu erfüllen ist. Das von der Nichtumsetzung ausgehende Risiko kann im Rahmen einer Risikoanalyse nicht akzeptiert werden.

## DARF NICHT / DARF KEIN

bedeutet, dass etwas zwingend zu unterlassen ist. Das durch die Umsetzung entstehende Risiko kann im Rahmen einer Risikoanalyse nicht akzeptiert werden.

## SOLLTE

bedeutet, dass etwas umzusetzen ist, es sei denn, im Einzelfall sprechen gute Gründe gegen eine Umsetzung. Die Begründung muss dokumentiert und bei einem Audit auf ihre Stichhaltigkeit geprüft werden können.

## SOLLTE NICHT / SOLLTE KEIN

bedeutet, dass etwas zu unterlassen ist, es sei denn, es sprechen gute Gründe für eine Umsetzung. Die Begründung muss dokumentiert und bei einem Audit auf ihre Stichhaltigkeit geprüft werden können.

[15  Vgl. BSI-Standard 200-2 (BSI 2017a, S. 18)](https://www.bsi.bund.de/dok/10027846)

[16  Vgl. Key words for use in RFCs (IETF 1997)](https://tools.ietf.org/html/rfc2119)

17  Vgl. DIN-820-2: Gestaltung von Dokumenten (DIN 2022)

<!-- page: 9 -->

## 2 Sicherheitsanforderungen

Der Mindeststandard für das Informationssicherheitsmanagementsystem in der IT-Konsolidierung Bund konkretisiert im Folgenden die in der ISR ITKB (Version 2.0) aufgeführten Regelungsbereiche.

## 2.1 Einheitliche Schutzbedarfskategorien

Zu einheitlichen Schutzbedarfskategorien in der ITKB wurden in der ISR ITKB 2.0 insbesondere die folgenden Regelungen getroffen:

'3. Die Dienstleister MÜSSEN für die Bereitstellung von Leistungen der ITKB die einheitlichen Schutzbedarfskategorien für die ITKB anwenden.

4. Institutionen der ITKB MÜSSEN für die Nutzung von Leistungen der ITKB die einheitlichen Schutzbedarfskategorien der ITKB in ihre eigenen Schutzbedarfskategorien übersetzen.'

Diese Regelungen werden wie folgt konkretisiert:

## ISMS-ITKB.2.1.01 - Festlegung des Schutzbedarfs einer Leistung der ITKB

a) Die Projektleitungen BKB/DK 18  MÜSSEN bei der Beauftragung oder Weiterentwicklung einer Leistung der ITKB angeben, für welchen Schutzbedarf diese bereitgestellt werden soll.

b) Die Projektleitungen BKB/DK MÜSSEN bei Beauftragung der Leistung der ITKB die einheitlichen Schutzbedarfskategorien verwenden, die im Rahmen der ITKB angewendet werden. 19

## ISMS-ITKB.2.1.02 - Umsetzung des beauftragten Schutzbedarfs

a) Der Dienstleister MUSS die Absicherung seiner Leistungen der ITKB entsprechend des beauftragten Schutzbedarfes sicherstellen.

b) Der Dienstleister MUSS bei Angaben, für welchen Schutzbedarf die jeweilige Leistung der ITKB angeboten wird, den Schutzbedarf auf Grundlage der einheitlichen Schutzbedarfskategorien feststellen.

## ISMS-ITKB.2.1.03 - Schutzbedarfsfeststellung vor Inanspruchnahme einer Leistung der ITKB

a) Die Kundeneinrichtungen MÜSSEN vor der Inanspruchnahme einer Leistung der ITKB für die eigenen Informationen, die im Rahmen der Inanspruchnahme der Leistung der ITKB verarbeitet werden sollen, unter Verwendung der einheitlichen Schutzbedarfskategorien eine Schutzbedarfsfeststellung durchführen.

b) Die Institutionen der ITKB SOLLTEN die durch die Dienstleister zur Schutzbedarfsfeststellung herausgegebenen Verfahrenshinweise berücksichtigen.

c) Die Institutionen der ITKB SOLLTEN die Korrektheit und Angemessenheit ihrer Schutzbedarfsfeststellungen in regelmäßigen Abständen überprüfen.

d) Die Kundeneinrichtungen MÜSSEN auf der Grundlage der Schutzbedarfsfeststellung entscheiden, ob sie eine vom Dienstleister bereitgestellte Leistung der ITKB in Anspruch nehmen können.

## ISMS-ITKB.2.1.04 - Umgang mit Abweichungen

a) Die Kundeneinrichtung DARF NUR auf Grundlage einer Risikoanalyse entscheiden, die Leistung der ITKB in Anspruch zu nehmen, wenn der durch die Kundeneinrichtung individuell festgestellte Schutzbedarf den von dem Dienstleister bereitgestellten Schutzbedarf überschreitet.

b) Die Institutionen der ITKB SOLLTEN bei einer Risikoanalyse die vom Dienstleister bereitgestellten Informationen zu den Risiken der jeweiligen Leistung der ITKB berücksichtigen.

18  Vgl. Glossar

19  Vgl. Anhang 1: Einheitliche Schutzbedarfskategorien ITKB

<!-- page: 10 -->

## 2.2 Kommunikation der Ergebnisse von Sicherheitskonzepten

Zur Kommunikation der Ergebnisse von Sicherheitskonzepten wurden in der ISR ITKB 2.0 insbesondere die folgenden Regelungen getroffen:

'1. Die Dienstleister MÜSSEN die Kundeneinrichtungen zentral über relevante Ergebnisse von Informationssicherheitskonzepten informieren. Dies sind bspw. Sicherheitsmaßnahmen für Leistungen der ITKB, falls diese Auswirkungen auf die Sicherheitsmaßnahmen der Kundeneinrichtungen selbst haben könnten. Ist die Umsetzung zusätzlicher Sicherheitsanforderungen durch die Kundeneinrichtungen erforderlich, MÜSSEN die Dienstleister diese in den jeweiligen Nutzungsbedingungen je Leistung festlegen.

2. Aufgrund der Verantwortungsübernahme durch den Dienstleister entfällt im Rahmen der Leistungen der ITKB das Recht der Kundeneinrichtungen zur Einsicht in Ergebnisse der Sicherheitskonzepte der Dienstleister. Dies ist der Fall, da die Kundeneinrichtungen keine Risiken übernehmen und keine individuellen Sicherheitsmaßnahmen beauftragen können.'

Diese Regelungen werden wie folgt konkretisiert:

## ISMS-ITKB.2.2.01 - Erstellung einer Leistungsbeschreibung

a) Der Dienstleister MUSS den Kundeneinrichtungen für jede Leistung der ITKB im Rahmen einer Leistungsbeschreibung kontinuierlich leistungsbezogene Informationen zur Verfügung stellen, die diese zu deren Inanspruchnahme und/ oder der damit verbundenen Erstellung von Informationssicherheitskonzepten (ISK) benötigen.

b) Der Dienstleister MUSS in der Leistungsbeschreibung mindestens Angaben zum Schutzbedarf, zum Servicemodell wie auch zu den Service Level Agreements (SLA) und der (Geo-)Redundanz einer Leistung der ITKB machen.

c) Der Dienstleister MUSS in der Leistungsbeschreibung angeben, wenn bestimmte Anwendungen auf den Endgeräten oder die Anbindung an ein Weitverkehrsnetz der Bundesverwaltung für die Inanspruchnahme einer Leistung der ITKB erforderlich sind.

d) Der Dienstleister MUSS den Kundeneinrichtungen innerhalb der Leistungsbeschreibung offenlegen, welche wesentlichen Schutzmechanismen zur Absicherung einer Leistung der ITKB umgesetzt sind, sodass Kundeneinrichtungen angemessen für eine Bewertung im eigenen Risikomanagement informiert sind.

e) Der Dienstleister MUSS den Kundeneinrichtungen auch Informationen über solche sicherheitsrelevanten Leistungsbestandteile (sog. Services) bereitstellen, die in Verantwortung des Dienstleisters für die Kundeneinrichtungen erbracht werden (kundengerichtete Sicherheitsleistungen).

f) Der Dienstleister MUSS die Kundeneinrichtungen in den Leistungsbeschreibungen über kundenseitig durchzuführende Konfigurationseinstellungen informieren, sofern dies für die Wirksamkeit von Schutzmechanismen oder kundengerichteten Sicherheitsleistungen erforderlich ist.

g) Der Dienstleister MUSS den Kundeneinrichtungen kontinuierlich in Form von Modellierungshinweisen mitteilen, welche Bausteine aus dem IT-Grundschutz-Kompendium bzw. Anforderungen im ISK des Dienstleisters abgedeckt sind und welche Bausteine bzw. Anforderungen im ISK der Kundeneinrichtungen zu betrachten sind.

## ISMS-ITKB.2.2.02 - Berichtswesen

a) Der Dienstleister MUSS die Kundeneinrichtungen im Rahmen eines regelmäßigen Berichtswesens jährlich über alle Risiken mit Bezug zu einer Leistung der ITKB informieren, die Auswirkungen auf andere Institutionen der ITKB haben können (sog. Verbundrisiken) und in einer Risikoanalyse als hohes/ sehr hohes Risiko bewertet wurden.

b) Der Dienstleister MUSS innerhalb des Berichtswesens die Kundeneinrichtungen auch über alle Verbundrisiken informieren, die sich mit Bezug zur Leistung der ITKB aus fehlenden oder unfertigen

<!-- page: 11 -->

- sicherheitsrelevanten Leistungsbestandteilen (Services),
- Schutzmechanismen wie auch
- Maßnahmen zur Notfallvorsorge bzw. Notfallbehandlung

ergeben.

c) Der Dienstleister MUSS die Kundeneinrichtungen innerhalb des Berichtswesens jährlich über die relevanten Ergebnisse aus

- Zertifizierungen, externen oder internen Audits,
- Überprüfungen nach § 4a BSIG,
- technischen Überprüfungen (insbesondere Penetrationstests) wie auch
- gemeinsam mit anderen Institutionen der ITKB durchgeführten (Notfall-) Übungen

mit Bezug zur Leistung der ITKB informieren.

## ISMS-ITKB.2.2.03 - Grundsätze bei der Kommunikation relevanter ISK-Ergebnisse

a) Der Dienstleister MUSS die bereitgestellten Informationen bezüglich relevanter ISK-Ergebnisse auf die notwendigen Inhalte reduzieren.

b) Der Dienstleister MUSS sicherstellen, dass die Weitergabe der Informationen bezüglich relevanter ISK-Ergebnisse keine Gefährdung für Institutionen der ITKB darstellt.

c) Der Dienstleister MUSS die bereitgestellten Informationen bezüglich relevanter ISK-Ergebnisse mindestens jährlich fortschreiben.

- d) Der Dienstleister MUSS die Kundeneinrichtungen über Änderungen an den Leistungsbeschreibungen informieren.

e) Der Dienstleister MUSS die Leistungsbeschreibung und das Berichtswesen an einem Ablageort veröffentlichen, der für alle Institutionen der ITKB erreichbar ist.

f) Der Dienstleister MUSS einen Auskunftsprozess für Anfragen von Kundeneinrichtungen einrichten, wenn Kundeneinrichtungen über die Leistungsbeschreibung nach ISMS-ITKB.2.2.01 und Berichtswesen nach ISMS-ITKB.2.2.02 hinaus weitere Informationen über die Leistung der ITKB benötigen.

## 2.3 Befugnisse der Dienstleister

Zu den Befugnissen der Dienstleister wurde in Kapitel 1.1 der ISR ITKB 2.0 insbesondere die folgende Regelung getroffen:

'Die Dienstleister tragen die Entscheidungs- und Durchführungsverantwortung für die Umsetzung von Sicherheitsmaßnahmen für IT-Schichten, die sie betreiben. Hierfür MÜSSEN ihnen angemessene Befugnisse gegenüber den Kundeneinrichtungen eingeräumt werden, bspw. das Recht zur Erstellung von Nutzungsbedingungen für die Leistungen der ITKB, die Nachhaltung der Einhaltung dieser Nutzungsbedingungen sowie die Möglichkeit auf Nicht-Einhaltung entsprechend reagieren zu können.'

Losgelöst vom jeweiligen Servicemodell muss der Dienstleister somit mit den Befugnissen ausgestattet werden, die es ihm ermöglichen, über alle Institutionen der ITKB hinweg ein einheitliches Sicherheitsniveau bereitstellen und aufrechterhalten zu können. Die Regelungen zu den Befugnissen der Dienstleister sind zum besseren Verständnis den einzelnen Themenbereichen zugeordnet und dort konkretisiert worden. Dies betrifft die Themenbereiche:

- Risikomanagement und Risikotransparenz
- Vorfallmanagement

<!-- page: 12 -->

- Leistungsbeziehung in der ITKB

Um der Wahrnehmung der Dienstleister-Befugnisse einen Handlungsrahmen im Hinblick auf die Dauer und den Kontext zu setzen, ergeben sich folgende Regelungen:

## ISMS-ITKB.2.3.01 - Grundsätze bei der Wahrnehmung der Befugnisse durch Dienstleister

a) Der Dienstleister DARF die in diesem Mindeststandard eingeräumten Befugnisse 20  NUR im Rahmen der Aufgaben wahrnehmen, die für die Bereitstellung oder den störungsfreien und sicheren Betrieb einer Leistung der ITKB erforderlich sind.

b) Der Dienstleister DARF die in diesem Mindeststandard eingeräumten Befugnisse 21  NUR in dem Zeitraum ausüben, der für die Erfüllung der vorgesehenen Aufgaben im Rahmen der ITKB erforderlich ist.

c) Die Kundeneinrichtung MUSS, wenn sie Bedenken hat, ob der Dienstleister seine Befugnisse im angemessenen Umfang wahrgenommen hat, dies dem Dienstleister über die bereits etablierten Kommunikationswege mitteilen.

d) Der Dienstleister MUSS gemeinsam mit der Kundeneinrichtung eine Abstimmung zur Angemessenheit der wahrgenommenen Befugnisse durchführen.

e) Die Kundeneinrichtung MUSS den Sachverhalt an die bestehenden Eskalationsstrukturen zur Klärung weiterleiten, wenn zwischen dem Dienstleister und der Kundeneinrichtung keine Einigung über die Angemessenheit der wahrgenommenen Befugnisse erzielt werden kann.

f) Die Kundeneinrichtung SOLLTE den Sachverhalt nur dann beilegen, sofern durch die zutreffenden Eskalationsmechanismen eine Einigung erzielt wurde.

## 2.4 Risikomanagement und Risikotransparenz

Zum Risikomanagement/-transparenz wurde in der ISR ITKB 2.0 insbesondere die folgende Regelung getroffen:

'Im Rahmen der ITKB können sich Informationssicherheitsrisiken von einzelnen Institutionen der ITKB auf andere Institutionen der ITKB auswirken. Auch können Kumulationseffekte zu Risiken führen, die für einzelne Institutionen der ITKB tragbar sind, in Summe jedoch die gesamte Informationssicherheit in der ITKB erheblich gefährden.'

Diese Regelungen werden wie folgt konkretisiert:

## ISMS-ITKB.2.4.01 - Identifikation potentieller Verbundrisiken

a) Die Institutionen der ITKB MÜSSEN im Rahmen ihrer Risikoanalysen identifizieren, welche Zielobjekte 22 einen Bezug zur ITKB haben. Für diese Zielobjekte MÜSSEN sie Gefährdungen (insbesondere die elementaren Gefährdungen gemäß IT-Grundschutz-Kompendium) 23  analysieren und Risiken ermitteln, die sich auf andere Institutionen der ITKB auswirken können (Verbundrisiken ITKB).

20  Vgl. Kapitel 2.4, 2.6, 2.9

21  Vgl. Kapitel 2.4, 2.6, 2.9

22  Basis für eine Risikoanalyse gemäß BSI-Standard 200-3 ist ein aus Zielobjekten bestehender Informationsverbund. Die Definition des Informationsverbunds als auch die Definition der Zielobjekte obliegt der jeweiligen Institution der ITKB, die die Risikoanalyse durchführt.

[23  Vgl. IT-Grundschutz-Kompendium (BSI 2023b)](https://www.bsi.bund.de/dok/1073656)

<!-- page: 13 -->

## ISMS-ITKB.2.4.02 - Meldung potentieller Verbundrisiken

a) Die Kundeneinrichtungen und Projektleitungen DK MÜSSEN alle identifizierten Risiken, die sich potentiell auf die ITKB auswirken können (Verbundrisiken ITKB), einmal jährlich zum Stichtag 24  1. April, dem jeweils verantwortlichen zentralen Dienstleister (ITZBund oder BDBOS) melden. Ist eine Leistung der ITKB betroffen, die nicht durch einen zentralen Dienstleister bereitgestellt wird, MUSS die Meldung an den ISB ITKB 25  erfolgen.

b) Die Kundeneinrichtungen und Projektleitungen DK SOLLTEN dem Dienstleister potentielle Verbundrisiken über das zentral im Rahmen der ITKB bereitgestellte IT-Grundschutz-Werkzeug übermitteln, wenn dieses durch die betreffende Institution der ITKB eingesetzt wird. Sofern dies nicht der Fall ist, MUSS die Übermittlung von potentiellen Verbundrisiken über die vom Dienstleister bereitgestellten Vorlagen erfolgen.

c) Die Institutionen der ITKB MÜSSEN dem Dienstleister folgende Informationen zu potentiellen Verbundrisiken übermitteln:

- Name des Ressorts der meldenden Kundeneinrichtung der ITKB
- Name der Kundeneinrichtung / Verantwortliche Organisationseinheit
- Datum der Risikobewertung
- Kurzbezeichnung des Risikos
- Risikobeschreibung
- Zuordnung zur betroffenen Leistung der ITKB bzw. dem betroffenen Service des Dienstleisters und soweit möglich dem betroffenen Zielobjekt
- Eintrittshäufigkeit (gering, mittel, hoch, sehr hoch)
- Beschreibung des potentiellen Schadens
- Schadenshöhe (vernachlässigbar, begrenzt, beträchtlich, existenzbedrohend)
- wenn verfügbar je Schadensdimension: Verstöße gegen Gesetze; Vorschriften und Verträge; Negative Innen- und Außenwirkung; Finanzielle Auswirkungen; Personenbezogene Sicherheit; Beeinträchtigung der Aufgabenerfüllung
- gewählte Risikobehandlungsoption inkl. Kurzbeschreibung der Risikobehandlungsmaßnahme
- bei Bedarf auch zusätzliche Anmerkungen / Kommentare

d) Die Institutionen der ITKB MÜSSEN bei der Meldung des Risikos die zum aktuellen Zeitpunkt bereits durchgeführten Risikobehandlungsmaßnahmen berücksichtigen.

e) Die Institutionen der ITKB MÜSSEN den betroffenen Dienstleistern im Rahmen der jährlichen Meldung für Verbundrisiken über die Entwicklung ihrer bisher gemeldeten potentiellen Verbundrisiken berichten. Ist eine Leistung der ITKB betroffen, die nicht durch einen zentralen Dienstleister bereitgestellt wird, MUSS die Meldung an den ISB ITKB 26  erfolgen.

f) Die Institutionen der ITKB MÜSSEN dem Dienstleister auf Nachfrage zusätzliche Informationen (insbesondere die zugrundeliegende Risikoanalyse) bezüglich der gemeldeten Verbundrisiken bereitstellen. Erfolgte die Meldung der Verbundrisiken an den ISB ITKB, MÜSSEN die Informationen dem ISB ITKB auf Nachfrage bereitgestellt werden.

24  Der Umgang mit Risiken aus Informationssicherheitsvorfällen oder Schwachstellen wird in den Kapiteln 2.6 und 2.7 behandelt.

25  Meldestelle-ISBITKB@bsi.bund.de

26  Meldestelle-ISBITKB@bsi.bund.de

<!-- page: 14 -->

## ISMS-ITKB.2.4.03 - Anlassbezogene Bewertung sicherheitsrelevanter Risiken

a) Die Kundeneinrichtung MUSS auf Nachfrage des Dienstleisters anlassbezogen ausgewählte, sicherheitsrelevante Risiken mit Bezug zur Inanspruchnahme einer Leistung der ITKB innerhalb der vom Dienstleister vorgegebenen Fristen bewerten.

b) Die Kundeneinrichtung MUSS dem Dienstleister eine Risikobewertung für die von ihm benannten Risiken im Rahmen der vorgegebenen Fristen übermitteln. Bei bereits bewerteten Risiken MUSS die Kundeneinrichtung dem Dienstleister eine aktualisierte Risikobewertung übermitteln.

## ISMS-ITKB.2.4.04 - Risikobehandlung

a) Die Institutionen der ITKB MÜSSEN auch für Verbundrisiken ITKB in ihrem Verantwortungsbereich 27 Risikobehandlungsoptionen/-pläne erstellen und kontinuierlich pflegen. Sie MÜSSEN dem ISB ITKB und den betroffenen Dienstleistern bei Bedarf weitergehende Informationen zur Risikobehandlung der ermittelten Verbundrisiken zur Verfügung stellen bzw. diese bei Bedarf gemeinsam abstimmen.

b) Die Kundeneinrichtung MUSS den Dienstleister bei der Behandlung eines Verbundrisikos unterstützen, sofern das Risiko nur durch die Mitwirkung der Kundeneinrichtung begrenzt werden kann.

c) Der Dienstleister DARF im Rahmen der vereinbarten Service Level Agreements (SLA) alle zur Behandlung des Verbundrisikos erforderlichen Maßnahmen NUR dann eigenständig durchführen, sofern die Kundeneinrichtung nicht im erforderlichen Umfang an der Reduktion des Risikos auf ein akzeptables Niveau mitwirkt.

d) Der Dienstleister MUSS bei eigenständiger Behandlung eines Verbundrisikos sicherstellen, dass der Nutzen die mit den erforderlichen Maßnahmen potentiell einhergehenden Beeinträchtigungen übersteigt.

e) Der Dienstleister MUSS die Kundeneinrichtung vorab über die eigenständige Behandlung eines Verbundrisikos inklusive der vorgenommenen Risiko-Nutzen-Abwägung informieren.

## ISMS-ITKB.2.4.05 - Konsolidierung der potentiellen Verbundrisiken ITKB und Weiterleitung an ISB ITKB

a) Die Dienstleister MÜSSEN potentielle Verbundrisiken ITKB, die ihnen gemeldet werden, verifizieren, sammeln, mit ihren eigenen potentiellen Verbundrisiken konsolidieren, bewerten und Verbundrisiken mit einem Schadensausmaß größer/gleich beträchtlich quartalsweise an den ISB ITKB melden.

b) Der ISB ITKB MUSS die Dienstleister über für sie relevante Verbundrisiken ITKB informieren.

c) Der ISB ITKB MUSS Ergebnisse aus der Prüfung nach § 4a BSIG im Verbundrisikomanagement berücksichtigen.

## ISMS ITKB.2.4.06 - Erstellung Risikobericht bzw. Ermittlung der übergreifenden Risikolage ITKB

a) Der ISB ITKB MUSS die Institutionen der ITKB über die übergreifende Risikolage der ITKB in Form eines jährlichen Berichts informieren.

b) Die Dienstleister MÜSSEN die Institutionen der ITKB halbjährlich über alle Veränderungen bei Verbundrisiken informieren.

c) Die Dienstleister MÜSSEN die Institutionen der ITKB unverzüglich über kritische Risiken informieren, die eine sofortige Handlung der Institutionen der ITKB erfordern oder deren Informationssicherheit erheblich gefährden.

d) Der ISB ITKB MUSS in den Sitzungen des CIO Boards zur Verbundrisikolage quartalsweise berichten.

e) Der ISB ITKB MUSS das CIO Board unverzüglich über existenzbedrohende übergreifende Verbundrisiken informieren.

27  abhängig von der Entscheidungs- und Durchführungsverantwortung in der ITKB gemäß Abbildung 2

<!-- page: 15 -->

## 2.5 Prüfungen/Nachweispflichten

Zu Prüfungen/ Nachweispflichten wurden in der ISR ITKB 2.0 insbesondere die folgenden Regelungen getroffen:

'1. Die Einhaltung der BSI-Standards durch die Institutionen der ITKB, einschließlich IT-Grundschutz, und BSIMindeststandards, SOLLTE im Rahmen von Prüfungen nach § 4a BSIG geprüft werden.

2. Aufgrund der regelmäßigen Überprüfung der Dienstleister nach § 4a BSIG sowie etwaiger Zertifizierungen entfallen im Rahmen der Leistungen der ITKB die Prüfpflichten und Prüfrechte der Kundeneinrichtungen gegenüber den Dienstleistern im Bereich der Informationssicherheit. […]

7. Der ISB ITKB kann, wenn dies zur Gewährleistung der Informationssicherheit in der ITKB erforderlich ist, unter bestimmten Bedingungen, welche im geplanten BSI-Mindeststandard aus zu detaillieren sind, Institutionen der ITKB anlassbezogen prüfen.'

Die Einhaltung der BSI-Standards wird grundsätzlich über die Standard-Revision nach § 4a BSIG nachgehalten. Prüfungen des ISB ITKB erfolgen nur bei Vorliegen der folgenden Ausnahmefälle und werden als Spezialprüfung im Sinne des Prüfkonzepts zu § 4a BSIG durchgeführt.

## ISMS-ITKB.2.5.01 - Prüfung bei begründetem Verdacht

a) Eine Institution der ITKB MUSS dem ISB ITKB ermöglichen, die Institution anlassbezogen zu prüfen, wenn der begründete Verdacht vorliegt, dass ein Verbundrisiko ITKB nicht bzw. nicht ausreichend behandelt wurde.

## ISMS-ITKB.2.5.02 - Prüfung der Beseitigung von Schwachstellen

a) Eine Institution der ITKB MUSS dem ISB ITKB ermöglichen, die Institution anlassbezogen zu prüfen, um die ordnungsgemäße und nachhaltige Beseitigung identifizierter Schwachstellen in der ITKB zu überprüfen.

## ISMS-ITKB.2.5.03 - Prüfung nach Eintritt eines Informationssicherheitsvorfalls

a) Eine Institution der ITKB MUSS dem ISB ITKB ermöglichen, die Institution anlassbezogen zu prüfen, wenn diese von einem Sicherheitsvorfall betroffen war, um sicherzustellen, dass daraus keine zusätzlichen Verbundrisiken ITKB resultieren.

## ISMS-ITKB.2.5.04 - Prüfung aufgrund fehlender Dokumentation

a) Eine Institution der ITKB MUSS dem ISB ITKB ermöglichen, die Institution anlassbezogen zu prüfen, wenn diese keine ausreichenden Prüfungen bzw. Prüfungsplanungen (z.B. Penetrationstests, IT-Audits etc.) für die Nutzung oder den Betrieb einer Leistung der ITKB nachweisen kann.

## ISMS-ITKB.2.5.05 - Prüfung aufgrund nicht umgesetzter Maßnahmen

a) Eine Institution der ITKB MUSS dem ISB ITKB ermöglichen, die Institution anlassbezogen zu prüfen, wenn die dokumentierten Maßnahmen aus den Prüfungsunterlagen des ISB ITKB nicht innerhalb der vorgegebenen Frist umgesetzt wurden.

## 2.6 Vorfallmanagement

## Zum Vorfallmanagement wurden in der ISR ITKB 2.0 insbesondere die folgenden Regelungen getroffen:

'1. Kundeneinrichtungen, die Informationssicherheitsvorfälle im Geltungsbereich der ISR ITKB feststellen, MÜSSEN diese gemäß der 'Allgemeinen Verwaltungsvorschrift § 4 Abs. 6 BSIG' an das BSI melden und, falls Dienstleister potentiell betroffen sind, SOLLTE die Meldung parallel an diese Dienstleister erfolgen.

2. Dienstleister, die Informationssicherheitsvorfälle im Geltungsbereich der ISR ITKB feststellen, MÜSSEN diese zusätzlich zur Meldung an das BSI gemäß der 'Allgemeinen Verwaltungsvorschrift § 4 Abs. 6 BSIG' auch direkt an potentiell betroffene Kundeneinrichtungen melden.'

<!-- page: 16 -->

Hier sind insbesondere die zentralen Dienstleister der IT-Konsolidierung Bund gemeint, welche als 'Generalunternehmer' Leistungen der ITKB erbringen.

Diese Regelungen werden wie folgt konkretisiert:

## ISMS-ITKB.2.6.01 - Vorfallmanagement bei jedem Informationssicherheitsvorfall (ISV)

a) Das BSI (nationales IT-Lagezentrum) MUSS bei jedem Informationssicherheitsvorfall prüfen, ob ein gemeldeter ISV potentiell die ITKB betrifft. Falls ein ISV potentiell die ITKB betrifft, MUSS das BSI sowohl die potentiell betroffenen Dienstleister als auch die potentiell betroffenen Kundeneinrichtungen sowie den ISB ITKB informieren, falls die Information nicht bereits erfolgt ist.

## ISMS-ITKB.2.6.02 - Vorfallmanagement der Kundeneinrichtung bei einem ISV

a) Die Kundeneinrichtung, die als Betreiber der IT-Komponente von einem ISV betroffen ist, MUSS unverzüglich alle zur Behandlung des ISV erforderlichen Maßnahmen initiieren.

b) Die Kundeneinrichtung, die als Betreiber der IT-Komponente von einem ISV betroffen ist, MUSS die Dienstleister und das nationale IT-Lagezentrum regelmäßig über den aktuellen Sachstand, die damit einhergehende Risikoeinschätzung sowie über getroffene Maßnahmen zur Mitigation informieren.

c) Andere Institutionen der ITKB, die von dem ISV einer Kundeneinrichtung potentiell betroffen sind, MÜSSEN der meldenden Kundeneinrichtung ihrerseits die für die Behandlung des ISV notwendigen Informationen bereitstellen.

d) Die Institutionen der ITKB SOLLTEN die Kundeneinrichtung im erforderlichen Umfang unterstützen, wenn die Kundeneinrichtung den ISV nicht ohne Mitwirkung anderer Institutionen der ITKB behandeln kann.

e) Die Kundeneinrichtung SOLLTE eigenständig alle zur Behandlung des ISV erforderlichen Maßnahmen durchführen, wenn Institutionen der ITKB nicht im erforderlichen Umfang an der Behandlung eines ISV mitwirken. Die betroffenen Institutionen der ITKB SOLLTEN über die Maßnahmen informiert werden.

## ISMS-ITKB.2.6.03 - Vorfallmanagement der Dienstleister bei einem ISV

a) Der Dienstleister, der als Betreiber der IT-Komponente von einem ISV betroffen ist, MUSS unverzüglich alle zur Behandlung des ISV erforderlichen Maßnahmen initiieren.

b) Der Dienstleister, der als Betreiber der IT-Komponente von einem ISV betroffen ist, MUSS potentiell betroffene Institutionen der ITKB regelmäßig über den aktuellen Sachstand, die damit einhergehende Risikoeinschätzung sowie über getroffene Maßnahmen zur Mitigation informieren.

c) Die Institutionen der ITKB, die von dem ISV bei einem Dienstleister potentiell betroffen sind, MÜSSEN dem Dienstleister ihrerseits die für die Behandlung des ISV notwendigen Informationen bereitstellen.

d) Die Institutionen der ITKB SOLLTEN den Dienstleister im erforderlichen Umfang unterstützen, sofern der Dienstleister den ISV nicht ohne Mitwirkung anderer Institutionen der ITKB behandeln kann.

e) Der Dienstleister SOLLTE eigenständig alle zur Behandlung des ISV erforderlichen Maßnahmen durchführen, wenn Institutionen der ITKB nicht im erforderlichen Umfang an der Behandlung eines ISV mitwirken. Die betroffenen Institutionen der ITKB SOLLTEN über die Maßnahmen informiert werden.

f) Der Dienstleister DARF, losgelöst vom Servicemodell, innerhalb der eigenen Räumlichkeiten NUR dann IT-forensische Untersuchungen bzw. Maßnahmen zur Bereinigung des ISV durchführen, sofern dies zu dessen Aufarbeitung für IT-Systeme bzw. Netzkomponenten erforderlich ist.

g) Der Dienstleister DARF NUR dann beispielsweise

- bis zum Abschluss der Behandlung eines ISV betroffene IT-Systeme bzw. Netzkomponenten vom Rest des Netzes trennen,
- Protokollierungsdaten von betroffenen IT-Systemen bzw. Netzkomponenten sicherstellen,

<!-- page: 17 -->

- darauf befindliche schadhafte Dateien löschen wie auch
- die IT-Systeme bzw. Netzkomponenten neu aufsetzen (lassen),

sofern dies zur Aufarbeitung sicherheitsrelevanter Ereignisse erforderlich ist.

h) Der Dienstleister MUSS betroffene Institutionen der ITKB vor der Durchführung IT-forensischer Untersuchungen wie auch von Maßnahmen zur Bereinigung der ISV informieren.

i) Die Kundeneinrichtung MUSS den Dienstleister - sofern erforderlich - bei der IT-forensischen Untersuchung unterstützen.

## 2.7 Schwachstellenmanagement

Zum Schwachstellenmanagement wurden in der ISR ITKB 2.0 insbesondere die folgenden Regelungen getroffen:

'Institutionen der ITKB MÜSSEN erkannte Schwachstellen, die sich potentiell auf andere Institutionen der ITKB auswirken könnten, beheben oder geeignete mitigierende Maßnahmen treffen. Ist dies nicht unmittelbar möglich, MUSS die jeweilige Institution der ITKB eine Risikoanalyse gemäß BSI-Standard 200-3 28  durchführen. Falls Risiken für andere Institutionen der ITKB entstehen, wird eine angemessene Überwachung der Behandlung im Rahmen des Verbundrisikomanagements ITKB sichergestellt.'

Einschlägig (insbesondere bezüglich der Meldung von Schwachstellen an das CERT Bund) ist zudem die Allgemeine Verwaltungsvorschrift über das Meldeverfahren gemäß § 4 Abs. 6 BSIG.

Die Regelungen werden wie folgt konkretisiert:

## ISMS-ITKB.2.7.01 - Anforderungen an das Schwachstellenmanagement für Institutionen der ITKB

a) Das BSI (CERT-Bund) MUSS kritische Schwachstellen, die die ITKB betreffen können, an den ISB ITKB melden.

b) Die Institutionen der ITKB, die Betreiber einer von einer Schwachstelle betroffenen IT-Komponente sind, MÜSSEN Maßnahmen zu deren Behandlung initiieren. Ist eine unverzügliche Behebung der Schwachstelle nicht möglich, MÜSSEN sie das damit verbundene Risiko bewerten. Falls damit ein potentielles Verbundrisiko einhergeht, MÜSSEN sie dieses an den jeweiligen zentralen Dienstleister melden. Ist eine Leistung der ITKB betroffen, die nicht durch einen zentralen Dienstleister bereitgestellt wird, MUSS die Meldung an den ISB ITKB erfolgen.

c) Die Institutionen der ITKB, die Betreiber einer von einer Schwachstelle betroffenen IT-Komponente sind, SOLLTEN auf Nachfrage des ISB ITKB oder eines Dienstleisters den Bearbeitungsstand der Behandlung der Schwachstelle mitteilen.

## 2.8 Schnittstellen im ISMS ITKB

Zu Schnittstellen im ISMS ITKB wurden in der ISR ITKB 2.0 insbesondere die folgenden Regelungen getroffen:

'1. Alle Institutionen der ITKB MÜSSEN einen Single Point of Contact (SPOC) für die Informationssicherheit in der ITKB einrichten, der über die notwendigen Berechtigungen und Befugnisse verfügt. Dieser dient als zentraler Ansprechpartner nach außen. D. h. er MUSS alle Anfragen bezüglich Informationssicherheit von außen annehmen, intern verteilen und seinerseits informationssicherheitsrelevante Informationen zentral nach außen kommunizieren.

2. Die Dienstleister können bei Bedarf auch mehrere Ansprechpartner für verschiedene Themen einrichten.

[28  Vgl. BSI-Standard 200-3 (BSI 2017b)](https://www.bsi.bund.de/dok/407502)

<!-- page: 18 -->

3. Die Kontaktdaten des jeweiligen SPOC MÜSSEN den Institutionen der ITKB bekannt gegeben und regelmäßig aktualisiert werden.

4. Die Institutionen der ITKB MÜSSEN die Besetzung und Erreichbarkeit der SPOC gewährleisten.'

Diese Regelungen werden wie folgt konkretisiert:

## ISMS-ITKB.2.8.01 - Anforderungen an die Bereitstellung der Kontaktdaten der Single Point of Contact (SPOC)

a) Die Institutionen der ITKB MÜSSEN ihren jeweiligen Single Point of Contact (SPOC) bzw. im Falle der Dienstleister ihre jeweiligen SPOC für die Informationssicherheit in der ITKB gegenüber dem ISB ITKB per bereitgestellten Formular 29  über E-Mail benennen. Dabei SOLLTEN mindestens folgende Anforderungen an einen SPOC erfüllt sein:

- Funktionspostfach
- Erreichbarkeit während der Dienstzeiten
- Alternative Erreichbarkeit im Störungs-/Not-/Krisen-/ Katastrophenfall (z. B. Mobiltelefon)
- Anschrift
- Eskalationsinstanz

b) Der ISB ITKB MUSS die SPOC der Institutionen der ITKB zentral dokumentieren, aktualisieren und an einem zentralen Ablageort zugänglich machen.

## ISMS-ITKB.2.8.02 - Berechtigungen und Befugnisse für SPOC der Kundeneinrichtungen

a) Die Kundeneinrichtungen MÜSSEN dem jeweiligen SPOC notwendige Berechtigungen und Befugnisse zur Wahrnehmung der vorgesehenen Aufgaben innerhalb der eigenen Institution der ITKB einrichten, insbesondere für:

- Entgegennahme der Leistungsbeschreibungen und -nachweise zur hausinternen Weitergabe der sicherheitsrelevanten Informationen
- Entgegennahme der jährlichen Berichte der Dienstleister zu Verbundrisiken und relevanten Prüf/Übungsergebnissen
- Meldung potentieller Verbundrisiken an die Dienstleister und/oder den ISB ITKB
- Übermittlung und Entgegennahme von Informationen zu Informationssicherheitsvorfällen
- Übermittlung und Entgegennahme von Informationen zu (der Betroffenheit von) Schwachstellen
- Falls relevant, Zugriff auf entsprechende Übermittlungstools (bspw. ZeDIS, E-Mail)
- Zugriff auf Kontaktdaten aller SPOC der Institutionen der ITKB

## ISMS-ITKB.2.8.03 - Berechtigungen und Befugnisse für SPOC der Dienstleister

a) Die Dienstleister MÜSSEN den jeweiligen SPOC notwendige Berechtigungen und Befugnisse zur Wahrnehmung der vorgesehenen Aufgaben innerhalb der eigenen Institution der ITKB einrichten, insbesondere für:

- Bereitstellung von Leistungsbeschreibungen und -nachweisen
- Übermittlung der jährlichen Berichte zu Verbundrisiken und relevanten Prüf-/Übungsergebnissen
- Entgegennahme der Meldungen potentieller Verbundrisiken der Kundeneinrichtungen

29  Das Formular wird auf der Webseite des MST ISMS ITKB zum Download bereitgestellt: https://bsi.bund.de/dok/1117162

<!-- page: 19 -->

- Entgegennahme von Warnhinweisen des CERT-Bund
- Übermittlung und Entgegennahme von SOFORT-Meldungen gemäß § 4 Abs. 6 BSIG
- Übermittlung und Entgegennahme von Informationen zu Informationssicherheitsvorfällen
- Übermittlung und Entgegennahme von Informationen zu (der Betroffenheit von) Schwachstellen
- Kommunikation zu aktuellen IT-Sicherheitsthemen

## ISMS-ITKB.2.8.04 - Pflichten der SPOC

a) Der jeweilige SPOC des Dienstleisters/der Kundeneinrichtung MUSS bis zur abschließenden Bearbeitung des Vorgangs sicherstellen, dass die für die Behandlung des Vorgangs erforderlichen Informationen wie auch Rückfragen unverzüglich, und in nachvollziehbarer Weise an die zuständigen Stellen im eigenen Verantwortungsbereich weitergeleitet und durch diese unverzüglich, sachgerecht, nachvollziehbar und abschließend beantwortet werden.

## 2.9 Leistungsbeziehung in der ITKB

Bei der Leistungsbeziehung zwischen Kundeneinrichtungen und Dienstleistern der ITKB handelt es sich nicht um ein klassisches Outsourcing-Verhältnis zwischen einem Auftraggeber und einem Auftragnehmer. In der ITKB wird die Entwicklung von Leistungen durch die Projektleitungen BKB/DK bei einem Dienstleister beauftragt, die in standardisierter Form durch den Dienstleister bereitgestellt wird und seitens der Kundeneinrichtungen genutzt werden kann.

Somit besteht keine Verpflichtung zur Anwendung der IT-Grundschutz-Bausteine zum Outsourcing oder zur Cloud-Nutzung und es werden stattdessen eigene Anforderungen für die ITKB in dem benutzerspezifischen IT-Grundschutz Baustein "OPS.bd.3.1 Leistungsbeziehung in der IT-Konsolidierung Bund (ITKB)" 30  festgelegt. Daher wird in diesem Dokument auch nicht von einer Outsourcing-Beziehung gesprochen, sondern von einer Leistungsbeziehung in der ITKB, welche zwischen den Kundeneinrichtungen als Nutzern einer Leistung der ITKB auf der einen Seite und dem jeweiligen Dienstleister als entsprechendem Bereitsteller der Leistung der ITKB auf der anderen Seite besteht.

Die in dem benutzerdefinierten Baustein "OPS.bd.3.1 Leistungsbeziehung in der IT-Konsolidierung Bund (ITKB)" aufgeführten Anforderungen wurden aus den genannten Bausteinen abgeleitet, um Anforderungen ergänzt, die im Rahmen der ITKB zur Gewährleistung der Informationssicherheit erforderlich sind und sollen die entstandene Regelungslücke schließen. Unbenommen bleibt die Verpflichtung zur Anwendung der Outsourcing-Bausteine bei einem Outsourcing an Dritte außerhalb der ITKB.

Die beiden nachfolgenden unter ISMS-ITKB.2.9.01 aufgeführten Anforderungen gelten für alle Leistungen der ITKB. Die Entscheidungs- und Durchführungsverantwortung für die Umsetzung von Sicherheitsmaßnahmen zum Schutz der entsprechenden IT liegt dabei bei derjenigen Institution der ITKB, die für den Betrieb der entsprechenden IT verantwortlich ist (Betreiber).

30  Vgl. Benutzerdefinierter Baustein: OPS.bd.3.1 Leistungsbeziehung in der IT-Konsolidierung Bund (BSI 2024b)

<!-- page: 20 -->

## ISMS-ITKB.2.9.01 - Anforderungen für alle Leistungen der ITKB

a) Dienstleister und Kundeneinrichtungen SOLLTEN für Leistungen der ITKB NICHT die Bausteine zum Outsourcing (OPS.2.3 Nutzung von Outsourcing 31  sowie OPS.3.2 Anbieten von Outsourcing 32 ) oder zur Cloud-Nutzung (OPS.2.2 Cloud-Nutzung 33 ) modellieren.

b) Dienstleister und Kundeneinrichtungen MÜSSEN für Leistungen der ITKB jeweils für jede in Anspruch genommene bzw. angebotene Leistung einmal die im benutzerdefinierten Baustein "OPS.bd.3.1 Leistungsbeziehung in der IT-Konsolidierung Bund (ITKB)" 34  festgelegten Anforderungen zur Leistungsbeziehung in der ITKB modellieren und anwenden.

31  Vgl. IT-Grundschutz-Kompendium: OPS.2.3 Nutzung von Outsourcing (BSI 2023b)

32     Vgl. IT-Grundschutz-Kompendium: OPS.3.2 Anbieten von Outsourcing (BSI 2023b)

33  Vgl. IT-Grundschutz-Kompendium: OPS.2.2 Cloud-Nutzung (BSI 2023b)

34  Vgl. Benutzerdefinierter Baustein: OPS.bd.3.1 Leistungsbeziehung in der IT-Konsolidierung Bund (BSI 2024b)

<!-- page: 21 -->

## Literaturverzeichnis

| BMI (2015)   | Bundesministerium des Innern und für Heimat: Grobkonzept IT-Konsolidierung Bund https://www.cio.bund.de/SharedDocs/downloads/Webs/CIO/DE/cio-bund/steuerung-it- bund/grobkonzept-it-konsolidierung.html, abgerufen am 15.04.2024                                                                                                  |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BMI (2017)   | Bundesministerium des Innern und für Heimat: Umsetzungsplan Bund - Leitlinie für Informationssicherheit in der Bundesverwaltung, 2017                                                                                                                                                                                             |
| BSI (2017a)  | Bundesamt für Sicherheit in der Informationstechnik: BSI-Standard 200-2 - IT-Grundschutz-Methodik, Version 1.0, 2017, https://www.bsi.bund.de/dok/10027846                                                                                                                                                                        |
| BSI (2017b)  | Bundesamt für Sicherheit in der Informationstechnik: BSI-Standard 200-3 - Risikoanalyse auf der Basis von IT-Grundschutz, Version 1.0, 2017, https://www.bsi.bund.de/dok/407502                                                                                                                                                   |
| BSI (2023a)  | Bundesamt für Sicherheit in der Informationstechnik: Informationssicherheitsrichtlinie für die IT-Konsolidierung Bund, Version 2.0, https://www.bsi.bund.de/DE/Intern/Sicherheitsberatung/Bund/Dokumente/Publikationen /IT-Konsolidierung/Richtlinie_IT-Konsolidierung_Bund_V200.html                                             |
| BSI (2023b)  | Bundesamt für Sicherheit in der Informationstechnik: IT-Grundschutz-Kompendium, Edition 2023, https://www.bsi.bund.de/dok/1073656 - OPS.2.3 Nutzung von Outsourcing: https://bsi.bund.de/dok/1073624 - OPS.3.2 Anbieten von Outsourcing: https://bsi.bund.de/dok/1073630 - OPS.2.2 Cloud-Nutzung: https://bsi.bund.de/dok/1073626 |
| BSI (2023c)  | Bundesamt für Sicherheit in der Informationstechnik: BSI-Standard 200-4 Business Continuity Management, Version 1.0, 2023, https://bsi.bund.de/dok/531578                                                                                                                                                                         |
| BSI (2024a)  | Bundesamt für Sicherheit in der Informationstechnik: Mindeststandards - Antworten auf häufig gestellte Fragen zu den Mindeststandards, https://www.bsi.bund.de/dok/MST-FAQ                                                                                                                                                        |
| BSI (2024b)  | Bundesamt für Sicherheit in der Informationstechnik: Benutzerdefinierte Bausteine - OPS.bd.3.1 Leistungsbeziehung in der IT-Konsolidierung Bund: https://www.bsi.bund.de/dok/943082                                                                                                                                               |
| DIN (2022)   | Deutsches Institut für Normung e.V.: Normungsarbeit - Teil 2: Gestaltung von Dokumenten, DIN 820-2:2022-12, 2022                                                                                                                                                                                                                  |
| IETF (1997)  | Internet Engineering Task Force: Key words for use in RFCs to Indicate Requirement Levels, RFC 2119, https://tools.ietf.org/html/rfc2119, abgerufen am 15.04.2024                                                                                                                                                                 |

<!-- page: 22 -->

## Abkürzungsverzeichnis

AG ISI Arbeitsgruppe Informationssicherheit

AG ISM Arbeitsgruppe Informationssicherheitsmanagement

BAköV Bundesakademie für öffentliche Verwaltung

BDBOS Bundesanstalt für den Digitalfunk der Behörden und Organisationen mit Sicherheitsaufgaben

BKB IT-Betriebskonsolidierung Bund

BMF Bundesministerium der Finanzen

BMI Bundesministerium des Innern und für Heimat

BSI Bundesamt für Sicherheit in der Informationstechnik

BSIG Gesetz über das Bundesamt für Sicherheit in der Informationstechnik

Cert-Bund Computer Emergency Response Team für Bundesbehörden

CIO Board Chief Information Officer Board (Gremium)

DIN

Deutsches Institut für Normung e.V.

DK

IT-Dienstekonsolidierung

FAQ Frequently Asked Questions

IaaS

Infrastructure as a Service

IETF

ISB

ISK

ISMS

ISR

ISV

ITKB

IT-SiBe

ITZBund

MST

PaaS

RFC

SaaS

SLA

SPOC

UP

Internet Engineering Task Force

Informationssicherheitsbeauftragte

Informationssicherheitskonzept

Informationssicherheitsmanagementsystem

Informationssicherheitsrichtlinie

Informationssicherheitsvorfall

IT-Konsolidierung Bund

IT-Sicherheitsbeauftragte

Informationstechnikzentrum Bund

Mindeststandard

Platform as a Service

Request for Comments

Software as a Service

Service Level Agreement

Single Point of Contact

Umsetzungsplan

ZeDIS Zentraler Dienst für Informationssicherheit

<!-- page: 23 -->

## Glossar

## Auslagerungsregister

Ein Auslagerungsregister ist ein Dokument zur Auflistung aller im Rahmen der ITKB ausgelagerten Leistungen inklusive des Dienstleisters, der für die Leistungserbringung verantwortlich ist. In diesem sollten auch die mit der ausgelagerten Leistung verbundenen SLA definiert sein.

## Betreiber

Der Betreiber ist die Institution der ITKB, die für den Betrieb von IT-Komponenten (IT-Schicht) verantwortlich ist. Dieser trägt die Entscheidungs- und Durchführungsverantwortung für die Umsetzung und Aufrechterhaltung von Sicherheitsmaßnahmen zum Schutz der betriebenen IT sowie die Verantwortung für die Risiken aus dem Betrieb.

## Dienstleister

Dienstleister im Rahmen des vorliegenden Mindeststandards sind zum einen Netzdienstleister und zum anderen IT-Dienstleister, die für die ITKB Leistungen erbringen. Sie entscheiden selbstständig über operative Angelegenheiten im eigenen Zuständigkeitsbereich.

## Institutionen der ITKB

Institutionen der ITKB sind die Projektleitungen BKB und DK, die Dienstleister und die Kundeneinrichtungen.

## Kundeneinrichtung

Eine Kundeneinrichtung ist eine juristische Person oder eine rechtlich unselbständige organisatorische Einheit der Bundesverwaltung, die Leistungen der ITKB nachfragt.

## Leistungen der ITKB

Leistungen der ITKB sind Betriebsplattformen, Dienste, Netze und IT-Lösungen, welche die Dienstleister für Kundeneinrichtungen in der ITKB anbieten.

## Leistungsbeschreibung

Mithilfe einer Leistungsbeschreibung stellt der Dienstleister notwendige Informationen über eine Leistung der ITKB zur Verfügung, welche die jeweilige Kundeneinrichtung entweder für die Nutzung der Leistung oder die Erstellung der eigenen Informationssicherheitskonzepte (ISK) benötigt.

## Projektleitungen BKB und DK

Projektleitungen BKB und DK sind die Projektleitung IT-Betriebskonsolidierung Bund und die Projektleitung IT-Dienstekonsolidierung, die gemäß Kabinettsbeschluss ITK1-17007/1#6 vom 20.05.2015 grundsätzlich standardisierte IT-Lösungen in Auftrag geben und in operativen Angelegenheiten der Projekte entscheiden. Diese können jeweils zuständige und entscheidungsbefugte Personen oder Organisationseinheiten als Vertreter benennen.

## Verbundrisiko

Ein Verbundrisiko im Rahmen der ITKB ist ein Risiko, welches Auswirkungen auf andere Institutionen der ITKB haben kann oder nicht durch eine Institution der ITKB allein behandelt werden kann.

## Verbundrisikomanagement

Das Verbundrisikomanagement der ITKB umfasst die Erfassung und Bewertung von Verbundrisiken der ITKB sowie das Berichtswesen und die Überwachung bzw. Nachverfolgung der Verbundrisikobehandlung.

<!-- page: 24 -->

## Vereinbarungen

Vereinbarungen umfassen die verbindlichen vertraglichen Vereinbarungen zwischen Dienstleister und Kundeneinrichtung zur Inanspruchnahme der Leistungen der ITKB.

## Weitverkehrsnetze der Bundesverwaltung

Unter den Weitverkehrsnetzen der Bundesverwaltung sind alle Weitverkehrsnetze zu verstehen, die durch einen Netzbetreiber zentral für Einrichtungen der Bundesverwaltung bereitgestellt werden und auf diese beschränkt bleiben.

<!-- page: 25 -->

## Anhang 1: Einheitliche Schutzbedarfskategorien ITKB

Schutzbedarfskategorie "normal"

| Szenario                                                      | Vertraulichkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integrität                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Verfügbarkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Verstöße gegen Gesetze, Vorschriften oder Verträge            | Ein Verstoß gegen Gesetze, Vorschriften oder Verträge hat maximal geringfügige Konsequenzen, die durch die bestehende Allgemeine Aufbauorganisation kompensiert werden können. Die Notwendigkeit zur Meldung des Verstoßes an die Leitungsebene erscheint unwahrscheinlich. Die Notwendigkeit zur Einbindung zusätzlicher Expertise (bspw. zu juristischen Fragestellungen) erscheint ausgeschlossen. Geld- oder Freiheitsstrafen erscheinen auch bei einem Verstoß ausgeschlossen. Die Informationen sind hinsichtlich ihrer Vertraulichkeit nicht als Verschlusssache eingestuft bzw. dürfen innerhalb und außerhalb der Organisationen frei an die vorgesehenen Personenkreise weitergegeben werden. | Ein Verstoß gegen Gesetze, Vorschriften oder Verträge hat maximal geringfügige Konsequenzen, die durch die bestehende Allgemeine Aufbauorganisation kompensiert werden können. Die Notwendigkeit zur Meldung des Verstoßes an die Leitungsebene erscheint unwahrscheinlich. Die Notwendigkeit zur Einbindung zusätzlicher Expertise (bspw. zu juristischen Fragestellungen) erscheint ausgeschlossen. Geld- oder Freiheitsstrafen erscheinen auch bei einem Verstoß ausgeschlossen | Ein Verstoß gegen Gesetze, Vorschriften oder Verträge hat maximal geringfügige Konsequenzen, die durch die bestehende Allgemeine Aufbauorganisation kompensiert werden können. Die Notwendigkeit zur Meldung des Verstoßes an die Leitungsebene erscheint unwahrscheinlich. Die Notwendigkeit zur Einbindung zusätzlicher Expertise (bspw. zu juristischen Fragestellungen) erscheint ausgeschlossen. Freiheitsstrafen erscheinen auch bei einem Verstoß ausgeschlossen. Eine Nicht-Verfügbarkeit der IT-Lösung von mehr als 24h wirkt sich bei vorhandenen SLA nicht auf deren Einhaltung aus. |
| Beeinträchtigung des informationellen Selbstbestimmungsrechts | Eine nachhaltige Beeinträchtigung von Betroffenen in ihrer gesellschaftlichen/wirt- schaftlichen Stellung bzw. ein Rückschluss auf das gesundheitliche Befinden erscheint unwahrscheinlich.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Eine nachhaltige Beeinträchtigung von Betroffenen in ihrer gesellschaftlichen/wirt- schaftlichen Stellung bzw. ein Rückschluss auf das gesundheitliche Befinden erscheint unwahrscheinlich.                                                                                                                                                                                                                                                                                        | Eine nachhaltige Beeinträchtigung von Betroffenen in ihrer gesellschaftlichen/wirt- schaftlichen Stellung bzw. ein Rückschluss auf das gesundheitliche Befinden erscheint unwahrscheinlich.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Beeinträchtigung der persönlichen Unversehrtheit              | Eine generelle Schädigung der physischen bzw. psychischen Unversehrtheit wie auch eine ärztliche Behandlung erscheint unwahrscheinlich.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Eine generelle Schädigung der physischen bzw. psychischen ist nicht zu erwarten wie auch eine ärztliche Behandlung erscheint unwahrscheinlich.                                                                                                                                                                                                                                                                                                                                     | Auch bei Nicht-Verfügbarkeit von Informationen von mehr als 24h erscheint eine generelle Schädigung der physischen bzw. psychischen Unversehrtheit wie auch eine ärztliche Behandlung unwahrscheinlich.                                                                                                                                                                                                                                                                                                                                                                                         |

<!-- page: 26 -->

| Szenario                               | Vertraulichkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integrität                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Verfügbarkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Beeinträchtigung der Aufgabenerfüllung | Ein mit der Beeinträchtigung der Aufgabenerfüllung verbundenes höheres Arbeitsaufkommen kann durch die bestehende Allgemeine Aufbauorganisation kompensiert werden. Eine Information und/oder Einbindung der Leitungsebene erscheint unwahrscheinlich.                                                                                                                                                                                                                                                                  | Ein mit der Beeinträchtigung der Aufgabenerfüllung verbundenes höheres Arbeitsaufkommen kann durch die bestehende Allgemeine Aufbauorganisation kompensiert werden. Eine Information und/oder Einbindung der Leitungsebene erscheint unwahrscheinlich.                                                                                                                                                                                                                                                                  | Eine Beeinträchtigung der Aufgabenerfüllung kann auch bei einer Dauer von mehr als 24h durch die bestehende Allgemeine Aufbauorganisation kompensiert werden. Eine Information und/oder Einbindung der Leitungsebene erscheint unwahrscheinlich.                                                                                                                                                                                                                                                                        |
| negative Innen- und Außenwirkung       | Es ist anzunehmen, dass mangels Interesses der Öffentlichkeit außerhalb des Ressorts nicht über den eingetretenen Schaden in den Medien berichtet wird. Eine Ansehens-/ Vertrauensbeeinträchtigung erscheint unwahrscheinlich oder führt voraussichtlich nicht zu politischer/ gesellschaftlicher Verunsicherung bzw. Zweifeln an der amtlichen Zuverlässigkeit und kann daher - ohne Einbindung der Leitungsebene oder jegliche Form der Außenkommunikation - in der Allgemeine Aufbauorganisation kompensiert werden. | Es ist anzunehmen, dass mangels Interesses der Öffentlichkeit außerhalb des Ressorts nicht über den eingetretenen Schaden in den Medien berichtet wird. Eine Ansehens-/ Vertrauensbeeinträchtigung erscheint unwahrscheinlich oder führt voraussichtlich nicht zu politischer/ gesellschaftlicher Verunsicherung bzw. Zweifeln an der amtlichen Zuverlässigkeit und kann daher - ohne Einbindung der Leitungsebene oder jegliche Form der Außenkommunikation - in der Allgemeine Aufbauorganisation kompensiert werden. | Es ist anzunehmen, dass mangels Interesses der Öffentlichkeit außerhalb des Ressorts nicht über den eingetretenen Schaden in den Medien berichtet wird. Eine Ansehens-/ Vertrauensbeeinträchtigung erscheint unwahrscheinlich oder führt voraussichtlich nicht zu politischer/ gesellschaftlicher Verunsicherung bzw. Zweifeln an der amtlichen Zuverlässigkeit und kann daher - ohne Einbindung der Leitungsebene oder jegliche Form der Außenkommunikation - in der Allgemeine Aufbauorganisation kompensiert werden. |
| finanzielle Auswirkungen               | Finanzielle Auswirkungen infolge von Konventionalstrafen oder Schäden (inklusive Kosten für deren Behandlung können ohne Umplanung aus dem vorhandenen Budget der Allgemeinen Aufbauorganisation abgedeckt werden.                                                                                                                                                                                                                                                                                                      | Finanzielle Auswirkungen infolge von Konventionalstrafen oder Schäden (inklusive Kosten für deren Behandlung) können ohne Umplanung aus dem vorhandenen Budget der Allgemeinen Aufbauorganisation abgedeckt werden                                                                                                                                                                                                                                                                                                      | Finanzielle Auswirkungen infolge von Konventionalstrafen, Abweichungen von den vertraglichen Verpflichtungen (wie bspw. den vereinbarten SLA) oder Schäden (inklusive Kosten für deren Behandlung) können ohne Umplanung aus dem vorhandenen Budget der Allgemeinen Aufbauorganisation abgedeckt werden.                                                                                                                                                                                                                |

<!-- page: 27 -->

## Schutzbedarfskategorie "hoch"

| Szenario                                           | Vertraulichkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integrität                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Verstöße gegen Gesetze, Vorschriften oder Verträge | Verstöße gegen Gesetze, Vorschriften und Verträge machen eine Behandlung durch eine dafür einzuberufende Besondere Aufbauorganisation erforderlich. Die Notwendigkeit zu einer gesonderten, unmittelbaren Meldung des Verstoßes an die Leitungsebene erscheint erforderlich. Eine Einbindung zusätzlicher Expertise (bspw. zu juristischen Fragestellungen) erscheint in Abhängigkeit der zu erwartenden Konsequenzen wahrscheinlich. Bei Verstößen gegen Gesetze erscheinen vorrangig Geldbußen/ Kürzungen der Dienstbezüge anstelle von Freiheitsstrafen wahrscheinlich. Verstöße gegen Vorschriften und Verträge werden mit zusätzlichen Sanktionen geahndet. Die Informationen sind hinsichtlich ihrer Vertraulichkeit als Verschlusssache VS-NfD eingestuft, sodass eine unbefugte Kenntnisnahme für die Interessen der Bundesrepublik Deutschland oder eines ihrer Länder nachteilig sein könnte. | Verstöße gegen Gesetze, Vorschriften und Verträge machen eine Behandlung durch eine dafür einzuberufende Besondere Aufbauorganisation erforderlich. Die Notwendigkeit zu einer gesonderten, unmittelbaren Meldung des Verstoßes an die Leitungsebene erscheint erforderlich. Eine Einbindung zusätzlicher Expertise (bspw. zu juristischen Fragestellungen) erscheint in Abhängigkeit der zu erwartenden Konsequenzen wahrscheinlich. Bei Verstößen gegen Gesetze erscheinen vorrangig Geldbußen/ Kürzungen der Dienstbezüge anstelle von Freiheitsstrafen wahrscheinlich. Verstöße gegen Vorschriften und Verträge werden mit zusätzlichen Sanktionen geahndet | Verfügbarkeit . Verstöße gegen Gesetze, Vorschriften und Verträge machen eine Behandlung durch eine dafür einzuberufende Besondere Aufbauorganisation erforderlich. Die Notwendigkeit zu einer gesonderten, unmittelbaren Meldung des Verstoßes an die Leitungsebene erscheint erforderlich. Eine Einbindung zusätzlicher Expertise (bspw. zu juristischen Fragestellungen) erscheint in Abhängigkeit der zu erwartenden Konsequenzen wahrscheinlich. Bei Verstößen gegen Gesetze erscheinen vorrangig Geldbußen/ Kürzungen der Dienstbezüge anstelle von Freiheitsstrafen wahrscheinlich. Verstöße gegen Vorschriften und Verträge werden mit zusätzlichen Sanktionen geahndet. Ein Ausfall der IT-Lösung im Zeitraum von 3h bis 24h führt bei vorhandenen SLA zu deren Nicht-Einhaltung. |

<!-- page: 28 -->

| Szenario                                                      | Vertraulichkeit                                                                                                                                                                                                                                                                                                                          | Integrität                                                                                                                                                                                                                                                                                                                               | Verfügbarkeit                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Beeinträchtigung des informationellen Selbstbestimmungsrechts | Eine nachhaltige Beeinträchtigung von Betroffenen in ihrer gesellschaftlichen/ wirtschaftlichen Stellung bzw. ein Rückschluss auf das gesundheitliche Befinden erscheint durch die Beeinträchtigung des informationellen Selbstbestimmungsrechts möglich.                                                                                | Eine nachhaltige Beeinträchtigung von Betroffenen in ihrer gesellschaftlichen/ wirtschaftlichen Stellung bzw. ein Rückschluss auf das gesundheitliche Befinden erscheint durch die Beeinträchtigung des informationellen Selbstbestimmungsrechts möglich.                                                                                | Eine nachhaltige Beeinträchtigung von Betroffenen in ihrer gesellschaftlichen/ wirtschaftlichen Stellung bzw. ein Rückschluss auf das gesundheitliche Befinden erscheint durch die Beeinträchtigung des informationellen Selbstbestimmungsrechts möglich.                                                                                                                              |
| Beeinträchtigung der persönlichen Unversehrtheit              | Die Beeinträchtigung der persönlichen Unversehrtheit kann eine ärztliche Behandlung erfordern. Eine Beeinträchtigung der körperlichen Unversehrtheit erscheint wahrscheinlich, tödliche Auswirkungen oder langfristige physische bzw. psychische Schäden, die eine langjährige Behandlung erfordern, erscheinen jedoch unwahrscheinlich. | Die Beeinträchtigung der persönlichen Unversehrtheit kann eine ärztliche Behandlung erfordern. Eine Beeinträchtigung der körperlichen Unversehrtheit erscheint wahrscheinlich, tödliche Auswirkungen oder langfristige physische bzw. psychische Schäden, die eine langjährige Behandlung erfordern, erscheinen jedoch unwahrscheinlich. | Die Beeinträchtigung der persönlichen Unversehrtheit kann eine ärztliche Behandlung erfordern. Bei Nicht-Verfügbarkeit im Zeitraum von 3h bis 24h erscheint eine Beeinträchtigung der körperlichen Unversehrtheit wahrscheinlich, tödliche Auswirkungen oder langfristige physische bzw. psychische Schäden, die eine langjährige Behandlung                                           |
| Beeinträchtigung der Aufgabenerfüllung                        | erfordert Einsetzen einer die sich eine weitergehende Behandlung zeigt bzw. die des zusätzlichen bedarf einer gesonderten, an die notwendigen                                                                                                                                                                                            | Eine Beeinträchtigung der Aufgabenerfüllung erfordert das Einsetzen einer Besonderen Aufbauorganisation, die sich für eine weitergehende Eskalation/ Behandlung verantwortlich zeigt bzw. die Bewältigung des zusätzlichen Arbeitsaufkommens übernimmt.                                                                                  | unwahrscheinlich. Eine Beeinträchtigung der Aufgabenerfüllung im Zeitraum von 3h bis 24h erfordert das Einsetzen einer Besonderen Aufbauorganisation, die sich für eine weitergehende Eskalation/ Behandlung verantwortlich zeigt bzw. die Bewältigung des zusätzlichen Arbeitsaufkommens übernimmt. Es bedarf einer gesonderten, Meldung an die die notwendigen Entscheidungen können |
|                                                               | Eine Beeinträchtigung der Aufgabenerfüllung das Besonderen Aufbauorganisation, für Eskalation/ verantwortlich Bewältigung Arbeitsaufkommens übernimmt. Es Meldung Leitungsebene, die Entscheidungen können jedoch ohne deren Einbindung herbeigeführt werden..                                                                           | Es bedarf einer gesonderten, Meldung an die Leitungsebene, die notwendigen Entscheidungen können jedoch ohne deren Einbindung herbeigeführt werden.                                                                                                                                                                                      | Leitungsebene, jedoch ohne deren Einbindung herbeigeführt werden.                                                                                                                                                                                                                                                                                                                      |

<!-- page: 29 -->

| Szenario                         | Vertraulichkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integrität                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Verfügbarkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| negative Innen- und Außenwirkung | Eine Ansehens-/ Vertrauensbeeinträchtigung außerhalb des Ressorts erscheint aufgrund der öffentlichen Berichterstattung wahrscheinlich. Eintretende Schäden führen unter Umständen zu politischer/ gesellschaftlicher Verunsicherung bzw. Zweifeln an der amtlichen Zuverlässigkeit und machen daher eine gesonderte Meldung an die Leitungsebene erforderlich. Über die Behandlung der Auswirkungen kann jedoch unterhalb der Leitungsebene entschieden werden und es bedarf keiner offiziellen Stellungnahme gegenüber externen Stellen. | Eine Ansehens-/ Vertrauensbeeinträchtigung außerhalb des Ressorts erscheint aufgrund der öffentlichen Berichterstattung wahrscheinlich. Eintretende Schäden führen unter Umständen zu politischer/ gesellschaftlicher Verunsicherung bzw. Zweifeln an der amtlichen Zuverlässigkeit und machen daher eine gesonderte, Meldung an die Leitungsebene erforderlich. Über die Behandlung der Auswirkungen kann jedoch unterhalb der Leitungsebene entschieden werden und es bedarf keiner offiziellen Stellungnahme gegenüber externen Stellen. | Durch die Nicht-Verfügbarkeit einer Leistung erscheint eine Ansehens-/ Vertrauensbeeinträchtigung außerhalb des Ressorts aufgrund der öffentlichen Berichterstattung wahrscheinlich. Eintretende Schäden führen unter Umständen zu politischer/ gesellschaftlicher Verunsicherung bzw. Zweifeln an der amtlichen Zuverlässigkeit und machen daher eine gesonderte, Meldung an die Leitungsebene erforderlich. Über die Behandlung der Auswirkungen kann jedoch unterhalb der Leitungsebene entschieden werden und es bedarf keiner offiziellen Stellungnahme gegenüber externen Stellen. |
| finanzielle Auswirkungen         | Finanzielle Auswirkungen infolge von Konventionalstrafen oder Schäden (inklusive Kosten für deren Behandlung) erscheinen möglich, bewegen sich allerdings in einem Rahmen, der durch Umplanungen in der regulären Planung für das jeweils laufende Haushaltsjahr abgedeckt werden können                                                                                                                                                                                                                                                   | Finanzielle Auswirkungen infolge von Konventionalstrafen oder Schäden (inklusive Kosten für deren Behandlung) erscheinen möglich, bewegen sich allerdings in einem Rahmen, der durch Umplanungen in der regulären Planung für das jeweils laufende Haushaltsjahr abgedeckt werden können.                                                                                                                                                                                                                                                   | Durch die Nicht-Verfügbarkeit einer Leistung erscheinen finanzielle Auswirkungen infolge von Konventionalstrafen, Abweichungen von den vertraglichen vereinbarten SLA oder Schäden (inklusive Kosten für deren Behandlung) möglich, bewegen sich allerdings in einem Rahmen, der durch Umplanungen in der regulären Planung für das jeweils laufende Haushaltsjahr abgedeckt werden können.                                                                                                                                                                                              |

<!-- page: 30 -->

## Schutzbedarfskategorie "sehr hoch"

| Szenario                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integrität                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Verfügbarkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Verstöße gegen Gesetze, Vorschriften oder Verträge | Vertraulichkeit Verstöße erfordern die Behandlung durch eine für Krisensituationen vorgesehene Besondere Aufbauorganisation unter Einbindung relevanter externer Aufsichtsstellen. Die Behandlung erfordert eine dauerhafte Einbindung und mit großer Wahrscheinlichkeit direkte Entscheidungen der Leistungsebene. Eine Einbindung zusätzlicher Expertise (bspw. zu juristischen Fragestellungen) erscheint zwingend erforderlich. Im Falle einer strafrechtlichen Behandlung des Verstoßes sind als Strafmaß eher Bewährungs-/ Freiheitsstrafen anstelle von Geldstrafen wahrscheinlich oder es droht eine Zurückstufung oder Entfernung aus dem Beamtenverhältnis/ Kündigung im TVöD. Die Informationen sind hinsichtlich ihrer Vertraulichkeit als Verschlusssache VS-Vertr. oder höher eingestuft, so dass eine unbefugte Kenntnisnahme für die Interessen der Bundesrepublik Deutschland oder eines ihrer Länder schädlich sein, die Sicherheit der Bundesrepublik Deutschland oder eines ihrer Länder gefährden oder ihren Interessen schweren Schaden zufügen bzw. den Bestand oder lebenswichtige Interessen der Bundesrepublik Deutschland oder eines ihrer Länder | Verstöße erfordern die Behandlung durch eine für Krisensituationen vorgesehene Besondere Aufbauorganisation unter Einbindung relevanter externer Aufsichtsstellen. Die Behandlung erfordert eine dauerhafte Einbindung und mit großer Wahrscheinlichkeit direkte Entscheidungen der Leitungsebene. Eine Einbindung zusätzlicher Expertise (bspw. zu juristischen Fragestellungen) erscheint zwingend erforderlich. Im Falle einer strafrechtlichen Behandlung des Verstoßes sind als Strafmaß eher Bewährungs-/ Freiheitsstrafen anstelle von Geldstrafen wahrscheinlich oder es droht eine Zurückstufung oder Entfernung aus dem Beamtenverhältnis/ Kündigung im TVöD | Verstöße erfordern die Behandlung durch eine für Krisensituationen vorgesehene Besondere Aufbauorganisation unter Einbindung relevanter externer Aufsichtsstellen. Die Behandlung erfordert eine dauerhafte Einbindung und mit großer Wahrscheinlichkeit direkte Entscheidungen der Leitungsebene. Eine Einbindung zusätzlicher Expertise (bspw. zu juristischen Fragestellungen) erscheint zwingend erforderlich. Im Falle einer strafrechtlichen Behandlung des Verstoßes sind als Strafmaß eher Bewährungs-/ Freiheitsstrafen anstelle von Geldstrafen wahrscheinlich oder es droht eine Zurückstufung oder Entfernung aus dem Beamtenverhältnis/ Kündigung im TVöD. Ein Ausfall der IT-Lösung bei weniger als 3h führt bei vorhandenen SLA zu deren Nicht-Einhaltung. |

<!-- page: 31 -->

| Szenario                                                      | Vertraulichkeit                                                                                                                                                                                                                                                                                                                                                                                                             | Integrität                                                                                                                                                                                                                                                                                                                                                                                                                  | Verfügbarkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Beeinträchtigung des informationellen Selbstbestimmungsrechts | Eine Verletzung resultiert mit hoher Wahrscheinlichkeit in einer kontinuierlichen Beeinträchtigung der Betroffenen hinsichtlich ihrer, gesellschaftlichen/ wirtschaftlichen Stellung, der persönlichen Freiheit oder führt zu einer Gefahr für Leib und Leben.                                                                                                                                                              | Eine Verletzung resultiert mit hoher Wahrscheinlichkeit in einer kontinuierlichen Beeinträchtigung der Betroffenen hinsichtlich ihrer, gesellschaftlichen/ wirtschaftlichen Stellung, der persönlichen Freiheit oder führt zu einer Gefahr für Leib und Leben.                                                                                                                                                              | Eine Verletzung resultiert mit hoher Wahrscheinlichkeit in einer kontinuierlichen Beeinträchtigung der Betroffenen hinsichtlich ihrer, gesellschaftlichen/ wirtschaftlichen Stellung, der persönlichen Freiheit oder führt zu einer Gefahr für Leib und Leben.                                                                                                                                                                                                                                                                            |
| Beeinträchtigung der persönlichen Unversehrtheit              | Die Beeinträchtigung der persönlichen Unversehrtheit macht eine ärztliche Behandlung zwingend erforderlich, da gravierende Auswirkungen bis hin zu Todesfolgen wahrscheinlich sind. Schäden können langfristige und nachhaltige Auswirkungen auf das Leben und die Lebensqualität von Personen implizieren (z.B. durch langjährige Behandlungen oder dauerhafte Schädigung der physischen bzw. psychischen Unversehrtheit). | Die Beeinträchtigung der persönlichen Unversehrtheit macht eine ärztliche Behandlung zwingend erforderlich, da gravierende Auswirkungen bis hin zu Todesfolgen wahrscheinlich sind. Schäden können langfristige und nachhaltige Auswirkungen auf das Leben und die Lebensqualität von Personen implizieren (z.B. durch langjährige Behandlungen oder dauerhafte Schädigung der physischen bzw. psychischen Unversehrtheit). | Die Beeinträchtigung der persönlichen Unversehrtheit macht eine ärztliche Behandlung zwingend erforderlich, da gravierende Auswirkungen bis hin zu Todesfolgen wahrscheinlich sind. Bei Nicht-Verfügbarkeit von weniger als 3h ist mitunter mit einer Beeinträchtigung der körperlichen Unversehrtheit zu rechnen. Schäden können langfristige und nachhaltige Auswirkungen auf das Leben und die Lebensqualität von Personen implizieren (z.B. durch langjährige Behandlungen oder dauerhafte Schädigung der physischen bzw. psychischen |
| Beeinträchtigung der Aufgabenerfüllung                        | Die Beeinträchtigung der Aufgabenerfüllung führt zu einem Schaden, der infolge des massiven zusätzlichen Arbeitsaufkommens durch eine für Krisensituationen vorgesehene Besondere Aufbauorganisation unter Einbindung relevanter externer Aufsichtsstellen behandelt werden muss. Die Behandlung erfordert eine dauerhafte Einbindung und mit hoher Wahrscheinlichkeit direkte Entscheidungen der Leitungsebene.            | Die Beeinträchtigung der Aufgabenerfüllung führt zu einem Schaden, der infolge des massiven zusätzlichen Arbeitsaufkommens durch eine für Krisensituationen vorgesehene Besondere Aufbauorganisation unter Einbindung relevanter externer Aufsichtsstellen behandelt werden muss. Die Behandlung erfordert eine dauerhafte Einbindung und mit hoher Wahrscheinlichkeit direkte Entscheidungen der Leitungsebene.            | Unversehrtheit). Die Beeinträchtigung der Aufgabenerfüllung führt vor Ablauf von 3h zu einem Schaden, der infolge des massiven zusätzlichen Arbeitsaufkommens durch eine für Krisensituationen vorgesehene Besondere Aufbauorganisation unter Einbindung relevanter externer Aufsichtsstellen behandelt werden muss. Die Behandlung erfordert eine dauerhafte Einbindung und mit hoher Wahrscheinlichkeit direkte Entscheidungen der Leitungsebene.                                                                                       |

<!-- page: 32 -->

| Szenario                         | Vertraulichkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integrität                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Verfügbarkeit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| negative Innen- und Außenwirkung | Eine dauerhafte Ansehens-/ Vertrauensbeeinträchtigung außerhalb des Ressorts, ggf. sogar auf internationaler Ebene, erscheint aufgrund der umfangreichen öffentlichen Berichterstattung möglich. Eintretende Schäden führen mit hoher Wahrscheinlichkeit zu politischer/ gesellschaftlicher Verunsicherung bzw. Zweifeln an der amtlichen Zuverlässigkeit, so dass es der dauerhaften Einbindung und mit hoher Wahrscheinlichkeit der direkten Entscheidung durch die Leitungsebene wie auch einer offiziellen Stellungnahme gegenüber externen Stellen bedarf. | Eine dauerhafte Ansehens-/ Vertrauensbeeinträchtigung außerhalb des Ressorts, ggf. sogar auf internationaler Ebene, erscheint aufgrund der umfangreichen öffentlichen Berichterstattung möglich. Eintretende Schäden führen mit hoher Wahrscheinlichkeit zu politischer/ gesellschaftlicher Verunsicherung bzw. Zweifeln an der amtlichen Zuverlässigkeit, so dass es der dauerhaften Einbindung und mit hoher Wahrscheinlichkeit der direkten Entscheidung durch die Leitungsebene wie auch einer offiziellen Stellungnahme gegenüber externen Stellen bedarf. | Durch die Nicht-Verfügbarkeit der Leistung bei weniger als 3h erscheint eine dauerhaften Ansehens-/ Vertrauensbeeinträchtigung außerhalb des Ressorts, ggf. sogar auf internationaler Ebene, aufgrund der umfangreichen öffentlichen Berichterstattung möglich. Eintretende Schäden führen mit hoher Wahrscheinlichkeit zu politischer/ gesellschaftlicher Verunsicherung bzw. Zweifeln an der amtlichen Zuverlässigkeit, so dass es der dauerhaften Einbindung und mit hoher Wahrscheinlichkeit der direkten Entscheidung durch die Leitungsebene wie auch einer offiziellen Stellungnahme gegenüber externen Stellen bedarf. |
| finanzielle Auswirkungen         | Finanzielle Auswirkungen infolge von Konventionalstrafen oder Schäden (inklusive Kosten für deren Behandlung) erscheinen möglich, die selbst durch Umplanungen nicht mehr durch die reguläre Planung für das jeweils laufende Haushaltsjahr abgedeckt werden können.                                                                                                                                                                                                                                                                                            | Finanzielle Auswirkungen infolge von Konventionalstrafen oder Schäden (inklusive Kosten für deren Behandlung) erscheinen möglich, die selbst durch Umplanungen nicht mehr durch die reguläre Planung für das jeweils laufende Haushaltsjahr abgedeckt werden können.                                                                                                                                                                                                                                                                                            | Durch die Nicht-Verfügbarkeit der Leistung erscheinen finanzielle Auswirkungen infolge von Konventionalstrafen, Abweichungen von den vertraglichen vereinbarten SLA oder Schäden (inklusive Kosten für deren Behandlung) möglich, die selbst durch Umplanungen nicht mehr durch die reguläre Planung für das jeweils laufende Haushaltsjahr abgedeckt werden können.                                                                                                                                                                                                                                                           |

<!-- page: 33 -->

## Anhang 2: Adressaten der MST-Anforderungen

Hinweis: Die Adressaten einer Anforderung sind mit X markiert

| Anforderungen                                             | Kunden- einrichtung   | Dienstleister   | Projekt- leitungen   | ISB ITKB   | CERT-Bund   |
|-----------------------------------------------------------|-----------------------|-----------------|----------------------|------------|-------------|
| 2.1 Einheitliche Schutzbedarfskategorien                  |                       |                 |                      |            |             |
| ISMS-ITKB.2.1.01                                          |                       |                 | X                    |            |             |
| ISMS-ITKB.2.1.02                                          |                       | X               |                      |            |             |
| ISMS-ITKB.2.1.03                                          | X                     | X               | X                    |            |             |
| ISMS-ITKB.2.1.04                                          | X                     | X               | X                    |            |             |
| 2.2 Kommunikation der Ergebnisse von Sicherheitskonzepten |                       |                 |                      |            |             |
| ISMS-ITKB.2.2.01                                          |                       | X               |                      |            |             |
| ISMS-ITKB.2.2.02                                          |                       | X               |                      |            |             |
| ISMS-ITKB.2.2.03                                          |                       | X               |                      |            |             |
| 2.3 Befugnisse der Dienstleister                          |                       |                 |                      |            |             |
| ISMS-ITKB.2.3.01                                          | X                     | X               |                      |            |             |
| 2.4 Risikomanagement und                                  |                       |                 |                      |            |             |
| Risikotransparenz                                         |                       |                 |                      |            |             |
| ISMS-ITKB.2.4.01                                          | X                     | X               | X                    |            |             |
| ISMS-ITKB.2.4.02                                          | X                     | X               | X                    |            |             |
| ISMS-ITKB.2.4.03                                          | X                     |                 |                      |            |             |
| ISMS-ITKB.2.4.04                                          | X                     | X               | X                    |            |             |
| ISMS-ITKB.2.4.05                                          |                       | X               |                      | X          |             |
| ISMS-ITKB.2.4.06                                          |                       | X               |                      | X          |             |
| 2.5 Prüfungen/Nachweispflichten                           |                       |                 |                      |            |             |
| ISMS-ITKB.2.5.01                                          | X                     | X               | X                    |            |             |
| ISMS-ITKB.2.5.02                                          | X                     | X               | X                    |            |             |
| ISMS-ITKB.2.5.03                                          | X                     | X               | X                    |            |             |
| ISMS-ITKB.2.5.04                                          | X                     | X               | X                    |            |             |
| ISMS-ITKB.2.5.05                                          | X                     | X               | X                    |            |             |
| 2.6 Vorfallmanagement                                     |                       |                 |                      |            |             |
| ISMS-ITKB.2.6.01                                          |                       |                 |                      |            | X           |
| ISMS-ITKB.2.6.02                                          | X                     | X               | X                    |            |             |
| ISMS-ITKB.2.6.03                                          | X                     | X               | X                    |            |             |
| 2.7 Schwachstellenmanagement                              |                       |                 |                      |            |             |
| ISMS-ITKB.2.7.01                                          | X                     | X               | X                    |            | X           |
| 2.8 Schnittstellen im ISMS ITKB                           |                       |                 |                      |            |             |
| ISMS-ITKB.2.8.01                                          | X                     | X               | X                    | X          |             |
| ISMS-ITKB.2.8.02                                          | X                     |                 |                      |            |             |
| ISMS-ITKB.2.8.03                                          |                       | X               |                      |            |             |
| ISMS-ITKB.2.8.04                                          | X                     | X               |                      |            |             |
| 2.9 Leistungsbeziehung in der ITKB                        |                       |                 |                      |            |             |
| ISMS-ITKB.2.9.01                                          | X                     | X               |                      |            |             |
