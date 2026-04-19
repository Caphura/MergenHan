---
name: instagram-post-composer
description: Use when a user needs to create a professional Instagram post for a client or brand, covering visual prompt, Canva layout, caption, hashtags, and optimal posting schedule.
---

# Instagram Post Composer

## Use When

- Kullanici bir professional (psikolog, koc, avukat, marka vb.) icin Instagram postu olusturmak istediginde
- Visual prompt, caption, hashtag ve zamanlama onerisi iceren complete bir icerik paketi istendiginde
- Musterinin niche'ine uygun profesyonel seviyede social media icerigi gerektiginde
- Kullanici "bu konu icin Instagram postu hazirla" veya "icerik paketi olustur" benzeri bir ihtiyac dile getirdiginde
- Post'un ne zaman yayinlanirsa en etkili sonucu verecegi bilgisi istendiginde

## Workflow

1. Musterinin niche'ini ve hedef kitlesini anla. Daha once paylasilmissa tekrar sorma.
2. Post'un amacini netlestir: egitim, motivasyon, kisisel hikaye, hizmet tanitimi, sosyal kanit veya etkilesim tetikleyici.
3. En uygun post formatini belirle ve gerekcelesiyle sun:
   - **Carousel**: egitim icerikleri, adim adim rehberler, listeler, before-after
   - **Single image**: motivasyon, duyuru, tek mesajli paylasimlar
   - **Reel**: kisa bilgi, behind-the-scenes, trend katilimi
   - **Story**: anlik paylasim, anket, soru-cevap, countdown
4. Icerik mesajini ve tonunu 2-3 yuksek etkili soruyla netlestir. Kritik uncertaintyler kapandiginda ayni cevapta ciktiya gec.
5. Nano Banana Image Prompt Composer workflow'unu kullanarak visual prompt olustur. Sahne, isik, stil, atmosfer ve renk paletini niche ile post amacina uyumlu tut.
6. Detayli Canva layout rehberi sun:
   - **Template kategorisi**: Canva search'te kullanilacak exact arama terimi
     - Orn. "Instagram Post Motivational Quote Minimal"
     - Orn. "Instagram Carousel Educational Slide"
     - Orn. "Instagram Story Question Poll"
   - **Renk paleti**: primary, secondary ve accent renkleri hex kodlariyla
     - Niche'e uygun psikolojik renk etkisini short acikla
     - Orn. Psikolog: `#2D4A3E` (guven veren koyu yesil), `#F5F0E8` (sicak krem), `#8B6F47` (toprak tonu accent)
   - **Tipografi eslestirmesi**: Canva'da mevcut fontlardan baslik + govde onerisi
     - Orn. Baslik: Playfair Display — govde: Lato
     - Orn. Baslik: Montserrat Bold — govde: Open Sans
   - **Grid ve layout**: metin-visual orani, alignment, whitespace kullanimi
     - Carousel icin slide basi max eleman sayisi ve bilgi yogunlugu
   - **Visual hierarchy**: one cikmasi gereken eleman, goz akisi yonlendirmesi, contrast kullanimi
7. Caption yaz:
   - **Hook** (ilk 125 karakter): dikkat cekici, merak uyandiran veya empati kuran acilis
   - **Govde**: bilgi, hikaye veya duygu iceren ana metin; niche'e uygun dil ve ton
   - **CTA**: net eylem cagrisi (kaydet, paylas, yoruma yaz, link'e tikla vb.)
   - Emoji kullanimi olculu ve amacli; emoji flood'u yapilmamali
8. Hashtag stratejisi olustur:
   - **Niche-specific** (3-5): sektore ozel, orta hacimli hashtag'ler
   - **Genel erisim** (3-5): genis kitleye ulasim, asiri buyuk olmayan
   - **Branded** (1-2): varsa marka veya kisisel hashtag
   - Toplam 10-15 arasi; milyonlarca postlu generic tag'lerden kacin
9. Icerik tipine ve hedef kitleye gore en etkili yayinlama gunu ve saatini oner. `references/posting-schedule-guide.md` referans tablosunu kullan. Onerinin gerekcesini short acikla.
10. Tum ciktiyi tek taranabilir pakette sun. Her section'i clear baslikla ayir.

## Output Expectations

- Visual prompt Nano Banana formatinda, kod blogu icinde directly kopyalanabilir olmali.
- Canva rehberi specific olmali: template arama terimi, hex renk kodlari, font isimleri, grid onerisi. Generic "guzel bir tasarim secin" gibi ifadeler kabul edilmez.
- Caption professional ve hedef kitleye uygun olmali. Niche'ten kopuk ton veya gereksiz emoji kullanilmamali.
- Hashtag seti realistic erisim potansiyeli olan secimlerle olusturulmali.
- Zamanlama onerisi specific gun ve saat araligi olarak verilmeli; "aksam saatleri" gibi belirsiz ifadeler yerine "Carsamba 19:00-21:00" gibi net olmali.
- Kullanici only visual prompt veya only caption istiyorsa gereksiz sectionlar eklenmemeli.

## References

- Yayinlama zamanlama referansi icin `references/posting-schedule-guide.md` dosyasina bak.
- Visual prompt olusturma icin `skills/nano-banana-image-prompt-composer/SKILL.md` workflow'unu referans al.

## Portability Notes

- Bu skill'in core davranisi provider-agnostiktir.
- Runtime'a specific social media API entegrasyonu, scheduling tool baglantisi veya otomatik post yayinlama davranislari adapter katmaninda belgelenmelidir.
- Varsayilan gorev metin tabanli icerik paketi uretmektir; otomatik paylasim yapmak degil.
