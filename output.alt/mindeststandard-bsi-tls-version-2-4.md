---
source_file: "Mindeststandard_BSI_TLS_Version_2_4.pdf"
source_sha256: 9aec6a3209f3214546baa98be986047f4d00197e4b89b235fcf7e8b3dd44c767
source_bytes: 418887
pages: 11
tables: 2
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T20:29:31+00:00"
text_coverage_percent: 100.0
appended_source_lines: 2
restored_hyphens: 2
extraction_status: warn
warnings:
  - "2 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): 021022 -> 02102-2, ITGrundschutz -> IT-Grundschutz"
  - "Der Textlayer der Quelle enthaelt 2 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
  - "2 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

<!-- image -->

## Mindeststandard des BSI zur Verwendung von Transport Layer Security

nach § 8 Absatz 1 Satz 1 BSIG - Version 2.4 vom 25 .0 5 . 2 023

<!-- image -->

<!-- page: 2 -->

## Änderungshistorie

|   Version | Datum         | Beschreibung                                      |
|-----------|---------------|---------------------------------------------------|
|       1.5 | 21.11.2014    | Erstveröffentlichung                              |
|       2.0 | 05.04.2019    | Major Release - umfassende Überarbeitung          |
|       2.1 | 09.04.2020    | Minor Release - Anpassungen und Konkretisierungen |
|       2.2 | 03.05.2021    | Minor Release - Anpassungen und Konkretisierungen |
|       2.3 | 15.03.2022    | Minor Release - Anpassungen und Konkretisierungen |
|       2.4 | 25 .0 5 .2023 | Minor Release - Anpassungen und Konkretisierungen |

Tabelle 1: Versionsgeschichte des Mindeststandards. Eine ausführliche Änderungsübersicht zum Mindeststandard erhalten Sie unter: https://www.bsi.bund.de/dok/MST-TLS-Log

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn

Internet: https://www.bsi.bund.de

© Bundesamt für Sicherheit in der Informationstechnik 2023

<!-- page: 3 -->

## Vorwort

Risiken für die Cyber- und Informationssicherheit sind nicht zuletzt aufgrund der zunehmenden Komplexität und Vernetzung von IT-Systemen allgegenwärtig. Dadurch betreffen potenzielle Schwachstellen und Cyber-Angriffe in der Regel nicht nur einzelne Stellen.

Umso wichtiger ist die Vorgabe verbindlicher Sicherheitsanforderungen an die Informationstechnik des Bundes. So kann ein einheitliches Mindestsicherheitsniveau mit effektiven Maßnahmen zur Abwehr von Cyber-Angriffen innerhalb der heterogenen Behördenlandschaft etabliert werden.

Dazu legt das Bundesamt für Sicherheit in der Informationstechnik (BSI) Mindeststandards (MST) für die Sicherheit der Informationstechnik des Bundes 1  fest. Dies erfolgt auf der Grundlage des § 8 Absatz 1 BSIG im Benehmen mit den Ressorts. Als gesetzliche Vorgabe definieren Mindeststandards somit ein verbindliches Mindestniveau für die Informationssicherheit.

Bereits 2017 hat das Bundeskabinett mit dem Umsetzungsplan Bund 2017 (UP Bund 2017) 2  eine Leitlinie für Informationssicherheit in der Bundesverwaltung in Kraft gesetzt. Damit wurde die Beachtung der Mindeststandards für den Bereich der Stellen des Bundes verbindlich. Durch das IT-Sicherheitsgesetz 2.0 wurde die Einhaltung der Mindeststandards des BSI auch gesetzlich geregelt. Die Umsetzungspflicht der Mindeststandards ergibt sich aus dem dadurch neu gefassten § 8 BSIG.

Die Mindeststandards richten sich primär an IT-Verantwortliche, IT-Sicherheitsbeauftragte (IT-SiBe), Informationssicherheitsbeauftragte (ISB), IT-Betriebspersonal und Beschaffungsstellen. Die Gesamtverantwortung für die Informationssicherheit und damit auch für die Einhaltung der Mindeststandards trägt gemäß UP Bund 2017 die Leitung der jeweiligen Einrichtung 1 .

