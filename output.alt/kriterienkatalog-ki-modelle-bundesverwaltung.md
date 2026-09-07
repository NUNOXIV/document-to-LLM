---
source_file: "Kriterienkatalog_KI-Modelle_Bundesverwaltung.pdf"
source_sha256: f7fcc0e47d9d7891b398dc91aef78c4f3b72cf14c41ac19df0eef580d82a07c3
source_bytes: 353317
pages: 16
tables: 2
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T20:25:11+00:00"
text_coverage_percent: 100.0
restored_hyphens: 9
extraction_status: warn
warnings:
  - "9 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): EUVerordnung -> EU-Verordnung, FineTuning -> Fine-Tuning, ITSicherheitsrisiken -> IT-Sicherheitsrisiken, KIModell -> KI-Modell, KIModelle -> KI-Modelle"
  - "Der Textlayer der Quelle enthaelt 21 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

<!-- image -->

Kriterienkatalog des BSI zur Integration von extern bereitgestellten generativen KI-Modellen in eigene Anwendungen

<!-- image -->

<!-- page: 2 -->

## Änderungshistorie

|   Version | Datum      | Name   | Beschreibung         |
|-----------|------------|--------|----------------------|
|       1.0 | 06.06.2025 | T 25   | Erstveröffentlichung |

Tabelle 1: Änderungshistorie

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn E-Mail:  ki-kontakt@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2025

<!-- page: 3 -->

## Inhalt

| 1                                                                                                                                                                                                                | Beschreibung .....................................................................................................................................................................................               | Beschreibung .....................................................................................................................................................................................               |   4 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
|                                                                                                                                                                                                                  | 1.1 Kontaktmöglichkeit für Feedback und Diskussion ................................................................................................                                                              | 1.1 Kontaktmöglichkeit für Feedback und Diskussion ................................................................................................                                                              |   4 |
| 1.2                                                                                                                                                                                                              | Einleitung und Abgrenzung..............................................................................................................................................                                          | Einleitung und Abgrenzung..............................................................................................................................................                                          |   4 |
| 1.3                                                                                                                                                                                                              | Definitionen ............................................................................................................................................................................                        | Definitionen ............................................................................................................................................................................                        |   5 |
| 1.3.1                                                                                                                                                                                                            | 1.3.1                                                                                                                                                                                                            | Beteiligte Stellen ...............................................................................................................................................................                               |   5 |
| 1.3.2                                                                                                                                                                                                            | 1.3.2                                                                                                                                                                                                            | Genutzte Dienste ..............................................................................................................................................................                                  |   6 |
| 1.3.3                                                                                                                                                                                                            | 1.3.3                                                                                                                                                                                                            | Sonstige Begriffe ...............................................................................................................................................................                                |   6 |
| 1.4                                                                                                                                                                                                              | 1.4                                                                                                                                                                                                              | Modalverben ...........................................................................................................................................................................                          |   6 |
| 2                                                                                                                                                                                                                | Sicherheitsanforderungen ...........................................................................................................................................................                             | Sicherheitsanforderungen ...........................................................................................................................................................                             |   8 |
| 2.1                                                                                                                                                                                                              | 2.1                                                                                                                                                                                                              | Globale KI-Governance ......................................................................................................................................................                                     |   8 |
| 2.2                                                                                                                                                                                                              | 2.2                                                                                                                                                                                                              | Anwendungsfallbezogene Planungsphase .................................................................................................................                                                           |   9 |
| 2.3                                                                                                                                                                                                              | 2.3                                                                                                                                                                                                              | Beschaffungsphase .............................................................................................................................................................                                  |  10 |
| 2.4                                                                                                                                                                                                              | 2.4                                                                                                                                                                                                              | Anpassungsphase ................................................................................................................................................................                                 |  11 |
| 2.4.1 Verwendung von System-Prompts ........................................................................................................................                                                     | 2.4.1 Verwendung von System-Prompts ........................................................................................................................                                                     | 2.4.1 Verwendung von System-Prompts ........................................................................................................................                                                     |  11 |
| 2.5                                                                                                                                                                                                              | 2.5                                                                                                                                                                                                              | Integrationsphase ................................................................................................................................................................                               |  11 |
| 2.6                                                                                                                                                                                                              | 2.6                                                                                                                                                                                                              | Einsatzphase ..........................................................................................................................................................................                          |  13 |
| 2.7                                                                                                                                                                                                              | 2.7                                                                                                                                                                                                              | Beendigungsphase ..............................................................................................................................................................                                  |  13 |
| Anhang ......................................................................................................................................................................................................... | Anhang ......................................................................................................................................................................................................... | Anhang ......................................................................................................................................................................................................... |  14 |

<!-- page: 4 -->

## 1 Beschreibung

## 1.1 Kontaktmöglichkeit für Feedback und Diskussion

Zum jetzigen Stand handelt es sich bei diesem Dokument um einen unverbindlichen Kriterienkatalog, der perspektivisch in einen Mindeststandard münden soll. Mit der Veröffentlichung wird das Ziel verfolgt frühzeitig Orientierung zu geben und Feedback zu sammeln.

Besonders erwünscht sind Rückmeldungen von Einrichtungen, die die Vorgaben dieses Kriterienkatalogs praktisch umsetzten. Natürlich sind auch inhaltliche Anmerkungen von anderen Einrichtungen willkommen. Orientieren Sie sich bei Ihrem Feedback z. B. an folgenden Fragen:

- Lassen sich die Vorgaben in praktische Maßnahmen umsetzen? An welchen Stellen gibt es Probleme oder Unklarheiten?
- Sind die Vorgaben zu strikt oder zu frei? Gibt es Stellen an denen Vorgaben fehlen?
- Ist die fachliche Tiefe der Formulierungen angemessen? Können die Maßnahmen mit dem individuell vorliegenden Hintergrundwissen verstanden werden?

- …

Bitte melden Sie sich unter ki-kontakt@bsi.bund.de.

Zudem plant das BSI einen Workshop mit Einrichtungen, die die Vorgaben praktisch umgesetzt haben. Sollten Sie Interesse an einer Teilnahme an diesem Workshop haben, nutzen Sie bitte ebenfalls die oben genannte Kontaktmöglichkeit. Sie erhalten dann zeitnah eine Rückmeldung mit weiteren Details.

