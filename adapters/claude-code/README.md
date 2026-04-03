# Claude Code Adapter

Bu klasor, MergenHan cekirdek prompt ve skill iceriklerini Claude Code tarzinda kullanmak icin gereken runtime esleme notlarini tutar.

## Kapsam

Burada su konular belgelenir:

- slash command veya komut girisi yaklasimi
- settings, hooks ve permission modeli
- agent wiring veya gorev dagitimi notlari
- cekirdek varliklarin Claude Code icindeki calistirma bicimi

## Ornekler

- [`mapping.md`](./mapping.md): cekirdek varligin Claude Code tarafinda nasil temsil edilecegi
- [`settings.example.json`](./settings.example.json): adapter katmanina ait, guvenli ve istege bagli ayar ornegi

## Sinir

Cekirdek davranis burada yeniden yazilmaz. Promptun veya skill'in asil mantigi `prompts/` ve `skills/` altinda kalir. Claude Code'a ozel syntax ve otomasyon ise bu adapter katmaninda tutulur.