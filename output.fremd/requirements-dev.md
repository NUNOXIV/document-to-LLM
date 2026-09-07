---
source_file: "requirements-dev.txt"
source_sha256: ef0b2efbd74087bd247ffa047bd0e0d3ed730e0927fe83e1f8a35e5f628e9ff6
source_bytes: 580
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
  - "Docling bringt fuer .txt keinen Reader mit. Der Inhalt (16 Zeile(n)) wurde woertlich und unveraendert uebernommen; es wurden keine Ueberschriften, Tabellen oder Seitenmarken abgeleitet. Zitate sind zeichengetreu, Strukturangaben gibt es fuer diese Datei nicht."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
# requirements-dev.txt

```text
# Nur fuer Tests und Pruefungen, nicht zur Laufzeit.

# Erzeugt das Norm-aehnliche Fixture-PDF aus fixtures/ground-truth/.
reportlab>=4.0

# Testlauf. Ohne pytest laufen die Tests mit Fixtures (tmp_path) nicht mit —
# der Skriptpfad von tests/test_units.py sagt das dann ausdruecklich.
pytest>=8.0

# Eigenschaftstests: sucht die Kennungsformen, die in keiner Beispielliste
# stehen. Genau daran ist die Ueberschriftenerkennung zweimal zerbrochen.
hypothesis>=6.100

# Linter. Konfiguration in pyproject.toml, damit lokal, im Hook und in CI
# dieselben Regeln gelten.
ruff>=0.6
```
