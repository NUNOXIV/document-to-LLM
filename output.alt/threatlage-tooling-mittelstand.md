---
source_file: "threatlage-tooling-mittelstand.md"
source_sha256: 8b857b3f62a673ff17d072df9c7729009d3edf30f98ce40935868f9c7b4569de
source_bytes: 5848
pages: 0
tables: 2
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-28T13:19:11+00:00"
extraction_status: warn
warnings:
  - "2 Tabellenzelle(n) beginnen mitten im Satz — moegliche Zellverschiebung, z. B. \"subfinder, amass, dnsx, httpx...\". Zeilen dieser Tabelle vor dem Zitat gegen die Quelle pruefen."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
# Threat-Lage und Tooling-Kontext Mittelstand

Zweck: Belastbare Zahlen für Kundengespräche und das technische Vokabular, um in ASM-, IR- und SOC-Diskussionen mitzuhalten, ohne selbst Findings zu erzeugen. Ergänzt die Fachbasis der Servicebereiche. Stand 08/2026; Zahlen mit Quelle, vor Kundenaussage aktualisieren.

## 1. Kernzahlen BSI-Lagebericht 2025 (Berichtszeitraum 07/2024 bis 06/2025)

| Zahl                                                                                         | Aussage                                             | Verwendung im Gespräch                                                  |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|-------------------------------------------------------------------------|
| 119 neue Schwachstellen pro Tag (+24 % ggü. Vorjahr; 2022: 68, 2024: 96)                     | Angriffsfläche wächst schneller als Patch-Kapazität | Begründet kontinuierliches ASM statt Jahres-Pentest                     |
| 950 Ransomware-Fälle, ca. 80 % davon KMU                                                     | Mittelstand ist Hauptziel, nicht Kollateralschaden  | Entkräftet "wir sind zu klein, um interessant zu sein"                  |
| Meist mit Datenabfluss oder Erpressungsdrohung                                               | Double Extortion ist Standard                       | Backup allein reicht nicht, Exfiltration ist das zweite Erpressungsbein |
| KMU erfüllen im Schnitt nur 56 % der Basis-Anforderungen und überschätzen sich               | Gefühlte vs. reale Sicherheit klaffen auseinander   | Argument für Messung (Kohorten-KPI) statt Selbstauskunft                |
| KRITIS: 80 % ISMS, 66 % BCM, 48 % Angriffserkennung auf gefordertem Reifegrad                | Selbst Regulierte hinken bei Detection              | SzA-Pflicht (§8a BSIG) ist der wunde Punkt, auch in der DD              |
| 25 % der beobachteten APT-Kampagnen zielen auf Deutschland; 800+ neue Phishing-Sites täglich | Professionalisierung, CaaS/RaaS-Ökonomie            | Einordnung, kein Alarmismus                                             |

Quelle: BSI, Die Lage der IT-Sicherheit in Deutschland 2025 (11/2025). Merkposten: Lagebericht 2026 erscheint voraussichtlich 11/2026, Zahlen dann austauschen.

## 2. Ransomware-Ökonomie in 90 Sekunden erklärt

Arbeitsteilung: Initial Access Broker verkaufen Zugänge (Phishing, gestohlene Credentials, exponierte VPN/RDP ohne MFA, ungepatchte Edge-Geräte). RaaS-Betreiber liefern Schadsoftware und Infrastruktur gegen Umsatzbeteiligung, Affiliates führen aus. Ablauf beim Opfer: Zugang → Privilegien-Ausweitung → Lateral Movement → Exfiltration → Verschlüsselung → Verhandlung über Leak-Site. Konsequenz für Beratung: Die drei billigsten wirksamen Hebel sind MFA überall (v. a. extern erreichbare Dienste), gehärtete und offline-fähige Backups, gepatchte Perimeter-Geräte. Das deckt die Mehrzahl der realen Einstiegswege: exakt die Logik der intcube-Kohortenthemen.

## 3. ASM-Tooling-Landkarte (mitreden, nicht bedienen)

