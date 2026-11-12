---
pvm: 2026-11-09
kategoria: ai_news
tunnisteet: [anthropic, muisti, klaviyo, duckdb, pinterest, sql]
lahde: TLDR Data
gmail-aihe: "Anthropic’s Agent Memory 🧠, How Klaviyo Scaled Analytics 🤖, Apache Spark 4.3.0 ⚡"
---

1. **Agentin muistin komponentit ja "unelmointi":** Lance Martin kuvailee, miten Claude reflektoi aiempia istuntoja korjatakseen muistissaan olevia virheitä ja rakentaakseen uusia. Unelmoinnin skaalautuessa 2:sta 128 istuntoon ~350 000 Stainless-tiedoston yli 25 kysymyksen pisteet nousivat 13 %:sta 48 %:iin, ja yhdistelmäkysymyksissä wiki voitti pelkän haun 87 %–73 %.

2. **Klaviyo skaalasi analytiikan pois kapeikosta:** Neljän henkilön kokeilusta kasvatettu KBI-järjestelmä yhdistää yli 100 dbt-semanttista mittaria, kuratoidun 90 taulun ympäristön ja luotetut SQL-tarkistukset yhteisen agenttirajapinnan taakse. Suurin osa varastokyselyistä tulee nyt agenteilta ilman analyytikkojen kyselypyyntöjä, ja määritelmät pysyvät yhtenäisinä.

3. **Pinterestin moniepookkikoulutus:** Useiden epookkien koulutus heikensi Homefeed-lajittelua lähes 6 %:lla. Embedding-optimoinnin eriyttäminen mallista, ensimmäisen epookin jäädyttäminen ja myöhäinen sopeutus käänsivät tilanteen (+1,09 % online-tallennuksia) ja pienensivät GPU-joutoaikaa hajautetussa koulutuksessa.

4. **DataGrip + DuckDB tietokantojen välisiin kyselyihin:** JetBrains valitsi DuckDB:n Apache Calciten sijaan, koska se oli helpoin integroida: mukautetut taulufunktiot yhdistävät PostgreSQL-, MySQL- ja MongoDB-datan yhteen kyselyyn DataGripin olemassa olevan suorituksen kautta.

5. **Hyvä SQL ei ole turvallista SQL:ää:** Tarkka text-to-SQL voi paljastaa luvatonta dataa, jos kyselyt ohittavat bisneskontekstin ja pääsypolitiikat. 900 kyselyn synteesibenchmarkissa politiikkatietoinen validointi soveltaa rivisuodattimia ja sarakemaskkeja ennen suoritusta.
