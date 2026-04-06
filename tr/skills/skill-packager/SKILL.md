---
name: skill-packager
description: Use when evaluating whether a blueprint is ready to become a packaged skill and when preparing the minimum safe packaging steps.
---

# Skill Packager

## Use When

- Bir blueprint'in paketlenmis skill olmaya hazir olup olmadigi degerlendirilecekse
- Paketleme oncesi eksik workflow, zayif kontrat veya gorunmeyen bagimliliklar tespit edilmek isteniyorsa
- Minimum guvenli paket yapisi ve katalog guncellemeleri netlestirilecekse

## Workflow

1. Hedef blueprint'i oku; workflow netligi, input/output contract'i ve bagimlilik gorunurlugunu degerlendir.
2. Terfiye engel olabilecek eksikleri ayristir: zayif veya belirsiz workflow, eksik kontrat, gorunmeyen dependency zinciri, eksik paket dosyalari veya unutulmus katalog guncellemeleri.
3. Minimum gerekli paket yapisini tanimla: `SKILL.md` ve `meta.yaml`.
4. Guncellenmesi gereken kataloglari belirt: `catalog/skills.md` ve `catalog/dependencies.md`; yalnizca gercekten faydaliysa `README.md` notunu ekle.
5. Sonucu `readiness`, `missing pieces`, `packaging steps` ve `next step` basliklari altinda kisa, uygulanabilir bir packaging ozeti olarak sun.

## Output Expectations

- `readiness`: Blueprint'in hemen terfiye uygun olup olmadigi ve neden.
- `missing pieces`: Workflow netligi, kontrat, dependency gorunurlugu, paket dosyalari veya katalog eksikleri.
- `packaging steps`: Paketlemek icin gereken minimum guvenli adimlar.
- `next step`: Bir sonraki uygulanabilir hareket.

## Portability Notes

- Bu skill packaging karar mantigini provider-agnostik bicimde korur.
- Runtime'a ozel uygulama, adapter veya otomasyon detaylari cekirdek skill paketine degil adapter katmanina aittir.
