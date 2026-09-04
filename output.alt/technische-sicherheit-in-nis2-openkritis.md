---
source_file: "Technische-Sicherheit-in-NIS2-OpenKRITIS.pdf"
source_sha256: 4446162c746e515471415bf179e8dc1fda9de66c0a3acc7efb555932ab823e6e
source_bytes: 516878
pages: 15
tables: 13
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-27T18:16:46+00:00"
text_coverage_percent: 100.0
appended_source_lines: 1
extraction_status: warn
warnings:
  - "1 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
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

## Technische Sicherheit

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

<!-- page: 3 -->

EU NIS2 fordert von regulierten Unternehmen basierend auf dem eigenen Risikomanagement umfangreiche Maßnahmen für einen sicheren Betrieb in der IT und OT. Die notwendigen Maßnahmen zur Gewährleistung der IT- und OT-Sicherheit umfassen weite Teile der aktuellen Cybersecurity-Landschaft an Prozessen und Technologien.

<!-- image -->

- Backup

<!-- page: 4 -->

- Entwicklung
- Wartung
- Schwachstellen
- Monitoring
- Netze
- Krypto
- Comms

NIS2 fordert von Einrichtungen umfangreiche IT- und OT-Sicherheit im Betrieb. Die folgende Ausarbeitung führt Sicherheitsmaßnahmen anhand der NIS2Anforderungen für Einrichtungen, zusätzlich dem KRITIS-Dachgesetz für Betreiber sowie der alten KRITIS-Anforderungen von RUN-KdA aus. Als Orientierung sind unten die Anforderungen der Durchführungsverordnung DVO (EU) aufgelistet.

| Bereich                | Anforderung                                | NIS2 BSIG   | KRITIS DachG   | RUN KdA                      |
|------------------------|--------------------------------------------|-------------|----------------|------------------------------|
| Backups                | Sicherungen, Infrastruktur, Kapazitäten    | NS.8        | DG.13          | 2 (22-24)                    |
| Sichere Entwicklung    | Entwicklung und Outsourcing von IT         | NS.14       |                | 2 (31,43-44)                 |
| Sichere Wartung        | Betrieb, Wartung und Änderung von IT       | NS.15       |                | 3/2 (20, 45-42)              |
| Schwachstellen         | Schwachstellen, Tests, Patches             | NS.16       |                | 2 (21,25,83) 5 (83,84,95,96) |
| Logging und Monitoring | Auswertung von Logs, SIEM, Automatisierung | NS.6        |                | 5 (80,90-94)                 |
| Netzwerksicherheit     | Netze und Übergänge                        | NS.17       |                | 2 (36-41)                    |
| Kryptographie          | Verschlüsselung und Schlüssel              | NS.21       |                | 2/3 (32-35)                  |
| Sichere Kommunikation  | Notfallkommunikation                       | NS.27 NS.28 |                |                              |

## Technische Sicherheit

## Backup

Einrichtungen müssen einen geregelten Umgang mit Backups (Sicherungen) von kritischen Systemen und deren Daten umsetzen. Backups und deren Wiederherstellungen müssen unbedingt getestet werden und dazu ausreichende Ressourcen bereitgestellt werden.

| Anforderung                                | NIS2   | KRITIS   |   ISO 27001 | RUN    |
|--------------------------------------------|--------|----------|-------------|--------|
|                                            | DVO-EU | DachG    |        2022 | KdA    |
| Datensicherung und Wiederherstellung 4.2.1 |        | A.8.13   |             | 2 (22) |

<!-- page: 5 -->

| Überwachung und Checks   | 4.2.3   | A.8.13 A.8.16   | 2 (23)   |
|--------------------------|---------|-----------------|----------|
| Tests der Backups        | 4.2.6   | A.8.13          | 2 (24)   |
| Angemessene Ressourcen   | 4.2.5   | A.8.6           | 3/2 (20) |

## Sicherung und Wiederherstellung

Datensicherungen (Backups) und Wiederherstellung (Recovery) müssen basierend auf einem Backupkonzept und risikoorientierten Anforderungen regelmäßig geplant und durchgeführt werden. Backups müssen auf Plänen basieren, die wiederum auf BCM-Anforderungen (RTO/RPO) und Risikoeinschätzungen basieren.

