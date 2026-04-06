---
id: mh-blueprint-apartment-investment-analyzer
title: Apartment Investment Analyzer
type: blueprint
status: stable
version: 1.0.0
summary: Apartman satis ilanlarini yatirim odakli, kanit ve belirsizlik ayrimini koruyan yapisal bir analiz formatina donusturen dogrulanmis real estate blueprint'i.
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
input_contract: Tek bir apartman ilani, birden fazla apartman satis ilani veya yatirim shortlist'i talebini kanit temelli ve karar odakli bicimde analiz etme istegi.
output_contract: Scope Summary, Market Snapshot, Listing-by-Listing Analysis, Rental Potential, Payback / Yield Estimate, Risks and Unknowns, Top Candidates ve Recommended Next Checks bolumlerinden olusan taranabilir apartment investment analizi.
notes: Bu blueprint farkli AI ortamlarda test edilmis ve karar destekleyici cikti yapisi, risk/belirsizlik disiplini ve apartman ilani odagi acisindan yeterli bulunmustur. Hukuki gorus, resmi ekspertiz, arsa / imar analizi, ticari gayrimenkul analizi veya finansman planlamasi uretmez.
---

# Responsibility

Tek bir apartman ilani veya birden fazla apartman satis ilanini, gercek karar vermeyi destekleyen yatirim odakli ve belirsizlik bilinci tasiyan yapisal bir analize donusturmek.

# Trigger Signals

- "Bu daire yatirim icin mantikli mi?"
- "Bu ilanlari yatirim acisindan karsilastir."
- "Hangisi daha iyi kira getirisi verir?"
- "Bu apartman ilanlarindan shortlist cikar."
- "Kaniti varsayimdan ayirarak analiz et."

# Workflow

1. Analiz kapsamini belirle: tek bir apartman, birden fazla apartman ilani veya yatirim shortlist'i talebi.
2. Mevcut kaniti normalize et: fiyat, brut / net m2, oda sayisi, kat, bina yasi, konum / mahalle, belirtilen durum ve ilan kalitesini ayristir; eksik veriyi not et.
3. Ilanlarin olasi piyasa konumunu belirle: piyasanin altinda, piyasa civarinda, piyasanin ustunde veya yetersiz veri nedeniyle belirsiz.
4. Yatirim kullanim degerini kabaca incele: kira potansiyeli, kaba geri donus / brut getiri mantigi, likidite / kiralanabilirlik ve gerekiyorsa pazarlik hassasiyeti.
5. Risk ve belirsizlikleri gorunur kil: zayif ilan kalitesi, eksik veya supheli veri, asiri fiyatlama riski, tadilat / durum riski, mahalle belirsizligi ve dogrulanmasi gereken kanit bosluklari.
6. Karar dostu bir cikti uret: kapsam ozeti, ilan bazli analiz, kira potansiyeli, geri donus / getiri mantigi, riskler ve bilinmeyenler, guclu adaylar ve sonraki kontrol adimlari.
7. Tum cikti boyunca kanit ile varsayimi ayir, belirsizligi etiketle, sahte kesinlikten ve garanti yatirim dili kullanmaktan kacin.

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
- kanit ile varsayimi ayir
- belirsizligi acikca etiketle
- false precision kullanma
- garanti yatirim dili kullanma

# Promotion Criteria

- Birden fazla gercek apartman ilan analizi vakasinda test edilmis olmasi
- Cikti yapisinin tutarli ve karar destekleyici oldugunun gorulmesi
- Risk ve belirsizlik davranisinin guvenilir sekilde korunmasi
- Kapsamin apartman satis ilanlariyla sinirli kalip genel property analysis tarafina kaymamasi
