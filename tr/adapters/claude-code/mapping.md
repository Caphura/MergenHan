# Claude Code Mapping

## Adapter Ne Bekler?

- Okunur bir cekirdek prompt, blueprint veya skill tanimi
- Acik `depends_on` zinciri
- Gerekirse `portability` ve `adapter_support` bilgisi

## Core Skill Burada Nasil Temsil Edilir?

- `SKILL.md` cekirdek talimat olarak okunur
- `meta.yaml` bagimlilik ve paket bilgisi saglar
- Claude Code'a ozel slash command, hooks, settings ve permission notlari bu adapter dokumaninda tarif edilir

## Core'dan Ne Degismeden Kalmalidir?

- ID, baslik ve amac
- Bagimlilik zinciri
- Tetikleyici kullanim mantigi
- Cekirdek workflow adimlari

## Runtime Duzeyinde Ne Uyarlanabilir?

- Komut cagrisi sekli
- Tool kullanimi ve izin modeli
- Agent dagitimi veya gorev orkestrasyonu
- Oturum acilis metninin Claude Code formatina cevrimi
