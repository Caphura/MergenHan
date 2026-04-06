# Resume Composer Test Pack

Bu belge, `Resume Composer` icin farkli AI ortamlarda uygulanabilecek test senaryolarini toplar. Amac, modelin yalnizca guzel gorunen bir CV / resume yazmasini degil; mevcut resume veya ham kariyer notlarini evidence-only, ATS-friendly ve gerekiyorsa role-tailored bir ciktiya donusturmesini test etmektir.

## Kullanim Sekli

Her testten once asagidaki acilis talimatini kullan:

```text
Asagidaki resume / CV, kariyer notlari veya inspectable kanitlari ATS-friendly bir resume draftina donustur. Ama hemen uzun bir final draft yazmaya atlama. Once girdinin mevcut resume mi, ham not mu, inspectable evidence mi, job post destekli tailoring istegi mi, yoksa export review mu oldugunu belirle. Eger ekran goruntusu, PDF, repo, local belge veya public link gibi inspectable materyal verilmis ise once onu tara. Eger kritik eksik hala varsa en fazla 1 kisa turda 2-4 yuksek etkili soru sor. Sonra sonucu su yapida ver:

1. Candidate Summary
2. Target Role Fit
3. Resume Draft
4. Weak Spots / Missing Inputs
5. Optional Tailoring Notes

Varsayilan final cikti English olsun. Uydurma metric, title, tarih, degree veya ownership ekleme.
```

## Test Senaryolari

### RC1 - Mevcut resume + job post tailoring

**Amac:** Model, mevcut resume'yi ilanla eslestirip tailoring yapabiliyor mu?

**Test girdisi:**

```text
Current resume notes:
- Operations Specialist, 2021-present
- Managed onboarding for new B2B clients
- Coordinated weekly reporting with sales and support
- Improved internal process documentation
- Worked with CRM and spreadsheets

Target job post summary:
Customer Success Operations Analyst
- improve onboarding workflows
- own KPI reporting
- partner with sales, support, and account managers
- strong process improvement mindset
- experience with CRM tools and cross-functional coordination

Please tailor my resume for this role.
```

**Beklenen guclu davranis:**

- Mevcut resume + job post modunu dogru okuyup tailoring yapmali
- Target Role Fit bolumunde role alignment'i gorunur kilmali
- Resume Draft'ta ilanla desteklenen keyword ve sorumluluklari spam yapmadan yansitmali

**Kirmizi bayraklar:**

- Job post varken genel-purpose resume vermek
- Ilanla desteklenmeyen keyword veya ownership uydurmak

### RC2 - Ham kariyer notlarindan sifirdan draft

**Amac:** Model, daginik kariyer notlarindan mantikli bir resume iskeleti kurabiliyor mu?

**Test girdisi:**

```text
I do not have a formal resume yet. Here are rough notes:
- 4 years in office operations
- handled vendor communication
- scheduled interviews and onboarding sessions
- built simple reporting sheets
- helped leadership prepare weekly updates
- often fixed messy internal processes
- want to apply to operations coordinator roles
```

**Beklenen guclu davranis:**

- Raw-notes mode'u dogru tespit etmeli
- Candidate Summary ve Resume Draft'i sifirdan anlamli sekilde kurmali
- Bullet'lari action + ownership + outcome mantigina yaklastirmali

**Kirmizi bayraklar:**

- Sanki tam resume varmis gibi davranmak
- Ham notlari sadece yeniden siralamak ama guclu bullet'a cevirmemek

### RC3 - Eksik veri ve tek kisa netlestirme turu

**Amac:** Model, kritik eksik bilgi oldugunda en fazla 1 kisa turla netlestirme yapabiliyor mu?

**Test girdisi:**

```text
Please rewrite my resume for better ATS performance.
I worked in administration and project support for several years, helped teams stay organized, prepared documents, and handled coordination.
```

**Beklenen guclu davranis:**

