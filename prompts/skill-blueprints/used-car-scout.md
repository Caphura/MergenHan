---
id: mh-blueprint-used-car-scout
title: Used Car Scout
type: blueprint
status: stable
version: 1.2.2
summary: Belirlenen konum ve yaricapta ikinci el arac ilanlarini derinlemesine analiz ederek firsat araclarini ve uzak durulmasi gereken araclari ilan linki ile birlikte sunan blueprint.
tags:
  - automotive
  - used-car
  - listing-analysis
  - tramer
  - decision-support
  - risk
  - pricing
depends_on:
  - mh-module-used-car-tramer-verification
  - mh-module-used-car-listing-red-flags
  - mh-module-used-car-pricing-logic
  - mh-module-used-car-no-hallucination-governance
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-04-05
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Konum, yaricap, butce araligi ve opsiyonel olarak marka/model/yil/km tercihleri ile birlikte ikinci el arac arama ve analiz istegi.
output_contract: Firsat araclari ve uzak durulmasi gereken araclar listeleri, her birinde ilan linki, tramer degerlendirmesi, kirmizi bayraklar, fiyat konumlama ve onerilen sonraki adimlar.
notes: Bu blueprint ikinci el arac ilanlarini analiz eder; aracin fiziksel muayenesini, resmi ekspertiz raporunu veya hukuki danismanlik hizmetini ikame etmez. Referans platformlar sahibinden.com, arabam.com, letgo ve benzeri Turkiye merkezli ikinci el arac platformlaridir.
---

# Responsibility

Belirlenen konum ve yaricap icinde ikinci el arac ilanlarini sistematik ve kanit temelli bicimde analiz ederek kullaniciya firsat araclari ve uzak durulmasi gereken araclari ilan linkleriyle birlikte sunmak.

# Trigger Signals

- "Bu bolgede 300-500 bin TL arasinda ikinci el SUV ariyorum."
- "Ankara Cankaya cevresinde 50 km yaricapta firsat araclari var mi?"
- "Sahibinden'de satilik su araclari bir inceler misin?"
- "Bu ilanlardaki araclarin tramerleri guvenilir mi?"
- "Hangi ilandan uzak durmaliyim, hangisi firsat?"
- "Bu arac ilanlarini karsilastirip bana en iyisini soyler misin?"

# Workflow

1. Arama kapsamini belirle: konum (sehir, ilce veya koordinat), yaricap (km), butce araligi, marka/model tercihi, yil araligi, km siniri, yakit tipi ve vites tercihi. Eksik kritik parametreleri kullanicidan iste; ikincil tercihleri makul varsayimlarla doldur.

   Butce toleransi kurali: kullanicinin belirttigi butce tavaninin en fazla %15 ustune cikan ilanlar "butceyi biraz asiyor ama bakmaya deger" olarak sunulabilir. %15'in ustundeki ilanlar analiz disinda tutulmali.

   Marka/model cesitliligi kurali: kullanici belirli bir marka/model belirtmediyse, taramayi tek bir marka veya modele daraltma. Butce, yil ve km kriterlerine uyan farkli markalari taramali ve en az 3-4 farkli markadan ilan sunmalisin. Tek markaya odaklanmak, piyasa karsilastirmasini anlamsiz kilar ve gercek firsatlari kacirmaya yol acar.

2. Ilan kaynagini belirle. Iki mod vardir:
   - Kullanici ilan verisi sagliyor: kullanici URL, ekran goruntusu, kopyalanmis ilan metni veya ilan listesi paylasiyorsa dogrudan bunlarla calis.
   - AI web taramasi yapiyor: eger calisma ortami gercek web erisimi sagliyorsa (browsing araci, web search vb.) sahibinden.com, arabam.com, letgo gibi platformlarda gercek ilanlari tara. Gercek web erisimi yoksa kullanicidan ilan linkleri veya ilan verileri istemeli; asla sahte veya tahmini URL uretmemelidir.
   Referans platformlar: sahibinden.com, arabam.com, letgo ve benzeri Turkiye merkezli ikinci el arac platformlari.

   Tarama cesitliligi kurali: her platformda farkli marka/model kombinasyonlariyla arama yap. Marka-bagimsiz filtrelerle basla; sonra ilgi cekici ilanlari marka bazinda derinlestir. Tek bir markanin sonuclarina takilip kalmak tarama hatasidir.

