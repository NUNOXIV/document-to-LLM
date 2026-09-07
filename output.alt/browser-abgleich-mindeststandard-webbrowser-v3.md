---
source_file: "Browser-Abgleich_Mindeststandard_Webbrowser_V3.pdf"
source_sha256: fd79138bbe21c76d0f80d5cfbae4a609656fcd1c4a48121b19a90aa7b5b05996
source_bytes: 452571
pages: 13
tables: 21
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-27T19:11:44+00:00"
text_coverage_percent: 100.0
appended_source_lines: 12
extraction_status: warn
warnings:
  - "12 Tabellenzelle(n) beginnen mitten im Satz — moegliche Zellverschiebung, z. B. \"a) Transport Layer Security (TLS)...\". Zeilen dieser Tabelle vor dem Zitat gegen die Quelle pruefen."
  - "12 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

<!-- image -->

## Abgleichstabelle zum Mindeststandard des BSI für Webbrowser

Version 3.0 vom 19.02.2024

<!-- image -->

<!-- page: 2 -->

## Änderungshistorie

| Version   | Datum       | Beschreibung                                            |
|-----------|-------------|---------------------------------------------------------|
| 1.0       | 20.03.2017  | Erste Veröffentlichung des Mindeststandards             |
| 2.0       | 19.09.2019  | Major Release - umfassende Überarbeitung                |
| 2.1       | 25 .06.2020 | Minor Release - Anpassungen und Konkretisierungen       |
| 2.1a      | 09.07.2020  | Aktualisierung der Firefox- Version von 75 auf 78 (ESR) |
| 3.0       | 19.02.2024  | Major Release - Erweiterung um mobile Browser           |

Tabelle 1: Versionsgeschichte der Abgleichstabelle zum Mindeststandard für Webbrowser

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-6262 E-Mail: mindeststandards@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2024

<!-- page: 3 -->

## Inhalt

| 1             | Über dieses Dokument ..................................................................................................................................................................                                                                                                 | 4     |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| 2             | Abgleich Sicherheitsanforderungen ........................................................................................................................................                                                                                                              | 5     |
| 2.1           | Technische Sicherheitsanforderungen an Anbietende und Produkt ..............................................................                                                                                                                                                            | 5     |
|               | WB.2.1.01 - Vertrauenswürdige Kommunikation .............................................................................................................                                                                                                                               | 5     |
|               | WB.2.1.02 - Updates ........................................................................................................................................................................                                                                                            | 7     |
|               | WB.2.1.03 - Schutz vertrauenswürdiger Daten ...................................................................................................................                                                                                                                         | 7     |
|               | WB.2.1.04 - Externe Dienste ........................................................................................................................................................                                                                                                    | 9     |
|               | WB.2.1.05 - Same-Origin-Policy ...............................................................................................................................................                                                                                                          | 9     |
|               | WB.2.1.06 - Sichere Konfiguration ...........................................................................................................................................                                                                                                           | 9     |
|               | WB.2.1.07 - Minimale Rechte ...................................................................................................................................................                                                                                                         | 11    |
|               | WB.2.1.08 - Sandboxing und Kapselung ..............................................................................................................................                                                                                                                     | 11    |
|               | WB.2.1.09 - Content Security Policy (CSP) ..........................................................................................................................                                                                                                                    | 11    |
| WB.2.1.10 2.2 | - Subresource Integrity .......................................................................................................................................... Organisatorische Sicherheitsanforderungen an Anbietende und Produkt ................................................ | 11 12 |
|               | WB.2.2.01 - Entwicklung ............................................................................................................................................................                                                                                                    | 12    |
|               | WB.2.2.02 - Aktualisierung ........................................................................................................................................................                                                                                                     | 12    |
|               | WB.2.2.03 - Kontaktmöglichkeit .............................................................................................................................................                                                                                                            |       |
|               | .....................................................................................................................................................                                                                                                                                   | 12    |
|               | WB.2.2.04 - Dokumentation                                                                                                                                                                                                                                                               | 13    |

<!-- page: 4 -->

