# Kullanim Rehberi

Bu belge, MergenHan kutuphanesindeki skill, master prompt ve modulleri herhangi bir AI ortaminda nasil kullanacaginizi adim adim aciklar.

## Temel Fikir

MergenHan'daki her `SKILL.md` dosyasi, bir AI'ya "bu gorevi su adimlarla, su kurallara gore yap" diyen hazir bir talimat setidir. Hangi AI kullanirsan kullan, ayni cekirdek talimati yapistirirsin; sadece yapistirma sekli degisir.

## Hangi Skill Bana Uygun?

`catalog/skills.md` dosyasina bak. Mevcut paketlenmis beceriler:

| Ihtiyac | Skill |
| --- | --- |
| CV / Resume yazmak | `resume-composer` |
| Gorsel prompt olusturmak | `nano-banana-image-prompt-composer` |
| 3D model promptu yazmak | `meshy-3d-prompt-composer` |
| Oyun fikrini stratejik degerlendirmek | `game-strategy-session-composer` |
| Oyun ozelligi spec'i yazmak | `feature-spec-composer` |
| Gayrimenkul degerlemesi | `real-estate-valuation-session-composer` |
| Daire yatirim analizi | `apartment-investment-analyzer` |
| Kutuphane bakimi | `prompt-library-curator` |
| Blueprint'ten skill'e terfi degerlendirmesi | `skill-packager` |
| Dogru aksiyona yonlendirme | `onboarding-router` |
| Adapter esleme | `adapter-mapper` |
| Katalog dogrulama | `catalog-validator` |

Emin degilsen `onboarding-router` ile basla; talebini dogru katmana yonlendirir.

## Uc Adimda Kullanim

1. `catalog/skills.md` dosyasindan ihtiyacina uyan skill'i bul.
2. `skills/<skill-adi>/SKILL.md` icerigini kopyala.
3. Kullandigin AI ortamina yapistir ve gorevini ver.

Her skill paketi en az iki dosya tasir:

