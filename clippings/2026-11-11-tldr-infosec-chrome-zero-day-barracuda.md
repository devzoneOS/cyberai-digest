---
pvm: 2026-11-11
kategoria: vulnerabilities
tunnisteet: [chrome, zero-day, barracuda, n-able, turla, aws]
lahde: TLDR Information Security
gmail-aihe: "Chrome zero-day patch 🌐, Barracuda ESG flaws 🔓, Google's AlphaProof Code 🤖"
---

1. **Google paikkasi vuoden kahdeksannen Chrome zero-dayn:** Hätäpäivitys korjaa aktiivisesti hyväksytyn haavoittuvuuden, joka johtuu use-after-free -viasta selaimen XML-jäsennyksessä ja mahdollistaa mielivaltaisen koodin suorittamisen.

2. **Barracuda ESG -aukot juurikäyttöön asti:** Viime viikolla paikattuja Email Security Gateway -haavoittuvuuksia hyödynnetään aktiivisesti: ensimmäinen mahdollistaa globaalin konfiguraation muokkaamisen valtuutusheikkoudella, toinen antaa autentikoitumattomalle hyökkääjälle root-oikeuksin ajettavia käyttöjärjestelmäkomentoja. Barracuda kehottaa pitämään hallintakonsolin poissa julkisesta internetistä.

3. **N-able sammutti N-central Cloudin 33 zero-dayn jälkeen:** Tutkija Sean Bales julkaisi 33 haavoittuvuutta (Able2Shell) proof-of-concept-hyökkäyksineen: tunnusten varastamista, tiedostokirjoituksia, XXE, XSS ja root-tason RCE. N-able ei ole havainnut aktiivista hyväksikäyttöä, mutta watchTowr näki honeypotteihin kohdistuneita yrityksiä.

4. **Turlan Cereal-kalusto kaappaa Exchange-palvelimet:** Passiivinen takaovi odottaa salattuja komentoja tavallisista OWA-, Autodiscover- ja ActiveSync-poluista, ja EdgeTransportiin injektoitu moduuli kopioi NATO- ja EU-osoitteita koskevat viestit. ESET löysi kaluston Kazakstanin ja Romanian viranomaisilta ja attribuoi sen Turlalle suurella varmuudella.

5. **Qubolen AWS-tunnukset väärinkäytössä:** Hyökkääjä käytti Qubolen AWS-tilin IAM-tunnuksia asiakkaiden integraatioroolien kautta, luki Lambda-ympäristömuuttujia, Secrets Manager -arvoja ja SSM-parametreja sekä latasi S3-objekteja. Suojaukseksi kannattaa poistaa käyttämättömät toimittajaroolit ja sitoa trust-politiikat aws:SourceIp-ehdolla.
