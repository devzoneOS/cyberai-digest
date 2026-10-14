#!/usr/bin/env python3
"""
CyberAI Digest Agent — paikallinen uutisagentti (v2)
====================================================
Automaattinen agentti, joka:
 1. Noutaa tuoreita kyberturvallisuus- ja tekoälyuutisia RSS-syötteistä
 2. LUOKITTELEE uutiset aiheittain (ks. CATEGORIES alla):
      Cybersecurity: Regulaatiot | Haavoittuvuudet | Uutuudet & uhat
      AI:            AI Security | Uutuudet | Suomi-uutiset | Muut uutiset
 3. Muodostaa suomenkielisen puheskriptin (Mistral API) aiheittain järjestettynä
 4. Muuntaa skriptin ääneksi (edge-tts, ilmainen; tai Kokoro GPU:lla)
 5. Tallentaa MP3:n + markdown-tekstihistorian + lähdelistaus + podcast-RSS
"""

import os
import re
import html
import hashlib
import datetime
import pathlib
import requests
import feedparser
import edge_tts

# ----------------------------------------------------------------- asetukset
BASE_DIR = pathlib.Path(os.environ.get("DIGEST_HOME", "~/cyberai-agent")).expanduser()
AUDIO_DIR = BASE_DIR / "audio"
TEXT_DIR = BASE_DIR / "digests"
STATE_FILE = BASE_DIR / "seen.txt"
RSS_FILE = BASE_DIR / "podcast.xml"
SOURCES_FILE = BASE_DIR / "sources.md"
BASE_URL = os.environ.get("DIGEST_BASE_URL", "http://192.168.1.10:8000")
VOICE = os.environ.get("DIGEST_VOICE", "fi-FI-HarriNeural")
MAX_ITEMS_PER_FEED = 3
MAX_ITEMS_TOTAL = 14
LLM_MODEL = os.environ.get("DIGEST_MODEL", "mistral-small-latest")
TTS_ENGINE = os.environ.get("DIGEST_TTS", "edge")  # "edge" tai "kokoro"

FEEDS_FILE = BASE_DIR / "feeds.txt"

def load_feeds() -> dict:
    """Lukee lähteet feeds.txt:sta: yksi 'Nimi: URL' per rivi."""
    feeds = {}
    if FEEDS_FILE.exists():
        for line in FEEDS_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or ":" not in line:
                continue
            name, url = line.split(":", 1)
            name, url = name.strip(), url.strip()
            if url.startswith("http"):
                feeds[name] = url
    return feeds

FEEDS = load_feeds()

# ------------------------------------------------------- aiheiden luokittelu
# Avainsanat pienillä kirjaimilla; osuman mukaan -> (pääaihe, alaluokka).
# Luokittelujärjestys: ensimmäinen osuva sääntö voittaa.
RULES = [
    # --- Cybersecurity: Regulaatiot & standardit ---
    ("regulation", ["iso 27001", "iso/iec", "nist", "nis2", "gdpr", "dora",
                    "eu ai act", "sääntely", "säädös", "directive", "regulation",
                    "compliance", "certification", "sertif", "audit",
                    "supervisory", "dpa ", "enforcement", "fine ", "sakko", "valvonta"]),
    # --- Cybersecurity: Haavoittuvuudet ---
    ("vulnerability", ["cve-", "vulnerability", "zero-day", "zeroday", "exploit",
                       "rce", "path traversal", "patch", "security update",
                       "advisory", "critical flaw", "privilege escalation",
                       "sql injection", "xss", "heap", "overflow", "poc "]),
    # --- Cybersecurity: Uutuudet & uhat (oletus-kuuluu tänne) ---
    ("cyber_news", ["ransomware", "breach", "malware", "phishing", "apt",
                    "hack", "attack", "infostealer", "botnet", "ddos", "scam",
                    "threat actor", "data leak", "leak", "credential", "spyware",
                    "backdoor", "trojan"]),
    # --- AI: AI Security ---
    ("ai_security", ["prompt injection", "jailbreak", "adversarial",
                     "model attack", "llm security", "ai security", "misuse",
                     "red team", "safeguard", "guardrail", "deepfake",
                     "ai-powered attack", "agentic attack", "fraud ai"]),
    # --- AI: Suomi ---
    ("ai_finland", ["suomi", "suomen", "finland", "suomalainen", " helsinki",
                    "espoo", "oulu", "tampere", " kybers", "tietosuoja"]),
    # --- AI: Uutuudet ---
    ("ai_news", ["model", "llm", "openai", "anthropic", "claude", "gpt",
                 "gemini", "deepmind", "llama", "mistral", "deepseek",
                 "benchmark", "release", "launch", "funding", "startup"]),
]

