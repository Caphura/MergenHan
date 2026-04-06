# Orkestrasyon Kurallari

Bu belge, MergenHan icindeki cekirdek varlik tiplerinin birbiriyle nasil iliski kuracagini ve repo genelinde nasil evrilecegini tanimlar.

## Genel Ilkeler

- Cekirdek icerik okunur, tasinabilir ve bagimliliklari acik olacak sekilde yazilir.
- Ayni davranis tekrar ettiginde once `module` adayligi dusunulur.
- Runtime'a ozel davranis cekirdekte gizlenmez; adapter katmanina tasinir.
- Terfi, katalog ve bagimlilik kayitlari guncellenmeden tamamlanmis sayilmaz.

## Master Kurallari

- `master` bir gorev ailesi icin birden fazla modulun acik bicimde birlestirilmis surumudur.
- Master'lar `Assembly Map` veya benzeri bir bolumle hangi bagimliliklari neden kullandigini gostermelidir.
- Master icinde yer alan davranis tekrar kullanilabilir hale geldiyse ayri bir module cikarilmalidir.

## Module Kurallari

- Moduller tekrar kullanilabilir destek birimleridir.
- Tek sorumluluk ilkesine yakin tutulurlar.
- Modul bir gorevin tamamini degil, goreve tasinabilir destek parcasi olusturur.
- Moduller bagimsiz kalabildigi surece baska modullere zorunlu baglanmamaya oncelik verir.

## Blueprint Kurallari

- Blueprint, paketleme oncesi stabilize edilen skill taslagidir.
- Her blueprint `depends_on` alaninda bagimliliklarini acikca beyan etmelidir.
- Blueprint paketlenmeye aday olsa bile runtime'a ozel syntax icermez.
- Promotion kriterleri belgenin icinde veya ilgili paket spec'inde izlenebilir olmalidir.

## Skill Kurallari

- Skill paketleri, blueprint kokenini kaybetmeden `skills/` altina terfi eder.
- Skill'ler bagimlilik zincirini gizlememelidir; `meta.yaml` veya katalog kayitlari bunu gostermelidir.
- Provider-specific davranis cekirdek skill taniminda degil adapter mapping'lerinde tutulur.
- Bir skill birden fazla adapter tarafindan desteklenebilir.

## Catalog Kurallari

- Yeni veya tasinan her varlik ilgili katalogda izlenebilir olmalidir.
- Promosyonlar `catalog/prompts.md`, `catalog/skills.md` ve gerekirse `catalog/dependencies.md` kayitlarini gunceller.
- `catalog/taxonomy.md` yeni etiket ihtiyaclarini kontrollu bicimde sabitler.
- Kataloglar yapinin sahibi degil, indeksidir; gercek kaynak dosya repodaki varligin kendisidir.

## Arsiv Kurallari

- Arsivlenen icerik silinmez; bulunabilir kalir.
- Arsiv kayitlari kataloglardan tamamen dusurulmez, durumu acik bicimde korunur.
- Yeni varyant eski icerigi ikame ediyorsa bu iliski notlarda veya katalogda gorunur olmalidir.

## Adapter Iliskisi

- Adapter mapping'i bir yasam dongusu asamasi degildir.
- Adapter, var olan cekirdek icerigin runtime uyumluluk katmanidir.
- Ayni cekirdek varlik farkli adapterlerde farkli calistirma notlariyla temsil edilebilir; buna ragmen kimlik, amac ve bagimlilik zinciri cekirdekten alinmaya devam eder.
