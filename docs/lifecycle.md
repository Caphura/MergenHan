# Yasam Dongusu

Bu belge, MergenHan icindeki iceriklerin zaman icinde nasil evrildigini tanimlar. Adapter mapping'i bu yasam dongusunun bir asamasi degil, ayri bir uyumluluk katmanidir.

## Iki Eksenli Model

MergenHan yasam dongusu iki eksende okunur:

- yapisal tip: `module`, `master`, `blueprint`, `skill`
- olgunluk durumu: `draft`, `active`, `stable`, `deprecated`, `archived`

Bu sayede bir varlik hem bir tur, hem de bir olgunluk durumu tasir.

## Yapisal Tipler

### `module`

- Tekrar kullanilabilir destek birimidir.
- Davranis, kisit, ton, alan bilgisi veya cikti parcasi olabilir.

### `master`

- Bir gorev ailesi icin birden fazla modulu orkestre eder.
- Bagimliliklarini acikca gostermelidir.

### `blueprint`

- Paketlenmeye aday, stabilize edilmis skill taslagidir.
- Hala insan tarafindan tartisilabilir ve gelistirilebilir formdadir.

### `skill`

- Paketlenmis ve tekrar kullanima hazir cekirdek beceridir.
- Adapterler tarafindan farkli runtime'lara eslenebilir.

## Olgunluk Durumlari

### `draft`

- Ilk taslak seviyesidir.
- Hizli degisime aciktir.

### `active`

- Guncel kullanimda olan iceriktir.
- Henuz tam oturmamis olabilir ama tercih edilen surumdur.

### `stable`

- Davranisi oturmus ve tekrar tekrar kullanilan iceriktir.
- Paketleme veya genis dagitim icin iyi adaydir.

### `deprecated`

- Yerine daha iyi bir icerik gelmistir.
- Yeni kullanim icin onerilmez, fakat gecis icin saklanir.

### `archived`

- Tarihsel referans olarak korunur.
- Silinmez; bulunabilir kalir.

## Tipler Arasi Tipik Gecisler

En sik gorulen evrimler sunlardir:

- yeni tekrar kullanilabilir davranis `draft module` olarak baslar
- birden fazla modulu birlestiren akis `active master` haline gelir
- tekrar eden, paketlenebilir gorev mantigi `blueprint` olarak netlesir
- davranisi oturan blueprint `skill` paketine terfi eder
- zamanla oturan varlik `stable` olur
- yerini daha iyisi alirsa `deprecated`, tarihsel referanssa `archived` olur

## Adapter Mapping Neden Ayri?

Adapter mapping bir lifecycle stage degildir cunku:

- cekirdek varligin turunu degistirmez
- yalnizca belirli bir runtime ile uyumluluk bilgisini tasir
- ayni cekirdek varlik icin birden fazla adapter mapping'i bulunabilir

Dolayisiyla `claude-code`, `chatgpt`, `codex` veya `generic-llm` destegi, `draft` ya da `stable` gibi bir durum degil; ayri bir uyumluluk katmanidir.