- `SKILL.md`: cekirdek calisma talimati (AI'ya verilen icerik)
- `meta.yaml`: bagimlilik, versiyon ve kaynak blueprint bilgisi (opsiyonel baglam)

## Platforma Gore Yapistirma

### ChatGPT

SKILL.md icerigini proje talimatlarina (Project Instructions) veya Custom GPT'nin Instructions alanina koy.

Ornek proje talimati:

```md
You are using MergenHan as a portable prompt and skill library.
Use the core behavior from `skills/resume-composer/SKILL.md`.
Use `skills/resume-composer/meta.yaml` for dependency and source-blueprint context.
Do not invent ChatGPT-specific runtime rules inside the core skill.
If a request is ChatGPT-specific, keep that adaptation in the adapter layer only.
```

Daha fazla ayrint icin: [`adapters/chatgpt/project-instructions-example.md`](../adapters/chatgpt/project-instructions-example.md)

### Claude Code

Claude Code repo-aware calistigi icin skill dosyalarini dogrudan gorebilir. Oturumda ilgili dosyayi referans vermek yeterlidir:

```text
Bu repo MergenHan prompt kutuphanesidir.
skills/resume-composer/SKILL.md dosyasindaki cekirdek davranisi kullan.
```

Adapter katmanina ait ayar ornegi: [`adapters/claude-code/settings.example.json`](../adapters/claude-code/settings.example.json)

Daha fazla ayrint icin: [`adapters/claude-code/README.md`](../adapters/claude-code/README.md)

### Codex

Cekirdek skill'i gorev paketi (task packet) olarak tanimla:

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

Daha fazla ayrint icin: [`adapters/codex/task-packet-example.md`](../adapters/codex/task-packet-example.md)

### Herhangi Bir LLM (Minimum Yol)

1. `SKILL.md` icerigini kopyala.
2. Oturuma yapistir.
3. Asagidaki gibi basit bir istem ekle:

```text
Use the core behavior from MergenHan's `resume-composer` skill.
Follow the workflow steps in order.
Keep runtime-specific assumptions out of the core recommendation.
```

Bu en dusuk ortak payda yontemidir; ozel arac, hook veya izin varsayimi yapmaz.

Daha fazla ayrint icin: [`adapters/generic-llm/minimal-usage-example.md`](../adapters/generic-llm/minimal-usage-example.md)

## Ornek Senaryo: CV Yazmak

1. `skills/resume-composer/SKILL.md` dosyasini ac ve icerigini kopyala.
2. AI oturumuna yapistir.
3. Ham kariyer notlarini, mevcut CV metnini veya ekran goruntusunu ver.
4. AI, skill'deki workflow adimlarini izleyerek sana yapilardirmis bir CV taslagi uretir.

Beklenen cikti yapisi:

- Candidate Summary
- Target Role Fit (istege bagli)
- Resume Draft (ATS-friendly)
- Weak Spots / Missing Inputs
- Optional Tailoring Notes (is ilani varsa)

## Ornek Senaryo: Oyun Fikrini Degerlendirmek

1. `skills/game-strategy-session-composer/SKILL.md` dosyasini ac ve icerigini kopyala.
2. AI oturumuna yapistir ve oyun fikrini anlat.
3. Skill dogru analiz oturumunu secer:
   - Steam potansiyeli: `Core + Steam Market Validation`
   - MVP daraltma: `Core + MVP Scope Reduction`
   - Uretim riski: `Core + Production Risk Strategy`
   - Tam degerlendirme: tumunu birlestirir
4. Sana copy-paste session opening verir; bunu yeni bir AI oturumuna yapistirirsin.

## Ornek Senaryo: Gorsel Prompt Olusturmak

1. `skills/nano-banana-image-prompt-composer/SKILL.md` dosyasini ac ve icerigini kopyala.
2. AI oturumuna yapistir ve "soyle bir sahne istiyorum" de.
3. Skill sana 2-4 netlestirici soru sorar.
4. Sonra dogrudan kopyalanabilir Nano Banana promptu uretir.

## Master Prompt Kullanimi

Master promptlar, birden fazla modulu birlestiren orkestrasyon dosyalaridir. Skill'lerden farkli olarak daha genis kapsamli gorevler icindir.

Ornegin prompt kutuphanesini duzenlemek icin:

```text
prompts/masters/active/prompt-library-orchestrator.md
```

Kullanim: master prompt icerigini AI'ya yapistir. Modullerin davranisi zaten prompt metninde acik Assembly Map ile gosterilir.

## Session Composer Farki

`game-strategy-session-composer` ve `real-estate-valuation-session-composer` gibi skill'ler analizi kendileri yapmaz. Once dogru analiz oturumunu secer, sonra sana kopyala-yapistir bir acilis mesaji uretir. Bu mesaji baska bir AI oturumuna tasirsiin.

## Temel Kurallar

- Cekirdek icerigi runtime'a ozel syntax ile kirletme; provider'a ozel notlari `adapters/` altinda tut.
- Skill'deki workflow adimlarini sirayla izle.
- Ozellikle `resume-composer` ve `real-estate` skill'leri kanitsiz bilgi eklemeyi yasaklar.
- Varsayilan cikti metin tabanlidir; kullanici acikca istemedikce gorsel veya dosya uretme.

## Ileri Duzey: Yeni Icerik Eklemek

Bu rehber mevcut skill'lerin kullanimina odaklanir. Yeni prompt, modul veya skill eklemek icin:

- Hizli baslangic: bu README'deki "30 Saniyelik Baslangic" bolumu
- Detayli kurallar: [`docs/conventions.md`](conventions.md)
- Birlestirme ve terfi akisi: [`docs/composition-guide.md`](composition-guide.md)
- Skill paket spesifikasyonu: [`docs/skill-package-spec.md`](skill-package-spec.md)
