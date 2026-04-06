---
id: mh-blueprint-apartment-investment-analyzer
title: Apartment Investment Analyzer
type: blueprint
status: stable
version: 1.0.0
summary: Apartman satis listinglarini investment odakli, evidence ve uncertainty ayrimini koruyan yapisal bir analysis formatina donusturen dogrulanmis real estate blueprint'i.
tags:
  - real-estate
  - apartment-analysis
  - investment
  - decision-support
depends_on:
  - mh-master-ultimate-real-estate-market-and-valuation-strategist-core
  - mh-module-real-estate-market-data-validation
  - mh-module-real-estate-comparable-analysis
  - mh-module-real-estate-valuation-logic
  - mh-module-real-estate-risk-and-uncertainty
  - mh-module-real-estate-investment-decision-support
  - mh-module-real-estate-no-hallucination-governance
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
input_contract: Tek bir apartman listingi, birden fazla apartman satis listingi veya investment shortlist'i talebini evidence temelli ve decision odakli bicimde analysis etme istegi.
output_contract: Scope Summary, Market Snapshot, Listing-by-Listing Analysis, Rental Potential, Payback / Yield Estimate, Risks and Unknowns, Top Candidates ve Recommended Next Checks bolumlerinden olusan taranabilir apartment investment analysis.
notes: This blueprint different AI ortamlarda test edilmis ve decision destekleyici output structure, risk/uncertainty disiplini ve apartman listingi odagi acisindan yeterli bulunmustur. Hukuki gorus, resmi ekspertiz, arsa / imar analysis, ticari gayrimenkul analysis veya finansman planlamasi uretmez.
---

# Responsibility

Tek bir apartman listingi veya birden fazla apartman satis listingini, gercek decision vermeyi destekleyen investment odakli ve uncertainty bilinci tasiyan yapisal bir analize donusturmek.

# Trigger Signals

- "Bu daire investment icin mantikli mi?"
- "Bu listinglari investment acisindan karsilastir."
- "Hangisi daha iyi kira getirisi verir?"
- "Bu apartman listinglarindan shortlist cikar."
- "Kaniti assumptiondan ayirarak analysis et."

# Workflow

1. Analiz kapsamini belirle: tek bir apartman, birden fazla apartman listingi veya investment shortlist'i talebi.
2. Mevcut evidencei normalize et: fiyat, brut / net m2, oda sayisi, kat, bina yasi, konum / mahalle, belirtilen durum ve listing kalitesini separate; eksik veriyi not et.
3. Ilanlarin olasi piyasa konumunu belirle: piyasanin altinda, piyasa civarinda, piyasanin ustunde veya yetersiz veri nedeniyle belirsiz.
4. Yatirim usage degerini kabaca incele: kira potansiyeli, kaba geri donus / brut getiri logic, likidite / kiralanabilirlik ve gerekiyorsa pazarlik hassasiyeti.
5. Risk ve uncertaintyleri surface: zayif listing kalitesi, eksik veya supheli veri, asiri fiyatlama riski, tadilat / durum riski, mahalle belirsizligi ve dogrulanmasi gereken evidence bosluklari.
6. Karar dostu bir output uret: scope ozeti, listing bazli analysis, kira potansiyeli, geri donus / getiri logic, riskler ve bilinmeyenler, guclu adaylar ve sonraki kontrol steps.
7. Tum output boyunca evidence ile assumptioni ayir, belirsizligi etiketle, false certaintyten ve garanti investment dili kullanmaktan kacin.

# Output Shape

Sonucu mumkun oldugunca su yapida toplula:

- Scope Summary
- Market Snapshot
- Listing-by-Listing Analysis
- Rental Potential
- Payback / Yield Estimate
- Risks and Unknowns
- Top Candidates
- Recommended Next Checks

Her bolumde:
- evidence ile assumptioni ayir
- belirsizligi explicitly etiketle
- false precision kullanma
- garanti investment dili kullanma

# Promotion Criteria

- Birden fazla gercek apartman listing analysis vakasinda test edilmis olmasi
- Cikti yapisinin tutarli ve decision destekleyici oldugunun gorulmesi
- Risk ve uncertainty davranisinin guvenilir way korunmasi
- Scopein apartman satis listinglariyla sinirli kalip genel property analysis tarafina kaymamasi
