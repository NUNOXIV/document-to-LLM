# document-to-LLM

Extraktions- und Retrieval-Skill für **ACSOS** (Automated Cyber Security Operating
System). Wandelt komplexe GRC-Dokumente — ISO 27001/42001, BSI IT-Grundschutz, C5,
TISAX/ISA, NIS2/BSIG, DORA, CRA, NIST — in strukturerhaltendes Markdown um, das
LLM-Agenten ohne Halluzinationsrisiko lesen können.

Die Konvertierung macht ausschließlich **[IBM Docling](https://github.com/docling-project/docling)**.
Es gibt in diesem Repo bewusst keinen eigenen PDF-Parser: Layout-, Tabellen- und
Hierarchie-Erkennung übernehmen die Docling-Modelle, nicht Regex.

## Installation

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Der erste **PDF**-Lauf lädt die Docling-Layout- und TableFormer-Modelle von
`huggingface.co` (einige hundert MB). In Umgebungen ohne HF-Zugriff einmalig
vorab holen und den Cache mitgeben:

```bash
docling-tools models download          # auf einer Maschine mit HF-Zugriff
export HF_HOME=/pfad/zum/model-cache   # in der abgeschotteten Umgebung
```

Office-Formate (DOCX, XLSX, PPTX) und HTML brauchen keine Modelle.

Air-gapped oder hinter einer Egress-Policy: Modelle einmal mitbringen statt HF-Zugriff.

```bash
docling-tools models download -o ./docling-models     # Maschine mit HF-Zugriff
python extract.py datei.pdf --models-dir ./docling-models
export ACSOS_DOCLING_MODELS=./docling-models          # alternativ dauerhaft
```

Konkret geholt werden (Stand Docling 2.123):

| Modell | Repository | Groesse |
| --- | --- | --- |
| Layout | `docling-project/docling-layout-heron` | 172 MB |
| Layout (ONNX-Engine) | `docling-project/docling-layout-heron-onnx` | 171 MB |
| Tabellen (ACCURATE) | `ds4sd/docling-models` → `model_artifacts/tableformer/accurate` | 213 MB |
| OCR | ONNX-Modelle in `rapidocr` enthalten, kein Download — **aber nur mit `onnxruntime`** (siehe unten) | — |

Die Groessen sind der Grund, warum ein HF-Connector oder API-Zugang das Problem
nicht loest: die Gewichte muessen als Dateien auf die Maschine, die konvertiert.
Entweder der Host `huggingface.co` ist erreichbar, oder der Ordner wird per
`--models-dir` mitgebracht.

Für OCR gilt das **nicht**: RapidOCRs Modelle liegen als ONNX bereits im Paket.
Fehlt aber `onnxruntime`, fällt RapidOCR auf das Torch-Backend zurück und will
dessen `.pth`-Gewichte von `modelscope.cn` nachladen. Ist der Host gesperrt,
scheitert jedes gescannte PDF mit der Meldung „Docling-Modelle nicht
verfügbar" — obwohl die Modelle lokal vorliegen. Es fehlt dann nicht das
Modell, sondern die Laufzeit, die es lesen kann.

Preflight, bevor ein Bestand konvertiert wird:

```bash
python extract.py --doctor
```

Tests:

```bash
python tests/test_units.py   # Unit-Tests, ohne Modelle lauffaehig
./tests/smoke.sh        # Office-Pfad (DOCX), ohne Modelle lauffaehig
./tests/smoke_pdf.sh    # PDF-Pfad: Layout, Tabellen, Lesereihenfolge, Vollstaendigkeit
```

## Nutzung

```bash
# 1) Konvertieren  (PDF, DOCX, XLSX, PPTX, HTML)
python extract.py input/ISO-27001.pdf
python extract.py input/ --recursive --json          # ganzer Bestand + JSON für den Index

# 2) Index bauen
python index.py build --output output --db output/acsos.db

# 2b) Abweichungspruefung gegen die Quelle (laeuft bei PDFs automatisch mit)
python verify.py output/iso-27001.md --source input/ISO-27001.pdf --min-coverage 99.5

# 3) Gezielt Kontext holen
python index.py search "Schlüsselverwaltung Kryptographie" -n 5
python index.py show iso-27001 --heading "A.8"
python index.py list
```

## Zwei Engines: Docling und xberg

`extract.py` kennt zwei Konvertierungs-Engines mit demselben Ausgabevertrag
(Kopfzeile, `<!-- page: N -->`-Marken, Wortdeckung gegen den Textlayer,
Bindestrich-Rückgabe). Welche gelaufen ist, steht in jedem Extrakt
(`converter`, `engine`) und im Manifest.

```bash
python extract.py norm.pdf --engine docling      # Standard
python extract.py norm.pdf --engine xberg        # Rust-Kern, nativer Textlayer-Pfad
python extract.py norm.pdf --engine xberg --xberg-layout   # mit Layoutmodell (huggingface.co)
ACSOS_ENGINE=xberg python extract.py input/ -r   # Standard per Umgebungsvariable umstellen
python extract.py --doctor                       # prüft beide Engines
```

Gemessen am Test-PDF (`tests/fixtures/Muster-Norm-Zweispaltig.pdf`, zwei
Seiten, eine Control-Tabelle) und an NIST CSWP 29 (32 Seiten), Stand xberg
1.0.14 / Docling 2.123.0, Befehle: `extract.py … --engine <e>` und
`fundstellen.py --ground-truth fixtures/ground-truth/muster-norm-99001.json --bestand <ordner>`:

| | Docling | xberg nativ |
|---|---|---|
| Test-PDF: Dauer | 14,0 s | 2,7 s (davon 0,02 s Konvertierung) |
| Test-PDF: Resolver gegen Ground Truth | 13 verifiziert, 0 abweichend | 13 verifiziert, 0 abweichend |
| Test-PDF: Control-Tabelle | als Tabelle (6 Zeilen) | als Fließtext (0 Zeilen) |
| NIST CSWP 29: Überschriften / Tabellenzeilen | 41 / 50 | 14 / 4 |

Der Wortlaut ist bei beiden vollständig und belegt. Was xberg im nativen
Pfad nicht liefert, ist die Struktur: Tabellen werden zu Prosa, Überschriften
fehlen zum Teil. Für `publish.py`, das Anhang-A-Controls über Tabellenzeilen
auflöst, ist das ein Verlust. Sein Layoutmodell (`--xberg-layout`) und seine
OCR-Backends holt xberg von huggingface.co; wo der Host gesperrt ist, meldet
der Extrakt das als Warnung und fällt auf den nativen Pfad zurück, statt
still weniger zu liefern. Deshalb bleibt Docling hier Standard, xberg ist
eine Zeile entfernt.

## Scan-Erkennung und zwei Worker

Vor jedem PDF liest `extract.py` den Textlayer mit pypdfium2 (Sekunden, keine
Modelle). Unter 120 Zeichen je Seite gilt die Datei als Scan und geht sofort
mit OCR an Docling, statt erst ohne OCR durchzulaufen, „textarm" zu melden und
ein zweites Mal zu laufen. Der Befund steht als `scan_probe: scan|textlayer`
in der Kopfzeile; die Prüfung nach dem Lauf bleibt bestehen.

`--workers 2` (Standard) hält zwei Docling-Prozesse mit je einmal geladenen
Modellen und verteilt die Dateien darauf. Jeder Worker braucht bis zu 8 GB,
zwei sind auf 16 GB das Maximum; `--reset-every 40` ersetzt einen Worker nach
40 Dokumenten, weil sein Speicher über lange Läufe wächst.

Gemessen auf 4 Kernen, 15 GB, dieselben drei PDFs (Test-PDF, NIST CSWP 29
mit 32 Seiten, CISM Strategic Blueprint als 14-seitiger Scan mit OCR),
Befehl: `extract.py <drei PDFs> --workers N --timeout 0 -o <ordner>`:

| | Wandzeit | Scan (OCR) | NIST |
|---|---|---|---|
| 1 Worker | 193 s | 112 s | 60 s |
| 2 Worker | 173 s | 144 s | 115 s |
| 2 Worker, je 2 Threads (`OMP_NUM_THREADS=2`) | 205 s | 184 s | 118 s |

Docling nutzt schon in einem Prozess alle Kerne. Zwei Worker bringen auf
vier Kernen 10 %, weil sich die Dokumente gegenseitig bremsen; der Gewinn
wächst mit der Kernzahl und ist dort neu zu messen. Die Scan-Vorabprobe
sparte am Blueprint den verlorenen ersten Lauf: 143 s statt 184 s mit
derselben OCR.

## Was den Output belastbar macht

- **Provenienz je Datei:** YAML-Front-Matter mit SHA-256 der Quelle, Seitenzahl,
  Tabellenanzahl, Docling-Version, Konvertierungszeitpunkt.
- **Seitenmarker:** `<!-- page: N -->` im Text, damit jede Aussage zitierfähig ist.
- **Tabellen im ACCURATE-Modus:** TableFormer mit Cell-Matching gegen den
  PDF-Textlayer — Zellwerte werden übernommen, nicht rekonstruiert. Bringt
  ACCURATE eine Seite zum Absturz (kommt je nach System vor), wiederholt das
  Tool den Lauf automatisch mit FAST und vermerkt das im Extrakt, statt eine
  lückenhafte Datei zu schreiben.
- **Kein Textverlust:** fehlt nach der Konvertierung Text der Quelle, wird er
  wörtlich als Abschnitt „Nachtrag: nicht zugeordneter Quelltext" mit Seitenzahl
  angehängt (abschaltbar mit `--no-repair`). Am realen ISO/IEC 27001:2022 hebt
  das die Deckung von 99,826 % auf 100,0 %: TableFormer hatte den Rest einer
  mehrzeiligen Control-Zelle verschluckt.
- **Kein stiller Teilerfolg:** der Docling-Konvertierungsstatus wird geprüft.
  Nicht verarbeitete Seiten stehen als `docling_status` und als Warnung in der
  Datei; ein Fehlschlag bricht ab.
- **OCR-Automatik:** textarme (gescannte) PDFs werden erkannt und mit OCR
  wiederholt. Ein solcher Extrakt ist **erzeugter Text, kein Wortlaut** — siehe
  den nächsten Punkt.
- **Abweichungsprüfung, wo es etwas zu prüfen gibt:** jeder Extrakt mit
  Textlayer wird Wort für Wort gegen die Quelle geprüft — PDFs gegen den
  Textlayer (Docling-PDF-Backend, keine ML-Modelle nötig), XLSX/DOCX/PPTX gegen
  den Standardleser des Formats. Bei einem **Scan ohne Textlayer entfällt diese
  Prüfung**, weil es nichts gibt, wogegen zu prüfen wäre: der Extrakt trägt dann
  keine Deckungszahl, sondern `deckung_pruefbar: false` und den Vermerk, dass
  der Text aus der Zeichenerkennung stammt. Solche Dokumente sind durchsuchbar,
  aber nicht zitierfähig.
  Der Abgleich kommt damit immer aus einer von Docling unabhängigen Quelle.
  Die Wortdeckung steht als `text_coverage_percent` in der Front-Matter; unter
  `--min-coverage` (Default 99.5 %) gibt es eine Warnung mit den fehlenden
  Wörtern und den schwächsten Seiten. Laufende Kopf-/Fußzeilen werden nicht
  mitgezählt, über Zeilenumbrüche getrennte Wörter gelten als vorhanden.
- **Qualitätsgates:** leerer Output bricht ab; textarme Seiten, fehlende
  Gliederung, kaputte Tabellenblöcke und Encoding-Fehler landen als Warnung in
  der Datei, im `manifest.json` und im Exit-Code (`--strict`).
- **Idempotenz:** unveränderte Quellen (Hash-Vergleich) werden übersprungen.

## Ausgabe in den Obsidian-Vault

`publish.py` schreibt aus einem Extrakt je Anforderung eine Normtext-Notiz nach
`Normen (lizenziert)/<framework>/<framework> <ID> (Normtext).md` — genau die
Dateien, auf die die Framework-Notizen im Vault per Embed verweisen.

```bash
python publish.py output/iso-iec-27001-2022.md \
    --vault ~/obsidian-vault --framework iso27001-2022 --dry-run
python publish.py output/iso-iec-27001-2022.md \
    --vault ~/obsidian-vault --framework iso27001-2022
```

Für alles, was kein Anforderungsraster hat — Leitfäden, Fachartikel, Studien,
Handbuchkapitel, Behördenschreiben — gibt es denselben Weg ohne Framework:

```bash
python publish.py output/<slug>.md --vault ~/obsidian-vault --as-document \
    --titel "OWASP Web Security Testing Guide v4.2" \
    --autor "OWASP Foundation" --art Leitfaden
```

Das legt den Volltext nach `Normen (lizenziert)/dokumente/` und eine
Metadatennotiz nach `GRC/Handbuch/` an, die ihn per Embed einbindet — dieselbe
Trennung wie bei den Normen: Text lokal, Metadaten versioniert.

Welche IDs gebraucht werden, liest das Tool aus dem Vault (`GRC/Frameworks/<framework>/`,
Feld `id`). Nichts wird erfunden: was im Extrakt nicht steht, wird als fehlend
gemeldet. Klauseln ohne eigenen Text werden aus ihren Unterklauseln
zusammengesetzt; Klauseln, die das Layoutmodell nicht als Überschrift erkannt
hat, werden über ID **und** den im Vault hinterlegten Titel angesteuert.
Beginnt ein Normtext mitten im Satz, bekommt die Notiz einen Warnhinweis auf
eine mögliche Zellverschiebung.

Der Zielordner ist im Vault von der Versionierung ausgenommen — lizenzierter
Normtext bleibt lokal. Dieses Repository enthält weder Quell-PDFs noch Extrakte.

## Kreuzreferenzen für abweichende Nummerierungen

Manche Frameworks nummerieren ihre Anforderungen thematisch statt in der
Reihenfolge des Dokuments. Beim CRA ist `AnnexI.1.3` der Buchstabe d) des
Anhangs I, `AnnexI.1.11` der Buchstabe c). Eine Zuordnung nach Position wäre
falsch, deshalb liegt in `mappings/cra.json` eine geprüfte Kreuzreferenz: je ID
ein wörtliches Textstück, an dem der Abschnitt beginnt. Findet `publish.py` den
Anker nicht, meldet es die ID als fehlend, statt etwas Falsches abzulegen.

