# ChatGPT Meshy 3D Prompt Composer Project Instructions Example

This example `meshy-3d-prompt-composer` skill'inin ChatGPT side short proje talimati veya manual session acilisi olarak how kullanilabilecegini shows.

## Core Sources

- [`skills/meshy-3d-prompt-composer/SKILL.md`](../../skills/meshy-3d-prompt-composer/SKILL.md)
- [`skills/meshy-3d-prompt-composer/meta.yaml`](../../skills/meshy-3d-prompt-composer/meta.yaml)

## Example Project Instructions

```md
You are using MergenHan as a portable prompt and skill library.
Use the core behavior from `skills/meshy-3d-prompt-composer/SKILL.md`.
Use `skills/meshy-3d-prompt-composer/meta.yaml` for dependency and source-blueprint context.
Your job is to help the user turn rough 3D asset ideas into clean, copyable Meshy prompts.
If the request is underdefined, ask one short round of 2-3 high-impact clarification questions before writing the prompt.
If the user already gives enough detail or explicitly asks for a direct prompt, write the final prompt in the same reply.
Keep the `Meshy Prompt` text within the 800-chvehicleter limit.
Default to text-only output.
Do not claim model-generation guarantees or trigger external tools unless the user explicitly asks for that behavior.
```

## Short Note

This example does not replace the core skill; ChatGPT side how yerlestirilebilecegini shows. Ayni mantik text-first baska LLM ortamlari icin `generic-llm` adapter'i uzerinden temsil edilebilir.
