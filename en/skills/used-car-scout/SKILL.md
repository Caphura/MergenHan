---
name: used-car-scout
description: Archived historical skill for second-hand car listing analysis. Kept for reference, not recommended for new use.
---

# Used Car Scout

## Status

This skill tarihsel referans olarak is preserved. Yeni usagelarda tercih edilmemelidir; gercek dunyada fazla karmasik ve halusinasyona clear calistigi goruldugu icin rafa kaldirilmistir.

## Use When

- Kullanici belirlenen konum ve yaricapta used car vehicle listinglarini taratmak istediginde
- Firsat vehiclelari ve uzak durulmasi gereken vehiclelari listing linki ile birlikte gormek istediginde
- Tramer bilgisinin listing aciklamasiyla tutarli olup olmadigini kontrol ettirmek istediginde
- Birden fazla listingi fiyat, km, yas, donanim ve tramer ekseninde karsilastirmak istediginde
- Ilan aciklamalarindaki supheli ifadeleri, eksik bilgileri ve manipulasyon isaretlerini tespit ettirmek istediginde
- Galeri listingi ile gercek sahip listingini ayirt etmek istediginde

Bu liste tarihsel context icindir. Yeni usagelarda bu skill'i aktif olarak onermeyin.

## Workflow

1. Arama kapsamini belirle: konum (sehir, ilce), yaricap (km), butce araligi, marka/model tercihi, yil araligi, km boundary, yakit tipi ve vites tercihi. Eksik kritik parametreleri userdan iste; ikincil tercihleri makul assumptionlarla doldur.

   Butce toleransi rule: the user's belirttigi butce tavaninin en fazla %15 ustune cikan listinglar "butceyi biraz asiyor ama bakmaya value" olarak sunulabilir. %15'in ustundeki listinglar analysis disinda tutulmali. Ornegin butce 900 bin TL ise en fazla 1.035.000 TL'ye kadar listing gosterilebilir; 1.035.000 TL'nin uzerindeki listinglar sonuclara dahil edilmemeli.

   Marka/model cesitliligi rule: user belirli bir marka/model belirtmediyse, taramayi tek bir marka veya modele daraltma. Butce, yil ve km kriterlerine uyan different markalari taramali ve en az 3-4 different markadan listing sunmalisin. Tek markaya odaklanmak, piyasa karsilastirmasini anlamsiz kilar ve gercek firsatlari kacirmaya yol acar.

2. Ilan kaynagini belirle. Iki mod vardir:
   - Kullanici listing verisi sagliyor: user URL, ekran goruntusu, kopyalanmis listing metni veya listing listesi paylasiyorsa directly bunlarla calis.
   - AI web taramasi yapiyor: eger working ortami gercek web erisimi sagliyorsa (browsing vehiclei, web search vb.) sahibinden.com, arabam.com, letgo such as platformlarda gercek listinglari tara. Gercek web erisimi yoksa userdan listing linkleri veya listing verileri istemeli; asla sahte veya tahmini URL uretmemelidir.

   Dogrudan listing linki rule: outputda verilen her URL, o listingin gercek detay sayfasina acmalidir. Arama sonuc sayfasina, liste sayfasina, filtre sayfasina veya kategori sayfasina yonlendiren URL'ler gecersizdir ve asla verilmemelidir.

   Platform URL yapilari: used car vehicle platformlarinin listing detay URL'leri standarttir ve JavaScript ile gizlenmez. Sayfanin content JS ile yuklense bile URL kendisi her zaman statik ve erislebilirdir:
   - sahibinden.com: https://www.sahibinden.com/listing/[kategori-slug]/[listing-basligi-slug]/[listing-id] — listing ID'si sayisal ve arama sonuclarinda gorunur
   - arabam.com: https://www.arabam.com/listing/[tur]/[listing-basligi-slug]/[listing-id] — listing ID'si sayisal ve arama sonuclarinda gorunur
   - letgo: https://www.letgo.com/item/[listing-basligi-slug]-iid-[listing-id]

   "JavaScript sitesi oldugu icin URL alinamadi" gecerli bir mazeret degildir. Ilan ID'si arama sonuc sayfasinda, HTML icerisinde veya listelemede gorunur.
   Ancak keskin cizgi sudur: only gercek listing detay sayfasi linki ver. Elindeki URL'nin arama/listing sayfasi oldugundan supheleniyorsan veya detay sayfasi oldugunu dogrulayamiyorsan, o URL'yi hic verme. Onun yerine listing basligini, platformunu ve varsa listing numarasini yaz.
   Referans platformlar: sahibinden.com, arabam.com, letgo ve benzeri Turkiye merkezli used car vehicle platformlari.

   Tarama cesitliligi rule: her platformda different marka/model kombinasyonlariyla arama yap. Marka-bagimsiz filtrelerle basla; sonra ilgi cekici listinglari marka bazinda derinlestir. Tek bir markanin sonuclarina takilip kalmak tarama hatasidir.

