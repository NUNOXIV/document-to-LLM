# CLAUDE.md — Arbeitsregeln für dieses Repo

Kurz gehalten. Was hier steht, gilt; was nicht mehr gilt, wird gelöscht.
Ein langes CLAUDE.md verdünnt die Aufmerksamkeit, es ist kein Archiv.
Vorgeschichte steht in `lessons-learned.md`, nicht hier.

## Was dieses Repo ist

Ein Skill, keine Bibliothek. Es wandelt GRC-Normen mit IBM Docling (Standard)
oder xberg (`--engine xberg`) in
strukturerhaltendes Markdown und stellt sie als Index bereit. Fachliche
Beschreibung: `SKILL.md`. Aufbau: `README.md`.

## Befehle

```bash
# Umgebung
pip install -r requirements.txt -r requirements-dev.txt
python extract.py --doctor            # Textlayer, Docling-Modelle, xberg einsatzbereit?

# Testlauf (das ist die Definition of Done, nicht "sieht gut aus")
python -m pytest                      # alle Tests, inkl. Eigenschaftstests
ruff check .                          # Linter, Konfiguration in pyproject.toml
./tests/smoke.sh                      # Office-Pfad, Ende zu Ende
./tests/smoke_pdf.sh                  # PDF-Pfad, braucht Docling-Modelle
./tests/pruefungen.sh                 # belegt, dass die Wächter anschlagen

# Prüfebenen einzeln
python pruefe.py    --export export/ --strict     # Plausibilität (Konsistenz)
python inhalt.py    --export export/ --output output/ --strict  # Wortlaut je Kennung
python fundstellen.py --bestand output/ --strict   # gegen den Primärtext
python vollstaendigkeit.py --strict               # hat JEDE Quelle einen Extrakt?
python bindestriche.py                            # verlorene Bindestriche (zählt nur)
python rechtsakte.py import input/ --alle         # amtliches XML als Ground Truth
```

`python tests/test_units.py` läuft auch ohne pytest, lässt dann aber die Tests
mit Fixtures aus — und sagt das am Ende ausdrücklich. Verlass dich im Zweifel
auf `pytest`.

## Die eine Regel

**Ein Agent parst niemals ein PDF selbst.** Kein PyPDF, kein `pdftotext`, kein
Regex über Rohtext. Konvertiert wird mit Docling oder xberg, sonst nichts. Inhalt kommt aus `output/` oder nirgendwoher. Begründung in
`SKILL.md`.

## Vier Verifikationsregeln

1. **Jede Fundstelle braucht einen Resolver-Treffer.** Was `fundstellen.py`
   nicht gegen `fixtures/ground-truth/` auflöst, trägt den Status
   `unverifiziert` — sichtbar, im Datenfeld, nicht im Fließtext. "Unverifiziert"
   ist erlaubt. Ein ungeprüftes Ergebnis, das wie ein geprüftes aussieht, nicht.
2. **Zwei Quellen für Zahlen, Fristen und Ausgabestände.** Eine Quelle heißt
   unbestätigt und wird so gekennzeichnet. Die Wortdeckung liest deshalb mit
   einem *zweiten*, unabhängigen Leser gegen (`verify.py`), nie mit demselben.
   Und zwei Prüfungen, die denselben Vorverarbeitungsschritt teilen, sind eine
   Prüfung: die verlorenen Bindestriche blieben unsichtbar, weil Extrakt und
   Quelle beide durch dieselbe Trennstrich-Entfernung liefen.
3. **Jede Summe wird gerechnet, nie geschrieben.** Anzahlen, Quoten und Mediane
   kommen aus Code (`pruefe.py`, `tracker.py`), nicht aus dem Kopf. Steht eine
   Zahl in einem Bericht, muss der Befehl daneben stehen, der sie erzeugt.
4. **Single-Source-Daten wandern nicht ungeprüft in Handlungsanweisungen.**
   Ein Dateiname, eine Kopfzeile, ein Registereintrag sind Hinweise, keine
   Belege. Erst der Abgleich mit dem Dokument macht daraus eine Aussage.

## Prüfebenen: Konsistenz ist nicht Wahrheit

