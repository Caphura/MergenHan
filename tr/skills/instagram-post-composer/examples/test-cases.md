# Instagram Post Composer — Test Cases

Bu dosya `instagram-post-composer` skill'ini farkli senaryolarda test etmek icin hazirlanmis ornek case'ler icerir. Her case'i bir AI oturumuna yapistirip skill'in ciktisini degerlendirin.

---

## Kullanim

1. AI oturumuna `skills/instagram-post-composer/SKILL.md` icerigini yapistirin.
2. Asagidaki test case'lerden birini gonderin.
3. Ciktiyi degerlendirme kriterlerine gore kontrol edin.

---

## Test Case 1 — Klasik Tam Paket (Psikolog)

**Niche:** Psikolog
**Zorluk:** Dusuk — skill'in en temel kullanimi

```
Klinik psikolog Ayse Hanım icin bir Instagram postu olustur.
Konu: "Anksiyete ile basa cikmanin 3 pratik yolu"
Hedef kitle: 25-40 yas arasi, buyuksehirde yasayan, stresli is hayati olan kadinlar.
```

### Degerlendirme Kriterleri
- [ ] Format onerisi gerekceleriyle sunulmus mu? (carousel beklenir)
- [ ] Nano Banana promptu kod blogunda, kopyalanabilir mi?
- [ ] Canva rehberinde exact template arama terimi var mi?
- [ ] Renk paleti hex kodlariyla verilmis mi?
- [ ] Font eslestirmesi Canva'da gercekten mevcut fontlar mi?
- [ ] Caption hook ilk 125 karakterde dikkat cekiyor mu?
- [ ] CTA net ve uygulanabilir mi?
- [ ] Hashtag sayisi 10-15 arasinda mi?
- [ ] Hashtag'lerde #love, #instagood gibi generic tag yok mu?
- [ ] Zamanlama onerisi specific gun + saat araligi mi? ("Sali 09:00-11:00" gibi)
- [ ] Zamanlama gerekcesi var mi?

---

## Test Case 2 — Farkli Niche (Fitness Kocu)

**Niche:** Fitness
**Zorluk:** Dusuk — farkli sektorde tutarlilik testi

```
Fitness kocu Mert Bey icin Instagram postu hazirla.
Konu: Ev ortaminda 15 dakikada yapilabilecek etkili bir sabah rutini.
Hedef kitle: 20-35 yas arasi, spor salonuna gidemeyen ama formda kalmak isteyen erkekler.
```

### Degerlendirme Kriterleri
- [ ] Renk paleti ve ton fitness niche'ine uygun mu? (enerjik, dinamik)
- [ ] Psikolog case'inden farkli bir gorsel atmosfer onerisi var mi?
- [ ] Zamanlama onerisi fitness icerigine uygun mu? (sabah erken saat beklenir)
- [ ] Caption dili motivasyonel ve hedef kitleye uygun mu?

---

## Test Case 3 — Format Zorlamasi (Single Image)

**Niche:** Avukat
**Zorluk:** Orta — kullanici belirli bir format istiyor

```
Is hukuku avukati icin Instagram postu olustur.
Konu: "Isten cikarildiginda bilmeniz gereken 1 numara hukuki hak"
Format: Single image olsun, carousel istemiyorum.
Hedef kitle: Calisanlar, 30-50 yas.
```

