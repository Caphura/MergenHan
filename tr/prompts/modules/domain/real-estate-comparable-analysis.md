---
id: mh-module-real-estate-comparable-analysis
title: Real Estate Comparable Analysis
type: module
status: active
version: 1.0.0
summary: Emsal benzerligini, guclu karsilastirmalari ve elenmesi gereken zayif emsalleri ayiran modul.
tags:
  - real-estate
  - comparables
  - valuation
  - analysis
depends_on: []
last_reviewed: 2026-04-03
input_contract: Konu gayrimenkul veya piyasa hedefi icin emsal uygunlugu analizi.
output_contract: Guclu, kabul edilebilir, zayif ve reddedilen emsal gruplari ile secim mantigi.
notes: Emsal sayisindan cok emsal kalitesine oncelik verir.
---

# Purpose

En cok sayida ilani toplamak degil, en anlamli ve en savunulabilir emsalleri secmek.

# Usage Rules

- Miktar yerine iliski kalitesini onceliklendir.
- Farkli alt pazarlari esit kabul etme.
- Her emsalin neden guclu veya zayif oldugunu acikla.
- Gerekirse emsali reddet.

# Module Text

When this module is active, prioritize comparable relevance over quantity.

The objective is not to collect many listings.
The objective is to identify the most relevant comparables.

Evaluate comparable relevance using:

- micro-location similarity
- property type match
- gross/net size similarity
- room count similarity
- building age similarity
- floor similarity
- building condition similarity
- amenities and parking
- view, frontage, and exposure
- renovation status
- occupancy / tenancy status
- listing recency

Always separate comparables into categories such as:

- Strong Comparables
- Acceptable Comparables
- Weak Comparables
- Reject

For each comparable, explain why it belongs in that category.

Do not treat properties from meaningfully different submarkets as equivalent without explicitly stating the limitation.

When useful, identify likely adjustment factors such as:

- superior location
- inferior condition
- larger size
- smaller size
- newer building
- older building
- better amenities
- worse amenities
- better floor / worse floor
- stronger demand pocket / weaker demand pocket

When this module is active, include these sections:

- Comparable Selection Criteria
- Strong Comparables
- Weak or Rejected Comparables
- Adjustment Factors
- Most Important Comparables
