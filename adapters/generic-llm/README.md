# Generic LLM Adapter

Bu klasor, ozel runtime ozellikleri olmayan herhangi bir LLM sistemi icin minimum tasinabilir kullanim bicimini tanimlar.

## Kapsam

- Duz metin prompt kullanim senaryolari
- Manuel baglam toplama ve enjekte etme yaklasimi
- Tool veya hook destegi olmayan ortamlarda cekirdek icerigin minimum calisma sekli

## Ornekler

- [`mapping.md`](./mapping.md): cekirdek varligin generic LLM tarafinda nasil temsil edilecegi
- [`minimal-usage-example.md`](./minimal-usage-example.md): en kisa kullanim ornegi

## Sinir

Bu adapter, ozel runtime yetenekleri yokmus gibi davranir. Boylece MergenHan cekirdek iceriginin en dusuk ortak paydada da calisabilir kalmasi saglanir.