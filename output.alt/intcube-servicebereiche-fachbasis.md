---
source_file: "intcube-servicebereiche-fachbasis.md"
source_sha256: 56581fb3d5ec36f43a60739086a12432c380141b31c02cef5e07fb24e9fb9b23
source_bytes: 7242
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
# intcube-Servicebereiche: Fachbasis

Zweck: Pro Servicebereich in 2 Minuten sattelfest sein: was es ist, wie es methodisch läuft, welche Regulatorik dranhängt, welche Fallstricke drohen. Ergänzt die Drive-Ablage (dort fehlen DD-Methodik, ASM und IR-Readiness bislang komplett). Stand 08/2026. Interne intcube-Templates ab Woche 1 gegen dieses Dokument abgleichen und es korrigieren.

## 1. Cyber Due Diligence (PE/M&amp;A, buy-side)

**Was** : Bewertung der Cyber-Lage eines Targets vor Investment. Output: fokussierter Report mit Red Flags, Investitionsbedarf (EUR), Stärken, 100-Tage-Plan. intcube: 50+ Projekte, kein Onboarding-Vorlauf.

**Die 10 intcube-Prüfdomänen mit Leitfrage**

| Domäne                     | Leitfrage                                                               | Typische Red Flag                                               |
|----------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------|
| Governance                 | Wer wacht nachts wegen Cyber-Risiko auf?                                | Verantwortung outgesourct, keine Roadmap, keine Board-Berichte  |
| IAM                        | Trust is not a control: wer kommt an Prod, Finanzen, Code, Kundendaten? | Kein MFA auf Admin, geteilte Accounts, Ex-Mitarbeiter aktiv     |
| External Attack Surface    | Was ist wirklich exponiert (nicht: was glaubt man)?                     | Kein Inventar, RDP/VPN ungeschützt, vergessene Subdomains       |
| Vulnerability Management   | Wird gefunden UND geschlossen?                                          | Scans ohne Remediation-Ownership, Ausnahmen ohne Ablauf         |
| Produkt-/Tech-Security     | Kann man dem Kernprodukt trauen?                                        | Keine Secrets-Verwaltung, kein Pentest, keine Mandantentrennung |
| Datenschutz                | Welche Daten, wo, wer, wie lange?                                       | Unverschlüsselte Backups, keine Datenflüsse dokumentiert        |
| Incident Response          | Plan getestet? Scar with no lesson?                                     | Vorfall ohne Konsequenzen, Logging reicht nicht für Forensik    |
| Third Party / Supply Chain | Outsourcing transfers tasks, rarely risk                                | Kritischer Einzeldienstleister, Verträge ohne Security-Klauseln |
| Backups & Resilience       | Wiederherstellung geprobt oder gewünscht?                               | Backups im Admin-Zugriff, nie restauriert, keine RTO/RPO        |
| Versicherung & Compliance  | Deckt die Police, was behauptet wird?                                   | Obliegenheiten nicht erfüllt, Zertifikat ohne gelebte Controls  |

**Regulatorik-Dimension (eigenes Modul)** : Betroffenheit als Bewertungsfaktor: BSIG-Einstufung (besonders wichtig/wichtig/KRITIS) mit Registrier- und Nachweispflichten; DORA bei Finanzbezug (auch als ICT-Dienstleister eines Finanzunternehmens!); CRA bei Produkten mit digitalen Elementen (Übergangsfristen = CapEx nach Closing); AI Act bei KI-Komponenten (Anbieter- vs. Betreiberrolle); DSGVO-Altlasten als Contingent Liability. Übersetzung immer in EUR und Zeit bis Pflichttermin.

**Fallstricke** : Zeitfenster 1 bis 3 Wochen, Datenraum lückenhaft, Management schönt, kein Systemzugriff. Gegenmittel: Evidenzhierarchie (Konfiguration &gt; Ticket &gt; Policy &gt; Aussage), externe Sicht (ASM-Scan geht ohne Zugang), Fragen nach dem letzten Vorfall statt nach der Policy.

## 2. Unconsulting in Kohorten (6 bis 8 Wochen, Mittelstand/PE-Portfolio)

**Mechanik** : Mehrere Firmen, ein Thema, wöchentliche Expertensessions, individuelle Umsetzung zwischen den Sessions, KPI vorher/nachher, Abschlussreport mit Benchmark. Preis ca. 1/3 unter klassischer Beratung. Referenz: 19 Firmen, minus 68 % externe Angriffsfläche in 8 Wochen.

**Warum es funktioniert** : Peer-Druck ersetzt Berater-Druck, Benchmark erzeugt Wettbewerb, fester Endtermin erzwingt Priorisierung, Manifesto-Logik (befähigen statt abhängig machen).

**Woran es scheitert** : Dropout ab Woche 4 (Alltag schlägt zurück), heterogene Reifegrade (die Schwächsten bremsen, die Stärksten langweilen sich), KPI-Kosmetik (Zahl sinkt, Risiko nicht).

