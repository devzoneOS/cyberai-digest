# agenttiparvet-rust-migraatio

- **Päivämäärä:** 2026-11-26
- **Lähde:** TLDR (dan@tldrnewsletter.com)
- **Gmail-aihe:** "Scaling agent swarms 🤖, Anthropic’s Rust migration 🦀, Search for Agents 🔍"
- **Kategoria:** ai_news
- **Tunnisteet:** hugging-face, agenttiparvet, anthropic, rust, redis, kafka, cloudflare, matematiikka

## Keskeiset uutiset

- **Hugging Face skaalasi parven 1 000 agenttiin.** Yhdeksässä päivässä 1 000 DeepSeek-agenttia rakensi PyBotin, 175 000 viestiä ja 8 500+ yhdistettyä PR:ää tuottaen. Suurimmat pullonkaulat olivat inferenssissa, työkalukutsuissa ja Gitissä.

- **Anthropicin Messages API siirtyi Rustiin.** Varjoliikenne varmisti toiminnon samanlaisuuden Python-toteutuksen kanssa. Siirto leikkasi CPU-käyttöä noin 70 % ja ensimmäisen tokenin mediaaniajan noin 20 % ilman katkoja.

- **Redisin tilalle Kafka ja yksi kirjoittaja.** Autumn korvasi Redis-cacheen perustuneen arkkitehtuurin järjestyneellä Kafka-lokilla ja yhdellä balanssikirjoittajella per asiakas. P99 viive laski 108 ms:stä 25 ms:iin.

- **Cloudflare Search for Agents.** Kytkin indeksoi sivuston ja tarjoaa hakupäätepisteen sivuston omalla domainilla, joka palauttaa vastaavuudet Markdownina lähdeluetteloin.

- **Alarajat kertovat edistyksestä.** AI-laboratoriot raportoivat tuloksia vanhoista matematiikan ongelmista, kuten matriisikertolaskun ja Fourier-muunnoksen ylä- ja alarajoista. Ala todistus P≠NP:stä voi olla kohta ulottuvissa.
