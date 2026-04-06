# Codex Meshy 3D Prompt Composer Task Packet Example

This example `meshy-3d-prompt-composer` skill'inin Codex side repo-aware task package olarak how kullanilabilecegini shows.

## Core Sources

- [`skills/meshy-3d-prompt-composer/SKILL.md`](../../skills/meshy-3d-prompt-composer/SKILL.md)
- [`skills/meshy-3d-prompt-composer/meta.yaml`](../../skills/meshy-3d-prompt-composer/meta.yaml)
- [`skills/meshy-3d-prompt-composer/examples/session-example.md`](../../skills/meshy-3d-prompt-composer/examples/session-example.md)
- [`examples/compositions/meshy-3d-prompt-composer-tests.md`](../../examples/compositions/meshy-3d-prompt-composer-tests.md)

## Example Task Packet

```md
Objective: Help the user turn a rough 3D asset idea into a clean Meshy prompt using the core `meshy-3d-prompt-composer` skill.
Core source:
- `skills/meshy-3d-prompt-composer/SKILL.md`
- `skills/meshy-3d-prompt-composer/meta.yaml`
Working set:
- `skills/meshy-3d-prompt-composer/examples/session-example.md`
- `examples/compositions/meshy-3d-prompt-composer-tests.md`
Constraints:
- If the request is underdefined, ask one short round of 2-3 high-impact clarification questions before writing the final prompt.
- If the request is already specific or the user explicitly asks for a direct prompt, respond with the final prompt in the same reply.
- Keep the `Meshy Prompt` text within the 800-chvehicleter limit.
- Stay text-only by default; do not claim unverifiable topology, UV, or engine-readiness guarantees.
Expected output:
- Asset Summary
- Meshy Prompt
- Production Notes if needed
- Optional Variations if they materially help
```

## Short Note

Codex'e specific task packaging dili bu adapter dosyasinda remains; core davranis ve 800 karakter guardrail'i skill paketinden gelir.
