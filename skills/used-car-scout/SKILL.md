---
name: used-car-scout
description: Archived historical skill for second-hand car listing analysis. Kept for reference, not recommended for new use.
---

# Used Car Scout

## Status

Bu skill tarihsel referans olarak korunur. Yeni kullanimlarda tercih edilmemelidir; gercek dunyada fazla karmasik ve halusinasyona acik calistigi goruldugu icin rafa kaldirilmistir.

## Use When

- Kullanici belirlenen konum ve yaricapta ikinci el arac ilanlarini taratmak istediginde
- Firsat araclari ve uzak durulmasi gereken araclari ilan linki ile birlikte gormek istediginde
- Tramer bilgisinin ilan aciklamasiyla tutarli olup olmadigini kontrol ettirmek istediginde
- Birden fazla ilani fiyat, km, yas, donanim ve tramer ekseninde karsilastirmak istediginde
- Ilan aciklamalarindaki supheli ifadeleri, eksik bilgileri ve manipulasyon isaretlerini tespit ettirmek istediginde
- Galeri ilani ile gercek sahip ilanini ayirt etmek istediginde

Bu liste tarihsel baglam icindir. Yeni kullanimlarda bu skill'i aktif olarak onermeyin.

## Workflow

1. Arama kapsamini belirle: konum (sehir, ilce), yaricap (km), butce araligi, marka/model tercihi, yil araligi, km siniri, yakit tipi ve vites tercihi. Eksik kritik parametreleri kullanicidan iste; ikincil tercihleri makul varsayimlarla doldur.

   Butce toleransi kurali: kullanicinin belirttigi butce tavaninin en fazla %15 ustune cikan ilanlar "butceyi biraz asiyor ama bakmaya deger" olarak sunulabilir. %15'in ustundeki ilanlar analiz disinda tutulmali. Ornegin butce 900 bin TL ise en fazla 1.035.000 TL'ye kadar ilan gosterilebilir; 1.035.000 TL'nin uzerindeki ilanlar sonuclara dahil edilmemeli.

   Marka/model cesitliligi kurali: kullanici belirli bir marka/model belirtmediyse, taramayi tek bir marka veya modele daraltma. Butce, yil ve km kriterlerine uyan farkli markalari taramali ve en az 3-4 farkli markadan ilan sunmalisin. Tek markaya odaklanmak, piyasa karsilastirmasini anlamsiz kilar ve gercek firsatlari kacirmaya yol acar.

2. Ilan kaynagini belirle. Iki mod vardir:
   - Kullanici ilan verisi sagliyor: kullanici URL, ekran goruntusu, kopyalanmis ilan metni veya ilan listesi paylasiyorsa dogrudan bunlarla calis.
   - AI web taramasi yapiyor: eger calisma ortami gercek web erisimi sagliyorsa (browsing araci, web search vb.) sahibinden.com, arabam.com, letgo gibi platformlarda gercek ilanlari tara. Gercek web erisimi yoksa kullanicidan ilan linkleri veya ilan verileri istemeli; asla sahte veya tahmini URL uretmemelidir.

   Dogrudan ilan linki kurali: ciktida verilen her URL, o ilanin gercek detay sayfasina acmalidir. Arama sonuc sayfasina, liste sayfasina, filtre sayfasina veya kategori sayfasina yonlendiren URL'ler gecersizdir ve asla verilmemelidir.

   Platform URL yapilari: ikinci el arac platformlarinin ilan detay URL'leri standarttir ve JavaScript ile gizlenmez. Sayfanin icerigi JS ile yuklense bile URL kendisi her zaman statik ve erislebilirdir:
   - sahibinden.com: https://www.sahibinden.com/ilan/[kategori-slug]/[ilan-basligi-slug]/[ilan-id] — ilan ID'si sayisal ve arama sonuclarinda gorunur
   - arabam.com: https://www.arabam.com/ilan/[tur]/[ilan-basligi-slug]/[ilan-id] — ilan ID'si sayisal ve arama sonuclarinda gorunur
   - letgo: https://www.letgo.com/item/[ilan-basligi-slug]-iid-[ilan-id]

   "JavaScript sitesi oldugu icin URL alinamadi" gecerli bir mazeret degildir. Ilan ID'si arama sonuc sayfasinda, HTML icerisinde veya listelemede gorunur.
   Ancak keskin cizgi sudur: sadece gercek ilan detay sayfasi linki ver. Elindeki URL'nin arama/listing sayfasi oldugundan supheleniyorsan veya detay sayfasi oldugunu dogrulayamiyorsan, o URL'yi hic verme. Onun yerine ilan basligini, platformunu ve varsa ilan numarasini yaz.
   Referans platformlar: sahibinden.com, arabam.com, letgo ve benzeri Turkiye merkezli ikinci el arac platformlari.

   Tarama cesitliligi kurali: her platformda farkli marka/model kombinasyonlariyla arama yap. Marka-bagimsiz filtrelerle basla; sonra ilgi cekici ilanlari marka bazinda derinlestir. Tek bir markanin sonuclarina takilip kalmak tarama hatasidir.

