# cisco-rce-toimitusketju

- **Päivämäärä:** 2026-11-24
- **Lähde:** TLDR (dan@tldrnewsletter.com)
- **Gmail-aihe:** "Cisco RCE under attack 🚨, AI root access in 11m 🤖, CrowdStrike buys Zscaler 🤝"
- **Kategoria:** vulnerabilities
- **Tunnisteet:** cisco, expressway, cve-2026-76466, binary-parser, virtualbox, wordpress-toimitusketju, aws-iam

## Keskeiset uutiset

- **Cisco Expressway -RCE:tä hyödynnetään.** CVE-2026-76466 (CVSS 9.8) käyttää kovakoodattuja tunnuksia ja heikkoa sertifikaattien tarkistusta root-oikeuksien suoritukseen ilman tunnistusta. Hyökkääjät levittäysivät SMB-, SQL Server- ja WinRM-skripteillä sisäverkkoon, ja CISA antoi liittovaltion virastoille korjausmääräajan.

- **binary-parser-koodi-injektio.** Versiot ennen 2.3.1 sisältävät CVE-2026-134814, jolla parser-määrittelyitä kontrolloiva hyökkääjä injektoi JavaScriptiä Node.js-prosessiin validoimattomien optioiden kautta.

- **Yksittäinen bitti ohitti VirtualBox-kovennuksen.** PE-otsikon lipun tyhjentäminen saa .NETin lataamaan assemblyn ohittaen koodieheyden tarkistukset. Project Zero ketjutti kolme ohihyökkäystä, mukaan lukien PPL-tason suorituksen ilman ylläpito-oikeuksia.

- **WordPress-toimitusketjuhuijaus.** Hyökkääjä käytti WP Connectin tiliä työntääkseen backdoorkaantuneita julkaisuja kuuteen lisäosaan. WordPress.org:n uusi julkaisujäähdytyspito esti päivitykset, mutta adminien pitää tarkistaa versiot ja etsiä webshellejä.

- **LLM:t erehtyvät AWS IAM:ssa.** Koodausagentit ylikäyttävät Deny-käytäntöjä ja lisäävät tarpeettomia Allow-sääntöjä, joten IAM-politiikat kannattaa pitää ihmisen katseltavina.
