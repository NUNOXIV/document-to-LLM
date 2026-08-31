#!/usr/bin/env bash
# Hook: laeuft nach jedem Schreibzugriff auf eine Python-Datei.
#
# Warum ein Hook und keine Bitte im Prompt: ein Prompt ist eine Bitte, ein Hook
# ist eine Regel. Was uebersprungen werden kann, wird irgendwann uebersprungen —
# meistens dann, wenn es eilig ist, also genau dann, wenn Fehler entstehen.
#
# Bewusst nur der Linter, nicht die Testsuite: die Tests brauchen ein paar
# Sekunden, ein Hook nach jedem Edit muss unter einer Sekunde bleiben, sonst
# wird er abgeschaltet. Die Tests laufen im pre-commit-Hook und in CI, also
# vor jedem Commit und vor jedem Merge.
#
# Eingabe kommt als JSON auf stdin (Claude-Code-Hook-Schnittstelle).
set -uo pipefail
cd "$(dirname "$0")/../.." || exit 0

datei="$(python3 -c 'import json,sys
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
print((d.get("tool_input") or {}).get("file_path", ""))' 2>/dev/null)"

case "$datei" in
  *.py) ;;
  *) exit 0 ;;
esac
[ -f "$datei" ] || exit 0

command -v ruff >/dev/null 2>&1 || exit 0

if ! ausgabe="$(ruff check "$datei" 2>&1)"; then
  # Exit 2 gibt die Meldung an Claude zurueck, statt sie nur zu protokollieren.
  echo "Linter rot in $datei — bitte beheben, bevor es weitergeht:" >&2
  echo "$ausgabe" >&2
  exit 2
fi
exit 0
