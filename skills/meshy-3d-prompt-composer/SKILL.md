---
name: meshy-3d-prompt-composer
description: Use when a user has a rough 3D asset idea and wants a short clarification flow that produces a clean Meshy prompt within the 800-character limit.
---

# Meshy 3D Prompt Composer

## Use When

- Kullanici yari tanimli bir 3D asset fikriyle gelip Meshy icin prompt istediginde
- Once kisa ama etkili sorularin sorulmasi, sonra nihai 3D promptun yazilmasi istendiginde
- Promptun 800 karakter siniri icinde kalmasi gerekiyorsa
- Modelin degil, modeli uretecek metin promptunun verilmesi gerektiginde

## Workflow

1. Kullanicinin istedigi varligi kisa bicimde yeniden ifade et ve temel kullanim baglamini dogrula.
2. Sonuca en cok etki edecek eksik alanlari ayikla: siluet, stil yonu, malzeme, renk, kondisyon, rarity hissi ve kullanim baglami.
3. Eger girdi eksikse 1 kisa turda 2-3 yuksek etkili soru sor; varsayilan olarak hemen prompta atlama.
4. Girdi zaten yeterince doluysa veya kullanici acikca hizli mod istediyse ayni cevapta nihai promptu ver.
5. Nihai Meshy promptunu 800 karakter icinde tut; limit asiliyorsa tekrar eden sifatlari ve dusuk etkili detaylari kisalt.
6. Sonucu su yapida ver: Asset Summary, Meshy Prompt, gerekiyorsa Production Notes ve Optional Variations.
7. Ortam 3D uretim araci sunuyor olsa bile varsayilan ciktiyi metin olarak koru; kullanici acikca istemedikce model uretme veya araci tetikleme.

## Output Expectations

- Asset Summary kisa, dogru ve kullanicinin hedefini yansitiyor olmali.
- Meshy Prompt bolumundeki asil prompt metni 800 karakteri asmamali.
- Prompt; ozne, siluet, stil, malzeme, renk ve kullanim hissini tek akista birlestirmeli.
- Belirsiz kalite sloganlari, anlamsiz superlatifler veya sahte teknik garanti ile sisirilmemeli.
- Kullanici yalnizca prompt istiyorsa ek analiz uzatilmamali; ama eksik girdilerde tek tur netlestirme atlanmamali.

## References

- Kisa oturum ornegi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel Meshy otomasyonu, arayuz adimlari veya tool cagrilari `adapters/` katmaninda belgelenmelidir.
- Varsayilan gorev Meshy icin metin tabanli prompt uretmektir; modeli dogrudan uretmek degil.
