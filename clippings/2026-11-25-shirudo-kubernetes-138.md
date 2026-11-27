# shirudo-kubernetes-138

- **Päivämäärä:** 2026-11-25
- **Lähde:** TLDR (dan@tldrnewsletter.com)
- **Gmail-aihe:** "Linux Runtime Shields 🛡️, Kubernetes 1.38 Preview ☸️, When Healthy DNS Breaks 🔎"
- **Kategoria:** cloud
- **Tunnisteet:** shirudo, ebpf, kubernetes-1-38, cloudflare, dns, fly-io, agentit, cgroup

## Keskeiset uutiset

- **OpenAI ja Cisco julkaisivat Shirudon.** Avoimen BSD-lisenssin runtime suojaa käynnissä olevia Linux-järjestelmiä ilman korjauksia tai uudelleenkäynnistyksiä. eBPF estää haavoittuvat koodipolut ja antaa tietoturbatiimille aikaa pysyvään korjaukseen.

- **Kubernetes v1.38 esikatselu.** Julkaisu muuttaa kubeletten cgroup-ajurin hankintaa CRI:n kautta, poistaa WebSocket-opt-out-ympäristömuuttujat ja pudottaa vanhentuneet name-aliakset. Operattorien pitää varmistaa runtime-yhteensopivuus.

- **Agentit ylittivät ihmiset web-liikenteessä.** Fly.io:lla agentit suorittavat jo yli 55 % deployeista. Palvelu tuo auth.md-agenttirekisteröinnin ja Machine Payments Protocolin, jolla agentit täydentävät tilejään ilman ihmistä.

- **DNS voi rikoutua ilman terveysvaroituksia.** Cloudflaren ajastusvika jätti DNS-muutokset julkaisematta tunteja vihreiden health-checkien alla. Flamingo-testikehys laajennettiin mittaamaan propagointia jokaisesta datakeskuksesta.

- **Sovellustason sharding kannattaa usein välttää.** Intercomin, Etyn ja Slackin kokemukset osoittavat vaikeat reshardingit, cross-shard-kyselyt ja lookup-taulujen yksittäispiste-riskit.
