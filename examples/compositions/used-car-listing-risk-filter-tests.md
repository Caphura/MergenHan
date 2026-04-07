# Used Car Listing Risk Filter Test Pack

This document `Used Car Listing Risk Filter` blueprint'i icin dar kapsamli test senaryolarini toplar. Amac, modelin only the user's verdigi listinglari inceleyip risk, tutarlilik ve sonraki step onerileri uretmesini test etmektir.

## Usage

Her testten once asagidaki acilis talimatini kullan.

```text
MergenHan prompt librarysindeki used-car-listing-risk-filter blueprint'inin core davranisini kullan.

Sadece bana verdigim listinglar uzerinden calis. Yeni listing arama, pazar taramasi veya firsat avciligi yapma.

Her listing icin:
- risk seviyesini belirle
- confidence seviyesini belirt
- tramer ve description tutarliligini incele
- kirmizi bayraklari listele
- eksik kritik verileri yaz
- sonraki validation adimlarini oner

Ciktini su yapida ver:
- Input Summary
- Listing-by-Listing Review
- Risk Level per Listing
- Tramer Consistency Notes
- Red Flags
- Missing Critical Data
- Recommended Verification Steps
- Shortlist / Hold / Eliminate

Onemli rules:
- Kanit ile assumptioni ayir.
- Facts, Inferences ve Unknowns ayrimini gorunur tut.
- Kullanici vermediyse URL fabricated.
- Kesin satin al tavsiyesi verme.
- Pazar taramasi veya yeni listing arama yapma.
```

## Test Senaryolari

### UCRF1 - Tek listing, bariz tramer celiskisi

**Amac:** Model, tek listingdaki temel celiskiyi yakalayabiliyor mu?

**Test girdisi:**

```text
Su listingi incele:

- 2018 Honda Civic Eco Elegance
- 128.000 km
- 965.000 TL
- Tramer: 0 TL
- Aciklama: "Sag iki kapi lokal boyali, on tampon degisen ama kesinlikle onemsiz, tramersiz aile vehiclei."
- Link: https://www.sahibinden.com/listing/example-civic
```

**Expected guclu davranis:**

- Tramer ile description arasindaki celiskiyi explicitly isaretlemeli
- Riski en az orta-yuksek seviyede gormeli
- Bagimsiz tramer sorgusu ve ekspertiz onermeli

**Red flags:**

- "tramersiz" iddiasini sorgusuz kabul etmek
- Boyali / degisen parca beyanini hafife almak

---

### UCRF2 - Iyi gorunen ama eksik verili listing

**Amac:** Model, iyi tonlu listingda bile veri eksigini not edebiliyor mu?

**Test girdisi:**

```text
Bu listingi degerlendir:

- 2020 Toyota Corolla Flame X-Pack
- 52.000 km
- 1.245.000 TL
- Aciklama: "Tum maintenancelari yetkili serviste. Arac son derece temiz. Alana hayirli olsun."
- Tramer bilgisi yok
- Eksper raporu bilgisi yok
- Sadece 4 fotograf var
```

**Expected guclu davranis:**

- Ilani otomatik guvenilir saymamali
- Eksik tramer ve eksper bilgisini kritik veri eksigi olarak yazmali
- Fotograf azligini not etmeli

**Red flags:**

- "maintenancelari yetkili serviste" ifadesinden fazla kesinlik uretmek
- Veri eksigini dusuk risk such as gostermek

---

### UCRF3 - Iki listing arasinda hangisi shortlist'e remains

**Amac:** Model, ikili karsilastirmada dar decision support verebiliyor mu?

**Test girdisi:**

```text
Su iki listingi risk acisindan karsilastir:

Ilan A
- 2019 Renault Megane 1.5 dCi Icon
- 96.000 km
- 875.000 TL
- Tramer: 18.500 TL
- Aciklama: "Sol arka kapida boya var, park halinde surtmeden kaynakli."

Ilan B
- 2019 Renault Megane 1.5 dCi Icon
- 101.000 km
- 845.000 TL
- Tramer: belirtilmemis
- Aciklama: "Hatasiz boyasiz degisensiz, detay isteyen arasın."
```

**Expected guclu davranis:**

- Ilan A'yi aciklanmis ama dogrulanmasi gereken riskli/temkinli listing olarak gormeli
- Ilan B'de veri boslugu ve asiri iddiayi not etmeli
- Birini "shortlist", digerini "hold" veya "eliminate" benzeri sinifa koymali

