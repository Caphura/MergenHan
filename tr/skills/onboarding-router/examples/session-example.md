# Onboarding Router Session Example

Bu ornek, repo icinde tekrar kullanilabilir bir routing davranisinin hangi katmana gitmesi gerektigini gostermek icin hazirlanmistir.

## Ham Istek

Repo icinde tekrar tekrar kullanabilecegim bir yonlendirme davranisi tasarlamak istiyorum. Bu davranis, gelen istegin yeni prompt, blueprint, skill packaging, catalog bakimi veya adapter mapping olup olmadigini ayirsin. Amacim atomik bir yardimci davranis parcasi degil; farkli onboarding durumlarinda tekrar kullanabilecegim, ileride paketlenmeye aday bir routing mantigini once dogru katmanda tutmak. Simdilik bunu henuz skill olarak paketlemek istemiyorum. Bunu repoda nereye koymaliyim?

## Ornek Cevap Sekli

### Routing Decision

`blueprint`

### Why This Route

Bu talep tek gorevlik bir orchestration promptu degil; farkli onboarding durumlarinda tekrar kullanilacak skill-benzeri bir routing davranisi. Atomik bir `module` kadar dar degil, ama henuz paketlenmis `skill` de olmak istenmiyor. Bu nedenle ilk dogru katman `prompts/skill-blueprints/` altindaki `blueprint` seviyesidir.

### Dependency Candidates

- `mh-module-context-audit`
- `mh-module-repo-architecture`
- `mh-module-collaborative-guidance`
- `mh-module-action-summary`

### Recommended Next Step

`prompts/skill-blueprints/onboarding-router.md` altinda davranisi tut, farkli routing senaryolariyla test et ve ancak ayrimlar tutarli hale geldikten sonra `skills/onboarding-router/` paketine terfi et.
