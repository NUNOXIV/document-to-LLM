---
source_file: "Hilfsmittel_Remote_Zugang_E_Mail_System_v1.pdf"
source_sha256: d630b1c365c3a0848f3be9d7f2084549b2efb0dba3ff7badb7453b2a7f47c2b3
source_bytes: 771748
pages: 20
tables: 0
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T19:30:31+00:00"
text_coverage_percent: 100.0
restored_hyphens: 6
extraction_status: warn
warnings:
  - "6 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): ExchangeDienste -> Exchange-Dienste, FaktorAuthentisierung -> Faktor-Authentisierung, GSHilfsmittel -> GS-Hilfsmittel, ITBetrieb -> IT-Betrieb, ITGrundschutz -> IT-Grundschutz"
  - "Der Textlayer der Quelle enthaelt 23 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

## IT-Grundschutz-Hilfsmittel: Remote-Zugang E-Mail-System

Datum: 2021-05-14, Version 1.0

## 1 Einleitung

## 1.1 Problemstellung

In vielen Organisationen ist E-Mail ein wichtiger und geschäftskritischer Kommunikationskanal. Da E-Mail Systeme Internet-weit funktionieren, besitzen sie in der Regel Anbindungen zu öffentlichen Netzen. Bestimmte E-Mail Systeme bieten viele Funktionen integriert an, obwohl diese Funktionen in der Sicherheitsbetrachtung differenziert bewertet werden müssen. Wenn solche Dienste durch öffentliche Netze erreichbar sind, entsteht ein höheres Risikopotenzial, als es bei einer reinen E-Mail Verarbeitung über SMTP/IMAP der Fall ist.

Besonders bei hoch integrierten E-Mail-Systemen wird dann der Webmailer oft auch ohne weitere Schutzmaßnahmen oder sachgerechte Risikoanalysen über das Internet zur Verfügung gestellt, um z.B. Mitarbeitern auf Reisen oder im Home-Office Zugriff auf ihr dienstliches E-Mail-Postfach zu ermöglichen.

Für die Nutzer ist der Fernzugriff auf E-Mail-Postfächer komfortabel, kann jedoch fatale Folgen bei Sicherheitsvorfällen entfalten. Diese lassen sich vermeiden oder zumindest stark abmildern, wenn das "System E-Mail" geeignet modelliert und betrachtet wird und die richtigen Entscheidungen hinsichtlich Netzdesign, Schutzmaßnahmen und Architektur getroffen werden.

## 1.2 Abgrenzung der Betrachtung

Dieses Dokument gibt einen Überblick darüber, welche IT-Grundschutz-Bausteine bei E-MailSystemen typischer Weise zu berücksichtigen sind und gibt Hinweise dazu, wo einige typische Probleme liegen. Hierbei liegt der Fokus auf den Konsequenzen, wenn aus externen Netzen (vgl. NET.1.1 Netzarchitektur und -design ) Zugriffe auf das E-Mail-System, speziell auf Postfächer, gewünscht sind.

Besonderheiten der Absicherung gegen interne Clients oder Aspekte der Systemadministration werden nicht detailliert adressiert. Für Fragestellungen zur Sicherheit beim reinen E-Mail-Transport (SMTP, eingehende E-Mails) sei auf die ISi Schriftenreihe des BSI verwiesen. (Dokument /2/ "ISi LANA: Sicherer Betrieb von E-Mail-Servern" ). Diese ISi-Schriftreihe stellt auch Empfehlungen für eine geeignete Netzsegmentierung über die Firewallstruktur zur Absicherung des internen Netzes dar. Dementsprechend wird in diesem IT-Grundschutz-Hilfsmittel (Remote-Zugang Mailsystem) nicht explizit auf Sicherheits-Proxies (hierunter fallen auch Anti-SPAM Gateways bzw. Content-Filter) eingegangen.

<!-- page: 2 -->

Zur Betrachtung der Abgrenzung von VPN- und Proxy-Systemen und grundsätzlichen Modellierungsaspekten bei Fernzugriffskomponenten, die verschiedene Funktionen integrieren, sollte das IT-Grundschutz-Hilfsmittel zu Application Delivery Controllern /08/ herangezogen werden. Es gilt der Grundsatz: Auch Bausteine oder Anforderungen, die in diesem Dokument nicht genannt werden, können relevant sein. Sie sind lediglich für die skizzierte Problemstellung und den Gegenstand dieses Dokuments nicht in besonderem Maße relevant. Im Speziellen betrachtet dieses Hilfsmittel keine Details zur Absicherung der Clients/Endgeräte. Dies wird besonders dann relevant, wenn die Endgeräte nicht nur auf vereinzelte Dienste aus der Ferne zugreifen, sondern ein großes Portfolio von Diensten nutzen und ggf. sogar lokal Daten verarbeiten. Hier zeigt sich schnell, dass eine zentralisierte VPN-Verbindung oft einfacher umzusetzen ist, als die auf vertieften Risikoanalysen basierende Absicherung jedes Dienstes getrennt vorzunehmen. Da die Architekturrichtlinie für die IT des Bundes (/10/ , TNAS-08) das IMAP-Protokoll zum Standard für die Bundesverwaltung bestimmt und dieses Protokoll der gängige Standard der IETF ist, fokussiert dieses Hilfsmittel im Weiteren auf IMAP, um den Zugriff auf E-Mail Postfächer zu betrachten.

## 2 Modellierung von E-Mail Systemen mit dem IT-Grundschutz

## 2.1 Dekomposition

Systeme, die unter dem Sammelbegriff "Mailserver" zusammengefasst werden, bestehen aus unterschiedlichen Subsystemen. Diese folgen der UNIX-Philosophie nach dem Paradigma "Ein Dienst pro Aufgabe". Vereinfacht gesprochen lässt sich dies auf die Funktionsbereiche "E-Mail Empfang und Transport" und "Zugriff auf E-Mail Postfächer" unterteilen, für die dann jeweils ein Client benötigt wird. Für den Bereich der E-Mail Übertragung ist der SMTP-Standard (vgl. RFC 5321) einschlägig, für den Zugriff auf Postfächer kann derzeit das IMAP-Protokoll (vgl. RFC 3501) als vorrangiger Standard genannt werden. Vor diesem Hintergrund wird deutlich, dass hier zwei entkoppelte Funktionen vorliegen und es eigentlich um das Zusammenspiel einer Architektur mit unterschiedlichen Schnittstellen in einem Gesamtverbund geht. In kleinen Installationen werden diese Dienste oft auf einem einzelnen Server zusammengefasst, während größere Installationen hier alleine für die SMTP-Funktion mehrere Serversysteme und Unterfunktionen beinhalten. Für eine weitere häufig im Einsatz befindliche Komponente, den Webmailer, gilt eine ähnliche Unterscheidung. Der Webmailer stellt in Form einer Webanwendung einen Funktionsumfang bereit, welcher sonst in Form einer Client-Applikation realisiert wird. Die Laufzeitumgebung ist damit nicht mehr der einzelne Client, sondern erstreckt sich auf den Webserver und den aufrufenden WebBrowser. Die Kommunikation mit den eigentlichen E-Mail Servern - den SMTP- und IMAP-Systemen - erfolgt damit nicht mehr durch den eigentlichen Client, sondern durch den Webserver des Webmailers. Für eine korrekte Modellierung mit dem IT-Grundschutz und eine damit einhergehende Risikoanalyse ist diese Unterscheidung in verschiedene Komponenten sehr nützlich, da sie Schnittstellen klarer identifiziert und damit detailliertere Möglichkeiten eröffnet, über Veränderungen in der Architektur sehr zielgerichtet bestimmten Gefährdungen zu begegnen.

Seite 2 Version: 1.0

<!-- page: 3 -->

## Basis-Architektur

Das hier im Weiteren betrachtete Konzept beinhaltet grundsätzlich einen Client, der aus der Ferne die E-Mail Dienste der Organisation nutzen möchte. Hierzu sollen der MTA (Mail Transfer Agent) zum internen und externen Versand von E-Mails, sowie der Message Store zum Lesen und Verwalten von E-Mails in den Postfächern der Benutzer genutzt werden. Um die Installation und Konfiguration von E-Mail Clients (Mail User Agent, MUA) auf dem Endgerät einzusparen, wird häufig auf Webmailer gesetzt. Diese bieten einen E-Mail Client in Form einer Web-Anwendung an, die im Hintergrund die Kommunikation mit den anderen Komponenten der E-Mail Infrastruktur übernimmt.

