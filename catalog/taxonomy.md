# Taxonomy

Bu belge, izinli etiketleri ve klasor bazli anlamlari sabitler. Yeni etiket eklemeden once burada yer alan gruplardan biriyle ifade edilip edilemeyecegi kontrol edilmelidir.

## Katmanlar

| Katman | Anlam |
| --- | --- |
| `core` | Tasinabilir prompt, modul, blueprint, skill ve katalog icerigi |
| `adapter` | Belirli bir runtime'a ozel esleme, komut ve otomasyon notlari |
| `validation` | Repo butunlugu, metadata ve link dogrulama araclari |

## Modul Kategorileri

| Klasor | Amac |
| --- | --- |
| `capability` | Davranis, muhakeme adimi veya uygulama yetenegi |
| `domain` | Alan bilgisi, repo yapisi, is kurali veya uzmanlik cercevesi |
| `tone` | Ses tonu, iletisim bicimi ve isbirligi tarzi |
| `constraints` | Yasatilacak kurallar, sinirlar ve guvenlik kosullari |
| `output` | Cikti bicimi, raporlama tarzi ve sunum kontrati |

## Izinli Etiketler

| Etiket | Anlam |
| --- | --- |
| `analysis` | Durum tespiti, inceleme veya baglam toplama agirlikli icerik |
| `collaboration` | Isbirligi, eslik etme ve destekleyici iletisim |
| `composition` | Modullerin birlestirilmesi veya orkestrasyonu |
| `discovery` | Mevcut durumu arastirma ve belgeleme |
| `documentation` | Repo belgeleri, aciklayici promptlar ve yazili standartlar |
| `governance` | Surum, durum, yasam dongusu ve bakim disiplini |
| `guidance` | Kullaniciyi yonlendiren veya karar netlestiren icerik |
| `legacy` | Yalnizca tarihsel referans icin saklanan icerik |
| `library` | Prompt kutuphanesi ve ic organizasyonla ilgili icerik |
| `output-format` | Cikti sekli, rapor bicimi ve sunum kontrati |
| `packaging` | Blueprint'i skill paketine donusturme pratikleri |
| `portability` | Icerigin birden fazla runtime'da tasinabilirligini koruma hedefi |
| `privacy` | Hassas veriyi koruma ve bilgi ayrimi |
| `readability` | Acik, taranabilir ve anlasilir yazim hedefi |
| `routing` | Talebi dogru varlik tipine veya akisa yonlendirme |
| `repo-architecture` | Klasorleme, repo iskeleti ve dosya kontrati |
| `repo-hygiene` | Temizlik, tutarlilik ve bakim kolayligi |
| `safety` | Guvenli kullanim sinirlari ve zarar azaltma |
| `summary` | Kisa sonuc, sonraki adim veya toparlama formatlari |
| `tone` | Ton modulleri veya ses karakteri |
| `validation` | Katalog, metadata, link veya bagimlilik tutarliligini denetleme |
| `workflow` | Adim adim is akisina hizmet eden icerik |

## Etiketleme Kurali

- Her prompt en az 2, ideal olarak 3-5 etiket tasir.
- Ayni anlami tasiyan yeni etiketler turetilmez.
- Skill metalarinda, blueprint ile uyumlu ana etiketler korunur.
