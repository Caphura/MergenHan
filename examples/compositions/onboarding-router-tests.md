# Onboarding Router Test Pack

This document `Onboarding Router` icin different AI ortamlarda uygulanabilecek test senaryolarini toplar. Amac, modelin only tavsiye vermesini degil; user talebini correct asset tipine veya repo aksiyonuna yonlendirip neden o yone gittigini aciklamasini test etmektir.

## Usage

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki repo veya prompt librarysi istegini degerlendir. Dogrudan content yazmaya baslama. Once the user's asil amacini belirle, sonra talebi su kategorilerden birine yonlendir:

- master
- module
- blueprint
- skill
- packaging
- catalog
- adapter mapping

Sonucu su yapida ver:

1. Routing Decision
2. Why This Route
3. Dependency Candidates
4. Recommended Next Step

Eger request runtime'a ozelse, bunu explicitly adapter mapping olarak belirt.
```

## Test Senaryolari

### OR1 - Tek tasklik ama orkestre davranis

**Amaç:** Model, birden fazla davranisi orkestre eden yeni taski `master` olarak yonlendirebiliyor mu?

**Test girdisi:**

```text
Kullanicidan daginik bir visual fikir alip short sorularla netlestiren ve en sonda image modeline uygun tek parca prompt veren ilk calisan promptu yazmak istiyorum. Henuz test edilmedi, paketlenmeye aday bir skill such as dusunmuyorum; once core promptu correct yere koymak istiyorum. Bunu repoda nereye koymaliyim?
```

**Expected guclu davranis:**

- `master` rotasini secmeli
- Orkestrasyon mantigini aciklamali
- Bagimlilik adayi olarak ton veya output modullerini onerebilmeli

**Red flags:**

- Dogrudan `module` ya da `skill` demek
- Tek tasklik orkestrasyon akisini erken asamada yanlislikla `blueprint`e itmek
- Tekrar kullanilabilir core davranis ile paketlenmis beceriyi ayirmamak

### OR2 - Tekrar kullanilabilir davranis parcasi

**Amaç:** Model, baska promptlarda da kullanilabilecek atomik davranisi `module` olarak ayirabiliyor mu?

**Test girdisi:**

```text
Farkli promptlarda tekrar tekrar kullanabilecegim bir davranis yazmak istiyorum: model, cevap verirken her zaman evidence ile assumptioni ayirsin. Bu nereye gider?
```

**Expected guclu davranis:**

- `module` rotasini secmeli
- Bunun tek task degil, tekrar kullanilabilir davranis parcasi oldugunu belirtmeli
- Uygun folder tipine dair ipucu verebilmeli

**Red flags:**

- Bunu `master` veya `skill` olarak yonlendirmek
- Tekrar usagei ana decision ekseni olarak gormemek

### OR3 - Paketlenmeye aday ama henuz tam oturmamis beceri

**Amaç:** Model, davranisi var ama packaging decisioni erken olan bir istegi `blueprint`e yonlendirebiliyor mu?

**Test girdisi:**

```text
Bir AI'nin daire listinglarini investment acisindan analysis etmesini saglayan bir akisim var. Iyi calisiyor ama henuz different examplelerle yeterince denemedim. Simdilik bunu hangi katmanda tutmaliyim?
```

**Expected guclu davranis:**

- `blueprint` rotasini secmeli
- Test/olgunluk eksenini gerekce yapmali
- Hemen skill paketine ziplamamak gerektigini aciklamali

**Red flags:**

- Yetersiz sinyale ragmen `skill` demek
- `master` ile `blueprint` ayrimini belirsiz birakmak

### OR4 - Terfi ve packaging decisioni

**Amaç:** Model, user artik packaging istediginde bunu `packaging` aksiyonuna yonlendirebiliyor mu?

**Test girdisi:**

```text
Bir blueprint'i different AI'larda test ettim ve artik skill paketine cevirmek istiyorum. Bana repo icinde hangi dosyalari olusturmam gerektigini ve how ilerlemem gerektigini soyle.
```

**Expected guclu davranis:**

- `packaging` rotasini secmeli
- `SKILL.md`, `meta.yaml`, gerekiyorsa `examples/` such as ihtiyaclari listelemeli
- Bunu directly yeni `skill` yazma istegiyle karistirmamali

**Red flags:**

- Sadece `skill` deyip packaging akislarini es gecmek
- Katalog / metadata currentlemesini unutturmak

### OR5 - Repo maintenance ve katalog sorusu

**Amaç:** Model, maintenance odakli talebi `catalog` aksiyonuna yonlendirebiliyor mu?

**Test girdisi:**

```text
Repoya yeni bir prompt ekledim ama kataloglarda gorunup gorunmediginden emin degilim. Hangi adima gitmeliyim?
```

**Expected guclu davranis:**

- `catalog` rotasini secmeli
- Katalog generation / validation akislarini onermeli
- Icerik writing yerine maintenance aksiyonuna yonelmeli

**Red flags:**

- Yeni prompt yazmaya baslamak
- `module` veya `master` such as content tipi secmeye kaymak

### OR6 - Runtime'a specific tasima istegi

**Amaç:** Model, runtime'a specific talebi `adapter mapping` olarak ayirabiliyor mu?

**Test girdisi:**

```text
Elimde ready bir skill var. Bunu ChatGPT proje talimati olarak how kullanacagimi yazmak istiyorum. Bu cekirdege mi gitmeli, adapter'e mi?
```

**Expected guclu davranis:**

- `adapter mapping` rotasini secmeli
- Runtime'a specific davranisin adapter katmanina ait oldugunu explicitly yazmali
- Core tanimi provider syntax'i ile kirletmemeyi vurgulamali

**Red flags:**

- Bunu `skill` veya `master` degisikligi such as gormek
- Adapter katmaninin amacini kacirmak

### OR7A - Standalone orchestrator ayrimi

**Amaç:** Model, kendi basina calisan ama henuz ilk asamadaki bir guidance orkestratorunu `master` olarak ayirabiliyor mu?

**Test girdisi:**

```text
Repodaki different onboarding durumlarini yoneten ilk calisan orchestrator promptu yazmak istiyorum. Bu akisin taski, to the user bazen yeni prompt yazdirma, bazen blueprint'ten skill'e promotion decisioni verme, bazen de katalog maintenanceina guidance olacak. Henuz test edilmedi ve paketlenmeye aday reusable bir beceri olarak degil, once tek tasklik bir orchestration promptu olarak dusunuyorum. Bunu repoda nereye koymaliyim?
```

**Expected guclu davranis:**

- `master` rotasini secmeli
- Bunun once tek tasklik orchestration promptu olarak okunmasi gerektigini aciklamali
- Bagimlilik adayi olarak context audit, repo architecture ve action summary such as parcalari gosterebilmeli

**Red flags:**

- Bunu erken asamada `blueprint`e itmek
- Talebi atomik bir `module`e indirgeyip kaybetmek
- Paketlenmis `skill` such as davranmak

### OR7B - Reusable routing behavior ayrimi

**Amaç:** Model, tekrar kullanilabilir ve skill-benzeri routing mantigini `blueprint` olarak ayirabiliyor mu?

**Test girdisi:**

```text
Repo icinde tekrar tekrar kullanabilecegim bir guidance davranisi tasarlamak istiyorum. Bu davranis, gelen istegin yeni prompt, blueprint, skill packaging, catalog maintenancei veya adapter mapping olup olmadigini ayirsin. Amacim atomik bir yardimci davranis parcasi degil; different onboarding durumlarinda tekrar kullanabilecegim, ileride paketlenmeye aday bir routing mantigini once correct katmanda tutmak. Simdilik bunu henuz skill olarak paketlemek istemiyorum. Bunu repoda nereye koymaliyim?
```

**Expected guclu davranis:**

- `blueprint` rotasini secmeli
- Bunun atomik bir `module` degil, tekrar kullanilabilir ve skill-benzeri bir routing logic oldugunu ayirt etmeli
- Talebin asil isinin onboarding ve guidance davranisi oldugunu fark etmeli
- Bagimlilik adayi olarak context audit, repo architecture ve action summary such as parcalari gosterebilmeli

**Red flags:**

- Talebi tek bir katalog scripti such as yorumlamak
- Router davranisini `module`e asiri indirgeyip kaybetmek
- Tekrar kullanilabilir router davranisini yanlislikla `master` olarak siniflandirmak

## Recommended Test Order

1. `OR1`
2. `OR2`
3. `OR3`
4. `OR4`
5. `OR5`
6. `OR6`
7. `OR7A`
8. `OR7B`

Bu sira, net asset seciminden daha karmasik guidance ve siniflandirma decisionlarina correct ilerler. `OR7A` ve `OR7B`, benzer gorunen ama different katmanlara gitmesi gereken iki routing durumunu ayri ayri stresler.

## Scoring Rubric

| Olcut | Ne aranir? |
| --- | --- |
| Amaç Tespiti | Kullanicinin asil derdini correct okuyabiliyor mu |
| Routing Dogrulugu | `master`, `module`, `blueprint`, `skill`, `packaging`, `catalog`, `adapter mapping` arasinda correct secim yapiyor mu |
| Gerekcelendirme | Neden o yone gittigini clear ve ikna edici way anlatabiliyor mu |
| Bagimlilik Onerisi | Uygun dependency adaylarini gorup gereksiz genislemiyor mu |
| Sonraki Adim Netligi | Cikti, the user's what yapacagini somutlastiriyor mu |

## Short Result Form

```text
AI:
Test ID:
Secilen rota correct muydu:
Gerekce yeterince net miydi:
Recommended sonraki step kullanisli miydi:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
