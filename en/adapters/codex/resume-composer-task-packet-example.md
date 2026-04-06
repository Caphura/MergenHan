# Codex Resume Composer Task Packet Example

This example `resume-composer` skill'inin Codex side repo-aware task package olarak how kullanilabilecegini shows.

## Core Sources

- [`skills/resume-composer/SKILL.md`](../../skills/resume-composer/SKILL.md)
- [`skills/resume-composer/meta.yaml`](../../skills/resume-composer/meta.yaml)
- [`skills/resume-composer/examples/session-example.md`](../../skills/resume-composer/examples/session-example.md)
- [`examples/compositions/resume-composer-tests.md`](../../examples/compositions/resume-composer-tests.md)

## Example Task Packet

```md
Objective: Help the user turn an existing resume, raw career notes, or inspectable evidence pack into an ATS-friendly English resume using the core `resume-composer` skill.
Core source:
- `skills/resume-composer/SKILL.md`
- `skills/resume-composer/meta.yaml`
Working set:
- `skills/resume-composer/examples/session-example.md`
- `examples/compositions/resume-composer-tests.md`
Constraints:
- First triage whether the input is an existing resume, raw notes, inspectable evidence, or a hybrid.
- If screenshots, PDFs, repos, local docs, or public links are provided, inspect them before asking clarification questions.
- If critical information is still missing, ask only one short round of 2-4 high-impact clarification questions.
- If a job post is present, tailor the resume to supported keywords and responsibilities without keyword spam.
- Stay evidence-only; do not invent metrics, dates, titles, ownership, degrees, or technologies.
- Preserve evidence tiers when certainty matters, and do not harden weak signals into verified claims.
- Support one-page final-copy mode by compressing to the strongest signals without flattening role progression.
- In export-review mode, audit Canva / PDF copy for placeholders, merged lines, unsupported claims, and generic filler.
- Default final draft language to English unless the user explicitly asks for another language.
Expected output:
- Candidate Summary
- Target Role Fit if applicable
- Resume Draft
- Weak Spots / Missing Inputs
- Optional Tailoring Notes if they materially help
```

## Short Note

Codex'e specific task packaging dili bu adapter dosyasinda remains; core workflow, EN-first assumptioni, evidence-onceligi ve no-fabrication guardrail'i skill paketinden gelir.
