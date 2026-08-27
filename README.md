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
  PDF-Textlayer — Zellwerte werden übernommen, nicht rekonstruiert. Bringt
  ACCURATE eine Seite zum Absturz (kommt je nach System vor), wiederholt das
  Tool den Lauf automatisch mit FAST und vermerkt das im Extrakt, statt eine
  lückenhafte Datei zu schreiben.
- **Kein Textverlust:** fehlt nach der Konvertierung Text der Quelle, wird er
  wörtlich als Abschnitt „Nachtrag: nicht zugeordneter Quelltext" mit Seitenzahl
  angehängt (abschaltbar mit `--no-repair`). Am realen ISO/IEC 27001:2022 hebt
  das die Deckung von 99,826 % auf 100,0 %: TableFormer hatte den Rest einer
  mehrzeiligen Control-Zelle verschluckt.
- **Kein stiller Teilerfolg:** der Docling-Konvertierungsstatus wird geprüft.
  Nicht verarbeitete Seiten stehen als `docling_status` und als Warnung in der
  Datei; ein Fehlschlag bricht ab.
- **OCR-Automatik:** textarme (gescannte) PDFs werden erkannt und mit OCR
  wiederholt.
- **Abweichungsprüfung für alle Formate:** jeder Extrakt wird Wort für Wort
  gegen die Quelle geprüft — PDFs gegen den Textlayer (Docling-PDF-Backend,
  keine ML-Modelle nötig), XLSX/DOCX/PPTX gegen den Standardleser des Formats.
  Der Abgleich kommt damit immer aus einer von Docling unabhängigen Quelle.
  Die Wortdeckung steht als `text_coverage_percent` in der Front-Matter; unter
  `--min-coverage` (Default 99.5 %) gibt es eine Warnung mit den fehlenden
  Wörtern und den schwächsten Seiten. Laufende Kopf-/Fußzeilen werden nicht
  mitgezählt, über Zeilenumbrüche getrennte Wörter gelten als vorhanden.
- **Qualitätsgates:** leerer Output bricht ab; textarme Seiten, fehlende
  Gliederung, kaputte Tabellenblöcke und Encoding-Fehler landen als Warnung in
  der Datei, im `manifest.json` und im Exit-Code (`--strict`).
- **Idempotenz:** unveränderte Quellen (Hash-Vergleich) werden übersprungen.

## Ausgabe in den Obsidian-Vault

`publish.py` schreibt aus einem Extrakt je Anforderung eine Normtext-Notiz nach
`Normen (lizenziert)/<framework>/<framework> <ID> (Normtext).md` — genau die
Dateien, auf die die Framework-Notizen im Vault per Embed verweisen.

```bash
python publish.py output/iso-iec-27001-2022.md \
    --vault ~/obsidian-vault --framework iso27001-2022 --dry-run
python publish.py output/iso-iec-27001-2022.md \
    --vault ~/obsidian-vault --framework iso27001-2022
```

Welche IDs gebraucht werden, liest das Tool aus dem Vault (`GRC/Frameworks/<framework>/`,
Feld `id`). Nichts wird erfunden: was im Extrakt nicht steht, wird als fehlend
gemeldet. Klauseln ohne eigenen Text werden aus ihren Unterklauseln
zusammengesetzt; Klauseln, die das Layoutmodell nicht als Überschrift erkannt
hat, werden über ID **und** den im Vault hinterlegten Titel angesteuert.
Beginnt ein Normtext mitten im Satz, bekommt die Notiz einen Warnhinweis auf
eine mögliche Zellverschiebung.

Der Zielordner ist im Vault von der Versionierung ausgenommen — lizenzierter
Normtext bleibt lokal. Dieses Repository enthält weder Quell-PDFs noch Extrakte.

## Kreuzreferenzen für abweichende Nummerierungen

Manche Frameworks nummerieren ihre Anforderungen thematisch statt in der
Reihenfolge des Dokuments. Beim CRA ist `AnnexI.1.3` der Buchstabe d) des
Anhangs I, `AnnexI.1.11` der Buchstabe c). Eine Zuordnung nach Position wäre
falsch, deshalb liegt in `mappings/cra.json` eine geprüfte Kreuzreferenz: je ID
ein wörtliches Textstück, an dem der Abschnitt beginnt. Findet `publish.py` den
Anker nicht, meldet es die ID als fehlend, statt etwas Falsches abzulegen.

## Versionsstand prüfen

Ein Extrakt ist nur so gut wie seine Fassung. `versioncheck.py` holt zu jedem
aufgenommenen Dokument den aktuellen Stand von der offiziellen Fundstelle und
meldet, was veraltet ist.

```bash
python versioncheck.py                                   # alle Dokumente
python versioncheck.py --only wstg-v4-2                  # eines
python versioncheck.py --strict                          # Exit 1 bei Veraltetem
python versioncheck.py --to ~/obsidian-vault/"document-to-LLM Versionsstand.md"
```

Die Fundstellen und Suchmuster stehen in `versions.json`. Nichts wird aus dem
Gedächtnis beantwortet: Was nicht abrufbar ist — ISO-Katalog hinter Paywall,
ENX-Portal mit Anmeldung, gesperrte Hosts — erscheint als „manuell prüfen"
beziehungsweise „Quelle offline" **mit** Fundstelle, statt als Vermutung.

## Aufnahmeprotokoll

`tracker.py` schreibt eine Übersicht über alle Extrakte — je Dokument Wortdeckung,
Seiten, Tabellen, Überschriften, entfernte Kopf-/Fußzeilen, Nachträge und offene
Warnungen. Die Datei wird bei jedem Lauf neu erzeugt und veraltet damit nicht.

```bash
python tracker.py --output output --input input \
    --vault ~/obsidian-vault \
    --to output/_TRACKER.md \
    --to ~/obsidian-vault/"document-to-LLM Tracker.md"
```

Typischer Durchlauf für einen ganzen Bestand:

```bash
python extract.py input/ --recursive --json      # konvertieren + prüfen
python publish.py output/<slug>.md --vault ~/obsidian-vault --framework <fw>
python index.py build --output output            # Retrieval-Index
python tracker.py --output output --vault ~/obsidian-vault --to output/_TRACKER.md
```

## Regeln für Agenten

Siehe [`SKILL.md`](SKILL.md). Kurzfassung: Kontext kommt aus `output/`, niemals
aus dem PDF; Zitate mit Slug, Gliederung und Seitenzahl belegen; bei
`extraction_status: warn` die Warnungen lesen.

## Ordner

```
input/     Quelldokumente
output/    *.md (verbindliche Textquelle), *.docling.json, manifest.json, acsos.db
```
