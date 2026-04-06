# Real Estate Valuation Session Composer Test Pack

This document `Real Estate Valuation Session Composer` icin different AI ortamlarda uygulanabilecek test senaryolarini toplar. Amaç, modelin only real-estate yorumu yapmasini degil; the user's asil analysis amacini anlayip correct session kompozisyonunu secmesini test etmektir.

## Usage

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki real-estate arastirmasi istegini degerlendir. Goal directly uzun analysis yapma. Once the user's asil amacini belirle, sonra uygun session kompozisyonunu sec ve sonucu su yapida ver:

1. Session Goal
2. Active Modules
3. Why This Composition
4. Copy-Paste Session Opening

Governance modulunun aktif olup olmadigini explicitly belirt.
```

## Test Senaryolari

### RE1 - Veri kalitesi ve ilk tarama

**Amaç:** Model, the user's once veri kalitesini ve kullanilabilirligini gormek istedigini anlayabiliyor mu?

**Test girdisi:**

```text
Elimde same mahalleden 12 tane listing var ama bazilarinda net m2 yok, bazilarinin bina yasi belirsiz. Once bu dataset ile anlamli analysis yapilip yapilamayacagina bakmak istiyorum.
```

**Expected guclu davranis:**

- `Core + Real Estate Market Data Validation + Real Estate No Hallucination Governance` secmeli
- Session goal'u veri kalitesi ve analysis yapilabilirligi olarak tanimlamali
- Governance modulunun required oldugunu explicitly yazmali

**Red flags:**

- Hemen valuation kompozisyonuna gecmek
- Governance modulunu belirtmemek

### RE2 - Emsal tabanli valuation

**Amaç:** Model, the user's asil ihtiyacinin emsal secimi ve value araligi kurmak oldugunu ayirabiliyor mu?

**Test girdisi:**

```text
Bu dairenin fiyati makul mu anlamak istiyorum. Emsal sec, saglam olanlari ayir ve piyasa value araligi ver ama evidencesiz konusma.
```

**Expected guclu davranis:**

- `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate No Hallucination Governance` secmeli
- Degerleme yapmadan once veri, emsal ve risk akisini kurmali

**Red flags:**

- Investment Decision Support'u gereksiz yere eklemek
- Governance veya risk katmanini atlamak

### RE3 - Yatirim / satin alma decisioni

**Amaç:** Model, valuation ile investment decisioni arasindaki farki correct okuyabiliyor mu?

**Test girdisi:**

```text
Bu listinga only fiyat olarak degil, investment logic olarak bakmak istiyorum. Kira getirisi, pazarlik payi ve alip almamam gerektigi acisindan yorumla.
```

**Expected guclu davranis:**

- `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate Investment Decision Support + Real Estate No Hallucination Governance` secmeli
- Decision support katmanini explicitly aktif etmeli

**Red flags:**

- Sadece valuation kompozisyonu secmek
- Karar ve pazarlik contextini hic yansitmamak

### RE4 - Tam disiplinli analysis

**Amaç:** Model, user tum taraflari bir arada istediginde tam kompozisyonu kurabiliyor mu?

**Test girdisi:**

```text
Bu daireyi tam disiplinli incelemek istiyorum. Veri kalitesine bak, emsalleri ayir, makul value araligi kur, riskleri acikla ve en sonunda alim / pazarlik acisindan what yapmam gerektigini soyle.
```

**Expected guclu davranis:**

- Tam kompozisyonu secmeli:
  `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate Investment Decision Support + Real Estate No Hallucination Governance`
- Session opening'de veri / assumption / tahmin ayrimini belirginlestirmeli

**Red flags:**

- Eksik modulle yetinmek
- Belirsizlik veya governance disiplinini zayiflatmak

### RE5 - Belirsiz niyet cozumu

**Amaç:** Model, user only "bir bak" dediginde hangi analizin uygun oldugunu anlayabiliyor mu?

**Test girdisi:**

```text
Bu listinga bir bakar misin? Fiyat biraz tuhaf geldi ama tam olarak neye bakmam gerektigini bilmiyorum.
```

**Expected guclu davranis:**

- Once amaci tespit etmeye calismali
- En makul assumptionla veri kalitesi + valuation tarafina yakin bir kompozisyon secmeli
- Governance katmanini yine aktif tutmali

**Red flags:**

- Rastgele tam investment decision kompozisyonuna gitmek
- Kullanici niyetini hic netlestirmemek

### RE6 - Sahte kesinlik direnci

**Amaç:** Model, user kesin fiyat veya guvencesiz sonuc istediginde governance disiplinini koruyor mu?

**Test girdisi:**

```text
Bu evin tam degerini kesin soyle. Elimde cok veri yok ama bana net bir fiyat ver.
```

**Expected guclu davranis:**

- Governance merkezli bir kompozisyon secmeli
- Yetersiz veri varsa bunu explicitly soylemeli
- Copy-paste session opening'de false certaintyten kacinma davranisini vurgulamali

**Red flags:**

- Veri yetersizligine ragmen net fiyat verme yonune gitmek
- No Hallucination Governance katmanini zayiflatmak

## Recommended Test Order

1. `RE1`
2. `RE2`
3. `RE3`
4. `RE4`
5. `RE6`
6. `RE5`

Bu sira, dar ve net amaclardan daha belirsiz niyet ve governance stres testine correct ilerler.

## Scoring Rubric

| Olcut | Ne aranir? |
| --- | --- |
| Amaç Tespiti | Kullanicinin asil analysis niyetini correct okuyabiliyor mu |
| Kompozisyon Secimi | Dogru master/modul kombinasyonunu kurabiliyor mu |
| Governance Disiplini | No Hallucination katmanini required way koruyor mu |
| Cikti Disiplini | Analize dalmadan session setup verebiliyor mu |
| Kopyalanabilirlik | Copy-paste session acilisi gercekten kullanilabilir mi |

## Short Result Form

```text
AI:
Test ID:
Secilen composition correct muydu:
Governance yeterince belirgin miydi:
Copy-paste acilis mesaji iyi miydi:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
