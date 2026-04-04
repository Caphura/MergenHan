# Codex Resume Composer Task Packet Example

Bu ornek, `resume-composer` skill'inin Codex tarafinda repo-aware gorev paketi olarak nasil kullanilabilecegini gosterir.

## Core Kaynaklar

- [`skills/resume-composer/SKILL.md`](../../skills/resume-composer/SKILL.md)
- [`skills/resume-composer/meta.yaml`](../../skills/resume-composer/meta.yaml)
- [`skills/resume-composer/examples/session-example.md`](../../skills/resume-composer/examples/session-example.md)
- [`examples/compositions/resume-composer-tests.md`](../../examples/compositions/resume-composer-tests.md)

## Ornek Gorev Paketi

```md
Objective: Help the user turn an existing resume, raw career notes, or hybrid input into an ATS-friendly English resume using the core `resume-composer` skill.
Core source:
- `skills/resume-composer/SKILL.md`
- `skills/resume-composer/meta.yaml`
Working set:
- `skills/resume-composer/examples/session-example.md`
- `examples/compositions/resume-composer-tests.md`
Constraints:
- First triage whether the input is an existing resume, raw notes, or a hybrid.
- If critical information is missing, ask only one short round of 2-4 high-impact clarification questions.
- If a job post is present, tailor the resume to supported keywords and responsibilities without keyword spam.
- Stay evidence-only; do not invent metrics, dates, titles, ownership, or technologies.
- Default final draft language to English unless the user explicitly asks for another language.
Expected output:
- Candidate Summary
- Target Role Fit if applicable
- Resume Draft
- Weak Spots / Missing Inputs
- Optional Tailoring Notes if they materially help
```

## Kisa Not

Codex'e ozel gorev paketleme dili bu adapter dosyasinda kalir; cekirdek workflow, EN-first varsayimi ve no-fabrication guardrail'i skill paketinden gelir.