# Eingelesener Dokumentenbestand — document-to-LLM

Stand: 01.09.2026. Alle Zahlen sind aus `_KORPUS.json` gerechnet, keine
geschätzt.

## Was hier drin liegt

    extrakte/                468 Markdown-Extrakte — die verbindliche Textquelle
    INHALTSVERZEICHNIS.csv   eine Zeile je Dokument: Quelle, SHA-256, Seiten,
                             Wörter, Deckung, Befund
    _KORPUS.json             dasselbe maschinenlesbar (Bestandsregister)
    manifest.json            Lauf-Protokoll der Extraktion
    _TRACKER.md              Zustandsbericht über den Bestand
    _VERSIONEN.md            Versionsstände je Dokument
    _GS-STRUKTUR.md          Gliederung des BSI-Grundschutz-Kompendiums

## Der Bestand in Zahlen

| | |
|---|---|
| Dokumente | **468** |
| Seiten | 11.708 |
| Wörter | 4.838.842 |
| Mit 100,0 % Wortdeckung | 441 |
| Ohne prüfbare Deckung | 12 |

**Quellformate:** 269 PDF, 146 XLSX, 21 DOCX, 19 YAML, 8 Markdown, 3 XML,
1 MM, 1 PPTX.

**Befund je Dokument:**

| Befund | Anzahl | Bedeutung |
|---|---|---|
| vollständig | 441 | kein Wort der Quelle fehlt |
| Rest wörtlich angehängt | 15 | Tabellenmodell hat einen Rest verschluckt, er steht wörtlich im Abschnitt „Nachtrag" |
| nicht gegengeprüft (Format) | 8 | Markdown-Quellen: es gibt keinen zweiten Leser, gegen den zu prüfen wäre |
| kein Textlayer | 3 | Scan, Text stammt aus der Zeichenerkennung — durchsuchbar, nicht zitierfähig |
| Textlayer zu dünn | 1 | Referenz zu klein für eine belastbare Deckungsquote |

## Wie die Dateien zu lesen sind

Jeder Extrakt trägt YAML-Front-Matter mit Provenienz: SHA-256 der Quelle,
Seitenzahl, Docling-Version, Konvertierungszeitpunkt, Wortdeckung und alle
Warnungen. Im Text stehen `<!-- page: N -->` Marker, damit jedes Zitat mit
Seitenzahl belegbar ist.

`restored_hyphens: N` im Kopf heißt: N Wörter hatten einen Bindestrich der
Quelle verloren (Docling entfernt den Trennstrich am Zeilenumbruch, auch wenn
er zum Wort gehört) und wurden zurückgesetzt — jeweils belegt durch den
Textlayer der Quelle. Korpusweit betraf das 187 Dokumente und 1058 Wörter.

## Was NICHT im Paket ist

- `*.docling.json` (445 Dateien, 571 MB) — verlustfreie Docling-Struktur für
  verarbeitende Systeme. Zu groß für dieses Paket; auf Zuruf separat.
- `acsos.db` (100 MB) — der SQLite-Volltextindex, 71.152 Chunks. Wird mit
  `python index.py build` aus den Extrakten neu erzeugt.
- Die Quelldateien selbst (`input/`). Die liegen bei dir.

## Rechtliches

Der Inhalt ist lizenzierter Normtext (ISO, DIN, TISAX u. a.) sowie amtliches
und frei verfügbares Material. Er liegt deshalb bewusst außerhalb des
Repositories — `input/`, `output/` und `export/` sind in `.gitignore`.
