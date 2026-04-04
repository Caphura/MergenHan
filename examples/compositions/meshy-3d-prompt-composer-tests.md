# Meshy 3D Prompt Composer Test Pack

Bu belge, `Meshy 3D Prompt Composer` icin farkli AI ortamlarda uygulanabilecek test senaryolarini toplar. Amac, modelin yalnizca rastgele 3D prompt yazmasini degil; kullanicinin ham asset fikrini kisa ama etkili sorularla netlestirip Meshy icin kopyalanabilir, metin odakli ve gercekci bir prompta donusturmesini test etmektir.

## Kullanim Sekli

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki 3D asset istegini Meshy icin prompta donustur. Ama hemen uzun prompt yazmaya atlama. Once eksik ama sonucu gercekten degistirecek detaylari bul, gerekirse sadece birkac yuksek etkili soru sor, sonra yeterli netlik varsa ayni cevapta sonucu su yapida ver:

1. Asset Summary
2. Meshy Prompt
3. Production Notes
4. Optional Variations

Varsayilan davranis text-only olsun. Modeli uretme, araci tetikleme veya sahte teknik garanti verme.
```

## Test Senaryolari

### MP1 - Stylized oyun asset'i

**Amac:** Model, stylized bir prop istegini uzun ankete cevirmeden netlestirip kullanilabilir prompt uretebiliyor mu?

**Test girdisi:**

```text
Meshy icin stylized bir health potion sisesi promptu istiyorum. Fantasy oyunu icin olacak.
```

**Beklenen guclu davranis:**

- Kisa ama yuksek etkili sorularla sise formu, renk hissi, malzeme ve kondisyonu netlestirmeli
- Sonucu stylized game prop mantigiyla toparlamali
- Prompt kismi kopyalanabilir olmali

**Kirmizi bayraklar:**

- Gereksiz uzun soru listesi acmak
- Sadece "high quality, detailed, amazing" gibi bos kalite sloganlariyla prompt sisirmek

**Referans guclu cevap:**

```text
Asset Summary

- Stylized fantasy health potion bottle
- Oyun ici prop olarak ilk bakista okunakli olmali
- Simdilik orta-neseli, temiz fantasy yone yakin bir varsayimla ilerliyorum

Meshy Prompt

stylized fantasy health potion bottle, readable game prop silhouette, small rounded glass vial with a slightly exaggerated body and short neck, cork stopper, glowing red healing liquid clearly visible inside, simple but appealing fantasy design, hand-crafted feel, subtle leather wrap and small metal accent details, polished glass material, clean shape language, charming collectible item look, balanced stylized proportions, suitable for an RPG inventory or world prop, single isolated asset

Production Notes

- Eger istersen bunu daha cute, daha dark fantasy veya daha premium rare item yonune cekebilirim.
- Bu versiyon bilincli olarak teknik garanti vermiyor; once form, stil ve okunaklilik tarafini temiz kuruyor.

Optional Variations

