---
source_file: "Hilfsmittel_Empfehlungen_App-Stores_v1.pdf"
source_sha256: 4f55cb2f3b0330aab58f26f16ab289ddcfd1fcb0a1b6d48c2c6f51af47496671
source_bytes: 186846
pages: 4
tables: 0
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T19:20:14+00:00"
text_coverage_percent: 100.0
restored_hyphens: 2
extraction_status: warn
warnings:
  - "2 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): AppBestandteile -> App-Bestandteile, AppEntwickler -> App-Entwickler"
  - "Der Textlayer der Quelle enthaelt 6 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

## IT-Grundschutz-Hilfsmittel: Empfehlungen zu App-Stores

Betrachtungen zur Vertrauensstellung von App Stores am Beispiel des Google Play Store Datum: 2021-10-19, Version: 1.0

## 1. Sachlage

Bei der Installation von Apps auf Geräten mit dem mobilen Betriebssystem Android werden die notwendigen Installationsdateien auf die Geräte geladen und anschließend vom zuständigen Dienst, dem sogenannten PacketManager, geprüft und installiert. Android-basierte Geräte können Apps jedoch nur dann installieren oder updaten, wenn die entsprechenden Installationspakete mit einem digitalen Zertifikat signiert sind. Siehe dazu Exkurs: Digitale Zertifikate und PKI . Der PacketManager vertraut bei der Installation einer App implizit dem Herausgeberzertifikat und prüft nur, ob das Installationspaket nicht verändert wurde. Bei einem Update prüft der PacketManager zusätzlich, ob das Update-Paket vom gleichen Herausgeberzertifikat signiert worden ist. Das heißt, es wird nicht geprüft, ob dem Zertifikat bzw. Aussteller des Zertifikats vertraut werden kann - dieses Vertrauen wird implizit vorausgesetzt. Weiterhin sind diese Prüfungen auf den PacketManager bei der Installation beschränkt; weder das Betriebssystem noch Nutzer nutzen zu einem späteren Zeitpunkt die Signatur eines Installationspaketes. Google stellt mit dem sogenannten Android App Bundle (AAB) ein spezielles Upload-Format für Entwickler bereit die Apps über den Play Store vertreiben wollen. AABs sind Pakete, die sämtlichen Programmcode sowie alle verfügbaren Ressourcen enthalten. Damit unterscheiden sie sich zunächst nicht grundsätzlich vom App-Installationspaket APK, sind intern jedoch modularer aufgebaut. Der Play Store will Nutzern aus diesen Bundles künftig nur die für ihre Geräte notwendigen App-Bestandteile (als APK) ausliefern. Android App Bundles wurden von Google 2018 als neues 'Publishing Format' vorgestellt und sind ab August 2021 für neue Apps verpflichtend (vgl. Google-Blog). Da im Android-Betriebssystem jedoch nur Apps installiert werden können, die digital signiert sind, muss der Play Store ein neu zusammengestelltes Installationspaket auch digital signieren (Google Play App Signing). Dazu verlangt Google von Entwicklern die Zurverfügungstellung ihrer privaten Signaturschlüssel. Dies bedeutet für die Entwickler den Verlust der Vertraulichkeit ihrer Signaturschlüssel. Aus Anwendersicht ist sowohl die Signatur selbst als auch die Verwendung der Signatur während der Installation vollständig unsichtbar. Anwender, die Apps im Play Store auswählen und installieren, vertrauen dem Play Store und damit auch Google. Für Anwender ist nicht der Entwickler, sondern der Play Store der Lieferant und damit die Quelle der Software. Mit diesem grundsätzlichen Vertrauen in den Play Store bekommt die Signatur des Installationspaketes jedoch eine andere Gewichtung. Sie sichert nun sozusagen nur den Transportweg vom Play Store zum Gerät ab und ist (in einer Übergangsphase) dazu da, die Lieferkette bei Updates nicht zu brechen. Daher ist die Herausgabe des privaten Entwickler-Signaturschlüssels an Google - trotz der grundsätzlichen sicherheitstechnischen Bedenken gegen die Herausgabe eines Geheimnisses - von geringer Bedeutung, solange dieser Signaturschlüssel nicht anderweitig verwendet wird (siehe dazu auch die Handlungs-Empfehlungen unten). Die Vertrauenswürdigkeit der Software wird an dieser Stelle nicht betrachtet. Eine Bewertung, ob die Software (nur) die beschriebene Funktion bereitstellt, die zugewiesenen Berechtigungen nicht missbraucht, unerwünscht Informationen abfließen lässt oder auf andere Weise das IT-System des Anwenders kompromittiert, muss unabhängig erfolgen. Das IT-Grundschutz-Kompendium behandelt diese Aspekte unter anderem in den Anforderungen APP.1.4.A5 Minimierung und Kontrolle von AppBerechtigungen sowie APP.1.4.A8 Verhinderung von Datenabfluss .

