# Adapter Modeli

MergenHan AI-agnostik bir prompt ve skill kutuphanesidir. Bu repoda cekirdek icerik tek bir saglayiciya, tek bir runtime'a veya tek bir arac ailesine kilitlenmez.

## Uc Katmanli Model

| Katman | Icerik | Neden Ayridir? |
| --- | --- | --- |
| `core` | Promptlar, moduller, masters, blueprints, skills, kataloglar, sablonlar ve temel belgeler | En uzun omurlu bilgi burada yasar ve tasinabilir kalir |
| `adapter` | Claude Code, ChatGPT, Codex veya generic LLM icin runtime eslemeleri | Her ortam farkli komut, arac, izin ve otomasyon modeline sahiptir |
| `validation` | Hafif kontrol scriptleri ve dogrulama kurallari | Bakim kalitesini artirir ama cekirdek icerigin anlamsal sahibi degildir |

## Cekirdek Icerik Nedir?

Cekirdek icerik su ilkeyle yazilir:

- Tek bir provider syntax'ina baglanmaz
- Ayni skill'in birden fazla adapter tarafindan temsil edilmesine izin verir
- Tasinabilir gorev mantigini ve bagimlilik zincirini saklar
- Insan tarafindan okunur ve elle bakima uygundur

Cekirdek icerigin icinde bulunmamasi gereken seyler:

- Sadece bir runtime'da gecerli slash command kaliplari
- Tool cagirimi icin platforma ozel komut soz dizimleri
- Hook, permission, agent wiring ve benzeri calistirma ortami detaylari
- Platforma ozel ayar dosyasi semantikleri

## Adapter Katmani Ne Yapar?

Adapter katmani, cekirdek prompt veya skill'i belirli bir runtime'a nasil tasiyacagimizi aciklar.

Ornek sorumluluklar:

- Claude Code icin slash command, settings, hooks ve permission yaklasimi
- ChatGPT icin project instruction, custom GPT ve manual prompt injection yaklasimi
- Codex icin repo gorev paketi, arac beklentisi ve yurutme notlari
- Generic LLM icin yalnizca minimum tasinabilir kullanim sekli

Bu detaylar cekirdege yazilmaz; ilgili adapter altinda belgelenir.

## Ayni Skill Birden Fazla Adapter ile Eslenebilir

Bir skill paketinin tek bir runtime karsiligi olmak zorunda degildir. Aksine, beklenen model sudur:

- cekirdekte bir adet ana skill tanimi bulunur
- bu skill icin bir veya daha fazla adapter mapping'i yazilir
- adapterler cekirdek davranisi degistirmez, sadece calistirma bicimini cevirir

## Yeni Bir Adapter Eklerken

Yeni bir runtime eklemek istediginizde asgari iskelet sunlardir:

- `adapters/<runtime>/README.md`
- `adapters/<runtime>/mapping.md`
- gerekiyorsa kompakt kullanim ornekleri veya istege bagli ayar ornekleri

Bu iskelet cekirdek sahipligi degistirmez; sadece yeni runtime'a gecis katmani ekler.

## Validation Katmani Neden Ayridir?

Validation katmani zorunlu bir runtime degildir. Amaci:

- katalogdaki kirik referanslari tespit etmek
- metadata eksiklerini gormek
- duplicate ID veya bozuk goreli link gibi bakim sorunlarini yakalamak

Bu katman cekirdek icerigin yerini almaz; yalnizca repo disiplinini destekler.

## Temel Kurallar

- MergenHan AI-agnostiktir.
- Cekirdek icerik Claude Code veya baska tek bir provider'a kilitlenmez.
- Runtime'a ozel komutlar, hook'lar, permission kurallari ve tool convention'lari adapter katmanina aittir.
- Ayni skill birden fazla adapter mapping'ine sahip olabilir.
- Adapter mapping'i cekirdek bagimlilik sahipligini degistirmez; adapterler cekirdek ID ve dependency zincirini referans alir.