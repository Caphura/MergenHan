---
name: skill-packager
description: Use when evaluating whether a blueprint is ready to become a packaged skill and when preparing the minimum safe packaging steps.
---

# Skill Packager

## Use When

- Bir blueprint'in paketlenmis skill olmaya ready olup olmadigi degerlendirilecekse
- Paketleme oncesi eksik workflow, zayif kontrat veya gorunmeyen dependencies tespit edilmek isteniyorsa
- Minimum guvenli package structure ve katalog currentlemeleri netlestirilecekse

## Workflow

1. Hedef blueprint'i oku; workflow netligi, input/output contract'i ve dependency gorunurlugunu degerlendir.
2. Terfiye engel olabilecek eksikleri separate: zayif veya belirsiz workflow, eksik kontrat, gorunmeyen dependency zinciri, eksik package dosyalari veya unutulmus katalog currentlemeleri.
3. Minimum required package yapisini tanimla: `SKILL.md` ve `meta.yaml`.
4. Guncellenmesi gereken kataloglari belirt: `catalog/skills.md` ve `catalog/dependencies.md`; only gercekten faydaliysa `README.md` notunu ekle.
5. Sonucu `readiness`, `missing pieces`, `packaging steps` ve `next step` basliklari altinda short, uygulanabilir bir packaging ozeti olarak sun.

## Output Expectations

- `readiness`: Blueprint'in immediately terfiye uygun olup olmadigi ve neden.
- `missing pieces`: Workflow netligi, kontrat, dependency gorunurlugu, package dosyalari veya katalog eksikleri.
- `packaging steps`: Paketlemek icin gereken minimum guvenli adimlar.
- `next step`: Bir sonraki uygulanabilir hareket.

## Portability Notes

- This skill packaging decision mantigini provider-agnostik bicimde preserves.
- Runtime'a specific uygulama, adapter veya otomasyon detaylari core skill paketine degil adapter katmanina aittir.
