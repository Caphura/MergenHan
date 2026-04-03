---
name: onboarding-router
description: Use when a user needs their repo or prompt-library request routed to the right content type or maintenance action before any writing or packaging starts.
---

# Onboarding Router

## Use When

- Kullanici bir istegin `master`, `module`, `blueprint`, `skill`, `packaging`, `catalog` veya `adapter mapping` katmanlarindan hangisine gittigini anlamak istediginde
- Yeni icerik yazmaya baslamadan once dogru repo aksiyonunu secmek gerektiginde
- Bir talebin atomik davranis mi, tek gorevlik orkestrasyon mu, yoksa paketlenmeye aday beceri mi oldugu ayristirilmak istendiginde
- Runtime'a ozel bir ihtiyacin cekirdege mi yoksa adapter katmanina mi gitmesi gerektigi net degilse

## Workflow

1. Kullanicinin asil amacini belirle; yeni icerik yazmak mi, mevcut icerigi terfi ettirmek mi, yoksa katalog / adapter bakimi mi istedigini ayristir.
2. Talebin davranis yapisini siniflandir:
   - `module`: tekrar kullanilabilir atomik davranis, kural veya output parcasi
   - `master`: tek bir gorevi bastan sona cozen orchestration promptu
   - `blueprint`: skill-benzeri ama henuz paketlenmemis tekrar kullanilabilir davranis
   - `skill`: artik paketlenmeye hazir, test edilmis ve `skills/` altina tasinacak olgun davranis
   - `packaging`: mevcut bir blueprint'i skill paketine cevirme istegi
   - `catalog`: katalog, metadata, dependency veya repo bakimi istegi
   - `adapter mapping`: runtime'a veya provider-specific kullanim bicimine ozel istek
3. Gerekliyse bagimlilik adaylarini listele; ama yeni icerik yazmadan once en kucuk mantikli sonraki adimi sec.
4. Runtime'a ozel isteklerde cekirdek dosyalari provider syntax'i ile kirletme; kullaniciyi adapter katmanina yonlendir.
5. Sonucu kisa ve taranabilir sekilde ver: routing decision, neden bu rota, bagimlilik adaylari ve onerilen sonraki adim.

## Output Expectations

- `Routing Decision` tek bir ana rota icermeli ve gereksiz ikili kararsizlik birakmamali.
- `Why This Route` bolumu baglam genisligi, tekrar kullanilabilirlik ve paket olgunlugu ayrimini aciklamali.
- `Dependency Candidates` yalnizca gercekten anlamli adaylari icermeli; listeyi sisirmemeli.
- `Recommended Next Step` somut olmali; hangi klasore, hangi dosya tipine veya hangi bakim akisina gidilecegini netlestirmeli.
- `master` ile `blueprint` ayrimini karistirmamali:
  - ilk calisan, tek gorevlik orchestration promptlari genelde once `master`
  - tekrar kullanilabilir, ileride paketlenmeye aday routing davranislari genelde once `blueprint`

## References

- Kisa test oturumu ve routing ayrimlari icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel onboarding UI, project instruction veya task packet notlari adapter katmaninda belgelenmelidir.
- Varsayilan gorev icerigi kullanici yerine yazmak degil; once dogru repo aksiyonunu secmektir.
