# 2026-11-16 — TLDR Information Security

- **Kategoria:** vulnerabilities
- **Tunnisteet:** windows-zero-day, cloud-pentesting-attack, data-leak, crypto-heist
- **Lähde:** TLDR Information Security (dan@tldrnewsletter.com), 2026-11-16
- **Gmail-aihe:** "Disgruntled Researchers Drop Windows 0-Day 🪟, Google's New Disclosure Policy 🤐, Cyber Chaos Monkey 🐒"

## Keskeiset uutiset

1. **SignDrop (Windows 0-day, tysytetty turhautuneen tutkijan toimesta): tavallinen kytt saa System-oikeudet.** Ketju hyvksikytt CLFS-jrjestelm, Windows Defenderi, symbolisia linkkej ja tiedostooikeuksia: Defender avaa kyttjn luoman CLFS-kontin, jonka jlkeen CLFS luo puuttuvan autentikointitiedoston Defenderin System-oikeuksilla. Toimii Windows 11 26H2:ssa ja Server 2025 Experimental -asetuksissa CLFS-autentikointitilalla 0 tai 1, ja ohittaa murheellisesti virustorjunnan suojaukset.
2. **AntiFox (avoin autonomisen pentestaamisen alusta) on nyt hykkyskalu:** Arctic Wolf yhdist sen IIS-murtoihin, joissa asennettiin ASPX-webshellej ja varastettiin konfiguraatiot, tietokannan tunnukset ja AWS-tunnukset; osa pssi tuotannon Secrets Manageriin ja S3:een. Vastatoimet: least privilege, IMDSv2, pitkaikaisten avainten poisto, GuardDuty.
3. **TSMC:n tyntekijdata vuoti pilvipalvelutoimittajan jrjestelmist:** 6,9 Gt dataa huutokaupassa, ml. kansalliset ID-numerot, osoitteet ja pankkitiedot; TSMC:n omat jrjestelmt eivt vaarantuneet.
4. **Binance-murron anatomia (osat I-II): yksi transaktio, jossa 50 EIP-7702-valtuutusta, ja yksi nonce-osui:** hot-lompakko ajoi hykkjn sweeper-sopimusta omana koodinaan 3 h 49 min, ja se tyhjennettiin seitsemn kertaa automaattisten tysydennysten jatkuessa.