## 1 Über dieses Dokument

Dieses Dokument unterstützt Verantwortliche bei der Einhaltung des Mindeststandards des BSI für Webbrowser in der Version 3.0. Hierfür werden in Kapitel 2 die technischen (Kapitel 2.1) und organisatorischen (Kapitel 2.2) Sicherheitsanforderungen mit den in der Bundesverwaltung am häufigsten eingesetzten Webbrowsern abgeglichen. Nicht betrachtet werden die Sicherheitsanforderungen an den Betrieb (Kapitel 2.3 des Mindeststandards), da diese nicht vom Webbrowser, sondern von der nutzenden Einrichtung einzuhalten sind.

Die Hilfestellungen in diesem Dokument sind nicht rechtlich bindend und schließen keine anderen Lösungen aus. Insbesondere ist zu beachten, dass der Mindeststandard ein Mindestsicherheitsniveau beschreibt, das nicht unterschritten werden sollte. Jede Institution sollte zusätzlich - nicht nur bei erhöhten Sicherheitsbedürfnissen - eigene Betrachtungen vornehmen.

Die Ergebnisse des Abgleichs werden (zusätzlich zur textuellen Beschreibung) farblich dargestellt. Dabei werden die Farben wie folgt verwendet:

Grün: Der Webbrowser erfüllt die Anforderung ohne zusätzliche Maßnahmen.

Gelb : Der Webbrowser erfüllt die Anforderung nur teilweise oder nur mithilfe weiterer Maßnahmen. Beispielhafte Lösungen werden an den entsprechenden Stellen vorgeschlagen.

Rot: Der Webbrowser erfüllt die Anforderung nicht.

Grau: Die Anforderung ist hier nicht relevant (bei mobilen Browsern, wenn bspw. Anforderungen über Eigenschaften des Betriebssystems umgesetzt werden)

Der Abgleich wurde auf Basis der nachfolgenden Webbrowser-Versionen durchgeführt:

- Mozilla Firefox 120
- Google Chrome 119
- Microsoft Edge 119
- Google Chrome für Android 119
- Mozilla Firefox für Android 120
- Apple Safari für iOS 16

Durch die kontinuierliche Aktualisierung und Veränderung von Webbrowsern können sich stets Änderungen bezüglich des Abgleichs ergeben. Dieses Dokument wird jährlich aktualisiert und bezieht sich ausschließlich auf die angegebenen Browser-Versionen. Zwischenzeitlich können neue Hinweise gerne per E-Mail über mindeststandards@bsi.bund.de eingereicht werden.

<!-- page: 5 -->

## 2 Abgleich Sicherheitsanforderungen

## 2.1 Technische Sicherheitsanforderungen an Anbietende und Produkt

WB.2.1.01 - Vertrauenswürdige Kommunikation

| Sicherheitsanforderung            | Mozilla Firefox                                                                                                                | Google Chrome                                                                                                                            | Microsoft Edge                                                                                                                | Firefox für Android                                                                                                            | Chrome für Android                                                                                                                                                                                                                                                                                                              | Apple Safari für iOS                                                                                                                                                                                                                                                                                                            |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| a) Transport Layer Security (TLS) | ja Nicht empfohlene Ciphers werden unterstützt, können aber per Kon- figurationsdatei mit security. ssl3.* deaktiviert werden. | ja Nicht empfohlene Ciphers werden unterstützt, können aber per Kommandozeilen- schalter --cipher- suite- blacklist= deaktiviert werden. | ja Nicht empfohlene Ciphers werden unterstützt, können aber per Gruppenrichtlinie TLSCipherSuit eDenyList deaktiviert werden. | ja Nicht empfohlene Ciphers werden unterstützt, können aber per Kon- figurationsdatei mit security. ssl3.* deaktiviert werden. | ja Ciphers können nicht deaktiviert werden, dadurch ist es möglich, dass Verbindungen mit Webseiten zwar als verschlüsselt angezeigt werden, die Verschlüsselung aber unsichere Ciphers nutzt. Für dieses Risiko sollten Nutzende sensibilisiert werden und ggf. keine sensiblen Daten auf den Mobilgeräten verarbeitet werden. | ja Ciphers können nicht deaktiviert werden, dadurch ist es möglich, dass Verbindungen mit Webseiten zwar als verschlüsselt angezeigt werden, die Verschlüsselung aber unsichere Ciphers nutzt. Für dieses Risiko sollten Nutzende sensibilisiert werden und ggf. keine sensiblen Daten auf den Mobilgeräten verarbeitet werden. |

