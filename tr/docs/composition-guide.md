# Birlestirme ve Terfi Rehberi

Bu belge, modullerden bir master prompt olusturma, bir blueprint'i skill paketine donusturma ve gerekirse adapter katmanina esleme akisini netlestirir.

## Modulden Master Prompta

Bir master prompt, tek bir uzun metin olmaktan ziyade acik gorevler etrafinda bir araya gelen moduller toplulugu olarak dusunulur.

### Onerilen Sira

1. Gorevin cekirdek amacini tanimla.
2. Gerekli modulleri sec:
   - yetenek davranisi
   - alan bilgisi
   - ton
   - kisit
   - cikti bicimi
3. Secilen modulleri `depends_on` alaninda listele.
4. Master prompt icinde modullerin nasil kullanildigini kisa bir `Assembly Map` bolumuyle belgeleyin.
5. Katalogu guncelleyin.

### Ne Zaman Yeni Modul Cikarmaliyim?

- Ayni paragrafi ikinci kez kopyalamaya basladiysaniz
- Farkli master promptlarda ayni kalite standardini korumak istiyorsaniz
- Davranis, ton veya kisit baska baglamlarda da is goruyorsa

## Blueprint'ten Skill'e

Bir blueprint, skill'in yazili dusunce surumudur. Skill paketi ise bunu farkli AI runtime'larinda tekrar kullanilabilir bir klasor kontratina donusturur.

### Terfi Kontrol Listesi

Asagidaki sorularin cogu "evet" ise paketleme zamani gelmistir:

- Tetikleyici kullanim senaryolari tekrar ediyor mu?
- Skill'in giris cikis kontrati yeterince net mi?
- Ana workflow maddeler halinde anlatilabiliyor mu?
- Referans, script veya asset gibi yardimci parcalara ihtiyac belli mi?
- Kataloga eklenince baskasi da bu skill'i bulup anlayabilir mi?

### Paketleme Akisi

1. Blueprint'i son kez gozden gecir.
2. `skills/<skill-slug>/SKILL.md` dosyasina sade calisma talimatlarini tasit.
3. Yonetisim bilgilerini `meta.yaml` icine koy.
4. Gerekirse `references/`, `scripts/`, `assets/`, `agents/` klasorlerini ekle.
5. `catalog/skills.md` kaydini olustur.
6. Ornek kullanim akisini `examples/compositions/` altinda belgeleyin.

## Skill'ten Adapter'e

Skill cekirdegi olustuktan sonra runtime'a ozel uyarlamalar `adapters/` altinda tutulur.

### Adapter Akisi

1. Cekirdek skill veya blueprint icinden degismemesi gereken kisitlari ayikla.
2. Runtime'a ozel komut, arac, izin ve otomasyon beklentilerini adapter icinde tanimla.
3. Cekirdek skill tanimina provider'a ozel syntax gommemeye dikkat et.
4. Adapter mapping notlarini ilgili README ve `mapping.md` dosyalarina ekle.
5. Yeni bir runtime destegi eklenirse cekirdek icerigi kirmadan `adapter_support` bilgisini guncelle.

## Neyi Paketlememeliyim?

- Hala sekillenmekte olan tek seferlik notlari
- Tek bir proje oturumuna ozel gecici denemeleri
- Sadece arka plan anlatimi olan ama net workflow icermeyen metinleri

## Hafif Dogrulama

Bu repoda agir CI bagimliliklari yerine hafif dogrulama betikleri tercih edilir.

- `scripts/validate_catalog.py`: katalog ve dosya uyumunu kontrol eder
- `scripts/validate_metadata.py`: frontmatter ve `meta.yaml` alanlarini kontrol eder
- `scripts/check_missing_links.py`: goreli markdown baglantilarini dogrular
