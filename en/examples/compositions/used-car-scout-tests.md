# Used Car Scout Test Pack

This document `Used Car Scout` blueprint'i icin different AI ortamlarda uygulanabilecek test senaryolarini toplar. Amac, modelin listingları correct analysis edip firsat ve risk separatemasini, tramer tutarsizlik tespitini, kirmizi bayrak taramasini ve fiyat karsilastirmasini guvenilir way yapabildigini test etmektir.

## Usage

Her testten once asagidaki acilis talimatini kullan. Bu talimati once AI oturumuna paste, then test girdisini ver.

```text
MergenHan prompt librarysindeki used-car-scout blueprint'inin core davranisini kullan.

Gorevi su adimlarla yap:

1. Verilen konum ve yaricap icindeki used car vehicle listinglarini analysis et.
2. Her listing icin tramer validation yap: tramer tutarinin listing aciklamasiyla tutarli olup olmadigini kontrol et.
3. Her listing icin kirmizi bayrak taramasi yap: supheli ifadeler, veri tutarsizliklari, eksik bilgiler.
4. Her listing icin fiyat konumlama yap: piyasanin altinda, civarinda veya ustunde mi?
5. Ilanlari iki gruba ayir: Firsat Araclari ve Uzak Durulmasi Gereken Araclar.
6. Her vehicle icin varsa only gercek listing detay linkini ver; arama, liste veya filtre sayfasi linki asla verme.

Ciktini su yapida sun:

- Search Summary
- Market Snapshot
- Opportunity Vehicles (listing linki, fiyat konumlama, tramer durumu, guc sinyalleri)
- Vehicles to Avoid (listing linki, tespit edilen riskler, kirmizi bayraklar)
- Tramer Consistency Overview
- Red Flag Summary
- Recommended Next Steps

Onemli rules:
- Kanit ile assumptioni her zaman ayir.
- Tramer verisini fabricated veya fix.
- Kesin alim/satim tavsiyesi verme; risk seviyesi sun.
- Eksik veriyi gizleme.
- Her vehiclein varsa only gercek listing detay linkini dahil et; detay linki yoksa URL fabricated.
- Arama sonuclari, liste sayfalari veya filtre URL'leri asla listing linki olarak verilmemeli.
- Detay sayfasi linki kesin dogrulanamiyorsa hic URL verme; onun yerine listing basligini ve platformunu yaz.
```

## Test Senaryolari

### UCS1 - Temel konum + butce taramasi

**Amac:** Model, konum ve butce araligi verildikten sonra listinglari tarayip structured output uretebiliyor mu?

**Test girdisi:**

```text
Ankara Cankaya civarinda 30 km yaricapta, 400.000 - 600.000 TL butce araliginda, 2018 model ve uzeri, 150.000 km altinda used car SUV ariyorum. Sahibinden.com ve arabam.com'da bakabilirsin. Otomatik vites tercihim var ama sarti degil.
```

**Expected guclu davranis:**

- Arama kapsamini correct ozetlemeli (konum, yaricap, butce, yil, km, vites tercihi)
- Hedef platformlari belirtmeli
- Bulunan listinglari normalize edip fiyat/km/yas ekseninde karsilastirmali
- Her listing icin tramer, kirmizi bayrak ve fiyat degerlendirmesi yapmali
- Firsat ve risk grubunu net ayirmali
- Her vehicle icin varsa only gercek listing detay linkini vermeli

**Red flags:**

- Konum veya yaricap bilgisini goz ardi etmek
- Butce disindaki vehiclelari listeye dahil etmek
- Tramer veya kirmizi bayrak analysis atlamak
- Ilan linkleri olmadan sonuc vermek
- Arama/listing sayfasi linki vermek
- Detay sayfasi dogrulanmamis URL fabricatedk

---

### UCS2 - Tramer tutarsizligi tespiti

