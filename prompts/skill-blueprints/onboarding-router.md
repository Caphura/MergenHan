---
id: mh-blueprint-onboarding-router
title: Onboarding Router
type: blueprint
status: draft
version: 0.1.0
summary: Kullanici talebini dogru varlik tipine veya repo aksiyonuna yonlendiren evrensel onboarding taslagi.
tags:
  - routing
  - workflow
  - documentation
depends_on:
  - mh-module-context-audit
  - mh-module-repo-architecture
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-04-03
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
notes: Bu blueprint siniflandirma ve yonlendirme davranisini cekirdekte tutar; runtime'a ozel onboarding UI detaylari adapterlere birakilir.
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

# Promotion Criteria

- Router sinyalleri tekrar eden onboarding ihtiyaclarinda net fayda sagliyorsa
- Karar ciktisi farkli adapterlerde de degismeden korunabiliyorsa
- Repo yeni katilimcilari icin tutarli yonlendirme dili olusturuyorsa