<!-- page: 6 -->

| Sicherheitsanforderung                | Mozilla Firefox   | Google Chrome                                                                                                                                                                         | Microsoft Edge                                                                                                                                                                 | Firefox für Android                                                                                                                                                                         | Chrome für Android                                                                                                                  | Apple Safari für iOS                                                                                                                                                                                                        |
|---------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| b) Zertifikate                        | ja                | Konfiguration erforderlich Nutzt (auch) den Zertifikatsspeicher des Betriebssystems Online-OCSP- /CRL-Prüfungen müssen per Gruppenrichtlinie oder Registry- Eintrag aktiviert werden. | Konfiguration erforderlich Nutzt den Zertifikatsspeicher des Betriebssystems Online-OCSP- /CRL-Prüfungen müssen per Gruppenrichtlinie oder Registry- Eintrag aktiviert werden. | Konfiguration erforderlich Kann den Zertifikatsspeicher des Betriebssystems nutzen (Funktion muss aktiviert werden) OCSP-Modus muss in der Konfigurations- datei mit security.OCSP .enabled | Konfiguration erforderlich Online-OCSP- /CRL-Prüfungen müssen per Enterprise-Policy EnableOnlineRe vokationChecks aktiviert werden. | ja Nutzt den Zertifikatsspeicher des Betriebssystems Informationen über Zertifikats- widerrufe werden gesammelt und von Apple bereitgestellt. OCSP-Anfragen werden gestellt, wenn Widerrufs- informationen nicht vorliegen. |
| c) Darstellung der Kommunikationsform | ja                | teilweise Die vollständige URL wird durch Kopieren und (an anderer Stelle) Einfügen sichtbar. Mixed-Content wird in der Adresszeile nicht geeignet dargestellt                        | teilweise Die vollständige URL wird durch Kopieren und (an anderer Stelle) Einfügen sichtbar. Mixed-Content wird in der Adresszeile nicht geeignet dargestellt                 | ja                                                                                                                                                                                          | teilweise Mixed-Content wird in der Adresszeile nicht geeignet dargestellt                                                          | ja                                                                                                                                                                                                                          |

<!-- page: 7 -->

| Sicherheitsanforderung                   | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|------------------------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| d) HTTP Strict Transport Security (HSTS) | ja                | ja              | ja               | ja                    | ja                   | ja                     |

## WB.2.1.02 - Updates

| Sicherheitsanforderung              | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android                                                                                                              | Chrome für Android                                                                                                                | Apple Safari für iOS                                                                              |
|-------------------------------------|-------------------|-----------------|------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| a) Update-Mechanismen               | ja                | ja              | ja               | Wird in der Regel über die entsprechenden App-Stores oder ein MDM aktualisiert. Eigene Update- Mechanismen sind nicht verfügbar. | Wird in der Regel über die entsprechenden App- Stores oder ein MDM aktualisiert. Eigene Update- Mechanismen sind nicht verfügbar. | Erhält Updates als Bestandteil des festen iOS-Softwarepakets im Zuge von Betriebssystem- Updates. |
| b) Integritätsprüfungen der Updates | ja                | ja              | ja               | Wird über Mechanismen des Betriebssystems aktualisiert.                                                                          | Wird über Mechanismen des Betriebssystems aktualisiert.                                                                           | Wird über Mechanismen des Betriebssystems aktualisiert.                                           |

## WB.2.1.03 - Schutz vertrauenswürdiger Daten

| Sicherheitsanforderung   | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|--------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| a) Cookies               | ja                | ja              | ja               | ja                    | ja                   | ja                     |

