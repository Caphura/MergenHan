---
id: mh-blueprint-onboarding-router
title: Onboarding Router
type: blueprint
status: stable
version: 1.0.0
summary: Kullanici talebini dogru varlik tipine veya repo aksiyonuna yonlendiren, testlerle dogrulanmis evrensel onboarding blueprint'i.
tags:
  - routing
  - workflow
  - documentation
depends_on:
  - mh-module-context-audit
  - mh-module-repo-architecture
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-04-04
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Kullanici talebinin hangi icerik tipine, klasore veya bakim aksiyonuna yonlenmesi gerektigini belirleme istegi.
output_contract: Talebin `master`, `module`, `blueprint`, `skill`, `packaging`, `catalog` veya `adapter mapping` aksiyonlarindan birine acik sekilde yonlendirilmesi.
notes: Bu blueprint siniflandirma ve yonlendirme davranisini cekirdekte tutar; runtime'a ozel onboarding UI detaylari adapterlere birakilir. Farkli AI denemelerinde genel olarak basarili bulunmus, ancak `master` ile `blueprint` ayrimini karistiran sapmalar goruldugu icin skill paketine terfiden once bu routing ayriminin dilsel olarak daha da keskinlestirilmesi faydali olabilir.
---

# Responsibility

Kullanicinin talebini once anlam, sonra repo icindeki dogru aksiyona yonlendir.

# Trigger Signals

- "Bunu nereye koymaliyim?"
- "Bu bir module mu, master mi, skill mi?"
- "Paketlemeli miyiz?"
- "Kataloga mi eklenmeli yoksa adapter mi yazilmali?"

# Workflow

1. Talebin amacini, tekrar kullanilabilirlik duzeyini ve baglam genisligini belirle.
2. Icerigi su kategorilerden birine yonlendir: `master`, `module`, `blueprint`, `skill`, `packaging`, `catalog`, `adapter mapping`.
3. Eger karar tekrar kullanima dayaniyorsa bagimlilik adaylarini acikca listele.
4. Eger runtime'a ozel bir istek varsa cekirdek degil adapter katmanina yonlendir.
5. Sonucu kisa bir karar ozeti ve onerilen sonraki adimla bitir.

# Routing Heuristics

Asagidaki ayrimlari acik ve tutarli sekilde koru:

- `module`: baska promptlarda da tekrar kullanilabilecek atomik bir davranis, kural veya output parcasiysa
- `master`: tek bir gorevi bastan sona cozen, birden fazla davranisi ayni akista orkestre eden prompt ise
- `blueprint`: artik skill davranisi tasiyorsa ama paketlenmis `skills/` klasorune gecmek icin henuz erken ise
- `skill`: davranis tekrarli testlerden gecmis, paketlenmeye hazir ve `SKILL.md` + `meta.yaml` yapisina tasinacak kadar olgun ise
- `packaging`: kullanici yeni davranis yazmak degil, mevcut bir blueprint'i skill paketine cevirmek istiyorsa
- `catalog`: konu yeni icerik yazmak degil, katalog uretimi, metadata veya dependency kayitlarini guncellemek ise
- `adapter mapping`: istek runtime'a, project instruction'a, tool wiring'e veya provider-specific kullanim notlarina ozelse

Ozellikle su iki hatadan kacin:

- Tek gorevlik ama orkestre prompt akisini erken `blueprint`e itme; bu tip icerikler once cogunlukla `master` olarak baslar.
- Talep siniflandirma ve repo icinde yonlendirme davranisi tasiyorsa bunu otomatik olarak `master` yapma; tekrar kullanilabilir routing mantigi guclu ise `blueprint` daha dogru olabilir.

# Decision Output Discipline

Karar verirken yalnizca sonucu soyleme; neden o yone gittigini de baglam genisligi, tekrar kullanilabilirlik ve paket olgunlugu eksenlerinde acikla.

Mumkunse su mantigi izle:

1. Bu talep yeni bir icerik mi, mevcut icerigin terfisi mi, yoksa bakim/adapter isi mi?
2. Davranis atomik mi, tek gorevlik orkestrasyon mu, yoksa paketlenmeye aday tekrar kullanilabilir beceri mi?
3. Sonraki en kucuk mantikli adim nedir?

# Promotion Criteria

- Router sinyalleri tekrar eden onboarding ihtiyaclarinda net fayda sagliyorsa
- Karar ciktisi farkli adapterlerde de degismeden korunabiliyorsa
- Repo yeni katilimcilari icin tutarli yonlendirme dili olusturuyorsa
