# Physical Content Inventory

## Source Root

Approved physical package content must come from existing prefab assets under:

```text
Assets/BlockCMailroom/Prefabs/PackIns
```

List the actual `.prefab` files from the current PDAI repository before assigning `PhysicalContents`. Use `assetPath` values first. Add GUIDs only if they were gathered from Unity or `AssetDatabase`.

## Ordinary

Use for packages whose contents should feel mundane, low-risk, or believable:

- documents
- books
- snacks
- cloths
- board
- printer

## Administrative

Use for office, routing, records, intake, or institutional clue packages:

- clipboard
- tags
- archive
- notebook

## Contraband / Tension

Use for suspicious but schema-compatible inspection tension:

- needle pen
- metal plate
- handcuffs
- push pins

## Medical

Use for clinical, care, hygiene, sickness, contamination, or ambiguous health packages:

- capsules
- ointment
- toothpaste
- bottle
- sponge
- soup

## Supernatural / Ruined

Use for horror-tension packages only when existing fields and verdict logic can support the clue:

- warm ash
- old photographs
- unsettling box

## Selection Rules

- Use only prefabs discovered under the source root.
- Prefer ordinary contents for `Release` and `Return` packages.
- Use medical, contraband, or ruined contents only when evidence and verdict logic support them.
- Do not invent new objects, broken variants, animated states, decals, particle effects, or scripted reactions.
- If a requested object is unavailable, select the closest existing prefab and state the substitution.
