# Yazi ve Yapi Kurallari

Bu belge, prompt library icindeki dosyalarin nasil adlandirilacagini, hangi metadata alanlarini tasiyacagini ve ne zaman bir ust seviyeye terfi edecegini tanimlar.

## Adlandirma Kurallari

- Tum dosya ve klasor adlari `kebab-case` olur.
- Dosya adlari icerigin turunu ve amacini kisa bicimde anlatir.
- Kimlik deseni sabittir: `mh-<kind>-<slug>`
- `kind` yalnizca su degerlerden birini alir: `master`, `module`, `blueprint`, `skill`

## Prompt Dosyasi Frontmatter Kurali

`prompts/` altindaki tum prompt dosyalari ve `templates/` altindaki prompt sablonlari su alanlari tasir:

- `id`
- `title`
- `type`
- `status`
- `version`
- `summary`
- `tags`
- `depends_on`
- `last_reviewed`

Ihtiyaca gore su alanlar eklenebilir:

- `input_contract`
- `output_contract`
- `notes`

## Skill Paket Istisnasi

Paketlenmis skill klasorlerindeki `SKILL.md` dosyalari Codex uyumlulugu icin sade tutulur ve yalnizca skill frontmatter'i (`name`, `description`) tasir.

Skill'e ait yonetisim verileri su dosyada tutulur:

- `skills/<skill-slug>/meta.yaml`

Bu ayirim sayesinde:

- `SKILL.md` calisma talimatlarina odaklanir
- versiyon, durum, bagimlilik ve kaynak blueprint baglantisi kaybolmaz
- skill paketleri repo genelindeki yonetisim kurallariyla uyumlu kalir

## Durum Yasam Dongusu

Yalnizca asagidaki `status` degerleri kullanilir:

- `draft`: Ilk taslak, hizli degisebilir
- `active`: Guncel kullanimda
- `stable`: Siklikla tekrar kullanilan ve davranisi oturmus
- `deprecated`: Yerine daha iyi bir icerik gelmis, yeni kullanim icin onerilmez
- `archived`: Tarihsel referans olarak saklanan surum

## Klasor Kullanim Kurallari

### `prompts/masters/`

- `active/`: Guncel master promptlar
- `archived/`: Tarihsel surumler veya emekliye ayrilmis varyantlar

### `prompts/modules/`

Asagidaki alt klasorler sabittir:

- `capability/`
- `domain/`
- `tone/`
- `constraints/`
- `output/`

Yeni kategori eklemek yerine mevcut taksonomi icinde kalmaya oncelik verilir.

### `prompts/skill-blueprints/`

- Paketlenmeden once stabilize edilen skill promptlari burada tutulur.
- Buradaki icerik insan tarafindan okunur, tartisilir ve iyilestirilir.

### `skills/`

- Sadece olgunlasmis skill paketleri bulunur.
- Gecici notlar veya arka plan dokumanlari buraya dagitilmaz.
- Yardimci kaynaklar gerekiyorsa `references/`, `scripts/`, `assets/`, `agents/` altinda tutulur.

## Terfi Kurallari

Bir icerik `module` olarak ayrilmalidir eger:

- ayni davranis baska promptlarda da kullaniliyorsa
- tek bir goreve degil tekrar kullanima hizmet ediyorsa

Bir icerik `blueprint` olarak tutulmalidir eger:

- skill davranisi var ama paketleme kararina hazir degilse
- giris cikis kontrati oturmussa ama yardimci klasor ihtiyaci net degilse

Bir `blueprint` skill paketine terfi ettirilmelidir eger:

- tetikleyici kullanim sinyalleri belirginse
- gorev akisi sabitlendi ise
- gerekiyorsa referans veya asset ihtiyaci netlesmisse
- katalog ve meta kayitlari guncellenmeye hazirsa

## Katalog Bakim Kurali

- `prompts/` altina yeni dosya eklendiginde `catalog/prompts.md` guncellenir.
- `skills/` altina yeni paket eklendiginde `catalog/skills.md` guncellenir.
- Yeni etiket turetmeden once `catalog/taxonomy.md` kontrol edilir.
