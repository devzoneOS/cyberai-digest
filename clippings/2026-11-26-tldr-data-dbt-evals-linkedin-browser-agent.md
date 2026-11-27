# 2026-11-26 — TLDR Data

- **Kategoria:** ai_news
- **Tunnisteet:** dbt, evals, linkedin, browser-agent, grab, scarlet, postgres, uuidv7
- **Lähde:** TLDR Newsletter (dan@tldrnewsletter.com)
- **Gmail-aihe:** dbt Evals, LinkedIn Browser Agent, How Salesforce Does Context Engineering

## Keskeiset uutiset

1. dbt Evals on kehys, joka esittää analytics-agenteille samat kysymykset useissa ajokertoja ja tarkistaa vastaukset SQL-testeillä. Lähestymistapa tuo arvioinnin datatöihin samaan tapaan kuin yksikkötestit ohjelmistokehityksessä.

2. LinkedIn rakensi sisäisen tekoälyagentin, joka toimii työntekijöiden olemassa olevissa Chrome-istunnoissa ja muuntaa incident-ketjut lipuiksi sekä dokumentit dioiksi. Rakenne suunniteltu sivudata pienentää tokenkulutusta, ja agentti näyttää toimintansa ja todisteensa käyttäjän varmistettavaksi.

3. Grabin Scarlet-agentti muuntaa Slack-viestit ja Jira-liput dataputkimuutoksiksi, tarkistaa datan tuotantoon verraten ja avaa vetopyynnöt katselmointiin. Uudelleenkäytettävien tiimikohtaisten ohjeiden ja automaattisten datatarkistusten myötä yhdistettyjen vetopyyntöjen osuus nousi noin 50 prosentista toukokuussa yli 85 prosenttiin syyskuussa.

4. Reprosentointikelpoiset vertailut monialueisen PostgreSQL:n pääavainstrategioista: UUIDv7 on tehokas eikä vaadi koordinaatiota, alueelliset sekvenssit voivat törmätä vikasietokytkennän jälkeen, aikaleimoihin perustuvat tunnukset ovat haavoittuvia kellojen rullaamiselle ja yhdistelmäavaimet helpottavat replikoinnin suodatusta mutta kuluttavat tallennustilaa.

5. PostgreSQL-migraatiossa kymmenien miljardien rivien takaisintäyttö suoritettiin loogisen replikoinnin ollessa käynnissä rinnakkaisella COPY:lla, kiinteillä ID-alueilla ja palautettavilla tarkistuspisteillä.
