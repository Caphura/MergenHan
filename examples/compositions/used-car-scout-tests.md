# Used Car Scout Test Pack

Bu belge, `Used Car Scout` blueprint'i icin farkli AI ortamlarda uygulanabilecek test senaryolarini toplar. Amac, modelin ilanları dogru analiz edip firsat ve risk ayristirmasini, tramer tutarsizlik tespitini, kirmizi bayrak taramasini ve fiyat karsilastirmasini guvenilir sekilde yapabildigini test etmektir.

## Kullanim Sekli

Her testten once asagidaki acilis talimatini kullan. Bu talimati once AI oturumuna yapistir, ardindan test girdisini ver.

```text
MergenHan prompt kutuphanesindeki used-car-scout blueprint'inin cekirdek davranisini kullan.

Gorevi su adimlarla yap:

1. Verilen konum ve yaricap icindeki ikinci el arac ilanlarini analiz et.
2. Her ilan icin tramer dogrulama yap: tramer tutarinin ilan aciklamasiyla tutarli olup olmadigini kontrol et.
3. Her ilan icin kirmizi bayrak taramasi yap: supheli ifadeler, veri tutarsizliklari, eksik bilgiler.
4. Her ilan icin fiyat konumlama yap: piyasanin altinda, civarinda veya ustunde mi?
5. Ilanlari iki gruba ayir: Firsat Araclari ve Uzak Durulmasi Gereken Araclar.
6. Her arac icin ilan linkini muhakkak ver.

Ciktini su yapida sun:

- Search Summary
- Market Snapshot
- Opportunity Vehicles (ilan linki, fiyat konumlama, tramer durumu, guc sinyalleri)
- Vehicles to Avoid (ilan linki, tespit edilen riskler, kirmizi bayraklar)
- Tramer Consistency Overview
- Red Flag Summary
- Recommended Next Steps

Onemli kurallar:
- Kanit ile varsayimi her zaman ayir.
- Tramer verisini uydurma veya duzeltme.
- Kesin alim/satim tavsiyesi verme; risk seviyesi sun.
- Eksik veriyi gizleme.
- Her aracin ilan linkini mutlaka dahil et.
```

## Test Senaryolari

### UCS1 - Temel konum + butce taramasi

**Amac:** Model, konum ve butce araligi verildikten sonra ilanlari tarayip yapilandirilmis cikti uretebiliyor mu?

**Test girdisi:**

```text
Ankara Cankaya civarinda 30 km yaricapta, 400.000 - 600.000 TL butce araliginda, 2018 model ve uzeri, 150.000 km altinda ikinci el SUV ariyorum. Sahibinden.com ve arabam.com'da bakabilirsin. Otomatik vites tercihim var ama sarti degil.
```

**Beklenen guclu davranis:**

- Arama kapsamini dogru ozetlemeli (konum, yaricap, butce, yil, km, vites tercihi)
- Hedef platformlari belirtmeli
- Bulunan ilanlari normalize edip fiyat/km/yas ekseninde karsilastirmali
- Her ilan icin tramer, kirmizi bayrak ve fiyat degerlendirmesi yapmali
- Firsat ve risk grubunu net ayirmali
- Her arac icin ilan linkini vermeli

**Kirmizi bayraklar:**

- Konum veya yaricap bilgisini goz ardi etmek
- Butce disindaki araclari listeye dahil etmek
- Tramer veya kirmizi bayrak analizi atlamak
- Ilan linkleri olmadan sonuc vermek

---

### UCS2 - Tramer tutarsizligi tespiti

**Amac:** Model, tramer bilgisi ile ilan aciklamasi arasindaki celiskiyi tespit edebiliyor mu?

**Test girdisi:**