Backups müssen regelmäßig überwacht und getestet werden. Ebenso muss unbedingt die Wiederherstellung gesicherter Daten regelmäßig geübt und überprüft werden (DR-Tests).

## Nachweise

Nachweise für effektives Backup sind u.a.:

1. Backup-Konzept
2. Testpläne
3. Testprotokolle

up

## Sichere Entwicklung

Entwicklung von Software, Code, Diensten und Systemen muss geregelten Vorgaben und Sicherheitsanforderungen unterliegen und mit organisierten Prozessen durchgeführt werden - inhouse aber auch bei ausgelagerter oder eingekaufter Entwicklung. Dies betrifft notwendige Prozesse, Vorgaben aber auch Umgebungen und Infrastruktur.

| Anforderung                   | NIS2 DVO-EU   | KRITIS DachG   | ISO 27001 2022   | RUN KdA   |
|-------------------------------|---------------|----------------|------------------|-----------|
| Beschaffung von IT und OT:    | 6.1.1         |                | A.5.21           |           |
| Vorgaben und Prozesse,        | 6.1.2         |                | A.5.22           | 2 (43)    |
| Sicherheitsanforderungen      | 6.1.3         |                | A.5.23           |           |
| Secure Development Life Cycle | 6.2.1         |                | A.8.25           | 2 (43)    |
| (SDLC)                        | 6.2.4         |                | A.8.26           |           |

<!-- page: 6 -->

|                                      |             | A.8.28 A.8.29   |        |
|--------------------------------------|-------------|-----------------|--------|
| Sicherheitsarchitektur Systemhärtung | 6.2.2       | A.8.27          | 2 (25) |
| Sicherheit in Projekten              | 6.2.1       | A.5.8           | 2 (43) |
| Auslagerte Entwicklung               | 6.2.3 6.2.4 | A.8.30          | 2 (44) |
| Zugriffskontrolle zu Quellcode       | 6.2.1       | A.8.4           | 2 (31) |
| Entwicklungsumgebungen separiert     | 6.2.2       | A.8.27          | 2 (53) |

## Beschaffung

Vorgaben und Anforderungen für die Beschaffung von IT- und OT-Systemen und Anwendungen müssen (risikoorientiert) definiert und in Beschaffungsprozessen beachtet werden. Sicherheitsanforderungen an Entwicklung (Secure Coding) muss auch in Beschaffungs- und Entwicklungsprojekten beachtet und vertraglich festgehalten werden.

Zertifizierte Dienstleister und Hersteller (z.B. nach ISO 27001) und Produkte (z.B. nach IEC 62443 für industrielle Systeme, aber auch EU CRA) sind dabei hilfreich. Detaillierte V orgaben zu Einkauf und Lieferanten in NIS2 in Supply Chain Security.

## Entwicklung

Für die sichere Entwicklung von Software, Anwendungen und Systemen muss ein geregelter Entwicklungsprozess samt Sicherheitsanforerungen definiert werden, Secure Development Life Cycle (SDLC). Der Prozess muss aktuelle Sicherheitsanforderungen basierend auf dem eigenen Risikoprofil berücksichtigen und entsprechend mit dem ISMS verzahnt sein.

## Auslagerung

Auch bei ausgelagerter Entwicklung sind Risiken und Sicherheit im Entwicklungsprozess zu beachten - und vertraglich in Ausschreibungen und Leistungsvereinbarungen festzuhalten und zu überprüfen. Auch ausgelagerte Entwicklung und Software Engineering (und auch Vibe Coding) ist eigene Entwicklung, die Sicherheitsvorgaben folgen sollte.

## Projekte

Informationssicherheit muss nicht nur im Betrieb und in Entwicklungen, sondern auch in Projekten eingehalten werden. Dies umfasst viele Aspekte im Umgang mit IT, OT, Kommunikationstechnik aber auch Datenaustausch und Umgang mit Informationen in Projekten.

<!-- page: 7 -->

## Nachweise

Nachweise für effektive Entwicklung sind u.a.:

1. Entwickungs-Policy
2. Code-Regeln
3. Härtungsvorgaben
4. Dokumentierter SDLC
5. Security-Gates

