---
id: mh-module-used-car-tramer-verification
title: Used Car Tramer Verification
type: module
status: active
version: 1.0.0
summary: Tramer kaydi validation, listing aciklamasiyla tutarsizlik tespiti ve yanlis girilmis hasar bilgisi ayiklama module.
tags:
  - automotive
  - used-car
  - tramer
  - data-quality
  - evidence
depends_on: []
last_reviewed: 2026-04-05
input_contract: Bir veya birden fazla used car vehicle listingindaki tramer bilgisi ve listing description metni.
output_contract: Tramer tutarliligi degerlendirmesi, tespit edilen celiskiler ve guvenilirlik seviyesi.
notes: This module tramer kaydinin kendisini directly sorgulayamaz; only listingda verilen bilgiler uzerinden tutarlilik analysis yapar.
---

# Purpose

Ikinci el vehicle listinglarindaki tramer bilgisinin listing aciklamasiyla tutarli olup olmadigini denetlemek ve yanlis veya eksik girilmis hasar bilgisini tespit etmek.

# Usage Rules

- Tramer tutarini tek basina yeterli gorme; description ile karsilastir.
- "Tramersiz" iddiasini otomatik olarak guvenilir kabul etme.
- Boyali veya degisen parca bilgisi ile tramer tutari arasindaki tutarsizligi isaretle.
- Tramer kaydinin yanlis girilmis olabilecegi ihtimalini her zaman goz onunde bulundur.
- Tramer bilgisi yoksa veya belirsizse bunu explicitly not et.

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
