# TLDR Dev 12.11.2026 — Gemini Decision, GitHub Actions -lukitus, Dropbox-agentti

- **Päivämäärä:** 2026-11-12
- **Kategoria:** ai_security
- **Tunnisteet:** github-actions, toimitusketjuturvallisuus, gemini, ai-api:t, agentit, nextjs, eval
- **Gmail-aihe:** Gemini Decision Model ⚡️, lock your GitHub Actions 🔒, Dropbox side projects 🎨

## Keskeiset uutiset

1. **GitHub Actions -työnkulut kannattaa lukita lockfile-tiedostolla.** Lockfile säilyttää luettavat versiotagit mutta tallentaa tarkat commit-pinnit, joita workflow ei voi hiljaisesti ajautua ohi. Lockfile päivitetään Renovatella tai Dependabotilla ja varmistetaan CI:ssä — keskeinen toimitusketjuturvallisuuden parannus.

2. **Googlen Gemini Decision 1 ja Decisions API pisteyttävät valintoja tekstiä generoimatta.** Malli arvioi jopa 1 000 kyllä/ei- tai rubriikkikysymystä yhdellä läpikäynnillä tekstiä, kuvia, ääntä ja PDF:ää vasten, latenssi 150–250 ms ja hinta 0,10 $ / miljoona input-tokenia. Kohdekäyttötapauksia ovat mallireititys, politiikkatarkistukset ja automatisoitu arviointi.

3. **Zepto korjasi Next.js-muistivuodon 5 gigatavusta 1,2:een.** Syynä oli react-query:n palvelinpuolen ajastin, joka sitoi jokaisen SSR-requestin AsyncLocalStorage-kontekstiin pysyvästi. Ratkaisuna palvelinpuolen kyselyihin asetettiin ääretön cache-aika; sama ansa pätee vielä v5-versiossa.

4. **Eval-driven development tuo testivetoisen silmukan AI-agenttien kehitykseen.** LangChain kehittää kirjoittamaan pass/fail-spesifikaation ennen muutosta, rakentamaan datasetin ja evaluaattorin ensin ja vertaamaan kokeita yksitellen — keskiarvon nousu voi piilottaa regressioita. Evaluaattorit kuuluvat myös CI:hin ja tuotantoliikenteeseen.

5. **Dropboxin agentti syntyi kahdesta insinöörin sivuprojektista.** Jokainen keskustelu ajetaan tuoreessa virtuaalikoneessa millisekunneissa, tunnukset ja käyttöoikeudet pidetään agentin ulottumattomissa, ja jokainen tiedostomuutos kytketään keskusteluun — käyttäjä voi perua vain yhden agentin muutokset.

6. **Chromen Modern Web Guidance 1.0 syöttää koodausagenteille web-osaamista.** Skill-pakki antaa agenteille asiantuntijoiden tarkistamaa ohjeistusta ja Baseline-yhteensopivuusdataa (saavutettavuus, suorituskyky, turvallisuus); Firefox ja Edge ovat mukana ylläpitäjinä.

7. **AWS Emulator ajaa AWS API:ita paikallisesti.** Koodausagentit saavat paikallisen AWS-kopion testattavaksi ilman tiliä tai kuluja — avoin lähdekoodi.
