# Used Car Listing Risk Filter Test Pack

Bu belge, `Used Car Listing Risk Filter` blueprint'i icin dar kapsamli test senaryolarini toplar. Amac, modelin yalnizca kullanicinin verdigi ilanlari inceleyip risk, tutarlilik ve sonraki adim onerileri uretmesini test etmektir.

## Kullanim Sekli

Her testten once asagidaki acilis talimatini kullan.

```text
MergenHan prompt kutuphanesindeki used-car-listing-risk-filter blueprint'inin cekirdek davranisini kullan.

Sadece bana verdigim ilanlar uzerinden calis. Yeni ilan arama, pazar taramasi veya firsat avciligi yapma.

Her ilan icin:
- risk seviyesini belirle
- tramer ve aciklama tutarliligini incele
- kirmizi bayraklari listele
- eksik kritik verileri yaz
- sonraki dogrulama adimlarini oner

Ciktini su yapida ver:
- Input Summary
- Listing-by-Listing Review
- Risk Level per Listing
- Tramer Consistency Notes
- Red Flags
- Missing Critical Data
- Recommended Verification Steps
- Shortlist / Hold / Eliminate

Onemli kurallar:
- Kanit ile varsayimi ayir.
- Kullanici vermediyse URL uydurma.
- Kesin satin al tavsiyesi verme.
- Pazar taramasi veya yeni ilan arama yapma.
```

## Test Senaryolari

### UCRF1 - Tek ilan, bariz tramer celiskisi

**Amac:** Model, tek ilandaki temel celiskiyi yakalayabiliyor mu?

**Test girdisi:**

```text
Su ilani incele:

- 2018 Honda Civic Eco Elegance
- 128.000 km
- 965.000 TL
- Tramer: 0 TL
- Aciklama: "Sag iki kapi lokal boyali, on tampon degisen ama kesinlikle onemsiz, tramersiz aile araci."
- Link: https://www.sahibinden.com/ilan/ornek-civic
```

**Beklenen guclu davranis:**

- Tramer ile aciklama arasindaki celiskiyi acikca isaretlemeli
- Riski en az orta-yuksek seviyede gormeli
- Bagimsiz tramer sorgusu ve ekspertiz onermeli

**Kirmizi bayraklar:**

- "tramersiz" iddiasini sorgusuz kabul etmek
- Boyali / degisen parca beyanini hafife almak

---

### UCRF2 - Iyi gorunen ama eksik verili ilan

**Amac:** Model, iyi tonlu ilanda bile veri eksigini not edebiliyor mu?

**Test girdisi:**

```text
Bu ilani degerlendir:

- 2020 Toyota Corolla Flame X-Pack
- 52.000 km
- 1.245.000 TL
- Aciklama: "Tum bakimlari yetkili serviste. Arac son derece temiz. Alana hayirli olsun."
- Tramer bilgisi yok
- Eksper raporu bilgisi yok
- Sadece 4 fotograf var
```

**Beklenen guclu davranis:**

- Ilani otomatik guvenilir saymamali
- Eksik tramer ve eksper bilgisini kritik veri eksigi olarak yazmali
- Fotograf azligini not etmeli

**Kirmizi bayraklar:**

- "bakimlari yetkili serviste" ifadesinden fazla kesinlik uretmek
- Veri eksigini dusuk risk gibi gostermek

---

### UCRF3 - Iki ilan arasinda hangisi shortlist'e kalir

**Amac:** Model, ikili karsilastirmada dar karar destegi verebiliyor mu?

**Test girdisi:**

```text
Su iki ilani risk acisindan karsilastir:

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

**Beklenen guclu davranis:**

- Ilan A'yi aciklanmis ama dogrulanmasi gereken riskli/temkinli ilan olarak gormeli
- Ilan B'de veri boslugu ve asiri iddiayi not etmeli
- Birini "shortlist", digerini "hold" veya "eliminate" benzeri sinifa koymali

**Kirmizi bayraklar:**

- Trameri belirtilmeyen ilani daha temiz varsaymak
- Iki ilani da ayni risk seviyesinde ele almak

---

### UCRF4 - Zayif veri durumunda fren yapabiliyor mu

**Amac:** Model, yetersiz veriyle yorumunu sinirli tutabiliyor mu?

**Test girdisi:**

```text
Bu ilan hakkinda ne dusunursun?

- 2017 BMW 3.20i
- 780.000 TL
- Aciklama: "Temiz arac, detaylar telefonda."
- Km bilgisi yok
- Tramer bilgisi yok
- Fotograf yok
```

**Beklenen guclu davranis:**

- Veri yetersizligini merkezde tutmali
- Kesin yargidan kacmali
- Listeyi "hold" veya "eliminate" tarafina itebilmeli

**Kirmizi bayraklar:**

- Fiyat veya kalite konusunda tahmini hikaye uretmek
- Veri eksigine ragmen olumlu shortlist tavsiyesi vermek

## Puanlama Rubrigi

| Olcut | Ne arayacaksin |
| --- | --- |
| Kapsam Disiplini | Sadece verilen ilanlarla mi calisiyor |
| Risk Muhakemesi | Risk seviyesi mantikli mi |
| Tramer Tutarliligi | Celiskileri yakaliyor mu |
| Veri Eksigi Duyarliligi | Eksik bilgiyle fren yapiyor mu |
| Halusinasyondan Kacinma | Uydurma veri, URL veya kesinlik uretiyor mu |

