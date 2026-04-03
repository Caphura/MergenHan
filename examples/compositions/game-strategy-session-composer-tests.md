# Game Strategy Session Composer Test Pack

Bu belge, `Game Strategy Session Composer` icin farkli AI ortamlarda uygulanabilecek test senaryolarini toplar. Amaç, modelin yalnizca oyun fikrini yorumlamasini degil; kullanicinin asil amacini anlayip dogru oturum kompozisyonunu secmesini test etmektir.

## Kullanim Sekli

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki oyun fikri istegini degerlendir. Ama dogrudan uzun analiz yapma. Once kullanicinin asil amacini belirle, sonra uygun oturum kompozisyonunu sec ve sonucu su yapida ver:

1. Session Goal
2. Active Modules
3. Why This Composition
4. Copy-Paste Session Opening

Eger gerekiyorsa "sert mod" ust katmanini da ekleyebilirsin.
```

## Test Senaryolari

### GS1 - Steam potansiyeli secimi

**Amaç:** Model, market/Steam odakli talebi dogru okuyup uygun modulleri secebiliyor mu?

**Test girdisi:**

```text
Bu oyun fikrinin Steam'de is yapip yapmayacagini anlamak istiyorum. Fikir: Kucuk bir kasabada gecen, karanlik mizahli bir gece vardiyasi market simulasyonu.
```

**Beklenen guclu davranis:**

- `Core + Steam Market Validation + Full Concept Greenlight` secmeli
- Session goal'u market ve greenlight odakli tanimlamali
- Kopyala-yapistir acilis mesaji vermeli

**Kirmizi bayraklar:**

- Dogrudan tam analiz yapmaya baslamak
- MVP veya production risk modullerine gereksiz kaymak

### GS2 - MVP indirgeme secimi

**Amaç:** Model, asıl ihtiyacin kapsam daraltma oldugunu anlayabiliyor mu?

**Test girdisi:**

```text
Bu fikri cok buyutmeden MVP'ye indirmem lazim. Fikir: co-op extraction roguelite ama ayni zamanda base building ve economy de var.
```

**Beklenen guclu davranis:**

- `Core + MVP Scope Reduction` secmeli
- Kapsam kesintisi ve en kucuk satilabilir versiyon mantigina yonelmeli

**Kirmizi bayraklar:**

- Steam analizi veya full greenlight'a gereksiz kaymak
- Tekrar kullanilabilir oturum acilisi vermemek

### GS3 - Uretim riski secimi

**Amaç:** Model, risk ve execution odagini diger amaclardan ayirabiliyor mu?

**Test girdisi:**

```text
Bu fikrin uretimde nerede patlayacagini gormek istiyorum. Fikir: procedural dedektiflik oyunu, NPC hafizasi var, oyuncu ipuclarini serbest bicimde birlestiriyor.
```

**Beklenen guclu davranis:**

- `Core + Production Risk Strategy` secmeli
- Bottleneck, test zorlugu ve solo-dev risklerine odaklanmali

**Kirmizi bayraklar:**

- Risk yerine oyun fikrini ovmeye kaymak
- Production phase mantigini hic dusunmemek

### GS4 - Tam stratejik degerlendirme

**Amaç:** Model, tam stratejik degerlendirme isteginde butun gerekli modulleri bir araya getirebiliyor mu?

**Test girdisi:**

```text
Bu oyun fikrine acimasiz ama ticari gercekcilikle bak. Steam potansiyeli, scope, risk ve greenlight acisindan tam degerlendirme istiyorum.
```

**Beklenen guclu davranis:**

- `Core + Steam Market Validation + MVP Scope Reduction + Production Risk Strategy + Full Concept Greenlight` secmeli
- Gerekliyse sert mod ust katmanini eklemeli

**Kirmizi bayraklar:**

- Sadece tek modulle yetinmek
- Sert tonu gerektigi halde yumusatmak

### GS5 - Belirsiz niyet cozumu

**Amaç:** Model, kullanicinin ne istedigini tam soylemedigi durumda en uygun oturumu secebiliyor mu?

**Test girdisi:**

```text
Bu fikre bir bakar misin? Fikir: tek tusla oynanan ama cok derin hisseden bir buyucu arena oyunu.
```

**Beklenen guclu davranis:**

- Once kullanicinin amacini tespit etmeye calismali
- Gerekirse en makul varsayimla uygun session composition secmeli

**Kirmizi bayraklar:**

- Rastgele bir kompozisyon secmek
- Kullanicinin amacini hic netlestirmemek

### GS6 - Sert mod kullanimi

**Amaç:** Model, kullanici acikca sert ve gercekci degerlendirme istediginde bunu session katmanina yansitiyor mu?

**Test girdisi:**

```text
Bu oyunu bana kirmadan degil, gercekci sekilde degerlendir. Kucuk ekip icin fazla mi buyuk, Steam'de dikkat ceker mi, durust ol.
```

**Beklenen guclu davranis:**

- Tam stratejik veya market + risk agirlikli kompozisyon secmeli
- Sert mod ust katmanini eklemeli

**Kirmizi bayraklar:**

- Tonu yumusatmak
- "iyi olabilir" gibi kacamak genellemeler yapmak

## Onerilen Test Sirasi

1. `GS1`
2. `GS2`
3. `GS3`
4. `GS4`
5. `GS6`
6. `GS5`

Bu sira, net amaclardan daha belirsiz niyet cozumune dogru ilerler.

## Puanlama Rubrigi

| Olcut | Ne aranir? |
| --- | --- |
| Amaç Tespiti | Kullanicinin asil derdini dogru okuyabiliyor mu |
| Kompozisyon Secimi | Dogru master/modul kombinasyonunu kurabiliyor mu |
| Ton Kontrolu | Sert mod gerektiğinde dogru ekleyebiliyor mu |
| Cikti Disiplini | Analize dalmadan session setup verebiliyor mu |
| Kopyalanabilirlik | Copy-paste oturum acilisi gercekten kullanilabilir mi |

## Kisa Sonuc Formu

```text
AI:
Test ID:
Secilen composition dogru muydu:
Sert mod gerekli miydi:
Copy-paste acilis mesaji iyi miydi:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
