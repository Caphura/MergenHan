# MergenHan Prompt Library

MergenHan, master prompt ve moduler skill promptlarini tek bir yerde okunur, bakimi kolay ve buyumeye dayanikli bicimde saklamak icin kurulmus aktif bir calisma alanidir.

## Bu Repo Ne Icin Var?

- Master promptlari tek seferlik notlar yerine surumlenebilir varliklar gibi yonetmek
- Tekrar kullanilabilir modulleri ayirip farkli akislarda birlestirmek
- Olgunlasan skill taslaklarini Codex-uyumlu paketlere donusturmek
- Katalog, taksonomi ve orneklerle birikimi kaybolmadan buyutmek

## Repo Haritasi

```text
.
|-- prompts/
|   |-- masters/
|   |   |-- active/
|   |   `-- archived/
|   |-- modules/
|   |   |-- capability/
|   |   |-- constraints/
|   |   |-- domain/
|   |   |-- output/
|   |   `-- tone/
|   `-- skill-blueprints/
|-- skills/
|-- templates/
|   `-- skill-package/
|-- catalog/
|-- docs/
`-- examples/
    `-- compositions/
```

## Hizli Baslangic

1. Yeni bir icerik baslatmak icin uygun sablonu `templates/` altindan kopyalayin.
2. Icerigi once `prompts/` altinda dogru kategoriye yerlestirin.
3. `catalog/prompts.md` veya `catalog/skills.md` icine yeni girdiyi ekleyin.
4. Gerekirse bagli modulleri ve etiketleri `catalog/taxonomy.md` ile hizalayin.
5. Skill davranisi stabil hale geldiginde `prompts/skill-blueprints/` altindaki taslagi `skills/<skill-slug>/` altina terfi ettirin.

## Nereden Baslamaliyim?

- Guncel bir master prompt ornegi: [`prompts/masters/active/prompt-library-orchestrator.md`](prompts/masters/active/prompt-library-orchestrator.md)
- Tekrar kullanilabilir bir modul ornegi: [`prompts/modules/capability/context-audit.md`](prompts/modules/capability/context-audit.md)
- Paketlenmemis skill taslagi: [`prompts/skill-blueprints/prompt-library-curator.md`](prompts/skill-blueprints/prompt-library-curator.md)
- Paketlenmis skill ornegi: [`skills/prompt-library-curator/SKILL.md`](skills/prompt-library-curator/SKILL.md)
- Repo kurallari: [`docs/conventions.md`](docs/conventions.md)
- Birlestirme ve terfi akisi: [`docs/composition-guide.md`](docs/composition-guide.md)

## Icerik Tipleri

- `master`: Birden fazla modulun belirli bir gorev icin birlestirilmis surumu
- `module`: Tekrar kullanilabilir davranis, kisit, ton veya cikti parcasi
- `blueprint`: Paketlenmeden once stabilize edilen skill taslagi
- `skill`: Codex tarafinda kullanilabilecek paketlenmis beceri

## Calisma Akisi

### 1. Fikirden Prompta

- Yeni fikirler once sablonla baslar.
- Tekrar kullanilabilir parcalar `prompts/modules/` altina ayrilir.
- Tam gorev akislari `prompts/masters/active/` altinda tutulur.

### 2. Prompttan Blueprint'e

- Moduler skill davranisi netlesince icerik `prompts/skill-blueprints/` altina tasinir.
- Giris ve cikis kontrati belirginlesmeden paketleme yapilmaz.

### 3. Blueprint'ten Skill'e

- Paketlenmis skill icin sade bir `SKILL.md` yazilir.
- Yonetisim metadatasi `meta.yaml` icinde tutulur.
- Gerekirse `references/`, `scripts/`, `assets/` gibi yardimci klasorler eklenir.

## Repo Prensipleri

- Dosya ve klasor adlari her zaman `kebab-case` olur.
- Ana dokumantasyon Turkce yazilir.
- Prompt icerikleri YAML frontmatter ile surumlenir.
- Gizli anahtar, musteri verisi ve paylasilmamasi gereken varyantlar repoya girmez.
- V1 kapsaminda otomasyon yoktur; okunabilirlik ve manuel bakim once gelir.

## Ilk Ornek Akislar

- Modulden master prompta gecis: [`examples/compositions/module-to-master.md`](examples/compositions/module-to-master.md)
- Blueprint'ten skill paketine gecis: [`examples/compositions/blueprint-to-skill.md`](examples/compositions/blueprint-to-skill.md)
