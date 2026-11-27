# 2026-11-13 — TLDR DevOps

- **Kategoria:** vulnerabilities
- **Tunnisteet:** apache, http/2, rce, soloio, kagent, heroku, planetscale, codemender
- **Lähde:** TLDR Newsletter (dan@tldrnewsletter.com)
- **Gmail-aihe:** Apache Server Vulnerability, Heroku Migration, CodeMender

## Keskeiset uutiset

1. Kriittinen RCE-haavoittuvuus Apache HTTP Serverin HTTP/2-moduulissa johtuu kilpailutilanteesta assign_headers()-funktiossa. Wizin mukaan 64 prosenttia pilviympäristöistä sisältää haavoittuvia resursseja; korjaus on päivitys versioon 2.4.71 tai uudempaan tai HTTP/2:n poistaminen käytöstä.

2. Solo.io julkaisi yleisesti saataville Agent Substraten ja kagentin enterprise-versiot, jotka pysäyttävät joutilaat agentti-istunnot ja palauttavat ne tarpeen mukaan. Agentgateway valvoo liikenteen identiteettiä ja sääntöjä, ja OutSystems ja Swissquote ajavat pinoa tuotannossa.

3. Googlen pilviarkkitehdit kuvaavat referenssiarkkitehtuuria, jossa CodeMender-turvallisuusagentti liitetään pull-pyyntöihin Cloud Runilla: komennot tarkistavat ja korjaavat löydökset, ja lyhytikäiset OIDC-tokenit korvaavat tallennetut avaimet.

4. Lyft rakensi Fake Payment Provider -työkalun monimutkaisten maksuvirhetilanteiden, kuten osittaisten maksulupien, viivästyneiden veloituksien ja palautusten, mallintamiseen. Skenaariologiikka upotetaan suoraan maksutokeniin, jolloin testit voidaan ajaa turvallisesti sekä staging- että tuotantoympäristössä.

5. PlanetScale julkaisi avoimen Heroku Migrator -työkalun, jolla tietokannat voidaan siirtää Herokusta ilman loogista replikointia. Bucardo-pohjainen triggerireplikointi ja kaksivaiheinen siirto (datansiirto ja indeksien uudelleenrakennus) nopeuttavat kopiointia noin viisinkertaisesti.
