# MergenHan Prompt Library

MergenHan, tasinabilir bir AI prompt ve skill kutuphanesi olarak tasarlanmis; okunur, bakimi kolay ve buyumeye dayanikli bir calisma alanidir. Cekirdek icerik tek bir saglayiciya kilitlenmez; Claude Code, ChatGPT, Codex ve genel LLM ortamlari icin uyarlamalar `adapters/` katmaninda tutulur.

## Bu Repo Ne Icin Var?

- Master promptlari tek seferlik notlar yerine surumlenebilir varliklar gibi yonetmek
- Tekrar kullanilabilir modulleri ayirip farkli akislarda birlestirmek
- Olgunlasan skill taslaklarini tasinabilir skill paketlerine donusturmek
- Ayni cekirdek icerigi farkli AI calisma ortamlarina adapterler uzerinden eslemek
- Katalog, taksonomi ve orneklerle birikimi kaybolmadan buyutmek

## Repo Haritasi

```text
.
|-- adapters/
|   |-- claude-code/
|   |-- chatgpt/
|   |-- codex/
|   `-- generic-llm/
|-- catalog/
|   |-- dependencies.md
|   |-- prompts.md
|   |-- skills.md
|   `-- taxonomy.md
|-- docs/
|   |-- adapter-model.md
|   |-- composition-guide.md
|   |-- conventions.md
|   |-- lifecycle.md
|   |-- orchestration-rules.md
|   |-- skill-package-spec.md
|   `-- validation-rules.md
|-- examples/
|   `-- compositions/
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
|-- scripts/
|-- skills/
`-- templates/
    `-- skill-package/
```

## 30 Saniyelik Baslangic

En kisa yol:

1. Ihtiyaciniza en yakin sablonu `templates/` altindan kopyalayin.
2. Sadece zorunlu metadata alanlarini doldurun.
3. Dosyayi `prompts/` altinda dogru yere koyun.
4. Kataloglari yeniden uretin: `python scripts/generate_catalog.py`
5. Dogrulama betiklerini calistirin.

Ilk eklemede yeterli olan zorunlu prompt alanlari:

- `id`
- `title`
- `type`
- `status`
- `version`
- `summary`
- `tags`
- `depends_on`
- `last_reviewed`

`input_contract`, `output_contract`, `notes`, `portability`, `adapter_support`, `runtime_dependencies` ve `tool_dependencies` gibi alanlar ihtiyac oldukca eklenir.

## Hizli Baslangic

1. Yeni bir icerik baslatmak icin uygun sablonu `templates/` altindan kopyalayin.
2. Icerigi once `prompts/` altinda dogru kategoriye yerlestirin.
3. Yeni etiket uretiyorsaniz `catalog/taxonomy.md` ile hizalayin.
4. Kataloglari elle duzenlemek yerine `python scripts/generate_catalog.py` calistirin.
5. Skill davranisi stabil hale geldiginde `prompts/skill-blueprints/` altindaki taslagi `skills/<skill-slug>/` altina terfi ettirin.
6. Runtime'a ozel notlar gerekiyorsa cekirdek icerigi degistirmek yerine ilgili adapter altinda mapping belgesi ekleyin.

## Nereden Baslamaliyim?

Okuma sirasini kisa tutmak isterseniz:

1. Bu README
2. Bir ornek prompt: [`prompts/masters/active/prompt-library-orchestrator.md`](prompts/masters/active/prompt-library-orchestrator.md)
3. Gerekirse kurallar: [`docs/conventions.md`](docs/conventions.md)

Derine inmek isterseniz:

- Tekrar kullanilabilir bir modul ornegi: [`prompts/modules/capability/context-audit.md`](prompts/modules/capability/context-audit.md)
- Paketlenmemis skill taslagi: [`prompts/skill-blueprints/prompt-library-curator.md`](prompts/skill-blueprints/prompt-library-curator.md)
- Paketlenmis skill ornegi: [`skills/prompt-library-curator/SKILL.md`](skills/prompt-library-curator/SKILL.md)
- Adapter modeli: [`docs/adapter-model.md`](docs/adapter-model.md)
- Yasam dongusu: [`docs/lifecycle.md`](docs/lifecycle.md)
- Birlestirme ve terfi akisi: [`docs/composition-guide.md`](docs/composition-guide.md)