**Red flags:**

- Trameri belirtilmeyen listingi daha temiz varsaymak
- Iki listingi da same risk seviyesinde ele almak

---

### UCRF4 - Zayif veri durumunda fren yapabiliyor mu

**Amac:** Model, yetersiz veriyle yorumunu sinirli tutabiliyor mu?

**Test girdisi:**

```text
Bu listing about what dusunursun?

- 2017 BMW 3.20i
- 780.000 TL
- Aciklama: "Temiz vehicle, detaylar telefonda."
- Km bilgisi yok
- Tramer bilgisi yok
- Fotograf yok
```

**Expected guclu davranis:**

- Veri yetersizligini merkezde tutmali
- Kesin yargidan kacmali
- Listeyi "hold" veya "eliminate" tarafina itebilmeli

**Red flags:**

- Fiyat veya kalite konusunda tahmini hikaye uretmek
- Veri eksigine ragmen olumlu shortlist tavsiyesi vermek

---

### UCRF5 - URL yoksa URL uydurmadan ilerliyor mu

**Amac:** Model, ekran goruntusu transkripti veya ozet detaylardan calisirken link uydurmadan karar destegi verebiliyor mu?

**Test girdisi:**

```text
Link yok. Ekran goruntusunden not aldigim bilgilerle degerlendir:

- 2021 Fiat Egea Cross 1.4 Urban
- 34.000 km
- 865.000 TL
- Tramer: belirtilmemis
- Aciklama: "Hatasiz boyasiz. Ciddi alici arasın. Galeriden degil."
- Fotograf bilgisi: sadece on taraf ve ic mekan gorunuyor, eksper gorseli yok
```

**Expected guclu davranis:**

- URL olmadigini acikca korumali ve link uydurmamali
- "hatasiz boyasiz" iddiasini dogrulanmamis claim olarak ele almali
- Eksper gorseli ve tramer eksigini kritik verification ihtiyaci olarak yazmali
- Saticiya sorulacak net follow-up sorular vermeli

**Red flags:**

- Kendiliginden listing linki eklemek
- "galeriden degil" ifadesini kanitlanmis kabul etmek
- Confidence seviyesini yuksek vermek

---

### UCRF6 - Coklu listingte harici piyasa taramasina kayiyor mu

**Amac:** Model, birden fazla listingi sadece verilen veriler arasinda goreli olarak karsilastirabiliyor mu?

**Test girdisi:**

```text
Su uc ilani sadece verdigim bilgilere gore karsilastir:

Ilan 1
- 2020 Opel Astra 1.4 AT Enjoy
- 78.000 km
- 1.020.000 TL
- Tramer: 6.800 TL
- Aciklama: "Sag arka kapida lokal boya var."

Ilan 2
- 2020 Opel Astra 1.4 AT Enjoy
- 81.000 km
- 995.000 TL
- Tramer: belirtilmemis
- Aciklama: "Hatasiz boyasiz, eksper isteyen getirsin."

Ilan 3
- 2020 Opel Astra 1.4 AT Enjoy
- 76.000 km
- 970.000 TL
- Tramer: 0 TL
- Aciklama: "Sol on camurluk boyali, tramersiz."
```

**Expected guclu davranis:**

- Karsilastirmayi yalnizca bu uc ilan arasinda yapmali
- Ilan 1'i aciklanmis ama dogrulanmasi gereken temkinli aday olarak gormeli
- Ilan 2'de veri boslugunu ve iddia-agir dili not etmeli
- Ilan 3'te tramer-aciklama celiskisini yakalamali

**Red flags:**

- Harici piyasa fiyati biliyormus gibi kesin konumlama yapmak
- Verilen uc ilan disinda yeni arac veya ilan onermek
- Uc ilanin ucu icin de benzer confidence vermek

---

### UCRF7 - Search URL ile detail URL'yi karistiriyor mu

**Amac:** Model, kullanici search veya category sayfasi linki verdiginde bunu listing detail URL'si gibi kullanmadan ilerleyebiliyor mu?

**Test girdisi:**

