# 2026-11-06 — TLDR DevOps

- **Kategoria:** vulnerabilities
- **Tunnisteet:** ssh, alpine-linux, ai-agents, kubernetes, networking
- **Lähde:** TLDR DevOps (dan@tldrnewsletter.com), 2026-11-06
- **Gmail-aihe:** "Silent Kubernetes 🤫, Open Infrastructure ✨, OpenTofu MCP 🍚"

## Keskeiset uutiset

1. **Alpine Linuxin openssh-server sisältää salasanatunnistuksen ohituksen (julkaisut 3.16–3.24).** Etähyökkääjä pääsee sisään ilman salasanaa, jos järjestelmässä on aktiivinen salasanaton tili; openssh pitää päivittää ja sshd käynnistää tai salasanakirjautuminen poistaa heti käytöstä.
2. **Google lahjoitti Agent Substraten, gVisorin ja OpenRL:n CNCF Sandboxille.** GA Agent Substrate palauttaa agentti-istunnot 500 ms:ssa, saavuttaa 10x konttitheyden ja yli 500 suspend/resume-aktivointia sekunnissa.
3. **Docker listaa viisi autonomisten agenttien riskiä** (prompt-injektio, tunnusten paljastuminen, datan eksfiltraatio) ja suosittelee eristystä ja hallintaa hiekkalaatikoiden kautta malliparannusten sijaan.
4. **GKE API:n ajoittaiset katkokset juurtuivat kolmeen toisiinsa kytkeytyvään vikaan:** PSC:n uudelleenjärjestetyt paketit, Envoin puolittain suljetut socketit ja Linuxin TCP-bugi — kernel-korjaus ratkaisi ongelman.
5. **K3s-ympäristöä voi pyörittää ilman keskitettyä lokikeräystä** Prometheus-metriikoilla ja väliaikaisella verbose-lokkauksella, mutta muuttumattomia lokia vaativat auditoinnit estävät tämän mallin.
