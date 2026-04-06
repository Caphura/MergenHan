# Onboarding Router Test Pack

Bu belge, `Onboarding Router` icin farkli AI ortamlarda uygulanabilecek test senaryolarini toplar. Amac, modelin yalnizca tavsiye vermesini degil; kullanici talebini dogru varlik tipine veya repo aksiyonuna yonlendirip neden o yone gittigini aciklamasini test etmektir.

## Kullanim Sekli

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki repo veya prompt kutuphanesi istegini degerlendir. Dogrudan icerik yazmaya baslama. Once kullanicinin asil amacini belirle, sonra talebi su kategorilerden birine yonlendir:

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

Eger talep runtime'a ozelse, bunu acikca adapter mapping olarak belirt.
```

## Test Senaryolari

### OR1 - Tek gorevlik ama orkestre davranis

**Amaç:** Model, birden fazla davranisi orkestre eden yeni gorevi `master` olarak yonlendirebiliyor mu?

**Test girdisi:**

```text
Kullanicidan daginik bir gorsel fikir alip kisa sorularla netlestiren ve en sonda image modeline uygun tek parca prompt veren ilk calisan promptu yazmak istiyorum. Henuz test edilmedi, paketlenmeye aday bir skill gibi dusunmuyorum; once cekirdek promptu dogru yere koymak istiyorum. Bunu repoda nereye koymaliyim?
```

**Beklenen guclu davranis:**

- `master` rotasini secmeli
- Orkestrasyon mantigini aciklamali
- Bagimlilik adayi olarak ton veya output modullerini onerebilmeli

**Kirmizi bayraklar:**

- Dogrudan `module` ya da `skill` demek
- Tek gorevlik orkestrasyon akisini erken asamada yanlislikla `blueprint`e itmek
- Tekrar kullanilabilir cekirdek davranis ile paketlenmis beceriyi ayirmamak

### OR2 - Tekrar kullanilabilir davranis parcasi

**Amaç:** Model, baska promptlarda da kullanilabilecek atomik davranisi `module` olarak ayirabiliyor mu?

**Test girdisi:**

```text
Farkli promptlarda tekrar tekrar kullanabilecegim bir davranis yazmak istiyorum: model, cevap verirken her zaman kanit ile varsayimi ayirsin. Bu nereye gider?
```

**Beklenen guclu davranis:**

- `module` rotasini secmeli
- Bunun tek gorev degil, tekrar kullanilabilir davranis parcasi oldugunu belirtmeli
- Uygun klasor tipine dair ipucu verebilmeli

**Kirmizi bayraklar:**

- Bunu `master` veya `skill` olarak yonlendirmek
- Tekrar kullanimi ana karar ekseni olarak gormemek

### OR3 - Paketlenmeye aday ama henuz tam oturmamis beceri

**Amaç:** Model, davranisi var ama paketleme karari erken olan bir istegi `blueprint`e yonlendirebiliyor mu?

**Test girdisi:**

```text
Bir AI'nin daire ilanlarini yatirim acisindan analiz etmesini saglayan bir akisim var. Iyi calisiyor ama henuz farkli orneklerle yeterince denemedim. Simdilik bunu hangi katmanda tutmaliyim?
```

**Beklenen guclu davranis:**

- `blueprint` rotasini secmeli
- Test/olgunluk eksenini gerekce yapmali
- Hemen skill paketine ziplamamak gerektigini aciklamali

**Kirmizi bayraklar:**

- Yetersiz sinyale ragmen `skill` demek
- `master` ile `blueprint` ayrimini belirsiz birakmak

### OR4 - Terfi ve paketleme karari

**Amaç:** Model, kullanici artik paketleme istediginde bunu `packaging` aksiyonuna yonlendirebiliyor mu?

**Test girdisi:**

```text
Bir blueprint'i farkli AI'larda test ettim ve artik skill paketine cevirmek istiyorum. Bana repo icinde hangi dosyalari olusturmam gerektigini ve nasil ilerlemem gerektigini soyle.
```

**Beklenen guclu davranis:**

- `packaging` rotasini secmeli
- `SKILL.md`, `meta.yaml`, gerekiyorsa `examples/` gibi ihtiyaclari listelemeli
- Bunu dogrudan yeni `skill` yazma istegiyle karistirmamali

**Kirmizi bayraklar:**

- Sadece `skill` deyip paketleme akislarini es gecmek
- Katalog / metadata guncellemesini unutturmak

### OR5 - Repo bakim ve katalog sorusu

**Amaç:** Model, bakim odakli talebi `catalog` aksiyonuna yonlendirebiliyor mu?

**Test girdisi:**

```text
Repoya yeni bir prompt ekledim ama kataloglarda gorunup gorunmediginden emin degilim. Hangi adima gitmeliyim?
```

**Beklenen guclu davranis:**

- `catalog` rotasini secmeli
- Katalog uretim / dogrulama akislarini onermeli
- Icerik yazimi yerine bakim aksiyonuna yonelmeli

**Kirmizi bayraklar:**

- Yeni prompt yazmaya baslamak
- `module` veya `master` gibi icerik tipi secmeye kaymak

### OR6 - Runtime'a ozel tasima istegi

**Amaç:** Model, runtime'a ozel talebi `adapter mapping` olarak ayirabiliyor mu?

**Test girdisi:**

```text
Elimde hazir bir skill var. Bunu ChatGPT proje talimati olarak nasil kullanacagimi yazmak istiyorum. Bu cekirdege mi gitmeli, adapter'e mi?
```

**Beklenen guclu davranis:**

- `adapter mapping` rotasini secmeli
- Runtime'a ozel davranisin adapter katmanina ait oldugunu acikca yazmali
- Cekirdek tanimi provider syntax'i ile kirletmemeyi vurgulamali

**Kirmizi bayraklar:**

- Bunu `skill` veya `master` degisikligi gibi gormek
- Adapter katmaninin amacini kacirmak

### OR7A - Standalone orchestrator ayrimi

**Amaç:** Model, kendi basina calisan ama henuz ilk asamadaki bir yonlendirme orkestratorunu `master` olarak ayirabiliyor mu?

**Test girdisi:**

```text
Repodaki farkli onboarding durumlarini yoneten ilk calisan orchestrator promptu yazmak istiyorum. Bu akisin gorevi, kullaniciya bazen yeni prompt yazdirma, bazen blueprint'ten skill'e terfi karari verme, bazen de katalog bakimina yonlendirme olacak. Henuz test edilmedi ve paketlenmeye aday reusable bir beceri olarak degil, once tek gorevlik bir orchestration promptu olarak dusunuyorum. Bunu repoda nereye koymaliyim?
```

**Beklenen guclu davranis:**

- `master` rotasini secmeli
- Bunun once tek gorevlik orchestration promptu olarak okunmasi gerektigini aciklamali
- Bagimlilik adayi olarak context audit, repo architecture ve action summary gibi parcalari gosterebilmeli

**Kirmizi bayraklar:**

- Bunu erken asamada `blueprint`e itmek
- Talebi atomik bir `module`e indirgeyip kaybetmek
- Paketlenmis `skill` gibi davranmak

### OR7B - Reusable routing behavior ayrimi

**Amaç:** Model, tekrar kullanilabilir ve skill-benzeri routing mantigini `blueprint` olarak ayirabiliyor mu?

**Test girdisi:**

```text
Repo icinde tekrar tekrar kullanabilecegim bir yonlendirme davranisi tasarlamak istiyorum. Bu davranis, gelen istegin yeni prompt, blueprint, skill packaging, catalog bakimi veya adapter mapping olup olmadigini ayirsin. Amacim atomik bir yardimci davranis parcasi degil; farkli onboarding durumlarinda tekrar kullanabilecegim, ileride paketlenmeye aday bir routing mantigini once dogru katmanda tutmak. Simdilik bunu henuz skill olarak paketlemek istemiyorum. Bunu repoda nereye koymaliyim?
```

**Beklenen guclu davranis:**

- `blueprint` rotasini secmeli
- Bunun atomik bir `module` degil, tekrar kullanilabilir ve skill-benzeri bir routing mantigi oldugunu ayirt etmeli
- Talebin asil isinin onboarding ve yonlendirme davranisi oldugunu fark etmeli
- Bagimlilik adayi olarak context audit, repo architecture ve action summary gibi parcalari gosterebilmeli

**Kirmizi bayraklar:**

- Talebi tek bir katalog scripti gibi yorumlamak
- Router davranisini `module`e asiri indirgeyip kaybetmek
- Tekrar kullanilabilir router davranisini yanlislikla `master` olarak siniflandirmak

## Onerilen Test Sirasi

1. `OR1`
2. `OR2`
3. `OR3`
4. `OR4`
5. `OR5`
6. `OR6`
7. `OR7A`
8. `OR7B`

Bu sira, net varlik seciminden daha karmasik yonlendirme ve siniflandirma kararlarina dogru ilerler. `OR7A` ve `OR7B`, benzer gorunen ama farkli katmanlara gitmesi gereken iki routing durumunu ayri ayri stresler.

## Puanlama Rubrigi

| Olcut | Ne aranir? |
| --- | --- |
| Amaç Tespiti | Kullanicinin asil derdini dogru okuyabiliyor mu |
| Routing Dogrulugu | `master`, `module`, `blueprint`, `skill`, `packaging`, `catalog`, `adapter mapping` arasinda dogru secim yapiyor mu |
| Gerekcelendirme | Neden o yone gittigini acik ve ikna edici sekilde anlatabiliyor mu |
| Bagimlilik Onerisi | Uygun bagimlilik adaylarini gorup gereksiz genislemiyor mu |
| Sonraki Adim Netligi | Cikti, kullanicinin ne yapacagini somutlastiriyor mu |

## Kisa Sonuc Formu

```text
AI:
Test ID:
Secilen rota dogru muydu:
Gerekce yeterince net miydi:
Onerilen sonraki adim kullanisli miydi:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
