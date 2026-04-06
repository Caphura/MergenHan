# Used Car Listing Risk Filter Test Pack

This document `Used Car Listing Risk Filter` blueprint'i icin dar kapsamli test senaryolarini toplar. Amac, modelin only the user's verdigi listinglari inceleyip risk, tutarlilik ve sonraki step onerileri uretmesini test etmektir.

## Usage

Her testten once asagidaki acilis talimatini kullan.

```text
MergenHan prompt librarysindeki used-car-listing-risk-filter blueprint'inin core davranisini kullan.

Sadece bana verdigim listinglar uzerinden calis. Yeni listing arama, pazar taramasi veya firsat avciligi yapma.

Her listing icin:
- risk seviyesini belirle
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

## Scoring Rubric

| Olcut | Ne arayacaksin |
| --- | --- |
| Scope Disiplini | Sadece verilen listinglarla mi calisiyor |
| Risk Muhakemesi | Risk seviyesi mantikli mi |
| Tramer Tutarliligi | Celiskileri yakaliyor mu |
| Veri Eksigi Duyarliligi | Eksik bilgiyle fren yapiyor mu |
| Halusinasyondan Kacinma | Uydurma veri, URL veya kesinlik uretiyor mu |

