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

**Formate ohne Docling-Reader (`.yml`, `.yaml`, `.json`, `.xml`, `.mm`, `.txt`)** — etwa der
maschinenlesbare C5:2026-Kriterienkatalog — laufen nicht durch Docling, sondern
werden **wörtlich** in einen Codeblock übernommen. Das Front-Matter sagt das
offen: `converter: "ACSOS Passthrough (wörtlich, kein Parser)"` und
`docling_status: not-applicable`. Es wird kein eigener YAML-Parser geschrieben —
genau der wäre die Fehlerquelle, die dieses Werkzeug vermeidet.

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

### Passthrough-Dateien richtig lesen

Bei `converter: "ACSOS Passthrough …"` gilt: der Zeichenbestand ist exakt der
der Quelle (Wortdeckung 100 % gilt per Konstruktion, nicht per Messung), aber
es gibt **keine** abgeleiteten Überschriften, Tabellen oder Seitenmarken.
Zitiere solche Dateien über den Schlüsselpfad im YAML (z. B. `GC-05`,
`SIM-01.02B`) statt über eine Seitenzahl — eine Seitenzahl existiert nicht.

### Baustein-Struktur des IT-Grundschutz

Die Struktur des Kompendiums liegt in zwei Dateien, die einander brauchen: die
Mindmap `GS_Struktur_Edition-2023.mm` trägt die Hierarchie und je Baustein ein
Symbol für die Umsetzungsreihenfolge, das Plakat `GS_Struktur_Edition-2023.pdf`
die Legende, die diese Symbole erklärt. Getrennt ist keine brauchbar.

```bash
python gs_struktur.py --output output --to output/_GS-STRUKTUR.md
```

Das Ergebnis ist **abgeleitet**, nicht extrahiert — es ordnet um und löst
Symbole in Klartext auf. Für wörtliche Zitate die beiden Extrakte heranziehen,
nicht diese Gliederung.

## Für nachgelagerte Systeme: die JSON-Schnittstelle

Ein **Agent** liest das Markdown: kompakt, mit Seitenmarken, sparsam im Kontext.
Ein **verarbeitendes System** liest JSON. Beides liegt für jeden Extrakt vor:

| Datei | Inhalt |
| --- | --- |
| `<slug>.md` | verbindliche Textquelle für Agenten |
| `<slug>.docling.json` | verlustfreies DoclingDocument: Elemente, Tabellen als Zellraster, Positionen |
| `<slug>.passthrough.json` | wörtlicher Inhalt, wo Docling keinen Reader hat (YAML, XML, `.mm`) |
| `output/_KORPUS.json` | **Einstiegspunkt**: alle Dokumente mit Pfaden, Deckung, Befund, Warnungen |

Erzeugt mit `extract.py --json` bzw. `tracker.py --korpus output/_KORPUS.json`.

`_KORPUS.json` sagt je Dokument, welche der beiden JSON-Arten vorliegt
(`struktur_art: docling | passthrough`) und listet unter `ohne_struktur_json`,
wo gar keine liegt — ein verarbeitendes System muss also nicht raten und fällt
nicht still auf einen Teilbestand zurück.

### Anforderungen je Framework rechenfertig exportieren

```bash
python export.py --vault <vault> --to export/        # alle Frameworks auf einmal
python export.py --vault <vault> --only iso27001-2022
```

Welcher Extrakt ein Framework belegt hat, wird **nicht gepflegt, sondern
gelesen**: jede Normtext-Notiz im Vault nennt ihre Quelle. Eine gepflegte Liste
könnte veralten, diese Ableitung nicht. Frameworks, die sich auf mehrere
Quellen verteilen (der C5-Katalog liegt als eine Datei je Kriterienbereich vor),
werden zu einer Datei zusammengeführt — einzeln exportiert meldete jeder Teil
die Anforderungen der anderen 17 als fehlend.

Für ein einzelnes Dokument geht es auch direkt:

```bash
python publish.py output/<slug>.md --vault <vault> --framework <framework> \
    --dry-run --export-json export/<framework>.json
```

Ergibt genau die Form, mit der ein Rechensystem ohne Übersetzung arbeiten kann:

```json
{
  "frameworkId": "iso27001-2022",
  "edition": "ISO/IEC 27001 2022",
  "sourceFile": "ISO-IEC-27001-2022.pdf",
  "sourceSha256": "e739019c…",
  "requirements": [
    {"id": "A.5.1", "title": "…", "text": "<Wortlaut>", "group": "A.5"}
  ],
  "missing": []
}
```

`group` wird aus der ID abgeleitet (`A.5.1` → `A.5`, `APP.1.1.A1` → `APP.1.1`,
`AM-01.01B` → `AM-01`), `edition` aus `versions.json` — steht das Dokument dort
nicht, bleibt das Feld `null` statt eine Ausgabe zu behaupten. IDs ohne
gefundenen Wortlaut stehen unter **`missing`**, nicht als Anforderung mit leerem
`text`: eine Lücke soll als Lücke sichtbar sein.

