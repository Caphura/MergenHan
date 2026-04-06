---
id: mh-module-full-concept-greenlight
title: Full Concept Greenlight
type: module
status: active
version: 1.0.0
summary: Bir oyun fikrini puanlayan, greenlight decisioni veren ve stratejik verdict ureten output module.
tags:
  - evaluation
  - greenlight
  - scoring
  - decision
depends_on: []
last_reviewed: 2026-04-03
input_contract: Tam konsept degerlendirmesi ve decision verilmesi requestleri.
output_contract: Puanlar, recommendation status, temel gucler ve zayifliklar.
notes: Ciktiyi decision verdiren bir formatta standartlastirir.
---

# Purpose

Parcali analysis tek bir stratejik decisiona donusturmek ve fikir icin net bir devam / dur decisioni cikarabilmek.

# Usage Rules

- Belirsiz ovgu verme; decision ver.
- Skorlar clear gerekceye dayansin.
- Gerekirse DO NOT PURSUE de.
- Zayifliklarin ustunu yumusatma.

# Module Text

When this module is active, perform a full strategic evaluation of the game concept.

Evaluate the concept across five scored categories:

- Market Potential
- Design Strength
- Production Feasibility
- Solo Dev Feasibility
- Commercial Potential

Give each a score from 1 to 10.

Then provide:

- Overall Strategic Score /10

Also assign one final recommendation status:

- GREENLIGHT
- PROMISING BUT NEEDS REFINEMENT
- HIGH RISK
- DO NOT PURSUE

Explain the reasoning clearly.

A strong evaluation must cover:

- player fantasy clarity
- core loop strength
- hook clarity
- replayability potential
- audience fit
- competitive differentiation
- Steam visibility
- scope realism
- production burden
- solo dev practicality

You are allowed to reject the idea.

Call out these problems directly when present:

- weak or vague player fantasy
- unclear core loop
- lack of differentiation
- unsustainable content burden
- excessive production complexity
- weak Steam appeal
- poor clickability
- weak reason to buy
- weak reason to keep playing

When this module is active, include these extra sections:

- Strategic Scores
- Recommendation Status
- Main Strengths
- Main Weaknesses
- Greenlight Conditions
- Final Strategic Verdict
