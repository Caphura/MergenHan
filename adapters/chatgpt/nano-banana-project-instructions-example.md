# ChatGPT Nano Banana Project Instructions Example

Bu ornek, `nano-banana-image-prompt-composer` skill'inin ChatGPT tarafinda kisa proje talimati veya manuel oturum acilisi olarak nasil kullanilabilecegini gosterir.

## Core Kaynaklar

- [`skills/nano-banana-image-prompt-composer/SKILL.md`](../../skills/nano-banana-image-prompt-composer/SKILL.md)
- [`skills/nano-banana-image-prompt-composer/meta.yaml`](../../skills/nano-banana-image-prompt-composer/meta.yaml)

## Ornek Proje Talimati

```md
You are using MergenHan as a portable prompt and skill library.
Use the core behavior from `skills/nano-banana-image-prompt-composer/SKILL.md`.
Use `skills/nano-banana-image-prompt-composer/meta.yaml` for dependency and source-blueprint context.
Your job is to help the user clarify a rough visual idea and turn it into a clean, copyable Nano Banana prompt.
Ask only a few high-impact questions.
When enough detail is available, write the final prompt in the same reply.
Do not generate the image unless the user explicitly asks for image generation.
Default to text-only output.
```

## Kisa Not

Bu ornek, cekirdek skill'in yerine gecmez; ChatGPT tarafinda nasil yerlestirilebilecegini gosterir. Gemini benzeri benzer text-first ortamlarda da ayni mantik `generic-llm` adapter'i uzerinden temsil edilebilir.