3. Ilanlari topla ve normalize et: her listing icin marka, model, package, model yili, kilometre, yakit tipi, vites, fiyat, konum, tramer tutari ve detayi, boyali/degisen parca bilgisi, sahip sayisi, listing tarihi, listing linki (only user verdiyse veya gercek tarama ile dogrulanmis detay sayfasi bulunduysa) ve description metnini separate.

   Eksik veri kurtarma rule: listing platformlari (ozellikle arabam.com, sahibinden.com) fiyat, tramer ve detay bilgilerini JavaScript ile dinamik yukler. Arama sonuc sayfasinda fiyat veya diger kritik alanlar gorunmuyorsa:
   - Once listing detay sayfasini directly ziyaret et; cogu bilgi detay sayfasinda mevcuttur.
   - Detay sayfasinda da gorunemiyorsa bu area "veri alinamadi" olarak isaretle ve to the user sor: "Su listinglarin fiyatlari benim tarafimda gorunmuyor, kontrol edip paylasir misiniz?"
   - Fiyat, km veya tramer such as kritik alanlari asla "bilinmiyor" olarak birakip analysis atlamaya working; once her yolu dene, son care userdan iste.

   Zorunlu description analysis rule: radarindaki her listingin description metnini oku ve analysis et. Aciklamasini okumadan hicbir listingi firsat veya risk olarak siniflandirma. Ilan detay sayfasini ziyaret ettiginde fiyat ve tramer verisinin yaninda description metnini de mutlaka oku. Aciklama metni listing sahibinin dili, iddialari, gizledikleri ve tutarsizliklari about kritik bilgi tasir; bu veriyi atlamak analysis eksik ve guvenilmez kilar.

4. Tramer validation katmanini calistir:
   - Tramer tutarinin listing aciklamasiyla tutarliligini kontrol et.
   - "Tramersiz" iddialarinin makullugunu degerlendir.
   - Boyali/degisen parca ile tramer arasindaki uyumsuzluklari isaretle.
   - Yanlis veya eksik girilmis olabilecek tramer verilerini tespit et.

   Eksper/hasar raporu visuali rule: listing platformlari (ozellikle arabam.com ve sahibinden.com) listing detay sayfasinda eksper raporu visuali veya hasar diagrimi shows. Bu visual vehiclein hangi parcalarinin boyali, degisen veya hasarli oldugunu renkli sema ile belirtir. Ilan detay sayfasini ziyaret ettiginde bu visuali mutlaka kontrol et. Sonra su capraz kontrolu yap:
   - Eksper visualindeki boyali/degisen parcalar ile listing aciklamasindaki beyanlar tutarli mi?
   - Eksper visualindeki hasar isaretleri ile belirtilen tramer tutari oranlali mi?
   - Aciklamada "hatasiz, boyasiz" deniyorken eksper visualinde boyali/degisen parca var mi?
   - Eksper visuali yoksa veya gorulemiyorsa bunu related listingin outputsinda "eksper visuali bulunamadi veya gorulemedi" olarak belirt.

5. Kirmizi bayrak taramasini calistir:
   - Aciklama dilindeki supheli ifadeleri tara (baskici dil, genel iddialar, galeri dili).
   - Veri tutarsizliklarini kontrol et (km-yas-fiyat uyumu).
   - Fotograf kalitesi ve eksikligini degerlendir.
   - Eksik bilgi noktalarini isaretle.
   - Galeri listingi ile gercek sahip listingini ayirt et.

6. Fiyat karsilastirma katmanini calistir:
   - Her listingi benzer marka/model/yil/km vehiclelarla karsilastir.
   - Fiyat konumlamasini belirle (piyasanin altinda, civarinda, ustunde).
   - Firsat puanlamasini yap.
   - Asiri dusuk fiyati tek basina firsat sayma; "too good to be true" mantigini uygula.

7. Sonuclari iki ana gruba ayir:
   - Firsat Araclari: uygun fiyat + temiz veya aciklanmis tramer + az kirmizi bayrak.
   - Uzak Durulmasi Gereken Araclar: yuksek risk + tramer tutarsizligi + ciddi kirmizi bayraklar.

8. Her vehicle icin decision destekleyici ozet olustur: varsa only gercek listing detay linki, fiyat konumlama, tramer degerlendirmesi, kirmizi bayrak ozeti, genel risk seviyesi ve onerilen sonraki step.

