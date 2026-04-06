---
id: mh-blueprint-real-estate-valuation-session-composer
title: Real Estate Valuation Session Composer
type: blueprint
status: stable
version: 1.0.0
summary: Emlak piyasa arastirmasi ve valuation oturumlari icin correct master ve modul kombinasyonunu secen kompozisyon taslagi.
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
input_contract: Kullanicinin bir gayrimenkul, listing grubu veya bolge icin valuation ya da piyasa yorumu istemesi.
output_contract: Dogru prompt kombinasyonu ve session acilisi icin kopyalanabilir instruction.
notes: Farkli AI ortamlari uzerindeki testlerde correct session composition secimi, governance disiplini ve copy-paste session acilisi kalitesi acisindan yeterli bulunmustur; paketlenmeye hazirdir.
---

# Responsibility

Talebin what olduguna gore correct real-estate arastirma ve valuation prompt kompozisyonunu secmek.

# Trigger Signals

- "Bu evin fiyati makul mu?"
- "Bu bolgede m2 fiyatlarini analysis et"
- "Emsal cikar"
- "Piyasa value araligi ver"
- "Yatirim icin mantikli mi?"
- "Kanitsiz konusma, only veriyle git"

# Workflow

1. Analizin hedefini belirle.
2. Governance modulunu required olarak aktif tut.
3. Gerekli uzman modules sec.
4. Kullaniciya kopyala-paste ready baslangic yonergesi ver.
5. Ciktilarda veri, assumption ve tahmini separate.

# Composition Map

## A) Piyasa veri kalitesi ve ilk tarama
- Core
- Real Estate Market Data Validation
- Real Estate No Hallucination Governance

## B) Emsal tabanli valuation
- Core
- Real Estate Market Data Validation
- Real Estate Comparable Analysis
- Real Estate Valuation Logic
- Real Estate Risk and Uncertainty
- Real Estate No Hallucination Governance

## C) Yatirim / satin alma decisioni
- Core
- Real Estate Market Data Validation
- Real Estate Comparable Analysis
- Real Estate Valuation Logic
- Real Estate Risk and Uncertainty
- Real Estate Investment Decision Support
- Real Estate No Hallucination Governance

## D) Tam disiplinli analysis
- Core
- Real Estate Market Data Validation
- Real Estate Comparable Analysis
- Real Estate Valuation Logic
- Real Estate Risk and Uncertainty
- Real Estate Investment Decision Support
- Real Estate No Hallucination Governance

# Output Expectations

- Governance modulunun aktif oldugu explicitly yazilmali.
- Veri ile tahmin kesin olarak ayrilmalidir.
- Eger veri yetersizse bu net bicimde soylenmelidir.
- Kullaniciya kopyala-paste ready baslangic mesaji verilmelidir.