CATEGORY_META = {
    # avain: (nimi puhesyylissä, markdown-otsikko)
    "regulation":    ("Kyberturvallisuus: säädökset ja standardit", "🔐 Säädökset ja standardit (ISO 27001, NIS2, GDPR, EU AI Act…)"),
    "vulnerability": ("Kyberturvallisuus: haavoittuvuudet", "🚨 Haavoittuvuudet ja patchit"),
    "cyber_news":    ("Kyberturvallisuus: uutiset ja uhat", "📰 Kyberuutiset ja uhat"),
    "ai_security":   ("Tekoäly: tietoturva", "🛡️ Tekoälyn tietoturva (AI Security)"),
    "ai_finland":    ("Tekoäly: Suomi-uutiset", "🇫🇮 Tekoälyuutiset Suomesta"),
    "ai_news":       ("Tekoäly: uutuudet", "🤖 Tekoälyn uutiset ja uutuudet"),
    "other":         ("Muut uutiset", "📎 Muut uutiset"),
}

SECTION_ORDER = ["regulation", "vulnerability", "cyber_news",
                 "ai_security", "ai_finland", "ai_news", "other"]


def classify(item: dict) -> str:
    """Palauttaa luokka-avaimen otsikko+tiivistelmän avainsääntöjen perusteella."""
    hay = f"{item['title']} {item['summary']}".lower()
    for cat, keywords in RULES:
        if any(k in hay for k in keywords):
            return cat
    return "other"


PROMPT = """Olet tiivistemestari. Tee alla olevista uutisista suomenkielinen
kuunnelmatiivistelmä podcast-muodossa.

Uutiset on jo luokiteltu aiheittain. Noudata TÄSMÄLLEEN tätä järjestystä ja
mainitse siirtymissä osion nimi (esim. "Haavoittuvuuksissa tapahtuu...").
Jos jokin osio on tyhjä, ohita se kokonaan mainitsematta.

Osiojärjestys:
1. Säädökset ja standardit (ISO 27001, NIS2, GDPR, EU AI Act)
2. Haavoittuvuudet ja patchit
3. Kyberuutiset ja uhat
4. Tekoälyn tietoturva
5. Tekoälyuutiset Suomesta
6. Tekoälyn uutiset ja uutuudet

PITUUS uutisten määrän mukaan:
- alle 6 uutista: lyhyt katsaus, n. 150 sanaa
- 6-12 uutista: n. 250 sanaa
- yli 12 uutista: perusteellinen katsaus, n. 400 sanaa

Säännöt:
- Aloita tervehdyksellä "Hyvää huomenta, Olli" ja KÄYTÄ uutisten alussa annettua
  päivämäärää täsmälleen. Älä keksi omaa päivämäärää.
- Puhetyyli, asiantunteva mutta rento. Ei luettelomerkkejä, ei otsikoita.
- Kirjoita desimaaliluvut (esim. CVSS-pisteet) pilkulla: "9,8" eikä "9.8".
- Kirjoita päivämäärät mieluiten kirjaimin: "kolmastoista lokakuuta".
- Mainitse versiot luontevasti, vältä pitkiä numeroketjuja.
- Kun uutisia on paljon, syvenny tärkeimpiin äläkä luettele kaikkia tasapaksusti.
- Älä sekoita aiheita keskenään — sama aihe pysyy samassa osiossa.
- Lopeta yhdellä käytännön vinkillä tai huomiolla päivältä.

Uutiset:
{news}
"""


# ----------------------------------------------------------------- apufunktiot
def load_seen() -> set:
    if STATE_FILE.exists():
        return {line.strip() for line in STATE_FILE.read_text().splitlines() if line.strip()}
    return set()


def save_seen(seen: set) -> None:
    STATE_FILE.write_text("\n".join(sorted(seen)))


def clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html.unescape(text or ""))
    return re.sub(r"\s+", " ", text).strip()


def fetch_news(seen: set):
    items = []
    feed_stats = {}  # lähde -> noudettujen määrä (lähdelistausta varten)
    broken = []
    for name, url in FEEDS.items():
        try:
            parsed = feedparser.parse(url)
            if parsed.bozo and not parsed.entries:
                raise RuntimeError(f"syote virheellinen: {parsed.bozo_exception}")
            count = 0
            for e in parsed.entries:
                uid = hashlib.md5(clean(e.get("title", "")).encode()).hexdigest()
                if uid in seen or not e.get("title"):
                    continue
                items.append({
                    "source": name,
                    "title": clean(e.title),
                    "summary": clean(e.get("summary", ""))[:300],
                    "link": e.get("link", ""),
                    "uid": uid,
                })
                seen.add(uid)
                count += 1
                if count >= MAX_ITEMS_PER_FEED:
                    break
            feed_stats[name] = count
        except Exception as exc:  # syötteen nouto ei saa kaataa ajoa
            broken.append(name)
            feed_stats[name] = 0
            print(f"[warn] {name}: {exc}")
    return items[:MAX_ITEMS_TOTAL], feed_stats, broken