**Amac:** Model, tramer bilgisi ile listing aciklamasi arasindaki celiskiyi tespit edebiliyor mu?

**Test girdisi:**

```text
Su iki listingi karsilastir:

Ilan A:
- 2019 Volkswagen Tiguan 1.5 TSI, 85.000 km, 580.000 TL
- Tramer: 0 TL
- Aciklama: "Arac cok temiz, sol arka camurluk boyali, on tampon degisen. Kucuk park hasari disinda sorun yok."
- Link: https://www.sahibinden.com/listing/example-listing-a

Ilan B:
- 2019 Volkswagen Tiguan 1.5 TSI, 92.000 km, 545.000 TL
- Tramer: 28.500 TL
- Aciklama: "Arac maintenanceli ve temiz. Tramer kaydi kucuk bir park kazasindan kaynaklidir. Degisen ve boyali parca yoktur."
- Link: https://www.sahibinden.com/listing/example-listing-b
```

**Expected guclu davranis:**

- Ilan A'da kritik tramer tutarsizligi tespit etmeli: boyali + degisen parca var ama tramer 0 TL
- Ilan B'de de tutarsizlik gormeli: 28.500 TL tramer var ama "degisen ve boyali parca yoktur" diyor
- Her iki celiskiyi explicitly raporlamali
- Risk seviyesini different derecelendirmeli (Ilan A daha ciddi cunku tramer sifir gosterilmis)
- Bagimsiz tramer sorgusu onermeli

**Red flags:**

- Tramer tutarsizligini atlama
- Ilan A'nin tramer verisini correct kabul etme
- Ilan B'nin "degisen parca yok" iddiasini tramer kaydiyla celisen halde sorgulamama
- Her iki listingda da sorun gormeme

---

### UCS3 - Ilan dili ve kirmizi bayrak taramasi

**Amac:** Model, listing aciklamasindaki supheli ifadeleri ve uslup kirmizi bayraklarini tespit edebiliyor mu?

**Test girdisi:**

```text
Su uc listingi kirmizi bayrak acisindan degerlendir:

Ilan 1:
- 2017 Ford Focus 1.5 TDCi, 120.000 km, 320.000 TL
- Aciklama: "ACIL SATILIK!!! Bugun satilacak, pazarlik yok, takas yok. Aracta hicbir sorun yoktur. Arayanlar lutfen ciddi olsun."
- Fotograf: 3 dis fotograf, ic mekan yok, motor bolumesi yok
- Link: https://www.sahibinden.com/listing/example-listing-1

Ilan 2:
- 2020 Toyota Corolla 1.8 Hybrid, 45.000 km, 620.000 TL
- Aciklama: "Garajda kullanilmistir. Tum maintenancelari yetkili serviste yapilmistir. Servis kayitlari mevcuttur. Muayenesi yeni yapilmistir. 2. sahibinden."
- Fotograf: 15 fotograf, dis, ic, motor, bagaj, detay
- Link: https://www.sahibinden.com/listing/example-listing-2

Ilan 3:
- 2016 Renault Megane 1.5 dCi, 85.000 km, 280.000 TL
- Aciklama: "vehicle temiz sorunsuz motor trt bak yapildi yag flt deisdi lastik yeni servis maintenancemli alinir kulanalir"
- Fotograf: 6 fotograf, hepsi dusuk cozunurluklu
- Link: https://www.sahibinden.com/listing/example-listing-3
```

**Expected guclu davranis:**

- Ilan 1 icin yuksek risk: baskici dil ("ACIL", "bugun satilacak"), "sorun yok" such as genel iddia, yetersiz fotograf (ic/motor yok), "pazarlik yok" + "takas yok" kombinasyonu
- Ilan 2 icin dusuk risk: detayli description, servis gecmisi referansi, yeterli fotograf, net sahip bilgisi
- Ilan 3 icin orta risk: imla hatalari ve ozensiz dil (galeri isareti olabilir), dusuk cozunurluklu fotograflar, belirsiz ifadeler
- Her listing icin kirmizi bayrak sayisi ve ciddiyet seviyesi
- Ilan 2'yi guvenilir listing olarak one cikarmali

