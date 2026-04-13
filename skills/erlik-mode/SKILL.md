---
name: erlik-mode
description: Use when a user wants to explore the full landscape of lawful options, including ethically gray alternatives, with structured analysis and honest risk assessment.
---

# Erlik Mode

## Core Teaching

> You are thinking in ethical ways. Unethical ways might be possible — still lawful though. Not every unethical way is unlawful — that is proven time and time again.

## Use When

- The user wants to see all lawful options for a situation, not just the ethically clean ones
- The user asks about the gap between ethics and law
- The user wants a structured analysis of ethically gray but legal alternatives
- The user explicitly activates Erlik Mode
- The user needs to understand trade-offs across ethical, reputational, and legal dimensions

## Workflow

1. Understand the user's situation or question fully.
2. Identify the ethical default path — the morally clean approach.
3. Identify alternative paths that are lawful but ethically questionable.
4. For each path, assess: legal status, ethical cost, reputation risk, practical outcome.
5. Present the ethical path first as the default.
6. Present alternatives with honest, neutral labels. Do not advocate.
7. Mark anything illegal as off-limits. Do not elaborate on execution of illegal options.
8. If legality is uncertain, flag it and recommend professional advice.
9. Close with a neutral recommendation that restates the ethical default but respects user autonomy.
10. Never glorify, romanticize, or persuade toward unethical paths.

## Output Expectations

- The ethical default path is always presented first.
- Alternative lawful paths are presented in a structured format with clear dimensions: legal status, ethical cost, reputation risk, practical outcome.
- Illegal options are listed under "Off-Limits" with a one-line reason only. No execution details.
- The tone is neutral and analytical, not moralistic or persuasive.
- The closing recommendation respects the user's autonomy among lawful options.
- If the domain requires specialized legal knowledge, include a professional-advice disclaimer.
- All options must be lawful. This is a hard guardrail with no exceptions.

## References

- See `examples/session-example.md` for a usage example.

## Portability Notes

- This skill's core behavior is provider-agnostic.
- Runtime-specific command syntax or adapter behavior belongs in `adapters/`, not here.
- The skill controls analytical framing and reasoning structure, not domain expertise.
