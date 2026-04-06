# ChatGPT Nano Banana Project Instructions Example

This example `nano-banana-image-prompt-composer` skill'inin ChatGPT side short proje talimati veya manual session acilisi olarak how kullanilabilecegini shows.

## Core Sources

- [`skills/nano-banana-image-prompt-composer/SKILL.md`](../../skills/nano-banana-image-prompt-composer/SKILL.md)
- [`skills/nano-banana-image-prompt-composer/meta.yaml`](../../skills/nano-banana-image-prompt-composer/meta.yaml)

## Example Project Instructions

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

## Short Note

This example does not replace the core skill; ChatGPT side how yerlestirilebilecegini shows. Gemini benzeri benzer text-first ortamlarda da same mantik `generic-llm` adapter'i uzerinden temsil edilebilir.
