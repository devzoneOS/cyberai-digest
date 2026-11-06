# 2026-11-02 — TLDR Data

- **Kategoria:** ai_news
- **Tunnisteet:** ai-evals, data-engineering, databases, duckdb, postgres
- **Lähde:** TLDR Data (dan@tldrnewsletter.com), 2026-11-02
- **Gmail-aihe:** "PostHog's AI Evals 🧪, Polars vs DuckDB 🏁, Jepsen Finds Issues in ParticleDB 💥"

## Keskeiset uutiset

1. **PostHog arvioi agentteja oikeilla tehtävillä:** katselmointiagentti löysi 62 % 33 menneen tuotantohäiriön bugien syistä; testit eristetään, etteivät agentit voi kopioida aiempia vastauksia.
2. **Polars 2.1 voitti DuckDB 2.0:n 23 GB:n aineistolla 2 GB muistilla: 438 s vs 837 s.** DuckDB tuo client-server- ja AI-ominaisuuksia, Polars keskittyy suurempiin-than-memory-virtaukseen.
3. **Jepsen löysi ParticleDB 1.1.4:stä 96 virhettä**, mukaan lukien datan menetyksiä ja virheellisiä SQL-tuloksia ilman palvelinvikoja; vakavia transaktiobugeja jäi mukaan myös korjausten jälkeen.
4. **Looginen replikatio mahdollistaa PostgreSQL:n päivitykset tai migraatiot sekuntien mittaisella seisokilla** rinnakkaisen klusterin ja cut-overin avulla, mikä tuo rullausturvallisuuden, jonka in-place-päivitykset ei tarjoa.
