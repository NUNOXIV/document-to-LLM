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

## 14 Verlorene Bindestriche: 1058 Wörter, unsichtbar für jede Prüfung

**Ursache:** Docling löst die Trennung am Zeilenende auf, indem es den
Trennstrich entfernt — richtig bei „Informations-/sicherheit", falsch bei
„IKT-/Systemen": daraus wurde „IKTSystemen", ein Wort, das in keiner Quelle
steht und das keine Suche findet.

**Warum es niemand sah:** `verify.tokenize()` entfernt denselben Trennstrich
auch auf der Quellseite. Beide Seiten hießen „iktsystemen", die Wortdeckung
blieb 100,0 %. Die Prüfung war nicht nachlässig — sie war blind an genau der
Stelle, an der der Fehler entstand.

**Gefunden durch:** den Abgleich gegen das amtliche XML von
gesetze-im-internet.de. Der erste Lauf des Fundstellen-Resolvers gegen den
BSIG-Extrakt meldete 55 von 68 Paragrafen als abweichend.

**Ausmaß:** 187 von 269 PDF-Extrakten, 1058 verschiedene Wörter.

**Fix:** `verify.verlorene_bindestriche()` mit doppeltem Beleg, inline in
`extract.py` und als Bestandslauf `bindestriche.py`.

**Test:** `test_bindestrich_nur_mit_doppeltem_beleg`.

**Lehre:** Zwei Prüfungen, die denselben Vorverarbeitungsschritt teilen, sind
eine Prüfung. Die Zwei-Quellen-Regel meint auch: zwei *Lesewege*.

---

## 15 Der Fix kehrte die Silbentrennung um

**Ursache:** Die erste Fassung verlangte nur einen Beleg — die Form mit
Bindestrich muss in der Quelle stehen. Bei zwischenraumfreiem Vergleich steht
sie das immer, auch bei echter Silbentrennung: aus dem richtigen „Abnahme"
hätte der Fix wieder „Ab-nahme" gemacht. 93 Fehlalarme in einer Datei, 3831
statt 1058 Treffer im Bestand.

**Fix:** Zweiter Beleg — die Form mit Bindestrich muss ZUSAMMENHÄNGEND in der
Quelle stehen, ohne Umbruch dazwischen. Ein Bindestrich, der zum Wort gehört,
steht irgendwo auch mitten in der Zeile; ein Trennstrich nur am Zeilenende.

**Test:** derselbe, mit „Ab-\nnahme" als Gegenprobe.

**Lehre:** Aufgefallen ist es nur, weil der Probelauf jeden Treffer im
Klartext ausgab und „Abnahme -> Ab-nahme" dort stand. Ein Werkzeug, das seine
Änderungen erst zeigt und dann macht, ist kein Komfort, sondern die Prüfung.

---

## 16 Dieselbe Regel, zwei Bedeutungen: U+FFFE

**Ursache:** Im BSIG-Druck bildet die Schrift den geschützten Bindestrich
U+2011 nicht ab; im Textlayer steht das Nichtzeichen U+FFFE. Ich habe geprüft,
ob es dort ein Bindestrich ist: 24 von 24 Stellen bestätigt das amtliche XML.
Daraus wurde eine Regel — und die hielt genau ein Dokument weit. In einer
anderen Datei desselben Bestandes stehen 1639 solche Zeichen, und dort sind es
Trennstriche am Zeilenende.

**Fix:** Das Zeichen taugt nicht als Beleg. Es wird gezählt und gemeldet
(`unlesbar_im_wort`), nicht gedeutet.

**Test:** `test_unlesbares_zeichen_ist_kein_bindestrichbeleg`.

**Lehre:** 24 von 24 in einem Dokument sind keine Grundgesamtheit. Eine Regel
gilt erst, wenn sie an einem zweiten Fall geprüft wurde, der sie widerlegen
könnte.

---

## 17 Ein vertauschter Variablenname, 187 zerstörte Extrakte

