---
id: mh-blueprint-game-strategy-session-composer
title: Game Strategy Session Composer
type: blueprint
status: stable
version: 1.0.0
summary: Oyun fikri degerlendirme oturumlari icin dogru master ve modul kombinasyonunu secen kompozisyon taslagi.
tags:
  - composition
  - game-development
  - workflow
  - session
depends_on:
  - mh-master-ultimate-game-development-strategist-core
  - mh-module-steam-market-validation
  - mh-module-mvp-scope-reduction
  - mh-module-production-risk-strategy
  - mh-module-full-concept-greenlight
last_reviewed: 2026-04-03
input_contract: Kullanicinin bir oyun fikrini belirli bir amacla degerlendirmek istemesi.
output_contract: Uygun prompt kombinasyonu ve oturum icin kisa calistirma yonergesi.
notes: Farkli AI ortamlarindaki testlerde gecer not almis, dogru session composition secimi ve copy-paste oturum acilisi uretimi acisindan paketlenmeye hazir kompozisyon taslagi.
---

# Responsibility

Oturum amacina gore hangi master ve modullerin aktif olacagini secmek ve kullaniciyi gereksiz prompt yukunden kurtarmak.

# Trigger Signals

- "Bu fikri Steam acisindan degerlendir"
- "Bunu MVP'ye indir"
- "Uretim risklerine bak"
- "Tam greenlight analizi yap"
- "Acimasiz ve ticari gercekcilikle yorumla"

# Workflow

1. Kullanici talebinin asil amacini belirle.
2. Asagidaki kompozisyonlardan uygun olanini sec.
3. Gerekirse ek bir sertlik veya ton katmani ekle.
4. Kisa bir oturum acilis mesaji uret.
5. Sonucu kullanicinin direkt kopyalayabilecegi bicimde ver.

# Composition Map

## A) Steam potansiyeli degerlendirme
- Core
- Steam Market Validation
- Full Concept Greenlight

## B) MVP'ye indirgeme
- Core
- MVP Scope Reduction

## C) Uretim riski inceleme
- Core
- Production Risk Strategy

## D) Tam stratejik degerlendirme
- Core
- Steam Market Validation
- MVP Scope Reduction
- Production Risk Strategy
- Full Concept Greenlight

## E) Sert mod ust katmani
Asagidaki mesaj oturum basina eklenebilir:

Be brutally honest.
Do not protect the idea.
Prioritize commercial realism, scope discipline, and shippability.
If the concept is weak, say so directly.
If the concept is too large, reduce it aggressively.

# Output Expectations

- Hangi modullerin aktif oldugu net yazilmali.
- Oturum amaci tek cumlede acik olmali.
- Kullaniciya kopyala-yapistir hazir bir baslangic mesaji verilmelidir.