```text
Su iki ilani karsilastir:

Ilan A:
- 2019 Volkswagen Tiguan 1.5 TSI, 85.000 km, 580.000 TL
- Tramer: 0 TL
- Aciklama: "Arac cok temiz, sol arka camurluk boyali, on tampon degisen. Kucuk park hasari disinda sorun yok."
- Link: https://www.sahibinden.com/ilan/ornek-ilan-a

Ilan B:
- 2019 Volkswagen Tiguan 1.5 TSI, 92.000 km, 545.000 TL
- Tramer: 28.500 TL
- Aciklama: "Arac bakimli ve temiz. Tramer kaydi kucuk bir park kazasindan kaynaklidir. Degisen ve boyali parca yoktur."
- Link: https://www.sahibinden.com/ilan/ornek-ilan-b
```

**Beklenen guclu davranis:**

- Ilan A'da kritik tramer tutarsizligi tespit etmeli: boyali + degisen parca var ama tramer 0 TL
- Ilan B'de de tutarsizlik gormeli: 28.500 TL tramer var ama "degisen ve boyali parca yoktur" diyor
- Her iki celiskiyi acikca raporlamali
- Risk seviyesini farkli derecelendirmeli (Ilan A daha ciddi cunku tramer sifir gosterilmis)
- Bagimsiz tramer sorgusu onermeli

**Kirmizi bayraklar:**

- Tramer tutarsizligini atlama
- Ilan A'nin tramer verisini dogru kabul etme
- Ilan B'nin "degisen parca yok" iddiasini tramer kaydiyla celisen halde sorgulamama
- Her iki ilanda da sorun gormeme

---

### UCS3 - Ilan dili ve kirmizi bayrak taramasi

**Amac:** Model, ilan aciklamasindaki supheli ifadeleri ve uslup kirmizi bayraklarini tespit edebiliyor mu?

**Test girdisi:**

```text
Su uc ilani kirmizi bayrak acisindan degerlendir:

Ilan 1:
- 2017 Ford Focus 1.5 TDCi, 120.000 km, 320.000 TL
- Aciklama: "ACIL SATILIK!!! Bugun satilacak, pazarlik yok, takas yok. Aracta hicbir sorun yoktur. Arayanlar lutfen ciddi olsun."
- Fotograf: 3 dis fotograf, ic mekan yok, motor bolumesi yok
- Link: https://www.sahibinden.com/ilan/ornek-ilan-1

Ilan 2:
- 2020 Toyota Corolla 1.8 Hybrid, 45.000 km, 620.000 TL
- Aciklama: "Garajda kullanilmistir. Tum bakimlari yetkili serviste yapilmistir. Servis kayitlari mevcuttur. Muayenesi yeni yapilmistir. 2. sahibinden."
- Fotograf: 15 fotograf, dis, ic, motor, bagaj, detay
- Link: https://www.sahibinden.com/ilan/ornek-ilan-2

Ilan 3:
- 2016 Renault Megane 1.5 dCi, 85.000 km, 280.000 TL
- Aciklama: "arac temiz sorunsuz motor trt bak yapildi yag flt deisdi lastik yeni servis bakimmli alinir kulanalir"
- Fotograf: 6 fotograf, hepsi dusuk cozunurluklu
- Link: https://www.sahibinden.com/ilan/ornek-ilan-3
```

**Beklenen guclu davranis:**

- Ilan 1 icin yuksek risk: baskici dil ("ACIL", "bugun satilacak"), "sorun yok" gibi genel iddia, yetersiz fotograf (ic/motor yok), "pazarlik yok" + "takas yok" kombinasyonu
- Ilan 2 icin dusuk risk: detayli aciklama, servis gecmisi referansi, yeterli fotograf, net sahip bilgisi
- Ilan 3 icin orta risk: imla hatalari ve ozensiz dil (galeri isareti olabilir), dusuk cozunurluklu fotograflar, belirsiz ifadeler
- Her ilan icin kirmizi bayrak sayisi ve ciddiyet seviyesi
- Ilan 2'yi guvenilir ilan olarak one cikarmali

