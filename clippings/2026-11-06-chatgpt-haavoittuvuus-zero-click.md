---
pvm: 2026-11-06
kategoria: vulnerability
tunnisteet: [chatgpt, openai, haavoittuvuus, zero-click, prompt-injection, lockdown-mode, check-point, sandbox]
lahde: Verkkouutiset 6.11.2026 (Ville Mäkilä)
liite: https://drive.google.com/file/d/1Iut2lgEiAUH12judP3X0OOQKfEYEaQ5AhsEMeCqpuC0/view
---

**ChatGPT:stä löytyi haavoittuvuus — keskustelutietoja voitiin vuotaa ilman käyttäjän klikkausta**

Verkkouutiset 6.11.2026. Check Point Research havaitsi ChatGPT:ssä
haavoittuvuuden, jolla hyökkääjä pystyi kiertämään Lockdown Mode
-suojauksen ja vuotamaan keskustelutietoja käyttäjän huomaamatta
(zero-click). Heikkous ei ollut tekoälymallissa vaan ChatGPT:n
HTML-sisältöä näyttävässä esikatselutoiminnossa: sandbox-ympäristön
pieni­­n rajoituksista pääsi yli ponnahdusikkunoiden käsittelyn kautta.
Vakavin osoitettu hyökkäystapa koski työpöytäsovellusta, jossa
haitallinen GPT lähetti keskustelun sisältöä hyökkääjän palvelimelle.
Samaa tekniikkaa olisi voitu käyttää huijausikkunoihin ja
haittaohjelmien levittämiseen. OpenAI poisti hyökkäyksen mahdollistaneet
sandbox-oikeudet 18.9.2026, ja Check Point vahvisti hyökkäystavan
kuiten enää toimivan.

Merkitys SecPromiselle: prompt injection ja tekoälykäyttöliittymien
kontrollin puute ovat nyt todistettuja tuotantohäiriöitä — asiakkaille
suositeltava: tekoälytyökalujen käyttöä koskevat rajoitukset ja
Lockdown-tyyppiset tilat eivät yksin riitä.