### 2a. Attack Surface Management (Kohortenthema)

Kern: Inventar aller internetexponierten Assets (Domains, Subdomains, IPs, Zertifikate, Dienste, Cloud-Ressourcen, Schatten-IT), kontinuierlich statt einmalig. Ablauf: Discovery (passiv: DNS, CT-Logs, ASN; aktiv: Portscan, Service-Fingerprinting) → Bewertung (Kritikalität, Exploitability) → Reduktion (abschalten, patchen, hinter VPN/WAF) → Wiederholungsmessung. KPI-Kandidaten: exponierte Dienste gesamt, kritische Findings, mittlere Zeit bis Schließung, Anteil unbekannter Assets. Messfrage, die Profis stellen: Wie wird über unterschiedlich große Firmen normalisiert und wie werden False Positives behandelt? Regulatorik-Anker: NIS2 Art. 21(2)e (Schwachstellenmanagement), §8a BSIG SzA-Bezug, CIS Controls 1/2/7, Grundschutz OPS.1.1.3.

### 2b. Incident Response Readiness (Kohortenthema)

Kern: Nicht Vorfall verhindern, sondern Reaktionsfähigkeit herstellen. Bausteine: IR-Plan (Rollen, Eskalation, Erreichbarkeit 24/7), Meldeprozesse (NIS2: 24h Frühwarnung, 72h Meldung, 1 Monat Abschlussbericht; DSGVO 72h; DORA eigene Taktung; Versicherer-Obliegenheiten), Logging-Mindeststand (kann man einen Vorfall überhaupt rekonstruieren?), Tabletop-Übung als Abschluss-KPI. Referenzrahmen: BSI 200-4 (BCM-Anbindung), NIST SP 800-61, Grundschutz DER.2. KPI-Kandidaten: Zeit bis Erstentscheidung im Tabletop, Vollständigkeit Kontaktkette, Log-Abdeckung kritischer Systeme. Fallstrick: Plan ohne Übung ist Papier; Übung ohne Management-Beteiligung ist Theater.

### 2c. NIS-2 Quick Wins (Kohortenthema)

Kern: In 6 bis 8 Wochen von Nichts zu belastbarem Fundament: Betroffenheitsanalyse und Registrierung, Verantwortlichkeiten und Leitungs-Governance (Billigung, Schulung), Risikoanalyse light, Meldeprozess, MFA/Backup/Patch-Basishygiene, Lieferantenüberblick. Abgrenzung: Quick Wins schaffen Meldefähigkeit und Startpunkt, kein vollständiges Art.-21-Programm; die Linie ehrlich ziehen ist Manifesto-Pflicht. Conversion-Logik: aus Kohorte wird Einzelmandat (ISMS-Aufbau, Nachweisvorbereitung).

## 3. Consulting (klassisch)

Themen laut Referenzen: Cybersecurity-Strategie, ISMS (ISO 27001, IT-Grundschutz, NIST, CIS), NIS2-Compliance (Stromnetz Berlin: KRITIS/Energie), Threat-Intel-Auswahl, BCM, Team-Building, DORA/CRA-Beratung, Interim Security Management. Arbeitsweise laut Selbstbeschreibung: zuhören, co-kreieren, funktionierende statt papierkonformer Lösungen. Eigene Heimzone (Bechtle/IONOS-Profil): ISMS-Aufbau, Nachweisstrukturen, Behörden/KRITIS, C5, Geheimschutz-Nähe.

## 4. Cybersecurity für PE-Portfolios

Kern: Investor kauft Sicherheit als Portfolio-Steuerung: jährliche KPI-Berichte über alle Beteiligungen, Vergleichbarkeit zwischen Firmen, ESG-Reporting-Tauglichkeit, Kohorten als Umsetzungsvehikel. Politisches Kernproblem: Mandat kommt vom Investor, Umsetzung braucht die Geschäftsführung der Portfoliofirma; ohne deren Eigeninteresse wird es Compliance-Theater (Manifesto-Konflikt: Fairness/Transparenz). Wertlogik für den Investor: Cyber-Reife als Werttreiber beim Exit, DD-Findings des Einkaufs werden 100-Tage-Plan der Beteiligung.

## 5. Servicebereich-übergreifende Verbindungen

- DD → 100-Tage-Plan → Kohorte oder Einzelmandat: der Umsatzmotor; Übergänge aktiv steuern.
- ASM-Kohorte liefert die External-Attack-Surface-Daten, die in DD und Portfolio-Reporting wiederverwendet werden: ein Tooling, drei Produkte.
- IR-Readiness bedient gleichzeitig NIS2-Meldepflicht, DORA-Anforderungen, Versicherungs-Obliegenheiten und DD-Domäne 7: ein Deliverable, vier Nachweise.
- Regulatorik-Schnellreferenz (separates Dokument) liefert die Brücken-Sätze für alle Bereiche.
