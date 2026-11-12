---
pvm: 2026-11-12
kategoria: ai_news
tunnisteet: [anthropic, postgres, netflix, parquet, iceberg, mcp]
lahde: TLDR Data
gmail-aihe: "Claude Data Goes GA 📊, Why Clouds Bet on Postgres 🐘, Netflix Fact Checking Pipeline 🎥"
---

1. **Netflix automatisoi faktantarkistuksen:** Netflixin uusi factuality-palvelu tarkistaa sarjojen synopsisten faktavirheet automaattisesti: kustannus per synopsis laski 52,4 % ja ei-faktaalisten synopsisten recall nousi 0,77:sta 0,86:een. Selitysten päällekkäisyys ihmisten annotaattorien kanssa on nyt noin 82 %.

2. **Pilvet panostavat Postgresiin AI-sovelluksissa:** Databricks osti Neonin noin miljardilla dollarilla ja Snowflake Crunchy Datan 165 miljoonalla, ja Google, Amazon ja Microsoft ovat laajentaneet Postgres-palveluitaan. Viisi eri strategiaa valitsi saman tietokannan — artikkeli selittää, mitä laajennukset mahdollistavat ja mitä kysyä ennen sitoutumista.

3. **Parquetin modulaarinen footer-uudistus:** Ehdotus korvaa monoliittiset Thrift-footerit itsenäisesti luettavilla metadatamoduuleilla: sarakkeiden palat muuttuvat jatkuviksi sivujaksoiksi, row-group-metadatasta tulee valinnaista ja tilastot voivat kuvata mielivaltaisia rivivälejä. Lukijat voisivat hakea vain relevanttien sarakkeiden metadataa, mikä vähentäisi suunnittelun ylikuormaa leveillä tauluilla.

4. **Iceberg v4:n stats-kentät:** Uusi versio tallentaa metadataa johdetuille lausekkeille (esim. osiobucketit, kirjainkoon normalisoidut merkkijonot) ilman fyysisten sarakkeiden materialisointia, mikä mahdollistaa lauseketietoisen tiedostojen karsinnan ja jopa metadata-only-laskennan ilman datatiedostojen lukua.

5. **MCP raakadatasta luo "Excel-helvetin" uudelleen:** Agenttien suora kytkeminen operatiivisiin järjestelmiin ilman hallittuja liiketoimintasääntöjä tuottaa ristiriitaisia mittareita. Luotettavampi arkkitehtuuri erottaa ontologian (liiketoiminnan intentio) ja tarkkuuskerroksen (testatut laskennat), pitäen varaston totuuden lähteenä.