- Hemen uydurma yapmadan once eksik target role ve impact alanlarini fark etmeli
- En fazla 1 kisa turda 2-4 yuksek etkili soru sormali
- Sorular uzun anket gibi olmamali

**Kirmizi bayraklar:**

- Hic soru sormadan asiri spesifik final draft yazmak
- Uzun, yorucu ve dusuk etkili soru listesi acmak

### RC4 - Uydurma metric baskisina direnc

**Amac:** Model, kullanici baski yapsa bile gucsuz veriyi uydurma metric ile doldurmuyor mu?

**Test girdisi:**

```text
Make my resume sound much stronger. I do not know the exact numbers, so just add realistic metrics where needed.
```

**Beklenen guclu davranis:**

- Uydurma metric, title veya ownership eklemeyi reddetmeli
- Gercekten eksik olan yerleri Weak Spots / Missing Inputs altinda gostermeli
- Yine de dili daha guclu hale getirecek evidence-safe yeniden yazim yapmali

**Kirmizi bayraklar:**

- Tahmini metrikleri sanki gercekmis gibi yazmak
- Guclendirme bahanesiyle sahte basari uretmek

### RC5 - Uzun anlatidan guclu bullet rewrite

**Amac:** Model, daginik ve uzun deneyim anlatimini taranabilir bullet'lara cevirebiliyor mu?

**Test girdisi:**

```text
Here is one long experience description:
I was basically the person everyone went to when something needed to be organized, whether it was meeting prep, document cleanup, onboarding support, or following up with different teams, and I also spent a lot of time making sure reports were updated and that leadership had what they needed before weekly meetings.

Turn this into strong resume bullets.
```

**Beklenen guclu davranis:**

- Uzun paragrafi 2-4 taranabilir bullet'a cevirmeli
- Bullet'lari result / ownership odakli yapmali
- Asiri kurumsal sisirme yerine net kalmali

**Kirmizi bayraklar:**

- Paragrafi neredeyse aynen tasimak
- Sonuc ve ownership'i tamamen kaybetmek

### RC6 - Job post yok, genel ATS baseline

**Amac:** Model, job post olmadan da temiz bir genel-purpose ATS draft uretebiliyor mu?

**Test girdisi:**

```text
Please improve my resume for ATS, but I do not have a specific job post yet. I want a clean baseline version for general operations and coordinator roles.
```

**Beklenen guclu davranis:**

- Target Role Fit'i genel baseline seviyesinde tutmali
- Tailoring varmis gibi spesifik keyword mapping yapmamali
- Resume Draft genel-purpose ama guclu olmali

**Kirmizi bayraklar:**

- Job post yokken sahte tailoring yapmak
- Fazla genel ve ayirt edici olmayan ciktida kalmak

### RC7 - EN-first davranis

**Amac:** Model, varsayilan final ciktiyi English uretirken kullanici diline netlestirme seviyesinde uyum saglayabiliyor mu?

**Test girdisi:**

```text
CV'mi ATS icin guclendirmek istiyorum. Elimde birkac deneyim notu var ama finali Ingilizce resume olarak istiyorum.
```

**Beklenen guclu davranis:**

- Final drafti English uretmeli
- Gerekirse netlestirme sorularini kullanicinin diline uyumlu tutabilir
- EN-first varsayimini korurken kullaniciyi yabancilastirmamali

**Kirmizi bayraklar:**

- Varsayilan olarak Turkce final resume vermek
- Dil tercihine dair net sinyali kacirmak

### RC8 - Screenshot + public evidence + local artifact reconstruction

**Amac:** Model, temiz resume olmadan da karisik kanitlardan desteklenebilir bir profile cikartabiliyor mu?

**Test girdisi:**

```text
I do not have a clean resume. I will give you LinkedIn screenshots, a Canva-exported PDF, GitHub repos, and two public articles about a game project. Build a one-page English resume from that evidence and do not invent anything.
```

**Beklenen guclu davranis:**

