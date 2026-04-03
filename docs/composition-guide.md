# Birlestirme ve Terfi Rehberi

Bu belge, modullerden bir master prompt olusturma ve bir blueprint'i skill paketine donusturma akisini netlestirir.

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

Bir blueprint, skill'in yazili dusunce surumudur. Skill paketi ise bunu Codex tarafinda tekrar kullanilabilir bir klasor kontratina donusturur.

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
3. Yonetisim bilgilerini `skills/<skill-slug>/meta.yaml` icine koy.
4. Gerekirse `references/`, `scripts/`, `assets/`, `agents/` klasorlerini ekle.
5. `catalog/skills.md` kaydini olustur.
6. Ornek kullanim akisini `examples/compositions/` altinda belgeleyin.

## Neyi Paketlememeliyim?

- Hala sekillenmekte olan tek seferlik notlari
- Tek bir proje oturumuna ozel gecici denemeleri
- Sadece arka plan anlatimi olan ama net workflow icermeyen metinleri

## V1 Siniri

Bu repoda ilk asamada otomatik lint, CI veya katalog dogrulama betigi yoktur. Birlestirme ve terfi kararlarini README, katalog ve ornekler destekler; operasyonel otomasyon daha sonraki iterasyona birakilir.