<!-- page: 2 -->

## Exkurs: Digitale Zertifikate und PKI

Das Prinzip einer PKI basiert auf asymmetrischer Kryptographie. Bei asymmetrischer Kryptographie besitzt jeder Teilnehmer ein Schlüsselpaar aus einem öffentlichen und einem privaten Schlüssel. Mit dem öffentlichen Schlüssel können Daten verschlüsselt und Signaturen geprüft werden und nur mit dem privaten Schlüssel können Daten entschlüsselt und Signaturen erstellt werden.

Wenn zwei Kommunikationspartner einander sicher Nachrichten übermitteln möchten, tauschen sie ihre öffentlichen Schlüssel aus und erhalten damit die Möglichkeit, Nachrichten so zu verschlüsseln, dass sie nur der jeweils andere entschlüsseln kann. Zusätzlich können sie auch die digitale Signatur des Anderen überprüfen.

Um Kommunikation zu vereinfachen und auch dann zu ermöglichen, wenn die Kommunikationspartner sich vorher nicht persönlich kennen, werden so genannte Public Key Infrastructures (PKI) genutzt.

Bei einer Public Key Infrastructure wird ein Schlüsselpaar bei einer für alle Teilnehmer vertrauenswürdigen Stelle, einer so genannten Certificate Authority (Zertifikats-Autorität, CA) erstellt. Dieses Schlüsselpaar bzw. ein damit erzeugtes (selbstsigniertes) Wurzelzertifikat kann als Vertrauensanker benutzt werden, welches auf einem sicheren Weg auf den Endgeräten verfügbar gemacht werden muss. Häufig erfolgt die Verteilung der Wurzelzertifikate über die Anbieter der Betriebssysteme. Darüber hinaus veröffentlichen die Zertifikatsaussteller oft auf ihren Webseiten ihre Wurzelzertifikate oder deren Hashwerte. Die CA beglaubigt öffentliche Schlüssel von Teilnehmer durch das Ausstellen von digitalen Zertifikaten. Ein digitales Zertifikat beinhaltet den öffentlichen Schlüssel eines Schlüsselpaares und zudem weitere Angaben, wie z.B. wer das Zertifikat ausgestellt hat, für wen es ausgestellt wurde (= der Besitzer des passenden privaten Schlüssels) und den Gültigkeitszeitraum. Die ausgestellten Zertifikate werden zudem für Certificate Transparency Server verfügbar gemacht. Bei der Prüfung von Signaturen kann daher immer auch die Besitzer-ID des Zertifikats dargestellt werden. So kann beispielsweise bei einer signierten ausführbaren Datei überprüft werden, ob diese von einem bestimmten Entwickler/Unternehmen erstellt worden ist. Durch die Vertrauenskette wird dann auch transitiv dem Entwicklerzertifikat vertraut.

Daneben werden auch selbstsignierte Zertifikate direkt verwendet. Um den Aussteller/Besitzer des Zertifikats zu prüfen, müssen diese wie Wurzelzertifikate behandelt werden. Das heißt, sie müssen auf einem sicheren Weg auf den Endgeräten verfügbar gemacht werden oder die entsprechenden Informationen veröffentlicht werden.

