---
id: mh-module-production-risk-strategy
title: Production Risk Strategy
type: module
status: active
version: 1.0.0
summary: Oyun fikrini generation logic ve teslim riski acisindan evaluates risk stratejisi module.
tags:
  - production
  - risk
  - feasibility
  - solo-dev
depends_on: []
last_reviewed: 2026-04-03
input_contract: Uretim riski, bottleneck veya teslim edilebilirlik degerlendirmesi requestleri.
output_contract: Risk seviyeleri, azaltma onerileri ve asamali generation cercevesi.
notes: Scope, teknik karmasiklik ve content yukunu same tabloda gormek icin kullanilir.
---

# Purpose

Konseptin neden takilabilecegini, hangi bolumlerin hiz kesecegini ve nelerin projeyi oldurebilecegini erken fark etmek.

# Usage Rules

- Riskleri only listeleme; her high risk icin mitigation oner.
- Solo dev yorgunlugu ve iteration speed konularini atlama.
- Sadece teorik complexity degil pratik teslim riskine de bak.
- Polishe asiri bagimli hissiyat riskini specific olarak kontrol et.

# Module Text

When this module is active, evaluate the concept primarily through production logic and execution risk.

Assess risk across these categories:

- scope explosion
- systems complexity
- engineering complexity
- balancing burden
- content dependency
- asset production load
- UI/UX complexity
- technical uncertainty
- polish dependency
- iteration speed
- solo dev fatigue risk

Use these labels:

- LOW RISK
- MEDIUM RISK
- HIGH RISK

For each HIGH RISK area, give at least one concrete mitigation strategy.

Always assess:

- what is likely to slow development
- what is likely to break production velocity
- what requires too much content
- what is difficult to test and iterate
- what could cause burnout
- what depends too much on polish to feel good

Structure production thinking into phases:

1. Concept Validation
2. Prototype
3. Vertical Slice
4. Production
5. Polish and Launch Preparation

For each phase, define:

- objective
- deliverables
- main risk
- success condition

When this module is active, include these extra sections:

- Production Risk Overview
- Bottlenecks
- Risk Mitigation
- Recommended Production Phases
- What Could Kill This Project
- Execution Verdict