## 1.2 Einleitung und Abgrenzung

Generative KI-Modelle 1  haben seit Ende 2022, aufgrund ihrer vielseitigen Einsatzmöglichkeiten in der Generation und Modifikation verschiedener Inhalte, enorm an Bedeutung gewonnen. Insbesondere KI-Modelle, die Texte ver- und bearbeiten sowie erstellen können, stellen eine große Chance für die Digitalisierung der öffentlichen Verwaltung dar. Immer häufiger besteht die Anforderung die Funktionalität eines generativen KI-Modells, das von einem externen Anbieter bereitgestellt wird, über geeignete Schnittstellen in eigene Anwendungen zu integrieren. Allerdings gehen mit der Nutzung generativer KI-Modelle auch Risiken für die IT-Sicherheit einher, die über klassische IT-Sicherheitsrisiken hinausgehen.

Dieser Katalog definiert Kriterien, die aus Sicht des BSI bei der Integration extern bereitgestellter generativer KI-Modelle in eigene Anwendungen in der Bundesverwaltung erfüllt werden sollten, um ein Mindestsicherheitsniveau zu erreichen. Der Kriterienkatalog betrachtet dabei sowohl GovernanceMaßnahmen, als auch technische Kriterien, die sich über den gesamten Lebenszyklus einer solchen Anwendung erstecken. In Teilen bezieht er sich hierbei auf den AI Cloud Service Compliance Criteria Catalogue (AIC4) 2  des BSI. Einzelne spezifische Aspekte generativer KI-Modelle sind dort jedoch, aufgrund der rasanten Entwicklung dieser Technologie über die vergangenen Jahre, nicht ausreichend abgebildet, so dass dieser Katalog hierzu separate Betrachtungen anstellt. Daneben bezieht sich der AIC4 nur auf cloud-basierte KI-Angebote, während dieser Kriterienkatalog auch den lokalen Betrieb eines extern bereitgestellten KI-Modells betrachtet.

Dieser Kriterienkatalog beschränkt sich auf die Regelung der Integration extern bereitgestellter generativer KI-Modelle in eigene Anwendungen. Regelungen, die die reine Nutzung solcher Dienste (ohne eine Integration) betreffen, können teilweise aus diesem Katalog abgeleitet werden, liegen aber außerhalb des Geltungsbereichs.

1  Definitionen siehe nächster Abschnitt

2  https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/AIC4/AI-Cloud-ServiceCompliance-Criteria-Catalogue\_AIC4.pdf?\_\_blob=publicationFile&amp;v=4

<!-- page: 5 -->

Im Fokus steht die Absicht, die Funktionalitäten eines KI-Modells nutzen zu wollen. Ist es für eine Einrichtung nicht ersichtlich, dass in einem Produkt KI-Modelle genutzt werden, so fällt dieses Produkt nicht in den Bereich dieses Kriterienkatalogs. Besteht die begründete Vermutung (z. B. weil dies bei vergleichbaren Produkten der Fall ist), dass in einem Produkt KI-Modelle genutzt werden, so sollte die Einrichtung den Anbieter um Auskunft hierzu bitten.

Bei den extern bereitgestellten generativen KI-Modellen kann es sich um open source, open weight oder proprietäre KI-Modelle handeln. Einrichtungen, die vollständig eigene KI-Modelle für ihre Anwendungen entwickeln möchten, können aus diesem Katalog einzelne Aspekte bzgl. der IT-Sicherheit von KI-Modellen ableiten. Diese Modelle befinden sich aber nicht im Geltungsbereich dieses Kriterienkatalogs. Nicht betrachtet wird zudem die Durchführung eines sogenannten Fine-Tunings extern bereitgestellter KI-Modelle.

Dieser Kriterienkatalog regelt nur die Nutzung im Rahmen eines regulären Betriebs zur Bearbeitung dienstlicher Prozesse. Forschungstätigkeiten, Proof of Concepts und Laborbetrieb sind von den Regelungen explizit nicht betroffen.

Der Kriterienkatalog betrifft sowohl Anwendungen zur Nutzung durch interne Endnutzende , als auch durch externe Endnutzende (z.B. Nutzende eines Chatbots auf der Webseite einer Einrichtung).

Regelungen, die die oben ausgeschlossenen Aspekte wie reine Nutzung eines KI-Modells oder Entwicklung eines eigenen KI-Modells betreffen, werden gegebenenfalls zu einem späteren Zeitpunkt in separaten Katalogen ergänzt.

Die Umsetzung dieses Kriterienkatalogs ersetzt nicht die Einhaltung von Pflichten, die sich aus der EU-Verordnung über künstliche Intelligenz 3  und anderen Vorschriften ergeben.

Für weitere Leitplanken über den IT-sicherheitlichen Aspekt hinaus können die 'Leitlinien für den Einsatz Künstlicher Intelligenz in der Bundesverwaltung' 4  konsultiert werden.

## 1.3 Definitionen

In Anlehnung an die EU-Verordnung über künstliche Intelligenz 5  und die BSI-Veröffentlichung 'Generative KI-Modelle: Chancen und Risiken für Industrie und Behörden' 6  werden in diesem Dokument folgende Begriffe verwendet.

## 1.3.1 Beteiligte Stellen

- 'Anbieter' eine natürliche oder juristische Person, Behörde, Einrichtung oder sonstige Stelle, die ein KI-Modell entwickelt oder entwickeln lässt und es unter ihrem eigenen Namen oder ihrer Handelsmarke in Verkehr bringt
- 'Betreiber' eine juristische Person, Behörde, Einrichtung oder sonstige Stelle, die ein KI-Modell in eigener Verantwortung verwendet, indem sie es Endnutzenden - ggf. in angepasster Form - integriert in eine Anwendung zur Verfügung stellt
- 'Endnutzende' natürliche Personen, die eine Anwendung, die auf einem KI-Modell basiert, verwenden

3  https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=OJ:L\_202401689

4  https://www.bmi.bund.de/SharedDocs/downloads/DE/publikationen/themen/moderneverwaltung/ki/BMI25020-leitlinien-ki-bundesverwaltung.html

