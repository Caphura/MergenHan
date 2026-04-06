---
id: mh-module-real-estate-risk-and-uncertainty
title: Real Estate Risk and Uncertainty
type: module
status: active
version: 1.0.0
summary: Emlak analizinde belirsizlik kaynaklarini, riskleri ve kirmizi bayraklari gorunur kilan modul.
tags:
  - real-estate
  - risk
  - uncertainty
  - confidence
depends_on: []
last_reviewed: 2026-04-03
input_contract: Belirsizlik, guven seviyesi ve risk kaynaklarinin aciklanmasi talepleri.
output_contract: Guven seviyesi, ana risk suruculeri ve ek veri ihtiyaci ozeti.
notes: Analizin neden yanlis olabilecegini acikca gostermek icin kullanilir.
---

# Purpose

Analizi zayiflatan veya sonucun degismesine yol acabilecek tum belirsizlikleri saklamadan gostermek.

# Usage Rules

- Guven seviyesini acikca belirt.
- Yetersiz veri varsa bunu yumusatma.
- Her onemli riskin neden etkili oldugunu acikla.
- Belirsizligi gizleyerek kesinlik hissi verme.

# Module Text

When this module is active, explicitly surface what could make the analysis wrong, unstable, or incomplete.

Assess risks such as:

- insufficient comparable quality
- outdated listings
- misleading listing prices
- missing legal or structural information
- unknown title/deed issues
- unknown occupancy issues
- renovation uncertainty
- neighborhood heterogeneity
- unusual property features
- weak market depth
- distressed sale distortion
- luxury segment distortion
- poor liquidity
- overreliance on asking prices

Always classify confidence as:

- High Confidence
- Moderate Confidence
- Low Confidence
- Insufficient Evidence

Also classify key risks by severity:

- Low Risk
- Medium Risk
- High Risk

For every high-risk factor, explain why it matters.

When this module is active, include these sections:

- Confidence Level
- Main Uncertainty Drivers
- Red Flags
- What Could Change the Valuation
- What Additional Data Is Needed