<!-- image -->

Abbildung 1: einfache Basis E-Mail Architektur mit Webmailer. vgl. hierzu auch RFC 5598 - Internet Mail Architecture (Netzwerksymbole von VRT Systems)

Sowohl aus Gründen der Informationssicherheit, als auch aus betrieblichen Aspekten bietet es Vorteile, eine E-Mail Infrastruktur auf unterschiedliche Serversysteme zu verteilen. So lassen sich diese Dienste einfacher skalieren, mit zusätzlichen Komponenten erweitern und im Störungsfall eines Servers sind nur Teile der Funktionalität betroffen. Siehe hierzu auch SYS.1.1.A30 Ein Dienst pro Server (H) .

Ein wesentlicher Aspekt in dieser Betrachtung ist der Schutzbedarf des Message Stores. Im E-Mail System sind die gespeicherten E-Mails oft geschäftskritische Informationen, die einen erhöhten Schutzbedarf bezüglich mehrerer Grundwerte der Informationssicherheit haben. Im obigen Beispiel ist damit die IMAPS-Schnittstelle von besonderer Bedeutung, da über diese die Zugriffe auf die Postfächer der Benutzer erfolgen. Wird ein Webmailer für diesen Zugriff genutzt, muss auch dieser besonders kritisch betrachtet werden, da er das IMAP Protokoll in eine Web-Anwendung übersetzt und typischer Weise zusätzliche Angriffsfläche und Komplexität erzeugt.

Fragestellungen zur Risikoanalyse folgen im Abschnitt zur Risikoanalyse.

<!-- page: 4 -->

## Beispiel 'gehärtete Architektur'

In der skizzierten Basis Architektur offenbaren sich direkt mehrere Schwachpunkte. Diese Schwachpunkte sollten ab einer gewissen Umgebungsgröße oder bei erhöhten Sicherheitsbedürfnissen durch Umsetzung der Anforderungen aus dem IT-GrundschutzKompendium beseitigt werden. Zunächst sollte ein Webmailer nicht im gleichen Netzbereich stehen, wie weitere Server für Dienste mit nennenswertem Schutzbedarf. Zudem sollten für den MTA bzw. eingehenden E-Mail Verkehr Absicherungsmaßnahmen analog der "ISi LANA: Sicherer Betrieb von E-Mail-Servern" (/1/) getroffen werden.

<!-- image -->

Abbildung 2: Gehärtete Architektur für ein E-Mail System mit mehreren Netzsegmenten Für einen öffentlich erreichbaren Webmailer gilt, dass dieser auch für unautorisierte Dritte zugänglich ist. Dadurch erhöht sich die Art und Anzahl der Angriffsvektoren erheblich. Unter anderem ist das Mailing-System dann den Angriffsvektoren eines Webservers ausgesetzt. Außerdem besteht in diesem Fall die Möglichkeit, dass Angreifer Schwachstellensuchmaschinen einsetzen, um so Informationen über den Webmailer zu erhalten. Im Falle einer neu entdeckten Schwachstelle muss deswegen mindestens mit einer kurzfristigen Ausnutzung dieser Schwachstelle gerechnet werden. In diesem Beispiel der gehärteten Architektur sind lediglich der Frontend MTA und der Webmailer exponiert. Damit wird das Risiko einer Kompromittierung zunächst auf den Webmailer selbst begrenzt. Dahinterliegende Systeme und Daten sind aufgrund der Netzsegmentierung über die Firewall-Struktur eher mittelbar betroffen. Eine laterale Ausbreitung vom Webmailer aus wird dadurch nur über wohldefinierte Protokolle und Kommunikationsverbindungen möglich und lässt sich zudem besser überwachen, als in einem nicht segmentierten Netz. Es muss jedoch beachtet werden, dass die von Nutzern auf einem kompromittierten Webmailer verarbeiteten Daten nicht mehr als sicher angesehen werden können.

<!-- page: 5 -->

## 2.2 IT-Grundschutz-Bausteine

Die folgenden Bausteine des IT-Grundschutz-Kompendiums sind ( mindestens ) zu modellieren, sofern ein E-Mail System z.B. Webmailer und Anbindung an einen Verzeichnisdienst beinhaltet. Produktspezifische Bausteine für z.B. Linux oder Microsoft Ökosysteme kommen noch hinzu. Beim Einsatz von Virtualisierung muss auch der entsprechende Baustein ergänzt werden. Hinzu kommen auch weitere Bausteine, wie z.B. Speicherlösungen, Backup etc., je nach Ausgestaltung des Informationsverbundes. Die Liste ist damit keinesfalls abschließend, gibt aber eine Hilfestellung.

ORP.4 Identitäts- und Berechtigungsmanagement

CON.1 Kryptokonzept

CON.2 Datenschutz

OPS.1.1.2 Ordnungsgemäße IT-Administration

OPS.1.1.5 Protokollierung

OPS.1.2.5 Fernwartung

DER.1 Detektion von sicherheitsrelevanten Ereignissen

DER.2.1 Behandlung von Sicherheitsvorfällen

DER.2.2 Vorsorge für die IT-Forensik

DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle.

DER.4 Notfallmanagement

APP.2.1 Allgemeiner Verzeichnisdienst

APP.3.1 Webanwendungen

APP.3.2 Webserver

APP.5.1 Allgemeine Groupware

APP.5.3 Allgemeiner E-Mail-Client und -Server

APP.6 Allgemeine Software

SYS.1.1 Allgemeiner Server

NET.1.1 Netzarchitektur und -design

NET.3.2 Firewall

NET.3.3 VPN

## 2.3 Gefährdungen

G 0.9 Ausfall oder Störung von Kommunikationsnetzen

G 0.22 Manipulation von Informationen G 0.23 Unbefugtes Eindringen in IT-Systeme G 0.26 Fehlfunktion von Geräten oder Systemen G 0.27 Ressourcenmangel G 0.28 Software-Schwachstellen oder -Fehler G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen G 0.32 Missbrauch von Berechtigungen G 0.36 Identitätsdiebstahl G 0.40 Verhinderung von Diensten (Denial of Service)

<!-- page: 6 -->

## 2.4 Typische Angriffe

Für das E-Mail-System als Gesamtes existieren unterschiedliche Angriffe, die besonders typisch sind. Neben Angriffen, die vorrangig auf den SMTP-Kanal oder das Endgerät des Benutzers selbst zielen (typische Malware Downloader), sind hier besonders jene Angriffe im Fokus, die auf die E-MailPostfächer, den Webmailer-Server, den Postfach-Server oder "Zusatzdienste" abzielen.

## DoS / DDoS

Denial-of-Service (DoS)-Angriffe richten sich gegen die Verfügbarkeit von Diensten, Webseiten, einzelnen Systemen oder ganzen Netzen. Wird ein solcher Angriff mittels mehrerer Systeme parallel ausgeführt, spricht man von einem verteilten DoS- oder DDoS-Angriff (DDoS = Distributed Denial of Service). DDoS-Angriffe erfolgen häufig durch eine sehr große Anzahl von Computern oder Servern.

Mittels (D)DoS Angriffen können Angreifer die Verfügbarkeit bzw. Erreichbarkeit von Webmailer, VPN-Zugang oder IMAP-Dienst beeinträchtigen.

## BruteForce

Wählen Nutzer ein schwaches Passwort und ist der Benutzername (z. B. die E-Mail-Adresse) bekannt, kann sich ein Angreifer unter Umständen auch durch wiederholtes Ausprobieren von Passwörtern (Brute-Force-Angriff) Zugang zu einem Benutzerkonto verschaffen. Mittels Brute-Force-Techniken kann der Angreifer auch versuchen, kryptografisch geschützte Daten, z. B. eine verschlüsselte Passwort-Datei, zu entschlüsseln.

Ein Angreifer könnte somit über einen öffentlich erreichbaren Webmailer oder IMAP-Dienst mittels Brute-Force versuchen, einen Zugang zum Dienst zu erlangen.

## Credential Stuffing