5  https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=OJ:L\_202401689

6  https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KI/Generative\_KI-Modelle.html

<!-- page: 6 -->

- 'KI-Zuständige/r' natürliche Person, die durch den Betreiber einer Anwendung, die auf einem KI-Modell basiert, bestimmt wird und im Zuständigkeitsbereich des Betreibers alle KI-Aktivitäten koordiniert (genaue Aufgabenbeschreibung erfolgt unter 2.1)

## 1.3.2 Genutzte Dienste

- 'KI-Modell' Software, die Techniken des maschinellen Lernens 7  nutzt, um eine Eingabe zu verarbeiten und eine Ausgabe zu produzieren, ein KI-Modell kann auch Komponenten beinhalten, die die Eingabe vorbearbeiten oder die Ausgabe nachbearbeiten (z. B. Filter oder Formatierungswerkzeuge)
- 'generatives KI-Modell' ein KI-Modell, das universell einsetzbar ist (engl.: general purpose AI) und eine flexible Generierung von Inhalten ermöglicht. Generative KI-Modelle sind mit einer großen Datenmenge trainiert worden, weisen einen hohen Generalisierungsgrad auf und sind in der Lage, ein breites Spektrum unterschiedlicher Aufgaben kompetent auszuführen. Sie erlernen während ihres Trainings die Datenverteilung der Trainingsdaten. In der Folge generieren sie Inhalte, denen diese Verteilung zugrunde liegt und die sich für eine Vielzahl unterschiedlicher Aufgaben eignen können. In einer Vielzahl von Anwendungsfällen handelt es sich bei den generierten Inhalten um Texte.
- 'extern bereitgestellt' ist ein KI-Modell, wenn ein Betreiber es verwendet, ohne selbst der Anbieter zu sein

## 1.3.3 Sonstige Begriffe

- 'Cloud-Nutzung' die Nutzung eines externen Cloud-Dienstes im Sinne des 'Mindeststandard des BSI zur Nutzung externer Cloud-Dienste'  8  (im Folgenden als 'Mindeststandard Cloud-Nutzung' bezeichnet)
- 'lokaler Betrieb' der Betrieb eines KI-Modells in eigener Verantwortung auf eigener Hardware
- 'Anwendungsfall' ein klar definierter dienstlicher Prozess oder eine Menge solcher Prozesse, die mit Unterstützung einer Anwendung, die auf einem KI-Modell basiert, bearbeitet werden sollen
- 'Integration eines KI-Modells in eigene Anwendungen' die Nutzung der Funktion eines KI-Modells in einer eigenen Anwendung. Dies erfolgt entweder via API-Zugriff, wenn das KI-Modell vom Anbieter cloud-basiert zur Verfügung gestellt wird, oder durch Zugriff auf ein lokal betriebenes KI-Modell.
- 'KI-Risiken' Faktoren, die die Vertraulichkeit, Integrität oder Verfügbarkeit von KI-Modellen oder auf ihnen basierenden Anwendungen gefährden können und nicht in den Bereich klassischer IT-Sicherheitsrisiken fallen 9

## 1.4 Modalverben

In Anlehnung an den IT-Grundschutz werden die Sicherheitsanforderungen mit den Modalverben MUSS und SOLLTE sowie den zugehörigen Verneinungen formuliert. Darüber hinaus wird das Modalverb KANN für ausgewählte Prüfaspekte verwendet. Die hier genutzte Definition basiert auf RFC 2119 und DIN 8202:2018.

## MUSS / DARF NUR

bedeutet, dass diese Anforderung zwingend zu erfüllen ist. Das von der Nichtumsetzung ausgehende Risiko kann im Rahmen einer Risikoanalyse nicht akzeptiert werden.

7  Die Beschränkung auf Techniken des maschinellen Lernens bezieht sich auf dieses Dokument, im Allgemeinen können KI-Modelle auch auf anderen Techniken basieren.

8 https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard\_Nutzun g\_externer\_Cloud-Dienste\_Version\_2\_1.pdf?\_\_blob=publicationFile&amp;v=4

9  eine nicht abschließende Übersicht über KI-Risiken liefert Anhang 1

<!-- page: 7 -->

## DARF NICHT / DARF KEIN

bedeutet, dass etwas zwingend zu unterlassen ist. Das durch die Umsetzung entstehende Risiko kann im Rahmen einer Risikoanalyse nicht akzeptiert werden.

## SOLLTE

bedeutet, dass etwas umzusetzen ist, es sei denn, im Einzelfall sprechen gute Gründe gegen eine Umsetzung. Die Begründung muss dokumentiert und bei einem Audit auf ihre Stichhaltigkeit geprüft werden können.

## SOLLTE NICHT / SOLLTE KEIN

bedeutet, dass etwas zu unterlassen ist, es sei denn, es sprechen gute Gründe für eine Umsetzung. Die Begründung muss dokumentiert und bei einem Audit auf ihre Stichhaltigkeit geprüft werden können.

## KANN

bedeutet, dass die Umsetzung oder Nicht-Umsetzung optional ist und ohne Angabe von Gründen unterbleiben kann.

<!-- page: 8 -->

## 2 Sicherheitsanforderungen

Nachfolgende Sicherheitsanforderungen adressieren die Informationssicherheit entlang des gesamten Lebenszyklus einer Anwendung, die auf einem extern bereitgestellten KI-Modell basiert.

## 2.1 Globale KI-Governance 10

Im Folgenden werden Maßnahmen aufgeführt, die einen geregelten Rahmen für die Governance von KI in der Einrichtung schaffen sollen.

