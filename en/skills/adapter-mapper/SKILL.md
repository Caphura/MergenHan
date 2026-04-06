---
name: adapter-mapper
description: Use when mapping a core prompt, blueprint, master, or skill into adapter-layer guidance for Claude Code, ChatGPT, Codex, or generic LLM environments.
---

# Adapter Mapper

## Use When

- Bir core prompt, blueprint, master veya skill icin adapter katmaninda neyin belgelenmesi gerektigi netlestirilecekse
- Hangi davranisin core'da kalmasi, hangisinin adapter guidance'a gitmesi gerektigi ayrilacaksa
- `claude-code`, `chatgpt`, `codex` ve `generic-llm` icin minimum yararli mapping ozeti isteniyorsa

## Workflow

1. Hedef core varligi incele; identity, purpose, dependency zinciri ve portability niyetini cikar.
2. Core'da degismeden kalmasi gereken kisimlari separate: purpose, dependency gorunurlugu, workflow logic ve provider-agnostik rules.
3. Adapter guidance'a gitmesi gereken kisimlari belirle: runtime beklentileri, session form, task packet veya project instruction such as temsil farklari.
4. Hangi adapterlerin gercekten alakali oldugunu belirt; mapping gerekmiyorsa bunu da explicitly soyle.
5. `claude-code`, `chatgpt`, `codex` ve `generic-llm` icin only minimum yararli mapping onerilerini `core invariants`, `adapter needs`, `mapping recommendations` ve `next step` basliklari altinda sun.

## Output Expectations

- `core invariants`: Core'da aynen korunmasi gereken identity, dependency ve davranis parcalari.
- `adapter needs`: Adapter katmanina tasinmasi gereken runtime-odakli notlar.
- `mapping recommendations`: Ilgili adapterler icin minimum faydali temsil onerileri.
- `next step`: Sonraki en kucuk uygulanabilir adapter belgeleme adimi.

## Portability Notes

- This skill adapter mapping decision mantigini provider-agnostik bicimde preserves.
- Runtime'a specific command, permission, hook veya vehicle detaylari core skill paketine degil adapter dosyalarina aittir.