**Kirmizi bayraklar:**

- Ilan 1'deki baskici dili goz ardi etmek
- Ilan 2'de olmayan sorunlar uydurmak
- Ilan 3'un ozensiz dilini ve fotograf kalitesini atlama
- Tum ilanlari ayni risk seviyesinde gormek

---

### UCS4 - Fiyat karsilastirma ve firsat puanlama

**Amac:** Model, benzer araclarin fiyat karsilastirmasini yapip firsat ve pahali araclari dogru ayirabiliyor mu?

**Test girdisi:**

```text
Istanbul Anadolu Yakasi'nda 2019-2021 arasi Hyundai Tucson 1.6 CRDi otomatik ariyorum. Butcem 550.000 - 750.000 TL. Su ilanlari karsilastir:

Ilan X: 2020, 65.000 km, 620.000 TL, Elite Plus paket, tramer 0, beyaz
Link: https://www.sahibinden.com/ilan/ornek-x

Ilan Y: 2019, 110.000 km, 580.000 TL, Style paket, tramer 12.000 TL (on tampon boyali), gri
Link: https://www.sahibinden.com/ilan/ornek-y

Ilan Z: 2021, 40.000 km, 730.000 TL, Elite paket, tramer 0, siyah
Link: https://www.sahibinden.com/ilan/ornek-z

Ilan W: 2020, 85.000 km, 490.000 TL, Style paket, tramer 0, beyaz, aciklama: "yurt disindan geldim acil satiyorum"
Link: https://www.sahibinden.com/ilan/ornek-w
```

**Beklenen guclu davranis:**

- Ilanlari yil/km/donanim normalizi ile karsilastirmali
- Ilan X: dusuk km + ust donanim + temiz tramer = iyi aday ama fiyati yuksek mi kontrol etmeli
- Ilan Y: yuksek km + dusuk donanim + tramer var ama aciklanmis = orta aday, fiyat uygun olabilir
- Ilan Z: en dusuk km + en yeni + temiz tramer = fiyat piyasa civari veya ustu, premium konumda
- Ilan W: piyasanin belirgin altinda fiyat + "acil satiyorum" = firsat gibi gorunur AMA asiri dusuk fiyat + baskici dil = kirmizi bayrak; cok dikkatli yaklasim
- "Too good to be true" mantigini Ilan W'de uygulamali
- Fiyat siralamasini donanim ve km farkliligiyla normalize etmeli

**Kirmizi bayraklar:**

- Ilan W'yu sorgusuz firsat olarak sunmak
- Donanim farklarini (Elite Plus vs Style) fiyata yansitmamak
- Km farklarini goz ardi etmek
- Tum ilanlari ayni kategoride degerlendirmek

---

### UCS5 - Eksik bilgi ve sinirli veri durumu

**Amac:** Model, yetersiz veri ile kesin yorum yapmaktan kacinabiliyor mu?

**Test girdisi:**

```text
Izmir civarinda bir arac ilani buldum, sadece su bilgiler var:

- 2018 Mercedes C180, 340.000 TL
- Fotografta plaka gorunmuyor, arac kenardan cekilmis tek fotograf var
- Aciklamada sadece "temiz arac, ilgilenen arasin" yazilmis
- Tramer bilgisi belirtilmemis
- Km bilgisi ilanda yok
- Link: https://www.sahibinden.com/ilan/ornek-eksik
```

**Beklenen guclu davranis:**

- Veri yetersizligini acikca belirtmeli
- Kesin fiyat konumlama yapmaktan kacinmali (km bilinmeden fiyat karsilastirmasi anlamli degil)
- Tek fotografi ve plaka gizlemeyi kirmizi bayrak olarak isaretlemeli
- Tramer bilgisi eksikligini onemli risk olarak belirtmeli
- "Bu ilanla ilgili guvenilir degerlendirme yapilamaz" gibi net bir ifade kullanmali
- Fiziksel inceleme ve bagimsiz tramer sorgusu onermeli
- Kesinlikle "kacinilmaz firsat" veya "sorun yok" gibi bir yorum yapmamali

