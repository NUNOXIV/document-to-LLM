---
source_file: "regulatorik-querverbindungen-schnellreferenz.md"
source_sha256: eb8a8671fe562c74cee3574f31771ed2cf043d5c1f662b1b192695428c301a58
source_bytes: 7445
pages: 0
tables: 3
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-28T13:19:11+00:00"
extraction_status: ok
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
# Regulatorik-Querverbindungen: Schnellreferenz für Beratungsgespräche

Zweck: Zusammenhänge zwischen Regularien in einem Satz artikulieren können. Aufbau: pro Achse die Brücke, dann die Detailtabelle. Stand 08/2026. Bei Stichtagen und Schwellenwerten vor Kundenaussage aktuell verifizieren (Regel: nie aus dem Gedächtnis).

## 1. Die Landkarte in drei Ebenen

| Ebene                                       | Instrumente                                                                               | Funktion                                            |
|---------------------------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------|
| EU-Recht (horizontal)                       | NIS2, CER, CRA, CSA, AI Act, DSGVO, Data Act, eIDAS 2.0                                   | Pflichten nach Marktrolle und Sektor                |
| EU-Recht (sektoral)                         | DORA (Finanz), NCCS (Strom), UNECE R155/156 (Automotive-Typgenehmigung)                   | Lex specialis, verdrängt oder konkretisiert NIS2    |
| Nationale Umsetzung DE                      | BSIG (NIS2UmsuCG), KRITIS-DachG (CER), BSI-KritisV, EnWG §11                              | Betroffenheit, Registrierung, Nachweise, Sanktionen |
| Normen/Frameworks (freiwillig, beweisfähig) | ISO 27001/27002/22301/31000/42001, IT-Grundschutz, C5, TISAX, IEC 62443, NIST CSF/SP, CIS | Wie man Pflichten umsetzt und nachweist             |

Merksatz: Gesetze sagen DASS und WAS GROB, Normen sagen WIE, Testate/Zertifikate sagen BEWIESEN.

## 2. Die zehn wichtigsten Brücken (je ein Satz)

1. **NIS2 → ISO 27001** : Art. 21 NIS2 verlangt Risikomanagement-Maßnahmen, die ein 27001-ISMS strukturell bereits abdeckt; ein zertifiziertes ISMS ist der schnellste Nachweisrahmen, ersetzt aber weder Registrierung noch Meldepflichten noch die persönliche Billigungs- und Schulungspflicht der Leitung.
2. **NIS2 → DORA** : DORA ist für Finanzunternehmen lex specialis (NIS2 Art. 4); wer DORA erfüllt, diskutiert mit der BaFin, nicht mit dem BSI, aber Konzerntöchter außerhalb des Finanzsektors können trotzdem unter BSIG fallen.
3. **NIS2 → CRA** : NIS2 reguliert Betreiber, CRA reguliert Produkte mit digitalen Elementen; ein Hersteller kann beides gleichzeitig sein, und CRA-konforme Produkte (Security Updates, SBOM, Schwachstellenmeldung) entlasten die NIS2-Lieferkettenpflicht seiner Kunden.
4. **NIS2 → CER/KRITIS-DachG** : NIS2/BSIG deckt Cyber, CER/KRITIS-DachG deckt physische Resilienz; kritische Anlagen brauchen beides, und das Dachgesetz zieht Registrierung und Resilienzplan nach, wo bisher nur IT-Sicherheit gefordert war.
5. **ISO 27001 → IT-Grundschutz** : Grundschutz ist die deutsche, maßnahmenkonkrete Implementierung derselben ISMS-Logik; 27001-Zertifikat auf Basis IT-Grundschutz bedient beide Welten, kostet aber Modellierungsaufwand, den der Mittelstand oft scheut.
6. **ISO 27001 → C5** : C5 ist kein Zertifikat, sondern ein Prüfbericht (ISAE 3000) über Cloud-Controls; er wirkt in der Lieferkette als Evidenz und wird von Behördenkunden (und zunehmend Versicherern) als Eintrittskarte verlangt.
7. **ISO 27001 → TISAX** : TISAX (VDA ISA) ist das Assessment-Ökosystem der Automotive-Lieferkette auf 27001-Basis mit eigenen Reifegraden und Labels; ohne Label kein OEM-Geschäft, mit 27001 allein auch nicht.
8. **AI Act → ISO 42001** : Der AI Act verlangt für Hochrisiko-Systeme ein Qualitäts- und Risikomanagement, das ISO 42001 als AIMS operationalisiert; 42001 dockt an ein bestehendes 27001-ISMS an (gleiche HLS), statt daneben zu stehen.
9. **DORA → ISO 22301/BSI 200-4** : DORAs digitale operationale Resilienz (Testing, ICT-BCM, Exit-Strategien) ist BCM-Logik in Finanzsprache; 22301 und 200-4 liefern die Methodik für RTO/RPO, Tests und Krisenorganisation.
10. **Alles → Lieferkette** : NIS2 Art. 21(2)d, DORA ICT-Drittparteirisiko, CRA-Herstellerpflichten, TISAX-Lieferantenlogik und C5 sind dieselbe Frage aus fünf Richtungen: wer haftet wofür in der Kette, und welche Evidenz fließt nach oben.

## 3. Betroffenheits-Schnellprüfung (DE, für DD und Erstgespräch)

