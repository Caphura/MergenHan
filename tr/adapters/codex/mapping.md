# Codex Mapping

## Adapter Ne Bekler?

- Acik gorev mantigi olan cekirdek prompt, blueprint veya skill
- Izlenebilir bagimlilik zinciri
- Gerekirse repo icindeki hedef dosya veya katalog baglantilari

## Core Skill Burada Nasil Temsil Edilir?

- `SKILL.md` cekirdek yurutme talimati olarak okunur
- `meta.yaml` bagimlilik, kaynak blueprint ve uyumluluk bilgisini verir
- Codex'e ozel gorev paketleme, arac kullanimi ve calisma akisi bu adapter tarafinda tarif edilir

## Core'dan Ne Degismeden Kalmalidir?

- Skill'in amaci ve kapsam siniri
- Dependency iliskileri
- Tetikleyici sinyaller ve workflow mantigi
- Cekirdek portability kurallari

## Runtime Duzeyinde Ne Uyarlanabilir?

- Repo icinde gorev parcasi haline getirme bicimi
- Arac secimi, komut yurutme disiplini ve is akisi formati
- Cikti sunumu ve kapanis ozetleri
