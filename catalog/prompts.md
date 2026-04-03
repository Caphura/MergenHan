# Prompt Catalog

Bu katalog, repodaki aktif ve tarihsel prompt varliklarini insan-okunur bir indeks halinde listeler.

## Master Prompts

| ID | Baslik | Durum | Surum | Etiketler | Bagimliliklar | Yol |
| --- | --- | --- | --- | --- | --- | --- |
| `mh-master-prompt-library-orchestrator` | Prompt Library Orchestrator | `active` | `1.0.0` | `library`, `composition`, `repo-hygiene` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-collaborative-guidance`, `mh-module-no-sensitive-data`, `mh-module-action-summary` | [`prompts/masters/active/prompt-library-orchestrator.md`](../prompts/masters/active/prompt-library-orchestrator.md) |
| `mh-master-prompt-library-orchestrator-legacy` | Prompt Library Orchestrator Legacy | `archived` | `0.8.0` | `library`, `legacy`, `repo-hygiene` | `mh-module-context-audit`, `mh-module-action-summary` | [`prompts/masters/archived/prompt-library-orchestrator-legacy.md`](../prompts/masters/archived/prompt-library-orchestrator-legacy.md) |

## Modules

| ID | Baslik | Durum | Surum | Etiketler | Bagimliliklar | Yol |
| --- | --- | --- | --- | --- | --- | --- |
| `mh-module-context-audit` | Context Audit | `active` | `1.0.0` | `analysis`, `discovery`, `workflow` | `-` | [`prompts/modules/capability/context-audit.md`](../prompts/modules/capability/context-audit.md) |
| `mh-module-repo-architecture` | Repo Architecture | `active` | `1.0.0` | `documentation`, `repo-architecture`, `workflow` | `-` | [`prompts/modules/domain/repo-architecture.md`](../prompts/modules/domain/repo-architecture.md) |
| `mh-module-collaborative-guidance` | Collaborative Guidance | `active` | `1.0.0` | `collaboration`, `tone`, `guidance` | `-` | [`prompts/modules/tone/collaborative-guidance.md`](../prompts/modules/tone/collaborative-guidance.md) |
| `mh-module-no-sensitive-data` | No Sensitive Data | `active` | `1.0.0` | `safety`, `governance`, `privacy` | `-` | [`prompts/modules/constraints/no-sensitive-data.md`](../prompts/modules/constraints/no-sensitive-data.md) |
| `mh-module-action-summary` | Action Summary | `active` | `1.0.0` | `output-format`, `summary`, `readability` | `-` | [`prompts/modules/output/action-summary.md`](../prompts/modules/output/action-summary.md) |

## Skill Blueprints

| ID | Baslik | Durum | Surum | Etiketler | Bagimliliklar | Yol |
| --- | --- | --- | --- | --- | --- | --- |
| `mh-blueprint-prompt-library-curator` | Prompt Library Curator | `stable` | `1.0.0` | `packaging`, `documentation`, `governance` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-action-summary` | [`prompts/skill-blueprints/prompt-library-curator.md`](../prompts/skill-blueprints/prompt-library-curator.md) |