- Cute casual fantasy item
- Rare item glow-up
- Simplified low poly version
```
### MP2 - Sci-fi hard-surface prop

**Amac:** Model, sert yuzeyli teknik bir objede siluet ve fonksiyon hissini yakalayabiliyor mu?

**Test girdisi:**

```text
Bir sci-fi ammo crate icin Meshy promptu yaz. Askeri ama cok jenerik durmasin.
```

**Beklenen guclu davranis:**

- Kasanin kullanim baglami, olcek hissi, panel yapisi, materyal dili ve yipranma seviyesini netlestirmeli
- "Askeri ama jenerik degil" kismini promptta farkli kimlik unsurlariyla yansitmali
- Hard-surface varlik mantigini image prompt diline kaydirmadan kurmali

**Kirmizi bayraklar:**

- Sadece renk ekleyip objeyi ayirt etmeden birakmak
- Teknik his vermek yerine yalnizca sinematik atmosfer tarif etmek

### MP3 - Karakter / creature netlestirme

**Amac:** Model, canli bir varlik isteginde form, tavir ve stil yonunu sorularla ayrisabiliyor mu?

**Test girdisi:**

```text
Meshy icin sevimli ama hafif yaramaz gorunen bir orman creature'i prompta donustur.
```

**Beklenen guclu davranis:**

- Creature'in boyut, beden orani, ana ayirt edici ozellikleri ve stil yonunu netlestirmeli
- Sevimli ile yaramaz arasindaki ton dengesini promptta hissettirmeli
- Promptu sadece duygu sifati listesine cevirmemeli

**Kirmizi bayraklar:**

- Somut siluet veya fiziksel detay olmadan soyut duygu sifati yigmak
- Kullaniciyi karakter sheet seviyesinde gereksiz teknik detaylara bogmak

### MP4 - Belirsiz istekten net prompta gecis

**Amac:** Model, daginik ve eksik bir istekte once dogru sorulari sorup sonra durabildigi yerde prompta gecebiliyor mu?

**Test girdisi:**

```text
Aklimda bir silah var ama tam oturtamadim. Biraz antik, biraz da teknoloji karisimi bir sey olsun. Meshy icin toparlar misin?
```

**Beklenen guclu davranis:**

- Silahin turu, donem hissi, enerji / mekanik karisimi ve kullanim sinifini netlestiren az sayida soru sormali
- Yeterli cevap gelince yeni tur acmadan nihai prompt vermeli
- Hybrid estetik fikrini tek akista toparlamali

**Kirmizi bayraklar:**

- Sonsuz soru moduna gecmek
- Kullanici hala belirsizken asiri spesifik ama uydurma kararlar vermek

### MP5 - Teknik garanti direnci

**Amac:** Model, kullanici teknik beklenti istediginde bilmedigi seyleri uydurmadan dikkatli kalabiliyor mu?

**Test girdisi:**

```text
Bana Meshy icin game-ready bir medieval kalkan promptu yaz. Low poly olsun, topology tertemiz olsun, UV sorunsuz olsun, her engine'e hazir olsun.
```

**Beklenen guclu davranis:**

- Kullanicinin teknik beklentisini not etmeli ama sahte garanti dili kullanmamali
- Promptta stil ve form tarafini guclu tutarken teknik notlari daha dikkatli, sinirli ve gercekci sunmali
- "Her engine'e hazir" gibi kesin iddialari yumusatmali veya baglama baglamali

**Kirmizi bayraklar:**

- Teknik olarak garanti veremeyecegi seyleri kesinmis gibi yazmak
- Promptun tamamini anlamsiz uretim sloganlarina cevirmek

### MP6 - Sadece prompt isteyen hizli kullanim

**Amac:** Model, kullanici zaten yeterince net tarif verdiginde ekstra analiz uzatmadan dogrudan iyi bir prompt verebiliyor mu?

**Test girdisi:**

```text
Meshy icin prompt yaz: kucuk bir masaustu collectible robot, retro-futuristic tasarim, beyaz ve turuncu govde, hafif ciziklerle kullanilmis hissi, sevimli ama premium bir urun gibi gorunsun.
```

**Beklenen guclu davranis:**

- Girdinin yeterince net oldugunu anlayip uzun soru turu acmamali
- Asset summary kisa kalmali, prompt ise yogun ve kopyalanabilir olmali
- Stil, malzeme, renk ve urun hissini dengeli sekilde birlestirmeli

**Kirmizi bayraklar:**

- Gereksiz soru sormak
- Kullanicinin zaten verdigi detaylari zayiflatmak veya dagitmak

## Onerilen Test Sirasi

1. `MP1`
2. `MP6`
3. `MP2`
4. `MP4`
5. `MP3`
6. `MP5`

Bu sira, net ve kolay prop isteklerinden daha belirsiz netlestirme durumlarina ve en sonda teknik guardrail stresine dogru ilerler.

## Puanlama Rubrigi

| Olcut | Ne aranir? |
| --- | --- |
| Niyet Tespiti | Kullanici prop, creature, weapon veya collectible istedigini dogru okuyabiliyor mu |
| Soru Disiplini | Yalnizca gerekli oldugunda az sayida yuksek etkili soru soruyor mu |
| Prompt Kalitesi | Nihai prompt somut, kopyalanabilir ve Meshy kullanimina uygun mu |
| Guardrail Disiplini | Model uretmeden, sahte teknik garanti vermeden text-first kaliyor mu |
| Eyleme Donukluk | Production Notes ve Optional Variations gercekten ise yariyor mu |

## Kisa Sonuc Formu

```text
AI:
Test ID:
Soru sayisi dengeli miydi:
Nihai prompt kopyalanabilir miydi:
Guardrail disiplini korundu mu:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```