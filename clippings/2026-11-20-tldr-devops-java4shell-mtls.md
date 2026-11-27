# 2026-11-20 — TLDR DevOps

- **Kategoria:** vulnerabilities
- **Tunnisteet:** openjdk-rce, mtls, flaky-tests, ai-sandboxing, kernel-compilers
- **Lähde:** TLDR DevOps (dan@tldrnewsletter.com), 2026-11-20
- **Gmail-aihe:** "OpenJDK RCE 🥷, Flaky Test Landscape ❄️, Megakernels 🍿"

## Keskeiset uutiset

1. **Java4Shell (CVE-2026-114938, CVSS 9.2): OpenJDK:n AVX-512 Base64-dekoodauksen muistivika aiheuttaa keon korruptoitumisen.** Koskee OpenJDK 17.0.6+ x86-64-laitteistossa ja mahdollistaa pre-auth RCE:n Jenkinsissä, Confluencessa ja Tomcatissa. Päivitä OpenJDK tai poista Base64-intrinsics käytöstä heti.
2. **AWS Network Load Balancer tuo mTLS-tuen:** asiakasvarmenteiden validointi siirtyy taustapalveluilta kuormantasaajalle (trust store, sulkulista- ja identiteettisuodattimet).
3. **IEEE-tutkimus 8,8 miljardista testiajosta: 9,8-16,3 % epäonnistuneista ajoista liittyi havaitsemattomiin hauraustesteihin.** Vertailu seitsemästä haurausvälinetyökalusta: toimittajat eroavat enemmän karanteenissa, palautuksessa ja käyttöönotossa kuin havaitsemisessa.
4. **Onko AI pelkkä kolmannen osapuolen riippuvuus? incident.io:n insinöörit: lähes kyllä** (SLA:t, SLO:t ja observability pätevät), mutta mallin laadun mittaus ja debuggaus ovat vaikeampia.
5. **Together AI poisti viimevuoden megakernelit ja korvasi ne Together Compilerilla:** AI-agentit kirjoittavat ja fuusioivat GPU-kernelit uudelleen; B200:llä 28 % parempi tulos (2 118 vs 1 649 tokenia/s) Llama 3.2 1B:llä.
6. **AWS Nitro Sandboxes EKS:in: jokainen agentti ajaa omassa kernelissä Nitro-hypervisorin valvomassa VM:ssä** mallin tuottaman koodin eristämiseksi.
