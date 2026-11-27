# 2026-11-18 — TLDR Information Security

- **Kategoria:** cyber_news
- **Tunnisteet:** supply-chain, java4shell, ml-backdoors, browser-extension-rce, loader-malware
- **Lähde:** TLDR Information Security (dan@tldrnewsletter.com), 2026-11-18
- **Gmail-aihe:** "Java4Shell RCE ☕️, Backdoors Against ML 🚪, NSA Net Disrupted ⛓️‍💥"

## Keskeiset uutiset

1. **WPPConnect vioitettiin projektin omassa julkaisuputkessa:** ylläpitäjätilin kauttaviety kommit toimittivat "diagnostiikka"-moduulin, joka lhti ympristmuuttujat, .env-tiedostot ja WhatsApp-session tokenit Telegram-bottiin - pteos ajaa importissa, joten --ignore-scripts ei auta, ja julkaisutag pakotettiin osoittamaan siistin nkisevn kommitiin kelvollisella SLSA-provenienssilla.
2. **Infoblox vahvisti tietoturvaloukkauksen kolmannen osapuolen SharePoint-siirtotoimittajan kautta**; tuotteet, pilvipalvelut ja build-julkaisuprosessit eivt olleet mukana, mutta lhde kertoo asiakastietojen varastetuksi.
3. **Java4Shell (CVSS 9.2): OpenJDK:n Base64-dekooderin ksin kirjoitetussa AVX-512 VBMI -assemblyssa 64 "A"-merkin syte ylitt muistisegmentin** - koskee Confluencea, Jiraa, Artifactorya, Keycloakta ja Elasticsearchi.
4. **ONNX-mallien takaovet: hyvntahtoinen Qwen2-malli vuotaa tiedostoja tai muistia palvelinverkosta laukaisusanan jlkeen** hyvksikyttmll ONNX Runtime -parserin tiheiden tensorien haittaa ennen polkutarkistusta; onnxruntime >= 1.27.0 ja mallien auditointi kuin epluotetun lhddekoodin.
5. **BubbleLoader muuttaa lailliset exet (WinRAR, x64dbg, Firefox) droppereiksi:** PNG XOR-avaimena, feikki-PNG shellcodella, jokaisella ajolla muuttuva tiiviste (CPU-aikaleima kompilaattorin tyynypaddingiin). Puolustus: koodiallekirjoitusten tarkistus, RWX-VirtualAlloc-hlytykset ja typistetyn IHDR:n lippuaminen.
6. **Sign2Shell: Brasilian viidest asennetuimmasta allekirjoitusliitnnisest (CVSS 9.6) jokaisessa drive-by RCE:** sivustot voivat valita natiiviprosessin lataamat DLL:t ilman polku- tai Authenticode-tarkistusta.
