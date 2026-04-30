---
name: branchable-chain-quest
description: Branching taskler, coklu gorev unlock gate'leri, quest chain progression ve tek seferlik chain tamamlandiktan sonra acilan daily questler iceren oyun quest sistemlerini tasarlamak, netlestirmek veya specification haline getirmek icin kullan.
---

# Branchable Chain Quest

## Use When

- Kullanici branchlere veya paralel task gruplarina ayrilabilen bir quest chain istediginde.
- Sonraki quest veya chain birden fazla onceki quest tamamlaninca acilmaliysa.
- Quest progression icin explicit `ALL`, `ANY` veya `COUNT` prerequisite logic gerekiyorsa.
- Daily questler sadece main, side, faction, tutorial veya onboarding chain tamamlandiktan sonra acilmaliysa.
- Istenen cikti final quest diyalogu veya engine-specific data degil, taranabilir quest logic spec ise.

## Workflow

1. Oyuncu progression baglamini, chain amacini ve istenen end-state'i belirle.
2. Tek seferlik chain content'i repeatable daily quest content'inden ayir.
3. Sistemi atomic quest node'larina bol; her node'a stable isim, amac, completion condition, reward intent ve dependency ver.
4. Branchleri paralel yollar, optional alternatifler veya zorunlu subchain'ler olarak map et.
5. Unlock gate'leri explicitly tanimla:
   - `ALL`: tum prerequisite'ler tamamlanmali.
   - `ANY`: prerequisite'lerden en az biri tamamlanmali.
   - `COUNT`: bir set icinden belirli sayida quest tamamlanmali.
6. Her unlock'in ne zaman tetiklenecegini tanimla: objective complete, quest turn-in, reward claim veya reset boundary sonrasi.
7. Sonraki chain'leri gate'lere bagla ve daily quest activation'i ayri bir final rule yap.
8. Edge case'leri kontrol et: abandon edilen questler, skipped branches, partial completion, replay, reset timing, reward duplication, account-wide versus character-specific unlocks ve daily unlock persistence.
9. Kritik bilgi eksikse tek kisa tur yuksek etkili soru sor; degilse konservatif varsayim yap ve isaretle.

## Output Expectations

- Default structure: `Quest System Summary`, `Quest Node List`, `Branch Map`, `Unlock Gates`, `Chain Completion Rules`, `Daily Quest Unlock Plan`, `Rewards and Progression Notes`, `Edge Cases`, `Open Questions`, `Acceptance Criteria`.
- Quest node'lari implementation-friendly ve kompakt olmali.
- Unlock rules test edilebilir olmali; "yeterince gorev yapinca" gibi muglak kosullardan kac.
- Branch, chain, gate ve daily loop kavramlarini ayri tut.
- Gerekliyse daily quest reset timing ve persistence varsayimlarini belirt.
- Kullanicinin vermedigi engine, backend, database veya live-ops destegini icat etme.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime-specific quest data schema'lari, Unity/Unreal implementation adimlari, editor otomasyonu veya backend scheduling detaylari adapter veya task-specific implementation isine aittir.
- Varsayilan task quest logic specification uretmektir; final narrative writing, localization ve code generation isleri kullanici istemedikce ayri follow-up tasklerdir.
