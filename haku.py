#!/usr/bin/env python3
"""Haku digest-arkistosta ja clippings-kansiosta.
Käyttö:
  python haku.py "tietomurto" --since 2026-05-04
  python haku.py "lunnasohjelma" --kategoria cyber_news --vain-tunnisteet
"""
import sys, re, pathlib, argparse, datetime

BASE = pathlib.Path(__file__).parent
KATEGORIAT = {
    "🔐": "regulation", "🚨": "vulnerability", "📰": "cyber_news",
    "🛡️": "ai_security", "🇫🇮": "ai_finland", "🤖": "ai_news",
    "🎓": "research",
}

def date_from_file(p: pathlib.Path):
    m = re.match(r"(\d{4}-\d{2}-\d{2})", p.name)
    return m.group(1) if m else None

def tiedot(p: pathlib.Path):
    """Palauttaa (pvm, kategoria, teksti)."""
    t = p.read_text(encoding="utf-8", errors="replace")
    pvm = None
    if p.parent.name == "clippings":
        m = re.search(r"^pvm:\s*(\S+)", t, re.M)
        pvm = m.group(1) if m else date_from_file(p)
        mk = re.search(r"^kategoria:\s*(\S+)", t, re.M)
        kat = mk.group(1) if mk else "other"
    else:  # digests/
        pvm = date_from_file(p)
        kat = "-"  # rivi-luokittelu alla
    return pvm, kat, t

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("hakusana")
    ap.add_argument("--since", default="0001-01-01")
    ap.add_argument("--kategoria", default=None)
    ap.add_argument("--vain-tunnisteet", action="store_true",
                    help="hae vain clippings-tunnisteista")
    args = ap.parse_args()

    tulokset = []
    for kansio in ("digests", "clippings"):
        for p in (BASE / kansio).glob("*.md"):
            pvm, kat, t = tiedot(p)
            if not pvm or pvm < args.since:
                continue
            # digest: kategoria per rivi — suodata rivit joissa hakusana
            if kansio == "digests":
                nyky = "other"
                for rivi in t.splitlines():
                    for emo, k in KATEGORIAT.items():
                        if emo in rivi and rivi.startswith("##"):
                            nyky = k
                    if args.hakusana.lower() in rivi.lower():
                        if args.kategoria and nyky != args.kategoria:
                            continue
                        tulokset.append((pvm, nyky, rivi.strip()[:200]))
            else:  # clippings
                if args.vain_tunnisteet:
                    m = re.search(r"^tunnisteet:\s*\[(.*?)\]", t, re.M)
                    osuma = m and args.hakusana.lower() in m.group(1).lower()
                else:
                    osuma = args.hakusana.lower() in t.lower()
                if osuma and (not args.kategoria or kat == args.kategoria):
                    otsikko = re.search(r"^\*\*(.+?)\*\*", t, re.M)
                    tulokset.append((pvm, kat, (otsikko.group(1) if otsikko else p.stem)))

    tulokset.sort()
    print(f"# Haku: '{args.hakusana}' (alkaen {args.since}) — {len(tulokset)} osumaa\n")
    for pvm, kat, rivi in tulokset:
        print(f"- {pvm} · {kat} · {rivi}")

if __name__ == "__main__":
    main()