## Yeni Bir AI Ortaminda Baslangic

1. Once cekirdek kaynagi secin: tekrar kullanilabilir davranis icin `skills/`, paketleme oncesi davranis icin `prompts/skill-blueprints/`, gorev orkestrasyonu icin `prompts/masters/`.
2. Sonra uygun adapteri secin: runtime'a ozel kullanim notlari `adapters/` altinda yer alir.
3. Yeni bir ortam ekleyecekseniz `adapters/<runtime>/` altinda en az bir `README.md` ve `mapping.md` olusturun; gerekiyorsa ornek dosya veya istege bagli ayar ornegi ekleyin.
4. Core kimlikleri, bagimlilik sahipligini ve workflow mantigini adaptere tasimayin; adapter yalnizca calistirma bicimini aciklar.

Pratik adapter ornekleri:

- Claude Code ayar ornegi: [`adapters/claude-code/settings.example.json`](adapters/claude-code/settings.example.json)
- ChatGPT proje talimati ornegi: [`adapters/chatgpt/project-instructions-example.md`](adapters/chatgpt/project-instructions-example.md)
- Codex gorev paketi ornegi: [`adapters/codex/task-packet-example.md`](adapters/codex/task-packet-example.md)
- Generic LLM minimum kullanim ornegi: [`adapters/generic-llm/minimal-usage-example.md`](adapters/generic-llm/minimal-usage-example.md)

## Icerik Tipleri

- `master`: Birden fazla modulun belirli bir gorev icin birlestirilmis surumu
- `module`: Tekrar kullanilabilir davranis, kisit, ton veya cikti parcasi
- `blueprint`: Paketlenmeden once stabilize edilen skill taslagi
- `skill`: Adapterler tarafindan farkli runtimelara eslenebilen paketlenmis beceri
- `adapter`: Cekirdek icerigi belirli bir runtime'in komut, arac ve izin modeline uyarlayan katman

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

### 4. Skill'ten Adapter'e

- Cekirdek prompt, blueprint ve skill tanimlari `prompts/` ile `skills/` altinda korunur.
- Runtime'a ozel slash command, hook, tool, permission veya agent wiring detaylari `adapters/` altina tasinir.
- Ayni skill birden fazla adapter tarafindan desteklenebilir.

## Repo Prensipleri

- Dosya ve klasor adlari her zaman `kebab-case` olur.
- Ana dokumantasyon Turkce yazilir.
- Prompt icerikleri YAML frontmatter ile surumlenir.
- Gizli anahtar, musteri verisi ve paylasilmamasi gereken varyantlar repoya girmez.
- Okunabilirlik ve manuel bakim once gelir; otomasyon yalnizca hafif uretim ve dogrulama scriptleriyle sinirli tutulur.
- Cekirdek icerik tek bir saglayicinin syntax veya runtime varsayimlarina baglanmaz.

## Ilk Ornek Akislar

- Modulden master prompta gecis: [`examples/compositions/module-to-master.md`](examples/compositions/module-to-master.md)
- Blueprint'ten skill paketine gecis: [`examples/compositions/blueprint-to-skill.md`](examples/compositions/blueprint-to-skill.md)

## Hafif Bakim ve Dogrulama

Kataloglari yeniden uretmek ve repo butunlugunu kontrol etmek icin `scripts/` altinda bagimsizliksiz yardimci betikler bulunur:

- `python scripts/generate_catalog.py`
- `python scripts/validate_catalog.py`
- `python scripts/validate_metadata.py`
- `python scripts/check_missing_links.py`

Onerilen akis:

1. Icerigi ekleyin veya guncelleyin.
2. `python scripts/generate_catalog.py` calistirin.
3. Diger betiklerle katalog, metadata ve link tutarliligini kontrol edin.

Bu betikler CI zorunlulugu getirmez; repo bakimini hizlandirmak ve manuel hatalari azaltmak icin kullanilir.
