---
id: mh-blueprint-used-car-listing-risk-filter
title: Used Car Listing Risk Filter
type: blueprint
status: draft
version: 0.1.0
summary: Kullanicinin verdigi ikinci el arac ilanlarini web taramasi yapmadan, risk, tutarlilik ve dogrulama ihtiyaci acisindan inceleyen dar kapsamli blueprint.
tags:
  - automotive
  - used-car
  - listing-analysis
  - tramer
  - risk
  - evidence
depends_on:
  - mh-module-used-car-tramer-verification
  - mh-module-used-car-listing-red-flags
  - mh-module-used-car-no-hallucination-governance
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-04-06
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Kullanici tarafindan paylasilan bir veya birden fazla ikinci el arac ilani; URL, ilan metni, ekran goruntusu transkripti veya ozet detaylar olabilir.
output_contract: Her ilan icin risk seviyesi, tramer tutarlilik yorumu, kirmizi bayraklar, eksik kritik veriler ve dogrulama icin sonraki adimlar.
notes: Bu blueprint bilerek dar tutulmustur. Pazar taramasi, otomatik ilan arama, genis fiyat avciligi ve firsat listesi uretimi yapmaz. Yalnizca kullanicinin verdigi ilanlari inceler.
---

# Responsibility

Kullanicinin verdigi ikinci el arac ilanlarini, halusinasyona dusmeden, risk ve tutarlilik acisindan on elemeden gecirmek.

# Trigger Signals

- "Su ilani bir incele."
- "Bu arac ilaninda risk var mi?"
- "Bu ilandaki tramer ve aciklama tutarli mi?"
- "Bu ilan shortlist'e kalir mi, elenmeli mi?"
- "Bu iki ilani risk acisindan karsilastir."

# Workflow

1. Kapsami dar tut: sadece kullanicinin verdigi ilanlar uzerinden calis. Yeni ilan arama, pazar taramasi veya platform gezintisi baslatma.

2. Her ilan icin mevcut veriyi normalize et:
   - marka, model, yil
   - kilometre
   - fiyat
   - yakit / vites
   - tramer bilgisi
   - boyali / degisen parca beyanlari
   - aciklama metni
   - varsa kullanicinin verdigi ilan detay linki

3. Governance katmanini zorunlu uygula:
   - kullanicinin vermedigi ilan detayini uydurma
   - eksik veriyi gizleme
   - kesin alim tavsiyesi verme
   - URL uydurma veya arama sayfasi linki kurma

4. Tramer tutarliligini incele:
   - tramer tutari ile aciklama birbiriyle uyumlu mu
   - "tramersiz" veya "onemsiz hasar" gibi ifadeler makul mu
   - boyali / degisen parca beyanlari tramerle celisiyor mu

5. Kirmizi bayrak taramasi yap:
   - supheli ilan dili
   - eksik kritik bilgiler
   - fotograf / aciklama eksikligi
   - km, yas, fiyat veya sahiplik tarafinda bariz tutarsizliklar

6. Ciktiyi karar destek seviyesinde tut:
   - "shortlist'e kalabilir"
   - "temkinli yaklas"
   - "elenmeli"
   gibi risk odakli siniflar kullan; kesin satin alma tavsiyesi verme.

7. Her ilan icin bir sonraki en dogru adimi ver:
   - bagimsiz tramer sorgusu
   - ekspertiz
   - servis kaydi isteme
   - saticiya sorulacak net sorular

# Output Shape

- Input Summary
- Listing-by-Listing Review
- Risk Level per Listing
- Tramer Consistency Notes
- Red Flags
- Missing Critical Data
- Recommended Verification Steps
- Shortlist / Hold / Eliminate

Her ilan icin:
- kanit ile varsayimi ayir
- eksik veri varsa acik yaz
- link yalnizca kullanici vermisse veya mevcut girdide acikca varsa kullan
- kullanici vermediyse URL uretme

# Promotion Criteria

- Tek ilan, iki ilan ve zayif veri senaryolarinda tutarli calismali
- Risk siniflari gereksiz sertlik veya gereksiz iyimserlik uretmemeli
- Tramer celiskilerini guvenilir bicimde yakalamali
- Pazar taramasina kaymadan dar kapsamda kalmali
- Kullaniciya gercek karar destegi vermeli ama sahte kesinlik uretmemeli