- Die Einrichtung MUSS einer/einem Mitarbeitenden die Rolle der/des KI-Zuständigen zuweisen. Es KANN sich hierbei um die/den IT-Sicherheitsbeauftragte/n handeln.
- Die/der KI-Zuständige hat folgende Aufgaben:
- Sie/er MUSS eine Übersicht aller in der Einrichtung vorhandenen Anwendungen, die auf KI-Modellen basieren, (sofern sie in den Geltungsbereich dieses Kriterienkatalogs fallen) erstellen. In die Übersicht MÜSSEN alle zum Zeitpunkt der Erstellung der Übersicht vorhandenen Anwendungen aufgenommen werden. Anwendungen, die neu eingeführt werden, MÜSSEN ab dem Moment der Nutzung im Normalbetrieb aufgeführt werden.
- Diese Übersicht MUSS die/den jeweilige/n Verantwortliche/n für eine Anwendung enthalten.
- Aus der Übersicht MUSS ersichtlich sein, welche KI-Modelle in welcher Anwendung verwendet werden und für welche Anwendungsfälle die jeweiligen Anwendungen genutzt werden dürfen. (Die Festlegung der erlaubten Anwendungsfälle erfolgt nach dem in 'Anwendungsfallbezogene Planungsphase' und 'Beschaffungsphase' beschriebenen Vorgehen) Es SOLLTE aus der Übersicht ersichtlich sein, welche internen Anpassungen an dem extern bereitgestellten KI-Modell vorgenommen wurden und auf welche internen Informationen es zugreifen kann.
- Die Übersicht MUSS es dem Betreiber ermöglichen, bei Bekanntwerden von Schwachstellen oder sonstigen Risiken ein KI-Modell betreffend, schnell die Betroffenheit feststellen zu können.
- Die Übersicht KANN als Grundlage zur Information der internen Endnutzenden über in der Einrichtung vorhandene Anwendungen, die auf KI-Modellen basieren, genutzt werden.
- Sie/er MUSS Nutzungsbedingungen, die insbesondere Informationen dazu enthalten, welche Daten in eine Anwendung eingegeben werden dürfen, für die in der Übersicht genannten Anwendungen erstellen (lassen) und diese in geeigneter Weise den Endnutzenden zur Verfügung stellen.
- Sie/er SOLLTE einen Prozess zum Schwachstellenmanagement definieren, der regelmäßig und anlassbezogen die Anwendungen auf Schwachstellen prüft und Gegenmaßnahmen entwickelt und umsetzt. Bei der Feststellung und Beurteilung von Schwachstellen und Bedrohungen KÖNNEN aktuelle Veröffentlichungen des BSI unterstützen.
- Sie/er MUSS eine regelmäßige (mindestens jährliche) und anlassbezogene Überprüfung der erlaubten Anwendungsfälle der jeweiligen Anwendungen sowie der Nutzungsbedingungen durchführen und dabei insbesondere neuartige Bedrohungen (und wesentliche Änderungen bei existierenden Bedrohungen) berücksichtigen. Diese Überprüfung KANN Bestandteil des Prozesses zum Schwachstellenmanagement sein.
- Sie/er MUSS sicherstellen, dass alle internen Endnutzenden von Anwendungen, die auf KI-Modellen basieren, eine Schulung/Sensibilisierung zur Erlangung von 'KI-Kompetenz' nachweisen können. Dazu KÖNNEN interne Schulungen angeboten werden.

10  zu einem späteren Zeitpunkt könnte dieser Abschnitt in einen separaten Standard überführt werden

<!-- page: 9 -->

- Sie/er MUSS sicherstellen, dass alle internen Endnutzenden sich mindestens der folgenden Regelungen bewusst sind. Dies KANN über Nutzungsbedingungen und/oder Schulungen realisiert werden.
- Endnutzende SOLLTEN sich mit den Funktionalitäten der Anwendung vertraut machen.
- Endnutzende MÜSSEN darauf achten, dass sensible Daten (z. B. persönliche Daten oder Interna) nur mit der Anwendung verarbeitet werden, wenn dies notwendig und explizit erlaubt ist.
- Die Eingaben Endnutzender in die Anwendung MÜSSEN den erlaubten Zwecken dienen und SOLLTEN präzise und sprachlich korrekt formuliert werden.
- Endnutzende MÜSSEN risikobewusst mit den Ausgaben der Anwendung umgehen. Dies KANN durch die Prüfung und Nachbearbeitung der Ausgaben erfolgen. Weitere Maßnahmen KÖNNEN anwendungsfallbezogen notwendig sein, z. B. in der Ausgabe enthaltene Weblinks nicht anklicken oder der Anwendung keine weiteren Rechte einräumen.
- Wenn es der Anwendungsfall erfordert, SOLLTEN Ausgaben bzw. daraus gewonnene Informationen als KI-generiert gekennzeichnet werden.
- Sie/er MUSS eine Kontaktmöglichkeit für Endnutzende zur Unterstützung bei Fragen und zur Meldung von Problemen bereitstellen.
- Bei Entscheidungen den Datenschutz betreffend MUSS sie/er den behördlichen Datenschutz einbeziehen. Bei Entscheidungen den Geheimschutz betreffend MUSS sie/er den Geheimschutzbeauftragten einbeziehen.
- Bei der Integration von extern bereitgestellten KI-Modellen, die Cloud-basiert zur Verfügung gestellt werden, MÜSSEN alle Kriterien, die im Mindeststandard Cloud-Nutzung unter 'Planungsphase' genannt werden, entsprechend beachtet werden.

## 2.2 Anwendungsfallbezogene Planungsphase

Wenn in einer Einrichtung die Anforderung besteht, zur Bearbeitung eines dienstlichen Prozesses ein extern bereitgestelltes KI-Modell in eigene Anwendungen zu integrieren, müssen in einem ersten Schritt Kriterien für die Auswahl dieses KI-Modells festgelegt werden. Hier geht es insbesondere darum, die Relevanz verschiedener allgemeiner KI-Risiken anwendungsfall-spezifisch zu beurteilen.

- Der Anwendungsfall MUSS klar definiert werden.
- Es MÜSSEN Auswahlkriterien für die Modellauswahl den spezifischen Anwendungsfall betreffend festgelegt werden. Für Kriterien, die sich aus KI-Risiken ergeben, MUSS das folgende Vorgehen genutzt werden:
- In einem ersten Schritt MÜSSEN KI-Risiken identifiziert werden, die für den Anwendungsfall relevant sind. Werden für den Anwendungsfall keine KI-Risiken als relevant identifiziert, MUSS dies begründet werden.
- Anhaltpunkte hierfür KÖNNEN der AIC4 11  oder die AICM 12  liefern. 13
- Außerdem KÖNNEN die in Anhang 1 dargestellten KI-Risiken als Basis für eine Risikoidentifikation genutzt werden.

