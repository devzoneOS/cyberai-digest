# 2026-11-20 — TLDR Dev

- **Kategoria:** ai_news
- **Tunnisteet:** performance-engineering, coding-evals, postgresql, sqlite, docker
- **Lähde:** TLDR Dev (dan@tldrnewsletter.com), 2026-11-20
- **Gmail-aihe:** "OpenAI's performance factory 🏭, hardware is software 🔩, PostgreSQL 19 🌱"

## Keskeiset uutiset

1. **OpenAI:n "suorituskykutehdas": kun ChatGPT hidastuu, yksi Codex-istunto tutkii ja toinen yrittää kumota selityksen ennen korjausta.** Julkaisun jälkeen Codex varmistaa suorituskyvyn palanneen lähtötasolle; yhdessä tapauksessa tarkistaja avasi tutkinnan uudelleen, kun syyllistetty palvelu oli jo toipunut.
2. **Stripe evals -benchmark: koodausagentit täyttivät keskimäärin 78,1 % vaatimuksista, mutta vain 29,4 % ajoista täytti kaikki.** Kaikki 14 agenttikonfiguraatiota päräsivät paremmin Striplen liitännäisellä.
3. **Spotifyn kriteeri offline-evaluaatiolle:** mittauskolhu saa offline-arvion selittämään vain 24 % verkkovaikutuksista mallinnetun 60 %:n sijaan; rajatapaukset menevät A/B-testiin ja osa päätöksistä auditoi sattumanvaraisesti.
4. **Chromeen: koodausagentit läpäisivät 52 % web-kehityksen tarkistuksista ilman ohjeita ja 91 % Modern Web Guidance -asennettuna.** Tyypillisiä virheitä: kohdistuksen palautus dialogin sulkemisen jälkeen, reduced-motion, sisällön tilan varaaminen.
5. **PostgreSQL 19: rinnakkainen taulun repack tilanpalautukseen ilman katkoa, valmiustietueen kirjoituksen odotus ja INSERT ... ON CONFLICT -rivin suora palautus.**
6. **Zerodhan Blobasaur: Redis-yhteensopiva blob-säilö, joka sirpaloittaa tiivistettyjä JSON-kuormia SQLite-tiedostoihin; 16 sirpaleella kirjoitusnopeus nousi noin 7 700:sta 25 300 operaatioon sekunnissa.**
