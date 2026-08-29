#!/usr/bin/env bash
# Smoke-Test der Pipeline gegen die Fixture unter tests/fixtures/.
# Nutzung: ./tests/smoke.sh   (aus dem Repo-Wurzelverzeichnis, venv aktiv)
set -euo pipefail

PY="${PYTHON:-python}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "== extract =="
"$PY" extract.py "tests/fixtures/Muster-Norm ISO Test.docx" -o "$TMP" --json

MD="$TMP/muster-norm-iso-test.md"
test -f "$MD" || { echo "FAIL: kein Markdown erzeugt"; exit 1; }
grep -q "source_sha256:" "$MD"                  || { echo "FAIL: Front-Matter fehlt"; exit 1; }
grep -q "^### 4.1 " "$MD"                        || { echo "FAIL: Gliederungsebene verloren"; exit 1; }
grep -q "^| A.8.24 " "$MD"                       || { echo "FAIL: Control-Tabelle verloren"; exit 1; }
grep -q "Schluesselverwaltung" "$MD"             || { echo "FAIL: Tabelleninhalt verloren"; exit 1; }

echo "== index =="
"$PY" index.py build --output "$TMP" --db "$TMP/acsos.db"
HIT="$("$PY" index.py search "Kryptographie" --db "$TMP/acsos.db" -n 1)"
grep -qi "kryptographie" <<<"$HIT" || { echo "FAIL: Suche liefert keinen Treffer"; exit 1; }

echo "== idempotenz =="
AGAIN="$("$PY" extract.py "tests/fixtures/Muster-Norm ISO Test.docx" -o "$TMP")"
grep -q "uebersprungen" <<<"$AGAIN" || { echo "FAIL: unveraenderte Quelle wurde erneut konvertiert"; exit 1; }

echo "OK — Extraktion, Struktur, Tabellen, Index und Idempotenz bestaetigt."
