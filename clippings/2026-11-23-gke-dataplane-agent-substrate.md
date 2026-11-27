# gke-dataplane-agent-substrate

- **Päivämäärä:** 2026-11-23
- **Lähde:** TLDR (dan@tldrnewsletter.com)
- **Gmail-aihe:** "GKE Dataplane V2 ✈️, Agentic Loops 🔁, AI Observability 🔍"
- **Kategoria:** cloud
- **Tunnisteet:** gke, google-cloud, agent-substrate, gvisor, karpenter, cncf, kubernetes

## Keskeiset uutiset

- **Agent Substrate ja gVisor CNCF:lle.** Google siirsi molemmat projektit säätiölle, jotta AI-agentteja voidaan ajaa turvallisesti suuressa mittakaavassa. Agent Substrate erottaa agentin tilan laskennasta esilämmitetyissä Kubernetes-pooleissa, jolloin agentit jatkavat alle 500 ms:ssa.

- **GKE Dataplane V2 -siirto paikan päällä.** Esikatselussa VPC-natiiviklusterit voivat siirtyä V1:stä V2:een ilman rinnakkaisklusteria, ja paluu onnistuu ennen viimeistelyä.

- **Karpenter v1.15.** Päivitys huomioi GPU-topologian ja verkon DRA-tuella, käsittelee noden korjaukset vapaaehtoisina häiriöinä ja tuo podin poistokustannusten kontrollerin sekä CEL-tuen.

- **170 PR:ää tuotantoon viikossa.** Tekninen johtaja skaalasi tuotantoon vietäviä muutoksia modernisoimalla CI/CD:n ja rakentamalla pilviharnessin orkestroiduille agenteille.

- **PlanetScalein agentti voi tehdä hitaampia kyselyitä.** Optimointiagentti ehdotti indeksiä, joka hidasti tuotantokyselyä SQL-yhteenvedon piilottaessa 645 alkion IN-listan. Korjaus pudotti keskimääräisen kyselyajan 28,5 ms:stä 1,95 ms:iin.