Drei Wächter, die verschiedene Dinge messen — keiner ersetzt einen anderen:

| Wächter | Frage | Blind für |
|---|---|---|
| `pruefe.py` | Ist der Bestand in sich plausibel? | Ob der Inhalt stimmt |
| `inhalt.py` | Steht unter jeder Kennung ihr eigener Wortlaut? | Ob die Quelle richtig gelesen wurde |
| `fundstellen.py` | Stimmt der Wortlaut mit dem Primärtext überein? | Alles, wofür keine Ground Truth vorliegt |
| `bindestriche.py` | Fehlt ein Bindestrich, den die Quelle hat? | Alles außer Bindestrichen |
| `vollstaendigkeit.py` | Hat **jede** Quelldatei einen Extrakt? | Ob der Extrakt etwas taugt |

Alle vier sehen sich an, was **da** ist. `vollstaendigkeit.py` fragt als
einziger, was **fehlt** — und läuft deshalb über `input/`, nicht über den
Bestand. Ein Dokument, das nie eingespeist wurde, hat keinen Extrakt, der
auffallen könnte: so fehlten 134 von 602 Dokumenten, und gemerkt hat es
niemand im System, sondern eine Übersicht außerhalb davon.

Ein Wächter, der nur auf gesunden Daten läuft, belegt nichts: er könnte kaputt
sein und schwiege genauso. `tests/pruefungen.sh` führt deshalb für jeden die
Gegenprobe — er muss bei gesunden Daten schweigen **und** bei absichtlich
beschädigten anschlagen. Wer einen Wächter ändert, hält die Gegenprobe mit.

## Ground Truth

`fixtures/ground-truth/` enthält Primärtexte, die niemand aus einem Ergebnis
abgeleitet hat. `tests/make_fixture.py` **erzeugt das Test-PDF daraus**, und
`fundstellen.py` prüft den Extrakt **dagegen**. Eine Datei, zwei Richtungen.
Schreib den Wortlaut nie ein zweites Mal in den Generator — ein Test, dessen
Sollwert aus derselben Hand stammt wie das Ergebnis, ist eine
Selbstbestätigung. `test_ground_truth_deckt_das_fixture` hält das fest.

Der einzige Primärtext im Repo ist frei erfunden. Lizenzierter Normtext (ISO,
DIN, TISAX) bleibt draußen: `input/`, `output/` und `export/` sind ignoriert,
der Vault liegt außerhalb des Repos.

## Datenregeln

- **Framework-eigene Nummerierungen sind unantastbar.** `A.5.16`, `APP.1.1.A1`,
  `INF.10.A3` werden nie ersetzt, nie umgeschrieben, nie „vereinheitlicht“. Eine
  einheitliche Nummerierung entsteht in ACSOS beim Mappen, zusätzlich.
- **Jedes Dokument wird vollständig übernommen.** Es wird nichts weggelassen,
  auch nicht mit Verweis auf Lizenzen — die Lizenzen liegen vor. Fehlt Text,
  ist das ein Fehler, keine Entscheidung.
- **Versionsstand prüfen, Abweichung melden** (`versioncheck.py`). Veraltete
  Fassungen werden ersetzt und nur als Historiendokument hinterlegt.

## Codestil

Deutsch in Kommentaren, Docstrings und Ausgaben, ASCII-Umschrift im Code
(`ue`, `ae`, `ss`), Umlaute in Nutzertexten. Ein Kommentar sagt **warum**,
nicht was — bevorzugt anhand des Fehlers, den die Zeile verhindert. Der
Linter-Regelsatz ist bewusst schmal, damit Rot etwas bedeutet.

Neuer Wächter oder neue Prüfung: erst der Test, der ohne den Fix rot ist, dann
der Fix. Ein Fix ohne Regressionstest ist unfertig.

Wer über den ganzen Bestand schreibt, prüft **vor** dem Schreiben eine Zusage
über das Ergebnis (`beginnt mit ---`, `Rumpf unverändert`) und bietet einen
Probelauf an, der nur zählt. Ein vertauschter Variablenname hat so einmal 187
Extrakte um ihre Provenienz gebracht — der Probelauf sah gut aus, weil er die
schreibende Zeile nie ausführt.
