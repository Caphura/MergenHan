---
id: mh-blueprint-instagram-post-composer
title: Instagram Post Composer
type: blueprint
status: active
version: 1.0.0
summary: Profesyonellerin Instagram postlarini bastan sona olusturan, Nano Banana ile gorsel prompt ureten, detayli Canva layout rehberi sunan, caption yazan ve en etkili yayinlama zamanini oneren paketlenmeye aday taslak.
tags:
  - social-media
  - instagram
  - content-strategy
  - image-generation
  - copywriting
  - workflow
depends_on:
  - mh-skill-nano-banana-image-prompt-composer
last_reviewed: 2026-04-19
portability: universal
adapter_support:
  claude-code: planned
  chatgpt: planned
  codex: planned
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Kullanici bir profesyonelin (psikolog, koc, marka vb.) niche'ini, post konusunu ve varsa format tercihini verir.
output_contract: Nano Banana gorsel promptu, detayli Canva layout rehberi (sablon kategorisi, hex renk kodlari, font eslestirmesi, grid onerisi), caption (hook + govde + CTA), hashtag stratejisi ve en etkili yayinlama zamani onerisi.
notes: Nano Banana gorsel prompt asamasinda mh-skill-nano-banana-image-prompt-composer is akisini referans alir. Canva rehberi sablon kategorisi, renk paleti, tipografi eslestirmesi ve grid onerilerini belirgin bicimde icerir.
---

# Sorumluluk

Profesyonel musteriler icin Instagram postlarini bastan sona tasarlayan, gorsel yonlendirmeden metin yazarligina ve yayinlama stratejisine kadar butunsel rehberlik sunan uzman is akisi. Yapay zeka bu beceriyi kullandiginda sosyal medya icerik stratejisti gibi davranir.

# Tetiklenme Sinyalleri

- "Bu psikolog icin Instagram postu olustur."
- "Sunun icin profesyonel bir Instagram postu hazirla."
- "Bu konuyla ilgili gorsel + caption + zamanlama onerisi ver."
- "Instagram icin icerik paketi hazirla."
- "Bu mesaji Instagram postu olarak tasarla."
- "Su niche icin haftalik post plani yap."

# Is Akisi

1. Musterinin niche'ini (psikolog, fitness kocu, avukat, marka vb.) ve hedef kitlesini anla. Daha once niche bilgisi paylasilmissa tekrar sorma.
2. Postun amacini netlestir: egitim, motivasyon, kisisel hikaye, hizmet tanitimi, sosyal kanit, etkilesim tetikleyici vb.
3. En uygun post formatini belirle: carousel (egitim icerikleri, adim adim rehberler), single image (motivasyon, duyuru), reel (kisa bilgi, behind-the-scenes), story (anlik paylasim, anket). Secimi gerekceleriyle sun.
4. Icerik mesajini ve tonunu 2-3 yuksek etkili soruyla netlestir; kullaniciyi uzun anketle yorma. Kritik belirsizlikler kapandiginda yeni tur acma.
5. Nano Banana Image Prompt Composer is akisini kullanarak gorsel prompt olustur. Sahne, isik, stil, atmosfer ve renk paletini niche'e ve post amacina uyumlu sec. Prompt dogrudan kopyalanabilir olmali.
6. Detayli Canva layout rehberi sun:
   - Sablon kategorisi: Canva aramasinda kullanilacak tam arama terimi (orn. "Instagram Post Motivational Quote", "Instagram Carousel Educational")
   - Renk paleti: birincil, ikincil ve vurgu renkleri hex kodlariyla; niche'e uygun psikolojik etki notu
   - Tipografi eslestirmesi: baslik fontu + govde fontu onerisi (Canva'da mevcut fontlardan)
   - Grid ve layout: metin-gorsel orani, hizalama, bosluk kullanimi
   - Gorsel hiyerarsi: hangi oge one cikmali, goz akisi yonlendirmesi
7. Caption yaz: dikkat cekici hook (ilk 125 karakter kritik), bilgi veya duygu iceren govde, net CTA. Niche'e uygun dil ve ton kullan. Emoji kullanimi olculu ve amacli olmali.
8. Hashtag stratejisi olustur:
   - Niche'e ozel (3-5): sektore ozel, orta hacimli
   - Genel erisim (3-5): genis kitleye ulasim, asiri buyuk olmayan
   - Markali (1-2): varsa marka veya kisisel hashtag
   - Toplam 10-15 arasi, gercekci erisim potansiyeli olan
9. Icerik tipine ve hedef kitleye gore en etkili yayinlama gununu ve saatini oner. `references/posting-schedule-guide.md` referans tablosunu kullan. Onerinin gerekcesini kisa acikla.
10. Tum ciktiyi tek taranabilir pakette sun: gorsel prompt, Canva rehberi, caption, hashtagler ve zamanlama onerisi. Her bolumu net baslikla ayir.

# Cikti Beklentileri

- Gorsel prompt Nano Banana formatinda, kod blogu icinde dogrudan kopyalanabilir olmali.
- Canva rehberi belirgin sablon kategorisi, hex renk kodlari ve font isimleriyle sunulmali; genel "guzel renkler secin" gibi ifadeler kabul edilmez.
- Caption profesyonel ve hedef kitleye uygun olmali; gereksiz emoji yogunlugu, itici ifadeler veya niche baglamidan kopuk ton kullanilmamali.
- Hashtag seti gercekci erisim potansiyeli olan secimlerle olusturulmali; milyonlarca postlu genel etiketler (orn. #love, #instagood) tercih edilmemeli.
- Zamanlama onerisi icerik tipi ile hedef kitle kesisiminde belirli gun ve saat araligi olarak verilmeli; "aksam saatleri" gibi belirsiz ifadeler yerine "Carsamba 19:00-21:00" gibi net olmali.
- Tum paket tek cevapta, taranabilir basliklarla sunulmali.
- Kullanici yalnizca gorsel prompt veya yalnizca caption istiyorsa gereksiz bolumler eklenmemeli.

# Terfi Kriterleri

- Farkli niche'lerde (saglik, egitim, hukuk, fitness, kisisel marka, gastronomi) tutarli sonuc veriyor olmali.
- Farkli post tiplerinde (egitim, motivasyon, hizmet tanitimi, sosyal kanit) is akisi dengeli calistirilmali.
- Canva rehberi farkli sektorlerde uygulanabilir detay seviyesinde olmali.
- Zamanlama onerileri farkli icerik turleriyle tutarli ve gerekceli kalmali.
- Farkli adapterlerde kolayca temsil edilebilmeli ve platforma ozel soz dizimine baglanmamali.
- Kullanici istek sinyalleri yeterince tekrar ediyorsa `skills/` altinda paketlenmeye hazir sayilabilir.
