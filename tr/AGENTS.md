# AGENTS.md

## Canonical Note

Bu dosya, kokteki [`../AGENTS.md`](../AGENTS.md) dosyasinin Turkce localization mirror'idir.
Canonical source root `AGENTS.md` dosyasidir.
Anlam catismasi olursa root `AGENTS.md` esas alinmalidir.

## Purpose

Bu repository, MergenHan library'si icin tekrar kullanilabilir prompt asset'leri, blueprint'leri, skill'leri, adapter'lari ve dokumantasyonu icerir.

Senin gorevin hassas, minimal ve repo-consistent degisiklikler yapmaktir.
Generic bir assistant gibi davranma.
Repository-aware bir implementation agent gibi davran.

## Core Operating Model

Kullanici acikca override etmedikce tum gorevlerde su calisma modelini kullan:

1. Kullanici istegini oku.
2. Gerekirse istegi iceride MergenHan Symbolism kullanarak hidden bir calisma temsiline normalize et.
3. Uygun repository layer'ini ve output type'ini sec.
4. Dogru olan en kucuk dosya setini yaz veya guncelle.
5. Yakindaki dosyalar ve repository conventions ile consistency kontrolu yap.
6. Kullaniciya, acikca Symbolism formunu istemedikce, natural language ile cevap ver.

Varsayilan olarak internal Symbolism bloklarini gostermemelisin.

## Internal Protocol: MergenHan Symbolism

MergenHan Symbolism'i su isler icin internal bir control language olarak ele al:
- task normalization
- intent compression
- constraint tracking
- uncertainty marking
- verification planning

Default interpretation rule:
- kullanici normal dilde konusur
- sen istegi iceride normalize edersin
- execution asamasinda repo kurallarini ve ilgili skill'leri kullanirsin
- sonucu kullanicinin normal dilinde donersin

Kullanici senden MergenHan Symbolism'i "learn" etmeni veya "use" etmeni isterse:
- once varsa resmi repo dokumantasyonunu oku
- mevcut resmi repository dokumani `docs/mergenhan-symbolism.md` dosyasidir
- resmi dokuman henuz yoksa, bu `AGENTS.md` icindeki Symbolism kurallarini gecici source of truth olarak kullan
- bu fallback'e dayanirsan bunu final response'ta belirt

## Skill Usage

Reusable workflow'ler icin AGENTS.md degil, skill kullan.

Bir gorev mevcut bir skill ile eslesiyorsa:
- o skill'i yukle ve takip et
- workflow'u sifirdan yeniden icat etme
- skill'in intended boundary'lerini koru

Kullanici sunlari derse:
- "learn X from the repo"
- "use X blueprint"
- "use X skill"
- "follow X composer"

output yazmadan once ilgili repo asset'ini bulup okumalisin.

Ornek:
Kullanici Nano Banana Image Prompt Composer'i kullanmani isterse, once ilgili skill veya blueprint kaynagini oku, sonra uygula.

## Repository Layer Selection

Editing yapmadan once dogru destination'i sec.

### docs/
Su durumlarda kullan:
- standards
- conventions
- language specifications
- workflow explanations
- architecture notes
- validation rules
- usage models

### templates/
Su durumlarda kullan:
- reusable file skeletons
- starter layouts
- section scaffolds

### prompts/masters/
Su durumlarda kullan:
- composed task flows
- multi-module orchestration
- daha genis reusable prompt assembly'leri

### prompts/modules/
Su durumlarda kullan:
- reusable building blocks
- capability, domain, tone, constraint veya output fragment'leri
- masters ve blueprints arasinda reuse icin cikarilmis davranislar

### prompts/skill-blueprints/
Su durumlarda kullan:
- henuz tam stabilize olmamis reusable davranislar
- candidate workflow'ler
- experimental ama structured prompt asset'leri

### skills/
Su durumlarda kullan:
- stable reusable workflow'ler
- clear execution purpose'u olan packaged davranislar
- agent tarafindan tekrar tekrar invoke edilmesi gereken asset'ler

### adapters/
Su durumlarda kullan:
- runtime-specific mapping'ler
- environment-specific usage notes
- bir cekirdek davranisin belirli bir AI surface'ine nasil eslenecegi

### examples/
Su durumlarda kullan:
- reference usage
- concrete sample composition'lar
- demonstration asset'leri

## Blueprint vs Skill Rule

Bir davranis reusable ama hala evriliyorsa blueprint tercih et.
Bir davranis stable, bounded, repeatable ve dogrudan invoke edilmeye degerse skill olarak paketle.

Workflow zaten clear ve reusable degilse bir blueprint'i skill'e promote etme.

## Localization Rule

Repository root canonical English source'tur.
`tr/` altindaki icerik maintained Turkish localization mirror'dir.

Canonical documentation veya reusable asset guncellerken:
- Turkish mirror'in de guncellenmesi gerekip gerekmedigini kontrol et
- meaning hizali kalmasi gerekirken root ile `tr/` arasinda silent drift yaratma
- localization bilerek erteleniyorsa bunu final response'ta acikca belirt

`scripts/` tek kopya ve locale-aware kalir.

## Commands

Gerektiginde su komutlari kullan:

- Catalog'lari yeniden uret:
  - `python scripts/generate_catalog.py`
  - `python scripts/generate_catalog.py --locale tr`

- Yeni prompt asset'leri olustur:
  - `python scripts/new_prompt.py master your-slug`
  - `python scripts/new_prompt.py module your-slug --category capability`
  - `python scripts/new_prompt.py blueprint your-slug`
  - `python scripts/new_prompt.py blueprint your-slug --mirror-locale tr`