## up

## Sichere Wartung

Wartungsprozesse von eingesetzter IT und OT müssen sicheren Vorgaben und Anforderungen folgen. Dies umfasst insbesondere sicherer Konfigurationen, Änderungsmanagement und Umgang mit Tests und Freigaben für den Betrieb und geregelte Notfallsituationen.

| Anforderung                  | NIS2 DVO-EU       | KRITIS DachG ISO 27001 2022   | RUN KdA   |
|------------------------------|-------------------|-------------------------------|-----------|
| Sichere Konfiguration        | 6.3.2             | A.8.9 A.8.19 A.8.31 A.8.32    | 2 (45)    |
| Change Management Änderungen | 6.4.1 6.4.2 6.4.4 | 8.1 A.8.31 A.8.32 A.7.13      | 2 (45-50) |
| Tests und Genehmigungen      | 6.4.2             | A.8.32                        | 2 (51)    |
| Notfalländerungen            | 6.4.3             | A.8.32                        | 2 (52)    |
| Ressourcen für den Betrieb   | 4.2.5             | A.8.6                         | 3/2 (20)  |

## Konfigurationen

Einrichtungen müssen für die eingesetzten Technologien geregeltes Konfigurationsmanagement und sichere Konfigurationen vorhalten und umsetzen. Konfigurationsvorgaben für Systeme und Dienste müssen Sicherheitsaspekte beachten. Prozesse im Betrieb müssen sicherstellen, dass die sicheren Konfigurationen auch umgesetzt und Abweichungen freigegeben und dokumentiert werden.

<!-- page: 8 -->

## Änderungen

Ein umfangreiches Change Management muss Konfigurationen und Betriebsparameter der eingesetzten IT- und OT-Systeme sowie entwickelte und genutzte Software umfassen. Es muss geordnete Prozesse für das Erstellen, Testen, Freigeben und Einspielen (Rollout) von Änderungen geben, inklusive Vorkehrungen für Behebungen und Notfälle.

## Ressourcen

Für den Betrieb und die notwendigen Steuerungs- und Sicherheitsprozesse müssen angemessene Ressourcen vorhanden sein - personell aber auch technologisch.

## Nachweise

Nachweise für die effektive Wartung von IT und OT sind u.a.:

1. Wartungsvorgaben
2. Härtungskonzept
3. Change-Prozess
4. Konfigurations-Templates

## up

## Schwachstellen

Mit regelmäßigen Sicherheitstests (Penetrationstests) können KRITIS-Betreiber Angriffe auf die KRITIS-Anlagen simulieren, um Schwachstellen in der IT und OT aufzudecken und die Reaktion der Organisation auf Vorfälle zu überprüfen. Penetrationstest können zur Awareness im Unternehmen beitragen und neben technischen Schwachstellen systematische Lücken aufdecken.

| Anforderung                          | NIS2 DVO-EU   | KRITIS DachG ISO 27001 2022   | RUN KdA   |
|--------------------------------------|---------------|-------------------------------|-----------|
| Schutz vor Schadprogrammen (Malware) | 6.9.1 6.9.2   | A.8.7 A.8.23                  | 2 (21)    |
| Systemhärtung                        | 6.2.2 6.3.2   | A.8.19 A.8.27                 | 2 (25)    |
| Prüfung offener Schwachstellen       | 6.10.2        | A.8.8                         | 5 (83,84) |
| Scans, anlassbezogene Prüfungen      | 6.10.3        | A.8.34                        | 5 (83,84) |

<!-- page: 9 -->

| Penetrationstest, Sicherheitstests                           | 6.5.1 6.5.2   | A.8.8 A.8.34                           | 5 (95)   |
|--------------------------------------------------------------|---------------|----------------------------------------|----------|
| Patch-Management                                             | 6.6.1 6.6.2   | A.8.19 A.8.8 A.5.7 A.8.31 A.8.32 A.8.8 | 5 (96)   |
| Informationen zu Schwachstellen, CSIRTs, Threat Intelligence | 6.10.1 6.10.2 | A.5.5 A.5.6 A.5.7                      | 2/3 (83) |

## Schwachstellen

