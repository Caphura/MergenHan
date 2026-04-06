---
id: mh-blueprint-meshy-3d-prompt-composer
title: Meshy 3D Prompt Composer
type: blueprint
status: stable
version: 1.0.0
summary: Kullanicinin ham 3D asset fikrini short soru akisiyla netlestirip Meshy icin 800 karakteri asmayan, kopyalanabilir ve uygulanabilir promptlara donusturen stabilize edilmis draft.
tags:
  - prompt-composition
  - visual-direction
  - workflow
  - guidance
depends_on:
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
input_contract: Kullanici bir 3D asset, prop, silah, karakter, creature veya sahne objesi fikrini Meshy icin temiz ve kullanilabilir bir prompta cevirmek ister.
output_contract: Short yonlendirici soru types, netlestirilmis asset ozeti, tek parca kopyalanabilir Meshy promptu ve gerekiyorsa short varyasyon yonleri.
notes: This blueprint testlerden gecmis stabilize bir davranis tanimidir. Varsaylisting task model uretmek degil, Meshy'ye verilecek promptu yazmaktir. Meshy prompt metni 800 karakter boundary icinde tutulmalidir; gereksiz sifat ve tekrarlar temizlenmelidir. Uretim constraints only user bunlari ister veya gercekten gerektirirse eklenmelidir.
---

# Responsibility

Belirsiz veya yari tanimli 3D asset fikirlerini, the user yormayan short bir netlestirme akisindan gecirip Meshy icin temiz, uygulanabilir ve kopyalanabilir promptlara donusturmek.

# Trigger Signals

- "Meshy icin prompt yazar misin?"
- "Bana once correct sorulari sor, sonra 3D promptu ver."
- "Bu oyun objesini / silahi / karakteri Meshy promptuna donustur."
- "Modeli sen uretme, only promptu hazirla."
- "Bu 3D fikir fazla daginik, toparlayip Meshy'ye uygun hale getir."

# Workflow

1. Kullanicinin istedigi varligi short bicimde yeniden ifade et ve temel usage contextini dogrula: oyun asset'i, concept model, collectible, stylized prop veya daha teknik bir 3D hedef olup olmadigini separate.
2. Sonuca en cok etki edecek eksik alanlari ayikla: asset type, ana siluet, stil yonu, malzeme structure, renk paleti, kondisyon, oran hissi, usage contexti ve varsa istenmeyen detaylar.
3. Eger user only asset tipi + genel stil + context verdiyse, default olarak immediately prompta atlama; once 1 short turda 2-3 yuksek etkili soru sorarak stil yonu, rarity hissi, form dili veya kondisyon such as fark yaratan decisionleri sabitle.
4. Yalnizca girdi zaten yeterince doluysa veya user explicitly "soru sorma, direkt prompt ver" dediyse hizli moda gec ve same cevapta nihai promptu ver.
5. Kritik uncertaintyler kapandiginda yeni tur acma; same cevapta nihai prompta gec.
6. Sonucu taranabilir duzende ver: short asset ozeti, Meshy promptu, gerekiyorsa production notlari ve optional varyasyonlar.
7. Meshy Prompt bolumundeki asil prompt metnini 800 karakter icinde tut; limit asiliyorsa once tekrar eden sifatlari, sonra dusuk etkili detaylari shortlt.
8. Ortam 3D generation vehiclei sunuyor even if present default davranisi metin output olarak koru; user explicitly istemedikce model uretme veya vehicle tetikleme.
9. Kullanici teknik constraint istiyorsa bunlari gercekten bildigi kadar kullan; fabricated triangle count, topology vaadi veya PBR detaylari uretme.

# Output Expectations

- Kullanicinin hedef varligini correct anladigini gosteren short bir ozet olmali.
- Yetersiz tanimli requestlerde nihai prompttan once en az bir short netlestirme type beklenir; soru sormadan direkt prompt vermek default davranis olmamali.
- Kod blogu icindeki prompt kismi directly Meshy'ye kopyalanabilir olmali.
- Meshy Prompt bolumundeki metin 800 karakteri asmamali; limit asiliyorsa daha short ama yogun bir formulasyona donusturulmeli.
- Prompt; ana ozne, siluet, stil, malzeme, renk, kondisyon ve usage hissini tek akista birlestirmeli.
- Belirsiz kalite sloganlari, anlamsiz superlatifler veya image-model kaliplariyla sisirilmemeli.
- Game-ready veya production-ready such as iddialar ancak user explicitly o yone gittiyse ve required context verildiyse eklenmeli.
- Teknik notlar short, gercekci ve the user's ihtiyacina bagli olmali.
- Kullanici only prompt istiyorsa ek analysis uzatilmamali; ama bu, eksik girdilerde tek tur netlestirmeyi atlamak anlamina gelmemeli.

# Promotion Criteria

- Farkli Meshy senaryolarinda tutarli calisiyor olmali: prop, silah, karakter, creature, environment parcasi ve stylized collectible such as.
- Soru secimi tekrar tekrar dengeli sonuc veriyor olmali; the user gereksiz yormadan anlamli netlik saglamali.
- "Metin promptu ver, modeli uretme" guardrail'i different runtime'larda da guvenilir kalmali.
- Nihai output tek bir runtime'in syntax'ina asiri baglanmadan adapterlerde temsil edilebilmeli.
- Gercek usage exampleleri biriktiginde `skills/` altinda paketlenmeye ve gerekiyorsa `examples/` klasoru ile desteklenmeye ready sayilabilir.