# 2026-11-16 — TLDR DevOps

- **Kategoria:** ai_news
- **Tunnisteet:** kubernetes-agents, cost-control, networking, gang-scheduling
- **Lähde:** TLDR DevOps (dan@tldrnewsletter.com), 2026-11-16
- **Gmail-aihe:** "kagent 1.0 🆕, Cloudflare Spend Management 💰, TPU Sync ⚡️"

## Keskeiset uutiset

1. **kagent 1.0 (GA): yritysvalmis Agent Substrate -distribuutio AI-agenteille Kubernetesissa.** Agenttityrmkset ajastetaan "actoreina" lmmin typutkille; jlkeiset actorit keskeytetn automaattisesti ja palautetaan uusien pyynt saapuessa - Agent Substrate on nyt CNCF-projekti.
2. **Cloudflaren Spend Management: pay-as-you-go-kyttjt voivat asettaa kulurajoja ja pysytt toiminnan rajan ylittyess** (beta kattaa Workersit ja Durable Objectsit), lhes reaaliaikainen kuluseuranta dashboardissa, CLI:ss ja API:ssa.
3. **Fly.io heitti puhelinluettelon pois: 6PN-yksityisverkon reititystietueet (satatuhansia jokaisessa palvelimessa) korvattiin laiskalla haulla,** joka pit 100-200 tietuetta palvelinta kohden ja oppii reitit tarvittaessa - VXLAN ja ytimen vakiotykalut monimutkaisen eBPF:n sijaan.
4. **Gang-scheduling ja topologia-tietoinen sijoitus Kubernetesissa:** jaetun AI-koulutuksen podien pit laskea oikean GPU-kaistanleveyden laitteille samanaikaisesti - Kueue ja Coscheduling-plugin ratkaisevat.
5. **AWS Nitro Sandboxes bin-pakkkaa useita SaaS-vuokralaisia jaetuille solmuille laitteistoeristetyiss hiekkalaatikoissa,** joilla kullakin on oma kerneli; luottamuksellinen tila lis attestoinnin.
