---
pvm: 2026-11-10
kategoria: vulnerabilities
tunnisteet: [sonicwall, mfa, qnap, plex, aws, qubole, ai-hyokkaykset]
lahde: TLDR Information Security
gmail-aihe: "SonicWall MFA bypass 🔓, DeepMind RSA-1024 Attack 🔑, Automaker admin hack 🚗"
---

1. **SonicWallin SSL-VPN MFA-ohitus aktiivisesti hyväksytty:** Uusi SonicOS-haavoittuvuus antaa vaihtoehtoisen autentikointitavan tunnukset omaavan hyökkääjän ohittaa SAML-kontrollit ja mahdollisesti MFA:n. CISA lisäsi aukon KEV-listalle; SonicWall paikkasi myös kuusi muuta aukkoa, mm. puskuriylivuotoja ja heikkoa salasanasalausta.

2. **QNAP: Plex2Shell-kampanjat murtavat NAS-laitteita:** Aktiivisesti hyväksyttyjen neljän Plex-haavoittuvuuden jälkeen QNAP kehottaa päivittämään Plex-palvelimet. Haavoittuvan ja julkiseen internetiin altistuneen Plex-palvelimen käyttäjien kannattaa pitää NAS-laitteita ja kaikkea sisältöä vaarannettuna.

3. **Qubolen cross-account-hyökkäys:** 14.–26.10. hyökkääjä käytti Qubolen AWS-tilin IAM-tunnuksia asiakkaiden luottamien roolien kautta: keräsi Secrets Manager-, SSM- ja Lambda-salaisuudet, tarkisti ne TruffleHogilla (AWS, Entra ID, Okta) ja latasi kokonaisia S3-bucketteja. aws:SourceIp-ehto yksin olisi estänyt jokaisen yrityksen.

4. **AI-avusteisten hyökkäysten tunnistaminen:** On tärkeää erottaa ihminen, LLM:tä käyttävä ihminen ja autonomiset agentit. LLM:t tekevät virheitä synteettisissä otsikoissa ja koodauksen antipattereissa, ja agentit toimivat usein map-reduce-tyyliin hajottaen tiedonkeruun ja syntetisoiden tulokset kerralla.

5. **PHP2Shell-ketju:** Use-after-free -ketju johtaa etäkoodin suoritukseen muokatun multipart-pyynnön laukaiseman muistivirheen kautta.