IT-Systeme sind in der Regel komplex und in ihren individuellen Anwendungsbereichen durch die unterschiedlichsten (zusätzlichen) Rahmenbedingungen und Anforderungen gekennzeichnet. Daher können sich in der Praxis regelmäßig höhere Anforderungen an die Informationssicherheit ergeben, als sie in den Mindeststandards beschrieben werden. Aufbauend auf dem Mindestsicherheitsniveau sind diese individuellen Anforderungen in der Planung, der Etablierung und im Betrieb der IT-Systeme zusätzlich zu berücksichtigen, um dem jeweiligen Bedarf an Informationssicherheit zu genügen. Die Vorgehensweise dazu beschreiben die IT-Grundschutz-Standards des BSI.

Zur Sicherstellung der Effektivität und Effizienz in der Erstellung und Betreuung von Mindeststandards arbeitet das BSI nach einer standardisierten Vorgehensweise. Zur Qualitätssicherung durchläuft jeder Mindeststandard mehrere Prüfzyklen einschließlich des Konsultationsverfahrens mit der Bundesverwaltung. 3  Über die Beteiligung bei der Erarbeitung von Mindeststandards hinaus kann sich jede Einrichtung auch bei der Erschließung fachlicher Themenfelder für neue Mindeststandards einbringen oder im Hinblick auf Änderungsbedarf für bestehende Mindeststandards Kontakt mit dem BSI aufnehmen. Einhergehend mit der Erarbeitung von Mindeststandards berät das BSI die Einrichtungen auf Ersuchen bei der Umsetzung und Einhaltung der Mindeststandards.

