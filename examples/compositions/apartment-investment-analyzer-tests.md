# Apartment Investment Analyzer Test Pack

Bu belge, `Apartment Investment Analyzer` icin farkli AI ortamlarda uygulanabilecek test senaryolarini toplar. Amac, modelin yalnizca emlak yorumu yapmasini degil; apartman satis ilanlarini yatirim bakisiyla karar destekleyici, kanit-temelli ve belirsizlik bilinci tasiyan bir formata donusturmesini test etmektir.

## Kullanim Sekli

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki apartman satis ilani veya ilanlarini yatirim odakli analiz et. Gereksiz uzun giris yapma. Ciktini su yapida ver:

1. Scope Summary
2. Market Snapshot
3. Listing-by-Listing Analysis
4. Rental Potential
5. Payback / Yield Estimate
6. Risks and Unknowns
7. Top Candidates
8. Recommended Next Checks

Tum cikti boyunca kanit ile varsayimi ayir. Belirsizligi acikca etiketle. Sahte kesinlik veya garanti yatirim dili kullanma.
```

## Test Senaryolari

### AIA1 - Tek ilan fizibilitesi

**Amaç:** Model, tek bir ilan icin hizli ama karar destekleyici bir yatirim analizi kurabiliyor mu?

**Test girdisi:**

```text
Kadikoy'de 2+1, 85 m2, 12 yasinda bir daire. Fiyat 6.450.000 TL. Ilanda metroya yakin, kiracili ve bakimli oldugu yaziyor. Bu ilan yatirim icin mantikli mi?
```

**Beklenen guclu davranis:**

- Tek ilan kapsaminda kaldigini netlestirmeli
- Kira potansiyeli, brut getiri mantigi ve fiyatlama riski tarafina girmeli
- Kanitlanamayan kisimlari varsayim veya bilinmeyen olarak etiketlemeli

**Kirmizi bayraklar:**

- Tek ilani kesin al / alma tavsiyesine indirgemek
- Eksik veri olmasina ragmen asiri net getiri hesabi vermek

### AIA2 - Coklu ilan karsilastirma

**Amaç:** Model, birden fazla apartman ilani arasinda karsilastirmali yatirim mantigi kurabiliyor mu?

**Test girdisi:**

```text
Bu uc ilani yatirim acisindan karsilastir:

1. Umraniye, 3+1, 120 m2, 5.900.000 TL, 8 yasinda, site icinde
2. Kartal, 2+1, 95 m2, 4.850.000 TL, 2 yasinda, deniz goruslu
3. Maltepe, 2+1, 100 m2, 5.100.000 TL, 14 yasinda, metroya yakin

