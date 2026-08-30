#!/usr/bin/env bash
# Prueft, ob die Waechter selbst funktionieren -- nicht, ob der Bestand sauber
# ist (den sieht CI nicht). Ein Waechter, der nur auf gesunden Daten laeuft,
# belegt nichts: er koennte kaputt sein und schwiege genauso.
#
# Deshalb zwei Richtungen: gegen einen gesunden Datensatz muss er schweigen,
# gegen einen absichtlich beschaedigten muss er anschlagen. Faellt eine der
# beiden Proben aus, ist die Pruefung wertlos und der Build bricht.
set -euo pipefail

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/export" "$tmp/output"

# --- gesunder Datensatz -------------------------------------------------
cat > "$tmp/output/muster.md" <<'MD'
---
source_file: "Muster.pdf"
source_sha256: abc123
pages: 2
text_coverage_percent: 100.0
---

## 1.1 Erste Anforderung

Die Institution MUSS das eine tun.

## 1.2 Zweite Anforderung

Die Institution SOLLTE das andere tun.
MD

"${PY:-python}" - "$tmp" <<'PY'
import json, sys
from pathlib import Path
t = Path(sys.argv[1])
gesund = {"frameworkId": "muster", "edition": "1.0", "sourceFile": "Muster.pdf",
          "sourceSha256": "abc123", "requirements": [
    {"id": "1.1", "title": "Erste Anforderung",
     "text": "Die Institution MUSS das eine tun.", "group": "1"},
    {"id": "1.2", "title": "Zweite Anforderung",
     "text": "Die Institution SOLLTE das andere tun.", "group": "1"}]}
(t / "export" / "muster.json").write_text(
    json.dumps(gesund, ensure_ascii=False, indent=2), encoding="utf-8")

# Beschaedigt: Versatz um eine Position. Laengen und Kennungen bleiben
# unauffaellig -- genau der Fehler, den keine Formpruefung findet.
kaputt = json.loads(json.dumps(gesund))
kaputt["requirements"][0]["text"] = "Die Institution SOLLTE das andere tun."
(t / "kaputt").mkdir()
(t / "kaputt" / "muster.json").write_text(
    json.dumps(kaputt, ensure_ascii=False, indent=2), encoding="utf-8")
PY

echo "1/3 gesunder Datensatz -> Inhaltspruefung muss schweigen"
"${PY:-python}" inhalt.py --export "$tmp/export" --output "$tmp/output" --strict

echo "2/3 Versatz eingebaut -> Inhaltspruefung muss anschlagen"
if "${PY:-python}" inhalt.py --export "$tmp/kaputt" --output "$tmp/output" --strict 2>/dev/null; then
  echo "FEHLER: Der Versatz blieb unbemerkt. Der Waechter ist blind." >&2
  exit 1
fi

echo "3/3 Plausibilitaetspruefung laeuft und meldet nichts Falsches"
"${PY:-python}" pruefe.py --export "$tmp/export" --korpus "$tmp/fehlt.json" --strict

echo "Beide Waechter belegt: sie schweigen bei gesunden und schlagen bei kaputten Daten an."
