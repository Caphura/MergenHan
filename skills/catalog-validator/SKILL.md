---
name: catalog-validator
description: Use when validating repository catalogs, metadata, links, and dependency integrity across MergenHan.
---

# Catalog Validator

## Use When

- Repo kataloglarinin current ve tutarli kalip kalmadigi kontrol edilecekse
- `catalog/`, `prompts/` ve `skills/` arasindaki baglar dogrulanacaksa
- Duplicate ID, kirik dependency veya eksik package dosyasi such as butunluk sorunlari aranacaksa

## Workflow

1. `catalog/` altindaki indeks dosyalarini incele ve listelenen yollarin gercekte var olup olmadigini kontrol et.
2. Katalog girdilerini `prompts/` ve `skills/` altindaki gercek dosyalarla karsilastir; eksik katalog kayitlarini, eksik dosyalari ve ID uyumsuzluklarini tespit et.
3. `depends_on`, `source_blueprint` ve goreli markdown baglantilarini dogrula; kirik referanslari explicitly separate.
4. Paketlenmis skill klasorlerinde `SKILL.md` ve `meta.yaml` varligini kontrol et; metadata ve skill frontmatter eksiklerini not et.
5. Sonucu `errors`, `warnings`, `suggested fixes` ve `next step` basliklari altinda taranabilir bir rapor olarak sun.

## Output Expectations

- `errors`: Kirik katalog links, eksik dosyalar, ID mismatch'leri, kirik `depends_on`, kirik `source_blueprint` ve kirik goreli linkler.
- `warnings`: Eksik katalog girdileri, portability odakli metadata eksikleri veya yapisal olarak riskli ama calismayi immediately bozmayan durumlar.
- `suggested fixes`: Hangi katalog satirinin, metadata alaninin veya package dosyasinin how duzeltilmesi gerektigi.
- `next step`: Once uygulanmasi gereken en kritik maintenance adimi.

## Portability Notes

- This skill'in core validation logic provider-agnostiktir.
- Runtime'a specific execution form, command akisi veya otomasyon notlari adapter katmaninda tutulmalidir.