Während der Angreifer bei Brute Force Angriffen Passworte zu einem ihm bekannten Benutzerkonto ausprobiert, werden beim Credential Stuffing bekannte Kombinationen aus Benutzernamen und Passworten ausprobiert. Wenn Benutzer ein Passwort wiederverwenden, entsteht hier eine Gefährdung, da das Passwort

womöglich durch andere, schlecht geschützte Systeme entwendet werden konnte.

<!-- page: 7 -->

## Cross Site Scripting (XSS)

Cross-Site-Scripting-Schwachstellen entstehen, wenn Benutzereingaben in einer Webanwendung ungefiltert durch den Server verarbeitet und an andere Clients zurückgegeben werden. Ein Angreifer hat damit unter Umständen die Möglichkeit, Programmcode wie JavaScript im Kontext des Benutzers einer Webseite auszuführen. Dies lässt sich unter anderem ausnutzen, um den Inhalt von Webseiten für einen Benutzer zu ändern oder auf Inhalte wie Cookies zugreifen zu können, um an SessionInformationen zu gelangen. Für einen Webmailer bedeutet dies, dass eine vom Benutzer aufgesuchte, bösartige Webseite z.B. die Zugangsdaten zum Webmailer ausspähen kann, oder die zwischen Client und Webmailer

übertragenen Inhalte manipulieren kann.

Mittels Cross-Site-Request-Forgery (CSRF) können ähnliche Gefährdungen entstehen.

## Ausnutzung von Schwachstellen (inkl. Zero Day Schwachstellen)

Bei der Ausnutzung von Schwachstellen werden Bugs bzw. Implementierungsfehler oder Konfigurationsfehler in einer dem Angreifer zugänglichen Komponenten ausgenutzt. Angreifer können solche Schwachstellen nutzen, um z.B. eigenen Code zur Ausführung zu bringen, Daten zu stehlen oder Zugang zu weiteren Komponenten zu erlangen. Von diesen Komponenten werden dann ggf. weitere Schwachstellen ausgenutzt, um eine laterale Ausbreitung für den Angreifer zu ermöglichen. Um die Ausnutzung von Schwachstellen zu erschweren, sind sichere Konfiguration, minimierte Angriffsflächen, aktuelle Patchstände und mehrschichtige Sicherheit wichtig. Auch bei regelmäßigem und zeitnahen Einspielen von Sicherheitsupdates bleiben oft Zeitfenster, in denen Patches noch nicht zur Verfügung stehen (insbesondere bei Zero Day Schwachstellen) oder aus betrieblichen Zwängen noch nicht eingespielt werden können. Diese Zeitfenster ermöglichen es Angreifern dann, die Schwachstellen auszunutzen. In diesen Szenarien verbleiben oft nur Mitigationsmaßnahmen zur Schadensbegrenzung oder das vorübergehende Deaktivieren von verwundbaren Diensten. Eine Minimierung der Angriffsfläche, durch Verzicht auf ohnehin nicht erforderliche Funktionen/Dienste, Schnittstellen und Erreichbarkeit von Systemen reduziert die Wahrscheinlichkeit, dass Softwareschwachstellen praktisch ausgenutzt werden können, da eine verwundbare Software sowohl im Einsatz sein, als auch von einem Angreifer überhaupt erreicht werden können muss, um zu einer konkreten Gefährdung zu werden. Wird eine mehrschichtige Sicherheit ("Brandschutzmauern" und "Defense in Depth") konsequent umgesetzt, so sind die Schadensauswirkungen bei erfolgreichem Ausnutzen einer Schwachstelle dennoch begrenzt, so dass z.B. nur in begrenztem Maße Daten abfließen können oder nur wenige Systeme überhaupt kompromittiert werden können. Dies bietet erhebliche Vorteile im Rahmen der Vorfallsbewältigung (vgl. DER.2.1 Behandlung von Sicherheitsvorfällen , DER.2.2 Vorsorge für die IT-

Forensik , DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle ) und für die Risikoanalyse.

## 2.5 Besonders relevante Anforderungen

Im Folgenden werden einige der für den hier betrachteten Anwendungsfall besonders bedeutsamen Anforderungen aus dem IT-Grundschutz-Kompendium (Edition 2021) zusammengetragen und kurz erläutert, inwiefern die Relevanz besteht. Es gilt allerdings zu beachten, dass diese Liste nicht alle relevanten Anforderungen enthält und auch nicht die der produktspezifischen Bausteine enthalten sind.

<!-- page: 8 -->

- ORP.1.A16 Richtlinie zur sicheren IT-Nutzung [Benutzer] (S)
- o Für die Planung der Remote-Zugänge ist es wichtig, die Sicherheitsziele der Organisation zu kennen, nach denen das System ausgelegt werden soll. Die Nutzer müssen zudem wissen, welche Sicherheitsmaßnahmen sie auf den von Ihnen genutzten Geräten und Diensten beachten müssen. Dies ist besonders relevant, wenn Nutzer mit eigenen Geräten Dienste und Infrastruktur der Organisation nutzen.
- ORP.4.A8 Regelung des Passwortgebrauchs [Benutzer, IT-Betrieb] (B)
- o Je nach Schutzbedarf und vor Allem bei Zugriffen aus entfernten Netzen sollten Maßnahmen zur Stärkung der Authentisierung, wie z.B. zeitbasierte Einmalpassworte (TOTP) berücksichtigt werden. Es sollte auch in Betracht gezogen werden, für welche Systeme die E-Mail-Zugangsdaten verwendet werden können (im Falle einer Kompromittierung) oder ob hieraus Informationen zum Erraten von Nutzerkonten oder Passworten abgeleitet werden können.
- ORP.4.A9 Identifikation und Authentisierung [IT-Betrieb] (B)
- o Zusätzlich müssen auch Aspekte der Authentisierung von E-Mail Diensten gegenüber etwaigen Verzeichnisdiensten o.Ä. betrachtet werden.
- ORP.4.A22 Regelung zur Passwortqualität [IT-Betrieb] (B)
- o Der Sicherheit der Passworte/Passphrasen kommt eine besondere Bedeutung zu.
- ORP.4.A10 Schutz von Benutzerkennungen mit weitreichenden Berechtigungen [IT-Betrieb] (S)
- o Hier sollte kritisch geprüft werden, ob bestimmte Mail-Nutzer weitreichende Rechte auf sensiblen Daten haben (können).
- ORP.4.A12 Entwicklung eines Authentisierungskonzeptes für IT-Systeme und Anwendungen [IT-Betrieb] (S)
- o Speziell eine Authentisierung auf verschiedenen Ebenen oder mit verteilter Haltung der Authentisierungsinformationen muss unbedingt adäquat konzeptionell vorbereitet werden.
- ORP.4.A13 Geeignete Auswahl von Authentisierungsmechanismen [IT-Betrieb] (S)
- o Die Authentisierungsmechanismen sind geeignet zu konfigurieren. Hierbei muss das Einsatzszenario Berücksichtigung finden. So ist es nachteilig, wenn Angreifer auf einfache Art Nutzerkonten zur Sperrung bringen können (DoS). Bei entsprechend großer Angriffsfläche sollte auch bei normalem Schutzbedarf geprüft werden, ob eine Nutzung starker Authentisierungsmechanismen dem Risiko angemessen ist.
- ORP.4.A14 Kontrolle der Wirksamkeit der Benutzertrennung am IT-System bzw. an der Anwendung [IT-Betrieb] (S)
- o Keinesfalls sollten mehrere Nutzer mit dem gleichen Konto arbeiten oder parallele unbefugte Anmeldungen (z. B. von Angreifern) unentdeckt bleiben.

<!-- page: 9 -->