**Kirmizi bayraklar:**

- Eksik bilgiye ragmen kesin yorum yapmak
- Km olmadan fiyat karsilastirmasi yapmak
- Tek fotografi ve plaka gizlemeyi normal karsilamak
- Tramer eksikligini goz ardi etmek

---

### UCS6 - Coklu platform ve genis tarama

**Amac:** Model, birden fazla platform ve genis bir arama alanini sistematik sekilde yonetebiliyor mu?

**Test girdisi:**

```text
Bursa merkez 40 km yaricapta, 250.000 - 400.000 TL araliginda, 2015-2019 arasi, dizel, manuel vites, sedan arac ariyorum. Marka farketmez. Sahibinden, arabam.com ve letgo'da bak. En az 10 ilani tara ve bana en iyi 3 firsati ve en kottu 3 riski goster.
```

**Beklenen guclu davranis:**

- Tarama kapsamini dogru ozetlemeli
- Birden fazla platformu organize sekilde taramali
- En az 10 ilan degerlendirmeli
- Her ilanda tramer + kirmizi bayrak + fiyat analizi yapmali
- En iyi 3 firsati guc sinyalleriyle sunmali
- En riskli 3 araci gerekceleriyle sunmali
- Tum ilan linklerini dahil etmeli
- Piyasa genel gorunumu vermeli

**Kirmizi bayraklar:**

- Tek platformla sinirli kalmak
- 10'dan az ilan degerlendirmek
- Firsat ve risk ayristirmasini yapmamak
- Herhangi bir ilani linksiz birakmak

---

### UCS7 - Galeri ilani vs sahibinden ilani ayrimi

**Amac:** Model, ilan sahibinin galeri mi gercek sahip mi oldugunu ayirt edebiliyor mu?

**Test girdisi:**

```text
Su iki ilani karsilastir:

Ilan P:
- 2019 Fiat Egea 1.3 Multijet, 75.000 km, 370.000 TL
- Ilan sahibi: "Ahmet Y." (ozel ilan)
- Aciklama: "Aracimi is degisikligi nedeniyle satiyorum. 2019'dan beri ilk sahibiyim. Tum bakimlari Fiat yetkili serviste yaptirdim. Muayene 2027'ye kadar gecerli. Ekspertiz raporunu da paylasabilirim."
- 12 fotograf, detayli
- Link: https://www.sahibinden.com/ilan/ornek-p

Ilan Q:
- 2019 Fiat Egea 1.3 Multijet, 80.000 km, 355.000 TL
- Ilan sahibi: "Ahmet Y." (ozel ilan)
- Aciklama: "Araclarimiz profesyonel olarak kontrol edilmistir. Tum araclarimiz garantili olarak teslim edilir. Takas ve kredi imkani mevcuttur. Diger araclarimiz icin magzamizi ziyaret edebilirsiniz."
- 8 fotograf, standart acili
- Link: https://www.sahibinden.com/ilan/ornek-q
```

**Beklenen guclu davranis:**

- Ilan P'yi gercek sahip ilani olarak degerlendirmeli (kisisel hikaye, yetkili servis, ekspertiz teklifi)
- Ilan Q'yu galeri ilani olarak tespit etmeli ("araclarimiz", "magzamizi ziyaret", kredi/takas)
- Galeri ilaninin "ozel ilan" olarak gosterilmesini kirmizi bayrak saymaali
- Fiyat farkliliklarina ragmen Ilan P'nin guven sinyallerinin daha guclu oldugunu belirtmeli

**Kirmizi bayraklar:**

- Galeri diline ragmen Ilan Q'yu gercek sahip ilani olarak kabul etmek
- "Ozel ilan" etiketini yeterli kanit olarak gormek
- Her iki ilani ayni guvenilirlikte degerlendirmek

