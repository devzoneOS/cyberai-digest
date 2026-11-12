---
pvm: 2026-11-09
kategoria: ai_security
tunnisteet: [uber, ai-agentit, tietoturva, x, web, css]
lahde: TLDR Dev
gmail-aihe: "X rebuilds its web app 🛠️, Uber secures AI agents 🔐, WebMCP in practice 🌐"
---

1. **Uberin agenttiturvallisuus käytännössä:** Uber suojaa agentteja provisiointitarkistuksilla, ajonaikaisella valvonnalla ja jatkuvalla testauksella, ja lisää perinteiseen auktorisointiin käyttäytymiskontrollit. Rajatut intentiot, istunnon konteksti ja promptin alkuperä kertovat, vastaako auktorisoitu toiminto käyttäjän pyyntöä; pienet erikoismallit ja rinnakkaiset tarkistukset pitävät latenssin hallinnassa.

2. **X rakensi web-sovelluksensa uudelleen:** Yksi palvelin ihmisiä, hakurobotteja ja linkkien esikatseluja varten korvaa kolme erillistä palvelinta. Hitaalla yhteydellä profiilin ensimmäinen postaus näkyy 2,7 sekunnissa yli 22 sekunnin sijaan, ja kirjautunut liikenne siirtyy vaiheittain maittain.

3. **Moderni CSS voi monimutkaistaa frontendiä:** Konttiqueryt ja :has() voivat helpottaa komponenttia mutta luoda piiloriippuvuuksia koko sovelluksessa. Migrointilista kattaa omistajuuden, laajuuden, kaskadin, siivouksen, mitatun suorituskyvyn ja ylläpidettävyyden.

4. **Agenttiorganisaatiot ilman uusia työkaluja:** Erityistäminen, delegointi, hallintakerrokset ja eskalointi tarjoavat lähtökohdan, mutta identiteetti, auktorisointi, kestävä tila ja inhimillinen vastuu on yhä ratkaistava.

5. **Koodausagentit tekivät sinusta managerin:** Tehokas yhteistyö agenttien kanssa nojaa selkeään kontekstiin, itsevarmennukseen, varhaiseen suunnan korjaukseen ja selkeisiin rajoihin; toistuvat korjaukset kannattaa muuttaa jaetuiksi ohjeiksi ja pitää ihmiset vastuussa tuotepäätöksistä, turvarajoista ja siitä, mitä julkaistaan.