**Red flags:**

- Ilan 1'deki baskici dili goz ardi etmek
- Ilan 2'de olmayan sorunlar fabricatedk
- Ilan 3'un ozensiz dilini ve fotograf kalitesini atlama
- Tum listinglari same risk seviyesinde gormek

---

### UCS4 - Fiyat karsilastirma ve firsat puanlama

**Amac:** Model, benzer vehiclelarin fiyat karsilastirmasini yapip firsat ve pahali vehiclelari correct ayirabiliyor mu?

**Test girdisi:**

```text
Istanbul Anadolu Yakasi'nda 2019-2021 arasi Hyundai Tucson 1.6 CRDi otomatik ariyorum. Butcem 550.000 - 750.000 TL. Su listinglari karsilastir:

Ilan X: 2020, 65.000 km, 620.000 TL, Elite Plus package, tramer 0, beyaz
Link: https://www.sahibinden.com/listing/example-x

Ilan Y: 2019, 110.000 km, 580.000 TL, Style package, tramer 12.000 TL (on tampon boyali), gri
Link: https://www.sahibinden.com/listing/example-y

Ilan Z: 2021, 40.000 km, 730.000 TL, Elite package, tramer 0, siyah
Link: https://www.sahibinden.com/listing/example-z

Ilan W: 2020, 85.000 km, 490.000 TL, Style package, tramer 0, beyaz, description: "yurt disindan geldim acil satiyorum"
Link: https://www.sahibinden.com/listing/example-w
```

**Expected guclu davranis:**

- Ilanlari yil/km/donanim normalizi ile karsilastirmali
- Ilan X: dusuk km + ust donanim + temiz tramer = iyi aday ama fiyati yuksek mi kontrol etmeli
- Ilan Y: yuksek km + dusuk donanim + tramer var ama aciklanmis = orta aday, fiyat uygun olabilir
- Ilan Z: en dusuk km + en yeni + temiz tramer = fiyat piyasa civari veya ustu, premium konumda
- Ilan W: piyasanin belirgin altinda fiyat + "acil satiyorum" = firsat such as gorunur AMA asiri dusuk fiyat + baskici dil = kirmizi bayrak; cok dikkatli yaklasim
- "Too good to be true" mantigini Ilan W'de uygulamali
- Fiyat siralamasini donanim ve km farkliligiyla normalize etmeli

**Red flags:**

- Ilan W'yu sorgusuz firsat olarak sunmak
- Donanim farklarini (Elite Plus vs Style) fiyata yansitmamak
- Km farklarini goz ardi etmek
- Tum listinglari same kategoride degerlendirmek

---

### UCS5 - Eksik bilgi ve sinirli veri durumu

**Amac:** Model, yetersiz veri ile kesin yorum yapmaktan kacinabiliyor mu?

**Test girdisi:**

```text
Izmir civarinda bir vehicle listingi buldum, only su bilgiler var:

- 2018 Mercedes C180, 340.000 TL
- Fotografta plaka gorunmuyor, vehicle kenardan cekilmis tek fotograf var
- Aciklamada only "temiz vehicle, ilgilenen arasin" yazilmis
- Tramer bilgisi belirtilmemis
- Km bilgisi listingda yok
- Link: https://www.sahibinden.com/listing/example-eksik
```

**Expected guclu davranis:**

- Veri yetersizligini explicitly belirtmeli
- Kesin fiyat konumlama yapmaktan kacinmali (km bilinmeden fiyat karsilastirmasi anlamli degil)
- Tek fotografi ve plaka gizlemeyi kirmizi bayrak olarak isaretlemeli
- Tramer bilgisi eksikligini onemli risk olarak belirtmeli
- "Bu listingla related guvenilir evaluation yapilamaz" such as net bir ifade kullanmali
- Fiziksel inceleme ve bagimsiz tramer sorgusu onermeli
- Kesinlikle "kacinilmaz firsat" veya "sorun yok" such as bir yorum yapmamali

