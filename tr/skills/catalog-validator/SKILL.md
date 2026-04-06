---
name: catalog-validator
description: Use when validating repository catalogs, metadata, links, and dependency integrity across MergenHan.
---

# Catalog Validator

## Use When

- Repo kataloglarinin guncel ve tutarli kalip kalmadigi kontrol edilecekse
- `catalog/`, `prompts/` ve `skills/` arasindaki baglar dogrulanacaksa
- Duplicate ID, kirik bagimlilik veya eksik paket dosyasi gibi butunluk sorunlari aranacaksa

## Workflow

1. `catalog/` altindaki indeks dosyalarini incele ve listelenen yollarin gercekte var olup olmadigini kontrol et.
2. Katalog girdilerini `prompts/` ve `skills/` altindaki gercek dosyalarla karsilastir; eksik katalog kayitlarini, eksik dosyalari ve ID uyumsuzluklarini tespit et.
3. `depends_on`, `source_blueprint` ve goreli markdown baglantilarini dogrula; kirik referanslari acikca ayristir.
4. Paketlenmis skill klasorlerinde `SKILL.md` ve `meta.yaml` varligini kontrol et; metadata ve skill frontmatter eksiklerini not et.
5. Sonucu `errors`, `warnings`, `suggested fixes` ve `next step` basliklari altinda taranabilir bir rapor olarak sun.

## Output Expectations

- `errors`: Kirik katalog baglantilari, eksik dosyalar, ID mismatch'leri, kirik `depends_on`, kirik `source_blueprint` ve kirik goreli linkler.
- `warnings`: Eksik katalog girdileri, portability odakli metadata eksikleri veya yapisal olarak riskli ama calismayi hemen bozmayan durumlar.
- `suggested fixes`: Hangi katalog satirinin, metadata alaninin veya paket dosyasinin nasil duzeltilmesi gerektigi.
- `next step`: Once uygulanmasi gereken en kritik bakim adimi.

## Portability Notes

- Bu skill'in cekirdek dogrulama mantigi provider-agnostiktir.
- Runtime'a ozel calistirma sekli, komut akisi veya otomasyon notlari adapter katmaninda tutulmalidir.