-------------------------------------------------------------------------------------------------------------

Im IT-Grundschutz-Kompendium (vgl. Download-Seite) wird in Baustein APP.6 Allgemeine Software die sichere Beschaffung von Software gefordert (APP.6.A3). ' Die ausgewählte Software MUSS aus vertrauenswürdigen Quellen beschafft werden. Die vertrauenswürdige Quelle SOLLTE eine Möglichkeit bereitstellen, die Software auf Integrität zu überprüfen. ' Bei normalem Schutzbedarf bedeutet dies, dass ein Anwender, der Apps aus einer vertrauenswürdigen Quelle bezieht, nicht jede zu installierende App einzeln prüfen muss.

<!-- page: 3 -->

Da aus Anwendersicht nicht der Entwickler, sondern der Play Store die Software-Quelle ist, verlagert sich die Betrachtung auch aus der Sichtweise des IT-Grundschutzes auf den Google Play Store. Nicht der Entwickler, sondern der Play Store muss gegenüber dem Anwender die Authentizität und Integrität der App sicherstellen. Um dies zu erfüllen, braucht ein App Store

- eine Prüfung der Identität der Entwickler,
- klare, öffentliche Anforderungen an Software-Qualität und Prozesse
- und muss deren Einhaltung prüfen.

Um sich beim Google Play Store als Entwickler anzumelden, wird ein gewöhnliches Google-Konto benötigt, welches mit einem beliebigen zweiten Faktor geschützt ist. Die für Entwickler geltenden Richtlinien werden von Google veröffentlicht und sind Bestandteil der Nutzungsbedingungen des Play Stores für Entwickler (vgl. Play Policy). Art und Umfang der Prüfung auf Einhaltung der Nutzungsbedingungen veröffentlicht Google nicht. Demnach kann Google nicht vollständig sicherstellen, dass alle Entwickler sich an die Nutzungsbestimmungen halten, was sich auch daran zeigt, das immer wieder öffentlich wird, dass Entwickler dagegen verstoßen haben. Bei dem Bekanntwerden von Verstößen gegen die Nutzungsbestimmungen ist Google in der Vergangenheit regelmäßig dagegen vorgegangen und hat Entwickler/Hersteller selbst von populären Apps gesperrt. Insbesondere hat Google es dadurch erreicht, den Anteil von Schadprogrammen im Play Store gering zu halten, die Softwarequalität zu verbessern und damit das diesbezügliche Vertrauen in die Software zu erhöhen. Mit den genannten Maßnahmen (kontrollierte Entwicklerbeziehung, Google Play App Signing) kann der Play Store für den normalen Schutzbedarf als vertrauenswürdiger SoftwareLieferant sowie zusätzlich über die vertrauensvolle Beziehung zu den Entwicklern als vertrauenswürdige Quelle für die App-Installation angesehen werden. Auf Anwenderseite muss beachtet werden, dass das Gerät selbst und das darauf installierte Betriebssystem Android aus einer sicheren Quelle stammen. Damit ist sichergestellt, dass die integrierten Google Play Dienste auch die Originalen sind. Ergänzend muss der Anwender bei der App-Auswahl anhand der im Play Store vorhandenen Information beachten/prüfen, dass diese seinen Anforderungen an Funktionalität und Datenschutz genügt.

Bei erhöhtem Schutzbedarf muss zusätzlich das Risiko betrachtet werden, dass Apps auf dem Weg vom Entwickler zum Endgerät verändert werden. Nutzer beziehungsweise Unternehmen müssen die Integrität und Authentizität prüfen sowie die Verfügbarkeit sicherstellen. Dazu ist eine Risikoanalyse notwendig.

Für die Integritätsprüfung stellt Google mit dem AAB-Format ein neues Prüfverfahren bereit. Bei dem sogenannten Code Transparency -Mechanismus (vgl. Dev-Guide) wird dem Installationspaket eine zusätzliche Datei mit Hashwerten über bestimmte Programmbestandteile (sogenannte DEX-Files) sowie Bibliotheken beigelegt. Dies bietet die Möglichkeit, die Integrität dieser App-Bestandteile zu prüfen, wobei diese Art der Absicherung wieder der klassischen Verwendung von Signaturen entspricht. Voraussetzung ist hierbei die Veröffentlichung des öffentlichen Schlüssels.

