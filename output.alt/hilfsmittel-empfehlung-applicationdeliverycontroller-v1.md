---
source_file: "Hilfsmittel_Empfehlung_ApplicationDeliveryController_v1.pdf"
source_sha256: 1a513145c2bc852bd67a17e2d7185d1e0aabbc8c7ad0f320e2808518daa62607
source_bytes: 345601
pages: 4
tables: 0
converter: "IBM Docling 2.123.0"
ocr: false # mode=auto
table_mode: accurate
docling_status: success
converted_at: "2026-08-31T19:20:09+00:00"
text_coverage_percent: 100.0
restored_hyphens: 6
extraction_status: warn
warnings:
  - "6 Wort(e) hatten einen Bindestrich der Quelle verloren und wurden zurueckgesetzt (belegt durch den Textlayer): HTTPServer -> HTTP-Server, ITGrundschutz -> IT-Grundschutz, SicherheitsProxy -> Sicherheits-Proxy, SoftwareSchwachstellen -> Software-Schwachstellen, VPNEndgeräten -> VPN-Endgeräten"
  - "Der Textlayer der Quelle enthaelt 14 unlesbare Zeichen innerhalb von Woertern (die Schrift bildet den Codepunkt nicht ab). Sie wurden als Bindestrich gelesen; das ist die Form, die das amtliche XML an solchen Stellen fuehrt. Kein Textverlust dieses Werkzeugs, sondern der Quelle."
---

<!-- ACSOS: Diese Datei ist die verbindliche Textquelle fuer Agenten. Das Quell-PDF darf nicht erneut geparst werden. Zitate mit Seitenzahl aus den <!-- page: N --> Markern belegen. -->
<!-- page: 1 -->

<!-- image -->

## Empfehlungen für den sicheren Einsatz von Application Delivery Controllern

(z. B. Citrix ADC)

Hilfsmittel IT-Grundschutz

Application Delivery Controller (ADC) sind Netzkomponenten, die wie ein Loadbalancer mit zusätzlichen (Kern-)Funktionen unterschiedliche Sicherheitsleistungen wie beispielsweise Transportverschlüsselung und betriebliche Funktionen (z. B. Lastverteilung) in einem IT-System vereinen. Durch diese Funktionsvielfalt und oft nicht klar abgegrenzten Aufgaben hinsichtlich ihres korrekten und sicheren Einsatzes stellen ADC eine Herausforderung dar. Daher sind die Komponenten bereits in der Planung (NET.1.1.A13 Netzplanung) besonders zu berücksichtigen, weil sie ansonsten ein Sicherheitsproblem erzeugen können. Besonders bei den über das Internet erreichbaren ADC-Systemen sind elementare Absicherungsmaßnahmen zu treffen. Durch die Aggregation unterschiedlicher Sicherheitsund betrieblicher Funktionen auf einem IT-System (vgl. Abbildung 1) führt eine nicht sachgerechte Adressierung von z. B. Gefährdungen durch Softwareschwachstellen (vgl. IT-Grundschutz Kompendium G0.28 Software-Schwachstellen oder -Fehler) durch wechselseitige Abhängigkeiten der Komponenten schnell zu erheblichen Sicherheitslücken. In der Folge kann dies dazu führen, dass die weiteren IT-Grundschutz-Anforderungen vorgesehenen flankierenden Sicherheitsmaßnahmen aufgrund der engen Integration nicht mehr greifen (u.a. NET.1.1.A10 DMZ-Segmentierung für Zugriffe aus dem Internet (B), NET.1.1.A11 Absicherung eingehender Kommunikation vom Internet in das interne Netz (B) ,

NET.1.1.A4 Netztrennung in Sicherheitszonen (B) ).

<!-- image -->

Abbildung 1: risikobehaftete ADC Integration Aus Sicht des IT-Grundschutzes erfüllt ein ADC zunächst die Funktion eines Loadbalancers bzw. eines Proxies oder einer Web Application Firewall (WAF). Diese Komponenten sind besonders zu schützen, da der (HTTP-) Datenverkehr durch und zwischen Komponenten oft im Klartext transportiert bzw. verarbeitet oder an dahinterliegende Systeme weitergeleitet wird. In solchen Fällen fließen auch ungeschützt kritische Daten wie z. B. Zugangsdaten/Benutzerkennungen in großem Umfang über diese  Komponenten.

