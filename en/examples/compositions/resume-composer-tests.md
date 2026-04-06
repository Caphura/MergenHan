# Resume Composer Test Pack

This document collects test scenarios that can be used across different AI environments for `Resume Composer`. The goal is not only to check whether the model can write a nice-looking resume, but whether it can turn existing resumes, raw notes, and inspectable evidence into evidence-only, ATS-friendly, and role-aware output.

## Usage

Before each test, use the opening instruction below:

```text
Turn the resume / CV, career notes, or inspectable evidence below into an ATS-friendly resume draft. Do not jump into a long final draft immediately. First determine whether the input is an existing resume, raw notes, inspectable evidence, a job-post-supported tailoring request, or an export review. If screenshots, PDFs, repos, local documents, or public links are already provided, inspect them first. If critical gaps still remain, ask at most one short round of 2-4 high-impact questions. Then return the result in this shape:

1. Candidate Summary
2. Target Role Fit
3. Resume Draft
4. Weak Spots / Missing Inputs
5. Optional Tailoring Notes

Default the final output to English. Do not invent metrics, titles, dates, degrees, or ownership.
```

## Test Scenarios

### RC1 - Existing Resume + Job Post Tailoring

**Goal:** Can the model read existing resume notes and tailor them against a job post?

### RC2 - Build from Raw Career Notes

**Goal:** Can the model build a meaningful resume skeleton from scattered notes?

### RC3 - Missing Data and One Short Clarification Round

**Goal:** Can the model ask only one short, high-impact clarification round when critical information is missing?

### RC4 - Resistance to Invented Metrics

**Goal:** Does the model refuse to invent metrics, ownership, or unsupported achievements even when the user asks for stronger language?

### RC5 - Rewrite a Long Paragraph into Strong Bullets

**Goal:** Can the model turn messy experience prose into scannable bullets with action, ownership, and outcome logic?

### RC6 - No Job Post, General ATS Baseline

**Goal:** Can the model produce a strong baseline resume without pretending job-post-specific tailoring?

### RC7 - EN-First Behavior

**Goal:** Does the model keep the final resume in English while allowing clarification in the user's language when helpful?

### RC8 - Screenshot + Public Evidence + Local Artifact Reconstruction

**Goal:** Can the model reconstruct a resume from mixed evidence without inventing claims?

### RC9 - One-Page Compression Discipline

**Goal:** Can the model keep only the strongest signals while preserving role progression in a real one-page version?

### RC10 - Export QA / Placeholder Audit

**Goal:** Can the model run a findings-first audit on an exported resume and catch placeholders, unsupported claims, merged lines, and ATS readability issues?

## Suggested Order

1. `RC2`
2. `RC1`
3. `RC3`
4. `RC5`
5. `RC4`
6. `RC6`
7. `RC7`
8. `RC8`
9. `RC9`
10. `RC10`

## Scoring Rubric

| Criterion | What to Look For |
| --- | --- |
| Input Triage | Can it separate existing resume, raw notes, inspectable evidence, hybrid, and review modes correctly? |
| Clarification Discipline | Does it ask only one short, high-impact clarification round when needed? |
| Evidence Discipline | Does it avoid inventing metrics, titles, dates, degrees, or ownership? |
| Evidence Intake | Can it use inspectable inputs such as screenshots, PDFs, repos, and public sources? |
| ATS Clarity | Does the draft remain ATS-friendly and readable? |
| Tailoring Quality | If there is a job post, is alignment visible without keyword spam? |
| Compression Quality | In one-page mode, does it trim repetition while preserving role progression? |
| Export QA | Does it catch placeholders, unsupported claims, and merged-copy problems? |
| Output Readability | Are Candidate Summary, Resume Draft, and the other sections scannable? |
| EN-first Behavior | Is the default final output English? |