3. Ilanlari topla ve normalize et: her ilan icin su bilgileri ayristir:
   - marka, model, paket/donanim
   - model yili
   - kilometre
   - yakit tipi ve vites
   - fiyat
   - konum
   - tramer tutari ve detayi
   - boyali/degisen parca bilgisi
   - sahip sayisi
   - ilan tarihi ve guncelleme gecmisi
   - ilan linki (kullanici verdiyse veya gercek tarama ile bulunduysa)
   - ilan aciklama metni

   Eksik veri kurtarma kurali: ilan platformlari (ozellikle arabam.com, sahibinden.com) fiyat, tramer ve detay bilgilerini JavaScript ile dinamik yukler. Arama sonuc sayfasinda fiyat veya diger kritik alanlar gorunmuyorsa:
   - Once ilan detay sayfasini dogrudan ziyaret et; cogu bilgi detay sayfasinda mevcuttur.
   - Detay sayfasinda da gorunemiyorsa bu alani "veri alinamadi" olarak isaretle ve kullaniciya sor.
   - Fiyat, km veya tramer gibi kritik alanlari "bilinmiyor" olarak birakip analizi atlamaya calisma; once her yolu dene, son care kullanicidan iste.

4. Tramer dogrulama katmanini calistir (mh-module-used-car-tramer-verification):
   - Tramer tutarinin ilan aciklamasiyla tutarliligini kontrol et
   - "Tramersiz" iddialarinin makullugunu degerlendir
   - Boyali/degisen parca ile tramer arasindaki uyumsuzluklari isaretle
   - Yanlis veya eksik girilmis olabilecek tramer verilerini tespit et

5. Kirmizi bayrak taramasini calistir (mh-module-used-car-listing-red-flags):
   - Aciklama dilindeki supheli ifadeleri tara
   - Veri tutarsizliklarini (km-yas-fiyat) kontrol et
   - Fotograf kalitesi ve eksikligini degerlendir
   - Eksik bilgi noktalarini isaretle
   - Toplam kirmizi bayrak sayisi ve ciddiyet seviyesini belirle

6. Fiyat karsilastirma katmanini calistir (mh-module-used-car-pricing-logic):
   - Her ilani benzer marka/model/yil/km araclarla karsilastir
   - Fiyat konumlamasini belirle (piyasanin altinda, civarinda, ustunde)
   - Firsat puanlamasini yap
   - Gizli maliyet uyarilarini ekle

7. Sonuclari iki ana gruba ayir:
   - Firsat Araclari: dusuk fiyat + temiz tramer + az kirmizi bayrak kombinasyonu
   - Uzak Durulmasi Gereken Araclar: yuksek risk + tramer tutarsizligi + ciddi kirmizi bayraklar

8. Her arac icin karar destekleyici ozet olustur: ilan linki, fiyat konumlama, tramer degerlendirmesi, kirmizi bayrak ozeti, genel risk seviyesi ve onerilen sonraki adim.

9. Governance katmanini (mh-module-used-car-no-hallucination-governance) tum cikti boyunca uygula: kanit ile varsayimi ayir, eksik veriyi gizleme, garanti ifade kullanma.

10. Sonucu action-summary formatinda toparla.

# Output Shape

Sonucu mumkun oldugunca su yapida topla:

- Search Summary: konum, yaricap, kriterler ve taranan platform ozeti
- Market Snapshot: bulunan toplam ilan sayisi, fiyat araligi, ortalama km ve genel piyasa gorunumu
- Opportunity Vehicles: firsat araclari listesi (her birinde ilan linki, fiyat konumlama, tramer durumu, guc sinyalleri)
- Vehicles to Avoid: uzak durulmasi gereken araclar listesi (her birinde ilan linki, tespit edilen riskler, kirmizi bayraklar)
- Tramer Consistency Overview: genel tramer guvenilirlik tablosu
- Red Flag Summary: en sik gorulen kirmizi bayrak kaliplari
- Recommended Next Steps: fiziksel muayene, bagimsiz tramer sorgusu, ekspertiz, pazarlik onerileri

Her bolumde:
- kanit ile varsayimi ayir
- belirsizligi acikca etiketle
- kesin alim/satim tavsiyesi verme; risk seviyesi sun
- ilan linki yalnizca kullanicinin verdigi veya gercek web taramasi ile bulunan URL'lerden alinmali; sahte, tahmini veya uydurma URL uretilmemeli; gercek link yoksa ilan basligini ve platformunu belirtmek yeterlidir

# Promotion Criteria

- Birden fazla gercek ilan grubu uzerinde test edilmis olmasi
- Tramer tutarsizlik tespitinin guvenilir calistigininn gorulmesi
- Fiyat konumlama ve firsat puanlamasinin tutarli olmasi
- Kirmizi bayrak tespitinin gercek riskleri yakalayabilmesi
- Kapsamin ikinci el arac ilanlariyla sinirli kalip genel otomotiv danismanligina kaymamasi
- Ciktinin ilan linkleri ile birlikte kullanilabilir olmasi
