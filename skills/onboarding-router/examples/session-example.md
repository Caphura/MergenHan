# Onboarding Router Session Example

This example repo icinde tekrar kullanilabilir bir routing davranisinin hangi katmana gitmesi gerektigini gostermek icin is prepared.

## Raw Request

Repo icinde tekrar tekrar kullanabilecegim bir guidance davranisi tasarlamak istiyorum. Bu davranis, gelen istegin yeni prompt, blueprint, skill packaging, catalog maintenancei veya adapter mapping olup olmadigini ayirsin. Amacim atomik bir yardimci davranis parcasi degil; different onboarding durumlarinda tekrar kullanabilecegim, ileride paketlenmeye aday bir routing mantigini once correct katmanda tutmak. Simdilik bunu henuz skill olarak paketlemek istemiyorum. Bunu repoda nereye koymaliyim?

## Example Response Shape

### Routing Decision

`blueprint`

### Why This Route

Bu request tek tasklik bir orchestration promptu degil; different onboarding durumlarinda tekrar kullanilacak skill-benzeri bir routing davranisi. Atomik bir `module` kadar dar degil, ama henuz paketlenmis `skill` de olmak istenmiyor. Bu nedenle ilk correct katman `prompts/skill-blueprints/` altindaki `blueprint` seviyesidir.

### Dependency Candidates

- `mh-module-context-audit`
- `mh-module-repo-architecture`
- `mh-module-collaborative-guidance`
- `mh-module-action-summary`

### Recommended Next Step

`prompts/skill-blueprints/onboarding-router.md` altinda davranisi tut, different routing senaryolariyla test et ve ancak ayrimlar tutarli hale geldikten sonra `skills/onboarding-router/` paketine promotion et.
