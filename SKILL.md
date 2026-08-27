---
name: document-to-llm
description: Konvertiert GRC-Normen und Regularien (PDF, DOCX, XLSX, PPTX, HTML) mit IBM Docling in strukturerhaltendes Markdown und stellt sie als durchsuchbaren Index bereit. Immer nutzen, wenn ein Agent Inhalte aus einem Norm- oder Regulatorik-Dokument braucht — ISO 27001, ISO 42001, BSI IT-Grundschutz, C5, TISAX/ISA, NIS2/BSIG, DORA, CRA, NIST — oder wenn eine neue Datei in den Dokumentenbestand aufgenommen wird.
---

# document-to-LLM

Verlässliche Textquelle für ACSOS. PDFs werden **einmal** sauber konvertiert;
Agenten lesen danach ausschließlich den Output.

## Die eine Regel

**Ein Agent parst niemals ein PDF selbst.**

Kein Lesen von `.pdf` ins Kontextfenster, kein PyPDF, kein `pdftotext`, kein
Regex über Rohtext, kein "ich schätze mal, was in der Tabelle steht". Wenn du
Inhalt aus einer Norm brauchst, kommt er aus `output/` — sonst nirgendwoher.

Grund: In mehrspaltigen, tabellenlastigen Normen zerlegt naives Text-Extrahieren
Control-Tabellen in Zeilenfragmente und wirft die Gliederung weg. Was dann im
Kontext landet, sieht plausibel aus und ist falsch. Bei Compliance-Aussagen ist
das kein Formatierungsproblem, sondern ein Haftungsproblem.

## Der Ablauf

### 1. Prüfen, ob das Dokument schon konvertiert ist

```bash
ls output/*.md
python index.py list --db output/acsos.db
```

Ist der Slug da (z. B. `iso-27001.md`), direkt zu Schritt 3.

### 2. Konvertieren (einmal pro Dokument)

```bash
# Einzelne Datei
python extract.py pfad/zur/ISO-27001.pdf

# Ganzer Ordner, rekursiv, inklusive verlustfreiem JSON für den Index
python extract.py input/ --recursive --json
```

Ergebnis: `output/<slug>.md` mit YAML-Front-Matter (Quell-Hash, Seitenzahl,
Docling-Version, Warnungen) und `<!-- page: N -->` Markern im Text.

Optionen, die zählen:

| Option | Wann |
| --- | --- |
| `--ocr auto` (Default) | normal; OCR wird nur bei textarmen PDFs nachgezogen |
| `--ocr on` | gescannte Dokumente, Behördenscans |
| `--json` | wenn das Dokument in den Suchindex soll |
| `--force` | Quelldatei wurde ersetzt |
| `--strict` | in CI: Exit 1 auch bei Warnungen |

### 3. Kontext holen — gezielt, nicht als Volltext

Ganze Normen gehören nicht in einen Prompt. Erst suchen, dann den Abschnitt lesen:

```bash
python index.py build --output output --db output/acsos.db     # einmal nach neuen Extraktionen
python index.py search "Kryptographie Schlüsselverwaltung" -n 5
python index.py show iso-27001 --heading "A.8"
```

`search` liefert Dokument, Gliederungspfad und Seitenzahl — genau die Angaben,
die ein Zitat belegen. Nur wenn ein Dokument klein ist (< ~2000 Zeilen), darfst
du `output/<slug>.md` komplett lesen.

## Pflichten beim Zitieren

1. Zitiere wörtlich aus `output/`. Formuliere Normtext nicht um und ergänze ihn nicht.
2. Gib Dokument-Slug, Gliederungsnummer und Seite an: `iso-27001.md, A.8.24, S. 31`.
3. Findest du eine Anforderung nicht im Output, existiert sie für dich nicht.
   Sag "steht nicht im extrahierten Dokument" — rate nicht aus dem Gedächtnis.
4. Steht in der Front-Matter `extraction_status: warn`, lies die `warnings`.
   Bei Tabellenwarnungen gilt: Tabelleninhalte vor dem Zitat gegen die Quelle
   prüfen oder als unsicher kennzeichnen.
5. Versionsstände (Edition, Fassung, Datum) nimmst du aus dem Dokument selbst,
   nie aus dem Dateinamen.

## Was du nicht tust

- Kein zweiter Parser. Keine `pypdf`/`pdfplumber`/`fitz`-Zeile "nur zum Prüfen".
- Kein Editieren von Dateien in `output/`. Der Output ist generiert; Korrekturen
  laufen über eine erneute Konvertierung.
- Kein Verschieben der Quell-PDFs in `output/`.
- Keine Aussage über eine Norm, die nicht im Bestand ist. Dann: konvertieren
  (Schritt 2) oder dem Nutzer sagen, dass das Dokument fehlt.

## Wenn etwas schief geht

| Symptom | Ursache | Handlung |
| --- | --- | --- |
| `Docling ist nicht installiert` | Umgebung frisch | `pip install -r requirements.txt` |
| `Docling-Modelle nicht verfügbar (403 …)` | kein Zugriff auf huggingface.co | Modelle vorab per `docling-tools models download` holen, `HF_HOME` setzen. Betrifft nur PDF/Bild — DOCX/XLSX/HTML laufen ohne Modelle. |
| Warnung "Zeichen/Seite" | gescanntes PDF | `python extract.py datei.pdf --ocr on --force` |
| Warnung "Keine Überschriften erkannt" | flaches Layout | Zitate über Seitenmarker statt Gliederung belegen |
| Warnung "inkonsistente Spaltenstruktur" | Tabelle unsicher rekonstruiert | Tabellenwerte nicht als Fakt zitieren, Quelle prüfen |
| `Index fehlt` | Index nicht gebaut | `python index.py build --output output` |
| Datei wird übersprungen | Hash unverändert | `--force`, wenn Neuerzeugung gewollt |

## Ablage

```
input/        Quelldokumente (nicht von Agenten lesen)
output/       *.md  ← einzige zulässige Textquelle
              *.docling.json  verlustfreie Struktur (Basis für den Index)
              manifest.json   Hashes, Seitenzahlen, Warnungen pro Lauf
              acsos.db        SQLite-FTS5-Index
```