## Versionsstand prüfen

Ein Extrakt ist nur so gut wie seine Fassung. `versioncheck.py` holt zu jedem
aufgenommenen Dokument den aktuellen Stand von der offiziellen Fundstelle und
meldet, was veraltet ist.

```bash
python versioncheck.py                                   # alle Dokumente
python versioncheck.py --only wstg-v4-2                  # eines
python versioncheck.py --strict                          # Exit 1 bei Veraltetem
python versioncheck.py --to ~/obsidian-vault/"document-to-LLM Versionsstand.md"
```

Die Fundstellen und Suchmuster stehen in `versions.json`. Nichts wird aus dem
Gedächtnis beantwortet. Es gibt drei Befunde:

| Befund | Bedeutung |
| --- | --- |
| `aktuell` / `VERALTET` | Stand von der offiziellen Seite geholt und verglichen |
| `aus Dokument belegt` | Die Fassung steht im lizenzierten Dokument selbst und wird von dort gelesen — mit Datei und Seitenzahl als Beleg. Belegt, **welche** Fassung vorliegt, nicht dass keine neuere existiert |
| `manuell prüfen` / `Quelle offline` | Weder Seite noch Dokument geben es her |

Der mittlere Fall greift für ISO 27001 und ISO 42001 (Katalog kostenpflichtig),
VDA ISA (ENX verlangt Anmeldung) und die EU-Rechtsakte (EUR-Lex führt
konsolidierte Fassungen ohne Versionsnummer, das Amtsblattdatum steht im Text).

