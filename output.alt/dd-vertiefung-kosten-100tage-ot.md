---
source_file: "dd-vertiefung-kosten-100tage-ot.md"
source_sha256: 67771c5d2fd2f5475d143b352e1904d8761b13fb937cca81de33b85aaeee35e5
source_bytes: 6114
pages: 0
tables: 2
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-28T13:19:10+00:00"
extraction_status: ok
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
# DD-Vertiefung: Remediation-Kosten, 100-Tage-Plan, OT-Targets

Zweck: Die drei DD-Handwerksteile, die in der Fachbasis noch fehlten: Findings in EUR übersetzen, den 100-Tage-Plan strukturieren, Industrie-Targets mit OT bewerten. Daumenregeln sind als solche markiert: interne intcube-Erfahrungswerte ab Woche 1 dagegenhalten und dieses Dokument korrigieren. Stand 08/2026.

## 1. Remediation-Kostenschätzung (Findings → EUR)

**Prinzip** : Der Investor braucht eine belastbare Größenordnung in Bandbreiten (low/high), keine Scheinpräzision. Immer trennen: **One-off** (CapEx-artig, verhandelbar am Kaufpreis) vs. **Run-rate** (drückt EBITDA, wirkt über den Multiple gehebelt).

**Schätzlogik pro Finding** : Aufwand = Beratung/Projekt (Personentage × Tagessatz 1.200 bis 1.800 EUR extern) + Lizenzen (pro User/Endpoint/Jahr) + interne Kapazität (oft der Engpass, nicht das Geld) + Zeitfaktor (was bis Closing, was in 100 Tagen, was in Jahr 1).

**Daumenregeln für typische Findings (Mittelstand 100 bis 500 MA, Bandbreiten, Daumenregel nicht Fakt)**

| Finding                                            | One-off                                  | Run-rate p. a.                     |
|----------------------------------------------------|------------------------------------------|------------------------------------|
| MFA flächendeckend (M365/Entra vorhanden)          | 5 bis 20k (Projekt, Ausnahmenbehandlung) | gering (Lizenzstufe)               |
| EDR-Rollout inkl. Tuning                           | 10 bis 30k                               | 25 bis 60 EUR/Endpoint             |
| MDR/SOC-Service                                    | 5 bis 15k Onboarding                     | 50 bis 150k                        |
| Backup-Härtung (immutable, offline, Restore-Tests) | 15 bis 50k                               | 10 bis 30k                         |
| ISMS-Aufbau bis zertifizierungsreif (27001)        | 60 bis 150k über 12 bis 18 Monate        | 20 bis 50k (Betrieb, Audits)       |
| IR-Retainer + Playbooks + Tabletop                 | 15 bis 40k                               | 10 bis 25k Retainer                |
| Vollzeit-Security-Rolle (ISB/CISO)                 | Recruiting                               | 90 bis 140k, Fraktional 30 bis 60k |
| Pentest/ASM-Ersteinrichtung                        | 15 bis 40k                               | 10 bis 40k (kontinuierlich)        |

**Plausibilisierung top-down** : Security-Budget gesunder Mittelständler liegt grob bei 5 bis 10 Prozent des IT-Budgets, IT-Budget grob 2 bis 5 Prozent vom Umsatz (branchenabhängig, Software deutlich höher). Liegt die Summe deiner Findings weit über dem, was das Target je pro Jahr stemmen kann, muss der Plan strecken oder der Preis reagieren: genau das gehört in den Report.

## 2. 100-Tage-Plan: Struktur, die funktioniert

**Formregeln** : maximal 8 bis 10 Maßnahmen. Jede mit Owner (real existierende Person/Rolle beim Target), EUR-Bandbreite, Termin, messbarem Abnahmekriterium. Muss ohne Vollzeit-CISO funktionieren, sonst ist Maßnahme 1 die Besetzung.

