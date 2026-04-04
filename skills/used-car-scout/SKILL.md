---
name: used-car-scout
description: Use when a user wants second-hand car listings in a given location and radius analyzed for opportunities and risks, with tramer verification, red flag detection, pricing comparison, and listing links.
---

# Used Car Scout

## Use When

- Kullanici belirlenen konum ve yaricapta ikinci el arac ilanlarini taratmak istediginde
- Firsat araclari ve uzak durulmasi gereken araclari ilan linki ile birlikte gormek istediginde
- Tramer bilgisinin ilan aciklamasiyla tutarli olup olmadigini kontrol ettirmek istediginde
- Birden fazla ilani fiyat, km, yas, donanim ve tramer ekseninde karsilastirmak istediginde
- Ilan aciklamalarindaki supheli ifadeleri, eksik bilgileri ve manipulasyon isaretlerini tespit ettirmek istediginde
- Galeri ilani ile gercek sahip ilanini ayirt etmek istediginde

## Workflow

1. Arama kapsamini belirle: konum (sehir, ilce), yaricap (km), butce araligi, marka/model tercihi, yil araligi, km siniri, yakit tipi ve vites tercihi. Eksik kritik parametreleri kullanicidan iste; ikincil tercihleri makul varsayimlarla doldur.

2. Hedef platformlari tanimla: sahibinden.com, arabam.com, letgo ve benzeri Turkiye merkezli ikinci el arac platformlari. Kullanici belirli bir platform belirtmisse ona oncelik ver.

3. Ilanlari topla ve normalize et: her ilan icin marka, model, paket, model yili, kilometre, yakit tipi, vites, fiyat, konum, tramer tutari ve detayi, boyali/degisen parca bilgisi, sahip sayisi, ilan tarihi, ilan linki ve aciklama metnini ayristir.

4. Tramer dogrulama katmanini calistir:
   - Tramer tutarinin ilan aciklamasiyla tutarliligini kontrol et.
   - "Tramersiz" iddialarinin makullugunu degerlendir.
   - Boyali/degisen parca ile tramer arasindaki uyumsuzluklari isaretle.
   - Yanlis veya eksik girilmis olabilecek tramer verilerini tespit et.

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

8. Her arac icin karar destekleyici ozet olustur: ilan linki, fiyat konumlama, tramer degerlendirmesi, kirmizi bayrak ozeti, genel risk seviyesi ve onerilen sonraki adim.

9. Tum cikti boyunca kanit ile varsayimi ayir, eksik veriyi gizleme, garanti alim/satim tavsiyesi verme, kesin fiyat degerlendirmesi yerine kaba araliklar sun.

## Output Expectations

- Cikti su bolumlerden olusmali: Search Summary, Market Snapshot, Opportunity Vehicles, Vehicles to Avoid, Tramer Consistency Overview, Red Flag Summary, Recommended Next Steps.
- Her arac icin ilan linki mutlaka dahil edilmeli.
- Firsat ve risk gruplari net ayrilmis olmali.
- Tramer tutarsizliklari acikca raporlanmali.
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
- "Hemen alin" gibi garanti tavsiye vermek
- Boyali/degisen parca iddiasini tramer kaydiyla karsilastirmamak

## References

- Test senaryolari ve puanlama rubrigi icin [`examples/compositions/used-car-scout-tests.md`](../../examples/compositions/used-car-scout-tests.md) dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel ilan tarama otomasyonu, web scraping araci veya platform API entegrasyonu adapter katmaninda belgelenmelidir.
- Varsayilan gorev ilan verisi uzerinden analiz ve karar destegi uretmektir; otomatik satin alma islemi baslatmak degildir.
- Referans platformlar sahibinden.com, arabam.com ve letgo'dur; baska ulke veya platform uyarlamalari adapter katmaninda yapilabilir.