## Aufnahmeprotokoll

`tracker.py` schreibt eine Übersicht über alle Extrakte — je Dokument Wortdeckung,
Seiten, Tabellen, Überschriften, entfernte Kopf-/Fußzeilen, Nachträge und offene
Warnungen. Die Datei wird bei jedem Lauf neu erzeugt und veraltet damit nicht.

```bash
python tracker.py --output output --input input \
    --vault ~/obsidian-vault \
    --to output/_TRACKER.md \
    --to ~/obsidian-vault/"document-to-LLM Tracker.md"
```

Typischer Durchlauf für einen ganzen Bestand:

```bash
python extract.py input/ --recursive --json      # konvertieren + prüfen
python publish.py output/<slug>.md --vault ~/obsidian-vault --framework <fw>
python index.py build --output output            # Retrieval-Index
python tracker.py --output output --vault ~/obsidian-vault --to output/_TRACKER.md
```

## Drei Prüfebenen — Konsistenz ist nicht Wahrheit

Die Abweichungsprüfung oben misst, ob der Extrakt zur Quelle passt. Sie misst
nicht, ob der *Wortlaut* stimmt, den ein Export unter einer Kennung führt.
Dafür gibt es drei Wächter, die verschiedene Dinge messen:

```bash
python pruefe.py      --export export/ --strict                   # Plausibilität
python inhalt.py      --export export/ --output output/ --strict  # Wortlaut je Kennung
python fundstellen.py --bestand output/ --strict                  # gegen den Primärtext
python bindestriche.py                                            # verlorene Bindestriche
```

