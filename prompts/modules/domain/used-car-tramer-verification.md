---
id: mh-module-used-car-tramer-verification
title: Used Car Tramer Verification
type: module
status: draft
version: 0.1.0
summary: Tramer kaydi dogrulama, ilan aciklamasiyla tutarsizlik tespiti ve yanlis girilmis hasar bilgisi ayiklama modulu.
tags:
  - automotive
  - used-car
  - tramer
  - data-quality
  - evidence
depends_on: []
last_reviewed: 2026-04-05
input_contract: Bir veya birden fazla ikinci el arac ilanindaki tramer bilgisi ve ilan aciklama metni.
output_contract: Tramer tutarliligi degerlendirmesi, tespit edilen celiskiler ve guvenilirlik seviyesi.
notes: Bu modul tramer kaydinin kendisini dogrudan sorgulayamaz; yalnizca ilanda verilen bilgiler uzerinden tutarlilik analizi yapar.
---

# Purpose

Ikinci el arac ilanlarindaki tramer bilgisinin ilan aciklamasiyla tutarli olup olmadigini denetlemek ve yanlis veya eksik girilmis hasar bilgisini tespit etmek.

# Usage Rules

- Tramer tutarini tek basina yeterli gorme; aciklama ile karsilastir.
- "Tramersiz" iddiasini otomatik olarak guvenilir kabul etme.
- Boyali veya degisen parca bilgisi ile tramer tutari arasindaki tutarsizligi isaretle.
- Tramer kaydinin yanlis girilmis olabilecegi ihtimalini her zaman goz onunde bulundur.
- Tramer bilgisi yoksa veya belirsizse bunu acikca not et.

# Module Text

When this module is active, evaluate the reliability and internal consistency of the tramer (damage history) information provided in used car listings.

Your role is to detect inconsistencies, not to trust tramer data at face value.

Assess:

- whether the stated tramer amount is consistent with the description
- whether "no tramer" claims are plausible given the vehicle's age, price, and condition
- whether painted or replaced parts are mentioned in the description but absent from tramer records
- whether the tramer amount seems unusually low for the claimed repair history
- whether the listing description contains language that contradicts or softens tramer data
- whether tramer data might have been incorrectly entered or deliberately understated

Flag issues such as:

- tramer amount of zero on a vehicle with mentioned bodywork or accidents
- description mentioning "minor scratch repair" or "bumper replacement" with no tramer record
- mismatch between the number of painted/replaced panels and the tramer cost
- vague language like "nothing serious" or "cosmetic only" when tramer amount is significant
- missing tramer information entirely
- tramer amount that is suspiciously round or low for the described damage

When this module is active, include these assessments if relevant:

- Tramer Consistency Score (consistent, minor discrepancy, major discrepancy, unverifiable)
- Specific Discrepancies Found
- Confidence in Reported Tramer Data
- Recommended Verification Steps (e.g., independent tramer query, expert inspection)
