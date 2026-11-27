# 2026-11-27 — TLDR InfoSec

- **Kategoria:** cyber_news
- **Tunnisteet:** hex.pm, elixir, cve-2026-129514, north-korea, polinrider, bithumb, dns-takeover
- **Lähde:** TLDR Newsletter (dan@tldrnewsletter.com)
- **Gmail-aihe:** PolinRider hits 7.6K repos, Erlang Package Manager incident, Samsung Knox root chain

## Keskeiset uutiset

1. Hex.pm-jakelupalvelun web-palvelimilla hyökkääjä suoritti komentoja lähettämällä kirjautumattomia Erlang-termipyyntöjä, jotka ohittivat Plug.Crypto-suojauksen ja laukaisivat koodin suorituksen Sentry-lokituksen kautta (CVE-2026-129514, haavoittuvuus ollut olemassa vuodesta 2016). Hex korjasi ongelman 20 minuutissa eikä löytänyt manipulated-paketteja, mutta sähköpostiosoitteiden, salasanatiivisteiden ja 2FA-salaisuuksien lukuunta ei voida sulkea pois. Käyttäjiä kehotetaan vaihtamaan salasana, nollaamaan 2FA ja päivittämään Ash versioon 3.38.0.

2. Eteläkorealainen kryptopörssi Bithumb ilmoitti, että hyökkääjä tunkeutui DaouOffice-yhteistyöpalveluun ja varasti asiakastietoja 15 päivän ajan ennen havaitsemista. Varkauteen sisältyy passi- ja henkilötunnusnumeroita, ajokorttitietoja, transaktiohistoriaa ja yhteystietoja.

3. Pohjois-Koreaan kytketty PolinRider-kampanja on käyttänyt varastettuja GitHub-tokeneja pakottaakseen haitallisia lataajia vähintään 7 609 repositorioon. Lataaja lukee vaiheensa ja C2-osoitteensa Ethereum-lompakkotransaktioista, joten palvelinten sulkeminen ei auta. Kehittäjiä kehotetaan estämään yhteydet kahteen mainittuun IP-osoitteeseen ja tarkistamaan conftest.py ja VS Code -tehtävät.

4. Intruder-tutkijat lunastivat 28 AWS Elastic IP -osoitetta, jotka vastasivat roikkuvia DNS-tietueita, mukaan lukien viisi Yhdysvaltain valtiovarainministeriön aladomainia, hintaan noin kolme dollaria kappaleelta.

5. Kierrossa käsitellään myös Samsung Knoxin root-ketjuun liittyvää tutkimusta.
