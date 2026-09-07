#!/usr/bin/env python3
"""Holt eine Drive-Datei per HTTPS, wenn der Connector sie nicht liefern kann.

Der Google-Drive-Connector uebertraegt base64-kodiert. Das blaeht den Umfang
um rund ein Drittel auf und laesst Dateien ab etwa 7 MB mit 'session expired'
scheitern — eine Groessengrenze, kein Sitzungsproblem. Fuer solche Dateien
bleibt der direkte HTTPS-Bezug.

Voraussetzung ist eine *befristete* Linkfreigabe der Datei ("Jeder mit dem
Link"). Ohne sie liefert Google die Anmeldeseite statt der Datei; das Skript
erkennt das und bricht ab, statt HTML als Dokument abzulegen. Die Freigabe
gehoert unmittelbar nach dem Bezug zurueckgestellt.

Ab etwa 25 MB schiebt Google eine Bestaetigungsseite vor den Download
("Diese Datei kann nicht auf Viren geprueft werden"). Das Skript liest das
Formular aus und schickt die Bestaetigung nach, statt an der Seite haengen
zu bleiben.

Die geladenen Bytes sind zu pruefen, bevor sie in den Bestand gehen: Groesse
und SHA-256 muessen zu den Drive-Metadaten passen. Genau dafuer sind
--expect-bytes und --expect-sha256 da; ohne sie meldet das Skript die Werte
nur, und der Abgleich bleibt Handarbeit.
"""
from __future__ import annotations

import hashlib
import html
import re
import urllib.parse
import urllib.request
from http.cookiejar import CookieJar
from pathlib import Path

import click

BASE = "https://drive.usercontent.google.com/download"
UA = "Mozilla/5.0 (X11; Linux x86_64) document-to-LLM/fetch_drive"
HTML_START = (b"<!DOCTYPE", b"<!doctype", b"<html", b"<HTML")


def opener() -> urllib.request.OpenerDirector:
    o = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(CookieJar()))
    o.addheaders = [("User-Agent", UA)]
    return o


def form_fields(page: str) -> dict[str, str] | None:
    """Liest die versteckten Felder der Bestaetigungsseite aus.

    Google baut die Seite gelegentlich um. Findet sich kein Formular, ist das
    kein Grund zu raten — dann meldet der Aufrufer den Befund und bricht ab.
    """
    if "confirm" not in page:
        return None
    felder = {}
    for name, value in re.findall(
            r'<input[^>]+name="([^"]+)"[^>]+value="([^"]*)"', page):
        felder[name] = html.unescape(value)
    return felder or None


def hole(file_id: str, ziel: Path) -> tuple[int, str]:
    o = opener()
    url = f"{BASE}?{urllib.parse.urlencode({'id': file_id, 'export': 'download', 'confirm': 't'})}"

    for versuch in (1, 2):
        with o.open(url, timeout=120) as antwort:
            kopf = antwort.read(1024)
            if not kopf.startswith(HTML_START):
                sha = hashlib.sha256()
                groesse = 0
                with ziel.open("wb") as f:
                    f.write(kopf)
                    sha.update(kopf)
                    groesse += len(kopf)
                    while stueck := antwort.read(1 << 20):
                        f.write(stueck)
                        sha.update(stueck)
                        groesse += len(stueck)
                return groesse, sha.hexdigest()
            seite = (kopf + antwort.read()).decode("utf-8", "replace")

        if versuch == 2:
            break
        if "accounts.google.com" in seite or "ServiceLogin" in seite:
            raise click.ClickException(
                "Google liefert die Anmeldeseite statt der Datei. Die Datei ist "
                "nicht per Link freigegeben — Freigabe 'Jeder mit dem Link' "
                "setzen, Datei holen, Freigabe wieder zuruecknehmen.")
        felder = form_fields(seite)
        if not felder:
            raise click.ClickException(
                "Antwort ist HTML, aber weder Anmeldeseite noch erkennbares "
                "Bestaetigungsformular. Google hat die Seite vermutlich "
                "umgebaut; von Hand pruefen, statt zu raten.")
        url = f"{BASE}?{urllib.parse.urlencode(felder)}"

    raise click.ClickException(
        "Auch nach der Bestaetigung kam HTML statt der Datei.")


@click.command()
@click.argument("file_id")
@click.option("--to", type=click.Path(file_okay=False, path_type=Path),
              default=Path("input"), show_default=True,
              help="Zielordner. Standard ist der Eingangsordner der Skill.")
@click.option("--name", required=True,
              help="Dateiname im Zielordner, mit Endung — wie in Drive.")
@click.option("--expect-bytes", type=int, default=None,
              help="Groesse laut Drive-Metadaten. Weicht sie ab, bricht das "
                   "Skript ab und laesst nichts Halbes im Eingang liegen.")
@click.option("--expect-sha256", default=None,
              help="SHA-256 laut Drive-Metadaten, falls bekannt.")
def main(file_id: str, to: Path, name: str,
         expect_bytes: int | None, expect_sha256: str | None) -> None:
    """Laedt die Drive-Datei FILE_ID nach --to und prueft die Bytes."""
    to.mkdir(parents=True, exist_ok=True)
    ziel = to / name
    if ziel.exists():
        raise click.ClickException(
            f"{ziel} liegt schon vor. Erst pruefen, dann bewusst ersetzen.")

    groesse, sha = hole(file_id, ziel)

    fehler = []
    if expect_bytes is not None and groesse != expect_bytes:
        fehler.append(f"Groesse {groesse} statt erwarteter {expect_bytes}")
    if expect_sha256 and sha != expect_sha256.lower():
        fehler.append(f"SHA-256 {sha} statt erwarteter {expect_sha256.lower()}")
    if fehler:
        ziel.unlink(missing_ok=True)
        raise click.ClickException(
            "Geladene Bytes passen nicht zu den Drive-Metadaten: "
            + "; ".join(fehler) + ". Datei wurde wieder entfernt.")

    click.echo(f"{ziel}  {groesse} Bytes  sha256 {sha}")
    if expect_bytes is None and not expect_sha256:
        click.secho("Ungeprueft: keine Erwartungswerte angegeben. Groesse und "
                    "SHA-256 gegen die Drive-Metadaten abgleichen, bevor die "
                    "Datei in den Bestand geht.", fg="yellow")
    click.secho("Linkfreigabe jetzt zuruecknehmen.", fg="yellow")


if __name__ == "__main__":
    main()