**Red flags:**

- Eksik bilgiye ragmen kesin yorum yapmak
- Km olmadan fiyat karsilastirmasi yapmak
- Tek fotografi ve plaka gizlemeyi normal karsilamak
- Tramer eksikligini goz ardi etmek

---

### UCS6 - Coklu platform ve genis tarama

**Amac:** Model, birden fazla platform ve genis bir arama alanini sistematik way yonetebiliyor mu?

**Test girdisi:**

```text
Bursa merkez 40 km yaricapta, 250.000 - 400.000 TL araliginda, 2015-2019 arasi, dizel, manual vites, sedan vehicle ariyorum. Marka farketmez. Sahibinden, arabam.com ve letgo'da bak. En az 10 listingi tara ve bana en iyi 3 firsati ve en kottu 3 riski goster.
```

**Expected guclu davranis:**

- Tarama kapsamini correct ozetlemeli
- Birden fazla platformu organize way taramali
- En az 10 listing degerlendirmeli
- Her listingda tramer + kirmizi bayrak + fiyat analysis yapmali
- En iyi 3 firsati guc sinyalleriyle sunmali
- En riskli 3 vehiclei gerekceleriyle sunmali
- Tum listing linklerini dahil etmeli
- Piyasa genel gorunumu vermeli

**Red flags:**

- Tek platformla sinirli kalmak
- 10'dan az listing degerlendirmek
- Firsat ve risk separatemasini yapmamak
- Herhangi bir listingi linksiz birakmak

---

### UCS7 - Galeri listingi vs sahibinden listingi ayrimi

**Amac:** Model, listing sahibinin galeri mi gercek sahip mi oldugunu ayirt edebiliyor mu?

**Test girdisi:**

```text
Su iki listingi karsilastir:

Ilan P:
- 2019 Fiat Egea 1.3 Multijet, 75.000 km, 370.000 TL
- Ilan sahibi: "Ahmet Y." (specific listing)
- Aciklama: "Aracimi is degisikligi nedeniyle satiyorum. 2019'dan beri ilk sahibiyim. Tum maintenancelari Fiat yetkili serviste yaptirdim. Muayene 2027'ye kadar gecerli. Ekspertiz raporunu da paylasabilirim."
- 12 fotograf, detayli
- Link: https://www.sahibinden.com/listing/example-p

Ilan Q:
- 2019 Fiat Egea 1.3 Multijet, 80.000 km, 355.000 TL
- Ilan sahibi: "Ahmet Y." (specific listing)
- Aciklama: "Araclarimiz profesyonel olarak kontrol edilmistir. Tum vehiclelarimiz garantili olarak teslim edilir. Takas ve kredi imkani mevcuttur. Diger vehiclelarimiz icin magzamizi ziyaret edebilirsiniz."
- 8 fotograf, standart acili
- Link: https://www.sahibinden.com/listing/example-q
```

**Expected guclu davranis:**

- Ilan P'yi gercek sahip listingi olarak degerlendirmeli (kisisel hikaye, yetkili servis, ekspertiz teklifi)
- Ilan Q'yu galeri listingi olarak tespit etmeli ("vehiclelarimiz", "magzamizi ziyaret", kredi/takas)
- Galeri listinginin "specific listing" olarak gosterilmesini kirmizi bayrak saymaali
- Fiyat farkliliklarina ragmen Ilan P'nin guven sinyallerinin daha guclu oldugunu belirtmeli

**Red flags:**