**Größenordnung:** das JSON ist rund siebenmal so groß wie das Markdown
(444 MB gegen 63 MB). Für die programmatische Verarbeitung ist es die richtige
Wahl, für den Kontext eines Agenten nicht — dort kostet dieselbe Aussage ein
Vielfaches an Token. Deshalb bleibt Markdown die Quelle fürs Zitieren.

## Versionsstand — immer prüfen

Bevor du aus einem Extrakt zitierst oder eine Norm für eine Aussage heranziehst:

```bash
python versioncheck.py --only <slug>
```

Meldet der Lauf **VERALTET**, sag das in deiner Antwort dazu und nenne die
aktuelle Fassung. Steht dort **aus Dokument belegt**, nenne die Ausgabe mit dem
angegebenen Beleg (Datei und Seite) und den Zusatz, dass eine neuere Ausgabe
nicht maschinell prüfbar war. Bei **manuell prüfen** oder **Quelle offline** ist
der Stand ungeprüft — dann kennzeichne die Aussage als „Stand des vorliegenden
Dokuments". Rate nie aus dem Gedächtnis, welche Fassung aktuell ist.

### Neueste Fassung ist nicht immer die geltende

Eine veröffentlichte Fassung kann ein Stichtag in der Zukunft haben. **Maßgeblich
ist, was heute gilt, nicht was zuletzt erschienen ist.** Beispiel aus dem
Bestand: VDA ISA 2027 erschien am 01.07.2026, gilt aber erst für Assessments ab
dem 01.01.2027 — bis dahin ist ISA 6.0.2 die geltende Fassung, obwohl sie älter
ist. Wer hier die neuere zitiert, sagt einem Kunden das Falsche über sein
laufendes Assessment.

Steht in der Registry eine `anmerkung` mit einem Stichtag, lies sie, bevor du
die Fassung als geltend bezeichnest. Für noch nicht in Kraft getretene Fassungen
gilt: nennbar als „kommende Fassung ab <Datum>", nie als geltende Anforderung.

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
6. Prüfe die Fassung (siehe oben). Eine korrekt extrahierte, aber veraltete
   Norm ist für eine Compliance-Aussage genauso falsch wie ein kaputter Extrakt.
7. Steht in der Front-Matter `extraction_status: warn`, lies die `warnings`.
   Bei Tabellenwarnungen gilt: Tabelleninhalte vor dem Zitat gegen die Quelle
   prüfen oder als unsicher kennzeichnen.
8. Versionsstände (Edition, Fassung, Datum) nimmst du aus dem Dokument selbst,
   nie aus dem Dateinamen.
9. Steht `deckung_pruefbar: false` oder der Warnblock „Maschinell gelesen", ist
   der Text **OCR und damit erzeugt, nicht extrahiert** — siehe unten.

### Gescannte Dokumente: erzeugter Text, kein Wortlaut

Ein PDF ohne Textlayer enthält keine Zeichen, sondern Bilder von Zeichen.
Docling liest sie per OCR. Das Ergebnis ist brauchbar zum Suchen, Überblicken
und Verweisen — aber es ist **erzeugter Text**, und das ändert, was du damit
tun darfst:

- Es gibt **keine Wortdeckung**. Nicht "0 %", sondern keine: es existiert
  nichts, wogegen sich prüfen ließe. Die Vaultnotiz trägt deshalb
  `text_coverage_percent: null` und `deckung_pruefbar: false` statt einer Zahl.
- **Lesefehler fallen nicht auf.** Ein falsch erkanntes "rn" statt "m" oder eine
  vertauschte Ziffer in einer Kontrollnummer sieht aus wie gültiger Text. Bei
  einem Extrakt mit Textlayer würde die Deckungsprüfung anschlagen; hier nicht.
- **Zitiere daraus nicht wörtlich.** Für ein Zitat gehst du ins Original. Im
  Fließtext kennzeichnest du die Herkunft: "sinngemäß nach `<slug>` (OCR)".

Diese Dokumente sind Teil des Bestands, aber sie tragen nicht dieselbe
Zusicherung wie der Rest. Die Unterscheidung darf nicht verwischen — sonst
wandert maschinell geratener Text als belegter Normwortlaut in ein Audit.

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
| `Docling-Modelle nicht verfügbar (… modelscope.cn … .pth)` | **nicht** fehlende Modelle: RapidOCRs ONNX-Modelle liegen im Paket `rapidocr`. Ohne `onnxruntime` fällt RapidOCR auf das Torch-Backend zurück und lädt `.pth`-Gewichte von modelscope.cn — dort meist gesperrt | `pip install onnxruntime`. Danach läuft OCR offline, ohne jeden Download |
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