Der Umgang mit kritischen Schwachstellen in Systemen und Prozessen muss Vorgaben aus dem ISMS folgen: Schwachstellen, die durch die Prozesse der Angriffserkennung in Protokollen, Scans oder Tests erkannt werden, aber auch automatisierte Scans durch das Schwachstellen-Management.

## Tests

Regelmäßige Sicherheitstests wie Penetrationstests, Red Teaming aber auch Scans helfen, Lücken zu finden und Detektions- und Präventionsmaßnahmen zu überprüfen. Wichtig ist eine Verzahnung mit dem ISMS und geregeltes Auditmanagement zur Planung und Nachverfolgung der Tests und Audits.

## Malware und Patches

Eingesetzte Systeme sollten, wo technisch möglich, mit Schutzmechanismen und Software gegen Schadcode (Malware) versehen werden. Regelmäßige Scans auf Systemen (und im Netzwerk) helfen, Schadsoftware zu erkennen, die dann entfernt und gefährdete Software gepatcht werden muss.

## Nachweise

Artefakte vom effektiven Umgang mit Schwachstellen und Tests sind u.a.:

1. Testberichte
2. Jahresplanung von Tests
3. Geschlossene Schwachstellen
4. Gepatchte Systeme

## up

<!-- page: 10 -->

## Logging und Monitoring

Um Vorfälle und Cyber-Angriffe zu erkennen, müssen Ereignisse (Events) in Systemen und Verbindungen protokolliert, zentral korreliert und ausgewertet werden. Basierend auf den Informationen aus Log-Dateien von Systemen und SIEM-Lösungen (Indikatoren) kann die Organisation für Sicherheitsvorfälle mit ihren Prozessen tätig werden.

| Anforderung                               | NIS2 DVO-EU             | KRITIS DachG ISO 27001 2022   | RUN KdA   |
|-------------------------------------------|-------------------------|-------------------------------|-----------|
| Security Incident Event Management (SIEM) | 3.2.1 3.2.2 3.2.4 3.4.1 | A.5.28 A.6.8 A.8.15           | 3 (80)    |
| Log-Auswertung                            | 3.2.1 3.2.2 3.2.4       | A.8.15                        | 5 (90,92) |
| Logging und kritische Assets              | 3.2.3 3.2.7             | A.8.15                        | 5 (91)    |
| Log-Auswertung: Aufbewahrung und Zugriff  | 3.2.1 3.2.2 3.2.4 3.2.5 | A.8.15                        | 5 (92,94) |
| Automatisierte Auswertung                 | 3.2.2                   | A.8.15                        | 5 (93)    |
| Zeitsynchronisation                       | 3.2.6                   | A.8.15                        | 5 (93)    |

## Logs und Assets

In den wichtigen Systemen und Netzen ( kritische Assets ) der Einrichtung müssen sicherheits­ relevante Ereignisse protokolliert und zentral (geschützt) aufbewahrt werden. Die Ereignisse umfassen in der Regel mindestens alle Vorgänge zu Nutzern, Berechtigungen und Anmeldungen in Systemen und speziell die Aktivitäten von Administratoren oder anderen privilegierten Benutzern.

Logs müssen kontinuierlich und automatisiert ausgewertet werden.

## SIEM

Mit einem SIEM, Security Information and Event Management, können Angriffsmuster im Internet- und Netzwerkverkehr erkannt und klassifiziert werden. Entsprechende SIEM-Systeme können mit Use Cases und Agenten aufkommenden Verkehr und Interaktionen auf mögliche Angriffe untersuchen - und die Logdateien angeschlossener Systeme und Dienste dazu einbeziehen.

<!-- page: 11 -->

## Scope

Der Scope der wichtigen Systeme sollte regelmäßig überprüft und angepasst werden - neue und veränderte Systeme müssen mit Inbetriebnahme an das Logging und Monitoring, oder das SIEM, angeschlossen ( ongeboarded ) werden. Dazu müssen die Logs der Systeme und Dienste in Scope kontinuierlich erfasst und ausgewertet werden.

## Incidents

An ein SIEM schliesst sich meist Incident Management als Prozess oder SOC-Organisaton an, um auf die detektierten Ereignisse und Vorfälle reagieren (und melden) zu können.

