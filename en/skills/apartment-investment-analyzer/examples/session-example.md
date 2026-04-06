# Apartment Investment Analysis Session Example

This example tek bir apartman satis listinginin `Apartment Investment Analyzer` by how decision destekleyici bir investment analizine donusturulecegini gostermek icin is prepared.

## Raw Request

Kadikoy'de 2+1, 85 m2, 12 yasinda bir daire. Fiyat 6.450.000 TL. Ilanda metroya yakin, kiracili ve maintenanceli oldugu yaziyor. Bu listing investment icin mantikli mi?

## Expected Clarification Points

- Net m2 mi brut m2 mi oldugu clear mi?
- Mevcut kira bilgisi veya bolgedeki muhtemel kira araligi var mi?
- Binanin aidat, otopark, asansor such as kiralanabilirligi etkileyen unsurlari biliniyor mu?
- Ilan metnindeki "maintenanceli" ve "metroya yakin" ifadeleri what kadar evidenceli?

## Example Response Shape

### Scope Summary

- Talep tek bir apartman satis listinginin investment mantigini hizli ama dikkatli bicimde degerlendirmek.
- Elde fiyat, temel tipoloji ve bazi listing iddialari var; kira verisi ve detayli emsal seti eksik.

### Market Snapshot

- Kadikoy such as talebin yuksek oldugu bir bolgede kiralanabilirlik genelde guclu olabilir.
- Ancak bu listingin piyasa altinda mi, civarinda mi, ustunde mi oldugunu soylemek icin emsal ve net alan verisi gerekir.

### Listing-by-Listing Analysis

- 2+1 ve 85 m2 bandi kiraci hedefi acisindan genis bir request kitlesine hitap edebilir.
- 12 yasinda olmasi cok yeni bina primi tasimadigini ama asiri eski stok riskinde de olmayabilecegini dusundurur.
- "Kiracili" bilgisi nakit akisi acisindan olumlu olabilir; ancak mevcut kira seviyesi bilinmedigi icin bu avantaj tam olculmuyor.

### Rental Potential

- Metroya yakinlik dogruysa kiralanabilirlik side arti puan olabilir.
- Mevcut kira kontrati ve bolgedeki benzer 2+1 kiralari gorulmeden saglam kira araligi kurmak erken olur.

### Payback / Yield Estimate

- Bu asamada only kaba mantik kurulabilir; kesin brut getiri hesabi icin current kira araligi gerekir.
- Mevcut fiyat seviyesinde, kira beklenenden zayif kalirsa geri donus suresi hizla uzayabilir.

### Risks and Unknowns

- Net alan, mevcut kira, aidat ve bina teknik durumu bilinmiyor.
- Ilan kalitesi dusukse "maintenanceli" such as ifadeler abartili olabilir.
- Piyasa ustu fiyatlama riski, emsal gormeden elenemez.

### Top Candidates

- Tek listing oldugu icin here "aday" yerine mevcut listingin izlenmesi gereken kritik decision noktasi one cikar:
- Ilan ancak kira seviyesi ve emsal fiyat bandi dogrulandiginda guclu aday sayilabilir.

### Recommended Next Checks

- Ayni mikrolokasyonda benzer 2+1 satis emsallerini topla.
- Mevcut kira kontratini ve kiracinin odedigi rakami ogren.
- Net m2 ve aidat bilgisini dogrula.
- Ilanda one surulen lokasyon avantajlarini harita uzerinden kontrol et.
