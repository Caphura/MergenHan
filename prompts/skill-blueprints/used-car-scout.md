---
id: mh-blueprint-used-car-scout
title: Used Car Scout
type: blueprint
status: archived
version: 1.4.0
summary: Tarihsel referans olarak korunan, ikinci el arac ilan analizi icin tasarlanmis ancak karmaşıklık ve halusinasyon riski nedeniyle yeni kullanim icin onerilmeyen blueprint.
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
last_reviewed: 2026-04-06
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Konum, yaricap, butce araligi ve opsiyonel olarak marka/model/yil/km tercihleri ile birlikte ikinci el arac arama ve analiz istegi.
output_contract: Firsat araclari ve uzak durulmasi gereken araclar listeleri, her birinde yalnizca gercek ilan detay linki, tramer degerlendirmesi, kirmizi bayraklar, fiyat konumlama ve onerilen sonraki adimlar.
notes: Bu blueprint repodan silinmeden tarihsel referans olarak korunmaktadir. Davranisin pratikte fazla karmasik ve halusinasyona acik oldugu goruldugu icin yeni kullanim icin onerilmez. Referans platformlar sahibinden.com, arabam.com, letgo ve benzeri Turkiye merkezli ikinci el arac platformlaridir. Arama/listing sayfasi URL'leri gecersizdir; yalnizca gercek ilan detay sayfasi linki verilmelidir.
---

# Archived Note

Bu blueprint tarihsel referans olarak korunur. Yeni kullanimlarda tercih edilmemelidir; davranisin karmasikligi ve halusinasyon riski nedeniyle rafa kaldirilmistir.

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

   Dogrudan ilan linki kurali: ciktida verilen her URL, o ilanin gercek detay sayfasina acmalidir. Arama sonuc sayfasi, liste sayfasi, filtre sayfasi veya kategori sayfasi URL'leri kesinlikle verilmemelidir. Platform URL yapilari standarttir ve JavaScript ile gizlenmez:
   - sahibinden.com: https://www.sahibinden.com/ilan/[kategori-slug]/[ilan-basligi-slug]/[ilan-id]
   - arabam.com: https://www.arabam.com/ilan/[tur]/[ilan-basligi-slug]/[ilan-id]
   - letgo: https://www.letgo.com/item/[ilan-basligi-slug]-iid-[ilan-id]
   "JavaScript sitesi oldugu icin URL alinamadi" gecerli bir mazeret degildir. Ilan ID'si arama sonuclarinda her zaman gorunur.
   Ancak keskin cizgi sudur: sadece gercek ilan detay sayfasi linki ver. Elindeki URL'nin arama/listing sayfasi oldugundan supheleniyorsan veya detay sayfasi oldugunu dogrulayamiyorsan, o URL'yi hic verme. Onun yerine ilan basligini, platformunu ve varsa ilan numarasini yaz.
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
   - ilan linki (yalnizca kullanici verdiyse veya gercek tarama ile dogrulanmis detay sayfasi bulunduysa)
   - ilan aciklama metni

   Eksik veri kurtarma kurali: ilan platformlari (ozellikle arabam.com, sahibinden.com) fiyat, tramer ve detay bilgilerini JavaScript ile dinamik yukler. Arama sonuc sayfasinda fiyat veya diger kritik alanlar gorunmuyorsa:
   - Once ilan detay sayfasini dogrudan ziyaret et; cogu bilgi detay sayfasinda mevcuttur.
   - Detay sayfasinda da gorunemiyorsa bu alani "veri alinamadi" olarak isaretle ve kullaniciya sor.
   - Fiyat, km veya tramer gibi kritik alanlari "bilinmiyor" olarak birakip analizi atlamaya calisma; once her yolu dene, son care kullanicidan iste.

   Zorunlu aciklama analizi kurali: radarindaki her ilanin aciklama metnini oku ve analiz et. Aciklamasini okumadan hicbir ilani firsat veya risk olarak siniflandirma. Aciklama metni ilan sahibinin dili, iddialari, gizledikleri ve tutarsizliklari hakkinda kritik bilgi tasir; bu veriyi atlamak analizi eksik ve guvenilmez kilar.

