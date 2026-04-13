---
name: suno-ai-prompt-composer
description: Use when a user has a rough song, instrumental, lyric, or sound-effect idea and wants a short clarification flow that turns it into a clean, copyable Suno AI prompt or Custom Mode field package.
---

# Suno AI Prompt Composer

## Use When

- Kullanici Suno AI icin sarki, instrumental, lyrics-first parca, loop, ambience, ses efekti veya sample promptu istediginde.
- Kullanici final Suno-ready prompttan once dogru sorularin sorulmasini istediginde.
- Kullanici Style, Lyrics, Exclude, Title veya Sounds settings gibi Custom Mode alanlarina ihtiyac duydugunda.
- Kullanici bir sanatci, unlu kisi, mevcut sarki veya telifli lyric referansi verdiginde ve talep guvenli betimleyici muzik ozelliklerine cevrilmeliyse.

## Workflow

1. Hedefi tek kisa cumleyle yeniden ifade et ve cikti turunu siniflandir: Simple song prompt, Custom Mode package, instrumental prompt, lyrics package veya Sounds prompt.
2. Kritik detaylar eksikse 2-4 soruluk tek kisa netlestirme turu sor. Mode, genre/mood, vokal yonu, dil, lyric temasi, enstrumantasyon, tempo/enerji, yapi, exclusions ve kullanim amacina oncelik ver.
3. Kullanici hiz isterse, yeterli detay verirse veya soru sormamani soylerse final paketi hemen uret.
4. Suno odakli muzik kelimeleri kullan: genre blend, mood, tempo, ritim, dinamikler, yapi, enstrumantasyon, vokal delivery, prodüksiyon dokusu, efektler ve duygusal akis.
5. Sanatci, unlu kisi, yasayan kisi, mevcut sarki veya telifli lyric referanslarinda korunan referansi final prompttan cikar ve donem, vokal register, aranjman, enstrumantasyon, tempo, prodüksiyon style ve mood gibi notr ozelliklerle degistir.
6. Simple Mode icin tek parca, kompakt, dogal dilde sarki aciklamasi ver.
7. Custom Mode icin cevabi kopyalanabilir alanlara ayir:
   - `Style`: genre karisimi, mood, tempo, enstrumantasyon, vokal style, aranjman, prodüksiyon dokusu ve yapi ipuclari.
   - `Lyrics`: yalnizca ozgun lyrics veya kullanici Suno'nun soz yazmasini istiyorsa kisa lyric brief.
   - `Exclude`: istenmeyen genre'lar, enstrumanlar, vokal ozellikleri, kufur veya prodüksiyon artifact'leri.
   - `Title`: faydaliysa 1-3 baslik onerisi.
8. Instrumental ciktilarda instrumental niyeti acikca belirt ve kullanici sonradan Add Vocals istemedikce vokal veya lyric talimati ekleme.
9. Sounds ciktilarinda kisa ses promptu ile opsiyonel `Type`, `BPM`, `Key` ve sure yonlendirmesi ver. Whoosh, rumble, glitch, impact, ambience, chatter, kick, snare, swell ve loop gibi dogrudan ses kelimelerini tercih et.
10. Slider veya iterasyon notlarini yalnizca faydaliysa ekle: ongorulebilir genre sadakati icin dusuk Weirdness, deneysel sonuc icin yuksek Weirdness, strict style adherence icin daha guclu Style Influence, yalnizca upload varsa Audio Influence.
11. Prompt metnini kopyalanabilir tut; dogrulanamaz kalite vaatlerini, sahte teknik garantileri, asiri uzun genre listelerini ve generic "best ever" dilini temizle.
12. Muzik uretme, Suno cagrisi yapma, dosya yukleme, track indirme, sarki dagitma veya hak garantisi verme. Varsayilan cikti metin tabanli prompt kompozisyonudur.

## Official Guardrails

- Suno iyi bilinen sanatci veya kisi adlarini, telifli veya trademark terimleri, asagilayici ya da iftira niteligindeki ifadeleri, asiri kufru ve uygunsuz konulari engelleyebilir. Bunlari final promptlara koyma.
- Yalnizca ozgun lyrics kullan. Kullanici ucuncu kisi sozleri verir veya isterse izin baglamini sor ya da yeni ve ozgun lyric yonune cevir.
- Haklar ve ticari kullanim; plan, uretim zamani, girdi sahipligi ve yerel telif hukukuna baglidir. Gerekli oldugunda yalnizca kisa politika hatirlatmasi yap; hukuki kesinlik verme.
- Public sharing; prompt, lyrics ve diger sarki detaylarini reuse riskine acabilir. Bunu yalnizca kullanici yayinlama, paylasma veya reuse riski sorarsa belirt.

## Output Expectations

- Soru soruyorsan ilk cevabi kisa ve uygulanabilir tut.
- Final paket uretiyorsan kullanicinin Suno'ya yapistirabilecegi net etiketler kullan.
- Varsayilan final yapi:

```text
Suno Setup
Mode:
Title:
Style:
Lyrics:
Exclude:
Notes:
```

- Simple Mode icin alan paketi yerine sunu kullan:

```text
Simple Mode Prompt
...
```

- Sounds icin sunu kullan:

```text
Suno Sounds Setup
Prompt:
Type:
BPM:
Key:
Notes:
```

## References

- Kisa Custom Mode akisi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi Suno prompt yazimina ozeldir ama runtime'dan bagimsizdir.
- Runtime otomasyonu, Suno UI talimatlari, hesap islemleri, download veya publishing davranisi bu core skill'de degil `adapters/` katmaninda yer almalidir.
- Current model availability, pricing, rights veya feature names onemli oldugunda cevap vermeden once en guncel resmi Suno dokumantasyonunu dogrula.
