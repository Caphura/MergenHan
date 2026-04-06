# ChatGPT Project Instructions Example

This example core bir skill'in ChatGPT proje talimatlarina how tasinabilecegini shows. Example olarak `prompt-library-curator` kullanilir; asil davranis core dosyalarda remains.

## Core Sources

- [`skills/prompt-library-curator/SKILL.md`](../../skills/prompt-library-curator/SKILL.md)
- [`skills/prompt-library-curator/meta.yaml`](../../skills/prompt-library-curator/meta.yaml)

## Example Project Instructions

```md
You are using MergenHan as a portable prompt and skill library.
Use the core behavior from `skills/prompt-library-curator/SKILL.md`.
Use `skills/prompt-library-curator/meta.yaml` for dependency and source-blueprint context.
Do not invent ChatGPT-specific runtime rules inside the core skill.
If a request is ChatGPT-specific, keep that adaptation in the adapter layer only.
When organizing repository content, preserve IDs, titles, and dependency chains unless a real inconsistency is found.
```

## Short Note

This adapter example cekirdegin yerine gecmez; only ChatGPT side how yerlestirilecegini shows.