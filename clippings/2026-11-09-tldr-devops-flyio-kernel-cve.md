# 2026-11-09 — TLDR DevOps

- **Kategoria:** vulnerabilities
- **Tunnisteet:** kernel-cve, fleet-recovery, dns, supply-chain, iac
- **Lähde:** TLDR DevOps (dan@tldrnewsletter.com), 2026-11-09
- **Gmail-aihe:** "Octopus Feature Flags 🐙, Harmess for Agents 🪄, Grafana Variables 📈"

## Keskeiset uutiset

1. **Fly.io patchasi ja bootti koko kalustonsa 10 tunnissa CVE-2026-99999:n (Linux-kernel) takia.** Vieraat VM:t pystyivät lukemaan isäntämuistia kaksi tavun IPv4-otsikon manipuloinnilla, mikä mahdollisti palomuurin ohitukset ja rajoja ylittävät luvut; salaamatonta liikennettä 15.–17.10. lähettäneitä kehotetaan kierrättämään tunnukset.
2. **Cloudflaren DNS-uudelleenrakennuksen poisto: huippumuisti putosi 79 GiB:stä 12 GiB:iin** ja mediaan-rakennusaika 7,7 sekunnista 3,3:een, kun vyöhykkeitä ei enää rakenneta kokonaan uudelleen.
3. **Docker ja ActiveState laajentavat luotettua sisältöä pip-, npm- ja Maven-paketteihin:** komponentit rakennetaan lähteestä ja kriittisille CVE:ille luvataan korjaukset viidessä työpäivässä.
4. **Octopus Feature Flags GA:ntui pilvessä ja self-hosted 2027.0:ssa** sääntöpohjaisella kohdentamisella ja porrastetuilla automaattirollaauksilla.
5. **OpenTofu-import-kansio kannattaa tehdä import-blockeina** CLI-komennon sijaan, koska ne näkyvät planissa ja applyssa; Spaceliftin tutoriaali kattaa for_each- ja identiteettiargumentit.
