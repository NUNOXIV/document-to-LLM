---
source_file: "requirements.txt"
source_sha256: c5b0de412308f1ecb3151520a71db388f8e1df75583ed3f1a7fdb40614a28362
source_bytes: 1406
pages: 0
tables: 0
converter: "ACSOS Passthrough (woertlich, kein Parser)"
engine: passthrough
ocr: false # mode=auto
table_mode: not-applicable
docling_status: not-applicable
converted_at: "2026-09-07T01:18:54+00:00"
text_coverage_percent: 100.0
extraction_status: warn
warnings:
  - "Docling bringt fuer .txt keinen Reader mit. Der Inhalt (24 Zeile(n)) wurde woertlich und unveraendert uebernommen; es wurden keine Ueberschriften, Tabellen oder Seitenmarken abgeleitet. Zitate sind zeichengetreu, Strukturangaben gibt es fuer diese Datei nicht."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
# requirements.txt

```text
# ACSOS document-to-LLM — Extraktions- und Retrieval-Stack
#
# Konvertierung ausschliesslich ueber IBM Docling. Es werden bewusst KEINE
# eigenen PDF-Parser (PyPDF, pdfminer, Regex) verwendet: Layout-, Tabellen- und
# Hierarchie-Erkennung uebernimmt das Docling-Layoutmodell.

docling>=2.26.0        # Konvertierungs-Engine (PDF, DOCX, XLSX, PPTX, HTML, MD)
docling-core>=2.23.0   # DoclingDocument, Serializer, HierarchicalChunker
xberg>=1.0.14          # zweite Engine (extract.py --engine xberg), Rust-Kern
click>=8.1.7           # CLI
PyYAML>=6.0            # publish.py: maschinenlesbare Kataloge (BSI C5 als YAML)
onnxruntime>=1.17      # OCR fuer gescannte PDFs, siehe Hinweis unten

# OCR: Docling nutzt RapidOCR. Dessen ONNX-Modelle liegen bereits im Paket
# rapidocr; ohne onnxruntime faellt RapidOCR aber auf das Torch-Backend zurueck
# und laedt Gewichte von modelscope.cn nach. Wo dieser Host gesperrt ist,
# scheitert damit jedes gescannte PDF ("Docling-Modelle nicht verfuegbar"),
# obwohl die Modelle lokal vorliegen. onnxruntime macht OCR offline nutzbar.
# Wichtig: OCR-Text ist erzeugter, nicht extrahierter Text. Ein Wortabgleich
# gegen den Textlayer ist bei Scans unmoeglich; die Extrakte tragen deshalb
# die Warnung "Kein Textlayer im PDF" und gelten nicht als deckungsgeprueft.

# Optional, nur fuer `index.py --chunker hybrid` (token-genaues Chunking):
#   transformers>=4.40.0
```
