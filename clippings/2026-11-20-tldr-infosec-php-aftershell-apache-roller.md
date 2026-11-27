# 2026-11-20 — TLDR Information Security

- **Kategoria:** vulnerabilities
- **Tunnisteet:** rce, deserialization, php, ruby, apache-roller, malvertisements
- **Lähde:** TLDR Information Security (dan@tldrnewsletter.com), 2026-11-20
- **Gmail-aihe:** "phpAfterShell Brings More RCEs 🐚, Muse Worries Meta Staff 😟, GTA 6 Hacker Arrested 🚗"

## Keskeiset uutiset

1. **Apache Roller 4.0.0-6.1.4 sisältää tunnuksettoman deserialisointivian XML-RPC-päätepisteessä ja sitä hyödynnetään aktiivisesti.** Paikkaus on 6.1.6; viivästyksessä poista /roller-services/xmlrpc -mappaus WEB-INF/web.xml:stä ja käynnistä uudelleen.
2. **Ruby2Shell: yksibyteinen keikkavuoto Rubyn single-byte-koodauksissa** (ß muuttuu SS:äksi upcasessa, mutta tarkistus lukee vain yhden tavun). GitHub Enterprise Server, GitLab ja muut vaikuttavat.
3. **PHP Foundation paikkasi seitsemän kriittistä vikaa; yksi, phpAfterShell, voidaan kytkeä mielivaltaiseen deserialisointiin ja RCE:hen** missä tahansa sovelluksessa, joka ajaa tiedostopohjaisia sessioita haavoittuvalla PHP-versiolla.
4. **EggStreme-malware rakennettiin uudelleen julkistuksen jälkeen:** AES-256-CBC-konfiguraatiot, RC5- ja räätälöity CBC-koodaus, gRPC:n tilalle raaka TCP keskinäisen TLS:n yli; uudet komennot luettelevat AD:tä, ajavat WMI:tä, imitoivat tokeneita ja lataavat .NET-kokonaisuuksia. Kohteina Filippiinien viranomaiset (korkea luottamus) ja Taiwan (matala-keskitaso).
5. **Kubernetesin lokilähteet ja sokeat pisteet:** solmun tapahtumat, API:n ohittavat kubelet-tapahtumat ja kubectl exec -kuoret jäävät helposti valvonnan ulkopuolelle; artikkelissa myös käytännön asennusohjeet.
