---
name: nano-banana-image-prompt-composer
description: Use when a user has a rough visual idea and wants a short question flow that turns it into a clean, copyable Nano Banana image prompt.
---

# Nano Banana Image Prompt Composer

## Use When

- Kullanici yari tanimli bir visual fikirle gelip Nano Banana icin prompt istediginde
- Once correct sorularin sorulmasi, sonra nihai image promptun yazilmasi istendiginde
- Gorselin degil, visuali uretecek metin promptunun verilmesi gerektiginde
- Kullanici "beni yonlendir, sonra promptu ver" benzeri bir ihtiyac dile getirdiginde

## Workflow

1. Kullanici fikrini short bicimde yeniden ifade et ve ana sahneyi dogrula.
2. Sonuca en cok etki edecek eksik alanlari ayikla: sahne, isik, kadraj, stil, atmosfer, gercekcilik seviyesi ve istenmeyen detaylar.
3. Mumkun oldugunca 2-4 arasi yuksek etkili soru sor; the user uzun anketle yorma.
4. Kritik uncertaintyler kapandiginda yeni tur acma; same cevapta nihai prompta gec.
5. Sonucu su yapida ver: short sahne ozeti, tek parca Nano Banana promptu, gerekiyorsa ince ayar notlari ve optional varyasyonlar.
6. Ortam visual uretebiliyor even if present default outputyi metin olarak koru; user explicitly istemedikce visual uretme veya vehiclei tetikleme.

## Output Expectations

- Sahne ozeti short, correct ve the user's hedefini yansitiyor olmali.
- Kod blogu icindeki prompt kismi directly kopyalanabilir olmali.
- Prompt; ozne, ortam, isik, kompozisyon, stil ve atmosferi tek akista birlestirmeli.
- Gereksiz tekrar, anlamsiz kalite sloganlari veya kopya artist listeleriyle sisirilmemeli.
- Kullanici only prompt istiyorsa ek analysis uzatilmamali.

## References

- Short session example icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- This skill'in core davranisi provider-agnostiktir.
- Runtime'a specific image tool, render, canvas veya otomatik visual generation davranislari adapter katmaninda belgelenmelidir.
- Varsaylisting task text-based Nano Banana promptu uretmektir; visual uretmek degil.