11  https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/AIC4/AI-Cloud-ServiceCompliance-Criteria-Catalogue\_AIC4.pdf?\_\_blob=publicationFile&amp;v=4

12  Noch nicht veröffentlicht (Link wird später ergänzt)

13  Perspektivisch sollen AIC4 oder AICM Testierungen vorausgesetzt werden, aufgrund der geringen Marktdurchdringung bzw. der Tatsache, dass sich die AICM noch in der Erarbeitung befindet, kann dies aktuell nicht gefordert werden

<!-- page: 10 -->

- Aus jedem KI-Risiko, das als relevant identifiziert wird, SOLLTE mindestens ein Kriterium für die Auswahl des KI-Modells abgeleitet werden. 14
- Die Einrichtung MUSS definieren, welche Kriterien sie als Grundlage für die Bewertung der Vertrauenswürdigkeit eines Anbieters von dem und einer Quelle aus der ein KI-Modell bezogen wird heranzieht. 15
- Es MUSS festgelegt werden, welche der oben definierten Kriterien als optional und welche als obligatorisch angesehen werden.

## 2.3 Beschaffungsphase

Ziel des Beschaffungsprozesses, für den die Vorgaben des Vergaberechts einschlägig sind, ist die Auswahl und der Bezug eines geeigneten KI-Modells.

- Ein KI-Modell, das für die Integration in Frage kommt, MUSS anhand der in der 'Anwendungsfallbezogenen Planungsphase' beschriebenen Kriterien beurteilt werden.
- Für identifizierte KI-Risiken KANN 16  ein AIC4 oder AICM Testat als Nachweis für eine ausreichende Sicherheit in Standardfällen verwendet werden, das Testat MUSS ausgewertet werden und es MUSS beurteilt werden, ob dies anwendungsfallbezogen ausreichend ist.
- Als Grundlage für die Beurteilung SOLLTEN Informationen des Anbieters (z. B. Nutzungsbedingungen, Model-Cards, Informationen zu durchgeführten Benchmark-Tests) gesichtet werden. Zusätzlich KÖNNEN Informationen Dritter zur Beurteilung genutzt werden.
- Ebenso KÖNNEN eigene Tests z. B. anhand von Benchmarks oder in Form eines Red Teamings durchgeführt werden.
- Die Auswahl eines KI-Modells MUSS anhand der festgelegten Kriterien begründet werden.
- Der Anbieter des KI-Modells SOLLTE zusichern, dass von einer nutzenden Person bereitgestellte Informationen (sowohl 'Profilinformationen' als auch Eingaben) nicht für Zwecke außerhalb der Nutzung des Modells durch diese Person verwendet werden, insbesondere nicht zur Weiterentwicklung von öffentlich zur Verfügung gestellten KI-Modellen.
- Der Bezug des KI-Modells MUSS aus vertrauenswürdigen Quellen erfolgen, falls vorhanden SOLLTEN Signaturen geprüft werden. Es SOLLTEN sichere Formate 17  genutzt werden.
- Bei Verwendung eines cloud-basierten KI-Modells KANN 18  ein AIC4 oder AICM Testat, welches geprüft wurde, als Nachweis der Vertrauenswürdigkeit der Quelle genutzt werden.

14  Beispiel: Die Anwendung, die betrachtet wird, soll Anträge von Dritten verarbeiten. Deshalb wird das Risiko von Indirect Prompt Injections als relevant identifiziert. Daraus leitet die Einrichtung folgendes Auswahlkriterium ab: 'Das KI-Modell, das in unserer Anwendung verwendet wird, sollte eine Härtung gegenüber manipulativen Eingaben Dritter aufweisen.' Das Kriterium wird von der Einrichtung als optional eingestuft, weil sie alternative Maßnahmen gegen Indirect Prompt Injections durch Prozessabläufe realisieren kann.

15  als Anhaltspunkt kann z. B. gesagt werden, dass ein direkt von einem bekannten Anbieter bereitgestelltes Modell auf gängigen Plattformen oder der Webseite des Anbieters eher als unproblematisch eingestuft werden kann; wohingegen ein von einem unbekannten Programmierenden bereitgestelltes leicht abgewandeltes Modell eher nicht auf eine vertrauenswürdige Quelle hindeutet

16  vgl. oben, perspektivisch sollen AIC4 oder AICM Testierungen vorausgesetzt werden, aufgrund der geringen Marktdurchdringung bzw. der Tatsache, dass sich die AICM noch in der Erarbeitung befindet, kann dies aktuell nicht gefordert werden

17  als nicht sicher gilt beispielsweise das Pickle-Format

18  vgl. oben, perspektivisch sollen AIC4 oder AICM Testierungen vorausgesetzt werden, aufgrund der geringen Marktdurchdringung bzw. der Tatsache, dass sich die AICM noch in der Erarbeitung befindet, kann dies aktuell nicht gefordert werden

<!-- page: 11 -->

- Bei der Integration von KI-Modellen, die Cloud-basiert zur Verfügung gestellt werden, MÜSSEN alle Kriterien, die im Mindeststandard Cloud-Nutzung unter 'Beschaffungsphase' genannt werden, entsprechend beachtet werden.
- Wenn ein KI-Modell lokal betrieben wird, MÜSSEN klassische IT-Sicherheitsmaßnahmen, z. B. wie sie in den Grundschutz Bausteinen 'OPS.1.1.6 Software-Tests und -Freigaben' 19  und 'APP.6 Allgemeine Software' 20  gefordert werden, ergriffen werden.

## 2.4 Anpassungsphase

In vielen Anwendungsfällen ist es möglich die Funktionsweise eines KI-Modells zu erweitern bzw. zu verbessern oder KI-Risiken zu mindern, indem man es mit zusätzlichen Komponenten verknüpft oder Anpassung am Modell vornimmt - z. B. durch die Verwendung sogenannter System-Prompts. Hierbei handelt es sich um textuelle Anweisungen, die jeder Eingabe von Endnutzenden vorangestellt werden und somit jede Ausgabe des KI-Modells beeinflussen. Zusätzliche Komponenten sind z. B. Datenbanken, Bibliotheken oder Werkzeuge. 21  Anpassungen sind optional, werden keine Anpassungen vorgenommen, kann diese Phase übersprungen werden.