- ORP.4.A21 Mehr-Faktor-Authentisierung [IT-Betrieb] (H)
- o Eine sichere Mehr-Faktor-Authentisierung ist auch bei normalem Schutzbedarf eine sinnvolle Maßnahme, speziell, wenn für den Dienst besondere Risiken zu erwarten sind.
- CON.1.A3 Verschlüsselung der Kommunikationsverbindungen (S) und APP.5.3.A2 Sicherer Betrieb von E-Mail-Servern (B)
- o E-Mail-Systeme bieten typischerweise eher leichte Möglichkeiten, die erforderlichen Verbindungen geeignet zu verschlüsseln.
- CON.1.A8 Erhebung der Einflussfaktoren für kryptografische Verfahren und Produkte (H)
- o Je nach Anforderungslage müssen hier spezifische Randbedingungen erfüllt werden.
- DER.2.1.A6 Wiederherstellung der Betriebsumgebung nach Sicherheitsvorfällen [IT-Betrieb] (B)
- o Schon der Aspekt des "vom Netz Nehmens" betroffener Komponenten hat unterschiedliche Implikationen. Hierzu müssen diese zunächst eindeutig identifizierbar sein. Zudem muss bereits frühzeitig betrachtet werden, welche Komponenten als unabhängig betrachtet werden können und welche stets gemeinsam betroffen sind. Es kann Vorteile bieten, wenn einzelne Komponenten ("Webmailer", "MTA", ...) eindeutig abgegrenzt werden können, so dass bei einem Sicherheitsvorfall nur Teile des Systems nicht mehr zur Verfügung stehen.
- DER.2.1.A10 Eindämmen der Auswirkung von Sicherheitsvorfällen [Notfallbeauftragter, IT-Betrieb] (S)
- o Hierbei helfen auch die Unterteilung des Mail-Systems in unterschiedliche Subsysteme und die Strategie Defense-in-Depth.
- DER.2.3.A2 Entscheidung für eine Bereinigungsstrategie (B)
- o Der Aufbau des Mail-Systems beeinflusst spätere mögliche Bereinigungsstrategien und deren Qualität. MTA und Webmailer sind in der Regel eher "zustandslose" Systeme, bei denen hauptsächlich Konfiguration und Installation im Rahmen einer Wiederherstellung erforderlich sind. Eine Datenhaltung, die ein Umfangreiches Backup benötigt, ist eher beim Message Store bzw. nur bei dessen Speichersystem erforderlich. Eine solche Trennung von Komponenten zur Datenhaltung von Servern mit Diensten kann eine Bereinigung erheblich vereinfachen.
- DER.2.3.A3 Isolierung der betroffenen Netzabschnitte (B)
- o Die betroffenen Netzabschnitte zielgerichtet zu isolieren ist besonders einfach, wenn das System stark segmentiert werden kann. Monolithische Systeme lassen sich zwar auch isolieren, aber weniger feingranular.
- DER.2.3.A8 Etablierung sicherer, unabhängiger Kommunikationskanäle (S)
- o Eine zentrale Frage ist oft, wie (sichere) Kommunikation beim Wegfall des E-Mail Systems erfolgen kann. Dies ist besonders relevant, wenn das Netz bereits isoliert werden musste, oder Kommunikationsdienste ausgelagert wurden und damit nicht mehr zur Verfügung stehen.

<!-- page: 10 -->

- APP.2.1.A11 Einrichtung des Zugriffs auf Verzeichnisdienste (S)
- o Die Zugriffe einzelner Mail Systeme sollten auf den für das jeweilige System unbedingt nötigen Rahmen beschränkt werden. So benötigen z.B. nicht alle MTAs Zugriffe mit der Möglichkeit zur Authentisierung der Nutzer.
- APP.3.1.A1 Authentisierung bei Webanwendungen (B)
- o Das Bundesamt für Sicherheit in der Informationstechnik (BSI) stellt im Dokument 'Hilfsmittel zur Nutzung des Bausteins Webanwendungen' Hinweise zum Umgang mit diesem Baustein zur Verfügung.
- APP.3.1.A11 Sichere Anbindung von Hintergrundsystemen (S)
- o Diese Anforderung wird über die Hinweise in diesem Papier berücksichtigt.
- APP.3.1.A21 Sichere HTTP-Konfiguration bei Webanwendungen (S)
- o Für über das Internet erreichbare Webmailer ist diese Anforderung besonders kritisch.
- APP.3.2.A1 Sichere Konfiguration eines Webservers (B)
- o Für über das Internet erreichbare Webmailer, ist diese Anforderung besonders kritisch.
- APP.3.2.A3 Absicherung von Datei-Uploads und -Downloads (B)
- o Beispiele aus der Vergangenheit zeigen, dass von Angreifern missbräuchlich hochgeladene Webshells bereits problematisch sind und oft unentdeckt bleiben.
- APP.3.2.A13 Zugriffskontrolle für Webcrawler (S)
- o Diese kann dazu beitragen, sensible Bereiche der Webanwendung vor der Auflistung in Schwachstellensuchmaschinen zu schützen.
- APP.6.A1 Planung des Software-Einsatzes [Fachverantwortliche] (B)
- o Hier sind besonders die verarbeiteten Informationen (internes Mailsystem oder weniger sensibel) und die Schnittstellen (im Mailsystem, zu weiteren Komponenten, nach Außen) zu betrachten.
- APP.6.A4 Regelung für die Installation und Konfiguration von Software [Fachverantwortliche] (B)
- o Sparsame Einstellungen und minimierter Funktionsumfang lassen sich deutlich einfacher umsetzen, wenn modulare und spezialisierte Software genutzt wird, statt monolithischer.
- APP.6.A6 Berücksichtigung empfohlener Sicherheitsanforderungen (S)
- o Sicherheitsfunktionen und die Möglichkeit, Härtungsfunktionen (und Architekturmaßnahmen) überhaupt erst nutzen zu können sind unerlässlich.
- APP.6.A7 Auswahl und Bewertung potenzieller Software [Fachverantwortliche, Beschaffungsstelle] (S)

<!-- page: 11 -->

- o Hier sollte auch das Einsatzszenario berücksichtigt werden, ebenso die Sicherheitseigenschaften der E-Mail Software.
- SYS.1.1.A2 Benutzerauthentisierung an Servern (B)
- o Hier ist ggf. nicht offensichtlich, dass über den Webmailer eine Authentisierung am MTA, bzw. am Message Store durchgeführt wird.
- SYS.1.1.A6 Deaktivierung nicht benötigter Dienste (B)
- o Statt unnötige Dienste explizit zu deaktivieren kann es eine leichter beherrschbare Strategie sein, die Software bereits so auszuwählen und die Architektur so zu wählen, dass ohnehin nur unbedingt erforderliche Dienste je Server installiert und gestartet werden.
- SYS.1.1.A12 Planung des Server-Einsatzes (S)
- o Bereits bei der Planung sind die Kommunikationsschnittstellen, Benutzerzugriffe und die Interaktion in Schutzsysteme besonders relevant.
- SYS.1.1.A19 Einrichtung lokaler Paketfilter (S)
- o Diese Anforderung ist besonders relevant, wenn Systeme zum Einsatz kommen, bei denen Dienste nicht sachgerecht deaktivierbar sind. Zwar sollten diese bereits bei der Produktauswahl möglichst schon verworfen werden, aber ein lokaler Paketfilter kann die entstehenden Sicherheitsprobleme zumindest teilweise verringern.
- SYS.1.1.A30 Ein Dienst pro Server (H)
- o Diese Anforderung entstammt zwar den Vorschlägen für erhöhten Schutzbedarf, ist aber gleichzeitig eine einfach umsetzbare Maßnahme mit hoher Wirkung und ist oft sehr kostengünstig.
- NET.1.1.A4 Netztrennung in Sicherheitszonen (B)
- o Die Komponenten des E-Mail Systems sind in den entsprechenden Sicherheitszonen einzuordnen.
- NET.1.1.A10 DMZ-Segmentierung für Zugriffe aus dem Internet (B)
- o Die aus dem öffentlichen Bereich erreichbaren Dienste sind in einer externen DMZ zu berücksichtigen.
- NET.1.1.A11 Absicherung eingehender Kommunikation vom Internet in das interne Netz (B)
- o Die Implikationen dieser Anforderung werden im IT-Grundschutz Hilfsmittel zu Application Delivery Controllern /8/ näher betrachtet. Es muss geklärt werden, wo Dienste zum internen Netz gehören und welche für Dritte angeboten werden, aber keine internen Dienste der Organisation sind. Für die Postfächer des E-Mail Dienstes wird in Abschnitt 4 die Variante skizziert, für interne und externe Nutzer unterschiedliche Instanzen des Message Stores zu betreiben.
- NET.1.1.A23 Trennung von Netzsegmenten (S)

<!-- page: 12 -->