| Wächter | Frage | Blind für |
|---|---|---|
| `pruefe.py` | Ist der Bestand in sich plausibel? Längenverteilung, doppelte Kennungen, leere Texte | Ob der Inhalt stimmt |
| `inhalt.py` | Steht unter jeder Kennung ihr eigener Wortlaut? | Ob die Quelle richtig gelesen wurde |
| `fundstellen.py` | Stimmt der Wortlaut mit einem Primärtext überein, den niemand aus dem Ergebnis abgeleitet hat? | Alles, wofür keine Ground Truth vorliegt |

Der Befund des Resolvers ist dreiwertig und nie zweiwertig: `verifiziert`,
`abweichend` (Kennung da, Wortlaut nicht — der gefährliche Fall) und
`unverifiziert` (nicht geprüft). „Unverifiziert" ist ausdrücklich erlaubt.
Ein ungeprüftes Ergebnis, das wie ein geprüftes aussieht, nicht.

### Primärtexte importieren

```bash
python rechtsakte.py import input/ --alle   # amtliches XML -> fixtures/ground-truth/
python rechtsakte.py liste                  # welche Primärtexte liegen vor, mit Stand
```

`rechtsakte.py` liest das XML von gesetze-im-internet.de über den XML-Parser der
Standardbibliothek — keine Ausnahme von der Parser-Regel: die gilt PDFs, wo ein
Parser aus Koordinaten und Schriftgrößen raten muss. Hier ist jeder Paragraf ein
Element mit Bezeichnung, Titel und Text, nach veröffentlichter DTD. Amtliche
Werke sind nach § 5 UrhG gemeinfrei; dieser Primärtext darf deshalb — anders als
ISO- oder TISAX-Wortlaut — im Repository liegen.

