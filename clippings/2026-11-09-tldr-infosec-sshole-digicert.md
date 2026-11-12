---
pvm: 2026-11-09
kategoria: vulnerabilities
tunnisteet: [alpine, ssh, digicert, litellm, toimitusketju, esxi]
lahde: TLDR Information Security
gmail-aihe: "*sshole Alpine SSH bug 🐛, DigiCert data breach 🔐, Claude sandbox escape 🤖"
---

1. **"*sshole" avaa Alpine-järjestelmät ilman salasanaa:** Aukko koskee musl-kirjastolla ja ilman PAM:ia koostettua OpenSSH:ää, jossa aktiivisella salasanattomalla tilillä on SHA256/SHA512-salaus. Yli 256 merkin syöte salasanakenttään antaa kirjautumisen yhdellä yrityksellä. Alpine ja OpenSSH ovat julkaisseet paikkaukset, ja järjestelmät pitää päivittää pikaisesti.

2. **DigiCertin tietomurto:** Hyökkääjät loivat vain-luku-tilin altistuneeseen sisäiseen arkistojärjestelmään ja näkivät yritysasiakkaiden yhteystiedot 27.6.–2.7. — nimiä, sähköposteja, puhelinnumeroita ja joissain tapauksissa henkilötodistuksia. Varmistetta myöntävät järjestelmät eivät vaikuttaneet; salasanat on nollattu ja oikeudet auditoitu.

3. **Iris Ohyaman pilvitietomurto: 7,7 miljoonaa asiakasta:** Kolmannen osapuolen pilvipalvelun murto paljasti täydet nimet, osoitteet, puhelinnumerot, sähköpostit, sukupuolet, syntymäajat ja tilin salasanat. Salasanat ovat salattuja, mutta yksityiskohtia ei ole julkistettu.

4. **LiteLLM-toimitusketjuhyökkäys:** Ylläpitoavain commitoitiin julkiseen repoon toukokuussa, poistettiin mutta ei koskaan kumottiin. Lokakuussa hyökkääjä käytti sitä varastamaan GitHub CLI-tokenin ja kaksi maintainer-tokenia, ohitti branch protectionin ja julkaisi myrkytettyjä wheelejä ja imageja noin kahdeksi tunniksi. Periaatteet: kumoa kaikki commitatut avaimet, äläkä pidä scopelemattomia CLI-tokeneja automaatiossa.

5. **Virtualisoinnin turvaaukot:** Kaspersky GERT:n BlackNevas-kiristystapauksessa hyökkääjät käyttivät PRTG-palvelimelta löytynyttä, isäntien välillä uudelleenkäytettyä ESXi-salasanaa, käänsivät execInstalledOnly:n pois päältä ja salakirjoittivat VMFS-osiot ennen lokien pyyhkimistä.
