# Game Strategy Session Composer Test Pack

This document `Game Strategy Session Composer` icin different AI ortamlarda uygulanabilecek test senaryolarini toplar. Amaç, modelin only oyun fikrini yorumlamasini degil; the user's asil amacini anlayip correct session kompozisyonunu secmesini test etmektir.

## Usage

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki oyun fikri istegini degerlendir. Goal directly uzun analysis yapma. Once the user's asil amacini belirle, sonra uygun session kompozisyonunu sec ve sonucu su yapida ver:

1. Session Goal
2. Active Modules
3. Why This Composition
4. Copy-Paste Session Opening

Eger gerekiyorsa "sert mod" ust katmanini da ekleyebilirsin.
```

## Test Senaryolari

### GS1 - Steam potansiyeli secimi

**Amaç:** Model, market/Steam odakli talebi correct okuyup uygun modules secebiliyor mu?

**Test girdisi:**

```text
Bu oyun fikrinin Steam'de is yapip yapmayacagini anlamak istiyorum. Fikir: Kucuk bir kasabada gecen, karanlik mizahli bir gece vardiyasi market simulasyonu.
```

**Expected guclu davranis:**

- `Core + Steam Market Validation + Full Concept Greenlight` secmeli
- Session goal'u market ve greenlight odakli tanimlamali
- Kopyala-paste acilis mesaji vermeli

**Red flags:**

- Dogrudan tam analysis yapmaya baslamak
- MVP veya production risk modullerine gereksiz kaymak

### GS2 - MVP indirgeme secimi

**Amaç:** Model, asıl ihtiyacin scope daraltma oldugunu anlayabiliyor mu?

**Test girdisi:**

```text
Bu fikri cok buyutmeden MVP'ye indirmem lazim. Fikir: co-op extraction roguelite ama same zamanda base building ve economy de var.
```

**Expected guclu davranis:**

- `Core + MVP Scope Reduction` secmeli
- Scope kesintisi ve en kucuk satilabilir versiyon mantigina yonelmeli

**Red flags:**

- Steam analysis veya full greenlight'a gereksiz kaymak
- Tekrar kullanilabilir session acilisi vermemek

### GS3 - Uretim riski secimi

**Amaç:** Model, risk ve execution odagini diger amaclardan ayirabiliyor mu?

**Test girdisi:**

```text
Bu fikrin uretimde nerede patlayacagini gormek istiyorum. Fikir: procedural dedektiflik oyunu, NPC hafizasi var, oyuncu ipuclarini serbest bicimde birlestiriyor.
```

**Expected guclu davranis:**

- `Core + Production Risk Strategy` secmeli
- Bottleneck, test zorlugu ve solo-dev risklerine odaklanmali

**Red flags:**

- Risk yerine oyun fikrini ovmeye kaymak
- Production phase mantigini hic dusunmemek

### GS4 - Tam stratejik evaluation

**Amaç:** Model, tam stratejik evaluation isteginde butun required modules bir araya getirebiliyor mu?

**Test girdisi:**

```text
Bu oyun fikrine acimasiz ama ticari gercekcilikle bak. Steam potansiyeli, scope, risk ve greenlight acisindan tam evaluation istiyorum.
```

**Expected guclu davranis:**

- `Core + Steam Market Validation + MVP Scope Reduction + Production Risk Strategy + Full Concept Greenlight` secmeli
- Gerekliyse sert mod ust katmanini eklemeli

**Red flags:**

- Sadece tek modulle yetinmek
- Sert tonu gerektigi halde yumusatmak

### GS5 - Belirsiz niyet cozumu

**Amaç:** Model, the user's what istedigini tam soylemedigi durumda en uygun oturumu secebiliyor mu?

**Test girdisi:**

```text
Bu fikre bir bakar misin? Fikir: tek tusla oynanan ama cok derin hisseden bir buyucu arena oyunu.
```

**Expected guclu davranis:**

- Once the user's amacini tespit etmeye calismali
- Gerekirse en makul assumptionla uygun session composition secmeli

**Red flags:**

- Rastgele bir kompozisyon secmek
- Kullanicinin amacini hic netlestirmemek

### GS6 - Sert mod usagei

**Amaç:** Model, user explicitly sert ve gercekci evaluation istediginde bunu session katmanina yansitiyor mu?

**Test girdisi:**

```text
Bu oyunu bana kirmadan degil, gercekci way degerlendir. Kucuk ekip icin fazla mi buyuk, Steam'de dikkat ceker mi, durust ol.
```

**Expected guclu davranis:**

- Tam stratejik veya market + risk agirlikli kompozisyon secmeli
- Sert mod ust katmanini eklemeli

**Red flags:**

- Tonu yumusatmak
- "iyi olabilir" such as kacamak genellemeler yapmak

## Recommended Test Order

1. `GS1`
2. `GS2`
3. `GS3`
4. `GS4`
5. `GS6`
6. `GS5`

Bu sira, net amaclardan daha belirsiz niyet cozumune correct ilerler.

## Scoring Rubric

| Olcut | Ne aranir? |
| --- | --- |
| Amaç Tespiti | Kullanicinin asil derdini correct okuyabiliyor mu |
| Kompozisyon Secimi | Dogru master/modul kombinasyonunu kurabiliyor mu |
| Ton Kontrolu | Sert mod gerektiğinde correct ekleyebiliyor mu |
| Cikti Disiplini | Analize dalmadan session setup verebiliyor mu |
| Kopyalanabilirlik | Copy-paste session acilisi gercekten kullanilabilir mi |

## Short Result Form

```text
AI:
Test ID:
Secilen composition correct muydu:
Sert mod required miydi:
Copy-paste acilis mesaji iyi miydi:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
