# 2026-11-17 — TLDR Information Security

- **Kategoria:** vulnerabilities
- **Tunnisteet:** ruby-rce, kernel-dos, agentic-offensive-frameworks, data-breach
- **Lähde:** TLDR Information Security (dan@tldrnewsletter.com), 2026-11-17
- **Gmail-aihe:** "Agentic Offensive Frameworks 😈, Apple Secure Enclaves 🍎, California AG Sues OpenAI 👨‍⚖️"

## Keskeiset uutiset

1. **httpx 1.9.0 (Ruby): Oj-objektitilassa jäsennetty JSON-vastaus antoi pahantahtoisen palvelimen muuttaa vastauksensa mielivaltaisiksi Ruby-objekteiksi (CVE-2026-129784, CVSS 8.5).** JFrog ketjutti ActiveSupport-luokat Kernel.load-kutsuun multipart-laatalla ladatun tiedoston kautta - RCE ilman kyttijn vuorovaikutusta. Pivitys 1.9.1, mode: :strict tai multi_json pssll.
2. **Maileva (Ranskan posti-konserni): 22 miljoonan ihmisen nimet ja postiosoitteet paljastuivat kyberhykkyyksess.** Ranskan kyberrikollisyksikko tutkii.
3. **NoisyTCP: 11 vuotta vanha Linux-ytimen NULL-osoitin-vika kaataa Nginx-, Apache- ja SSH-palvelimet oletusasetuksilla** tunnuksettomien hykkjien laukaisemalla kilpailutilalla; DoS-ketju.
4. **Elasticin analyysi viidest agenteettomasta hykkyskehyksest (ARTEX, CyberStrikeAI, Cairn, PentAGI, HexStrike):** LLM ajaa skannereita, kuoria ja pilvi-CLI:t 2-25 sekunnin purskeissa; yksikn ei valvo valtuutusta koodissa, ARTEX ja CyberStrikeAI vaihtavat proxia ja User-Agentia torjunnassa. GTIG/Mandiant on nhtnyt nelj todellisissa murroissa; ARTEX on kytketty Storm-0940:een. Puolustus: ennalta valitut automaattiset containement -ptspt, IP-estot + token/sessiosidonnaiset peruutukset ja identiteettien toimintanopeuden seuranta.
5. **Applen Secure Exclaves: eristet ajot lat, jotka ksittelevt mikrofoni- ja kameradataa pstelmist erilln** - ympristvhnt tunnistus tuottaa vain rajattua metadataa, raakani ja -video pysyvt suljettuina.
