# Lessons Learned

Ein Eintrag je Defekt, in der Reihenfolge: **Ursache in einem Satz**, Fix,
Regressionstest. Kein Fix ohne Test — sonst steht hier nur eine Anekdote.

Die Liste erfüllt einen zweiten Zweck: sie zeigt, welche Fehler *keine*
Prüfung gefunden hat. Alle unten stehenden Befunde waren formal einwandfrei —
Felder befüllt, Schema gültig, Zahlen im Rahmen. Geprüft wurde, ob etwas
dasteht, nicht ob es stimmen kann.

---

## 1 Wortdeckung 100 % aus zwei Wörtern

**Ursache:** Die Deckungsquote startete mit dem Vorgabewert `100.0`, und der
Vergleich setzte die Trefferzahl ins Verhältnis zur *Referenz* — bei einem
291-Seiten-Scan mit zwei lesbaren Wörtern im Textlayer waren 2 von 2 Wörtern
gedeckt und der Extrakt galt als vollständig.

**Fix:** Kein Vorgabewert mehr (`coverage: float | None = None`), und eine
Schwelle gegen die Gegenrichtung: ist die Referenz kleiner als 5 % des
Extrakts, ist sie keine tragfähige Grundlage und die Quote entfällt. Nur für
PDFs — bei XLSX mit verbundenen Zellen ist ein dünner Referenztext normal.

**Test:** `test_deckung_braucht_tragfaehige_grundlage`,
`test_document_note_ohne_pruefbare_deckung`.

**Lehre:** Ein Vorgabewert, der wie ein Ergebnis aussieht, ist eine Lüge mit
Verspätung. Fehlende Prüfung heißt `None`, nicht `100.0`.

---

## 2 Der eigene Fix erzeugte einen Fehlalarm

**Ursache:** Die neue Dünn-Schwelle galt zunächst für alle Formate; eine XLSX
mit über 45 verbundenen Spalten hat naturgemäß wenig Referenztext und hätte
ihre verdient erreichten 100 % verloren.

**Fix:** Schwelle auf PDFs beschränkt — das Risiko, gegen das sie schützt
(OCR-Text über fast leerem Textlayer), gibt es nur dort.

**Lehre:** Jeder neue Wächter braucht auch die Gegenprobe auf gesunden Daten.
Ein Wächter, der Gesundes anschlägt, wird abgeschaltet — und dann fehlt er.

---

## 3 Überschriftenerkennung ohne Buchstabenpräfix

**Ursache:** Der Regex verlangte eine führende Ziffer, der BSI-Grundschutz
führt aber `APP.1.1.A1`; damit wurde im Kompendium keine einzige Überschrift
erkannt, die Auflösung fiel auf den Textanker zurück, und jede Anforderung
schleppte den Rest des Dokuments mit — im Median 54.019 Zeichen statt ~380.

**Fix:** Zweiter Regex-Zweig für Buchstabenpräfixe.

**Test:** `test_kennung_faellt_unveraendert_wieder_heraus` (Eigenschaftstest).

---

## 4 „INF“ beginnt mit „I“

**Ursache:** Nach dem Fix aus Nr. 3 stand der römische Zweig `[0-9IVX]+` vor
dem Buchstabenzweig; bei `INF.1.A1` matchte er das bloße `I`, brach ab und
lieferte die Kennung `I` — 49 Anforderungen aus INF, IND und ISMS verloren
ihre Abschnittsgrenze.

**Fix:** Buchstabenzweig vor den römischen gestellt.

**Test:** derselbe Eigenschaftstest. Gegenprobe gemacht: mit der historischen
Reihenfolge schlägt er fehl und meldet `IND.1 nicht erkannt, erkannt wurde: ['i']`.

**Lehre:** Der Median sah nach dem ersten Fix gesund aus (440 Zeichen).
Gefunden hat den Rest erst die *Verteilung*, nicht der Mittelwert. Und
dauerhaft absichern konnte ihn erst ein Test, der die Fälle selbst erzeugt —
`INF` stand in keiner handgeschriebenen Beispielliste.

---

## 5 Zellversatz in der ISO-27001-Anhang-A-Tabelle

**Ursache:** In der Tabelle rutschte der Satz eines Controls in die Folgezeile;
`A.5.16` trug nur noch das Wort „Control“, sein Wortlaut stand am Anfang von
`A.5.17`.

**Fix:** `zellmarke()` erkennt die wiederkehrende Zellanfangsmarke selbst
(hier „Control“); `repariere_zellversatz()` schiebt Text vor der Marke in die
vorige Zeile zurück. Ohne erkennbare Marke wird nichts verschoben — lieber
unrepariert als falsch repariert.

**Test:** `test_zellversatz_repariert`, plus `tests/pruefungen.sh` Schritt 2
und 6.

**Lehre:** Der gefährlichste Befund heißt nicht „fehlt“, sondern „steht an der
falschen Stelle“. Kennung stimmt, Länge stimmt, Schema stimmt — nur der Inhalt
gehört jemand anderem. Deshalb ist der Resolver dreiwertig: `verifiziert`,
`abweichend`, `unverifiziert`.

---

## 6 Kennung nicht in der ersten Spalte

**Ursache:** Die Kennung wurde nur in der ersten Tabellenspalte gesucht, die
VDA-ISA führt davor aber eine Referenzspalte mit `#REF!` — das gesamte
TISAX-Kapitel 8 (Prototypenschutz, 23 Kriterien) fiel auf Füllzeichen zurück.

**Fix:** `zeilen_kennung()` sucht in den ersten vier Zellen.

**Test:** `test_kennung_nicht_nur_in_erster_spalte`.