- o Auch bei gleichem Schutzbedarf schafft das Verteilen der Einzelsysteme in unterschiedliche Netzsegmente einen Sicherheitsgewinn.
- NET.3.2.A20 Absicherung von grundlegenden Internetprotokollen (S)
- o Für den eingehenden SMTP-Verkehr wird dies über Frontend-MTA und Contentfilter realisiert.
- NET.3.3.A6 Durchführung einer VPN-Anforderungsanalyse (S)
- o Hier ist auch zu betrachten, ob der Webmailer über ein VPN geschützt werden muss.

## 2.6 Fragestellungen im Rahmen der Risikoanalyse

Da sich die Risikoanalyse auf die Schutzbedarfsfeststellung, Geschäftsprozesse und damit einhergehende Sicherheitsziele abstützt, muss zunächst beantwortet werden, wo die Prioritäten innerhalb der Organisation liegen und welche Schadensszenarien vorrangig abgewendet werden sollen.

In einer Risikoanalyse MUSS dann betrachtet werden,

- ob die Implementierung der Message-Store Schnittstelle hinreichend vertraut werden kann,
- ob die Komponenten des Mailsystems durch eine angemessene Netzsegmentierung entkoppelt werden,
- ob die Schnittstelle zum Message Store ein gut geprüftes Protokoll verwendet,
- ob für die Schnittstelle zum Message Store angemessene Absicherungsmaßnahmen zur Verfügung stehen,
- ob ein in Betracht kommender Webmailer als sicherer bewertet werden kann, als die Schnittstelle zum Message Store,
- ob für die Absicherung eines Webmailers angemessene Maßnahmen zur Verfügung stehen.

Die folgenden Fragestellungen sind für den Aufbau oder Veränderungen der E-Mail Architektur wichtig:

1. Wie kann möglichst allen Nutzern mittels VPN-Verbindungen ein Zugang zu den E-Mail Systemen ermöglicht werden?
2. Für welche Benutzer ist dies unmöglich - und wenn ja, was sind die Hinderungsgründe?
3. Wie kann auch innerhalb der E-Mail Architektur mehrstufige Sicherheit erreicht werden?
4. Können die Nutzer der E-Mail Systeme in Gruppen unterteilt werden, die unterschiedlichen Schutzbedarf oder unterschiedliches Risikopotential haben?
5. Ermöglicht eine solche Gruppierung eine Aufteilung des Message Stores in einen internen und einen Message Store in einer Fernzugriffszone (Vgl. IT-Grundschutz Hilfsmittel ADC /8/) oder ggf. DMZ?

Wird ein hinreichend sicherer Dienst für den Message Store Dienst verwendet und geeignet konfiguriert, so bietet dieser grundsätzlich weniger Angriffsfläche, als Webmailer.

<!-- page: 13 -->

