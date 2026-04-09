# Taxonomy

This document defines the allowed tags and the folder-based meanings used throughout the repository. Before adding a new tag, check whether the idea can already be expressed through one of the groups listed here.

## Layers

| Layer | Meaning |
| --- | --- |
| `core` | Portable prompt, module, blueprint, skill, and catalog content |
| `adapter` | Runtime-specific mapping, command, and automation notes |
| `validation` | Repo integrity, metadata, and link validation utilities |

## Module Categories

| Folder | Purpose |
| --- | --- |
| `capability` | A behavior, reasoning step, or execution capability |
| `domain` | Domain knowledge, repo structure, business rules, or an expertise frame |
| `tone` | Voice, communication style, and collaboration style |
| `constraints` | Rules, boundaries, and safety conditions that must be enforced |
| `output` | Output format, reporting style, and presentation contract |

## Allowed Tags

| Tag | Meaning |
| --- | --- |
| `adapters` | Content about mapping a core asset into multiple runtimes or providers |
| `analysis` | Content centered on diagnosis, inspection, or context gathering |
| `apartment-analysis` | Content focused on comparing apartment listings, filtering them, and evaluating them from an investment perspective |
| `anti-hallucination` | Guardrail content that limits unsupported inferences and prevents false certainty |
| `automotive` | Content focused on the automotive domain, vehicle valuation, listing analysis, and the used-car market |
| `catalog` | Content related to repo indexes, lists, and generated reference catalogs |
| `collaboration` | Collaboration, companionship, and supportive communication |
| `commercial-viability` | Content that evaluates whether an idea is likely to be buyable or sellable in the market |
| `composition` | Combining modules or orchestrating them together |
| `comparables` | Content built around comparable data, similar examples, and comparison-based pricing logic |
| `confidence` | Content that makes the confidence level and uncertainty factor visible |
| `data-quality` | Content that identifies missing, weak, or inconsistent aspects of source data |
| `decision` | Content focused on choosing among alternatives or forming a final decision |
| `evaluation` | Content that evaluates an idea, asset, or decision against explicit criteria |
| `ethics` | Content focused on ethical reasoning, moral trade-offs, and the distinction between ethical and legal |
| `evidence` | Content focused on separating observation, source, or evidence from assumption |
| `feasibility` | Content focused on viability, source realism, and practical executability |
| `game-development` | Content that treats a game idea together with product, scope, market, and production reality |
| `discovery` | Researching and documenting the current state |
| `documentation` | Repo documents, explanatory prompts, and written standards |
| `decision-support` | Content that turns analysis into a buying, selling, choosing, or action decision |
| `feature-design` | Content focused on defining a specific game feature, formalizing it, and turning it into a spec |
| `game-design` | Content focused on game systems, mechanics, and player-experience design |
| `governance` | Versioning, status, lifecycle, and maintenance discipline |
| `greenlight` | Content that clarifies whether an idea or concept is worth continuing |
| `guidance` | Content that guides the user or helps clarify a decision |
| `image-generation` | Content for workflows that target image-generation models, image prompt design, or visual outputs |
| `legacy` | Content kept only for historical reference |
| `library` | Content related to the prompt library and its internal organization |
| `listing-analysis` | Content focused on listing review, red-flag detection, description analysis, and opportunity evaluation |
| `investment` | Content that supports decisions around return, payback, negotiation sensitivity, and purchase logic |
| `logic` | Content that makes the reasoning logic, rule flow, or decision structure explicit |
| `maintenance` | Content focused on ongoing repo maintenance, updates, and operational consistency |
| `mapping` | Mapping logic between core content and adapters or other representation layers |
| `market` | Content related to market structure, demand, positioning, or commercial context |
| `market-data` | Content built on market data, listing data, or outside quantitative context |
| `market-research` | Content focused on researching market conditions, comparable dynamics, or industry outlook |
| `mvp` | Content built around minimum viable product or first-version scope logic |
| `nano-banana` | Content for Nano Banana prompt design, guidance, and output preparation |
| `negotiation` | Content focused on negotiation space, concession points, and price flexibility |
| `output-format` | Output shape, report format, and presentation contract |
| `packaging` | Practices for turning a blueprint into a skill package |
| `portability` | The goal of preserving content portability across multiple runtimes |
| `positioning` | Content that creates a positioning or differentiation frame in a market or product context |
| `pricing` | Content focused on price ranges, pricing logic, or price interpretation |
| `prioritization` | Content that ranks what should be done first or kept in scope |
| `production` | Content focused on production process, implementation reality, or team capacity |
| `promotion` | Content focused on moving an asset to a higher maturity level |
| `prompt-composition` | Content that turns a raw idea or incomplete brief into a target-model-ready, copyable prompt |
| `privacy` | Protecting sensitive data and separating information appropriately |
| `readability` | The goal of clear, scannable, understandable writing |
| `real-estate` | Content focused on real estate, listings, market context, comparables, and valuation |
| `risk` | Content that makes danger, uncertainty, and loss scenarios visible |
| `routing` | Directing a request to the right asset type or workflow |
| `repo-architecture` | Foldering, repo skeleton, and file contracts |
| `repo-hygiene` | Cleanliness, consistency, and ease of maintenance |
| `safety` | Safe usage boundaries and harm reduction |
| `scope` | Content focused on scope boundaries, workload narrowing, or breadth control |
| `scoring` | Content that evaluates ideas, candidates, or options by scoring them |
| `session` | Content focused on session opening, session setup, or choosing the right analysis session |
| `solo-dev` | Content focused on the reality of solo or very small-team development |
| `steam` | Content related to the Steam ecosystem, player expectations, and market signals |
| `strategy` | Content focused on high-level choice, direction-setting, and commercial or product planning |
| `summary` | Short conclusions, next steps, or wrap-up formats |
| `tone` | Tone modules or voice character |
| `tramer` | Content focused on damage-record verification, inconsistency in Tramer amounts, and damage-history detection |
| `uncertainty` | Content that explains unknowns, data gaps, and decision uncertainty |
| `used-car` | Content focused on used-car buying and selling, market scanning, and vehicle evaluation |
| `valuation` | Content focused on building value ranges, pricing logic, and comparable-based price interpretation |
| `validation` | Checking catalog, metadata, link, or dependency consistency |
| `visual-direction` | Visual guidance content that clarifies scene, composition, lighting, style, and atmosphere |
| `workflow` | Content that supports a step-by-step workflow |

## Tagging Rule

- Every prompt carries at least 2 tags, ideally 3 to 5.
- Do not create new tags that duplicate an existing meaning.
- In skill metadata, preserve the primary tags that align with the source blueprint.
