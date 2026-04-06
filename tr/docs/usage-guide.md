# Herhangi Bir AI'da MergenHan Nasil Kullanilir

Bu belge, MergenHan kutuphanesindeki skill, master prompt, blueprint ve modulleri herhangi bir AI ortaminda nasil kullanacaginizi adim adim aciklar.

## Dil ve Kaynak Notu

- Repo kokundeki `README.md` canonical English kaynaktir.
- Turkce kullanim aynasi `tr/README.md` ve `tr/docs/` altinda bulunur.
- `scripts/` locale-aware olarak hem EN hem TR katalog ve dogrulama akisini destekler.

## Temel Fikir

MergenHan, portable core content ile runtime-specific adapter notlarini birbirinden ayirir.

Tipik akis soyledir:

1. En dogru ve en kucuk cekirdek varligi sec.
2. Bu cekirdek varligi AI'ya ver.
3. Gorevini, girdilerini ve kisitlarini ekle.
4. Runtime-specific davranisi cekirdek varligin icine degil, adapter katmanina koy.

## Dogru Varlikla Basla

| Ihtiyacin buysa | Bunu kullan | Neden |
| --- | --- | --- |
| Tekrarlanabilir ve sinirli bir gorev | `skills/` | Dogrudan tekrar kullanim icin paketlenmistir |
| Daha genis, orkestre bir is akisi | `prompts/masters/` | Bir gorev ailesi icin birden fazla modulu birlestirir |
| Paketleme oncesi workflow taslagi | `prompts/skill-blueprints/` | Paketlenmis skill henuz yoksa ise yarar |
| Yeniden kullanilabilir davranis parcasi | `prompts/modules/` | Baska varliklari birlestirmek veya genisletmek icin en uygunudur |

Emin degilsen `onboarding-router` ile basla.

## Evrensel Kullanim Akisi

1. `catalog/skills.md` veya `prompts/` altinda en yakin varligi bul.
2. AI'ya cekirdek kaynagi ver:
   - repo-aware AI: dosya yolunu referans ver
   - instruction-based AI: varlik icerigini instructions alanina yapistir
   - plain chat AI: sadece minimum gerekli varligi sohbete yapistir
3. Gorevini, kaynak materyalini ve kisitlarini ekle.
4. Gerekiyorsa opsiyonel baglam ekle:
   - skill: `meta.yaml`
   - master: `depends_on` ve `Assembly Map`
   - blueprint: input/output contract ve notlar
5. AI'ya workflow'u sirayla takip etmesini ve eksik bilgileri uydurmak yerine raporlamasini soyle.
6. Runtime ozel komut, arac veya izin ihtiyaci varsa `adapters/` altindaki ilgili notlari kullan.

## En Hizli Kopyala-Yapistir Sablonu

AI repo dosyalarini dogrudan goremiyorsa bunu kullan:

```md
You are using the MergenHan library.

Core source:
- skills/resume-composer/SKILL.md

Optional context:
- skills/resume-composer/meta.yaml

Task:
- Draft an ATS-friendly resume from the notes below.

Rules:
- Follow the core workflow in order.
- Keep runtime-specific assumptions out of the core skill.
- If information is missing, say so instead of inventing it.

Expected output:
- Candidate Summary
- Resume Draft
- Weak Spots / Missing Inputs
```

## Hangi Skill Bana Uygun?

`catalog/skills.md` dosyasina bak. Mevcut paketlenmis beceriler:

| Ihtiyac | Skill |
| --- | --- |
| CV / resume yazmak | `resume-composer` |
| Gorsel prompt olusturmak | `nano-banana-image-prompt-composer` |
| 3D asset promptu yazmak | `meshy-3d-prompt-composer` |
| Oyun fikirlerini stratejik degerlendirmek | `game-strategy-session-composer` |
| Oyun ozelligi spec'i yazmak | `feature-spec-composer` |
| Gayrimenkul degerlemesi | `real-estate-valuation-session-composer` |
| Daire yatirim analizi | `apartment-investment-analyzer` |
| Kutuphane bakimi | `prompt-library-curator` |
| Blueprint'ten skill'e terfi | `skill-packager` |
| Dogru varliga yonlendirme | `onboarding-router` |
| Adapter esleme | `adapter-mapper` |
| Katalog dogrulama | `catalog-validator` |

Emin degilsen `onboarding-router` ile basla.

Not: `archived` durumundaki skill'ler katalogda tarihsel referans olarak kalabilir, fakat yeni kullanimlarda tercih edilmemelidir.

## Platforma Gore Yapistirma

### ChatGPT

`SKILL.md` icerigini project instructions veya Custom GPT'nin Instructions alanina koy.

Ornek proje talimati:

```md
You are using MergenHan as a portable prompt and skill library.
Use the core behavior from `skills/resume-composer/SKILL.md`.
Use `skills/resume-composer/meta.yaml` for dependency and source-blueprint context.
Do not invent ChatGPT-specific runtime rules inside the core skill.
If a request is ChatGPT-specific, keep that adaptation in the adapter layer only.
```

Daha fazla ayrinti icin: [`adapters/chatgpt/project-instructions-example.md`](../adapters/chatgpt/project-instructions-example.md)

### Claude Code

Claude Code repo-aware calistigi icin skill dosyalarini dogrudan gorebilir. Oturumda ilgili dosyayi referans vermek yeterlidir:

```text
This repository is the MergenHan prompt library.
Use the core behavior from `skills/resume-composer/SKILL.md`.
```

Daha fazla ayrinti icin: [`adapters/claude-code/README.md`](../adapters/claude-code/README.md) ve [`adapters/claude-code/settings.example.json`](../adapters/claude-code/settings.example.json)

