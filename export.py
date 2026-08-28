#!/usr/bin/env python3
"""ACSOS document-to-LLM — Anforderungen je Framework als JSON exportieren.

Erzeugt fuer jedes Framework des Vaults eine Datei in der Form, mit der ein
rechnendes System ohne Uebersetzung arbeiten kann:

    {"frameworkId": …, "edition": …, "sourceFile": …, "sourceSha256": …,
     "requirements": [{"id":…, "title":…, "text":…, "group":…}], "missing": […]}

Welcher Extrakt ein Framework belegt hat, wird nicht gepflegt, sondern gelesen:
jede Normtext-Notiz im Vault nennt die Quelle, aus der sie stammt. Eine
gepflegte Liste koennte veralten, diese Ableitung nicht.

Frameworks, die sich auf mehrere Quellen verteilen (der C5-Katalog liegt als
eine Datei je Kriterienbereich vor), werden zu einer Datei zusammengefuehrt:
einzeln exportiert meldete jeder Teil die Anforderungen der anderen als
fehlend.

    python export.py --vault ~/obsidian-vault --to export/
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import click

import publish

LICENSED_DIR = "Normen (lizenziert)"


def framework_editionen() -> dict[str, str]:
    """Optionale Zuordnung Framework -> Registry-Eintrag fuer die Ausgabe.

    Noetig, wo der Extrakt selbst nicht in versions.json steht: der C5-Katalog
    verteilt sich auf 18 Kriterienbereiche, seine Fassung steht in einer
    19. Datei. Ohne diese Zuordnung bliebe 'edition' leer, obwohl die Angabe
    vorliegt.
    """
    path = Path(__file__).parent / "mappings" / "frameworks.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("edition_slug", {})


def extrakte_nach_sha(out_dir: Path) -> dict[str, str]:
    """sha256 der Quelle -> Slug des Extrakts."""
    treffer: dict[str, str] = {}
    for md in sorted(out_dir.glob("*.md")):
        if md.name.startswith("_"):
            continue
        m = re.search(r"source_sha256:\s*([0-9a-f]{64})",
                      md.read_text(encoding="utf-8")[:1500])
        if m:
            treffer[m.group(1)] = md.stem
    return treffer


def quellen_des_frameworks(ordner: Path) -> Counter:
    """Welche Quellen die Normtext-Notizen eines Frameworks nennen."""
    shas: Counter = Counter()
    for note in ordner.glob("*.md"):
        m = re.search(r"source_sha256:\s*([0-9a-f]{64})",
                      note.read_text(encoding="utf-8")[:1200])
        if m:
            shas[m.group(1)] += 1
    return shas


def sammle(framework: str, slugs: list[str], vault: Path, out_dir: Path) -> dict:
    """Anforderungen eines Frameworks ueber alle seine Quellen einsammeln."""
    wanted = publish.vault_ids(vault, framework)
    reqs: dict[str, dict] = {}
    quellen: list[dict] = []

    for slug in slugs:
        md = out_dir / f"{slug}.md"
        meta, body = publish.split_front_matter(md.read_text(encoding="utf-8"))
        quellen.append({"sourceFile": meta.get("source_file", ""),
                        "sourceSha256": meta.get("source_sha256", "")})
        for ident, sec in publish.aufgeloeste_abschnitte(
                body, meta, wanted, framework).items():
            reqs.setdefault(ident, {"id": ident, "title": sec.title,
                                    "text": sec.text, "group": publish.gruppe(ident)})

    fehlend = sorted(set(wanted) - set(reqs))
    edition = publish.edition_aus_registry(framework_editionen().get(framework, "")) \
        or (publish.edition_aus_registry(slugs[0]) if len(slugs) == 1 else None)
    return {
        "frameworkId": framework,
        "edition": edition,
        # Bei mehreren Quellen waere eine einzelne sourceFile falsch; die
        # Aufstellung steht dann unter 'sources'.
        "sourceFile": (quellen[0]["sourceFile"] if len(quellen) == 1
                       else f"{len(quellen)} Quelldateien"),
        "sourceSha256": quellen[0]["sourceSha256"] if len(quellen) == 1 else "",
        **({"sources": quellen} if len(quellen) > 1 else {}),
        "requirements": [reqs[i] for i in sorted(reqs)],
        "missing": fehlend,
    }


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--vault", required=True, type=click.Path(file_okay=False, exists=True),
              help="Wurzel des Obsidian-Vaults.")
@click.option("-o", "--output", "out_dir", default="output", show_default=True,
              type=click.Path(exists=True, file_okay=False),
              help="Ordner mit den Extrakten.")
@click.option("--to", "ziel", default="export", show_default=True,
              help="Zielordner fuer die JSON-Dateien.")
@click.option("--only", default=None, help="Nur dieses Framework exportieren.")
def main(vault: str, out_dir: str, ziel: str, only: str | None) -> None:
    """Schreibt je Framework eine JSON-Datei mit seinen Anforderungen."""
    vault_path, out = Path(vault).expanduser(), Path(out_dir)
    zielordner = Path(ziel).expanduser()
    zielordner.mkdir(parents=True, exist_ok=True)
    sha2slug = extrakte_nach_sha(out)

    liz = vault_path / LICENSED_DIR
    ordner = sorted(p for p in liz.iterdir()
                    if p.is_dir() and p.name != "dokumente"
                    and (only is None or p.name == only))
    if not ordner:
        raise click.ClickException(
            f"Keine Frameworks in {liz} gefunden" + (f" (--only {only})" if only else ""))

    gesamt = 0
    for o in ordner:
        shas = quellen_des_frameworks(o)
        slugs = [sha2slug[s] for s, _ in shas.most_common() if s in sha2slug]
        unbekannt = [s for s in shas if s not in sha2slug]
        if not slugs:
            click.secho(f"{o.name}: keine Quelle im Bestand — uebersprungen", fg="yellow")
            continue
        daten = sammle(o.name, slugs, vault_path, out)
        (zielordner / f"{o.name}.json").write_text(
            json.dumps(daten, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        gesamt += len(daten["requirements"])
        hinweis = f" · {len(unbekannt)} Quelle(n) nicht im Bestand" if unbekannt else ""
        click.echo(f"{o.name:20} {len(daten['requirements']):5} Anforderungen"
                   f" · {len(daten['missing']):4} ohne Wortlaut"
                   f" · {len(slugs)} Quelle(n){hinweis}")
    click.secho(f"\n{gesamt} Anforderungen in {zielordner}/", fg="green")


if __name__ == "__main__":
    main()
