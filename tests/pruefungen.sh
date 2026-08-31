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

echo "1/6 gesunder Datensatz -> Inhaltspruefung muss schweigen"
"${PY:-python}" inhalt.py --export "$tmp/export" --output "$tmp/output" --strict

echo "2/6 Versatz eingebaut -> Inhaltspruefung muss anschlagen"
if "${PY:-python}" inhalt.py --export "$tmp/kaputt" --output "$tmp/output" --strict 2>/dev/null; then
  echo "FEHLER: Der Versatz blieb unbemerkt. Der Waechter ist blind." >&2
  exit 1
fi

echo "3/6 Plausibilitaetspruefung laeuft und meldet nichts Falsches"
"${PY:-python}" pruefe.py --export "$tmp/export" --korpus "$tmp/fehlt.json" --strict

# --- Fundstellen-Resolver ------------------------------------------------
# Die Ebene, die den anderen Waechtern fehlt: Abgleich gegen einen Primaertext,
# den niemand aus dem Ergebnis abgeleitet hat. Auch hier beide Richtungen.
mkdir -p "$tmp/gt"
cat > "$tmp/gt/muster.json" <<'GT'
{
  "quelle": "Muster-Primaertext",
  "kurzname": "muster",
  "fundstellen": [
    {"id": "1.1", "art": "abschnitt", "titel": "Erste Anforderung",
     "text": "Die Institution MUSS das eine tun."},
    {"id": "1.2", "art": "abschnitt", "titel": "Zweite Anforderung",
     "text": "Die Institution SOLLTE das andere tun."}
  ]
}
GT

echo "4/6 Extrakt stimmt mit dem Primaertext ueberein -> Resolver muss schweigen"
"${PY:-python}" fundstellen.py --ground-truth "$tmp/gt" --bestand "$tmp/output/muster.md" --strict

echo "5/6 Woertlaut im Extrakt veraendert -> Resolver muss anschlagen"
sed 's/das eine tun/das eine unterlassen/' "$tmp/output/muster.md" > "$tmp/verdreht.md"
if "${PY:-python}" fundstellen.py --ground-truth "$tmp/gt" --bestand "$tmp/verdreht.md" \
     --strict >/dev/null 2>&1; then
  echo "FEHLER: veraenderter Woertlaut galt als verifiziert. Der Resolver ist blind." >&2
  exit 1
fi

echo "6/6 Versatz im Export -> Resolver muss die Kennung als abweichend melden"
# Der Export ordnet Text einer Kennung zu. Steht unter 1.1 der Satz von 1.2,
# ist die Kennung da und der Woertlaut falsch -- der Fall, den Laenge und
# Schema nicht sehen.
if "${PY:-python}" fundstellen.py --ground-truth "$tmp/gt" \
     --bestand "$tmp/kaputt/muster.json" --strict >/dev/null 2>&1; then
  echo "FEHLER: Versatz im Export galt als verifiziert. Der Resolver ist blind." >&2
  exit 1
fi

echo "Drei Waechter belegt: sie schweigen bei gesunden und schlagen bei kaputten Daten an."