### Codex

Cekirdek skill'i task packet olarak tanimla:

```md
Objective: Draft an ATS-friendly resume using the MergenHan resume-composer skill.
Core source: skills/resume-composer/SKILL.md
Working set:
- skills/resume-composer/SKILL.md
- skills/resume-composer/meta.yaml
Constraints:
- Follow the skill's workflow steps exactly
- Keep output in English unless instructed otherwise
Expected output:
- Candidate Summary
- Resume Draft
- Weak Spots / Missing Inputs
```

Daha fazla ayrinti icin: [`adapters/codex/task-packet-example.md`](../adapters/codex/task-packet-example.md)

### Herhangi Bir LLM (Minimum Yol)

1. `SKILL.md` icerigini oturuma yapistir.
2. Gerekiyorsa `meta.yaml` bilgisini kisaca ozetle.
3. Asagidaki gibi basit bir talimat ekle:

```text
Use the core behavior from MergenHan's `resume-composer` skill.
Follow the workflow steps in order.
Keep runtime-specific assumptions out of the core recommendation.
```

Bu en dusuk ortak payda yontemidir. Ozel arac, hook veya izin varsayimi yapmaz.

Daha fazla ayrinti icin: [`adapters/generic-llm/minimal-usage-example.md`](../adapters/generic-llm/minimal-usage-example.md)

## Master Prompt Kullanimi

Master prompt'lar, birden fazla modulu birlestiren orkestrasyon dosyalaridir. Skill'lerden farkli olarak daha genis kapsamli gorevler icindir.

Ornegin prompt kutuphanesini duzenlemek icin:

```text
prompts/masters/active/prompt-library-orchestrator.md
```

Kullanim: master prompt icerigini AI'ya yapistir. Modullerin davranisi prompt icindeki `Assembly Map` bolumunde zaten aciklanir.

## Blueprint Kullanimi

Blueprint'ler paketleme oncesi stabilize olmus workflow taslaklaridir. Paketlenmis bir skill henuz yoksa kullanilabilirler, ancak paketlenmis skill'lere gore daha hizli degisebilirler.

Blueprint kullanirken:

1. Once blueprint'in kendisini yapistir.
2. Gorevi etkiliyorsa `depends_on`, contract ve notes alanlarini gorunur tut.
3. `skills/` altina terfi etmedigi surece onu tamamen donmus bir paket gibi dusunme.

## Modul Kullanimi

Moduller yeniden kullanilabilir destek parcalaridir. Genelde tek basina yapistirilmazlar; daha cok yeni bir master prompt olustururken veya mevcut bir workflow'u uyarlarken kullanilirlar.

Tipik modul rolleri:

- capability behavior
- domain knowledge
- tone guidance
- constraints
- output formatting

## Session Composer Farki

`game-strategy-session-composer` ve `real-estate-valuation-session-composer` gibi skill'ler tam analizi kendileri yapmaz. Once dogru analiz oturumunu secer, sonra baska bir AI oturumuna tasiyabilecegin kopyala-yapistir bir acilis mesaji uretir.

## Ornek Senaryo: CV Yazmak

1. `skills/resume-composer/SKILL.md` dosyasini ac ve kopyala.
2. AI oturumuna yapistir.
3. Ham kariyer notlarini, mevcut CV metnini veya ekran goruntulerini ver.
4. AI workflow'u takip ederek yapilandirilmis bir CV taslagi uretir.

Beklenen cikti yapisi:

- Candidate Summary
- Target Role Fit (istege bagli)
- Resume Draft (ATS-friendly)
- Weak Spots / Missing Inputs
- Optional Tailoring Notes (is ilani varsa)

## Ornek Senaryo: Oyun Fikrini Degerlendirmek

1. `skills/game-strategy-session-composer/SKILL.md` dosyasini ac ve kopyala.
2. AI oturumuna yapistir ve oyun fikrini anlat.
3. Skill dogru analiz oturumunu secer:
   - Steam potansiyeli: `Core + Steam Market Validation`
   - MVP daraltma: `Core + MVP Scope Reduction`
   - Uretim riski: `Core + Production Risk Strategy`
   - Tam degerlendirme: hepsini birlestirir
4. Sana baska bir AI oturumuna tasiyabilecegin kopyala-yapistir bir acilis mesaji verir.

## Ornek Senaryo: Gorsel Prompt Olusturmak

1. `skills/nano-banana-image-prompt-composer/SKILL.md` dosyasini ac ve kopyala.
2. AI oturumuna yapistir ve nasil bir sahne istedigini anlat.
3. Skill 2-4 netlestirici soru sorar.
4. Sonra dogrudan kopyalanabilir bir Nano Banana promptu uretir.

## Temel Kurallar

- Runtime-specific syntax'i cekirdek katmana koyma; provider-specific notlari `adapters/` altinda tut.
- Skill workflow adimlarini sirayla takip et.
- `resume-composer` ve real-estate skill seti gibi varliklar unsupported claim uretmeyi acikca yasaklar.
- Kullanici acikca gorsel veya dosya istemedikce varsayilan cikti metin tabanlidir.

## Ileri Duzey: Yeni Icerik Eklemek

Bu rehber mevcut kutuphane varliklarini kullanmaya odaklanir. Yeni prompt, modul veya skill eklemek istiyorsan:

- Hizli baslangic: README icindeki "30-Second Start" bolumu
- Detayli kurallar: [`docs/conventions.md`](conventions.md)
- Birlestirme ve terfi akisi: [`docs/composition-guide.md`](composition-guide.md)
- Skill paket spesifikasyonu: [`docs/skill-package-spec.md`](skill-package-spec.md)