Hangisi daha mantikli gorunuyor?
```

**Beklenen guclu davranis:**

- Ilan bazli karsilastirmayi net ayirmali
- Her ilanin guclu ve zayif yatirim taraflarini gostermeli
- En sonunda guclu aday veya adaylari gerekceli sekilde ayristirmali

**Kirmizi bayraklar:**

- Ilanlari birbirine karistirmak
- Tek kriter olarak sadece fiyat dusuklugune yaslanmak

### AIA3 - Kira getirisi ve geri donus odagi

**Amaç:** Model, kullanicinin asil sorusunun kira getirisi ve geri donus mantigi oldugunu ayirabiliyor mu?

**Test girdisi:**

```text
Bu daireyi ozellikle kira getirisi icin degerlendirmeni istiyorum. Fiyat 4.200.000 TL. Ilana gore aylik muhtemel kira 23.000-26.000 TL araliginda. Yatirim acisindan geri donus mantikli mi?
```

**Beklenen guclu davranis:**

- Rental Potential ve Payback / Yield Estimate bolumlerini merkezde tutmali
- Ilan metnindeki kira araligini dogrudan kesin kabul etmemeli
- Brut getiri mantigini kabaca kurup belirsizligi gostermeli

**Kirmizi bayraklar:**

- Kira bilgisini sorgusuz kabul etmek
- Getiri hesabini kesin ve risksiz gibi sunmak

### AIA4 - Kisa liste cikarma

**Amaç:** Model, bir ilan grubundan karar dostu shortlist uretebiliyor mu?

**Test girdisi:**

```text
Elimde ayni bolgeden 7 apartman ilani var. Hepsini tek tek uzun anlatma; yatirim acisindan hangileri on plana cikiyor, hangileri elenmeli, bana kisa bir shortlist mantigi kur.
```

**Beklenen guclu davranis:**

- Kapsami shortlist cikarma olarak okumali
- Tum ilanlari esit ayrinti seviyesinde bogmadan gruplamali
- Top Candidates bolumunu gercekten ayirici hale getirmeli

**Kirmizi bayraklar:**

- Her ilani gereksiz uzunlukta tekrar etmek
- Shortlist vermeden genel piyasa yorumu yapmak

### AIA5 - Zayif veri ve governance stresi

**Amaç:** Model, veri zayif oldugunda yine de yapisal ama dikkatli analiz uretebiliyor mu?

**Test girdisi:**

```text
Ilan biraz zayif: "Merkezi konumda, yatirima uygun, kacirilmayacak firsat." Fiyat 5.750.000 TL. m2, bina yasi ve kira potansiyeli net degil. Buna ragmen yatirim acisindan hizli yorum yap.
```

**Beklenen guclu davranis:**

- Veri zayifligini ilk anda acikca not etmeli
- Risks and Unknowns bolumunu guclu kurmali
- Analizi tamamen reddetmeden ama belirsizlik etiketleriyle ilerlemeli

**Kirmizi bayraklar:**

- Eksik veriye ragmen kesin degerleme yapmak
- Ilan sloganlarini kanit gibi kullanmak

### AIA6 - Asiri fiyatlama ve pazarlik hassasiyeti

**Amaç:** Model, kullanici yatirim kararini pazarlik ve overpricing acisindan okumak istediginde bunu ciktiya yansitabiliyor mu?

**Test girdisi:**

```text
Bu ilan bana piyasanin ustunde gibi geliyor. Yatirim acisindan bu fiyattan mantikli mi, yoksa ancak ciddi pazarlik olursa mi dusunulur? Ilani bu gozle analiz et.
```

**Beklenen guclu davranis:**

- Market Snapshot ile Listing-by-Listing Analysis arasinda overpricing riskini gorunur kilmali
- Risk ve karar destegi tarafini birlikte kurmali
- Recommended Next Checks icinde pazarlik oncelemesi veya ek veri ihtiyacini belirtmeli

**Kirmizi bayraklar:**

- Pazarlik acisini hic yansitmamak
- Fiyatin yuksek oldugunu kanitsiz ama kesin dille ilan etmek

## Onerilen Test Sirasi

1. `AIA1`
2. `AIA3`
3. `AIA2`
4. `AIA5`
5. `AIA6`
6. `AIA4`

Bu sira, tek ilan fizibilitesinden coklu ilan secimine ve oradan zayif veri / karar stresi durumlarina dogru ilerler.

## Puanlama Rubrigi

| Olcut | Ne aranir? |
| --- | --- |
| Kapsam Tespiti | Tek ilan, coklu ilan veya shortlist amacini dogru okuyabiliyor mu |
| Kanit Disiplini | Kanit ile varsayimi net ayirabiliyor mu |
| Yatirim Mantigi | Kira, getiri, likidite ve fiyatlama riskini karar destekleyici sekilde kurabiliyor mu |
| Risk ve Belirsizlik | Eksik veri ve bilinmeyenleri gorunur kilabiliyor mu |
| Eyleme Donukluk | Recommended Next Checks ve Top Candidates bolumleri gercekten ise yariyor mu |

## Kisa Sonuc Formu

```text
AI:
Test ID:
Kapsam tespiti dogru muydu:
Kanit ve varsayim ayrimi yeterli miydi:
Top Candidates / next checks ise yariyor muydu:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
