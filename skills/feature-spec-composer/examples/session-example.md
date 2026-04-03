# Feature Spec Session Example

Bu ornek, yari tanimli bir oyun mekaniginin Feature Spec Composer tarafindan nasil yapisal bir feature specification'a donusturulecegini gostermek icin hazirlanmistir.

## Ham Istek

Oyuncu oyunda zaman zaman "focus mode" acabilsin. Bu mod acikken etraftaki onemli seyler daha gorunur olsun ve oyuncu biraz daha kontrollu oynasin.

## Beklenen Netlestirme Noktalari

- Focus mode manuel mi otomatik mi aktiflesiyor?
- Sureli mi, cooldown var mi?
- Hangi nesneler veya etkileşimler "onemli" sayiliyor?
- Mod combat, puzzle veya exploration akisini nasil etkiliyor?

## Ornek Cevap Sekli

### Feature Summary

Oyuncunun kisa sureli olarak cevredeki kritik ipucu, hedef ve etkilesimli unsurlari daha net algilamasini saglayan istege bagli bir odak modu.

### Design Goals

- Oyuncunun bilgi yogun sahnelerde neye dikkat etmesi gerektigini daha iyi anlamasi
- Puzzle ve exploration anlarinda gereksiz tarama yukunu azaltmak
- Kontrol hissini arttirmak ama temel zorlugu ortadan kaldirmamak

### Player Experience

Oyuncu sikistiginda veya dikkatini toparlamak istediginde focus mode'u aktif eder. Ortam biraz daha okunakli hale gelir; kritik nesneler ve rota ipuclari daha belirginlesir.

### Functional Description

- Focus mode oyuncu tarafindan manuel olarak aktiflestirilir.
- Mod 5 saniye surer ve tekrar kullanilabilmesi icin 20 saniyelik cooldown gerekir.
- Kritik nesneler, etkilesimli objeler ve guncel objective ile iliskili izler vurgulanir.

### Rules and Logic

- Mod aktifken zaman yavaslamaz; yalnizca cevresel okunabilirlik artar.
- Vurgular sadece o anki objective ile iliskili unsurlara uygulanir.
- Cooldown dolmadan mod tekrar acilamaz.

### UI / UX Notes

- Ekranda yumusak bir focus overlay kullanilabilir.
- Cooldown durumu oyuncuya sade bir ikon veya radial gosterge ile anlatilmalidir.

### Technical / Implementation Notes

- Sistem objective baglamina gore hangi nesnelerin vurgulanacagini ust seviye bir etiketleme veya state mantigiyla belirlemelidir.

### Edge Cases

- Oyuncu cooldown sirasinda tekrar aktivasyon denerse ne olacak?
- Objective bagli vurgu verisi eksikse mod nasil davranacak?
- Combat aninda kullanima izin verilecek mi?

### Dependencies

- Objective / quest sistemi
- Etkilesimli obje tanimlari
- UI cooldown gosterimi

### Open Questions

- Combat sirasinda mod acik kalmali mi?
- Puzzle odakli sahnelerde sure veya cooldown farklilastirilmali mi?

### Acceptance Criteria

- Oyuncu focus mode'u manuel olarak aktiflestirebilir.
- Kritik objective bagli nesneler mod sirasinda belirginlesir.
- Cooldown mantigi tutarli calisir.
- Oyuncu, modun ne zaman aktif ve ne zaman yeniden kullanilabilir oldugunu UI uzerinden anlayabilir.
