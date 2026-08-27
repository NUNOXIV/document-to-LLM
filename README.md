# document-to-LLM

Extraktions- und Retrieval-Skill für **ACSOS** (Automated Cyber Security Operating
System). Wandelt komplexe GRC-Dokumente — ISO 27001/42001, BSI IT-Grundschutz, C5,
TISAX/ISA, NIS2/BSIG, DORA, CRA, NIST — in strukturerhaltendes Markdown um, das
LLM-Agenten ohne Halluzinationsrisiko lesen können.

Die Konvertierung macht ausschließlich **[IBM Docling](https://github.com/docling-project/docling)**.
Es gibt in diesem Repo bewusst keinen eigenen PDF-Parser: Layout-, Tabellen- und
Hierarchie-Erkennung übernehmen die Docling-Modelle, nicht Regex.

## Installation

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Der erste **PDF**-Lauf lädt die Docling-Layout- und TableFormer-Modelle von
`huggingface.co` (einige hundert MB). In Umgebungen ohne HF-Zugriff einmalig
vorab holen und den Cache mitgeben:

```bash
docling-tools models download          # auf einer Maschine mit HF-Zugriff
export HF_HOME=/pfad/zum/model-cache   # in der abgeschotteten Umgebung
```

Office-Formate (DOCX, XLSX, PPTX) und HTML brauchen keine Modelle.

Air-gapped oder hinter einer Egress-Policy: Modelle einmal mitbringen statt HF-Zugriff.

```bash
docling-tools models download -o ./docling-models     # Maschine mit HF-Zugriff
python extract.py datei.pdf --models-dir ./docling-models
export ACSOS_DOCLING_MODELS=./docling-models          # alternativ dauerhaft
```

Konkret geholt werden (Stand Docling 2.123):

| Modell | Repository | Groesse |
| --- | --- | --- |
| Layout | `docling-project/docling-layout-heron` | 172 MB |
| Layout (ONNX-Engine) | `docling-project/docling-layout-heron-onnx` | 171 MB |
| Tabellen (ACCURATE) | `ds4sd/docling-models` → `model_artifacts/tableformer/accurate` | 213 MB |
| OCR | in `rapidocr` enthalten, kein Download | — |

Die Groessen sind der Grund, warum ein HF-Connector oder API-Zugang das Problem
nicht loest: die Gewichte muessen als Dateien auf die Maschine, die konvertiert.
Entweder der Host `huggingface.co` ist erreichbar, oder der Ordner wird per
`--models-dir` mitgebracht.

Preflight, bevor ein Bestand konvertiert wird:

```bash
python extract.py --doctor
```

Tests:

```bash
python tests/test_units.py   # Unit-Tests, ohne Modelle lauffaehig
./tests/smoke.sh        # Office-Pfad (DOCX), ohne Modelle lauffaehig
./tests/smoke_pdf.sh    # PDF-Pfad: Layout, Tabellen, Lesereihenfolge, Vollstaendigkeit
```

## Nutzung

```bash
# 1) Konvertieren  (PDF, DOCX, XLSX, PPTX, HTML)
python extract.py input/ISO-27001.pdf
python extract.py input/ --recursive --json          # ganzer Bestand + JSON für den Index

# 2) Index bauen
python index.py build --output output --db output/acsos.db

# 2b) Abweichungspruefung gegen die Quelle (laeuft bei PDFs automatisch mit)
python verify.py output/iso-27001.md --source input/ISO-27001.pdf --min-coverage 99.5

# 3) Gezielt Kontext holen
python index.py search "Schlüsselverwaltung Kryptographie" -n 5
python index.py show iso-27001 --heading "A.8"
python index.py list
```

## Was den Output belastbar macht

- **Provenienz je Datei:** YAML-Front-Matter mit SHA-256 der Quelle, Seitenzahl,
  Tabellenanzahl, Docling-Version, Konvertierungszeitpunkt.
- **Seitenmarker:** `<!-- page: N -->` im Text, damit jede Aussage zitierfähig ist.
- **Tabellen im ACCURATE-Modus:** TableFormer mit Cell-Matching gegen den
  PDF-Textlayer — Zellwerte werden übernommen, nicht rekonstruiert.
- **OCR-Automatik:** textarme (gescannte) PDFs werden erkannt und mit OCR
  wiederholt.
- **Abweichungsprüfung:** jeder PDF-Extrakt wird Wort für Wort gegen den
  Textlayer der Quelle geprüft (Docling-PDF-Backend, keine ML-Modelle nötig).
  Die Wortdeckung steht als `text_coverage_percent` in der Front-Matter; unter
  `--min-coverage` (Default 99.5 %) gibt es eine Warnung mit den fehlenden
  Wörtern und den schwächsten Seiten. Laufende Kopf-/Fußzeilen werden nicht
  mitgezählt, über Zeilenumbrüche getrennte Wörter gelten als vorhanden.
- **Qualitätsgates:** leerer Output bricht ab; textarme Seiten, fehlende
  Gliederung, kaputte Tabellenblöcke und Encoding-Fehler landen als Warnung in
  der Datei, im `manifest.json` und im Exit-Code (`--strict`).
- **Idempotenz:** unveränderte Quellen (Hash-Vergleich) werden übersprungen.

## Regeln für Agenten

Siehe [`SKILL.md`](SKILL.md). Kurzfassung: Kontext kommt aus `output/`, niemals
aus dem PDF; Zitate mit Slug, Gliederung und Seitenzahl belegen; bei
`extraction_status: warn` die Warnungen lesen.

## Ordner

```
input/     Quelldokumente
output/    *.md (verbindliche Textquelle), *.docling.json, manifest.json, acsos.db
```
