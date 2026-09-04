---
source_file: "cti-threat-intelligence-fachbasis.md"
source_sha256: 84655603927c229acd74f2c026f5e9d8c6a568b7c0071e0e143b0880ee4fe7ea
source_bytes: 4599
pages: 0
tables: 1
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-28T13:19:10+00:00"
extraction_status: ok
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
# Threat Intelligence: Auswahl und Integration (Fachbasis)

Zweck: intcube nennt "Auswahl von Threat-Intelligence-Providern und Prozessintegration" als Consulting-Leistung; bisher null Abdeckung in der Wissensbasis. Dieses Dokument macht in einem Kundengespräch und einem Auswahlprojekt sattelfest. Stand 08/2026.

## 1. CTI in drei Ebenen (das Ordnungsschema für jedes Gespräch)

| Ebene             | Inhalt                                                    | Konsument                          | Beispiel-Artefakt                           |
|-------------------|-----------------------------------------------------------|------------------------------------|---------------------------------------------|
| Strategisch       | Bedrohungslage je Branche/Region, Akteursmotive, Trends   | Geschäftsführung, Risikomanagement | Quartalsbericht, Lagebild für Board         |
| Operativ/Taktisch | TTPs von Akteuren (MITRE ATT&CK), Kampagnen, Vorwarnungen | SOC-Leitung, IR-Team, Vuln Mgmt    | Akteursprofile, ATT&CK-Mappings, Advisories |
| Technisch         | IoCs: Hashes, IPs, Domains, Signaturen                    | SIEM/EDR/Firewall (maschinell)     | Feeds via STIX/TAXII, MISP-Events           |

Merksatz: Feeds sind billig, Einordnung ist teuer. Der Mittelstand kauft meist Ebene 3 und braucht Ebene 1 und 2.

## 2. Quellenlandschaft

- Offen/kostenlos: BSI (CERT-Bund, WID-Advisories, Allianz für Cybersicherheit), CISA KEV-Katalog (Known Exploited Vulnerabilities: bester Patch-Priorisierer, kostenlos), abuse.ch (URLhaus, MalwareBazaar, Feodo), MISP-Communities, Hersteller-Blogs (Microsoft MSTIC, Google/Mandiant, Cisco Talos).
- Sharing-Kreise: CERT-Verbund, Branchen-ISACs, UP KRITIS Branchenarbeitskreise, DCSO-Community (Dror kennt die Innensicht: DCSO wurde von deutschen Konzernen genau dafür gegründet).
- Kommerziell (Beispiele zur Einordnung, keine Empfehlung): Recorded Future, Mandiant/Google, CrowdStrike, Intel471, ZeroFox/Darknet-Monitoring, EclecticIQ/Threatray (EU-Anbieter als Souveränitätsargument).
- Eingebettet: die CTI, die im vorhandenen EDR/SIEM-Stack schon drinsteckt und oft ungenutzt bleibt: erste Prüffrage jedes Auswahlprojekts.

## 3. Auswahlprojekt in 5 Schritten (Beratungsablauf)

1. **Anforderungen aus Risiken, nicht aus Features** : Welche Entscheidungen sollen mit CTI besser werden? (Patch-Priorisierung, Detection-Regeln, Lagebild, Brand/Leak-Monitoring, M&amp;A-Screening). Priority Intelligence Requirements (PIRs) schriftlich festhalten.
2. **Bestandsaufnahme** : Was liefern EDR/SIEM/Firewall-Hersteller bereits? Welche Formate kann der Stack konsumieren (STIX/TAXII, API, MISP)? Wer soll CTI lesen: gibt es überhaupt einen Konsumenten?
3. **Shortlist und PoC** : 2 bis 3 Anbieter, 4 bis 6 Wochen Test gegen definierte PIRs. Bewertung: Relevanz für die eigene Branche/Region (DACH-Abdeckung!), False-Positive-Quote der Feeds, Latenz, Sprache, Integrationstiefe, Preisstruktur (pro Nutzer, pro Feed, Enterprise).
4. **Integration** : IoCs automatisiert in SIEM/EDR (mit Ablaufdatum, sonst Alert-Müll), Advisories in Vuln-Mgmt-Prozess (KEV-Abgleich), Lagebild in Risiko-/Board-Reporting. Ownership benennen: ohne benannten CTI-Verantwortlichen verrottet jeder Feed.
5. **Wirksamkeitsmessung** : Anteil Detections mit CTI-Bezug, Patch-Priorisierungsentscheidungen auf KEV/CTI-Basis, Time-to-Awareness bei branchenrelevanten Kampagnen. Jährliche Renewal-Entscheidung gegen diese Zahlen.

## 4. Mittelstands-Empfehlungslogik (ehrlich, Manifesto-konform)

Reihenfolge des Nutzens pro Euro: 1. KEV-Katalog + CERT-Bund/WID in den Patch-Prozess (kostenlos, sofort), 2. vorhandene EDR/SIEM-Intel aktivieren, 3. Branchen-Sharing (ISAC/UP KRITIS) beitreten, 4. erst dann kommerzieller Anbieter, und nur mit benanntem Konsumenten. Ein 40-Personen-Betrieb mit kommerziellem CTI-Abo ohne SOC ist Geldverbrennung: das offen zu sagen ist der intcube-Stil.

## 5. Regulatorische Anker

- NIS2/BSIG: Risikoanalyse "auf dem Stand der Technik" und Umgang mit Schwachstellen implizieren Bedrohungsinformationen; CSIRTs liefern Lageinformationen, Empfang muss organisiert sein.
- DORA Art. 13/45: Finanzunternehmen müssen Cyber-Bedrohungsinformationen auswerten; Sharing-Arrangements ausdrücklich vorgesehen; TLPT (TIBER-EU/DE) ist Threat-Intelligence-geführtes Testen: CTI-Reife ist Voraussetzung.
- ISO 27001:2022 A.5.7 "Threat intelligence": expliziter Control, Auditoren fragen nach Prozess, Quellen und Nutzungsnachweis, nicht nach Abo-Rechnung.
- IT-Grundschutz: Lageinformationen in DER-Bausteinen und über CERT-Bund-Anbindung.

## 6. Gesprächssätze

- "Ein Feed ohne benannten Leser ist ein Abo, kein Schutz."
- "Die günstigste Threat Intelligence steckt schon in Ihrem EDR. Nutzen Sie die erst."
- "KEV-Abgleich kostet nichts und beantwortet die wichtigste Frage: was wird gerade wirklich ausgenutzt."
- "A.5.7 verlangt keinen Anbieter, sondern einen Prozess."
