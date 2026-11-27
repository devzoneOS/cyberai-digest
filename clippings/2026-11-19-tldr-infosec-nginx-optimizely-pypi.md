# 2026-11-19 — TLDR Information Security

- **Kategoria:** cyber_news
- **Tunnisteet:** supply-chain-attack, nginx-rce, cdn-malware, smart-card-abuse, llm-backdoors
- **Lähde:** TLDR Information Security (dan@tldrnewsletter.com), 2026-11-19
- **Gmail-aihe:** "Wiz Discovers NGINX RCEs 😈, Optimizely CDN Hijacked to Spread Malware 🛜, Chainguard Adds Starter Tier ⛓️"

## Keskeiset uutiset

1. **Microsoftin agent-framework PyPI-paketti (versiot 1.26.1-1.26.2) vioitettiin julkaisijatililtä:** .pth-tiedosto käynnistyy jokaisella Python-käynnistyksellä, varastaa ympäristömuuttujat, tunnukset ja muiden prosessien /proc-environit, sekä pyytää tuoreet GitHub Actions-, Azure DevOps- ja Azure-hallintaidentiteettitokenit webhookiin. Kaikki salaisuudet on kiertävä ja asennus käsiteltävä täyttä tunnusten vaarantumisena.
2. **Optimizelyn CDN:ä väärinkäytettiin malwaresyöttöön: 178 sivustoa (CNN, Zoom, BBC, Salesforce) sai track.js-koodin, joka korvasi lompakkoosoitteita, kaappasi korttinumeroita, CVV:tä, evästeitä ja näyttökuvia sekä tarjosi iOS-hyökkäyskokoelmia.** Optimizely ei ole selittänyt kirjoitusoikeuden alkuperää.
3. **Wiz löysi kaksi tunnuksetonta RCE:tä NGINX:stä (use-after-free ja kokonaislukuylivuoto HTTP/2:ssa).** Paikattuihin versioihin päivitys tai HTTP/2:n poisto käytöstä.
4. **Windowsin älykorttiminiajuriarkkitehtuurin väärinkäyttö:** matalaoikeuksinen prosessi voi ladata uhrin älykortin miniajurin, kaapata PIN-koodin (CardAuthenticateEx-hook) ja allekirjoittaa hyökkääjän dataa SMB-nimettyjen putkien yli (Hermes-proxy) - suunnittelun mukaista toimintaa, ei haavoittuvuus. Älykorttitodennus ei ole todiste fyysisestä läsnäolosta.
5. **"LLM:ien takaovet": hienosäädetty Qwen3-8B voi suolttaa hyökkääjän tavoitteita vastaavaa koodia vain kehotteen muuttuessa** - luottamus AI-mallin tarjoajaan on nyt toimitusketjukysymys.
