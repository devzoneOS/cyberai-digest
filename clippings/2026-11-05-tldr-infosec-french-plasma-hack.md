# 2026-11-05 — TLDR Information Security

- **Kategoria:** cyber_news
- **Tunnisteet:** ot-security, healthcare, ai-infra, supply-chain, vulnerabilities
- **Lähde:** TLDR Information Security (dan@tldrnewsletter.com), 2026-11-05
- **Gmail-aihe:** "French plasma hack 🩸, OpenEMR 40+ flaws 🏥, White House residential proxies 🏛️"

## Keskeiset uutiset

1. **Hyökkääjät murtautuivat Ranskan veriplasmalaitoksen kylmähuoneiden toimitusketjuun ja muuttivat lämpötiloja -30 °C:sta 110 °C:seen.** EFS:n valvonta havaitsi muutokset eikä verituotteita menetetty; CERT-FR oli aiemmin kehottanut korjaamaan Danfoss-ohjainten haavoittuvuudet.
2. **Kiinankielinen Greeter-kehys hyödyntää Flowisen CVE-2024-58351-injektiota seitsemässä honey potissa.** Kehys tekee isäntätiedustelun, etsii .env- ja SSH-avaimia, kokeilee pilvimetadatapalveluita ja Docker-socketia; 703 alttiista 3 277 Flowise-instanssista puuttui autentikointi.
3. **OpenEMR:stä löytyi 42 tietoturvalistaa, korjattu versiossa 8.5.0 (27.10.2026).** Kolme kriittistä: PDF-generaattorin tiedostovuoto, SQL-injektio potilasdatan kentissä ja OAuth-todennuksen ohittava impersonaatio; ohjelmisto palvelee yli 100 miljoonaa potilasta.
4. **Tavanomaiset maine/listat ylipääsevät 70–90 % ohjelmistotoimitusketjuhyökkäyksistä julkaisupäivänä**, jolloin organisaatiot ovat alttiita kuukausia.
5. **Filippiinien siirtotyöläisdata vuoti 69 GB:n tietomurrossa.** Hyökkääjä kopioi 27 SQL Server -varmuuskopiota 24 minuutissa GodPotato/Impacket-työkaluilla ja jätti työkalut auki olevaan Singaporeen staging-palvelimelle.