4. Tramer dogrulama katmanini calistir (mh-module-used-car-tramer-verification):
   - Tramer tutarinin ilan aciklamasiyla tutarliligini kontrol et
   - "Tramersiz" iddialarinin makullugunu degerlendir
   - Boyali/degisen parca ile tramer arasindaki uyumsuzluklari isaretle
   - Yanlis veya eksik girilmis olabilecek tramer verilerini tespit et

   Eksper/hasar raporu gorseli kurali: ilan detay sayfasindaki eksper raporu gorseli veya hasar diagramini mutlaka kontrol et. Bu gorsel aracin hangi parcalarinin boyali, degisen veya hasarli oldugunu renkli sema ile belirtir. Sonra su capraz kontrolu yap:
   - Eksper gorselindeki boyali/degisen parcalar ile ilan aciklamasindaki beyanlar tutarli mi?
   - Eksper gorselindeki hasar isaretleri ile belirtilen tramer tutari oranlali mi?
   - Aciklamada "hatasiz, boyasiz" deniyorken eksper gorselinde boyali/degisen parca var mi?
   - Eksper gorseli yoksa veya gorulemiyorsa bunu "eksper gorseli bulunamadi veya gorulemedi" olarak belirt.

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

8. Her arac icin karar destekleyici ozet olustur: varsa yalnizca gercek ilan detay linki, fiyat konumlama, tramer degerlendirmesi, kirmizi bayrak ozeti, genel risk seviyesi ve onerilen sonraki adim.

9. Governance katmanini (mh-module-used-car-no-hallucination-governance) tum cikti boyunca uygula: kanit ile varsayimi ayir, eksik veriyi gizleme, garanti ifade kullanma.

10. Sonucu action-summary formatinda toparla.

# Output Shape

Sonucu mumkun oldugunca su yapida topla:

- Search Summary: konum, yaricap, kriterler ve taranan platform ozeti
- Market Snapshot: bulunan toplam ilan sayisi, fiyat araligi, ortalama km ve genel piyasa gorunumu
- Opportunity Vehicles: firsat araclari listesi (her birinde varsa yalnizca gercek ilan detay linki, fiyat konumlama, tramer degerlendirmesi, guc sinyalleri)
- Vehicles to Avoid: uzak durulmasi gereken araclar listesi (her birinde varsa yalnizca gercek ilan detay linki, tramer degerlendirmesi, tespit edilen riskler, kirmizi bayraklar)

Her ilan icin tramer degerlendirmesi zorunludur: tramer tutari, boyali/degisen parca bilgisi, aciklama ile tutarliligi ve guvenilirlik yorumu ayri bir alan olarak yer almali. Tramer bilgisi belirtilmemisse acikca "tramer bilgisi ilanda belirtilmemis — bagimsiz sorgu onerilir" yazilmali.
- Tramer Consistency Overview: genel tramer guvenilirlik tablosu
- Red Flag Summary: en sik gorulen kirmizi bayrak kaliplari
- Recommended Next Steps: fiziksel muayene, bagimsiz tramer sorgusu, ekspertiz, pazarlik onerileri

Her bolumde:
- kanit ile varsayimi ayir
- belirsizligi acikca etiketle
- kesin alim/satim tavsiyesi verme; risk seviyesi sun
- ilan linki yalnizca kullanicinin verdigi veya gercek web taramasi ile dogrulanmis gercek detay sayfasi URL'lerinden alinmali; sahte, tahmini veya uydurma URL uretilmemeli
- arama sonuc sayfasi, liste sayfasi, filtre sayfasi veya kategori sayfasi linki asla verilmemeli
- detay sayfasi linki kesin olarak dogrulanamiyorsa hic URL verme; bunun yerine ilan basligini, platformunu ve varsa ilan numarasini belirt

# Promotion Criteria

- Birden fazla gercek ilan grubu uzerinde test edilmis olmasi
- Tramer tutarsizlik tespitinin guvenilir calistigininn gorulmesi
- Fiyat konumlama ve firsat puanlamasinin tutarli olmasi
- Kirmizi bayrak tespitinin gercek riskleri yakalayabilmesi
- Kapsamin ikinci el arac ilanlariyla sinirli kalip genel otomotiv danismanligina kaymamasi
- Ciktinin ilan linkleri ile birlikte kullanilabilir olmasi