```text
Bu ilani yorumla. Elimde sadece su link ve notlar var:

- URL: https://www.sahibinden.com/otomobil?queryText=2020+mazda+3
- 2020 Mazda 3
- 61.000 km
- 1.390.000 TL
- Tramer: 12.400 TL
- Aciklama: "Sol arka kapi boyali. Sahibinden temiz arac."
```

**Expected guclu davranis:**

- URL'nin listing detail URL'si olmadigini fark etmeli
- Linki listing URL'si gibi tekrar etmemeli
- Analizi verilen notlar uzerinden surdurmeli
- Kullaniciya dogrulanmis detail link, ilan numarasi veya ekran goruntusu istemeyi onermeli

**Red flags:**

- Search sayfasi linkini dogrudan ilan linki gibi sunmak
- URL var diye confidence'i gereksiz yuksek vermek
- Link yapisini kontrol etmeden "dogrulanmis ilan" demek

---

### UCRF8 - Facts, Inferences, Unknowns ayrimi bozuluyor mu

**Amac:** Model, ayni ilanda dogrudan verilen veriyle kendi cikarimini karistirmadan raporlayabiliyor mu?

**Test girdisi:**

```text
Su ilani facts, inferences ve unknowns ayirarak degerlendir:

- 2016 Skoda Octavia 1.6 TDI DSG
- 182.000 km
- 835.000 TL
- Aciklama: "Arac aile araci olarak kullanildi. Iki parca lokal boya var. Tramer kaydi onemsizdir."
- Tramer: tutar yazmiyor
- Satici notu: "Ben ikinci sahibiyim" bilgisi telefonda soylenmis, ilanda yazmiyor
- Fotograf bilgisi: sag yan, sol yan, on konsol var; motor ve eksper gorseli yok
```

**Expected guclu davranis:**

- Listing icindeki dogrudan verileri `Facts` tarafina koymali
- "aile araci", "onemsiz hasar" ve benzeri yumusatma dilinden yaptigi cikarimlari `Inferences` tarafina koymali
- Tramer tutari, servis gecmisi ve sahiplik bilgisinin dogrulanmamis kisimlarini `Unknowns` tarafinda tutmali
- Telefonda soylenen ama listing icinde olmayan bilgiyi sinirli guvenle ele almali

**Red flags:**

- Telefon notunu listing fact'i gibi yazmak
- Tramer tutari verilmedigi halde tahmini tutar uretmek
- Facts ve inferences'i ayni satirda eritmek

---

### UCRF9 - Galeri dili ve sahiplik iddiasi celisince nasil davranıyor

**Amac:** Model, satıcı tipi belirsiz oldugunda risk ve confidence'i dogru ayarlayabiliyor mu?

**Test girdisi:**

```text
Bu ilan riskli mi?

- 2019 Peugeot 3008 1.5 BlueHDi Allure
- 89.000 km
- 1.575.000 TL
- Tramer: 0 TL
- Aciklama: "Aracimiz tamamen bakimli ve masrafsizdir. Magazamiza bekleriz. Sahibinden temiz aile araci."
- Fotograf bilgisi: showroom ortami, ayni fonla cekilmis 12 foto
```

**Expected guclu davranis:**

- "aracimiz" ve "magazamiza bekleriz" dilini galeri sinyali olarak isaretlemeli
- "sahibinden" iddiasini dogrulanmamis claim olarak tutmali
- 0 TL trameri tek basina guven sinyali yapmamali
- Satici tipi belirsizligi yuzunden confidence'i kontrollu tutmali

**Red flags:**

- Ilani net bicimde sahibinden ilan diye siniflandirmak
- Galeri dilini gormezden gelmek
- Foto seti profesyonel diye otomatik guven vermek

## Scoring Rubric

| Olcut | Ne arayacaksin |
| --- | --- |
| Scope Disiplini | Sadece verilen listinglarla mi calisiyor |
| Risk Muhakemesi | Risk seviyesi mantikli mi |
| Confidence Disiplini | Kanit azaldikca confidence'i dusuruyor mu |
| Tramer Tutarliligi | Celiskileri yakaliyor mu |
| Facts / Inferences / Unknowns Ayrimi | Dogrudan veriyle cikarimi ayri tutuyor mu |
| Veri Eksigi Duyarliligi | Eksik bilgiyle fren yapiyor mu |
| URL Disiplini | Kullanici vermediyse link uydurmuyor mu |
| Halusinasyondan Kacinma | Uydurma veri, URL veya kesinlik uretiyor mu |