### Degerlendirme Kriterleri
- [ ] Kullanicinin format tercihine (single image) uyulmus mu?
- [ ] Carousel onerilmemis mi?
- [ ] Canva rehberi single image formatina uygun mu?
- [ ] Ton ciddi ve guven veren mi? (hukuk niche'i)
- [ ] Emoji kullanimi minimum veya sifir mi?

---

## Test Case 4 — Minimal Girdi (Belirsiz Niche)

**Niche:** Belirsiz
**Zorluk:** Orta — skill eksik bilgiyle nasil basa cikiyor?

```
Instagram postu lazim. Konu: motivasyon.
```

### Degerlendirme Kriterleri
- [ ] Skill niche ve hedef kitle sorusu sormus mu?
- [ ] Dogrudan genel bir post uretmek yerine netlestirme yapmis mi?
- [ ] Soru sayisi 2-3 ile sinirli mi? (ankete donusmemis mi?)
- [ ] Sorular yuksek etkili mi? (gereksiz detay sorulmamis mi?)

---

## Test Case 5 — Sadece Gorsel Prompt

**Niche:** Gastronomi
**Zorluk:** Orta — kullanici sadece bir alt cikti istiyor

```
Bir gurme burger restorani icin Instagram postu hazirliyorum ama sadece Nano Banana gorsel promptuna ihtiyacim var. Caption ve hashtag istemiyorum.
```

### Degerlendirme Kriterleri
- [ ] Sadece gorsel prompt verilmis mi?
- [ ] Gereksiz caption, hashtag ve zamanlama section'lari eklenmemis mi?
- [ ] Prompt yemek fotografciligina uygun detay iceriyor mu? (isik, kadraj, renk sicakligi)
- [ ] Prompt kopyalanabilir formatta (kod blogu) mi?

---

## Test Case 6 — Sadece Caption + Hashtag

**Niche:** Kisisel marka / Kocluk
**Zorluk:** Orta — gorsel prompt olmadan caption testi

```
Yasam kocu olarak bir Instagram postu paylasacagim. Gorseli kendim hazirladim, sadece caption ve hashtag stratejisi lazim.
Konu: "Konfor alanindan cikmanin gercek bedeli"
Hedef kitle: 25-40 yas, kisisel gelisimle ilgilenen profesyoneller.
```

### Degerlendirme Kriterleri
- [ ] Gorsel prompt ve Canva rehberi atlanmis mi?
- [ ] Hook guclu ve merak uyandirici mi?
- [ ] CTA kaydet/paylas/yoruma yaz gibi net mi?
- [ ] Hashtag'ler kisisel gelisim niche'ine uygun mu?
- [ ] Zamanlama onerisi motivasyon icerigine uygun mu?

---

## Test Case 7 — Carousel Derinlik Testi

**Niche:** Diyetisyen
**Zorluk:** Yuksek — carousel icin slide detayi beklenir

```
Diyetisyen Selin Hanim icin "Ofiste saglikli atistirmalik icin 5 kolay tarif" konulu bir carousel post hazirla.
Hedef kitle: Ofis calisanlari, 25-45 yas.
```

### Degerlendirme Kriterleri
- [ ] Carousel formati secilmis mi?
- [ ] Canva rehberinde slide basi max eleman sayisi belirtilmis mi?
- [ ] Her slide icin bilgi yogunlugu notu var mi?
- [ ] Kapak slide + icerik slide + CTA slide yapisi oneriliyor mu?
- [ ] Renk paleti saglik/beslenme niche'ine uygun mu?
- [ ] Zamanlama onerisi carousel + egitim kesisiminde mi? (hafta ici sabah beklenir)

---

## Test Case 8 — Sosyal Kanit / Referans Postu

**Niche:** Dis hekimi
**Zorluk:** Orta — farkli post amaci testi

```
Dis hekimi icin bir hasta referansi / sosyal kanit postu olustur.
Hasta memnuniyeti temasini isliyoruz. Oncesi-sonrasi gosterimi yapilacak.
Hedef kitle: 25-55 yas, dis estetigi ile ilgilenen kisiler.
```

### Degerlendirme Kriterleri
- [ ] Post amaci "sosyal kanit" olarak dogru tanimlanmis mi?
- [ ] Format onerisinde oncesi-sonrasi icin carousel veya single split-image gibi uygun secim var mi?
- [ ] Canva rehberinde before-after layout onerisi var mi?
- [ ] Zamanlama onerisi sosyal kanit kategorisine uygun mu? (Persembe-Cuma beklenir)
- [ ] Caption'da abartili vaatler yerine gercekci ton kullanilmis mi?
- [ ] Saglik icerigine uygun hassasiyet var mi? (etik sinirlar)

---

## Genel Basari Olcutleri

Her test case'in sonunda su sorulari kontrol edin:

1. **Taranabilirlik**: Cikti net basliklarla bolunmus mu?
2. **Kopyalanabilirlik**: Gorsel prompt kod blogunda mi?
3. **Spesifiklik**: Generic ifadeler yerine somut oneriler var mi?
4. **Niche uyumu**: Ton, renk, dil secimi niche'e uygun mu?
5. **Gereksiz uzama yok mu**: Istenmemis section eklenmemis mi?
6. **Zamanlama tutarliligi**: Referans tablosuyla uyumlu mu?
