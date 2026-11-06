# 2026-10-30 — TLDR DevOps

- **Kategoria:** ai_news
- **Tunnisteet:** kubernetes, cloud, observability, postgres
- **Lähde:** TLDR DevOps (dan@tldrnewsletter.com), 2026-10-30
- **Gmail-aihe:** "Workload Conformance 🏋️, Supabase Compute 💽, 1M Durable Workflows 🌊"

## Keskeiset uutiset

1. **Kubernetes-yhteisö perusti Workload Conformance -työryhmän.** Tavoitteena on yhteinen spesifikaatio ja testit sille, miten työkuormat käyttäytyvät ajonaikaisesti; vakaan ensimmäisen spesifikaation arvioidaan valmistuvan 2–3 julkaisusyklin aikana.
2. **Supabase Compute saapui yksityisessä alfassa** agenttien, taustatöiden ja API:en ajamiseen suoraan käyttäjän datan vieressä; Dreambase raportoi kyselyviiveen pudonneen 65 ms:stä mediaanissa 2,9 ms:iin.
3. **DBOS skaalasi 20 000 kestävää workflow'ta sekunnissa yhdestä Postgres-palvelimesta miljoonaan 46:lla shardilla PgDogin avulla.** Suurin este oli kilpailutilanteen takaisinkytkentä, joka korjattiin advisory-lukoilla.
4. **Datadog julkaisi Infrastructure Basic -tason**, kevyen kerroksen, joka kerää ydinmetriikat ja prosessistatukset matalan prioriteetin työkuormille saman agentin rinnalle muiden tasojen kanssa.
5. **Yhden Argo CD -hubin hallinnoimat 34 klusteria ja 174 Helm-kaaviota** osoittavat GitOps-skaalautuvuuden: klusterikohtaiset sopimukset ja CI-manifestidiffit pudottivat onboarding-ajan neljästä päivästä 1,7 tuntiin.