- Bezüglich des Bezugs aller weiteren Komponenten (z.B. Bibliotheken, Werkzeuge, externe Datenbanken) MÜSSEN klassische IT-Sicherheitsmaßnahmen, z. B. wie sie in den Grundschutz Bausteinen 'OPS.1.1.6 Software-Tests und -Freigaben' 22  und 'APP.6 Allgemeine Software' 23  gefordert werden, ergriffen werden.

## 2.4.1 Verwendung von System-Prompts

- Wenn System-Prompts verwendet werden, SOLLTEN sie an zentraler Stelle (z. B. als Anhang der vom KI-Zuständigen geführten Übersicht) verwaltet werden und Änderungen nachverfolgbar sein, damit nachvollziehbar ist, welche KI-Risiken mittels System-Prompts mitigiert werden sollen.
- In System-Prompts DÜRFEN KEINE sensiblen Daten integriert werden.
- Es MUSS bei den Personen, die die Anpassungen durchführen, ein Bewusstsein für die Möglichkeit der Umgehung von System-Prompts (sog. Prompt Injections) vorliegen, damit beurteilt werden kann, ob die Verwendung von System-Prompts für die beabsichtigte Funktionserweiterung, die durch die Anpassung erreicht werden soll, geeignet bzw. ausreichend ist.
- System-Prompts SOLLTEN NICHT zur Umsetzung eines Rechte-/Rollensystems genutzt werden.

## 2.5 Integrationsphase

Ziel der Integrationsphase ist es, sichere Schnittstellen zwischen internen IT-Komponenten und dem extern bereitgestellten KI-Modell zu schaffen.

19  https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium\_Einzel\_PDFs\_2023/04\_OPS\_Betrieb/OPS\_1\_1\_6\_Software\_Tests\_und\_Freigaben\_Edition\_2 023.pdf?\_\_blob=publicationFile&amp;v=3#download=1

20  https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium\_Einzel\_PDFs\_2023/06\_APP\_Anwendungen/APP\_6\_Allgemeine\_Software\_Edition\_2023.p df?\_\_blob=publicationFile&amp;v=3#download=1

21  Dieser Kriterienkatalog betrachtet nicht den Fall, dass innerhalb der Einrichtung ein 'eigenes' Fine-Tuning des extern bereitgestellten KI-Modells erfolgt.

22  https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium\_Einzel\_PDFs\_2023/04\_OPS\_Betrieb/OPS\_1\_1\_6\_Software\_Tests\_und\_Freigaben\_Edition\_2 023.pdf?\_\_blob=publicationFile&amp;v=3#download=1

23  https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium\_Einzel\_PDFs\_2023/06\_APP\_Anwendungen/APP\_6\_Allgemeine\_Software\_Edition\_2023.p df?\_\_blob=publicationFile&amp;v=3#download=1

<!-- page: 12 -->

- Die Anwendung, die auf dem KI-Modell basiert, MUSS vollständig in das ISMS der Einrichtung integriert werden.
- Es SOLLTE ein Threat Modelling nach folgendem Vorgehen durchgeführt werden. Dies dient der Identifikation von Aspekten, die die Integration betreffen und die Sicherheit der Anwendung beeinträchtigen können. 24  Als Anhaltspunkt KÖNNEN die KI-Risiken aus Anhang 1 verwendet werden.
- Der Weg einer Information, die in die Anwendung eingegeben werden soll, wird in seiner Gesamtheit nachvollzogen.
- Es wird identifiziert, welche Urheber von Informationen es gibt (z.B. Endnutzende, Antragstellende, Autoren von Webseiten, Komponenten der Anwendung).
- Es werden Stellen identifiziert, an denen Manipulationen an den Informationen vorgenommen werden können.
- Es wird nachvollzogen, welche Aktionen eine Information innerhalb der Anwendung auslösen soll und welche Aktionen sie fälschlicherweise auslösen könnte. Dabei werden auch 'Kettenreaktionen' betrachtet, wenn beispielsweise eine Komponente der Anwendung Aktionen einer anderen Komponente auslösen kann.
- Ebenso werden Aktionen betrachtet, die außerhalb der Anwendung ausgelöst werden können (z. B. die Ausführung von Code, das Abfließen von Informationen).
- Es wird nachvollzogen, ob Aktionen ausgelöst werden können, die eine Reaktion des Endnutzende provozieren können (z. B. die Ausgabe eines Links, den der Endnutzende anklickt).
- Basierend auf dem zuvor durchgeführten Threat Modelling SOLLTEN Maßnahmen zur Absicherung der Integration ergriffen werden. Hierbei KANN es sich z. B. um folgende Maßnahmen handeln:
- Authentisierung und Autorisierung aller Komponenten der Anwendung
- Umsetzung eines eindeutigen Rechte- und Rollenkonzepts
- Anwendung des Least Privilege Principle
- Maßnahmen zur Validierung und ggf. Änderung oder Ablehnung von Input und Output, auch zwischen Komponenten
- Durchführung von Aktionen in Sandbox-Umgebungen
- Einschränkung der Rechte der Anwendung bestimmte Aktionen durchzuführen
- Maßnahmen des Monitoring, des Logging und der automatisierten Reaktion auf Sicherheitsvorfälle
- Nach Abschluss der Integration MÜSSEN Tests durchgeführt werden. Diese überprüfen die Anwendung anwendungsfallbezogen hinsichtlich der in der 'Anwendungsfallbezogenen Planungsphase' und der im Threat Modelling der 'Integrationsphase' als relevant identifizierten (KI-)Risiken.
- Die Ergebnisse der Tests MÜSSEN dokumentiert werden. Aus der Dokumentation MUSS für interne Zwecke zu einem späteren Zeitpunkt ersichtlich sein, ob bei Auftreten neuartige Bedrohungen oder relevante Änderungen bestehender Bedrohungen erneut getestet werden muss oder ob die bereits durchgeführten Tests ausreichend sind.
- Bei nicht zufriedenstellenden Testergebnissen MÜSSEN einzelne der vorherigen Phasen (Beschaffungs-, Anpassungs-, Integrationsphase) - je nach Optionen für eine Risikomitigation - wiederholt werden.