1  Die von den Mindeststandards adressierten Stellen werden in § 8 Absatz 1 BSI-Gesetz (BSIG) definiert (siehe https://www.gesetze-im-internet.de/bsig\_2009/\_\_8.html). Zur besseren Lesbarkeit wird im weiteren Verlauf für alle dort genannten Stellen der Begriff 'Einrichtung' verwendet.

2  Vgl. UP Bund (BMI 2017)

[3  Siehe FAQ zu den MST: https://www.bsi.bund.de/dok/MST-FAQ](https://www.bsi.bund.de/dok/MST-FAQ)

<!-- page: 4 -->

## Inhalt

| 1                                                                                                                                                                                                         | Beschreibung .......................................................................................................................................................................................... 5   |   Beschreibung .......................................................................................................................................................................................... 5 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1                                                                                                                                                                                                       | Einleitung und Abgrenzung ..................................................................................................................................................                                |                                                                                                                                                                                                           5 |
| 1.2                                                                                                                                                                                                       | Modalverben ................................................................................................................................................................................                |                                                                                                                                                                                                           6 |
| 2                                                                                                                                                                                                         | Sicherheitsanforderungen ................................................................................................................................................................                   |                                                                                                                                                                                                           7 |
| Literaturverzeichnis..................................................................................................................................................................................... | Literaturverzeichnis.....................................................................................................................................................................................   |                                                                                                                                                                                                          10 |
| Abkürzungsverzeichnis ..............................................................................................................................................................................      | Abkürzungsverzeichnis ..............................................................................................................................................................................        |                                                                                                                                                                                                          11 |

<!-- page: 5 -->

## 1 Beschreibung

Im Rahmen der stetig zunehmenden Digitalisierung und der damit verbundenen Übertragung von Informationen über Kommunikationsnetze ist es eine zwingende Notwendigkeit, Informationen während der Übertragung abzusichern, um die Schutzziele Vertraulichkeit, Authentizität und Integrität gewährleisten zu können. Eine zuverlässige Absicherung der Übertragung in Netzen kann durch den Einsatz des Protokolls Transport Layer Security (TLS) erreicht werden. Dieser Mindeststandard stellt konkrete Anforderungen an die sichere Verwendung und Konfiguration von TLS.

## 1.1 Einleitung und Abgrenzung

TLS wird verwendet, um Informationen während der Übertragung in Netzen kryptographisch durch Etablierung eines sicheren Kanals (verschlüsselt, authentisiert und integritätsgeschützt) abzusichern. So können Daten aus höheren Schichten des OSI-Referenzmodells 4  sicher über TCP/IP-basierte Verbindungen übertragen werden (z.B. HTTPS, FTPS, IMAPS, LDAPS). Es existieren jedoch unterschiedliche Versionen von TLS, wobei nicht jede Version heute als sicher eingestuft werden kann. Daher ist es wichtig, die geeignete Version in der richtigen Konfiguration einzusetzen, um die oben genannten Schutzziele zu erreichen.

Der Mindeststandard zur Verwendung von Transport Layer Security fordert nicht, dass TLS zur kryptographischen Absicherung von Informationen während der Übertragung in Netzen verwendet werden muss. Unter der Voraussetzung, dass keine Einschränkungen für das angestrebte Sicherheitsniveau entstehen, können auch andere Protokolle und/oder Verfahren zur Transportverschlüsselung verwendet werden.

Sobald TLS verwendet wird, müssen die in Kapitel 2 dieses Mindeststandards beschriebenen Sicherheitsanforderungen beachtet und umgesetzt werden.

Der Mindeststandard setzt die IT-Grundschutz-Vorgehensweise des BSI zum Management der Informationssicherheit voraus. 5  Er gilt für alle Schutzbedarfskategorien.

Die Erfüllung der im Mindeststandard vorgegebenen Sicherheitsanforderungen ist für ein angemessenes Sicherheitsniveau notwendig, aber in der Regel nicht hinreichend. Unter Berücksichtigung des individuellen Schutzbedarfs muss die Prüfung sowie gegebenenfalls die Festlegung und Umsetzung eventuell zusätzlich erforderlicher Sicherheitsmaßnahmen erfolgen.

4  Vgl. Basic Reference Model (ISO/IEC, 1994)

5  Vgl. BSI-Standard 200-2 (BSI 2017a)

<!-- page: 6 -->

## 1.2 Modalverben

In Anlehnung an den IT-Grundschutz 6  werden die Sicherheitsanforderungen mit den Modalverben MUSS und SOLLTE sowie den zugehörigen Verneinungen formuliert. Darüber hinaus wird das Modalverb KANN für ausgewählte Prüfaspekte verwendet. Die hier genutzte Definition basiert auf RFC 2119 7  und DIN 820-2: 2018 8 .

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

6  Vgl. BSI-Standard 200-2 (BSI 2017a), S. 18

7  Vgl. Key words for use in RFCs (IETF 1997)

8  Vgl. DIN-820-2: Gestaltung von Dokumenten (DIN 2018)

<!-- page: 7 -->

## 2 Sicherheitsanforderungen

Die nachfolgenden Sicherheitsanforderungen sind zu erfüllen, wenn zur Transportverschlüsselung TLS eingesetzt wird. Dieser Mindeststandard stellt konkrete Anforderungen an die sichere Verwendung und Konfiguration von TLS. Die Möglichkeit, andere Protokolle und/oder Verfahren zur Transportverschlüsselung zu verwenden, bleibt davon unberührt.

Grundlage für die Sicherheitsanforderungen dieses Mindeststandards sind die in der Technischen Richtlinie TR-02102-2 9  formulierten Empfehlungen. Durch die Umsetzung der Empfehlungen der jeweils aktuellen Technischen Richtlinie TR-02102-2 10  wird eine sichere Verwendung von TLS erzielt.

## TLS.2.0.01 - Verwendung von TLS-Protokoll-Versionen

- a) Die Einrichtung MUSS TLS in der Version TLS 1.2 und/oder TLS 1.3 einsetzen.
- b) TLS-Versionen, die nicht TLS.2.0.01 a) entsprechen, MÜSSEN deaktiviert werden.
- c) Bei Neubeschaffungen, die für einen produktiven Einsatz gedacht sind, MUSS auf Kompatibilität mit TLS 1.3 geachtet werden.

## TLS.2.0.02 - Verwendung von kryptografischen Verfahren

a) Die Einrichtung MUSS TLS mit kryptografischen Verfahren einsetzen, die in der jeweils aktuellen Technischen Richtlinie TR-02102-2 11  empfohlen werden und die Eigenschaft 'Perfect Forward Secrecy' (PFS) erfüllen.

## TLS.2.0.03 - Abweichungen und Risikomanagement

Ist der Einsatz von Versionen, abweichend von TLS.2.0.01 oder von kryptografischen Verfahren abweichend von TLS.2.0.02 zwingend erforderlich, kann dies ein Risiko für die Informationssicherheit darstellen. 12,13