**Lehre:** Befüllt ist schlimmer als leer. Leer fällt auf.

---

## 7 CIS-Safeguards 3.10, 4.10, 8.10, 13.10, 16.10

**Ursache:** Die Quell-XLSX speichert die Safeguard-Nummer als Fließkommazahl,
`3.10` wird dort zu `3.1` — fünf Safeguards existierten scheinbar doppelt und
fehlten in Wahrheit.

**Fix:** Kreuzreferenz in `mappings/cis-v8.1.json` mit doppelter Beweisführung:
Position zwischen x.9 und x.11 **und** der offizielle CIS-Wortlaut.

---

## 8 NIS2 Art.20.2 trug den Text von Art.20.1

**Ursache:** Beide Absätze stehen im Richtlinientext unter derselben
Überschrift „Governance“; ohne Anker lösten beide auf denselben Abschnitt auf.

**Fix:** Wörtliche Textanker je Absatz in `mappings/nis2.json`.

**Lehre:** Weder Länge noch Kennung verrät diesen Versatz. Nur der Wortlaut.

---

## 9 „C5 nicht prüfbar“ — war er nie

**Ursache:** Die Inhaltsprüfung suchte *eine* Quelldatei, der C5-Export
vermerkt aber `18 Quelldateien`; zusätzlich bekam der YAML-Pfad ein leeres
Meta-Dict, lief also und sah nichts. 796 Anforderungen galten als ungeprüft,
obwohl jede Quelle vorlag.

**Fix:** `extrakte_zu()` löst Mehrquellen-Frameworks auf; echtes Front-Matter
wird durchgereicht. Ergebnis: 766 von 796 geprüft, null Abweichungen.

**Lehre:** „Nicht prüfbar“ ist eine Aussage über das Prüfwerkzeug, nicht über
die Daten. Sie gehört untersucht, nicht berichtet.

---

## 10 Zwei zurückgezogene Behauptungen

**a)** „16 Anforderungen fehlen im Register“ — verglichen wurde gegen erzeugte
Normtext-Notizen statt gegen das Register. Alle 2.236 waren vorhanden.

**b)** „Diese Einträge stammen von dir, sie tragen `grc-claude-generated`“ —
diese Marke tragen *alle* Registereinträge.

**Fix:** Beide Befunde stehen als `KORREKTUR` in
`mappings/vault-ausnahmen.json`, ein Test hält das fest
(`test_tracker_vault_luecken`).

**Lehre:** Ein Befund braucht dieselbe Prüfung wie ein Ergebnis. Ein falscher
Alarm kostet mehr Vertrauen als eine offene Lücke, weil er auch die richtigen
Alarme entwertet.

---

## 11 Tests, die es gab und die nie liefen

**Ursache:** `if __name__ == "__main__": raise SystemExit(main())` stand mitten
in `tests/test_units.py`; alles danach Definierte existierte beim Aufruf noch
nicht. Zusätzlich lief `main()` eine handgepflegte Testliste ab. Fünf
Wächtertests waren geschrieben und liefen im CI-Skriptpfad nie mit.

**Fix:** Der Block steht am Dateiende, `main()` findet die Tests selbst und
benennt ausdrücklich, welche ohne pytest nicht laufen. CI ruft `pytest`.

**Lehre:** Eine Liste, die man vergessen kann, ist keine Prüfung. Und ein
grüner Lauf sagt nichts, solange nicht dabeisteht, *wie viele* Tests er
ausgeführt hat.

---

## 12 Der Resolver fand im ersten Lauf eine Abweichung — in den Testdaten

**Ursache:** Die Titelspalte des Fixtures war 45 mm breit; reportlab brach
`Informationssicherheitsrichtlinien` ohne Trennstrich um, der Textlayer der
Quelle enthielt danach `...richtlinie n`. Der Extrakt gab das getreu wieder —
die Abweichung saß in der Vorlage, nicht in der Pipeline.

**Fix:** Spalte auf 54 mm verbreitert; ein Test hält fest, dass kein Wort im
Primärtext länger als 40 Zeichen in einer Tabellenzelle steht.

**Lehre:** Genau dafür ist der erste Ground-Truth-Lauf da. Dass er etwas
findet, ist kein Rückschlag, sondern der Zweck.

---

## 13 Drei Lambdas, eines davon kaputt

**Ursache:** `esc = lambda v: ...` stand dreimal im Modul; eine Fassung
schrieb `.replace('"', '\"')` — in Python ersetzt das ein Anführungszeichen
durch sich selbst. Ein Dateiname mit `"` hätte dort das Front-Matter zerbrochen.

**Fix:** Eine Funktion `publish.yaml_wert()`, an allen drei Stellen benutzt.

**Lehre:** Dreimal dieselbe Zeile heißt: zwei Gelegenheiten, sie
unterschiedlich falsch zu schreiben. Gefunden hat das der Linter, nachdem er
überhaupt eingeschaltet wurde.

---

## Muster über alle Fälle

1. **Sechs von sieben Fehlern waren Abgleichsfehler gegen eine externe
   Wahrheit, keiner war ein Logikfehler.** Konsistenzprüfungen konnten sie
   deshalb nicht finden — sie messen die Maschine gegen sich selbst.
2. **Der Median verbirgt die Ausreißer.** Nr. 4 sah nach dem ersten Fix
   gesund aus. Verteilungen prüfen, nicht Mittelwerte.
3. **Befüllt ist gefährlicher als leer.** Nr. 5, 6 und 8 sahen alle vollständig
   aus.
4. **Ein Fix ist erst fertig, wenn die Gegenprobe steht.** Nr. 2 und 11 zeigen,
   wie leicht ein Wächter blind wird, ohne dass es jemand merkt.