**Ursache:** In `bindestriche.py` hieß der Markdown-Text `roh`. Beim Umbau
habe ich `roh = verify.quelltext(quelle)` ergänzt und damit dieselbe Variable
mit dem PDF-Text überschrieben. Die nächste Zeile schnitt das Front-Matter aus
dem PDF-Text statt aus dem Markdown: 187 Extrakte bekamen einen Kopf aus
Seitentext und verloren ihre Provenienz.

**Fix:** Variable umbenannt; zusätzlich schreibt die Funktion nichts mehr,
wenn das Ergebnis nicht mit `---` beginnt. Die Rümpfe wurden gesichert und die
187 Dokumente aus der Quelle neu extrahiert — rekonstruiert wurde nichts, weil
geratene Provenienz schlimmer ist als keine.

**Test:** `test_front_matter_ueberlebt_die_reparatur`.

**Lehre:** Ein Schreibvorgang über einen ganzen Bestand braucht eine Zusage,
die er vor dem Schreiben prüft. „Das Ergebnis beginnt mit `---`" wäre hier eine
Zeile gewesen. Und: der Probelauf sah gut aus, weil er nur zählt — die Zeile,
die den Schaden anrichtet, lief in keinem Test.

---

## 18 134 von 602 Dokumenten waren nie eingelesen

**Ursache:** Jede Prüfung im System sieht sich an, was **da** ist — Deckung,
Zellversatz, Kennungen, Fundstellen, Bindestriche. Keine einzige fragte, was
**fehlt**. Ein Dokument, das nie eingespeist wurde, hat keinen Extrakt, der
auffallen könnte, und keinen Registereintrag, der widerspräche; es fällt durch
jedes Netz.

**Ausmaß:** 4 PDFs lagen unkonvertiert in `input/`, 130 weitere steckten in
zwei ZIP-Archiven, die niemand ausgepackt hat. Bestand 468 statt 602.

**Gefunden durch:** eine Übersicht außerhalb dieses Systems (Notion). Nicht
durch das Werkzeug — das hätte den Fehler nie gefunden, weil es die falsche
Richtung prüft.

**Fix:** `vollstaendigkeit.py` läuft über `input/`, schaut in Archive hinein
und verlangt für jede Datei einen Registereintrag. `--strict` bricht ab.

**Test:** `test_vollstaendigkeit_findet_die_nie_eingelesene_quelle`, beide
Richtungen, inklusive Archiv.

**Lehre:** Eine Prüfung, die vom Ergebnis ausgeht, kann Vollständigkeit nicht
messen. Sie muss von der Quelle ausgehen. Das ist dieselbe Blindheit wie bei
den Bindestrichen, nur eine Ebene höher: dort teilten sich zwei Prüfungen
einen Schritt, hier teilen sich **alle** Prüfungen dieselbe Ausgangsmenge.

---

## 19 Ein Warntext, der etwas anderes sagte als der Code tut

**Ursache:** Als ich die U+FFFE-Deutung aus dem Code entfernte (Nr. 16), blieb
der Warntext stehen: „Sie wurden als Bindestrich gelesen." Der Code liest sie
seitdem gar nicht mehr — die Warnung behauptete eine Verarbeitung, die es nicht
gibt.

**Fix:** Text auf das berichtigt, was tatsächlich passiert: an der Stelle fehlt
ein Zeichen, welches, wird nicht geraten.

**Lehre:** Wer eine Regel zurückzieht, muss auch den Satz zurückziehen, der sie
erklärt. Eine falsche Warnung ist schlimmer als keine — sie wird geglaubt.

---

## 20 Zwei Quellen, ein Zielname: 125 Extrakte überschrieben oder nie geschrieben

**Ursache:** `Checkliste-APP-1-1.xlsx` und `checklisten-2023/Checkliste_APP.1.1.xlsx`
ergeben denselben Slug. Der Kollisionsschutz kannte nur den eigenen Prozess
(`claimed`) und nur den Fall „gleicher Stem, anderes Format". Über die
Prozessgrenzen der Häppchen-Extraktion hinweg überschrieb die zweite Quelle
die erste, oder ihr Extrakt fehlte ganz. Die Vollständigkeitsprüfung
(Nr. 18) fand die Lücke — genau dafür war sie gebaut —, aber erst nach dem
Lauf. 110 der 111 XLSX und alle 19 DOCX aus den ZIPs waren dabei
byte-identische Kopien der Originale daneben; nur eine Datei und der vierte
Scan waren echte Lücken.

