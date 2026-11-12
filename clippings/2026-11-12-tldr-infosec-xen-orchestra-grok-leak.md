---
pvm: 2026-11-12
kategoria: vulnerabilities
tunnisteet: [xen-orchestra, tietomurto, valtuutus-aukko, nitori, grok-build, agenttien-tietoturva]
lahde: TLDR Information Security
gmail-aihe: "Xen Orchestra flaw 🔓, Grok Build leak 🤖, OpenAI kill switch 🛑"
---

1. **Kriittinen Xen Orchestra -aukko aktiivisessa hyväksikäytössä:** Verkkopohjaisen XCP-NG-hallinta-alustan valtuutuksen ohitus mahdollistaa kirjautumistokenien varastamisen erityisellä evästeellä, mielivaltaisen koodin suorittamisen hallinnoivissa pooleissa ja koko klusterin kaappauksen. Ylläpitäjiä kehotetaan päivittämään heti ja rajoittamaan portaalin julkisen internetin altistusta.

2. **Nitorin tietomurto: 37,6 miljoonaa asiakastietuetta:** Japanilainen huonekalujätti Nitori paljasti, että hakkerit varastivat 37,62 miljoonan jäsenen ja asiakkaan tiedot, mukaan lukien nimet, osoitteet ja syntymäajat. Salasanoja tai luottokorttinumeroita ei varastettu.

3. **Grok Build vuotaa luottamuksellista dataa:** Claroc löysi passiivisella DNS-luetteloinnilla yli 35 000 julkista Grok Build -sovellusta. Altistuneeseen aineistoon kuuluvat SpaceXSI:n myyntisuunnitelmat, 3 784 työntekijän terveystarkistusta, Tesla-pisteytyksiä ja laivaurakoitsijoiden listoja — URL-satunnaisuus sijoitettiin alidomainiin, jonka DNS paljasti.

4. **AI-agentit voi takaportata muokkaamalla alle 10 neuronia:** Microsoftin "Lazarus"-menetelmä upottaa piilokomennon avaamalla muokkaamalla alle 10 harvoin käytettyä neuronia avoimen mallin painoissa. Testissä 98,8 %:n onnistumisaste saavutettiin seitsemällä muokatulla neuronilla. Microsoft suosittelee painojen vertailua, hiekkalaatikoita ja hyväksyntäprosesseja korkean vaikutuksen toiminnoille.

5. **M365-istunnon peruutus ei katkaise sähköpostiä heti:** Kun Entra peruuttaa istunnon, access-token voi pysyä voimassa jopa 90 minuuttia, eikä kriittinen tapahtumien evaluointi estä Graph API -käyttöä. Ainoa taattu tapa katkaista käyttö heti on tilin poistaminen käytöstä.

6. **Falcon C2 selaimessa:** Hyökkääjä upotti script-tagin 39 Roundcube-portaalin otsikkoihin, jolloin kullekin kävijälle tarjoillaan omat obfuskoitu implantit, jotka varastavat salasanat, viestit ja evästeet salatun WebSocketin yli. Uhreina mm. Lähi-idän ulkoministeriö ja Kaakkois-Aasian poliisi- ja oikeusjärjestelmät.