Das Schadenspotential des Webmailers und des exponierten Message-Store Dienstes ist unterschiedlich. Für den Webmailer gilt, dass dieser grundsätzlich leichter kompromittiert werden kann und die auf dem Webmailer aktiven Nutzer gefährdet, sowie es einem Angreifer erleichtert ein erstes System für die laterale Ausbreitung in Bereichen des eigenen Netzes oder gar im internen Netz zu übernehmen. Jedoch müsste ein Angreifer zunächst den Webmailer kompromittieren, bevor ein Angriff auf den Message Store überhaupt erst möglich ist. Für den Message Store gilt, dass dieser bei Verwendung von sicheren Implementierungen und geeigneten Protokollen grundsätzlich als widerstandsfähiger betrachtet werden kann, als eine Web-Anwendung. Zudem können hier weitere Sicherheitsmechanismen (Vgl. ORP.4, ...) direkt vom Message Store zur Anwendung gebracht werden. Dementgegen steht das Schadensszenario, dass bei einer Kompromittierung des Message Stores potentiell alle auf diesem gespeicherten Postfächer betroffen sind. Hier kann durch die o.A. Aufteilung und Gruppierung ein Sicherheitsgewinn erreicht werden, welcher über die Konfiguration des Transportroutings im MTA vglw. leicht und kostengünstig zu implementieren ist. Mit vertieften Kenntnissen der eingesetzten Produkte können mitunter spezifische Härtungsmaßnahmen implementiert werden. So bietet z.B. der Dovecot IMAP Server die Möglichkeit, die Prozesse, welche die Zugriffe auf die Postfächer durchführen, mit den Rechten des Postfach Eigentümers zu starten, so dass ein erfolgreicher Angriff auf diesen Prozess wiederum zunächst nur ein einzelnes Postfach kompromittiert (vgl. https://doc.dovecot.org/admin\_manual/system\_users\_used\_by\_dovecot/ ).

## 3 Microsoft Exchange und Outlook im Web mit dem IT-Grundschutz

Im folgenden Abschnitt soll exemplarisch eine Architektur diskutiert werden, bei der Microsoft Exchange ab der Version 2016 zum Einsatz kommt. In dieser Architekturbetrachtung wird der Kanal, durch den E-Mails von externen Mailservern verarbeitet werden, bewusst ausgeklammert. Anforderungen die dort zu beachten sind, werden im Dokument "ISi LANA: Sicherer Betrieb von EMail Servern" /2/ näher erläutert. Microsoft Exchange ist eine proprietäre Groupware- und E-Mail-Transport-Server-Lösung, die auf Microsoft Windows-Servern betrieben werden kann. Sie integriert sich in Microsofts Verzeichnisdienstlösung Active Directory, so dass Microsoft Exchange als zentraler Kommunikationsdienst häufig in klassischen Windows-Infrastrukturen vorzufinden ist.

Microsoft Exchange ist seit Version 2016 in zwei Rollen aufgeteilt, die auf separaten Servern betrieben werden müssen:

- Microsoft Exchange Edge-Transportserver (nicht im Fokus dieses Hilfsmittels)
- Microsoft Exchange Postfach-Server

Die aus früheren Versionen bekannte Clientzugriffsrolle ist entfallen, ihre Funktionalitäten wurden in die Postfach-Serverrolle integriert. In der Postfach-Serverrolle werden seit Version 2016 der Transportdienst zum Routen von E-Mails, die Postfachdatenbanken, die Clientzugriffsdienste und die Unified-Messaging-Komponenten zusammengefasst. Microsoft Exchange liefert mit dem Produkt "Outlook im Web" eine integrierte Webmailer-Funktion, welche ebenfalls auf dem Postfach-Server bereitgestellt wird.

Durch den monolithischen Aufbau der Exchange-Infrastruktur wird das o.g. Paradigma 'Ein Dienst pro Server' und damit die IT-Grundschutz-Anforderung SYS.1.1.A30 Ein Server pro Dienst nicht erfüllt, der Postfachserver übernimmt sowohl den E-Mail Empfang, den (internen) Transport, als auch die Bereitstellung des Zugriffs auf E-Mail Postfächer. Der Zugriff auf Postfächer erfolgt in modernen Exchange-Infrastrukturen im Standard HTTP-basiert u.a. durch Nutzung von proprietären Schnittstellen wie "Messaging Application Programming Interface (MAPI)". Insbesondere der monolithische Aufbau und die proprietären Schnittstellen erschweren eine Modellierung mit dem IT-Grundschutz, da die Schnittstellen der beteiligten Komponenten schwierig zu identifizieren sind und möglichen Gefährdungen durch die Architekturvorgaben ggf. nur durch hohen Aufwand begegnet werden kann. Die in Kapitel 2.1.2 erläuterte gehärtete Architektur lässt sich mit Microsoft Exchange auf Grund der Bündelung von Diensten auf dem Postfachserver und den Architekturvorgaben wie bspw. die enge Abhängigkeit zum Active Directory nicht umsetzen. Ist der Webmailer 'Outlook on the Web' öffentlich auch für unautorisierte Dritte frei aus dem Internet erreichbar und wird eine Schwachstelle in diesem ausgenutzt, so kann dies unmittelbare Auswirkungen auf den in der internen Zone des Unternehmens-Netzes befindlichen Postfach-Server mit Domänenmitgliedschaft und ggf. mittelbare Auswirkungen auf die gesamte Domäne haben (vgl. APP.5.2 Gefährdung 2.3 Unzulässiger Browserzugriff auf Microsoft Exchange und APP.5.2.A12 Einsatz von Outlook Anywhere, MAPI over HTTP und Outlook Web App (S) ).

<!-- page: 14 -->

## Praxisbeispiel:

Anfang März 2021 veröffentlichte Microsoft einen Out-Of-Band-Patch für Microsoft Exchange Server, welcher insgesamt 7 kritische Schwachstellen behob von denen 4 bereits aktiv und weitreichend ausgenutzt wurden. Eine Kombination der 4 aktiv ausgenutzten Schwachstellen führte dazu, dass Angreifer Daten abgreifen oder weitere Schadsoftware installieren konnten. Der initiale Angriffsvektor erhielt den Namen ProxyLogon (CVE-202126855) und eine Kritikalität im Common Vulnerability Scoring System (CVSS) von 9.8. ProxyLogon erforderte lediglich eine nicht-vertrauenswürdige Verbindung (z.B. aus dem Internet) auf Port 443 zum Exchange Server, so dass ein hohes Risiko eines erfolgreichen Angriffs für alle aus dem Internet erreichbaren Exchange-Server bestand. Die Absicherung der Exchange-Dienste nach Außen durch eine Authentisierung bereits beim Aufbau der TLS-Verbindung hätte eine mögliche Ausnutzung der Schwachstelle ProxyLogon deutlich begrenzt, da eine nicht vertrauenswürdige Verbindung nicht möglich gewesen wäre. Die betroffenen Schnittstellen wären in diesem Fall nicht ohne vorherige Authentisierung durch Schwachstellen-Suchmaschinen auffindbar und durch Angreifer ohne gültige Zugangsdaten ausnutzbar gewesen. Diente der TLS-Kanal lediglich für die Übertragungssicherheit (Transportverschlüsselung) der Web-Anwendungen (APP.3.2.A11 Verschlüsselung über TLS (B) ), bestand ein hohes Risiko. Wurde der TLS-Kanal mit einer Authentisierung als VPN (NET.1.1.A11 Absicherung eingehender Kommunikation vom Internet in das interne Netz (B) ) genutzt, bestand ein deutlich geringeres Risiko. Für weitere Details zur Abgrenzung der TLS-Verbindungen sei an dieser Stelle auf die 'Empfehlungen für den sicheren Einsatz von Application Delivery Controllern' verwiesen. /8/

In Deutschland waren mehrere 10.000 frei im Internet erreichbare Exchange-Server von den Schwachstellen betroffen. In einigen Fällen kam es auch zu weitergehenden Kompromittierungen der Domäne. Da viele direkt im Internet erreichbare Microsoft Exchange Server sowohl als Mailserver, als auch als Webserver mit entsprechenden Webanwendungen gleichzeitig eingesetzt wurden und diese Systeme häufig sehr hohe Rechte im Verzeichnisdienst besaßen, war das Schadenspotenzial entsprechend hoch. In der unter 3.1. skizzierten Architektur haben Clients einen Zugriffsweg über ein VPN auf die interne Zone des Unternehmens-Netzes, von dort kann auf die Funktionen, die der Postfachserver bereitstellt, zugegriffen werden. Durch die Verwendung eines VPN wird ein höheres Sicherheitsniveau erreicht als bei einem frei im Internet verfügbaren Zugriff auf die E-Mail-Dienste des Unternehmens, die auf Servern in der internen Zone des Unternehmens-Netzes verortet sind.

<!-- page: 15 -->

Der Postfachserver speichert Konfigurations- und Empfängerinformationen, Informationen zu Clientzugriffsprotokollen, dem Transportdienst, Postfachdatenbanken und Unified Messaging im Active Directory. Der Postfachserver besitzt dementsprechend schreibenden Zugriff auf das Active Directory. Ein Betrieb eines Postfachservers in einer Zone, die nur einen schreibgeschützten Verzeichnisserver bereitstellt wird nicht unterstützt. /15/

Microsoft Exchange wird nur in einer durch den Hersteller unterstützen Konfiguration betrieben, wenn der Datenverkehr zwischen dem Postfachserver und dem Active Directory-Domänencontroller nicht eingeschränkt wird. Beim Einsatz von Firewalls oder anderen Netzkomponenten, die den internen Netzverkehr potentiell einschränken oder verändern könnten, müssen die Konfigurationen eine uneingeschränkte Kommunikation ermöglichen. Für den Fall einer Firewall zwischen Postfachserver und Active Directory Domänencontroller bedeutet dies, dass eingehender und ausgehender Netzkverkehr an jedem Port einschließlich zufälliger RPC-Ports zugelassen werden muss. /16/ Durch diese Produktanforderung lassen sich u.a. die IT-Grundschutzanforderungen SYS.1.1.A19 Einrichtung lokaler Paketfilter (S) und NET.1.1.A23 Trennung von Netzsegmenten (S) , sowie je nach Netzstruktur und Schutzbedarf die Anforderung NET.3.2.A2 Festlegen der Firewall-Regeln (B) nicht vollständig umsetzen.

Bei einer Standardinstallation wird Exchange mit den Berechtigungen des "RBAC Shared Permissions Models" in das Active Directory integriert. In diesem Modell haben Exchange-Konten und Exchange-Dienste schreibenden Zugriff auf AD-Objekte und können so selbst u.a. Benutzer anlegen. Im Standard erfolgt keine stringente Trennung der Active Directory Verwaltungsberechtigungen und den Exchange-spezifischen Verwaltungsberechtigungen. Gerade hier besteht jedoch auf Grund der Kritikalität des Verzeichnisdienstes eine hohe Notwendigkeit einer strikten Rechte- und Rollentrennung, um eine möglichst geringe Angriffsfläche zu bieten. Die Exchange-Infrastruktur sollte im "AD Split Permission Model" /14/ betrieben werden, da dieses Modell durch die strikte Trennung von Active Directory- und Exchange-Berechtigungen eine höhere Sicherheit bietet. Die Verwaltung des Exchange wird hierbei von der Active-Directory-Verwaltung getrennt. Exchange-Konten und Gruppen sind im Active Directory nur noch berechtigt ExchangeAttribute zu verwalten. Dies bedeutet u.a., dass ein Active-Directory Administrator zunächst einen Benutzer anlegen muss, bevor ein Exchange-Administrator diesem ein Postfach zuweisen kann. Das "AD Split Permission Model" folgt dem Grundsatz der Aufgabenverteilung und Funktionstrennung, wie u.a. in der IT-Grundschutz Basis-Anforderung ORP.4.A4 Aufgabenverteilung und Funktionstrennung [IT-Betrieb] (B) gefordert. Dies reduziert im Exchange-Kompromittierungsfall die Möglichkeiten eines Angreifers mit potentiell geringem Aufwand die gesamte Domäne zu übernehmen. Gerade in Bestandsumgebungen besitzen Exchange-Server (teilweise ungerechtfertigt) diverse Berechtigungen im Active Directory, die kritisch auf ihre Notwendigkeit hin geprüft werden sollten.

<!-- page: 16 -->

Der Baustein APP.5.2 konzentriert sich auf den Betrieb eines Exchange-Servers. Die Integration der Exchange-Infrastruktur in die Netze der Institution wird jedoch nicht direkt betrachtet. Die Exchange-Architekturvorgaben führen dazu, dass eine Exchange-Infrastruktur nicht hinreichend mit den vorliegenden IT-Grundschutz-Bausteinen aus dem IT-Grundschutz-Kompendium abbildbar ist. Somit ist eine erweiterte Sicherheitsbetrachtung erforderlich, wenn die Integration in die übrige Infrastruktur geplant wird. Insbesondere die Integration von unterschiedlichen, umfangreichen Funktionen auf dem Postfachserver, die eingeschränkten Segmentierungsmöglichkeiten und die potentielle direkte Erreichbarkeit der Dienste aus dem Internet steigern das Gefährdungspotential, welchem der Exchange-Server als stark integriertes IT-System ausgesetzt ist, immens. Die in 2.6 aufgeführten Fragen zur Risikoanalyse müssen vor diesem Hintergrund besonders kritisch geprüft und teilweise auch mit "nein" beantwortet werden. Für die jeweilige Infrastruktur müssen damit geeignete Maßnahmen entwickelt werden, die diese entstehenden Risiken geeignet behandeln. Der sachgerechte Einsatz einer VPN-Lösung ist hierbei ein erster, aber beim Einsatz von "Outlook im Web" grundsätzlich sehr wichtiger Schritt, der u.a. eine sinnvolle Umsetzung der Anforderungen APP.5.2.A12 Einsatz von Outlook Anywhere, MAPI over HTTP und Outlook Web App (S) und NET.1.1.A11 Absicherung eingehender Kommunikation vom Internet in das interne Netz (B) darstellen kann. Alternative Absicherungsmaßnahmen sind grundsätzlich sehr individuell und mitunter mit unverhältnismäßig hohen Aufwänden verbunden, die ein VPN durch den für viele Dienste einheitlich erzielten Sicherheitsgewinn zur wirtschaftlich sinnvollen Lösung werden lassen.

## 3.1 Architektur

<!-- image -->

Abbildung 3: Flache E-Mail Struktur mit Microsoft Exchange

## 4 Postfix/Dovecot und Roundcube mit dem IT-Grundschutz

Im folgenden Abschnitt soll exemplarisch eine Architektur diskutiert werden, die auf bewährten und gängigen Open-Source Komponenten basiert. Dazu wählen wir Postfix für die Funktion des MTA aus, für den Message Store kommt Dovecot zum Einsatz und openLDAP als Verzeichnisdienst. Um einen Webmail-Dienst bereitzustellen, nehmen wir Roundcube auf einem gängigen Webserver an. Für den Dovecot Server existiert ein unabhängiger Audit-Bericht /12/, dessen Inhalt das Vertrauen in die Sicherheit der Implementierung stärkt und bei der Risikoanalyse Berücksichtigung finden kann. In dieser Architektur wird der Kanal, über den E-Mails von externen Mailservern verarbeitet werden, bewusst ausgeklammert. Anforderungen die dort zu beachten sind, werden im Dokument "ISi LANA: Sicherer Betrieb von E-Mail-Servern" /2/ näher erläutert. Im einfachsten Fall könnten alle diese Dienste auf einem einzelnen Server installiert und betrieben werden. Davon wird grundsätzlich abgeraten und zumindest eine Aufteilung der Dienste auf einzelne Server gemäß der Basis-Architektur nach 2.1.1 empfohlen, da im Fehler- oder Kompromittierungsfall alle Dienste gemeinsam ausfallen. Eine Zusammenlegung der verschiedenen Dienste sollte nur dann

erwogen werden, wenn eine Verteilung ob einer sehr kleinen Installation mit sehr begrenztem Schadensausmaß tatsächlich in keinem Verhältnis von Aufwand zu Sicherheitsgewinn steht. In diesem Kapitel soll die gehärtete Basis-Architektur, die in Kapitel 2.1.2 skizziert wurde, weiter betrachtet werden. Die Dienste und benötigten Server werden über drei unterschiedliche Zonen verteilt und durch Paketfilter voneinander getrennt. Dadurch werden insbesondere die besonders relevanten Anforderungen gemäß Kapitel 2.5 DER.2.1.A10 Eindämmen der Auswirkungen von Sicherheitsvorfällen (S) , DER.2.1.A6 Wiederherstellung der Betriebsumgebung nach Sicherheitsvorfall (B) , DER.2.3.A3 Isolierung der betroffenen Netzabschnitte (B), NET.1.1.A23 Trennung von Netzsegmenten (S) sowie SYS.1.1.A30 Ein Dienst pro Server (H) berücksichtigt. Da der Webmailer öffentlich erreichbar sein muss und damit einem erhöhten Risiko exponiert wird, steht dieser in einer eigenen DMZ-Zone. Exemplarisch sind die Anforderungen hochrelevant: APP.3.1.A21 Sichere HTTP-Konfiguration bei Webanwendungen (S) , APP.3.2.A1 Sichere Konfiguration eines Webservers , APP.3.2.A3 Absicherung von Datei-Uploads und Downloads sowie APP.3.2.A13 Zugriffskontrolle für Webcrawler (S) . Über einen Paketfilter können Zugriffe in eine Fernzugriffs-Zone zu einem MTA und Mailstore freigegeben werden, damit ein Client E-Mails versenden und auf sein Postfach zugreifen kann. Weitere Zugriffe in die interne Zone benötigt der Webmailer nicht. In der Fernzugriffs-Zone ist weiterhin ein Verzeichnis-Dienst verortet. Dieser kann als Read-Only-Verzeichnis-Dienst ausgelegt werden, da lediglich lesende Zugriffe vom MTA erforderlich sind, um zu prüfen, ob eine eingehende E-Mail einem konkreten Postfach zugeordnet werden kann oder zurückgewiesen werden muss. Weiterhin braucht der Message Store lesenden Zugriff auf den Verzeichnis-Dienst, damit dieser ClientAnmeldungen authentifizieren kann. Daneben ist eine dritte Zone für interne Dienste vorgesehen. Hier ist schließlich der Verzeichnis-Dienst verortet neben einem internen MTA und Message Store. Hier benötigt der Message Store auch wieder lesenden Zugriff auf den Verzeichnis-Dienst, um ClientAnmeldung zu authentifizieren. Bei eingehenden Mails hat der vorgeschaltete MTA in der Fernzugriffszone bereits das Vorhandensein eines gültigen Postfachs geprüft, weshalb hier der MTA ohne Anbindung an den Verzeichnis-Dienst auskommen kann. Für ein E-Mail Gesamtsystem wird die Mail-Kommunikation zwischen Clients in der externen und internen Zone über Mailrouting zwischen den MTAs gewährleistet. Dazu müssen die beiden MTA ebenfalls SMTPS miteinander reden dürfen. Diese Kommunikationsverbindung wird in Abbildung 4 lediglich gestrichelt angedeutet und wird bewusst nicht näher erläutert. Ggf. sind hier weitere Sicherheitselemente und -Maßnahmen erforderlich, da diese Kommunikation wie der Empfang einer externen E-Mail zu behandeln ist. Anforderungen die dort zu beachten sind, werden im Dokument "ISi LANA: Sicherer Betrieb von EMail-Servern" /2/ näher erläutert. Für die einzelnen Kommunikationsbeziehungen sind jeweils entsprechende Anforderungen zu berücksichtigen (exemplarisch) CON.1.A3 Verschlüsselung der Kommunikationsverbindungen (S) , DER.2.3.A8 Etablierung sicherer, unabhängiger Kommunikationskanäle (S) oder auch APP.3.1.A11 Sichere Anbindung von Hintergrundsysteme (B) . Clients haben in dieser Architektur zwei verschiedene Wege um auf ihre Postfächer zuzugreifen. Die Verwendung der ersten Variante schließt die Zweite jedoch aus, da es zu einer festen Zuordnung der Postfächer zu einem Message Store (entweder Fernzugriffs oder interne Zone) kommt.

<!-- page: 17 -->

1. Ein Client A kann per VPN auf die interne Zone des Unternehmens-Netz zugreifen. Von dort kann er dann auf den internen MTA und Message Store zugreifen. Durch die Verwendung eines VPN wird ein höheres Sicherheitsniveau erreicht.
2. Ein Client B kann per Browser auf den Webmailer zugreifen. Der Webmailer ist in diesem Kontext als klassische Webanwendung zu betrachten und entsprechende IT-Grundschutz Bausteine zu modellieren. Für die Authentisierung am Webmailer stehen verschiedene Möglichkeiten zur Verfügung. Eine einfache Variante wäre die Authentisierung am Webmailer

<!-- page: 18 -->

- mit den Zugangsdaten für den Mail Store. Der Webmailer benötigt keine eigene Benutzerverwaltung und würde die Authentisierung direkt an den Mail Store durchreichen. Eine zweite Variante wäre eine Authentisierung am Webmailer mit einfachen Zugangsdaten oder auch bereits ergänzt um einen zweiten Faktor wie z.B. OTP, die nur für den Webmailer gültig sind. Hier ist eine separate Benutzerverwaltung für den Webmailer erforderlich. Das BSI stellt im Dokument "Hilfsmittel zur Nutzung des Bausteins Webanwendungen" weitere Hinweise zur Verfügung. Für die Authentisierung am Mail Store ist dann ein zweites Paar Authentisierungsmerkmale erforderlich, die unabhängig von den Authentisierungsmerkmalen vom Webmailer sind. Auch für die Anmeldung am Mail Store kann ggf. ein zweiter Faktor wie z.B. OTP verwendet werden. Weitere Details hierzu können in dem IT-GS-Hilfsmittel "Empfehlungen für den sicheren Einsatz von Application Delivery Controllern" /8/ nachgelesen werden. Weiterhin sind die folgenden Anforderungen von besonderer Relevanz (exemplarisch): ORP.4.A8 Regelungen des Passwortgebrauchs (B) , ORP.4.A9 Identifikation und Authentisierung (B) , ORP.4.A10 Schutz von Benutzerkennungen mit weitreichenden Berechtigungen (S) , ORP.4.A21 Mehr-Faktor-Authentisierung (H) , SYS.1.1.A2 Benutzerauthentisierung an Servern (B) .
3. Eine dritte Möglichkeit stellt die Verwendung von Zertifikaten für die Client-Authentisierung noch während des TLS-Verbindungs-Aufbaus dar. Diese Variante kann sowohl für die Authentisierung am Webmailer als auch für die Authentisierung am Mail Store (in 4.1. Architektur nicht dargestellt) verwendet werden. Weitere Details hierzu können auch dem IT-GS-Hilfsmittel "Empfehlungen für den sicheren Einsatz von Application Delivery Controllern" /8/ entnommen werden.

Mit der Aufteilung der Message Stores auf unterschiedliche Zonen wird ein unterschiedlich abgestuftes Sicherheitsniveau erzielt, das auf die Schutzbedürftigkeit der Postfächer im Unternehmen angewendet werden kann. Auf Postfächer, die auf dem Message Store in der Fernzugriffszone verortet sind, kann auf eine relativ einfache Art und Weise über den Webmailer zugegriffen werden. Die etwas stärkere Exponiertheit des Message Stores in der DMZ führt aber auch zwangsläufig zu einem größeren Risiko der Kompromittierung. Im Gegensatz dazu steht der interne Message Store, der lediglich in der internen Zone erreichbar ist und zu der ein Client zunächst ein VPN-Verbindung aufbauen muss, damit er überhaupt mit dem Message Store kommunizieren kann. Das Risiko einer Kompromittierung über die in Kapitel 2.4 skizzierten typischen Angriffe wird stark reduziert. Hervorzuheben sind an dieser Stelle die besonders relevanten Anforderungen DER.2.1.A6 Wiederherstellung der Betriebsumgebung nach Sicherheitsvorfällen (B) , DER.2.1.A10 Eindämmen der Auswirkungen von Sicherheitsvorfällen (S) , DER.2.3.A2 Entscheidung für eine Bereinigungsstrategie (B) und DER.2.3.A3 Isolierung der betroffenen Netzabschnitte (B) . Die genannten Anforderungen sind keinesfalls eine abschließende Liste der zu berücksichtigenden Anforderungen, sondern stellen lediglich eine Gedankenstütze dar, welche verschiedenen

Anforderungen relevant sein können.

<!-- page: 19 -->

## 4.1 Architektur

Abbildung 4: Mehrzonige E-Mail Struktur mit Open Source Lösungen

<!-- image -->

## 5 Häufige Fragen und Antworten

Werden die Anforderungen durch die Nutzung eines Webmail-Dienstes erfüllt?

- Das kann pauschal nicht beantwortet werden. Dies muss für die oben aufgeführten Bausteine detailliert geprüft werden. Hierzu müssen speziell noch der Baustein OPS.2.1 Outsourcing für Kunden und daraus erwachsende weitere Bausteine betrachtet werden. Wird ein E-Mail System in einer Art IaaS (gemietete Server, virtuelle Maschinen oder Container) betrieben, ist dies eher wie eine Erweiterung des Informationsverbundes zu modellieren. Wird ein Webmailer als SaaS Dienst genutzt, muss die Sicherheit der SaaS Infrastruktur analog zu einer selbst betriebenen Infrastruktur bewertet werden. Cloud Anbieter bieten hier teilweise C5-Testate an, die einen anteiligen Überblick über Maßnahmen beim Diensteanbieter geben können. Eine Analyse der Maßnahmen, sowie eine Bewertung, ob diese Maßnahmen ausreichend sind, obliegt jedoch dem Kunden.

Verbietet der IT-Grundschutz damit mobile Zugriffe auf E-Mail?

- Nein. Hier ist einerseits zu unterscheiden, welchen Charakter der E-Mail Dienst in der Organisation hat - also auch, welche Daten dort verarbeitet werden - und wie genau die Zugriffe geregelt und realisiert sind. Grundsätzlich erlaubt eine sichere VPN-Konfiguration, Dienste von mobilen Geräten wie interne Dienste zu nutzen. Ist jedoch kein sicheres VPN (einschließlich dazu gehörender geeigneter Netzsegmentierung zwischen VPN-Zugriff und E-Mail System) vorhanden oder möglich, müssen die entstehenden Risiken besonders sorgfältig betrachtet werden. Ein VPN stellt hier eine enorme Erleichterung dar, weil es oft eine einfachere und risikoärmere Lösung ist, als vorhandene Mailsysteme und Netze in sich robuster und sicherer zu konfigurieren.

## 6 Quellen/Verweise

1. BSI IT-Grundschutz Kompendium (Edition 2021) -

[https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html)

<!-- page: 20 -->

- [Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium\_node.html#](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html)
2. [ISi LANA: Sicherer Betrieb von E-Mail-Servern - https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/isi\_mail\_server\_stu die\_pdf.pdf?\_\_blob=publicationFile&amp;v=1](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/isi_mail_server_studie_pdf.pdf?__blob=publicationFile&v=1)
3. [BSI ISi LANA - https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/ISI-Reihe/isi-reihe\_node.html](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/ISI-Reihe/isi-reihe_node.html)
4. [RFC 5321 SMTP - https://tools.ietf.org/html/rfc5321](https://tools.ietf.org/html/rfc5321)
5. [RFC 3501 IMAP - https://tools.ietf.org/html/rfc3501](https://tools.ietf.org/html/rfc3501)
6. RFC 5598 Internet Mail Architecture - https://tools.ietf.org/html/rfc5598
7. [Postfix Transport Maps man page - http://www.postfix.org/transport.5.html](http://www.postfix.org/transport.5.html)
8. [Empfehlungen für den sicheren Einsatz von Application Delivery Controllern - https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Hilfsmittel/Hilfsmittel\_ Empfehlung\_ApplicationDeliveryController\_v1.pdf?\_\_blob=publicationFile&amp;v=1](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Hilfsmittel/Hilfsmittel_Empfehlung_ApplicationDeliveryController_v1.pdf?__blob=publicationFile&v=1)
9. Open Web Application Security Projekt (OWASP) - https://owasp.org/
10. [Architekturrichtlinie für die IT des Bundes - https://www.cio.bund.de/Web/DE/Architekturenund-Standards/Architekturrichtlinie-IT-Bund/architekturrichtlinie\_it\_bund\_node.html](https://www.cio.bund.de/Web/DE/Architekturen-und-Standards/Architekturrichtlinie-IT-Bund/architekturrichtlinie_it_bund_node.html)
11. Dovecot Systembenutzer - https://doc.dovecot.org/admin\_manual/system\_users\_used\_by\_dovecot/
12. [Dovecot Pentest und Audit-Bericht - https://cure53.de/pentest-report\_dovecot.pdf](https://cure53.de/pentest-report_dovecot.pdf)
13. Dovecot SSL Configuration - https://doc.dovecot.org/configuration\_manual/dovecot\_ssl\_configuration/
14. [Microsoft Dokumentation AD Split Permission Model - https://docs.microsoft.com/dede/exchange/understanding-split-permissions-exchange-2013-help](https://docs.microsoft.com/de-de/exchange/understanding-split-permissions-exchange-2013-help)
15. [Microsoft Dokumentation Zugriff auf Active Directory von Exchange Servern https://docs.microsoft.com/de-de/exchange/plan-and-deploy/active-directory/adaccess?view=exchserver-2016](https://docs.microsoft.com/de-de/exchange/plan-and-deploy/active-directory/ad-access?view=exchserver-2016)
16. [Netzwerkports für Clients und E-Mail-Fluss in Exchange https://docs.microsoft.com/dede/exchange/plan-and-deploy/deployment-ref/network-ports?view=exchserver-2016](https://docs.microsoft.com/de-de/exchange/plan-and-deploy/deployment-ref/network-ports?view=exchserver-2016)
17. Netzwerksymbole für LibreOffice unter Creative Commons Lizenz von VRT Systems - https://www.vrt.com.au/downloads/vrt-network-equipment
