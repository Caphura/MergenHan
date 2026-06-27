# Physical Content Inventory

## Source Root

Approved physical package content existing prefab asset'lerinden gelmelidir:

```text
Assets/BlockCMailroom/Prefabs/PackIns
```

`PhysicalContents` atamadan once current PDAI repository'deki actual `.prefab` file'larini listele. Once `assetPath` value'larini kullan. GUID'leri yalnizca Unity veya `AssetDatabase` ile toplandiysa ekle.

## Ordinary

Mundane, low-risk veya believable hissettirmesi gereken package'lar icin kullan:

- documents
- books
- snacks
- cloths
- board
- printer

## Administrative

Office, routing, records, intake veya institutional clue package'lari icin kullan:

- clipboard
- tags
- archive
- notebook

## Contraband / Tension

Suspicious ama schema-compatible inspection tension icin kullan:

- needle pen
- metal plate
- handcuffs
- push pins

## Medical

Clinical, care, hygiene, sickness, contamination veya ambiguous health package'lari icin kullan:

- capsules
- ointment
- toothpaste
- bottle
- sponge
- soup

## Supernatural / Ruined

Horror-tension package'lari icin yalnizca existing field'lar ve verdict logic clue'yu destekliyorsa kullan:

- warm ash
- old photographs
- unsettling box

## Selection Rules

- Sadece source root altinda discovered prefab'lari kullan.
- `Release` ve `Return` package'lari icin ordinary contents tercih et.
- Medical, contraband veya ruined contents'i yalnizca evidence ve verdict logic destekliyorsa kullan.
- Yeni object, broken variant, animated state, decal, particle effect veya scripted reaction uydurma.
- Requested object yoksa en yakin existing prefab'i sec ve substitution'i belirt.
