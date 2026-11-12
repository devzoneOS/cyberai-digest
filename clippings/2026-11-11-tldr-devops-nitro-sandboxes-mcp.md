---
pvm: 2026-11-11
kategoria: ai_security
tunnisteet: [aws, nitro, eks, gke, mcp, argo-cd, tietoturva]
lahde: TLDR DevOps
gmail-aihe: "Argo CD Cost 💰, AWS Nitro Sandboxes ☁️, MCP Security 🥷"
---

1. **AWS Nitro Sandboxes EKS:iin:** Ominaisuus tarjoaa laitteistolla pakotetun eristyksen Amazon EKS -podeille ajamalla jokaisen podin omassa kevyessä virtuaalikoneessa. Vahvat turvarajat saa päälle yhdellä rivillä pod-määrityksessä ilman kontti-imagen tai deployment-putken muutoksia; confidential-moodi lisää kattavan kryptografisen attestoinnin.

2. **GKE dynamic slicing GA:lle:** GKE:n dynaaminen sliceytys erottaa slicejen muodostuksen nodepool-valmistelusta ja lyhentää AI-työkuormien käynnistysaikoja jopa 5x ja palautusaikoja 4,5x.

3. **MCP-palvelinten tietoturva-aukot:** MCP-palvelimista puuttuvat sisäänrakennetut autentikointi, rate limiting ja työkalukontrollit, mikä luo organisaatioille turva-aukkoja. Artikkeli käsittelee, miten aukot tulpataan.

4. **Argo CD:n kustannusnäkyvyys:** Avoimen lähdekoodin Cost Intelligence -laajennus näyttää jokaisen sovelluksen kustannuksen UI-välilehdessä edellisen 24 tunnin OpenCost-datan pohjalta (vaatii Argo CD 3.4–3.6 ja OpenCost 1.121.1+).

5. **Kubernetes ei anna agenttien palautua oikein:** Kubernetes voi palauttaa agentin ympäristön, mutta ei tallenna mitkä askeleet valmistuivat, joten uudelleen käynnistetty agentti voi toistaa toimia kuten maksuja. Kirjoittaja ehdottaa kestävää suoritusta, joka lokittaa jokaisen askeleen (esim. Daprin workflow-engine).
