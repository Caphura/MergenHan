---
id: mh-blueprint-used-car-scout
title: Used Car Scout
type: blueprint
status: archived
version: 1.4.0
summary: Tarihsel referans olarak korunan, used car vehicle listing analysis icin designed ancak karmaşıklık ve halusinasyon riski nedeniyle yeni usage icin onerilmeyen blueprint.
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
input_contract: Konum, yaricap, butce araligi ve opsiyonel olarak marka/model/yil/km tercihleri ile birlikte used car vehicle arama ve analysis istegi.
output_contract: Firsat vehiclelari ve uzak durulmasi gereken vehiclelar listeleri, her birinde only gercek listing detay linki, tramer degerlendirmesi, kirmizi bayraklar, fiyat konumlama ve onerilen sonraki adimlar.
notes: This blueprint repodan silinmeden tarihsel referans olarak korunmaktadir. Davranisin pratikte fazla karmasik ve halusinasyona clear oldugu goruldugu icin yeni usage icin onerilmez. Referans platformlar sahibinden.com, arabam.com, letgo ve benzeri Turkiye merkezli used car vehicle platformlaridir. Arama/listing sayfasi URL'leri gecersizdir; only gercek listing detay sayfasi linki verilmelidir.
---

# Archived Note

This blueprint tarihsel referans olarak is preserved. Yeni usagelarda tercih edilmemelidir; davranisin karmasikligi ve halusinasyon riski nedeniyle rafa kaldirilmistir.

# Responsibility

Belirlenen konum ve yaricap icinde used car vehicle listinglarini sistematik ve evidence temelli bicimde analysis ederek to the user firsat vehiclelari ve uzak durulmasi gereken vehiclelari listing linkleriyle birlikte sunmak.

# Trigger Signals

- "Bu bolgede 300-500 bin TL arasinda used car SUV ariyorum."
- "Ankara Cankaya cevresinde 50 km yaricapta firsat vehiclelari var mi?"
- "Sahibinden'de satilik su vehiclelari bir inceler misin?"
- "Bu listinglardaki vehiclelarin tramerleri guvenilir mi?"
- "Hangi listingdan uzak durmaliyim, hangisi firsat?"
- "Bu vehicle listinglarini karsilastirip bana en iyisini soyler misin?"

# Workflow

1. Arama kapsamini belirle: konum (sehir, ilce veya koordinat), yaricap (km), butce araligi, marka/model tercihi, yil araligi, km boundary, yakit tipi ve vites tercihi. Eksik kritik parametreleri userdan iste; ikincil tercihleri makul assumptionlarla doldur.

   Butce toleransi rule: the user's belirttigi butce tavaninin en fazla %15 ustune cikan listinglar "butceyi biraz asiyor ama bakmaya value" olarak sunulabilir. %15'in ustundeki listinglar analysis disinda tutulmali.

   Marka/model cesitliligi rule: user belirli bir marka/model belirtmediyse, taramayi tek bir marka veya modele daraltma. Butce, yil ve km kriterlerine uyan different markalari taramali ve en az 3-4 different markadan listing sunmalisin. Tek markaya odaklanmak, piyasa karsilastirmasini anlamsiz kilar ve gercek firsatlari kacirmaya yol acar.