## 2. Handlungsempfehlungen

## 2.1. Grundsätzliche Empfehlungen

Private Signaturschlüssel, die möglicherweise auch zu weiteren Zwecken verwendet werden, sollten nicht an Dritte weitergegeben, sondern geheim gehalten und eigenverantwortlich verwaltet werden.

Sicherungskopien von Schlüsselmaterial sollte erzeugt und sicher gelagert werden.

Schlüsselmaterial sollte nur gewechselt werden, wenn dafür eine Notwendigkeit besteht. Beispiele sind Kompromittierung des Schlüsselmaterials oder eine entsprechende Unternehmensstrategie.

Die öffentlichen Teile von Schlüsselmaterial sollten für die Überprüfung der Signatur auf einem vertrauenswürdigen Weg bereitgestellt werden.

<!-- page: 4 -->

## 2.2. Empfehlungen für den normalen Schutzbedarf

## 2.2.1 Nutzer

Durch die Vertrauensstellung des Play Stores und damit dem transitiven Vertrauen in den Entwickler kann trotz fehlender Überprüfungsmöglichkeit beim Installationsprozess eine Einzelprüfung der AppIntegrität bei der Installation unterbleiben. Die für die Nutzung des Play Stores benötigten PlayDienste sind in der Regel in den ausgelieferten Geräten enthalten. Bisher ist noch kein Fall von veränderten Play-Diensten öffentlich geworden, weshalb bei neuen Geräten für normalen Schutzbedarf davon ausgegangen werden kann, dass die Geräte auf dem Lieferweg nicht verändert worden sind. Dennoch ist immer auch ein Grundvertrauen in den Produkthersteller, App-Entwickler und Betreiber des App-Shops erforderlich, dass die Geräte keine unerwünschten Funktionen enthalten.

Bei nicht-vertrauenswürdigen Quellen müssen weitere Maßnahmen ergriffen werden, um die Integrität der App und die Authentizität der Quelle zu überprüfen.

## 2.2.2 Entwickler

Neben der Beachtung der grundsätzlichen Empfehlungen zum Umgang mit Schlüsselmaterial sollten Entwickler für das Google Play App Signing exklusiv einen Signaturschlüssel erzeugen. Dieses Schlüsselmaterial wird dann an Google übergeben und sollte anderweitig nicht mehr verwendet werden. Aus dem zugehörigen öffentlichen Zertifikat sollte zudem erkennbar sein, dass das Zertifikat nicht vom Entwickler, sondern von Google verwendet wird (z. B. durch Angabe von Google als Organisation).

## 2.3. Empfehlungen für den erhöhten Schutzbedarf

## 2.3.1 Unternehmen

Unternehmen müssen die Integrität, Authentizität sowie Verfügbarkeit von Apps selbst sicherstellen. Dazu müssen sie durch eine Risikoanalyse abwägen, ob Apps, die sensible/kritische Geschäftsprozesse verarbeiten, über einen fremdkontrollierten App Store verteilt werden können und wer als App-Entwickler/-Herausgeber über das erforderliche Vertrauen im Sinne des Unternehmens verfügt. Ist das Risiko einer Bereitstellung durch den Play Store nicht tragbar, muss ein sicherer alternativer Weg zur Bereitstellung von Apps genutzt werden.

## 2.3.2 Entwickler

Um die Anforderung APP.6.A3 des IT-Grundschutz-Bausteins durch den Anwender vollständig erfüllbar zu machen, sollten Entwickler die Prüfbarkeit der Integrität ihrer Apps ermöglichen.

## 3. Anwendung auf andere App-Stores

Diese Empfehlungen sind nicht ausschließlich an den Google Play Store gebunden, sondern gelten auch für andere App-Stores sowie grundsätzlich auch für andere Ökosysteme mit deren integrierten App-Stores.