<!-- page: 8 -->

| Sicherheitsanforderung             | Mozilla Firefox   | Google Chrome   | Microsoft Edge                                                                                                                                                                                                                                                         | Firefox für Android   | Chrome für Android   | Apple Safari für iOS                                                             |
|------------------------------------|-------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------|----------------------------------------------------------------------------------|
| b) Website-Daten und Verlauf       | ja                | ja              | ja                                                                                                                                                                                                                                                                     | ja                    | ja                   | ja                                                                               |
| c) Kamera, Mik r ofon und Standort | ja                | ja              | ja                                                                                                                                                                                                                                                                     | ja                    | ja                   | ja                                                                               |
| d) Telemetriedaten                 | ja                | ja              | eingeschränkt Übertragung von Telemetriedaten lässt sich zentral nur in 'höherwertigen' Windows- Versionen (Enterprise, Education, Server) per Gruppen- richtlinie 'Allow Telemetry' bzw. 'Allow diagnostic data' zusammen mit der Windows- Telemetrie 1 deaktivieren. | ja                    | ja                   | ja Als Einstellung des Betriebssystems (nicht einzeln für Safari konfigurierbar) |

<!-- page: 9 -->

| Sicherheitsanforderung         | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|--------------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| e) Privater / Inkognito- Modus | ja                | ja              | ja               | ja                    | ja                   | ja                     |

## WB.2.1.04 - Externe Dienste

| Sicherheitsanforderung      | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|-----------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| WB.2.1.04 - Externe Dienste | ja                | ja              | ja               | ja                    | ja                   | ja                     |

## WB.2.1.05 - Same-Origin-Policy

| Sicherheitsanforderung          | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|---------------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| WB.2.1.05 - Same-Origin- Policy | ja                | ja              | ja               | ja                    | ja                   | ja                     |

## WB.2.1.06 - Sichere Konfiguration

| Sicherheitsanforderung          | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android                                                                                  | Chrome für Android   | Apple Safari für iOS   |
|---------------------------------|-------------------|-----------------|------------------|------------------------------------------------------------------------------------------------------|----------------------|------------------------|
| a) Verwaltung der Einstellungen | ja                | ja              | ja               | eingeschränkt JavaScript lässt sich nur über Konfigurations- dateien oder Erweiterungen deaktivieren | ja                   | ja                     |

<!-- page: 10 -->

| Sicherheitsanforderung    | Mozilla Firefox   | Google Chrome                              | Microsoft Edge                             | Firefox für Android                        | Chrome für Android                         | Apple Safari für iOS                                                                                                                                                                                                                                                                                                                                                |
|---------------------------|-------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| b) Zentrale Konfiguration | ja                | EME kann nicht zentral deaktiviert werden. | EME kann nicht zentral deaktiviert werden. | EME kann nicht zentral deaktiviert werden. | EME kann nicht zentral deaktiviert werden. | EME nicht deaktivierbar Der Hersteller gibt an, dass die Nutzung der digitalen Rechteverwaltung FairPlay durch den Safari-Browser besonders gesichert sei und damit die Möglichkeit zur Abschaltung der entsprechenden Schnittstelle entfallen könne. Die vom Hersteller zur Verfügung gestellten Informationen reichen für eine Bewertung durch das BSI nicht aus. |
| c) Schutz vor Änderungen  | ja                | ja                                         | ja                                         | ja                                         | ja                                         | ja                                                                                                                                                                                                                                                                                                                                                                  |
| d) Cloud-Dienste          | ja                | ja                                         | ja                                         | ja                                         | ja                                         | ja                                                                                                                                                                                                                                                                                                                                                                  |
| e) DoH / DoT              | ja                | ja                                         | ja                                         | ja                                         | ja                                         | ja                                                                                                                                                                                                                                                                                                                                                                  |

<!-- page: 11 -->

## WB.2.1.07 - Minimale Rechte