- Input'u inspectable evidence pack olarak dogru tespit etmeli
- Soru sormadan once ekran goruntusu, PDF, repo ve public source'lardan veri toplama egilimi gostermeli
- Verified, user-asserted ve inferred sinyalleri birbirine karistirmamali
- Final positioning'i generic corporate filler yerine domain'e uygun kurmali

**Kirmizi bayraklar:**

- Kanitlar ortadayken hemen soru listesi acmak
- Zayif sinyalleri verified employment / degree claim'e cevirmek
- Teknik veya oyun odakli profili genele indirmek

### RC9 - One-page compression discipline

**Amac:** Model, guclu ama uzun materyali gercekten tek sayfaya uygun copy'ye sikistirabiliyor mu?

**Test girdisi:**

```text
I already have a long draft resume, but I need a one-page final version for applications. Keep the strongest signals, remove repetition, and preserve my role progression.
```

**Beklenen guclu davranis:**

- Tekrarlari budamali
- Stacked-role progression'i kaybetmemeli
- En guclu teknik veya domain sinyallerini saklamali
- Sonuc gercekten kisa ve taranabilir olmali

**Kirmizi bayraklar:**

- One-page isterken hala iki sayfalik yogunlukta copy vermek
- Sikistirma bahanesiyle deneyim akisini bozmak

### RC10 - Export QA / placeholder audit

**Amac:** Model, guzel yazmanin otesinde export edilmis resume'deki somut kalite sorunlarini yakalayabiliyor mu?

**Test girdisi:**

```text
Review this exported PDF of my resume. I want you to tell me what is broken, misleading, placeholder, or likely to hurt ATS readability.
```

**Beklenen guclu davranis:**

- Findings-first review yapmali
- Placeholder adres / telefon, unsupported education claim, merged lines ve generic filler gibi sorunlari kirmizi bayrak olarak isaretlemeli
- Gerekirse duzeltme yonu da onermeli

**Kirmizi bayraklar:**

- Sadece gorunuse dair genel yorum yapmak
- Somut copy / claim / ATS sorunlarini kacirmak

## Onerilen Test Sirasi

1. `RC2`
2. `RC1`
3. `RC3`
4. `RC5`
5. `RC4`
6. `RC6`
7. `RC7`
8. `RC8`
9. `RC9`
10. `RC10`

Bu sira, sifirdan iskelet kurmadan kanit rekonstruksiyonu ve export QA stresine dogru ilerler.

## Puanlama Rubrigi

| Olcut | Ne aranir? |
| --- | --- |
| Input Triage | Existing resume, raw notes, inspectable evidence, hybrid ve review modlarini dogru ayirabiliyor mu |
| Clarification Discipline | En fazla 1 kisa turda yuksek etkili soru soruyor mu |
| Evidence Discipline | Uydurma metric, title, tarih, degree veya ownership eklemeden kaliyor mu |
| Evidence Intake | Ekran goruntusu, PDF, repo ve public source gibi inspectable girdileri kullanabiliyor mu |
| ATS Clarity | Draft ATS-friendly ama okunur kaliyor mu |
| Tailoring Quality | Job post varsa alignment gorunur mu, yoksa gereksiz tailoring yapmiyor mu |
| Compression Quality | One-page modunda tekrarli copy'yi buduyor ve role progression'i koruyor mu |
| Export QA | Placeholder, unsupported claim ve merged copy gibi sorunlari yakaliyor mu |
| Output Readability | Candidate Summary, Resume Draft ve diger bolumler taranabilir mi |
| EN-first Behavior | Varsayilan final cikti English mi |

## Kisa Sonuc Formu

```text
AI:
Test ID:
Input triage dogru muydu:
Netlestirme turu dengeli miydi:
Inspectable evidence kullanildi mi:
Uydurma veri yok muydu:
Tailoring veya compression gorunur muydu:
Export QA varsa yeterli miydi:
Final output ATS-friendly ve okunur muydu:
En guclu yani:
En zayif yani:
Tekrar dener miydim: Evet / Hayir
```
