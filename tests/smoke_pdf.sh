#!/usr/bin/env bash
# End-to-End-Test des PDF-Pfads: Docling-Konvertierung mit Layout- und
# Tabellenmodell, Strukturpruefung, Abweichungspruefung, Index.
# Braucht die Docling-Modelle (erster Lauf laedt sie).
#
# Nutzung: ./tests/smoke_pdf.sh
set -euo pipefail

PY="${PYTHON:-python}"
PDF="tests/fixtures/Muster-Norm-Zweispaltig.pdf"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

test -f "$PDF" || { echo "FAIL: Fixture fehlt ($PDF) — 'python tests/make_fixture.py'"; exit 1; }

echo "== extract (PDF, strikt, Mindestdeckung 99.5 %) =="
"$PY" extract.py "$PDF" -o "$TMP" --json --strict --min-coverage 99.5

MD="$TMP/muster-norm-zweispaltig.md"
test -f "$MD" || { echo "FAIL: kein Markdown erzeugt"; exit 1; }

fail() { echo "FAIL: $1"; echo "--- Auszug ---"; sed -n 1,60p "$MD"; exit 1; }

echo "== Struktur =="
grep -q "^text_coverage_percent: " "$MD"        || fail "Deckungsquote fehlt in der Front-Matter"
grep -q "extraction_status: ok"   "$MD"          || fail "Status nicht ok (Warnungen im Extrakt)"
grep -q "<!-- page: 1 -->" "$MD"                 || fail "Seitenmarker Seite 1 fehlt"
grep -q "<!-- page: 2 -->" "$MD"                 || fail "Seitenmarker Seite 2 fehlt"
grep -qE "^#{1,6} .*4\.1 Verstehen" "$MD"        || fail "Gliederungspunkt 4.1 ist keine Ueberschrift"
grep -qE "^#{1,6} .*5\.1 " "$MD"                 || fail "Gliederungspunkt 5.1 ist keine Ueberschrift"

echo "== Tabelle =="
grep -qE "^\|.*A\.8\.24.*\|" "$MD"               || fail "Control A.8.24 nicht als Tabellenzeile erhalten"
grep -qE "^\|.*A\.8\.24.*Schlüsselverwaltung|Schlüsselverwaltung" "$MD" \
                                                 || fail "Zellinhalt der Control-Tabelle verloren"
for c in A.5.1 A.8.24 A.8.25 A.8.28; do
  grep -q "$c" "$MD"                             || fail "Control $c fehlt vollstaendig"
done

echo "== Zweispaltigkeit / Lesereihenfolge =="
# Der Text von 4.1 muss vor 5.1 stehen, sonst wurde spaltenweise falsch gelesen.
L41=$(grep -n "4\.1 Verstehen" "$MD" | head -1 | cut -d: -f1)
L51=$(grep -n "5\.1 " "$MD" | head -1 | cut -d: -f1)
[ "$L41" -lt "$L51" ]                            || fail "Lesereihenfolge der Spalten vertauscht"

echo "== Kopf-/Fusszeilen =="
HDR=$(grep -c "nur zu Testzwecken" "$MD" || true)
[ "$HDR" -le 1 ]                                 || fail "Kopfzeile verschmutzt den Extrakt ($HDR Treffer)"

echo "== Abweichungspruefung (eigenstaendig) =="
"$PY" verify.py "$MD" --source "$PDF" --min-coverage 99.5

echo "== Regression: Luecke muss erkannt werden =="
GAP="$TMP/gap.md"
sed 's/Schlüsselverwaltung//g; s/Kryptographie//g' "$MD" > "$GAP"
if "$PY" verify.py "$GAP" --source "$PDF" --min-coverage 99.5 >/dev/null 2>&1; then
  echo "FAIL: entfernter Text wurde nicht als Abweichung erkannt"; exit 1
fi

echo "== Index =="
"$PY" index.py build --output "$TMP" --db "$TMP/acsos.db"
HIT="$("$PY" index.py search "Schlüsselverwaltung" --db "$TMP/acsos.db" -n 1)"
grep -qi "schlüsselverwaltung" <<<"$HIT" || { echo "FAIL: Suche findet den Controltext nicht"; exit 1; }

echo "OK — PDF-Pfad: Struktur, Tabellen, Lesereihenfolge, Vollstaendigkeit und Index bestaetigt."