| Frage                                                                                | Instrument                 | Konsequenz                                                                                                                             |
|--------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| >50 MA oder >10 Mio. EUR Umsatz UND Sektor in Anlage 1/2 BSIG?                       | BSIG (NIS2UmsuCG)          | Registrierung, Maßnahmen nach Stand der Technik, Meldung 24h/72h/1M, Leitungspflichten, Sanktionen bis 10 Mio./2 %                     |
| Kritische Anlage (Schwellenwerte BSI-KritisV, 500k versorgte Personen als Leitwert)? | BSIG-KRITIS + KRITIS-DachG | Zusätzlich: Angriffserkennung (SzA), Nachweise alle 3 Jahre, physische Resilienz, Störfallmeldung                                      |
| Finanzunternehmen oder ICT-Dienstleister dafür?                                      | DORA + RTS/ITS             | IKT-Risikomanagement, Vertragsklauseln, TLPT, Register der IKT-Verträge, Aufsicht BaFin                                                |
| Produkt mit digitalen Elementen im EU-Markt?                                         | CRA                        | CE-Kennzeichnung mit Cyber-Anforderungen, Schwachstellenprozess, Meldung aktiv ausgenutzter Lücken an ENISA, Übergangsfristen beachten |
| KI-System im Einsatz oder im Produkt?                                                | AI Act                     | Rollenklärung (Anbieter/Betreiber), Risikoklasse, ab Hochrisiko QMS+Risikomanagement+Logging, GPAI-Transparenz                         |
| Personenbezug?                                                                       | DSGVO/BDSG                 | Immer parallel, Art. 32 verknüpft mit ISMS-Maßnahmen                                                                                   |
| Automotive-Lieferkette?                                                              | TISAX, ISO 21434, R155/156 | Label-Pflicht de facto, CSMS für Typgenehmigung                                                                                        |
| Cloud-Anbieter oder -Nutzer mit Behörden-/Finanzkunden?                              | C5, EUCS (kommend)         | Testat als Marktzugang, Shared-Responsibility sauber ziehen                                                                            |

## 4. Kontroll-Mapping-Kerne (was auf was einzahlt)

| Anforderung (Gesetz)                    | ISO 27001:2022 Annex A   | IT-Grundschutz   | C5:2020       | CIS v8.1        | NIST CSF 2.0     |
|-----------------------------------------|--------------------------|------------------|---------------|-----------------|------------------|
| Risikomanagement (NIS2 Art. 21(1))      | 5.x Governance, 8.2      | ISMS.1, ORP      | OIS           | IG-übergreifend | GOVERN, IDENTIFY |
| Incident Handling + Meldung             | 5.24-5.28, 6.8           | DER.2            | SIM           | 17              | RESPOND          |
| BCM/Krisenmanagement                    | 5.29, 5.30, 8.14         | DER.4, BSI 200-4 | BCM           | 11              | RECOVER          |
| Lieferkette                             | 5.19-5.23                | OPS.2, ORP       | SSO           | 15              | GV.SC            |
| Zugriff/MFA/Krypto                      | 5.15-5.18, 8.5, 8.24     | ORP.4, CON.1     | IDM, KRY      | 5, 6            | PROTECT          |
| Schwachstellen/Patching                 | 8.8                      | OPS.1.1.3        | OPS           | 7               | ID.RA, PR.PS     |
| Angriffserkennung (§8a BSIG SzA)        | 8.15, 8.16               | DER.1, OH-SzA    | RB-Monitoring | 8, 13           | DETECT           |
| Schulung/Awareness (inkl. Leitung NIS2) | 6.3                      | ORP.3            | HR            | 14              | PR.AT            |

Nutzung: In der DD pro Domäne fragen, welches Framework-Artefakt als Evidenz existiert; in der Beratung ein Control einmal umsetzen und auf alle geforderten Rahmenwerke mappen (Compliance-Synergie statt Parallelprojekte).

## 5. Zeitachse und Aufsicht (DE, verifizierungspflichtig vor Kundenaussage)

- BSIG/NIS2UmsuCG: in Kraft; Registrierungs- und Nachweisregime beim BSI läuft, Übergangsfristen je Einrichtungskategorie prüfen.
- KRITIS-DachG: in Kraft, Durchführungsverordnung und Registrierungspflichten im Aufbau; Mapping auf ISO 27001/22301 vorhanden (siehe openkritis-Ablage).
- CRA: in Kraft, Hauptpflichten greifen gestaffelt (Meldepflichten früher als Produktpflichten); für DD bei Software-Targets heute schon bewertungsrelevant.
- AI Act: gestaffelt in Anwendung (Verbote und AI Literacy zuerst, GPAI-Pflichten, dann Hochrisiko); für Mittelstand meist Betreiberpflichten plus Schatten-KI-Problem.
- DORA: anwendbar seit 01/2025, RTS/ITS-Detailpflichten (Register, TLPT) in der Aufsichtspraxis angekommen.

## 6. Formulierungen für den Kundenmund (getestet auf Verständlichkeit)

- "Sie haben nicht fünf Compliance-Projekte, Sie haben ein Sicherheitsprogramm mit fünf Berichtsformaten."
- "Das Zertifikat ist der Beifang, die Steuerungsfähigkeit ist der Fang."
- "NIS2 bestraft nicht den Vorfall, sondern die fehlende Vorbereitung und die verpasste Meldung."
- "Ihre Lieferanten erben Ihre Pflichten nicht automatisch, Ihre Haftung bleibt bei Ihnen."
- "Erst Betroffenheit, dann Gap, dann Fahrplan. Alles andere ist Folklore."
