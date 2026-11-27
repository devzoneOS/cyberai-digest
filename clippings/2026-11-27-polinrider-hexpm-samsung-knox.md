# polinrider-hexpm-samsung-knox

- **Päivämäärä:** 2026-11-27
- **Lähde:** TLDR (dan@tldrnewsletter.com)
- **Gmail-aihe:** "PolinRider hits 7.6K repos 📦, Erlang Package Manager incident 📦, Samsung Knox root chain 📱"
- **Kategoria:** vulnerabilities
- **Tunnisteet:** polinrider, pohjois-korea, github, hex-pm, erlang, cve-2026-129514, bithumb, samsung-knox, subdomain-takeover, remus, usa-treasury

## Keskeiset uutiset

- **PolinRider saastutti 7 609 repoa.** Pohjois-korealainen kampanja käytti varastettuja GitHub-tokeneita pakottaakseen loader-committeja yli 7 600 repositorioon. Koodi piilotetaan build-konfiguraatioihin, conftest.py:hin tai VS Code -tehtäviin, ja C2-osoite luetaan Ethereum-lompakon transaktioista. Kehittäjiä kehotetaan kierrättämään tokenit ja estämään kaksi osoitetta.

- **Tietoturvapoikkeama hex.pm:ssa.** Hyökkääjä ajoi komentoja kuudessa palvelimessa väärennettyjen Elixir-structien kautta (CVE-2026-129514, olemassa vuodesta 2016). Sentry-lokitus laukaisi Ecto-gadget-ketjun, joka ajoi hyökkääjän koodia. Salasana ja 2FA kannattaa vaihtaa, eikä paketteja kannata hakea muualta kuin repo.hex.pm:stä.

- **Bithumbin murto kesti 15 päivää.** DaouOffice-yhteistyöpalvelun kautta varastettiin asiakkaiden passinumerot, pankki- ja lompakkotiedot ja transaktiohistoriat ennen havaitsemista.

- **Yhdysvaltain valtionvarainministeriön alidomainit kaapattavissa 3 dollarilla.** Intruder varasi 28 AWS Elastic IP:tä, jotka vastasivat vanhentuneita DNS-tietueita, mukaan lukien viittä treasury.gov-alidomainia. AWS ei aio muuttaa toimintaansa.

- **Samsung Knox DualDAR -rootketju.** Nollaoikeuksinen sovellus voi rootata Galaxy S23- ja lukitun S26-laitteen relayAsync-kutsun kautta: komento välittyy system_serverissä ja page-UAF in /dev/dd ajaa natiivikoodia, minkä jälkeen SELinux, RKP ja DEFEX poistetaan käytöstä (CVE-2026-21102, korjattu elo-syyskuussa 2026).

- **Remus varastaa Gmail-viestit.** Uusi versio väittää hyödyntävän Gmailin zero-daytä, mutta tutkijoiden mukaan se asentaa Google Sheetsinä naamioituvan Chrome-laajennuksen, joka hakee viestit minuutin välein.
