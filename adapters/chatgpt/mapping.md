# ChatGPT Mapping

## Adapter Ne Bekler?

- Kopyalanabilir cekirdek prompt veya skill ozeti
- Oturumda tasinacak bagimlilik ve kisitlarin acik ifadesi
- Gerekirse proje veya custom GPT seviyesinde yerlestirilebilecek yonerge yapisi

## Core Skill Burada Nasil Temsil Edilir?

- `SKILL.md` kullaniciya veya proje baglamina aktarilacak cekirdek skill talimati olarak okunur
- `meta.yaml` kaynak blueprint ve bagimliliklari gosterir
- ChatGPT'ye ozel injection veya project instruction bicimi bu adapter tarafindan aciklanir

## Core'dan Ne Degismeden Kalmalidir?

- Kimlik ve amac
- Giris / cikis kontrati
- Cekirdek workflow
- Provider-agnostik davranis ilkeleri

## Runtime Duzeyinde Ne Uyarlanabilir?

- Promptun tek parca veya parca parca verilmesi
- Project instruction, custom GPT veya manuel oturum kullanimi
- Cikti biciminin ChatGPT arayuzundeki kullanim seklinde sunulmasi