## Angriffserkennung

Für Betreiber kritischer Anlagen (KRITIS) ist Angriffserkennung nach der BSI-Vorgaben OH-SzA bzw. RUN verbindlich.

## Nachweise

Nachweise für die effektive Auswertungen von Logs und Vorfällen sind u.a.:

1. Zentrale Log-Auszüge
2. Assets im SIEM
3. Ausgewertete Ereignisse
4. Indikatoren

## up

## Netzwerksicherheit

Für die Netzwerkinfrastruktur der regulierten Einrichtung müssen umfangreiche Schutzmechanismen im Netz und an den Netzwerkgrenzen umgesetzt werden - um Angriffe im und auf das Netzwerk erkennen und abwehren zu können.

| Anforderung                                                | NIS2 DVO-EU   | KRITIS DachG ISO 27001 2022   | RUN KdA   |
|------------------------------------------------------------|---------------|-------------------------------|-----------|
|                                                            |               | A.8.20                        | 2 (36)    |
| Technische Schutzmaßnahmen Zugriffe, Verbindungen, Dienste | 6.7.1         | A.8.21                        | 2 (36)    |
|                                                            | 6.7.2         | A.8.23                        | 2 (36)    |
| E-Mail, DNS, Routing                                       |               | A.8.26                        | 2 (36)    |

<!-- page: 12 -->

| Netzdokumentation Topologie, Konfiguration          | 6.7.2             | A.8.22                      | 2 (40,41)    |
|-----------------------------------------------------|-------------------|-----------------------------|--------------|
| Segregation, Zonen Zugriffskontrolle, DMZ Übergänge | 6.8.1 6.8.2       | A.8.26 A.8.27 A.8.31 A.5.14 | 2 (38,39,40) |
| Netzüberwachung Filter                              | 6.7.1 6.7.2 6.9.1 | A.8.16 A.8.20 A.8.23 A.8.27 | 2 (37,38,21) |

## Netze

Netze und Bereiche müssen basierend auf ihren Risiken und enthaltenen Systemen/Daten eingeteilt und segregiert werden, üblicherweise in Zonen . Netze und Netzbereiche müssen dann mit umfangreichen Schutzmaßnahmen gesichert werden - für Zugriffe, erlaubten Verkehr (Filter, Schutzsysteme), erlaubte Protokolle und Dienste.

Einrichtungen sollten im Rahmen der Netzwerksicherheit Vorkehrungen für netzbasierte Dienste treffen und entsprechende Sicherheitsanforderungen festlegen, für E-Mail, Namensauflösung (DNS), Routing und Netzwerkprotokolle.

## Übergänge

Die Übergänge zwischen Netzen und unterschiedlichen Schutzniveaus müssen reglementiert, beschränkt und überwacht werden - mit Systemen wie Paketfiltern und netzseitigen Schutzmaßnahmen zur Verkehrssteuerung und Kontrolle. Dies umfasst auf Proxies und Web- und Anwendungsfilter für passierenden Netzwerkverkehr ein.

## Nachweise

Nachweise für effektive Netzsicherheit sind u.a.:

1. Netzdokumentation
2. Topologie
3. Zonen
4. Firewall-Konzept
5. Filter-Regeln
6. Netzarchitektur

<!-- page: 13 -->

up

## Kryptographie

Der Umgang mit Kryptographie und kryptographischen Verfahren wie Verschlüsselung und Schlüsselmanagement muss nach Sicherheitsvorgaben mit geordneten Prozessen organisiert werden. Damit muss sichergestellt werden, dass bestimmte Daten und Verkehrsflüssen angemessen kryptographisch geschütz werden - im Transit und in der Speicherung.

| Anforderung                            | NIS2 DVO-EU   | KRITIS DachG ISO 27001 2022   | RUN KdA   |
|----------------------------------------|---------------|-------------------------------|-----------|
| Vorgaben Kryptographie Verschlüsselung | 9.1 9.2 9.3   | A.5.14 A.8.24                 | 2/3 (32)  |
| Transportverschlüsselung               | 9.2           | A.8.20 A.8.21 A.8.24 A.8.33   | 3 (33)    |
| Verschlüsselung bei der Speicherung    | 9.2 12.3.2    | A.8.24                        | 3 (34)    |
| Schlüsselverwaltung Key-Management     | 9.2           | A.8.24                        | 3 (35)    |

