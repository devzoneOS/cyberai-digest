---
pvm: 2026-11-09
kategoria: vulnerabilities
tunnisteet: [flyio, linux-kernel, cve, docker, octopus, opentofu, cloudflare]
lahde: TLDR DevOps
gmail-aihe: "Octopus Feature Flags 🐙, Harmess for Agents 🪄, Grafana Variables 📈"
---

1. **Fly.io korjasi koko laivaston kernel-bugin takia:** CVE-2026-99999 salli vieras-VM:ien lukea isäntämuistia — hyökkääjä saattoi kontrolloida kahta IPv4-otsakkeen tavua, mikä johti palomuurien ohituksiin ja oob-lukuihin. Fly.io paikkasi ja boottasi koko laivaston 10 tunnissa ja kehottaa salaamatonta liikennettä 15.–17.10. lähettäneitä kiertämään tunnuksensa.

2. **Alpinen OpenSSH-salasanakierros:** openssh-server-paketin aukko salli kirjautumisen ilman salasanaa, jos tilillä ei ole salasanaa. Vaikuttaa julkaisuihin 3.16–3.24; openssh pitää päivittää ja sshd käynnistää uudelleen tai salasanakirjautumiset poistaa heti.

3. **Docker ja ActiveState laajentavat luotettua sisältöä paketteihin:** Kumppanuus ulottaa trusted content -standardin peruskuvista pip-, npm- ja Maven-paketteihin; ActiveState rakentaa komponentit lähdekoodista ja lupaa korjaukset kriittisiin CVE:ihin viidessä työpäivässä.

4. **Octopus Feature Flags GA:ksi:** Ominaisuus poistuu julkisesta esikatselusta Octopus Cloudissa ja saapuu itse isännöityyn Octopus 2027.0:aan sääntöpohjaisella kohdentamisella ja vaiheistetulla automaattisella julkaisulla; vanhat liput vaativat päivitetyt asiakas-SDK:t ennen päivitystä.

5. **Cloudflare puolitti DNS-rakennusten viiveen:** Lopettamalla kokonaisten DNS-vyöhykkeiden uudelleenrakentamisen asetusmuutosten yhteydessä Cloudflare pudotti piikkimuistin 79 GiB:stä 12 GiB:iin ja mediaanin rakennusajan 7,7 sekunnista 3,3 sekuntiin.