3. Ilanlari topla ve normalize et: her ilan icin marka, model, paket, model yili, kilometre, yakit tipi, vites, fiyat, konum, tramer tutari ve detayi, boyali/degisen parca bilgisi, sahip sayisi, ilan tarihi, ilan linki (yalnizca kullanici verdiyse veya gercek tarama ile dogrulanmis detay sayfasi bulunduysa) ve aciklama metnini ayristir.

   Eksik veri kurtarma kurali: ilan platformlari (ozellikle arabam.com, sahibinden.com) fiyat, tramer ve detay bilgilerini JavaScript ile dinamik yukler. Arama sonuc sayfasinda fiyat veya diger kritik alanlar gorunmuyorsa:
   - Once ilan detay sayfasini dogrudan ziyaret et; cogu bilgi detay sayfasinda mevcuttur.
   - Detay sayfasinda da gorunemiyorsa bu alani "veri alinamadi" olarak isaretle ve kullaniciya sor: "Su ilanlarin fiyatlari benim tarafimda gorunmuyor, kontrol edip paylasir misiniz?"
   - Fiyat, km veya tramer gibi kritik alanlari asla "bilinmiyor" olarak birakip analizi atlamaya calisma; once her yolu dene, son care kullanicidan iste.

   Zorunlu aciklama analizi kurali: radarindaki her ilanin aciklama metnini oku ve analiz et. Aciklamasini okumadan hicbir ilani firsat veya risk olarak siniflandirma. Ilan detay sayfasini ziyaret ettiginde fiyat ve tramer verisinin yaninda aciklama metnini de mutlaka oku. Aciklama metni ilan sahibinin dili, iddialari, gizledikleri ve tutarsizliklari hakkinda kritik bilgi tasir; bu veriyi atlamak analizi eksik ve guvenilmez kilar.

4. Tramer dogrulama katmanini calistir:
   - Tramer tutarinin ilan aciklamasiyla tutarliligini kontrol et.
   - "Tramersiz" iddialarinin makullugunu degerlendir.
   - Boyali/degisen parca ile tramer arasindaki uyumsuzluklari isaretle.
   - Yanlis veya eksik girilmis olabilecek tramer verilerini tespit et.

   Eksper/hasar raporu gorseli kurali: ilan platformlari (ozellikle arabam.com ve sahibinden.com) ilan detay sayfasinda eksper raporu gorseli veya hasar diagrimi gosterir. Bu gorsel aracin hangi parcalarinin boyali, degisen veya hasarli oldugunu renkli sema ile belirtir. Ilan detay sayfasini ziyaret ettiginde bu gorseli mutlaka kontrol et. Sonra su capraz kontrolu yap:
   - Eksper gorselindeki boyali/degisen parcalar ile ilan aciklamasindaki beyanlar tutarli mi?
   - Eksper gorselindeki hasar isaretleri ile belirtilen tramer tutari oranlali mi?
   - Aciklamada "hatasiz, boyasiz" deniyorken eksper gorselinde boyali/degisen parca var mi?
   - Eksper gorseli yoksa veya gorulemiyorsa bunu ilgili ilanin ciktisinda "eksper gorseli bulunamadi veya gorulemedi" olarak belirt.

5. Kirmizi bayrak taramasini calistir:
   - Aciklama dilindeki supheli ifadeleri tara (baskici dil, genel iddialar, galeri dili).
   - Veri tutarsizliklarini kontrol et (km-yas-fiyat uyumu).
   - Fotograf kalitesi ve eksikligini degerlendir.
   - Eksik bilgi noktalarini isaretle.
   - Galeri ilani ile gercek sahip ilanini ayirt et.

6. Fiyat karsilastirma katmanini calistir:
   - Her ilani benzer marka/model/yil/km araclarla karsilastir.
   - Fiyat konumlamasini belirle (piyasanin altinda, civarinda, ustunde).
   - Firsat puanlamasini yap.
   - Asiri dusuk fiyati tek basina firsat sayma; "too good to be true" mantigini uygula.

7. Sonuclari iki ana gruba ayir:
   - Firsat Araclari: uygun fiyat + temiz veya aciklanmis tramer + az kirmizi bayrak.
   - Uzak Durulmasi Gereken Araclar: yuksek risk + tramer tutarsizligi + ciddi kirmizi bayraklar.

8. Her arac icin karar destekleyici ozet olustur: varsa yalnizca gercek ilan detay linki, fiyat konumlama, tramer degerlendirmesi, kirmizi bayrak ozeti, genel risk seviyesi ve onerilen sonraki adim.

