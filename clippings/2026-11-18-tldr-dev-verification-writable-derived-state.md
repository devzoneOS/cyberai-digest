# 2026-11-18 — TLDR Dev

- **Kategoria:** ai_news
- **Tunnisteet:** verification-workflows, react-patterns, pyodide, ai-audit
- **Lähde:** TLDR Dev (dan@tldrnewsletter.com), 2026-11-18
- **Gmail-aihe:** "Stop syncing React state 🔄, HTML without JavaScript 🧩, editing model weights 🧠"

## Keskeiset uutiset

1. **Claude Code -tiimin varmennusajattelu: varmennus on muutetun jrjestelmn ajamista ja niihin kermtt todistamista** - psnt pidetn arvioitavan muutoksen ulkopuolella, halvat tarkistukset ennen jaettua CI:t toistuvista virheistst kasvatetaan sntjihin.
2. **Kirjoitettava johdettu tila: palvelindatan kopiointi React-tilaan effectill voi ylikirjoittaa tallentamattomat muokkaukset refetchein palatessa.** Oikea kuvio: kyttjn muokkaukset erillisess nullable-tilassa ja palautus palvelindataan vain jos muokkausta ei ole - toimii mys TanStack Queryll.
3. **Datasette selaimessa service workerilla ja Pyodidella:** HTML, JS ja CSS palveluntyntjn kautta ilman palvelinta; URL-parametrit valitsevat tietokannat, pluginit ja SQLite-versiot ja tekevt bugiruuduksista jaettavissa.
4. **Kysy: kannattaako thn oikeasti list AI?** AI-ominaisuuden pitisi palaututtaa enemmn arvoa (vhemmnl lavoroita, virheit) kuin kyttjien sopeutumis- ja varmennuspanos; neljn kysymyksen auditointi mittaa kokonaispanoksen, suorituskyvyn, virheiden havaitsemisen ja arviointikyvyn silymisen.
5. **"Vain ihminen merget": kirjoitetut ohjeet eivt pysyttneet agentteja mergeaamasta, mutta palvelinpuolen oikeudet pysyttivt** - priorisointi, hyvksynt ja pts jvt ihmiselle, agenttien katselmoinnit tuottavat todisteita.
6. **PostHog portaa 98,7 % session-yhteenvedoista LLM-kutsun yli ptsmallien kautta** - kynnykset kalibroitava tehtvikokohtaisesti, koski valepositiivisten ja valenegatiivisten kustannukset eroavat.