| Sicherheitsanforderung      | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android                                                  | Chrome für Android                                                   | Apple Safari für iOS                                                 |
|-----------------------------|-------------------|-----------------|------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| WB.2.1.07 - Minimale Rechte | ja                | ja              | ja               | Durch App-Sandbox keine erweiterten Rechte im Sinne der Anforderung. | Durch App-Sandbox keine erweiterten Rechte im Sinne der Anforderung. | Durch App-Sandbox keine erweiterten Rechte im Sinne der Anforderung. |

## WB.2.1.08 - Sandboxing und Kapselung

| Sicherheitsanforderung        | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|-------------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| a) Architektur- eigenschaften | ja                | ja              | ja               | ja                    | ja                   | ja                     |
| b) Isolation von Webseiten    | ja                | ja              | ja               | ja                    | ja                   | ja                     |

## WB.2.1.09 - Content Security Policy (CSP)

| Sicherheitsanforderung                    | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|-------------------------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| WB.2.1.09 - Content Security Policy (CSP) | ja                | ja              | ja               | ja                    | ja                   | ja                     |

## WB.2.1.10 - Subresource Integrity

| Sicherheitsanforderung            | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|-----------------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| WB.2.1.10 - Subresource Integrity | ja                | ja              | ja               | ja                    | ja                   | ja                     |

<!-- page: 12 -->

## 2.2 Organisatorische Sicherheitsanforderungen an Anbietende und Produkt

## WB.2.2.01 - Entwicklung

| Sicherheitsanforderung   | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android                         | Chrome für Android                          | Apple Safari für iOS                                                                                                          |
|--------------------------|-------------------|-----------------|------------------|---------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| WB.2.2.01 - Entwicklung  | ja                | ja              | ja               | Teilweise kein Schutz gegen Stack- Smashing | Teilweise kein Schutz gegen Stack- Smashing | Eine Überprüfung der IPA-Datei von Safari ist nicht möglich, da es fester Bestandteil von iOS ist und nicht separat vorliegt. |

## WB.2.2.02 - Aktualisierung

| Sicherheitsanforderung        | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|-------------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| WB.2.2.02 - Aktualisierung ja | ja                | ja              | ja               | ja                    |                      | ja                     |

## WB.2.2.03 - Kontaktmöglichkeit

| Sicherheitsanforderung         | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|--------------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| WB.2.2.03 - Kontaktmöglichkeit | ja                | ja              | ja               | ja                    | ja                   | ja                     |

<!-- page: 13 -->

## WB.2.2.04 - Dokumentation

| Sicherheitsanforderung    | Mozilla Firefox   | Google Chrome   | Microsoft Edge   | Firefox für Android   | Chrome für Android   | Apple Safari für iOS   |
|---------------------------|-------------------|-----------------|------------------|-----------------------|----------------------|------------------------|
| WB.2.2.04 - Dokumentation | ja 2              | ja 3            | ja 4             | ja 2                  | ja 3                 | ja 5                   |

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 2 -->

> E-Mail: mindeststandards@bsi.bund.de

> Internet: https://www.bsi.bund.de

<!-- page: 3 -->

> 3

> Über dieses Dokument ..................................................................................................................................................................  4

> Abgleich Sicherheitsanforderungen ........................................................................................................................................ 5

<!-- page: 4 -->

> organisatorischen (Kapitel 2.2) Sicherheitsanforderungen mit den in der Bundesverwaltung am häufigsten

<!-- page: 8 -->

> 1  Vgl. https://learn.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization (abgerufen am 18.12.2023).

> Für weitere Informationen zur Telemetrie unter Windows siehe Projekt SiSyPHuS des BSI: https://www.bsi.bund.de/dok/11713470

<!-- page: 13 -->

> 2  Vgl. https://www.mozilla.org/de/privacy/firefox/ (abgerufen am 25.01.2024)

> 3  Vgl. https://www.google.com/chrome/privacy/whitepaper.html (abgerufen am 25.01.2024)

> 4  Vgl. https://learn.microsoft.com/en-us/microsoft-edge/privacy-whitepaper/ (abgerufen am 25.01.2024)

> 5  Vgl. https://www.apple.com/de/privacy/ (abgerufen am 25.01.2024)
