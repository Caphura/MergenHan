# ChatGPT Project Instructions Example

Bu ornek, cekirdek bir skill'in ChatGPT proje talimatlarina nasil tasinabilecegini gosterir. Ornek olarak `prompt-library-curator` kullanilir; asil davranis cekirdek dosyalarda kalir.

## Core Kaynaklar

- [`skills/prompt-library-curator/SKILL.md`](../../skills/prompt-library-curator/SKILL.md)
- [`skills/prompt-library-curator/meta.yaml`](../../skills/prompt-library-curator/meta.yaml)

## Ornek Proje Talimati

```md
You are using MergenHan as a portable prompt and skill library.
Use the core behavior from `skills/prompt-library-curator/SKILL.md`.
Use `skills/prompt-library-curator/meta.yaml` for dependency and source-blueprint context.
Do not invent ChatGPT-specific runtime rules inside the core skill.
If a request is ChatGPT-specific, keep that adaptation in the adapter layer only.
When organizing repository content, preserve IDs, titles, and dependency chains unless a real inconsistency is found.
```

## Kisa Not

Bu adapter ornegi, cekirdegin yerine gecmez; yalnizca ChatGPT tarafinda nasil yerlestirilecegini gosterir.