def make_digest(items):
    """Luokittelee uutiset ja palauttaa (skripti, markdown, feed_stats, used, broken)."""
    # --- luokittelu ---
    buckets = {}
    for it in items:
        it["category"] = classify(it)
        buckets.setdefault(it["category"], []).append(it)

    # --- puheskripti Mistralilta ---
    news_parts = []
    for cat in SECTION_ORDER:
        for it in buckets.get(cat, []):
            news_parts.append(f"[{CATEGORY_META[cat][0]}] {it['title']}: {it['summary']}")

    # ← UUSI: kertoa mallille tänään päivä (ei arvaamista)
    today = datetime.date.today()
    paivys = f"{today.day}.{today.month}.{today.year}"
    viikonpaiva = ["maanantai", "tiistai", "keskiviikko", "torstai",
                   "perjantai", "lauantai", "sunnuntai"][today.weekday()]
    news_text = (
        f"TÄNÄÄN ON {viikonpaiva} {paivys}. "
        "Käytä tätä päivämäärää tervehdyksessä täsmälleen oikein. Älä keksi omaa.\n\n"
        + "\n".join(news_parts)
    )

    api_key = os.environ["MISTRAL_API_KEY"]
    resp = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": LLM_MODEL,
            "messages": [{"role": "user", "content": PROMPT.format(news=news_text)}],  # ← muutos
            "temperature": 0.4,
        },
        timeout=120,
    )
    resp.raise_for_status()
    script = resp.json()["choices"][0]["message"]["content"].strip()

    # --- markdown-digest aiheittain + lähdelistaus ---
    today = datetime.date.today().isoformat()
    md = [f"# Digest — {today}", ""]
    for cat in SECTION_ORDER:
        group = buckets.get(cat, [])
        if not group:
            continue
        md += [f"## {CATEGORY_META[cat][1]}", ""]
        for i, it in enumerate(group, 1):
            md.append(f"{i}. **{it['title']}** — {it['summary']} ([{it['source']}]({it['link']}))")
        md.append("")
    used = sorted({it["source"] for it in items})
    md += ["## Käytetyt lähteet tänään", ""]
    md += [f"- {s}" for s in used]
    md += ["", "## Puheskripti", "", script]
    return script, "\n".join(md), used

def clean_for_tts(text: str) -> str:
    """Poistaa merkinnät, joita TTS ei saa lukea ääneen."""
    import re
    text = re.sub(r"\*\*+", "", text)      # ** ja *** pois
    text = text.replace("*", "")           # yksittäiset asteriskit
    text = re.sub(r"^#+\s*", "", text)     # otsikkomerkit
    text = re.sub(r"`{1,3}", "", text)     # koodimerkit
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", text)  # teksti -> teksti
    text = re.sub(r"https?://\S+", "linkki", text)     # paljaat URL:t sanaksi "linkki"
    text = re.sub(r"[_#|>]+", " ", text)   # loput merkinnät
    # Versioketjut ENSIN (vaativampi sääntö): 14.0.3650 -> "14 piste 0 piste 3650"
    text = re.sub(r"\b(\d+(?:\.\d+){2,})\b",
                  lambda m: m.group(1).replace(".", " piste "), text)
    # Sitten desimaalit: 9.8 -> "9 pilkku 8" (ei tulkita päivämääräksi)
    text = re.sub(r"(\d{1,2})\.(\d)(?!\d)", r"\1 pilkku \2", text)
                  lambda m: m.group(1).replace(".", " piste "), text)
    return re.sub(r"\s{2,}", " ", text).strip()


def update_sources_stats(feed_stats: dict, broken: list, used: list) -> None:
    """Ylläpitää sources.md-tilastoa: mitkä lähteet aktiivisia, mitkä rikki."""
    today = datetime.date.today().isoformat()
    stats = {}
    if SOURCES_FILE.exists():
        for line in SOURCES_FILE.read_text().splitlines():
            m = re.match(r"\| (.+?) \| (\d+) \| (\d+) \| (\d+) \| ([\d-]+) \|", line)
            if m:
                stats[m.group(1)] = {"days": int(m.group(2)), "items": int(m.group(3)),
                                     "broken": int(m.group(4)), "last": m.group(5)}
    for name in FEEDS:
        s = stats.setdefault(name, {"days": 0, "items": 0, "broken": 0, "last": "-"})
        s["days"] += 1
        s["items"] += feed_stats.get(name, 0)
        if name in broken:
            s["broken"] += 1
        if name in used:
            s["last"] = today
    rows = ["| Lähde | päiviä | uutisia | rikki | viimeksi tuotti |",
            "|---|---|---|---|---|"]
    for name, s in sorted(stats.items(), key=lambda kv: -kv[1]["items"]):
        rows.append(f"| {name} | {s['days']} | {s['items']} | {s['broken']} | {s['last']} |")
    SOURCES_FILE.write_text(f"# Lähdetilastot (päivitetty {today})\n\n" + "\n".join(rows) + "\n")