| Kategorie                       | Beispiele                                                                | Was es liefert                                                     |
|---------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------|
| Internet-Scan-Datenbanken       | Shodan, Censys, BinaryEdge                                               | Passive Sicht auf exponierte Dienste, Zertifikate, Banner          |
| Subdomain/Asset Discovery (OSS) | subfinder, amass, dnsx, httpx                                            | Inventar aus DNS, CT-Logs, ASN-Räumen                              |
| Schwachstellen-Templates (OSS)  | nuclei                                                                   | Schnelle, reproduzierbare Checks auf bekannte Lücken               |
| Kommerzielle EASM-Plattformen   | z. B. Sweepatic/Outpost24, CyCognito, Detectify, Microsoft Defender EASM | Kontinuierliches Monitoring, Scoring, Reporting: Kohorten-tauglich |
| Leak-/Breach-Quellen            | HaveIBeenPwned, Dehashed, Darknet-Monitoring der CTI-Anbieter            | Kompromittierte Credentials als Frühindikator                      |
| Schwachstellen-Scanner (innen)  | Nessus/Tenable, Qualys, OpenVAS/Greenbone                                | Inside-out-Sicht, Abgrenzung zu EASM (outside-in)                  |

Prüffragen an jedes ASM-Ergebnis: Wie wurde das Inventar erzeugt (Seed-Qualität)? Wie werden False Positives und geteilte Infrastruktur (CDN, Shared Hosting) behandelt? Wird Reduktion gemessen oder nur Findings-Zählung? Normalisierung über Firmengröße (pro exponiertem Asset, nicht absolut)?

## 4. Detection- und Response-Stack (Vokabular für IR-Readiness und DD-Domäne 7)

- **EDR/XDR** : Endpoint-Sensorik mit Response (Defender for Endpoint, CrowdStrike, SentinelOne). DD-Frage: Abdeckungsgrad in Prozent der Endpunkte und Server, nicht Produktname.
- **SIEM** : Log-Zentralisierung und Korrelation (Sentinel, Splunk, Elastic, Wazuh als OSS: intcube pflegt einen Wazuh-Fork). DD-Frage: Welche Quellen sind angebunden und wie lange ist Retention: reicht es für Rekonstruktion?
- **SOC/MDR/MSSP** : Wer schaut 24/7 auf die Alarme? Mittelstandsrealität: MDR-Dienstleister statt eigenem SOC. Prüffrage: Reaktionszeit vertraglich? Eskalationsweg getestet?
- **SzA (§8a BSIG)** : für KRITIS verpflichtende Systeme zur Angriffserkennung, BSI-Orientierungshilfe definiert Reifegrade (Lagebericht: nur 48 % auf Soll): wiederkehrendes Beratungs- und DD-Thema.
- **NDR, Honeypots, Canary Tokens** : Netzwerksensorik und Stolperdrähte; billige Readiness-Quick-Wins für KMU.
- **IR-Retainer** : vorverhandelter Incident-Response-Vertrag mit Forensik-Dienstleister; Versicherer verlangen oder stellen ihn. DD-Red-Flag: kein Retainer, keine Forensik-Fähigkeit, Logs zu kurz.

## 5. Cyber-Versicherung: Marktlogik für Beratung und DD

Versicherer sind faktisch Regulator des Mittelstands geworden: Fragebögen erzwingen MFA, EDR, Backup-Konzepte, sonst keine Police oder Ausschlüsse. Prüfpunkte: Obliegenheiten der Police vs. gelebte Realität (Deckungslücke bei Falschangaben), Sublimits für Ransomware und Betriebsunterbrechung, Ausschlüsse (Krieg/State Actor-Klauseln), Meldefristen an den Versicherer parallel zu NIS2/DSGVO-Fristen. Im Deal-Kontext: W&amp;I- und Cyber-Police sauber trennen (siehe PE-Dokument).

## 6. Einordnungssätze für Kundengespräche

- "119 neue Schwachstellen pro Tag heißt: Nicht das Finden ist knapp, das Schließen ist knapp."
- "80 Prozent der Ransomware-Opfer sind Mittelstand. Zielauswahl läuft über offene Türen, nicht über Firmengröße."
- "Ihr Backup beantwortet die Verschlüsselung. Was beantwortet die Veröffentlichung Ihrer Daten?"
- "Ein SIEM ohne definierte Reaktionswege ist ein Archiv, kein Schutz."
- "Die Versicherung ersetzt kein Control. Sie prüft nur nach dem Vorfall, ob Sie eines hatten."
