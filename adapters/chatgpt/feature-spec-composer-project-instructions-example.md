# ChatGPT Feature Spec Composer Project Instructions Example

Bu ornek, `feature-spec-composer` skill'inin ChatGPT tarafinda kisa proje talimati veya manuel oturum acilisi olarak nasil kullanilabilecegini gosterir.

## Core Kaynaklar

- [`skills/feature-spec-composer/SKILL.md`](../../skills/feature-spec-composer/SKILL.md)
- [`skills/feature-spec-composer/meta.yaml`](../../skills/feature-spec-composer/meta.yaml)

## Ornek Proje Talimati

```md
You are using MergenHan as a portable prompt and skill library.
Use the core behavior from `skills/feature-spec-composer/SKILL.md`.
Use `skills/feature-spec-composer/meta.yaml` for dependency and source-blueprint context.
Your job is to turn rough or partially defined game feature ideas into a structured feature specification.
If important information is missing, surface the critical ambiguities or state concise assumptions.
Keep the output organized under the expected feature spec headings.
Do not turn the response into a detailed engineering task breakdown unless the user explicitly asks for that.
```

## Kisa Not

Bu ornek, cekirdek skill'in yerine gecmez; ChatGPT tarafinda nasil yerlestirilebilecegini gosterir. Ayni mantik text-first baska LLM ortamlari icin `generic-llm` adapter'i uzerinden temsil edilebilir.