Was der erste Lauf gegen den BSIG-Extrakt fand: **Docling verliert Bindestriche.**
Beim Zeilenumbruch entfernt es den Trennstrich — richtig bei „Informations-/
sicherheit", falsch bei „IKT-/Systemen", woraus „IKTSystemen" wird. Die
Wortdeckung sah das nie, weil sie denselben Strich auch auf der Quellseite
entfernt: beide Seiten hießen gleich, die Deckung blieb 100,0 %. Betroffen waren
**187 von 269 PDF-Extrakten mit 1058 Wörtern.**

`bindestriche.py` setzt sie zurück — nur mit doppeltem Beleg: die Form ohne
Bindestrich kommt in der Quelle nirgends vor, **und** die Form mit Bindestrich
steht dort zusammenhängend, also ohne Umbruch dazwischen. Der zweite Beleg ist
der entscheidende: ohne ihn kehrt die Reparatur die echte Silbentrennung um und
macht aus dem richtigen „Abnahme" wieder „Ab-nahme". Ohne Schalter wird nur
gezählt und angezeigt; `--reparieren` ändert.

`fixtures/ground-truth/` hält den Primärtext. `tests/make_fixture.py` **erzeugt
das Test-PDF daraus**, `fundstellen.py` prüft **dagegen** — eine Datei, zwei
Richtungen. Stünde der Wortlaut zweimal, wäre die Prüfung eine
Selbstbestätigung.

`tests/pruefungen.sh` belegt für jeden Wächter beide Richtungen: bei gesunden
Daten muss er schweigen, bei absichtlich beschädigten anschlagen. Ein Wächter,
der nur die erste Probe besteht, könnte kaputt sein und schwiege genauso.

## Regeln für Agenten

Siehe [`SKILL.md`](SKILL.md). Kurzfassung: Kontext kommt aus `output/`, niemals
aus dem PDF; Zitate mit Slug, Gliederung und Seitenzahl belegen; bei
`extraction_status: warn` die Warnungen lesen.

Wer am Repo selbst arbeitet: [`CLAUDE.md`](CLAUDE.md) (Befehle, vier
Verifikationsregeln, Codestil) und [`lessons-learned.md`](lessons-learned.md)
(jeder gefundene Defekt mit Ursache, Fix und Regressionstest).

## Ordner

```
fixtures/ground-truth/   Primärtexte als Prüfmaßstab (erfunden oder amtlich, deshalb im Repo)
input/     Quelldokumente
output/    *.md (verbindliche Textquelle für Agenten)
           *.docling.json / *.passthrough.json (Struktur für verarbeitende Systeme)
           _KORPUS.json (Bestandsregister: Pfade, Deckung, Befund je Dokument)
           manifest.json (Lauf-Protokoll), acsos.db (Suchindex)
```
