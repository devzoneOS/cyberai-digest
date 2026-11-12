# 2026-11-10 — TLDR Information Security

- **Kategoria:** vulnerabilities
- **Tunnisteet:** vpn, mfa-bypass, nas, cloud-iam, use-after-free
- **Lähde:** TLDR Information Security (dan@tldrnewsletter.com), 2026-11-10
- **Gmail-aihe:** "SonicWall MFA bypass 🔓, DeepMind RSA-1024 Attack 🔑, Automaker admin hack 🚗"

## Keskeiset uutiset

1. **SonicWallin SonicOS SSL-VPN MFA-ohitus on KEV-listalla ja mahdollisesti hyväksikäytössä.** Vaihtoehtoisella tunnistautumistavalla varustettu hyökkääjä voi ohittaa SAML-ohjaukset; mukana myös kaksi pre-auth-puskuriylivuotoa ja heikkoja salasanahajautuksia.
2. **QNAP kehottaa päivittämään Plex-palvelimet aktiivisesti hyväksyttyjen Plex2Shell-haavoittuvuuksien takia.** Julkiseen internetiin alttiina ajaneita NAS-laitteita pitää pitää vaarannettuina.
3. **Qubolen AWS-tilin IAM-tunnukset väärinkäytettiin 14.–26.10. välisenä aikana.** Hyökkääjä assasi asiakkaiden luottamusrooleja, luki Secrets Manager-, SSM- ja Lambda-arvoja ja latasi S3-objekteja — aws:SourceIp-ehto olisi estänyt jokaisen yrityksen.
4. **AI- ja agenttihyökkäysten tunnistaminen vaatii käyttäytymiseroavaisuuksien hahmottamista:** LLM:t tekevät "koneystävällisiä" virheitä, ja agentit käyttävät map-reduce-tyylisiä tiedustelumalleja, joita valvonnalla voi erottaa ihmisistä.
5. **PHP2Shell on use-after-free-ketju etäkoodisuoritukseen**, joka laukaistaan muokatulla multipart-pyynnöllä.
