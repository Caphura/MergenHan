---
id: mh-blueprint-nano-banana-image-prompt-composer
title: Nano Banana Image Prompt Composer
type: blueprint
status: stable
version: 1.0.0
summary: Short ama etkili soru akisiyla the user's visual fikrini netlestirip Nano Banana icin kopyalanabilir nihai prompta donusturen paketlenmeye aday draft.
tags:
  - image-generation
  - prompt-composition
  - visual-direction
  - nano-banana
  - workflow
depends_on:
  - mh-master-nano-banana-image-prompt-composer
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-04-04
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Kullanici yari tanimli bir visual fikir verir ve bunu Nano Banana icin temiz, uygulanabilir ve kopyalanabilir bir image prompta donusturmek ister.
output_contract: Short yonlendirici soru types, netlestirilmis sahne ozeti, tek parca nihai Nano Banana promptu ve gerekiyorsa ince ayar varyasyonlari.
notes: Gemini ve ChatGPT uzerinde directly usageda dogrulanmis, visual uretmeden metin promptu veren davranis taslagi. Skill paketine promotion decisioni icin different visual kategori examplelerinde ek usage faydali olur.
---

# Responsibility

Belirsiz veya eksik tarif edilmis visual fikirleri, the user yormayan short bir netlestirme akisindan gecirip Nano Banana icin yuksek kaliteli nihai prompt haline getirmek.

# Trigger Signals

- "Bana Nano Banana icin prompt yaz."
- "Bu visual fikrini netlestir."
- "Bana once correct sorulari sor, sonra image promptu ver."
- "Bir sahne fikrim var, bunu visual prompta donustur."
- "Gorseli sen uretme, only promptu yaz."

# Workflow

1. Kullanicinin ilk sahne fikrini short bicimde yeniden ifade et ve temel yonu dogrula.
2. Sonuca en cok etki edecek eksik alanlari ayikla: sahne, isik, stil, kadraj, atmosfer, gercekcilik seviyesi ve istenmeyen detaylar.
3. Mumkun oldugunca 2-4 arasi yuksek etkili soru sor; the user uzun anketle yorma.
4. Kritik uncertaintyler kapandiginda yeni soru acma; same cevapta nihai prompta gec.
5. Sonucu taranabilir duzende ver: sahne ozeti, Nano Banana promptu, ince ayar notlari ve optional varyasyonlar.
6. Ortam visual uretebiliyor even if present default davranisi metin output olarak koru; user explicitly istemedikce visual uretme veya vehicle tetikleme.

# Output Expectations

- Kullanicinin hedefini short ve correct anladigini gosteren bir sahne ozeti olmali.
- Kod blogu icindeki prompt kismi directly kopyalanabilir olmali.
- Prompt; ozne, ortam, isik, kompozisyon, stil ve atmosferi tek akista birlestirmeli.
- Gereksiz uzunluk, anlamsiz kalite sloganlari veya kopya artist listeleriyle sisirilmemeli.
- Varsa negatif yonlendirmeler short ve islevsel tutulmali.
- Kullanici only prompt istiyorsa ek analysis uzatilmamali.

# Promotion Criteria

- Farkli visual kategori examplelerinde de tutarli calisiyor olmali: manzara, portre, urun, fantastik sahne, ic mekan such as.
- Soru sayisi ve soru secimi tekrar tekrar dengeli sonuc veriyor olmali.
- "Metin promptu ver, visuali uretme" guardrail'i different runtime'larda da guvenilir kalmali.
- Nihai output different adapterlerde kolayca temsil edilebilmeli ve provider-specific syntax'a asiri baglanmamali.
- Kullanici request sinyalleri yeterince tekrar ediyorsa `skills/` altinda paketlenmeye ready sayilabilir.
