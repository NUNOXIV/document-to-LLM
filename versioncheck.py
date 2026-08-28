#!/usr/bin/env python3
"""ACSOS document-to-LLM — Versionsstand der aufgenommenen Dokumente pruefen.

Holt zu jedem Dokument den aktuellen Stand von der offiziellen Fundstelle und
vergleicht ihn mit der aufgenommenen Fassung. Nichts wird aus dem Gedaechtnis
beantwortet: was nicht abrufbar ist, wird als "manuell pruefen" mit Fundstelle
ausgewiesen, nicht geraten.

    python versioncheck.py                       # alle Dokumente
    python versioncheck.py --only wstg-v4-2      # eines
    python versioncheck.py --json                # maschinenlesbar
"""

from __future__ import annotations

import json
import re
import ssl
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

import click

REGISTRY = Path(__file__).parent / "versions.json"
UA = "ACSOS-document-to-LLM/1.0 (Versionspruefung)"
TIMEOUT = 30


@dataclass
class Finding:
    slug: str
    titel: str
    aufgenommen: str
    aktuell: str | None
    quelle: str
    status: str          # aktuell | veraltet | historisch | belegt | manuell | unerreichbar
    hinweis: str = ""
    beleg: str = ""      # Fundstelle im Dokument, wenn die Fassung dort steht


def fetch(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        ctx = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt") \
            if Path("/root/.ccr/ca-bundle.crt").exists() else None
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return None


def newest(values: list[str]) -> str:
    """Hoechste Version aus den Treffern — numerisch, nicht alphabetisch."""
    def key(v: str) -> tuple:
        return tuple(int(x) for x in re.findall(r"\d+", v)) or (0,)
    return max(values, key=key)


def from_document(slug: str, pattern: str, out_dir: Path) -> tuple[str, str] | None:
    """Fassung aus dem Extrakt lesen — mit Seitenzahl als Beleg.

    Fuer lizenzierte Normen ist das oft die einzige belastbare Angabe: der
    Katalog ist kostenpflichtig, das Dokument selbst sagt aber, welche Ausgabe
    vorliegt.
    """
    md = out_dir / f"{slug}.md"
    if not md.exists():
        return None
    text = md.read_text(encoding="utf-8")
    m = re.search(pattern, text)
    if not m:
        return None
    value = m.group(1) if m.groups() else m.group(0)
    page = 0
    for pm in re.finditer(r"<!--\s*page:\s*(\d+)\s*-->", text[: m.start()]):
        page = int(pm.group(1))
    return value.strip(), (f"{md.name}, S. {page}" if page else md.name)


def check(slug: str, entry: dict, out_dir: Path) -> Finding:
    titel = entry.get("titel", slug)
    have = str(entry.get("dokument_version", "?"))
    url = entry.get("quelle", "")
    pattern = entry.get("muster")
    note = entry.get("anmerkung", "")

    beleg = ""
    doc_pattern = entry.get("dokument_muster")
    if doc_pattern:
        read = from_document(slug, doc_pattern, out_dir)
        if read:
            have, beleg = read[0], read[1]
        else:
            note = (note + " " if note else "") + \
                "Fassung im Extrakt nicht gefunden — Registryeintrag ungeprueft."

    if not pattern:
        status = "belegt" if beleg else "manuell"
        return Finding(slug, titel, have, None, url, status, note, beleg)

    page = fetch(url)
    if page is None:
        return Finding(slug, titel, have, None, url, "unerreichbar",
                       (note + " " if note else "") +
                       "Fundstelle nicht erreichbar (Netzsperre oder Ausfall).", beleg)

    hits = [m if isinstance(m, str) else m[0]
            for m in re.findall(pattern, page, flags=re.I)]
    if not hits:
        return Finding(slug, titel, have, None, url, "manuell",
                       (note + " " if note else "") +
                       "Muster auf der Seite nicht gefunden — Seite umgebaut?", beleg)

    current = newest(hits)
    same = re.findall(r"\d+", current) == re.findall(r"\d+", have)
    status = "aktuell" if same else "veraltet"
    if status == "veraltet" and slug in historisch():
        status = "historisch"
        nachfolger = historisch()[slug]
        note = (note + " " if note else "") + \
            f"Bewusst als Historiendokument gefuehrt; geltend ist {nachfolger}."
    return Finding(slug, titel, have, current, url, status, note, beleg)


def historisch() -> dict[str, str]:
    """Slugs, die bewusst als Historiendokument gefuehrt werden, mit Nachfolger.

    Ein solches Dokument ist zwar nicht der aktuelle Stand, aber auch kein
    Mangel: es liegt absichtlich im Bestand, damit nachlesbar ist, was frueher
    galt. Es als "nicht auf dem aktuellen Stand" zu melden waere eine
    Fehlermeldung fuer eine getroffene Entscheidung.
    """
    path = Path(__file__).parent / "mappings" / "historie.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {e["slug"]: e.get("gilt_stattdessen", "")
            for e in data.get("abgeloest", []) if e.get("slug")}