---

### UCS8 - Governance kurallarinin testi

**Amac:** Model, kanitsiz iddialarda bulunmaktan kaciniyor mu ve eksik veriyi acikca belirtiyor mu?

**Test girdisi:**

```text
Bu arac hakkinda ne dusunuyorsun? Hemen alayim mi?

2020 BMW 320i, 60.000 km, 680.000 TL, tramer 0, beyaz
Aciklama: "Kusursuz arac, garajda kullanildi, cizik bile yok."
Link: https://www.sahibinden.com/ilan/ornek-governance
```

**Beklenen guclu davranis:**

- "Hemen alayim mi?" sorusuna kesin "al" veya "alma" demekten kacinmali
- Mevcut verilere dayali bir risk degerlendirmesi sunmali
- Eksik bilgileri (servis gecmisi, sahip sayisi, donanim detayi) isaretemeli
- "Kusursuz" ve "cizik bile yok" gibi kanitlanamaz ifadeleri sorgulamali
- Fiziksel muayene ve bagimsiz ekspertiz onermeli
- Kesin satin alma tavsiyesi yerine "risk seviyesi dusuk gorunuyor, ancak su dogrulamalar yapilmali" gibi kosullu bir ifade kullanmali

**Kirmizi bayraklar:**

- "Evet, al" veya "Hayir, alma" gibi kesin tavsiye vermek
- "Kusursuz" iddiasini kanit olarak kabul etmek
- Eksik bilgileri goz ardi etmek
- Fiziksel muayene onermemek

## Onerilen Test Sirasi

1. `UCS1` - temel tarama yetenegini test eder
2. `UCS2` - tramer tutarsizlik tespitini test eder (kritik)
3. `UCS3` - kirmizi bayrak taramasini test eder
4. `UCS4` - fiyat karsilastirma ve firsat puanlamasini test eder
5. `UCS5` - eksik veri davranisinni test eder (governance)
6. `UCS6` - genis tarama ve organizasyon becerisini test eder
7. `UCS7` - galeri/sahip ayrimi becerisini test eder
8. `UCS8` - governance kurallarinin uygulanmasini test eder

Ilk 4 test cekirdek davranisi olcer; son 4 test gelismis ayirt etme ve governance disiplinini olcer.

## Puanlama Rubrigi

| Olcut | Ne aranir? |
| --- | --- |
| Tramer Tutarlilik Tespiti | Tramer tutari ile ilan aciklamasi arasindaki celiskiyi buluyor mu |
| Kirmizi Bayrak Taramasi | Supheli ifadeleri, eksik bilgileri ve manipulasyon isaretlerini yakalayabiliyor mu |
| Fiyat Konumlama | Fiyati benzer araclarla dogru karsilastirip firsat/pahali ayrimini yapabiliyor mu |
| Firsat vs Risk Ayristirmasi | Ilanlari guvenilir bir sekilde iki gruba ayirabiliyor mu |
| Ilan Linki Disiplini | Her arac icin ilan linkini veriyor mu |
| Governance Disiplini | Kanitsiz iddialarda bulunmaktan kaciniyor mu, eksik veriyi gizlemiyor mu |
| Cikti Yapisi | Beklenen baslik ve bolumleri uretiyor mu, taranabilir mi |
| Benzer Arac Normalizasyonu | Yil, km, donanim farklarini fiyat karsilastirmasina dogru yansitaiyor mu |

## Kisa Sonuc Formu

```text
AI:
Test ID:
Tramer tutarsizligini buldu mu:
Kirmizi bayraklari dogru tespit etti mi:
Fiyat konumlama dogru muydu:
Firsat / risk ayristirmasi mantikli miydi:
Ilan linkleri dahil miydi:
Kanitsiz iddia uydurdu mu:
Eksik veriyi acikca belirtti mi:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
