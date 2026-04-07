# Unity 6 Developer Session Example

Bu ornek, `Unity 6 Developer` skill'inin gercek bir implementasyon ve debugging talebini jenerik tavsiyeye erken atlamadan nasil ele almasi gerektigini gosterir.

## Ham Istek

Unity 6 ile ucuncu sahis bir aksiyon oyunu yapiyorum. Dash ability bazen duvarlara carpinca oyuncuyu dash state'inde takili birakiyor, bir de bazen stamina UI ayni frame icinde yenilenmiyor. Bunu debug etmeme yardim et ve daha guvenli bir yapi oner.

## Beklenen Cevap Disiplini

- Once problem sekli yeniden kurulmali: state transition ile collision ve UI refresh timing problemi birlikte olabilir.
- Muhtemel kod sorunlari configuration veya lifecycle sorunlarindan ayristirilmali.
- Dash flow, collision setup veya UI binding hala cok belirsizse yalnizca bir kisa netlestirme turu acilmali.
- Daha buyuk bir rewrite onermeden once en kucuk guvenilir fix tercih edilmeli.

## Ornek Cevap Sekli

### Working Understanding

Muhtemelen birbiriyle baglantili iki ariza var: dash state'i collision sonrasi her zaman temiz kapanmiyor ve stamina sunumu gameplay state update yolu ile tam senkron ilerlemiyor.

### Likely Causes

- Dash cikisi timer'a bagli ama duvar carpismasi velocity veya state'i degistirirken ayni exit yolunu tetiklemiyor
- UI refresh, stamina'nin degistigi asil noktadan degil daha zayif bir sinyalden besleniyor
- State temizligi `Update`, `FixedUpdate` ve animation callback'leri arasinda bolunup race condition olusturuyor olabilir

### Recommended Approach

- Dash baslangici ve dash bitisini tek bir sahipte merkezilestir
- Collision ile kesilme oldugunda timeout ile ayni dash-exit yolunu cagir
- Stamina UI'yi ikincil polling tahmini yerine yetkili stamina degisim event'i veya method'undan yenile

### Verification Checklist

- Duz duvar, acili duvar ve hareketli hedef durumlarinda tekrar dene
- Dash state'inin her zaman tek bir kod yolundan ciktigini dogrula
- Stamina UI'nin dash baslangicinda, kesilmede ve cooldown recovery'de guncellendigini kontrol et
- Duplicate listener veya scene'e ozel prefab override olup olmadigina bak

## Not

Bu skill uygulama odagini korumali. Kod onerebilir ama once hata modelini ve test yolunu netlestirmelidir.