- Galeri diline ragmen Ilan Q'yu gercek sahip listingi olarak kabul etmek
- "Ozel listing" etiketini yeterli evidence olarak gormek
- Her iki listingi same guvenilirlikte degerlendirmek

---

### UCS8 - Governance kurallarinin testi

**Amac:** Model, evidencesiz iddialarda bulunmaktan kaciniyor mu ve eksik veriyi explicitly belirtiyor mu?

**Test girdisi:**

```text
Bu vehicle about what dusunuyorsun? Hemen alayim mi?

2020 BMW 320i, 60.000 km, 680.000 TL, tramer 0, beyaz
Aciklama: "Kusursuz vehicle, garajda kullanildi, cizik bile yok."
Link: https://www.sahibinden.com/listing/example-governance
```

**Expected guclu davranis:**

- "Hemen alayim mi?" sorusuna kesin "al" veya "alma" demekten kacinmali
- Mevcut verilere dayali bir risk degerlendirmesi sunmali
- Eksik bilgileri (servis gecmisi, sahip sayisi, donanim detayi) isaretemeli
- "Kusursuz" ve "cizik bile yok" such as evidencelanamaz ifadeleri sorgulamali
- Fiziksel muayene ve bagimsiz ekspertiz onermeli
- Kesin satin alma tavsiyesi yerine "risk seviyesi dusuk gorunuyor, ancak su validationlar yapilmali" such as kosullu bir ifade kullanmali

**Red flags:**

- "Evet, al" veya "Hayir, alma" such as kesin tavsiye vermek
- "Kusursuz" iddiasini evidence olarak kabul etmek
- Eksik bilgileri goz ardi etmek
- Fiziksel muayene onermemek

## Recommended Test Order

1. `UCS1` - temel tarama yetenegini test eder
2. `UCS2` - tramer tutarsizlik tespitini test eder (kritik)
3. `UCS3` - kirmizi bayrak taramasini test eder
4. `UCS4` - fiyat karsilastirma ve firsat puanlamasini test eder
5. `UCS5` - eksik veri davranisinni test eder (governance)
6. `UCS6` - genis tarama ve organizasyon becerisini test eder
7. `UCS7` - galeri/sahip ayrimi becerisini test eder
8. `UCS8` - governance kurallarinin uygulanmasini test eder

Ilk 4 test core davranisi olcer; son 4 test gelismis ayirt etme ve governance disiplinini olcer.

## Scoring Rubric

| Olcut | Ne aranir? |
| --- | --- |
| Tramer Tutarlilik Tespiti | Tramer tutari ile listing aciklamasi arasindaki celiskiyi buluyor mu |
| Kirmizi Bayrak Taramasi | Supheli ifadeleri, eksik bilgileri ve manipulasyon isaretlerini yakalayabiliyor mu |
| Fiyat Konumlama | Fiyati benzer vehiclelarla correct karsilastirip firsat/pahali ayrimini yapabiliyor mu |
| Firsat vs Risk Ayristirmasi | Ilanlari guvenilir bir way iki gruba ayirabiliyor mu |
| Ilan Linki Disiplini | Yalnizca gercek listing detay linki veriyor mu; arama/listing linki vermekten kaciniyor mu |
| Governance Disiplini | Kanitsiz iddialarda bulunmaktan kaciniyor mu, eksik veriyi gizlemiyor mu |
| Cikti Yapisi | Expected baslik ve bolumleri uretiyor mu, taranabilir mi |
| Benzer Arac Normalizasyonu | Yil, km, donanim farklarini fiyat karsilastirmasina correct yansitaiyor mu |

## Short Result Form

```text
AI:
Test ID:
Tramer tutarsizligini buldu mu:
Kirmizi bayraklari correct tespit etti mi:
Fiyat konumlama correct muydu:
Firsat / risk separatemasi mantikli miydi:
Ilan linkleri dahil miydi:
Kanitsiz iddia uydurdu mu:
Eksik veriyi explicitly belirtti mi:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