24  im Gegensatz zu den in der 2.2 identifizierten KI-Risiken geht es hier allein um Risiken, die aus der Integration entstehen, während die dort beschriebenen KI-Risiken sich auf die generelle Funktion des KI-Modells beziehen

<!-- page: 13 -->

## 2.6 Einsatzphase

Die Anforderungen an den Einsatz regeln, welche organisatorischen und sicherheitstechnischen Maßnahmen im Betrieb beachtet werden müssen.

- Bei der Integration von KI-Modellen, die Cloud-basiert zur Verfügung gestellt werden, MÜSSEN alle Kriterien, die im Mindeststandard Cloud-Nutzung unter 'Einsatzphase' genannt werden, entsprechend beachtet werden.
- Die Einrichtung MUSS für Endnutzende ersichtlich machen, dass eine Anwendung KI-Komponenten verwendet.
- Die Einrichtung MUSS Maßnahmen zur Verhinderung missbräuchlicher Nutzung der Anwendung umsetzen. Dazu können entweder organisatorische (z. B. Regelung in den Nutzungsbedingungen) oder technische Maßnahmen umgesetzt werden.
- Die Einrichtung SOLLTE (insbesondere bei externer Nutzung) den Zugriff auf die Anwendung auf das notwendige Minimum beschränken.
- Die Einrichtung SOLLTE wichtige Regelungen der Nutzungsbedingungen (z. B. wofür und in welcher Form Ausgaben verwendet werden dürfen) an auffälliger Position in der Anwendung darstellen, um Endnutzende an die Regelungen zu erinnern.
- Die Einrichtung SOLLTE anwendungsspezifische Schulungen anbieten.

## 2.7 Beendigungsphase

Anforderungen an die Beendigung adressieren die geordnete Beendigung der Nutzung der Anwendung, die auf einem extern bereitgestellten KI-Modell basiert.

- Bei der Integration von KI-Modellen, die Cloud-basiert zur Verfügung gestellt werden, MÜSSEN alle Kriterien, die im Mindeststandard Cloud-Nutzung unter 'Beendigungsphase' genannt werden, entsprechend beachtet werden.
- Wenn eine Anwendung nicht mehr für den bisherigen Anwendungsfall genutzt wird, MUSS sichergestellt werden, dass den Anwendungsfall betreffende sensible Daten aus der Anwendung entfernt werden, bevor sie für einen anderen Anwendungsfall verwendet wird (z. B. Löschung von verknüpften Datenbanken mit sensiblen Informationen).

<!-- page: 14 -->

## Anhang

## Anhang 1: KI-Risiken

Im Folgenden werden einige häufig auftretende Risiken generativer KI-Modelle dargestellt, sowie Anhaltspunkte für die Beurteilung der anwendungsfallbezogenen Relevanz als Hilfsmittel zur Verfügung gestellt. Zudem werden ausgewählte Gegenmaßnahmen präsentiert, dies soll insbesondere dabei unterstützen, zu beurteilen, an welcher Stelle im Lebenszyklus Gegenmaßnahmen ergriffen werden können und welche Instanzen (z. B. Anbieter, Betreiber, Endnutzende) diese ergreifen können.

Diese Auflistung von Risiken und Gegenmaßnahmen erhebt keinen Anspruch auf Vollständigkeit, insbesondere können aufgrund der rasanten Entwicklungen im Bereich generative KI laufend neue Bedrohungen auftreten. Sie soll lediglich ein Hilfsmittel darstellen.

Für eine detailliertere Beschreibung von Risiken und Gegenmaßnahmen generativer KI-Modelle verweisen wir auf die BSI-Veröffentlichung 'Generative KI-Modelle: Chancen und Risiken für Industrie und Behörden' 25 .

- Fehlende Robustheit : KI-Modelle haben häufig Probleme damit, Eingaben wie vom Endnutzenden intendiert zu bearbeiten, wenn die Eingabe stark von den Trainingsdaten abweicht oder (absichtlich wie unabsichtlich) 'unscharf' ist (z.B. ein verrauschtes Bild oder ein Text mit vielen Rechtschreibfehlern oder uneindeutigen Formulierungen). In diesen Fällen kann es zu fehlerhaften und ggf. auch problematischen Ausgaben kommen.
- Die Wahrscheinlichkeit, dass solche Eingaben an ein KI-Modell getätigt werden, hängt i.d.R. von der Gruppe der Endnutzenden und der Art der eingegebenen Informationen ab.
- Wichtig ist, zu bewerten, wie kritisch fehlerhafte Ausgaben sich auswirken (werden Ausgaben z. B. ungesehen weiterverwendet).
- Maßnahmen zur Steigerung der Robustheit werden in der Regel während des Trainings des KI-Modells ergriffen, daneben ist die Sensibilisierung der Endnutzenden eine effektive Gegenmaßnahme.
- Fehlende Qualität der Ausgabe :  Auch robuste KI-Modelle weisen Mängel in der Qualität ihrer Ausgaben auf, diese können etwa faktisch falsch, diskriminierend, anders problematisch (z. B. vulgär) oder unsicher (wenn es sich um Programmcode handelt) sein.
- Wichtig ist, zu bewerten, wie kritisch fehlerhafte Ausgaben sich auswirken (werden Ausgaben z.B. ungesehen weiterverwendet).
- Maßnahmen zur Erhöhung der Qualität können während des gesamten Lebenszyklus ergriffen werden: Verbesserung der Trainingsdaten, Verwendung von System-Prompts, einem KI-Modell Zugriff auf Datenbanken geben, damit es fundiertere Ausgaben tätigen kann, Verwendung von Ausgabe-Filtern, präzises Prompting, manuelle Nachbearbeitung/Prüfung der Ausgabe, …
- Risiko der missbräuchlichen Nutzung : Endnutzende mit böswilligen Absichten können KI-Modelle für ihre Zwecke missbrauchen, z. B. um Falschnachrichten zu erzeugen oder zu untermauern oder Cyberangriffe durchzuführen. Selbst wenn Sicherheitsmaßnahmen etabliert sind, ist es häufig möglich diese durch geschicktes Formulieren der Eingabe zu umgehen (sog. Evasion Attacks).
- Wichtig ist zu bewerten, wie hoch das Risiko ist, dass Endnutzende böswillige Absichten haben (gibt es z. B. nur einen eingeschränkten Nutzerkreis oder können auch Externe die Anwendung nutzen) und wie hoch der Schaden für die Einrichtung ist, der durch eine missbräuchliche Nutzung entstehen kann (z. B. Rufschädigung, rechtliche Konsequenzen).

