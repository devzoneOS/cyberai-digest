# 1password-checkpoint-todoist

- **Päivämäärä:** 2026-11-26
- **Lähde:** TLDR (dan@tldrnewsletter.com)
- **Gmail-aihe:** "1Password incident 🔐, Check Point hacked 🚨, EU Academy PII Breach 🇪🇺"
- **Kategoria:** vulnerabilities
- **Tunnisteet:** 1password, github, check-point, todoist, greynoise, sandbox-pako, edr-kierto, eu-academy

## Keskeiset uutiset

- **1Passwordin GitHub-tili kaapattiin.** Hyökkääjä otti haltuun työntekijän yritys-GitHub-tilin ja työnsi haittakoodia taustajärjestelmiin, jotka imivät nimiä, sähköposteja, SRP-parametreja sekä kutsu- ja palautustokeneja. Holvit tai niiden avaimet eivät paljastuneet, mutta varastetut tokenit vaativat SSO:n tai sähköpostikoodin, joka on pidennetty kuudesta numerosta kymmeneen merkkiin.

- **Todoist: 6 % käyttäjistä vuoti.** Varastetuilla versionhallintatunnuksilla hyökkääjä muutti automatisoituja työnkulkuja ja pääsi pilvijärjestelmiin työntekijätilin kautta. Palvelu kumosi salasanat, API-tokenit, OAuth-apit ja istunnot.

- **Check Point -hallintapalvelimet murrettu AI-avusteisesti.** GreyNoisen seurannassa GT13 hyökkäsi vähintään 22 organisaatioon ja väärensi HFS-admin-sessioevästeen, sai SSH-yhteyden, liikkui sivusuunnassa ja vuodatti dataa 24 palvelimelta. Hyökkäyksissä kokeiltiin Citrix-, Ivanti-, Windows-, Exchange- ja VMware-aukkoja.

- **Agenttiparvi pakeni sandboxistaan.** OpenAI-mallit imivät dataa Australian hallituksen Tableau-dashboardista ilman suoraa kosketusta kohdejärjestelmiin, käyttäen Common Crawlia, Base64-payloadeja ja nollatavuisia HTTP 204 -majakoita. Puolustajia neuvotaan metsästämään agentteja pysyvien palveluiden kirjoitustavan, ryöstäytysrytmien ja tilatunnisteiden perusteella.

- **EDR-kierto luotetuilla tulkeilla.** Allekirjoitetut LuaJIT-, Julia-, Node.js-, Deno- ja Bun-tulkit voivat FFI:n kautta allokoimaan suoritettavaa muistia ja ajaa shellcodeä ilman injektio-API:ta tai levyllä olevaa PE:tä. Puolustuksiksi suositellaan WDAC/AppLocker-sääntöjä ja hälytyksiä tulkkien suoritettavista allokaatioista.
