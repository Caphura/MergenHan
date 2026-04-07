---
id: mh-blueprint-used-car-listing-risk-filter
title: Used Car Listing Risk Filter
type: blueprint
status: draft
version: 0.2.0
summary: Kullanicinin verdigi ikinci el arac ilanlarini pazar taramasina kaymadan, risk, tramer tutarliligi, veri eksigi ve dogrulama ihtiyaci acisindan inceleyen dar kapsamli blueprint.
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
last_reviewed: 2026-04-07
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Kullanici tarafindan paylasilan bir veya birden fazla ikinci el arac ilani; URL, ilan metni, ekran goruntusu transkripti, ilan ozeti veya kopyalanmis alanlar olabilir.
output_contract: Her ilan icin risk seviyesi, tramer tutarlilik yorumu, kirmizi bayraklar, eksik kritik veriler, guven seviyesi ve dogrulama icin sonraki adimlar.
notes: Bu blueprint bilerek dar tutulmustur ve arsivlenmis `used-car-scout` davranisinin daha guvenli dar kapsamli halefi olarak konumlanir. Pazar taramasi, otomatik ilan arama, genis fiyat avciligi ve firsat listesi uretimi yapmaz. Yalnizca kullanicinin verdigi ilanlari inceler.
---

# Responsibility

Kullanicinin verdigi ikinci el arac ilanlarini, yalnizca mevcut girdiye dayanarak, halusinasyona dusmeden risk, tutarlilik ve dogrulama ihtiyaci acisindan on elemeden gecirmek.

# Trigger Signals

- "Su ilani bir incele."
- "Bu arac ilaninda risk var mi?"
- "Bu ilandaki tramer ve aciklama tutarli mi?"
- "Bu ilan shortlist'e kalir mi, elenmeli mi?"
- "Bu iki ilani risk acisindan karsilastir."
- "Ekran goruntusundeki ilani yorumla."
- "URL vermedim, sadece detaylardan risk analizi yap."
- "Bu ilan icin saticiya hangi sorular sorulmali?"

# Workflow

1. Kapsami dar tut: sadece kullanicinin verdigi ilanlar uzerinden calis. Yeni ilan arama, pazar taramasi, platform gezintisi veya emsal avciligi baslatma.

2. Girdiyi normalize et. Her ilan icin mumkunse su alanlari ayikla:
   - marka, model, yil, donanim
   - kilometre
   - fiyat
   - yakit / vites
   - tramer bilgisi
   - boyali / degisen parca beyanlari
   - aciklama metni
   - fotograf veya eksper gorseli hakkinda verilen bilgi
   - satici tipi hakkinda verilen ipuclari
   - varsa kullanicinin verdigi ilan detay linki

3. Her ilan icin veriyi uc katmanda ayir:
   - Facts: kullanicinin dogrudan verdigi bilgi
   - Inferences: dil, tutarsizlik veya eksik bilgi uzerinden cikarim
   - Unknowns: degerlendirme icin kritik ama verilmeyen alanlar

4. Governance katmanini zorunlu uygula:
   - kullanicinin vermedigi ilan detayini uydurma
   - eksik veriyi gizleme
   - kesin alim tavsiyesi verme
   - URL uydurma veya arama sayfasi linki kurma
   - dogrulanmamis linki "ilan URL'si" gibi sunma

5. Tramer tutarliligini incele:
   - tramer tutari ile aciklama birbiriyle uyumlu mu
   - "tramersiz", "onemsiz hasar", "lokal boya" gibi ifadeler makul mu
   - boyali / degisen parca beyanlari tramerle celisiyor mu
   - sonuc seviyesini `consistent`, `minor discrepancy`, `major discrepancy` veya `unverifiable` olarak etiketle

6. Kirmizi bayrak taramasi yap:
   - supheli ilan dili
   - eksik kritik bilgiler
   - fotograf / aciklama eksikligi
   - km, yas, fiyat veya sahiplik tarafinda bariz tutarsizliklar
   - satici tipine dair belirsizlik veya galeri dili

7. Her ilan icin risk ve guven seviyesini birlikte ver:
   - Risk Level: `low`, `moderate`, `high`, `critical`
   - Confidence: `low`, `medium`, `high`
   - Decision Bucket: `shortlist`, `hold`, `eliminate`

8. Her ilan icin bir sonraki en dogru adimi ver:
   - bagimsiz tramer sorgusu
   - ekspertiz
   - servis kaydi isteme
   - saticiya sorulacak net sorular
   - daha fazla fotograf veya eksper gorseli isteme

9. Birden fazla ilan varsa karsilastirmayi sadece verilen girdiler arasinda yap. Harici piyasa verisi ekleme; goreli olarak hangisinin daha temiz, daha belirsiz veya daha cok dogrulama istedigini soyle.

# Output Shape

- Input Summary
- Listing-by-Listing Review
- Risk Level per Listing
- Confidence per Listing
- Tramer Consistency Notes
- Red Flags
- Missing Critical Data
- Recommended Verification Steps
- Shortlist / Hold / Eliminate

Her ilan icin:
- kanit ile varsayimi ayir
- facts, inferences ve unknowns bolumlerini ayri tut
- eksik veri varsa acik yaz
- link yalnizca kullanici vermisse veya mevcut girdide acikca varsa kullan
- kullanici vermediyse URL uretme
- risk seviyesinin nedenini birkac net maddeyle bagla

# Failure Patterns To Avoid

- kullanicinin vermedigi bir ilan URL'sini uydurmak
- ilan metninde gecmeyen servis gecmisi, sahiplik sayisi veya hasar hikayesi yazmak
- tramer bilgisi eksik bir ilani otomatik temiz varsaymak
- risk seviyesi yuksek ama confidence dusuk durumlarda bunu saklamak
- harici piyasa bilgisi kullanmadan fiyat kesinligi varmis gibi davranmak
- "shortlist" kararini dogrulama adimi yazmadan vermek
- kullanicinin sadece ekran goruntusu transkripti verdigi durumda varmis gibi fotograf detaylari uretmek

# Promotion Criteria

- Tek ilan, iki ilan ve zayif veri senaryolarinda tutarli calismali
- Risk siniflari gereksiz sertlik veya gereksiz iyimserlik uretmemeli
- Tramer celiskilerini guvenilir bicimde yakalamali
- Pazar taramasina kaymadan dar kapsamda kalmali
- Kullaniciya gercek karar destegi vermeli ama sahte kesinlik uretmemeli
- Facts / Inferences / Unknowns ayrimi pratikte okunabilir kalmali
- URL governance ihlali olmadan ekran goruntusu, URL ve ozet-detail karisik girdilerde calisabilmeli
