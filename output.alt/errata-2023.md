---
source_file: "errata_2023.pdf"
source_sha256: f5c12c5cda02225e88e11ebc103fea22626209e6f208467c597be9a53d24161d
source_bytes: 120688
pages: 3
tables: 6
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T21:17:29+00:00"
text_coverage_percent: 100.0
restored_hyphens: 1
extraction_status: warn
warnings:
  - "1 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): ITGrundschutz -> IT-Grundschutz"
  - "Der Textlayer der Quelle enthaelt 2 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

## Errata zum IT-Grundschutz-Kompendium Edition 2023

Stand: 26. März 2026

In diesem Dokument werden Fehler zum IT-Grundschutz-Kompendium 2023 aufgeführt, die nach Redaktionsschluss und Drucklegung bekanntgeworden sind und nicht mehr in die aktuelle Edition einfließen konnten.

Die hier aufgeführten Korrekturen ersetzen bzw. ergänzen die entsprechenden Stellen im IT-Grundschutz-Kompendium und sind verbindlich anzuwenden.

## Modellierung

Die folgende Zuordnung von Bausteinen zu Zielobjekten ist korrekt:

| Baustein                           | Reihenfolge   | Anzuwenden auf Zielobjekt   |
|------------------------------------|---------------|-----------------------------|
| OPS.1.2.6 NTP -Zeitsynchronisation | R2            | Anwendung IT-System         |

## SYS.1.2.3 Windows Server

## 3.2. Standard-Anforderungen

Folgende Anforderungsnummer ist korrekt:

| Verwendete Anforderungsnummer                                                  | Korrekte Anforderungsnummer                                                    |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| SYS.1.2. 2 .A5 Sichere Authentisierung und Autorisierung in Windows Server (S) | SYS.1.2. 3 .A5 Sichere Authentisierung und Autorisierung in Windows Server (S) |

<!-- page: 2 -->

## SYS.2.2.3 Clients unter Windows

## SYS.2.2.3.A6 Integration von Online-Konten in das Betriebssystem (B)

In der ersten Teilanforderung ist das verwendete Modalverb nicht korrekt:

| Verwendetes Modalverb                                                                                                         | Korrektes Modalverb                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Die Anmeldung am System sowie an der Domäne DARF NUR mit dem Konto eines selbst betriebenen Verzeichnisdienstes möglich sein. | Die Anmeldung am System sowie an der Domäne SOLLTE nur mit dem Konto eines selbst betriebenen Verzeichnisdienstes möglich sein. |

## CON.11.1 Geheimschutz VS-NUR FÜR DEN DIENSTGEBRAUCH (VSNfD)

## Kapitel 1.3 Abgrenzung und Modellierung

| Bisherige Abgrenzung                                                                                                                 | Überarbeitete Abgrenzung                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dieser Baustein richtet sich an Bundesbehörden oder bundesunmittelbare öffentlich-rechtliche Einrichtungen, die der VSA unterliegen. | Dieser Baustein richtet sich ausschließlich an Bundesbehörden oder bundesunmittelbare öffentlich-rechtliche Einrichtungen, die der VSA unterliegen. Der Baustein ist von Unternehmen und Landesbehörden nicht anzuwenden. |

## CON.10 Entwicklung von Webanwendungen

## 3.1. Basis-Anforderungen

## CON.10.A7 Schutz vertraulicher Daten (B)

Die ursprüngliche Formulierung beschränkte die Übertragung vertraulicher Daten unnötig auf die http-Post-Methode und war damit zu restriktiv. Die Anpassung erweitert die Übertragung im Body eines http-Requests.

| Bisherige Basis-Anforderung                                                                                                                     | Überarbeitete Basis-Anforderung                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Die Entwickelnden MÜSSEN sicherstellen, dass vertrauliche Daten von den Clients zu den Servern nur mit der http-Post-Methode übertragen werden. | Die Entwickelnden MÜSSEN sicherstellen, dass vertrauliche Daten von den Clients zu den Servern nur im Body eines http-Requests übertragen werden. |

<!-- page: 3 -->

## Kreuzreferenztabellen zum IT-Grundschutz-Kompendium (Edition 2023)

## INF.2 Rechenzentrum sowie Serverraum

Die folgenden Anforderungen müssen statt zu G 0.0 der elementaren Gefährdung G 0.4 zugeordnet werden:

## G 0.4 Verschmutzung, Staub, Korrosion

| Anforderung   | G 0.0   | G 0.4   |
|---------------|---------|---------|
| INF.2.A13     |         | X       |
| INF.2.A29     |         | X       |
