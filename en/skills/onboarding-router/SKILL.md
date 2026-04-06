---
name: onboarding-router
description: Use when a user needs their repo or prompt-library request routed to the right content type or maintenance action before any writing or packaging starts.
---

# Onboarding Router

## Use When

- Kullanici bir istegin `master`, `module`, `blueprint`, `skill`, `packaging`, `catalog` veya `adapter mapping` katmanlarindan hangisine gittigini anlamak istediginde
- Yeni content yazmaya baslamadan once correct repo aksiyonunu secmek gerektiginde
- Bir talebin atomik davranis mi, tek tasklik orkestrasyon mu, yoksa paketlenmeye aday beceri mi oldugu separateilmak istendiginde
- Runtime'a specific bir ihtiyacin cekirdege mi yoksa adapter katmanina mi gitmesi gerektigi net degilse

## Workflow

1. Kullanicinin asil amacini belirle; yeni content yazmak mi, mevcut content promotion ettirmek mi, yoksa katalog / adapter maintenancei mi istedigini separate.
2. Talebin davranis yapisini siniflandir:
   - `module`: tekrar kullanilabilir atomik davranis, rule veya output parcasi
   - `master`: tek bir taski bastan sona cozen orchestration promptu
   - `blueprint`: skill-benzeri ama henuz paketlenmemis tekrar kullanilabilir davranis
   - `skill`: artik paketlenmeye ready, test edilmis ve `skills/` altina to carry over olgun davranis
   - `packaging`: mevcut bir blueprint'i skill paketine cevirme istegi
   - `catalog`: katalog, metadata, dependency veya repo maintenancei istegi
   - `adapter mapping`: runtime'a veya provider-specific usage bicimine specific request
3. Gerekliyse dependency adaylarini listele; ama yeni content yazmadan once en kucuk mantikli sonraki adimi sec.
4. Runtime'a specific requestlerde core dosyalari provider syntax'i ile kirletme; the user adapter katmanina yonlendir.
5. Sonucu short ve taranabilir way ver: routing decision, neden bu rota, dependency adaylari ve onerilen sonraki step.

## Output Expectations

- `Routing Decision` tek bir ana rota icermeli ve gereksiz ikili decisionsizlik birakmamali.
- `Why This Route` bolumu context genisligi, tekrar kullanilabilirlik ve package olgunlugu ayrimini aciklamali.
- `Dependency Candidates` only gercekten anlamli adaylari icermeli; listeyi sisirmemeli.
- `Recommended Next Step` somut olmali; hangi klasore, hangi dosya tipine veya hangi maintenance akisina gidilecegini netlestirmeli.
- `master` ile `blueprint` ayrimini karistirmamali:
  - ilk calisan, tek tasklik orchestration promptlari genelde once `master`
  - tekrar kullanilabilir, ileride paketlenmeye aday routing davranislari genelde once `blueprint`

## References

- Short test oturumu ve routing ayrimlari icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- This skill'in core davranisi provider-agnostiktir.
- Runtime'a specific onboarding UI, project instruction veya task packet notlari adapter katmaninda belgelenmelidir.
- Varsaylisting task content user yerine yazmak degil; once correct repo aksiyonunu secmektir.