2. Ilan kaynagini belirle. Iki mod vardir:
   - Kullanici listing verisi sagliyor: user URL, ekran goruntusu, kopyalanmis listing metni veya listing listesi paylasiyorsa directly bunlarla calis.
   - AI web taramasi yapiyor: eger working ortami gercek web erisimi sagliyorsa (browsing vehiclei, web search vb.) sahibinden.com, arabam.com, letgo such as platformlarda gercek listinglari tara. Gercek web erisimi yoksa userdan listing linkleri veya listing verileri istemeli; asla sahte veya tahmini URL uretmemelidir.

   Dogrudan listing linki rule: outputda verilen her URL, o listingin gercek detay sayfasina acmalidir. Arama sonuc sayfasi, liste sayfasi, filtre sayfasi veya kategori sayfasi URL'leri kesinlikle verilmemelidir. Platform URL yapilari standarttir ve JavaScript ile gizlenmez:
   - sahibinden.com: https://www.sahibinden.com/listing/[kategori-slug]/[listing-basligi-slug]/[listing-id]
   - arabam.com: https://www.arabam.com/listing/[tur]/[listing-basligi-slug]/[listing-id]
   - letgo: https://www.letgo.com/item/[listing-basligi-slug]-iid-[listing-id]
   "JavaScript sitesi oldugu icin URL alinamadi" gecerli bir mazeret degildir. Ilan ID'si arama sonuclarinda her zaman gorunur.
   Ancak keskin cizgi sudur: only gercek listing detay sayfasi linki ver. Elindeki URL'nin arama/listing sayfasi oldugundan supheleniyorsan veya detay sayfasi oldugunu dogrulayamiyorsan, o URL'yi hic verme. Onun yerine listing basligini, platformunu ve varsa listing numarasini yaz.
   Referans platformlar: sahibinden.com, arabam.com, letgo ve benzeri Turkiye merkezli used car vehicle platformlari.

   Tarama cesitliligi rule: her platformda different marka/model kombinasyonlariyla arama yap. Marka-bagimsiz filtrelerle basla; sonra ilgi cekici listinglari marka bazinda derinlestir. Tek bir markanin sonuclarina takilip kalmak tarama hatasidir.

3. Ilanlari topla ve normalize et: her listing icin su bilgileri separate:
   - marka, model, package/donanim
   - model yili
   - kilometre
   - yakit tipi ve vites
   - fiyat
   - konum
   - tramer tutari ve detayi
   - boyali/degisen parca bilgisi
   - sahip sayisi
   - listing tarihi ve currentleme gecmisi
   - listing linki (only user verdiyse veya gercek tarama ile dogrulanmis detay sayfasi bulunduysa)
   - listing description metni

   Eksik veri kurtarma rule: listing platformlari (ozellikle arabam.com, sahibinden.com) fiyat, tramer ve detay bilgilerini JavaScript ile dinamik yukler. Arama sonuc sayfasinda fiyat veya diger kritik alanlar gorunmuyorsa:
   - Once listing detay sayfasini directly ziyaret et; cogu bilgi detay sayfasinda mevcuttur.
   - Detay sayfasinda da gorunemiyorsa bu area "veri alinamadi" olarak isaretle ve to the user sor.
   - Fiyat, km veya tramer such as kritik alanlari "bilinmiyor" olarak birakip analysis atlamaya working; once her yolu dene, son care userdan iste.

   Zorunlu description analysis rule: radarindaki her listingin description metnini oku ve analysis et. Aciklamasini okumadan hicbir listingi firsat veya risk olarak siniflandirma. Aciklama metni listing sahibinin dili, iddialari, gizledikleri ve tutarsizliklari about kritik bilgi tasir; bu veriyi atlamak analysis eksik ve guvenilmez kilar.

4. Tramer validation katmanini calistir (mh-module-used-car-tramer-verification):
   - Tramer tutarinin listing aciklamasiyla tutarliligini kontrol et
   - "Tramersiz" iddialarinin makullugunu degerlendir
   - Boyali/degisen parca ile tramer arasindaki uyumsuzluklari isaretle
   - Yanlis veya eksik girilmis olabilecek tramer verilerini tespit et

   Eksper/hasar raporu visuali rule: listing detay sayfasindaki eksper raporu visuali veya hasar diagramini mutlaka kontrol et. Bu visual vehiclein hangi parcalarinin boyali, degisen veya hasarli oldugunu renkli sema ile belirtir. Sonra su capraz kontrolu yap:
   - Eksper visualindeki boyali/degisen parcalar ile listing aciklamasindaki beyanlar tutarli mi?
   - Eksper visualindeki hasar isaretleri ile belirtilen tramer tutari oranlali mi?
   - Aciklamada "hatasiz, boyasiz" deniyorken eksper visualinde boyali/degisen parca var mi?
   - Eksper visuali yoksa veya gorulemiyorsa bunu "eksper visuali bulunamadi veya gorulemedi" olarak belirt.

