# Real Estate Valuation Session Composer Test Pack

Bu belge, `Real Estate Valuation Session Composer` icin farkli AI ortamlarda uygulanabilecek test senaryolarini toplar. Amaç, modelin yalnizca emlak yorumu yapmasini degil; kullanicinin asil analiz amacini anlayip dogru oturum kompozisyonunu secmesini test etmektir.

## Kullanim Sekli

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki emlak arastirmasi istegini degerlendir. Ama dogrudan uzun analiz yapma. Once kullanicinin asil amacini belirle, sonra uygun oturum kompozisyonunu sec ve sonucu su yapida ver:

1. Session Goal
2. Active Modules
3. Why This Composition
4. Copy-Paste Session Opening

Governance modulunun aktif olup olmadigini acikca belirt.
```

## Test Senaryolari

### RE1 - Veri kalitesi ve ilk tarama

**Amaç:** Model, kullanicinin once veri kalitesini ve kullanilabilirligini gormek istedigini anlayabiliyor mu?

**Test girdisi:**

```text
Elimde ayni mahalleden 12 tane ilan var ama bazilarinda net m2 yok, bazilarinin bina yasi belirsiz. Once bu dataset ile anlamli analiz yapilip yapilamayacagina bakmak istiyorum.
```

**Beklenen guclu davranis:**

- `Core + Real Estate Market Data Validation + Real Estate No Hallucination Governance` secmeli
- Session goal'u veri kalitesi ve analiz yapilabilirligi olarak tanimlamali
- Governance modulunun zorunlu oldugunu acikca yazmali

**Kirmizi bayraklar:**

- Hemen degerleme kompozisyonuna gecmek
- Governance modulunu belirtmemek

### RE2 - Emsal tabanli degerleme

**Amaç:** Model, kullanicinin asil ihtiyacinin emsal secimi ve deger araligi kurmak oldugunu ayirabiliyor mu?

**Test girdisi:**

```text
Bu dairenin fiyati makul mu anlamak istiyorum. Emsal sec, saglam olanlari ayir ve piyasa deger araligi ver ama kanitsiz konusma.
```

**Beklenen guclu davranis:**

- `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate No Hallucination Governance` secmeli
- Degerleme yapmadan once veri, emsal ve risk akisini kurmali

**Kirmizi bayraklar:**

- Investment Decision Support'u gereksiz yere eklemek
- Governance veya risk katmanini atlamak

### RE3 - Yatirim / satin alma karari

**Amaç:** Model, degerleme ile yatirim karari arasindaki farki dogru okuyabiliyor mu?

**Test girdisi:**

```text
Bu ilana sadece fiyat olarak degil, yatirim mantigi olarak bakmak istiyorum. Kira getirisi, pazarlik payi ve alip almamam gerektigi acisindan yorumla.
```

**Beklenen guclu davranis:**

- `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate Investment Decision Support + Real Estate No Hallucination Governance` secmeli
- Decision support katmanini acikca aktif etmeli

**Kirmizi bayraklar:**

- Sadece degerleme kompozisyonu secmek
- Karar ve pazarlik baglamini hic yansitmamak

### RE4 - Tam disiplinli analiz

**Amaç:** Model, kullanici tum taraflari bir arada istediginde tam kompozisyonu kurabiliyor mu?

**Test girdisi:**

```text
Bu daireyi tam disiplinli incelemek istiyorum. Veri kalitesine bak, emsalleri ayir, makul deger araligi kur, riskleri acikla ve en sonunda alim / pazarlik acisindan ne yapmam gerektigini soyle.
```

**Beklenen guclu davranis:**

- Tam kompozisyonu secmeli:
  `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate Investment Decision Support + Real Estate No Hallucination Governance`
- Session opening'de veri / varsayim / tahmin ayrimini belirginlestirmeli

**Kirmizi bayraklar:**

- Eksik modulle yetinmek
- Belirsizlik veya governance disiplinini zayiflatmak

### RE5 - Belirsiz niyet cozumu

**Amaç:** Model, kullanici sadece "bir bak" dediginde hangi analizin uygun oldugunu anlayabiliyor mu?

**Test girdisi:**

```text
Bu ilana bir bakar misin? Fiyat biraz tuhaf geldi ama tam olarak neye bakmam gerektigini bilmiyorum.
```

**Beklenen guclu davranis:**

- Once amaci tespit etmeye calismali
- En makul varsayimla veri kalitesi + degerleme tarafina yakin bir kompozisyon secmeli
- Governance katmanini yine aktif tutmali

**Kirmizi bayraklar:**

- Rastgele tam yatirim karar kompozisyonuna gitmek
- Kullanici niyetini hic netlestirmemek

### RE6 - Sahte kesinlik direnci

**Amaç:** Model, kullanici kesin fiyat veya guvencesiz sonuc istediginde governance disiplinini koruyor mu?

**Test girdisi:**

```text
Bu evin tam degerini kesin soyle. Elimde cok veri yok ama bana net bir fiyat ver.
```

**Beklenen guclu davranis:**

- Governance merkezli bir kompozisyon secmeli
- Yetersiz veri varsa bunu acikca soylemeli
- Copy-paste session opening'de sahte kesinlikten kacinma davranisini vurgulamali

**Kirmizi bayraklar:**

- Veri yetersizligine ragmen net fiyat verme yonune gitmek
- No Hallucination Governance katmanini zayiflatmak

## Onerilen Test Sirasi

1. `RE1`
2. `RE2`
3. `RE3`
4. `RE4`
5. `RE6`
6. `RE5`

Bu sira, dar ve net amaclardan daha belirsiz niyet ve governance stres testine dogru ilerler.

## Puanlama Rubrigi

| Olcut | Ne aranir? |
| --- | --- |
| Amaç Tespiti | Kullanicinin asil analiz niyetini dogru okuyabiliyor mu |
| Kompozisyon Secimi | Dogru master/modul kombinasyonunu kurabiliyor mu |
| Governance Disiplini | No Hallucination katmanini zorunlu sekilde koruyor mu |
| Cikti Disiplini | Analize dalmadan session setup verebiliyor mu |
| Kopyalanabilirlik | Copy-paste oturum acilisi gercekten kullanilabilir mi |

## Kisa Sonuc Formu

```text
AI:
Test ID:
Secilen composition dogru muydu:
Governance yeterince belirgin miydi:
Copy-paste acilis mesaji iyi miydi:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
