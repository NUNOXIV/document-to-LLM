---
type: struktur
framework: bsi-grundschutz
quellen: ["GS_Struktur_Edition-2023.mm", "GS_Struktur_Edition-2023.pdf"]
abgeleitet: true
tags: ["grc/struktur", "grc/framework/bsi-grundschutz"]
generated-by: document-to-LLM
---

# IT-Grundschutz-Kompendium 2023 — Baustein-Struktur

> [!info] Abgeleitete Darstellung
> Diese Gliederung ist **zusammengesetzt**, nicht woertlich extrahiert: die
> Hierarchie stammt aus `GS_Struktur_Edition-2023.mm`, die Bedeutung der
> Rangstufen aus der Legende von `GS_Struktur_Edition-2023.pdf`. Getrennt
> ist keine der beiden Quellen brauchbar — die Mindmap traegt Symbole ohne
> Erklaerung, das Plakat die Erklaerung ohne maschinenlesbare Struktur.
> Fuer woertliche Zitate die beiden Extrakte heranziehen.

**110 Bausteine** mit Rangstufe. Farben: neuer Baustein, Baustein verschoben/umbenannt · Stand: Februar 2023

## Umsetzungsreihenfolge

- **R1** — Diese Bausteine sollten vorrangig umgesetzt werden, da sie die Grundlage für einen effektiven Sicherheitsprozess bilden.
- **R2** — Diese Bausteine sollten als nächstes umgesetzt werden, da sie in wesentlichen Teilen des Informationsverbundes für nachhaltige Sicherheit erforderlich sind.
- **R3** — Diese Bausteine werden zur Erreichung des angestrebten Sicherheitsniveaus ebenfalls benötigt und müssen umgesetzt werden, es wird aber empfohlen, diese erst nach den anderen Bausteinen zu betrachten.

> [!warning] Ohne Rangstufe in der Quelle
> Diese Bausteine tragen in der Mindmap kein Symbol, obwohl sie
> Bausteine sind. Die Angabe fehlt in der Quelle, sie wurde hier
> nicht ergaenzt: `SYS.1.9 Terminalserver`.

## Gliederung

- IT-Grundschutz-Kompendium 2023
- System-Bausteine
  - APP (Anwendungen)
    - APP.1 Client-Anwendungen
      - APP.1.1 Office-Produkte · **R2**
      - APP.1.2 Web-Browser · **R2**
      - APP.1.4 Mobile Anwendungen (Apps) · **R2**
    - APP.2 Verzeichnisdienst
      - APP.2.1 Allgemeiner Verzeichnisdienst · **R2**
      - APP.2.2 Active Directory · **R2**
      - APP.2.3 OpenLDAP · **R2**
    - APP.3 Netzbasierte Dienste
      - APP.3.1 Webanwendungen und Webservices · **R2**
      - APP.3.2 Webserver · **R2**
      - APP.3.3 Fileserver · **R2**
      - APP.3.4 Samba · **R2**
      - APP.3.6 DNS-Server · **R2**
    - APP.4 Business-Anwendungen
      - APP.4.2 SAP-ERP-System · **R2**
      - APP.4.3 Relationale Datenbanksysteme · **R2**
      - APP.4.4 Kubernetes · **R2**
      - APP.4.6 SAP ABAP-Programmierung · **R2**
    - APP.5 E-Mail/Groupware/Kommunikation
      - APP.5.2 Microsoft Exchange und Outlook · **R2**
      - APP.5.3 Allgemeiner E-Mail-Client und -Server · **R2**
      - APP.5.4 Unified Communications und Collaboration (UCC) · **R2**
    - APP.6 Allgemeine Software · **R2**
    - APP.7 Entwicklung von individualsoftware · **R3**
  - SYS (IT-Systeme)
    - SYS.1 Server
      - SYS.1.1 Allgemeiner Server · **R2**
      - SYS.1.2 Windows-Server
        - SYS.1.2.2 Windows Server 2012 · **R2**
        - SYS.1.2.3 Windows Server · **R2**
      - SYS.1.3 Server unter Linux und Unix · **R2**
      - SYS.1.5 Virtualisierung · **R2**
      - SYS.1.6 Containerisierung · **R2**
      - SYS.1.7 IBM Z · **R2**
      - SYS.1.8 Speicherlösungen · **R2**
      - SYS.1.9 Terminalserver
    - SYS.2 Desktop-Systeme
      - SYS.2.1 Allgemeiner Client · **R2**
      - SYS.2.2 Windows-Clients
        - SYS.2.2.3 Clients unter Windows · **R2**
      - SYS.2.3 Clients unter Linux und Unix · **R2**
      - SYS.2.4 Clients unter macOS · **R2**
      - SYS.2.5 Client-Virtualisierung · **R2**
      - SYS.2.6 Virtual Desktop Infrastructure · **R2**
    - SYS.3 Mobile Devices
      - SYS.3.1 Laptops · **R2**
      - SYS.3.2 Tablet und Smartphone
        - SYS.3.2.1 Allgemeine Smartphones und Tablets · **R2**
        - SYS.3.2.2 Mobile Device Management (MDM) · **R2**
        - SYS.3.2.3 iOS (for Enterprise) · **R2**
        - SYS.3.2.4 Android · **R2**
      - SYS.3.3 Mobiltelefon · **R2**
    - SYS.4 Sonstige Systeme
      - SYS.4.1 Drucker, Kopierer und Multifunktionsgeräte · **R2**
      - SYS.4.3 Eingebettete Systeme · **R2**
      - SYS.4.4 Allgemeines IoT-Gerät · **R2**
      - SYS.4.5 Wechseldatenträger · **R2**
  - IND (Industrielle IT)
    - IND.1 Prozessleit- und Automatisierungstechnik · **R2**
    - IND.2 ICS-Komponenten
      - IND.2.1 Allgemeine ICS-Komponente · **R2**
      - IND.2.2 Speicherprogrammierbare Steuerung (SPS) · **R2**
      - IND.2.3 Sensoren und Aktoren · **R2**
      - IND.2.4 Maschine · **R2**
      - IND.2.7 Safety Instrumented Systems · **R2**
    - IND.3 Produktionsnetze
      - IND.3.2 Fernwartung im industriellen Umfeld · **R2**
  - NET (Netze und Kommunikation)
    - NET.1 Netze
      - NET.1.1 Netzarchitektur und -design · **R2**
      - NET.1.2 Netzmanagement · **R2**
    - NET.2 Funknetze
      - NET.2.1 WLAN-Betrieb · **R2**
      - NET.2.2 WLAN-Nutzung · **R2**
    - NET.3 Netzkomponenten
      - NET.3.1 Router und Switches · **R2**
      - NET.3.2 Firewall · **R2**
      - NET.3.3 VPN · **R2**
      - NET.3.4 Network Access Control · **R2**
    - NET.4 Telekommunikation
      - NET.4.1 TK-Anlagen · **R2**
      - NET.4.2 VoIP · **R2**
      - NET.4.3 Faxgeräte und Faxserver · **R2**
  - INF (Infrastruktur)
    - INF.1 Allgemeines Gebäude · **R2**
    - INF.2 Rechenzentrum sowie Serverraum · **R2**
    - INF.5 Raum sowie Schrank für technische Infrastruktur · **R2**
    - INF.6 Datenträgerarchiv · **R2**
    - INF.7 Büroarbeitsplatz · **R2**
    - INF.8 Häuslicher Arbeitsplatz · **R2**
    - INF.9 Mobiler Arbeitsplatz · **R2**
    - INF.10 Besprechungs-, Veranstaltungs-. Schulungsraum · **R2**
    - INF.11 Allgemeines Fahrzeug · **R3**
    - INF.12 Verkabelung · **R2**
    - INF.13 Technisches Gebäudemanagement · **R2**
    - INF.14 Gebäudeautomation · **R2**
