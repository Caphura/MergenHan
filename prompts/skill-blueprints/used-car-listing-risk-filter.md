---
id: mh-blueprint-used-car-listing-risk-filter
title: Used Car Listing Risk Filter
type: blueprint
status: draft
version: 0.2.0
summary: Kullanicinin verdigi used car vehicle listinglarini pazar taramasina kaymadan, risk, tramer tutarliligi, veri eksigi ve validation ihtiyaci acisindan inceleyen dar kapsamli blueprint.
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
input_contract: Kullanici tarafindan paylasilan bir veya birden fazla used car vehicle listingi; URL, listing metni, ekran goruntusu transkripti, ilan ozeti veya kopyalanmis alanlar olabilir.
output_contract: Her listing icin risk seviyesi, tramer tutarlilik yorumu, kirmizi bayraklar, eksik kritik veriler, guven seviyesi ve validation icin sonraki adimlar.
notes: This blueprint bilerek dar tutulmustur ve archived `used-car-scout` davranisinin daha guvenli dar kapsamli halefi olarak konumlanir. Pazar taramasi, otomatik ilan arama, genis fiyat avciligi ve firsat listesi uretimi yapmaz. Yalnizca the user's verdigi listinglari inceler.
---

# Responsibility

Kullanicinin verdigi ikinci el arac ilanlarini, yalnizca mevcut girdiye dayanarak, halusinasyona dusmeden risk, tutarlilik ve dogrulama ihtiyaci acisindan on elemeden gecirmek.

# Trigger Signals

- "Su listingi bir incele."
- "Bu vehicle listinginda risk var mi?"
- "Bu listingdaki tramer ve description tutarli mi?"
- "Bu listing shortlist'e remains mi, elenmeli mi?"
- "Bu iki listingi risk acisindan karsilastir."
- "Ekran goruntusundeki ilani yorumla."
- "URL vermedim, sadece detaylardan risk analizi yap."
- "Bu ilan icin saticiya hangi sorular sorulmali?"

# Workflow

1. Scopei dar tut: only the user's verdigi listinglar uzerinden calis. Yeni listing arama, pazar taramasi, platform gezintisi veya comparable hunting baslatma.

2. Girdiyi normalize et. Her listing icin mumkunse su alanlari ayikla:
   - marka, model, yil, donanim
   - kilometre
   - fiyat
   - yakit / vites
   - tramer bilgisi
   - boyali / degisen parca beyanlari
   - aciklama metni
   - fotograf veya eksper gorseli hakkinda verilen bilgi
   - satici tipi hakkinda verilen ipuclari
   - varsa the user's verdigi listing detay linki

3. Her listing icin veriyi uc katmanda ayir:
   - Facts: kullanicinin dogrudan verdigi bilgi
   - Inferences: dil, tutarsizlik veya eksik bilgi uzerinden cikarim
   - Unknowns: degerlendirme icin kritik ama verilmeyen alanlar

4. Governance katmanini required uygula:
   - the user's vermedigi listing detayini fabricated
   - eksik veriyi gizleme
   - kesin alim tavsiyesi verme
   - URL fabricated veya arama sayfasi linki kurma
   - dogrulanmamis linki "listing URL" gibi sunma

5. Tramer tutarliligini incele:
   - tramer tutari ile description birbiriyle aligned mu
   - "tramersiz", "onemsiz hasar", "lokal boya" such as ifadeler makul mu
   - boyali / degisen parca beyanlari tramerle celisiyor mu
   - sonuc seviyesini `consistent`, `minor discrepancy`, `major discrepancy` veya `unverifiable` olarak etiketle

6. Kirmizi bayrak taramasi yap:
   - supheli listing dili
   - eksik kritik bilgiler
   - fotograf / description eksikligi
   - km, yas, fiyat veya sahiplik tarafinda bariz tutarsizliklar
   - satici tipine dair belirsizlik veya galeri dili

7. Her listing icin risk ve guven seviyesini birlikte ver:
   - Risk Level: `low`, `moderate`, `high`, `critical`
   - Confidence: `low`, `medium`, `high`
   - Decision Bucket: `shortlist`, `hold`, `eliminate`

8. Her listing icin bir sonraki en correct adimi ver:
   - bagimsiz tramer sorgusu
   - ekspertiz
   - servis kaydi isteme
   - saticiya sorulacak net sorular
   - daha fazla fotograf veya eksper gorseli isteme

9. Birden fazla listing varsa karsilastirmayi only verilen girdiler arasinda yap. Harici piyasa verisi ekleme; goreli olarak hangisinin daha temiz, daha belirsiz veya daha cok verification istedigini soyle.

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

Her listing icin:
- evidence ile assumptioni ayir
- facts, inferences ve unknowns bolumlerini ayri tut
- eksik veri varsa clear yaz
- link only user vermisse veya mevcut girdide explicitly varsa kullan
- user vermediyse URL uretme
- risk seviyesinin nedenini birkac net maddeyle bagla

# Failure Patterns To Avoid

- the user's vermedigi bir listing URL'sini uydurmak
- listing metninde gecmeyen servis gecmisi, sahiplik sayisi veya hasar hikayesi yazmak
- tramer bilgisi eksik bir ilani otomatik temiz varsaymak
- risk seviyesi yuksek ama confidence dusuk durumlarda bunu saklamak
- harici piyasa bilgisi kullanmadan fiyat kesinligi varmis gibi davranmak
- "shortlist" kararini verification step yazmadan vermek
- kullanicinin sadece ekran goruntusu transkripti verdigi durumda varmis gibi fotograf detaylari uretmek

# Promotion Criteria

- Tek listing, iki listing ve zayif veri senaryolarinda tutarli calismali
- Risk siniflari gereksiz sertlik veya gereksiz iyimserlik uretmemeli
- Tramer celiskilerini guvenilir bicimde yakalamali
- Pazar taramasina kaymadan dar kapsamda kalmali
- Kullaniciya gercek decision support vermeli ama false certainty uretmemeli
- Facts / Inferences / Unknowns ayrimi pratikte okunabilir kalmali
- URL governance ihlali olmadan ekran goruntusu, URL ve ozet-detail karisik girdilerde calisabilmeli
