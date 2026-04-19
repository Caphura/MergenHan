---
id: mh-blueprint-instagram-post-composer
title: Instagram Post Composer
type: blueprint
status: active
version: 1.0.0
summary: Professional'larin Instagram postlarini end-to-end olusturan, Nano Banana ile visual prompt ureten, detayli Canva layout rehberi sunan, caption yazan ve optimal yayinlama zamani oneren paketlenmeye aday draft.
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
input_contract: Kullanici bir professional'in (psikolog, koc, marka vb.) niche'ini, post konusunu ve varsa format tercihini verir.
output_contract: Nano Banana visual promptu, detayli Canva layout rehberi (template kategorisi, hex renk kodlari, font eslestirmesi, grid onerisi), caption (hook + govde + CTA), hashtag stratejisi ve optimal yayinlama zamani onerisi.
notes: Nano Banana image prompt asamasinda mh-skill-nano-banana-image-prompt-composer workflow'unu referans alir. Canva rehberi template kategorisi, renk paleti, tipografi eslestirmesi ve grid onerilerini specific olarak icerir.
---

# Responsibility

Professional musteriler icin Instagram postlarini end-to-end tasarlayan, visual yonlendirmeden metin yazarligina ve yayinlama stratejisine kadar butunsel rehberlik sunan uzman workflow. AI bu skill'i kullandiginda social media content strategist gibi davranir.

# Trigger Signals

- "Bu psikolog icin Instagram postu olustur."
- "Sunun icin profesyonel bir Instagram postu hazirla."
- "Bu konuyla ilgili visual + caption + zamanlama onerisi ver."
- "Instagram icin icerik paketi hazirla."
- "Bu mesaji Instagram postu olarak tasarla."
- "Su niche icin haftalik post plani yap."

# Workflow

1. Musterinin niche'ini (psikolog, fitness koc, avukat, marka vb.) ve hedef kitlesini anla. Daha once niche bilgisi paylasilmissa tekrar sorma.
2. Post'un amacini netlestir: egitim, motivasyon, kisisel hikaye, hizmet tanitimi, sosyal kanit, etklesim tetikleyici vb.
3. En uygun post formatini belirle: carousel (egitim icerikleri, adim adim rehberler), single image (motivasyon, duyuru), reel (kisa bilgi, behind-the-scenes), story (anlik paylasim, anket). Secimi gerekceleriyle sun.
4. Icerik mesajini ve tonunu 2-3 yuksek etkili soruyla netlestir; the user'i uzun anketle yorma. Kritik uncertaintyler kapandiginda yeni tur acma.
5. Nano Banana Image Prompt Composer workflow'unu kullanarak visual prompt olustur. Sahne, isik, stil, atmosfer ve renk paletini niche'e ve post amacina uyumlu sec. Prompt directly kopyalanabilir olmali.
6. Detayli Canva layout rehberi sun:
   - Template kategorisi: Canva search'te kullanilacak exact arama terimi (orn. "Instagram Post Motivational Quote", "Instagram Carousel Educational")
   - Renk paleti: primary, secondary ve accent renkleri hex kodlariyla; niche'e uygun psikolojik etki notu
   - Tipografi eslestirmesi: baslik fontu + govde fontu onerisi (Canva'da mevcut fontlardan)
   - Grid ve layout: metin-visual orani, alignment, whitespace kullanimi
   - Visual hierarchy: hangi eleman one cikmali, goz akisi yonlendirmesi
7. Caption yaz: dikkat cekici hook (ilk 125 karakter kritik), bilgi veya duygu iceren govde, net CTA. Niche'e uygun dil ve ton kullan. Emoji kullanimi olculu ve amacli olmali.
8. Hashtag stratejisi olustur:
   - Niche-specific (3-5): sektore ozel, orta hacimli
   - Genel erisim (3-5): genis kitleye ulasim, asiri buyuk olmayan
   - Branded (1-2): varsa marka veya kisisel hashtag
   - Toplam 10-15 arasi, realistic erisim potansiyeli olan
9. Icerik tipine ve hedef kitleye gore en etkili yayinlama gunu ve saatini oner. `references/posting-schedule-guide.md` referans tablosunu kullan. Onerinin gerekcesini short acikla.
10. Tum ciktiyi tek taranabilir pakette sun: visual prompt, Canva rehberi, caption, hashtag'ler ve zamanlama onerisi. Her section basligini clearly ayir.

# Output Expectations

- Visual prompt Nano Banana formatinda, kod blogu icinde directly kopyalanabilir olmali.
- Canva rehberi specific template kategorisi, hex renk kodlari ve font isimleriyle sunulmali; generic "guzel renkler secin" gibi ifadeler kabul edilmez.
- Caption professional ve hedef kitleye uygun olmali; gereksiz emoji flood'u, cringe ifadeler veya niche baglamindan kopuk ton yoksa kullanilmamali.
- Hashtag seti realistic erisim potansiyeli olan secimlerle olusturulmali; milyonlarca postlu generic tag'ler (orn. #love, #instagood) tercih edilmemeli.
- Zamanlama onerisi icerik tipi ile hedef kitle kesisiminde specific gun ve saat araligi olarak verilmeli; "aksam saatleri" gibi belirsiz ifadeler yerine "Carsamba 19:00-21:00" gibi net olmali.
- Tum paket tek cevapta, taranabilir basliklarla sunulmali.
- Kullanici only visual prompt veya only caption istiyorsa gereksiz sectionlar eklenmemeli.

# Promotion Criteria

- Farkli niche'lerde (saglik, egitim, hukuk, fitness, kisisel marka, gastronomi) tutarli sonuc veriyor olmali.
- Farkli post tiplerinde (egitim, motivasyon, hizmet tanitimi, sosyal kanit) workflow dengeli calistirilmali.
- Canva rehberi farkli sektorlerde uygulanabilir detay seviyesinde olmali.
- Zamanlama onerileri farkli icerik turleriyle tutarli ve gerekceli kalmali.
- Different adapter'lerde kolayca temsil edilebilmeli ve provider-specific syntax'a baglanmamali.
- Kullanici request sinyalleri yeterince tekrar ediyorsa `skills/` altinda paketlenmeye ready sayilabilir.