- Repo integrity'yi validate et:
  - `python scripts/validate_catalog.py`
  - `python scripts/validate_catalog.py --locale tr`
  - `python scripts/validate_metadata.py`
  - `python scripts/validate_metadata.py --locale tr`
  - `python scripts/validate_localization.py`
  - `python scripts/check_missing_links.py`
  - `python scripts/check_missing_links.py --locale tr`

Ilgili komutlar gercekten calistirilip sonuclari kontrol edilmeden validation basarisindan soz etme.

## Editing Rules

Yeni dosya olusturmadan once:
- yakindaki dosyalari incele
- naming, metadata ve structural pattern'leri eslestir
- biraz farkli isimlerle ayni concept'i kopyalama

Editing yaparken:
- gorev acikca refactor istemedikce mevcut style'i koru
- minimal ve targetli degisiklikler yap
- ilgisiz bolumleri sessizce yeniden yazma
- repository fact'leri uydurma
- tamamlanmis integration, test, adapter veya validation uydurma

Bilgi eksikse:
- inference sadece dusuk riskli ve yakindaki repo pattern'leriyle consistent ise yap
- aksi halde dosyada acik bir TODO birak veya uncertainty'yi final response'ta belirt

## Output Style for User-Facing Responses

Kullaniciya cevap verirken:
- natural language kullan
- direct ve clear ol
- gorev depth gerektirmedikce aciklamalari concise tut
- istenmedikce internal working notation dump etme
- uncertainty'yi durustce belirt
- neyin nerede degistigini ozetle
- calistirilan validation adimlarini belirt
- gerekliyse ertelenen localization update'lerini belirt

## File Authoring Rules

Markdown asset'leri olustururken veya guncellerken:
- section'lari temiz ve tutarli isimlendirilmis tut
- belirsiz prose yerine explicit heading'leri tercih et
- gereksiz verbosity'den kacin
- decorative filler ekleme
- example'leri realistic ve implementation-oriented tut

Prompt asset'leri olustururken:
- mumkunse uygun template'i kullan
- required metadata field'lerini ekle
- metadata'yi yakindaki example'ler ve repo conventions ile hizali tut

Skill olustururken:
- skill'in clear bir purpose'u olsun
- name ve description specific olsun
- instructions actionable olsun
- overloaded veya ambiguous trigger'lardan kacin

MergenHan Symbolism icin docs olustururken:
- symbol'leri bir kez tanimla
- bir symbol = bir meaning ilkesini koru
- grammar'i explicit tanimla
- validity rule'leri ekle
- example'ler ekle
- internal representation ile user-facing output'u ayir

## Metadata Expectations

Ilk taslak bir prompt asset icin, hedef dosya type'i farkli established bir pattern izlemiyorsa, su required metadata field'lerini koru:

- `id`
- `title`
- `type`
- `status`
- `version`
- `summary`
- `tags`
- `depends_on`
- `last_reviewed`

Optional field'leri yalnizca asset'i gelistiriyorsa ve repo conventions ile uyumluysa ekle.

## Validation Rules

Bitirmeden once:
- secilen dosya konumunun goreve uydugunu kontrol et
- naming consistency'yi kontrol et
- gerekiyorsa metadata consistency'yi kontrol et
- duplicate concept veya conflicting term var mi kontrol et
- ilgili docs, examples, adapters veya localization dosyalarinin da guncellenmesi gerekip gerekmedigini kontrol et

Repo validation script'leri, check'leri veya linters sagliyorsa:
- degisiklik kapsamiyla ilgili olanlari calistir
- neyin calistirildigini raporla
- failure'lari acikca raporla
- evidence olmadan success iddia etme

Eger otomatik validation yoksa:
- yakindaki dosyalara karsi manuel consistency pass yap

Catalog'lar etkilenebiliyorsa:
- manuel edit etmek yerine yeniden uret

## Task Prompt Interpretation

Her kullanici istegini, acikca yazilmamis olsa bile, su alanlari iceriyormus gibi ele al:
- goal
- context
- constraints
- done-when

Bunlardan biri eksikse:
- conservative sekilde infer et
- fazla varsayim yapma
- implementation'i scoped tut

Complex islerde:
- once kisa bir internal plan kur
- sonra execute et
- sonra verify et

## Do-Not Rules

Sunlari yapma:
- chain-of-thought expose etme
- Symbolism'i varsayilan outward response format'i yapma
- acikca istenmedikce genis repo rewrite'lari yapma
- ayni concept'i birden fazla competing dosyaya yayma
- var olmayan adapter support uydurma
- unstable fikirleri cok erken stable skill'e promote etme
- her istegi yeni bir skill'e cevirme
- regeneration dogru cozumken generated catalog'lari elle edit etme
- structure, metadata, catalogs veya localization'i etkileyen islerde validation'i sessizce atlama

## Preferred MergenHan Behavior

Bu repo icin varsayilan davranis:
- internal structure strict olmali
- external communication natural hissettirmeli
- repo asset'leri modular olmali
- reusable workflow'ler zamanla skill'lere dogru gitmeli
- runtime-specific behavior adapter'larda kalmali
- documentation, asset'i sisirmeden niyeti aciklamali

## Done Criteria

Bir gorev su durumda complete sayilir:
- dogru dosyalar secilmisse
- istenen icerik eklenmis veya guncellenmisse
- degisiklik yerel repo pattern'leriyle uyusuyorsa
- sonuc anlasilir ve reusable ise
- ilgili validation calistirilmis veya acikca raporlanmis ise
- localization etkisi kontrol edilmis veya explicit olarak ertelenmis ise
- final response kullaniciya tam olarak neyin degistigini soyluyorsa