<!-- page: 2 -->

Wird ein ADC als Loadbalancer eingesetzt, muss vielfach eine Risikoanalyse durchgeführt werden, weil ADCs als Zielobjekte häufig mit den bestehenden IT-Grundschutz-Bausteinen des IT-Grundschutz-Kompendiums nicht hinreichend modelliert werden können.

Wird ein ADC als WAF eingesetzt, muss eine Risikoanalyse durchgeführt werden, weil diese Zielobjekte mit den bestehenden Bausteinen des IT-Grundschutz-Kompendiums nicht hinreichend abgebildet werden können.

Wird ein ADC stattdessen als Sicherheits-Proxy eingesetzt, so kann er mit dem Baustein NET.3.2 Firewall hinreichend abgebildet werden.

Zudem besteht die Möglichkeit, TLS-Verbindungen auf dem ADC zu terminieren. Hierbei sollte bei einer Modellierung nochmals überprüft werden, ob der TLS-Kanal in der Gesamtarchitektur lediglich der Übertragungssicherheit (Transportverschlüsselung) der Web-Anwendung (APP.3.2.A11 V erschlüsselung über TLS (B)) oder als VPN (NET.1.1.A11 Sichere Anbindung eines externen Netzes (S) ) dient bzw. genutzt wird.

ADCs sollten immer in einer Demilitarisierten Zone (DMZ) verortet sein (siehe NET.1.1.A10 DMZ-Segmentierung für Zugriffe aus dem Internet ) . Außerdem sollten sie ausschließlich über ein separates VPN-Gateway erreichbar sein (siehe NET.1.1.A11 Absicherung eingehender Kommunikation vom Internet in das interne Netz ). Kann dies nicht sichergestellt werden, dürfen ADC nach außen keine internen Dienste anbieten.

Wird der ADC als VPN-Gateway genutzt, muss dafür der Baustein NET.3.3 VPN angewendet werden. In diesem Einsatzszenario ist die TLS-Verbindung für den ADC mit dem Baustein NET.3.3 VPN abzusichern. Daraus ergibt sich auch, dass eine Authentisierung der VPNBenutzer VOR bzw. BEIM Verbindungsaufbau geschehen muss. Keinesfalls dürfen nicht authentisierte Benutzer Zugang zu den dahinterliegenden (HTTP-) Servern erlangen können. Zudem ist der Client für den Fernzugriff abzusichern (SYS.3.1.A9, NET.3.3.A3 Sichere Installation von VPN-Endgeräten (B) ) .

Um ADCs sicher einsetzen zu können, muss bereits in der Planungsphase der Einsatzzweck definiert und die Einsatzszenarien festgelegt werden. Denn die Art der Verwendung bestimmt auch die Funktionen, die von einem ADC bereitgestellt werden. Diese Funktionen sind bei der Modellierung eines ADC nach IT-Grundschutz entscheidend. Werden beispielsweise unterschiedliche Funktionen (z. B. VPN-Gateway, Loadbalancing und Sicherheits-Proxy) auf einem einzelnen Gerät vereint, kann dies dazu führen, dass einige Anforderungen aus dem IT-Grundschutz-Kompendium nicht ohne Weiteres erfüllt werden können (NET.1.1.A18 P-A-PStruktur für die Internet-Anbindung (S) ). Zudem kann es passieren, dass eine Architektur entsteht, die nicht hinreichend mit den vorliegenden IT-Grundschutz-Bausteinen aus dem IT-Grundschutz-Kompendium abbildbar ist und somit eine Risikoanalyse erforderlich macht. Es ist auch zu beachten, dass mit der Integration von unterschiedlichen Funktionen bzw. (IT-Grundschutz-Baustein-) Komponenten auf einem IT-System auch das Gefährdungspotenzial, dem ein solch integriertes IT-System ausgesetzt ist, steigt. Eine solche Konfiguration kann besonders risikobehaftet sein, wie das folgende Praxisbeispiel zeigt.

