---
name: nano-banana-image-prompt-composer
description: Use when a user has a rough visual idea and wants a short question flow that turns it into a clean, copyable Nano Banana image prompt.
---

# Nano Banana Image Prompt Composer

## Use When

- Kullanici yari tanimli bir gorsel fikirle gelip Nano Banana icin prompt istediginde
- Once dogru sorularin sorulmasi, sonra nihai image promptun yazilmasi istendiginde
- Gorselin degil, gorseli uretecek metin promptunun verilmesi gerektiginde
- Kullanici "beni yonlendir, sonra promptu ver" benzeri bir ihtiyac dile getirdiginde

## Workflow

1. Kullanici fikrini kisa bicimde yeniden ifade et ve ana sahneyi dogrula.
2. Sonuca en cok etki edecek eksik alanlari ayikla: sahne, isik, kadraj, stil, atmosfer, gercekcilik seviyesi ve istenmeyen detaylar.
3. Mumkun oldugunca 2-4 arasi yuksek etkili soru sor; kullaniciyi uzun anketle yorma.
4. Kritik belirsizlikler kapandiginda yeni tur acma; ayni cevapta nihai prompta gec.
5. Sonucu su yapida ver: kisa sahne ozeti, tek parca Nano Banana promptu, gerekiyorsa ince ayar notlari ve istege bagli varyasyonlar.
6. Ortam gorsel uretebiliyor olsa bile varsayilan ciktiyi metin olarak koru; kullanici acikca istemedikce gorsel uretme veya araci tetikleme.

## Output Expectations

- Sahne ozeti kisa, dogru ve kullanicinin hedefini yansitiyor olmali.
- Kod blogu icindeki prompt kismi dogrudan kopyalanabilir olmali.
- Prompt; ozne, ortam, isik, kompozisyon, stil ve atmosferi tek akista birlestirmeli.
- Gereksiz tekrar, anlamsiz kalite sloganlari veya kopya artist listeleriyle sisirilmemeli.
- Kullanici yalnizca prompt istiyorsa ek analiz uzatilmamali.

## References

- Kisa oturum ornegi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel image tool, render, canvas veya otomatik gorsel uretim davranislari adapter katmaninda belgelenmelidir.
- Varsayilan gorev metin tabanli Nano Banana promptu uretmektir; gorsel uretmek degil.
