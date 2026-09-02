---
source_file: "pe-ma-deal-mechanik-cyber-dd.md"
source_sha256: cc6cba1e6d7fe3b3e81d0d9e77cb91a69ed8bd2e3e152fb2be311f69d01b1825
source_bytes: 7702
pages: 0
tables: 1
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-28T13:19:11+00:00"
extraction_status: ok
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
# PE/M&amp;A-Deal-Mechanik für Cyber Due Diligence

Zweck: Das PE-Vokabular und die Deal-Logik beherrschen, in die eine Cyber-DD eingebettet ist. Das ist die Sprache von intcube-Kunden (Investoren, M&amp;A-Berater), nicht die von CISOs. Wer sie spricht, wird als Deal-Team-Mitglied wahrgenommen, nicht als IT-Prüfer. Stand 08/2026.

## 1. Der Deal-Ablauf und wo die Cyber-DD sitzt

| Phase                           | Was passiert                                                                                                        | Cyber-Rolle                                                                                                             |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Teaser / IM                     | Verkäufer (Sell-side, meist über M&A-Advisor) streut anonymes Kurzprofil, dann Information Memorandum               | Noch keine. Höchstens Outside-in-Scan auf eigene Rechnung des Interessenten                                             |
| NDA + indikatives Angebot (NBO) | Käufer signalisiert Preisspanne auf Basis IM                                                                        | Red-Flag-Scan outside-in möglich (ASM, Leaks, Breach-Historie): ohne Zugang, ohne Wissen des Targets                    |
| LOI / Exklusivität              | Letter of Intent, oft mit Exklusivitätsfenster (4 bis 12 Wochen)                                                    | Jetzt startet die DD formal. Zeitfenster ist hart, alle DD-Streams laufen parallel                                      |
| Due Diligence                   | Financial, Legal, Tax, Commercial, Tech, HR, ESG, Cyber parallel; Datenraum (VDR), Q&A-Prozess, Management-Sessions | Kernarbeit: Datenraum, Interviews, Scans. Cyber ist oft der kleinste und späteste Stream, Zeitbudget 1 bis 3 Wochen     |
| SPA-Verhandlung                 | Kaufvertrag (Share/Asset Purchase Agreement)                                                                        | Findings werden zu Klauseln: Reps & Warranties, Indemnities, Conditions Precedent, Preisanpassung                       |
| Signing → Closing               | Vertragsunterschrift, dann Vollzug (kartellrechtliche Freigaben etc.)                                               | Zwischen Signing und Closing: Interim-Covenants (keine wesentlichen IT-Änderungen), Vorbereitung Tag-1                  |
| Post-Closing / 100 Tage         | Integration oder Stand-alone-Stabilisierung                                                                         | 100-Tage-Plan aus der DD wird Umsetzungsauftrag, oft mit Budget aus dem Deal-Modell                                     |
| Hold (3 bis 7 Jahre) → Exit     | Wertsteigerung, dann Verkauf/IPO                                                                                    | Portfolio-Reporting, Kohorten; bei Exit: Vendor DD (Verkäufer lässt sich selbst prüfen, um Überraschungen zu vermeiden) |

## 2. Vokabular, das im Raum fällt (und was es für Cyber heißt)

