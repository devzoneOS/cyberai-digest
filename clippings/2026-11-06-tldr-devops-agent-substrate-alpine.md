---
pvm: 2026-11-06
kategoria: vulnerabilities
tunnisteet: [alpine, openssh, google, cncf, docker, gke, agentit]
lahde: TLDR DevOps
gmail-aihe: "Silent Kubernetes 🤫, Open Infrastructure ✨, OpenTofu MCP 🍚"
---

1. **Alpinen OpenSSH-salasanaväistö:** openssh-server-paketin haavoittuvuus salli hyökkääjien ohittaa salasanatodennuksen ja kirjautua ilman salasanaa, jos järjestelmässä on salasanaton tili. Vaikuttaa julkaisuihin 3.16–3.24; openssh pitää päivittää ja sshd käynnistää uudelleen tai salasanakirjautuminen poistaa käytöstä heti.

2. **Google luovuttaa avoimen agentti-infran CNCF:lle:** Agent Substrate, gVisor ja OpenRL siirtyvät CNCF Sandboxiin, ja Agent Substrate on nyt GA GKE:ssä. Se irrottaa tilalliset agentti-istunnot laskennasta ja palauttaa joutoiset istunnot alle 500 ms:ssa, saavuttaa 10x konttitiheyden ja yli 500 suspend/resume-aktivointia sekunnissa.

3. **Docker: agentit eristettävä ja hallittava:** Docker listaa autonomisten AI-agenttien viisi riskiä, mukaan lukien prompt-injektion, tunnusten altistumisen ja dataeksfiltration, ja suosittelee eristystä ja hallintoa (Docker Sandboxes, AI Governance) pelkkien malliparannusten sijaan.

4. **GKE API:n hiljenemisen kolmen kerroksen mysteeri:** Google jäljitti katkonaiset GKE API -aikakatkaisut kolmeen vuorovaikutteiseen vioon: Private Service Connectin uudelleenjärjestetyt paketit, Envoyn pitämät half-closed-socketit ja Linuxin TCP-vika, joka esti socketien sulkeutumisen. Samanaikaiset pakettikaappaukset useista pisteistä paljastivat uudelleenjärjestämisen, ja kernel-korjaus ratkaisi ongelman.

5. **Tuotanto ilman keskitettyjä lokeja:** Yli 15 mikropalvelun K3s-alusta voidaan ajaa ilman keskitettyä lokinkeräystä suodattamien Prometheus-mittareiden ja väliaikaisen verboosilokin avulla — kompromisseina kysymysten ennakointi ja audit-sovellusten sopimattomuus muuttumattomia jälkiä vaativissa tilanteissa.