**Fix:** `target_name` liest jetzt auch die Kopfzeile des Ziels auf Platte.
Eigen ist ein Ziel, wenn Quellname oder Hash dort stehen — so bleibt die
Idempotenz erhalten und ein Duplikat bekommt kein zweites Extrakt. Fremde
Ziele werden nie überschrieben: Ausweichname aus Ordnername, zuletzt
Hash-Präfix. `vollstaendigkeit.py` erkennt Duplikate am Hash und meldet sie
getrennt statt als Lücke. Regressionstest in beide Richtungen.

**Lehre:** Ein Name ist kein Schlüssel. Wer nach Dateinamen adressiert, muss
den Inhalt dazuhalten — und jeder Schutz, der nur im Prozessspeicher lebt,
endet mit dem Prozess.

---

## 21 Zwei ISO-Exporte, 32 Anforderungen mit dem Text einer anderen Nummer

**Ursache:** ISO 27001 und ISO 42001 führen Klausel 5.1 (Leadership) *und*
Control A.5.1 (Policies). Die Tabellenzeile A.5.1 wurde beim Lesen auch
unter „5.1" abgelegt, und Tabellenzeilen überschrieben Überschriften. Dazu
verdrängte die Inhaltsverzeichnis-Tabelle („| 10.1 | Continual improvement
| 23 |") das Kapitel 10.1 durch eine Zeile ohne Text, und „A.10" fiel über
die Variante „10" auf das Kapitel Improvement zurück. 18 von 74 Anforderungen
in ISO 42001 und 14 von 118 in ISO 27001 trugen so den Wortlaut einer anderen
Nummer — genau der Fehler, den ein Compliance-Bestand nicht haben darf.
Die Inhaltsprüfung (`inhalt.py`) sah nur eine Titelabweichung, weil sie
dieselbe Zusammenführung benutzte wie der Schreiber: derselbe Vorverarbeitungsschritt
auf beiden Seiten, also eine Prüfung, nicht zwei (Nr. 14, Muster 5).
Gefunden hat es ein Zweitleser, der nur Überschriften kennt.

**Fix:** Kennungen bleiben, wie sie in der Zelle stehen; Überschriften mit
Text haben Vorrang, Tabellen und Katalog füllen nur, was fehlt; führt das
Dokument einen Anhang A, fällt „A.10" nie auf „10" zurück. Regressionstest
mit Klausel und gleichnamigem Control im selben Dokument.

**Lehre:** Eine Nummer ist erst dann eindeutig, wenn ihr Präfix mitläuft.
Und wer den Schreiber prüfen will, darf nicht mit den Augen des Schreibers lesen.

---

## 22 Ein check(), das unter pytest nie fehlschlug

**Ursache:** `check()` sammelt Fehlschläge in einer Liste; der eigene Runner
wertet sie am Ende aus. pytest tat das nicht. Jeder check()-basierte Test war
unter pytest grün, egal was er fand — und pytest war laut CLAUDE.md die
Definition of Done. Aufgefallen ist es, weil ein neuer Test *vor* dem Fix
grün war, obwohl der Fehler nachweislich drin war.

**Fix:** `tests/conftest.py` leert die Liste vor jedem Test und lässt den Test
scheitern, wenn danach etwas darin steht. Alle 42 Tests bleiben grün — das
ist jetzt eine Aussage.

**Lehre:** Ein Test, der rot sein kann, ist ein Test. Vor jedem Fix gehört der
Nachweis, dass der Test ohne Fix rot ist — nicht als Ritual, sondern weil
genau dieser Nachweis hier gefehlt hat.

---

## 23 Zwölf Zeilen mit dem Text einer anderen Nummer, und volle Wortdeckung

**Ursache:** Das Aufnahmetor des Auftraggebers wies vier Frameworks ab: DSGVO
Art.21 enthielt Art.22 und Art.23, Art.6 den Art.7, DORA Art.30 den Art.31,
KI-VO Art.49 den Art.50. Vier Mechanismen, alle im Amtsblattsatz: „Artikel
22" steht mal als Überschrift, mal als nackte Zeile, und die nackte Zeile
beendete keinen Abschnitt; „Artikel 45 der Verordnung … wird wie folgt
geändert" galt als Anker für Art.45; „## A.1 General" war keine Überschrift,
also lief ISO 42001 Klausel 10.2 bis in den Anhang; „Art.20.1" fiel über die
Variante „Artikel 20" auf den ganzen Artikel zurück, und der Kreuzreferenz-
Anker endete nicht am nackten Absatz „(2)". Kein Wächter sah es: doppelter
Text hat volle Wortdeckung, und `inhalt.py` las mit den Augen des Schreibers.

**Fix:** Nackte Artikelzeilen und Strukturüberschriften sind Grenzen,
Anker akzeptieren keinen Kleinbuchstaben nach der ID, Anhangskennungen mit
einem Buchstaben sind Überschriften, Absatz-IDs fallen nie auf den Artikel
zurück. Neu in `inhalt.py`: die Gegenfrage „enthält diese Zeile den vollen
Text einer anderen?" — sie fand 27 Fälle, darunter 15, die das Tor nicht
kannte. Nach drei Läufen 0.

**Lehre:** Die Frage „ist alles da?" beantwortet die Wortdeckung. Die Frage
„ist auch nichts zu viel da?" beantwortet nur ein Vergleich der Zeilen
untereinander. Beide gehören in die Definition of Done.

---

## Muster über alle Fälle

1. **Sechs von sieben Fehlern waren Abgleichsfehler gegen eine externe
   Wahrheit, keiner war ein Logikfehler.** Konsistenzprüfungen konnten sie
   deshalb nicht finden — sie messen die Maschine gegen sich selbst.
2. **Der Median verbirgt die Ausreißer.** Nr. 4 sah nach dem ersten Fix
   gesund aus. Verteilungen prüfen, nicht Mittelwerte.
3. **Befüllt ist gefährlicher als leer.** Nr. 5, 6 und 8 sahen alle vollständig
   aus.
4. **Ein Fix ist erst fertig, wenn die Gegenprobe steht.** Nr. 2, 11 und 15
   zeigen, wie leicht ein Wächter blind wird, ohne dass es jemand merkt.
5. **Zwei Prüfungen mit derselben Vorverarbeitung sind eine Prüfung.** Nr. 14
   blieb unsichtbar, weil Extrakt und Quelle denselben Schritt durchliefen.
   Die Zwei-Quellen-Regel meint auch zwei Lesewege.
6. **Wer über einen ganzen Bestand schreibt, braucht eine Zusage vorab.**
   Nr. 17: eine Zeile Prüfung vor dem Schreiben hätte 187 Dateien gerettet.
7. **Prüfungen, die vom Ergebnis ausgehen, messen keine Vollständigkeit.**
   Nr. 18: 134 fehlende Dokumente, und kein Wächter konnte sie sehen, weil
   alle dieselbe Ausgangsmenge teilten — den Bestand statt der Quelle.
8. **Namen sind Hinweise, Hashes sind Belege.** Nr. 20: derselbe Slug für zwei
   Dateien, und der Schutz davor lebte nur im Prozessspeicher.
9. **Ein Wächter, der nicht rot werden kann, ist keiner.** Nr. 22: check()
   unter pytest. Die Gegenprobe (Nr. 4) gilt auch für die Testinfrastruktur.
10. **Vollständig heißt auch: nichts zu viel.** Nr. 23: zwölf Zeilen mit fremdem
    Text bei 100 % Wortdeckung. Die Gegenfrage gehört neben die Deckung.
