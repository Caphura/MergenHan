# Dogrulama Kurallari

Bu belge, repo butunlugunu korumak icin uygulanacak hafif dogrulama kontrollerini tanimlar.

## Katalog Kontrolleri

- Kirik katalog girdileri raporlanir.
- Katalogda listelenen dosya gercekte yoksa hata kabul edilir.
- Repoda bulunan ama katalogda yer almayan prompt veya skill dosyalari raporlanir.
- Katalog satirlarindaki ID ve yol uyumsuzluklari tespit edilir.

## Bagimlilik Kontrolleri

- `depends_on` alanindaki her ID repoda veya ilgili katalogda cozulmelidir.
- Kirik dependency referanslari raporlanir.
- Ayni varlik icin cift kayit veya duplicate ID bulunursa hata kabul edilir.
- Skill ile blueprint arasindaki `source_blueprint` baglantisi bozulmamalidir.
- Adapter mapping notlari cekirdek dependency sahipligini degistirmez.

## Metadata Kontrolleri

- Frontmatter veya `meta.yaml` icinde zorunlu alan eksigi raporlanir.
- `id`, `title`, `type`, `status`, `version` gibi temel alanlar bos veya gecersiz ise sorun sayilir.
- Paketlenmis skill klasorlerinde `SKILL.md` ve `meta.yaml` birlikte bulunmalidir.
- `SKILL.md` icindeki `name` ve `description` frontmatter alanlari dogrulanabilir.
- Yeni standartta kullanilan `portability`, `adapter_support`, `runtime_dependencies`, `tool_dependencies` alanlari eksikse uyari seviyesinde raporlanabilir.
- Bu portability uyari katmani ozellikle yeni blueprints, paketlenmis skill'ler ve aktif olarak evrilen ana cekirdek varliklar icin uygulanir.

## Link Kontrolleri

- Markdown icindeki goreli baglantilar cozulmelidir.
- Hedef dosya veya klasor yoksa kirik link olarak isaretlenir.
- Kataloglardan ve README'den verilen linkler ozellikle kontrol edilir.

## Kapsam

Asgari kontrol kapsamimiz sunlardir:

- `README.md`
- `catalog/*.md`
- `docs/*.md`
- `prompts/**/*.md`
- `skills/**/SKILL.md`
- `skills/**/meta.yaml`
- `adapters/**/*.md`

## Uygulama Notu

Bu kurallar agir CI veya harici paket bagimliligi gerektirmez. `scripts/validate_catalog.py`, `scripts/validate_metadata.py` ve `scripts/check_missing_links.py` bu kontrollerin hafif ve okunur uygulamalaridir.