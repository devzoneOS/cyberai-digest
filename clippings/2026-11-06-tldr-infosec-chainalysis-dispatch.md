---
pvm: 2026-11-06
kategoria: cyber_news
tunnisteet: [chainalysis, anthropic, claude-dispatch, rce, venaja, firecracker, sharepoint]
lahde: TLDR Information Security
gmail-aihe: "Chainalysis data leak ⛓️ , Claude Dispatch RCE 🤖 , Apple to scan iCloud content 🍎"
---

1. **Anthropic ei korjaa Claude Dispatch -aukkoa:** Selainlaajennus, jolla on claude.ai-oikeudet, voi lähettää Dispatchilla kehotteita Claude Desktopille ja saavuttaa etäkoodin suorituksen hyödyntäen jaettuja web- ja työpöytäistuntoja, toistuvia hyväksyntäklikkauksia ja haitallista npm-pakettia. Hyökkäys ulottuu henkilökohtaisesta selainistunnosta työkoneelle. Anthropic on tiennyt ongelmasta toukokuusta, mutta Dispatch on yhä olemassa olevien käyttäjien käytettävissä.

2. **Venäjään liitetty mobiilikampanja iOS:ään ja Androidiin:** Hyökkääjät käyttivät watering hole -sivustoja, proxy-domaineja ja kaapatua ukrainalaista analytiikkapalvelua Javascriptin ruiskeeseen, joka profiloi kävijät ja toimitti zero-click-hyökkäysketjuja vanhentuneisiin laitteisiin (mm. DarkSword). Kohteena evästeet, Wi-Fi-salasanat ja koko laitedata; kohteina mm. US:n ja UK:n diplomaattipiireihin liittyvät sivustot.

3. **Chainalysisin tietomurto kaikkien käyttäjien osalta:** Blockchain-analytiikkayhtiö varoitti, että kaikki käyttäjätiedot ovat saattaneet vaarantua "aggressiivisia agenttitekniikoita" käyttäneen hyökkääjän toimesta. Varastettuun aineistoon kuuluvat nimet, käyttäjänimet, salasanahajautumat ja live-tokenit; KYT-transaction-monitorointipalvelu otettiin väliaikaisesti offline-tilaan.

4. **Firecracker-hiekkalaatikkopako:** Coinspect demonstroi CVE-2026-122192:n, jolla vieras voi lukea ja muokata elävää Firecracker VMM-muistia ja saada koodin suorituksen isäntäprosessissa. Toinen aukko (FC-03) salli io_uringin kautta isäntätoimintoja, jotka seccomp esti. Versiot v0.23.0–v1.16.1 ovat haavoittuvia, v1.16.2 ja v1.17.0 korjaavat pakon.

5. **Storm-2603:n fileless SharePoint-murto:** Hyökkääjä skannasi ToolShell-haavoittuvuuden (CVE-2025-53770), latasi jouluaattona webshellin suoraan IIS:n w3wp.exe-muistiin, tunneli sisäverkkoon suo5:llä, eskaloi SYSTEMiin EfsPotatolla ja yritti lopulta kiristyshyökkäystä. Puolustajien kannattaa metsästää IIS-polkuja, jotka resolveutuvat konfiguraatiossa mutta joita ei ole levyllä.