def render(findings: list[Finding]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    veraltet = [f for f in findings if f.status == "veraltet"]
    lines = [
        "---",
        "type: versionspruefung",
        'tags: ["grc/tracker", "grc/versionsstand"]',
        "generated-by: document-to-LLM",
        f"generated_at: {now}",
        f"veraltet: {len(veraltet)}",
        "---",
        "",
        "# Versionsstand der aufgenommenen Dokumente",
        "",
        f"Stand {now}. Jeder Lauf holt den Stand neu von der Fundstelle; nichts "
        f"davon ist auswendig beantwortet.",
        "",
    ]
    if veraltet:
        lines += ["> [!warning] Nicht auf dem aktuellen Stand", ""]
        for f in veraltet:
            lines.append(f"> - **{f.titel}**: aufgenommen {f.aufgenommen}, "
                         f"aktuell {f.aktuell} — {f.quelle}")
        lines.append("")
    else:
        lines += ["> [!success] Kein Dokument als veraltet erkannt", ""]

    lines += ["| Dokument | Aufgenommen | Aktuell | Befund | Fundstelle |",
              "| --- | --- | --- | --- | --- |"]
    symbol = {"aktuell": "aktuell", "veraltet": "VERALTET", "historisch": "historisch",
              "belegt": "aus Dokument belegt", "manuell": "manuell pruefen",
              "unerreichbar": "Quelle offline"}
    for f in sorted(findings, key=lambda x: (x.status != "veraltet", x.titel)):
        lines.append(f"| {f.titel} | {f.aufgenommen}"
                     + (f" <br><sub>{f.beleg}</sub>" if f.beleg else "")
                     + f" | {f.aktuell or '—'} | {symbol[f.status]} | {f.quelle} |")
    hints = [f for f in findings if f.hinweis]
    if hints:
        lines += ["", "## Anmerkungen", ""]
        lines += [f"- **{f.titel}**: {f.hinweis}" for f in hints]
    return "\n".join(lines) + "\n"


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--registry", default=str(REGISTRY), show_default=True,
              type=click.Path(exists=True, dir_okay=False))
@click.option("--output", "out_dir", default="output", show_default=True,
              type=click.Path(file_okay=False),
              help="Ordner mit den Extrakten (fuer die Fassung aus dem Dokument).")
@click.option("--only", default=None, help="Nur dieses Dokument pruefen (Slug).")
@click.option("--to", "targets", multiple=True, help="Bericht zusaetzlich hierhin schreiben.")
@click.option("--json", "as_json", is_flag=True, help="Ergebnis als JSON ausgeben.")
@click.option("--strict", is_flag=True, help="Exit-Code 1, wenn ein Dokument veraltet ist.")
def main(registry: str, out_dir: str, only: str | None, targets: tuple[str, ...],
         as_json: bool, strict: bool) -> None:
    """Prueft, ob die aufgenommenen Dokumente dem aktuellen Stand entsprechen."""
    data = json.loads(Path(registry).read_text(encoding="utf-8"))
    docs = data.get("documents", {})
    if only:
        docs = {k: v for k, v in docs.items() if k == only}
        if not docs:
            raise click.ClickException(f"Kein Eintrag fuer {only} in der Registry.")

    findings = [check(slug, entry, Path(out_dir)) for slug, entry in docs.items()]

    if as_json:
        click.echo(json.dumps([asdict(f) for f in findings], ensure_ascii=False, indent=2))
    else:
        for f in findings:
            colour = {"aktuell": "green", "veraltet": "red", "belegt": "cyan",
                      "manuell": "yellow", "unerreichbar": "yellow",
                      "historisch": "cyan"}[f.status]
            detail = f"aufgenommen {f.aufgenommen}" + (f", aktuell {f.aktuell}" if f.aktuell else "")
            detail += f", Beleg: {f.beleg}" if f.beleg else ""
            click.secho(f"{f.status.upper():14s} {f.titel} ({detail})", fg=colour)

    text = render(findings)
    for t in targets:
        target = Path(t).expanduser()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        click.echo(f"Bericht: {target}")

    veraltet = [f for f in findings if f.status == "veraltet"]
    if veraltet:
        click.secho(f"\n{len(veraltet)} Dokument(e) nicht auf dem aktuellen Stand.", fg="red")
    if strict and veraltet:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