- a) Der Einsatz nicht konformer Versionen und/oder nicht konformer kryptografischer Verfahren 14  DARF NUR in sachlich begründeten Ausnahmefällen und nach Rücksprache mit dem BSI erfolgen. 15
- b) Die Einrichtung MUSS den Einsatz nicht konformer Versionen und/oder nicht konformer kryptografischer Verfahren identifizieren und im Rahmen des eigenen Risikomanagements behandeln. 16
- c) Die Einrichtung MUSS die Risiken, die sich durch den Einsatz nicht konformer Versionen und/oder nicht konformer kryptografischer Verfahren ergeben, bewerten und dokumentieren.
- d) Die Einrichtung MUSS die zur Risikobehandlung zu ergreifenden Maßnahmen identifizieren, umsetzen und dokumentieren.
- e) Die Einrichtung MUSS das nach der Umsetzung mitigierender Maßnahmen verbleibende Restrisiko dokumentieren.

9  Vgl. TR-02102-2 (BSI 2023a)

10  Vgl. TR-02102-2 (BSI 2023a)

11  Vgl. TR-02102-2 (BSI 2023a)

12  Vgl. Deprecating TLS 1.0 and TLS 1.1 (IETF 2021)

13  Hinweis: Mit der Veröffentlichung der RFC 8996 hat die Internet Engineering Taskforce (IETF) die Versionen TLS 1.0 und TLS 1.1 für veraltet (deprecated) erklärt. Der Einsatz von TLS 1.0 und TLS 1.1 wird auf Grund mehrerer Schwachstellen in der TR-02102-2 nicht empfohlen.

14  Nicht konforme Versionen und/oder nicht konforme kryptografische Verfahren sind im Kontext dieses Mindeststandards Versionen, die von TLS.2.0.01 abweichen und/oder kryptografische Verfahren, die von TLS.2.0.02 abweichen.

15  mindeststandards@bsi.bund.de

16  Eine ausführliche Beschreibung der Vorgehensweise bei der Risikoanalyse auf der Basis von IT-Grundschutz bietet der BSI-Standard 200-3 (BSI 2017b).

<!-- page: 8 -->

f) Die Einrichtung MUSS einen dem Risiko angemessenen Zeit- und Maßnahmenplan zur Ablösung der nicht konformen Versionen und/oder der nicht konformen kryptografischen Verfahren erstellen.

g) Die Dokumentation des Restrisikos sowie der Zeit- und Maßnahmenplan zur Ablösung der nicht konformen Versionen und/oder der nicht konformen kryptografischen Verfahren MÜSSEN der jeweiligen Leitung der Einrichtung zur Zustimmung vorgelegt werden. 17

## TLS.2.0.04 - TLS für Webserver

Webserver bieten eine exponierte Angriffsfläche und sind durch geeignete Schutzmaßnahmen abzusichern.

Das IT-Grundschutz-Kompendium adressiert dies in der Basis-Anforderung APP.3.2.A11 18  :

'Der Webserver MUSS für alle Verbindungen durch nicht vertrauenswürdige Netze eine sichere Verschlüsselung über TLS anbieten (HTTPS). Falls es aus Kompatibilitätsgründen erforderlich ist, veraltete Verfahren zu verwenden, SOLLTEN diese auf so wenige Fälle wie möglich beschränkt werden. Wenn eine HTTPS-Verbindung genutzt wird, MÜSSEN alle Inhalte über HTTPS ausgeliefert werden. Sogenannter Mixed Content DARF NICHT verwendet werden.'

Diese Basis-Anforderung wird nachfolgend konkretisiert:

a) Im Kontext dieses Mindeststandards sind veraltete Verfahren als Versionen und Verfahren zu verstehen, die nicht die Anforderungen von TLS.2.0.01 und TLS.2.0.02 erfüllen.

b) Werden Abweichungen von TLS.2.0.01 oder von TLS.2.0.02 umgesetzt, MUSS die Einrichtung diese nach TLS.2.0.03 behandeln.

## TLS.2.0.05 - Sicherheitsanforderungen für Projekte des Bundes

Für die Authentisierung innerhalb von Projekten des Bundes verweist die Technische Richtlinie TR-02102-2 19  auf die Technische Richtlinie TR-03116-4 20 .

a) Die Vorgaben der jeweils aktuellen TR-03116-4 21  bezüglich der Authentisierung MÜSSEN eingehalten werden.

17  Vgl. BSI-Standard 200-2 (BSI 2017a Kapitel 8.5)

18  Vgl. IT-Grundschutz-Kompendium (BSI 2023b)

19  Vgl. TR-02102-2 (BSI 2023a)