9. Tum cikti boyunca kanit ile varsayimi ayir, eksik veriyi gizleme, garanti alim/satim tavsiyesi verme, kesin fiyat degerlendirmesi yerine kaba araliklar sun.

## Output Expectations

- Cikti su bolumlerden olusmali: Search Summary, Market Snapshot, Opportunity Vehicles, Vehicles to Avoid, Tramer Consistency Overview, Red Flag Summary, Recommended Next Steps.
- Ilan linki yalnizca kullanicinin verdigi veya gercek web taramasi ile dogrulanmis gercek detay sayfasi URL'lerinden alinmali.
- Arama sayfasina, liste sayfasina, filtre sayfasina veya kategori sayfasina yonlendiren URL'ler gecersizdir ve asla verilmemeli.
- Detay sayfasi URL'si kesin olarak dogrulanamiyorsa hic URL verme; bunun yerine ilan basligini, platformunu ve ilan numarasini yaz.
- Firsat ve risk gruplari net ayrilmis olmali.
- Tramer tutarsizliklari acikca raporlanmali.
- Sonuclarda yer alan her ilan icin tramer degerlendirmesi zorunludur. Tramer tutari, boyali/degisen parca bilgisi, aciklama ile tutarliligi ve guvenilirlik yorumu her ilanin ciktisinda ayri bir alan olarak yer almali. Tramer bilgisi belirtilmemisse bu durum acikca "tramer bilgisi ilanda belirtilmemis — bagimsiz sorgu onerilir" olarak yazilmali; bos birakilmamali.
- Kirmizi bayraklar kategorize edilmis ve ciddiyet seviyesi belirtilmis olmali.
- Fiyat konumlama kaba araliklarda sunulmali; kesin deger bicilmemeli.
- Kesin alim/satim tavsiyesi yerine risk seviyesi ve kosullu degerlendirme verilmeli.
- Eksik veri acikca belirtilmeli ve fiziksel muayene her zaman onerilmeli.
- Galeri ilani ile gercek sahip ilani ayrimi gorunur olmali.

## Failure Patterns To Avoid

- Tramer tutarini ilan aciklamasiyla karsilastirmadan dogru kabul etmek
- "Tramersiz" iddiasini otomatik guvenilir saymak
- Asiri dusuk fiyati sorgusuz firsat olarak sunmak
- Eksik kilometre, fotograf veya tramer bilgisi ile kesin degerlendirme yapmak
- Galeri dilini ("araclarimiz", "magzamizi ziyaret") fark etmemek
- Ilan linklerini ciktidan cikarmak
- Gercek olmayan, sahte veya arama sayfasina dusen URL'ler uretmek
- Dogrulanmamis ilan URL'lerini gercek ilan linki gibi sunmak
- Detay sayfasi oldugundan kesin emin olunmayan URL'leri vermek
- "Hemen alin" gibi garanti tavsiye vermek
- Boyali/degisen parca iddiasini tramer kaydiyla karsilastirmamak
- Fiyat veya tramer bilgisini arama sayfasindan okuyamayinca "gorunmuyor" deyip analizi atlamak; ilan detay sayfasini ziyaret etmeli veya kullanicidan istemeli
- Kullanici belirli bir marka/model istemedigi halde tek bir marka veya modele odaklanmak; en az 3-4 farkli markadan ilan sunulmali
- Ilanin aciklama metnini okumadan veya analiz etmeden o ilani firsat ya da risk olarak siniflandirmak
- Herhangi bir ilani tramer degerlendirmesi yapmadan veya tramer bilgisini ciktiya yazmadan sunmak
- Ilan detay sayfasindaki eksper/hasar raporu gorselini kontrol etmeden tramer degerlendirmesi yapmak
- Eksper gorselindeki boyali/degisen parca bilgisini aciklama metniyle capraz kontrol etmemek
- Arama sayfasina, liste sayfasina veya filtre sayfasina yonlendiren URL'leri ilan linki olarak vermek
- "JavaScript sitesi oldugu icin URL alinamadi" gibi bahanelerle arama/listing sayfasi linki vermek; sadece dogrulanmis detay sayfasi linki verilebilir

## References

- Test senaryolari ve puanlama rubrigi icin [`examples/compositions/used-car-scout-tests.md`](../../examples/compositions/used-car-scout-tests.md) dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel ilan tarama otomasyonu, web scraping araci veya platform API entegrasyonu adapter katmaninda belgelenmelidir.
- Varsayilan gorev ilan verisi uzerinden analiz ve karar destegi uretmektir; otomatik satin alma islemi baslatmak degildir.
- Referans platformlar sahibinden.com, arabam.com ve letgo'dur; baska ulke veya platform uyarlamalari adapter katmaninda yapilabilir.
