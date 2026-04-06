# Feature Spec Session Example

This example yari tanimli bir oyun mekaniginin Feature Spec Composer by how yapisal bir feature specification'a donusturulecegini gostermek icin is prepared.

## Raw Request

Oyuncu oyunda zaman zaman "focus mode" acabilsin. Bu mod acikken etraftaki onemli seyler daha gorunur olsun ve oyuncu biraz daha kontrollu oynasin.

## Expected Clarification Points

- Focus mode manual mi otomatik mi aktiflesiyor?
- Sureli mi, cooldown var mi?
- Hangi nesneler veya etkileşimler "onemli" sayiliyor?
- Mod combat, puzzle veya exploration akisini how etkiliyor?

## Example Response Shape

### Feature Summary

Oyuncunun short sureli olarak cevredeki kritik ipucu, hedef ve etkilesimli unsurlari daha net algilamasini saglayan optional bir odak modu.

### Design Goals

- Oyuncunun bilgi yogun sahnelerde neye dikkat etmesi gerektigini daha iyi anlamasi
- Puzzle ve exploration anlarinda gereksiz tarama yukunu azaltmak
- Kontrol hissini arttirmak ama temel zorlugu ortadan kaldirmamak

### Player Experience

Oyuncu sikistiginda veya dikkatini toparlamak istediginde focus mode'u aktif eder. Ortam biraz daha okunakli hale gelir; kritik nesneler ve rota ipuclari daha belirginlesir.

### Functional Description

- Focus mode oyuncu by manual olarak aktiflestirilir.
- Mod 5 saniye surer ve tekrar kullanilabilmesi icin 20 saniyelik cooldown gerekir.
- Kritik nesneler, etkilesimli objeler ve current objective ile iliskili izler vurgulanir.

### Rules and Logic

- Mod aktifken zaman yavaslamaz; only cevresel okunabilirlik artar.
- Vurgular only o anki objective ile iliskili unsurlara uygulanir.
- Cooldown dolmadan mod tekrar acilamaz.

### UI / UX Notes

- Ekranda yumusak bir focus overlay kullanilabilir.
- Cooldown durumu oyuncuya sade bir ikon veya radial gosterge ile anlatilmalidir.

### Technical / Implementation Notes

- Sistem objective contextina gore hangi nesnelerin vurgulanacagini ust seviye bir etiketleme veya state mantigiyla belirlemelidir.

### Edge Cases

- Oyuncu cooldown sirasinda tekrar aktivasyon denerse what olacak?
- Objective bagli vurgu verisi eksikse mod how davranacak?
- Combat aninda usagea permission verilecek mi?

### Dependencies

- Objective / quest sistemi
- Etkilesimli obje definesi
- UI cooldown gosterimi

### Open Questions

- Combat sirasinda mod clear kalmali mi?
- Puzzle odakli sahnelerde sure veya cooldown farklilastirilmali mi?

### Acceptance Criteria

- Oyuncu focus mode'u manual olarak aktiflestirebilir.
- Kritik objective bagli nesneler mod sirasinda belirginlesir.
- Cooldown logic tutarli calisir.
- Oyuncu, modun what zaman aktif ve what zaman yeniden kullanilabilir oldugunu UI uzerinden anlayabilir.
