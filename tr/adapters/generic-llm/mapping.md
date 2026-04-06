# Generic LLM Mapping

## Adapter Ne Bekler?

- Duz metin olarak tasinabilir cekirdek prompt veya skill tanimi
- Bagimliliklarin ve kisitlarin acik yazimi
- Tool veya permission varsayimi yapmayan workflow anlatimi

## Core Skill Burada Nasil Temsil Edilir?

- `SKILL.md` dogrudan kullanilabilir cekirdek talimat olarak ele alinir
- `meta.yaml` baglam ve yonetisim bilgisi saglar
- Gerekirse blueprint veya master aciklamalari oturum baglamina manuel olarak eklenir

## Core'dan Ne Degismeden Kalmalidir?

- Kimlik, kapsam ve bagimliliklar
- Cekirdek workflow
- Kisitlar ve cikti beklentileri

## Runtime Duzeyinde Ne Uyarlanabilir?

- Baglamin tek mesajda veya asamali verilmesi
- Oturum acilis metninin kisaltilmasi veya genisletilmesi
- Cikti sablonunun arayuze gore duzenlenmesi

Kisa not:

- Text-only image prompt composer turu skill'ler generic LLM tarafinda dogrudan `SKILL.md` uzerinden tasinabilir.
- Gemini benzeri ortamlarda, gorsel araclari olsa bile varsayilan davranis metin cikti olarak korunmalidir.
