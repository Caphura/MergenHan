---
id: mh-module-used-car-listing-red-flags
title: Used Car Listing Red Flags
type: module
status: active
version: 1.0.0
summary: Ikinci el vehicle listinglarindaki supheli ifadeleri, eksik bilgileri ve manipulasyon isaretlerini tespit eden modul.
tags:
  - automotive
  - used-car
  - listing-analysis
  - risk
  - data-quality
depends_on: []
last_reviewed: 2026-04-05
input_contract: Bir veya birden fazla used car vehicle listing metni, fotograf bilgisi ve listing detaylari.
output_contract: Tespit edilen kirmizi bayraklar, risk seviyesi ve onerilen validation steps.
notes: This module listing icerigini analysis eder; vehiclein fiziksel muayenesini ikame etmez.
---

# Purpose

Ikinci el vehicle listinglarindaki supheli ifadeleri, bilgi eksikliklerini, manipulasyon isaretlerini ve potansiyel dolandiricilik sinyallerini tespit etmek.

# Usage Rules

- Aciklarici listing metnini bire bir correct kabul etme.
- Eksik bilgiyi "sorun yok" olarak yorumlama.
- Birden fazla kirmizi bayrak biriktiginde toplu risk degerlendirmesi yap.
- Kirmizi bayrak tespit edilse bile kesin dolandiricilik iddiasi yapma; risk seviyesi olarak sun.

# Module Text

When this module is active, scan used car listing descriptions, metadata, and available details for warning signs and manipulation patterns.

Your role is to protect the buyer by surfacing hidden risks, not to assume all listings are honest.

Scan for:

Description red flags:
- "acil satilik", "bugün satilacak", "son fiyat" such as baskici ifadeler
- "takas yok", "pazarlik yok" ile birlikte dusuk fiyat
- agiri short veya iceriksiz aciklamalar
- asiri uzun ve dikkat dagitici aciklamalar
- "sahibinden" iddiasi ancak galeri dili kullanan listing
- birden fazla vehiclein same satirda veya same hesaptan satilmasi
- "vehicleta sorun yok" such as genel ve evidencelanmamis iddialar
- "degisen boya var ama onemsiz" type kuculten dil

Data inconsistency red flags:
- kilometre ile vehicle yasi arasinda tutarsizlik (asiri dusuk veya yuksek km)
- fiyat ile vehiclein yasi, km, donanim seviyesi arasinda uyumsuzluk
- listing tarihi ile vehiclein model yili arasinda anormallik
- listing currentleme sikligi (surekli fiyat degisen listing)
- konum ile vehiclein plaka bolgesinin uyumsuzlugu

Photo red flags:
- fotograf sayisinin yetersiz olmasi
- fotograf kalitesinin dusuk veya tutarsiz olmasi
- stocktan alinmis such as gorunen fotograflar
- plaka, sasi veya onemli detaylarin gizlenmesi
- ic mekan fotografinin bulunmamasi
- motor bolumesi fotografinin bulunmamasi

Missing information red flags:
- donanim package belirtilmemis
- vites tipi belirtilmemis
- yakit tipi veya motor hacmi eksik
- sigorta veya muayene durumu about bilgi yok
- servis gecmisi about bilgi yok
- kac sahip oldugu belirtilmemis

When this module is active, include these assessments if relevant:

- Red Flag Count and Severity (low, moderate, high, critical)
- Specific Flags Found (categorized)
- Overall Listing Trustworthiness (trustworthy, caution advised, high risk, avoid)
- Recommended Verification Actions
