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

Vor dem ersten PDF-Lauf einmal `python extract.py --doctor` — das sagt in zehn
Sekunden, ob Textlayer und Modelle einsatzbereit sind.

```bash
# Einzelne Datei
python extract.py pfad/zur/ISO-27001.pdf

# Ganzer Ordner, rekursiv, inklusive verlustfreiem JSON für den Index
python extract.py input/ --recursive --json
```

Ergebnis: `output/<slug>.md` mit YAML-Front-Matter (Quell-Hash, Seitenzahl,
Docling-Version, Wortdeckung, Warnungen) und `<!-- page: N -->` Markern im Text.

Bei PDFs läuft automatisch die Abweichungsprüfung mit: der Extrakt wird Wort für
Wort gegen den Textlayer der Quelle verglichen. `text_coverage_percent: 100.0`
heißt, dass kein Wort der Quelle fehlt. Alles unter der Schwelle erzeugt eine
Warnung samt fehlender Wörter und schwächster Seiten.

Optionen, die zählen:

| Option | Wann |
| --- | --- |
| `--ocr auto` (Default) | normal; OCR wird nur bei textarmen PDFs nachgezogen |
| `--ocr on` | gescannte Dokumente, Behördenscans |
| `--json` | wenn das Dokument in den Suchindex soll |
| `--force` | Quelldatei wurde ersetzt |
| `--strict` | in CI: Exit 1 auch bei Warnungen |
| `--min-coverage 99.5` | geforderte Wortdeckung gegen die Quelle |
| `--models-dir DIR` | Umgebung ohne Zugriff auf huggingface.co |

### 3. Kontext holen — gezielt, nicht als Volltext

Ganze Normen gehören nicht in einen Prompt. Erst suchen, dann den Abschnitt lesen:

```bash
python index.py build --output output --db output/acsos.db     # einmal nach neuen Extraktionen
python index.py search "Kryptographie Schlüsselverwaltung" -n 5
python index.py show iso-27001 --heading "A.8"
```

Zweifel an der Vollständigkeit? Prüfen statt raten:

```bash
python verify.py output/iso-27001.md --source input/ISO-27001.pdf
```

`search` liefert Dokument, Gliederungspfad und Seitenzahl — genau die Angaben,
die ein Zitat belegen. Nur wenn ein Dokument klein ist (< ~2000 Zeilen), darfst
du `output/<slug>.md` komplett lesen.

### Der Abschnitt „Nachtrag: nicht zugeordneter Quelltext"

Steht am Dateiende, wenn das Layout- oder Tabellenmodell Quelltext keinem
Element zuordnen konnte — meist ein Zellrest. Die Zeilen sind wörtlich aus dem
PDF übernommen, damit nichts verloren geht, aber **ohne Struktur**: du siehst
nicht, zu welcher Tabellenzelle sie gehören. Zitierbar mit Seitenangabe; wenn
die Zuordnung für die Aussage zählt, in der Quelle nachsehen und das kenntlich
machen.

## Pflichten beim Zitieren

1. Zitiere wörtlich aus `output/`. Formuliere Normtext nicht um und ergänze ihn nicht.
2. Gib Dokument-Slug, Gliederungsnummer und Seite an: `iso-27001.md, A.8.24, S. 31`.
3. Findest du eine Anforderung nicht im Output, existiert sie für dich nicht.
   Sag "steht nicht im extrahierten Dokument" — rate nicht aus dem Gedächtnis.
4. Prüfe `text_coverage_percent`. Steht `appended_source_lines`, sieh dir den
   Nachtrag an, bevor du eine Tabelle zitierst.
5. Unter 100 % fehlen Wörter der Quelle — bei
   Zitaten aus den betroffenen Seiten (siehe Warnung) ist der Extrakt nicht
   belastbar; dann neu konvertieren, notfalls mit `--ocr on`.
6. Steht in der Front-Matter `extraction_status: warn`, lies die `warnings`.
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
| `Docling-Modelle nicht verfügbar (403 …)` | kein Zugriff auf huggingface.co | `docling-tools models download -o ./docling-models`, dann `--models-dir ./docling-models`. Betrifft nur PDF/Bild — DOCX/XLSX/HTML laufen ohne Modelle. |
| Warnung "Zeichen/Seite" | gescanntes PDF | `python extract.py datei.pdf --ocr on --force` |
| Warnung "Keine Überschriften erkannt" | flaches Layout | Zitate über Seitenmarker statt Gliederung belegen |
| Warnung "inkonsistente Spaltenstruktur" | Tabelle unsicher rekonstruiert | Tabellenwerte nicht als Fakt zitieren, Quelle prüfen |
| Warnung "Wortdeckung nur X %" | Text der Quelle fehlt im Extrakt | `--ocr on --force`; bleibt es dabei, betroffene Seiten nicht zitieren und melden |
| Warnung "FAST zurueckgefallen" | ACCURATE-Tabellenmodell brach ab | kein Handlungsbedarf, Zellinhalte stammen weiter aus dem Textlayer; Tabellenstruktur ist etwas grober |
| Warnung "Seite(n) nicht verarbeiten" | Docling-Teilerfolg | Seiten fehlen im Extrakt — nicht zitieren, neu konvertieren |
| `Index fehlt` | Index nicht gebaut | `python index.py build --output output` |
| Datei wird übersprungen | Hash unverändert | `--force`, wenn Neuerzeugung gewollt |

## Ausgabe in den Vault

Sollen die Extrakte in den Obsidian-Vault:

```bash
python publish.py output/<slug>.md --vault <vault> --framework <slug> --dry-run
```

Erst `--dry-run` lesen: er sagt, wie viele Anforderungen belegt werden und
welche IDs im Extrakt fehlen. Erst danach ohne `--dry-run` schreiben.

## Ablage

```
input/        Quelldokumente (nicht von Agenten lesen)
output/       *.md  ← einzige zulässige Textquelle
              *.docling.json  verlustfreie Struktur (Basis für den Index)
              manifest.json   Hashes, Seitenzahlen, Warnungen pro Lauf
              acsos.db        SQLite-FTS5-Index
```
