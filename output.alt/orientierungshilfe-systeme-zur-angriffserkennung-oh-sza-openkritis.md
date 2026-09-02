---
source_file: "Orientierungshilfe-Systeme-zur-Angriffserkennung-OH-SzA-OpenKRITIS.pdf"
source_sha256: 515ed1d765a54c770ca057de37bc964e554afabfa28daf5d483d4f2d96246e3a
source_bytes: 387491
pages: 11
tables: 8
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-27T18:14:27+00:00"
text_coverage_percent: 100.0
appended_source_lines: 4
extraction_status: warn
warnings:
  - "2 Tabellenzelle(n) beginnen mitten im Satz — moegliche Zellverschiebung, z. B. \"werden. Systeme sollten gruppiert werden. Zur Angriffserkenn...\". Zeilen dieser Tabelle vor dem Zitat gegen die Quelle pruefen."
  - "4 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
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

## Angriffserkennung KRITIS

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

Mit der Orientierungshilfe für Systeme zur Angriffserkennung (OH SzA) legt das BSI Vorgaben zur Erkennung von Cyberangriffen durch KRITIS-Betreiber fest. Die Orientierungshilfe definiert verbindliche Anforderungen für Protokollierung, Erkennung und Reaktion bei Betreibern, die seit 2023 umgesetzt werden müssen.

<!-- image -->

<!-- page: 4 -->