<!-- page: 3 -->

## Praxisbeispiel

Um den Jahreswechsel 2019/2020 erlangte eine Schwachstelle in den ADC-Produkten des Herstellers Citrix große Aufmerksamkeit in der Presse. Hierbei war es durch einen DirectoryTraversal-Angriff auf den HTTP-Server im Citrix ADC möglich, auf kritische Konfigurationsdateien zuzugreifen und mit diesen Informationen die Kontrolle über den ADC zu erlangen. Es handelte sich um eine Softwareschwachstelle ( siehe G 0.28 Software-Schwachstellen oder -Fehler ) in einer besonders kritischen Komponente.

Da viele im Internet erreichbare Citrix ADC sowohl als VPN-Gateway als auch als Sicherheits-Proxy, Loadbalancer und ALG (Application Level Gateway) gleichzeitig eingesetzt wurden (vgl. Abbildung 1), war das Schadenspotenzial entsprechend hoch. Die Schwachstelle konnte nur umfangreich ausgenutzt werden, weil die 'VPN-Verbindung', das heißt, die TLS-Verbindung nicht authentisiert aufgebaut worden war. Vielmehr konnten beliebige IT-Systeme im Internet eine TLS-Verbindung zum ADC aufbauen. Eine Benutzer-Authentisierung durch den HTTP-Server erfolgte erst im Anschluss innerhalb des TLS-Kanals. Eine Authentisierung bereits beim Aufbau der TLS-Verbindung hätte eine mögliche Ausnutzung der Schwachstelle deutlich begrenzt, da diese ausschließlich zuvor authentisierten Angreifern verfügbar gewesen wäre. Eine Erreichbarkeit des verwundbaren Webservers über bekannte SchwachstellenSuchmaschinen und eine damit einhergehende Ausnutzung durch Angreifer, die nicht ohnehin bereits im Besitz gültiger Zugangsdaten sind, wäre damit nicht möglich gewesen.

## Hilfreiche Fragen:

- 1) Falls Web-Anwendungen oder Terminalserver von außen erreichbar gemacht werden: Wer sind die hierfür vorgesehenen Anwender?
- 2) Sind INTERNE Anwendungen ausschließlich über dedizierte VPN-Gateways erreichbar?
- 3) Haben Dritte, die nicht zur eigenen Organisation gehören oder externe/nicht ausdrücklich legitimierte Endgeräte nutzen, Zugriff auf interne Anwendungen?
- 4) Wurden SYS.3.1.A9 (Sicherer Fernzugriff) und NET.3.3.A3 (Sichere Installation von VPN-Endgeräten) für alle Fernzugriffe auf interne Anwendungen umgesetzt?
- 5) Erfüllt der ADC übergeordnete Vorgaben der Institution (z. B. Sicherheitsrichtlinie, Datenschutzkriterien etc.)?
- 6) Wurden Einsatzzweck und Einsatzszenarien vor der Beschaffung des ADC definiert und festgelegt?
- 7) Wurden die IT-Systeme nach ihrem Einsatzzweck und Aufgaben betrachtet und entsprechend modelliert?
- 8) Nutzt Ihre Behörde die Netze des Bundes? In diesem Fall gelten unabhängig von dieser Orientierungshilfe der Mindeststandard Bund 'Nutzerpflichten NdB' sowie die VSA.

<!-- page: 4 -->

<!-- image -->

Abbildung 2: Beispiel einer Grundschutz-konformen ADC-Integration für den erhöhten Schutzbedarf

Für Fragen stehen Ihnen die Sicherheitsberatung des BSI und das IT-Grundschutz-Team gerne zur Verfügung: Kontakt:

[sicherheitsberatung@bsi.bund.de](mailto:sicherheitsberatung@bsi.bund.de)

[grundschutz@bsi.bund.de](mailto:it-grundschutz@bsi.bund.de)
