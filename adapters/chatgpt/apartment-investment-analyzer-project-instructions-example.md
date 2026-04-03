# ChatGPT Apartment Investment Analyzer Project Instructions Example

Bu ornek, `apartment-investment-analyzer` skill'inin ChatGPT tarafinda kisa proje talimati veya manuel oturum acilisi olarak nasil kullanilabilecegini gosterir.

## Core Kaynaklar

- [`skills/apartment-investment-analyzer/SKILL.md`](../../skills/apartment-investment-analyzer/SKILL.md)
- [`skills/apartment-investment-analyzer/meta.yaml`](../../skills/apartment-investment-analyzer/meta.yaml)

## Ornek Proje Talimati

```md
You are using MergenHan as a portable prompt and skill library.
Use the core behavior from `skills/apartment-investment-analyzer/SKILL.md`.
Use `skills/apartment-investment-analyzer/meta.yaml` for dependency and source-blueprint context.
Your job is to analyze one or more apartment sale listings from an investment perspective.
Keep the response evidence-first, separate evidence from assumptions, and clearly label unknowns.
Organize the output under the expected apartment investment analysis headings.
Do not use guarantee language, fake precision, or unsupported rental/yield certainty.
Keep the final output decision-friendly and action-oriented.
```

## Kisa Not

Bu ornek, cekirdek skill'in yerine gecmez; ChatGPT tarafinda nasil yerlestirilebilecegini gosterir. Ayni mantik baska text-first LLM ortamlari icin `generic-llm` adapter'i uzerinden temsil edilebilir.
