---
source_file: "IT_Grundschutz_Profils_Rettungsleitstellen.pdf"
source_sha256: e704876348636f14e159c6c53a8dd8b6a164d92d37136ac672c3ea898782b4ec
source_bytes: 1410211
pages: 157
tables: 233
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T20:22:44+00:00"
text_coverage_percent: 99.998
appended_source_lines: 79
restored_hyphens: 6
extraction_status: warn
warnings:
  - "3 Tabellenzelle(n) beginnen mitten im Satz — moegliche Zellverschiebung, z. B. \"negative Innen- oder Außenwirkung...\". Zeilen dieser Tabelle vor dem Zitat gegen die Quelle pruefen."
  - "6 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): BSIStandard -> BSI-Standard, GrundschutzProfils -> Grundschutz-Profils, ITGrundschutzes -> IT-Grundschutzes, ITSysteme -> IT-Systeme, KernAbsicherung -> Kern-Absicherung"
  - "Der Textlayer der Quelle enthaelt 614 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
  - "79 Quellzeile(n) wurden vom Layout-/Tabellenmodell keinem Element zugeordnet und stehen woertlich im Abschnitt 'Nachtrag: nicht zugeordneter Quelltext' — dort ohne Tabellenstruktur."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

## FernUniversität in Hagen

## Fakultät für Mathematik und Informatik

## Lehrgebiet Parallelität und VLSI

## Masterarbeit zur Erlangung des Grades eines Master of Science über das Thema

## Erstellung eines IT-Grundschutz-Profils für Rettungsleitstellen

Name: Matrikelnummer: E-Mail: Studiengang: Abgabedatum: 1. Prüfer: 2. Prüfer Betreuung: Henning Schmidtpott XXXXXXXX henning.schmidtpott@studium.fernuni-hagen.de M. Sc. Wirtschaftsinformatik 02.01.2020 Prof. Dr. Jörg Keller Prof. Dr. Tobias Eggendorfer Daniel Gilles, Birger Klein (BSI)

<!-- page: 2 -->

## Inhaltsverzeichnis

Abbildungsverzeichnis.......................................................................................................................IV

Tabellenverzeichnis.............................................................................................................................V

Abkürzungsverzeichnis......................................................................................................................VI

1 Einleitung..........................................................................................................................................1

1.1 Motivation..................................................................................................................................1

1.2 Aufgabenstellung und Abgrenzung............................................................................................2

1.3 Aufbau und Struktur der Arbeit.................................................................................................3

2 Grundlagen und Begriffe...................................................................................................................5

2.1 Nichtpolizeiliche Gefahrenabwehr............................................................................................5

2.2 Feuerwehr, Rettungsdienst und Katastrophenschutz.................................................................5

2.2.1 Einsatzmittel.......................................................................................................................

2.2.2 Hilfsfrist und Schutzziel.....................................................................................................

6

2.3 Rettungsleitstellen......................................................................................................................8

7

2.3.1 Organisation und Betrieb...................................................................................................

2.3.2 Rettungsleitstellen als kritische Infrastrukturen...............................................................

9

2.4 Informationssicherheit.............................................................................................................11

10

2.5 IT-Grundschutz........................................................................................................................12

2.5.1 Sicherheitsmanagementsystem........................................................................................

2.5.2 BSI-Standards..................................................................................................................

12

2.5.3 IT-Grundschutz-Kompendium.........................................................................................

13

3 Erstellung des IT-Grundschutz-Profils............................................................................................15

13

3.1 Formale Aspekte und Management Summary.........................................................................15

3.2 Festlegung des Geltungsbereichs.............................................................................................16

3.2.1 Zielgruppe........................................................................................................................

3.2.2 Schutzbedarf und IT-Grundschutz Vorgehensweise.........................................................

3.2.2.1 Ermittlung der Rahmenbedingungen........................................................................

3.2.2.2 Formulierung allgemeiner Sicherheitsziele..............................................................

3.2.2.3 Bestimmung des zur erreichenden Sicherheitsniveaus............................................

3.2.2.4 Festlegung der IT-Grundschutz Vorgehensweise.....................................................

17

16

17

19

3.2.3 Kompatibilität zu anderen Standards und die rechtlichen Rahmenbedingungen.............

19

20

3.3 Abgrenzung des Informationsverbundes.................................................................................20

20

3.3.1 Bestandteile des Informationsverbundes..........................................................................

3.3.2 Nicht berücksichtigte Teile...............................................................................................

21

3.4 Strukturanalyse........................................................................................................................22

21

3.4.1 Prozesse............................................................................................................................

3.4.1.1 Meldungseingang.....................................................................................................

3.4.1.2 Einsatzaufnahme......................................................................................................

3.4.1.3 Einsatzbearbeitung...................................................................................................

3.4.1.4 Einsatzabschluss.......................................................................................................

3.4.1.5 Weitere Prozesse.......................................................................................................

3.4.2 Anwendungen...................................................................................................................

3.4.2.1 Einsatzleitsystem einer Rettungsleitstelle................................................................

3.4.2.2 Kommunikationssystem einer Rettungsleitstelle.....................................................

3.4.2.3 Weitere Anwendungen in einer Rettungsleitstelle....................................................

3.4.2.4 Zusammenfassung der Anwendungen......................................................................

3.4.3 IT-Systeme.......................................................................................................................

3.4.4 Netzwerke........................................................................................................................

23

22

24

25

24

25

26

26

28

30

28

30

31

<!-- page: 3 -->

3.4.4.1 Netze und Netzkomponenten...................................................................................

3.4.4.2 Alarmierungsnetz......................................................................................................

3.4.4.3 Netzübersicht und Netzplan.....................................................................................

3.4.5 Gebäude und Räume........................................................................................................

31

33

3.4.6 Übersicht Objekte Informationsverbund..........................................................................

32

34

3.5 Schutzbedarfsfeststellung........................................................................................................36

35

3.5.1 Schutzbedarfsfeststellung für Prozesse............................................................................

3.5.1.1 Schutzbedarfsfeststellung der Vertraulichkeit für Prozesse.....................................

3.5.1.2 Schutzbedarfsfeststellung der Integrität für Prozesse..............................................

3.5.1.3 Schutzbedarfsfeststellung der Verfügbarkeit für Prozesse.......................................

3.5.2 Schutzbedarfsfeststellung für Anwendungen...................................................................

3.5.2.1 Schutzbedarfsfeststellung der Vertraulichkeit für Anwendungen............................

3.5.2.2 Schutzbedarfsfeststellung der Integrität für Anwendungen.....................................

3.5.2.3 Schutzbedarfsfeststellung der Verfügbarkeit für Anwendungen..............................

3.5.3 Schutzbedarfsfeststellung für IT-Systeme........................................................................

3.5.3.1 Schutzbedarfsfeststellung der Vertraulichkeit für IT-Systeme.................................

3.5.3.2 Schutzbedarfsfeststellung der Integrität für IT-Systeme..........................................

3.5.3.3 Schutzbedarfsfeststellung der Verfügbarkeit für IT-Systeme...................................

3.5.4 Schutzbedarfsfeststellung für Netzwerke.........................................................................

3.5.4.1 Schutzbedarfsfeststellung der Vertraulichkeit für Netzwerke..................................

3.5.4.2 Schutzbedarfsfeststellung der Integrität für Netzwerke...........................................

3.5.4.3 Schutzbedarfsfeststellung der Verfügbarkeit für Netzwerke....................................

3.5.5 Schutzbedarfsfeststellung für Räume...............................................................................

3.5.5.1 Schutzbedarfsfeststellung der Vertraulichkeit für Räume........................................

3.5.5.2 Schutzbedarfsfeststellung der Integrität für Räume.................................................

37

39

37

39

41

41

42

43

42

43

44

44

45

45

45

46

46

3.5.5.3 Schutzbedarfsfeststellung der Verfügbarkeit für Räume..........................................

46

47

3.6 Zu erfüllende Anforderungen und umzusetzende Maßnahmen...............................................49

48

3.6.1 Auswahl relevanter Bausteine..........................................................................................

3.6.2 Anforderungen der Bausteine...........................................................................................

49

3.7 Behandlung nicht hinreichend abgedeckter Zielobjekte..........................................................50

50

3.8 Restrisiko.................................................................................................................................50

3.9 Notfallmanagement (BCM).....................................................................................................51

4 Risikoanalyse...................................................................................................................................53

4.1 Ermittlung elementarer Gefährdungen....................................................................................53

4.2 Ermittlung weiterer relevanter Gefährdungen.........................................................................57

4.3 Risikoeinschätzung..................................................................................................................57

4.4 Risikobewertung......................................................................................................................58

4.5 Risikobehandlung....................................................................................................................64

4.6 Risikobeobachtung...................................................................................................................66

5 Theoretische Evaluation..................................................................................................................67

5.1 Ergebnisse aus BSI Workshop mit Leitstellen.........................................................................67

5.2 Übertragbarkeit des Profils auf andere Länder........................................................................68

6 Fazit und Ausblick...........................................................................................................................69

Literaturverzeichnis............................................................................................................................71

Anhang...............................................................................................................................................76

<!-- page: 4 -->

## Abbildungsverzeichnis

Abbildung 1: Zeitstrahl von Eintreten des Notfallereignisses bis zum Eintreffen der Einsatzmittel an der Einsatzstelle........................................................................................................8 Abbildung 2: Rettungskette bei Unfallgeschehen mit Personenschaden.............................................9 Abbildung 3: Verhalten im Brandfall (aus Brandschutzverordnung, DIN 14096)..............................9 Abbildung 4: Kernprozesse in einer Rettungsleitstelle.....................................................................23 Abbildung 5: Aufbau eines POCSAG Alarmierungsnetzes mit einem Master-DAU (links) und mehreren Master-DAUs (rechts)..................................................................................32 Abbildung 6: Netzplan des Informationsverbundes..........................................................................33 Abbildung 7: Matrix zur Einstufung von Risiken.............................................................................58

<!-- page: 5 -->

## Tabellenverzeichnis

Tabelle 1: Die vom BBK definierten KRITIS-Sektoren....................................................................10

Tabelle 2: Aktuelle BSI-Standards (Stand September 2019)..............................................................13

Tabelle 3: Allgemeine Einflussfaktoren in einer Rettungsleitstelle auf die Erfüllung der Haupt-

aufgaben............................................................................................................................18

Tabelle 4: Sicherheitsziele in einer Rettungsleitstelle........................................................................19

Tabelle 5: Bestandteile des Informationsverbundes, die Prozesse und Verfahren in

Rettungsleitstellen unterstützen........................................................................................21

Tabelle 6: Prozesse bei Meldungseingang..........................................................................................23

Tabelle 7: Prozesse der Einsatzaufnahme...........................................................................................24

Tabelle 8: Prozesse der Einsatzbearbeitung........................................................................................24

Tabelle 9: Prozesse des Einsatzabschlusses........................................................................................25

Tabelle 10: Weitere Prozesse des Informationsverbundes..................................................................26

Tabelle 11: Anwendungen des Informationsverbundes, die in einer Rettungsleitstelle verwendet

werden..............................................................................................................................30

Tabelle 12: IT-Systeme des Informationsverbundes, die in einer Rettungsleitstelle verwendet wer-

den....................................................................................................................................30

Tabelle 13: Netzkomponenten und Netze des Informationsverbundes..............................................33

Tabelle 14: Räume des Informationsverbundes..................................................................................34

Tabelle 15: Im IT-Grundschutz-Profil für Rettungsleitstellen berücksichtigte Objekte des Informati-

onsverbundes....................................................................................................................36

Tabelle 16: Potentielle Schadensszenarien.........................................................................................36

Tabelle 17: Vom BSI empfohlene Schutzbedarfskategorien, übertragen auf Leitstellen...................37

Tabelle 18: Schutzbedarf der Vertraulichkeit für Prozesse.................................................................38

Tabelle 19: Schutzbedarf der Integrität für Prozesse..........................................................................39

Tabelle 20: Schutzbedarf der Verfügbarkeit für Prozesse...................................................................40

Tabelle 21: Schutzbedarf der Vertraulichkeit für Anwendungen........................................................41

Tabelle 22: Schutzbedarf der Integrität für Anwendungen.................................................................42

Tabelle 23: Schutzbedarf der Verfügbarkeit für Anwendungen.........................................................43

Tabelle 24: Schutzbedarf der Vertraulichkeit für IT-Systeme............................................................43

Tabelle 25: Schutzbedarf der Integrität für IT-Systeme.....................................................................44

Tabelle 26: Schutzbedarf der Verfügbarkeit für IT-Systeme..............................................................44

Tabelle 27: Schutzbedarf der Vertraulichkeit für Netzwerke.............................................................45

Tabelle 28: Schutzbedarf der Integrität für Netzwerke......................................................................46

Tabelle 29: Schutzbedarf der Verfügbarkeit für Netzwerke...............................................................46

Tabelle 30: Schutzbedarf der Vertraulichkeit für Räume...................................................................47

Tabelle 31: Schutzbedarf der Integrität für Räume............................................................................47

Tabelle 32: Schutzbedarf der Verfügbarkeit für Räume.....................................................................48

Tabelle 33: Phasen des Notfallmanagement-Prozesses des BSI, bezogen auf Rettungsleitstellen....51

Tabelle 34: Objekte, für die beispielhaft eine Risikoanalyse durchgeführt wird...............................53

Tabelle 35: Ermittlung der Relevanz der Gefährdungen für die Beispiel-Objekte N4 und N7..........57

Tabelle 36: Kategorien der Eintrittshäufigkeiten nach BSI-Standard 200-3......................................57

Tabelle 37: Kategorien der Schadensauswirkungen nach BSI-Standard 200-3.................................58

Tabelle 38: Kategorien der Risiken....................................................................................................59

Tabelle 39: Risikobewertung für das Netz zum Internet Service Provider (N4)................................61

Tabelle 40: Risikobewertung für das Alarmierungsnetz für Funkmeldeempfänger (N7)..................63

Tabelle 41: Behandlung der Risiken des Netzes zum ISP..................................................................65

Tabelle 42: Behandlung der Risiken des Alarmierungsnetzes............................................................66

<!-- page: 6 -->

## Abkürzungsverzeichnis

ACS Allianz für Cybersecurity AAO Alarm- und Ausrückeordnung BBK Bundesamt für Bevölkerungsschutz und Katastrophenhilfe BCM Business Continuity Management BMA Brandmeldeanlage BOS Behörden und Organisationen mit Sicherheitsaufgaben BSI Bundesamt für Sicherheit in der Informationstechnik DAU Digitaler Alarmumsetzer DIN Deutsches Institut für Normung DME Digitaler Funkmeldeempfänger EENA European Emergency Number Association ELS Einsatzleitsystem ELW Einsatzleitwagen GIS Geoinformationssystem HvO Helfer vor Ort ISP Internet Service Provider KMS Kommunikationssystem KRITIS Kritische Infrastrukturen POCSAG Post Office Code Standard Advisory Group QMS Qualitätsmanagementsystem RMS Risikomanagementsystem RTH Rettungstransporthelikopter RTW Rettungswagen SQR-BW Stelle zur trägerübergreifenden Qualitätssicherung im Rettungsdienst Baden-Württemberg VoIP Voice over IP

<!-- page: 7 -->

## 1 Einleitung

Rettungsleitstellen nehmen Notfallmeldungen für Feuerwehr sowie Rettungsdienst entgegen und entsenden die notwendige Hilfe an den Einsatzort. Hierfür müssen sie rund um die Uhr erreichbar und betriebsbereit sein. Die Systeme der Leitstellen verarbeiten unter anderem vertrauliche Daten, die oft auch medizinische Diagnosen von Patienten enthalten. Damit diese nicht in die Hände Dritter gelangen, ist eine sehr hohe Absicherung erforderlich. Ebenso muss das korrekte Verhalten aller Anwendungen  ständig   gewährleistet   sein.  Grundvoraussetzung  für   die   dafür   zu   erreichenden Schutzziele Verfügbarkeit, Vertraulichkeit und Integrität sind entsprechend abgesicherte Softwareanwendungen, Netzwerke und weitere IT-Komponenten. Durch neue Technologien erhalten Informationen aus dem Internet, neben den klassischen telefonischen Notrufen über die Notrufnummer 112, auch in einer Rettungsleitstelle einen immer höheren Stellenwert und müssen in den Einsatzleit- und Kommunikationssystemen verarbeitet werden. Ein Beispiel ist die geplante Einführung der bundesweiten Notruf-App, die es auch hörgeschädigten oder anderweitig eingeschränkten Personen ermöglichen soll, einen Notruf abzusetzen [BMWi17]. Eine Anbindung an das Internet wird hierdurch für alle Rettungsleitstellen in Deutschland unumgänglich. Ebenso spielt der Datenaustausch mit anderen Leitstellen oder Institutionen, wie Krankenhäusern, eine immer größere Rolle. Eine komplette physische Abschottung der Netzwerke in der Leitstelle ist nicht mehr möglich. Aufgrund der bundesweiten Abschaltung der ISDN-Technik seitens der Telefonnetzbetreiber, wird die Notrufnummer 112 zukünftig zudem über einen IP-basierten Telefonanschluss bereitgestellt [TsSc13]. Hierdurch ergeben sich weitere neue Risiken [DHS18]. Wie jede  andere   Organisation   betreffen   Gefahren   durch   Cyberattacken   daher   auch   Rettungsleitstellen. Eine Nicht-Erreichbarkeit, mangelnde Betriebsbereitschaft oder fehlerhaft verarbeitete Daten können Gesundheitsschäden von Menschen zur Folge haben. Ebenso muss die Vertraulichkeit der Daten gewahrt bleiben. Gleichzeitig stellen Rettungsleitstellen als Teil der kritischen Infrastruktur eines Staats, ein potentielles Ziel von Angreifern mit kriminellen oder sogar terroristischen Absichten dar. Das Risiko, Opfer einer Cyberattacke zu werden, steigt durch diese Umstände an. In Deutschland gibt es derzeit rund 250 Rettungsleitstellen [FVLS19]. Das individuelle Level der

Informationssicherheit kann sehr unterschiedlich sein. Durch die Erstellung und Herausgabe eines IT-Grundschutz-Profils können die Leitstellen ihr Sicherheitsniveau überprüfen und entsprechende Maßnahmen einleiten, um ihre Systeme abzusichern.

## 1.1 Motivation

Rettungsleitstellen sind auf die Verwendung aktueller Technik angewiesen [KKMS15]. Die Informationssicherheit ist für Rettungsleitstellen somit von zunehmender Bedeutung. Informationen zu Methoden, die Sicherheit in den im professionellen Umfeld eingesetzten Informationssystemen zu verbessern, sind grundsätzlich in großer Zahl vorhanden. Diejenigen Mittel herauszufiltern, die für den speziellen Bereich der Rettungsleitstellen notwendigerweise umzusetzen sind, kann dagegen viele Leitstellen vor eine schwierige Aufgabe stellen. Das Bundesamt für Sicherheit in der Informationstechnik (BSI) stellt mit dem IT-GrundschutzKompendium ein Nachschlagewerk bereit, das Institutionen dabei helfen soll, ihr Sicherheitsniveau zu überprüfen und bei Bedarf zu erhöhen [BSI19]. Es besteht aus einer Vielzahl an Bausteinen, die den Anwendern Empfehlungen für typische Anwendungsfälle geben sollen und ihnen somit das Treffen geeigneter Maßnahmen zur Erhöhung der Informationssicherheit erleichtert. In dieser Arbeit wird untersucht, welche Risiken in der speziellen Umgebung von Rettungsleitstellen eine Rolle spielen und welche Bausteine des BSI dort praktisch umgesetzt werden sollten. Ebenso stellt sich die Frage, ob zusätzliche Bausteine erstellt werden müssen, für die im IT-Grundschutz-Kompendium des BSI bislang kein Bedarf zu erkennen war. IT-Grundschutz-Profile des BSI sollen Institutionen darin unterstützen, die für ihre jeweilige Branche passenden Bausteine auszuwählen und die richtigen Maßnahmen zu ergreifen [BSI19a]. Die Erstellung eines IT-Grundschutz-Profils für Rettungsleitstellen gibt den Leitstellen somit eine Hilfe an die Hand, notwendige Sicherheitsmaßnahmen, unter Berücksichtigung der speziellen Anforderungen, ressourcenschonend zu ermitteln und umzusetzen.

<!-- page: 8 -->

## 1.2 Aufgabenstellung und Abgrenzung

Ziel dieser Arbeit ist die Erstellung eines IT-Grundschutz-Profils für Rettungsleitstellen, mit dem diese den IT-Grundschutz praktisch umsetzen können. Außerdem wird eine abstrakte Risikoanalyse durchgeführt, um die speziellen Risiken für Leitstellen zu identifizieren und zu bewerten. Parallel zur Erstellung dieser Arbeit veranstaltet das BSI einen Workshop, in dem Vertreter von Leitstellen ein IT-Grundschutz-Profil für Leitstellen erarbeiten. Im Gegensatz zu dem in dieser Arbeit zu erstellenden IT-Grundschutz-Profil, soll das im Workshop erarbeitete Profil auch den Bereich der polizeilichen Leitstellen umfassen. Die Herausforderungen und Ergebnisse dieses Workshops sollen ebenfalls in dieser Masterarbeit behandelt werden. Die European Emergency Number Association (EENA) ist eine internationale Nichtregierungsorganisation mit dem Zweck, Mitarbeiter und Entscheidungsträger im Bereich der Rettungsleitstellen zu vernetzen und die Arbeit in den Leitstellen durch technische und organisatorische Verbesserungen zu erleichtern. 1 Die Inhalte des erstellten IT-Grundschutz-Profils sollen von den EENA Mitgliedern theoretisch evaluiert und Ergebnisse hieraus in die Masterarbeit aufgenommen werden. Ziel ist es darzustellen,   inwiefern   das   IT-Grundschutz-Profil,   aufgrund   unterschiedlicher   Strukturen   und Organisationsformen   der   Leitstellen   anderer   Länder,   auf   diese   direkt   übertragbar   ist   oder entsprechend angepasst werden muss. Die Arbeit schlägt ein Konzept zur Umsetzung des IT-Grundschutzes vor, das die IT-Infrastruktur umfasst,   die   im   Verantwortungsbereich   der   Rettungsleitstellen   liegt.   Die   Sicherheit   der

1

https://www.eena.org   (abgerufen am 07.08.2019).

<!-- page: 9 -->

Interoperabilität mit Komponenten dritter Anbieter muss jeweils individuell betrachtet werden. Diese externen Systeme sind nachfolgend aufgeführt:

- Der auf den TETRA-Standard basierende digitale Behördenfunk der Behörden und Organisationen mit Sicherheitsaufgaben (BOS). Ein Baustein ist durch das BSI in Erstellung.
- Notruf-Apps verschiedener Hersteller.
- Alarmierungs-Apps für Hilfsorganisationen.
- Die Sicherheit der Daten- und Telefonanschlüsse auf Seiten der Netzbetreiber.

Die Absicherung dieser Komponenten liegt nicht in der Verantwortung der Rettungsleitstellen, sondern der jeweiligen Betreiber der Anwendungen und Netzwerke. Schnittstellen zu den aufgeführten externen Systemen werden in dieser Arbeit aber berücksichtigt. Diese Arbeit konzentriert sich auf Leitstellen von Feuerwehr und Rettungsdienst. Ein Teil des Konzepts wird sich auch auf Leitstellen der Polizei übertragen lassen. Da bei diesen, durch die Organisation und den Betrieb auf Bundesländer-Ebene, andere strukturelle Voraussetzungen im Vergleich zu den meist kommunal, von Landkreisen oder kreisfreien Städten betriebenen Rettungsleitstellen gelten, ergeben sich für die polizeilichen Leitstellen allerdings Unterschiede. Gleiches gilt für Servicezentralen privater Sicherheitsdienstleister oder Industrieleitstellen, weil an diese Leitstellen bezüglich ihrer Betriebsbereitschaft und Verantwortung andere Maßstäbe angelegt werden. Außerdem weichen die Anforderungen dieser Leitstellen auch untereinander stark voneinander ab.

## 1.3 Aufbau und Struktur der Arbeit

Die nachfolgenden Kapitel gliedern sich wie folgt: Nach Klärung der Grundlagen zu Rettungsleitstellen, Informationssicherheit und IT-Grundschutz, beginnt in Kapitel 3 der Teil der Arbeit, der die Erstellung des IT-Grundschutz-Profils für Rettungsleitstellen beschreibt. Das komplette ITGrundschutz-Profil ist der Arbeit als Anhang A angefügt und steht nach Fertigstellung dem BSI zur Veröffentlichung und späteren Aktualisierungen zur Verfügung. Die Veröffentlichung beim BSI und die   weitere   Pflege   des   IT-Grundschutz-Profils   soll   in   Zusammenarbeit   mit   dem   Fachverband Leitstellen erfolgen, einer Organisation, die dem überregionalen Erfahrungsaustausch zwischen verschiedenen Leitstellen dient. 2 Während der Erstellung der Arbeit wurde in der Schutzbedarfsfeststellung bei den meisten Objekten ein sehr hoher Schutzbedarf festgestellt. Infolgedessen sieht der IT-Grundschutz neben der Modellierung auch eine Risikoanalyse vor. Kapitel 4 identifiziert und bewertet daher in einer abstrakten Risikoanalyse, beispielhaft für zwei Objekte, die Risiken für Rettungsleitstellen. Um eine theoretische Evaluation zu erreichen, wird eine englische Version des IT-Grundschutz-Profils   internationalen   Vertretern   über   die   EENA  zur   Verfügung   gestellt.   Hieraus   gewonnene Erkenntnisse beschreibt Kapitel 5. Die englische Version befindet sich in Anhang B der Arbeit. Da

2

[http://www.fachverband-leitstellen.de/   (abgerufen am 01.07.2019).](http://www.fachverband-leitstellen.de/)

<!-- page: 10 -->

die Bausteine des IT-Grundschutz-Kompendiums nur in deutscher Sprache zur Verfügung stehen, weicht   der   englische   Teil   stellenweise   von   der   deutschen   Version   des   erstellten   Profils   ab. Zusätzlich behandelt Kapitel  5  die Herausforderungen und Ergebnisse des BSI-Workshops zur Erstellung eines IT-Grundschutz-Profils für Leitstellen.

Mit einem Fazit und dem Ausblick auf die weitere Bearbeitung des IT-Grundschutz-Profils für Rettungsleitstellen schließt Kapitel 6 die Arbeit ab.

<!-- page: 11 -->

## 2 Grundlagen und Begriffe

Dieses Kapitel erläutert die zentralen Grundlagen und Begriffe zu Rettungsleitstellen, stellt deren Aufgaben und Arbeitsweisen dar und ordnet die Rettungsleitstelle in den Prozess der nichtpolizeilichen Gefahrenabwehr ein. Abschnitt 2.1 beschreibt den Begriff der nichtpolizeilichen Gefahrenabwehr. Der nächste Abschnitt gibt einen Überblick zu Feuerwehr, Rettungsdienst und Katastrophenschutz. Zweck und Strukturen der Hilfsorganisationen werden kurz dargestellt. Der darauffolgende Abschnitt 2.3 betrachtet Rettungsleitstellen, deren Organisation und Aufgaben. Anschließend erklärt Abschnitt  2.4  Begriffe aus dem Bereich der Informationssicherheit. Eine Beschreibung des IT-Grundschutzes in Abschnitt 2.5 schließt das Kapitel ab.

## 2.1 Nichtpolizeiliche Gefahrenabwehr

Das Bundesamt für Bevölkerungsschutz und Katastrophenhilfe (BBK) definiert Gefahrenabwehr als 'Gesamtheit der notwendigen staatlichen Maßnahmen, um eine im Einzelfall bestehende, konkrete Gefahr für die öffentliche Sicherheit oder Ordnung abzuwehren' [BBK18]. Hierfür zuständig sind Behörden und Organisationen mit Sicherheitsaufgaben (BOS). Diese bestehen aus polizeilichen und nichtpolizeilichen Organisationen. Die nichtpolizeilichen BOS sind kommunale Behörden, Hilfsorganisationen wie die Feuerwehr, das Deutsche Rote Kreuz, der Malteser Hilfsdienst, die Johanniter Unfallhilfe oder der Arbeiter-Samariter-Bund.

Polizeiliche Gefahrenabwehr erbringt die Polizei, nichtpolizeiliche die anderen Institutionen. Während die Polizeigesetze die Aufgaben der Polizei regeln, findet die nichtpolizeiliche Gefahrenabwehr ihren Rechtsrahmen in den Feuerwehr-, Rettungsdienst- und Katastrophenschutzgesetzen der Bundesländer. Polizeiliche und nichtpolizeiliche Gefahrenabwehr unterscheiden sich in ihren Organisationsformen, Taktiken und Methoden. Viele Einsätze erfordern aber eine Zusammenarbeit beider Institutionen [WuHZ18].

## 2.2 Feuerwehr, Rettungsdienst und Katastrophenschutz

Die Aufgaben von Feuerwehr und Rettungsdienst sind in den jeweiligen Gesetzen der Länder beschrieben. Die Bezeichnung der Gesetze variiert in den einzelnen Bundesländern. In der Regel werden die Tätigkeiten der Feuerwehr in einem Brandschutz- oder Feuerwehrgesetz aufgeführt. 3 Oft ist in diesen Gesetzen auch der Katastrophenschutz geregelt. Daneben gibt es meistens ein eigenes Rettungsdienstgesetz, das die Arbeit des Rettungsdienstes beschreibt. 4 Es gibt aber auch Bundesländer, die alle Rechtsgrundlagen für die Arbeit von Feuerwehr und Rettungsdienst in einem gemeinsamen Gesetz zusammengefasst haben. 5 In einigen Bundesländern gibt es zudem separate Gesetze zur Regelung des Katastrophenschutzes. 6 Die Aufgaben der Feuerwehr sind in allen Gesetzen ähnlich geregelt. Die Hilfe bei Bränden, die Rettung von Menschen und Tieren aus lebensbedrohlichen Lagen oder die Hilfeleistung bei Unwettern oder anderen Naturereignissen gehört zu den originären Tätigkeiten der Feuerwehr in jedem Bundesland. In Analogie zu den Feuerwehrgesetzen sind auch die Aufgaben des Rettungsdienstes in allen Bundesländern gleichartig festgelegt. Aufgabe des Rettungsdienstes ist es, die Versorgung der Bevölkerung mit Leistungen der Notfallrettung und des Krankentransports sicherzustellen (so u.a. §1 RDG BW 7 ). Notfallrettung bezeichnet dabei die Behandlung und Herstellung der Transportfähigkeit von Patienten, die lebensrettende Maßnahmen benötigen oder bei denen schwere gesundheitliche Schäden zu befürchten sind [BÄK19]. Eine Katastrophe bezeichnet ein Ereignis, durch das die Gesundheit oder das Leben einer größeren Anzahl an Menschen oder die natürlichen Lebensgrundlagen aber auch bedeutende Sachwerte gefährdet sind. Weiter muss die, durch dieses Ereignis entstehende Gefahr, nur abgewendet werden können, wenn die im Katastrophenschutz mitwirkenden Institutionen unter einheitlicher Führung tätig werden [BBK18]. Die Einheiten von Feuerwehr und Rettungsdienst sind ein Teil des Katastrophenschutzes.

3 Zum Beispiel im Bayrischen Feuerwehrgesetz (BayFwG) in der Fassung vom 23.12.1981: https://www.gesetze-bayern.de/Content/Document/BayFwG.

4 Zum Beispiel das Gesetz über den Rettungsdienst sowie die Notfallrettung und den Krankentransport durch Unternehmer (Rettungsgesetz NRW - RettG NRW) in der Fassung vom 24.11.1992: https://recht.nrw.de/lmi/owa/br\_text\_anzeigen?v\_id=10000000000000000325.

<!-- page: 12 -->

## 2.2.1 Einsatzmittel

Es gibt eine Vielzahl verschiedener Einsatzmitteltypen, die von den Rettungsleitstellen disponiert werden. Alleine 25 Feuerwehrfahrzeuge sind vom Deutschen Institut für Normung (DIN) standardisiert worden [DIN18]. Je nach Art des Einsatzes wird bei Feuerwehreinsätzen die passende Ausrüstung am Einsatzort benötigt.  Neben verschiedenen Spezialfahrzeugen für weitere Einsätze, gibt es daher Feuerwehrfahrzeuge für die Brandbekämpfung und für die technische Hilfeleistung  [LFSBW05]. Bei bestimmten Einsatzarten rücken die meisten Feuerwehren zusätzlich mit einem Einsatzleitwagen (ELW) aus. Der ELW ist für die Verbindung zwischen Feuerwehr und Rettungsleitstelle besonders relevant, weil über dieses Fahrzeug in der Regel die Kommunikation stattfindet. Ein ELW hält verschiedene Kommunikationsmittel, wie Funkgeräte oder Telefon, und oft auch digitale Anwendungen zur Einsatzdokumentation vor. Im Rettungsdienst werden vor allem Rettungswagen (RTW) und Notarzteinsatzfahrzeuge eingesetzt [ScAn99].   Auch   Rettungstransporthelikopter   (RTH)   stehen   an   ausgewählten   Standorten   zur

5

6

7

Zum Beispiel das Sächsische Gesetz über den Brandschutz, Rettungsdienst und Katastrophenschutz in der Fassung

[vom 24.06.2004 (SächsGVBl): https://www.revosax.sachsen.de/vorschrift/4911-SaechsBRKG.](https://www.revosax.sachsen.de/vorschrift/4911-SaechsBRKG)

Zum Beispiel das Niedersächsische Katastrophenschutzgesetz (NKatSG) in der Fassung vom 14.02.2002:

[http://www.nds-voris.de/jportal/?quelle=jlink&amp;query=KatSchG+ND&amp;psml=bsvorisprod.psml.](http://www.nds-voris.de/jportal/?quelle=jlink&query=KatSchG+ND&psml=bsvorisprod.psml)

Rettungsdienstgesetz (RDG) Baden-Württemberg in der Fassung vom 08.02.2010:

[http://www.landesrecht-bw.de/jportal/?](http://www.landesrecht-bw.de/jportal/?quelle=jlink&query=RettDG+BW&psml=bsbawueprod.psml&max=true&aiz=true)

[quelle=jlink&amp;query=RettDG+BW&amp;psml=bsbawueprod.psml&amp;max=true&amp;aiz=true.](http://www.landesrecht-bw.de/jportal/?quelle=jlink&query=RettDG+BW&psml=bsbawueprod.psml&max=true&aiz=true)

<!-- page: 13 -->

Verfügung. Mit einem RTH ist sowohl die zügige Erreichbarkeit abgelegener Einsatzstellen möglich,   als   auch   ein   schneller   und   schonender   Transport   in   geeignete   Krankenhäuser  [LiDo00]. Besonders  in   ländlichen   Gebieten,   zu   denen   der   RTW   oft   eine   längere  Anfahrt   hat,   können zusätzlich freiwillige 'Helfer vor Ort' (HvO) alarmiert werden [SLMSA03]. Welche Einsatzmittel von der Leitstelle zu einem Einsatz alarmiert werden, ist in der Alarm- und Ausrückeordnung (AAO) festgelegt. Die Alarmierungen sind in der AAO abhängig von Einsatzort und Einsatzstichwort beschrieben. Im Einsatzleitsystem (ELS) der Leitstelle wird die AAO so abgebildet, dass der Disponent bei einem Einsatz die geeigneten Einsatzmittel direkt vorgeschlagen bekommt. Viele Leitstellen disponieren neben der Notfallrettung auch den Krankentransport. Dieser dient dem reinen Transport von nicht lebensbedrohlich Erkrankten, die nicht gehfähig sind oder aus medizinischen Gründen nicht auf andere Art transportiert werden können [BMSW99].

## 2.2.2 Hilfsfrist und Schutzziel

Das Ergebnis der Arbeit von Feuerwehr oder Rettungsdienst lässt sich nicht immer daran messen, ob die Einsatzmittel den Notfallort rechtzeitig erreicht haben. So kann ein Brand zwar schnell gelöscht worden sein, bis zum Eintreffen der Retter wurden dennoch große Teile eines Objekts zerstört. Ebenso kann der Rettungsdienst einen Patienten zwar lebend in ein geeignetes Krankenhaus transportiert haben, aber aufgrund eines langen therapiefreien Intervalls kann dieser bleibende Schäden davontragen. Entscheidend ist auch immer der Zeitpunkt, an dem die Rettungsleitstelle von einem Notfall Kenntnis  erlangt  und   die   Hilfe   an   den   Einsatzort   alarmieren   kann.   In   einigen medizinischen Publikationen werden hierfür Fachbegriffe, wie zum Beispiel die call-to-ballon-time verwendet  [VCGB17].   Diese   gibt   bei   einem   Herzinfarkt   den   Zeitraum   vom   Notruf   bis   zum Behandlungsbeginn des Patienten im Krankenhaus an. Gesetzliche Regelungen gibt es hierfür nicht. Um die Qualität von Rettungsleitstelle, Feuerwehr und Rettungsdienst messbar darstellen zu können, werden Hilfsfristen und Schutzziele festgelegt. Als Hilfsfrist gilt die Zeit zwischen dem Eingang einer Notfallmeldung in der Rettungsleitstelle und dem Eintreffen des ersten geeigneten Rettungsmittels am Einsatzort. Die Hilfsfristen für den Rettungsdienst definieren die Rettungsdienstgesetze der Bundesländer und sind daher bundesweit nicht einheitlich. Je nach Bundesland beträgt die Hilfsfrist zwischen 8 und 15 Minuten. Auch die exakte Definition der Hilfsfristen variiert in den verschiedenen Ländern. Während zum Beispiel in Bayern die Hilfsfrist erst ab dem Ausrücken der Rettungsmittel berechnet wird (§2 Abs.1 AVBayRDG 8 ), startet sie im Saarland bereits mit Eingang des Notrufs in der Rettungsleitstelle (§ 6 Abs. 3 SRettG 9 ). Entscheidend für ihre Einhaltung ist auch, welcher Rettungsmittel-Typ als geeignet angesehen wird. In der Regel ist dies bei einem medizinischen Notfalleinsatz der RTW. Das Eintreffen eines HvO ist nicht ausreichend.

8

9

Bayrisches Rettungsdienstgesetz (AVBayRDG) in der Fassung vom 30.11.2010:

[https://www.gesetze-bayern.de/Content/Document/BayAVRDG.](https://www.gesetze-bayern.de/Content/Document/BayAVRDG)

Saarländisches Rettungsdienstgesetz (SRettG) in der Fassung vom 9.2.1994:

[https://www.zrf-saar.de/mediapool/237/3\_1\_saarlaendisches\_rettungsdienstgesetz.pdf.](https://www.zrf-saar.de/mediapool/237/3_1_saarlaendisches_rettungsdienstgesetz.pdf)

<!-- page: 14 -->

In Abbildung 1 ist der zeitliche Ablauf vom Entstehen eines Notfallereignisses bis zum Eintreffen der Einsatzmittel aufgeführt. Je nach Bundesland beginnt ab T2 oder ab T5 die Berechnung der Hilfsfrist. Die Zeitspanne zwischen T0 und T2 liegt außerhalb des Einflussbereichs der Rettungsleitstelle und der Hilfsorganisationen. Bei Bränden kann diese zum Beispiel durch die Installation von Rauchmeldern oder Brandmeldeanlagen verkürzt werden.

Die Dauer, bis die Notrufverbindung aufgebaut und das Gespräch in der Rettungsleitstelle angenommen wird (T2 bis T3), sollte nur wenige Sekunden betragen. Für die Gesprächs- und Dispositionszeit (T3 bis T4) liegt die Empfehlung bei 1,5 Minuten  [AGBF15]. Hierzu gibt es aber keine gesetzlichen Vorgaben. Beeinflussen kann die Rettungsleitstelle auch die Zeitspanne von T5 bis T6, indem sie das zum Einsatzort nächstgelegene geeignete Rettungsmittel disponiert.

Abbildung 1: Zeitstrahl von Eintreten des Notfallereignisses bis zum Eintreffen der Einsatzmittel an der Einsatzstelle.

<!-- image -->

Neben der reinen Eintreffzeit des ersten Einsatzmittels wird bei Feuerwehreinsätzen die Funktionsstärke, ähnlich wie im Rettungsdienst der Typ des Rettungsmittels, als weiteres Kriterium zur Qualitätsbemessung berücksichtigt. Die Funktionsstärke stellt die Anzahl der Feuerwehrleute dar, die am Einsatzort zur Verfügung stehen. Bei einem Wohnungsbrand im Obergeschoss eines mehrstöckigen Gebäudes wird eine Mindeststärke von 10 Funktionen nach 8 Minuten und von 16 Funktionen nach 13   Minuten   empfohlen  [AGBF15].   Diese   Form   der   Qualitätsbemessung   von   Hilfsfrist   und Funktionsstärke wird bei Feuerwehreinsätzen als Schutzziel bezeichnet.

Hilfsfristen und Schutzziele dienen auch als Planungsgrößen. Werden ihre Grenzwerte zu oft überschritten, lässt sich hieraus der Bedarf für zusätzliche Ressourcen in Form von Einsatzmitteln oder weiterer Feuer- und Rettungswachen ableiten.

## 2.3 Rettungsleitstellen

Leitstellen der nichtpolizeilichen Gefahrenabwehr werden als Rettungsleitstellen bezeichnet. Sie sind Abfragestelle für den Notruf 112 und bearbeiten in der Regel Einsätze für die Feuerwehr, den Rettungsdienst und den Katastrophenschutz.

In Abbildung 2 ist die Rettungskette bei Unfallgeschehen mit Personenschaden dargestellt. Die Relevanz der Rettungsleitstelle wird sofort sichtbar. Erreicht die Notfallmeldung die Rettungsleitstelle nicht optimal oder kann diese die Rettungsmittel nicht bestmöglich disponieren, sind Verzögerungen oder sogar ein Bruch der Rettungskette möglich. Als Folge kann es zu gesundheitlichen Schäden des Patienten kommen, die bis zum Tod reichen können.

<!-- page: 15 -->

<!-- image -->

## Abbildung 2: Rettungskette bei Unfallgeschehen mit Personenschaden.

Abbildung   3 zeigt   die   Verhaltensanweisungen   im   Brandfall   nach   Brandschutzverordnung [DIN14096] in einer ähnlichen Form wie die Rettungskette in Abbildung 2. Im Brandfall muss das Ereignis frühzeitig der Rettungsleitstelle gemeldet werden, damit diese die Feuerwehr alarmieren kann, um Menschenrettungen durchzuführen und das Feuer zu löschen. Eine Unterbrechung der Kette kann auch hier eine Schädigung der Gesundheit von Menschen oder Tieren sowie anderer bedeutender Güter zur Folge haben.

<!-- image -->

## Abbildung 3: Verhalten im Brandfall (aus Brandschutzverordnung, DIN 14096).

Ist die Betriebsbereitschaft der Rettungsleitstelle beeinträchtigt, kann dies zu einer kritischen Unterbrechung der Abläufe führen. In der nichtpolizeilichen Gefahrenabwehr fällt der Leitstelle demnach eine Schlüsselrolle zu [KaKa12].

## 2.3.1 Organisation und Betrieb

Über den Notruf 112 ist es rund um die Uhr möglich, die Rettungsleitstelle anzurufen. Damit der Anruf die zuständige Leitstelle erreicht, ist jeder Landkreis und jede kreisfreie Stadt in Deutschland einer Rettungsleitstelle zugeordnet. Oft schließen sich mehrere benachbarte Gebietskörperschaften zur Bildung einer gemeinsamen Rettungsleitstelle zusammen. In Deutschland sind rund 250 Rettungsleitstellen in Betrieb [FVLS19]. Es gibt jedoch immer wieder Bestrebungen, die Anzahl durch Zusammenlegungen zu verringern [DNN19]. Betrieben werden die Rettungsleitstellen von den BOS. Die Mehrzahl der Rettungsleitstellen in Deutschland sind sogenannte integrierte Leitstellen . Der Begriff bezeichnet Leitstellen, die sowohl Einsätze der Feuerwehr als auch des Rettungsdiensts entgegennehmen und bearbeiten. Daneben gibt es in einigen Bundesländern auch kooperative Leitstellen . Sie bearbeiten auch Notrufe der Polizei. In dieser Arbeit werden ausschließlich integrierte Leitstellen betrachtet, da sie in Deutschland den Regelfall darstellen. Neben der Entgegennahme von Notrufen sind Disposition und Alarmierung von Rettungsmitteln die Hauptaufgaben der Leitstellen. Außerdem muss bei vielen Einsätzen mit weiteren Institutionen kommuniziert werden. Zum Beispiel wird oft die Polizei benötigt, um Unfallstellen abzusichern oder Hilfskräfte zu schützen. Auch Krankenhäuser müssen als geeignete Transportziele in den Ablauf eines Rettungseinsatzes mit einbezogen werden [BMSW99]. Die Vermittlung des ärztlichen Bereitschaftsdienstes für nicht lebensbedrohliche Fälle, oder die Disposition des Krankentransports, stellen weitere Aufgaben dar, die viele Rettungsleitstellen wahrnehmen.

<!-- page: 16 -->

## 2.3.2 Rettungsleitstellen als kritische Infrastrukturen

Eine funktionierende Gesellschaft ist von bestimmten Basisdiensten abhängig [Köhl17]. Dazu zählen unter anderem die Versorgung mit Energie und Wasser, die Informations- und Kommunikationsinfrastrukturen, Einrichtungen der Gesundheitsfürsorge und Einrichtungen aus dem Bereich Staat und Verwaltung [BrFi18]. Die betroffenen Sektoren sind in Tabelle 1 aufgeführt. Dienste, die in den aufgeführten Sektoren erbracht werden, zählen zu den kritischen Infrastrukturen (KRITIS). Die Bundesregierung definiert kritische Infrastrukturen als 'Organisationen oder Einrichtungen mit wichtiger Bedeutung für das staatliche Gemeinwesen, bei deren Ausfall oder Beeinträchtigung nachhaltig wirkende Versorgungsengpässe, erhebliche Störungen der öffentlichen Sicherheit oder andere dramatische Folgen eintreten würden' [BBK09].

| Sektor                                    | Beispiele                                                                                |
|-------------------------------------------|------------------------------------------------------------------------------------------|
| Staat und Verwaltung                      | Regierung und Verwaltung, Notfall- und Ret- tungswesen einschließlich Katastrophenschutz |
| Energie                                   | Stromversorger                                                                           |
| Gesundheit                                | Krankenhäuser, Rettungsdienst                                                            |
| Informationstechnik und Telekommunikation | Internetprovider, Mobilnetzbetreiber                                                     |
| Transport und Verkehr                     | Straßenverkehr, Autobahnmeisterei                                                        |
| Medien und Kultur                         | Rundfunkanstalten                                                                        |
| Wasser                                    | Wasserversorger                                                                          |
| Finanz- und Versicherungswesen            | Banken                                                                                   |
| Ernährung                                 | Lebensmittelhandel                                                                       |

## Tabelle 1: Die vom BBK definierten KRITIS-Sektoren.

Einrichtungen, die als kritische Infrastrukturen gelten, müssen folglich eine erhöhte Widerstandsfähigkeit gegen Bedrohungen aller Art aufbringen. Dabei spielt es keine Rolle, ob es sich um privatwirtschaftliche oder öffentlich-rechtlich organisierte Institutionen handelt. Für diese Einrichtungen gilt das IT-Sicherheitsgesetz 10 . Das Gesetz regelt unter anderem, dass IT-Sicherheitsvorfälle an das BSI gemeldet werden müssen.

Rettungsleitstellen fallen einerseits als hoheitliche Einrichtungen in den Bereich Staat und Verwaltung, finden sich aber andererseits auch im Sektor Gesundheit wieder. Gleichzeitig besteht für Rettungsleitstellen auch eine Abhängigkeit von anderen KRITIS-Sektoren. So benötigt eine Rettungsleitstelle   für   ihre   Betriebsbereitschaft   Strom   und   eine   funktionierende   Kommunikationsinfrastruktur.  Andere Institutionen müssen im Notfall wiederum auf die Dienste der Rettungsleitstelle zurückgreifen.

10 Gesetz zur Erhöhung der Sicherheit informationstechnischer Systeme (IT-Sicherheitsgesetz) in der Fassung vom 17.7.2015: https://www.bmi.bund.de/SharedDocs/downloads/DE/gesetztestexte/it-sicherheitsgesetz.html.

<!-- page: 17 -->

## 2.4 Informationssicherheit

Die Bedeutung von Informationstechnik hat in den letzten Jahren in allen Bereichen der Gesellschaft zugenommen [HaMN19]. Sowohl in privaten Haushalten, in Unternehmen, als auch in staatlichen Einrichtungen ist die Verwendung von Informationstechnik stark fortgeschritten und gilt in den meisten Institutionen als unverzichtbar [Tiem17]. Gleichzeitig steigt mit zunehmender Nutzung von Informationstechnik das Risiko, durch einen Ausfall, technische Fehlfunktionen oder einen Datenverlust, Schäden zu erleiden [Müll14]. Der Sicherheit der verwendeten Systeme fällt somit eine Schlüsselrolle zu [Ecke18]. Regelmäßig werden neue Beispiele für Vorfälle im Bereich der Informationssicherheit bekannt. Dabei ist es unerheblich, ob es sich um staatliche Stellen handelt, wie zum Beispiel eine Steuerbehörde 11 , oder um Unternehmen. Die Analyse eines britischen Internetanbieters hat ergeben, dass alle 50 Sekunden ein Cyberangriff auf eine britische Firma stattfindet [InfSec19]. Um das Risiko einer Verletzung der Informationssicherheit möglichst gering zu halten, sind verschiedene Schutzziele von Bedeutung. Allgemein gelten die Vertraulichkeit, die Integrität und die Verfügbarkeit als die drei übergeordneten Schutzziele der Informationssicherheit [BeAc10]. In einigen   Publikationen   werden   zusätzlich   noch   die   Authentizität,   die   Verbindlichkeit   oder   die Anonymisierung aufgeführt [Ecke18]. Auch die Nutzbarkeit von Informationen wird als Ziel von Sicherheitsmaßnahmen   genannt  [Pelt14].   Das   BSI   definiert   die   Schutzziele   der   Informationssicherheit mit der Vertraulichkeit, der Integrität und der Verfügbarkeit [BSI19b]. Diese drei Ziele werden oft auch als Grundwerte bezeichnet. Viele Menschen denken an Vertraulichkeit, wenn sie auf Informationssicherheit Bezug nehmen [JaId13]. Vertraulichkeit ist gewährleistet, wenn keine unautorisierte Informationsgewinnung möglich ist [Ecke18]. Praktisch basiert Vertraulichkeit darauf, eine Zugriffskontrolle auf Informationen festzulegen und durchzusetzen [KoSS17]. Im Zusammenhang mit Rettungsleitstellen muss die Vertraulichkeit an mehreren Stellen sichergestellt sein. Zum Beispiel darf der Zugriff auf medizinische Diagnosen von Notfallpatienten nur berechtigten Personen möglich sein. Ebenso müssen sensible Gebäude- und Lagepläne vor unbefugtem Einblick geschützt werden. Die Sicherstellung der Integrität eines Informationssystems bedeutet, dass Änderungen an den Bestandteilen des Systems nicht unbemerkt bleiben dürfen [RaPM96]. Sie dürfen nur von autorisierten Anwendern durchgeführt werden. Dies betrifft sowohl die Hardware, als auch die Software und die Daten des Systems  [TaSt08]. Änderungen an Informationen können auch unbeabsichtigt oder aufgrund eines Fehlers in der Technik auftreten. Mängel an der Integrität können in Leitstellen zum

11

Der bulgarischen Steuerbehörde wurden persönliche Daten fast aller Steuerzahler Bulgariens entwendet:

[https://www.bbc.com/news/technology-49015511 (abgerufen am 04.08.2019).](https://www.bbc.com/news/technology-49015511)

<!-- page: 18 -->

Beispiel   dazu   führen,   Rettungskräfte   zu   inkorrekten   Einsatzorten   zu   disponieren   oder   falsche Alarme auszulösen. Verfügbarkeit bezeichnet die Möglichkeit, Informationen in der erforderlichen Geschwindigkeit zum benötigten Zeitpunkt verarbeiten zu können [GrGJ17]. Dies setzt eine Betriebsbereitschaft der Systeme voraus, mit denen die Informationen bereitgestellt werden. Einschränkungen der Verfügbarkeit können beispielsweise durch Denial-of-Service (DoS) Angriffe ausgelöst werden [WuZh15]. Auch Defekte in der Hardware oder Fehler in Anwendungen können zu Ausfällen führen. Bezogen auf Rettungsleitstellen kann ein Ausfall des Kommunikationssystems (KMS) die Verfügbarkeit einschränken. Eine Erreichbarkeit der Notrufnummer 112 ist dann nicht mehr gewährleistet.

## 2.5 IT-Grundschutz

Der IT-Grundschutz des BSI hat das Ziel, die Informationssicherheit in Institutionen, unabhängig von ihrer Größe, zu erhöhen. Entstanden ist er 1994 durch die erste Veröffentlichung eines ITGrundschutzhandbuchs  [BSI19e]. Über die Jahre entwickelte sich der IT-Grundschutz zu einem Standard des Informationssicherheitsmanagements, der kompatibel zu ISO 27001:2013 12 ist und daher auch international anerkannt wird. Der IT-Grundschutz soll Institutionen unterstützen, ein Sicherheitsmanagementsystem einzuführen. Kernkomponenten des IT-Grundschutzes sind die BSI-Standards 200-1, 200-2, 200-3 und das ITGrundschutz-Kompendium. Was darunter zu verstehen ist, erläutern die nächsten Abschnitte.

## 2.5.1 Sicherheitsmanagementsystem

Informationssicherheit ist nach einem ganzheitlichen Konzept umzusetzen und nicht auf einzelne Systeme zu beschränken. Zur Erhöhung der Sicherheit lassen sich verschiedene Maßnahmen anwenden. Ein allumfassender Schutz lässt sich dennoch in den meisten Fällen nicht realisieren [KrWe17]. Das BSI unterstützt Institutionen darin, ein Sicherheitsmanagementsystem einzuführen. Dieses besteht aus den Komponenten Managementprinzipien, 'Ressourcen und Mitarbeiter' sowie einem Sicherheitsprozess [BSI19d]. Zu den Managementprinzipien gehören die Vorgabe  von   Zielen,   die   bei   der   Umsetzung   der Informationssicherheit erreicht werden sollen, die Festlegung von Grundsätzen in der Kommunikation oder Bestimmungen zur Analyse von Kosten und Nutzen. Der passende Einsatz von Technik und Personal wird durch die Komponente Ressourcen und Mitarbeiter abgebildet [BSI19d]. Die Informationstechnik obliegt einer ständigen Weiterentwicklung, die bei der Absicherung der Systeme   berücksichtigt   werden   muss.   Es   ist   daher   unumgänglich,   die   Informationssicherheit kontinuierlich  an   sich   ändernde   Rahmenbedingungen   anzupassen.   Durch   die   Umsetzung   eines Sicherheitsprozesses wird dieser Umstand im Informationssicherheitsmanagement berücksichtigt. Er   soll   dazu   beitragen,   das   Niveau   der   Informationssicherheit   durch   eine   strukturierte

12

Der internationale Standard ISO 27001:2013 beschreibt die Anforderungen für ein Informationssicherheits-

managementsystem: https://www.iso.org/standard/54534.html (abgerufen am 06.08.2019).

<!-- page: 19 -->

Vorgehensweise sukzessive zu erhöhen und durch zyklische Anwendung auf einem angemessenen Level zu halten. [BSI19c].

## 2.5.2 BSI-Standards

Das BSI hat Standards veröffentlicht, die Empfehlungen zu verschiedenen Aspekten der Informationssicherheit enthalten. Sie sollen Institutionen bei der Erreichung und Aufrechterhaltung eines angemessenen Sicherheitsniveaus unterstützen. Derzeit gibt es vier aktuelle BSI-Standards, die in Tabelle 2 aufgeführt sind. Jeder BSI-Standard setzt einen anderen Schwerpunkt.

Tabelle 2: Aktuelle BSI-Standards (Stand September 2019)

| Aktuelle BSI-Standards   | Aktuelle BSI-Standards                       | Aktuelle BSI-Standards   |
|--------------------------|----------------------------------------------|--------------------------|
| Bezeichnung              | Inhalt                                       | Stand                    |
| BSI-Standard 200-1       | Managementsysteme für Informationssicherheit | Oktober 2017             |
| BSI-Standard 200-2       | IT-Grundschutz-Methodik                      | Oktober 2017             |
| BSI-Standard 200-3       | Risikomanagement                             | Oktober 2017             |
| BSI-Standard 100-4       | Notfallmanagement                            | November 2008            |

Der   BSI-Standard   200-1   beschreibt   den   allgemeinen   Aufbau   eines   Informationssicherheitsmanagementsystems   und   die   daraus   resultierenden   Aufgaben   für   die   Leitungsebene   in   den Institutionen. Aufbauend darauf stellt der BSI-Standard 200-2 die entsprechende Methodik dar, um den im BSI-Standard 200-1 dargestellten Rahmen zu konkretisieren. Er definiert als Vorgehensweisen die Basis-, die Standard- und die Kern-Absicherung und richtet sich in erster Linie an Verantwortliche für die Informationssicherheit.

Mit dem Risikomanagement befasst sich der BSI-Standard 200-3. Hier wird dargestellt, wie Institutionen ihre Risiken in der Informationssicherheit durch eine Risikoanalyse bewerten und durch welche Maßnahmen diese verringert werden können. Trotz aller Vorkehrungen können Sicherheitsvorfälle nicht ausgeschlossen werden. Der BSI-Standard 100-4 beschreibt daher die Methodik, eine Institution auf Notfälle vorzubereiten, um den Betrieb möglichst schnell wieder aufnehmen zu können.

## 2.5.3 IT-Grundschutz-Kompendium

Das IT-Grundschutz-Kompendium des BSI ist eine Sammlung an Bausteinen für verschiedene Komponenten der Informationstechnik. Jeder Baustein enthält eine Beschreibung, die typischen Gefährdungen und die umzusetzenden Anforderungen zur Minimierung des Risikos. Diese sind unterteilt   in   Basis-   und   Standard-Anforderungen   sowie   Anforderungen   bei   erhöhtem Sicherheitsbedarf. Basis- und Standard-Anforderungen sind immer umzusetzen, sofern der Baustein für den betrachteten Informationsverbund relevant ist. Die Umsetzung der Basis-Anforderungen erzeugt die größte Wirkung und sollte daher als erstes realisiert werden. Die Anforderungen bei erhöhtem Schutzbedarf sollten in Betracht gezogen werden, wenn der Schutzbedarf über das übliche Maß hinausgeht. Derzeit   umfasst   das   IT-Grundschutz-Kompendium   94   Bausteine,   die   sich   in   verschiedene Kategorien gliedern. 13 Prozess-Bausteine sind auf den gesamten Informationsverbund anzuwenden. System-Bausteine sind nur für definierte Objekte relevant. Findet sich für ein Objekt kein passender Baustein, können auch eigene, benutzerdefinierte Bausteine, vom Anwender erstellt werden.

<!-- page: 20 -->

13 https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKompendium/bausteine/bausteine\_node.html (abgerufen am 13.09.2019).

<!-- page: 21 -->

## 3 Erstellung des IT-Grundschutz-Profils

Dieses Kapitel beschreibt die Erstellung des IT-Grundschutz-Profils für Rettungsleitstellen. Der Aufbau dieses Profils richtet sich nach der vom BSI empfohlenen Strukturbeschreibung. 14  Nachdem die   formalen  Aspekte   benannt   und   die   wichtigsten   Punkte   in   einem   Management   Summary zusammengefasst sind, wird der Geltungsbereichs des IT-Grundschutz-Profils festgelegt. Die Unterabschnitte   in  3.2  erläutern   den   Hintergrund   zu   dieser   Festlegung.  Anschließend   werden   in Abschnitt 3.3 die zu betrachtenden Objekte im Informationsverbund definiert und die getroffenen Auswahlentscheidungen begründet. Im weiteren Verlauf wird in Abschnitt  3.4  eine Strukturanalyse erstellt. Anhand dieser kann in Abschnitt 3.5 eine Schutzbedarfsanalyse durchgeführt werden. Daraus ergeben sich die in Abschnitt 3.6  beschriebenen Entscheidungsprozesse zur Auswahl der Bausteine und Anforderungen für das IT-Grundschutz-Profil.   In  Abschnitt  3.7  wird   der   Umgang   mit   nicht   hinreichend   abgedeckten Zielobjekten beschrieben. Restrisiken, die trotz Schutzmaßnahmen bestehen bleiben, werden in Abschnitt 3.8 betrachtet. Die Bewertung dieser Restrisiken wird ebenfalls in das IT-Grundschutz-Profil übernommen. Kommt es trotz   aller   Sicherheitsvorkehrungen   zu   einem  Ausfall   von   Komponenten,   darf   der   Betrieb   der Rettungsleitstelle nur so wenig wie möglich beeinträchtigt werden. Abschnitt 3.9 befasst sich daher mit dem Notfallmanagement, das auch als Business Continuity Management (BCM) bezeichnet wird.

Das erstellte IT-Grundschutz-Profil für Rettungsleitstellen wird der Arbeit als Anhang A angefügt.

## 3.1 Formale Aspekte und Management Summary

Ein IT-Grundschutz-Profil beginnt mit der Auflistung formaler Aspekte, wie den Autoren, den Herausgebern und einer vom BSI, nach Fertigstellung und Überprüfung, vergebenen Registrierungsnummer. Ebenso wird die Version des Dokuments aufgeführt. Mit Fertigstellung erhält das ITGrundschutz-Profil für Rettungsleitstellen die Versionsnummer 1.0. Grundlegende Überarbeitungen des  Dokuments erhöhen die Versionsnummer. Bei kleineren Aktualisierungen  wird die  Nachkommastelle um den Wert 1 erhöht. Um Änderungen nachvollziehen zu können, werden diese in einer Versionshistorie tabellarisch dokumentiert. Die Anforderungen an Rettungsleitstellen müssen regelmäßig an sich ändernde Rahmenbedingungen angepasst werden. Grund hierfür können zum Beispiel gesetzliche Vorgaben sein, wie die Empfangsbereitschaft für Fahrzeugnotrufe durch eCall oder die bundesweite Notruf-App. Auch technologische Umbrüche können Ursache für Modifikationen in den Rettungsleitstellen sein. Ein Beispiel ist   die   Abschaltung   des   ISDN-Netzes   der   Telefonnetzbetreiber  [MiRSW05].   Änderungen   in Organisation   oder   Technologie   können   ebenso   eine   Anpassung   der   Maßnahmen   zur

[14 https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Hilfsmittel/Profile/ Strukturbeschreibung.pdf (abgerufen am 01.07.2019).](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Hilfsmittel/Profile/Strukturbeschreibung.pdf)

<!-- page: 22 -->

Informationssicherheit   bedeuten.   Hieraus   resultierend   sollte   das   IT-Grundschutz-Profil   für Rettungsleitstellen   einer   regelmäßigen   Prüfung   auf   Aktualität   unterzogen   werden.   Der   Revisionszyklus wird auf ein Jahr festgelegt. Angesichts der Vielzahl an Rettungsleitstellen in Deutschland kann nicht davon ausgegangen werden, dass alle Institutionen die im IT-Grundschutz-Profil aufgeführten Maßnahmen zeitnah umsetzen. Um potentiellen Angreifern die Möglichkeiten einer Cyberattacke auf eine Rettungsleitstelle zu erschweren, könnte in Betracht gezogen werden, das Profil vertraulich zu behandeln und nur einem befugten Anwenderkreis zugänglich zu machen. Nachteilig an einer solchen Einstufung ist der erheblich höhere Aufwand für berechtigte Anwender, auf das Profil zuzugreifen. Diese müssten eine vorherige Autorisierung erhalten, was eine Umsetzung des IT-Grundschutz-Profils durch möglichst viele Rettungsleitstellen deutlich erschweren würde. Es ist daher nicht praktikabel den Zugriff auf das Profil einzuschränken. Zudem stellt eine Veröffentlichung des Dokuments keine konkrete Gefahr für die Leitstellen dar, weil deren Systeme nur abstrakt beschrieben werden und somit auch keine anwendungsbezogenen Sicherheitslücken aufgezeigt werden. Die Abwägung der Vor- und Nachteile, das Dokument vertraulich zu behandeln, ergibt einen größeren Nutzen, wenn das IT-Grundschutz-Profil für Rettungsleitstellen veröffentlicht wird. Im Anschluss an die formalen Aspekte enthält ein IT-Grundschutz-Profil einen kurzen Überblick über das Ziel und die wichtigsten Botschaften des Dokuments. Ebenso werden der Adressatenkreis beschrieben, erste Empfehlungen gegeben und Restrisiken benannt. Diese kompakte Übersicht ist unter der Überschrift Management Summary im IT-Grundschutz-Profil zusammengefasst.

## 3.2 Festlegung des Geltungsbereichs

In einem der ersten Schritte bei der Erstellung eines IT-Grundschutz-Profils wird der Geltungsbereich des Profils festgelegt. Zunächst wird in Abschnitt 3.2.1 die Zielgruppe definiert. Anschließend wird das zu erreichende angemessene Sicherheitsniveau abgeschätzt. Aus dieser Abschätzung ergibt sich die IT-Grundschutz Vorgehensweise, die in Abschnitt 3.2.2, nach einer rudimentären Betrachtung der Prozesse und Rahmenbedingungen in Rettungsleitstellen, festgelegt wird. Die Kompatibilität zu anderen Standards und die rechtlichen Rahmenbedingungen, die im ITGrundschutz-Profil für Rettungsleitstellen berücksichtigt sind, werden in Abschnitt 3.2.3 aufgeführt.

## 3.2.1 Zielgruppe

Das IT-Grundschutz-Profil für Rettungsleitstellen richtet sich an die für Informationstechnik verantwortlichen Entscheidungsträger aus diesem Bereich. Gleichzeitig soll es auch Herstellern und Lieferanten   von   Leitstellentechnik   als   Grundlage   für  Aufbau   und   Entwicklung   ihrer   Systeme   und Anwendungen dienen.

<!-- page: 23 -->

Für die Planung von technisch anspruchsvollen Projekten in Rettungsleitstellen kann auf die Expertise   von   externen   Fachplanern   zurückgegriffen   werden.   Auch   sie   sind Zielgruppe   des   ITGrundschutz-Profils für Rettungsleitstellen.

## 3.2.2 Schutzbedarf und IT-Grundschutz Vorgehensweise

Die Strukturbeschreibung des BSI für IT-Grundschutz-Profile sieht im Abschnitt Festlegung des Geltungsbereichs unter anderem vor, den Schutzbedarf zu ermitteln, der dem Profil zugrunde liegt. Vom Ergebnis hängt wiederum die Vorgehensweise ab, wie der IT-Grundschutz umzusetzen ist. Der IT-Grundschutz   des   BSI   bietet   hierfür   die   V orgehensweisen   Basis-,   Standard-   oder   Kern-Absicherung an (siehe Abschnitt 2.5). Abhängig davon müssen die in den Bausteinen beschriebenen Anforderungen umgesetzt werden. Eine   Schutzbedarfsfeststellung   ist   Bestandteil   der   V orgehensweisen   Standard-   und   Kern-Absicherung. Um zu klären, ob eine dieser beiden Vorgehensweisen gewählt und somit die Schutzbedarfsfeststellung durchgeführt werden muss, sind zunächst die Rahmenbedingungen in Rettungsleitstellen zu ermitteln. Hierzu werden die wesentlichen Prozesse in Rettungsleitstellen rudimentär erfasst und deren zu erreichendes Sicherheitsniveau abgeschätzt. Ebenso sind auch die Anforderungen an die Sicherheit derjenigen Parteien zu beachten, deren Daten in der Rettungsleitstelle verarbeitet   werden,   und   die   somit   ein   unmittelbares   Interesse   an   einem   angemessenen Sicherheitsniveau in der Rettungsleitstelle haben. Diese Maßnahmen entscheiden darüber, welche Vorgehensweise des IT-Grundschutzes bei der Umsetzung in Rettungsleitstellen geeignet erscheint. In den folgenden Abschnitten wird genauer auf die einzelnen Schritte eingegangen.

## 3.2.2.1 Ermittlung der Rahmenbedingungen

Um die Rahmenbedingungen für die Festlegung der Strategie zur Informationssicherheit zu ermitteln, müssen im ersten Schritt die wichtigsten Aufgaben und Prozesse in einer Rettungsleitstelle untersucht werden. Dazu gehört auch die Auswertung, welche weiteren beteiligten Institutionen zu berücksichtigen und wie hoch deren Anforderungen an die Sicherheit sind [BSI17]. Diese erste Analyse soll verdeutlichen, welche Teile des Betriebs von Rettungsleitstellen besonders gefährdet und an welchen Stellen Maßnahmen zur Verringerung dieser Gefahren notwendig sind. Das Ergebnis stellt  die   Grundlage   für   die   Formulierung   der   allgemeinen   Sicherheitsziele   dar. Nachfolgend werden diese allgemeinen Einflussfaktoren auf die Informationssicherheit analysiert und anschließend in Tabelle 3 zusammengefasst. Abhängig von der Organisationsstruktur der Institution sind zentrale oder dezentrale Formen der Entscheidung möglich. Werden diese an einer hierarchisch höher angesiedelten Stelle getroffen, handelt es sich um eine Entscheidungszentralisation. Dagegen steht die Entscheidungsdezentralisation, bei der die Entscheidungskompetenz auf niedrigere Ebenen verteilt wird  [Gabl18]. In Rettungsleitstellen liegt eine Entscheidungszentralisation vor, weil in einer zentralen Einrichtung entschieden werden muss, ob zum Beispiel eine Gefahr vorliegt und wie diese einzustufen ist.

<!-- page: 24 -->

Bei der Ermittlung der Rahmenbedingungen wird auch berücksichtigt, ob in der betrachteten Institution   ein   Qualitätsmanagementsystem   (QMS)   vorhanden   ist.   QMS   in   Rettungsleitstellen dokumentieren Abläufe und setzen Kontrollmechanismen um [NeSB13]. Eng verbunden mit einem QMS ist das Risikomanagementsystem (RMS). Das RMS soll unter anderem die Risiken identifizieren und bewerten. Es gibt Rettungsleitstellen, die QMS und RMS eingeführt haben 15 , allerdings kann nicht von einem flächendeckenden Einsatz solcher Systeme ausgegangen werden.

Wie in Abschnitt 2.3.1 beschrieben, ist für die Wahrnehmung der Aufgaben der Rettungsleitstelle eine Zusammenarbeit mit Externen erforderlich: Organisationen, die an den Einsatzort alarmiert werden, Hilfesuchende, die persönlich betroffen sind, oder Dritte, die einen Notfall entdeckt haben und diesen an die Rettungsleitstelle melden, obwohl sie selbst nicht Geschädigte sind.

Der strategische Kontext ergibt sich einerseits aus den rechtlichen Rahmenbedingungen, die in den allgemeinen nationalen 16 und internationalen 17 Bestimmungen geregelt sind und aus den, in den Gesetzen der Länder aufgeführten Aufgaben der Rettungsleitstelle. Andererseits fungiert diese als Dienstleister für die Bürger und die angebundenen Hilfsorganisationen, die mit ihr, auf zuverlässige, dem Stand der Technik entsprechenden Art und Weise, zusammenarbeiten müssen. Zum Beispiel stellen die Hilfsorganisationen Anforderungen an ein geeignetes Alarmierungssystem.

Tabelle  3: Allgemeine Einflussfaktoren in einer Rettungsleitstelle auf die Erfüllung der Hauptaufgaben.

| Einflussfaktoren zur Erfüllung der Hauptaufgaben einer Rettungsleitstelle   | Einflussfaktoren zur Erfüllung der Hauptaufgaben einer Rettungsleitstelle                                                                                               |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hauptaufgaben                                                               | - Notfallmeldungen entgegennehmen. - am besten geeignete Hilfe schnellstmöglich an Einsatzort alarmieren.                                                               |
| Organisationsstruktur                                                       | - Entscheidungszentralisation. - Risiko- oder Qualitätsmanagement nicht grundsätzlich vorhanden.                                                                        |
| Zusammenarbeit mit Ex- ternen                                               | - alarmierte Organisationen (z.B. Feuerwehr, Rettungsdienst). - Hilfesuchender (Dritter oder persönlich Betroffener).                                                   |
| Strategischer Kontext                                                       | - Gesetzlicher Auftrag für Rettungsleitstellen. - Nationale und internationale Bestimmungen. - Rettungsleitstelle als Dienstleister für Bürger und Hilfsorganisationen. |

## 3.2.2.2 Formulierung allgemeiner Sicherheitsziele

Aus  den   ermittelten  Aufgaben   und   Rahmenbedingungen   lassen   sich   die   Sicherheitsziele   der Rettungsleitstelle ableiten. Zunächst werden diese allgemein benannt. Eine Konkretisierung erfolgt erst,   nachdem   die   IT-Grundschutz-Vorgehensweise   festgelegt   und   geklärt   wurde,   ob   eine ausführliche Schutzbedarfsfeststellung notwendig ist. Entscheidende Faktoren für die Durchführung der Hauptaufgaben einer Rettungsleitstelle sind eine ständige Erreichbarkeit und eine zuverlässige Bearbeitung der Einsätze. Dies beinhaltet auch einen verlässlichen Umgang mit den vertraulichen Informationen, die für den Betrieb der Rettungsleitstelle erforderlich sind. Zu berücksichtigen ist dabei auch das notwendige Vertrauen, das den Rettungsleitstellen von den Bürgern entgegengebracht werden muss. Dieses hängt unmittelbar mit dem Ansehen einer Rettungsleitstelle in der Bevölkerung zusammen.

15 Die Leitstelle Ansbach (Bayern) hat bereits 2004 ein QMS eingeführt: https://www.ils-ansbach.de/index.php/qual (abgerufen am 11.08.2019).

16 Beispiele für Rahmenbedingungen, die sich aus den allgemeinen nationalen Gesetzen ergeben sind die Unterlassene Hilfeleistung (§323c StGB), die Schweigepflicht (§203 StGB) oder die Schadensersatzpflicht (§ 823 BGB).

17 Beispiel für eine Rahmenbedingung, die sich aus den allgemeinen internationalen Gesetzen ergibt, ist die europaweit gültige Datenschutz-Grundverordnung (DSGVO).

<!-- page: 25 -->

| Allgemeine Sicherheitsziele einer Rettungs- leitstelle   | Zugehörige Sicherheitsziele der Informations- sicherheit   |
|----------------------------------------------------------|------------------------------------------------------------|
| Ständige Erreichbarkeit                                  | Verfügbarkeit                                              |
| Zuverlässige Bearbeitung der Einsätze                    | Integrität, Verfügbarkeit                                  |
| Verlässlicher Umgang mit vertraulichen Infor- mationen   | Integrität, Vertraulichkeit                                |
| Guter Ruf in der Öffentlichkeit                          | Integrität, Verfügbarkeit, Vertraulichkeit                 |

## Tabelle 4: Sicherheitsziele in einer Rettungsleitstelle.

In Tabelle 4 sind die allgemeinen Sicherheitsziele einer Rettungsleitstelle den allgemeinen Sicherheitszielen der Informationssicherheit zugeordnet. Die ständige Erreichbarkeit der Rettungsleitstelle hängt von der Verfügbarkeit der eingesetzten Informationstechnik ab. Für eine zuverlässige Bearbeitung der Einsätze ist eine Sicherstellung von Integrität und Verfügbarkeit der Anwendungen und Daten erforderlich. Der verlässliche Umgang mit vertraulichen Informationen setzt voraus, dass die Sicherheitsziele Integrität und Vertraulichkeit erfüllt werden. Die Information soll weder verfälscht, noch   an   Unbefugte   weitergegeben   werden.   Der   gute   Ruf   einer   Rettungsleitstelle   in   der   Öffentlichkeit ist von einer Erfüllung der Sicherheitsziele Integrität, Verfügbarkeit und Vertraulichkeit abhängig.

## 3.2.2.3 Bestimmung des zur erreichenden Sicherheitsniveaus

Nachdem die allgemeinen Informationssicherheitsziele der Rettungsleitstelle festgelegt wurden, wird in diesem Abschnitt das Sicherheitsniveau bestimmt, das mit dem IT-Grundschutz-Profil erreicht werden soll. Nur mit Unterstützung   der   informationstechnischen   Systeme   kann   eine   Rettungsleitstelle   ihre Aufgaben angemessen durchführen: Erreichbarkeit für Hilfesuchende und eine zügige Bearbeitung der Einsätze. Ausfallzeiten können nicht akzeptiert werden. Die Systeme einer Rettungsleitstelle müssen korrekt arbeiten, um zu gewährleisten, dass die geeig-

nete Hilfe möglichst schnell an den Einsatzort alarmiert wird. Auch die Integrität der zu verarbeitenden Informationen muss stets gegeben sein.

<!-- page: 26 -->

Der Schutz vertraulicher Informationen muss zu jedem Zeitpunkt sichergestellt sein. Da es sich bei den Daten, die in einer Rettungsleitstelle verarbeitet werden, teilweise um kritische Informationen handelt, kann ein Verlust der Vertraulichkeit zu schweren Konsequenzen für die Leitstelle führen. Dies betrifft sowohl rechtliche Folgen, als auch das Ansehen in der Öffentlichkeit.

Die Informationssicherheitsziele Vertraulichkeit, Verfügbarkeit und Integrität müssen daher in einer Rettungsleitstelle über das übliche Maß hinaus erreicht werden. Infolgedessen ist das durch Umsetzung des IT-Grundschutz-Profils zu erreichende Schutzniveau als sehr hoch zu betrachten.

## 3.2.2.4 Festlegung der IT-Grundschutz Vorgehensweise

Der IT-Grundschutz des BSI bietet die Vorgehensweisen Basis-, Standard- oder Kern-Absicherung an. Abhängig von der gewählten Vorgehensweise müssen die in den Bausteinen beschriebenen Anforderungen umgesetzt werden.

In den letzten Abschnitten wurde ermittelt, dass für Rettungsleitstellen ein sehr hohes Schutzniveau erreicht werden muss. Die beschriebenen Anforderungen im IT-Grundschutz-Profil für Rettungsleitstellen entsprechen daher der Standard-Absicherung des BSI-Standards 200-2. Zudem sind einzelne Anforderungen aus dem erhöhten Schutzbedarf zu realisieren.

## 3.2.3 Kompatibilität zu anderen Standards und die rechtlichen Rahmenbedingungen

Die Umsetzung der Standard-Absicherung des BSI-Standards 200-2 entspricht der Erfüllung von ISO 27001:2013. Da im IT-Grundschutz-Profil für Rettungsleitstellen die Standard-Absicherung gewählt wurde, ist auch die Kompatibilität zu ISO 27001 gegeben.

Rechtliche Rahmenbedingungen werden durch Vorgaben aus der DSGVO und dem BSI-Gesetz im zu erstellenden IT-Grundschutz-Profil für Rettungsleitstellen berücksichtigt.

## 3.3 Abgrenzung des Informationsverbundes

Für die Erstellung eines IT-Grundschutz-Profils muss der Gültigkeitsbereich festgelegt werden. Ebenso   werden   Teile   benannt,   die   keine   Berücksichtigung   finden.   Die   zusammenhängenden Komponenten   einer   Institution   oder   eines   speziellen   Anwendungsbereichs   werden   als Informationsverbund bezeichnet.

Zunächst   werden   im   IT-Grundschutz   Profil   die   in   Abschnitt 3.3.1 festgelegten   relevanten Bestandteile des Informationsverbunds Rettungsleitstelle beschrieben. Es folgen die in Abschnitt 3.3.2 bestimmten Objekte, die im IT-Grundschutz-Profil nicht berücksichtigt werden.

## 3.3.1 Bestandteile des Informationsverbundes

Zum Informationsverbund gehören alle Prozesse innerhalb der Rettungsleitstelle, die durch Informationstechnik unterstützt werden. Diese besteht in erste Linie aus dem Einsatzleit- und dem Kommunikationssystem, den hierfür benötigten Netzwerkkomponenten, sowie deren Schnittstellen zu weiteren Systemen, die für den Betrieb der Rettungsleitstelle erforderlich sind. Neben Einsatzleit- und Kommunikationssystem spielen eine Reihe weiterer Anwendungen eine bedeutende Rolle. Eine wichtige Komponente stellt zum Beispiel das Alarmierungsnetz zum Auslösen von Funkmeldeempfängern dar, das von den Leitstellen selbst betrieben wird. Aus Standardsoftware bestehende Komponenten, wie Webbrowser und E-Mailclient, werden ebenso in den Informationsverbund mit einbezogen. Nicht   nur   Prozesse,   Anwendungen,   IT-Systeme   und   Netzwerke   sind   Teil   des   Informationsverbundes. Gebäude und Räume, in denen die Rettungsleitstelle betrieben wird, müssen in die Betrachtungen ebenfalls mit einbezogen werden. In Tabelle 5 sind die Bestandteile des Informationsverbundes aufgeführt. Zur eindeutigen Ausweisung wird jeder Komponente ein Identifikator zugewiesen.

<!-- page: 27 -->

Tabelle 5:   Bestandteile   des   Informationsverbundes,   die   Prozesse   und   Verfahren   in Rettungsleitstellen unterstützen.

| Identifikator   | Objekte des Informationsverbundes   |
|-----------------|-------------------------------------|
| IV1             | Prozesse                            |
| IV2             | Anwendungen                         |
| IV3             | Gebäude und Räume                   |
| IV4             | IT-Systeme                          |
| IV5             | Netzwerke                           |

## 3.3.2 Nicht berücksichtigte Teile

Nachdem im letzten Abschnitt die Bestandteile des Informationsverbundes im IT-GrundschutzProfil dargestellt wurden, werden zur Abgrenzung diejenigen Teile aufgeführt, die nicht berücksichtigt   werden.   Die   folgenden   Erklärungen   zu   diesen   Bestandteilen   werden   teilweise   in   den   entsprechenden Abschnitt im IT-Grundschutz-Profil übernommen.

## Digitaler Behördenfunk TETRA

Der auf den TETRA-Standard basierende digitale Funk der Behörden und Organisationen mit Sicherheitsaufgaben (BOS) wird im IT-Grundschutz-Profil für Rettungsleitstellen nicht vollständig berücksichtigt, weil dieser ein eigenständiges System darstellt, das lediglich Schnittstellen zu den Rettungsleitstellen bereitstellt. Das BSI erstellt hierzu derzeit einen Baustein im IT-GrundschutzKompendium, der nach Fertigstellung von den Leitstellen berücksichtigt werden sollte.

## Daten- und Telefonanschlüsse

Die technische Sicherheit der Daten- und Telefonanschlüsse liegt in Verantwortung der Netzbetreiber. Eine Berücksichtigung im IT-Grundschutz-Profil für Rettungsleitstellen ist daher nicht notwendig.

<!-- page: 28 -->

## Notruf-Apps

Immer mehr Hersteller bieten Notruf-Apps für Smartphones an, über die eine Notfallmeldung an die Rettungsleitstelle abgesetzt werden kann. Eine offizielle Notruf-App des Bundes soll im Jahr 2020 erscheinen [BR19]. Diese Form von Apps stellt ein eigenständiges System dar. Die Schnittstelle zu Rettungsleitstellen besteht in der Regel aus einer Webapplikation, die über den Webbrowser   abgerufen   werden   kann.   Notruf-Apps   müssen   daher   im   IT-Grundschutz-Profil   für Rettungsleitstellen nicht berücksichtigt werden.

## Alarmierungs-Apps

Neben   der   Alarmierung   über   das   Funknetz   der   BOS   nutzen   viele   Feuerwehren   und   Hilfsorganisationen Alarmierungs-Apps für Smartphones. Auf eine sichere Implementierung dieser Apps hat die Rettungsleitstelle keinen Einfluss. Auch hier muss daher lediglich die Schnittstelle zwischen den Anwendungen in der Rettungsleitstelle und der Alarmierungs-App betrachtet werden. Deshalb findet eine Berücksichtigung der Alarmierungs-App im IT-Grundschutz-Profil nicht statt.

## 3.4 Strukturanalyse

Die Strukturanalyse definiert Prozesse in der Rettungsleitstelle, die für die Durchführung benötigten Anwendungen, IT-Systeme, Kommunikationsverbindungen und Netzwerke sowie die verwendeten Gebäude und Räumlichkeiten. Außerdem wird untersucht, welche Informationen in der betrachteten Institution   verarbeitet   werden.   Im   IT-Grundschutz-Profil   werden   die   Ergebnisse   hieraus   in   der Referenzarchitektur abgebildet. Mit dem Resultat der Strukturanalyse soll außerdem der Schutzbedarf festgelegt werden. Die Schutzbedarfsfeststellung wird in Abschnitt 3.5 durchgeführt.

## 3.4.1 Prozesse

Der Betrieb einer Rettungsleitstelle gliedert sich in unterschiedliche Prozesse, die für das ITGrundschutz-Profil relevant sind und in diesem Abschnitt definiert werden. Als Kernprozesse gelten die Entgegennahme von Notfallmeldungen und die darauffolgende Einsatzbearbeitung in Form von Disposition und Alarmierung von Rettungsmitteln. Anschließend können weitere Prozesse stattfinden, die mit der Einsatzbearbeitung in Zusammenhang stehen. Um die Abläufe besser zu verstehen, werden die einzelnen Prozesse in der Reihenfolge beschrieben, in der sie üblicherweise auftreten.

<!-- image -->

## Abbildung 4: Kernprozesse in einer Rettungsleitstelle.

In Abbildung 4 sind die Kernprozesse in einer Rettungsleitstelle in ihrem Fluss grafisch dargestellt. Der erste zu berücksichtigende Prozess ist der Eingang einer Meldung in der Rettungsleitstelle. Es folgt deren Aufnahme in die dafür vorgesehene Anwendung. In der Regel in das Einsatzleitsystem. Anschließend wird der aus der eingegangenen Meldung resultierende Einsatz bearbeitet. Nach Beendigung des Einsatzes erfolgt dessen Abschluss. Alle Kernprozesse teilen sich in verschiedene Unterprozesse auf. Je nach Art des Einsatzes müssen dabei nicht immer alle Unterprozesse durchlaufen werden.

<!-- page: 29 -->

Daneben müssen noch weitere Prozesse in einer Rettungsleitstelle im Rahmen einer Absicherung nach IT-Grundschutz berücksichtigt werden. Dies betrifft die Eingabe und Aktualisierungen von Stammdaten in der verwendeten Software. Auch  Besprechungen und Schulungen werden regelmäßig durchgeführt.

## 3.4.1.1 Meldungseingang

Notfallmeldungen erreichen Leitstellen überwiegend per Telefon über die Notrufnummer 112. Wie Tabelle 6 zu entnehmen ist, gibt es allerdings weit mehr Meldungen, die für den Betrieb relevant sein können und im Sicherheitsprozess zur Informationssicherheit berücksichtigt werden müssen.

Tabelle 6: Prozesse bei Meldungseingang.

| Identifikator   | Prozess des Informationsverbundes          |
|-----------------|--------------------------------------------|
| P1.1            | Meldungseingang per Telefon                |
| P1.2            | Meldungseingang per Fax                    |
| P1.3            | Meldungseingang per E-Mail                 |
| P1.4            | Meldungseingang per Funk                   |
| P1.5            | Meldungseingang per Web                    |
| P1.6            | Meldungseingang per Brandmeldeanlage (BMA) |
| P1.7            | Meldungseingang per eCall                  |

Neben dem telefonischen Meldungseingang (P1.1) gibt es weitere Wege, über die eine Meldung in einer Rettungsleitstelle eingehen kann: Fax (P1.2), E-Mail (P1.3) oder eine Meldung über Funk (P1.4). Oft ist dann ein Rettungsmittel Absender der Meldung. Einige Rettungsleitstellen tauschen mit   ihren   Nachbarleitstellen   Einsatzdaten   aus   um   sich   gegenseitig   zu   unterstützen.   Die Datenübertragung erfolgt durch Webservices. Mit Einführung der Bundes-Notruf-App werden auch diese Notfallmeldungen zukünftig über Internet in die Rettungsleitstellen übermittelt (P1.5).

Daneben können Einsatzmeldungen auch über die Alarmempfangseinrichtung für Brandmeldeanlagen (BMA) in der Rettungsleitstelle eingehen (P1.6). Seit Oktober 2017 muss zudem jede Rettungsleitstelle den automatischen Fahrzeugnotruf 'eCall' empfangen können (P1.7).

## 3.4.1.2 Einsatzaufnahme

Unabhängig davon, über welchen Weg die Meldung in der Rettungsleitstelle eingeht, muss sie zur weiteren Bearbeitung in das Einsatzleitsystem aufgenommen werden (Tabelle 7). Dies kann manuell (P2.1) oder automatisch (P2.2) passieren. Die Meldungen durch die Prozesse P1.1 bis P1.5 werden manuell aufgenommen, während Meldungen durch die Prozesse P1.6 und P1.7 automatisch in das Einsatzleitsystem gespeichert werden.

<!-- page: 30 -->

Während bei der automatischen Einsatzaufnahme sämtliche, für eine Alarmierung relevanten Daten, bereits eingegeben sind und der Disponent diese nur kontrollieren muss, kann es bei der manuellen Einsatzaufnahme notwendig sein, weitere Anwendungen zur Unterstützung heranzuziehen. Befindet sich der Notrufende zum Beispiel fernab einer benannten Straße und wurden mit dem Notruf keine genauen Standortdaten übermittelt, muss der Disponent anhand des GIS den Einsatzort festlegen. Wird ein Gefahrgutunfall gemeldet, kann eine Recherche im Internet oder in anderen speziellen Anwendungen zum betroffenen Stoff und dessen Gefährdungspotential notwendig sein.

Tabelle 7: Prozesse der Einsatzaufnahme.

| Identifikator   | Prozess des Informationsverbundes                |
|-----------------|--------------------------------------------------|
| P2.1            | Einsatzaufnahme manuell in Einsatzleitsystem     |
| P2.2            | Einsatzaufnahme automatisch in Einsatzleitsystem |

## 3.4.1.3 Einsatzbearbeitung

Nach Aufnahme des Einsatzes folgen die, in Tabelle 8 aufgeführten, Schritte zur Einsatzbearbeitung: Der Einsatz muss an die nächsten geeigneten Einsatzkräfte verteilt werden. Dieser Vorgang wird in Leitstellen auch als Disposition bezeichnet (P3.1). Durch die Alarmierung werden die Kräfte über ihren Einsatzauftrag in Kenntnis gesetzt (P3.2). Läuft der Einsatz, muss dieser von der Rettungsleitstelle durch Überwachung (P3.3) und Dokumentation (P3.4) begleitet werden.

Tabelle 8: Prozesse der Einsatzbearbeitung.

| Identifikator   | Prozess des Informationsverbundes   |
|-----------------|-------------------------------------|
| P3.1            | Disposition                         |
| P3.2            | Alarmierung                         |
| P3.3            | Überwachung                         |
| P3.4            | Dokumentation                       |

Es muss zum Beispiel überwacht werden, ob die Einsatzmittel den Alarm erhalten haben, zum Einsatz ausrücken und die Einsatzstelle so schnell wie möglich erreichen. Dabei kann es vorkommen, dass die Einsatzmittel Unterstützung benötigen. Zum Beispiel beim Auffinden des Einsatzortes oder zu einem späteren Zeitpunkt bei der Suche nach einem geeigneten Transportziel für den Notfallpatienten. Außerdem muss die Dynamik des Einsatzes überwacht werden. Ändert sich die Einsatzsituation, kann es zu Nachforderungen und Alarmierungen zusätzlicher Rettungsmittel kommen.

Dokumentiert werden weitere eingehende Notrufe zu einem Einsatz. Ebenso Rückmeldungen von Einsatzmitteln vor Ort und andere wichtige Ereignisse während des Einsatzes.

<!-- page: 31 -->

## 3.4.1.4 Einsatzabschluss

Sobald alle Rettungsmittel nach einem Einsatz wieder zu ihrem Standort zurückgekehrt oder zu einem Folgeeinsatz alarmiert worden sind, gilt dieser als abgeschlossen. Der Abschluss ist mit Tätigkeiten verbunden, die in Tabelle 9 aufgeführt sind.

Die am Einsatz beteiligten Organisationen benötigen für ihre Dokumentation und zur Abrechnung diverse Daten von der Rettungsleitstelle, zum Beispiel wann die Meldung zum Einsatz einging und die Rettungsmittel alarmiert wurden. Die Rettungsleitstelle muss diese Daten den Organisationen zur Weiterverarbeitung zur Verfügung stellen. Je nach Bundesland sind statistische Einsatzdaten an organisationsübergreifende Institutionen zur Qualitätssicherung zu übermitteln. Ein Beispiel hierfür ist die Stelle zur trägerübergreifenden Qualitätssicherung im Rettungsdienst Baden-Württemberg (SQR-BW). 18 Die SQR-BW erhebt Daten von Rettungsleitstellen und Rettungsmitteln, um regelmäßige Qualitätsberichte herauszugeben (P4.1).

Abschließend werden die Einsatzdaten in den IT-Systemen der Rettungsleitstelle archiviert (P4.2). Die Frist bis zur Löschung ist gesetzlich in den Rettungsdienst- und Gefahrenabwehrgesetzen der Bundesländer geregelt. Das Feuerwehrgesetz Baden-Württemberg schreibt den Leitstellen zum Beispiel vor, aufgezeichnete Notrufe nach sechs Monaten zu löschen. Dies umfasst sowohl Inhalts- als auch Verbindungsdaten der Notrufe, wie Rufnummern oder Standortdaten.

Tabelle 9: Prozesse des Einsatzabschlusses.

| Identifikator   | Prozess des Informationsverbundes   |
|-----------------|-------------------------------------|
| P4.1            | Einsatzdatenübermittlung an Dritte  |
| P4.2            | Archivierung                        |

## 3.4.1.5 Weitere Prozesse

Die Stammdatenpflege gewährleistet, dass der Disponent bei einem Notfalleinsatz die bestmögliche Unterstützung durch die Anwendungen erhält und somit schneller Hilfe alarmieren kann. Eine korrekte Umsetzung und ein aktueller Datenbestand ist daher für den Betrieb der Rettungsleitstelle von hoher Bedeutung. Um mit ELS und KMS erfolgreich arbeiten zu können, müssen diese Systeme mit Daten versorgt werden. Dies sind Adressdaten wie Orte, Straßen oder Hausnummern. Ebenso werden wichtige Objekte wie Krankenhäuser, Gewerbebetriebe oder Schwimmbäder in die Systeme eingepflegt, um einen Notruf an diesen Orten schneller aufzunehmen. Oft werden hierzu auch weitere Informationen, wie Alarm- und Gebäudepläne, hinterlegt.

Neben den Adressdaten müssen sämtliche Einsatzmittel mit ihren Alarmierungsmöglichkeiten in den Systemen hinterlegt sein. Auch Kontaktadressen, zum Beispiel Telefonnummern oder E-Mailadressen von Funktionsträgern, gehören zum Datenbestand von ELS und KMS und müssen immer auf dem aktuellen Stand gehalten werden. Einsatztaktische Informationen werden ebenfalls im Rahmen der Stammdatenpflege in das ELS eingegeben. Dazu zählen Ausrückfolgen von Feuerwehren oder Bestimmungen, bei welchem Einsatzstichwort zusätzlich zum RTW direkt ein Notarzt alarmiert werden muss. Eine weitere Form von Informationen sind Geodaten, zum Beispiel digitale Landkarten oder Vektordaten, um die schnellste Route der Rettungsmittel zum Einsatzort zu berechnen.

18 https://www.sqrbw.de   (abgerufen am 01.07.2019).

<!-- page: 32 -->

Die Stammdatenpflege wird von Disponenten mit erweiterten Rechten in ELS und KMS übernommen. Die einzugebenden Daten erhalten diese in der Regel durch E-Mails oder auf Datenträgern wie USB-Speicher. Im IT-Grundschutz-Profil muss daher, neben der Eingabe von Daten (P5.2) in den Systemen, auch der Empfang der Daten berücksichtigt werden (P5.1).

Um die Kenntnisse der Mitarbeiter auf dem neuesten Stand zu halten, müssen regelmäßig Schulungen durchgeführt werden. Dies betrifft sowohl das fachliche Wissen, als auch die technischen Fähigkeiten bei Nutzung der Anwendungen. Neben Aus- und Fortbildungen werden auch Dienstbesprechungen durchgeführt, um organisatorische Themen zu behandeln (P6). Tabelle 10 fasst diese Prozesse zusammen.

Tabelle 10: Weitere Prozesse des Informationsverbundes.

| Identifikator   | Prozess des Informationsverbundes                                |
|-----------------|------------------------------------------------------------------|
| P5.1            | Empfang von zu hinterlegenden Daten über E-Mail und USB-Speicher |
| P5.2            | Eingabe und Speicherung von Daten in ELS und KMS                 |
| P6              | Besprechungen und Schulungen                                     |

## 3.4.2 Anwendungen

Die Prozesse des Informationsverbundes werden durch Anwendungen unterstützt. Dies sind in einer Rettungsleitstelle insbesondere ELS und KMS. Weitere wichtige Komponenten sind E-Mailclient und Webbrowser. Die Anwendungen werden in den folgenden Abschnitten beschrieben und mit einem Identifikator versehen.

## 3.4.2.1 Einsatzleitsystem einer Rettungsleitstelle

Bei der Entgegennahme einer Notrufmeldung ist keine Zeit zu verlieren. Die am besten geeigneten Rettungsmittel sind möglichst schnell zu alarmieren. Unterstützt wird dies durch ein ELS (A1). Das ELS stellt zusammen mit dem KMS die Kernanwendung für die Disponenten dar. Dieser Abschnitt führt die wichtigsten Funktionen eines ELS auf. Das KMS wird im nächsten Abschnitt beschrieben.

Zunächst unterstützt das ELS bei der Aufnahme der Notfallmeldung: Mit Entgegennahme des Notrufs werden Informationen, wie zum Beispiel die Rufnummer des Notrufenden, automatisch in das System übernommen. Übermittelte Standortdaten können direkt in einem Geoinformationssystem (GIS) angezeigt werden. Bei der Suche nach einem Einsatzort schlägt das ELS passende mögliche Ortsnamen, Straßen oder hinterlegte Objekte vor.

Ist   der   Einsatzort   festgelegt,   sind   im   GIS   verschiedene   Geoinformationen   abrufbar.   Durch Einbeziehung   von   Luftbildern   der   Einsatzstelle   kann   sich   der   Disponent   einen   Überblick verschaffen. Zum Beispiel kann es bei einem Gebäudebrand relevant sein, ob es sich um ein freistehendes Haus handelt, oder benachbarte Gebäude ebenfalls gefährdet sind. Im   ELS   sind   verschiedene   Einsatzstichwörter   hinterlegt.   Diese   können   sich   auf   einen Feuerwehreinsatz beziehen, zum Beispiel 'Brand 1', oder auf einen medizinischen Notall, zum Beispiel mit dem Stichwort 'Atemnot akut' 19 . Anhand von Einsatzort und Einsatzstichwort kann das ELS anschließend berechnen, welche Einsatzmittel vom Disponenten alarmiert werden sollen. Für die Alarmierung stellt das ELS Schnittstellen zu den verschiedenen Alarmierungsmöglichkeiten bereit. Die Alarmierung von Feuerwehr und Rettungsdienst wird oft über Funkmeldeempfänger durchgeführt. In den letzten Jahren sind zunehmend weitere Alarmierungsdienste wie SMS oder Alarm-Apps hinzugekommen. Auch in Einsatzfahrzeuge verbaute Navigationsgeräte können vom ELS, bei Alarmierung, die Koordinaten der Einsatzstelle empfangen und die Route berechnen, bevor das Personal in den Fahrzeugen eintrifft. Während des Einsatzes wird im ELS das Einsatzgeschehen dokumentiert. Rückmeldungen von den Einsatzkräften zur Lage vor Ort werden ebenso festgehalten wie Nachforderungen oder weitere Notrufe zu bereits eröffneten Einsätzen. Verändert sich die Situation im Verlauf des Einsatzes, kann im ELS eine Eskalation, also eine Erhöhung des Einsatzstichworts, zum Beispiel von 'Brand 1' auf 'Brand 2', vorgenommen werden. Hiervon hängen weitere Alarmierungen ab. Nach Beendigung eines Einsatzes   erzeugt   das   ELS   Datensätze,   die   automatisch   an   die   Verwaltungen,   der   am   Einsatz   beteiligten   Hilfsorganisationen,   zur   Dokumentation   oder   zu Abrechnungszwecken   übermittelt   werden.   Ebenso   werden   die   Einsatzdaten   für   spätere Recherchezwecke archiviert. Zwischen KMS und ELS bestehen ebenfalls Schnittstellen. Neben der Übermittlung von Daten zum Anruf, wie Rufnummer oder Standortdaten, ist es auch möglich, durch eine Aktion im ELS, den Aufbau eines Anrufs im KMS zu starten. Die weiteren Funktionen des KMS sind Inhalt des nächsten Abschnitts.

<!-- page: 33 -->

## 3.4.2.2 Kommunikationssystem einer Rettungsleitstelle

Waren Rettungsleitstellen früher mit einfachen Telefonzentralen vergleichbar, haben sie sich in den letzten Jahrzehnten zu Hochzuverlässigkeitsorganisationen gewandelt  [HaLM2015]. Dementsprechend haben sich auch Technik und Softwareanwendungen weiterentwickelt. Um interne und externe   Kommunikation   zu   betreiben,   ist   in   jeder   Rettungsleitstelle   ein   KMS   (A2)   im   Einsatz. 20 Hauptaufgabe des KMS ist die Entgegennahme der Notrufe über die Notrufnummer 112. Aber auch Anrufe   über   Nicht-Notrufleitungen   werden   im   KMS   gebündelt.   Ebenso   können   abgehende Telefonate über das KMS geführt werden. Im IT-Grundschutz-Profil für Rettungsleitstellen wird,

19

20

Die SQR-BW stellt für Rettungsleitstellen in Baden-Württemberg einen einheitlichen Einsatzstichwortkatalog zur

[Verfügung: https://www.sqrbw.de/adbimage/516/asset-original//einsatzstichwortkatalog-v11.pdf (abgerufen am](https://www.sqrbw.de/adbimage/516/asset-original//einsatzstichwortkatalog-v11.pdf)

09.08.2019).

Einige Hersteller verwenden den Begriff Sprachvermittlungssystem, z.B.

[https://www.frequentis.com/sites/default/files/support/2018-02/Frequentis%20-%20Public%20Safety%20-](https://www.frequentis.com/sites/default/files/support/2018-02/Frequentis%20-%20Public%20Safety%20-%20ASGARD%20BOS.PDF)

[%20ASGARD%20BOS.PDF (abgerufen am 28.7.2019).](https://www.frequentis.com/sites/default/files/support/2018-02/Frequentis%20-%20Public%20Safety%20-%20ASGARD%20BOS.PDF)

<!-- page: 34 -->

aufgrund der bevorstehenden Abschaltung der ISDN-Telefonanschlüsse, nur auf die neue VoIPTechnik eingegangen. Notrufbegleitende Daten können im KMS ausgewertet und für den Benutzer dargestellt werden. Diese Daten beinhalten bei Notrufen von Festnetz-Anschlüssen die Adresse des Anschlusses, von dem aus die Notrufverbindung aufgebaut wird. Bei Notrufen aus dem Mobilfunknetz werden Informationen zur Funkzelle übermittelt, aus der ein Notruf abgesetzt wird  [BNetzA18]. Einige KMS stellen auch Standortinformationen aus dem Endgerät des Notrufenden dar, sofern dieses eine solche Technik unterstützt [MMOVL16]. Seit Einführung des Fahrzeugnotrufsystems eCall für Neuwagen im Jahr 2018, erhalten die Rettungsleitstellen Datensätze, die bei einem Verkehrsunfall vom Unfallwagen generiert und mit einem automatisch ausgelösten Notruf versendet werden. 21 Den Empfang dieses Datensatzes übernimmt in der Regel ebenfalls das KMS. Neben der Telefonie dient das KMS auch der Abwicklung von Funkgesprächen. In jedem Zuständigkeitsbereich einer Rettungsleitstelle existieren verschiedene Funkkanäle, oft aufgeteilt nach geografischen Bereichen oder Zweck. So kann beispielsweise ein Funkkanal für die Feuerwehr und einer für den Rettungsdienst zugeteilt werden. Neben den Kernfunktionen Telefonie und Funk, lassen sich über das KMS auch Torsteuerungen oder elektronische Lautsprecheranlagen in Feuer- und Rettungswachen bedienen. Ebenso kann durch innovative KMS eine Vernetzung mehrerer Rettungsleitstellen zu einem Leitstellenverbund realisiert werden [EFK17].

## 3.4.2.3 Weitere Anwendungen in einer Rettungsleitstelle

Der Webbrowser gehört zur Standardanwendung für jeden Büroarbeitsplatz. Auch in Leitstellen wird   mittels   Webbrowser   im   täglichen   Betrieb   auf   Webapplikationen   und   Informationen   von Onlinemedien zugegriffen (A3). Um eine höhere Sicherheit zu erreichen, wird dieser in der Regel nicht auf dem selben Betriebssystem ausgeführt wie ELS und KMS. Über Webapplikationen externer Dienstleister können die Disponenten zum Beispiel Übersichten zu den   freien   Ressourcen   von   Krankenhäusern   abrufen.   Dadurch   arbeiten   beide   Seiten, Rettungsleitstelle   und   Krankenhaus,   ohne   großen   technischen   Aufwand   in   einer   einzigen Anwendung. 22 Auch Übersichten zu den Standorten der Einsatzmittel lassen sich über Webapplikationen aufrufen. Können die aktuellen Positionen aus technischen Gründen nicht im GIS des ELS dargestellt werden, weil das System zum Beispiel keine Internetanbindung hat, dienen Anwendungen im Webbrowser als Alternativen. Ein weiterer Grund für die Nutzung einer Webapplikation als Einsatzmittelübersicht sind zusätzliche Funktionen, die das Einsatzleitsystem nicht bereitstellt. Ein Beispiel

21

[https://ec.europa.eu/germany/news/20180328-ecall-neuwagen-verpflichtend\_de   (abgerufen am 28.7.2019).](https://ec.europa.eu/germany/news/20180328-ecall-neuwagen-verpflichtend_de)

22

Das Gesundheitsamt der Stadt Frankfurt am Main und die Firma mainis IT-Service GmbH bieten mit dem Produkt

IVENA eine Anwendung zum Versorgungsnachweis der Krankenhäuser an, die bundesweit von Leitstellen genutzt

werden kann: http://www.ivena.de (abgerufen am 13.8.2019).

<!-- page: 35 -->

ist der automatische Vorschlag für die Verschiebung von freien Einsatzmitteln für eine bessere Bereichsabdeckung. 23 Bei Einsätzen können Recherchen im Internet notwendig sein, zum Beispiel bei Gefahrstoffeinsätzen. Um die Risiken schnell abzuschätzen und passende Gegenmaßnahmen zu recherchieren, gibt es spezielle Informationssysteme zu gefährlichen Stoffen. 24 Gefahrstoffdatenbanken können aber auch als eigenständige Anwendung lokal installiert werden (A5). 25 Neben diesen speziellen Webapplikationen, deren Nutzung exklusiv den Leitstellen vorbehalten ist und eine vorherige Authentifizierung erfordert, können auch allgemeine, für jeden Bürger zugängliche Informationen aus dem Internet, für die Arbeit der Leitstelle hilfreich sein. Beispiele sind Wettervorhersagen, die Recherche nach Medikamenten oder die aktuelle Verkehrssituation. Wie in fast allen Institutionen wird in Rettungsleitstellen zur internen und externen Kommunikation E-Mail verwendet. Zum komfortablen Empfang und Versand von E-Mails kann ein E-Mailclient eingesetzt werden (A4). Neben dem Webbrowser ist auch der E-Mailclient in der Regel nicht auf dem Betriebssystem wie ELS und KMS installiert. Zur Betrachtung von Dokumenten, zum Beispiel Alarmpläne oder Anfahrtsskizzen, wird außerdem ein PDF-Viewer benötigt (A6). An den Büroarbeitsplätzen werden Anwendungen zur Textbearbeitung und Tabellenkalkulation verwendet. Auch für das Erstellen von Präsentationen muss eine entsprechende Software bereitgestellt werden. Für diese Zwecke ist auf den Büroarbeitsplätzen ein Office-Produkt installiert (A7). Um untereinander Dateien auszutauschen, kann ein Laufwerk im Netzwerk freigegeben werden (A8). Dabei sind Rechte und Rollen zu berücksichtigen.

## 3.4.2.4 Zusammenfassung der Anwendungen

Alle in den vorherigen Abschnitten beschriebenen Anwendungen sind in Tabelle 11 mit einem Identifikator   aufgeführt.   In   der   rechten   Spalte   ist   angegeben,   welche   Prozesse   von   den   jeweiligen Anwendungen unterstützt werden.

23

24

25

Die Firma Rescuetrack bietet zum Beispiel mit ihrem Produkt Rescuetrack entsprechende Dienste an:

[http://www.rescuetrack.de/de-de/leitstelle/ (abgerufen am 13.8.2019).](http://www.rescuetrack.de/de-de/leitstelle/)

Das Landesamt für Natur, Umwelt und Verbraucherschutz Nordrhein-Westfalen stellt Rettungsleitstellen und ande-

ren autorisierten Institutionen ein passwortgeschütztes Informationssystem für gefährliche Stoffe bereit:

http://stoffliste.de (abgerufen am 13.8.2019).

Ein Beispiel hierfür ist das Produkt Memplex der Keudel av-Technik GmbH: https://memplex.de/ (abgerufen am

13.8.2019).

<!-- page: 36 -->

| Identifikator   | Anwendungen des Informationsverbundes   | Unterstützte Prozesse        |
|-----------------|-----------------------------------------|------------------------------|
| A1              | Einsatzleitsystem                       | P1.6, P1.7, P2, P3, P4, P5.2 |
| A2              | Kommunikationssystem                    | P1.1, P1.4, P1.7, P3, P5.2   |
| A3              | Webbrowser                              | P1.5, P3, P5                 |
| A4              | E-Mailclient                            | P1.3, P5.1                   |
| A5              | Gefahrstoffinformationssysteme          | P2.1, P3                     |
| A6              | PDF-Viewer                              | P2.1, P3, P5                 |
| A7              | Office-Produkt                          | P5.1                         |
| A8              | Dateiablage/freigegebene Netzlaufwerke  | P4, P5                       |

## Tabelle 11: Anwendungen des Informationsverbundes, die in einer Rettungsleitstelle verwendet werden.

## 3.4.3 IT-Systeme

Alle beschriebenen Anwendungen benötigen für ihren Betrieb unterschiedliche Systeme. Diese sind in Tabelle 12 aufgeführt. Komponenten, die Netzwerkverbindungen betreffen, werden in Abschnitt 3.4.4 extra betrachtet.

| Identifikator   | IT-Systeme des Informationsverbundes                  | Abhängige Anwendungen/Prozesse   |
|-----------------|-------------------------------------------------------|----------------------------------|
| S1.1            | Betriebssysteme für Clients                           | A1, A2, A3, A4, A5, A6, A7, A8   |
| S1.2            | Betriebssysteme für Server                            | A1, A2                           |
| S2.1            | Server                                                | A1, A2                           |
| S2.2            | Virtualisierungsplattformen                           | A1, A2                           |
| S3              | Arbeitsplatz-Client                                   | A1, A2, A3, A4, A5, A6, A7, A8   |
| S4              | Faxgeräte                                             | P1.2                             |
| S5              | Drucker und Multifunktionsgeräte (Scan- ner/Kopierer) | A1, A6, A7                       |

## Tabelle 12: IT-Systeme des Informationsverbundes, die in einer Rettungsleitstelle verwendet werden.

ELS und KMS erfordern zur Bereitstellung ihrer Funktionalität ein Betriebssystem (S1) und Hardware (S2) als Unterbau. Die Auswahl des Betriebssystems hängt vom verwendeten ELS und KMS ab. In der Regel werden auf den Arbeitsplatz-Clients (S1.1) Windows-Betriebssysteme verwendet. Auf   den   Servern   (S1.2)   können   Linux-   und   Windows-Betriebssysteme   genutzt   werden.   Als Hardware (S2.1) kommen   normalerweise   Standardkomponenten zum   Einsatz. Auch Virtualisierungsplattformen (S2.2), auf denen mehrere virtuelle Server installiert werden können,

sind in Leitstellen üblich.

Schriftliche Kommunikation wird heute in der Regel über E-Mails geführt. Jedoch können in Rettungsleitstellen Informationen noch per Telefax (S4) ausgetauscht werden. Unter anderem muss die Erreichbarkeit des Notrufs 112 auch für körperlich beeinträchtigte Personen, wie zum Beispiel Hörgeschädigte, gewährleistet sein. Hierfür wird ein Faxgerät in der Rettungsleitstelle vorgehalten. Eingehende Faxe können entweder vom KMS automatisch erkannt oder manuell auf ein Faxgerät weitergeleitet werden. Ebenso gehören Drucker und Multifunktionsgeräte (S5) zum Scannen und Kopieren zur Grundausstattung einer Leitstelle. Dies schließt auch Drucker in den Feuer- und Rettungswachen mit ein, die über VPN mit der Leitstelle verbunden sind. Auf diesen Geräten können Alarmdepeschen 26 bei Einsätzen der Wachen ausgedruckt werden.

<!-- page: 37 -->

## 3.4.4 Netzwerke

Anwendungen und IT-Systeme der Rettungsleitstelle sind in unterschiedliche Netzwerke eingebunden. Anzahl und Aufbau der Netze lassen sich nicht im Detail verallgemeinern. Allerdings wird davon ausgegangen, dass die Architektur in vielen Leitstellen zumindest ähnlich ist. Zum Betrieb der Netze sind aktive und passive Netzkomponenten erforderlich. Eine besondere Bedeutung hat in Rettungsleitstellen das Alarmierungsnetz zum Auslösen von Funkmeldeempfängern. Die Übersicht über alle Netzkomponenten und Netze des Informationsverbundes enthält Tabelle 13 in Abschnitt 3.4.4.3.

## 3.4.4.1 Netze und Netzkomponenten

Zur Erstellung des IT-Grundschutz-Profils für Rettungsleitstellen wird von einer Netzwerkarchitektur ausgegangen, in der ELS und KMS in separaten Netzwerken betrieben werden (N1 und N2). Zwischen den Netzwerken besteht  eine  Verbindung   zum  Austausch   von   Informationen.   Zum Beispiel müssen bei einem eingehenden Notruf die Rufnummer des Anrufers und notrufbegleitende Daten wie Standortinformationen, in das ELS übernommen werden. Umgekehrt muss es möglich sein, aus dem ELS heraus, einen Telefonanruf aufzubauen, der über das KMS geführt wird. Für die Nutzung von Webanwendungen, die Kommunikation über E-Mail und die Verwendung von Office-Produkten werden Arbeitsplatz-Clients in einem, von ELS und KMS getrennten, eigenen Netzwerk bereitgestellt.   Um   diese  Aufgaben   durchführen   zu   können,   ist   auf   den   Clients   oft Standard-Software installiert. Das Netz wird daher als Büro-Netz bezeichnet (N3). Zur Erfüllung ihrer jeweiligen Anforderungen benötigen alle drei Netzwerke eine Verbindung zum Internet Service Provider (ISP, N4). Zum Beispiel ruft das ELS Positionsdaten von Einsatzmitteln über das Internet ab und versendet Informationen an die beteiligten Organisationen als automatische E-Mail. Um in externen Feuer- und Rettungswachen bei Einsätzen Alarmdurchsagen abzuspielen oder dortige Alarmmonitore anzusteuern, wird über das Internet ein VPN zum ELS aufgebaut. Die Umstellung der Telefonanschlüsse auf Voice over IP (VoiP) erfordert auch für das KMS eine Anbindung an das Internet. 27 Webbrowser und E-Mailclient auf den Arbeitsplätzen im BüroNetzwerk benötigen ebenfalls Zugriff auf das Internet.

26

27

Als Alarmdepeschen werden Dokumente bezeichnet, die den Einsatzauftrag für ein Einsatzmittel enthalten. In der

Regel enthält die Alarmdepesche den Einsatzort, das Einsatzstichwort und weitere Informationen.

Die Deutsche Telekom plant eine Umstellung der Notrufanschlüssen 110 und 112 auf IP bis Ende 2020 [DeTe18].

<!-- page: 38 -->

Zum Betrieb der aufgeführten Netzwerke werden Netzkomponenten (N5) benötigt. Router stellen die Verbindung zwischen den internen Netzen der Rettungsleitstelle und dem Internet her. Um eingehenden   und   ausgehenden   Netzwerkverkehr   zu   filtern   und   den   Zugriff   innerhalb   der verschiedenen Netzwerke zu regeln, werden Firewalls eingesetzt. Durch die Verwendung von Switches kann eine Vielzahl von Clients mit Servern und anderen IT-Systemen verbunden werden. Auch Kabel und Patchfelder (N6) werden in einer Rettungsleitstelle benötigt.

## 3.4.4.2 Alarmierungsnetz

Die meisten Rettungsleitstellen verwenden zur unverzüglichen Alarmierung der Rettungskräfte ein spezielles Netz (N7) zum Auslösen von Digitalen Funkmeldemepfängern (DME). Dabei handelt es sich   um   ein   Funknetz   der   BOS   im   2-Meter-Band.  Als   Protokoll   wird   POCSAG   verwendet. POCSAG ist die Abkürzung  für Post Office Code Standard Advisory Group und wurde in den späten 70er Jahren von der britischen Post entwickelt [RMBD98].

<!-- image -->

## Abbildung 5: Aufbau eines POCSAG Alarmierungsnetzes mit einem Master-DAU (links) und mehreren Master-DAUs (rechts).

Um den kompletten Zuständigkeitsbereich einer Rettungsleitstelle abzudecken, besteht das Funkalarmierungsnetz aus drahtlos miteinander kommunizierenden Digitalen Alarmumsetzern (DAU). Der Alarm wird vom ELS über den Digitalen Alarmgeber (DAG) an einen Master-DAU übermittelt, der sich in der Regel in der Leitstelle befindet. Orte, die vom Master-DAU weit entfernt sind, empfangen einen Alarm daher erst nach einer Weiterleitung über mehrere DAUs. Dies kostet Zeit. Um die Aussendezeit zu verringern, können mehrere Master-DAUs im Netz installiert werden. Diese versenden den Alarm zeitgleich mit dem Master-DAU in der Leitstelle. Hierzu sind sie über einen weiteren Kommunikationsweg mit der Leitstelle verbunden, zum Beispiel über eine Internetverbindung. Beide Varianten sind in Abbildung 5 dargestellt.

## 3.4.4.3 Netzübersicht und Netzplan

In Tabelle 13 sind die Netzkomponenten und Netze des Informationsverbundes zusammengefasst. Hieraus ergibt sich der in Abbildung 6 aufgeführte Netzplan des Informationsverbundes. Faxgeräte (S4) sind nicht aufgeführt, da diese unabhängig betrieben werden oder im KMS integriert sind.

<!-- page: 39 -->

Tabelle 13: Netzkomponenten und Netze des Informationsverbundes.

| Identifikator   | Objekt des Informationsverbundes   | Abhängige Objekte                      |
|-----------------|------------------------------------|----------------------------------------|
| N1              | ELS-Netz                           | A1, S1, S2, S3, S5                     |
| N2              | KMS-Netz                           | A2, S1, S2, S3, S5                     |
| N3              | Büro-Netz                          | A3, A4, A5, A6, A7, A8, S1, S2, S3, S5 |
| N4              | Netz zum Internet Service Provider | A1, A2, A3, A4                         |
| N5.1            | Router                             | N1, N2, N3                             |
| N5.2            | Switches                           | N1, N2, N3                             |
| N5.3            | Firewalls                          | N1, N2, N3                             |
| N5.4            | Session Border Controller          | N2                                     |
| N6              | Kabel/Patchfelder                  | N1, N2, N3                             |
| N7              | Alarmierungsnetz für Funkmelder    | A1                                     |

Abbildung 6: Netzplan des Informationsverbundes.

<!-- image -->

## 3.4.5 Gebäude und Räume

Nicht nur die technischen Komponenten sind für die Informationssicherheit wichtig. Auch die Sicherheit der Gebäude und Räume, in denen die Rettungsleitstelle betrieben wird, muss in einem IT-Grundschutz-Profil berücksichtigt werden.

<!-- page: 40 -->

Der Dispositionsraum (R1) stellt den Kern einer Rettungsleitstelle dar. Hier nehmen Disponenten Notfallmeldungen entgegen und disponieren die Rettungsmittel zu den Einsätzen. In allen Leitstellen   ist   dieser   Raum   24   Stunden   am   Tag,   an   sieben   Tagen   die   Woche,   besetzt.   In Ausnahmesituationen,   wie   bei   Unwettern,   können   binnen   kürzester   Zeit   eine   Vielzahl   an zusätzlichen Notfallmeldungen eingehen. Für diese Fälle gibt es einen Raum mit zusätzlichen, einfacher ausgestatteten Arbeitsplätzen. Sind in der Rettungsleitstelle solche Räume vorhanden, werden sie im Folgenden nicht separat betrachtet, sondern wie der Dispositionsraum behandelt.

Jede Rettungsleitstelle benötigt ein Rechenzentrum oder einen Technikraum (R2), in dem die Server und weitere Technik untergebracht sind. Neben der Disposition müssen in einer Rettungsleitstelle auch Verwaltungsaufgaben übernommen werden. Hierfür stehen Büroarbeitsplätze (R3) zur Verfügung. Benötigt werden Büros für die Leitung der Rettungsleitstelle (R3.1), Räume in denen die Stammdatenpflege (R3.2) durchgeführt wird und Arbeitszimmer für die Administratoren (R3.3). Zur weiteren Betrachtung werden die Büroräume in einer Gruppe (R3) zusammengefasst.

Die Anschlüsse für Telefon- und Datenverbindungen befinden sich häufig in einem speziellen Raum im Gebäude der Rettungsleitstelle. Dieser Raum für Telekommunikationsanschlüsse (R4) muss bei der Betrachtung der Informationssicherheit ebenfalls berücksichtigt werden und ist somit Teil des Informationsverbundes.  In  Tabelle   14  sind   außerdem   ein  Archivraum   für   die   Lagerung   von Datenträgern und ein Besprechungsraum aufgeführt.

Tabelle 14: Räume des Informationsverbundes.

| Identifikator   | Räume des Informationsverbundes       | In den Räumen installierte IT- Systeme oder durchgeführte Prozesse   |
|-----------------|---------------------------------------|----------------------------------------------------------------------|
| R1              | Dispositionsraum                      | P1, P2, P3, S3, S4, S5                                               |
| R2              | Rechenzentrum/Technikraum             | S2                                                                   |
| R3.1            | Büro der Leitung der Leitstelle       | S3, S4, S5                                                           |
| R3.2            | Stammdatenpflegebüro                  | P5, S3, S4, S5                                                       |
| R3.3            | Administratorbüro                     | S3, S4, S5                                                           |
| R4              | Raum für Telekommunikationsanschlüsse | N2, N4                                                               |
| R5              | Archivraum                            | P4                                                                   |
| R6              | Besprechungs- und Schulungsraum       | P6                                                                   |

## 3.4.6 Übersicht Objekte Informationsverbund

Die in den vorangegangenen Abschnitten definierten Objekte des Informationsverbundes werden in Tabelle 15 zur besseren Übersicht zusammengefasst.

| IV       | Identifikator   | Objekte und Prozesse des Informationsverbunds   |
|----------|-----------------|-------------------------------------------------|
| IV1      | P1              | Meldungseingang                                 |
| Prozesse | P2              | Einsatzaufnahme                                 |

<!-- page: 41 -->

|                            | P3   | Einsatzbearbeitung                                  |
|----------------------------|------|-----------------------------------------------------|
|                            | P4   | Einsatzabschluss                                    |
|                            | P5   | Stammdatenpflege                                    |
|                            | P6   | Besprechungen und Schulungen                        |
| IV2 Anwendungen            | A1   | Einsatzleitsystem                                   |
| IV2 Anwendungen            | A2   | Kommunikationssystem                                |
| IV2 Anwendungen            | A3   | Webbrowser                                          |
| IV2 Anwendungen            | A4   | E-Mailclient                                        |
| IV2 Anwendungen            | A5   | Gefahrstoffinformationssysteme                      |
| IV2 Anwendungen            | A6   | PDF-Viewer                                          |
| IV2 Anwendungen            | A7   | Office-Produkt                                      |
| IV2 Anwendungen            | A8   | Dateiablage/freigegebene Netzlaufwerke              |
| IV3 IT-Systeme             | S1   | Betriebssysteme                                     |
| IV3 IT-Systeme             | S2   | Server                                              |
| IV3 IT-Systeme             | S3   | Arbeitsplatz-Clients                                |
| IV3 IT-Systeme             | S4   | Faxgeräte                                           |
| IV3 IT-Systeme             | S5   | Drucker und Multifunktionsgeräte (Scanner/Kopierer) |
| IV4 Netzwerk- verbindungen | N1   | ELS-Netz                                            |
| IV4 Netzwerk- verbindungen | N2   | KMS-Netz                                            |
| IV4 Netzwerk- verbindungen | N3   | Büro-Netz                                           |
| IV4 Netzwerk- verbindungen | N4   | Netz zum Internet Service Provider                  |
| IV4 Netzwerk- verbindungen | N5   | Aktive Netzkomponenten                              |
| IV4 Netzwerk- verbindungen | N6   | Passive Netzkomponenten                             |
| IV4 Netzwerk- verbindungen | N7   | Alarmierungsnetz für Funkmeldeempfänger             |
| IV5 Gebäude und Räume      | R1   | Dispositionsraum                                    |
| IV5 Gebäude und Räume      | R2   | Rechenzentrum/Technikraum                           |
| IV5 Gebäude und Räume      | R3   | Büroräume                                           |
| IV5 Gebäude und Räume      | R4   | Raum für Telekommunikationsanschlüsse               |
| IV5 Gebäude und Räume      | R5   | Archivraum                                          |
| IV5 Gebäude und Räume      | R6   | Besprechungs- und Schulungsraum                     |

## Tabelle 15: Im IT-Grundschutz-Profil für Rettungsleitstellen berücksichtigte Objekte des Informationsverbundes.

<!-- page: 42 -->

## 3.5 Schutzbedarfsfeststellung

Grundlegend sind bei der Festlegung des Schutzbedarfs die Auswirkungen, die eine Verletzung der Grundziele der Informationssicherheit hätten. Dies sind Vertraulichkeit, Integrität und Verfügbarkeit, wie in Abschnitt 2.4 beschrieben. Im Folgenden werden die Auswirkungen betrachtet. Das BSI benennt verschiedene Szenarien, auf die sich ein Schaden beziehen kann. Sie sind in Tabelle 16 aufgeführt.

Verstöße gegen Gesetze, Vorschriften oder Verträge (SZ1) können zum Beispiel vorliegen, wenn die Rettungsleitstelle nicht betriebsbereit ist und ihre Aufgaben nicht erfüllen kann (SZ4). Hierdurch kann es zu Beeinträchtigungen der persönlichen Unversehrtheit von Notrufenden kommen (SZ3), wenn diesen nicht rechtzeitig geholfen wird. Verstöße gegen Datenschutzgesetze fallen ebenfalls unter   SZ1.   Die   Übermittlung   vertraulicher   Informationen,   über   Anrufer   oder   Patienten,   an Unbefugte, stellt zudem eine Beeinträchtigung des informationellen Selbstbestimmungsrechts der Hilfesuchenden dar (SZ2). Aufgrund von Schadensersatzforderungen der Betroffenen können die benannten Fälle auch finanzielle Auswirkungen auf die Leitstelle haben (SZ6).

Für die Menschen ist ein hohes Vertrauen in die Arbeit der Rettungsleitstelle elementar. Die Hilfe im Notfall gibt ihnen ein sicheres Gefühl. Durch eine negative Außenwirkung (SZ5) kann diese Gewissheit   verloren   gehen.   Gleiches   gilt   für   das   Personal   der   Rettungsleitstelle   oder   der angebundenen Hilfsorganisationen bei einer negativen Innenwirkung. Diese Effekte können zum Beispiel aufgrund von Ausfällen und damit verbundener negativer Berichterstattung in den Medien auftreten.

| Identifikator   | Schadensszenario                                                |
|-----------------|-----------------------------------------------------------------|
| SZ1             | Verstöße gegen Gesetze, Vorschriften oder Verträge              |
| SZ2             | Beeinträchtigungen des informationellen Selbstbestimmungsrechts |
| SZ3             | Beeinträchtigungen der persönlichen Unversehrtheit              |
| SZ4             | Beeinträchtigungen der Aufgabenerfüllung                        |
| SZ5             | negative Innen- oder Außenwirkung                               |
| SZ6             | finanzielle Auswirkungen                                        |

## Tabelle 16: Potentielle Schadensszenarien.

Die Schadensszenarien werden in den folgenden Abschnitten für jedes der Grundziele der Informationssicherheit einzeln betrachtet. Dabei kann die Schadensauswirkung nicht im voraus detailgenau festgelegt   werden.   Aus   diesem   Grund   empfiehlt   die   IT-Grundschutz-Methodik   des   BSI   den Schutzbedarf in die drei Kategorien normal , hoch und sehr hoch einzustufen [BSI18]. Tabelle 17 führt   die   Kategorien   und   die   Schadensauswirkungen   auf.   Diese   können   sich   auf   die Rettungsleitstelle selbst oder auf die hilfesuchenden Bürger beziehen.

<!-- page: 43 -->

Tabelle 17: Vom BSI empfohlene Schutzbedarfskategorien, übertragen auf Leitstellen.

| Kategorie   | Schadensauswirkung                                                                                                                                                           |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| normal      | Die Schadensauswirkungen für die Leitstelle oder die hilfesuchenden Bürger sind be- grenzt und überschaubar.                                                                 |
| hoch        | Die Schadensauswirkungen können den Betrieb der Leitstelle erheblich einschränken. Für die hilfesuchenden Bürger können die Konsequenzen beträchtlich sein.                  |
| sehr hoch   | Die Schadensauswirkungen können den Betrieb der Leitstelle stilllegen. Für die hilfe- suchenden Bürger kann es zu existenziell- oder lebensbedrohlichen Konsequenzen kommen. |

Bei der Bestimmung des Schutzbedarfs eines in Abschnitt 3.4 bestimmten Objekts müssen auch die Prozesse oder andere Objekte betrachtet werden, für die dieses Objekt benötigt wird. Wird zum Beispiel ein Objekt für einen Prozess verwendet, dessen Schutzbedarf sehr hoch ist, so ist auch der Schutzbedarf des betrachteten Objekts als sehr hoch einzustufen.

## 3.5.1 Schutzbedarfsfeststellung für Prozesse

Für die Schutzbedarfsfeststellung der Prozesse muss das Ausmaß eines Schadens auf den jeweiligen Prozess ermittelt werden. Zunächst werden alle in Abschnitt 3.4.1 definierten Prozesse hinsichtlich der   Vertraulichkeit   untersucht.   Anschließend   findet   in   Abschnitt 3.5.1.2 eine   Untersuchung bezüglich   der   Integrität   statt.   Zuletzt   wird   in   Abschnitt 3.5.1.3 der   Schutzbedarf   für   die Verfügbarkeit der einzelnen Prozesse ermittelt.

## 3.5.1.1 Schutzbedarfsfeststellung der Vertraulichkeit für Prozesse

In den Prozessen zum Meldungseingang P1.1, P1.2, P1.4 und P1.5 können personenbezogene Daten von Patienten verarbeitet werden, die medizinische Diagnosen beinhalten. Eine Beeinträchtigung der Vertraulichkeit würde somit gegen gesetzliche Vorgaben verstoßen (SZ1) und das informationelle Selbstbestimmungsrecht des Betroffenen verletzen (SZ2). Dies könnte zu einer negativen Außenwirkung (SZ5) führen und Schadensersatzzahlungen (SZ6) zur Folge haben. Neben den medizinischen Diagnosen von Patienten werden in der Leitstelle weitere vertrauliche Daten verarbeitet. Zum Beispiel können Einsätze der Polizei eine Unterstützung durch die Feuerwehr im Rahmen der Amtshilfe erfordern. Aus diesen Gründen ist die Vertraulichkeit für die genannten Prozesse als sehr hoch einzustufen.

Die in einer Rettungsleitstelle über E-Mail empfangenen Nachrichten (P1.3) enthalten in der Regel allgemeine Informationen wie Wetterwarnungen, Meldungen zur Einsatzbereitschaft und Dienstzeiten   von   Rettungsmitteln   oder   zu   geplanten   Großveranstaltungen.   E-Mails   beinhalten   somit normalerweise keine vertraulichen Informationen. Meldungen, die automatisch über eine Brandmeldeanlage (P1.6) oder den Fahrzeugnotruf eCall (P1.7) eingehen, enthalten keine personenbezogenen Daten. Die übermittelten Informationen bestehen lediglich aus technischen Parametern, wie dem mit einer Brandmeldeanlage verknüpften Objekt oder die Anzahl der Fahrzeuginsassen beim eCall.

<!-- page: 44 -->

Für den, in der Regel parallel zum eCall eingehenden Sprachanruf, gilt der Schutzbedarf wie beim Meldungseingang per Telefon (P1.1).

Der Schutzbedarf hinsichtlich der Vertraulichkeit bei den Einsatzaufnahmeprozessen leitet sich aus dem jeweiligen Schutzbedarf der Prozesse des Meldungseingangs ab.  Unabhängig davon, auf welchem Weg eine Meldung in der Rettungsleitstelle eingegangen ist, muss bei den Prozessen der Einsatzbearbeitung (P3) und des Einsatzabschlusses (P4) immer von einer Verarbeitung personenbezogener Daten mit medizinischen Diagnosen ausgegangen werden. Der Schutzbedarf hinsichtlich der Vertraulichkeit ist somit bei allen Prozessen als sehr hoch einzustufen.

Tabelle 18: Schutzbedarf der Vertraulichkeit für Prozesse.

| Schutzbedarfsfeststellung der Vertraulichkeit für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Vertraulichkeit für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Vertraulichkeit für Prozesse des Informationsverbundes                                            |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Objekt                                                                                 | Schutzbedarf                                                                           | Begründung                                                                                                                      |
| P1.1                                                                                   | sehr hoch                                                                              | Verarbeitung von Daten mit medizinischen Diagnosen oder zu vertraulichen Einsätzen anderer Institutionen (SZ1, SZ2, SZ5, SZ6).  |
| P1.2                                                                                   | sehr hoch                                                                              | Verarbeitung von Daten mit medizinischen Diagnosen oder zu vertraulichen Einsätzen anderer Institutionen (SZ1, SZ2, SZ5, SZ6).  |
| P1.3                                                                                   | normal                                                                                 | Über E-Mail werden in der Regel keine vertraulichen Informationen empfangen.                                                    |
| P1.4                                                                                   | sehr hoch                                                                              | Verarbeitung personenbezogener Daten mit medizinischen Diagnosen, die vertraulich behandelt werden müssen (SZ1, SZ2, SZ5, SZ6). |
| P1.5                                                                                   | sehr hoch                                                                              | Verarbeitung personenbezogener Daten mit medizinischen Diagnosen, die vertraulich behandelt werden müssen (SZ1, SZ2, SZ5, SZ6). |
| P1.6                                                                                   | normal                                                                                 | Es werden nur technische Parameter übermittelt.                                                                                 |
| P1.7                                                                                   | normal                                                                                 | Es werden nur technische Parameter übermittelt.                                                                                 |
| P2.1                                                                                   | sehr hoch                                                                              | Verarbeitung personenbezogener Daten mit medizinischen Diagnosen (SZ1, SZ2, SZ5, SZ6).                                          |
| P2.2                                                                                   | normal                                                                                 | Es werden nur technische Parameter aufgenommen.                                                                                 |
| P3, P4                                                                                 | sehr hoch                                                                              | Verarbeitung von Daten mit medizinischen Diagnosen oder zu vertraulichen Einsätzen anderer Institutionen (SZ1, SZ2, SZ5, SZ6).  |
| P5                                                                                     | hoch                                                                                   | Verarbeitung personenbezogener Daten (SZ1, SZ2, SZ5, SZ6).                                                                      |
| P6                                                                                     | normal                                                                                 | Bei Schulungen wird nicht mit produktiven Daten gearbeitet.                                                                     |

Für die Prozesse der Stammdatenpflege ist der Schutzbedarf als hoch einzustufen. Es werden keine Daten mit medizinischen   Diagnosen   verarbeitet,   allerdings   müssen   vertrauliche   Informationen gewerblicher und öffentlicher Einrichtungen sowie Kontaktdaten von Amts- und Funktionsträgern in die Anwendungen der Rettungsleitstelle eingetragen werden.

Bei Schulungen wird in der Regel mit simulierten Daten gearbeitet, so dass für den Prozess P6 ein normaler Schutzbedarf ausreichend ist. Dies gilt auch für Dienstbesprechungen, in denen üblicherweise organisatorische Themen behandelt werden. Tabelle 18 fasst den Schutzbedarf der Vertraulichkeit für die verschiedenen Prozesse zusammen.

<!-- page: 45 -->

## 3.5.1.2 Schutzbedarfsfeststellung der Integrität für Prozesse

Hinsichtlich der Integrität der verarbeiteten Daten in einer Leitstelle wird von einem erhöhtem Schutzbedarf ausgegangen. Werden zum Beispiel fehlerhafte Daten zum Einsatzort aufgenommen (P1, P2) und die Rettungsmittel erreichen deshalb den Einsatzort verspätet oder gar nicht, kann dies für   Hilfesuchende lebensbedrohliche Konsequenzen haben (SZ3). Die Leitstelle verstößt in so einem Fall auch gegen Gesetze (SZ1), weil sie ihrer Aufgabenerfüllung nicht nachkommt (SZ4). Daraus   können   sich   eine   negative   Außenwirkung   (SZ5)   und   Schadensersatzzahlungen   (SZ6) ergeben. Dabei ist es unerheblich, auf welchem Weg die Meldung die Rettungsleitstelle erreicht.

Tabelle 19: Schutzbedarf der Integrität für Prozesse.

| Schutzbedarfsfeststellung der Integrität für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Integrität für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Integrität für Prozesse des Informationsverbundes                                      |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Objekt                                                                            | Schutzbedarf                                                                      | Begründung                                                                                                           |
| P1, P2, P3, P5                                                                    | sehr hoch                                                                         | Lebensbedrohliche Folgen bei Verarbeitung inkorrekter Daten oder feh- lerhaftem Verhalten (SZ1, SZ3, SZ4, SZ5, SZ6). |
| P4, P6                                                                            | normal                                                                            | Geringe Auswirkungen bei Verarbeitung inkorrekter Daten oder fehler- haftem Verhalten (SZ1, SZ6).                    |

Der gleiche Schutzbedarf gilt für die Einsatzbearbeitung (P3) und die Stammdatenpflege (P5). Für den Einsatzabschluss (P4) sind die Auswirkungen einer Beeinträchtigung der Integrität der verarbeiteten Informationen geringer. Der mögliche Schaden betrifft Verstöße gegen Verträge mit den angebundenen Organisationen (SZ1) und finanzielle Auswirkungen (SZ6). Auch bei Schulungen und Besprechungen (P6) sind die Konsequenzen begrenzt. Der Schutzbedarf wird daher für die Prozesse P4 und P6 auf normal festgelegt. In Tabelle 19 ist der Schutzbedarf für die Integrität der Prozesse zusammengefasst.

## 3.5.1.3 Schutzbedarfsfeststellung der Verfügbarkeit für Prozesse

Die   Rettungsleitstelle   muss   jederzeit   erreichbar   sein.  Ausfallzeiten   können   für   Hilfesuchende lebensbedrohliche Folgen haben. Entsprechend hoch ist der Schutzbedarf für die Verfügbarkeit der Systeme der Rettungsleitstelle in  Tabelle 20 zu bewerten.

Die Meldungen erreichen die Rettungsleitstelle meistens über den telefonischen Notruf 112 (P1.1). Sofern der Hilfesuchende, zum Beispiel aufgrund einer Sprachstörung, nicht in der Lage ist, einen Notruf telefonisch abzusetzen, ist er auf eine Erreichbarkeit der Rettungsleitstelle über Fax angewiesen (P1.2). Beide Kommunikationswege setzen daher einen sehr hohen Schutzbedarf für die Verfügbarkeit voraus. Gleiches gilt für die Alarmempfangseinrichtung für Brandmeldeanlagen in der Rettungsleitstelle. Ein Feuer kann großen Schaden anrichten, wenn es nicht bemerkt wird (P1.6). Auch der Empfang von Notfallmeldungen über den automatischen Fahrzeugnotruf eCall setzt eine ständige Verfügbarkeit der dafür verwendeten Systeme in der Leitstelle voraus (P1.7). Andernfalls könnte ein Verkehrsunfall unbemerkt bleiben, was für die Fahrzeuginsassen lebensbedrohliche Konsequenzen nach sich ziehen kann.

<!-- page: 46 -->

Ausfälle beim Empfang von E-Mails haben dagegen geringe Auswirkungen, weil über diesen Kommunikationsweg normalerweise keine zeitkritischen Notfallmeldungen empfangen werden (P1.3). Fällt das Funknetz aus und können keine Notfallmeldungen an die Leitstelle übermittelt werden (P1.4), so hat dies ebenfalls nur geringe Auswirkungen, weil alternative Kommunikationswege, wie zum Beispiel das Mobiltelefon, möglich sind.

Tabelle 20: Schutzbedarf der Verfügbarkeit für Prozesse.

| Schutzbedarfsfeststellung der Verfügbarkeit für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Verfügbarkeit für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Verfügbarkeit für Prozesse des Informationsverbundes                               |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Objekt                                                                               | Schutzbedarf                                                                         | Begründung                                                                                                       |
| P1.1, P1.2                                                                           | sehr hoch                                                                            | Lebensbedrohliche Folgen bei Ausfall des Notrufs 112 über Telefon oder Fax (SZ1, SZ3, SZ4, SZ5, SZ6).            |
| P1.3                                                                                 | normal                                                                               | Geringe Auswirkungen, weil über E-Mail keine Notfallmeldungen einge- hen (SZ4, SZ5).                             |
| P1.4                                                                                 | normal                                                                               | Von den Rettungskräften können alternative Kommunikationswege zur Leitstelle genutzt werden (SZ4, SZ5).          |
| P1.5                                                                                 | sehr hoch                                                                            | Die Auswirkungen eines Ausfalls steigen durch Einführung der bundes- weiten Notrufapp (SZ1, SZ3, SZ4, SZ5, SZ6). |
| P1.6                                                                                 | sehr hoch                                                                            | Hoher materieller Schaden bei Ausfall der Alarmempfangseinrichtung (SZ1, SZ3, SZ4, SZ5, SZ6).                    |
| P1.7                                                                                 | sehr hoch                                                                            | Lebensbedrohliche Folgen bei Ausfall der Empfangseinrichtung für eCalls (SZ1, SZ3, SZ4, SZ5, SZ6).               |
| P2, P3                                                                               | sehr hoch                                                                            | Lebensbedrohliche Folgen bei Beeinträchtigungen von Einsatzaufnahme oder -bearbeitung (SZ1, SZ3, SZ4, SZ5, SZ6). |
| P4, P5, P6                                                                           | normal                                                                               | Geringe Auswirkungen, weil die Prozesse nicht zeitkritisch sind (SZ4, SZ6).                                      |

Findet ein Austausch von Einsatzdaten mit anderen Leitstellen mangels Verfügbarkeit der Internetverbindung nicht mehr statt, können auch hier Alternativen, zum Beispiel Funk oder Telefon, genutzt werden. Dagegen steigt mit Einführung der bundesweiten Notrufapp der Schutzbedarf für P1.5,   weil   der   Empfang   von   Notfallmeldungen   der   App   eine   Internetverbindung   zwingend erforderlich macht.

Für die Prozesse der Einsatzaufnahme (P2) und der Einsatzbearbeitung (P3) wird der Schutzbedarf als sehr hoch eingestuft. Analog zu den Prozessen des Meldungseingangs kann es zu lebensbedrohlichen Konsequenzen für Hilfesuchende kommen, wenn diese Prozesse mangels Verfügbarkeit der Hilfsmittel nicht auf geeignete Weise durchgeführt werden können.

Ein Ausfall der Prozesse des Einsatzabschlusses (P4) hat dagegen nur geringe Auswirkungen, weil er keinen Einfluss auf die Gesundheit von Personen oder die Höhe eines Sachschadens hat. Diese Prozesse sind nicht zeitkritisch und können nachgeholt werden, sobald die Verfügbarkeit wieder hergestellt ist. Gleiches gilt in der Regel für die Stammdatenpflege (P5) sowie für Schulungen und Besprechungen (P6).

<!-- page: 47 -->

## 3.5.2 Schutzbedarfsfeststellung für Anwendungen

Die Schutzbedarfsfeststellung für Anwendungen richtet sind nach dem Schutzbedarf der Prozesse, die durch die Verwendung der jeweiligen Anwendung unterstützt werden. Dabei wird das Maximumprinzip berücksichtigt und der jeweils höchste Schutzbedarf durch die Anwendung geerbt. Ist der Schutzbedarf für einen Teil, der von den Anwendungen unterstützten Prozesse, als sehr hoch eingestuft, so ist der Schutzbedarf der gesamten Anwendung als sehr hoch einzustufen.

## 3.5.2.1 Schutzbedarfsfeststellung der Vertraulichkeit für Anwendungen

Der Schutzbedarf für die Vertraulichkeit von ELS (A1), KMS (A2), Webbrowser (A3), PDF-Viewer (A6) und freigegebene Netzlaufwerke (A8) muss als sehr hoch eingestuft werden, weil Prozesse mit diesen Anwendungen bearbeitet werden, für die in 3.5.1.1 ein sehr hoher Schutzbedarf festgelegt wurde.

Tabelle 21: Schutzbedarf der Vertraulichkeit für Anwendungen.

| Schutzbedarfsfeststellung der Vertraulichkeit für Anwendungen   | Schutzbedarfsfeststellung der Vertraulichkeit für Anwendungen   | Schutzbedarfsfeststellung der Vertraulichkeit für Anwendungen      |
|-----------------------------------------------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------|
| Objekt                                                          | Schutzbedarf                                                    | Begründung                                                         |
| A1                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozesse P2.1, P3 und P4.              |
| A2                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozesse P1.1, P1.4 und P3.            |
| A3                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozesse P1.5 und P3.                  |
| A4                                                              | hoch                                                            | Hoher Schutzbedarf für Prozess P5.1.                               |
| A5                                                              | normal                                                          | Keine Verarbeitung personenbezogener Daten, daher keine Vererbung. |
| A6                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozesse P2.1 und P3.                  |
| A7                                                              | hoch                                                            | Hoher Schutzbedarf für Prozess P5.1.                               |
| A8                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozess P4.                            |

Gefahrstoffinformationssysteme (A5) werden für Prozesse verwendet, die einen sehr hohen Schutzbedarf der Vertraulichkeit haben. Da in den Prozessen aber keine vertraulichen Informationen an A5 übergeben werden und in A5 keine personenbezogenen Daten verarbeitet werden, wird von der Vererbung des Schutzbedarfs abgewichen. Dieser wird für A5 auf normal festgelegt. Für E-Mailclient (A4) und Office-Anwendungen besteht jeweils ein hoher Schutzbedarf, weil die damit unterstützten Prozesse einen hohen Schutzbedarf haben. Tabelle 21 fasst den Schutzbedarf der Vertraulichkeit für Anwendungen zusammen.

<!-- page: 48 -->

## 3.5.2.2 Schutzbedarfsfeststellung der Integrität für Anwendungen

Alle Anwendungen in Tabelle 22 erfordern bezüglich ihrer Integrität einen sehr hohen Schutzbedarf, weil sie Prozesse unterstützen, für die ein sehr hoher Schutzbedarf der Integrität festgelegt wurde.

Tabelle 22: Schutzbedarf der Integrität für Anwendungen.

| Schutzbedarfsfeststellung der Integrität für Anwendungen   | Schutzbedarfsfeststellung der Integrität für Anwendungen   | Schutzbedarfsfeststellung der Integrität für Anwendungen            |
|------------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------------------|
| Objekt                                                     | Schutzbedarf                                               | Begründung                                                          |
| A1                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P1.6, P1.7, P2, P3 und P5.2.   |
| A2                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P1.1, P1.4, P1.7, P3 und P5.2. |
| A3                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P1.5, P3 und P5.               |
| A4                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P1.3 und P5.1.                 |
| A5                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P2.1 und P3.                   |
| A6                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P2.1, P3 und P5.               |
| A7                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozess P5.1.                           |
| A8                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozess P5.                             |

## 3.5.2.3 Schutzbedarfsfeststellung der Verfügbarkeit für Anwendungen

Sind ELS (A1) oder KMS (A2) nicht verfügbar, müssen die Prozesse des Meldungseingangs (P1), der   Einsatzaufnahme   (P2)   und   -bearbeitung   (P3)   ohne   technische   Unterstützung   durchgeführt werden. In den Leitstellen können für diesen Fall zum Beispiel einfache Telefone verwendet werden, um Notrufe entgegenzunehmen. Bei hohem Einsatzaufkommen stellt dies Rettungsleitstellen vor hohe Herausforderungen. Der Betrieb wird stark eingeschränkt.

Gefahrstoffinformationssystem (A5) und PDF-Viewer (A6) werden für die Einsatzaufnahme und Einsatzbearbeitung benötigt. Diese Prozesse sind mit einem sehr hohen Schutzbedarf der Verfügbarkeit definiert. Daraus ergibt sich ein sehr hoher Schutzbedarf für A5 und A6. Ein Ausfall von Webbrowser (A3), E-Mailclient (A4), Office-Anwendungen (A7) und Dateiablage (A8) hätte dagegen nur geringe Auswirkungen. Sollte der Standard-Webbrowser ausfallen, lässt sich leicht ein alternativer Browser nutzen. Da E-Mails nicht zeitkritisch sind, können alternative Kommunikationswege verwendet werden. Tabelle 23 fasst den Schutzbedarf der Verfügbarkeiten für die Anwendungen der Rettungsleitstelle zusammen.

<!-- page: 49 -->

Tabelle 23: Schutzbedarf der Verfügbarkeit für Anwendungen.

| Schutzbedarfsfeststellung der Verfügbarkeit für Anwendungen   | Schutzbedarfsfeststellung der Verfügbarkeit für Anwendungen   | Schutzbedarfsfeststellung der Verfügbarkeit für Anwendungen   |
|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Objekt                                                        | Schutzbedarf                                                  | Begründung                                                    |
| A1                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P1.6, P1.7, P2 und P3.   |
| A2                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P1.1, P1.7 und P3.       |
| A3                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P1.5 und P3.             |
| A4                                                            | normal                                                        | Normaler Schutzbedarf für Prozesse P1.3 und P5.1.             |
| A5                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P2.1 und P3.             |
| A6                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P2.1 und P3.             |
| A7                                                            | normal                                                        | Normaler Schutzbedarf für Prozess P5.1.                       |
| A8                                                            | normal                                                        | Normaler Schutzbedarf für Prozesse P5 und P5.                 |

## 3.5.3 Schutzbedarfsfeststellung für IT-Systeme

Der Schutzbedarf für die IT-Systeme einer Rettungsleitstelle richtet sich nach den Anwendungen, die auf den IT-Systemen installiert oder mit diesen verbunden sind. Nach dem Maximumprinzip muss der Schutzbedarf wieder mindestens so hoch angesetzt werden, wie für diese Anwendungen.

## 3.5.3.1 Schutzbedarfsfeststellung der Vertraulichkeit für IT-Systeme

Für ELS (A1), KMS (A2), Webbrowser (A3), Gefahrstoffinformationssysteme (A5), PDF-Viewer (A6) und Netzwerkfreigaben (A8) wurde in 3.5.2.1 ein sehr hoher Schutzbedarf der Vertraulichkeit definiert. Folglich müssen auch die Betriebssysteme für Clients und Server (S1), auf denen die Anwendungen installiert sind, mit einem sehr hohen Schutzbedarf versehen werden. Gleiches gilt für die Hardware der Server (S2.1), Virtualisierungsplattformen (S2.2) und Arbeitsplatz-Clients (S3).

Tabelle 24: Schutzbedarf der Vertraulichkeit für IT-Systeme.

| Schutzbedarfsfeststellung der Vertraulichkeit für IT-Systeme   | Schutzbedarfsfeststellung der Vertraulichkeit für IT-Systeme   | Schutzbedarfsfeststellung der Vertraulichkeit für IT-Systeme   |
|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Objekt                                                         | Schutzbedarf                                                   | Begründung                                                     |
| S1.1                                                           | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A2, A3, A5, A6, A8             |
| S1.2                                                           | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A2                             |
| S2                                                             | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A2                             |
| S3                                                             | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A2, A3, A5, A6, A8             |
| S4                                                             | sehr hoch                                                      | Sehr hoher Schutzbedarf für P1.2                               |
| S5                                                             | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A6                             |

Werden in der Rettungsleitstelle Nachrichten per Telefax empfangen (P1.2), ausgedruckt oder eingescannt, so können auch hier personenbezogene Daten mit medizinischen Diagnosen verarbeitet werden. Entsprechend muss der Schutzbedarf für die Faxgeräte (S4), Drucker und Multifunktionsgeräte (S5) als sehr hoch eingestuft werden. Tabelle 24 fasst den Schutzbedarf der Vertraulichkeit für IT-Systeme zusammen.

<!-- page: 50 -->

## 3.5.3.2 Schutzbedarfsfeststellung der Integrität für IT-Systeme

In 3.5.2.2 wurde ein sehr hoher Schutzbedarf hinsichtlich der Integrität für alle Anwendungen in der Rettungsleitstelle festgestellt. Dies macht für die in Tabelle 25 aufgeführten IT-Systeme ebenfalls einen sehr hohen Schutzbedarf der Integrität erforderlich.

Tabelle 25: Schutzbedarf der Integrität für IT-Systeme.

| Schutzbedarfsfeststellung der Integrität für IT-Systeme   | Schutzbedarfsfeststellung der Integrität für IT-Systeme   | Schutzbedarfsfeststellung der Integrität für IT-Systeme    |
|-----------------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------|
| Objekt                                                    | Schutzbedarf                                              | Begründung                                                 |
| S1.1                                                      | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A2, A3, A4, A5, A6, A7, A8 |
| S1.2                                                      | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A2                         |
| S2                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A2                         |
| S3                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A2, A3, A4, A5, A6, A7, A8 |
| S4                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für P1.2                           |
| S5                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A6, A7                     |

## 3.5.3.3 Schutzbedarfsfeststellung der Verfügbarkeit für IT-Systeme

Der   Schutzbedarf   der   Verfügbarkeit   für   ELS   (A1),   KMS   (A2),   Webbrowser   (A3), Gefahrstoffinformationssysteme (A5), PDF-Viewer und das Empfangen von Notfallmeldungen über Fax (P1.2) wurde als sehr hoch eingestuft. Als Konsequenz ergibt sich für alle IT-Systeme ebenso ein sehr hoher Schutzbedarf. In Tabelle 26 ist der Schutzbedarf der Verfügbarkeit für IT-Systeme aufgeführt.

Tabelle 26: Schutzbedarf der Verfügbarkeit für IT-Systeme.

| Schutzbedarfsfeststellung der Verfügbarkeit für IT-Systeme   | Schutzbedarfsfeststellung der Verfügbarkeit für IT-Systeme   | Schutzbedarfsfeststellung der Verfügbarkeit für IT-Systeme   |
|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Objekt                                                       | Schutzbedarf                                                 | Begründung                                                   |
| S1.1                                                         | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A2, A3, A5, A6               |
| S1.2                                                         | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A2                           |
| S2                                                           | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A2                           |
| S3                                                           | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A2, A3, A5, A6               |
| S4                                                           | sehr hoch                                                    | Sehr hoher Schutzbedarf für P1.2                             |
| S5                                                           | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A6                           |

## 3.5.4 Schutzbedarfsfeststellung für Netzwerke

Viele Anwendungen und IT-Systeme, die in der Rettungsleitstelle verwendet werden, übermitteln und empfangen Daten über die in Abschnitt  3.4.4  definierten Netze und Netzkomponenten. Der Schutzbedarf   der   Netze   und   Netzkomponenten   ist   somit   abhängig   vom   Schutzbedarf   der Anwendungen und IT-Systeme, die mit diesen Netzen verbunden sind.

<!-- page: 51 -->

## 3.5.4.1 Schutzbedarfsfeststellung der Vertraulichkeit für Netzwerke

Die Netzwerke N1, N2, N3 und N4 werden von ELS (A1), KMS (A2) und Webbrowser (A3) benötigt. Für diese Anwendungen wurde in 3.5.2.1 ein sehr hoher Schutzbedarf der Vertraulichkeit festgelegt. Die Netzkomponenten aus den Kategorien N5 und N6 werden wiederum zum Betrieb der Netzwerke N1, N2 und N3 benötigt. Das Alarmierungsnetz (N7) überträgt Informationen aus dem ELS (A1) mit sehr hohem Schutzbedarf. Aufgrund dieser Abhängigkeiten muss der Schutzbedarf für alle Netze und Netzkomponenten in Tabelle 27 als sehr hoch festgelegt werden.

Tabelle 27: Schutzbedarf der Vertraulichkeit für Netzwerke.

| Schutzbedarfsfeststellung der Vertraulichkeit für Netzwerke   | Schutzbedarfsfeststellung der Vertraulichkeit für Netzwerke   | Schutzbedarfsfeststellung der Vertraulichkeit für Netzwerke   |
|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Objekt                                                        | Schutzbedarf                                                  | Begründung                                                    |
| N1                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A1                                |
| N2                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A2                                |
| N3                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A3, A5, A6, A8                    |
| N4                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A1, A2, A3, A4                    |
| N5                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für N1, N2 und N3                     |
| N6                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für N1, N2 und N3                     |
| N7                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A1                                |

## 3.5.4.2 Schutzbedarfsfeststellung der Integrität für Netzwerke

Ein fehlerhaftes Verhalten der Netzkomponenten oder die inkorrekte Übertragung von Daten in den Netzen kann den Betrieb der Anwendungen negativ beeinflussen. Da für diese ein sehr hoher Schutzbedarf   der   Integrität   gilt,   wird   der   Schutzbedarf   für   Netze   und   die   dafür   benötigten Komponenten in Tabelle 28 ebenfalls als sehr hoch eingestuft.

| Schutzbedarfsfeststellung der Integrität für Netzwerke   | Schutzbedarfsfeststellung der Integrität für Netzwerke   | Schutzbedarfsfeststellung der Integrität für Netzwerke   |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Objekt                                                   | Schutzbedarf                                             | Begründung                                               |
| N1                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A1                           |
| N2                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A2                           |
| N3                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A3, A5, A6, A7, A8           |
| N4                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A1, A2, A3                   |
| N5                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für N1, N2 und N3                |
| N6                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für N1, N2 und N3                |
| N7                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A1                           |

<!-- page: 52 -->

Tabelle 28: Schutzbedarf der Integrität für Netzwerke.

## 3.5.4.3 Schutzbedarfsfeststellung der Verfügbarkeit für Netzwerke

Da ELS und KMS auf einer Client-Server-Architektur basieren, ist ein funktionierendes Netzwerk für deren Betrieb erforderlich. Sind die Netzwerke nicht verfügbar, entspricht dies einem Ausfall der Anwendungen. Gleiches gilt auch für das Büro-Netz (N3), für die Verbindung zum ISP und für das Alarmierungsnetz (N7). Die von diesen Netzen abhängigen Anwendungen haben alle einen sehr hohen Schutzbedarf der Verfügbarkeit. Dementsprechend  ist der Schutzbedarf für alle Netze und Netzkomponenten in Tabelle 29 als sehr hoch einzustufen.

Tabelle 29: Schutzbedarf der Verfügbarkeit für Netzwerke.

| Schutzbedarfsfeststellung der Verfügbarkeit für Netzwerke   | Schutzbedarfsfeststellung der Verfügbarkeit für Netzwerke   | Schutzbedarfsfeststellung der Verfügbarkeit für Netzwerke   |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| Objekt                                                      | Schutzbedarf                                                | Begründung                                                  |
| N1                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A1                              |
| N2                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A2                              |
| N3                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A3, A5, A6                      |
| N4                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A1, A2, A3                      |
| N5                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für N1, N2 und N3                   |
| N6                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für N1, N2 und N3                   |
| N7                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A1                              |

## 3.5.5 Schutzbedarfsfeststellung für Räume

Die Schutzbedarfsfeststellung für Räume richtet sich nach den IT-Systemen, die in dem betrachteten Raum installiert sind und den Prozessen, die dort durchgeführt werden. Je höher deren Schutzbedarf ist, desto höher ist auch der Schutzbedarf für den Raum einzustufen. Dabei ist auch die Anzahl der Systeme zu berücksichtigen, die in dem Raum installiert sind.

## 3.5.5.1 Schutzbedarfsfeststellung der Vertraulichkeit für Räume

Im Dispositionsraum (R1) und den Büroräumen (R3) der Rettungsleitstelle (R1) werden Prozesse mit sehr hohem Schutzbedarf der Vertraulichkeit durchgeführt. Zudem befinden sich in diesen Räumen Arbeitsplatz-Clients (S3), Faxgeräte (S4) und Drucker (S5), die ebenfalls einen sehr hohen Schutzbedarf benötigen. Im Archivraum (R5) werden vertrauliche Datenträger gelagert. Aus diesen Gründen ist der Schutzbedarf der Räume in  Tabelle 30  als sehr hoch einzustufen. Auch für den Technikraum der Leitstelle (R2) und den Raum für Telekommunikationsanschlüsse (R4) gilt ein sehr hoher Schutzbedarf. Dieser leitet sich von den dort installierten IT-Systemen (S2) und Netzen (N2) ab. Der Schutzbedarf für den Besprechungs- und Schulungsraum ist dagegen normal.

<!-- page: 53 -->

Tabelle 30: Schutzbedarf der Vertraulichkeit für Räume.

| Schutzbedarfsfeststellung der Vertraulichkeit für Räume   | Schutzbedarfsfeststellung der Vertraulichkeit für Räume   | Schutzbedarfsfeststellung der Vertraulichkeit für Räume   |
|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Objekt                                                    | Schutzbedarf                                              | Begründung                                                |
| R1                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für P1, P2, P3, S3, S4, S5        |
| R2                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für S2                            |
| R3                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für S3, S4, S5 und P5             |
| R4                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für N2                            |
| R5                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für P4                            |
| R6                                                        | normal                                                    | Normaler Schutzbedarf für P6                              |

## 3.5.5.2 Schutzbedarfsfeststellung der Integrität für Räume

Durch Zugriff auf Anwendungen und IT-Systeme der Rettungsleitstelle können Unbefugte Informationen manipulieren. Kommt es infolgedessen zu fehlerhaftem Verhalten der Anwendungen, sind für Hilfesuchende lebensbedrohliche Konsequenzen möglich. Zum Beispiel kann dem Disponenten im ELS nicht das nächste geeignete Rettungsmittel vorgeschlagen werden, sondern ein Fahrzeug, das eine deutlich längere Anfahrt zum Einsatzort hat.

In den Räumen der Rettungsleitstelle werden Systeme betrieben, bei denen eine Manipulation von Informationen möglich ist. Der Schutzbedarf der Integrität für diese Systeme wurde in 3.5.3.2 als sehr hoch eingestuft. Daraus resultiert in Tabelle 31 ein sehr hoher Schutzbedarf für die betrachteten Räume. Lediglich im Archiv- sowie im Besprechungs- und Schulungsraum kann der Schutzbedarf auf normal festgelegt werden.

Tabelle 31: Schutzbedarf der Integrität für Räume.

| Schutzbedarfsfeststellung der Integrität für Räume   | Schutzbedarfsfeststellung der Integrität für Räume   | Schutzbedarfsfeststellung der Integrität für Räume   |
|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| Objekt                                               | Schutzbedarf                                         | Begründung                                           |
| R1                                                   | sehr hoch                                            | Sehr hoher Schutzbedarf für S3, S4, S5               |
| R2                                                   | sehr hoch                                            | Sehr hoher Schutzbedarf für S2                       |
| R3                                                   | sehr hoch                                            | Sehr hoher Schutzbedarf für S3, S4, S5               |
| R4                                                   | sehr hoch                                            | Sehr hoher Schutzbedarf für N2                       |
| R5                                                   | normal                                               | Normaler Schutzbedarf für P4                         |
| R6                                                   | normal                                               | Normaler Schutzbedarf für P6                         |

## 3.5.5.3 Schutzbedarfsfeststellung der Verfügbarkeit für Räume

Steht der Dispositionsraum einer Rettungsleitstelle (R1) nicht zur Verfügung, kann das Personal den Betrieb nur stark eingeschränkt in einem anderen Raum aufrechterhalten. Zwar sind für jede Leitstelle Ersatz-Notrufabfragestellen definiert, die bei einem Ausfall die Notrufe der ursprünglichen Leitstelle entgegennehmen können. 28 Bis diese aber eingerichtet und mit ausreichendem Personal besetzt sind, bleibt ein Zeitraum, in dem Notfallmeldungen nicht entgegengenommen werden können oder eine Disposition von Rettungsmitteln nicht erfolgen kann. Die Rolle der Ersatz-Notrufabfragestellen kann zum Beispiel von benachbarten Leitstellen übernommen werden. Einige Leitstellen halten auch eigene redundante Räume in anderen Gebäuden bereit. Beide Optionen bringen Herausforderungen mit sich. Die eigenen redundanten Räume sind nicht ständig mit Personal besetzt. Werden die Notrufe auf benachbarte Leitstellen umgeschaltet, so bedeutet das für diese Leitstelle ein erhöhtes Notrufaufkommen, weil auch die Notrufe aus dem eigenen Einzugsgebiet weiter entgegengenommen werden müssen. Beim Disponieren von Rettungsmitteln in einem Bereich, der nicht dem gewöhnlichen Einzugsgebiet der Leitstelle entspricht, sind außerdem lokale Besonderheiten zu berücksichtigen. Betroffen sind die Prozesse P1, P2 und P3, für die in 3.5.1.3 ein sehr hoher Schutzbedarf der Verfügbarkeit festgelegt wurde. Der Schutzbedarf für den Dispositionsraum (R1) muss daher ebenfalls als sehr hoch eingestuft werden. Auch für den Technikraum der Rettungsleitstelle (R2) ist angesichts der dort vorgehaltenen IT-Systeme (S2) ein Ausfall mit erheblichen Konsequenzen verbunden. Steht der Raum mit der entsprechenden Technik nicht zur Verfügung, muss der Betrieb ohne technische Unterstützung durchgeführt werden. Eine Alternative ist auch in diesem Szenario das Ausweichen in eine Ersatz-Notrufabfragestelle.

<!-- page: 54 -->

| Schutzbedarfsfeststellung der Verfügbarkeit für Räume   | Schutzbedarfsfeststellung der Verfügbarkeit für Räume   | Schutzbedarfsfeststellung der Verfügbarkeit für Räume   |
|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Objekt                                                  | Schutzbedarf                                            | Begründung                                              |
| R1                                                      | sehr hoch                                               | Sehr hoher Schutzbedarf für P1, P2 und P3               |
| R2                                                      | sehr hoch                                               | Sehr hoher Schutzbedarf für S2                          |
| R3                                                      | normal                                                  | Nutzung alternativer Räume möglich                      |
| R4                                                      | sehr hoch                                               | Sehr hoher Schutzbedarf für N4                          |
| R5                                                      | normal                                                  | Normaler Schutzbedarf für P4                            |
| R6                                                      | normal                                                  | Normaler Schutzbedarf für P6                            |

## Tabelle 32: Schutzbedarf der Verfügbarkeit für Räume.

Der Schutzbedarf wird daher für den Technikraum auf sehr hoch festgelegt. Der Schutzbedarf des Raums für Telekommunikationsanschlüsse (R4) wird ebenfalls auf sehr hoch festgelegt. Ist dieser Raum nicht verfügbar, muss mit Beeinträchtigungen der Kommunikationsverbindungen (N4) gerechnet werden.

28 Siehe §3 Abs. 1 NotrufV: https://www.gesetze-im-internet.de/notrufv/BJNR048100009.html (abgerufen am 25.08.2019)

<!-- page: 55 -->

Für Büro- (R3), Archiv- (R5) sowie Besprechungs- und Schulungsräume gilt dagegen ein normaler Schutzbedarf. Für die in diesen Räumen durchgeführten Prozesse können, ohne erhebliche Konsequenzen, alternative Räume genutzt werden. Tabelle 32 listet die definierten Schutzbedarfe auf.

## 3.6 Zu erfüllende Anforderungen und umzusetzende Maßnahmen

Das IT-Grundschutz-Kompendium des BSI stellt Bausteine bereit, die anwendungsbezogene Empfehlungen zur Umsetzung des IT-Grundschutzes geben. Nachdem im letzten Abschnitt der Schutzbedarf festgestellt wurde, werden im nächsten Schritt die relevanten Bausteine identifiziert und eine Anpassung der Anforderungen an die entsprechende Zielgruppe durchgeführt. Ebenso können Anforderungen in einer Rettungsleitstelle als irrelevant eingestuft werden. Zusätzlich folgen Vorgaben zur Umsetzung der Anforderungen der Bausteine.

## 3.6.1 Auswahl relevanter Bausteine

Im IT-Grundschutz-Kompendium sind im Jahr 2019 insgesamt 94 Bausteine veröffentlicht. 29 In den Tabellen des Abschnitts 5.2 im Anhang A wird jeder Baustein aufgelistet und auf Relevanz überprüft. Sofern ein Baustein nicht relevant ist, wird dies begründet. Dabei kommt das Mindestprinzip zur Anwendung: Es werden nur diejenigen Bausteine modelliert, die für eine Mehrheit der Leitstellen bedeutend sind. Diese Vorgehensweise fokussiert das IT-Grundschutz-Profil auf die wesentlichen   und   wiederverwendbaren   Aspekte.   Dies   vereinfacht   die   spätere   Umsetzung   für   die Leitstellen. Unabhängig davon, muss von den Leitstellen untersucht werden, inwiefern der eigene Informationsverbund vom Profil abweicht. Gegebenenfalls sind bei der späteren Umsetzung weitere Bausteine als relevant einzustufen. Die Bausteine aus der Rubrik Industrielle IT werden mangels Relevanz für den Betrieb von Rettungsleitstellen von vornherein nicht aufgeführt. Tabelle A-28 im Anhang A beinhaltet die Prozessbausteine. Diese behandeln ganzheitliche Anfordeentscheidend, ob der Baustein für eine spezifische, in Abschnitt  3.4  bestimmte, Komponente re-

rungen und gelten für sämtliche Teile des Informationsverbundes. Dagegen führt Tabelle A-29 die Systembausteine auf. Systembausteine behandeln die Facetten bestimmter Komponenten. Hier ist levant ist.

## 3.6.2 Anforderungen der Bausteine

Nachdem die Bausteine bezüglich der Informationssicherheit in Rettungsleitstellen auf Relevanz untersucht wurden, werden im nächsten Schritt die Anforderungen der relevanten Bausteine geprüft. Sofern notwendig werden sie an die Rahmenbedingungen in Rettungsleitstellen angepasst. Die Bausteine sind in Anhang A im Abschnitt 5.3 tabellarisch dargestellt. Aufgeführt sind Basis- und

29

[https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/IT_Grundschutz_Kompendium_Edition2019.pdf)

[IT\_Grundschutz\_Kompendium\_Edition2019.pdf (abgerufen am 22.09.2019).](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/IT_Grundschutz_Kompendium_Edition2019.pdf)

<!-- page: 56 -->

Standard-Anforderungen. Sind bei einzelnen Bausteinen auch die Anforderungen für erhöhten Schutzbedarf zu erfüllen, werden diese extra benannt.

## 3.7 Behandlung nicht hinreichend abgedeckter Zielobjekte

Es gibt Objekte, die mit den vorhandenen Bausteinen des IT-Grundschutzes nicht hinreichend modelliert werden können. Diese müssen gesondert betrachtet werden. Die Verbindung zum ISP (N4) hat bei allen drei Schutzzielen einen sehr hohen Schutzbedarf. Die Rettungsleitstelle hat aber keinen Einfluss auf das Sicherheitsniveau des ISP. Für das Alarmierungsnetz N7 existiert  derzeit   kein   Baustein,   der   die  Anforderungen   für   den Schutzbedarf dieser Komponente passend abbildet. Da für dieses Netz ein sehr hoher Schutzbedarf in allen drei Schutzzielen ermittelt wurde, müssen auch für N7 die Risiken gesondert betrachtet werden. Die aufgeführten Objekte werden in die Risikoanalyse in Kapitel 4 mit aufgenommen.

## 3.8 Restrisiko

Auch bei Umsetzung aller Anforderungen ist keine hundertprozentige Sicherheit zu erreichen. Dies muss sowohl den Anwendern des IT-Grundschutz-Profils, als auch den Entscheidungsträgern bewusst sein. Ein Restrisiko bleibt bestehen. Durch die Zusammenarbeit mit anderen Organisationen werden vertrauliche Informationen an Institutionen übertragen, auf deren Sicherheitsmanagement eine Leitstelle nur beschränkt Einfluss nehmen kann. Auch eigene Mitarbeiter können trotz Dienstanweisungen und Schulungen, absichtlich oder unbewusst, solche Informationen an Unbefugte weitergeben. Gezielte Angriffe auf die Informationstechnik einer Institution nehmen zu. Bekannt gewordene Sicherheitslücken in den Systemen werden immer schneller ausgenutzt. Eine rechtzeitige Behebung durch entsprechende Updates ist nicht immer möglich. Dies betrifft insbesondere Systeme, bei deren Entwicklung der Schwerpunkt nicht auf die Informationssicherheit gelegt wurde. Ein Restrisiko bleibt auch beim Bezug von Dienstleistungen Dritter. Zum Beispiel kann es trotz redundanter Internetanschlüsse zu Störungen an großen Netzknotenpunkten kommen, wodurch mehrere ISP betroffen sein können.

## 3.9 Notfallmanagement (BCM)

Auch auf einem hohen Sicherheitsniveau kann eine Beeinträchtigung der Betriebsbereitschaft der Rettungsleitstelle nicht ausgeschlossen werden. Aus diesem Grund müssen weitere Vorbereitungen getroffen werden, um auch bei einem Ausfall, der Aufgabenerfüllung einer Rettungsleitstelle nachkommen zu können.

<!-- page: 57 -->

| Initiierung                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| - Festlegung strategischer Zielsetzungen und Schaffung grundlegender organisatorischer Vor- aussetzungen.                                             | - Die Leitung der Rettungsleitstelle muss den Prozess zur Einführung eines Notfallmanage- ments initiieren.                                                                                                                                                                                                                                                                                          |
| Konzeption                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                      |
| - Ermittlung der kritischen Geschäftsprozesse und Ressourcen und deren Risiken. - Entwicklung von passenden Notfallvorsorge- konzepten                | - Aus den in Abschnitt 3.4 ermittelten Objekten müssen die kritischen Prozesse und Ressourcen herausgefiltert werden und deren maximal tolerierbare Ausfallzeit bestimmt werden. - Durchführung einer Risikoanalyse für die kriti- schen Prozesse und Ressourcen - Festlegen von Rückfallebenen für die Aufnah- me und Bearbeitung von Notfalleinsätzen - Definition einer Ersatznotrufabfragestelle |
| Umsetzung des Notfallvorsorgekonzepts                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                      |
| - Prioritäten bei der Umsetzung setzen - Bereitstellung von Ressourcen - Festlegung von Verantwortlichkeiten - Identifizierung begleitender Maßnahmen | - Kosten für Rückfallebenen für ELS und KMS schätzen - Auch bei Vorfällen außerhalb der Bürozeiten Verantwortlichkeiten festlegen                                                                                                                                                                                                                                                                    |
| Notfallbewältigung                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                      |
| - Reaktion und Handeln in Notfallhandbuch re- geln                                                                                                    | - Festhalten von Reaktionen auf Ausfälle von ELS und KMS in Notfallhandbuch                                                                                                                                                                                                                                                                                                                          |
| Tests und Übungen                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                      |
| - Testen der Konzepte                                                                                                                                 | - Durchführung von Übungen für Ausfall von ELS und KMS - Übungen zum Betrieb der Ersatznotrufabfrage- stelle                                                                                                                                                                                                                                                                                         |
| Aufrechterhaltung und kontinuierliche Verbesserung                                                                                                    | Aufrechterhaltung und kontinuierliche Verbesserung                                                                                                                                                                                                                                                                                                                                                   |
| - Regelmäßiges Überprüfen der Konzepte auf Wirksamkeit und Angemessenheit                                                                             | - Ergebnisse der Ausfallübungen auswerten                                                                                                                                                                                                                                                                                                                                                            |

Tabelle 33: Phasen des Notfallmanagement-Prozesses des BSI, bezogen auf Rettungsleitstellen Die Planung des Umgangs mit solchen unvorhersehbaren Situationen wird als Notfallmanagement oder mit dem englischen Begriff Business Continuity Management (BCM) bezeichnet [GaMa17] [KlSK11]. Ein standardisiertes Vorgehen zum BCM ist in DIN EN ISO 22301:2014 [DIN22301] spezifiziert.

Der Begriff des Notfalls ist im Zusammenhang mit BCM nicht zu verwechseln mit dem Notfalleinsatz, den die Rettungsleitstelle üblicherweise bearbeitet. Das BSI definiert einen Notfall als:

<!-- page: 58 -->

'Länger andauernder Ausfall von Prozessen oder Ressourcen mit hohem oder sehr hohem Schaden.' 30 Im Standard 100-4 beschreibt das BSI einen Notfallmanagement-Prozess [BSI08]. Dieser besteht aus fünf Phasen, die nach einer Initiierung kontinuierlich durchlaufen werden müssen: Konzeption, Umsetzung des Notfallvorsorgekonzepts, Notfallbewältigung, Tests und Übungen, Aufrechterhaltung und Verbesserung. In Tabelle 33 sind diese Phasen des Notfallmanagement-Prozesses dargestellt. Während in der linken Spalte allgemeine Erläuterungen zu den einzelnen Phasen aufgeführt sind, beinhaltet die rechte Spalte beispielhaft konkrete Hinweise auf den Anwendungsbereich einer Rettungsleitstelle.

30

[https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzSchulung/Webkurs1004/1\_Einfuehrung/](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzSchulung/Webkurs1004/1_Einfuehrung/4_Definitionen/Definitionen_node.html)

[4\_Definitionen/Definitionen\_node.html (abgerufen am 24.10.2019).](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzSchulung/Webkurs1004/1_Einfuehrung/4_Definitionen/Definitionen_node.html)

<!-- page: 59 -->

## 4 Risikoanalyse

Für Objekte, bei denen ein hoher oder sehr hoher Schutzbedarf festgestellt worden ist, sieht der ITGrundschutz nach der Modellierung mit den IT-Grundschutz-Bausteinen auch eine Risikoanalyse vor. Das BSI stellt hierzu im IT-Grundschutz-Kompendium eine Auflistung der elementaren Gefährdungen zur Verfügung. In der Risikoanalyse wird ermittelt, wie diese Gefährdungen auf die Objekte einwirken. Das Vorgehen bei einer Risikoanalyse wird im BSI-Standard 200-3 beschrieben [BSI17a].

Das Ergebnis der Schutzbedarfsfeststellung in Abschnitt 3.5 hat gezeigt, dass in der Rettungsleitstelle sehr viele Objekte einen hohen oder sehr hohen Schutzbedarf benötigen. Für diese Objekte ist daher eine Risikoanalyse durchzuführen. Aufgrund der hohen Anzahl wird die Risikoanalyse in dieser Arbeit beispielhaft nur für die Objekte durchgeführt, die in Abschnitt 3.6 nicht hinreichend mit Bausteinen modelliert werden konnten. Die zwei ausgewählten Objekte sind in Tabelle 34 aufgeführt. Beide haben einen sehr hohen Schutzbedarf für die Schutzziele Vertraulichkeit, Integrität und Verfügbarkeit.

Tabelle 34: Objekte, für die beispielhaft eine Risikoanalyse durchgeführt wird

| ID   | Objekte und Prozesse des Informationsverbunds   |
|------|-------------------------------------------------|
| N4   | Netz zum Internet Service Provider              |
| N7   | Alarmierungsnetz für Funkmeldeempfänger         |

## 4.1 Ermittlung elementarer Gefährdungen

In Tabelle 35 wird für jede Gefährdung ermittelt, inwieweit diese auf das betrachtete Objekt einwirkt. Die Gefährdung kann für das Objekt direkt, indirekt oder nicht relevant sein. In der zweiten Spalte sind die Grundwerte aufgeführt, die von der Gefährdung beeinträchtigt werden können. Zur besseren Unterscheidung werden Anfangsbuchstaben der englischen Übersetzung ( C onfidentiality, I ntegrity und A vailability) verwendet. Zu jeder Gefährdung wird die Relevanz kurz begründet.

|                                                                                                                                  | Grundwert                                                                                                                        | Relevanz                                                                                                                         | Relevanz                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Gefährdung                                                                                                                       |                                                                                                                                  | N4                                                                                                                               | N7                                                                                                                               |
| G 0.1 Feuer                                                                                                                      | A                                                                                                                                | indirekt                                                                                                                         | indirekt                                                                                                                         |
| Netzkomponenten können durch Brandschäden in der Funktion beeinträchtigt werden.                                                 | Netzkomponenten können durch Brandschäden in der Funktion beeinträchtigt werden.                                                 | Netzkomponenten können durch Brandschäden in der Funktion beeinträchtigt werden.                                                 | Netzkomponenten können durch Brandschäden in der Funktion beeinträchtigt werden.                                                 |
| G 0.2 Ungünstige klimatische Bedingungen                                                                                         | I, A                                                                                                                             | nein                                                                                                                             | nein                                                                                                                             |
| Die verwendeten Komponenten sind üblicherweise resistent gegen extreme Temperaturen oder befinden sich in klimatisierten Räumen. | Die verwendeten Komponenten sind üblicherweise resistent gegen extreme Temperaturen oder befinden sich in klimatisierten Räumen. | Die verwendeten Komponenten sind üblicherweise resistent gegen extreme Temperaturen oder befinden sich in klimatisierten Räumen. | Die verwendeten Komponenten sind üblicherweise resistent gegen extreme Temperaturen oder befinden sich in klimatisierten Räumen. |

<!-- page: 60 -->

| G 0.3 Wasser                                                                             | I, A                                                                                     | indirekt                                                                                 | indirekt                                                                                 |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Durch das Eindringen von Wasser in Netzkomponenten kann es zu Beeinträchtigungen kommen. | Durch das Eindringen von Wasser in Netzkomponenten kann es zu Beeinträchtigungen kommen. | Durch das Eindringen von Wasser in Netzkomponenten kann es zu Beeinträchtigungen kommen. | Durch das Eindringen von Wasser in Netzkomponenten kann es zu Beeinträchtigungen kommen. |
| G 0.4 Verschmutzung, Staub, Korrosion                                                    | I, A                                                                                     | indirekt                                                                                 | indirekt                                                                                 |
| Betrieb der Netzkomponenten kann durch übermäßige Verschmutzung beeinträchtigt werden.   | Betrieb der Netzkomponenten kann durch übermäßige Verschmutzung beeinträchtigt werden.   | Betrieb der Netzkomponenten kann durch übermäßige Verschmutzung beeinträchtigt werden.   | Betrieb der Netzkomponenten kann durch übermäßige Verschmutzung beeinträchtigt werden.   |
| G 0.5 Naturkatastrophen                                                                  | A                                                                                        | indirekt                                                                                 | indirekt                                                                                 |
| Netzkomponenten können durch Zerstörung beeinträchtigt werden.                           | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                           | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                           | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                           |
| G 0.6 Katastrophen im Umfeld                                                             | A                                                                                        | indirekt                                                                                 | indirekt                                                                                 |
| Netzkomponenten können durch Zerstörung beeinträchtigt werden.                           | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                           | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                           | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                           |
| G 0.7 Großereignisse im Umfeld                                                           | C, I, A                                                                                  | indirekt                                                                                 | indirekt                                                                                 |
| Hohe Netzauslastung bei N4 und durch Vielzahl an Alarmierungen auch bei N7.              | Hohe Netzauslastung bei N4 und durch Vielzahl an Alarmierungen auch bei N7.              | Hohe Netzauslastung bei N4 und durch Vielzahl an Alarmierungen auch bei N7.              | Hohe Netzauslastung bei N4 und durch Vielzahl an Alarmierungen auch bei N7.              |
| G 0.8 Ausfall oder Störung der Stromversorgung                                           | I, A                                                                                     | direkt                                                                                   | direkt                                                                                   |
| Ohne Strom können die Netzkomponenten ausfallen und somit das System.                    | Ohne Strom können die Netzkomponenten ausfallen und somit das System.                    | Ohne Strom können die Netzkomponenten ausfallen und somit das System.                    | Ohne Strom können die Netzkomponenten ausfallen und somit das System.                    |
| G 0.9 Ausfall oder Störung von Kommunikationsnetzen                                      | I, A                                                                                     | direkt                                                                                   | indirekt                                                                                 |
| Ausfall des ISP bei N4. Ausfall des Multi-Master-Betriebs bei N7.                        | Ausfall des ISP bei N4. Ausfall des Multi-Master-Betriebs bei N7.                        | Ausfall des ISP bei N4. Ausfall des Multi-Master-Betriebs bei N7.                        | Ausfall des ISP bei N4. Ausfall des Multi-Master-Betriebs bei N7.                        |
| G 0.10 Ausfall oder Störung von Versorgungsnetzen                                        | A                                                                                        | nein                                                                                     | nein                                                                                     |
| Keine Auswirkungen auf N4 oder N7.                                                       | Keine Auswirkungen auf N4 oder N7.                                                       | Keine Auswirkungen auf N4 oder N7.                                                       | Keine Auswirkungen auf N4 oder N7.                                                       |
| G 0.11 Ausfall oder Störung von Dienstleistern                                           | C, I, A                                                                                  | direkt                                                                                   | nein                                                                                     |
| N4: Ausfall des ISP                                                                      | N4: Ausfall des ISP                                                                      | N4: Ausfall des ISP                                                                      | N4: Ausfall des ISP                                                                      |
| G 0.12 Elektromagnetische Störstrahlung                                                  | I, A                                                                                     | nein                                                                                     | direkt                                                                                   |
| N4: Keine Auswirkungen, weil Verwendung abgeschirmter Kabel. N7: Direkte Auswirkung.     | N4: Keine Auswirkungen, weil Verwendung abgeschirmter Kabel. N7: Direkte Auswirkung.     | N4: Keine Auswirkungen, weil Verwendung abgeschirmter Kabel. N7: Direkte Auswirkung.     | N4: Keine Auswirkungen, weil Verwendung abgeschirmter Kabel. N7: Direkte Auswirkung.     |
| G 0.13 Abfangen kompromittierender Strahlung                                             | C                                                                                        | nein                                                                                     | nein                                                                                     |
| Keine Auswirkungen auf N4 oder N7.                                                       | Keine Auswirkungen auf N4 oder N7.                                                       | Keine Auswirkungen auf N4 oder N7.                                                       | Keine Auswirkungen auf N4 oder N7.                                                       |
| G 0.14 Ausspähen von Informationen (Spionage)                                            | C                                                                                        | indirekt                                                                                 | nein                                                                                     |
| N7: Keine Übertragung von Informationen, die zur Spionage geeignet sind                  | N7: Keine Übertragung von Informationen, die zur Spionage geeignet sind                  | N7: Keine Übertragung von Informationen, die zur Spionage geeignet sind                  | N7: Keine Übertragung von Informationen, die zur Spionage geeignet sind                  |
| G 0.15 Abhören                                                                           | C                                                                                        | direkt                                                                                   | direkt                                                                                   |
| Netzwerkverkehr kann abgehört werden.                                                    | Netzwerkverkehr kann abgehört werden.                                                    | Netzwerkverkehr kann abgehört werden.                                                    | Netzwerkverkehr kann abgehört werden.                                                    |
| G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten                               | C, A                                                                                     | nein                                                                                     | direkt                                                                                   |
| N7: Diebstahl von Netzkomponenten möglich, weil Betrieb an verteilten Standorten.        | N7: Diebstahl von Netzkomponenten möglich, weil Betrieb an verteilten Standorten.        | N7: Diebstahl von Netzkomponenten möglich, weil Betrieb an verteilten Standorten.        | N7: Diebstahl von Netzkomponenten möglich, weil Betrieb an verteilten Standorten.        |
| G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten                                 | C, A                                                                                     | nein                                                                                     | nein                                                                                     |
| Alle Komponenten sind stationär verbaut. Die Gefahr eines Verlusts besteht daher nicht.  | Alle Komponenten sind stationär verbaut. Die Gefahr eines Verlusts besteht daher nicht.  | Alle Komponenten sind stationär verbaut. Die Gefahr eines Verlusts besteht daher nicht.  | Alle Komponenten sind stationär verbaut. Die Gefahr eines Verlusts besteht daher nicht.  |
| G 0.18 Fehlplanung oder fehlende Anpassung                                               | C, I, A                                                                                  | direkt                                                                                   | direkt                                                                                   |

<!-- page: 61 -->

| Kapazitätsengpässe sind bei N4 und N7 möglich.                                                                                                               | Kapazitätsengpässe sind bei N4 und N7 möglich.                                                                                                               | Kapazitätsengpässe sind bei N4 und N7 möglich.                                                                                                               | Kapazitätsengpässe sind bei N4 und N7 möglich.                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.19 Offenlegung schützenswerter Informationen                                                                                                             | C                                                                                                                                                            | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Netzwerkverkehr kann abgehört werden.                                                                                                                        |                                                                                                                                                              |                                                                                                                                                              |                                                                                                                                                              |
| G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle                                                                                                | C, I, A                                                                                                                                                      | nein                                                                                                                                                         | nein                                                                                                                                                         |
| Durch Nutzung zuverlässiger und geprüfter Komponenten für N4 und N7 nicht relevant.                                                                          | Durch Nutzung zuverlässiger und geprüfter Komponenten für N4 und N7 nicht relevant.                                                                          | Durch Nutzung zuverlässiger und geprüfter Komponenten für N4 und N7 nicht relevant.                                                                          | Durch Nutzung zuverlässiger und geprüfter Komponenten für N4 und N7 nicht relevant.                                                                          |
| G 0.21 Manipulation von Hard- oder Software                                                                                                                  | C, I, A                                                                                                                                                      | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Netzkomponenten könnten manipuliert werden.                                                                                                                  | Netzkomponenten könnten manipuliert werden.                                                                                                                  | Netzkomponenten könnten manipuliert werden.                                                                                                                  | Netzkomponenten könnten manipuliert werden.                                                                                                                  |
| G 0.22 Manipulation von Informationen                                                                                                                        | I                                                                                                                                                            | direkt                                                                                                                                                       | nein                                                                                                                                                         |
| N4: Manipulation durch Einspielen von veränderten Informationen möglich. N7: Geschlossenes Netzwerk lässt kein Einspielen von Informationen durch Dritte zu. | N4: Manipulation durch Einspielen von veränderten Informationen möglich. N7: Geschlossenes Netzwerk lässt kein Einspielen von Informationen durch Dritte zu. | N4: Manipulation durch Einspielen von veränderten Informationen möglich. N7: Geschlossenes Netzwerk lässt kein Einspielen von Informationen durch Dritte zu. | N4: Manipulation durch Einspielen von veränderten Informationen möglich. N7: Geschlossenes Netzwerk lässt kein Einspielen von Informationen durch Dritte zu. |
| G 0.23 Unbefugtes Eindringen in IT-Systeme                                                                                                                   | C, I                                                                                                                                                         | direkt                                                                                                                                                       | nein                                                                                                                                                         |
| N7: Geschlossenes Netzwerk lässt kein unbefugtes Eindringen zu.                                                                                              | N7: Geschlossenes Netzwerk lässt kein unbefugtes Eindringen zu.                                                                                              | N7: Geschlossenes Netzwerk lässt kein unbefugtes Eindringen zu.                                                                                              | N7: Geschlossenes Netzwerk lässt kein unbefugtes Eindringen zu.                                                                                              |
| G 0.24 Zerstörung von Geräten oder Datenträgern                                                                                                              | A                                                                                                                                                            | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Beeinträchtigung von Netzkomponenten.                                                                                                                        | Beeinträchtigung von Netzkomponenten.                                                                                                                        | Beeinträchtigung von Netzkomponenten.                                                                                                                        | Beeinträchtigung von Netzkomponenten.                                                                                                                        |
| G 0.25 Ausfall von Geräten oder Systemen                                                                                                                     | A                                                                                                                                                            | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Beeinträchtigung von Netzkomponenten.                                                                                                                        | Beeinträchtigung von Netzkomponenten.                                                                                                                        | Beeinträchtigung von Netzkomponenten.                                                                                                                        | Beeinträchtigung von Netzkomponenten.                                                                                                                        |
| G 0.26 Fehlfunktion von Geräten oder Systemen                                                                                                                | C, I, A                                                                                                                                                      | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Beeinträchtigungen durch Fehlfunktionen am Router oder am DAG.                                                                                               | Beeinträchtigungen durch Fehlfunktionen am Router oder am DAG.                                                                                               | Beeinträchtigungen durch Fehlfunktionen am Router oder am DAG.                                                                                               | Beeinträchtigungen durch Fehlfunktionen am Router oder am DAG.                                                                                               |
| G 0.27 Ressourcenmangel                                                                                                                                      | A                                                                                                                                                            | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Kapazitätsengpässe in den Netzen.                                                                                                                            | Kapazitätsengpässe in den Netzen.                                                                                                                            | Kapazitätsengpässe in den Netzen.                                                                                                                            | Kapazitätsengpässe in den Netzen.                                                                                                                            |
| G 0.28 Software-Schwachstellen oder -Fehler                                                                                                                  | C, I, A                                                                                                                                                      | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Beeinträchtigungen der Netzkomponenten.                                                                                                                      | Beeinträchtigungen der Netzkomponenten.                                                                                                                      | Beeinträchtigungen der Netzkomponenten.                                                                                                                      | Beeinträchtigungen der Netzkomponenten.                                                                                                                      |
| G 0.29 Verstoß gegen Gesetze oder Regelungen                                                                                                                 | C, I, A                                                                                                                                                      | indirekt                                                                                                                                                     | indirekt                                                                                                                                                     |
| Missbrauch durch Schadprogramme im Router (N4). Datenschutzverstoß bei fehlender Verschlüsselung (N7).                                                       | Missbrauch durch Schadprogramme im Router (N4). Datenschutzverstoß bei fehlender Verschlüsselung (N7).                                                       | Missbrauch durch Schadprogramme im Router (N4). Datenschutzverstoß bei fehlender Verschlüsselung (N7).                                                       | Missbrauch durch Schadprogramme im Router (N4). Datenschutzverstoß bei fehlender Verschlüsselung (N7).                                                       |
| G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen                                                                                    | C, I, A                                                                                                                                                      | indirekt                                                                                                                                                     | indirekt                                                                                                                                                     |
| N4: Möglich durch physischen Zugriff auf Netzkomponenten.                                                                                                    | N4: Möglich durch physischen Zugriff auf Netzkomponenten.                                                                                                    | N4: Möglich durch physischen Zugriff auf Netzkomponenten.                                                                                                    | N4: Möglich durch physischen Zugriff auf Netzkomponenten.                                                                                                    |
| G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen                                                                                      | C, I, A                                                                                                                                                      | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Eine Fehlerhafte Administration von Router oder Netzkomponenten kann den Betrieb der Netze beeinträchtigen.                                                  | Eine Fehlerhafte Administration von Router oder Netzkomponenten kann den Betrieb der Netze beeinträchtigen.                                                  | Eine Fehlerhafte Administration von Router oder Netzkomponenten kann den Betrieb der Netze beeinträchtigen.                                                  | Eine Fehlerhafte Administration von Router oder Netzkomponenten kann den Betrieb der Netze beeinträchtigen.                                                  |
| G 0.32 Missbrauch von Berechtigungen                                                                                                                         | C, I, A                                                                                                                                                      | nein                                                                                                                                                         | nein                                                                                                                                                         |
| Verschiedene Rollen sind nicht vorhanden.                                                                                                                    | Verschiedene Rollen sind nicht vorhanden.                                                                                                                    | Verschiedene Rollen sind nicht vorhanden.                                                                                                                    | Verschiedene Rollen sind nicht vorhanden.                                                                                                                    |

<!-- page: 62 -->

Tabelle 35: Ermittlung der Relevanz der Gefährdungen für die Beispiel-Objekte N4 und N7.

| G 0.33 Personalausfall                                                                       | A                                                                                            | nein                                                                                         | nein                                                                                         |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Personal wird für Betrieb der Netze nicht benötigt.                                          |                                                                                              |                                                                                              |                                                                                              |
| G 0.34 Anschlag                                                                              | C, I, A                                                                                      | indirekt                                                                                     | indirekt                                                                                     |
| Anschlag kann Netzkomponenten beeinträchtigen.                                               |                                                                                              |                                                                                              |                                                                                              |
| G 0.35 Nötigung, Erpressung oder Korruption                                                  | C, I, A                                                                                      | nein                                                                                         | nein                                                                                         |
| Personal wird für Betrieb der Netze nicht benötigt.                                          |                                                                                              |                                                                                              |                                                                                              |
| G 0.36 Identitätsdiebstahl                                                                   | C, I, A                                                                                      | nein                                                                                         | nein                                                                                         |
| Keine persönlichen Accounts vorhanden.                                                       |                                                                                              |                                                                                              |                                                                                              |
| G 0.37 Abstreiten von Handlungen                                                             | C, I                                                                                         | nein                                                                                         | nein                                                                                         |
| Keine persönlichen Accounts vorhanden.                                                       |                                                                                              |                                                                                              |                                                                                              |
| G 0.38 Missbrauch personenbezogener Daten                                                    | C                                                                                            | nein                                                                                         | direkt                                                                                       |
| Abgehörte Daten können missbraucht werden.                                                   |                                                                                              |                                                                                              |                                                                                              |
| G 0.39 Schadprogramme                                                                        | C, I, A                                                                                      | indirekt                                                                                     | nein                                                                                         |
| Schadprogramme im Router können Verbindung beeinträchtigen.                                  |                                                                                              |                                                                                              |                                                                                              |
| G 0.40 Verhinderung von Diensten (Denial of Service)                                         | A                                                                                            | direkt                                                                                       | nein                                                                                         |
| N7: Nicht relevant, weil geschlossenes Netzwerk.                                             |                                                                                              |                                                                                              |                                                                                              |
| G 0.41 Sabotage                                                                              | A                                                                                            | direkt                                                                                       | direkt                                                                                       |
| N4: z.B. durch gezielte Angriffe auf IP-Adresse. N7: z.B. durch Störsender.                  | N4: z.B. durch gezielte Angriffe auf IP-Adresse. N7: z.B. durch Störsender.                  |                                                                                              |                                                                                              |
| G 0.42 Social Engineering                                                                    | C, I                                                                                         | nein                                                                                         | nein                                                                                         |
| Keine persönlichen Accounts vorhanden.                                                       |                                                                                              |                                                                                              |                                                                                              |
| G 0.43 Einspielen von Nachrichten                                                            | C, I                                                                                         | direkt                                                                                       | nein                                                                                         |
| N7: Nicht relevant, weil geschlossenes Netzwerk.                                             |                                                                                              |                                                                                              |                                                                                              |
| G 0.44 Unbefugtes Eindringen in Räumlichkeiten                                               | C, I, A                                                                                      | indirekt                                                                                     | indirekt                                                                                     |
| Relevant, wenn Manipulationen an den Komponenten vorgenommen werden.                         | Relevant, wenn Manipulationen an den Komponenten vorgenommen werden.                         | Relevant, wenn Manipulationen an den Komponenten vorgenommen werden.                         | Relevant, wenn Manipulationen an den Komponenten vorgenommen werden.                         |
| G 0.45 Datenverlust                                                                          | A                                                                                            | nein                                                                                         | nein                                                                                         |
| N4 und N7 sind zustandslose Systeme.                                                         |                                                                                              |                                                                                              |                                                                                              |
| G 0.46 Integritätsverlust schützenswerter Informationen                                      | I                                                                                            | indirekt                                                                                     | nein                                                                                         |
| N7: Nicht relevant, weil geschlossenes Netzwerk.                                             |                                                                                              |                                                                                              |                                                                                              |
| G 0.47 Schädliche Seiteneffekte IT-gestützter Angriffe                                       | C, I, A                                                                                      | indirekt                                                                                     | nein                                                                                         |
| N4: Auswirkungen von Angriffen auf Router des ISP. N7: Da System geschlossen nicht relevant. | N4: Auswirkungen von Angriffen auf Router des ISP. N7: Da System geschlossen nicht relevant. | N4: Auswirkungen von Angriffen auf Router des ISP. N7: Da System geschlossen nicht relevant. | N4: Auswirkungen von Angriffen auf Router des ISP. N7: Da System geschlossen nicht relevant. |

<!-- page: 63 -->

## 4.2 Ermittlung weiterer relevanter Gefährdungen

Neben den vom BSI aufgeführten Gefährdungen, können für ein Objekt noch weitere potentielle Gefahren bestehen. Sofern diese identifiziert werden, müssen sie ebenfalls in einer Risikoanalyse berücksichtigt werden. Für die beiden Objekte N4 und N7 bestehen allerdings keine weiteren Gefährdungen.

## 4.3 Risikoeinschätzung

Die Höhe des Risikos, das von einer Gefährdung ausgeht, ist im wesentlichen von zwei Faktoren abhängig: von der Eintrittshäufigkeit und von der Schadenshöhe. Die Eintrittshäufigkeit wird bei einer Risikoanalyse in der Regel durch Statistiken und Erfahrungswerte bestimmt, wobei insbesondere bei Statistiken ein bleibender Unsicherheitsfaktor mit einbezogen werden muss. In dieser Masterarbeit wird die Eintrittshäufigkeit anhand eigener Erfahrungen und den Erkenntnissen der Teilnehmer am BSI-Workshop festgelegt.

Tabelle 36: Kategorien der Eintrittshäufigkeiten nach BSI-Standard 200-3.

| Kategorien der Eintrittshäufigkeit   | Kategorien der Eintrittshäufigkeit                 |
|--------------------------------------|----------------------------------------------------|
| selten                               | Eintritt höchstens alle fünf Jahre.                |
| mittel                               | Eintritt einmal in fünf Jahren bis einmal im Jahr. |
| häufig                               | Eintritt einmal im Jahr bis einmal im Monat.       |
| sehr häufig                          | Eintritt mehrmals im Monat.                        |

Vom BSI wird die Eintrittshäufigkeit in vier Kategorien eingeteilt: selten, mittel, häufig und sehr häufig. Die Bedeutungen sind Tabelle 36 zu entnehmen. Die Schadenswirkungen bemessen sich durch den eigentlichen Schaden, dessen Folgeschäden und

den Aufwand zur Wiederherstellung. Auch hierfür werden im BSI-Standard 200-3 vier Kategorien zur   Einstufung   vorgeschlagen.   In  Tabelle   37  sind   diese   aufgeführt   und   auf   den   Bereich   der Rettungsleitstelle übertragen.

Tabelle 37: Kategorien der Schadensauswirkungen nach BSI-Standard 200-3.

| Kategorien der Schadensauswirkungen   | Kategorien der Schadensauswirkungen                                                                                                                                           |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vernachlässigbar                      | Auswirkungen sind gering und können vernachlässigt werden. Eine Beeinträchtigung des Betriebs der Rettungsleitstelle ist nicht zu erwarten.                                   |
| begrenzt                              | Auswirkungen sind begrenzt und überschaubar. Gesundheitliche Schäden für Hilfresuchende sind aufgrund des Schadens nicht zu erwarten.                                         |
| beträchtlich                          | Auswirkungen können beträchtlich sein. Es kann in einzelnen Fällen zu gesundheitlichen Schäden von Hilfesuchenden kommen.                                                     |
| existenzbedrohend                     | Auswirkungen können existenzbedrohend sein und ein katastrophales Ausmaß erreichen. Es muss mit mehreren Fällen gesundheitlicher Schäden von Hilfesuchenden gerechnet werden. |

<!-- page: 64 -->

## 4.4 Risikobewertung

Im nächsten Schritt müssen die identifizierten Gefährdungen und deren Risiken bewertet werden. Die Bewertung erfolgt nach der in Abbildung 7 aufgeführten Matrix zur Einstufung von Risiken.

Abbildung 7: Matrix zur Einstufung von Risiken.

| Auswirkungen / Schadenshöhe   | existenz- bedrohend   | mittel              | hoch                | sehr hoch           | sehr hoch           |
|-------------------------------|-----------------------|---------------------|---------------------|---------------------|---------------------|
| Auswirkungen / Schadenshöhe   | beträchtlich          | gering              | mittel              | hoch                | sehr hoch           |
| Auswirkungen / Schadenshöhe   | begrenzt              | gering              | gering              | mittel              | hoch                |
| Auswirkungen / Schadenshöhe   | vernachlässigbar      | gering              | gering              | gering              | mittel              |
| Auswirkungen / Schadenshöhe   |                       | selten              | mittel              | häufig              | sehr häufig         |
|                               | Eintrittshäufigkeit   | Eintrittshäufigkeit | Eintrittshäufigkeit | Eintrittshäufigkeit | Eintrittshäufigkeit |

Die Risiken werden vom BSI in vier Kategorien eingestuft: gering, mittel, hoch und sehr hoch. Die Bedeutungen der einzelnen Kategorien sind in Tabelle 38 dargestellt.

Tabelle 38: Kategorien der Risiken

| Kategorien der Risiken   | Kategorien der Risiken                                                                                                   |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------|
| gering                   | Umgesetzte oder vorgesehene Maßnahmen bieten ausreichenden Schutz.                                                       |
| mittel                   | Umgesetzte oder vorgesehene Maßnahmen reichen möglicherweise nicht aus.                                                  |
| hoch                     | Umgesetzte oder vorgesehene Maßnahmen bieten keinen ausreichenden Schutz. Eine Risikoreduzierung ist notwendig.          |
| sehr hoch                | Umgesetzte oder vorgesehene Maßnahmen bieten keinen ausreichenden Schutz. Eine Risikoreduzierung ist dringend notwendig. |

In Tabelle 39 werden die Gefährdungen für das Objekt N4 hinsichtlich Schadensauswirkungen und Eintrittswahrscheinlichkeit bewertet. Es werden nur die Gefährdungen berücksichtigt, die direkte Auswirkungen   auf   das   Objekt   N4   haben.   Die   Schadensauswirkung   ist   bei   den   meisten Gefährdungen beträchtlich, weil bei einem Eintritt mit dem Auftreten gesundheitlicher Schäden bei Hilfesuchenden zu rechnen ist. Lediglich die Gefährdung G 0.18 (Fehlplanung oder fehlende Anpassung) hat nur begrenzte Auswirkungen. Dies liegt daran, dass sich  Fehlplanungen beim Netz zum ISP leicht korrigieren lassen. Ist die Bandbreite der Internetverbindung zu gering, kann diese zum Beispiel erhöht werden.

<!-- page: 65 -->

| Netz zum Internet Service Provider N4 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Netz zum Internet Service Provider N4 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Netz zum Internet Service Provider N4 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Netz zum Internet Service Provider N4 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Gefährdung: G 0.8 Ausfall oder Störung der Stromversorgung                                                        | Gefährdung: G 0.8 Ausfall oder Störung der Stromversorgung                                                        | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                             | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                             |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                                                            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Risiko ohne zusätzliche Maßnahmen: mittel                                                                         |
| Gefährdung: G 0.9 Ausfall oder Störung von Kommunikationsnetzen                                                   | Gefährdung: G 0.9 Ausfall oder Störung von Kommunikationsnetzen                                                   | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                             | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                             |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                                                            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Risiko ohne zusätzliche Maßnahmen: mittel                                                                         |
| Gefährdung: G 0.11 Ausfall oder Störung von Dienstleistern                                                        | Gefährdung: G 0.11 Ausfall oder Störung von Dienstleistern                                                        | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit                                            | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit                                            |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                                                            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Risiko ohne zusätzliche Maßnahmen: mittel                                                                         |
| Gefährdung: G 0.15 Abhören                                                                                        | Gefährdung: G 0.15 Abhören                                                                                        | Beeinträchtigte Grundwerte: Vertraulichkeit                                                                       | Beeinträchtigte Grundwerte: Vertraulichkeit                                                                       |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                                                            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Risiko ohne zusätzliche Maßnahmen: gering                                                                         |
| Gefährdung: G 0.18 Fehlplanung oder fehlende Anpassung                                                            | Gefährdung: G 0.18 Fehlplanung oder fehlende Anpassung                                                            | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit                                            | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit                                            |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                                                            | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                                                                 | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                                                                 | Risiko ohne zusätzliche Maßnahmen: gering                                                                         |
| Gefährdung: G 0.19 Offenlegung schützenswerter Informationen                                                      | Gefährdung: G 0.19 Offenlegung schützenswerter Informationen                                                      | Beeinträchtigte Grundwerte: Vertraulichkeit                                                                       | Beeinträchtigte Grundwerte: Vertraulichkeit                                                                       |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                                                            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Risiko ohne zusätzliche Maßnahmen: gering                                                                         |
| Gefährdung: G 0.21 Manipulation von Hard- oder Software                                                           | Gefährdung: G 0.21 Manipulation von Hard- oder Software                                                           | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit                                            | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit                                            |

<!-- page: 66 -->

| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Gefährdung: G 0.22 Manipulation von Informationen                                   | Gefährdung: G 0.22 Manipulation von Informationen                                   | Beeinträchtigte Grundwerte: Integrität                                 | Beeinträchtigte Grundwerte: Integrität                                 |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.23 Unbefugtes Eindringen in IT-Systeme                              | Gefährdung: G 0.23 Unbefugtes Eindringen in IT-Systeme                              | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität                | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität                |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.24 Zerstörung von Geräten oder Datenträgern                         | Gefährdung: G 0.24 Zerstörung von Geräten oder Datenträgern                         | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.25 Ausfall von Geräten oder Systemen                                | Gefährdung: G 0.25 Ausfall von Geräten oder Systemen                                | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.26 Fehlfunktion von Geräten oder Systemen                           | Gefährdung: G 0.26 Fehlfunktion von Geräten oder Systemen                           | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.27 Ressourcenmangel                                                 | Gefährdung: G 0.27 Ressourcenmangel                                                 | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.28 Software-Schwachstellen oder -Fehler                             | Gefährdung: G 0.28 Software-Schwachstellen oder -Fehler                             | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen | Gefährdung: G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.40 Verhinderung von Diensten (Denial of Service)                    | Gefährdung: G 0.40 Verhinderung von Diensten (Denial of Service)                    | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |

<!-- page: 67 -->

| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel   | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich   | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich   | Risiko ohne zusätzliche Maßnahmen: mittel               |
|----------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Gefährdung: G 0.41 Sabotage                              | Gefährdung: G 0.41 Sabotage                             | Beeinträchtigte Grundwerte: Verfügbarkeit               | Beeinträchtigte Grundwerte: Verfügbarkeit               |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten   | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich   | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich   | Risiko ohne zusätzliche Maßnahmen: gering               |
| Gefährdung: G 0.43 Einspielen von Nachrichten            | Gefährdung: G 0.43 Einspielen von Nachrichten           | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten   | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich   | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich   | Risiko ohne zusätzliche Maßnahmen: gering               |

## Tabelle 39: Risikobewertung für das Netz zum Internet Service Provider (N4)

Für das Alarmierungsnetz für Funkmeldeempfänger wird in Tabelle 40 ebenfalls eine Risikobewertung durchgeführt. Auch hier sind die Schadensauswirkungen der meisten Gefährdungen beträchtlich. Ein Ausfall oder eine Störung der Stromversorgung (G 0.8) hat nur begrenzte Auswirkungen, weil die Netzkomponenten normalerweise mit einem Batteriepuffer für mehrere Stunden ausgestattet sind. Die Gefährdung durch einen Ressourcenmangel (G 0.27) kann zum Beispiel eintreten, indem sehr viele Alarme in kurzer Zeit ausgesendet werden. In diesem Fall kommt es zu Verzögerungen. Da die Rettungskräfte dennoch alarmiert werden, sind die Auswirkungen nur als begrenzt einzuordnen. Da das POCSAG-Netz mit frei verkäuflichen Funkscannern leicht abgehört werden kann, ist die Eintrittshäufigkeit   bei   den   Gefährdungen   G   0.15   und   G   0.19   sehr   häufig.   Werden personenbezogene Daten und bei Einsätzen des Rettungsdienstes auch medizinische Diagnosen

übermittelt, sind die Auswirkungen beträchtlich und das Risiko entsprechend sehr hoch.

| Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Gefährdung: G 0.8 Ausfall oder Störung der Stromversorgung                                                             | Gefährdung: G 0.8 Ausfall oder Störung der Stromversorgung                                                             | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                                  | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                                  |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                                                                 | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                                                                      | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                                                                      | Risiko ohne zusätzliche Maßnahmen: gering                                                                              |
| Gefährdung: G 0.12 Elektromagnetische Störstrahlung                                                                    | Gefährdung: G 0.12 Elektromagnetische Störstrahlung                                                                    | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                                  | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                                  |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                                                                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                                  | Risiko ohne zusätzliche Maßnahmen: gering                                                                              |
| Gefährdung: G 0.15 Abhören                                                                                             | Gefährdung: G 0.15 Abhören                                                                                             | Beeinträchtigte Grundwerte: Vertraulichkeit                                                                            | Beeinträchtigte Grundwerte: Vertraulichkeit                                                                            |
| Eintrittshäufigkeit ohne                                                                                               | Auswirkungen ohne zusätzliche                                                                                          | Auswirkungen ohne zusätzliche                                                                                          | Risiko ohne zusätzliche                                                                                                |

<!-- page: 68 -->

| zusätzliche Maßnahmen: sehr häufig                                     | Maßnahmen: beträchtlich                                                | Maßnahmen: beträchtlich                                                | Maßnahmen: sehr hoch                                                   |
|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Gefährdung: G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten | Gefährdung: G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten | Beeinträchtigte Grundwerte: Vertraulichkeit, Verfügbarkeit             | Beeinträchtigte Grundwerte: Vertraulichkeit, Verfügbarkeit             |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.18 Fehlplanung oder fehlende Anpassung                 | Gefährdung: G 0.18 Fehlplanung oder fehlende Anpassung                 | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.19 Offenlegung schützenswerter Informationen           | Gefährdung: G 0.19 Offenlegung schützenswerter Informationen           | Beeinträchtigte Grundwerte: Vertraulichkeit                            | Beeinträchtigte Grundwerte: Vertraulichkeit                            |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: sehr häufig            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: sehr hoch                           |
| Gefährdung: G 0.21 Manipulation von Hard- oder Software                | Gefährdung: G 0.21 Manipulation von Hard- oder Software                | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.24 Zerstörung von Geräten oder Datenträgern            | Gefährdung: G 0.24 Zerstörung von Geräten oder Datenträgern            | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.25 Ausfall von Geräten oder Systemen                   | Gefährdung: G 0.25 Ausfall von Geräten oder Systemen                   | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.26 Fehlfunktion von Geräten oder Systemen              | Gefährdung: G 0.26 Fehlfunktion von Geräten oder Systemen              | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.27 Ressourcenmangel                                    | Gefährdung: G 0.27 Ressourcenmangel                                    | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                 | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                      | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                      | Risiko ohne zusätzliche Maßnahmen: gering                              |

<!-- page: 69 -->

Tabelle 40: Risikobewertung für das Alarmierungsnetz für Funkmeldeempfänger (N7)

| Gefährdung: G 0.28 Software-Schwachstellen oder -Fehler                             | Gefährdung: G 0.28 Software-Schwachstellen oder -Fehler                             | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit   | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit   |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                    | Risiko ohne zusätzliche Maßnahmen: gering                                |
| Gefährdung: G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen | Gefährdung: G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit   | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit   |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                    | Risiko ohne zusätzliche Maßnahmen: gering                                |
| Gefährdung: G 0.38 Missbrauch personenbezogener Daten                               | Gefährdung: G 0.38 Missbrauch personenbezogener Daten                               | Beeinträchtigte Grundwerte: Vertraulichkeit                              | Beeinträchtigte Grundwerte: Vertraulichkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                    | Risiko ohne zusätzliche Maßnahmen: mittel                                |
| Gefährdung: G 0.41 Sabotage                                                         | Gefährdung: G 0.41 Sabotage                                                         | Beeinträchtigte Grundwerte: Verfügbarkeit                                | Beeinträchtigte Grundwerte: Verfügbarkeit                                |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                    | Risiko ohne zusätzliche Maßnahmen: gering                                |

## 4.5 Risikobehandlung

Nach der Bewertung muss im nächsten Schritt der Umgang mit den Risiken festgelegt werden. Grundsätzlich stehen vier Optionen zur Auswahl [Klip15]:

- Vermeidung (z.B. durch Ausschluss der Risikoursache).
- Reduktion/Modifikation (z.B. durch Änderung der Rahmenbedingungen).
- Transfer/Teilen (z.B. durch Versicherung oder Outsourcing).
- Akzeptanz/Übernahme (Risiko des Eintritts eines Schadenfalls wird in Kauf genommen).

Akzeptiert werden Risiken in der Regel nur dann, wenn sie als gering eingestuft werden und der Aufwand, das Risiko anderweitig unter Kontrolle zu bringen, schwerer wiegt als die potentielle Beeinträchtigung der Grundwerte [Gibs11].

Für die Risiken, die bei den betrachteten Objekten als mittel oder höher eingestuft wurden, sind in Tabelle 41 für N4 und in Tabelle 42 für N7 Optionen zur Behandlung beschrieben. Durch ergänzende Maßnahmen ergibt sich jeweils eine neue Einstufung des Risikos.

## Netz zum Internet Service Provider N4

Vertraulichkeit: sehr hoch

Integrität: sehr hoch

Verfügbarkeit: sehr hoch

<!-- page: 70 -->

| Gefährdung                                           | Risikokategorie                     | Risikobehandlungsoptionen                                                                                                                           |
|------------------------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.8 Ausfall oder Störung der Stromversorgung       | mittel                              | Risikoreduktion: Es wird ein Notstromsystem vorgehalten.                                                                                            |
| G 0.8 Ausfall oder Störung der Stromversorgung       | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Es wird ein Notstromsystem vorgehalten.                                                                                            |
| G 0.9 Ausfall oder Störung von Kommunikationsnetzen  | mittel                              | Risikoreduktion: Es wird ein redundanter Anschluss zum ISP vorgehalten.                                                                             |
| G 0.9 Ausfall oder Störung von Kommunikationsnetzen  | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Es wird ein redundanter Anschluss zum ISP vorgehalten.                                                                             |
| G 0.11 Ausfall oder Störung von Dienstleistern       | mittel                              | Risikoreduktion: Es wird ein redundanter Anschluss zum ISP vorgehalten.                                                                             |
| G 0.11 Ausfall oder Störung von Dienstleistern       | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Es wird ein redundanter Anschluss zum ISP vorgehalten.                                                                             |
| G 0.25 Ausfall von Geräten oder Systemen             | mittel                              | Risikoreduktion: Es werden ein redundanter Anschluss zum ISP und redundante Netzkomponenten vorgehalten.                                            |
| G 0.25 Ausfall von Geräten oder Systemen             | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Es werden ein redundanter Anschluss zum ISP und redundante Netzkomponenten vorgehalten.                                            |
| G 0.27 Ressourcenmangel                              | mittel                              | Risikoreduktion: Der Anschluss zum ISP wird ausreichend dimensioniert.                                                                              |
| G 0.27 Ressourcenmangel                              | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Der Anschluss zum ISP wird ausreichend dimensioniert.                                                                              |
| G 0.28 Software- Schwachstellen oder - Fehler        | mittel                              | Risikoreduktion: Updates zur Fehlerbehebung müssen zeitnah eingespielt werden.                                                                      |
| G 0.28 Software- Schwachstellen oder - Fehler        | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Updates zur Fehlerbehebung müssen zeitnah eingespielt werden.                                                                      |
| G 0.40 Verhinderung von Diensten (Denial of Service) | mittel                              | Risikoreduktion: Der Anschluss zum ISP wird ausreichend dimensioniert. Zusätzlich wird ein redundanter Anschluss bei einem anderen ISP vorgehalten. |
| G 0.40 Verhinderung von Diensten (Denial of Service) | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Der Anschluss zum ISP wird ausreichend dimensioniert. Zusätzlich wird ein redundanter Anschluss bei einem anderen ISP vorgehalten. |

Tabelle 41: Behandlung der Risiken des Netzes zum ISP.

| Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch   | Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch   | Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Gefährdung                                                              | Risikokategorie                                                         | Risikobehandlungsoptionen                                               |

<!-- page: 71 -->

Tabelle 42: Behandlung der Risiken des Alarmierungsnetzes.

| G 0.15 Abhören                                   | Sehr hoch                           | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
|--------------------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.15 Abhören                                   | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
| G 0.15 Offenlegung schützenswerter Informationen | Sehr hoch                           | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
| G 0.15 Offenlegung schützenswerter Informationen | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
| G 0.25 Ausfall von Geräten oder Systemen         | mittel                              | Risikoreduktion: Benötigte Netzkomponenten werden redundant vorgehalten. Als Rückfallebene wird ein weiteres Alarmierungssystem parallel betrieben, z.B. über eine App. |
| G 0.25 Ausfall von Geräten oder Systemen         | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Benötigte Netzkomponenten werden redundant vorgehalten. Als Rückfallebene wird ein weiteres Alarmierungssystem parallel betrieben, z.B. über eine App. |
| G 0.26 Fehlfunktion von Geräten oder Systemen    | mittel                              | Risikoreduktion: Die Netzkomponenten und Geräte werden vor der Inbetriebnahme ausgiebig geprüft.                                                                        |
| G 0.26 Fehlfunktion von Geräten oder Systemen    | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Die Netzkomponenten und Geräte werden vor der Inbetriebnahme ausgiebig geprüft.                                                                        |
| G 0.38 Missbrauch personenbezogener Daten        | mittel                              | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
| G 0.38 Missbrauch personenbezogener Daten        | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |

Durch die aufgeführten Maßnahmen zur Risikoreduktion können alle Risiken der Objekte N4 und N7 als gering eingestuft und somit akzeptiert werden. Es ist möglich, dass Schritte zur Risikoreduktion   mehrfach   durchlaufen   werden   müssen,   um   die   Kriterien   zur  Akzeptanz   eines   Risikos   zu erreichen. Zum Beispiel lässt sich die Bandbreite des Internetanschlusses nach oben skalieren, um das Risiko eines Ressourcenmangels als gering einordnen zu können.

## 4.6 Risikobeobachtung

Möglicherweise können Risiken derzeit als gering eingestuft und daher akzeptiert werden. Jedoch können sich Bedingungen ändern und die Risiken bestimmter Gefährdungen steigen. Diese sollten daher ständig beobachtet werden. Im Optimalfall liegen bereits Konzepte für die Behandlung von Risiken vor, sollten sich diese erhöhen. Kann ein Risiko nicht mehr akzeptiert werden, ist hierdurch eine unmittelbare Reaktion möglich.

<!-- page: 72 -->

## 5 Theoretische Evaluation

Das in dieser Arbeit erstellte IT-Grundschutz-Profil sollen die Leitstellen nach Fertigstellung anwenden. Die Eignung des Profils wird daher zuvor auf zwei Arten theoretisch überprüft: Das BSI veranstaltet einen mehrteiligen Workshop mit Vertretern von BOS-Leitstellen mit dem Ziel, ein IT-Grundschutz-Profil für Leitstellen zu erstellen. Aus dem Workshop gewonnene Erkenntnisse sollen die Ähnlichkeit der Strukturen und somit die Anwendbarkeit eines IT-Grundschutz-Profils für Leitstellen verifizieren. Die ersten beiden Teile des Workshops fanden parallel zu dieser Masterarbeit statt. Ein weiterer Termin ist im Frühjahr 2020 geplant. Als Grundlage des Workshops dient das in dieser Arbeit entwickelte Profil, das im Anhang A angefügt ist. Ergebnisse, die im Workshop entstanden sind, fließen in das Profil zurück. Diese sind im Abschnitt 5.1 aufgeführt. Anhang B enthält das englisch übersetzte IT-Grundschutz-Profil, welches an Mitglieder der EENA, mit der Bitte um Feedback zur Anwendung, verteilt wird. Es soll untersucht werden, ob das Profil auf andere Länder übertragbar ist.

## 5.1 Ergebnisse aus BSI Workshop mit Leitstellen

Der Workshop hat gezeigt, dass in den Leitstellen Ähnlichkeiten in den Strukturen bestehen und somit die Anwendung eines IT-Grundschutz-Profils möglich sein sollte. Alle Leitstellen führen dieselben Kernprozesse durch und verwenden hierzu ähnliche Anwendungen sowie IT-Systeme. Bei lokalen Besonderheiten kann das Profil ergänzt werden. Andererseits kann auf einzelne Objekte verzichtet werden, sofern diese in der betrachteten Leitstelle nicht existieren.  Einige Teilnehmer zählen   zum   Beispiel   die   Prozesse   der   Stammdatenpflege   nicht   zum   eigentlichen   Betrieb   der Leitstelle. Unterschiede ergeben sich außerdem im Gebrauch von Bezeichnungen. Eine mögliche Lösung für dieses Problem ist die Erstellung eines Glossars innerhalb des Profils, in dem Begriffe eindeutig bestimmt werden. In Ergänzung zu Abschnitt 3.5 dieser Arbeit wurde entschieden, jedes potentielle Schadensszenario in jeder Schutzbedarfskategorie einzeln zu betrachten. In Abschnitt 5.1 des Anhangs A wurde diese Darstellung   in   den   Tabellen   A-10,   A-11   und   A-12   übernommen.   V orausgegangen   war  eine Diskussion über die Schutzbedarfskategorien und die Definition der Dauer eines Ausfalls, ab dem die   Aufgabenerfüllung   einer   Leitstelle   beeinträchtigt   wird.   Als   Ergebnis   erwies   sich   eine Begrenzung der tolerierbaren Ausfalldauer auf 72 Stunden in der Schutzbedarfskategorie normal , 24 Stunden in der Kategorie hoch und 4 Stunden in der Kategorie sehr hoch als sinnvoll. Die Fragestellung, ob ein Ausfall ohne zeitliche Begrenzung tolerierbar sei, wenn der Schaden durch Ersatzsysteme   oder  Ausweichlösungen   weitgehend   kompensiert   werden   kann,   wurde   als   nicht akzeptabel   bewertet.   Die   Diskussionen   haben   jedoch   gezeigt,   dass   Bedarf   an   einer   weiteren Untersuchung zu Auswirkungen von Verletzungen der Informationssicherheit in Leitstellen besteht.

<!-- page: 73 -->

## 5.2 Übertragbarkeit des Profils auf andere Länder

Zur Untersuchung der Übertragbarkeit des Profils auf andere Länder wurde in Anhang B eine englische Version des IT-Grundschutz-Profils erstellt und über die EENA ausländischen Leitstellen zur Verfügung gestellt. Die folgenden Erkenntnisse resultieren aus Gesprächen mit dem Geschäftsführer der Leitstelle in Niederösterreich und der technischen Direktion der EENA. Die grundsätzliche Übertragbarkeit des Profils auf internationale Leitstellen wurde dabei bestätigt. Die Leitstelle in Niederösterreich ist seit 2010 auf vier Standorte im Bundesland aufgeteilt. 31 An allen Standorten wird dieselbe Technik in Form eines integrierten Systems für ELS und KMS genutzt. Der Schutzbedarf für die Netzwerkverbindungen zwischen den Standorten muss daher besonders hoch eingestuft werden. Die Leitstelle nutzt hierfür redundante Datenleitungen unterschiedlicher ISP. 32 Der Ausfall eines Standortes kann durch die geografische Verteilung besonders leicht kompensiert werden, da die Notrufe dann von den anderen Standorten bearbeitet werden können. Einen innovativen Weg geht die Leitstelle auch bei erhöhtem Notrufaufkommen, zum Beispiel bei Unwettern. Hier können Mitarbeiter auch von zu Hause aus Notrufe entgegennehmen und so kurzfristig für Entlastung sorgen. Eine Anwendung des IT-Grundschutz-Profils müsste daher weitere Bausteine berücksichtigen. Im internationalen Vergleich ergeben sich Unterschiede zwischen den Leitstellen. Zum Beispiel gibt es die Trennung zwischen polizeilichem und nichtpolizeilichem Notruf in vielen Ländern nicht [EENA19]. Das bekannteste Beispiel ist die Notrufnummer 911 in den USA. Diese gilt für alle Notrufe unabhängig davon, ob der Anrufer die Feuerwehr, den Rettungsdienst oder die Polizei benötigt. In den Leitstellen werden durch diesen organisatorischen Aufbau zusätzliche sensible Daten verarbeitet, wodurch das Sicherheitsniveau weiter angehoben werden muss. Zum Beispiel kann eine Leitstelle der Polizei, im Vergleich zu einer nichtpolizeilichen Leitstelle, für Kriminelle ein besonders lohnenswertes Angriffsziel darstellen, um die Verfolgung nach einer Straftat zu erschweren. Dementsprechend müsste der Schutzbedarf der betroffenen Objekte bei einer Anwendung des ITGrundschutz-Profils überprüft werden. Wie in Abschnitt 3.4.2 beschrieben, werden in deutschen Leitstellen in der Regel ein KMS und ein ELS verwendet. Diese Aufteilung in Anwendungen für die Kommunikation einerseits und die Einsatzaufnahme sowie -bearbeitung andererseits, gibt es in anderen Ländern oft nicht. Stattdessen werden Systeme genutzt, die alle Prozesse in einer integrierten Anwendung abbilden können. Ist ihr Betrieb beeinträchtigt, müssen mehrere Prozesse gleichzeitig über Redundanzsysteme bearbeitet werden. Entsprechend hoch ist der Schutzbedarf für die integrierten Systeme zu bewerten, was bei Anwendung des Profils zu berücksichtigen ist. Die technische Direktion der EENA hat die Fokussierung des IT-Grundschutz-Profils auf deutsche Leitstellen hervorgehoben. Eine Übertragbarkeit auf internationale Ebene ist mit den entsprechenden Anpassungen aber ebenso möglich.

31

32

[https://notrufnoe.com/ueber/historie/   (abgerufen am 28.11.2019).](https://notrufnoe.com/ueber/historie/)

[https://notrufnoe.com/technikcenter/   (abgerufen am 28.11.2019).](https://notrufnoe.com/technikcenter/)

<!-- page: 74 -->

## 6 Fazit und Ausblick

Ziel dieser Masterarbeit war die Erstellung eines IT-Grundschutz-Profils für Rettungsleitstellen, mit dem diese den IT-Grundschutz praktisch umsetzen können. Nach der Festlegung des Geltungsbereichs und der Abgrenzung des Informationsverbundes wurde eine Strukturanalyse durchgeführt. Hierbei wurden zunächst die gängigen Prozesse einer Leitstelle definiert. Die Durchführung der Prozesse wird durch Anwendungen unterstützt. Diese und die IT-Systeme, die für den Betrieb der Anwendungen benötigt werden, wurden ermittelt und beschrieben. Anhand der in den Leitstellen gewöhnlich vorhandenen Netzwerke wurde ein Netzplan erstellt. Mit einer Betrachtung der Gebäude und Räume wurde die Strukturanalyse abgeschlossen. Anschließend wurde der Schutzbedarf aller in der Strukturanalyse ermittelten Objekte erfasst. Bei allen drei Schutzzielen der Informationssicherheit ging aus der Untersuchung für viele Objekte ein sehr hoher Schutzbedarf hervor. Angesichts der wichtigen und sensiblen Aufgaben von Rettungsleitstellen entspricht dies den Erwartungen. Die Bausteine aus dem IT-Grundschutz-Kompendium des BSI sind auch in Leitstellen für die meisten Objekte anwendbar, da viele Komponenten im Einsatz sind, die auch in anderen Institutionen verwendet werden. Ein zusätzlicher Baustein könnte zukünftig für das Alarmierungsnetz erstellt werden, da hierfür bislang kein passendes Modul existiert. Aufgrund des sehr hohen Schutzbedarfs mehrerer Objekte wurde, exemplarisch für zwei Objekte, eine Risikoanalyse durchgeführt. Das Ergebnis zeigt, dass Risiken bestehen, die jedoch durch zusätzliche Maßnahmen reduziert werden können. Trotz der großen Anzahl von Rettungsleitstellen in Deutschland ist deren Systemarchitektur grundsätzlich ähnlich und ermöglicht daher die Erstellung eines IT-Grundschutz-Profils. Verifiziert wurde dies   durch   den   Workshop   des   BSI,   an   dem   Vertreter   verschiedener   Leitstellen   teilnahmen. Bezüglich der maximal tolerierbaren Ausfallzeiten besteht Bedarf an weiteren wissenschaftlichen Untersuchungen. Eine Anwendung des IT-Grundschutz-Profils im Ausland ist praktikabel, sofern bei der Umsetzung entsprechende Anpassungen an die lokalen Gegebenheiten erfolgen. Die Strukturen und Systeme in internationalen Leitstellen unterscheiden sich teilweise von denen in Deutschland. Durch den Gebrauch innovativer Techniken und einer stärkeren Vernetzung müssen zudem weitere Aspekte bei der Anwendung des Profils berücksichtigt werden. Demgegenüber können die Innovationen einiger ausländischer Leitstellen richtungsweisend für die Entwicklung in Deutschland sein. Vorteile durch die Verbreitung neuer Techniken, wie zum Beispiel Videotelefonie, müssen in Zukunft auch beim Notruf berücksichtigt werden. Darüber hinaus können Livebilder von Einsatzstellen, die von Drohnen gefilmt werden, bevor die ersten Einsatzkräfte eintreffen, eine weiteren Hilfe für die Leitstelle sein, um Notfallsituationen besser einzuschätzen. Dies sind zwei Beispiele von vielen, die für eine Qualitätssteigerung in den Leitstellen sorgen können; gleichzeitig aber auch ein angepasstes Sicherheitsniveau bei der verwendeten Informationstechnik erfordern.

<!-- page: 75 -->

Galt früher die Regel, Leitstellentechnik komplett vom Internet zu trennen, erfordern aktuelle und neue Techniken die Vernetzung mit externen Systemen. Eine Isolierung wird zunehmend schwieriger und spätestens mit der endgültigen Abschaltung der ISDN-Technik unmöglich. Hierdurch steigt das Risiko eines Sicherheitsvorfalls, unabhängig davon, ob dieser absichtlich oder unabsichtlich herbeigeführt wird. Während Rettungsdiensten im humanitären Völkerrecht eine Sonderrolle zukommt, sind sie im Internet den gleichen Risiken ausgesetzt wie jeder andere Nutzer. Informationssicherheit obliegt einer stetigen Veränderung. Deshalb ist die regelmäßige Anpassung des IT-Grundschutz-Profils an die aktuellen Begebenheiten unabdingbar. Hierzu hat sich im Fachverband Leitstellen eine Arbeitsgruppe gebildet, die diese Aufgabe zukünftig übernimmt. Die englische Version des Profils kann durch die EENA aktualisiert werden. Bei der Anwendung dieser Version ist zu beachten, dass die Bausteine des BSI bisher nur in deutscher Sprache verfügbar sind. Eine englische Übersetzung soll jedoch in Kürze vom BSI veröffentlicht werden. Im nächsten Schritt müssen die potentiellen Anwender Kenntnis von der Existenz des IT-Grundschutz-Profils erlangen. Hierzu sind Beiträge in Fachzeitschriften und auf Konferenzen geplant. Eine Vorstellung der englischen Version soll auf der EENA-Konferenz im April 2020 stattfinden, an der über tausend Vertreter von Leitstellen teilnehmen werden. Die Erstellung des IT-Grundschutz-Profils in dieser Masterarbeit war somit der Beginn eines Prozesses, die Informationstechnik in den Leitstellen sicherer zu betreiben.

<!-- page: 76 -->

## Literaturverzeichnis

AGBF15: Stein, Jochen, Qualitätskriterien für die Bedarfsplanung von Feuerwehren in Städten, Arbeitsgemeinschaft der Leiter der Berufsfeuerwehren, 2015

BÄK19: Rettungswesen, [online] https://www.bundesaerztekammer.de/aerzte/versorgung/notfallmedizin/rettungswesen/ [abgerufen am: 03.08.2019]

BBK09: Kritische Infrastrukturen, [online] https://www.bbk.bund.de/DE/AufgabenundAusstattung/ KritischeInfrastrukturen/kritischeinfrastrukturen\_node.html [abgerufen am: 01.07.2019]

BBK18: Bundesamt für Bevölkerungsschutz und Katastrophenhilfe, BBK-Glossar, 2018

BeAc10: Bedner, Mark/Ackermann, Tobias, Schutzziele der IT-Sicherheit, Datenschutz und Datensicherheit, Ausgabe 5, 2010

BMSW99: Böhmer, Roman/Merz,Thomas/Schneider,Thomas/Wolcke,Benno, Taschenatlas Rettungsdienst, Böhmer &amp; Merz Verlag GbR, Mainz, 1999

BMWi17: Zypries: Startschuss für bundesweite Notruf-App ist wichtiger Schritt zu mehr Sicherheit und Digitalisierung, [online] https://www.bmwi.de/Redaktion/DE/Pressemitteilungen/2017/20170922-zypries-startschussfuer-bundesweite-notruf-app-ist-wichtiger-schritt-zu-mehr-sicherheit-und-digitalisierung.html [abgerufen am: 01.07.2019]

BNetzA18: Technische Richtlinie Notrufverbindungen, [online] https://www.bundesnetzagentur.de/ DE/Sachgebiete/Telekommunikation/Unternehmen\_Institutionen/Anbieterpflichten/Notruf/ TechnischeRichtlinie/technischerichtlinie.html [abgerufen am: 28.07.2019]

BR19: Die bundesweite Notruf-App kommt 2020, [online] https://www.br.de/nachrichten/bayern/die-bundesweite-notruf-app-kommt,RT5iNlm [abgerufen am: 01.07.2019]

BrFi18: Brauner, Florian/Fiedrich, Frank, Kritische Infrastrukturen und Business Continuity Management, Springer Vieweg, Wiesbaden, 2018

BSI08: BSI-Standard 100-4, [online] https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzStandards/Standard04/ ITGStandard04\_node.html [abgerufen am: 12.10.2019]

BSI17: BSI-Standard 200-2, [online] https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/ standard\_200\_2.html [abgerufen am: 11.08.2019]

<!-- page: 77 -->

BSI17a: BSI-Standard 200-3, [online] https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzStandards/Standard203/ ITGStandard203\_node.html [abgerufen am: 22.10.2019]

BSI18: Online-Kurs IT-Grundschutz, [online] https://www.bsi.bund.de/SharedDocs/Downloads/DE/ BSI/Grundschutz/Webkurs/onlinekurs2018.html [abgerufen am: abgerufen am 01.07.2019]

BSI19: IT-Grundschutz-Kompendium, [online] https://www.bsi.bund.de/DE/Themen/ITGrundschutz/itgrundschutz\_node.html [abgerufen am: 01.07.2019]

BSI19a: IT-Grundschutz-Profile, [online] https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzProfile/ itgrundschutzProfile\_node.html [abgerufen am: 01.07.2019]

BSI19b: Glossar, [online] https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKompendium/vorkapitel/ Glossar\_.html [abgerufen am: 04.08.2019]

BSI19c: IT-Grundschutz-Schulung - Lerneinheit 2.1: Der Sicherheitsprozess, [online] https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzSchulung/ OnlinekursITGrundschutz2018/Lektion\_2\_Sicherheitsmanagement/Lektion\_2\_01/ Lektion\_2\_01\_node.html [abgerufen am: 04.08.2019]

BSI19d: IT-Grundschutz-Schulung - Lektion 2: Sicherheitsmanagement, [online] https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzSchulung/ OnlinekursITGrundschutz2018/Lektion\_2\_Sicherheitsmanagement/Lektion\_2\_node.html [abgerufen am: 05.08.2019]

BSI19e: Das BSI - Historie, [online] https://www.bsi.bund.de/DE/DasBSI/Historie/historie\_node.html [abgerufen am: 06.08.2019]

DeTe18: Deutsche Telekom AG, Notruf 110/112 Migration Notrufleitstellen, 2018

DHS18: Cyber Risks to Next Generation 9-1-1, [online] https://www.911.gov/pdf/OEC\_NG911\_Cybersecurity\_Primer\_May\_2018.pdf [abgerufen am: 01.07.2019]

DIN14096: Beuth Verlag, DIN 14096:2014-05, 2014

DIN18: Feuerwehrfahrzeug-Typenliste der gängigsten genormten Fahrzeuge, [online] https://www.din.de/blob/273898/9ab852208877be21ce9842b382d7b418/feuerwehrfahrzeugtypenliste-22-fassung-2018-04-data.pdf [abgerufen am: 03.08.2019]

DIN22301: Beuth-Verlag, DIN EN ISO 22301:2014-12, 2014

<!-- page: 78 -->

DNN19: Barmer will Leitstellen zusammenlegen, [online] https://www.dnn.de/Region/Mitteldeutschland/Barmer-will-Leitstellen-zusammenlegen [abgerufen am: 01.07.2019]

Ecke18: Eckert, Claudia, IT-Sicherheit, Walter de Gruyter, Berlin/Boston, 2018

EENA19: European Emergency Number Association, Public Safety Answering Points - Global Edition, 2019

EFK17: IDDS ICiP - Unified Mission Critical Communications, [online] https://www.eurofunk.com/wp-content/uploads/Broschuere\_IDDS\_UCiP\_DE\_WEB-1.pdf [abgerufen am: 28.07.2019]

FVLS19: BOS-Leitstellen, [online] http://www.fachverband-leitstellen.de/index.php/ct-menu-item5 [abgerufen am: 01.07.2019]

Gabl18: Gabler Wirtschftslexikon, [online] https://wirtschaftslexikon.gabler.de/definition/organisationsstruktur-43095/version-266428 [abgerufen am: 11.08.2019]

GaMa17: Gadatsch, Andreas/Mangiapane, Markus, IT-Sicherheit, Springer Vieweg, Wiesbaden, 2017

Gibs11: Gibson, Darril, Managing Risk in Information Systems, Jones &amp; Bartlett Learning, Sudbury (MA), 2011

GrGJ17: Groom, Frank M./Groom, Kevin/Jones, Stephan S., Network and Data Security for NonEngineers, Taylor &amp; Francis Group, Boca Raton (FL), 2017

HaLM2015: Hackstein, A./Lenz W./Marung H., Personalqualifikation in der Leitstelle, Springer Medizin Verlag GmbH, Berlin, Notfall + Rettungsmedizin, Ausgabe 7, 2015

HaMN19: Hansen, Hans Robert/Mendling, Jan/Neumann, Gustaf, Wirtschaftsinformatik, Walter de Gruyter GmbH, Berlin/Boston, 2019

InfSec19: UK Firms Hit By Attacks Every 50 Seconds, [online] https://www.infosecuritymagazine.com/news/uk-firms-hit-by-attacks-every-50/ [abgerufen am: 04.08.2019]

JaId13: Jacobson, Douglas/Idziorek, Joseph, Computer Security Literacy, Taylor &amp; Francis Group, Boca Raton (FL), 2013

KaKa12: von Kaufmann, Florentin/Kanz, Karl-Georg, Die Rolle der Leitstelle im Prozess der präklinischen Versorgung, Springer, Heidelberg, Notfall + Rettungsmedizin, Ausgabe 4, 2012

KKMS15: Kaufmann, Florentin/Kiening, S./Morhart-Klute, V./Schmid, F., Technik als Voraussetzung für eine effizientere Prozessabwicklung in der Leitstelle, Springer, Heidelberg, Notfall + Rettungsmedizin, Ausgabe 18, 2015

<!-- page: 79 -->

Klip15: Klipper, Sebastian, Information Security Risk Management, Springer Vieweg, Wiesbaden, 2015

KlSK11: Klett, Gerhard/Schröder, Klaus-Werner/Kersten, Heinrich, IT-Notfallmanagement mit System, Vieweg+Teubner, Wiesbaden, 2011

Köhl17: Köhler, Dr. Markus, Der Schutz kritischer Infrastrukturen im Gesundheitswesen - gesetzliche Anforderungen an die IT-Sicherheit, Verlag Dr. Otto Schmidt KG, GesundheitsRecht, Band 16, Heft 3, 2017

KoSS17: Kohnke, Anne/Sigler, Ken/Shoemaker, Dan, Implementing Cybersecurity, Taylor &amp; Francis Group, Boca Raton (FL), 2017

KrWe17: Kraft, Peter/Weyert, Andreas, Network Hacking, Franzis Verlag, Haar, 2017

LFSBW05: Landesfeuerwehrschule Baden-Württemberg, Ausbildung der FreiwilligenFeuerwehren, Neckar-Verlag GmbH, Villingen-Schwenningen, 2005

LiDo00: Lipp, Roland/Domres, Bernd, Lehrbuch für präklinische Notfallmedizin Band 4, Stumpf und Kossendy, Edewecht, 2000

MiRSW05: Mintz-Habib, Matthew/Rawat, Anshuman/Schulzrinne, Henning/Wu, Xiaotao,  A VoIP emergency services architecture and prototype, Institute of Electrical and Electronics Engineers (IEEE), Proceedings. 14th International Conference on Computer Communications and Networks (IEEE Cat. No. 05EX1184), 2005

MMOVL16: Machado Gary/Medland, John/O'Brien, Tony/Vivier, Benoît/Lumbreras, Christina, Advanced Mobile Location (AML) Specifications &amp; Requirements, European Emergency Number Association, 2016

Müll14: Müller, Klaus-Rainer, IT-Sicherheit mit System, Springer Vieweg, Wiesbaden, 2014

NeSB13: Neumayr, Agnes/Schinnerl, Adolf/Baubin, Michael, Qualitätsmanagement im prähospitalen Notfallwesen, Springer-Verlag, Wien, 2013

Pelt14: Peltier, Thomas R., Information Security Fundamentals, Taylor &amp; Francis Group, Boca Raton (FL), 2014

RaPM96: Rannenberg, Kai/Pfitzmann, Andreas/Müller, Günter, Sicherheit, insbesondere mehrseitige IT-Sicherheit, Oldenbourg Wissenschaftsverlag GmbH, München, 2013

RMBD98: Rappaport, Theodore S./Muhamed, Rias/Buehrer, Michael/Doradla, Anil, Mobile and Cellular Radio Communications, Ed. Richard C. Dorf, CRC Press LLC, 1998

ScAn99: Schmid, Markus/Angerer, Richard, Lehrbuch für den Rettungsdienst, HofmannVerlagGmbH, Augsburg, 1999

<!-- page: 80 -->

SLMSA03: Schlechtriemen, T./Lackner, Chr.-K./Moecke, Hp./Stratmann, D./Altemeyer, K.H., Sicherung der flächendeckenden Notfallversorgung: notwendige Strukturverbesserungen, Springer Medizin Verlag GmbH, Notfall + Rettungsmedizin, Ausgabe 21, 2003

TaSt08: Tanenbaum, Andrew S./Steen van, Maarten, Verteilte Systeme - Prinzipien und Paradigmen, Pearson Deutschland GmbH, Hallbergmoos, 2008

Tiem17: Tiemeyer, Ernst, Handbuch IT-Management, Carl Hanser Verlag, München, 2017

TsSc13: Tschofenig, Hannes/Schulzrinne, Henning, Internet Protocol-Based Emergency Services, John Wiley &amp; Sons Verlag, Hoboken (New Jersey), 2013

VCGB17: Varcoe, Richard W./Clayton, Tim C./Gray, Huon/de Belder, Mark A/Ludman, Peter F/Henderson, Robert A., Impact of call-to-balloon time on 30-day mortality in contemporary practice, Heart, Band 103, 2017

WuHZ18: Wurmb, T./Hossfeld, B./Zoller, G., Polizei und Rettungsdienst bei der Bewältigung lebensbedrohlicher Einsatzlagen, Springer Medizin Verlag GmbH, Notfall + Rettungsmedizin, Ausgabe 21, 2018

WuZh15: Wu, Hanqing/Zhao, Liz, Web Security, Taylor &amp; Francis Group, Boca Raton (FL), 2015

<!-- page: 81 -->

## Anhang

<!-- page: 82 -->

## IT-Grundschutz-Profil für Rettungsleitstellen

Herausgeber: XXX Registrierungsnummer: XXX Version: 1.0 Revisionszyklus: jährlich

<!-- page: 83 -->

## Inhaltsverzeichnis

1 Management Summary.................................................................................................................A-1

2 Festlegung des Geltungsbereichs..................................................................................................A-1

3 Abgrenzung des Informationsverbundes.......................................................................................A-2

3.1 Bestandteile des Informationsverbundes...............................................................................A-2

3.2 Nicht berücksichtigte Teile....................................................................................................A-2

4 Referenzarchitektur.......................................................................................................................A-3

4.1 Prozesse.................................................................................................................................A-3

4.2 Anwendungen........................................................................................................................A-4

4.3 IT-Systeme.............................................................................................................................A-4

4.4 Netze und Netzkomponenten.................................................................................................A-5

4.4.1 Netzplan.........................................................................................................................A-6

4.5 Gebäude und Räume..............................................................................................................A-6

4.6 Umgang mit Abweichungen..................................................................................................A-7

5 Zu erfüllende Anforderungen und umzusetzende Maßnahmen....................................................A-7

5.1 Feststellung des Schutzbedarfs..............................................................................................A-7

5.1.1 Schutzbedarfsfeststellung für Prozesse........................................................................A-10

5.1.2 Schutzbedarfsfeststellung für Anwendungen...............................................................A-12

5.1.3 Schutzbedarfsfeststellung für IT-Systeme...................................................................A-13

5.1.4 Schutzbedarfsfeststellung für Netzwerke....................................................................A-14

5.1.5 Schutzbedarfsfeststellung für Räume..........................................................................A-16

5.2 Auswahl relevanter Bausteinen...........................................................................................A-17

5.3 Anforderungen übergreifend gültiger Prozessbausteine......................................................A-21

5.4 Anforderungen spezifisch gültiger Prozessbausteine..........................................................A-26

6 Restrisiko.....................................................................................................................................A-31

7 Anwendungshinweise..................................................................................................................A-32

8 Notfallmanagement (BCM).........................................................................................................A-32

9 Unterstützende Informationen.....................................................................................................A-32

10 Risikoanalyse............................................................................................................................A-32

10.1 Ermittlung elementarer Gefährdungen..............................................................................A-33

10.2 Ermittlung weiterer relevanter Gefährdungen...................................................................A-36

10.3 Risikoeinschätzung............................................................................................................A-36

10.4 Risikobehandlung..............................................................................................................A-41

10.5 Risikobeobachtung............................................................................................................A-43

<!-- page: 84 -->

## Versionshistorie

| Datum   |   Version | Änderung             | Bearbeiter   |
|---------|-----------|----------------------|--------------|
|         |       1.0 | Erstveröffentlichung |              |

<!-- page: 85 -->

## 1 Management Summary

Das IT-Grundschutz-Profil für Rettungsleitstellen richtet sich an die für Informationstechnik verantwortlichen Entscheidungsträger aus dem Bereich der Rettungsleitstellen. Ebenso soll es aber auch Herstellern von Leitstellentechnik und mit der technischen Planung von Leitstellen beauftragten Fachplanern als Handlungsleitfaden für die Informationssicherheitskonzeption in Rettungsleitstellen dienen. Dieses IT-Grundschutz-Profil soll den Anwendern helfen, einen Informationssicherheitsprozess in einer Rettungsleitstelle zu installieren und diesen an die Bedürfnisse in Rettungsleitstellen anzupassen. Es soll als Schablone dienen, den IT-Grundschutz des BSI in geeigneter Weise zu implementieren.

## 2 Festlegung des Geltungsbereichs

## Zielgruppe

Das IT-Grundschutz-Profil für Rettungsleitstellen richtet sich an die für Informationstechnik verantwortlichen Entscheidungsträger aus diesem Bereich. Gleichzeitig soll es auch Herstellern und Lieferanten   von   Leitstellentechnik   als   Grundlage   für  Aufbau   und   Entwicklung   ihrer   Systeme   und Anwendungen   dienen.   Auch   Fachplaner   für   Rettungsleitstellen sind Zielgruppe   des   ITGrundschutz-Profils.

## Beschreibung des Schutzbedarfs

Die Betriebsbereitschaft von Rettungsleitstellen muss ständig gegeben sein. Ebenso muss auf die Korrektheit und Vertraulichkeit der verarbeiteten Daten großen Wert gelegt werden. Die Informationssicherheitsziele Vertraulichkeit, Verfügbarkeit und Integrität müssen daher über das übliche Maß hinaus   erreicht   werden.   Infolgedessen   liegt   das   in   diesem   IT-Grundschutz-Profil   beschriebene Schutzniveau über der Standard-Absicherung der IT-Grundschutz-Vorgehensweise und ist als sehr hoch zu betrachten.

## IT-Grundschutz Vorgehensweise

Der IT-Grundschutz des BSI bietet die Vorgehensweisen Basis-, Standard oder Kern-Absicherung an. Abhängig von der gewählten Vorgehensweise müssen die in den Bausteinen beschriebenen Anforderungen umgesetzt werden. Die beschriebenen Anforderungen in diesem IT-Grundschutz-Profil entsprechen mindestens der Standard-Absicherung des BSI-Standards 200-2. Zudem wird empfohlen, einzelne Anforderungen aus dem erhöhten Schutzbedarf umzusetzen.

## Kompatibilität zu anderen Standards

Durch eine Umsetzung der Standard-Absicherung besteht Kompatibilität zu ISO 27001. 1

## Berücksichtigte Rahmenbedingungen

Vorgaben aus der DSGVO und dem BSI-Gesetz werden in diesem IT-Grundschutz-Profil berücksichtigt.

[1 https://www.beuth.de/de/norm/din-en-iso-iec-27001/269670716   (aufgerufen am 01.07.2019)](https://www.beuth.de/de/norm/din-en-iso-iec-27001/269670716)

<!-- page: 86 -->

## 3 Abgrenzung des Informationsverbundes

Die   zusammenhängenden   Komponenten   einer   Institution   oder   eines   speziellen  Anwendungsbereichs werden als Informationsverbund bezeichnet. Im nächsten Abschnitt werden die für das ITGrundschutz-Profil relevanten Bestandteile des Informationsverbunds Rettungsleitstelle definiert. Anschließend werden die Teile des Informationsverbundes aufgeführt, die in diesem IT-Grundschutz-Profil nicht berücksichtigt werden.

## 3.1 Bestandteile des Informationsverbundes

Die folgende Tabelle zeigt die technischen Bestandteile des Informationsverbundes, die Prozesse und Verfahren in Rettungsleitstellen unterstützen und in diesem IT-Grundschutz-Profil berücksichtigt werden.

| Identifikator   | Objekt des Informationsverbundes   |
|-----------------|------------------------------------|
| IV1             | Prozesse                           |
| IV2             | Anwendungen                        |
| IV3             | Gebäude und Räume                  |
| IV4             | IT-Systeme                         |
| IV5             | Netzwerke                          |

## Tabelle A-1: Bestandteile des Informationsverbundes, die Prozesse und Verfahren in Rettungsleitstellen unterstützen.

## 3.2 Nicht berücksichtigte Teile

Der auf den TETRA-Standard basierende digitale Funk der Behörden und Organisationen mit Sicherheitsaufgaben (BOS) wird im IT-Grundschutz-Profil für Rettungsleitstellen nicht vollständig berücksichtigt, weil dieser ein eigenständiges System darstellt, das lediglich Schnittstellen zu den Rettungsleitstellen bereitstellt. Das BSI erstellt hierzu derzeit einen Baustein im IT-GrundschutzKompendium, der nach Fertigstellung von den Leitstellen berücksichtigt werden sollte. Die technische Sicherheit der Daten- und Telefonanschlüsse liegt in Verantwortung der Netzbetreiber. Eine Berücksichtigung im IT-Grundschutz-Profil für Rettungsleitstellen ist daher nicht notwendig. Immer mehr Hersteller bieten Notruf-Apps für Smartphones an, über die eine Notfallmeldung an die Rettungsleitstelle abgesetzt werden kann. Eine offizielle Notruf-App des Bundes soll im Jahr 2020 erscheinen. Diese Form von Apps stellen ein eigenständiges System dar. Die Schnittstelle zu Rettungsleitstellen   besteht   in   der   Regel   aus   einer   Webapplikation,   die   über   den   Webbrowser abgerufen werden kann. Notruf-Apps müssen daher im IT-Grundschutz-Profil für Rettungsleitstellen nicht berücksichtigt werden. Neben   der   Alarmierung   über   das   Funknetz   der   BOS   nutzen   viele   Feuerwehren   und   Hilfsorganisationen Alarmierungs-Apps für Smartphones. Auf eine sichere Implementierung dieser Apps hat die Rettungsleitstelle keinen Einfluss. Auch hier muss daher lediglich die Schnittstelle zwischen den Anwendungen in der Rettungsleitstelle und der Alarmierungs-App betrachtet werden. Deshalb findet eine Berücksichtigung der Alarmierungs-App im IT-Grundschutz-Profil nicht statt.

<!-- page: 87 -->

## 4 Referenzarchitektur

Die Referenzarchitektur beinhaltet neben Gebäuden und Räumen, in denen die Rettungsleitstelle betrieben wird, die Kommunikationsverbindungen, Netzwerke und die dafür benötigten Komponenten. Außerdem werden alle beteiligten IT-Systeme, die verwendeten Anwendungen und die in der Rettungsleitstelle durchgeführten Prozesse in der Referenzarchitektur aufgeführt. Es ist möglich, dass sich die Referenzarchitektur von der tatsächlich vorhandenen Architektur einer

Rettungsleitstelle unterscheidet. Der Umgang mit solchen Abweichungen ist in Abschnitt 4.6 beschrieben.

## 4.1 Prozesse

Der Betrieb einer Rettungsleitstelle gliedert sich in unterschiedliche Prozesse, die für das IT-Grundschutz-Profil relevant sind und in diesem Abschnitt definiert werden. Die Kernprozesse sind der Meldungseingang und die damit verbundene Einsatzaufnahme, die Bearbeitung, sowie schließlich der Abschluss des Einsatzes.

<!-- image -->

## Schaubild A-1: Kernprozesse in einer Rettungsleitstelle.

In der folgenden Tabelle werden die in der Rettungsleitstelle durchgeführten Prozesse in Unterprozesse gegliedert und mit einem Identifikator versehen.

Tabelle A-2: Prozesse in der Leitstelle bei Meldungseingang und Einsatzaufnahme.

| Identifikator   | Prozesse des Meldungseingangs und Einsatzaufnahme   |
|-----------------|-----------------------------------------------------|
| P1.1            | Meldungseingang per Telefon                         |
| P1.2            | Meldungseingang per Fax                             |
| P1.3            | Meldungseingang per E-Mail                          |
| P1.4            | Meldungseingang per Funk                            |
| P1.5            | Meldungseingang per Web                             |
| P1.6            | Meldungseingang per Brandmeldeanlage (BMA)          |
| P1.7            | Meldungseingang per eCall                           |
| P2.1            | Einsatzaufnahme manuell in Einsatzleitsystem        |
| P2.2            | Einsatzaufnahme automatisch in Einsatzleitsystem    |

<!-- page: 88 -->

Tabelle A-3: Prozesse in der Leitstelle bei Einsatzabschluss, Stammdatenpflege und weiteren Tätigkeiten.

| Identifikator   | Prozesse der Einsatzbearbeitung und -abschluss                   |
|-----------------|------------------------------------------------------------------|
| P3.1            | Disposition                                                      |
| P3.2            | Alarmierung                                                      |
| P3.3            | Überwachung                                                      |
| P3.4            | Dokumentation                                                    |
| P4.1            | Einsatzdatenübermittlung an Dritte                               |
| P4.2            | Archivierung                                                     |
| Identifikator   | Prozesse der Stammdatenpflege                                    |
| P5.1            | Empfang von zu hinterlegenden Daten über E-Mail und USB-Speicher |
| P5.2            | Eingabe und Speicherung von Daten in ELS und KMS                 |
| Identifikator   | Weitere Prozesse                                                 |
| P6              | Besprechungen und Schulungen                                     |

## 4.2 Anwendungen

Zum Informationsverbund gehören neben den Prozessen auch die Anwendungen, die eine optimale Bearbeitung der Prozesse unterstützen sollen. Dies sind in einer Rettungsleitstelle insbesondere das Einsatzleit- und das Kommunikationssystem. Auch E-Mailclient und Webbrowser stellen wichtige Komponenten dar. Alle Anwendungen sind in der folgenden Tabelle mit einem Identifikator aufgeführt. In der rechten Spalte ist angegeben, welche Prozesse von den Anwendungen unterstützt werden.

Tabelle A-4: Anwendungen des Informationsverbundes, die in einer Rettungsleitstelle verwendet werden.

| Identifikator   | Anwendungen des Informationsverbundes   | Unterstützte Prozesse        |
|-----------------|-----------------------------------------|------------------------------|
| A1              | Einsatzleitsystem                       | P1.6, P1.7, P2, P3, P4, P5.2 |
| A2              | Kommunikationssystem                    | P1.1, P1.4, P1.7, P3, P5.2   |
| A3              | Webbrowser                              | P1.5, P3, P5                 |
| A4              | E-Mailclient                            | P1.3, P5.1                   |
| A5              | Gefahrstoffinformationssysteme          | P2.1, P3                     |
| A6              | PDF-Viewer                              | P2.1, P3, P5                 |
| A7              | Office-Produkt                          | P5.1                         |
| A8              | Dateiablage/freigegebene Netzlaufwerke  | P4, P5                       |

## 4.3 IT-Systeme

Neben den Anwendungen, sind auch die IT-Systeme, die für den Betrieb der Anwendungen benötigt werden Teil des Informationsverbundes. Dazu zählen zum Beispiel Betriebssysteme, oder die hierfür bereitgestellte Hardware. Komponenten, die Netzwerkverbindungen betreffen, werden in Abschnitt 4.4 extra betrachtet.

<!-- page: 89 -->

| Identifikator   | IT-Systeme des Informationsverbundes                  | Abhängige Anwendungen/Prozesse   |
|-----------------|-------------------------------------------------------|----------------------------------|
| S1.1            | Betriebssysteme für Clients                           | A1, A2, A3, A4, A5, A6, A7, A8   |
| S1.2            | Betriebssysteme für Server                            | A1, A2                           |
| S2.1            | Server                                                | A1, A2                           |
| S2.2            | Virtualisierungsplattformen                           | A1, A2                           |
| S3              | Arbeitsplatz-Client                                   | A1, A2, A3, A4, A5, A6, A7, A8   |
| S4              | Faxgeräte                                             | P1.2                             |
| S5              | Drucker und Multifunktionsgeräte (Scan- ner/Kopierer) | A1, A6, A7                       |

## Tabelle A-5: IT-Systeme des Informationsverbundes, die in einer Rettungsleitstelle verwendet werden.

## 4.4 Netze und Netzkomponenten

Anwendungen und IT-Systeme der Rettungsleitstelle sind in verschiedene Netzwerke eingebunden. Auch wenn sich Anzahl und Aufbau der Netze nicht im Detail verallgemeinern lassen, wird davon ausgegangen, dass die Architektur in vielen Leitstellen zumindest ähnlich ist. Zum Betrieb der Netze sind aktive und passive Netzkomponenten erforderlich. Eine besondere Rolle spielt in Rettungsleitstellen das Alarmierungsnetz zum Auslösen von Funkmeldeempfängern.

| Identifikator   | Objekt des Informationsverbundes   | Abhängige Objekte                      |
|-----------------|------------------------------------|----------------------------------------|
| N1              | ELS-Netz                           | A1, S1, S2, S3, S5                     |
| N2              | KMS-Netz                           | A2, S1, S2, S3, S5                     |
| N3              | Büro-Netz                          | A3, A4, A5, A6, A7, A8, S1, S2, S3, S5 |
| N4              | Netz zum Internet Service Provider | A1, A2, A3, A4                         |
| N5.1            | Router                             | N1, N2, N3                             |
| N5.2            | Switches                           | N1, N2, N3                             |
| N5.3            | Firewalls                          | N1, N2, N3                             |
| N5.4            | Session Border Controller          | N2                                     |
| N6              | Kabel/Patchfelder                  | N1, N2, N3                             |
| N7              | Alarmierungsnetz für Funkmelder    | A1                                     |

## Tabelle A-6: Netzkomponenten und Netze des Informationsverbundes.

<!-- page: 90 -->

## 4.4.1 Netzplan

Schaubild A-2: Netzplan

<!-- image -->

## 4.5 Gebäude und Räume

Nicht nur die informationstechnischen Komponenten spielen bei der Informationssicherheit eine große Rolle. Auch die Sicherheit der Gebäude und Räume in denen die Rettungsleitstelle betrieben wird muss in einem IT-Grundschutz-Profil berücksichtigt werden. Dies betrifft nicht nur den Dispositionsraum, in denen die Notfallmeldungen entgegengenommen und die Rettungsmittel zu den Einsätzen disponiert werden. Die Räume, in denen die Server und andere Technik untergebracht sind müssen ebenso betrachtet werden wie die Büroräume für Verwaltungsmitarbeiter.

<!-- page: 91 -->

Tabelle A-7: Räume des Informationsverbundes.

| Identifikator   | Räume des Informationsverbundes       | In den Räumen installierte IT- Systeme oder durchgeführte Prozesse   |
|-----------------|---------------------------------------|----------------------------------------------------------------------|
| R1              | Dispositionsraum                      | P1, P2, P3, S3, S4, S5                                               |
| R2              | Rechenzentrum/Technikraum             | S2                                                                   |
| R3.1            | Büro der Leitung der Leitstelle       | S3, S4, S5                                                           |
| R3.2            | Stammdatenpflegebüro                  | P5, S3, S4, S5                                                       |
| R3.3            | Administratorbüro                     | S3, S4, S5                                                           |
| R4              | Raum für Telekommunikationsanschlüsse | N2, N4                                                               |
| R5              | Archivraum                            | P4                                                                   |
| R6              | Besprechungs- und Schulungsraum       | P6                                                                   |

## 4.6 Umgang mit Abweichungen

Weicht der zu schützende Informationsverbund von der hier dargestellten Referenzarchitektur ab, müssen die zusätzlichen oder nicht vorhandenen Objekte dokumentiert werden. Die Objekte sollten passenden Komponenten des IT-Grundschutz Kompendium zugeordnet werden. Die abgeleiteten Anforderungen müssen an den jeweiligen Schutzbedarf angepasst werden.

## 5 Zu erfüllende Anforderungen und umzusetzende Maßnahmen

Das   IT-Grundschutz-Kompendium   des   BSI   stellt   Bausteine   bereit,   die   anwendungsbezogene Empfehlungen zur Umsetzung des IT-Grundschutzs geben. Hierzu muss zunächst der Schutzbedarf der Prozesse, Anwendungen, IT-Systeme und Kommunikationsverbindungen festgelegt werden. Anschließend müssen die relevanten Bausteine identifiziert und eine Anpassung der Anforderungen an   die   entsprechende   Zielgruppe   durchgeführt   werden.   Das   Resultat   der   Anpassung   der Anforderungen kann bedeuten, dass alle oder nur bestimmte Anforderungen des Bausteins für die Informationssicherheit   in   Rettungsleitstellen   relevant   sind.   Ebenso   können  Anforderungen   als komplett irrelevant eingestuft werden. Auch die Relevanz der in den Anforderungen aufgeführten Maßnahmen muss identifiziert werden.

## 5.1 Feststellung des Schutzbedarfs

Grundlegend sind bei der Festlegung des Schutzbedarfs die Auswirkungen, die eine Verletzung der Grundziele der Informationssicherheit, Vertraulichkeit, Integrität oder Verfügbarkeit hätten. Diese Effekte werden im Folgenden betrachtet. Das BSI benennt verschiedene Szenarien, auf die sich ein Schaden beziehen kann. Diese sind in Tabelle A-8 aufgeführt.

Verstöße gegen Gesetze, Vorschriften oder Verträge (SZ1) können zum Beispiel vorliegen, wenn die Rettungsleitstelle nicht betriebsbereit ist und somit ihre Aufgaben nicht erfüllen kann (SZ4). Gleichzeitig kann es hierdurch zu Beeinträchtigungen der persönlichen Unversehrtheit von Notrufenden kommen (SZ3), wenn diesen nicht rechtzeitig geholfen wird. Verstöße gegen Datenschutzgesetze fallen ebenfalls unter Schadensszenario 1. Die Übermittlung vertraulicher Informationen, über Anrufer oder Patienten an Unbefugte, stellt zudem eine Beeinträchtigung des informationellen Selbstbestimmungsrechts der Hilfesuchenden dar (SZ2). Alle diese Fälle können aufgrund von Schadensersatzforderungen der Betroffenen auch finanzielle Auswirkungen auf die Rettungsleitstelle haben (SZ6). Für die Bürger ist ein hohes Vertrauen in die Arbeit der Rettungsleitstelle elementar. Dass ihnen im Notfall geholfen werden kann, gibt den Menschen ein sicheres Gefühl. Durch eine negative Außenwirkung (SZ5) kann diese Gewissheit abhanden kommen. Gleiches gilt für das eigene Personal der Rettungsleitstelle oder der angebundenen Hilfsorganisationen bei einer negativen Innenwirkung. Diese Effekte können zum Beispiel aufgrund von Ausfällen und damit verbundener negativer Berichterstattung in den Medien auftreten.

<!-- page: 92 -->

| Identifikator   | Schadensszenario                                                |
|-----------------|-----------------------------------------------------------------|
| SZ1             | Verstöße gegen Gesetze, Vorschriften oder Verträge              |
| SZ2             | Beeinträchtigungen des informationellen Selbstbestimmungsrechts |
| SZ3             | Beeinträchtigungen der persönlichen Unversehrtheit              |
| SZ4             | Beeinträchtigungen der Aufgabenerfüllung                        |
| SZ5             | negative Innen- oder Außenwirkung                               |
| SZ6             | finanzielle Auswirkungen                                        |

## Tabelle A-8: Potentielle Schadensszenarien.

Die   Schadensszenarien   werden   in   den   folgenden   Abschnitten   für   jedes   der   Grundziele   der Informationssicherheit   einzeln   betrachtet.   Die   Schadensauswirkung   kann   dabei   im   voraus normalerweise   nicht   detailgenau   festgelegt   werden.   Aus   diesem   Grund   empfiehlt   die   ITGrundschutz-Methodik des BSI drei Kategorien zu bestimmen, die den Schutzbedarf einstufen. Die drei Kategorien sind normal , hoch oder sehr hoch . Tabelle A-9 führt die Kategorien auf, ergänzt um die   Schadensauswirkungen.   Die   Schadensauswirkung   kann   sich   dabei   immer   auf   die Rettungsleitstelle selbst oder auf die hilfesuchenden Bürger beziehen.

| Kategorie   | Schadensauswirkung                                                                                                                                               |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| normal      | Die Schadensauswirkungen für die Leitstelle oder die hilfesuchenden Bürger sind be- grenzt und überschaubar.                                                     |
| hoch        | Die Schadensauswirkungen können den Betrieb der Leitstelle erheblich einschränken. Für die hilfesuchenden Bürger können die Konsequenzen beträchtlich sein.      |
| sehr hoch   | Die Schadensauswirkungen können den Betrieb der Leitstelle stilllegen. Für Hilfesu- chende kann es zu existenziell- oder lebensbedrohlichen Konsequenzen kommen. |

## Tabelle A-9: Vom BSI empfohlene Schutzbedarfskategorien.

In den folgenden drei Tabellen werden die Schutzbedarfskategorien mit den potentiellen Schadensszenarien verknüpft.

<!-- page: 93 -->

Tabelle A-10: Schadensszenarien bei Schutzbedarfskategorie normal.

| Schutzbedarfskategorie: Normal   | Schutzbedarfskategorie: Normal                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SZ1                              | Verstöße gegen Vorschriften und Landesgesetze (RD-G, FW-G, KatS-G, LS-G), sowie Aus- führungsverordnungen und Dienstanweisungen , die zu arbeitsrechtlichen und / oder zivil- rechtlichen Folgen für das Leitstellenpersonal führen können.                                                                                                                                                          |
| SZ2                              | Es handelt sich hierbei um personenbezogene Daten, durch deren Verarbeitung der Betroffe- ne in seiner gesellschaftlichen Stellung oder in seinen wirtschaftlichen Verhältnissen beein- trächtigt werden kann. In diese Kategorie fallen alle öffentlich zugänglichen Daten, wie Name, Adresse, Telefonnummer, sowie besondere personenbezogene Daten für die eine Freigabe nach dem BDSG vorliegen. |
| SZ3                              | Eine Beeinträchtigung der persönlichen Unversehrtheit kann nicht ausgeschlossen werden. Es ist mit leichten Gesundheitsschäden zu rechnen.                                                                                                                                                                                                                                                           |
| SZ4                              | Der Schaden ist durch Ersatzsysteme oder Ausweichlösungen weitgehend kompensierbar. Die Beeinträchtigung würde von den Betroffenen weitgehend als tolerabel eingeschätzt wer- den. Die maximal tolerierbare Ausfallzeit des IT-Systems ist größer als 24 Stunden (SLA-2).                                                                                                                            |
| SZ5                              | Der Schadensfall wird nur innerhalb der Leitstelle und den angegliederten Einsatzkräften wahrgenommen. Es kommt zu keiner Offenlegung innerhalb der Bevölkerung.                                                                                                                                                                                                                                     |
| SZ6                              | Der finanzielle Schaden ist durch Versicherungen abgedeckt oder kann durch das Leitstel- lenbudget aufgefangen werden.                                                                                                                                                                                                                                                                               |

Tabelle A-11: Schadensszenarien bei Schutzbedarfskategorie hoch.

| Schutzbedarfskategorie: Hoch   | Schutzbedarfskategorie: Hoch                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SZ1                            | Verstöße gegen Vorschriften und Landesgesetze (RD-G, FW-G, KatS-G, LS-G), sowie all- gemeingültigem Recht (BGB, Strafrecht) , die zu strafrechtlichen und zivilrechtlichen Fol- gen für das Leitstellenpersonal, sowie zu Haftungsschäden beim Leitstellenträger führen können.                                                                                       |
| SZ2                            | Es handelt sich hierbei um personenbezogene Daten, durch deren unkontrollierter Offenle- gung der Betroffene in seiner gesellschaftlichen Stellung oder in seinen wirtschaftlichen Verhältnissen erheblich beeinträchtigt werden kann. In diese Kategorie fallen alle besonders schutzbedürftigen Daten nach dem BDSG, besipielsweise persönliche medizinische Daten. |
| SZ3                            | Eine Beeinträchtigung der persönlichen Unversehrtheit ist wahrscheinlich. Es ist mit erheb- lichen Gesundheitsschäden einzelner Personen zu rechnen und/oder mit irreparablen Fol- gen ohne die Möglichkeit einer vollständigen Genesung.                                                                                                                             |
| SZ4                            | Die Schadenshöhe in der Leitstelle führt zu Ausfällen in der polizeilichen / nichtpolizeiliche Gefahrenabwehr. Die Reaktionszeiten und sonstige Leistungsmerkmale sind stark einge- schränkt. Der Schaden ist durch Ersatzsysteme oder Ausweichlösungen nur teilweise kom- pensierbar. Der Ausfall muss innerhalb von 24 Stunden behoben werden (SLA-1).              |
| SZ5                            | Der Schaden ist öffentlich sichtbar. Regionale Presseeinrichtungen berichten über das Scha- densausmaß. Es müssen öffentliche Durchsagen ausgestrahlt werden.                                                                                                                                                                                                         |
| SZ6                            | Der finanzielle Schaden ist nur durch den Betreiber (Organisation, Stadt, Landkreis, Bun- desland) insgesamt, aber nicht durch das Einzelbudget der Leitstelle tragbar.                                                                                                                                                                                               |

<!-- page: 94 -->

| Schutzbedarfskategorie: Sehr hoch   | Schutzbedarfskategorie: Sehr hoch                                                                                                                                                                                                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SZ1                                 | Verstöße gegen Vorschriften und Landesgesetze (RD-G, FW-G, KatS-G, LS-G), sowie all- gemeingültigem Recht (BGB, Strafrecht) , die zu erheblichen strafrechtlichen und zivil- rechtlichen Folgen für das Leitstellenpersonal, sowie zu umfangreichen (über 1 Million Euro) Haftungsschäden beim Leitstellenträger führen können. |
| SZ2                                 | Es handelt sich um personenbezogene Daten, bei deren Verarbeitung eine Gefahr für Leib und Leben oder die persönliche Freiheit des Betroffenen gegeben ist, sowie Daten die zu ei- nem wirtschaftlichen Ruin des Betroffenen führen können, z.B. Bankdaten oder private Zu- gangsdaten.                                         |
| SZ3                                 | Es ist mit sehr hoher Wahrscheinlichkeit mit dem Tode einzelner oder mehrerer Personen zu rechnen.                                                                                                                                                                                                                              |
| SZ4                                 | Die polizeiliche / nichtpolizeiliche Gefahrenabwehr ist erheblich eingeschränkt. Externe Notfallpläne müssen eingesetzt werden. Der Schaden kann nicht kompensiert werden. Die Beeinträchtigung wird von allen Betroffenen als nicht tolerabel eingeschätzt. Der Ausfall muss innerhalb von 4 Stunden behoben werden (SLA-0).   |
| SZ5                                 | Es kommt zur Berichterstattung in überregionalen Presseorganen, mit hohem Vertauensver- lust in der Bevölkerung und den handelnden Personen in die eingesetzte technik ist zu rech- nen.                                                                                                                                        |
| SZ6                                 | Der finanzielle Schaden ist durch den Betreiber nicht mehr kompensierbar. Der Schaden führt zum Ruin des Betreibers und hinterlässt offene Forderungen.                                                                                                                                                                         |

## Tabelle A-12: Schadensszenarien bei Schutzbedarfskategorie sehr hoch.

Bei der Bestimmung des Schutzbedarfs eines in Abschnitt 4 bestimmten Objekts müssen immer auch die Prozesse oder andere Objekte betrachtet werden, für die dieses Objekt benötigt wird. Wird zum Beispiel ein Objekt für einen Prozess verwendet, dessen Schutzbedarf sehr hoch ist, so ist auch der Schutzbedarf des betrachteten Objekts als sehr hoch einzustufen.

## 5.1.1 Schutzbedarfsfeststellung für Prozesse

Für die Schutzbedarfsfeststellung der Prozesse muss das Ausmaß eines Schadens auf den jeweiligen Prozess ermittelt werden. Zunächst wird jeder in Abschnitt 4.1 definierte Prozess hinsichtlich der Vertraulichkeit untersucht. Anschließend findet eine Untersuchung bezüglich der Integrität statt. Zuletzt wird der Schutzbedarf für die Verfügbarkeit der einzelnen Prozesse ermittelt.

<!-- page: 95 -->

Tabelle A-13: Schutzbedarfsfeststellung der Vertraulichkeit für Prozesse in der Leitstelle.

| Schutzbedarfsfeststellung der Vertraulichkeit für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Vertraulichkeit für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Vertraulichkeit für Prozesse des Informationsverbundes                                            |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Objekt                                                                                 | Schutzbedarf                                                                           | Begründung                                                                                                                      |
| P1.1                                                                                   | sehr hoch                                                                              | Verarbeitung personenbezogener Daten mit medizinischen Diagnosen, die vertraulich behandelt werden müssen (SZ1, SZ2, SZ5, SZ6). |
| P1.2                                                                                   | sehr hoch                                                                              | Verarbeitung personenbezogener Daten mit medizinischen Diagnosen, die vertraulich behandelt werden müssen (SZ1, SZ2, SZ5, SZ6). |
| P1.3                                                                                   | normal                                                                                 | Über E-Mail werden in der Regel keine vertraulichen Informationen empfangen.                                                    |
| P1.4                                                                                   | sehr hoch                                                                              | Verarbeitung personenbezogener Daten mit medizinischen Diagnosen, die vertraulich behandelt werden müssen (SZ1, SZ2, SZ5, SZ6). |
| P1.5                                                                                   | sehr hoch                                                                              | Verarbeitung personenbezogener Daten mit medizinischen Diagnosen, die vertraulich behandelt werden müssen (SZ1, SZ2, SZ5, SZ6). |
| P1.6                                                                                   | normal                                                                                 | Es werden nur technische Parameter übermittelt.                                                                                 |
| P1.7                                                                                   | normal                                                                                 | Es werden nur technische Parameter übermittelt.                                                                                 |
| P2.1                                                                                   | sehr hoch                                                                              | Verarbeitung personenbezogener Daten mit medizinischen Diagnosen (SZ1, SZ2, SZ5, SZ6).                                          |
| P2.2                                                                                   | normal                                                                                 | Es werden nur technische Parameter aufgenommen.                                                                                 |
| P3, P4                                                                                 | sehr hoch                                                                              | Verarbeitung personenbezogener Daten mit medizinischen Diagnosen (SZ1, SZ2, SZ5, SZ6).                                          |
| P5                                                                                     | hoch                                                                                   | Verarbeitung personenbezogener Daten (SZ1, SZ2, SZ5, SZ6).                                                                      |
| P6                                                                                     | normal                                                                                 | Bei Schulungen wird nicht mit produktiven Daten gearbeitet.                                                                     |

Tabelle A-14: Schutzbedarfsfeststellung der Integrität für Prozesse in der Leitstelle.

| Schutzbedarfsfeststellung der Integrität für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Integrität für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Integrität für Prozesse des Informationsverbundes                                      |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Objekt                                                                            | Schutzbedarf                                                                      | Begründung                                                                                                           |
| P1, P2, P3, P5                                                                    | sehr hoch                                                                         | Lebensbedrohliche Folgen bei Verarbeitung inkorrekter Daten oder feh- lerhaftem Verhalten (SZ1, SZ3, SZ4, SZ5, SZ6). |
| P4, P6                                                                            | normal                                                                            | Geringe Auswirkungen bei Verarbeitung inkorrekter Daten oder fehler- haftem Verhalten (SZ1, SZ6).                    |

<!-- page: 96 -->

Tabelle A-15: Schutzbedarfsfeststellung der Verfügbarkeit für Prozesse in der Leitstelle.

| Schutzbedarfsfeststellung der Verfügbarkeit für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Verfügbarkeit für Prozesse des Informationsverbundes   | Schutzbedarfsfeststellung der Verfügbarkeit für Prozesse des Informationsverbundes                               |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Objekt                                                                               | Schutzbedarf                                                                         | Begründung                                                                                                       |
| P1.1, P1.2                                                                           | sehr hoch                                                                            | Lebensbedrohliche Folgen bei Ausfall des Notrufs 112 über Telefon oder Fax (SZ1, SZ3, SZ4, SZ5, SZ6).            |
| P1.3                                                                                 | normal                                                                               | Geringe Auswirkungen, weil über E-Mail keine Notfallmeldungen einge- hen (SZ4, SZ5).                             |
| P1.4                                                                                 | normal                                                                               | Von den Rettungskräften können alternative Kommunikationswege zur Leitstelle genutzt werden (SZ4, SZ5).          |
| P1.5                                                                                 | sehr hoch                                                                            | Die Auswirkungen eines Ausfalls steigen durch Einführung der bundes- weiten Notrufapp (SZ1, SZ3, SZ4, SZ5, SZ6). |
| P1.6                                                                                 | sehr hoch                                                                            | Hoher materieller Schaden bei Ausfall der Alarmempfangseinrichtung (SZ1, SZ3, SZ4, SZ5, SZ6).                    |
| P1.7                                                                                 | sehr hoch                                                                            | Lebensbedrohliche Folgen bei Ausfall der Empfangseinrichtung für eCalls (SZ1, SZ3, SZ4, SZ5, SZ6).               |
| P2, P3                                                                               | sehr hoch                                                                            | Lebensbedrohliche Folgen bei Beeinträchtigungen von Einsatzaufnahme oder -bearbeitung (SZ1, SZ3, SZ4, SZ5, SZ6). |
| P4, P5, P6                                                                           | normal                                                                               | Geringe Auswirkungen, weil die Prozesse nicht zeitkritisch sind (SZ4, SZ6).                                      |

## 5.1.2 Schutzbedarfsfeststellung für Anwendungen

Die Schutzbedarfsfeststellung für Anwendungen richtet sind nach dem Schutzbedarf der Prozesse, die durch die Verwendung der jeweiligen Anwendung unterstützt werden. Dabei wird das Maximumprinzip berücksichtigt und der jeweils höchste Schutzbedarf durch die Anwendung geerbt. Ist der Schutzbedarf nur für einen Teil, der von den Anwendungen unterstützten Prozesse als sehr hoch eingestuft, so ist der Schutzbedarf der gesamten Anwendung als sehr hoch einzustufen.

Tabelle A-16: Schutzbedarfsfeststellung der Vertraulichkeit für Anwendungen.

| Schutzbedarfsfeststellung der Vertraulichkeit für Anwendungen   | Schutzbedarfsfeststellung der Vertraulichkeit für Anwendungen   | Schutzbedarfsfeststellung der Vertraulichkeit für Anwendungen   |
|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| Objekt                                                          | Schutzbedarf                                                    | Begründung                                                      |
| A1                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozesse P2.1, P3 und P4.           |
| A2                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozesse P1.1, P1.4 und P3.         |
| A3                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozesse P1.5 und P3.               |
| A4                                                              | hoch                                                            | Hoher Schutzbedarf für Prozess P5.1.                            |
| A5                                                              | normal                                                          | Keine Verarbeitung personenbezogener Daten.                     |
| A6                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozesse P2.1 und P3.               |
| A7                                                              | hoch                                                            | Hoher Schutzbedarf für Prozess P5.1.                            |
| A8                                                              | sehr hoch                                                       | Sehr hoher Schutzbedarf für Prozess P4.                         |

<!-- page: 97 -->

Tabelle A-17: Schutzbedarfsfeststellung der Integrität für Anwendungen.

| Schutzbedarfsfeststellung der Integrität für Anwendungen   | Schutzbedarfsfeststellung der Integrität für Anwendungen   | Schutzbedarfsfeststellung der Integrität für Anwendungen            |
|------------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------------------|
| Objekt                                                     | Schutzbedarf                                               | Begründung                                                          |
| A1                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P1.6, P1.7, P2, P3 und P5.2.   |
| A2                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P1.1, P1.4, P1.7, P3 und P5.2. |
| A3                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P1.5, P3 und P5.               |
| A4                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P1.3 und P5.1.                 |
| A5                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P2.1 und P3.                   |
| A6                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozesse P2.1, P3 und P5.               |
| A7                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozess P5.1.                           |
| A8                                                         | sehr hoch                                                  | Sehr hoher Schutzbedarf für Prozess P5.                             |

Tabelle A-18: Schutzbedarfsfeststellung der Verfügbarkeit für Anwendungen.

| Schutzbedarfsfeststellung der Verfügbarkeit für Anwendungen   | Schutzbedarfsfeststellung der Verfügbarkeit für Anwendungen   | Schutzbedarfsfeststellung der Verfügbarkeit für Anwendungen   |
|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Objekt                                                        | Schutzbedarf                                                  | Begründung                                                    |
| A1                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P1.6, P1.7, P2 und P3.   |
| A2                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P1.1, P1.7 und P3.       |
| A3                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P1.5 und P3.             |
| A4                                                            | normal                                                        | Normaler Schutzbedarf für Prozesse P1.3 und P5.1.             |
| A5                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P2.1 und P3.             |
| A6                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für Prozesse P2.1 und P3.             |
| A7                                                            | normal                                                        | Normaler Schutzbedarf für Prozess P5.1.                       |
| A8                                                            | normal                                                        | Normaler Schutzbedarf für Prozesse P5 und P5.                 |

## 5.1.3 Schutzbedarfsfeststellung für IT-Systeme

Der Schutzbedarf für die IT-Systeme einer Rettungsleitstelle richtet sich nach den Anwendungen, die auf den IT-Systemen installiert sind oder mit diesen verbunden sind. Nach dem Maximumprinzip muss der Schutzbedarf auch wieder mindestens so hoch angesetzt werden, wie für diese Anwendungen.

<!-- page: 98 -->

| Schutzbedarfsfeststellung der Vertraulichkeit für IT-Systeme   | Schutzbedarfsfeststellung der Vertraulichkeit für IT-Systeme   | Schutzbedarfsfeststellung der Vertraulichkeit für IT-Systeme   |
|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Objekt                                                         | Schutzbedarf                                                   | Begründung                                                     |
| S1.1                                                           | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A2, A3, A5, A6, A8             |
| S1.2                                                           | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A2                             |
| S2                                                             | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A2                             |
| S3                                                             | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A2, A3, A5, A6, A8             |
| S4                                                             | sehr hoch                                                      | Sehr hoher Schutzbedarf für P1.2                               |
| S5                                                             | sehr hoch                                                      | Sehr hoher Schutzbedarf für A1, A6                             |

Tabelle A-19: Schutzbedarfsfeststellung der Vertraulichkeit für IT-Systeme.

Tabelle A-20: Schutzbedarfsfeststellung der Integrität für IT-Systeme.

| Schutzbedarfsfeststellung der Integrität für IT-Systeme   | Schutzbedarfsfeststellung der Integrität für IT-Systeme   | Schutzbedarfsfeststellung der Integrität für IT-Systeme    |
|-----------------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------|
| Objekt                                                    | Schutzbedarf                                              | Begründung                                                 |
| S1.1                                                      | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A2, A3, A4, A5, A6, A7, A8 |
| S1.2                                                      | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A2                         |
| S2                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A2                         |
| S3                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A2, A3, A4, A5, A6, A7, A8 |
| S4                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für P1.2                           |
| S5                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für A1, A6, A7                     |

Tabelle A-21: Schutzbedarfsfeststellung der Verfügbarkeit für IT-Systeme.

| Schutzbedarfsfeststellung der Verfügbarkeit für IT-Systeme   | Schutzbedarfsfeststellung der Verfügbarkeit für IT-Systeme   | Schutzbedarfsfeststellung der Verfügbarkeit für IT-Systeme   |
|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Objekt                                                       | Schutzbedarf                                                 | Begründung                                                   |
| S1.1                                                         | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A2, A3, A5, A6               |
| S1.2                                                         | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A2                           |
| S2                                                           | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A2                           |
| S3                                                           | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A2, A3, A5, A6               |
| S4                                                           | sehr hoch                                                    | Sehr hoher Schutzbedarf für P1.2                             |
| S5                                                           | sehr hoch                                                    | Sehr hoher Schutzbedarf für A1, A6                           |

## 5.1.4 Schutzbedarfsfeststellung für Netzwerke

Viele Anwendungen und IT-Systeme, die in der Rettungsleitstelle verwendet werden, übermitteln und empfangen Daten über die in Abschnitt  4.4  definierten Netze und Netzkomponenten. Der Schutzbedarf   der   Netze   und   Netzkomponenten   ist   somit   abhängig   vom   Schutzbedarf   der Anwendungen und IT-Systeme, die über diese Netze Daten übermitteln und empfangen.

<!-- page: 99 -->

| Schutzbedarfsfeststellung der Vertraulichkeit für Netzwerke   | Schutzbedarfsfeststellung der Vertraulichkeit für Netzwerke   | Schutzbedarfsfeststellung der Vertraulichkeit für Netzwerke   |
|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Objekt                                                        | Schutzbedarf                                                  | Begründung                                                    |
| N1                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A1                                |
| N2                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A2                                |
| N3                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A3, A5, A6, A8                    |
| N4                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A1, A2, A3, A4                    |
| N5                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für N1, N2 und N3                     |
| N6                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für N1, N2 und N3                     |
| N7                                                            | sehr hoch                                                     | Sehr hoher Schutzbedarf für A1                                |

## Tabelle A-22: Schutzbedarfsfeststellung der Vertraulichkeit für Netzwerke.

| Schutzbedarfsfeststellung der Integrität für Netzwerke   | Schutzbedarfsfeststellung der Integrität für Netzwerke   | Schutzbedarfsfeststellung der Integrität für Netzwerke   |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Objekt                                                   | Schutzbedarf                                             | Begründung                                               |
| N1                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A1                           |
| N2                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A2                           |
| N3                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A3, A5, A6, A7, A8           |
| N4                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A1, A2, A3                   |
| N5                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für N1, N2 und N3                |
| N6                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für N1, N2 und N3                |
| N7                                                       | sehr hoch                                                | Sehr hoher Schutzbedarf für A1                           |

## Tabelle A-23: Schutzbedarfsfeststellung der Integrität für Netzwerke.

| Schutzbedarfsfeststellung der Verfügbarkeit für Netzwerke   | Schutzbedarfsfeststellung der Verfügbarkeit für Netzwerke   | Schutzbedarfsfeststellung der Verfügbarkeit für Netzwerke   |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| Objekt                                                      | Schutzbedarf                                                | Begründung                                                  |
| N1                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A1                              |
| N2                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A2                              |
| N3                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A3, A5, A6                      |
| N4                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A1, A2, A3                      |
| N5                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für N1, N2 und N3                   |
| N6                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für N1, N2 und N3                   |
| N7                                                          | sehr hoch                                                   | Sehr hoher Schutzbedarf für A1                              |

## Tabelle A-24: Schutzbedarfsfeststellung der Verfügbarkeit für Netzwerke.

<!-- page: 100 -->

## 5.1.5 Schutzbedarfsfeststellung für Räume

Die Schutzbedarfsfeststellung für Räume richtet sich nach den IT-Systemen, die in dem betrachteten Raum installiert sind und den Prozessen, die in diesen Räumen durchgeführt werden. Je höher deren Schutzbedarf ist, desto höher ist auch der Schutzbedarf für den Raum einzustufen. Dabei ist bei der Festlegung des Schutzbedarfs auch die Menge an Systemen zu berücksichtigen, die in dem Raum installiert sind.

| Schutzbedarfsfeststellung der Vertraulichkeit für Räume   | Schutzbedarfsfeststellung der Vertraulichkeit für Räume   | Schutzbedarfsfeststellung der Vertraulichkeit für Räume   |
|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Objekt                                                    | Schutzbedarf                                              | Begründung                                                |
| R1                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für P1, P2, P3, S3, S4, S5        |
| R2                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für S2                            |
| R3                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für S3, S4, S5 und P5             |
| R4                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für N2                            |
| R5                                                        | sehr hoch                                                 | Sehr hoher Schutzbedarf für P4                            |
| R6                                                        | normal                                                    | Normaler Schutzbedarf für P6                              |

Tabelle A-25: Schutzbedarfsfeststellung der Vertraulichkeit für Räume.

Tabelle A-26: Schutzbedarfsfeststellung der Integrität für Räume.

| Schutzbedarfsfeststellung der Integrität für Räume   | Schutzbedarfsfeststellung der Integrität für Räume   | Schutzbedarfsfeststellung der Integrität für Räume   |
|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| Objekt                                               | Schutzbedarf                                         | Begründung                                           |
| R1                                                   | sehr hoch                                            | Sehr hoher Schutzbedarf für S3, S4, S5               |
| R2                                                   | sehr hoch                                            | Sehr hoher Schutzbedarf für S2                       |
| R3                                                   | sehr hoch                                            | Sehr hoher Schutzbedarf für S3, S4, S5               |
| R4                                                   | sehr hoch                                            | Sehr hoher Schutzbedarf für N2                       |
| R5                                                   | normal                                               | Normaler Schutzbedarf für P4                         |
| R6                                                   | normal                                               | Normaler Schutzbedarf für P6                         |

Tabelle A-27: Schutzbedarfsfeststellung der Verfügbarkeit für Räume.

| Schutzbedarfsfeststellung der Verfügbarkeit für Räume   | Schutzbedarfsfeststellung der Verfügbarkeit für Räume   | Schutzbedarfsfeststellung der Verfügbarkeit für Räume   |
|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Objekt                                                  | Schutzbedarf                                            | Begründung                                              |
| R1                                                      | sehr hoch                                               | Sehr hoher Schutzbedarf für P1, P2 und P3               |
| R2                                                      | sehr hoch                                               | Sehr hoher Schutzbedarf für S2                          |
| R3                                                      | normal                                                  | Nutzung alternativer Räume möglich                      |
| R4                                                      | sehr hoch                                               | Sehr hoher Schutzbedarf für N4                          |
| R5                                                      | normal                                                  | Normaler Schutzbedarf für P4                            |
| R6                                                      | normal                                                  | Normaler Schutzbedarf für P6                            |

<!-- page: 101 -->

## 5.2 Auswahl relevanter Bausteinen

Das IT-Grundschutz-Kompendium des BSI stellt Bausteine bereit, die anwendungsbezogene Empfehlungen zur Umsetzung des IT-Grundschutz geben. Nachdem im letzten Abschnitt der Schutzbedarf   der   Prozesse,  Anwendungen,   IT-Systeme   und   Kommunikationsverbindungen   festgestellt worden ist, müssen im nächsten Schritt die relevanten Bausteine identifiziert und eine Anpassung der Anforderungen an die entsprechende Zielgruppe durchgeführt werden. Das Resultat der Anpassung der Anforderungen kann bedeuten, dass alle oder nur bestimmte Anforderungen des Bausteins für die Informationssicherheit in Rettungsleitstellen relevant sind. Ebenso können Anforderungen als komplett irrelevant eingestuft werden. Auch die Relevanz der in den Anforderungen aufgeführten Maßnahmen muss identifiziert werden. Zusätzlich werden Vorgaben zur Umsetzung der Anforderungen der Bausteine beschrieben. Die Bausteine aus der Rubrik Industrielle IT werden mangels Relevanz für den Betrieb von Rettungsleitstellen von vornherein nicht mit aufgeführt.

| Baustein                           | Baustein                                              | Relevant?   | Begründung (falls nicht relevant)                                |
|------------------------------------|-------------------------------------------------------|-------------|------------------------------------------------------------------|
| ISMS: Sicherheitsmanagement        | ISMS: Sicherheitsmanagement                           |             |                                                                  |
| ISMS.1                             | Sicherheitsmanagement                                 | Ja          |                                                                  |
| ORP: Organisation und Personal     | ORP: Organisation und Personal                        |             |                                                                  |
| ORP.1                              | Organisation                                          | Ja          |                                                                  |
| ORP.2                              | Personal                                              | Ja          |                                                                  |
| ORP.3                              | Sensibilisierung und Schu- lung                       | Ja          |                                                                  |
| ORP.4                              | Identitäts- und Berechti- gungsmanagement             | Ja          |                                                                  |
| ORP.5                              | Comliance Management (Anforderungsmanagement)         | Ja          |                                                                  |
| CON: Konzeption und Vorgehensweise | CON: Konzeption und Vorgehensweise                    |             |                                                                  |
| CON.1                              | Kryptokonzept                                         | Ja          |                                                                  |
| CON.2                              | Datenschutz                                           | Ja          |                                                                  |
| CON.3                              | Datensicherungskonzept                                | Ja          |                                                                  |
| CON.4                              | Auswahl und Einsatz von Standardsoftware              | Ja          |                                                                  |
| CON.5                              | Entwicklung und Einsatz von Allgemeinen Anwen- dungen | Ja          |                                                                  |
| CON.6                              | Löschen und Vernichten                                | Ja          |                                                                  |
| CON.7                              | Informationssicherheit auf Auslandsreisen             | Nein        | Rettungsleitstellen arbeiten üblicherweise ausschließlich lokal. |

<!-- page: 102 -->

| OPS: Betrieb                | OPS: Betrieb                                      | OPS: Betrieb                | OPS: Betrieb                                                                                                                |
|-----------------------------|---------------------------------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| OPS.1.1.2                   | Ordnungsgemäße IT-Admi- nistration                | Ja                          |                                                                                                                             |
| OPS.1.1.3                   | Patch- und Änderungs- management                  | Ja                          |                                                                                                                             |
| OPS.1.1.4                   | Schutz vor Schadprogram- men                      | Ja                          |                                                                                                                             |
| OPS.1.1.5                   | Protokollierung                                   | Ja                          |                                                                                                                             |
| OPS.1.1.6                   | Software-Tests und -Freigaben                     | Ja                          |                                                                                                                             |
| OPS.1.2.2                   | Archivierung                                      | Ja                          |                                                                                                                             |
| OPS.1.2.3                   | Informations- und Datenträ- geraustausch          | Ja                          |                                                                                                                             |
| OPS.1.2.4                   | Telearbeit                                        | Nein                        | Die Mitarbeiter einer Rettungsleitstelle arbei- ten üblicherweise ausschließlich in den Ge- schäftsräumen des Arbeitgebers. |
| OPS.2.1                     | Outsourcing für Kunden                            | Ja                          |                                                                                                                             |
| OPS.2.2                     | Cloud-Nutzung                                     | Nein                        | Der Betrieb der IT-Systeme findet in Ret- tungsleitstellen üblicherweise lokal statt.                                       |
| OPS.2.4                     | Fernwartung                                       | Ja                          |                                                                                                                             |
| OPS.3.1                     | Outsourcing für Dienst- leister                   | Nein                        | Rettungsleitstellen übernehmen üblicher- weise keine ausgelagerten Dienstleistungen für andere Institutionen.               |
| DER: Detektion und Reaktion | DER: Detektion und Reaktion                       | DER: Detektion und Reaktion | DER: Detektion und Reaktion                                                                                                 |
| DER.1                       | Detektion von sicherheits- relevanten Ereignissen | Ja                          |                                                                                                                             |
| DER.2.1                     | Behandlung von Sicher- heitsvorfällen             | Ja                          |                                                                                                                             |
| DER.2.2                     | Vorsorge für die IT-Forensik                      | Ja                          |                                                                                                                             |
| DER.2.3                     | Bereinigung weitreichender Sicherheitsvorfälle    | Ja                          |                                                                                                                             |
| DER.3.1                     | Audits und Revisionen                             | Ja                          |                                                                                                                             |
| DER.3.2                     | Revision auf Basis des Leit- fadens IS-Revision   | Ja                          |                                                                                                                             |
| DER.4                       | Notfallmanagement                                 | Ja                          |                                                                                                                             |

## Tabelle A-28: Relevanz der Prozessbausteine des IT-Grundschutz-Kompendium des BSI.

In der folgenden Tabelle werden die Systembausteine aufgeführt. Hier ist entscheidend, ob der Baustein für eine spezifische, in Abschnitt 4 bestimmte, Komponente relevant ist.

<!-- page: 103 -->

| Baustein         | Baustein                        | Relevant?        | Begründung (falls nicht relevant)                                                                                                                           |
|------------------|---------------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APP: Anwendungen | APP: Anwendungen                | APP: Anwendungen | APP: Anwendungen                                                                                                                                            |
| APP.1.1          | Office-Produkte                 | Ja               |                                                                                                                                                             |
| APP.1.2          | Web-Browser                     | Ja               |                                                                                                                                                             |
| APP.1.4          | Mobile Anwendung (Apps)         | Nein             | Für Apps zur Alarmierung der angebundenen Organisationen oder Notruf-Apps liegt die Verantwortung bei den jeweiligen Betreibern und Nutzern.                |
| APP.2.1          | Allgemeiner Verzeichnis- dienst | Nein             | Insbesondere in kleineren Leitstellen kann z.B. eine Benutzerverwaltung rein auf der Ebene von ELS und KMS durchgeführt werden.                             |
| APP.2.2          | Active Directory                | Nein             | Siehe APP.2.1                                                                                                                                               |
| APP.2.3          | OpenLDAP                        | Nein             | Siehe APP.2.1                                                                                                                                               |
| APP.3.1          | Webanwendungen                  | Nein             | Eigene Webwendungen sind in der Regel nicht erforderlich.                                                                                                   |
| APP.3.2          | Webserver                       | Nein             | Für den Betrieb der Leitstelle in der Regel nicht erforderlich.                                                                                             |
| APP.3.3          | Fileserver                      | Ja               |                                                                                                                                                             |
| APP.3.4          | Samba                           | Nein             | Für den Betrieb der Leitstelle in der Regel nicht erforderlich.                                                                                             |
| APP.3.6          | DNS-Server                      | Nein             | DNS kann in Leitstellen in der Regel als Teil- prozess auf Router oder Firewall betrieben werden.                                                           |
| APP.4.2          | SAP-ERP-System                  | Nein             | In Leitstellen üblicherweise nicht vorhanden.                                                                                                               |
| APP.4.3          | Relationale Datenbank- systeme  | Ja               | Wird von ELS und KMS verwendet.                                                                                                                             |
| APP.4.6          | SAP ABAP-Programmie- rung       | Nein             | In Leitstellen üblicherweise nicht vorhanden.                                                                                                               |
| APP.5.1          | Allgemeine Groupware            | Ja               |                                                                                                                                                             |
| APP.5.2          | Microsoft Exchange und Outlook  | Nein             | Nicht zwingend erforderlich, sofern kein Ex- change/Outlook eingesetzt wird. Alternative E- Mailclients beachten (z.B. Thunderbird, Lotus Notes, Groupwise) |
| SYS: IT-Systeme  | SYS: IT-Systeme                 | SYS: IT-Systeme  | SYS: IT-Systeme                                                                                                                                             |
| SYS.1.1          | Allgemeine Server               | Ja               |                                                                                                                                                             |
| SYS.1.2          | Windows Server 2012             | Nein             | Für den Betrieb der Leitstelle nicht zwingend erforderlich.                                                                                                 |
| SYS.1.3          | Server unter Unix               | Nein             | Für den Betrieb der Leitstelle nicht zwingend erforderlich.                                                                                                 |

<!-- page: 104 -->

| SYS.1.5                      | Virtualisierung                            | Nein                         | Für den Betrieb der Leitstelle nicht zwingend erforderlich.                                                                                              |
|------------------------------|--------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYS.1.7                      | IBM Z-System                               | Nein                         | In Rettungsleitstellen üblicherweise nicht vor- handen.                                                                                                  |
| SYS.1.8                      | Speicherlösungen                           | Nein                         | Für den Betrieb der Anwendungen in der Leitstelle in der Regel nicht erforderlich, weil Speichermedien direkt an die Server angeschlossen werden können. |
| SYS.2.1                      | Allgemeiner Client                         | Ja                           |                                                                                                                                                          |
| SYS.2.2.2                    | Clients unter Windows 8.1                  | Nein                         | Nutzung anderer Windows-Betriebssysteme möglich.                                                                                                         |
| SYS.2.2.3                    | Clients unter Windows 10                   | Ja                           |                                                                                                                                                          |
| SYS.2.3                      | Clients unter Unix                         | Nein                         | Üblicherweise nicht vorhanden, weil ELS- und KMS-Clients meistens Windows benötigen.                                                                     |
| SYS.2.4                      | Clients unter macOS                        | Nein                         | Üblicherweise nicht vorhanden, weil ELS- und KMS-Clients meistens Windows benötigen.                                                                     |
| SYS.3.1                      | Laptops                                    | Nein                         | Für Betrieb der Leitstelle nicht erforderlich.                                                                                                           |
| SYS.3.2.1                    | Allgemeine Smartphones und Tablets         | Nein                         | In Leitstellen üblicherweise nicht vorhanden.                                                                                                            |
| SYS.3.2.2                    | Mobile Device Manage- ment (MDM)           | Nein                         | Für Betrieb der Leitstelle nicht erforderlich.                                                                                                           |
| SYS.3.2.3                    | iOS (for Enterprise)                       | Nein                         | In Leitstellen üblicherweise nicht vorhanden.                                                                                                            |
| SYS.3.2.4                    | Android                                    | Nein                         | In Leitstellen üblicherweise nicht vorhanden.                                                                                                            |
| SYS.3.3                      | Mobiltelefon                               | Nein                         | In Leitstellen üblicherweise nicht vorhanden.                                                                                                            |
| SYS.3.4                      | Mobile Datenträger                         | Ja                           |                                                                                                                                                          |
| SYS.4.1                      | Drucker, Kopierer und Multifunktionsgeräte | Ja                           |                                                                                                                                                          |
| SYS.4.3                      | Eingebettete Systeme                       | Nein                         | In Leitstellen üblicherweise nicht vorhanden.                                                                                                            |
| SYS.4.4                      | Allgemeines IoT-Gerät                      | Nein                         | In Leitstellen üblicherweise nicht vorhanden.                                                                                                            |
| NET: Netze und Kommunikation | NET: Netze und Kommunikation               | NET: Netze und Kommunikation | NET: Netze und Kommunikation                                                                                                                             |
| NET.1.1                      | Netzwerkarchitektur und -design            | Ja                           |                                                                                                                                                          |
| NET.1.2                      | Netzmanagement                             | Ja                           |                                                                                                                                                          |
| NET.2.1                      | WLAN-Betrieb                               | Nein                         | Für Betrieb der Leitstelle nicht erforderlich, weil ausschließlich festangebundene lokale Arbeitsplätze genutzt werden.                                  |
| NET.2.2                      | WLAN-Nutzung                               | Nein                         | Siehe NET.2.1                                                                                                                                            |
| NET.3.1                      | Router und Switches                        | Ja                           |                                                                                                                                                          |
| NET.3.2                      | Firewall                                   | Ja                           |                                                                                                                                                          |

<!-- page: 105 -->

Tabelle A-29: Relevanz der Systembausteine des IT-Grundschutz-Kompendium des BSI.

| NET.3.3            | VPN                                                | Ja                 |                                                                                                                             |
|--------------------|----------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|
| NET.4.1            | TK-Anlagen                                         | Ja                 |                                                                                                                             |
| NET.4.2            | VoIP                                               | Ja                 |                                                                                                                             |
| NET.4.3            | Faxgeräte und Faxserver                            | Ja                 |                                                                                                                             |
| INF: Infrastruktur | INF: Infrastruktur                                 | INF: Infrastruktur | INF: Infrastruktur                                                                                                          |
| INF.1              | Allgemeines Gebäude                                | Ja                 |                                                                                                                             |
| INF.2              | Rechenzentrum sowie Ser- verraum                   | Ja                 |                                                                                                                             |
| INF.3              | Elektrotechnische Verka- belung                    | Ja                 |                                                                                                                             |
| INF.4              | IT-Verkabelung                                     | Ja                 |                                                                                                                             |
| INF.6              | Datenträgerarchiv                                  | Ja                 |                                                                                                                             |
| INF.7              | Büroarbeitsplatz                                   | Ja                 |                                                                                                                             |
| INF.8              | Häuslicher Arbeitsplatz                            | Nein               | Die Mitarbeiter einer Rettungsleitstelle arbei- ten üblicherweise ausschließlich in den Ge- schäftsräumen des Arbeitgebers. |
| INF.9              | Mobiler Arbeitsplatz                               | Nein               | Abweichend kann es in einigen Leitstellen mo- bile Arbeitsplätze z.B. im ELW geben.                                         |
| INF.10             | Besprechungs-, Veranstal- tungs- und Schulungsraum | Ja                 |                                                                                                                             |

## 5.3 Anforderungen übergreifend gültiger Prozessbausteine

Im nächsten Schritt werden die Anforderungen der relevanten Bausteine geprüft. Sofern notwendig werden sie an die Rahmenbedingungen in Rettungsleitstellen angepasst. Aufgeführt sind Basis- und Standard-Anforderungen. Sind bei einzelnen Bausteinen auch die Anforderungen für erhöhten Schutzbedarf zu erfüllen, werden diese extra benannt.

| ISMS.1 Sicherheitsmanagement   | ISMS.1 Sicherheitsmanagement                                                                                                                                                                                                             |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen                  | ISMS.1.A1 - A15                                                                                                                                                                                                                          |
| Umsetzungs- vorgaben           | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                                                                                             |
| Hinweise                       | A4: Der Informationssicherheitsbeauftragte kann je nach Größenordnung der Ret- tungsleitstelle auch weitere Funktionen in Personalunion ausüben.                                                                                         |
|                                | A10: Bei der Erstellung eines Sicherheitskonzepts empfiehlt es sich mit den Be- reichen der Leitstelle zu beginnen, die das höchste Schutzniveau erfordern. Anschließend kann das Sicherheitskonzept um weitere Bereiche ergänzt werden. |

<!-- page: 106 -->

| ORP.1 Organisation   | ORP.1 Organisation                                                                                                                                                                                                                             |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen        | ORP.1.A1 - A13                                                                                                                                                                                                                                 |
| Umsetzungs- vorgaben | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                                                                                                   |
| Hinweise             | ORP.1.A12 Sofern eine Beeinträchtigung des Betriebs der Leitstelle unvermeidbar ist, sind Wartungs- und Reparaturarbeiten, sofern möglich, zu Tageszeiten durch- zuführen, in denen mit weniger Einsätzen gerechnet werden kann (z.B. nachts). |

| ORP.2 Personal       | ORP.2 Personal                                               |
|----------------------|--------------------------------------------------------------|
| Anforderungen        | ORP.2.A1 - A10                                               |
| Umsetzungs- vorgaben | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| ORP.3 Sensibilisierung und Schulung   | ORP.3 Sensibilisierung und Schulung                                                                                                                           |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen                         | ORP.3.A1 - A8                                                                                                                                                 |
| Umsetzungs- vorgaben                  | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                  |
| Hinweise                              | ORP.3.A4 Die Landesschulen für Feuerwehr und Rettungsdienst können im Rah- men der Aus- und Fortbildungen für Leitstellendisponenten mit einbezogen wer- den. |

| ORP.4 Identitäts- und Berechtigungsmanagement   | ORP.4 Identitäts- und Berechtigungsmanagement                |
|-------------------------------------------------|--------------------------------------------------------------|
| Anforderungen                                   | ORP.4.A1 - A19                                               |
| Umsetzungs- vorgaben                            | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| ORP.5 Compliance Management (Anforderungsmanagement)   | ORP.5 Compliance Management (Anforderungsmanagement)                                                                                                                                                                                                |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen                                          | ORP.5.A1 - A8                                                                                                                                                                                                                                       |
| Umsetzungs- vorgaben                                   | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                                                                                                        |
| Hinweise                                               | ORP.5.A1 Das Personal der Leitstelle muss auf die Dokumentation der Vorgaben schnellen Zugriff haben.                                                                                                                                               |
|                                                        | ORP.5.A3 Neben den entscheidenden Stellen in den Gesetzen zum Datenschutz (Datenschutz Grundverordnung und Ländergesetze) umfasst dies für das Personal der Leitstelle auch Teile der Ländergesetze zur Gefahrenabwehr und des Straf- gesetzbuches. |

<!-- page: 107 -->

| CON.1 Kryptokonzept   | CON.1 Kryptokonzept                                          |
|-----------------------|--------------------------------------------------------------|
| Anforderungen         | CON.1.A1 - A6                                                |
| Umsetzungs- vorgaben  | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| CON.2 Datenschutz    | CON.2 Datenschutz                                            |
|----------------------|--------------------------------------------------------------|
| Anforderungen        | CON.2.A1                                                     |
| Umsetzungs- vorgaben | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| CON.3 Datensicherungskonzept   | CON.3 Datensicherungskonzept                                                                                                       |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen                  | CON.3.A1 - A12                                                                                                                     |
| Umsetzungs- vorgaben           | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                       |
| Hinweise                       | CON3.A.3 Die Regelungen zur Speicherdauer von Notrufen in den Gesetzen der Länder sind zu beachten.                                |
| Hinweise                       | CON.3.A12 Als geografisch entfernter Aufbewahrungsort kann zum Beispiel eine definierte Ersatznotrufabfragestelle bestimmt werden. |

| CON.4 Auswahl und Einsatz von Standardsoftware   | CON.4 Auswahl und Einsatz von Standardsoftware                                                                                                                                        |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen                                    | CON.4.A1 - A9                                                                                                                                                                         |
| Umsetzungs- vorgaben                             | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                                          |
| Hinweise                                         | Die Anforderungen dieses Bausteins können zum Beispiel auf Office- Anwendungen, Webbrowser oder PDF-Viewer bezogen werden. Für ELS und KMS sollte Baustein CON.5 herangezogen werden. |

| CON.5 Entwicklung und Einsatz von Allgemeinen Anwendungen   | CON.5 Entwicklung und Einsatz von Allgemeinen Anwendungen                                                        |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Anforderungen                                               | CON.5.A1 - A10                                                                                                   |
| Umsetzungs- vorgaben                                        | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                     |
| Hinweise                                                    | Die Anforderungen dieses Bausteins können zum Beispiel auf Einsatzleit- und Kommunikationssystem bezogen werden. |

| CON.6 Löschen und Vernichten   | CON.6 Löschen und Vernichten                                 |
|--------------------------------|--------------------------------------------------------------|
| Anforderungen                  | CON.6.A1 - A8                                                |
| Umsetzungs- vorgaben           | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

<!-- page: 108 -->

| OPS.1.1.2 Ordnungsgemäße IT-Administration   | OPS.1.1.2 Ordnungsgemäße IT-Administration                                                                                                                                                                                   |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen                                | OPS.1.1.2.A1 - A13                                                                                                                                                                                                           |
| Umsetzungs- vorgaben                         | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                                                                                 |
| Hinweise                                     | OPS.1.1.2.A1 Auch wenn die Tätigkeiten der Administration durch Disponenten in Personalunion durchgeführt werden, ist auf Rollentrennung zu achten. Der Dis- ponent sollte nicht mit Administrationsrechten eingeloggt sein. |

| OPS.1.1.3 Patch- und Änderungsmanagement   | OPS.1.1.3 Patch- und Änderungsmanagement                                                                                                                                                                                                                           |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen                              | OPS.1.1.3.A1 - A11                                                                                                                                                                                                                                                 |
| Umsetzungs- vorgaben                       | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                                                                                                                       |
| Hinweise                                   | OPS.1.1.3.A7 Die Erreichbarkeit des Supports sollte bei und unmittelbar nach der Installation von Patches gewährleistet sein. Eine Installation vor Wochenenden, Feiertagen oder Terminen, die eine hohe Einsatzanzahl erwarten lassen, sollte ver- mieden werden. |
| Hinweise                                   | OPS.1.1.3.A9 Nach Möglichkeit können Änderungen zunächst an einem Schu- lungssystem getestet werden, bevor sie in das Produktivsystem übernommen wer- den.                                                                                                         |

| OPS.1.1.4 Schutz vor Schadprogrammen   | OPS.1.1.4 Schutz vor Schadprogrammen                                                                                                                         |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen                          | OPS.1.1.4.A1 - A9                                                                                                                                            |
| Umsetzungs- vorgaben                   | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                 |
| Hinweise                               | OPS.1.1.4.A5 Um Funktionseinschränkungen zu vermeiden, sollte die Auswahl des Viren-Schutzprogramms mit den Herstellern von ELS und KMS abgesprochen werden. |

| OPS.1.1.5 Protokollierung   | OPS.1.1.5 Protokollierung                                    |
|-----------------------------|--------------------------------------------------------------|
| Anforderungen               | OPS.1.1.5.A1 - A10                                           |
| Umsetzungs- vorgaben        | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| OPS.1.1.6 Software-Tests und -Freigaben   | OPS.1.1.6 Software-Tests und -Freigaben                                                  |
|-------------------------------------------|------------------------------------------------------------------------------------------|
| Anforderungen                             | OPS.1.1.6.A1 - A13                                                                       |
| Umsetzungs- vorgaben                      | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                             |
| Hinweise                                  | OPS.1.1.6.A11 Empfohlen wird die Nutzung separater Testsystem-Instanzen von ELS und KMS. |

<!-- page: 109 -->

| OPS.1.2.2 Archivierung   | OPS.1.2.2 Archivierung                                                                                                                             |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen            | OPS.1.2.2.A1 - A19                                                                                                                                 |
| Umsetzungs- vorgaben     | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                       |
| Hinweise                 | OPS.1.2.2.A9 Bei einem Wechsel des Einsatzleitsystems muss darauf geachtet werden, den Zugriff auf die Einsatzdaten des alten Systems zu behalten. |

| OPS.1.2.3 Informations- und Datenträgeraustausch   | OPS.1.2.3 Informations- und Datenträgeraustausch             |
|----------------------------------------------------|--------------------------------------------------------------|
| Anforderungen                                      | OPS.1.2.3.A1 - A12                                           |
| Umsetzungs- vorgaben                               | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| OPS.2.1 Outsourcing für Kunden   | OPS.2.1 Outsourcing für Kunden                                                                                                    |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen                    | OPS.2.1.A1 - A15                                                                                                                  |
| Umsetzungs- vorgaben             | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                      |
| Hinweise                         | Dieser Baustein betrifft eine Leitstelle zum Beispiel bei der Auslagerung der IT- Administration zu einem externen Dienstleister. |

| OPS.2.4 Fernwartung   | OPS.2.4 Fernwartung                                                                                                                                          |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anforderungen         | OPS.2.4.A1 - A20                                                                                                                                             |
| Umsetzungs- vorgaben  | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                 |
| Hinweise              | Der Baustein ist relevant, wenn externe IT-Dienstleister oder die Hersteller von ELS und KMS Wartungsarbeiten per Fernwartung in der Leitstelle durchführen. |
| Hinweise              | OPS.2.4.A14 Um auch Probleme beim Internetzugang beheben zu können, ist ein dedizierter Internetzugang bei externen Fernwartungen zu empfehlen.              |

| DER.1 Detektion von sicherheitsrelevanten Ereignissen   | DER.1 Detektion von sicherheitsrelevanten Ereignissen        |
|---------------------------------------------------------|--------------------------------------------------------------|
| Anforderungen                                           | DER.1.A1 - A13                                               |
| Umsetzungs- vorgaben                                    | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| DER.2.1 Behandlung von Sicherheitsvorfällen   | DER.2.1 Behandlung von Sicherheitsvorfällen                                                   |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------|
| Anforderungen                                 | DER.2.1.A1 - A18                                                                              |
| Umsetzungs- vorgaben                          | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                  |
| Hinweise                                      | DER.2.1.A6 Eine Inbetriebnahme der Ersatznotrufabfragestelle kann in Betracht gezogen werden. |

<!-- page: 110 -->

| DER.2.2 Vorsorge für die IT-Forensik   | DER.2.2 Vorsorge für die IT-Forensik                         |
|----------------------------------------|--------------------------------------------------------------|
| Anforderungen                          | DER.2.2.A1 - A12                                             |
| Umsetzungs- vorgaben                   | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle   | DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle       |
|----------------------------------------------------------|--------------------------------------------------------------|
| Anforderungen                                            | DER.2.3.A1 - A8                                              |
| Umsetzungs- vorgaben                                     | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| DER.3.1 Audits und Revisionen   | DER.3.1 Audits und Revisionen                                |
|---------------------------------|--------------------------------------------------------------|
| Anforderungen                   | DER.3.1.A1 - A27                                             |
| Umsetzungs- vorgaben            | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| DER.3.2 Revisionen auf Basis des Leitfadens IS-Revision   | DER.3.2 Revisionen auf Basis des Leitfadens IS-Revision      |
|-----------------------------------------------------------|--------------------------------------------------------------|
| Anforderungen                                             | DER.3.2.A1 - A22                                             |
| Umsetzungs- vorgaben                                      | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| DER.4 Notfallmanagement   | DER.4 Notfallmanagement                                      |
|---------------------------|--------------------------------------------------------------|
| Anforderungen             | DER.4.A1 - A2                                                |
| Umsetzungs- vorgaben      | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |
| Hinweise                  | Siehe hierzu Kapitel 8.                                      |

## 5.4 Anforderungen spezifisch gültiger Prozessbausteine

Die folgenden aufgeführten Bausteine betreffen nur die jeweils angegebenen Zielobjekte. Erfüllt werden müssen in der Regel die Basis- und Standard-Anforderungen. Sind bei einzelnen Bausteinen zusätzlich die Anforderungen für erhöhten Schutzbedarf zu erfüllen, werden diese extra benannt.

| APP.1.1 Office-Produkte   | APP.1.1 Office-Produkte                                                                                                                           |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Zielobjekte               | S3                                                                                                                                                |
| Anforderungen             | APP.1.1.A1 - A14                                                                                                                                  |
| Umsetzungs- vorgaben      | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                      |
| Hinweise                  | A9: Ein geeignetes Format für die Weitergabe von Dokumenten, die vom Empfän- ger nicht bearbeitet werden müssen, ist zum Beispiel das PDF-Format. |

<!-- page: 111 -->

| APP.1.2 Web-Browser   | APP.1.2 Web-Browser                                                             |
|-----------------------|---------------------------------------------------------------------------------|
| Zielobjekte           | P1.5, A3                                                                        |
| Anforderungen         | Zu den Basis- und Standardanforderungen ist zusätzlich APP.1.2.A12 zu erfüllen. |
| Umsetzungs- vorgaben  | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                    |

| APP.3.3 Fileserver   | APP.3.3 Fileserver                                           |
|----------------------|--------------------------------------------------------------|
| Zielobjekte          | A8, N3                                                       |
| Anforderungen        | APP.3.3.A1 - A11                                             |
| Umsetzungs- vorgaben | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| APP.4.3 Relationale Datenbanksysteme   | APP.4.3 Relationale Datenbanksysteme                                                                         |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Zielobjekte                            | A1, A2                                                                                                       |
| Anforderungen                          | APP.4.3.A1 - A20                                                                                             |
| Umsetzungs- vorgaben                   | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                 |
| Hinweise                               | APP.4.3.A10 Die Auswahl des Datenbanksystems für ELS und KMS muss in Absprache mit den Herstellern erfolgen. |

| APP.5.1 Allgemeine Groupware   | APP.5.1 Allgemeine Groupware                                 |
|--------------------------------|--------------------------------------------------------------|
| Zielobjekte                    | A4, N3                                                       |
| Anforderungen                  | APP.5.1.A1 - A19                                             |
| Umsetzungs- vorgaben           | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| SYS.1.1 Allgemeiner Server   | SYS.1.1 Allgemeiner Server                                   |
|------------------------------|--------------------------------------------------------------|
| Zielobjekte                  | S1.2, S2.1                                                   |
| Anforderungen                | SYS.1.1.A1 - A25                                             |
| Umsetzungs- vorgaben         | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| SYS.2.1 Allgemeiner Client   | SYS.2.1 Allgemeiner Client                                   |
|------------------------------|--------------------------------------------------------------|
| Zielobjekte                  | S1.1, S3                                                     |
| Anforderungen                | SYS.2.1.A1 - A27                                             |
| Umsetzungs- vorgaben         | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

<!-- page: 112 -->

| SYS.2.2.3 Clients unter Windows 10   | SYS.2.2.3 Clients unter Windows 10                                           |
|--------------------------------------|------------------------------------------------------------------------------|
| Zielobjekte                          | S1.1                                                                         |
| Anforderungen                        | SYS.2.2.3.A1 - A20                                                           |
| Umsetzungs- vorgaben                 | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                 |
| Hinweise                             | SYS.2.2.3.A4 Gesperrt werden können diese Verbindungen z.B. in der Firewall. |

| SYS.3.4 Mobile Datenträger   | SYS.3.4 Mobile Datenträger                                                                                    |
|------------------------------|---------------------------------------------------------------------------------------------------------------|
| Zielobjekte                  | P5.1                                                                                                          |
| Anforderungen                | SYS.3.4.A1 - A7                                                                                               |
| Umsetzungs- vorgaben         | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                  |
| Hinweise                     | SYS.3.4.A4 Durch das Verwenden einer Datenschleuse mit Anti-Viren-Software kann die Sicherheit erhöht werden. |

| SYS.4.1 Drucker, Kopierer und Multifunktionsgeräte   | SYS.4.1 Drucker, Kopierer und Multifunktionsgeräte           |
|------------------------------------------------------|--------------------------------------------------------------|
| Zielobjekte                                          | P4.1, P4.2, P5.1                                             |
| Anforderungen                                        | SYS.4.1.A1 - A19                                             |
| Umsetzungs- vorgaben                                 | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| NET.1.1 Netzarchitektur und -design   | NET.1.1 Netzarchitektur und -design                                                 |
|---------------------------------------|-------------------------------------------------------------------------------------|
| Zielobjekte                           | N1, N2, N3, N4, N6                                                                  |
| Anforderungen                         | NET.1.1.A1 - A27                                                                    |
| Umsetzungs- vorgaben                  | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                        |
| Hinweise                              | NET.1.1.A23 Die Trennung von ELS-, KMS- und Büro-Netz erhöht das Sicherheitsniveau. |

| NET.1.2 Netzmanagement   | NET.1.2 Netzmanagement                                       |
|--------------------------|--------------------------------------------------------------|
| Zielobjekte              | N1, N2, N3, N4                                               |
| Anforderungen            | NET.1.2.A1 - A29                                             |
| Umsetzungs- vorgaben     | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

<!-- page: 113 -->

| NET.3.1 Router und Switches   | NET.3.1 Router und Switches                                  |
|-------------------------------|--------------------------------------------------------------|
| Zielobjekte                   | N1, N2, N3, N4, N5                                           |
| Anforderungen                 | NET.3.1.A1 - A23                                             |
| Umsetzungs- vorgaben          | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| NET.3.2 Firewall     | NET.3.2 Firewall                                                                                                                                                                                                                                                      |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zielobjekte          | N1, N2, N3, N4, N5                                                                                                                                                                                                                                                    |
| Anforderungen        | NET.3.2.A1 - A24                                                                                                                                                                                                                                                      |
| Umsetzungs- vorgaben | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                                                                                                                                                                          |
| Hinweise             | NET.3.2.A15 Wird das Netzwerk durch zwei Firewalls segmentiert, ist darauf zu achten, die Firewalls von unterschiedlichen Herstellern zu beschaffen. Dies verringert die Chancen eines Angreifers, dieselbe Sicherheitslücke in beiden Produkten ausnutzen zu können. |

| NET.3.3 VPN          | NET.3.3 VPN                                                  |
|----------------------|--------------------------------------------------------------|
| Zielobjekte          | N1                                                           |
| Anforderungen        | NET.3.3.A1 - A13                                             |
| Umsetzungs- vorgaben | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| NET.4.1 TK-Anlagen   | NET.4.1 TK-Anlagen                                           |
|----------------------|--------------------------------------------------------------|
| Zielobjekte          | A2                                                           |
| Anforderungen        | NET.4.1.A1 - A16                                             |
| Umsetzungs- vorgaben | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| NET.4.2 VoIP         | NET.4.2 VoIP                                                                                                   |
|----------------------|----------------------------------------------------------------------------------------------------------------|
| Zielobjekte          | A2, N2                                                                                                         |
| Anforderungen        | NET.4.2.A1 - A13                                                                                               |
| Umsetzungs- vorgaben | Die Anforderungen müssen auf geeignete Weise erfüllt werden.                                                   |
| Hinweise             | NET.4.2.A1 Die Erfüllung der technischen Richtlinie Notruf ist bei der Planung des VoIP-Einsatzes zu beachten. |

<!-- page: 114 -->

| NET.4.3 Faxgeräte und Faxserver   | NET.4.3 Faxgeräte und Faxserver                              |
|-----------------------------------|--------------------------------------------------------------|
| Zielobjekte                       | S4                                                           |
| Anforderungen                     | NET.4.3.A1 - A10                                             |
| Umsetzungs- vorgaben              | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| INF.1 Allgemeines Gebäude   | INF.1 Allgemeines Gebäude                                    |
|-----------------------------|--------------------------------------------------------------|
| Zielobjekte                 | R1, R2, R3, R4, R5, R6                                       |
| Anforderungen               | INF.1.A1 - A20                                               |
| Umsetzungs- vorgaben        | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| INF.2 Rechenzentrum sowie Serverraum   | INF.2 Rechenzentrum sowie Serverraum                         |
|----------------------------------------|--------------------------------------------------------------|
| Zielobjekte                            | R2                                                           |
| Anforderungen                          | INF.2.A1 - A20                                               |
| Umsetzungs- vorgaben                   | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| INF.3 Elektrotechnische Verkabelung   | INF.3 Elektrotechnische Verkabelung                          |
|---------------------------------------|--------------------------------------------------------------|
| Zielobjekte                           | R1, R2, R3, R4, R6                                           |
| Anforderungen                         | INF.3.A1 - A12                                               |
| Umsetzungs- vorgaben                  | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| INF.4 IT-Verkabelung   | INF.4 IT-Verkabelung                                         |
|------------------------|--------------------------------------------------------------|
| Zielobjekte            | N6                                                           |
| Anforderungen          | INF.4.A1 - A11                                               |
| Umsetzungs- vorgaben   | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| INF.6 Datenträgerarchiv   | INF.6 Datenträgerarchiv                                      |
|---------------------------|--------------------------------------------------------------|
| Zielobjekte               | R2, R3, R5                                                   |
| Anforderungen             | INF.6.A1 - A8                                                |
| Umsetzungs- vorgaben      | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

<!-- page: 115 -->

| INF.7 Büroarbeitsplatz   | INF.7 Büroarbeitsplatz                                       |
|--------------------------|--------------------------------------------------------------|
| Zielobjekte              | R1, R3                                                       |
| Anforderungen            | INF.7.A1 - A7                                                |
| Umsetzungs- vorgaben     | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

| INF.10 Besprechungs-, Veranstaltungs- und Schulungsräume   | INF.10 Besprechungs-, Veranstaltungs- und Schulungsräume     |
|------------------------------------------------------------|--------------------------------------------------------------|
| Zielobjekte                                                | R6                                                           |
| Anforderungen                                              | INF.10.A1 - A8                                               |
| Umsetzungs- vorgaben                                       | Die Anforderungen müssen auf geeignete Weise erfüllt werden. |

Es gibt Objekte, die mit den vorhandenen Bausteinen des IT-Grundschutz nicht hinreichend modelliert werden können. Diese müssen gesondert betrachtet werden. Die Verbindung zum ISP (N4) hat in allen drei Schutzzielen einen sehr hohen Schutzbedarf. Die Rettungsleitstelle hat aber keinen Einfluss auf das erreichte Sicherheitsniveau des ISP. Für das Alarmierungsnetz N7 existiert kein Baustein, der die Anforderungen für den Schutzbedarf dieser Komponente passend abbildet. Da für dieses Netz ein sehr hoher Schutzbedarf in allen drei Schutzzielen ermittelt wurde, müssen auch für N7 die Risiken gesondert betrachtet werden. Die aufgeführten Objekte werden in die Risikoanalyse mit aufgenommen.

## 6 Restrisiko

Auch bei Umsetzung aller Anforderungen ist keine hundertprozentige Sicherheit zu erreichen. Dies muss sowohl den Anwendern des IT-Grundschutz-Profils, als auch den Entscheidungsträgern bewusst sein. Ein Restrisiko bleibt bestehen. Durch die Zusammenarbeit mit anderen Organisationen werden vertrauliche Informationen an Institutionen übertragen, auf deren Sicherheitsmanagement eine Leitstelle nur beschränkt Einfluss nehmen kann. Auch eigene Mitarbeiter können trotz Dienstanweisungen und Schulungen, absichtlich oder unbewusst, solche Informationen an Unbefugte weitergeben. Gezielte Angriffe auf die Informationstechnik einer Institution nehmen zu. Bekannt gewordene Sicherheitslücken in den Systemen werden immer schneller ausgenutzt. Eine rechtzeitige Behebung durch entsprechende Updates ist nicht immer möglich. Dies betrifft insbesondere Systeme, bei denen der Schwerpunkt bei der Entwicklung nicht auf die Informationssicherheit gelegt wurde. Ein Restrisiko bleibt auch beim Bezug von Dienstleistungen Dritter. Trotz redundanter Internetanschlüsse kann es zum Beispiel zu Störungen an großen Netzknotenpunkten kommen, wodurch mehrere ISP betroffen sein können.

<!-- page: 116 -->

## 7 Anwendungshinweise

Die ermittelten Anforderungen sind in das Gesamtsicherheitskonzept zu integrieren und im Zuge der geplanten Realisierung umzusetzen. Das BSI empfiehlt die Anforderungen der Bausteine in einer festgelegten Reihenfolge durchzuführen. Dadurch wird gewährleistet, dass die grundlegenden Risiken frühzeitig abgedeckt sind. Folgende Bausteine sollten als erstes umgesetzt werden:

- ISMS Sicherheitsmanagement
- CON.3 und CON.6 aus CON Konzepte und Vorgehensweisen
- ORP.1 bis ORP.4 aus ORP Organisation und Personal
- alle Bausteine aus OPS.1.1 Kern-IT-Betrieb

## 8 Notfallmanagement (BCM)

Trotz   eines   hohen   Sicherheitsniveaus   kann   eine   Beeinträchtigung   der   Betriebsbereitschaft   der Rettungsleitstelle nicht ausgeschlossen werden. Aus diesem Grund müssen weitere Vorbereitungen getroffen werden, um auch bei einem Ausfall, der Aufgabenerfüllung in einer Rettungsleitstelle nachkommen zu können. Die Planung des Umgangs mit Krisen in einem kontinuierlichen Zyklus wird als Notfallmanagement oder mit dem englischen Begriff Business Continuity Management (BCM) bezeichnet. Ein standardisiertes Vorgehen ist in DIN EN ISO 22301:2014 2 spezifiziert. Das BSI beschreibt im Standard 100-4 3 einen Notfallmanagement-Prozess. Dieser besteht aus fünf Phasen,   die   nach   einer   Initiierung   kontinuierlich   durchlaufen   werden   müssen:   Konzeption, Umsetzung des Notfallvorsorgekonzepts, Notfallbewältigung, Tests und Übungen, Aufrechterhaltung und Verbesserung.

## 9 Unterstützende Informationen

Detailliertere Informationen zu den einzelnen Anforderungen finden sich in den Umsetzungshinweisen der einzelnen Bausteine des IT-Grundschutzes. Außerdem gibt es ein Dokument der Europan Emergency Number Association (EENA) zum Thema IT-Sicherheit in Rettungsleitstellen. 4

## 10 Risikoanalyse

Für Objekte, bei denen ein hoher oder sehr hoher Schutzbedarf festgestellt worden ist, sieht der ITGrundschutz nach der Modellierung mit den IT-Grundschutz-Bausteinen auch eine Risikoanalyse vor. Das BSI stellt hierzu im IT-Grundschutz-Kompendium eine Auflistung der elementaren Gefährdungen zur Verfügung. In der Risikoanalyse wird ermittelt, wie diese Gefährdungen auf die Objekte einwirken. Das Vorgehen bei einer Risikoanalyse wird im BSI-Standard 200-3 beschrieben.

2

3

4

[https://www.beuth.de/de/norm/din-en-iso-22301/215741063   (abgerufen am 13.10.2019).](https://www.beuth.de/de/norm/din-en-iso-22301/215741063)

[https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzStandards/Standard04/](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzStandards/Standard04/ITGStandard04_node.html)

ITGStandard04\_node.html (abgerufen am 13.10.2019).

[https://eena.org/cybersecurity-guidelines-and-best-practices-for-emergency-services/   (abgerufen am 13.10.2019).](https://eena.org/cybersecurity-guidelines-and-best-practices-for-emergency-services/)

<!-- page: 117 -->

Das Ergebnis der Schutzbedarfsfeststellung hat gezeigt, dass in der Rettungsleitstelle sehr viele Objekte einen hohen oder sehr hohen Schutzbedarf benötigen. Für alle diese Objekte ist daher eine Risikoanalyse   durchzuführen.   Aufgrund   der   Menge   wird   die   Risikoanalyse   in   dieser   Arbeit beispielhaft nur für die Objekte durchgeführt, die nicht hinreichend mit Bausteinen modelliert werden konnten. Die ausgewählten Objekte sind in Tabelle A-30 aufgeführt. Beide haben einen sehr hohen Schutzbedarf für die Schutzziele Vertraulichkeit, Integrität und  Verfügbarkeit.

Tabelle A-30: Objekte, für die beispielhaft eine Risikoanalyse durchgeführt wird.

| ID   | Objekte und Prozesse des Informationsverbunds   |
|------|-------------------------------------------------|
| N4   | Netz zum Internet Service Provider              |
| N7   | Alarmierungsnetz für Funkmeldeempfänger         |

## 10.1 Ermittlung elementarer Gefährdungen

In Tabelle A-31 wird für jeden Gefährdung ermittelt, inwieweit diese auf das betrachtete Objekt einwirken. Die Gefährdung kann für das Objekt direkt, indirekt oder nicht relevant sein. In der zweiten Spalte sind die Grundwerte aufgeführt, die von der Gefährdung beeinträchtigt werden können. Zur besseren Unterscheidung werden Anfangsbuchstaben der englischen Übersetzung ( C onfidentiality, I ntegrity und A vailability) verwendet. Sofern die Relevanz nicht eindeutig ist, wird in der rechten Spalte eine Begründung aufgeführt.

| Gefährdung                                                                                                                       | Grundwert                                                                                                                        | Relevanz                                                                                                                         | Relevanz                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                  |                                                                                                                                  | N4                                                                                                                               | N7                                                                                                                               |
| G 0.1 Feuer                                                                                                                      | A                                                                                                                                | indirekt                                                                                                                         | indirekt                                                                                                                         |
| Netzkomponenten können durch Brandschäden in der Funktion beeinträchtigt werden.                                                 | Netzkomponenten können durch Brandschäden in der Funktion beeinträchtigt werden.                                                 | Netzkomponenten können durch Brandschäden in der Funktion beeinträchtigt werden.                                                 | Netzkomponenten können durch Brandschäden in der Funktion beeinträchtigt werden.                                                 |
| G 0.2 Ungünstige klimatische Bedingungen                                                                                         | I, A                                                                                                                             | nein                                                                                                                             | nein                                                                                                                             |
| Die verwendeten Komponenten sind üblicherweise resistent gegen extreme Temperaturen oder befinden sich in klimatisierten Räumen. | Die verwendeten Komponenten sind üblicherweise resistent gegen extreme Temperaturen oder befinden sich in klimatisierten Räumen. | Die verwendeten Komponenten sind üblicherweise resistent gegen extreme Temperaturen oder befinden sich in klimatisierten Räumen. | Die verwendeten Komponenten sind üblicherweise resistent gegen extreme Temperaturen oder befinden sich in klimatisierten Räumen. |
| G 0.3 Wasser                                                                                                                     | I, A                                                                                                                             | indirekt                                                                                                                         | indirekt                                                                                                                         |
| Durch das Eindringen von Wasser in Netzkomponenten kann es zu Beeinträchtigungen kommen.                                         | Durch das Eindringen von Wasser in Netzkomponenten kann es zu Beeinträchtigungen kommen.                                         | Durch das Eindringen von Wasser in Netzkomponenten kann es zu Beeinträchtigungen kommen.                                         | Durch das Eindringen von Wasser in Netzkomponenten kann es zu Beeinträchtigungen kommen.                                         |
| G 0.4 Verschmutzung, Staub, Korrosion                                                                                            | I, A                                                                                                                             | indirekt                                                                                                                         | indirekt                                                                                                                         |
| Betrieb der Netzkomponenten kann durch übermäßige Verschmutzung beeinträchtigt werden.                                           | Betrieb der Netzkomponenten kann durch übermäßige Verschmutzung beeinträchtigt werden.                                           | Betrieb der Netzkomponenten kann durch übermäßige Verschmutzung beeinträchtigt werden.                                           | Betrieb der Netzkomponenten kann durch übermäßige Verschmutzung beeinträchtigt werden.                                           |
| G 0.5 Naturkatastrophen                                                                                                          | A                                                                                                                                | indirekt                                                                                                                         | indirekt                                                                                                                         |
| Netzkomponenten können durch Zerstörung beeinträchtigt werden.                                                                   | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                                                                   | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                                                                   | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                                                                   |
| G 0.6 Katastrophen im Umfeld                                                                                                     | A                                                                                                                                | indirekt                                                                                                                         | indirekt                                                                                                                         |
| Netzkomponenten können durch Zerstörung beeinträchtigt werden.                                                                   | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                                                                   | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                                                                   | Netzkomponenten können durch Zerstörung beeinträchtigt werden.                                                                   |
| G 0.7 Großereignisse im Umfeld                                                                                                   | C, I, A                                                                                                                          | indirekt                                                                                                                         | indirekt                                                                                                                         |
| Hohe Netzauslastung bei N4 und durch Vielzahl an Alarmierungen auch bei N7.                                                      | Hohe Netzauslastung bei N4 und durch Vielzahl an Alarmierungen auch bei N7.                                                      | Hohe Netzauslastung bei N4 und durch Vielzahl an Alarmierungen auch bei N7.                                                      | Hohe Netzauslastung bei N4 und durch Vielzahl an Alarmierungen auch bei N7.                                                      |

<!-- page: 118 -->

| G 0.8 Ausfall oder Störung der Stromversorgung                                                                                                               | I, A                                                                                                                                                         | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ohne Strom können die Netzkomponenten ausfallen und somit das System.                                                                                        | Ohne Strom können die Netzkomponenten ausfallen und somit das System.                                                                                        | Ohne Strom können die Netzkomponenten ausfallen und somit das System.                                                                                        | Ohne Strom können die Netzkomponenten ausfallen und somit das System.                                                                                        |
| G 0.9 Ausfall oder Störung von Kommunikationsnetzen                                                                                                          | I, A                                                                                                                                                         | direkt                                                                                                                                                       | indirekt                                                                                                                                                     |
| Ausfall des ISP bei N4. Ausfall des Multi-Master-Betriebs bei N7.                                                                                            | Ausfall des ISP bei N4. Ausfall des Multi-Master-Betriebs bei N7.                                                                                            | Ausfall des ISP bei N4. Ausfall des Multi-Master-Betriebs bei N7.                                                                                            | Ausfall des ISP bei N4. Ausfall des Multi-Master-Betriebs bei N7.                                                                                            |
| G 0.10 Ausfall oder Störung von Versorgungsnetzen                                                                                                            | A                                                                                                                                                            | nein                                                                                                                                                         | nein                                                                                                                                                         |
| Keine Auswirkungen auf N4 oder N7.                                                                                                                           | Keine Auswirkungen auf N4 oder N7.                                                                                                                           | Keine Auswirkungen auf N4 oder N7.                                                                                                                           | Keine Auswirkungen auf N4 oder N7.                                                                                                                           |
| G 0.11 Ausfall oder Störung von Dienstleistern                                                                                                               | C, I, A                                                                                                                                                      | direkt                                                                                                                                                       | nein                                                                                                                                                         |
| N4: Ausfall des ISP                                                                                                                                          | N4: Ausfall des ISP                                                                                                                                          | N4: Ausfall des ISP                                                                                                                                          | N4: Ausfall des ISP                                                                                                                                          |
| G 0.12 Elektromagnetische Störstrahlung                                                                                                                      | I, A                                                                                                                                                         | nein                                                                                                                                                         | direkt                                                                                                                                                       |
| N4: Keine Auswirkungen, weil Verwendung abgeschirmter Kabel. N7: Direkte Auswirkung.                                                                         | N4: Keine Auswirkungen, weil Verwendung abgeschirmter Kabel. N7: Direkte Auswirkung.                                                                         | N4: Keine Auswirkungen, weil Verwendung abgeschirmter Kabel. N7: Direkte Auswirkung.                                                                         | N4: Keine Auswirkungen, weil Verwendung abgeschirmter Kabel. N7: Direkte Auswirkung.                                                                         |
| G 0.13 Abfangen kompromittierender Strahlung                                                                                                                 | C                                                                                                                                                            | nein                                                                                                                                                         | nein                                                                                                                                                         |
| Keine Auswirkungen auf N4 oder N7.                                                                                                                           | Keine Auswirkungen auf N4 oder N7.                                                                                                                           | Keine Auswirkungen auf N4 oder N7.                                                                                                                           | Keine Auswirkungen auf N4 oder N7.                                                                                                                           |
| G 0.14 Ausspähen von Informationen (Spionage)                                                                                                                | C                                                                                                                                                            | indirekt                                                                                                                                                     | nein                                                                                                                                                         |
| N7: Keine Übertragung von Informationen, die zur Spionage geeignet sind                                                                                      | N7: Keine Übertragung von Informationen, die zur Spionage geeignet sind                                                                                      | N7: Keine Übertragung von Informationen, die zur Spionage geeignet sind                                                                                      | N7: Keine Übertragung von Informationen, die zur Spionage geeignet sind                                                                                      |
| G 0.15 Abhören                                                                                                                                               | C                                                                                                                                                            | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Netzwerkverkehr kann abgehört werden.                                                                                                                        | Netzwerkverkehr kann abgehört werden.                                                                                                                        | Netzwerkverkehr kann abgehört werden.                                                                                                                        | Netzwerkverkehr kann abgehört werden.                                                                                                                        |
| G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten                                                                                                   | C, A                                                                                                                                                         | nein                                                                                                                                                         | direkt                                                                                                                                                       |
| N7: Diebstahl von Netzkomponenten möglich, weil Betrieb an verteilten Standorten.                                                                            | N7: Diebstahl von Netzkomponenten möglich, weil Betrieb an verteilten Standorten.                                                                            | N7: Diebstahl von Netzkomponenten möglich, weil Betrieb an verteilten Standorten.                                                                            | N7: Diebstahl von Netzkomponenten möglich, weil Betrieb an verteilten Standorten.                                                                            |
| G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten                                                                                                     | C, A                                                                                                                                                         | nein                                                                                                                                                         | nein                                                                                                                                                         |
| Alle Komponenten sind stationär verbaut. Die Gefahr eines Verlusts besteht daher nicht.                                                                      | Alle Komponenten sind stationär verbaut. Die Gefahr eines Verlusts besteht daher nicht.                                                                      | Alle Komponenten sind stationär verbaut. Die Gefahr eines Verlusts besteht daher nicht.                                                                      | Alle Komponenten sind stationär verbaut. Die Gefahr eines Verlusts besteht daher nicht.                                                                      |
| G 0.18 Fehlplanung oder fehlende Anpassung                                                                                                                   | C, I, A                                                                                                                                                      | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Kapazitätsengpässe sind bei N4 und N7 möglich.                                                                                                               | Kapazitätsengpässe sind bei N4 und N7 möglich.                                                                                                               | Kapazitätsengpässe sind bei N4 und N7 möglich.                                                                                                               | Kapazitätsengpässe sind bei N4 und N7 möglich.                                                                                                               |
| G 0.19 Offenlegung schützenswerter Informationen                                                                                                             | C                                                                                                                                                            | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Netzwerkverkehr kann abgehört werden.                                                                                                                        | Netzwerkverkehr kann abgehört werden.                                                                                                                        | Netzwerkverkehr kann abgehört werden.                                                                                                                        | Netzwerkverkehr kann abgehört werden.                                                                                                                        |
| G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle                                                                                                | C, I, A                                                                                                                                                      | nein                                                                                                                                                         | nein                                                                                                                                                         |
| Durch Nutzung zuverlässiger und geprüfter Komponenten für N4 und N7 nicht relevant.                                                                          | Durch Nutzung zuverlässiger und geprüfter Komponenten für N4 und N7 nicht relevant.                                                                          | Durch Nutzung zuverlässiger und geprüfter Komponenten für N4 und N7 nicht relevant.                                                                          | Durch Nutzung zuverlässiger und geprüfter Komponenten für N4 und N7 nicht relevant.                                                                          |
| G 0.21 Manipulation von Hard- oder Software                                                                                                                  | C, I, A                                                                                                                                                      | direkt                                                                                                                                                       | direkt                                                                                                                                                       |
| Netzkomponenten könnten manipuliert werden.                                                                                                                  | Netzkomponenten könnten manipuliert werden.                                                                                                                  | Netzkomponenten könnten manipuliert werden.                                                                                                                  | Netzkomponenten könnten manipuliert werden.                                                                                                                  |
| G 0.22 Manipulation von Informationen                                                                                                                        | I                                                                                                                                                            | direkt                                                                                                                                                       | nein                                                                                                                                                         |
| N4: Manipulation durch Einspielen von veränderten Informationen möglich. N7: Geschlossenes Netzwerk lässt kein Einspielen von Informationen durch Dritte zu. | N4: Manipulation durch Einspielen von veränderten Informationen möglich. N7: Geschlossenes Netzwerk lässt kein Einspielen von Informationen durch Dritte zu. | N4: Manipulation durch Einspielen von veränderten Informationen möglich. N7: Geschlossenes Netzwerk lässt kein Einspielen von Informationen durch Dritte zu. | N4: Manipulation durch Einspielen von veränderten Informationen möglich. N7: Geschlossenes Netzwerk lässt kein Einspielen von Informationen durch Dritte zu. |
| G 0.23 Unbefugtes Eindringen in IT-Systeme                                                                                                                   | C, I                                                                                                                                                         | direkt                                                                                                                                                       | nein                                                                                                                                                         |
| N7: Geschlossenes Netzwerk lässt kein unbefugtes Eindringen zu.                                                                                              | N7: Geschlossenes Netzwerk lässt kein unbefugtes Eindringen zu.                                                                                              | N7: Geschlossenes Netzwerk lässt kein unbefugtes Eindringen zu.                                                                                              | N7: Geschlossenes Netzwerk lässt kein unbefugtes Eindringen zu.                                                                                              |

<!-- page: 119 -->

| G 0.24 Zerstörung von Geräten oder Datenträgern                                                             | A                                                                                                           | direkt                                                                                                      | direkt                                                                                                      |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Beeinträchtigung von Netzkomponenten.                                                                       |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.25 Ausfall von Geräten oder Systemen                                                                    | A                                                                                                           | direkt                                                                                                      | direkt                                                                                                      |
| Beeinträchtigung von Netzkomponenten.                                                                       |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.26 Fehlfunktion von Geräten oder Systemen                                                               | C, I, A                                                                                                     | direkt                                                                                                      | direkt                                                                                                      |
| Beeinträchtigungen durch Fehlfunktionen am Router oder am DAG.                                              | Beeinträchtigungen durch Fehlfunktionen am Router oder am DAG.                                              |                                                                                                             |                                                                                                             |
| G 0.27 Ressourcenmangel                                                                                     | A                                                                                                           | direkt                                                                                                      | direkt                                                                                                      |
| Kapazitätsengpässe in den Netzen.                                                                           |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.28 Software-Schwachstellen oder -Fehler                                                                 | C, I, A                                                                                                     | direkt                                                                                                      | direkt                                                                                                      |
| Beeinträchtigungen der Netzkomponenten.                                                                     |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.29 Verstoß gegen Gesetze oder Regelungen                                                                | C, I, A                                                                                                     | indirekt                                                                                                    | indirekt                                                                                                    |
| Missbrauch durch Schadprogramme im Router (N4). Datenschutzverstoß bei fehlender Verschlüsselung (N7).      | Missbrauch durch Schadprogramme im Router (N4). Datenschutzverstoß bei fehlender Verschlüsselung (N7).      | Missbrauch durch Schadprogramme im Router (N4). Datenschutzverstoß bei fehlender Verschlüsselung (N7).      | Missbrauch durch Schadprogramme im Router (N4). Datenschutzverstoß bei fehlender Verschlüsselung (N7).      |
| G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen                                   | C, I, A                                                                                                     | indirekt                                                                                                    | indirekt                                                                                                    |
| N4: Möglich durch physischen Zugriff auf Netzkomponenten.                                                   |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen                                     | C, I, A                                                                                                     | direkt                                                                                                      | direkt                                                                                                      |
| Eine Fehlerhafte Administration von Router oder Netzkomponenten kann den Betrieb der Netze beeinträchtigen. | Eine Fehlerhafte Administration von Router oder Netzkomponenten kann den Betrieb der Netze beeinträchtigen. | Eine Fehlerhafte Administration von Router oder Netzkomponenten kann den Betrieb der Netze beeinträchtigen. | Eine Fehlerhafte Administration von Router oder Netzkomponenten kann den Betrieb der Netze beeinträchtigen. |
| G 0.32 Missbrauch von Berechtigungen                                                                        | C, I, A                                                                                                     | nein                                                                                                        | nein                                                                                                        |
| Verschiedene Rollen sind nicht vorhanden.                                                                   |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.33 Personalausfall                                                                                      | A                                                                                                           | nein                                                                                                        | nein                                                                                                        |
| Personal wird für Betrieb der Netze nicht benötigt.                                                         |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.34 Anschlag                                                                                             | C, I, A                                                                                                     | indirekt                                                                                                    | indirekt                                                                                                    |
| Anschlag kann Netzkomponenten beeinträchtigen.                                                              |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.35 Nötigung, Erpressung oder Korruption                                                                 | C, I, A                                                                                                     | nein                                                                                                        | nein                                                                                                        |
| Personal wird für Betrieb der Netze nicht benötigt.                                                         |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.36 Identitätsdiebstahl                                                                                  | C, I, A                                                                                                     | nein                                                                                                        | nein                                                                                                        |
| Keine persönlichen Accounts vorhanden.                                                                      |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.37 Abstreiten von Handlungen                                                                            | C, I                                                                                                        | nein                                                                                                        | nein                                                                                                        |
| Keine persönlichen Accounts vorhanden.                                                                      |                                                                                                             |                                                                                                             |                                                                                                             |
| G 0.38 Missbrauch personenbezogener Daten                                                                   | C                                                                                                           | nein                                                                                                        | direkt                                                                                                      |
| Abgehörte Daten können missbraucht werden.                                                                  | Abgehörte Daten können missbraucht werden.                                                                  | Abgehörte Daten können missbraucht werden.                                                                  | Abgehörte Daten können missbraucht werden.                                                                  |

<!-- page: 120 -->

Tabelle A-31: Ermittlung der Relevanz der Gefährdungen für die Beispiel-Objekte N4 und N7.

| G 0.39 Schadprogramme                                                                        | C, I, A                                                                                      | indirekt                                                                                     | nein                                                                                         |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Schadprogramme im Router können Verbindung beeinträchtigen.                                  | Schadprogramme im Router können Verbindung beeinträchtigen.                                  | Schadprogramme im Router können Verbindung beeinträchtigen.                                  | Schadprogramme im Router können Verbindung beeinträchtigen.                                  |
| G 0.40 Verhinderung von Diensten (Denial of Service)                                         | A                                                                                            | direkt                                                                                       | nein                                                                                         |
| N7: Nicht relevant, weil geschlossenes Netzwerk.                                             | N7: Nicht relevant, weil geschlossenes Netzwerk.                                             | N7: Nicht relevant, weil geschlossenes Netzwerk.                                             | N7: Nicht relevant, weil geschlossenes Netzwerk.                                             |
| G 0.41 Sabotage                                                                              | A                                                                                            | direkt                                                                                       | direkt                                                                                       |
| N4: z.B. durch gezielte Angriffe auf IP-Adresse. N7: z.B. durch Störsender.                  | N4: z.B. durch gezielte Angriffe auf IP-Adresse. N7: z.B. durch Störsender.                  | N4: z.B. durch gezielte Angriffe auf IP-Adresse. N7: z.B. durch Störsender.                  | N4: z.B. durch gezielte Angriffe auf IP-Adresse. N7: z.B. durch Störsender.                  |
| G 0.42 Social Engineering                                                                    | C, I                                                                                         | nein                                                                                         | nein                                                                                         |
| Keine persönlichen Accounts vorhanden.                                                       | Keine persönlichen Accounts vorhanden.                                                       | Keine persönlichen Accounts vorhanden.                                                       | Keine persönlichen Accounts vorhanden.                                                       |
| G 0.43 Einspielen von Nachrichten                                                            | C, I                                                                                         | direkt                                                                                       | nein                                                                                         |
| N7: Nicht relevant, weil geschlossenes Netzwerk.                                             | N7: Nicht relevant, weil geschlossenes Netzwerk.                                             | N7: Nicht relevant, weil geschlossenes Netzwerk.                                             | N7: Nicht relevant, weil geschlossenes Netzwerk.                                             |
| G 0.44 Unbefugtes Eindringen in Räumlichkeiten                                               | C, I, A                                                                                      | indirekt                                                                                     | indirekt                                                                                     |
| Relevant, wenn Manipulationen an den Komponenten vorgenommen werden.                         | Relevant, wenn Manipulationen an den Komponenten vorgenommen werden.                         | Relevant, wenn Manipulationen an den Komponenten vorgenommen werden.                         | Relevant, wenn Manipulationen an den Komponenten vorgenommen werden.                         |
| G 0.45 Datenverlust                                                                          | A                                                                                            | nein                                                                                         | nein                                                                                         |
| N4 und N7 sind zustandslose Systeme.                                                         | N4 und N7 sind zustandslose Systeme.                                                         | N4 und N7 sind zustandslose Systeme.                                                         | N4 und N7 sind zustandslose Systeme.                                                         |
| G 0.46 Integritätsverlust schützenswerter Informationen                                      | I                                                                                            | indirekt                                                                                     | nein                                                                                         |
| N7: Nicht relevant, weil geschlossenes Netzwerk.                                             | N7: Nicht relevant, weil geschlossenes Netzwerk.                                             | N7: Nicht relevant, weil geschlossenes Netzwerk.                                             | N7: Nicht relevant, weil geschlossenes Netzwerk.                                             |
| G 0.47 Schädliche Seiteneffekte IT-gestützter Angriffe                                       | C, I, A                                                                                      | indirekt                                                                                     | nein                                                                                         |
| N4: Auswirkungen von Angriffen auf Router des ISP. N7: Da System geschlossen nicht relevant. | N4: Auswirkungen von Angriffen auf Router des ISP. N7: Da System geschlossen nicht relevant. | N4: Auswirkungen von Angriffen auf Router des ISP. N7: Da System geschlossen nicht relevant. | N4: Auswirkungen von Angriffen auf Router des ISP. N7: Da System geschlossen nicht relevant. |

## 10.2 Ermittlung weiterer relevanter Gefährdungen

Neben den vom BSI aufgeführten Gefährdungen, können für ein Objekt noch weitere potentielle Gefahren bestehen. Sofern diese identifiziert werden, müssen sie ebenfalls in einer Riskoanalyse berücksichtigt werden. Für die beiden Objekte N4 und N7 bestehen allerdings keine weiteren Gefährdungen.

## 10.3 Risikoeinschätzung

Die Bewertung der Risiken erfolgt nach der in Schaubild A-3 aufgeführten Matrix zur Einstufung von Risiken.

<!-- page: 121 -->

Seite A-37

| Auswirkungen / Schadenshöhe   | existenz- bedrohend   | mittel              | hoch                | sehr hoch           | sehr hoch           |
|-------------------------------|-----------------------|---------------------|---------------------|---------------------|---------------------|
| Auswirkungen / Schadenshöhe   | beträchtlich          | gering              | mittel              | hoch                | sehr hoch           |
| Auswirkungen / Schadenshöhe   | begrenzt              | gering              | gering              | mittel              | hoch                |
| Auswirkungen / Schadenshöhe   | vernachlässigbar      | gering              | gering              | gering              | mittel              |
| Auswirkungen / Schadenshöhe   |                       | selten              | mittel              | häufig              | sehr häufig         |
|                               | Eintrittshäufigkeit   | Eintrittshäufigkeit | Eintrittshäufigkeit | Eintrittshäufigkeit | Eintrittshäufigkeit |

## Schaubild A-3: Matrix zur Einstufung von Risiken.

Für jedes betrachtete Objekt werden im nächsten Schritt die Gefährdungen hinsichtlich Schadenshöhe und Eintrittswahrscheinlichkeit bewertet.

| Netz zum Internet Service Provider N4 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Netz zum Internet Service Provider N4 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Netz zum Internet Service Provider N4 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Netz zum Internet Service Provider N4 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Gefährdung: G 0.8 Ausfall oder Störung der Stromversorgung                                                        | Gefährdung: G 0.8 Ausfall oder Störung der Stromversorgung                                                        | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                             | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                             |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                                                            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Risiko ohne zusätzliche Maßnahmen: mittel                                                                         |
| Gefährdung: G 0.9 Ausfall oder Störung von Kommunikationsnetzen                                                   | Gefährdung: G 0.9 Ausfall oder Störung von Kommunikationsnetzen                                                   | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                             | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                             |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                                                            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Risiko ohne zusätzliche Maßnahmen: mittel                                                                         |
| Gefährdung: G 0.11 Ausfall oder Störung von Dienstleistern                                                        | Gefährdung: G 0.11 Ausfall oder Störung von Dienstleistern                                                        | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit                                            | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit                                            |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                                                            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                             | Risiko ohne zusätzliche Maßnahmen: mittel                                                                         |

<!-- page: 122 -->

| Gefährdung: G 0.15 Abhören                                   | Gefährdung: G 0.15 Abhören                                   | Beeinträchtigte Grundwerte: Vertraulichkeit                            | Beeinträchtigte Grundwerte: Vertraulichkeit                            |
|--------------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten       | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich        | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.18 Fehlplanung oder fehlende Anpassung       | Gefährdung: G 0.18 Fehlplanung oder fehlende Anpassung       | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten       | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt            | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                      | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.19 Offenlegung schützenswerter Informationen | Gefährdung: G 0.19 Offenlegung schützenswerter Informationen | Beeinträchtigte Grundwerte: Vertraulichkeit                            | Beeinträchtigte Grundwerte: Vertraulichkeit                            |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten       | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich        | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.21 Manipulation von Hard- oder Software      | Gefährdung: G 0.21 Manipulation von Hard- oder Software      | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten       | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich        | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.22 Manipulation von Informationen            | Gefährdung: G 0.22 Manipulation von Informationen            | Beeinträchtigte Grundwerte: Integrität                                 | Beeinträchtigte Grundwerte: Integrität                                 |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten       | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich        | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.23 Unbefugtes Eindringen in IT-Systeme       | Gefährdung: G 0.23 Unbefugtes Eindringen in IT-Systeme       | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität                | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität                |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten       | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich        | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.24 Zerstörung von Geräten oder Datenträgern  | Gefährdung: G 0.24 Zerstörung von Geräten oder Datenträgern  | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten       | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich        | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.25 Ausfall von Geräten oder Systemen         | Gefährdung: G 0.25 Ausfall von Geräten oder Systemen         | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel       | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich        | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.26 Fehlfunktion von Geräten oder Systemen    | Gefährdung: G 0.26 Fehlfunktion von Geräten oder Systemen    | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten       | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich        | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.27 Ressourcenmangel                          | Gefährdung: G 0.27 Ressourcenmangel                          | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |

<!-- page: 123 -->

| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Gefährdung: G 0.28 Software-Schwachstellen oder -Fehler                             | Gefährdung: G 0.28 Software-Schwachstellen oder -Fehler                             | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen | Gefährdung: G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.40 Verhinderung von Diensten (Denial of Service)                    | Gefährdung: G 0.40 Verhinderung von Diensten (Denial of Service)                    | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.41 Sabotage                                                         | Gefährdung: G 0.41 Sabotage                                                         | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.43 Einspielen von Nachrichten                                       | Gefährdung: G 0.43 Einspielen von Nachrichten                                       | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität                | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität                |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |

Tabelle A-32: Risikoeinschätzung für Netz zum ISP N4.

| Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   | Alarmierungsnetz für Funkmeldeempfänger N7 Vertraulichkeit: sehr hoch Integrität: sehr hoch Verfügbarkeit: sehr hoch   |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Gefährdung: G 0.8 Ausfall oder Störung der Stromversorgung                                                             | Gefährdung: G 0.8 Ausfall oder Störung der Stromversorgung                                                             | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                                  | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                                  |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                                                                 | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                                                                      | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                                                                      | Risiko ohne zusätzliche Maßnahmen: gering                                                                              |
| Gefährdung: G 0.12 Elektromagnetische Störstrahlung                                                                    | Gefährdung: G 0.12 Elektromagnetische Störstrahlung                                                                    | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                                  | Beeinträchtigte Grundwerte: Integrität, Verfügbarkeit                                                                  |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                                                                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                                                                  | Risiko ohne zusätzliche Maßnahmen: gering                                                                              |
| Gefährdung: G 0.15 Abhören                                                                                             | Gefährdung: G 0.15 Abhören                                                                                             | Beeinträchtigte Grundwerte: Vertraulichkeit                                                                            | Beeinträchtigte Grundwerte: Vertraulichkeit                                                                            |

<!-- page: 124 -->

| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: sehr häufig            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: sehr hoch                           |
|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Gefährdung: G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten | Gefährdung: G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten | Beeinträchtigte Grundwerte: Vertraulichkeit, Verfügbarkeit             | Beeinträchtigte Grundwerte: Vertraulichkeit, Verfügbarkeit             |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.18 Fehlplanung oder fehlende Anpassung                 | Gefährdung: G 0.18 Fehlplanung oder fehlende Anpassung                 | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.19 Offenlegung schützenswerter Informationen           | Gefährdung: G 0.19 Offenlegung schützenswerter Informationen           | Beeinträchtigte Grundwerte: Vertraulichkeit                            | Beeinträchtigte Grundwerte: Vertraulichkeit                            |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: sehr häufig            | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: sehr hoch                           |
| Gefährdung: G 0.21 Manipulation von Hard- oder Software                | Gefährdung: G 0.21 Manipulation von Hard- oder Software                | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.24 Zerstörung von Geräten oder Datenträgern            | Gefährdung: G 0.24 Zerstörung von Geräten oder Datenträgern            | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.25 Ausfall von Geräten oder Systemen                   | Gefährdung: G 0.25 Ausfall von Geräten oder Systemen                   | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.26 Fehlfunktion von Geräten oder Systemen              | Gefährdung: G 0.26 Fehlfunktion von Geräten oder Systemen              | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                 | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.27 Ressourcenmangel                                    | Gefährdung: G 0.27 Ressourcenmangel                                    | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |

<!-- page: 125 -->

Tabelle A-33: Risikoeinschätzung für Alarmierungsnetz N7.

| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                                   | Auswirkungen ohne zusätzliche Maßnahmen: begrenzt                      | Risiko ohne zusätzliche Maßnahmen: gering                              |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Gefährdung: G 0.28 Software-Schwachstellen oder -Fehler                             | Gefährdung: G 0.28 Software-Schwachstellen oder -Fehler                             | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen | Gefährdung: G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit | Beeinträchtigte Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |
| Gefährdung: G 0.38 Missbrauch personenbezogener Daten                               | Gefährdung: G 0.38 Missbrauch personenbezogener Daten                               | Beeinträchtigte Grundwerte: Vertraulichkeit                            | Beeinträchtigte Grundwerte: Vertraulichkeit                            |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: mittel                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: mittel                              |
| Gefährdung: G 0.41 Sabotage                                                         | Gefährdung: G 0.41 Sabotage                                                         | Beeinträchtigte Grundwerte: Verfügbarkeit                              | Beeinträchtigte Grundwerte: Verfügbarkeit                              |
| Eintrittshäufigkeit ohne zusätzliche Maßnahmen: selten                              | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                               | Auswirkungen ohne zusätzliche Maßnahmen: beträchtlich                  | Risiko ohne zusätzliche Maßnahmen: gering                              |

## 10.4 Risikobehandlung

Nach der Bewertung muss im nächsten Schritt der Umgang mit den Risiken festgelegt werden. Grundsätzlich stehen vier Optionen zur Auswahl:

- Vermeidung (z.B. durch Ausschluss der Risikoursache).
- Reduktion/Modifikation (z.B. durch Änderung der Rahmenbedingungen).
- Transfer/Teilen (z.B. durch Versicherung oder Outsourcing).
- Akzeptanz/Übernahme (Risiko des Eintritt eines Schadenfalls wird in Kauf genommen).

Akzeptiert werden Risiken in der Regel nur dann, wenn sie als gering eingestuft werden und der Aufwand, das Risiko anderweitig unter Kontrolle zu bringen, schwerer wiegt als die potentielle Beeinträchtigung der Grundwerte.

Für die Risiken, die bei den betrachteten Objekten als mittel oder höher eingestuft wurden, sind in Tabelle A-34  für N4 und in  Tabelle A-35  für N7 Optionen zur Behandlung beschrieben. Durch ergänzende Maßnahmen ergibt sich jeweils eine neue Einstufung des Risikos.

## Netz zum Internet Service Provider N4

Vertraulichkeit: sehr hoch

Integrität: sehr hoch

<!-- page: 126 -->

Tabelle A-34: Behandlung der Risiken des Netz zum ISP.

| Verfügbarkeit: sehr hoch                             | Verfügbarkeit: sehr hoch            | Verfügbarkeit: sehr hoch                                                                                                                            |
|------------------------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Gefährdung                                           | Risikokategorie                     | Risikobehandlungsoptionen                                                                                                                           |
| G 0.8 Ausfall oder Störung der Stromversorgung       | mittel                              | Risikoreduktion: Es wird ein Notstromsystem vorgehalten.                                                                                            |
| G 0.8 Ausfall oder Störung der Stromversorgung       | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Es wird ein Notstromsystem vorgehalten.                                                                                            |
| G 0.9 Ausfall oder Störung von Kommunikationsnetzen  | mittel                              | Risikoreduktion: Es wird ein redundanter Anschluss zum ISP vorgehalten.                                                                             |
| G 0.9 Ausfall oder Störung von Kommunikationsnetzen  | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Es wird ein redundanter Anschluss zum ISP vorgehalten.                                                                             |
| G 0.11 Ausfall oder Störung von Dienstleistern       | mittel                              | Risikoreduktion: Es wird ein redundanter Anschluss zum ISP vorgehalten.                                                                             |
| G 0.11 Ausfall oder Störung von Dienstleistern       | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Es wird ein redundanter Anschluss zum ISP vorgehalten.                                                                             |
| G 0.25 Ausfall von Geräten oder Systemen             | mittel                              | Risikoreduktion: Es werden ein redundanter Anschluss zum ISP und redundante Netzkomponenten vorgehalten.                                            |
| G 0.25 Ausfall von Geräten oder Systemen             | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Es werden ein redundanter Anschluss zum ISP und redundante Netzkomponenten vorgehalten.                                            |
| G 0.27 Ressourcenmangel                              | mittel                              | Risikoreduktion: Der Anschluss zum ISP wird ausreichend dimensioniert.                                                                              |
| G 0.27 Ressourcenmangel                              | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Der Anschluss zum ISP wird ausreichend dimensioniert.                                                                              |
| G 0.28 Software- Schwachstellen oder - Fehler        | mittel                              | Risikoreduktion: Updates zur Fehlerbehebung müssen zeitnah eingespielt werden.                                                                      |
| G 0.28 Software- Schwachstellen oder - Fehler        | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Updates zur Fehlerbehebung müssen zeitnah eingespielt werden.                                                                      |
| G 0.40 Verhinderung von Diensten (Denial of Service) | mittel                              | Risikoreduktion: Der Anschluss zum ISP wird ausreichend dimensioniert. Zusätzlich wird ein redundanter Anschluss bei einem anderen ISP vorgehalten. |
| G 0.40 Verhinderung von Diensten (Denial of Service) | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Der Anschluss zum ISP wird ausreichend dimensioniert. Zusätzlich wird ein redundanter Anschluss bei einem anderen ISP vorgehalten. |

<!-- page: 127 -->

## Alarmierungsnetz für Funkmeldeempfänger N7

Vertraulichkeit: sehr hoch

Integrität: sehr hoch

Verfügbarkeit: sehr hoch

| Gefährdung                                       | Risikokategorie                     | Risikobehandlungsoptionen                                                                                                                                               |
|--------------------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G 0.15 Abhören                                   | Sehr hoch                           | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
| G 0.15 Abhören                                   | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
| G 0.15 Offenlegung schützenswerter Informationen | Sehr hoch                           | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
| G 0.15 Offenlegung schützenswerter Informationen | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
| G 0.25 Ausfall von Geräten oder Systemen         | mittel                              | Risikoreduktion: Benötigte Netzkomponenten werden redundant vorgehalten. Als Rückfallebene wird ein weiteres Alarmierungssystem parallel betrieben, z.B. über eine App. |
| G 0.25 Ausfall von Geräten oder Systemen         | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Benötigte Netzkomponenten werden redundant vorgehalten. Als Rückfallebene wird ein weiteres Alarmierungssystem parallel betrieben, z.B. über eine App. |
| G 0.26 Fehlfunktion von Geräten oder Systemen    | mittel                              | Risikoreduktion: Die Netzkomponenten und Geräte werden vor der Inbetriebnahme ausgiebig geprüft.                                                                        |
| G 0.26 Fehlfunktion von Geräten oder Systemen    | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Die Netzkomponenten und Geräte werden vor der Inbetriebnahme ausgiebig geprüft.                                                                        |
| G 0.38 Missbrauch personenbezogener Daten        | mittel                              | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |
| G 0.38 Missbrauch personenbezogener Daten        | Nach erzänzen- der Maßnahme: gering | Risikoreduktion: Die übermittelten Nachrichten werden verschlüsselt.                                                                                                    |

## Tabelle A-35: Behandlung der Risiken des Alarmierungsnetzes.

Durch die aufgeführten Maßnahmen zur Risikoreduktion können alle Risiken der Objekte N4 und N7 als gering eingestuft und somit akzeptiert werden. Es ist möglich, dass Schritte zur Risikoreduktion mehrfach durchlaufen werden müssen bis die Kriterien zur Akzeptanz eines Risikos erreicht wird. Zum Beispiel muss die Bandbreite des Internetanschlusses eventuell mehrfach nach oben skaliert werden um das Risiko eines Ressourcenmangels als gering einzuordnen.

## 10.5 Risikobeobachtung

Es kann sein, dass Risiken derzeit als gering eingestuft und daher akzeptiert werden können. Jedoch können sich Bedingungen ändern und das Risiko bestimmter Gefährdungen steigen. Alle Risiken sollten daher ständig beobachtet werden. Im Optimalfall werden bereits Konzepte für die Behandlung von Risiken erarbeitet, sollten sich diese erhöhen. Kann ein Risiko nicht mehr akzeptiert werden, ist hierdurch eine unmittelbare Reaktion möglich.

<!-- page: 128 -->

## Cybersecurity in a PSAP - a practical approach

Author:

Henning Schmidtpott

<!-- page: 129 -->

## Table of Contents

1 Executive Summary.......................................................................................................................B-3

2 Specification of scope....................................................................................................................B-3

3 Specification of information domain.............................................................................................B-4

3.1 Components of information domain......................................................................................B-4

3.2 Not considered components...................................................................................................B-4

4 Reference architecture...................................................................................................................B-4

4.1 Processes................................................................................................................................B-5

4.2 Applications...........................................................................................................................B-6

4.3 IT systems..............................................................................................................................B-6

4.4 Communication links and network........................................................................................B-6

4.5 Network diagram...................................................................................................................B-7

4.6 Buildings and rooms..............................................................................................................B-8

4.7 Handling differences..............................................................................................................B-8

5 Protection requirements.................................................................................................................B-8

5.1 Assessment of protection requirements.................................................................................B-8

5.1.1 Protection requirements for processes.........................................................................B-10

5.1.2 Protection requirements for applications......................................................................B-11

5.1.3 Protection requirements for IT systems.......................................................................B-12

5.1.4 Protection requirements for communication links and networks.................................B-13

5.1.5 Protection requirements for buildings and rooms........................................................B-14

5.2 Measures..............................................................................................................................B-15

5.3 General relevant modules....................................................................................................B-20

5.4 Relevant modules for specific objects.................................................................................B-24

6 Directions for use........................................................................................................................B-29

7 Supporting information...............................................................................................................B-30

<!-- page: 130 -->

## 1 Executive Summary

This paper is build on the EENA document Cybersecurity - Guidelines and Best Practices for Emergency  Services 1 and   on   the   recommended   approach   of   the   German   Federal   Office   for Information Security (BSI) IT-Grundschutz 2 . The aim is to help Public Safety Answering Points (PSAPs) by publishing a concrete approach to make their systems safer and resistant against cyberattacks. The document is splitted in different parts. In the first part the formal frame conditions are set. In the   second   part   the   reference   architecture   of   a   typical   PSAP  is   specified   and   the   protection requirements   for   the   different   objects   are   identified.   In   the   third   part   the   measures   to   be implemented are determined. Both, requirements and measures, are corresponding to BSI ITGrundschutz. The standard protection of IT-Grundschutz is compatible to ISO 27001 certification.

## 2 Specification of scope

## Target audience

This paper is aimed to decision-maker of information technology in PSAPs, industrial solution providers offering products and planning offices for PSAPs.

## Protection requirements

Operational readiness of PSAPs must be guaranteed permanent. Correctness and confidentiality of the processed data have to be emphasized. The aims of IT security, confidentiality, availability and integrity have to be achieved far in excess of the usual quality. So the level of cyber security protection of a PSAP has to be above the Standard Protection of the BSI IT-Grundschutz.

## IT-Grundschutz procedure

BSI IT-Grundschutz offers the three approaches Basis Protection, Standard Protection and Core Protection.   Depending   of   the   chosen   approach,   the   requirements   in   the   modules   have   to   be implemented. The requirements in this paper corresponding at least the Standard Protection of BSI-Standard 200-2. Furthermore it is recommended to implement some requirements of the higher protection need.

## Compatability to other standards

By implementing the Standard Protection compatibility to ISO 27001 is given.

## Framework

The GDPR 3 is considered.

1

2

3

[https://eena.org/wp-content/uploads/2018/11/Cybersecurity-Guidelines-and-Best-Practices-for-Emergency-](https://eena.org/wp-content/uploads/2018/11/Cybersecurity-Guidelines-and-Best-Practices-for-Emergency-Services.pdf)

Services.pdf (requested 2019/07/01)

[https://www.bsi.bund.de/EN/Topics/ITGrundschutz/itgrundschutz\_node.html   (requested 2019/07/01)](https://www.bsi.bund.de/EN/Topics/ITGrundschutz/itgrundschutz_node.html)

[https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1528874672298&amp;uri=CELEX%3A32016R0679   (requested](https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1528874672298&uri=CELEX%3A32016R0679)

2019/07/01)

<!-- page: 131 -->

## 3 Specification of information domain

The information domain indicates the associated components of the general institution or of a specific scope of application. In a first step the information domain has to be specified by defining the relevant and not relevant parts for cyber security in PSAPs considered in this paper.

## 3.1 Components of information domain

The following table shows the technical parts of the information domain supporting the processes within a PSAP considered in this paper.

Table B-1: Technical parts of the information domain

| Identifier   | Objects of information domain   |
|--------------|---------------------------------|
| ID1          | Processes                       |
| ID2          | Applications                    |
| ID3          | Buildings and rooms             |
| ID4          | IT systems                      |
| ID5          | Communication and networks      |

## 3.2 Not considered components

Not considered in this paper is the broadcasting system. The broadcasting system is an independent system with interfaces to the CAD and ICCS systems in the PSAP and needs to be considered separate.

The protection of the external telecommunication connections is in responsibility of the network operators. The PSAPs can't intervene in this domain or take any provisions. For this reason the telecommunication connections are not part of this paper.

As well mobile Apps are not part of this paper. CAD or ICCS systems in the PSAPs may have interfaces   to   receive   or   send   information   by  Apps   but   the   security   of   the  App   itself   isn't   in responsibility of the PSAP as it has to be seen as a third party application.

## 4 Reference architecture

The reference architecture  includes buildings and  rooms  in which  the  PSAP is  operated,  the communication links, networks and the components required for them. In addition, all involved IT systems, the applications used and the processes running in the PSAPs are listed in the reference architecture.

It is possible that the reference architecture differs from the actual existing architecture of a PSAP. The handling of such deviations is described in Section 4.7.

<!-- page: 132 -->

## 4.1 Processes

The   operation   of   a   PSAP   is   subdivided   into   different   processes,   which   are   relevant   for implementing the BSI IT-Grundschutz. These processes are defined in this section. The core processes are the receipt of the incoming emergency information and the input in the CAD, the processing and attendance of the mission, as well as the post-processing and completion of the mission (see 1).

<!-- image -->

In the following table, the processes to be carried out in the PSAP are subdivided into sub-processes and provided with an identifier.

| Identifier   | Process of information domain                                        |
|--------------|----------------------------------------------------------------------|
| P1.1         | Information receipt by phone call                                    |
| P1.2         | Information receipt by telefax                                       |
| P1.3         | Information receipt by E-Mail                                        |
| P1.4         | Information receipt by broadcast                                     |
| P1.5         | Information receipt by Web                                           |
| P1.6         | Information receipt by automatic fire alarm systems                  |
| P1.7         | Information receipt by eCall                                         |
| P2.1         | Input in CAD manually                                                |
| P2.2         | Input in CAD automatically                                           |
| P3.1         | Dispatch                                                             |
| P3.2         | Alarm                                                                |
| P3.3         | Control                                                              |
| P3.4         | Documentation                                                        |
| P4.1         | Transmit data to third parties                                       |
| P4.2         | Archiving                                                            |
| P5.1         | Receiving data by e-Mail and on USB storage (master data management) |
| P5.2         | Input of data in CAD and ICCS (master data management)               |
| P6           | Conferences and training                                             |

<!-- page: 133 -->

## 4.2 Applications

In addition to the processes, the information domain also includes the applications that support optimal processing of the processes. These are in a PSAP in particular the CAD and the ICCS. EMail client and webbrowser are also important components. All applications are listed in the following table with an identifier. The right-hand column indicates which processes are supported by the applications.

| Identifier   | Applications of information domain     | Supported processes          |
|--------------|----------------------------------------|------------------------------|
| A1           | CAD                                    | P1.6, P1.7, P2, P3, P4, P5.2 |
| A2           | ICCS                                   | P1.1, P1.4, P1.7, P3, P5.2   |
| A3           | Webbrowser                             | P1.5, P3, P5                 |
| A4           | E-Mail client                          | P1.3, P5.1                   |
| A5           | Hazardous material information systems | P2.1, P3                     |
| A6           | PDF-Viewer                             | P2.1, P3, P5                 |
| A7           | Office-Products                        | P5.1                         |
| A8           | File depot, network drive              | P4, P5                       |

## 4.3 IT systems

In addition to the applications, the IT systems required for operating the applications are also part of the information domain. These include, for example, operating systems, or the hardware provided for this purpose. Components that affect network connections are considered separately in section 4.4.

| Identifier   | IT systems of information domain   | Depending objects              |
|--------------|------------------------------------|--------------------------------|
| S1.1         | Operating systems for Clients      | A1, A2, A3, A4, A5, A6, A7, A8 |
| S1.2         | Operating systems for Servers      | A1, A2                         |
| S2.1         | Server                             | A1, A2                         |
| S2.2         | Virtualization platforms           | A1, A2                         |
| S3           | Work station clients               | A1, A2, A3, A4, A5, A6, A7, A8 |
| S4           | Fax machine                        | P1.2                           |
| S5           | Printer and Scanner                | A1, A6, A7                     |

## 4.4 Communication links and network

Applications and IT systems of the PSAP are integrated in various networks. Even if the number and structure of the networks can not be generalized in detail, it is assumed that the architecture is at least similar in many control centers. The operation of the networks requires active and passive network components.

<!-- page: 134 -->

Table B-2: Networks and components of information domain

| Identifier   | Networks of information domain       | Depending objects                      |
|--------------|--------------------------------------|----------------------------------------|
| N1           | CAD network                          | A1, S1, S2, S3, S5                     |
| N2           | ICCS network                         | A2, S1, S2, S3, S5                     |
| N3           | Office network                       | A3, A4, A5, A6, A7, A8, S1, S2, S3, S5 |
| N4           | Network to Internet Service Provider | A1, A2, A3, A4                         |
| N5.1         | Router                               | N1, N2, N3                             |
| N5.2         | Switches                             | N1, N2, N3                             |
| N5.3         | Firewalls                            | N1, N2, N3                             |
| N5.4         | Session Border Controller            | N2                                     |
| N6           | Cable and patch panels               | N1, N2, N3                             |
| N7           | Alerting POCSAG network              | A1                                     |

## 4.5 Network diagram

Figure B-2: Network diagram

<!-- image -->

<!-- page: 135 -->

## 4.6 Buildings and rooms

Not only the information technology components play a major role in information security. The security of the buildings and rooms in which the PSAP operates must also be taken into account. This does not only apply to the dispatching room, where the emergency calls are received and the rescue services are dispatched. The rooms where servers and other technology are housed must be considered as well as the office space for administrative employees.

Table B-3: Rooms of information domain

| Identifi er   | Rooms of information domain    | Depending objects      |
|---------------|--------------------------------|------------------------|
| R1            | Dispatching room               | P1, P2, P3, S3, S4, S5 |
| R2            | Computer center                | S2                     |
| R3.1          | Management office rooms        | S3, S4, S5             |
| R3.2          | Master data management office  | P5, S3, S4, S5         |
| R3.3          | System administrator office    | S3, S4, S5             |
| R4            | Telecommunication network room | N2, N4                 |
| R5            | Archive room                   | P4                     |
| R6            | Conference- and training room  | P6                     |

## 4.7 Handling differences

If   the   information   domain   to   be   protected   differs   from   the   reference   architecture,   the additional   or   non-existent   objects   have   to   be   documented.   These   objects   have   to   be allocated   to   suitable   components   of   the   BSI   IT-Grundschutz   Compendium.   The   derived requirements must be adjusted depending on the protection requirements.

## 5 Protection requirements

The   BSI IT-Grundschutz   Compendium   provides   modules   that   provide   application   specific recommendations   for   the   implementation   of   IT-Grundschutz.   First   of   all,   the   protection requirements of the processes, applications, IT systems and communication links must be defined. Afterwards, the relevant modules have to be identified and an adaptation of the requirements to the corresponding target group has to be carried out. The result of adapting the requirements may mean that   all   or   only   certain   requirements   of   the   module   are   relevant   for   information   security   in emergency response centers. Also requirements can be considered as completely irrelevant. The relevance of the measures listed in the requirements must also be identified.

## 5.1 Assessment of protection requirements

When determining the protection requirements, the implications of violating the basic objectives of information security, confidentiality, integrity or availability are fundamental. These effects are considered below. The BSI names various scenarios to which damage can relate. This takes into account the damage scenarios listed in table 4. Violations of laws, regulations or contracts (DS1) may be present, for example, if the PSAP is not ready for operation and thus can not fulfill its tasks (DS4). At the same time, this can lead to impairments to the personal integrity of the caller (DS3) if it is not helped on time. Infringements of data   protection   laws   also   fall   under   damage   scenario   1.   The   transmission   of   confidential information, via callers or patients to unauthorized persons, also constitutes an impairment of the informational right of self-determination of the persons seeking help (DS2). All of these cases can also have financial consequences for the PSAP due to claims for damages by the victims (DS6). For the citizens, a high level of confidence in the work of the PSAP is fundamental. Being helped in an emergency gives people a safe feeling. Due to a negative external effect (DS5) this certainty can be lost. The same applies to the own personnel of the PSAP or the affiliated rescue organizations with a negative interior effect. These effects can occur, for example, due to defaults and associated negative media coverage.

<!-- page: 136 -->

| Identifier   | Damage Scenario                                             |
|--------------|-------------------------------------------------------------|
| DS1          | Violations of laws, regulations or contracts                |
| DS2          | Impairment of the informational right of self-determination |
| DS3          | Impaired personal integrity                                 |
| DS4          | Impairment of task fulfillment                              |
| DS5          | Negative interior or exterior effect                        |
| DS6          | Financial impacts                                           |

## Table B-4: prospective damage scenarios

The damage scenarios are considered individually in the following sections for each of the basic objectives of information security. The damage impact can usually not be determined in detail in advance. For this reason, the IT-Grundschutz methodology of the BSI recommends defining three categories that classify the protection requirement. The three categories are normal, high or very high. Table 5 lists the categories, plus the damage impact. The damage impact can always refer to the PSAP itself or to the citizens seeking help.

| categorie   | Recommended protection needs                                                                                                                                                                                                                          |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| normal      | The effects of damage for the PSAP or the citizens seeking for help are limited and manageable.The damage effects can considerably restrict the operation of the control center. For the citizens seeking help, the consequences can be considerable. |
| high        | The damage effects can considerably restrict the operation of the PSAP. For the citizens seeking for help, the consequences can be considerable.                                                                                                      |
| very high   | The damage effects can shut down the operation of the PSAP. For people seeking help, there can be existential or life-threatening consequences.                                                                                                       |

## Table B-5: Recommended protection needs

When determining the protection requirements of an object specified in Section  4, it is always necessary to consider the processes or other objects for which this object is needed. If, for example, an   object   is   used   for   a   process   whose   protection   requirement   is   very   high,   the   protection requirement of the object considered must also be classified as very high.

<!-- page: 137 -->

## 5.1.1 Protection requirements for processes

For determining the protection requirements of the processes, the extent of damage to the respective process   must   be   determined.   First   of   all,   every   process   defined   in   section  4.1  is   examined concerning confidentiality. This is followed by an inquiry into integrity. Finally, the protection requirement for the availability of the individual processes is determined.

| Protection requirements concerning confidentiality for processes   | Protection requirements concerning confidentiality for processes   | Protection requirements concerning confidentiality for processes         |
|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------|
| Object                                                             | Protection need                                                    | Reasons                                                                  |
| P1.1                                                               | very high                                                          | Processing of personal data with medical diagnosis (DS1, DS2, DS5, DS6). |
| P1.2                                                               | very high                                                          | Processing of personal data with medical diagnosis (DS1, DS2, DS5, DS6). |
| P1.3                                                               | normal                                                             | PSAPs usually don't receive confidential data by e-Mail.                 |
| P1.4                                                               | very high                                                          | Processing of personal data with medical diagnosis (DS1, DS2, DS5, DS6). |
| P1.5                                                               | very high                                                          | Processing of personal data with medical diagnosis (DS1, DS2, DS5, DS6). |
| P1.6                                                               | normal                                                             | Only technical parameters are transmitted.                               |
| P1.7                                                               | normal                                                             | Only technical parameters are transmitted.                               |
| P2.1                                                               | very high                                                          | Processing of personal data with medical diagnosis (DS1, DS2, DS5, DS6). |
| P2.2                                                               | normal                                                             | Only technical parameters are processed.                                 |
| P3                                                                 | very high                                                          | Processing of personal data with medical diagnosis (DS1, DS2, DS5, DS6). |
| P4                                                                 | very high                                                          | Processing of personal data with medical diagnosis (DS1, DS2, DS5, DS6). |
| P5                                                                 | high                                                               | Processing of personal data (DS1, DS2, DS5, DS6).                        |

| Protection requirements concerning integrity for processes   | Protection requirements concerning integrity for processes   | Protection requirements concerning integrity for processes                                               |
|--------------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Object                                                       | Protection need                                              | Reasons                                                                                                  |
| P1, P2, P3, P5                                               | very high                                                    | Life-threatening consequences by processing incorrect data or faulty behavior (DS1, DS3, DS4, DS5, DS6). |
| P4, P6                                                       | normal                                                       | Slight consequences by processing incorrect data or faulty behavior (DS1, DS6).                          |

<!-- page: 138 -->

| Protection requirements concerning availability for processes   | Protection requirements concerning availability for processes   | Protection requirements concerning availability for processes                                                             |
|-----------------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Object                                                          | Protection need                                                 | Reasons                                                                                                                   |
| P1.1, P1.2                                                      | very high                                                       | Life-threatening consequences by failure of emergency number 112 (DS1, DS3, DS4, DS5, DS6).                               |
| P1.3                                                            | normal                                                          | Slight consequences by failure of e-Mail, because emergency messages usually are not received by e-Mail (DS4, DS5).       |
| P1.4                                                            | normal                                                          | Alternative ways of communication can be used (DS4, DS5).                                                                 |
| P1.5                                                            | very high                                                       | Consequences increase if non phone emergency calls are received by webbrowser e.g. from an app (DS1, DS3, DS4, DS5, DS6). |
| P1.6                                                            | very high                                                       | High material damage possible (DS1, DS3, DS4, DS5, DS6).                                                                  |
| P1.7                                                            | very high                                                       | Life-threatening consequences by failure of eCall receiver (SZ1, SZ3, SZ4, SZ5, SZ6).                                     |
| P2, P3                                                          | very high                                                       | Life-threatening consequences by failure of CAD (DS1, DS3, DS4, DS5, DS6).                                                |
| P4, P5                                                          | normal                                                          | Slight consequences as processes are not time-critical (DS4, DS6).                                                        |

## 5.1.2 Protection requirements for applications

The protection requirements for applications  are  based  on the  protection  requirements of  the processes that are supported by the use of the particular application. The maximum principle is taken into account and the highest protection requirements are inherited by the application. If the protection requirement for only a part of the processes supported by the applications is classified as very high, then the protection requirement of the entire application must be rated as very high as well.

| Protection requirements concerning confidentiality for applications   | Protection requirements concerning confidentiality for applications   | Protection requirements concerning confidentiality for applications   |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| Object                                                                | Protection need                                                       | Reasons                                                               |
| A1                                                                    | very high                                                             | Very high protection requirements for P2.1, P3 und P4.                |
| A2                                                                    | very high                                                             | Very high protection requirements for P1.1, P1.4 und P3.              |
| A3                                                                    | very high                                                             | Very high protection requirements for P1.5 und P3.                    |
| A4                                                                    | high                                                                  | High protection requirements for P5.1.                                |
| A5                                                                    | very high                                                             | Very high protection requirements for P2.1 und P3.                    |
| A6                                                                    | very high                                                             | Very high protection requirements for P2.1 und P3.                    |
| A7                                                                    | high                                                                  | High protection requirements for P5.1.                                |
| A8                                                                    | very high                                                             | Very high protection requirements for P4.                             |

<!-- page: 139 -->

| Protection requirements concerning integrity for applications   | Protection requirements concerning integrity for applications   | Protection requirements concerning integrity for applications        |
|-----------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------|
| Object                                                          | Protection need                                                 | Reasons                                                              |
| A1                                                              | very high                                                       | Very high protection requirements for P1.6, P1.7, P2, P3 und P5.2.   |
| A2                                                              | very high                                                       | Very high protection requirements for P1.1, P1.4, P1.7, P3 und P5.2. |
| A3                                                              | very high                                                       | Very high protection requirements for P1.5, P3 und P5.               |
| A4                                                              | very high                                                       | Very high protection requirements for P1.3 und P5.1.                 |
| A5                                                              | very high                                                       | Very high protection requirements for P2.1 und P3.                   |
| A6                                                              | very high                                                       | Very high protection requirements for P2.1, P3 und P5.               |
| A7                                                              | very high                                                       | Very high protection requirements for P5.1.                          |
| A8                                                              | very high                                                       | Very high protection requirements for P5.                            |

| Protection requirements concerning availability for applications   | Protection requirements concerning availability for applications   | Protection requirements concerning availability for applications   |
|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Object                                                             | Protection need                                                    | Reasons                                                            |
| A1                                                                 | very high                                                          | Very high protection requirements for P1.6, P1.7, P2 und P3.       |
| A2                                                                 | very high                                                          | Very high protection requirements for P1.1, P1.7 und P3.           |
| A3                                                                 | very high                                                          | Very high protection requirements for P1.5 und P3.                 |
| A4                                                                 | normal                                                             | Normal protection requirements for P1.3 und P5.1.                  |
| A5                                                                 | very high                                                          | Very high protection requirements for P2.1 und P3.                 |
| A6                                                                 | very high                                                          | Very high protection requirements for P2.1 und P3.                 |
| A7                                                                 | normal                                                             | Normal protection requirements for P5.1.                           |
| A8                                                                 | normal                                                             | Normal protection requirements for P5 und P5.                      |

## 5.1.3 Protection requirements for IT systems

The protection requirements for the IT systems of a PSAP depend on the applications that are installed on or connected to the IT systems. According to the maximum principle, the protection requirement must again be at least as high as for these applications.

<!-- page: 140 -->

| Protection requirements concerning confidentiality for IT systems   | Protection requirements concerning confidentiality for IT systems   | Protection requirements concerning confidentiality for IT systems   |
|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Object                                                              | Protection need                                                     | Reasons                                                             |
| S1.1                                                                | very high                                                           | Very high protection requirements for A1, A2, A3, A5, A6, A8        |
| S1.2                                                                | very high                                                           | Very high protection requirements for A1, A2                        |
| S2                                                                  | very high                                                           | Very high protection requirements for A1, A2                        |
| S3                                                                  | very high                                                           | Very high protection requirements for A1, A2, A3, A5, A6, A8        |
| S4                                                                  | very high                                                           | Very high protection requirements for P1.2                          |
| S5                                                                  | very high                                                           | Very high protection requirements for A1, A6                        |

| Protection requirements concerning integrity for IT systems   | Protection requirements concerning integrity for IT systems   | Protection requirements concerning integrity for IT systems          |
|---------------------------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------------------|
| Object                                                        | Protection need                                               | Reasons                                                              |
| S1.1                                                          | very high                                                     | Very high protection requirements for A1, A2, A3, A4, A5, A6, A7, A8 |
| S1.2                                                          | very high                                                     | Very high protection requirements for A1, A2                         |
| S2                                                            | very high                                                     | Very high protection requirements for A1, A2                         |
| S3                                                            | very high                                                     | Very high protection requirements for A1, A2, A3, A4, A5, A6, A7, A8 |
| S4                                                            | very high                                                     | Very high protection requirements for P1.2                           |
| S5                                                            | very high                                                     | Very high protection requirements for A1, A6, A7                     |

| Protection requirements concerning availability for IT systems   | Protection requirements concerning availability for IT systems   | Protection requirements concerning availability for IT systems   |
|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Object                                                           | Protection need                                                  | Reasons                                                          |
| S1.1                                                             | very high                                                        | Very high protection requirements for A1, A2, A3, A5, A6         |
| S1.2                                                             | very high                                                        | Very high protection requirements for A1, A2                     |
| S2                                                               | very high                                                        | Very high protection requirements for A1, A2                     |
| S3                                                               | very high                                                        | Very high protection requirements for A1, A2, A3, A5, A6         |
| S4                                                               | very high                                                        | Very high protection requirements for P1.2                       |
| S5                                                               | very high                                                        | Very high protection requirements for A1, A6                     |

## 5.1.4 Protection requirements for communication links and networks

Many applications and IT systems used in the PSAP transmit and receive data via the networks and components defined in Section 4.4. The protection requirements of the networks and components thus depend on the protection requirements of the applications and IT systems that transmit and receive data via these networks.

<!-- page: 141 -->

| Protection requirements concerning confidentiality for networks   | Protection requirements concerning confidentiality for networks   | Protection requirements concerning confidentiality for networks   |
|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Object                                                            | Protection need                                                   | Reasons                                                           |
| N1                                                                | very high                                                         | Very high protection requirements for A1                          |
| N2                                                                | very high                                                         | Very high protection requirements for A2                          |
| N3                                                                | very high                                                         | Very high protection requirements for A3, A5, A6, A8              |
| N4                                                                | very high                                                         | Very high protection requirements for N1, N2 und N3               |
| N5                                                                | very high                                                         | Very high protection requirements for N1, N2 und N3               |
| N6                                                                | very high                                                         | Very high protection requirements for A1                          |

| Protection requirements concerning integrity for networks   | Protection requirements concerning integrity for networks   | Protection requirements concerning integrity for networks   |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| Object                                                      | Protection need                                             | Reasons                                                     |
| N1                                                          | very high                                                   | Very high protection requirements for A1                    |
| N2                                                          | very high                                                   | Very high protection requirements for A2                    |
| N3                                                          | very high                                                   | Very high protection requirements for A3, A5, A6, A7, A8    |
| N4                                                          | very high                                                   | Very high protection requirements for N1, N2 und N3         |
| N5                                                          | very high                                                   | Very high protection requirements for N1, N2 und N3         |
| N6                                                          | very high                                                   | Very high protection requirements for A1                    |

| Protection requirements concerning availability for networks   | Protection requirements concerning availability for networks   | Protection requirements concerning availability for networks   |
|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Object                                                         | Protection need                                                | Reasons                                                        |
| N1                                                             | very high                                                      | Very high protection requirements for A1                       |
| N2                                                             | very high                                                      | Very high protection requirements for A2                       |
| N3                                                             | very high                                                      | Very high protection requirements for A3, A5, A6               |
| N4                                                             | very high                                                      | Very high protection requirements for N1, N2 und N3            |
| N5                                                             | very high                                                      | Very high protection requirements for N1, N2 und N3            |
| N6                                                             | very high                                                      | Very high protection requirements for A1                       |

## 5.1.5 Protection requirements for buildings and rooms

The determination of protection requirements for rooms depends on the IT systems installed in the room and the processes that are carried out in these rooms. The higher their need for protection, the higher the need for protection for the room. When determining the protection requirement, the amount of systems installed in the room must also be taken into account.

<!-- page: 142 -->

| Protection requirements concerning confidentiality for buildings and rooms   | Protection requirements concerning confidentiality for buildings and rooms   | Protection requirements concerning confidentiality for buildings and rooms   |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Object                                                                       | Protection need                                                              | Reasons                                                                      |
| R1                                                                           | very high                                                                    | Very high protection requirements for P1, P2, P3, S3, S4, S5                 |
| R2                                                                           | very high                                                                    | Very high protection requirements for S2                                     |
| R3                                                                           | very high                                                                    | Very high protection requirements for S3, S4, S5 und P5                      |
| R4                                                                           | very high                                                                    | Very high protection requirements for N2                                     |
| R5                                                                           | very high                                                                    | Very high protection requirements for P4                                     |
| R6                                                                           | normal                                                                       | Normal protection requirements for P6                                        |

| Protection requirements concerning integrity for buildings and rooms   | Protection requirements concerning integrity for buildings and rooms   | Protection requirements concerning integrity for buildings and rooms   |
|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Object                                                                 | Protection need                                                        | Reasons                                                                |
| R1                                                                     | very high                                                              | Very high protection requirements for S3, S4, S5                       |
| R2                                                                     | very high                                                              | Very high protection requirements for S2                               |
| R3                                                                     | very high                                                              | Very high protection requirements for S3, S4, S5                       |
| R4                                                                     | very high                                                              | Very high protection requirements for N2                               |
| R5                                                                     | very high                                                              | Normal protection requirements for P4                                  |
| R6                                                                     | normal                                                                 | Normal protection requirements for P6                                  |

| Protection requirements concerning availability for buildings and rooms   | Protection requirements concerning availability for buildings and rooms   | Protection requirements concerning availability for buildings and rooms   |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Object                                                                    | Protection need                                                           | Reasons                                                                   |
| R1                                                                        | very high                                                                 | Very high protection requirements for P1, P2 und P3                       |
| R2                                                                        | very high                                                                 | Very high protection requirements for S2                                  |
| R3                                                                        | normal                                                                    | Using alternative room is possible                                        |
| R4                                                                        | very high                                                                 | Very high protection requirements for N2                                  |
| R5                                                                        | very high                                                                 | Normal protection requirements for P4                                     |
| R6                                                                        | normal                                                                    | Normal protection requirements for P6                                     |

## 5.2 Measures

The IT-Grundschutz Compendium of the BSI provides modules that provide application-specific recommendations   for   the   implementation   of   IT-Grundschutz.   After   having   determined   the protection requirements of the processes, applications, IT systems and communication networks in the last section, the next step is to identify the relevant modules and adapt the requirements to the corresponding target group. The result of adapting the requirements may mean that all or only certain requirements of the module are relevant for information security in PSAPs. Likewise, requirements can be considered completely irrelevant. The relevance of the measures listed in the requirements must also be identified. In addition, specifications for implementing the requirements of the blocks are described. The modules of the category Industrial IT are   not   listed   from   the   outset   due   to   their   lack   of relevance for the operation of PSAPs.

<!-- page: 143 -->

| Module                                        | Module                                        | Relevant?                                     | Reason (if not relevant)                      |
|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| ISMS: Information Security Management Systems | ISMS: Information Security Management Systems | ISMS: Information Security Management Systems | ISMS: Information Security Management Systems |
| ISMS.1                                        | Security Management                           | Yes                                           |                                               |
| ORP: Organisation and Personnel               | ORP: Organisation and Personnel               | ORP: Organisation and Personnel               | ORP: Organisation and Personnel               |
| ORP.1                                         | Organisation                                  | Yes                                           |                                               |
| ORP.2                                         | Personell                                     | Yes                                           |                                               |
| ORP.3                                         | Awareness and Training                        | Yes                                           |                                               |
| ORP.4                                         | Identity and Access Management                | Yes                                           |                                               |
| ORP.5                                         | Comliance Management                          | Yes                                           |                                               |
| CON: Concepts                                 | CON: Concepts                                 | CON: Concepts                                 | CON: Concepts                                 |
| CON.1                                         | Crypto Concept                                | Yes                                           |                                               |
| CON.2                                         | Data Protection                               | Yes                                           |                                               |
| CON.3                                         | Backup Concept                                | Yes                                           |                                               |
| CON.4                                         | Selection and Use of Standard Software        | Yes                                           |                                               |
| CON.5                                         | Development and Use of Generic Applications   | Yes                                           |                                               |
| CON.6                                         | Deleting and Destroying                       | Yes                                           |                                               |
| CON.7                                         | Information Security on Trips Abroad          | No                                            | PSAPs usually work local only                 |
| OPS: Operation                                | OPS: Operation                                | OPS: Operation                                | OPS: Operation                                |
| OPS.1.1.2                                     | Proper IT Administration                      | Yes                                           |                                               |
| OPS.1.1.3                                     | Patch and Change Management                   | Yes                                           |                                               |
| OPS.1.1.4                                     | Protection Against Malware                    | Yes                                           |                                               |
| OPS.1.1.5                                     | Logging                                       | Yes                                           |                                               |
| OPS.1.1.6                                     | Software Tests and Approvals                  | Yes                                           |                                               |
| OPS.1.2.2                                     | Archiving                                     | Yes                                           |                                               |

<!-- page: 144 -->

| OPS.1.2.3                   | Exchange of Information and Storage Media         | Yes                         |                                                             |
|-----------------------------|---------------------------------------------------|-----------------------------|-------------------------------------------------------------|
| OPS.1.2.4                   | Teleworking                                       | No                          | Employees of PSAPs usually work in the PSAP rooms.          |
| OPS.2.1                     | Outsourcing for Customers                         | Yes                         |                                                             |
| OPS.2.2                     | Cloud Usage                                       | No                          | Operation of IT systems in PSAPs usually is in local rooms. |
| OPS.2.4                     | Remote Maintenance                                | Yes                         |                                                             |
| OPS.3.1                     | Outsourcing for Third Parties                     | No                          | PSAPs usually don't deliver IT services for third parties.  |
| DER: Detection and Reaction | DER: Detection and Reaction                       | DER: Detection and Reaction | DER: Detection and Reaction                                 |
| DER.1                       | Detecting Security-Relevant Events                | Yes                         |                                                             |
| DER.2.1                     | Security Incident Handling                        | Yes                         |                                                             |
| DER.2.2                     | Provisions for IT Forensics                       | Yes                         |                                                             |
| DER.2.3                     | Clean-Up of Extensive Security Incidents          | Yes                         |                                                             |
| DER.3.1                     | Audits and Revisions                              | Yes                         |                                                             |
| DER.3.2                     | Audits Based on the BSI 'Guideline for IS Audits' | Yes                         |                                                             |
| DER.4                       | Business Continuity Management                    | Yes                         |                                                             |

The following table lists the system modules. Here it is crucial whether the module is relevant to a specific component defined in Section 4.

| Module            |                            | Relevant?         | Reason (if not relevant)                                                                                             |
|-------------------|----------------------------|-------------------|----------------------------------------------------------------------------------------------------------------------|
| APP: Applications | APP: Applications          | APP: Applications | APP: Applications                                                                                                    |
| APP.1.1           | Office Products            | Yes               |                                                                                                                      |
| APP.1.2           | Web Browsers               | Yes               |                                                                                                                      |
| APP.1.4           | Mobile Applications (Apps) | No                | For apps to alert the connected organizations or emergency apps, the respective operators and users are responsible. |
| APP.2.1           | General Directory Service  | No                | Especially in smaller PSAPs, a user administration is performed purely at the level of CAD and ICCS.                 |
| APP.2.2           | Active Directory           | No                | see APP.2.1                                                                                                          |
| APP.2.3           | OpenLDAP                   | No                | see APP.2.1                                                                                                          |
| APP.3.1           | Web Applications           | No                | Own web applications are usually not required.                                                                       |

<!-- page: 145 -->

| APP.3.2         | Web servers                      | No              | For the operation of the PSAP usually not necessary.                                                                                                |
|-----------------|----------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| APP.3.3         | File Servers                     | Yes             |                                                                                                                                                     |
| APP.3.4         | Samba                            | No              | For the operation of the PSAP usually not necessary.                                                                                                |
| APP.3.6         | DNS Servers                      | No              | DNS can usually be operated as a subprocess on routers or firewalls in PSAPs.                                                                       |
| APP.4.2         | SAP ERP System                   | No              | Usually not available in PSAPs.                                                                                                                     |
| APP.4.3         | Relational Database Systems      | Yes             | Used by CAD and ICCS.                                                                                                                               |
| APP.4.6         | SAP ABAP Programming             | No              | Usually not available in PSAPs.                                                                                                                     |
| APP.5.1         | General Groupware                | Yes             |                                                                                                                                                     |
| APP.5.2         | Microsoft Exchange and Outlook   | No              | Not mandatory, unless Exchange / Outlook is used. Take account to use alternative e-mail clients (for example Thunderbird, Lotus Notes, Groupwise). |
| SYS: IT Systems | SYS: IT Systems                  | SYS: IT Systems | SYS: IT Systems                                                                                                                                     |
| SYS.1.1         | General Server                   | Yes             |                                                                                                                                                     |
| SYS.1.2         | Windows Server 2012              | No              | Not mandatory for the operation of the PSAP.                                                                                                        |
| SYS.1.3         | Unix Servers                     | No              | Not mandatory for the operation of the PSAP.                                                                                                        |
| SYS.1.5         | Virtualisation                   | No              | Not mandatory for the operation of the PSAP.                                                                                                        |
| SYS.1.7         | IBM Z-System                     | No              | Usually not available in PSAPs.                                                                                                                     |
| SYS.1.8         | Storage Solutions                | No              | For the operation of the applications in the PSAP usually not required, since storage media can be connected directly to the server.                |
| SYS.2.1         | General Client                   | Yes             |                                                                                                                                                     |
| SYS.2.2.2       | Windows 8.1 Clients              | No              | Use of other Windows operating systems is possible.                                                                                                 |
| SYS.2.2.3       | Windows 10 Clients               | Yes             |                                                                                                                                                     |
| SYS.2.3         | Unix Clients                     | No              | Usually not available, as CAD and ICCS clients mostly require Windows.                                                                              |
| SYS.2.4         | MacOS Clients                    | No              | Usually not available, as CAD and ICCS clients mostly require Windows.                                                                              |
| SYS.3.1         | Laptops                          | No              | Not required for operation of the PSAP.                                                                                                             |
| SYS.3.2.1       | General Smartphones and Tablets  | No              | Usually not available in PSAPs.                                                                                                                     |
| SYS.3.2.2       | Mobile Device Manage- ment (MDM) | No              | Not required for operation of the PSAP.                                                                                                             |
| SYS.3.2.3       | iOS (for Enterprise)             | No              | Usually not available in PSAPs.                                                                                                                     |

<!-- page: 146 -->

| SYS.3.2.4                       | Android                                    | No                              | Usually not available in PSAPs.                                                               |
|---------------------------------|--------------------------------------------|---------------------------------|-----------------------------------------------------------------------------------------------|
| SYS.3.3                         | Mobile Telephones                          | No                              | Usually not available in PSAPs.                                                               |
| SYS.3.4                         | Mobile Storage Media                       | Yes                             |                                                                                               |
| SYS.4.1                         | Printers, Copiers, and All- in-One Devices | Yes                             |                                                                                               |
| SYS.4.3                         | Embedded Systems                           | No                              | Usually not available in PSAPs.                                                               |
| SYS.4.4                         | General IoT Devices                        | No                              | Usually not available in PSAPs.                                                               |
| NET: Networks and Communication | NET: Networks and Communication            | NET: Networks and Communication | NET: Networks and Communication                                                               |
| NET.1.1                         | Network Architecture and Design            | Yes                             |                                                                                               |
| NET.1.2                         | Network Management                         | Yes                             |                                                                                               |
| NET.2.1                         | WLAN Operation                             | No                              | Not required for the operation of the PSAP, since only fixed local workplaces are used.       |
| NET.2.2                         | WLAN Usage                                 | No                              | see NET.2.1                                                                                   |
| NET.3.1                         | Router and Switches                        | Yes                             |                                                                                               |
| NET.3.2                         | Firewall                                   | Yes                             |                                                                                               |
| NET.3.3                         | VPN                                        | Yes                             |                                                                                               |
| NET.4.1                         | Telecommunications Systems                 | Yes                             |                                                                                               |
| NET.4.2                         | VoIP                                       | Yes                             |                                                                                               |
| NET.4.3                         | Fax Machines and Fax Servers               | Yes                             |                                                                                               |
| INF: Infrastructure             | INF: Infrastructure                        | INF: Infrastructure             | INF: Infrastructure                                                                           |
| INF.1                           | Generic Building                           | Yes                             |                                                                                               |
| INF.2                           | Data Centre/Server Room                    | Yes                             |                                                                                               |
| INF.3                           | Cabling                                    | Yes                             |                                                                                               |
| INF.4                           | IT Cabling                                 | Yes                             |                                                                                               |
| INF.6                           | Storage Media Archives                     | Yes                             |                                                                                               |
| INF.7                           | Office Workplace                           | Yes                             |                                                                                               |
| INF.8                           | Working from Home                          | No                              | The employees of a PSAP usually work exclusively in the offices of the PSAP.                  |
| INF.9                           | Mobile Workplace                           | No                              | Deviant, mobile workstations can be used in some PSAPs, e.g. in vehicles of the squad leader. |
| INF.10                          | Meeting, Event, and Training Rooms         | Yes                             |                                                                                               |

## 5.3 General relevant modules

<!-- page: 147 -->

In the next step, the requirements of the relevant modules are checked. If necessary, they are adapted to the framework conditions in PSAPs. Listed are basic and standard requirements. If the requirements   for   increased   protection   requirements   also   have   to   be   fulfilled   for   individual components, these are named separately.

| ISMS.1 Security Management   | ISMS.1 Security Management                                                                                                                                                                                           |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirements                 | ISMS.1.A1 - A15                                                                                                                                                                                                      |
| Implementation guidlines     | The requirements must be met in an appropriate way.                                                                                                                                                                  |
| Hints                        | A4: Depending on the size of the PSAP, the Information Security Officer may also perform other functions in a uniform manner.                                                                                        |
|                              | A10: When creating a safety concept, it is advisable to start with the areas of the PSAP that require the highest level of protection. Subsequently, the security concept can be supplemented with additional areas. |

| ORP.1 Organisation       | ORP.1 Organisation                                                                                                                                                                                                           |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirements             | ORP.1.A1 - A13                                                                                                                                                                                                               |
| Implementation guidlines | The requirements must be met in an appropriate way.                                                                                                                                                                          |
| Hints                    | ORP.1.A12 If an impairment of the operation of the PSAP is unavoidable, maintenance and repair work shall, if possible, be carried out at times of the day in which fewer operations can be expected (for example at night). |

| ORP.2 Personell           | ORP.2 Personell                                     |
|---------------------------|-----------------------------------------------------|
| Requirements              | ORP.2.A1 - A10                                      |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| ORP.3 Awareness and Training   | ORP.3 Awareness and Training                                                                                                                            |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirements                   | ORP.3.A1 - A8                                                                                                                                           |
| Implementation guidelines      | The requirements must be met in an appropriate way.                                                                                                     |
| Hints                          | ORP.3.A4 Training centers for fire brigade and rescue service can be included in the training and advanced training for PSAP calltaker and dispatchers. |

| ORP.4 Identity and Access Management   | ORP.4 Identity and Access Management                |
|----------------------------------------|-----------------------------------------------------|
| Requirements                           | ORP.4.A1 - A19                                      |
| Implementation guidelines              | The requirements must be met in an appropriate way. |

| ORP.5 Compliance Management   |
|-------------------------------|

<!-- page: 148 -->

| Requirements              | ORP.5.A1 - A8                                                                                                                                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Implementation guidelines | The requirements must be met in an appropriate way.                                                                                                                                                         |
| Hints                     | ORP.5.A1 The personnel of the PSAP must have quick access to the documentation of the specifications.                                                                                                       |
|                           | ORP.5.A3 In addition to the decisive points in the data protection laws (GDPR and national laws), this also includes parts of the legislation on security and the penal code for the personnel of the PSAP. |

| CON.1 Crypto Concept      | CON.1 Crypto Concept                                |
|---------------------------|-----------------------------------------------------|
| Requirements              | CON.1.A1 - A6                                       |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| CON.2 Data Protection     | CON.2 Data Protection                               |
|---------------------------|-----------------------------------------------------|
| Requirements              | CON.2.A1                                            |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| CON.3 Backup Concept      | CON.3 Backup Concept                                                                                |
|---------------------------|-----------------------------------------------------------------------------------------------------|
| Requirements              | CON.3.A1 - A12                                                                                      |
| Implementation guidelines | The requirements must be met in an appropriate way.                                                 |
| Hints                     | CON3.A.3 The rules governing the duration of storing emergency calls in the laws must be observed.  |
| Hints                     | CON.3.A12 As a geographically remote storage location a defined replacement PSAP can be determined. |

| CON.4 Selection and Use of Standard Software   | CON.4 Selection and Use of Standard Software                                                                                                              |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirements                                   | CON.4.A1 - A9                                                                                                                                             |
| Implementation guidelines                      | The requirements must be met in an appropriate way.                                                                                                       |
| Hints                                          | The requirements of this module can, for example, be related to office applications, web browsers or PDF viewers. For CAD and ICCS, CON.5 should be used. |

<!-- page: 149 -->

| CON.5 Development and Use of Generic Applications   | CON.5 Development and Use of Generic Applications                |
|-----------------------------------------------------|------------------------------------------------------------------|
| Requirements                                        | CON.5.A1 - A10                                                   |
| Implementation guidelines                           | The requirements must be met in an appropriate way.              |
| Hints                                               | The requirements of this module can be referred to CAD and ICCS. |

| CON.6 Deleting and Destroying   | CON.6 Deleting and Destroying                       |
|---------------------------------|-----------------------------------------------------|
| Requirements                    | CON.6.A1 - A8                                       |
| Implementation guidelines       | The requirements must be met in an appropriate way. |

| OPS.1.1.2 Proper IT Administration   | OPS.1.1.2 Proper IT Administration                                                                                                                                                                                                  |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirements                         | OPS.1.1.2.A1 - A13                                                                                                                                                                                                                  |
| Implementation guidelines            | The requirements must be met in an appropriate way.                                                                                                                                                                                 |
| Hints                                | OPS.1.1.2.A1 Even if the activities of the administration are carried out by dispatchers in personal union, it is important to pay attention to role separation. The dispatcher should not be logged in with administration rights. |

| OPS.1.1.3 Patch and Change Management   | OPS.1.1.3 Patch and Change Management                                                                                                                                                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirements                            | OPS.1.1.3.A1 - A11                                                                                                                                                                                                                       |
| Implementation guidelines               | The requirements must be met in an appropriate way.                                                                                                                                                                                      |
| Hints                                   | OPS.1.1.3.A7 The availability of the support should be guaranteed at and immediately after the installation of patches. An installation before weekends, holidays or appointments, which can be expected many events, should be avoided. |
| Hints                                   | OPS.1.1.3.A9 If possible, changes can first be tested on a training system before they are transferred to the production system.                                                                                                         |

| OPS.1.1.4 Protection Against Malware   | OPS.1.1.4 Protection Against Malware                                                                                                                           |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirements                           | OPS.1.1.4.A1 - A9                                                                                                                                              |
| Implementation guidelines              | The requirements must be met in an appropriate way.                                                                                                            |
| Hints                                  | OPS.1.1.4.A5 In order to avoid functional restrictions, the selection of the virus protection program should be agreed with the manufacturers of CAD and ICCS. |

<!-- page: 150 -->

| OPS.1.1.5 Logging         | OPS.1.1.5 Logging                                   |
|---------------------------|-----------------------------------------------------|
| Requirements              | OPS.1.1.5.A1 - A10                                  |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| OPS.1.1.6 Software Tests and Approvals   | OPS.1.1.6 Software Tests and Approvals                                                  |
|------------------------------------------|-----------------------------------------------------------------------------------------|
| Requirements                             | OPS.1.1.6.A1 - A13                                                                      |
| Implementation guidelines                | The requirements must be met in an appropriate way.                                     |
| Hints                                    | OPS.1.1.6.A11 The use of separate test system instances of CAD and ICCS is recommended. |

| OPS.1.2.2 Archiving       | OPS.1.2.2 Archiving                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| Requirements              | OPS.1.2.2.A1 - A19                                                                                       |
| Implementation guidelines | The requirements must be met in an appropriate way.                                                      |
| Hints                     | OPS.1.2.2.A9 When changing the CAD, care must be taken to retain access to the events of the old system. |

| OPS.1.2.3 Exchange of Information and Storage Media   | OPS.1.2.3 Exchange of Information and Storage Media   |
|-------------------------------------------------------|-------------------------------------------------------|
| Requirements                                          | OPS.1.2.3.A1 - A12                                    |
| Implementation guidelines                             | The requirements must be met in an appropriate way.   |

| OPS.2.1 Outsourcing for Customers   | OPS.2.1 Outsourcing for Customers                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Requirements                        | OPS.2.1.A1 - A15                                                                                                  |
| Implementation guidelines           | The requirements must be met in an appropriate way.                                                               |
| Hints                               | This module concerns a PSAP, for example, when outsourcing the IT administration to an external service provider. |

| OPS.2.4 Remote Maintenance   | OPS.2.4 Remote Maintenance                                                                                                                                   |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirements                 | OPS.2.4.A1 - A20                                                                                                                                             |
| Implementation guidelines    | The requirements must be met in an appropriate way.                                                                                                          |
| Hints                        | The module is relevant if external IT service providers or manufacturers of CAD and ICCS carry out maintenance work remotely in the control center.          |
| Hints                        | OPS.2.4.A14 In order to be able to solve also problems with the Internet access, a dedicated Internet access is recommended for external remote maintenance. |

<!-- page: 151 -->

| DER.1 Detecting Security-Relevant Events   | DER.1 Detecting Security-Relevant Events            |
|--------------------------------------------|-----------------------------------------------------|
| Requirements                               | DER.1.A1 - A13                                      |
| Implementation guidelines                  | The requirements must be met in an appropriate way. |

| DER.2.1 Security Incident Handling   | DER.2.1 Security Incident Handling                               |
|--------------------------------------|------------------------------------------------------------------|
| Requirements                         | DER.2.1.A1 - A18                                                 |
| Implementation guidelines            | The requirements must be met in an appropriate way.              |
| Hints                                | DER.2.1.A6 Commissioning the replacement PSAP can be considered. |

| DER.2.2 Provisions for IT Forensics   | DER.2.2 Provisions for IT Forensics                 |
|---------------------------------------|-----------------------------------------------------|
| Requirements                          | DER.2.2.A1 - A12                                    |
| Implementation guidelines             | The requirements must be met in an appropriate way. |

| DER.2.3 Clean-Up of Extensive Security Incidents   | DER.2.3 Clean-Up of Extensive Security Incidents    |
|----------------------------------------------------|-----------------------------------------------------|
| Requirements                                       | DER.2.3.A1 - A8                                     |
| Implementation guidelines                          | The requirements must be met in an appropriate way. |

| DER.3.1 Audits and Revisions   | DER.3.1 Audits and Revisions                        |
|--------------------------------|-----------------------------------------------------|
| Requirements                   | DER.3.1.A1 - A27                                    |
| Implementation guidelines      | The requirements must be met in an appropriate way. |

| DER.3.2 Audits Based on the BSI 'Guideline for IS Audits'   | DER.3.2 Audits Based on the BSI 'Guideline for IS Audits'   |
|-------------------------------------------------------------|-------------------------------------------------------------|
| Requirements                                                | DER.3.2.A1 - A22                                            |
| Implementation guidelines                                   | The requirements must be met in an appropriate way.         |

## 5.4 Relevant modules for specific objects

The following listed modules only affect the specified target objects. Usually the basic and standard requirements have to be fulfilled. If the requirements for increased protection requirements are also to be fulfilled for individual components, these are named separately.

<!-- page: 152 -->

| APP.1.1 Office Products   | APP.1.1 Office Products                                                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Targets                   | S3                                                                                                                                           |
| Requirements              | APP.1.1.A1 - A14                                                                                                                             |
| Implementation guidelines | The requirements must be met in an appropriate way.                                                                                          |
| Hints                     | A9: A suitable format for the distribution of documents that does not need to be processed by the recipient is, for example, the PDF format. |

| APP.1.2 Web Browsers      | APP.1.2 Web Browsers                                                                 |
|---------------------------|--------------------------------------------------------------------------------------|
| Targets                   | P1.5, A3                                                                             |
| Requirements              | In addition to the basic and standard requirements, APP.1.2.A12 has to be fulfilled. |
| Implementation guidelines | The requirements must be met in an appropriate way.                                  |

| APP.3.3 File servers      | APP.3.3 File servers                                |
|---------------------------|-----------------------------------------------------|
| Targets                   | A8, N3                                              |
| Requirements              | APP.3.3.A1 - A11                                    |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| APP.4.3 Relational Database Systems   | APP.4.3 Relational Database Systems                                                                                    |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Targets                               | A1, A2                                                                                                                 |
| Requirements                          | APP.4.3.A1 - A20                                                                                                       |
| Implementation guidelines             | The requirements must be met in an appropriate way.                                                                    |
| Hints                                 | APP.4.3.A10 The selection of the database system for CAD and ICCS must be made in consultation with the manufacturers. |

| APP.5.1 General Groupware   | APP.5.1 General Groupware                           |
|-----------------------------|-----------------------------------------------------|
| Targets                     | A4, N3                                              |
| Requirements                | APP.5.1.A1 - A19                                    |
| Implementation guidelines   | The requirements must be met in an appropriate way. |

<!-- page: 153 -->

| SYS.1.1 General Server    | SYS.1.1 General Server                              |
|---------------------------|-----------------------------------------------------|
| Targets                   | S1.2, S2.1                                          |
| Requirements              | SYS.1.1.A1 - A25                                    |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| SYS.2.1 General Client    | SYS.2.1 General Client                              |
|---------------------------|-----------------------------------------------------|
| Targets                   | S1.1, S3                                            |
| Requirements              | SYS.2.1.A1 - A27                                    |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| SYS.2.2.3 Windows 10 Clients   | SYS.2.2.3 Windows 10 Clients                                                 |
|--------------------------------|------------------------------------------------------------------------------|
| Targets                        | S1.1                                                                         |
| Requirements                   | SYS.2.2.3.A1 - A20                                                           |
| Implementation guidelines      | The requirements must be met in an appropriate way.                          |
| Hints                          | SYS.2.2.3.A4 These connections can be blocked, for example, in the firewall. |

| SYS.3.4 Mobile Storage Media   | SYS.3.4 Mobile Storage Media                                                         |
|--------------------------------|--------------------------------------------------------------------------------------|
| Targets                        | P5.1                                                                                 |
| Requirements                   | SYS.3.4.A1 - A7                                                                      |
| Implementation guidelines      | The requirements must be met in an appropriate way.                                  |
| Hints                          | SYS.3.4.A4 By using a data lock with anti-virus software, security can be increased. |

| SYS.4.1 Printers, Copiers, and All-in-One Devices   | SYS.4.1 Printers, Copiers, and All-in-One Devices   |
|-----------------------------------------------------|-----------------------------------------------------|
| Targets                                             | P4.1, P4.2, P5.1                                    |
| Requirements                                        | SYS.4.1.A1 - A19                                    |
| Implementation guidelines                           | The requirements must be met in an appropriate way. |

<!-- page: 154 -->

| NET.1.1 Network Architecture and Design   | NET.1.1 Network Architecture and Design                                                  |
|-------------------------------------------|------------------------------------------------------------------------------------------|
| Targets                                   | N1, N2, N3, N4, N6                                                                       |
| Requirements                              | NET.1.1.A1 - A27                                                                         |
| Implementation guidelines                 | The requirements must be met in an appropriate way.                                      |
| Hints                                     | NET.1.1.A23 The separation of CAD, ICCS and office network increases the security level. |

| NET.1.2 Network Management   | NET.1.2 Network Management                          |
|------------------------------|-----------------------------------------------------|
| Targets                      | N1, N2, N3, N4                                      |
| Requirements                 | NET.1.2.A1 - A29                                    |
| Implementation guidelines    | The requirements must be met in an appropriate way. |

| NET.3.1 Router and Switches   | NET.3.1 Router and Switches                         |
|-------------------------------|-----------------------------------------------------|
| Targets                       | N1, N2, N3, N4, N5                                  |
| Requirements                  | NET.3.1.A1 - A23                                    |
| Implementation guidelines     | The requirements must be met in an appropriate way. |

| NET.3.2 Firewall          | NET.3.2 Firewall                                                                                                                                                                                                             |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Targets                   | N1, N2, N3, N4, N5                                                                                                                                                                                                           |
| Requirements              | NET.3.2.A1 - A24                                                                                                                                                                                                             |
| Implementation guidelines | The requirements must be met in an appropriate way.                                                                                                                                                                          |
| Hints                     | NET.3.2.A15 If the network is segmented by two firewalls, it is important to procure the firewalls from different manufacturers. This reduces the chances of an attacker exploiting the same vulnerability in both products. |

| NET.3.3 VPN               | NET.3.3 VPN                                         |
|---------------------------|-----------------------------------------------------|
| Targets                   | N1                                                  |
| Requirements              | NET.3.3.A1 - A13                                    |
| Implementation guidelines | The requirements must be met in an appropriate way. |

<!-- page: 155 -->

| NET.4.1 Telecommunications Systems   | NET.4.1 Telecommunications Systems                  |
|--------------------------------------|-----------------------------------------------------|
| Targets                              | A2                                                  |
| Requirements                         | NET.4.1.A1 - A16                                    |
| Implementation guidelines            | The requirements must be met in an appropriate way. |

| NET.4.2 VoIP              | NET.4.2 VoIP                                                                                                                 |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Targets                   | A2, N2                                                                                                                       |
| Requirements              | NET.4.2.A1 - A13                                                                                                             |
| Implementation guidelines | The requirements must be met in an appropriate way.                                                                          |
| Hints                     | NET.4.2.A1 Compliance with the technical guidelines of the country must be taken into account when planning the use of VoIP. |

| NET.4.3 Fax Machines and Fax Servers   | NET.4.3 Fax Machines and Fax Servers                |
|----------------------------------------|-----------------------------------------------------|
| Targets                                | S4                                                  |
| Requirements                           | NET.4.3.A1 - A10                                    |
| Implementation guidelines              | The requirements must be met in an appropriate way. |

| INF.1 Generic Building    | INF.1 Generic Building                              |
|---------------------------|-----------------------------------------------------|
| Targets                   | R1, R2, R3, R4, R5, R6                              |
| Requirements              | INF.1.A1 - A20                                      |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| INF.2 Data Centre/Server Room   | INF.2 Data Centre/Server Room                       |
|---------------------------------|-----------------------------------------------------|
| Targets                         | R2                                                  |
| Requirements                    | INF.2.A1 - A20                                      |
| Implementation guidelines       | The requirements must be met in an appropriate way. |

| INF.3 Cabling             | INF.3 Cabling                                       |
|---------------------------|-----------------------------------------------------|
| Targets                   | R1, R2, R3, R4, R6                                  |
| Requirements              | INF.3.A1 - A12                                      |
| Implementation guidelines | The requirements must be met in an appropriate way. |

<!-- page: 156 -->

| INF.4 IT Cabling          | INF.4 IT Cabling                                    |
|---------------------------|-----------------------------------------------------|
| Targets                   | N6                                                  |
| Requirements              | INF.4.A1 - A11                                      |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| INF.6 Storage Media Archives   | INF.6 Storage Media Archives                        |
|--------------------------------|-----------------------------------------------------|
| Targets                        | R2, R3, R5                                          |
| Requirements                   | INF.6.A1 - A8                                       |
| Implementation guidelines      | The requirements must be met in an appropriate way. |

| INF.7 Office Workplace    | INF.7 Office Workplace                              |
|---------------------------|-----------------------------------------------------|
| Targets                   | R1, R3                                              |
| Requirements              | INF.7.A1 - A7                                       |
| Implementation guidelines | The requirements must be met in an appropriate way. |

| INF.10 Meeting, Event, and Training Rooms   | INF.10 Meeting, Event, and Training Rooms           |
|---------------------------------------------|-----------------------------------------------------|
| Targets                                     | R6                                                  |
| Requirements                                | INF.10.A1 - A8                                      |
| Implementation guidelines                   | The requirements must be met in an appropriate way. |

There are objects that can not be adequately modeled using the existing modules of IT-Grundschutz. These must be considered separately. The connection to the ISP (N4) has a very high protection requirement in all three protection goals. The PSAP has no influence on the achieved security level of the ISP. There is no module for the alarm network N7 which suitably maps the requirements for the

protection   requirement   of   this   component.   Since   this   network   has   a   very   high   protection requirement in all three protection objectives, the risks must also be considered separately.

## 6 Directions for use

The identified requirements must be integrated into the overall safety concept and implemented in the course of the planned realization. The BSI recommends carrying out the requirements of the blocks in a defined order. This ensures

that the basic risks are covered early. The following modules should be implemented first:

<!-- page: 157 -->

- ISMS security management
- ORP.1 to ORP.4 from ORP organization and personnel
- CON.3 and CON.6 from CON concepts and procedures
- all modules from OPS.1.1 core IT operation

## 7 Supporting information

More detailed information on the individual requirements can be found in the implementation notes of the individual modules of IT-Grundschutz. Another helpful document are the EENA Guidelines and Best Practices for Emergency Services. 4

[4 https://eena.org/cybersecurity-guidelines-and-best-practices-for-emergency-services/   (retrieved on 10/24/2019).](https://eena.org/cybersecurity-guidelines-and-best-practices-for-emergency-services/)

## Nachtrag: nicht zugeordneter Quelltext

<!-- ACSOS: Diese Zeilen stehen woertlich im Quell-PDF, wurden vom Layout- oder Tabellenmodell aber keinem Element zugeordnet. Sie sind hier ergaenzt, damit kein Normtext verloren geht. Die urspruengliche Struktur (Tabellenzelle, Spalte) ist an dieser Stelle nicht rekonstruiert — beim Zitieren die Seite angeben und den Zusammenhang in der Quelle pruefen. -->

<!-- page: 2 -->

> Seite II

> Abkürzungsverzeichnis......................................................................................................................VI

> 9

> 3.2 Festlegung des Geltungsbereichs.............................................................................................16

> 19

> 21

> 3.4 Strukturanalyse........................................................................................................................22

> 23

> 25

> 26

> 28

<!-- page: 3 -->

> Seite III

> 39

> 42

> 44

> 45

> 47

> 48

> 3.6 Zu erfüllende Anforderungen und umzusetzende Maßnahmen...............................................49

> 3.9 Notfallmanagement (BCM).....................................................................................................51

> 4.2 Ermittlung weiterer relevanter Gefährdungen.........................................................................57

> 4.4 Risikobewertung......................................................................................................................58

> 4.5 Risikobehandlung....................................................................................................................64

> 6 Fazit und Ausblick...........................................................................................................................69

> Literaturverzeichnis............................................................................................................................71

<!-- page: 5 -->

> aufgaben............................................................................................................................18

> Tabelle 18: Schutzbedarf der Vertraulichkeit für Prozesse.................................................................38

> Tabelle 20: Schutzbedarf der Verfügbarkeit für Prozesse...................................................................40

> Tabelle 38: Kategorien der Risiken....................................................................................................59

> Tabelle 39: Risikobewertung für das Netz zum Internet Service Provider (N4)................................61

> Tabelle 40: Risikobewertung für das Alarmierungsnetz für Funkmeldeempfänger (N7)..................63

> Tabelle 41: Behandlung der Risiken des Netzes zum ISP..................................................................65

<!-- page: 9 -->

> Erkenntnisse beschreibt Kapitel 5. Die englische Version befindet sich in Anhang B der Arbeit. Da

<!-- page: 24 -->

> - alarmierte Organisationen (z.B. Feuerwehr, Rettungsdienst).

<!-- page: 33 -->

> Einige Hersteller verwenden den Begriff Sprachvermittlungssystem, z.B.

<!-- page: 58 -->

> Seite 52

<!-- page: 60 -->

> Seite 54

<!-- page: 61 -->

> Seite 55

<!-- page: 62 -->

> Seite 56

> N4: z.B. durch gezielte Angriffe auf IP-Adresse. N7: z.B. durch Störsender.

<!-- page: 66 -->

> Seite 60

<!-- page: 68 -->

> Seite 62

<!-- page: 69 -->

> Vermeidung (z.B. durch Ausschluss der Risikoursache).

> Reduktion/Modifikation (z.B. durch Änderung der Rahmenbedingungen).

> Transfer/Teilen (z.B. durch Versicherung oder Outsourcing).

<!-- page: 71 -->

> weiteres Alarmierungssystem parallel betrieben, z.B.

<!-- page: 72 -->

> Begrenzung der tolerierbaren Ausfalldauer auf 72 Stunden in der Schutzbedarfskategorie

<!-- page: 76 -->

> Seite 70

<!-- page: 79 -->

> Seite 73

<!-- page: 80 -->

> Seite 74

<!-- page: 81 -->

> Seite 75

<!-- page: 130 -->

> Page B-3

<!-- page: 131 -->

> Page B-4

<!-- page: 132 -->

> Page B-5

<!-- page: 133 -->

> Page B-6

<!-- page: 134 -->

> Page B-7

<!-- page: 135 -->

> Page B-8

<!-- page: 136 -->

> Page B-9

<!-- page: 137 -->

> Page B-10

<!-- page: 138 -->

> Page B-11

<!-- page: 139 -->

> Page B-12

<!-- page: 140 -->

> Page B-13

<!-- page: 141 -->

> Page B-14

<!-- page: 142 -->

> Page B-15

<!-- page: 143 -->

> Page B-16

<!-- page: 144 -->

> Page B-17

<!-- page: 145 -->

> Page B-18

<!-- page: 146 -->

> Page B-19

<!-- page: 147 -->

> Page B-20

<!-- page: 148 -->

> Page B-21

<!-- page: 149 -->

> Page B-22

<!-- page: 150 -->

> Page B-23

<!-- page: 151 -->

> Page B-24

<!-- page: 152 -->

> Page B-25

<!-- page: 153 -->

> Page B-26

<!-- page: 154 -->

> Page B-27

<!-- page: 155 -->

> Page B-28

<!-- page: 156 -->

> Page B-29

<!-- page: 157 -->

> Page B-30
