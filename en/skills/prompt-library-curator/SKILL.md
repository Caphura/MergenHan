---
name: prompt-library-curator
description: Use when organizing, packaging, or reviewing master prompts, prompt modules, and skill blueprints inside the MergenHan library.
---

# Prompt Library Curator

## Use When

- Prompt librarysinde daginik content duzenlenecekse
- Bir blueprint'in skill paketine donusup donusmemesi degerlendirilecekse
- Katalog, metadata veya folder yeri decisionlari netlestirilecekse

## Workflow

1. Once repo yapisini, kataloglari ve bagli promptlari tara.
2. Icerigi correct ture yerlestir: `master`, `module`, `blueprint` veya `skill`.
3. Paketlenmis skill icin `SKILL.md` dosyasini sade tut; governance alanlarini `meta.yaml` icinde koru.
4. Yeni veya currentlenen varliklari kataloglara yansit.
5. Sonucu taranabilir bir ozet ve clear sonraki adimla bitir.

## Output Expectations

- Recommended veya yaplisting degisiklikler anlasilir olmali.
- Hangi icerigin neden promotion ettigi ya da etmedigi net belirtilmeli.
- Gerekirse `references/` altindaki checklist kullanilmali.

## References

- Ayrintili gozden gecirme icin `references/review-checklist.md` dosyasina bak.

## Portability Notes

- This skill'in core davranisi provider-agnostiktir.
- Runtime'a specific slash command, vehicle, permission veya agent wiring bilgileri `adapters/` altindaki mapping belgelerinde tutulmalidir.
