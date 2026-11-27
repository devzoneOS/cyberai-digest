# 2026-11-26 — TLDR InfoSec

- **Kategoria:** vulnerabilities
- **Tunnisteet:** 1password, todoist, github, ci-cd, check-point, gt13
- **Lähde:** TLDR Newsletter (dan@tldrnewsletter.com)
- **Gmail-aihe:** 1Password incident, Check Point hacked, EU Academy PII Breach

## Keskeiset uutiset

1. Hyökkääjä otti hallintaansa 1Passwordin työntekijän yritys-GitHub-tilin ja työnsi haitallista koodia taustajärjestelmiin, jotka imivät käyttäjien nimiä, sähköpostiosoitteita, SRP-parametreja sekä kutsu- ja palautustokeneja sekä pääsivät lähdekoodiin ja CI/CD-salaisuuksiin. Holvit ja niiden avaimet eivät paljastuneet, ja varastetut tokenit ovat hyödyttömiä ilman SSO:a tai sähköpostikoodia, jonka pituutta 1Password nosti kuudesta numerosta kymmeneen merkkeihin.

2. Todoist kertoi, että varastetuilla versiohallinnan tunnuksilla hyökkääjät muuttivat automaattisia työnkulkuja ja pääsivät pilvijärjestelmiin työntekijätilin kautta. Noin 6 prosentin käyttäjien sähköpostiosoitteet, suolatut SHA1-salasanatiivisteet ja tilinluontipäivät paljastuivat.

3. GreyNoise seuraa GT13-nimistä toimijaa, joka hyökkäsi vähintään 22 organisaatioon energia-, rahoitus-, julkishallinto- ja teollisuussektoreilla. Toimija käytti 99 IP-osoitetta, automatisoitua skannausta ja väärennettyä HFS-ylläpitäjän istuntotokenia kaatakseen Check Point Security Management -palvelimet ja ekstrafoi dataa 24 palvelimelta.

4. Artikkelissa kehotetaan turvatiimejä harkitsemaan uudelleen haavoittuvuusten käsittelymallia: uhkamallinnusagentit rakentavat proaktiivisen näkymän organisaation alttiudesta, jota voidaan käyttää uusien haavoittuvuuksien julkistusten yhteydessä.

5. EU Academy -oppimisalustan PII-tietomurrosta tiedottavat EU:n toimeenpaneva virasto ja EU:n kyberagentti.
