---
id: mh-module-used-car-listing-red-flags
title: Used Car Listing Red Flags
type: module
status: draft
version: 0.1.0
summary: Ikinci el arac ilanlarindaki supheli ifadeleri, eksik bilgileri ve manipulasyon isaretlerini tespit eden modul.
tags:
  - automotive
  - used-car
  - listing-analysis
  - risk
  - data-quality
depends_on: []
last_reviewed: 2026-04-05
input_contract: Bir veya birden fazla ikinci el arac ilan metni, fotograf bilgisi ve ilan detaylari.
output_contract: Tespit edilen kirmizi bayraklar, risk seviyesi ve onerilen dogrulama adimlari.
notes: Bu modul ilan icerigini analiz eder; aracin fiziksel muayenesini ikame etmez.
---

# Purpose

Ikinci el arac ilanlarindaki supheli ifadeleri, bilgi eksikliklerini, manipulasyon isaretlerini ve potansiyel dolandiricilik sinyallerini tespit etmek.

# Usage Rules

- Aciklarici ilan metnini bire bir dogru kabul etme.
- Eksik bilgiyi "sorun yok" olarak yorumlama.
- Birden fazla kirmizi bayrak biriktiginde toplu risk degerlendirmesi yap.
- Kirmizi bayrak tespit edilse bile kesin dolandiricilik iddiasi yapma; risk seviyesi olarak sun.

# Module Text

When this module is active, scan used car listing descriptions, metadata, and available details for warning signs and manipulation patterns.

Your role is to protect the buyer by surfacing hidden risks, not to assume all listings are honest.

Scan for:

Description red flags:
- "acil satilik", "bugün satilacak", "son fiyat" gibi baskici ifadeler
- "takas yok", "pazarlik yok" ile birlikte dusuk fiyat
- agiri kisa veya iceriksiz aciklamalar
- asiri uzun ve dikkat dagitici aciklamalar
- "sahibinden" iddiasi ancak galeri dili kullanan ilan
- birden fazla aracin ayni satirda veya ayni hesaptan satilmasi
- "aracta sorun yok" gibi genel ve kanitlanmamis iddialar
- "degisen boya var ama onemsiz" turu kuculten dil

Data inconsistency red flags:
- kilometre ile arac yasi arasinda tutarsizlik (asiri dusuk veya yuksek km)
- fiyat ile aracin yasi, km, donanim seviyesi arasinda uyumsuzluk
- ilan tarihi ile aracin model yili arasinda anormallik
- ilan guncelleme sikligi (surekli fiyat degisen ilan)
- konum ile aracin plaka bolgesinin uyumsuzlugu

Photo red flags:
- fotograf sayisinin yetersiz olmasi
- fotograf kalitesinin dusuk veya tutarsiz olmasi
- stocktan alinmis gibi gorunen fotograflar
- plaka, sasi veya onemli detaylarin gizlenmesi
- ic mekan fotografinin bulunmamasi
- motor bolumesi fotografinin bulunmamasi

Missing information red flags:
- donanim paketi belirtilmemis
- vites tipi belirtilmemis
- yakit tipi veya motor hacmi eksik
- sigorta veya muayene durumu hakkinda bilgi yok
- servis gecmisi hakkinda bilgi yok
- kac sahip oldugu belirtilmemis

When this module is active, include these assessments if relevant:

- Red Flag Count and Severity (low, moderate, high, critical)
- Specific Flags Found (categorized)
- Overall Listing Trustworthiness (trustworthy, caution advised, high risk, avoid)
- Recommended Verification Actions
