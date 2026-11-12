---
pvm: 2026-11-12
kategoria: ai_news
tunnisteet: [gemini, github-actions, nextjs, evaluaatio, ohjelmistokehitys, suorituskyky]
lahde: TLDR Dev
gmail-aihe: "Gemini Decision Model ⚡️, lock your GitHub Actions 🔒, Dropbox side projects 🎨"
---

1. **Next.js-muistivuoto 5 GBsta 1,2 GB:iin:** Zepton podit pysyivät ~5 GB:ssa, koska react-query v3 käynnistää jokaiselle palvelimella renderöidylle querylle minuuttien mittaisen ajastimen, ja Node sitoo ajastimen pyynnön AsyncLocalStorage-kontekstiin pitäen valmiit pyynnöt muistissa. Palvelinpuolen queryille riittämätön (ääretön) cache time pysäytti ajastimet ja pudotti muistinkäytön ~1,2 GB:iin — sama ansa pätee v5:llä explicit gcTimella.

2. **Eval-driven development agenttien parantamiseen:** LangChain ehdottaa testivetoinen silmukkaa AI-agenttien kehitykseen: kirjoita läpäisy/hylkäys-määrittely yhdelle käyttäytymiselle ennen muutosta, aja vertailu esimerkeittäin, pidä holdout-joukko ylisovituksen varalta ja aja evaluaatiot CI:ssä ja tuotantoliikenteessä.

3. **Lukitse GitHub Actionsisi:** Actions-lukkotiedostot pitävät luettavat versiotunnisteet mutta tallentavat tarkat commitit, joihin ne ratkeavat. Käytännön opas kattaa lukkotiedoston generoinnin, päivityksen Renovate/Dependabotilla ja varmistuksen CI:ssä, jottei workflow hiljalleen lipsu pineistä.

4. **Gemini Decision 1:** Uusi malli arvioi rajattuja valintoja teksti-generoinnin sijaan ja käy läpi jopa 1 000 kysymystä kerralla tekstin, kuvien, äänen, videon ja PDF-aineiston pohjalta. Latenssi on 150–250 ms ja hinta $0,10 per miljoona syöte-tokenia ilman lähtötokenimaksuja; kohde käyttötapauksia ovat mallireititys, politiikkatarkistukset ja rubriikkiarviointi.
