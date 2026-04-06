---
name: adapter-mapper
description: Use when mapping a core prompt, blueprint, master, or skill into adapter-layer guidance for Claude Code, ChatGPT, Codex, or generic LLM environments.
---

# Adapter Mapper

## Use When

- Bir cekirdek prompt, blueprint, master veya skill icin adapter katmaninda neyin belgelenmesi gerektigi netlestirilecekse
- Hangi davranisin core'da kalmasi, hangisinin adapter guidance'a gitmesi gerektigi ayrilacaksa
- `claude-code`, `chatgpt`, `codex` ve `generic-llm` icin minimum yararli mapping ozeti isteniyorsa

## Workflow

1. Hedef cekirdek varligi incele; kimlik, amac, bagimlilik zinciri ve portability niyetini cikar.
2. Core'da degismeden kalmasi gereken kisimlari ayristir: amac, dependency gorunurlugu, workflow mantigi ve provider-agnostik kurallar.
3. Adapter guidance'a gitmesi gereken kisimlari belirle: runtime beklentileri, oturum sekli, task packet veya project instruction gibi temsil farklari.
4. Hangi adapterlerin gercekten alakali oldugunu belirt; mapping gerekmiyorsa bunu da acikca soyle.
5. `claude-code`, `chatgpt`, `codex` ve `generic-llm` icin sadece minimum yararli mapping onerilerini `core invariants`, `adapter needs`, `mapping recommendations` ve `next step` basliklari altinda sun.

## Output Expectations

- `core invariants`: Core'da aynen korunmasi gereken kimlik, dependency ve davranis parcalari.
- `adapter needs`: Adapter katmanina tasinmasi gereken runtime-odakli notlar.
- `mapping recommendations`: Ilgili adapterler icin minimum faydali temsil onerileri.
- `next step`: Sonraki en kucuk uygulanabilir adapter belgeleme adimi.

## Portability Notes

- Bu skill adapter mapping karar mantigini provider-agnostik bicimde korur.
- Runtime'a ozel komut, izin, hook veya arac detaylari cekirdek skill paketine degil adapter dosyalarina aittir.
