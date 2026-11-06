# 2026-11-05 — TLDR Data

- **Kategoria:** ai_news
- **Tunnisteet:** data-engineering, duckdb, trino, llm-classifiers, cost-optimization
- **Lähde:** TLDR Data (dan@tldrnewsletter.com), 2026-11-05
- **Gmail-aihe:** "PostHog moves off DuckDB 🚚, Airbnb's LLM classifiers 🎯, Less coding, more verification 🛂"

## Keskeiset uutiset

1. **PostHog siirtyy pois DuckDB:stä viiden kuukauden käytön jälkeen.** Jokainen instanssi piti kooltaan ennen kyselyn saapumista, ja biljoonan rivin DuckLakeen yksittäistaulukon kirjoitus saattoi kestää yli kolme minuuttia; uusi rakennus pohjautuu Trinoon ja omaan HogLake-muotoon.
2. **Airbnb hienosääti 2 miljardin tehokkaan parametrin mallin hinnoittelupoliittiklassifioijaksi.** F1 nousi 0,563:sta 0,902:een frontier-API:iden tasolla, ja mediaanlatenssi oli 35 ms vs noin 900 ms; itse isännöity GPU on kaksi kertalukua halvempi.
3. **Kun agentit kirjoittavat enemmän koodia, työt siirtyvät koodauksesta todentamiseen.** Tarvitaan kääntäjätyylisiä validointeja, kerroksellisia testisarjoja ja yhtenäinen lineage agenttien tuottaman analytiikan auditointiin.
4. **Meta F3 Lightning nopeuttaa mainos-ML-ominaisuuksien tuotantoon vientiä 3,6x** yli 20 000 ominaisuuden infrastruktuurissa vakaiden laskenta-ID:iden ja jaetun muistin avulla.
5. **Halodocin Redshift-migraatio RA3:sta Graviton-RG-instansseihin pudotti kustannuksia 32 %:** COPY-operaatiot nopeutuivat noin 6x ja jonotusajat laskivat 70 %.