| Phase                       | Fokus                                   | Typische Inhalte                                                                                                                                                                                    |
|-----------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tag 0 bis 30: Stabilisieren | Die Tür schließen, durch die alle gehen | MFA auf alle externen Zugänge und Admins, Notfall-Kontaktkette und IR-Retainer, Backup-Restore-Test, Offboarding-Altlasten (Ex-Accounts), Cyber-Police-Obliegenheiten prüfen                        |
| Tag 31 bis 70: Sichtbarkeit | Wissen, was da ist und was passiert     | ASM-Baseline und externe Angriffsfläche reduzieren, EDR-Abdeckung messen und schließen, Logging-Mindeststand für Forensik, kritische Lieferanten inventarisieren                                    |
| Tag 71 bis 100: Struktur    | Vom Projekt zum Betrieb                 | Security-Ownership benennen (intern oder fraktional), Patch- und Vuln-Prozess mit KEV-Priorisierung, Regulatorik-Fahrplan (BSIG-Registrierung, DORA-Register, CRA-Timeline), Board-Reporting-Format |
| Danach: Jahr 1              | Aus dem DD-Report                       | ISMS-Aufbau, Zertifizierungsziel, Kohorten-Teilnahme, Reifegrad-Messung                                                                                                                             |

Verzahnung mit dem Deal: Tag-0-bis-30-Punkte sind Kandidaten für Conditions Precedent oder Closing-nahe Covenants; alles mit EUR-Bandbreite gehört parallel in die Preis-/Escrow-Verhandlung (siehe PE-Dokument, Eskalationsleiter).

## 3. OT/ICS bei Industrie-Targets (IEC-62443-Schnellbasis)

Warum relevant: PE kauft Mittelstand, Mittelstand ist oft produzierend. Eine DD, die nur Office-IT prüft, übersieht den Teil, der bei Ransomware den Umsatz stoppt (Produktionsstillstand ist der teuerste Schadenstreiber, oft teurer als Datenabfluss).

**Vokabular** : OT (Operational Technology), ICS/SCADA, PLC/SPS, HMI, Historian. Purdue-Modell Level 0 bis 4 als Referenzarchitektur (0 bis 2 Prozess/Steuerung, 3 Betriebsleitebene, 3.5 DMZ, 4 Unternehmens-IT). IEC 62443: Zonen und Conduits (Segmentierung nach Risiko), Security Level SL1 bis SL4, Rollen (Asset Owner, Integrator, Produkthersteller: 62443-2-1, -3-3, -4-1/-4-2).

**DD-Prüffragen OT (ergänzt die 10 Domänen)**

- Segmentierung: Ist Produktion von Office-IT getrennt (eigene Zone, kontrollierte Übergänge), oder flach vernetzt? Flaches Netz = Red Flag Nummer 1.
- Fernzugriffe: Wartungszugänge von Maschinenherstellern (TeamViewer, eigene Router im Schaltschrank!): inventarisiert, MFA, protokolliert?
- Altsysteme: Windows-Versionen ohne Support an Maschinen mit 20 Jahren Lebensdauer sind normal; Frage ist Kompensation (Segmentierung, Virtual Patching), nicht Patch-Illusion.
- Verfügbarkeit vor Vertraulichkeit: RTO je Linie bekannt? Wiederanlaufplan getestet? Was kostet ein Stillstandstag (Zahl vom CFO holen: sie gehört in den Report)?
- Backup der Steuerungsprogramme (PLC-Projekte, Rezepturen): existiert, liegt es offline, kann ein Integrator wiederherstellen?
- Regulatorik: produzierende NIS2-Sektoren (Anlage 1/2 BSIG: verarbeitendes Gewerbe je nach NACE), Maschinenbauer als Zulieferer der Automotive-Kette (TISAX), Produkte mit digitalen Elementen (CRA trifft Maschinenbauer mit vernetzten Produkten hart).

**Grenzlinie (ehrlich halten)** : Du bewertest OT-Governance, Segmentierungslogik und Prozessreife; ein OT-Pentest oder eine 62443-Detailbewertung braucht Spezialisten. Genau so im Report kennzeichnen: seriöser Scope-Hinweis, keine Schwäche.

## 4. Gesprächssätze

- "Die Summe der Findings übersteigt das realistische Jahresbudget des Targets: der Plan streckt auf 24 Monate oder der Preis reagiert."
- "Ein Stillstandstag kostet hier sechsstellig. Die wichtigste Backup-Frage ist nicht die Datenbank, sondern das SPS-Programm."
- "Der Wartungsrouter des Maschinenherstellers ist ein Fernzugriff ohne Vertrag. Das ist Third-Party-Risiko in Reinform."
- "100-Tage-Plan heißt: 8 Maßnahmen, 8 Owner, 8 Abnahmekriterien. Alles andere ist ein Wunschzettel."
