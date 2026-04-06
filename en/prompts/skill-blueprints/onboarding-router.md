---
id: mh-blueprint-onboarding-router
title: Onboarding Router
type: blueprint
status: stable
version: 1.0.0
summary: Kullanici talebini correct asset tipine veya repo aksiyonuna yonlendiren, testlerle dogrulanmis evrensel onboarding blueprint'i.
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
input_contract: Kullanici talebinin hangi content tipine, klasore veya maintenance aksiyonuna yonlenmesi gerektigini belirleme istegi.
output_contract: Talebin `master`, `module`, `blueprint`, `skill`, `packaging`, `catalog` veya `adapter mapping` aksiyonlarindan birine clear way yonlendirilmesi.
notes: This blueprint siniflandirma ve guidance davranisini corete tutar; runtime'a specific onboarding UI detaylari adapterlere birakilir. Farkli AI denemelerinde genel olarak basarili bulunmus, ancak `master` ile `blueprint` ayrimini karistiran sapmalar goruldugu icin skill paketine terfiden once bu routing ayriminin dilsel olarak daha da keskinlestirilmesi faydali olabilir.
---

# Responsibility

Kullanicinin talebini once anlam, sonra repo icindeki correct aksiyona yonlendir.

# Trigger Signals

- "Bunu nereye koymaliyim?"
- "Bu bir module mu, master mi, skill mi?"
- "Paketlemeli miyiz?"
- "Kataloga mi eklenmeli yoksa adapter mi yazilmali?"

# Workflow

1. Talebin amacini, tekrar kullanilabilirlik duzeyini ve context genisligini belirle.
2. Icerigi su kategorilerden birine yonlendir: `master`, `module`, `blueprint`, `skill`, `packaging`, `catalog`, `adapter mapping`.
3. Eger decision tekrar usagea dayaniyorsa dependency adaylarini explicitly listele.
4. Eger runtime'a specific bir request varsa core degil adapter katmanina yonlendir.
5. Sonucu short bir decision ozeti ve onerilen sonraki adimla bitir.

# Routing Heuristics

Asagidaki ayrimlari clear ve tutarli way koru:

- `module`: baska promptlarda da tekrar kullanilabilecek atomik bir davranis, rule veya output parcasiysa
- `master`: tek bir taski bastan sona cozen, birden fazla davranisi same akista orkestre eden prompt ise
- `blueprint`: artik skill davranisi tasiyorsa ama paketlenmis `skills/` klasorune gecmek icin henuz erken ise
- `skill`: davranis tekrarli testlerden gecmis, paketlenmeye ready ve `SKILL.md` + `meta.yaml` yapisina to carry over kadar olgun ise
- `packaging`: user yeni davranis yazmak degil, mevcut bir blueprint'i skill paketine cevirmek istiyorsa
- `catalog`: topic yeni content yazmak degil, katalog uretimi, metadata veya dependency kayitlarini currentlemek ise
- `adapter mapping`: request runtime'a, project instruction'a, tool wiring'e veya provider-specific usage notlarina ozelse

Ozellikle su iki hatadan kacin:

- Tek tasklik ama orkestre prompt akisini erken `blueprint`e itme; bu tip icerikler once cogunlukla `master` olarak baslar.
- Talep siniflandirma ve repo icinde guidance davranisi tasiyorsa bunu otomatik olarak `master` yapma; tekrar kullanilabilir routing logic guclu ise `blueprint` daha correct olabilir.

# Decision Output Discipline

Karar verirken only sonucu soyleme; neden o yone gittigini de context genisligi, tekrar kullanilabilirlik ve package olgunlugu eksenlerinde acikla.

Mumkunse su logic izle:

1. Bu request yeni bir content mi, mevcut icerigin terfisi mi, yoksa maintenance/adapter isi mi?
2. Davranis atomik mi, tek tasklik orkestrasyon mu, yoksa paketlenmeye aday tekrar kullanilabilir beceri mi?
3. Sonraki en kucuk mantikli step nedir?

# Promotion Criteria

- Router sinyalleri tekrar eden onboarding ihtiyaclarinda net fayda sagliyorsa
- Karar outputsi different adapterlerde de degismeden korunabiliyorsa
- Repo yeni katilimcilari icin tutarli guidance dili olusturuyorsa
