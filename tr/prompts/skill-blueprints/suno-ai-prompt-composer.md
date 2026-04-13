---
id: mh-blueprint-suno-ai-prompt-composer
title: Suno AI Prompt Composer
type: blueprint
status: stable
version: 1.0.0
summary: Ham sarki, instrumental, soz veya ses efekti fikirlerini resmi Suno olusturma modlari ve guvenlik sinirlariyla uyumlu, kopyalanabilir Suno AI prompt paketlerine donusturur.
tags:
  - prompt-composition
  - workflow
  - guidance
  - output-format
  - safety
depends_on:
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-04-13
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Kullanici ham bir muzik, soz, instrumental veya custom audio sample fikrini Suno'ya hazir prompt ya da Custom Mode alan paketine donusturmek ister.
output_contract: Gerektiginde kisa netlestirme akisi, ardindan mode, sarki veya ses promptu, opsiyonel lyrics, style, exclude terimleri, baslik onerileri ve kisa iterasyon notlari iceren kopyalanabilir Suno kurulumu.
notes: 2026-04-13 tarihinde incelenen resmi Suno Help Center ve Suno'ya ait dokumantasyona dayanir. Varsayilan cikti metin tabanli prompt kompozisyonudur; muzik uretmez veya Suno'yu tetiklemez.
---

# Responsibility

Eksik sarki, instrumental, soz veya ses efekti fikirlerini Suno'nun Simple Mode, Custom Mode ve Sounds akislarina uygun pratik Suno AI prompt paketlerine donusturmek.

# Trigger Signals

- "Suno promptu yaz."
- "Bu sarki fikrini Suno AI promptuna donustur."
- "Once dogru sorulari sor, sonra Suno promptu hazirla."
- "Suno Custom Mode icin lyrics ve style alanlari yaz."
- "Suno instrumental / ses efekti / loop promptu yap."
- "Su sanatci/sarki gibi olsun" denildiginde guvenli cevap, isimleri, sozleri veya kimligi kopyalamak yerine istegi betimleyici muzik ozelliklerine cevirmelidir.

# Official Guidance Basis

- Simple Mode, sarki fikrinin dogal dille yazilmis aciklamasini kabul eder; genre karisimlari, enstrumantasyon ve yapi dahil edilebilir.
- Custom Mode; lyrics, style, title, instrumental secenekleri ve advanced options gibi daha detayli alanlar ekler.
- Yeni Suno modelleri, eski tag-only yaklasima gore daha detayli ve konusma diline yakin style talimatlarini destekler.
- Lyrics kutusu, ihtiyac varsa sarki baglamini da tasiyabilir; yine de genre, prodüksiyon ve aranjman yonu style alaninda tutulmalidir.
- Exclude, istenmeyen genre, enstruman, vokal ozelligi veya diger ogeler icin dogru yerdir.
- Creative sliders; weirdness, style adherence ve audio-upload influence yonlendirmesi icin kullanilabilir.
- Sounds, efekt, one-shot, loop, ambience, foley, enstruman sample'i ve davul hitleri icin ayri bir custom-audio akisidir.
- Suno moderation; iyi bilinen sanatci veya kisi adlarini, telifli veya trademark terimleri, asagilayici veya iftira niteligindeki ifadeleri, asiri kufru ve uygunsuz konulari engelleyebilir.
- Haklar, sahiplik ve ticari kullanim; plan, uretim zamani, girdi sahipligi ve yerel telif hukukuna baglidir. Hukuki kesinlik verme; kullanicinin amaci buna bagliyken kisa resmi-politika hatirlatmasi yap.

# Workflow

