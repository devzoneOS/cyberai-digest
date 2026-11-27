# terraform-octopus-chainguard

- **Päivämäärä:** 2026-11-27
- **Lähde:** TLDR (dan@tldrnewsletter.com)
- **Gmail-aihe:** "Beyond GitHub Actions ⚙️, Terraform Updates 🛠️, GPU Networks 🔌"
- **Kategoria:** cloud
- **Tunnisteet:** terraform, hcp, octopus-deploy, chainguard, kubernetes, gpu-verkko, teleport, ai-agentit

## Keskeiset uutiset

- **Terraformin TFPolicy ja SCIM yleisesti saatavilla.** HashiCorp toi HCL-pohjaisen politiikan Stacksille GA:na, lisäsi monen deployment-ryhmän orkestroinnin ja agent-valmiit CLI-komennot JSON-tulosteella. SCIM 2.0 -provisionointi on nyt GA Standard- ja Premium-tasoilla.

- **Chainguard siirtyi omalle microVM-infralle.** Tuhansien päivittäisten buildien siirto GitHub Actionsista omalle infrastruktuurille esti julkaisujonojen tahmean pilvikatkoissa. CVE-korjausagentit onnistuvat 97-98 %:sti viikoittain.

- **Octopus Deployin uusi käyttöliittymä.** Instanssikohtainen haku, ryhmitelty navigaatio ja läpikäytävä REST API -referenssi (noin 1 800 päätepistettä) rullaavat pilveen nyt ja itse isännöityille joulukuussa.

- **AI-agentit eivät saa SSH-avaimia.** Teleportin delegoitu identiteetti aloittaa agentit ilman oikeuksia, pyytää vain tehtävän vaatimat ja jättää auditoitavan jäljen tekojen ja teettäjän välille.

- **GPU-työkuormat muokittavat verkkoa.** Suuremmat NVLink-domainit ja kytkinten sisäinen SHARP-aggregointi määrittävät, missä kommunikaatiopainotteinen rinnakkaisuus voi ajaa.