25  https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KI/Generative\_KI-Modelle.html

<!-- page: 15 -->

- Zur Verhinderung missbräuchlicher Nutzung können sowohl organisatorische (z. B. Einschränkung der Zugangsmöglichkeiten zur Anwendung, Veröffentlichung von Nutzungsbedingungen) als auch technische Maßnahmen (z. B. Filterung von Ein- und Ausgaben, adversariales Training, Verwendung von System-Prompts) ergriffen werden.
- Manipulation der Funktionsweise im Betrieb durch Dritte (sog. Indirect Prompt Injections): Werden mit einer Anwendung, die auf einem KI-Modell basiert, Informationen verarbeitet, die von Dritten (sprich nicht von Endnutzenden selber) zur Verfügung gestellt wurden, so können diese Informationen fälschlicherweise als Anweisung an das KI-Modell interpretiert werden. Sie können so zu Ausgaben führen, die vom Endnutzenden nicht beabsichtigt sind. Personen können solche Anweisungen absichtlich in Informationen, von denen sie wissen, dass sie mit KI verarbeitet werden, platzieren, um die Bearbeitung zu ihren Gunsten zu beeinflussen (z.B. kann bei einer Prüfung auf Kreditwürdigkeit in den eingereichten Informationen die Aufforderung versteckt werden, dem Antrag auf jeden Fall stattzugeben).
- Dieses Risiko besteht immer, wenn Informationen aus anderen Quellen (z. B. Dokumente, Webseiten, E-Mails) mit Sprachmodellen verarbeitet werden.
- Die Auswirkungen können umso größer sein, je mehr Rechte eine Anwendung hat selbstständig Aktionen durchzuführen (z. B. E-Mails versenden oder Daten abspeichern).
- Technisch lässt sich das Problem nur schwer eingrenzen, da ein KI-Modell im Wesentlichen in seiner vorgesehenen Funktion agiert, wichtig ist daher die möglichen Konsequenzen einer Manipulation zu kontrollieren (z. B. manuelle Prüfung/Nachbearbeitung der Ausgabe, einer Anwendung nur notwendige Rechte einräumen).
- Manipulation der Anwendung außerhalb des Betriebs (sog. Poisoning Attacks): Angreifende können eine Anwendung, die auf einem KI-Modell basiert, außerhalb des Betriebs - i.d.R. während der Entwicklungsphase - manipulieren und so z. B. Hintertüren einbauen, die während des Betriebs ausgenutzt werden können. Manipulationen sind an allen Komponenten denkbar wie Trainingsdaten, dem KI-Modell selbst, System-Prompts oder vorgeschalteten Bearbeitungstools. Konsequenzen können z.B. eine Leistungsverschlechterung oder die Möglichkeit der Ausnutzung für missbräuchliche Zwecke während des Betriebs sein.
- Wichtig für die Beurteilung der Relevanz dieses Risikos, ist es die möglichen Konsequenzen einer Manipulation zu betrachten.
- Bei extern bereitgestellten KI-Modellen oder Komponenten (z. B. Trainingsdatensätzen) sollte auf eine Herkunft aus vertrauenswürdigen Quellen und das Vorliegen eines sicheren Dateiformats geachtet werden. Zudem können Informationen vom Anbieter eingeholt werden, welche Maßnahmen dieser ergriffen hat, um Manipulationen durch Dritte zu verhindern.
- Abfluss sensibler Daten : Alle Daten, die zur Funktion einer Anwendung, die auf einem KI-Modell basiert, beitragen, sind potenziell gefährdet an Unberechtigte abzufließen, also z. B. Trainingsdaten, Eingaben, Ausgaben, Modellspezifikationen oder Spezifikationen über sonstige Komponenten. Ein Abfluss kann einerseits durch Zufall an Endnutzende der Anwendung erfolgen, z. B. wenn Endnutzende in ihrer Eingabe um die Imitation des Schreibstils eines bestimmten Künstlers bitten und das Modell Daten aus seinen Trainingsdaten wortwörtlich wiedergibt. Andererseits können Angreifende bewusst versuchen die genannten Daten durch geschickte Formulierungen der Eingabe zu erlangen (sog. Privacy Attacks). Zudem haben die Anbieter und Betreiber von KI-Modellen potenziell Zugriff auf bestimmte Daten der Endnutzenden und behalten sich teilweise das Recht vor diese z. B. zum weiteren Training ihrer KI-Modelle zu nutzen.
- Es sollte klar geregelt werden, welche Informationen Endnutzende als Eingabe für welche Anwendungen verwenden dürfen. Besonders relevant ist dies für persönliche Daten, Interna und eingestufte Informationen!

<!-- page: 16 -->

- Wichtig ist es, sich zu informieren, welche Rechte sich der Anbieter eines KI-Modells einräumt (siehe z. B. Nutzungsbedingungen), ggf. gibt es verschiedene Versionen (z. B. kostenlos vs. kostenpflichtig), die sich hierin unterscheiden oder man kann der Verwendung durch eine Änderung der Einstellungen widersprechen.
- Als Grundsatz muss gelten: Dienstliche Informationen dürfen von externen Stellen nicht verwendet werden!
- Bei selbstentwickelten Komponenten von Anwendungen ist es wichtig sicherzustellen, dass schützenswerte Daten (z. B. sensible Daten in einer Datenbank) vor dem direkten und indirekten Zugriff durch Unberechtigte geschützt sind. Hierbei helfen klassische IT-Sicherheitsmaßnahmen, aber auch spezielle Maßnahmen, wie das Filtern von Ein- und Ausgaben oder, wenn möglich, Maßnahmen zur Anonymisierung.