Maschinenlesbare Kataloge, die als Passthrough vorliegen (BSI C5 als YAML),
werden dabei mit PyYAML gelesen und je Kriterium abgelegt. Die Anforderung
steht unter `criterion`/`condition`, der `hint` des BSI kommt als eigener
Hinweisblock in die Notiz — er ist Auslegungshilfe, keine Anforderung. Da
solche Quellen keine Seiten haben, trägt die Notiz statt `source_page` einen
`source_locator` mit dem Schlüsselpfad (`basic/01B in AM.yml`).

### Überholte Fassungen

Wird ein Dokument von einer neueren Fassung abgelöst, wird die alte **nie
gelöscht**, sondern als Historiendokument abgelegt:

```bash
python publish.py output/<alt>.md --vault <vault> --as-document \
    --titel "<Titel> (Vorgängerfassung)" --superseded-by <geltender-slug>
```

Die Notiz trägt dann `status: historisch`, den Tag `grc/historisch` und vorweg
eine Warnung, die die geltende Fassung nennt. Der Wortlaut bleibt nachlesbar —
für Audits mit Stichtag in der Vergangenheit, für Änderungsnachweise und um
Abweichungen zur neuen Fassung belegen zu können. **Zitiere ein solches Dokument
nie als geltenden Stand**; `mappings/historie.json` und der Abschnitt
„Historienstand" im Tracker sagen dir, was stattdessen gilt.

`--superseded-by` gilt nur mit `--as-document`: eine überholte Fassung als
Normtext abzulegen würde die geltenden Notizen überschreiben.

Kennt der Vault eine ID, die der aktuelle Katalog nicht mehr führt, hält
`--mark-withdrawn` sie als `status: entfallen` fest, statt eine leere Notiz
stehen zu lassen. Der Schalter greift **nur** bei maschinenlesbaren Katalogen:
aus einem PDF folgt aus einer fehlenden ID nicht, dass die Anforderung entfallen
ist — sie kann auch nur nicht gefunden worden sein.

Dokumente ohne Anforderungsraster — Leitfäden, Fachartikel, Studien,
Handbuchkapitel — kommen genauso in den Bestand, nur ohne Framework:

```bash
python publish.py output/<slug>.md --vault <vault> --as-document \
    --titel "<Titel>" --autor "<Urheber>" --art "<Art>"
```

Der Bestand umfasst **alle** aufgenommenen Dokumente, nicht nur Normen. Was
kein Normtext ist, ist deshalb nicht weniger wert — aber zitiere es als das,
was es ist: ein Fachartikel ist keine Anforderung.

## Was wurde schon aufgenommen?

`output/_TRACKER.md` (und im Vault `document-to-LLM Tracker.md`) listet jedes
aufgenommene Dokument mit Wortdeckung, Seiten, Tabellen und offenen Warnungen.
Erste Anlaufstelle bei der Frage, ob eine Norm im Bestand ist und wie gut.

```bash
python tracker.py --output output --vault <vault> --to output/_TRACKER.md
```

## Ablage

```
input/        Quelldokumente (nicht von Agenten lesen)
output/       *.md  ← einzige zulässige Textquelle
              *.docling.json  verlustfreie Struktur (Basis für den Index)
              manifest.json   Hashes, Seitenzahlen, Warnungen pro Lauf
              acsos.db        SQLite-FTS5-Index
```

## Quellen, die der Drive-Connector nicht liefert

Der Connector überträgt base64-kodiert. Das bläht den Umfang um rund ein
Drittel und lässt Dateien ab etwa 7 MB mit `session expired` scheitern — die
Meldung nennt eine Sitzung, gemeint ist die Größe. Für solche Dateien:

```bash
python fetch_drive.py <file-id> --name <Dateiname.pdf> \
       --expect-bytes <Groesse laut Drive-Metadaten>
```

Voraussetzung ist eine **befristete** Linkfreigabe der Datei. Dazu drei Dinge,
die in dieser Reihenfolge zusammengehören:

1. **Einzeln freigeben, nicht den Ordner.** Eine Ordnerfreigabe vererbt sich auf
   alles darin — im GRC-Bestand also auch auf lizenzierten Normtext, dessen
   Weitergabe an Dritte vertraglich ausgeschlossen ist (ENX/TISAX). Prüfe vor
   dem Bezug mit `get_file_permissions`, was tatsächlich offen steht.
2. **Sofort zurücknehmen.** Das Skript erinnert nach jedem Lauf daran.
3. **Bytes prüfen.** Ohne `--expect-bytes` meldet das Skript den Bezug
   ausdrücklich als ungeprüft. Eine Datei, deren Größe nicht zu den
   Drive-Metadaten passt, gehört nicht in den Bestand.

Liefert Google die Anmeldeseite, bricht das Skript ab, statt HTML als
vermeintliches Dokument abzulegen. Ab etwa 25 MB schiebt Google eine
Virenscan-Bestätigung vor den Download; die beantwortet das Skript selbst.
