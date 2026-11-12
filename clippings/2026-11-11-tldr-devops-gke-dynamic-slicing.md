# 2026-11-11 — TLDR DevOps

- **Kategoria:** ai_security
- **Tunnisteet:** kubernetes, sandboxing, mcp-security, cost-monitoring
- **Lähde:** TLDR DevOps (dan@tldrnewsletter.com), 2026-11-11
- **Gmail-aihe:** "Argo CD Cost 💰, AWS Nitro Sandboxes ☁️, MCP Security 🥷"

## Keskeiset uutiset

1. **AWS Nitro Sandboxes tarjoaa laitteistotuetun eristyksen EKS-podeille:** jokainen pod ajaa omassa kevyessä virtuaalikoneessa, yksi rivi pod-spekiä riittää, ja confidential-tila tuo kryptografisen attestoinnin — sopii luotettamattoman LLM-koodin ajamiseen.
2. **GKE:n dynaaminen slicaus TPuille GA:ntui:** slice-muodostus erotettu nodepool-provisioinnista, mikä nopeutti AI-kuormien käynnistyksiä jopa 5x ja palautuksia 4,5x.
3. **MCP-palvelimista puuttuu sisäänrakennettu autentikointi, rate limiting ja työkaluvalvonta.** Ratkaisuksi esitetään AI Gatewayn asentamista tokenpohjaisella tunnistuksella ja työkalukohtaisia rajoituksia.
4. **Kubernetes ei tallenna agentin tekemiä askeleita, joten uudelleenkäynnistetty agentti voi toistaa esimerkiksi maksuja.** Kirjoittaja suosittelee kestävää suoritusta (esim. Dapr workflow) lokittamaan jokaisen vaiheen.
5. **Cost Intelligence for Argo CD näyttää jokaisen sovelluksen kustannukset UI:ssa OpenCost-datan perusteella.** CloudNativePG nousi CNCF Sandboxista Incubation-vaiheeseen.