- **Buy-side / Sell-side** : für wen die DD arbeitet. intcube: buy-side. Vendor-DD (sell-side) ist das Spiegelprodukt: Findings vorab beheben oder transparent machen.
- **VDR (Virtual Data Room)** : Datenraum (Datasite, Intralinks, Drooms, iDeals). Cyber bekommt oft nur einen Unterordner. Q&amp;A-Prozess ist formalisiert, Fragenkontingent begrenzt: Fragen präzise stellen.
- **Red Flag Report vs. Full Scope** : Red-Flag = nur Dealbreaker und große Risiken, 5 bis 15 Seiten, schnell. Full Scope = vollständige Domänenprüfung. Preis- und Zeitrahmen unterscheiden sich um Faktor 2 bis 4.
- **Reps &amp; Warranties (R&amp;W)** : Garantien des Verkäufers im SPA ("keine wesentlichen Sicherheitsvorfälle in den letzten 3 Jahren", "Einhaltung DSGVO"). Cyber-Findings entscheiden, welche Reps der Käufer fordern muss.
- **W&amp;I-Versicherung (Warranty &amp; Indemnity)** : versichert Garantieverletzungen. Achtung: Cyber ist häufig ausgeschlossen oder nur nach separater Cyber-DD versicherbar; bekannte Findings (disclosed) sind nie gedeckt. Eine saubere Cyber-DD kann die W&amp;I-Deckung für Cyber-Reps erst ermöglichen: das ist ein Verkaufsargument für die DD selbst.
- **Indemnity (Freistellung)** : verschuldensunabhängige Freistellung für ein bekanntes, konkretes Risiko (z. B. laufendes DSGVO-Verfahren). Für identifizierte Cyber-Altlasten das schärfere Instrument gegenüber der Rep.
- **Condition Precedent (CP)** : Vollzugsbedingung. Selten für Cyber, aber möglich (z. B. MFA auf Admin-Zugängen vor Closing).
- **Purchase Price Adjustment / Escrow / Holdback** : Kaufpreisanpassung oder Einbehalt auf Treuhandkonto. Cyber-Findings mit bezifferbarem Remediation-Aufwand landen hier: deshalb muss der DD-Report in EUR sprechen.
- **Locked Box vs. Closing Accounts** : Kaufpreismechanik. Für Cyber nur relevant, weil bei Locked Box nach dem Stichtag entstandene Schäden (Vorfall zwischen Signing und Closing!) Streitfall werden: MAC-Klausel prüfen.
- **MAC-Klausel (Material Adverse Change)** : Rücktrittsrecht bei wesentlicher Verschlechterung. Ein Ransomware-Vorfall in der Exklusivität ist der Klassiker.
- **EBITDA-Multiple** : Bewertungslogik. Wiederkehrende Cyber-Kosten (Lizenzen, Personal, MSSP) drücken EBITDA und wirken über den Multiple gehebelt auf den Preis; einmalige Remediation ist CapEx-artig und wird separat verhandelt. Deshalb trennen: run-rate vs. one-off.
- **Add-on / Buy-and-Build / Carve-out** : Add-on = Zukauf zu bestehender Plattform (Cyber-Frage: Integration zweier IT-Landschaften, Identität, Alt-Tenant). Carve-out = Herauslösung aus Konzern (Cyber-Frage: TSA-Abhängigkeiten, eigene Security-Funktion ab Tag 1 aufbauen).
- **TSA (Transitional Service Agreement)** : Übergangsleistungen des Verkäufers (oft IT und Security). Rote Fahne: Security-Monitoring liegt beim alten Konzern, endet nach 12 Monaten, kein Aufbauplan.
- **100-Tage-Plan** : Standard-PE-Instrument nach Closing. Cyber-Anteil: die 5 bis 10 Maßnahmen mit Preis, Owner und Termin, die aus der DD kommen. Muss ohne Vollzeit-CISO umsetzbar sein.
- **Value Creation Plan** : der mehrjährige Wertsteigerungsplan des Fonds. Cyber taucht dort als Risikominderung, zunehmend als Exit-Asset auf (saubere Security-Story erhöht Käufervertrauen beim Weiterverkauf).
- **Fund-Level-Begriffe** : LP (Investoren des Fonds), GP (Fondsmanager), IC (Investment Committee, entscheidet über den Deal; der DD-Report wird für das IC geschrieben), DPI/IRR (Renditemaße). Der Cyber-Report hat genau einen Leser, der zählt: das IC. Drei Seiten Substanz schlagen dreißig Seiten Vollständigkeit.

## 3. Was Cyber-Findings im Deal bewirken (Eskalationsleiter)

1. Kein Effekt: Finding wird 100-Tage-Plan-Punkt mit Budget.
2. Preis: bezifferter Remediation-Aufwand wird verhandelt (Abschlag, Escrow, Holdback).
3. Vertrag: Rep, Indemnity oder CP im SPA; W&amp;I-Ausschlüsse.
4. Struktur: Asset- statt Share-Deal (Altlasten bleiben beim Verkäufer), Carve-out-Perimeter ändern.
5. Dealbreaker: selten, real bei aktivem, nicht eingedämmtem Incident, systematischer Compliance-Täuschung oder nicht sanierbarer Produkt-Security bei Software-Targets.

Merksatz für den Report: Jedes Finding braucht eine Adresse: Plan (Punkt 1), Preis (2), Vertrag (3) oder Struktur (4). Ein Finding ohne Adresse ist eine Beobachtung, kein Ergebnis.

## 4. Regulatorik im Deal (deine Dimension, deal-spezifisch)

- **Betroffenheit ändert sich durch den Deal selbst** : Das Target kann durch Konzernzugehörigkeit über Schwellenwerte rutschen (BSIG-Größenschwellen zählen verbundene Unternehmen mit; DORA erfasst ICT-Dienstleister von Finanzunternehmen). Prüfung immer für Ist und für Post-Closing-Struktur.
- **CRA bei Produkt-Targets** : Übergangsfristen sind CapEx mit Termin; fehlende SBOM- und Update-Prozesse sind bezifferbarer Investitionsbedarf, kein weiches Risiko.
- **DSGVO-Altlasten** : laufende Verfahren und nicht gemeldete Breaches sind Indemnity-Kandidaten; Bußgeldrahmen skaliert mit Konzernumsatz des Käufers: derselbe Verstoß wird durch den Deal teurer.
- **Exportkontrolle/Geheimschutz** : bei Targets mit VS-Bezug oder Dual-Use entscheidet das über Käuferkreis und Freigaben (Investitionsprüfung AWV §55 ff.).

## 5. Formulierungen für Investor-Ohren

- "Das kostet einmalig X, senkt das EBITDA nicht und ist in 100 Tagen erledigt."
- "Das ist kein IT-Problem, das ist eine ungedeckte Garantie im SPA."
- "Ohne diese drei Maßnahmen ist die Cyber-Rep nicht versicherbar."
- "Regulatorische Exposure ändert sich durch den Deal: Post-Closing gilt BSIG-Registrierungspflicht."
- "Der Vorfall von 2024 ist eingepreist, wenn er gelernt wurde. Wir haben keine Lektion gefunden."