5. Kirmizi bayrak taramasini calistir (mh-module-used-car-listing-red-flags):
   - Aciklama dilindeki supheli ifadeleri tara
   - Veri tutarsizliklarini (km-yas-fiyat) kontrol et
   - Fotograf kalitesi ve eksikligini degerlendir
   - Eksik bilgi noktalarini isaretle
   - Toplam kirmizi bayrak sayisi ve ciddiyet seviyesini belirle

6. Fiyat karsilastirma katmanini calistir (mh-module-used-car-pricing-logic):
   - Her listingi benzer marka/model/yil/km vehiclelarla karsilastir
   - Fiyat konumlamasini belirle (piyasanin altinda, civarinda, ustunde)
   - Firsat puanlamasini yap
   - Gizli maliyet uyarilarini ekle

7. Sonuclari iki ana gruba ayir:
   - Firsat Araclari: dusuk fiyat + temiz tramer + az kirmizi bayrak kombinasyonu
   - Uzak Durulmasi Gereken Araclar: yuksek risk + tramer tutarsizligi + ciddi kirmizi bayraklar

8. Her vehicle icin decision destekleyici ozet olustur: varsa only gercek listing detay linki, fiyat konumlama, tramer degerlendirmesi, kirmizi bayrak ozeti, genel risk seviyesi ve onerilen sonraki step.

9. Governance katmanini (mh-module-used-car-no-hallucination-governance) tum output boyunca uygula: evidence ile assumptioni ayir, eksik veriyi gizleme, garanti ifade kullanma.

10. Sonucu action-summary formatinda toparla.

# Output Shape

Sonucu mumkun oldugunca su yapida topla:

- Search Summary: konum, yaricap, kriterler ve taranan platform ozeti
- Market Snapshot: bulunan toplam listing sayisi, fiyat araligi, ortalama km ve genel piyasa gorunumu
- Opportunity Vehicles: firsat vehiclelari listesi (her birinde varsa only gercek listing detay linki, fiyat konumlama, tramer degerlendirmesi, guc sinyalleri)
- Vehicles to Avoid: uzak durulmasi gereken vehiclelar listesi (her birinde varsa only gercek listing detay linki, tramer degerlendirmesi, tespit edilen riskler, kirmizi bayraklar)

Her listing icin tramer degerlendirmesi requireddur: tramer tutari, boyali/degisen parca bilgisi, description ile tutarliligi ve guvenilirlik yorumu ayri bir alan olarak yer almali. Tramer bilgisi belirtilmemisse explicitly "tramer bilgisi listingda belirtilmemis — bagimsiz sorgu onerilir" yazilmali.
- Tramer Consistency Overview: genel tramer guvenilirlik tablosu
- Red Flag Summary: en sik gorulen kirmizi bayrak kaliplari
- Recommended Next Steps: fiziksel muayene, bagimsiz tramer sorgusu, ekspertiz, pazarlik onerileri

Her bolumde:
- evidence ile assumptioni ayir
- belirsizligi explicitly etiketle
- kesin alim/satim tavsiyesi verme; risk seviyesi sun
- listing linki only the user's verdigi veya gercek web taramasi ile dogrulanmis gercek detay sayfasi URL'lerinden alinmali; sahte, tahmini veya fabricated URL uretilmemeli
- arama sonuc sayfasi, liste sayfasi, filtre sayfasi veya kategori sayfasi linki asla verilmemeli
- detay sayfasi linki kesin olarak dogrulanamiyorsa hic URL verme; bunun yerine listing basligini, platformunu ve varsa listing numarasini belirt

# Promotion Criteria

- Birden fazla gercek listing grubu uzerinde test edilmis olmasi
- Tramer tutarsizlik tespitinin guvenilir calistigininn gorulmesi
- Fiyat konumlama ve firsat puanlamasinin tutarli olmasi
- Kirmizi bayrak tespitinin gercek riskleri yakalayabilmesi
- Scopein used car vehicle listinglariyla sinirli kalip genel otomotiv danismanligina kaymamasi
- Ciktinin listing linkleri ile birlikte kullanilabilir olmasi
