# 2026-11-09 — TLDR Information Security

- **Kategoria:** vulnerabilities
- **Tunnisteet:** ssh, certificate-authority, data-breach, supply-chain, virtualization
- **Lähde:** TLDR Information Security (dan@tldrnewsletter.com), 2026-11-09
- **Gmail-aihe:** "*sshole Alpine SSH bug 🐛, DigiCert data breach 🔐, Claude sandbox escape 🤖"

## Keskeiset uutiset

1. **"Starsshole" sallii salasananoton Alpine-Linux-järjestelmiin (OpenSSH + musl, ilman PAM:ia).** Aktiivisella salasanattomalla tilillä yli 256 merkin salasanakenttä antaa kirjautumisen yhdellä yrityksellä; korjaukset on julkaistu.
2. **DigiCertin tietomurta (27.6.–2.7.):** hyökkääjä loi read-only-tilin paljastuneeseen arkistojärjestelmään ja pääsi käsiksi asiakkaiden yhteystietoihin ja osin henkilöllisyysdokumentteihin; varmennepalveluihin ei vaikuttanut.
3. **Iris Ohyaman kolmannen osapuolen pilvimurta paljasti 7,7 miljoonan asiakkaan tiedot.** Mukana nimiä, osoitteita, puhelinnumeroita, syntymäaikoja ja (salattuja) salasanoja.
4. **LiteLLM 1.107.0 -julkaisun myrkyttämisketju:** toukokuussa julkiseen repoonsa unohdettu admin-avain ei koskaan peruttu; lokakuussa sillä nostettiin omistajan GitHub-avain, kaarrettiin haarasuojaus ja julkaistiin myrkytetyt wheel-paketit kahdeksi tunniksi.
5. **Virtualisointirikollisuus:** BlackNevas-kiristyshaittaohjelma käytti PRTG:ssä tallennettua ESXi-root-salasanaa ja Proxmox-klusteri kaapattiin adminin muistiinpanoista löytyneillä tekstillä olevilla tunnuksilla.
