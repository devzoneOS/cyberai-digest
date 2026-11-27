# 2026-11-26 — TLDR Dev

- **Kategoria:** ai_news
- **Tunnisteet:** hugging-face, swarm, deepseek, anthropic, rust, redis, kafka
- **Lähde:** TLDR Newsletter (dan@tldrnewsletter.com)
- **Gmail-aihe:** Scaling agent swarms, Anthropic's Rust migration, Search for Agents

## Keskeiset uutiset

1. Hugging Face kasvatti agenttiparven 1 000 DeepSeek-agenttiin yhdeksässä päivässä rakentaakseen PyBotin, puhtaan Python-keskustelubottiprogram, joka ylsi SmolLM-360M:n tasolle arkikeskustelussa. Ajo tuotti 175 000 viestiä ja yli 8 500 yhdistettyä vetopyyntöä ja paljasti pullonkauloin päättelyssä, työkalukutsuissa ja Gitissä.

2. Anthropic varjosti liikennettä varmistaakseen, että sen Rustilla kirjoitettu Messages API vastasi Python-versiota: sama mallitulo toistettiin molempien toteutusten läpi erojen eristämiseksi. Migraatio laski suorittimen käyttöä pyynnittä noin 70 prosenttia ja mediaaniaikaa ensimmäiseen tokeniin noin 20 prosenttia ilman katkoa.

3. Autumn korvasi Redis-write-behind-välimuistin järjestyksessä olevalla Kafka-lokilla ja yhdellä saldokirjoittajalla asiakasta kohti, kun Postgres kirjasi perässä erissä. P99-latenssi putosi 108 millisekunnista 25 millisekuntiin viikoittaisen tarkistusmäärän kasvaessa 28 prosenttia.

4. SISU: Jira-lippujen murskaaminen on temppu, ei vaikutuksen tie. Vaikutus syntyy prioriteettiprojekteista, näkyvistä incidenteistä ja tiimiläisten esteiden poistamisesta.

5. Tekoälylaboratoriot raportoivat tuloksia pitkäaikaisista matematiikan ongelmista, muun muassa matriisikertolaskun ja Fourier-muunnoksen ylä- ja alarajojen yhtämisestä.
