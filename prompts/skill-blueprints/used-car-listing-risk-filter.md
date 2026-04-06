---
id: mh-blueprint-used-car-listing-risk-filter
title: Used Car Listing Risk Filter
type: blueprint
status: draft
version: 0.1.0
summary: Kullanicinin verdigi used car vehicle listinglarini web taramasi yapmadan, risk, tutarlilik ve validation ihtiyaci acisindan inceleyen dar kapsamli blueprint.
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
input_contract: Kullanici by paylaslisting bir veya birden fazla used car vehicle listingi; URL, listing metni, ekran goruntusu transkripti veya ozet detaylar olabilir.
output_contract: Her listing icin risk seviyesi, tramer tutarlilik yorumu, kirmizi bayraklar, eksik kritik veriler ve validation icin sonraki adimlar.
notes: This blueprint bilerek dar tutulmustur. Pazar taramasi, otomatik listing arama, genis fiyat avciligi ve firsat listesi uretimi yapmaz. Yalnizca the user's verdigi listinglari inceler.
---

# Responsibility

Kullanicinin verdigi used car vehicle listinglarini, halusinasyona dusmeden, risk ve tutarlilik acisindan on elemeden gecirmek.

# Trigger Signals

- "Su listingi bir incele."
- "Bu vehicle listinginda risk var mi?"
- "Bu listingdaki tramer ve description tutarli mi?"
- "Bu listing shortlist'e remains mi, elenmeli mi?"
- "Bu iki listingi risk acisindan karsilastir."

# Workflow

1. Scopei dar tut: only the user's verdigi listinglar uzerinden calis. Yeni listing arama, pazar taramasi veya platform gezintisi baslatma.

2. Her listing icin mevcut veriyi normalize et:
   - marka, model, yil
   - kilometre
   - fiyat
   - yakit / vites
   - tramer bilgisi
   - boyali / degisen parca beyanlari
   - description metni
   - varsa the user's verdigi listing detay linki

3. Governance katmanini required uygula:
   - the user's vermedigi listing detayini fabricated
   - eksik veriyi gizleme
   - kesin alim tavsiyesi verme
   - URL fabricated veya arama sayfasi linki kurma

4. Tramer tutarliligini incele:
   - tramer tutari ile description birbiriyle aligned mu
   - "tramersiz" veya "onemsiz hasar" such as ifadeler makul mu
   - boyali / degisen parca beyanlari tramerle celisiyor mu

5. Kirmizi bayrak taramasi yap:
   - supheli listing dili
   - eksik kritik bilgiler
   - fotograf / description eksikligi
   - km, yas, fiyat veya sahiplik side bariz tutarsizliklar

6. Ciktiyi decision destek seviyesinde tut:
   - "shortlist'e kalabilir"
   - "temkinli yaklas"
   - "elenmeli"
   such as risk odakli siniflar kullan; kesin satin alma tavsiyesi verme.

7. Her listing icin bir sonraki en correct adimi ver:
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

Her listing icin:
- evidence ile assumptioni ayir
- eksik veri varsa clear yaz
- link only user vermisse veya mevcut girdide explicitly varsa kullan
- user vermediyse URL uretme

# Promotion Criteria

- Tek listing, iki listing ve zayif veri senaryolarinda tutarli calismali
- Risk siniflari gereksiz sertlik veya gereksiz iyimserlik uretmemeli
- Tramer celiskilerini guvenilir bicimde yakalamali
- Pazar taramasina kaymadan dar kapsamda kalmali
- Kullaniciya gercek decision support vermeli ama false certainty uretmemeli