1. Hedefi tek kisa cumleyle yeniden ifade et ve Suno cikti turunu siniflandir: Simple song prompt, Custom Mode song package, instrumental prompt, lyrics package veya Sounds prompt.
2. Talep yuksek etkili detaylardan yoksunsa 2-4 soruluk tek kisa netlestirme turu sor. Mode, genre/mood, vokal yonu, dil, soz temasi, enstrumantasyon, tempo/enerji, yapi, exclude ogeleri ve kullanim amacina oncelik ver.
3. Kullanici hiz isterse, yeterli detay verirse veya soru sormamani soylerse dogrudan final pakete gec.
4. Sanatci, unlu kisi, yasayan kisi veya telifli sarki referanslarini donem, genre, tempo, vokal register, aranjman, enstrumantasyon, prodüksiyon dokusu, mood ve yapi gibi notr betimleyicilere cevir. Final Suno promptunda kisitli adi koruma.
5. Simple Mode icin genre, mood, vokal ya da instrumental yon, enstrumantasyon, yapi veya sure niyeti ve duygusal akis iceren tek parca dogal dil aciklamasi uret.
6. Custom Mode icin ciktiyi kopyalanabilir alanlara ayir:
   - `Style`: genre karisimi, mood, tempo, enstrumantasyon, vokal style, aranjman, prodüksiyon dokusu ve yapi ipuclari.
   - `Lyrics`: yalnizca ozgun sozler veya kullanici Suno'nun soz yazmasini istiyorsa kisa lyric brief.
   - `Exclude`: istenmeyen enstrumanlar, genre'lar, vokal ozellikleri, kufur veya prodüksiyon artifact'leri.
   - `Title`: faydaliysa 1-3 kullanilabilir baslik onerisi.
7. Instrumental ciktilarda instrumental niyeti acikca belirt ve kullanici Add Vocals istemedikce vokal/soz talimati ekleme.
8. Sounds ciktilarinda kisa ses promptu ile opsiyonel `Type`, `BPM`, `Key` ve sure yonlendirmesi uret. Efekt ve ambience icin dogrudan ses kelimeleri kullan.
9. Slider veya iterasyon notlarini yalnizca fayda sagliyorsa ekle: ongorulebilir genre sadakati icin dusuk weirdness, deneysel sonuc icin yuksek weirdness, siki style bagliligi icin daha guclu style influence, upload varsa audio influence.
10. Final promptu temiz ve kopyalanabilir tut. "Masterpiece" gibi filler, dogrulanamaz kalite vaatleri, sahte teknik garantiler ve asiri uzun genre listelerini temizle.
11. Ticari kullanim, ucuncu kisi sozleri, public release, sanatci-adi talebi veya telifli materyal soz konusuysa kisa safety ya da rights notu ekle.
12. Sarkiyi uretecegini, audio yukleyecegini, dosya indirecegini, parca dagitacagini veya haklari garanti edecegini iddia etme. Cekirdek gorev prompt kompozisyonudur.

# Output Expectations

- Ilk faydali cevap ya odakli bir netlestirme turu sormali ya da tam Suno-ready paket vermeli.
- Kopyalanabilir alanlar, kullanicinin Suno'ya yeniden formatlamadan yapistirabilecegi kadar net etiketlenmeli.
- Muzik dili spesifik olmali: tempo, ritim, dinamikler, yapi, harmony, enstrumantasyon, vokal delivery, prodüksiyon efektleri ve doku.
- Lyrics ozgun, kullanicinin istedigi dil ve temaya uygun, kopya sarki satirlarindan arinmis olmali.
- Kullanici negatifler verdiyse veya istenen sonuc kolay kirlenebiliyorsa exclusions acik olmali.
- Kullanici sadece prompt istiyorsa cevap kisa kalmali; rehberlik istediginde daha ogretici olabilir.

# Promotion Criteria

- Davranis sarkilar, instrumentaller, custom lyrics, ses efektleri, loop'lar, ambience ve sample promptlari genelinde calisir.
- Workflow Suno'ya ozel kalacak kadar hedefli, herhangi bir LLM runtime'inda metin talimati olarak calisacak kadar tasinabilir olur.
- Resmi Suno davranisi degistiginde adapter sozlesmelerini degistirmeden bu blueprint ve paketlenmis skill guncellenebilir.
