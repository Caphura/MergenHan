# Dependency Catalog

Bu belge, cekirdek varliklar arasindaki bagimlilik iliskilerini ozetler. Adapter dosyalari bu katalogda cekirdek bagimlilik olarak sayilmaz; onlar uyumluluk katmanidir.

## Sahiplik Notu

- Adapter mapping'leri cekirdek dependency sahipligini degistirmez.
- Cekirdek ID'ler, blueprint kaynaklari ve `depends_on` zinciri `prompts/` ile `skills/` altinda sahiplenilmeye devam eder.
- Adapterler bu cekirdek sahipligi referans alir; yeni runtime destegi eklemek cekirdekte yeni bagimlilik sahibi yaratmaz.

## Skills -> Blueprints

| Skill | Baglidir | Not |
| --- | --- | --- |
| `mh-skill-catalog-validator` | `mh-blueprint-catalog-validator` | Paketlenmis skill, kaynak blueprint bagini korur |
| `mh-skill-prompt-library-curator` | `mh-blueprint-prompt-library-curator` | Paketlenmis skill, kaynak blueprint bagini korur |
| `mh-skill-skill-packager` | `mh-blueprint-skill-packager` | Paketlenmis skill, kaynak blueprint bagini korur |
| `mh-skill-adapter-mapper` | `mh-blueprint-adapter-mapper` | Paketlenmis skill, kaynak blueprint bagini korur |

## Blueprints -> Masters / Modules / Blueprints

| Blueprint | Bagimliliklar |
| --- | --- |
| `mh-blueprint-prompt-library-curator` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-action-summary` |
| `mh-blueprint-game-strategy-session-composer` | `mh-master-ultimate-game-development-strategist-core`, `mh-module-steam-market-validation`, `mh-module-mvp-scope-reduction`, `mh-module-production-risk-strategy`, `mh-module-full-concept-greenlight` |
| `mh-blueprint-real-estate-valuation-session-composer` | `mh-master-ultimate-real-estate-market-and-valuation-strategist-core`, `mh-module-real-estate-market-data-validation`, `mh-module-real-estate-comparable-analysis`, `mh-module-real-estate-valuation-logic`, `mh-module-real-estate-risk-and-uncertainty`, `mh-module-real-estate-investment-decision-support`, `mh-module-real-estate-no-hallucination-governance` |
| `mh-blueprint-onboarding-router` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-collaborative-guidance`, `mh-module-action-summary` |
| `mh-blueprint-catalog-validator` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-action-summary` |
| `mh-blueprint-skill-packager` | `mh-blueprint-prompt-library-curator`, `mh-module-repo-architecture`, `mh-module-action-summary` |
| `mh-blueprint-adapter-mapper` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-action-summary` |

## Masters -> Modules

| Master | Bagimliliklar |
| --- | --- |
| `mh-master-prompt-library-orchestrator` | `mh-module-context-audit`, `mh-module-repo-architecture`, `mh-module-collaborative-guidance`, `mh-module-no-sensitive-data`, `mh-module-action-summary` |
| `mh-master-ultimate-game-development-strategist-core` | `mh-module-steam-market-validation`, `mh-module-mvp-scope-reduction`, `mh-module-production-risk-strategy`, `mh-module-full-concept-greenlight` |
| `mh-master-ultimate-real-estate-market-and-valuation-strategist-core` | `mh-module-real-estate-market-data-validation`, `mh-module-real-estate-comparable-analysis`, `mh-module-real-estate-valuation-logic`, `mh-module-real-estate-risk-and-uncertainty`, `mh-module-real-estate-investment-decision-support`, `mh-module-real-estate-no-hallucination-governance` |
| `mh-master-prompt-library-orchestrator-legacy` | `mh-module-context-audit`, `mh-module-action-summary` |

## Modules

Moduller su anda cekirdek katalogda bagimsiz destek birimleri olarak listelenir; kataloglanan moduller icin ikincil bir `depends_on` iliskisi bulunmamaktadir.
