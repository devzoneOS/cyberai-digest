# aspnet-rce-kepco-turnitin

- **Päivämäärä:** 2026-11-25
- **Lähde:** TLDR (dan@tldrnewsletter.com)
- **Gmail-aihe:** "OpenAI & Cisco Shirudo 🛡️, ASP.NET RCE exploited 🚨, Inception claims 7 firms 🕵️"
- **Kategoria:** vulnerabilities
- **Tunnisteet:** aspnet, idunno-anticsrf, rce, kepco, turnitin, cset, vastuunjako, agentit

## Keskeiset uutiset

- **ASP.NET anti-CSRF-kirjaston RCE:tä hyödynnetään.** CVE-2026-131914 (CVSS 9.3) on tunnistautumaton RCE vuonna 2008 hylätyssä Idunno.AntiCsrf-kirjastossa: yksi Base64-koodattu POST ajaa gadget-ketjun w3wp.exe-prosessina. Korjausta ei tule, joten kirjasto pitää korvata ja avaimet kierrättää.

- **KEPCO:n tietomurto koskee 1,5 miljoonaa.** Eteläkorealaisen sähköyhtiön asiakasportaali ja hankintajärjestelmä vuodattivat yli 650 000 asiakkaan nimet, pankki- ja korttitiedot sekä 869 761 hankintatietuetta.

- **Turnitin ilmoitti kyberhyökkäyksestä.** Yli 16 000 oppilaitoksen ja 71 miljoonan opiskelijan palvelussa havaittiin luvatonta toimintaa asiakasjärjestelmissä. Vaikutuspiiriä ei ole kerrottu, ja oppilaitosten kannattaa varoa Turnitin-huijauksia ja tarkistaa SSO- ja LMS-lokit.

- **Kyberapokalypsin data ei tue otsikoita.** CSET:n analyysi osoittaa, että vaikka tekniset indikaattorit suosivat hyökkääjiä, merkittävien tapausten määrä, tietomurtojen kustannukset ja lunnaat ovat tasaisia tai laskussa. Pelko attributionista voi rajoittaa kansallisvaltioita enemmän kuin tekninen kyvykkyys.

- **Agentit luovat vastuunjakoaukon.** MCP-spesifikaatio ja harnesstit siirtävät arkaluontoisten toimien vastuun ja auditointilokit käyttäjälle. Microsoftin agenttitunnus-dokumentaatiokin palauttaa vastuun asiakkaalle, joten organisaatiot eivät voi delegoida vastuuta eteenpäin.