20  Vgl. TR-03116-4 (BSI 2023c)

21  Vgl. TR-03116-4 (BSI 2023c)

<!-- page: 9 -->

Abbildung 1 veranschaulicht die Beziehungen dieses Mindeststandards zu den technischen Richtlinien und die damit verbundenen Auswirkungen:

Abbildung 1: Mindeststandard zur Verwendung von Transport Layer Security und Technische Richtlinien

<!-- image -->

<!-- page: 10 -->

## Literaturverzeichnis

- BMI (2017) Bundesministerium des Innern und für Heimat (BMI). 2017 Umsetzungsplan Bund 2017 - Leitlinie für die Informationssicherheit
- BSI (2017a) Bundesamt für Sicherheit in der Informationstechnik: BSI-Standard 200-2 - IT-Grundschutz-Methodik, Version 1.0, 2017, https://www.bsi.bund.de/dok/10027846, abgerufen am 25 .0 5 .2023
- BSI (2017b) Bundesamt für Sicherheit in der Informationstechnik: BSI-Standard 200-3 - Risikoanalyse auf der Basis von IT-Grundschutz, Version 1.0, 2017, https://www.bsi.bund.de/dok/407502, abgerufen am 2 5.0 5 .2023
- BSI (2022) Antworten auf häufig gestellte Fragen zu den Mindeststandards, 2022, https://www.bsi.bund.de/dok/MST-FAQ, abgerufen am 2 5.0 5 .2023
- BSI (2023a) Bundesamt für Sicherheit in der Informationstechnik: TR 02102-2: Kryptographische Verfahren: Empfehlungen und Schlüssellängen, Teil 2 - Verwendung von Transport Layer Security (TLS), https://www.bsi.bund.de/dok/TR-02102, abgerufen am 2 5.0 5 .2023
- BSI (2023b) Bundesamt für Sicherheit in der Informationstechnik: IT-Grundschutz-Kompendium, Edition 2023, https://www.bsi.bund.de/dok/1073656, abgerufen am 2 5.0 5 .2023
- BSI (2023c) Bundesamt für Sicherheit in der Informationstechnik: TR 03116-4: Kryptographische Vorgaben für Projekte der Bundesregierung, Teil 4: Kommunikationsverfahren in Anwendungen, https://www.bsi.bund.de/dok/TR-03116, abgerufen am 2 5.0 5 .2023
- DIN (2018) Deutsches Institut für Normung e.V.: Normungsarbeit - Teil 2: Gestaltung von Dokumenten, DIN 820-2:2018-09
- IETF (1997) Internet Engineering Task Force: Key words for use in RFCs to Indicate Requirement Levels, RFC 2119, https://tools.ietf.org/html/rfc2119, abgerufen am 2 5.0 5 .2023
- IETF (2021) Internet Engineering Task Force: Deprecating TLS 1.0 and TLS 1.1, RFC 8996, https://datatracker.ietf.org/doc/html/rfc8996, abgerufen am 2 5.0 5 .2023
- ISO/IEC. (1994) Information technology - Open Systems Interconnection - Basic Reference Model: The Basic Model, ISO/IEC 7498-1. 1994

<!-- page: 11 -->

## Abkürzungsverzeichnis

BSI

BSIG

DIN

FTPS

HTTP

HTTPS

IEC

IETF

IMAPS

ISB

IT-SiBe

LDAPS

MST

OSI

PFS

RFC

SSL

TCP/IP

TLS

TR

UP-BUND

Bundesamt für Sicherheit in der Informationstechnik

Gesetz über das Bundesamt für Sicherheit in der Informationstechnik

Deutsches Institut für Normung e.V.

File Transfer Protocol over SSL/TLS

Hypertext Transfer Protocol

Hypertext Transfer Protocol Secure

International Electrotechnical Commission

Internet Engineering Task Force

Internet Message Access Protocol over SSL/TLS

Informationssicherheitsbeauftragte

IT-Sicherheitsbeauftragte

Lightweight Directory Access Protocol over SSL/TLS

Mindeststandard

Open Systems Interconnection

Perfect Forward Secrecy

Request for Comments

Secure Sockets Layer

Transmission Control Protocol/Internet Protocol

Transport Layer Security

Technische Richtlinie

Umsetzungsplan BUND

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 2 -->

> Tel.: +49 22899 9582-6262

> E-Mail: mindeststandards@bsi.bund.de
