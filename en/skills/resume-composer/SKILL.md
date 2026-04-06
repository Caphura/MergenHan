---
name: resume-composer
description: Use when a user wants an ATS-friendly English resume drafted, reconstructed, compressed, reviewed, or tailored from resumes, raw notes, screenshots, public evidence, local artifacts, and optionally a job post.
---

# Resume Composer

## Use When

- The user wants to strengthen an existing resume or CV and make it more ATS-friendly
- The user wants an English resume drafted from raw career notes
- The user wants a resume reconstructed from screenshots, PDFs, repos, profile links, or mixed evidence
- Resume tailoring is requested against a specific job post
- Bullets need to be rewritten to emphasize outcome, impact, and ownership
- A final one-page version or export review is requested
- The profile needs game, technical, research, builder, or project-led positioning instead of a generic white-collar baseline

## Workflow

1. Separate whether the input is an existing resume, raw notes, an inspectable evidence pack, or a hybrid. Also determine whether the request is for a draft, one-page final, section rewrite, tailoring, or export review.
2. Inspect the materials the user already provided first: screenshots, PDFs, repo READMEs, local documents, profile links, public sources, and earlier drafts. If visible evidence already exists, do not ask unnecessary clarification questions.
3. Tier the evidence: `user-asserted`, `screenshot-or-document-verified`, `local-artifact-verified`, `public-source-verified`, `inferred`. Only harden supported claims in final copy, and preserve provenance differences when certainty matters.
4. Identify critical gaps: target role, seniority, title progression, concrete achievements, metrics, date boundaries, ownership, technical stack, domain positioning, and education certainty.
5. If clarification is truly necessary, ask at most one short round of 2-4 high-impact questions. When inspectable evidence exists, prefer extracting maximum value from it before asking.
6. Do evidence-only bullet rewriting. Strengthen vague language, but do not invent metrics, degrees, titles, technologies, or ownership.
7. Build domain-appropriate positioning: game, technical, product, operations, research, and so on. Do not force the user into a default generic white-collar baseline.
8. Draft ATS-friendly sections and apply tailoring when a job post exists at the level of supported keywords and responsibilities.
9. If the user wants a final one-page version, compress to the strongest signals, remove repetition, preserve role progression, and keep the copy truly scannable.
10. If the user wants export review, audit for placeholder contact info, unsupported degree claims, generic filler, merged lines, ATS-breaking layout copy issues, and evidence drift.
11. Return the result under this structure: Candidate Summary, Target Role Fit when applicable, Resume Draft, Weak Spots / Missing Inputs, and Optional Tailoring Notes when helpful. In review mode, behave findings-first.
12. Default the final draft to English unless the user explicitly requests another language.

## Output Expectations

- Resume Draft should use a concise ATS-friendly professional tone.
- Final bullets should reflect action, ownership, and outcomes.
- Do not invent metrics, titles, dates, technologies, or ownership.
- If a job post exists, tailoring should be visible; otherwise keep a strong domain-aware baseline.
- For builder, designer, engineer, or project-led profiles, do not collapse the profile into a generic corporate summary.
- One-page mode should remove repetition, keep the strongest proof signals visible, and preserve ATS readability.
- Export-review mode should treat placeholder address or phone data, unsupported degrees, merged lines, and fake strengthening as red flags.
- Weak Spots / Missing Inputs should show real missing information clearly.
- ATS optimization must not become keyword spam.

## Failure Patterns To Avoid

- Leaving placeholder address, phone number, or dummy contact information in the final draft
- Turning ambiguous education signals into verified degree claims
- Inflating team labels, showcase placement, or photo visibility into unsupported official titles or employment claims
- Flattening technical or game-oriented profiles into a generic corporate summary
- Losing stacked-role progression or compressing roles into a single line
- Missing merged-copy or layout artifacts caused by Canva or PDF export

## References

- See `examples/session-example.md` for a short session example.

## Portability Notes

- This skill's core behavior is provider-agnostic.
- Runtime-specific document export, formatting, or editor automation should be documented in `adapters/`.
- The default task is to produce a plain-text or markdown English resume draft; design-tool integration is not part of the core behavior.
