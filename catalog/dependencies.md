# Dependency Catalog

This document summarizes dependency relationships between core assets. Adapter files are not treated as core dependencies in this catalog; they are compatibility-layer material.

Note: This catalog is generated with `python scripts/generate_catalog.py`.

## Ownership Notes

- Adapter mappings do not change core dependency ownership.
- Core IDs, blueprint sources, and the `depends_on` chain continue to be owned under `prompts/` and `skills/`.
- Adapters reference that core ownership; adding support for a new runtime does not create a new dependency owner in the core layer.

## Skills -> Blueprints

| Skill | Depends On | Notes |
| --- | --- | --- |
| `mh-skill-adapter-mapper` | `mh-blueprint-adapter-mapper` | Packaged skill keeps its source blueprint link |
| `mh-skill-apartment-investment-analyzer` | `mh-blueprint-apartment-investment-analyzer` | Packaged skill keeps its source blueprint link |
| `mh-skill-catalog-validator` | `mh-blueprint-catalog-validator` | Packaged skill keeps its source blueprint link |
| `mh-skill-feature-spec-composer` | `mh-blueprint-feature-spec-composer` | Packaged skill keeps its source blueprint link |
| `mh-skill-game-strategy-session-composer` | `mh-blueprint-game-strategy-session-composer` | Packaged skill keeps its source blueprint link |
| `mh-skill-meshy-3d-prompt-composer` | `mh-blueprint-meshy-3d-prompt-composer` | Packaged skill keeps its source blueprint link |
| `mh-skill-nano-banana-image-prompt-composer` | `mh-blueprint-nano-banana-image-prompt-composer` | Packaged skill keeps its source blueprint link |
| `mh-skill-onboarding-router` | `mh-blueprint-onboarding-router` | Packaged skill keeps its source blueprint link |
| `mh-skill-prompt-library-curator` | `mh-blueprint-prompt-library-curator` | Packaged skill keeps its source blueprint link |
| `mh-skill-real-estate-valuation-session-composer` | `mh-blueprint-real-estate-valuation-session-composer` | Packaged skill keeps its source blueprint link |
| `mh-skill-resume-composer` | `mh-blueprint-resume-composer` | Packaged skill keeps its source blueprint link |
| `mh-skill-skill-packager` | `mh-blueprint-skill-packager` | Packaged skill keeps its source blueprint link |
| `mh-skill-unity-6-developer` | `mh-blueprint-unity-6-developer` | Packaged skill keeps its source blueprint link |
| `mh-skill-used-car-scout` | `mh-blueprint-used-car-scout` | Packaged skill keeps its source blueprint link |

## Blueprints -> Masters / Modules / Blueprints

| Blueprint | Dependencies |
| --- | --- |
| `mh-blueprint-adapter-mapper` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-action-summary` |
| `mh-blueprint-apartment-investment-analyzer` | `mh-master-ultimate-real-estate-market-and-valuation-strategist-core`, `mh-module-real-estate-market-data-validation`, `mh-module-real-estate-comparable-analysis`, `mh-module-real-estate-valuation-logic`, `mh-module-real-estate-risk-and-uncertainty`, `mh-module-real-estate-investment-decision-support`, `mh-module-real-estate-no-hallucination-governance`, `mh-module-action-summary` |
| `mh-blueprint-catalog-validator` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-action-summary` |
| `mh-blueprint-feature-spec-composer` | `mh-module-context-audit`, `mh-module-collaborative-guidance`, `mh-module-action-summary` |
| `mh-blueprint-game-strategy-session-composer` | `mh-master-ultimate-game-development-strategist-core`, `mh-module-steam-market-validation`, `mh-module-mvp-scope-reduction`, `mh-module-production-risk-strategy`, `mh-module-full-concept-greenlight` |
| `mh-blueprint-meshy-3d-prompt-composer` | `mh-module-collaborative-guidance`, `mh-module-action-summary` |
| `mh-blueprint-nano-banana-image-prompt-composer` | `mh-master-nano-banana-image-prompt-composer`, `mh-module-collaborative-guidance`, `mh-module-action-summary` |
| `mh-blueprint-onboarding-router` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-collaborative-guidance`, `mh-module-action-summary` |
| `mh-blueprint-prompt-library-curator` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-action-summary` |
| `mh-blueprint-real-estate-valuation-session-composer` | `mh-master-ultimate-real-estate-market-and-valuation-strategist-core`, `mh-module-real-estate-market-data-validation`, `mh-module-real-estate-comparable-analysis`, `mh-module-real-estate-valuation-logic`, `mh-module-real-estate-risk-and-uncertainty`, `mh-module-real-estate-investment-decision-support`, `mh-module-real-estate-no-hallucination-governance` |
| `mh-blueprint-resume-composer` | `mh-module-context-audit`, `mh-module-collaborative-guidance`, `mh-module-action-summary` |
| `mh-blueprint-skill-packager` | `mh-blueprint-prompt-library-curator`, `mh-module-repo-architecture`, `mh-module-action-summary` |
| `mh-blueprint-unity-6-developer` | `mh-module-context-audit`, `mh-module-collaborative-guidance`, `mh-module-action-summary` |
| `mh-blueprint-used-car-listing-risk-filter` | `mh-module-used-car-tramer-verification`, `mh-module-used-car-listing-red-flags`, `mh-module-used-car-no-hallucination-governance`, `mh-module-collaborative-guidance`, `mh-module-action-summary` |
| `mh-blueprint-used-car-scout` | `mh-module-used-car-tramer-verification`, `mh-module-used-car-listing-red-flags`, `mh-module-used-car-pricing-logic`, `mh-module-used-car-no-hallucination-governance`, `mh-module-collaborative-guidance`, `mh-module-action-summary` |

## Masters -> Modules

| Master | Dependencies |
| --- | --- |
| `mh-master-nano-banana-image-prompt-composer` | `mh-module-collaborative-guidance`, `mh-module-action-summary` |
| `mh-master-prompt-library-orchestrator` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-collaborative-guidance`, `mh-module-no-sensitive-data`, `mh-module-action-summary` |
| `mh-master-ultimate-game-development-strategist-core` | `mh-module-steam-market-validation`, `mh-module-mvp-scope-reduction`, `mh-module-production-risk-strategy`, `mh-module-full-concept-greenlight` |
| `mh-master-ultimate-real-estate-market-and-valuation-strategist-core` | `mh-module-real-estate-market-data-validation`, `mh-module-real-estate-comparable-analysis`, `mh-module-real-estate-valuation-logic`, `mh-module-real-estate-risk-and-uncertainty`, `mh-module-real-estate-investment-decision-support`, `mh-module-real-estate-no-hallucination-governance` |
| `mh-master-prompt-library-orchestrator-legacy` | `mh-module-context-audit`, `mh-module-action-summary` |

## Modules

Modules are currently listed in the core catalog as independent support units; cataloged modules do not have a secondary `depends_on` relationship at this time.
