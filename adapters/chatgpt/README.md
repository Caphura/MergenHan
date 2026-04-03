# ChatGPT Adapter

Bu klasor, MergenHan cekirdek iceriginin ChatGPT projeleri, custom GPT benzeri is akisleri veya manuel prompt injection yaklasimlariyla nasil kullanilacagini aciklar.

## Kapsam

- project instruction veya benzeri kalici baglamlar
- custom GPT tarzi paketleme notlari
- manuel kopyala-yapistir kullanim akislari
- cekirdek skill veya blueprint'in ChatGPT oturumuna tasinma bicimi

## Ornekler

- [`mapping.md`](./mapping.md): cekirdek varligin ChatGPT tarafinda nasil temsil edilecegi
- [`project-instructions-example.md`](./project-instructions-example.md): kisa proje talimati ornegi
- [`feature-spec-composer-project-instructions-example.md`](./feature-spec-composer-project-instructions-example.md): feature spec odakli skill icin kisa oturum / proje talimati ornegi
- [`nano-banana-project-instructions-example.md`](./nano-banana-project-instructions-example.md): text-only image prompt skill'i icin kisa oturum / proje talimati ornegi

## Sinir

ChatGPT'ye ozel davranis cekirdekte tutulmaz. Cekirdek tanim `prompts/` ve `skills/` altinda kalir; runtime'a ozel kullanim notlari bu adapter altina yazilir.
