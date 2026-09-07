---
source_file: ".pre-commit-config.yaml"
source_sha256: 6c99705d9c0ee8892e4d777c67a12b04da41fb025c9d6626f1b5249cc3b11e54
source_bytes: 1510
pages: 0
tables: 0
converter: "ACSOS Passthrough (woertlich, kein Parser)"
engine: passthrough
ocr: false # mode=auto
table_mode: not-applicable
docling_status: not-applicable
converted_at: "2026-09-07T01:18:48+00:00"
text_coverage_percent: 100.0
extraction_status: warn
warnings:
  - "Docling bringt fuer .yaml keinen Reader mit. Der Inhalt (44 Zeile(n)) wurde woertlich und unveraendert uebernommen; es wurden keine Ueberschriften, Tabellen oder Seitenmarken abgeleitet. Zitate sind zeichengetreu, Strukturangaben gibt es fuer diese Datei nicht."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
# .pre-commit-config.yaml

```yaml
# Dieselben Pruefungen wie in CI, nur frueher. Zweck ist nicht Ordnung,
# sondern Zeit: eine rote CI kostet einen Push, eine Mail und einen
# Kontextwechsel; ein roter Commit kostet zehn Sekunden.
#
#   pip install pre-commit && pre-commit install
#
# Was hier NICHT laeuft: smoke_pdf.sh. Der Lauf braucht die Docling-Modelle und
# eine halbe Minute — vor jedem Commit ist das zu teuer, in CI ist es richtig.
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.12.5
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-json
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-merge-conflict
      # Lizenzierter Normtext gehoert nicht ins Repo. Die .gitignore deckt
      # input/, output/ und export/ ab; diese Grenze faengt das versehentlich
      # anderswo abgelegte grosse PDF.
      - id: check-added-large-files
        args: [--maxkb=2048]

  - repo: local
    hooks:
      - id: tests
        name: Testlauf (pytest, inkl. Eigenschaftstests)
        entry: python -m pytest
        language: system
        pass_filenames: false
        types: [python]

      - id: waechter
        name: Waechter belegen (schweigen bei gesund, anschlagen bei kaputt)
        entry: ./tests/pruefungen.sh
        language: system
        pass_filenames: false
        files: '^(pruefe|inhalt|fundstellen|publish)\.py$|^tests/pruefungen\.sh$'
```
