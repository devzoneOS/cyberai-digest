# 2026-11-13 — TLDR InfoSec

- **Kategoria:** vulnerabilities
- **Tunnisteet:** apache, http/2, rce, cve-2026-119618, github, supply-chain
- **Lähde:** TLDR Newsletter (dan@tldrnewsletter.com)
- **Gmail-aihe:** Apache HTTP/2 flaw, Linux 59 AI kernel bugs, Maersk $5M extortion

## Keskeiset uutiset

1. Apache HTTP Serverin mod_http2-moduulissa on kriittinen muistivika (CVE-2026-119618, CVSS 9.8), joka mahdollistaa kirjautumattoman etähyökkääjän ottavan palvelinprosessin haltuun versioissa 2.4.55-2.4.70, kun HTTP/2 on käytössä. Korjaus on päivitys versioon 2.4.71 tai HTTP/2:n poistaminen käytöstä.

2. WFX-Loot-kampanja levitti CI-salasanoja varastavaa haittaohjelmaa kymmenientuhansiin GitHub-repositorioihin: 4 837 vaarantuneen tilin kautta avattiin yli 61 000 koepyyntöä ja vähintään 1 835 repositoriota suoritti hyökkäyspayloadin. Haittaohjelma varastaa muun muassa GitHub Actions -salaisuudet, pilviroolit ja tekoälypalveluiden tokenit.

3. Baker Tilly ilmoitti asiakkailleen kolmannen osapuolen palveluntarjoajan tietomurrosta. Varastettuihin tietoihin kuuluu kokonaisia nimiä, Yhdysvaltain sosiaaliturvatunnuksia ja osoitteita.

4. Unit 42 varoittaa ARTEX- ja CyberStrikeAI-työkaluista: tekoälyllä toimivat punaisen tiimin agentit muuttivat julkisia salasananpalautussivuja ja paljastuneita OpenAPI-määrittelyjä pilvipääsyiksi, ja yli 200 asiakassalaisuutta validoitiin noin kolmessa minuutissa. Verkossa on yli 600 ARTEX-isäntää.

5. Katsauksessa käsitellään lisäksi 59 uutta tekoälyyn liittyvää Linux-kernel-vikaa sekä Maerskin 5 miljoonan dollarin kiristystapausta.