9. Tum output boyunca evidence ile assumptioni ayir, eksik veriyi gizleme, garanti alim/satim tavsiyesi verme, kesin fiyat degerlendirmesi yerine kaba araliklar sun.

## Output Expectations

- Cikti su bolumlerden olusmali: Search Summary, Market Snapshot, Opportunity Vehicles, Vehicles to Avoid, Tramer Consistency Overview, Red Flag Summary, Recommended Next Steps.
- Ilan linki only the user's verdigi veya gercek web taramasi ile dogrulanmis gercek detay sayfasi URL'lerinden alinmali.
- Arama sayfasina, liste sayfasina, filtre sayfasina veya kategori sayfasina yonlendiren URL'ler gecersizdir ve asla verilmemeli.
- Detay sayfasi URL'si kesin olarak dogrulanamiyorsa hic URL verme; bunun yerine listing basligini, platformunu ve listing numarasini yaz.
- Firsat ve risk gruplari net ayrilmis olmali.
- Tramer tutarsizliklari explicitly raporlanmali.
- Sonuclarda yer alan her listing icin tramer degerlendirmesi requireddur. Tramer tutari, boyali/degisen parca bilgisi, description ile tutarliligi ve guvenilirlik yorumu her listingin outputsinda ayri bir alan olarak yer almali. Tramer bilgisi belirtilmemisse bu durum explicitly "tramer bilgisi listingda belirtilmemis — bagimsiz sorgu onerilir" olarak yazilmali; bos birakilmamali.
- Red flags kategorize edilmis ve ciddiyet seviyesi belirtilmis olmali.
- Fiyat konumlama kaba araliklarda sunulmali; kesin value bicilmemeli.
- Kesin alim/satim tavsiyesi yerine risk seviyesi ve kosullu evaluation verilmeli.
- Eksik veri explicitly belirtilmeli ve fiziksel muayene her zaman onerilmeli.
- Galeri listingi ile gercek sahip listingi ayrimi gorunur olmali.

## Failure Patterns To Avoid

- Tramer tutarini listing aciklamasiyla karsilastirmadan correct kabul etmek
- "Tramersiz" iddiasini otomatik guvenilir saymak
- Asiri dusuk fiyati sorgusuz firsat olarak sunmak
- Eksik kilometre, fotograf veya tramer bilgisi ile kesin evaluation yapmak
- Galeri dilini ("vehiclelarimiz", "magzamizi ziyaret") fark etmemek
- Ilan linklerini outputdan cikarmak
- Gercek olmayan, sahte veya arama sayfasina dusen URL'ler uretmek
- Dogrulanmamis listing URL'lerini gercek listing linki such as sunmak
- Detay sayfasi oldugundan kesin emin olunmayan URL'leri vermek
- "Hemen alin" such as garanti tavsiye vermek
- Boyali/degisen parca iddiasini tramer kaydiyla karsilastirmamak
- Fiyat veya tramer bilgisini arama sayfasindan okuyamayinca "gorunmuyor" deyip analysis atlamak; listing detay sayfasini ziyaret etmeli veya userdan istemeli
- Kullanici belirli bir marka/model istemedigi halde tek bir marka veya modele odaklanmak; en az 3-4 different markadan listing sunulmali
- Ilanin description metnini okumadan veya analysis etmeden o listingi firsat ya da risk olarak siniflandirmak
- Herhangi bir listingi tramer degerlendirmesi yapmadan veya tramer bilgisini outputya yazmadan sunmak
- Ilan detay sayfasindaki eksper/hasar raporu visualini kontrol etmeden tramer degerlendirmesi yapmak
- Eksper visualindeki boyali/degisen parca bilgisini description metniyle capraz kontrol etmemek
- Arama sayfasina, liste sayfasina veya filtre sayfasina yonlendiren URL'leri listing linki olarak vermek
- "JavaScript sitesi oldugu icin URL alinamadi" such as bahanelerle arama/listing sayfasi linki vermek; only dogrulanmis detay sayfasi linki verilebilir

## References

- Test senaryolari ve puanlama rubrigi icin [`examples/compositions/used-car-scout-tests.md`](../../examples/compositions/used-car-scout-tests.md) dosyasina bak.

## Portability Notes

- This skill'in core davranisi provider-agnostiktir.
- Runtime'a specific listing tarama otomasyonu, web scraping vehiclei veya platform API entegrasyonu adapter katmaninda belgelenmelidir.
- Varsaylisting task listing verisi uzerinden analysis ve decision support uretmektir; otomatik satin alma islemi baslatmak degildir.
- Referans platformlar sahibinden.com, arabam.com ve letgo'dur; baska ulke veya platform adaptationlari adapter katmaninda yapilabilir.