- Systeme zur Angriffserkennung
- Detektion
- Reaktion
- [Mapping](https://www.openkritis.de/massnahmen/sza-mapping-iso-27001-nis2.html)

Die OH SzA fordert dazu eine umfangreiche Organisation und Infrastruktur zur Erkennung von Cyberangriffen. Starker Fokus liegt auf Automatisierung, Zentralisierung und sehr vielen und teils sehr spezifischen Vorgaben zur Architektur á la SOC, CERT und SIEM.

## Orientierungshilfe Angriffserkennung

## Governance

Übergreifende Anforderungen an alle Phasen der Angriffserkennung, die sich vor allem um Rahmenbedingungen und Aktualität der Plattform und Systeme drehen.

Angriffserkennung allgemeine MUSS-Kriterien, eigene Zusammenstellung, Stand Oktober 2024

| OH SzA   | Thema                                                                                                              | Anforderung                                                                                                        |
|----------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Kap 1.2  | Rahmenbedingungen Die für Angriffserkennung notwendige Technologie, Organisation und Personal muss vorhanden sein. | Rahmenbedingungen Die für Angriffserkennung notwendige Technologie, Organisation und Personal muss vorhanden sein. |
| Kap 1.2  | Angriffsmuster                                                                                                     | Informationen zu Schwachstellen eingesetzter Systeme und zu Angriffen müssen eingeholt werden.                     |
| Kap 1.2  | Plattform                                                                                                          | Die zur Angriffserkennung notwendige Hardware und Software muss auf dem aktuellen Stand sein.                      |
| Kap 1.2  | Signaturen                                                                                                         | Die Signaturen zur Detektion müssen aktuell gehalten werden.                                                       |
| Kap 1.2  | Konfiguration                                                                                                      | Systeme müssen so konfiguriert werden, dass 'bekannte Möglichkeiten der Schwachstellen­ erkennung' genutzt werden. |

up

## Protokollierung (SZA-P)

Spezifische Anforderungen zum Logging und der Speicherung von Logdaten, damit Systeme der Kritischen Infrastruktur abgedeckt werden und die Protokollierung zentral geschützt ist.

KRITIS SzA Protokollierung MUSS/SOLL, eigene Zusammenstellung, Draft 20241024

| BSI KRITIS KdA/RUN   | Thema   | Anforderung                                                                                                                                                                                                                                                                                                     |
|----------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BSI-101 3/4/5        | Planung | Die zur Speicherung und Auswertung notwendige IT muss in der Planung 'bedacht' und gesetzliche Regelungen (mind. Datenschutz) berücksichtigt werden. Die Planung muss dokumentiert werden, inkl. Netzbereiche, Daten­ - quellen/-flüsse, Kommunikations­ beziehungen und protokollierter Ereignisse pro System. |

<!-- page: 5 -->

| 101.7, 101.9 101.1, 101.5 101.8 101.3, 101.6 17:20   | Richtlinie (OPS.1.1.5)                                          | Die für die Kritische Infrastruktur (kDL) wichtigen Systeme müssen identifiziert werden. Die notwendige Protokollierung muss nach Änderungen (Changes) im Geltungsbereich mittels Prozess angepasst werden. Orientierungshilfe Systeme zur Angriffserkennung (OH SzA) - OpenKRITIS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BSI-102 3 102.1, 102.3 BSI-102.S 4                   | Protokollierung Planung SOLL                                    | Die sichere Planung, Aufbau und Betrieb von Protokollierung muss in einer Richtlinie definiert werden, inkl. 'wie, wo und was protokolliert werden soll.' Die Richtlinie muss vom ISB mit Fachverantwortlichen erstellt, abgestimmt, allen Mitarbeitern in der Protokollierung bekannt und die Umsetzung regelmäßig überprüft werden. Die Protokollierung muss stichpunktartig überprüft werden. Die Protokollierung sollte schrittweise, basierend auf Risiko-Analyse und der kritischen Dienstleistung, geplant                                                                                                                                                                                                                                                                                                                                                       |
| 102.2 BSI-103 3 103.1, 103.3, 103.6, 103.10,         | Protokollierung System, Netze, Daten, Infrastruktur (OPS.1.1.5) | werden. Systeme sollten gruppiert werden. Zur Angriffserkennung notwendige Daten auf System- und Netzebene müssen gespeichert und zur Auswertung bereitgestellt werden. Sicherheits­ relevante Ereignisse von IT und Anwendungen müssen protokolliert werden. Dafür müssen systemeigene Funktionen oder separate Systeme genutzt und Vorgaben eingehalten werden. Die gesammelten Daten müssen gefiltert, normalisiert, aggregiert, korreliert und verfügbar gemacht. Protokolldaten müssen vor Manipulation geschützt und nach bestimmten Fristen gelöscht werden. Bei 'großen Verbünden' müssen die Daten an 'für den Netzbereich' zentralen (Logging-)Stellen gespeichert Die Systemzeit der protokollierenden Systeme und Anwendungen muss synchron sein. Für Systeme ohne eigene Protokollierungs-Funktion muss dies von Systemen auf Netzebene übernommen werden. |
| 103.2 103.4 103.7 103.11                             |                                                                 | werden. Gesetzliche und regulatorische Anforderungen, inklusive Bundes- und Landesdatenschutz (ggf. Anonymisierung oder Pseudonymisierung) und ggf. branchenspezifische Regulierung, an die Protokollierung müssen eingehalten werden, ebenso Persönlichkeits- und Mitbestimmungsrechte. Die Logging-Infrastruktur muss ausreichend mit personellen, tech­ nischen und finanziellen Ressourcen dimensioniert und budgetiert werden. Log-Quellen sollten zur Erkennung von Angriffen im Geltungsbereich wie folgt erschlossen werden:                                                                                                                                                                                                                                                                                                                                    |
| BSI-103.S 4/5 103.5, 103.9 103.8                     | Sichtbarkeit, Infrastruktur SOLL                                | Außen nach innen: von Netz-Grenzen zu inneren Bereichen Systeme: zuerst kritische und zentrale Systeme zur Steuerung, Leitsysteme etc. Priorisierung basierend auf der Kritikalität der Systeme [siehe BCM] Die Zahl zentraler Logging-Stellen sollte möglichst gering gehalten werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## up

## Erkennung (SZA-D)

<!-- page: 6 -->

Anforderungen zur geregelten, automatisierten Detektion von Cyberangriffen durch Systeme und Mechanismen. Schwerpunkt liegt auf kontinuierlicher Überwachung zentraler Punkte und Netzübergänge.

KRITIS SzA Erkennung MUSS/SOLL, eigene Zusammenstellung, Draft 20241024

| BSI KRITIS KdA                        | Thema                                | Anforderung                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BSI-104 3/5                           | Bedrohungen und Risiken              | Relevante Bedrohungen müssen durch Detektion 'umfassend und effizient' abgedeckt werden, wozu die Risikoanalyse und 'Größe und Struktur' des Betreibers 'einbezogen' werden muss.                                                                                                                                                                                                                                                                                    |
| BSI-105 3                             | Richtlinie Detektion (DER.1.A1)      | Die Detektion von Sicherheits­ vorfällen muss in einer Richtlinie definiert werden. Dort muss die sichere Planung, Aufbau und Betrieb von Detektion beschrieben werden. Die Richtlinie muss allen Mitarbeitern in der Detektion bekannt und die Umsetzung regelmäßig überprüft, Abweichungen mit dem ISO/ISB abgestimmt werden. Für die relevanten IT-Systeme müssen für Detektion Verantwortliche festgelegt sein, die die Einhaltung der Richtlinie sicherstellen. |
| BSI-106 3                             | Regulierung Detektion (tw. DER.1.A2) | Gesetzliche und regulatorische Anforderungen, inklusive Bundes- und Landesdatenschutz, müssen bei der Auswertung von Protokollierung eingehalten werden, ebenso Persönlichkeits- und Mitbestimmungsrechte, TKG etc.                                                                                                                                                                                                                                                  |
| BSI-107 3                             | Meldewege Detektion (DER.1.A3)       | Melde- und Alarmierungswege müssen dokumentiert, eingerichtet und bekannt sein, inklusive der relevanten Stellen und Meldewege, Dringlichkeiten, Aufgaben und Prozesse. Die Verantwortlichen müssen die eigene Rolle in den Alarmierungs- und Meldeprozessen kennen.                                                                                                                                                                                                 |
| BSI-107.S 4                           | Überprüfung Meldewege (DER.1.A3)     | Die Meldewege sollten regelmäßig geprüft, aktualisiert und erprobt werden.                                                                                                                                                                                                                                                                                                                                                                                           |
| BSI-108 3                             | Awareness (DER.1.A4)                 | Mitarbeitern müssen für Ereignisse sensibilisiert werden. Der allgemeine Meldeprozess, Umgang mit sicherheits­ relevanten Ereignissen und korrektem Verhalten in der Meldung ans Incident Management, und von Sicherheits­ vorfällen muss bekannt sein.                                                                                                                                                                                                              |
| BSI-109 3                             | Systemfunktionen (DER.1.A5)          | Vorhandene Funktionen zur Detektion von Systemen und Anwendungen müssen genutzt und ausgewertet werden. Bei einem sicherheits­ relevanten Vorfall müssen Meldungen und protokollierte Ereignisse ausgewertet werden.                                                                                                                                                                                                                                                 |
| BSI-109.S 4                           | Kontrolle Meldungen (DER.1.A5)       | Gesammelte Meldungen sollten stichpunktartig kontrolliert werden.                                                                                                                                                                                                                                                                                                                                                                                                    |
| BSI-110 3/5 110.1, 110.3 101.1, 101.5 | Kontinuierliche Überwachung          | Protokoll­ daten müssen kontinuierlich überwacht und ausgewertet werden. Dazu müssen eigene Mitarbeiter oder Mitarbeiter von Dienstleistern benannt werden, die in einer der Risikoanalyse angemessenen Zeitspanne reagieren. Manuelle, aktive Prozesse durch Mitarbeiter (inkl. Kontrolle und Test) und Aufgaben müssen in Verfahrens­ anleitungen dokumentiert sein.                                                                                               |
| BSI-111 3                             | Schadcode Netze, IDS (mit DER.1)     | Es müssen 'Schadcode­ detektions­ systeme' und ggf. zusätzlich auf zentralen Systemen 'Schadcode­ scanner' eingesetzt werden. Auf diese muss zentraler Zugriff möglich sein, Meldungen müssen ausgewertet und untersucht werden.                                                                                                                                                                                                                                     |

<!-- page: 7 -->

| BSI-112 3                      | Korrelation und Signaturen             | (NIDS), jeweils anhand des Netzstrukturplans. Protokolldaten müssen regelmäßig auf Auffälligkeiten kontrolliert werden. Die Signaturen der Detektionssysteme müssen aktuell und synchron gehalten werden.                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BSI-112.S 3                    | Korrelation SOLL                       | Protokoll- und Logging-Daten sollten zur Korrelation zeitlich synchronisiert werden (sein).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| BSI-113 3                      | Externe Quellen                        | Erkenntnisse und Meldungen externen Quellen müssen herangezogen werden, grundsätzlich ausgewertet und bewertet, und bei Relevanz an die richtigen Stellen weitergeleitet werden. Bei Relevanz muss entsprechend eskaliert werden.                                                                                                                                                                                                                                                                                                                                                                                 |
| BSI-114 3                      | Personal Detektion                     | Es müssen genug personelle Ressourcen für die Detektion bereit­ gestellt werden. Für die Auswertung müssen Mitarbeiter oder Dienstleister beauftragt werden, ein Personenkreis muss ausschließlich für Angriffserkennung benannt werden.                                                                                                                                                                                                                                                                                                                                                                          |
| 114.1, 114.3 BSI-114.S 4 114.2 | Personal Detektion SOLL                | Detektion sollte die überwiegende oder höher­ priorisierte Aufgabe des Personals sein. Das Personal sollte spezialisierte Schulungen erhalten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| BSI-115 3                      | Zentral und dauerhaft                  | Zur Erkennung und Auswertung müssen zentrale Komponenten eingesetzt werden. Sicherheits­ relevante Vorgänge müssen mit zentralen automatisierten Analysen erkannt werden. Protokolldaten müssen lückenlos einsehbar und auswertbar sein, die Daten möglichst permanent ausgewertet werden. Systemverantwortliche müssen Analyseparameter auditieren und anpassen, Protokolldaten müssen regelmäßig automatisch auf sicherheits­ relevante Ereignisse überprüft werden. Bei Überschreiten von Schwellenwerten (und Regeln) muss automatisch alarmiert werden, das zuständige Personal dann die Reaktion einleiten. |
| BSI-116 3 116.1, 116.3 116.5   | Sicherheits­ relevante Ereignisse      | Informationen zu Schwachstellen und Angriffsmustern für die eingesetzten Systeme müssen für die Detektion fortlaufend eingeholt werden. Im Schwachstellen-Management müssen dazu fortlaufend Meldungen relevanter Stellen und Hersteller eingeholt werden und in Prozesse einfließen. Sicherheits­ relevante Ereignisse (SRE) müssen bewertet werden, ob sie einen Vorfall darstellen. Detektionsmechanismen müssen daraufhin 'nachjustiert' werden.                                                                                                                                                              |
| BSI-116.S 4 116.2, 116.4       | Sicherheits­ relevante Ereignisse SOLL | Vor der Umsetzung und bei wichtigen Änderungen im Geltungsbereich sollte eine Kalibrierung der Detektion und Baselining der auftretenden Ereignisse vorgenommen werden. Die Zahl von False Positives im Normalbetrieb sollte überprüft bewertet werden. Die Detektions­ systeme sollten in eindeutigen Fällen SREs automatisch qualifizieren können - andernfalls manuell durch festgelegte Verantwortliche.                                                                                                                                                                                                      |

## up

## Reaktion (SZA-R)

<!-- page: 8 -->

Umfangreiche organisatorische Anforderungen zur Reaktion auf Vorfälle mit definierten Vorgaben, Prozessen, Verantwortlichkeiten und Abläufen in der Wiederherstellung.

KRITIS SzA Reaktion MUSS/SOLL, eigene Zusammenstellung, Draft 20241024

| BSI KRITIS KdA         | Thema                                      | Anforderung                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BSI-117                |                                            |                                                                                                                                                                                                                                                                                                                                                                                                    |
| 3                      | Sicherheits­ vorfall (DER.2.1.A1)          | Sicherheits­ vorfälle müssen klar definiert und vom Regelbetrieb abgegrenzt sein. Die Definition muss den relevanten Mitarbeitern bekannt sein.                                                                                                                                                                                                                                                    |
| 117.1                  |                                            |                                                                                                                                                                                                                                                                                                                                                                                                    |
| BSI-117.S 4            | Umgang mit Vorfällen (DER.2.1) SOLL        | Es sollte ein einheitliches Verfahren zur Einstufung von Sicherheits­ vorfällen und Störungen geben, abgestimmt mit ISMS und Incident Management. In der Vorfallsbehandlung sollten die Auswirkungen abgeschätzt und entschieden werden, ob Aufklärung oder Eindämmung Priorität hat; im Vorfeld sollten Worst Case Szenarien analysiert werden.                                                   |
| 117.2                  | 116.2, 116.4,                              |                                                                                                                                                                                                                                                                                                                                                                                                    |
| BSI-118 3 118.1, 118.3 | Richtlinie Reaktion (DER.2.1.A2)           | Die Behandlung von Sicherheits­ vorfällen muss in einer Richtlinie definiert werden. Dort müssen Zweck, Ziele und Verhaltensregeln für die Arten von Sicherheits­ vorfällen und für verschiedene Zielgruppen festgelegt werden. Die Richtlinie muss allen Mitarbeitern bekannt, von den relevanten Stellen freigegeben sein und regelmäßig überprüft werden.                                       |
| BSI-118.S 4 118.2      | Schnittstellen (DER.2.1.A2) SOLL           | Schnittstellen zu anderen Managementsysteme wie IT-Notfallmanagement sollten etabliert sein.                                                                                                                                                                                                                                                                                                       |
| BSI-119 3              | Verantwortlichkeiten Reaktion (DER.2.1.A3) | Rollen und Verantwortlichkeiten für Sicherheits­ vorfälle müssen definiert sein, relevante Mitarbeiter müssen über ihre Aufgaben unter­ richtet werden. Ansprechpartner, Regeln, Entscheidungen und Kontakt­ informationen müssen festgelegt sein.                                                                                                                                                 |
| BSI-120 3              | Benachrichtigungen (DER.2.1.A4)            | Relevante interne und externe Stellen müssen über Sicherheits­ vorfälle informiert werden, inklusive Behörden, Datenschutz­ beauftragte, Rechtsabteilung, Mitbestimmung usw. Ebenso müssen mögliche Maßnahmen kommuniziert werden.                                                                                                                                                                 |
| BSI-121 3              | Behebung (DER.2.1.A5)                      | Die Behebung des Sicherheits­ vorfalls muss im IT-Betrieb nach festgelegten Schritte erfolgen. Nach Finden des Problems und der Ursache müssen geeignete Maßnahmen ausgewählt und nach Freigabe durch die IT umgesetzt werden, um die Ursache zu Beheben. Es müssen sichere Kommunikations­ verfahren und Listen interner und externer Experten bestehen.                                          |
| BSI-122 3 122.1, 122.3 | Wiederherstellung (DER.2.1.A6)             | Nach einem Sicherheits­ vorfalls müssen betroffene Systeme vom Netz genommen, Daten gesichert und Hard- und Software auf Veränderungen untersucht werden. Die Wiederherstellung muss dann festgelegten Schritten folgen - Restore von Originaldaten, Konfigurationen und Patches, die nicht vom Vorfall betroffen waren. Zugangsdaten müssen geändert, Nutzer in Funktionstest eingebunden werden. |

<!-- page: 9 -->

| BSI-122.S 4     | Penetrationstests (DER.2.1.A6) SOLL     | Komponenten sollten nach einem Angriff vor der Wiederinbetriebnahme einem Penetrationstest unterzogen werden                                                                                                                                                                                                                                         |
|-----------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 122.2 BSI-123 4 | Vorgehensweise (DER.2.1.A7) SOLL        | Es sollte eine definierte Vorgehensweise zur Behandlung von Sicherheits­ vorfällen geben - mit Prozessen, Vorgaben und Abläufen. Die Vorgehensweise muss allen Beteiligten zugänglich, von der Leitungsebene freigegeben sein und regelmäßig überprüft und angepasst werden.                                                                         |
| BSI-124 4       | Organisationsstruktur (DER.2.1.A8) SOLL | Es sollten geeignete Organisationsstrukturen für den Umgang festgelegt werden, mit Team, geeigneten Mitgliedern und Überprüfung.                                                                                                                                                                                                                     |
| BSI-125 4       | Meldewegen (DER.2.1.A9) SOLL            | Passende Meldewegen für Arten von Vorfällen sollten aufgebaut und kommuniziert werden. Dazu sollte es eine Kommunikations- und Kontaktstrategie geben mit Festlegungen, wer meldeberechtigt ist.                                                                                                                                                     |
| BSI-126 4       | Eindämmen SOLL                          | Es sollte entschieden werden, ob der Vorfall eingedämmt oder aufgeklärt wird, dazu sollten Informationen und Worst Case Szenarien vorliegen.                                                                                                                                                                                                         |
| BSI-127 4       | Einstufung SOLL                         | Sicherheitsvorfälle sollten nach einem einheitlichen Verfahren eingestuft werden, das zwischen ISMS und Incident Management abgestimmt ist.                                                                                                                                                                                                          |
| BSI-128 4       | Schnittstellen SOLL                     | Schnittstellen zwischen Störungsbehebung, Notfallmanagement und ISMS sollten analysiert werden, ebenso gemeinsame Ressourcen. Relevante Mitarbeiter im Betrieb, Service Desk und Fehlerbehebung sollten sensibilisiert werden. Das ISMS sollte lesenden Zugriff auf Incident Management Tools haben.                                                 |
| BSI-129 4       | Einbindung SOLL                         | Behandlung von Sicherheitsvorfällen sollten mit dem Notfallmanagement abgestimmt sein, ggf. auch mit Störungs- und Fehlerbehebung.                                                                                                                                                                                                                   |
| BSI-130 4       | Eskalation (DER.2.1) SOLL               | Eine Eskalationsstrategie sollte Anweisungen für Sicherheits­ vorfälle festlegen, mit ISMS und Störungsmanagement abgestimmt: Einbindung interessierter Parteien, zu ergreifende Maßnahmen, Auswahl geeigneter (und bei Notfällen erreichbarer) Tools und Eskalationswege. Die Strategie sollte regelmäßig überprüft, geübt und aktualisiert werden. |
| BSI-131 4       | Schulungen SOLL                         | Mitarbeitern im Service Design sollten Hilfsmittel zur Verfügung stehen, sie sollten geschult sein und Schutzbedarfe der IT-Systeme kennen.                                                                                                                                                                                                          |
| BSI-132 4       | Dokumentation SOLL                      | Behebung sollte nach einem standardisierten Verfahren dokumentiert werden, die Berichte sollten vertraulich sein. Die Dokumentation sollte vor (formellem) Abschluss des Vorfalls in entsprechenden Systemen gepflegt werden, nach Kriterien abgestimmt mit dem ISB.                                                                                 |
| BSI-133 4       | Nachbereitung SOLL                      | Die Behebung und Reaktion sollte standardisiert ausgewertet werden (Lessons Learned), Maßnahmen und Meldewege bewertet und Handlungs­ anweisungen aus Erfahrungen erstellt und kommuniziert werden. Die Leitungsebene sollte über Vorfälle unterrichtet werden.                                                                                      |
| BSI-134 4       | Weiterentwicklung SOLL                  | Nach der Analyse von Sicherheitsvorfällen sollten Prozesse und Abläufe ggf. weiterentwickelt werden und auch neue Entwicklungen im Incident Management und Forensik geprüft werden, Hilfsmittel sollten überprüft und aktualisiert werden.                                                                                                           |

<!-- page: 10 -->

<!-- image -->

| BSI-135 3    | Automatische Reaktion     | Detektions­ systeme müssen sicherheits­ relevante Ereignisse automatisch melden und in Netzen wenn möglich automatisch reagieren, wenn die kDL nicht gefährdet wird. Dabei muss automatisch in Datenströme eingegriffen werden können, um Sicherheits­ vorfälle zu unterbinden, oder alternativ über manuelle Prozesse.   |
|--------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 135.1, 135.2 |                           | Sicherheits­ vorfälle im 'vermeintlichen Zusammenhang' mit Angriffen müssen behandelt werden.                                                                                                                                                                                                                             |
| BSI-135.S 4  | Auswertung (DER.2.1) SOLL | Sicherheitsvorfälle sollten standardisiert protokolliert und dokumentiert werden. Anforderungen an QS, Vertraulichkeit und ggf. ein DMS sollten berücksichtigt werden.                                                                                                                                                    |

Das OH SzA-Mapping zu ISO 27001, C5 und KRITIS ist in einem eigenen Artikel.

up

## Umsetzung

## Umsetzungsgrad (Reifegrad)

In Prüfungen muss Reifegrad der Systeme zur Angriffserkennung von KRITIS-Prüfern untersucht und in einer Skala von 0 bis 5 in den Nachweis­ formularen bewertet werden (RUN).

## Grad

- 0 Keine Maßnahmen umgesetzt, keine Pläne vorhanden
- 1 Planungen vorhanden, jedoch noch keine konkrete Umsetzung
- 2 Umsetzung wurde in allen Bereichen begonnen, jedoch noch nicht erfüllt
- 3 Alle MUSS-Anforderungen umgesetzt, KVP umgesetzt oder in Planung
- 4 Alle MUSS-Anforderungen umgesetzt, alle SOLL -Anforderungen umgesetzt oder stichhaltig begründet ausgeschlossen, KVP etabliert
- 5 Alle MUSS, SOLL und KANN-Anforderungen umgesetzt oder stichhaltig begründet ausgeschlossen. Sinnvolle zusätzliche Maßnahmen wurden umgesetzt, KVP etabliert.

## Prüfung und Nachweise

Das Mindestniveau ist Reifegrad 3 (UG3), grundsätzlich sollten Betreiber jedoch Reifegrad 4 (MUSS und SOLL ) erreichen, um den Nachweis nach §8a (1a) BSIG zu erbringen. Nachweise müssen Aussagen zum Einsatz von Systemen zur Angriffserkennung enthalten:

1. Nachweisdokument P, Umsetzungsgrad SzA PE.3
2. Mängelliste

## Umsetzung

<!-- page: 11 -->

<!-- image -->

## Weitere Informationen

## Literatur

1. Orientierungshilfe Angriffserkennung OH SzA, OpenKRITIS Briefing, Webinar Oktober 2022
2. [OpenKRITIS-Mapping Orientierungshilfe Angriffserkennung zu KRITIS, C5 und ISO 27001, OpenKRITIS, Oktober 2022](https://www.openkritis.de/r/OpenKRITIS_Mapping_KRITIS-Angriffserkennung.pdf)
3. Fragen und Antworten zum Einsatz von Systemen zur Angriffserkennung, Webseite des BSI, Bundesamt für Sicherheit in der Informationstechnik, o.D.
4. Kritische Infrastrukturen und weitere meldepflichtige Unternehmen: Einen Vorfall bewältigen, Webseite des BSI, Bundesamt für Sicherheit in der Informationstechnik
5. BSI veröffentlicht Orientierungshilfe zum Einsatz von Systemen zur Angriffserkennung, Pressemeldung, Bundesamt für Sicherheit in der Informationstechnik, September 2022

## Quellen

1. Konkretisierung der KRITIS-Anforderungen (§ 8a Absatz 1 und Absatz 1a BSIG), OH SzA, Bundesamt für Sicherheit in der Informationstechnik, September 2024
2. Orientierungshilfe zum Einsatz von Systemen zur Angriffserkennung (PDF), OH SzA, Bundesamt für Sicherheit in der Informationstechnik, September 2022
3. IT-Grundschutz-Baustein (200-1): DER.1: Detektion von sicherheitsrelevanten Ereignissen, Bundesamt für Sicherheit in der Informationstechnik, Februar 2021
4. [IT-Grundschutz-Baustein (200-1): DER.2.1: Behandlung von Sicherheitsvorfällen, Bundesamt für Sicherheit in der Informationstechnik, Februar 2021](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium_Einzel_PDFs_2021/05_DER_Detektion_und_Reaktion/DER_2_1_Behandlung_von_Sicherheitsvorfaellen_Edition_2021.pdf)
5. [OpenKRITIS](https://www.openkritis.de/)
6. [Cybersecurity in KRITIS und NIS2](https://www.openkritis.de/massnahmen/)
7. [Orientierungshilfe Angriffserkennung](https://www.openkritis.de/massnahmen/orientierungshilfe_angriffserkennung_oh_sza.html)
8. up

OpenKRITIS ∙ Die gemeinnützige Informationsplattform für NIS2-Einrichtungen und Kritische Infrastrukturen. 50670 Köln ∙ info@openkritis.de ∙ ISSN 2748-565X

Paul Weissmann ist der Herausgeber von OpenKRITIS und publiziert seit 1999 das PA-RISC-Referenzwerk, und Insel Westberlin. OpenKRITIS hat keinen Anspruch auf Vollständigkeit oder Korrektheit und stellt keine Rechtsberatung dar.

Copyright © 2021-2026 ∙ Impressum ∙ Datenschutz ∙ Über uns und Kontakt

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 6 -->

> Netze, IDS

<!-- page: 7 -->

> Netzsegmente müssen durch 'zusätzliche Detektionssysteme' geschützt werden, Netz­ übergänge durch 'netzbasierte' IDS

<!-- page: 10 -->

> 135.4

> Vorfälle 'im Zusammenhang' mit Angriffen müssen an die zuständigen Behörden gemeldet werden.
