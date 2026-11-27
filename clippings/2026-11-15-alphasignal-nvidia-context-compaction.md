# 2026-11-15 — AlphaSignal

- **Kategoria:** ai_news
- **Tunnisteet:** context-compaction, long-context, inference-throughput, agent-economy
- **Lähde:** AlphaSignal (news@alphasignal.ai), 2026-11-15
- **Gmail-aihe:** "🧠 Nvidia Shows How to Cut AI Context Without Sacrificing Accuracy"

## Keskeiset uutiset

1. **Nvidian tutkimus: AI-agentit eivt aina tarvitse pitki konteksteja.** Kontekstin pienentminen 256 000:sta 16 000 tokeniin nosti lhtputaan lpi 3,6x (GLM 5.2), 5,6x (Kimi K2.6) ja 7x (Qwen 3 Coder Next) H100-GPU:illa.
2. **Kaksi tehtvtyyppi erilleen: long-horizon (agentti kerrytt komentoja ja ptksi monivaiheisessa tyss) ja long-input (iso lhdeaineisto yhten tehtvn).** Testit 13 benchmarkilla (SWE-bench Verified, Terminal-Bench, LongBench v2, LOONG) Opus 4.5:ll ja GPT-5.6 Solilla.
3. **Kompaktiointi (historian tiivistys kynnysarvon yltyess) silytt tarkkuuden useimmissa tehtvis** - vhenn "huomioveroa": jokainen tokeni vaatii huomiota kaikkiin edeltjiin, joten pitk konteksti on kallista.
4. **Kehittjnsuositus: pid kontekstissa vain vhimmtieto, jonka agentti tarvitsee seuraavaan askeleeseen,** eik kaikkea historiaa - jopa 7x nopeampi lpiutus ilman tarkkuuden menetyst.
