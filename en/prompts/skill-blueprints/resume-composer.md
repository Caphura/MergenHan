---
id: mh-blueprint-resume-composer
title: Resume Composer
type: blueprint
status: stable
version: 1.1.0
summary: A stabilized blueprint that reads existing resumes, raw career notes, and inspectable evidence, opens at most one short clarification round when needed, and produces ATS-friendly, evidence-only, role-aware English resume outputs, including one-page and export-review modes.
tags:
  - positioning
  - guidance
  - workflow
  - readability
  - evidence
  - validation
depends_on:
  - mh-module-context-audit
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-04-04
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: The user provides an existing resume or CV, raw career notes, screenshots, public sources, local artifacts, and optionally a job post, and wants a stronger ATS-friendly evidence-only resume draft, a one-page version, or an export review.
output_contract: At most one short clarification round when needed, followed by Candidate Summary, Target Role Fit when a job post exists, ATS-friendly Resume Draft, Weak Spots / Missing Inputs, and Optional Tailoring Notes when useful. Findings-first review mode is also supported.
notes: Default output is EN-first. When a job post exists, tailoring becomes active; otherwise the blueprint builds a domain-appropriate baseline. It never invents metrics, titles, dates, ownership, degrees, or technologies. Inspectable evidence is used before asking questions, and exported artifacts are audited separately.
---

# Responsibility

Turn existing resumes, messy career notes, or inspectable evidence packs into an ATS-friendly but human-readable, evidence-only, role-aware resume output.

# Trigger Signals

- "Fix my CV / resume."
- "Tailor my resume for this role."
- "Turn my raw career notes into a strong resume."
- "Make these bullets stronger, but do not invent information."
- "I want a better resume for ATS."
- "Rebuild the resume from this PDF / these screenshots."
- "Compress this into a one-page final CV."
- "Review this exported CV and find what is broken."

# Workflow

1. Triage the input: decide whether it is an existing resume, raw career notes, an inspectable evidence pack, or a hybrid. Also separate whether the user wants a draft, section rewrite, one-page final, tailoring, or export review.
2. If the user provided inspectable material, inspect it first: screenshots, PDF exports, repo READMEs, local documents, public profile or article links, earlier drafts. Do not ask unnecessary questions when the evidence is already visible.
3. Apply evidence tiering: `user-asserted`, `screenshot-or-document-verified`, `local-artifact-verified`, `public-source-verified`, `inferred`. Preserve that difference when hardening final copy; do not write uncertain claims as verified.
4. Identify the critical gaps that affect outcome quality: target role, seniority, title progression, concrete achievements, metrics, date ranges, ownership, technical stack, domain positioning, and education certainty.
5. If the input is still critically incomplete, open at most one short clarification round with 2-4 high-impact questions. Do not turn this into a long questionnaire, and do not ask for information that can already be extracted from inspectable evidence.
6. Perform evidence-only bullet rewriting: preserve action, ownership, and outcome logic while strengthening vague language without inventing metrics, degrees, titles, technologies, or ownership.
7. Choose domain-appropriate positioning: game, technical, product, operations, research, or another relevant baseline. Do not force the user into a generic white-collar profile.
8. Draft ATS-friendly sections: Candidate Summary, core strengths or skills, experience bullets, and education or certification structure when relevant.
9. If a job post exists, tailor only toward supported keywords and responsibilities. Do not keyword-spam and do not force unsupported equivalence.
10. If the user asks for a one-page final, keep the strongest signals up front, trim repetition, preserve stacked-role progression, and produce copy that truly fits a one-page target.
11. If the user asks for export review, run a findings-first audit for placeholder contact info, unsupported degree claims, generic filler, merged lines, ATS-breaking layout copy issues, and evidence drift.
12. Return the result in this shape: Candidate Summary, Target Role Fit when a job post exists, Resume Draft, Weak Spots / Missing Inputs, and Optional Tailoring Notes when helpful. In review mode, list findings first and add direction for correction if useful.
13. Default the final output to English unless the user explicitly asks for another language. Clarification questions may still adapt to the user's language when helpful.
14. Even if the user pushes for stronger positioning, do not invent achievements, degrees, titles, or metrics. Mark unclear or missing areas explicitly.

# Output Expectations

- The default Resume Draft should use a concise, ATS-friendly, professional tone.
- Final bullets should be outcome-, impact-, and ownership-oriented rather than reading like task lists.
- If a job post exists, tailoring should be visible; otherwise keep a domain-appropriate baseline.
- Candidate Summary should stay short, positioning-focused, and free of slogan-like filler.
- Target Role Fit should appear only when a job post or clear target role exists.
- Weak Spots / Missing Inputs should surface real gaps, weak metrics, unclear ownership, or low-confidence claims.
- Keyword optimization must not degrade readability into keyword spam.
- If the user wants only one section, do not expand scope unnecessarily, while still preserving the default full-draft logic where appropriate.
- For technical, game, builder, or project-led profiles, do not dilute the strongest proof signals with generic corporate filler.
- One-page mode should trim repetition and secondary detail while keeping the copy truly short and scannable.
- Export-review mode should treat placeholder address or phone data, unsupported degrees, merged lines, and drifting claims as red flags.

# Failure Patterns To Avoid

- Leaving placeholder address, phone number, or dummy contact information in the final output
- Converting ambiguous education signals into verified degree claims
- Inflating team labels, showcase placement, or photo visibility into unsupported official titles or employment claims
- Flattening technical or game-oriented profiles into generic corporate summaries
- Losing stacked-role progression or crushing multiple roles into one line
- Missing merged-copy or layout artifacts caused by Canva or PDF export

# Promotion Criteria

- Produces consistent results across scenarios such as existing resume + job post, raw notes without a job post, and incomplete evidence
- Makes meaningful progress with at most one short clarification round
- Keeps the no-fabrication guardrail reliable across runtimes
- Cleanly separates job-post-guided tailoring mode from general baseline mode
- Can reconstruct resume content from mixed evidence such as screenshots, public sources, and local artifacts
- Preserves the strongest signals in one-page compression mode without losing brevity
- Catches placeholder, unsupported-claim, and merged-copy problems in export-review mode
- Remains easy to carry into other runtimes through skill packages and adapter examples
