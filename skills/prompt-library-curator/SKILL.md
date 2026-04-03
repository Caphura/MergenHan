---
name: prompt-library-curator
description: Use when organizing, packaging, or reviewing master prompts, prompt modules, and skill blueprints inside the MergenHan library.
---

# Prompt Library Curator

## Use When

- Prompt kutuphanesinde daginik icerik duzenlenecekse
- Bir blueprint'in skill paketine donusup donusmemesi degerlendirilecekse
- Katalog, metadata veya klasor yeri kararlari netlestirilecekse

## Workflow

1. Once repo yapisini, kataloglari ve bagli promptlari tara.
2. Icerigi dogru ture yerlestir: `master`, `module`, `blueprint` veya `skill`.
3. Paketlenmis skill icin `SKILL.md` dosyasini sade tut; yonetisim alanlarini `meta.yaml` icinde koru.
4. Yeni veya guncellenen varliklari kataloglara yansit.
5. Sonucu taranabilir bir ozet ve acik sonraki adimla bitir.

## Output Expectations

- Onerilen veya yapilan degisiklikler anlasilir olmali.
- Hangi icerigin neden terfi ettigi ya da etmedigi net belirtilmeli.
- Gerekirse `references/` altindaki checklist kullanilmali.

## References

- Ayrintili gozden gecirme icin `references/review-checklist.md` dosyasina bak.
