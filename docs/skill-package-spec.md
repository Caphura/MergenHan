# Skill Paket Spesifikasyonu

Bu belge, MergenHan icindeki skill paketleri icin resmi klasor ve metadata standardini tanimlar.

## Paket Amaci

Bir skill paketi:

- cekirdek workflow'u tekrar kullanilabilir hale getirir
- blueprint kokenini korur
- runtime'a ozel davranisi cekirdege gommeden farkli adapterlerce eslenebilir kalir

## Asgari Paket Yapisi

```text
skills/<skill-slug>/
|-- SKILL.md
`-- meta.yaml
```

Ihtiyaca gore asagidaki klasorler eklenebilir:

- `references/`
- `examples/`
- `assets/`
- `scripts/`
- `agents/`

Bu klasorler yalnizca gercek ihtiyac oldugunda eklenir; her skill'e zorunlu degildir.

## `SKILL.md` Zorunlu Alanlari

`SKILL.md` icinde su frontmatter alanlari zorunludur:

- `name`
- `description`

Belge govdesinde asgari olarak su bolumler beklenir:

- `# <Skill Title>`
- `## Use When`
- `## Workflow`
- `## Output Expectations`

Ihtiyaca gore su bolumler eklenebilir:

- `## References`
- `## Portability Notes`
- adaptere degil cekirdege ait diger kullanim notlari

`SKILL.md` cekirdek skill tanimidir; provider-specific davranis burada yasamaz.

## `meta.yaml` Zorunlu Alanlari

Her skill paketinde `meta.yaml` su alanlari tasimalidir:

- `id`
- `title`
- `type`
- `status`
- `version`
- `summary`
- `tags`
- `depends_on`
- `last_reviewed`
- `source_blueprint`
- `input_contract`
- `output_contract`

Asagidaki alanlar guclu bicimde onerilir ve yeni paketlerde standart kabul edilir:

- `portability`
- `adapter_support`
- `runtime_dependencies`
- `tool_dependencies`
- `notes`

## Destek Klasorleri

### `references/`

- Kontrol listeleri, arka plan notlari ve uzun aciklamalar burada tutulur.
- Cekirdek skill'i sisirmeden yardimci bilgi saglar.

### `examples/`

- Beklenen kullanim ornekleri veya mini senaryolar tutulur.
- Ozellikle onboarding ve kalite kontrol icin yararlidir.

### `assets/`

- Gorsel, sablon, sabit veri veya baska tasinabilir kaynaklar burada tutulur.
- Platforma ozel gecici dosyalar icin kullanilmaz.

### `scripts/`

- Hafif otomasyonlar, donusum araclari veya kontrol yardimcilari burada tutulur.
- Agir bagimliliklardan kacinilir.

## Blueprint'ten Skill'e Terfi Kriterleri

Bir blueprint skill paketine terfi etmeye hazir kabul edilir eger:

- tetikleyici kullanim sinyalleri tekrar eden bir kalip olusturuyorsa
- workflow maddeler halinde aciklanabiliyorsa
- giris ve cikis kontrati netlesmisse
- gerekli yardimci klasor ihtiyaci belli ise
- katalog ve bagimlilik kayitlari guncellenmeye hazirsa
- cekirdek davranis tek bir provider veya runtime syntax'ina bagli degilse

## Tasinabilirlik Kurallari

- Cekirdek skill tanimi her zaman provider-agnostik kalir.
- Ayni skill birden fazla adapter mapping'i tarafindan temsil edilebilir.
- `portability: universal` veya benzeri isaretler cekirdek niyeti gosterir; runtime gerceklemesi adapterler tarafindan yapilir.
- `runtime_dependencies` ve `tool_dependencies` alani varsa, bunlar cekirdek skill'in calisabilmesi icin gerekli genel kosullari aciklar; provider'a ozel komut listesi yazmak icin kullanilmaz.

## Provider-Specific Davranis Kurali

Provider-specific davranis cekirdek skill taniminda yasamaz.

Asagidaki icerikler `SKILL.md` veya cekirdek `meta.yaml` icine konmamalidir:

- belirli bir runtime'a ait slash command isimleri
- hook tanimlari
- permission policy detaylari
- agent wiring veya tool secim syntax'i

Bu bilgiler `adapters/<runtime>/mapping.md` veya ilgili adapter README'sinde tutulur.