- Prozess-Bausteine
  - ISMS (Sicherheitsmanagement)
    - ISMS.1 Sicherheitsmanagement · **R1**
  - ORP (Organisation und Personal)
    - ORP.1 Organisation · **R1**
    - ORP.2 Personal · **R1**
    - ORP.3 Sensibilisierung und Schulung zur Informationssicherheit · **R1**
    - ORP.4 Identitäts- und Berechtigungsmanagement · **R1**
    - ORP.5 Compliance Management (Anforderungsmanagement) · **R3**
  - CON (Konzepte und Vorgehensweisen)
    - CON.1 Kryptokonzept · **R3**
    - CON.2 Datenschutz · **R2**
    - CON.3 Datensicherungskonzept · **R1**
    - CON.6 Löschen und Vernichten · **R1**
    - CON.7 Informationssicherheit auf Auslandsreisen · **R3**
    - CON.8 Software-Entwicklung · **R3**
    - CON.9 Informationsaustausch · **R3**
    - CON.10 Entwicklung von Webanwendungen · **R2**
    - CON.11 Geheimschutz
      - CON.11.1 Geheimschutz VS-NUR FÜR DEN DIENSTGEBRAUCH (VS-NfD) · **R3**
  - OPS (Betrieb)
    - OPS.1 Eigener Betrieb
      - OPS.1.1 Kern-IT-Betrieb
        - OPS.1.1.1 Allgemeiner IT-Betrieb · **R1**
        - OPS.1.1.2 Ordnungsgemäße IT-Administration · **R1**
        - OPS.1.1.3 Patch- und Änderungsmanagement · **R1**
        - OPS.1.1.4 Schutz vor Schadprogrammen · **R1**
        - OPS.1.1.5 Protokollierung · **R1**
        - OPS.1.1.6 Software-Tests und -Freigaben · **R1**
        - OPS.1.1.7 Systemmanagement · **R2**
      - OPS.1.2 Weiterführende Aufgaben
        - OPS.1.2.2 Archivierung · **R3**
        - OPS.1.2.4 Telearbeit · **R2**
        - OPS.1.2.5 Fernwartung · **R3**
        - OPS.1.2.6 NTP-Zeitsynchronisation · **R2**
    - OPS.2 Betrieb von Dritten
      - OPS.2.2 Cloud-Nutzung · **R2**
      - OPS.2.3 Nutzung von Outsourcing · **R2**
    - OPS.3 Betrieb für Dritte
      - OPS.3.2 Anbieten von Outsourcing · **R3**
  - DER (Detektion & Reaktion)
    - DER.1 Detektion von sicherheitsrelevanten Ereignissen · **R1**
    - DER.2 Security Incident Management
      - DER.2.1 Behandlung von Sicherheitsvorfällen · **R1**
      - DER.2.2 Vorsorge für die IT-Forensik · **R3**
      - DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle · **R3**
    - DER.3 Sicherheitsprüfungen
      - DER.3.1 Audits und Revisionen · **R3**
      - DER 3.2 Revisionen auf Basis des Leitfadens IS-Revision · **R3**
    - DER.4 Notfallmanagement · **R3**
