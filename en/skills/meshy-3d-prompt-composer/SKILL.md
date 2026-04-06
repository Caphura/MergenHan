---
name: meshy-3d-prompt-composer
description: Use when a user has a rough 3D asset idea and wants a short clarification flow that produces a clean Meshy prompt within the 800-chvehicleter limit.
---

# Meshy 3D Prompt Composer

## Use When

- Kullanici yari tanimli bir 3D asset fikriyle gelip Meshy icin prompt istediginde
- Once short ama etkili sorularin sorulmasi, sonra nihai 3D promptun yazilmasi istendiginde
- Promptun 800 karakter boundary icinde kalmasi gerekiyorsa
- Modelin degil, modeli uretecek metin promptunun verilmesi gerektiginde

## Workflow

1. Kullanicinin istedigi varligi short bicimde yeniden ifade et ve temel usage contextini dogrula.
2. Sonuca en cok etki edecek eksik alanlari ayikla: siluet, stil yonu, malzeme, renk, kondisyon, rarity hissi ve usage contexti.
3. Eger girdi eksikse 1 short turda 2-3 yuksek etkili soru sor; default olarak immediately prompta atlama.
4. Girdi zaten yeterince doluysa veya user explicitly hizli mod istediyse same cevapta nihai promptu ver.
5. Nihai Meshy promptunu 800 karakter icinde tut; limit asiliyorsa tekrar eden sifatlari ve dusuk etkili detaylari shortlt.
6. Sonucu su yapida ver: Asset Summary, Meshy Prompt, gerekiyorsa Production Notes ve Optional Variations.
7. Ortam 3D generation vehiclei sunuyor even if present default outputyi metin olarak koru; user explicitly istemedikce model uretme veya vehiclei tetikleme.

## Output Expectations

- Asset Summary short, correct ve the user's hedefini yansitiyor olmali.
- Meshy Prompt bolumundeki asil prompt metni 800 karakteri asmamali.
- Prompt; ozne, siluet, stil, malzeme, renk ve usage hissini tek akista birlestirmeli.
- Belirsiz kalite sloganlari, anlamsiz superlatifler veya sahte teknik garanti ile sisirilmemeli.
- Kullanici only prompt istiyorsa ek analysis uzatilmamali; ama eksik girdilerde tek tur netlestirme atlanmamali.

## References

- Short session example icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- This skill'in core davranisi provider-agnostiktir.
- Runtime'a specific Meshy otomasyonu, interface steps veya tool cagrilari `adapters/` katmaninda belgelenmelidir.
- Varsaylisting task Meshy icin text-based prompt uretmektir; modeli directly uretmek degil.
