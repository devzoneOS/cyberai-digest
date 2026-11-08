---
pvm: 2026-11-06
kategoria: ai_security
tunnisteet: [openai, gpt-6-cyber, kyberturvamalli, haavoittuvuudet, firefox, linux, brotli, daybreak, red-teaming]
lahde: Mobiili.fi 6.11.2026 (Markus Lehtiniitty)
liite: https://drive.google.com/file/d/1S4NKKcsLgQ_jHqGBixq4bRkXiV0Z0WPiQ6ztjj4Y1T0/view
---

**OpenAI julkisti GPT-6 Cyberin — malli löysi jo 81 tuntematonta haavoittuvuutta Firefoxista**

Mobiili.fi 6.11.2026. OpenAI on julkaissut GPT-6 Cyber -mallin, joka on
suunnattu erityisesti kyberturvallisuustehtäviin: haavoittuvuuksien
löytämiseen, korjausten kehittämiseen ja turvallisuusrajojen
noudattamiseen. Malli on saatavilla aluksi Daybreak Red -ohjelmassa
rajatulle käyttäjäjoukolle luvalliseen red teaming -testaukseen.
OpenAI:n mukaan GPT-6 Cyber on löytänyt Firefoxista vähintään 81
aiemmin tuntematonta haavoittuvuutta, kehittänyt
hyväksikäyttömenetelmiä 948 Linux-ytimen haavoittuvuuteen sekä
löytänyt ja validoinut kriittisen etäkoodinsuorituksen mahdollistavan
haavoittuvuuden Brotli-pakkauskirjastosta; löydöksistä on ilmoitettu
ylläpitäjille ja ne on korjattu. Kehityksessä on keskitytty tehtävän
rajauksen ja käyttäjän aikomuksen ymmärtämiseen: tiukemmat identiteetti-
ja tiliturvavaatimukset, tarkistuspisteet korkean riskin toiminnoille
ja lisävalvonta sääntöpoikkeamissa. Taustalla kesän tapaukset, joissa
malleja on onnistuttu poistamaan testiympäristöistään; mallia koulutettiin
mm. Hugging Face -tapausta jäljittelevillä simuloiduilla arvioilla.
OpenAI täsmensi myös Daybreak Blue -ohjelman tietokäytäntöjä: käyttäjä
voi kieltäytyä istuntojen hyödyntämisestä mallikoulutuksessa.

Merkitys SecPromiselle: tekoälypohjainen haavoittuvuustutkimus
teollistuu — vaikuttaa suoraan SecPromisen haavoittuvuusarviointi- ja
testauspalveluiden tulevaisuuteen; mallin turvamekanismit (rajaukset,
tarkistuspisteet, valvonta) ovat myös oman AI SOC -suunnitelman
vertailukohta.