## Nachweise

Nachweise für den effektiven Umgang mit Verschlüsselung sind u.a.:

1. Krypto-Policy
2. Vorgaben für Chiffren
3. Prozesse für CA
4. Schlüsselverteilung

up

## Sichere Kommunikation

NIS2 fordert für die Kommunikation im Unternehmen und in Notfällen bestimmte, gesonderte Verfahren und Sicherheitsvorkehrungen. Explizit geregelt werden müssen die Sicherung von Sprach-, Video- und Textkommunikation sowie Notfallkommunikationssysteme. Technologien zur Kommunikation müssen Sicherheitsanforderungen genügen und für Notfälle müsse z.B. gesonderte, separierte Verfahren genutzt werden.

<!-- page: 14 -->

| Anforderung                                      | NIS2   | KRITIS ISO 27001   | RUN         |
|--------------------------------------------------|--------|--------------------|-------------|
|                                                  | DVO-EU | DachG 2022         | KdA         |
| Gesicherte Sprach-, Video- und Textkommunikation | 6.7.1  | A.8.20             | 2/3 (33,36) |
|                                                  | 6.7.2  | A.8.21             | 2/3 (33,36) |
| Gesicherte Notfallkommunikationssysteme          | 4.2.4  | A.8.14             |             |

## Nachweise

Nachweise für effektive Vorkehrungen in der Kommunikation sind u.a.:

1. Alternative Kommunikationskanäle
2. Sichere Telefone
3. Krisenkommunikation

up

## Integration im Unternehmen

Die technische Sicherheit muss zur Behebung mit weiteren Organisationen vernetzt sein.

- ISMS: Abgleich zu Sicherheitsvorgaben und Kontrollen
- Angriffserkennung: Austausch mit dem SOC und CSIRT zu Schutzmaßnahmen
- Betrieb: Umsetzung der Sicherheitsmaßnahmen

up

## Weitere Informationen

## Literatur

1. [Managing Information Security Risk: Organization, Mission, and Information System View, NIST SP 800-39, März 2011](https://doi.org/10.6028/NIST.SP.800-39)

## Quellen

1. Konkretisierung der Anforderungen an die gemäß § 8a Absatz 1 BSIG umzusetzenden Maßnahmen, Bundesamt für Sicherheit in der Informationstechnik, Version 1.0, 28.2.2020

<!-- page: 15 -->

2. Gesetz über das Bundesamt für Sicherheit in der Informationstechnik und die Sicherheit in der Informationstechnik von Einrichtungen, BSI-Gesetz vom 2. Dezember 2025
3. Reife- und Umsetzungsgradbewertung (RUN) im Rahmen der Nachweisprüfung, Bundesamt für Sicherheit in der Informationstechnik, 09.01.2025
4. Mapping von Anforderungen aus der Konkretisierung der KRITIS-Anforderungen auf RUN-Umsetzungsgrade, Bundesamt für Sicherheit in der Informationstechnik, 09.01.2025
5. ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection - Information security management systems - Requirements
5. [OpenKRITIS](https://www.openkritis.de/)
6. [Cybersecurity in KRITIS und NIS2](https://www.openkritis.de/massnahmen/)
7. [Technische Sicherheit](https://www.openkritis.de/massnahmen/it-sicherheit.html)
8. up

OpenKRITIS ∙ Die gemeinnützige Informationsplattform für NIS2-Einrichtungen und Kritische Infrastrukturen. 50670 Köln ∙ info@openkritis.de ∙ ISSN 2748-565X

Paul Weissmann ist der Herausgeber von OpenKRITIS und publiziert seit 1999 das PA-RISC-Referenzwerk, und Insel Westberlin. OpenKRITIS hat keinen Anspruch auf Vollständigkeit oder Korrektheit und stellt keine Rechtsberatung dar.

Copyright © 2021-2026 ∙ Impressum ∙ Datenschutz ∙ Über uns und Kontakt

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 7 -->

> 6.3
