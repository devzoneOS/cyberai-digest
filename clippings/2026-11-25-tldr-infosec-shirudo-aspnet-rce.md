# 2026-11-25 — TLDR InfoSec

- **Kategoria:** vulnerabilities
- **Tunnisteet:** openai, cisco, shirudo, ebpf, aspnet, rce, cve-2026-131914, kepco, turnitin
- **Lähde:** TLDR Newsletter (dan@tldrnewsletter.com)
- **Gmail-aihe:** OpenAI & Cisco Shirudo, ASP.NET RCE exploited, Inception claims 7 firms

## Keskeiset uutiset

1. OpenAI ja Cisco julkaisivat Shirudon, avoimen lähdekoodin eBPF-ajoympäristön, joka ottaa käyttöön väliaikaisia suojakuoria haavoittuvan koodipolun estämiseksi ajossa olevassa prosessissa ilman uudelleenkäynnistystä.

2. Hyökkääjät hyödyntävät kriittistä turvatonta deserialisointivikaa Idunno.AntiCsrf-kirjastossa, vuonna 2008 hylätyssä ASP.NET WebForms-kirjastossa: yksi kirjautumaton POST-pyyntö Base64-koodatulla ObjectStateFormatter-gadgetiketjulla saavuttaa RCE-oikeudet w3wp.exe-prosessina (CVE-2026-131914, CVSS 9.3). Mandiant vahvisti hyödyntämisen tuotannossa, eikä paikkaa ole tulossa. Puolustajien tulee etsiä Web.config-tiedostoista ja bin-hakemistoista AntiCsrfModule-viittauksia, korvata kirjasto System.Web.Helpers.AntiForgery- tai ASP.NET Core IAntiforgery-kirjastolla ja kiertää machineKey-avaimet.

3. Eteläkorealainen sähköyhtiö KEPCO kertoi ulkoisen hyökkääjän imeneen dataa KEPCO ON -asiakasportaalin ja toimittajahallintajärjestelmän kautta. Kaikkiaan 1,5 miljoonaa tietuetta paljastui: 650 487 asiakastietuetta, jotka sisältävät nimiä, tunnisteita, pankkitietoja ja laskutustietoja, sekä 869 761 toimittaja- ja työntekijätietuetta.

4. Turnitin paljasti kyberhyökkäyksen asiakasjärjestelmiin. Yli 16 000 oppilaitoksen ja 71 miljoonan opiskelijan palvelussa havaittiin luvatonta toimintaa, mutta yritys ei ole kertonut hyökkäystapaa, ajankohtaa tai datan varastamista. Oppilaitosten kannattaa varautua Turnitin-huijauksiin ja tarkistaa SSO- ja LMS-lokit.

5. CSETin Andrew Lohn muistuttaa arvioimaan kyberuhkia datan eikä otsikoiden perusteella: kuukausittainen CVE-määrä on kolminkertaistunut, korjausajat pitenevät ja hyödyntäminen on nopeutunut, mutta kokonaiskuva on monimutkaisempi.
