---
id: mh-blueprint-real-estate-valuation-session-composer
title: Real Estate Valuation Session Composer
type: blueprint
status: stable
version: 1.0.0
summary: Emlak piyasa arastirmasi ve degerleme oturumlari icin dogru master ve modul kombinasyonunu secen kompozisyon taslagi.
tags:
  - real-estate
  - valuation
  - composition
  - workflow
depends_on:
  - mh-master-ultimate-real-estate-market-and-valuation-strategist-core
  - mh-module-real-estate-market-data-validation
  - mh-module-real-estate-comparable-analysis
  - mh-module-real-estate-valuation-logic
  - mh-module-real-estate-risk-and-uncertainty
  - mh-module-real-estate-investment-decision-support
  - mh-module-real-estate-no-hallucination-governance
last_reviewed: 2026-04-03
input_contract: Kullanicinin bir gayrimenkul, ilan grubu veya bolge icin degerleme ya da piyasa yorumu istemesi.
output_contract: Dogru prompt kombinasyonu ve oturum acilisi icin kopyalanabilir yonerge.
notes: Henuz paketlenmis skill degildir; once kullanim kaliplari olgunlastirilmalidir.
---

# Responsibility

Talebin ne olduguna gore dogru emlak arastirma ve degerleme prompt kompozisyonunu secmek.

# Trigger Signals

- "Bu evin fiyati makul mu?"
- "Bu bolgede m2 fiyatlarini analiz et"
- "Emsal cikar"
- "Piyasa deger araligi ver"
- "Yatirim icin mantikli mi?"
- "Kanitsiz konusma, sadece veriyle git"

# Workflow

1. Analizin hedefini belirle.
2. Governance modulunu zorunlu olarak aktif tut.
3. Gerekli uzman modulleri sec.
4. Kullaniciya kopyala-yapistir hazir baslangic yonergesi ver.
5. Ciktilarda veri, varsayim ve tahmini ayristir.

# Composition Map

## A) Piyasa veri kalitesi ve ilk tarama
- Core
- Real Estate Market Data Validation
- Real Estate No Hallucination Governance

## B) Emsal tabanli degerleme
- Core
- Real Estate Market Data Validation
- Real Estate Comparable Analysis
- Real Estate Valuation Logic
- Real Estate Risk and Uncertainty
- Real Estate No Hallucination Governance

## C) Yatirim / satin alma karari
- Core
- Real Estate Market Data Validation
- Real Estate Comparable Analysis
- Real Estate Valuation Logic
- Real Estate Risk and Uncertainty
- Real Estate Investment Decision Support
- Real Estate No Hallucination Governance

## D) Tam disiplinli analiz
- Core
- Real Estate Market Data Validation
- Real Estate Comparable Analysis
- Real Estate Valuation Logic
- Real Estate Risk and Uncertainty
- Real Estate Investment Decision Support
- Real Estate No Hallucination Governance

# Output Expectations

- Governance modulunun aktif oldugu acikca yazilmali.
- Veri ile tahmin kesin olarak ayrilmalidir.
- Eger veri yetersizse bu net bicimde soylenmelidir.
- Kullaniciya kopyala-yapistir hazir baslangic mesaji verilmelidir.
