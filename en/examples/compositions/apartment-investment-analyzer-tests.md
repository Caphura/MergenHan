# Apartment Investment Analyzer Test Pack

This document `Apartment Investment Analyzer` icin different AI ortamlarda uygulanabilecek test senaryolarini toplar. Amac, modelin only real-estate yorumu yapmasini degil; apartman satis listinglarini investment bakisiyla decision destekleyici, evidence-temelli ve uncertainty bilinci tasiyan bir formata donusturmesini test etmektir.

## Usage

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki apartman satis listingi veya listinglarini investment odakli analysis et. Gereksiz uzun input yapma. Ciktini su yapida ver:

1. Scope Summary
2. Market Snapshot
3. Listing-by-Listing Analysis
4. Rental Potential
5. Payback / Yield Estimate
6. Risks and Unknowns
7. Top Candidates
8. Recommended Next Checks

Tum output boyunca evidence ile assumptioni ayir. Belirsizligi explicitly etiketle. Sahte kesinlik veya garanti investment dili kullanma.
```

## Test Senaryolari

### AIA1 - Tek listing fizibilitesi

**Amaç:** Model, tek bir listing icin hizli ama decision destekleyici bir investment analysis kurabiliyor mu?

**Test girdisi:**

```text
Kadikoy'de 2+1, 85 m2, 12 yasinda bir daire. Fiyat 6.450.000 TL. Ilanda metroya yakin, kiracili ve maintenanceli oldugu yaziyor. Bu listing investment icin mantikli mi?
```

**Expected guclu davranis:**

- Tek listing kapsaminda kaldigini netlestirmeli
- Kira potansiyeli, brut getiri logic ve fiyatlama riski tarafina girmeli
- Kanitlanamayan kisimlari assumption veya bilinmeyen olarak etiketlemeli

**Red flags:**

- Tek listingi kesin al / alma tavsiyesine indirgemek
- Eksik veri olmasina ragmen asiri net getiri hesabi vermek

### AIA2 - Coklu listing karsilastirma

**Amaç:** Model, birden fazla apartman listingi arasinda karsilastirmali investment logic kurabiliyor mu?

**Test girdisi:**

```text
Bu uc listingi investment acisindan karsilastir:

1. Umraniye, 3+1, 120 m2, 5.900.000 TL, 8 yasinda, site icinde
2. Kartal, 2+1, 95 m2, 4.850.000 TL, 2 yasinda, deniz goruslu
3. Maltepe, 2+1, 100 m2, 5.100.000 TL, 14 yasinda, metroya yakin

Hangisi daha mantikli gorunuyor?
```

**Expected guclu davranis:**

- Ilan bazli karsilastirmayi net ayirmali
- Her listingin guclu ve zayif investment taraflarini gostermeli
- En sonunda guclu aday veya adaylari gerekceli way separatemali

**Red flags:**

- Ilanlari birbirine karistirmak
- Tek kriter olarak only fiyat dusuklugune yaslanmak

### AIA3 - Kira getirisi ve geri donus odagi

**Amaç:** Model, the user's asil sorusunun kira getirisi ve geri donus logic oldugunu ayirabiliyor mu?

**Test girdisi:**

```text
Bu daireyi ozellikle kira getirisi icin degerlendirmeni istiyorum. Fiyat 4.200.000 TL. Ilana gore aylik muhtemel kira 23.000-26.000 TL araliginda. Yatirim acisindan geri donus mantikli mi?
```

**Expected guclu davranis:**

- Rental Potential ve Payback / Yield Estimate bolumlerini merkezde tutmali
- Ilan metnindeki kira araligini directly kesin kabul etmemeli
- Brut getiri mantigini kabaca kurup belirsizligi gostermeli

**Red flags:**

- Kira bilgisini sorgusuz kabul etmek
- Getiri hesabini kesin ve risksiz such as sunmak

### AIA4 - Short liste cikarma

**Amaç:** Model, bir listing grubundan decision dostu shortlist uretebiliyor mu?

**Test girdisi:**

```text
Elimde same bolgeden 7 apartman listingi var. Hepsini tek tek uzun anlatma; investment acisindan hangileri on plana cikiyor, hangileri elenmeli, bana short bir shortlist logic kur.
```

**Expected guclu davranis:**

- Scopei shortlist cikarma olarak okumali
- Tum listinglari esit ayrinti seviyesinde bogmadan gruplamali
- Top Candidates bolumunu gercekten ayirici hale getirmeli

**Red flags:**

- Her listingi gereksiz uzunlukta tekrar etmek
- Shortlist vermeden genel piyasa yorumu yapmak

### AIA5 - Zayif veri ve governance stresi

**Amaç:** Model, veri zayif oldugunda yine de yapisal ama dikkatli analysis uretebiliyor mu?

**Test girdisi:**

```text
Ilan biraz zayif: "Merkezi konumda, investmenta uygun, kacirilmayacak firsat." Fiyat 5.750.000 TL. m2, bina yasi ve kira potansiyeli net degil. Buna ragmen investment acisindan hizli yorum yap.
```

**Expected guclu davranis:**

- Veri zayifligini ilk anda explicitly not etmeli
- Risks and Unknowns bolumunu guclu kurmali
- Analizi tamamen reddetmeden ama uncertainty etiketleriyle ilerlemeli

**Red flags:**

- Eksik veriye ragmen kesin valuation yapmak
- Ilan sloganlarini evidence such as kullanmak

### AIA6 - Asiri fiyatlama ve pazarlik hassasiyeti

**Amaç:** Model, user investment decisionini pazarlik ve overpricing acisindan okumak istediginde bunu outputya yansitabiliyor mu?

**Test girdisi:**

```text
Bu listing bana piyasanin ustunde such as geliyor. Yatirim acisindan bu fiyattan mantikli mi, yoksa ancak ciddi pazarlik olursa mi dusunulur? Ilani bu gozle analysis et.
```

**Expected guclu davranis:**

- Market Snapshot ile Listing-by-Listing Analysis arasinda overpricing riskini surfacemali
- Risk ve decision support tarafini birlikte kurmali
- Recommended Next Checks icinde pazarlik oncelemesi veya ek veri ihtiyacini belirtmeli

**Red flags:**

- Pazarlik acisini hic yansitmamak
- Fiyatin yuksek oldugunu evidencesiz ama kesin dille listing etmek

## Recommended Test Order

1. `AIA1`
2. `AIA3`
3. `AIA2`
4. `AIA5`
5. `AIA6`
6. `AIA4`

Bu sira, tek listing fizibilitesinden coklu listing secimine ve oradan zayif veri / decision stresi durumlarina correct ilerler.

## Scoring Rubric

| Olcut | Ne aranir? |
| --- | --- |
| Scope Tespiti | Tek listing, coklu listing veya shortlist amacini correct okuyabiliyor mu |
| Kanit Disiplini | Kanit ile assumptioni net ayirabiliyor mu |
| Yatirim Mantigi | Kira, getiri, likidite ve fiyatlama riskini decision destekleyici way kurabiliyor mu |
| Risk ve Belirsizlik | Eksik veri ve bilinmeyenleri surfaceabiliyor mu |
| Eyleme Donukluk | Recommended Next Checks ve Top Candidates bolumleri gercekten ise yariyor mu |

## Short Result Form

```text
AI:
Test ID:
Scope tespiti correct muydu:
Kanit ve assumption ayrimi yeterli miydi:
Top Candidates / next checks ise yariyor muydu:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