def text_to_mp3(script: str, out_path: pathlib.Path) -> None:
    if TTS_ENGINE == "kokoro":
        # Paikallinen Kokoro-82M GPU:lla — asenna: pip install kokoro soundfile
        import asyncio
        from kokoro import KPipeline  # type: ignore
        import numpy as np  # type: ignore
        import soundfile as sf  # type: ignore
        pipeline = KPipeline(lang_code="f")
        audio_chunks = []
        for _, _, audio in pipeline(script):
            audio_chunks.append(audio)
        sf.write(str(out_path), np.concatenate(audio_chunks), 24000)
    else:
        import asyncio

        async def edge_save():
            await edge_tts.Communicate(clean_for_tts(script), VOICE).save(str(out_path))

        for attempt in range(1, 4):  # 3 yritystä
            try:
                asyncio.run(edge_save())
                return
            except Exception as exc:
                print(f"[warn] edge-tts yritys {attempt}/3 epäonnistui: {exc}")
        print("[warn] edge-tts ei vastaa — siirrytään varajärjestelmään (gTTS).")
        from gtts import gTTS
        gTTS(clean_for_tts(script), lang="fi").save(str(out_path))


def write_podcast_rss(entries: list) -> None:
    """entries: [{"title", "date", "mp3_url", "size"}] — uusin ensin."""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    items = []
    for e in entries:
        items.append(
            f"<item><title>{html.escape(e['title'])}</title>"
            f"<enclosure url='{e['mp3_url']}' length='{e['size']}' type='audio/mpeg'/>"
            f"<pubDate>{e['date']}</pubDate>"
            f"<guid>{e['mp3_url']}</guid></item>"
        )
    rss = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        "<rss version='2.0'><channel>"
        "<title>Ollin Cyber &amp; AI Digest</title>"
        f"<link>{BASE_URL}</link><description>Paivittainen luokiteltu kyberturvallisuus- ja tekalyuutisagentti</description>"
        f"<lastBuildDate>{now}</lastBuildDate>"
        + "".join(items)
        + "</channel></rss>"
    )
    RSS_FILE.write_text(rss)


def recent_episodes() -> list:
    entries = []
    for mp3 in sorted(AUDIO_DIR.glob("*.mp3"), reverse=True)[:30]:
        date_str = mp3.stem  # YYYY-MM-DD
        entries.append({
            "title": f"Cyber & AI Digest {date_str}",
            "date": datetime.datetime.strptime(date_str, "%Y-%m-%d")
                            .strftime("%a, %d %b %Y 07:30:00 GMT"),
            "mp3_url": f"{BASE_URL}/audio/{mp3.name}",
            "size": mp3.stat().st_size,
        })
    return entries

def prune_old_audio(days: int = 30) -> None:
    """Poistaa MP3:t jotka vanhempia kuin `days` — podcast-RSS paivittyy automaattisesti."""
    raj = datetime.date.today() - datetime.timedelta(days=days)
    for mp3 in AUDIO_DIR.glob("*.mp3"):
        try:
            if datetime.date.fromisoformat(mp3.stem) < raj:
                mp3.unlink()
                print(f"[info] Poistettu vanha jakso: {mp3.name}")
        except ValueError:
            pass


# ----------------------------------------------------------------- pääajo
def main() -> None:
    for d in (BASE_DIR, AUDIO_DIR, TEXT_DIR):
        d.mkdir(parents=True, exist_ok=True)

    today = datetime.date.today().isoformat()
    mp3_path = AUDIO_DIR / f"{today}.mp3"
    md_path = TEXT_DIR / f"{today}.md"
    if mp3_path.exists():
        print(f"[info] {today} on jo tehty — ohitetaan.")
        return

    seen = load_seen()
    items, feed_stats, broken = fetch_news(seen)
    if not items:
        print("[info] Ei uusia uutisia.")
        update_sources_stats(feed_stats, broken, [])
        return
    print(f"[info] {len(items)} uutista noudettu.")

    script, markdown, used = make_digest(items)
    md_path.write_text(markdown)
    print(f"[ok] Tekstidigesti: {md_path}")

    text_to_mp3(script, mp3_path)
    print(f"[ok] Audio: {mp3_path} ({mp3_path.stat().st_size / 1024:.0f} kt)")

    save_seen(seen)
    update_sources_stats(feed_stats, broken, used)
    prune_old_audio(30)
    write_podcast_rss(recent_episodes())
    print(f"[ok] Podcast-RSS: {RSS_FILE}")


if __name__ == "__main__":
    main()
