# Package Content Contract

## Core PDAI Path Anchors

Locate these files in the current PDAI repository before authoring or revising content:

- `PackageInspectionData.cs`: schema source for `PackageInspectionRecord`, verdict enums, evidence fields, inspection text fields, and optional mutation fields.
- `PackageInspectionDatabase.asset`: canonical Unity database asset when working inside the project.
- `PackageContentsRevealProfile.cs`: rules and data shape for revealing package contents.
- `PackageDecisionValidator.cs`: verdict, evidence, progression, and package consistency checks.
- `PackageInspectionDatabaseJsonUtility.cs`: preferred JSON export/import and dry-run import surface.

Do not rely on stale remembered paths. Find the current file locations in the working PDAI repo and cite what was inspected.

## Authoring Constraint

This skill may modify or propose only:

- package content data
- localization text
- existing prefab references

This skill must not add or request:

- new gameplay features
- new scripts or runtime systems
- new editor tools
- new Unity components
- new validators
- new physical prefabs
- new mechanics required to make a package concept work

If a concept needs a new system, label it out of scope and either simplify it to fit existing fields or ask the user to start a separate feature-spec task.

## Required Progression

- Preserve the canonical 24-package demo progression from `BCM_001` through `BCM_024`.
- Preserve package order unless the user explicitly requests a progression or validator change.
- Preserve existing `PrimaryLessonId` values unless the user explicitly requests validator changes.
- Do not silently add, remove, renumber, or split package IDs.

## Verdict Rules

### `Release`

Use `Release` only when all conditions are clean:

- registry is clean
- weight is within range
- seal is clean
- actual contents match declared contents
- evidence does not imply isolation, disposal, or administrative return

### `Return`

Use `Return` when the problem is administrative and the physical contents are ordinary:

- there is an admin, registry, routing, recipient, address, documentation, or intake issue
- contents are ordinary or non-hazardous
- there is no physical hazard
- the evidence does not justify isolation or disposal

### `Quarantine`

Use `Quarantine` when isolation evidence is present:

- evidence supports containment, contamination, infection, supernatural bleed-through, unstable contents, or unresolved package risk
- package does not include `NoRoutingValue`
- disposal is not the primary supported action

### `Destroy`

Use `Destroy` only when disposal evidence is explicit:

- evidence includes `NoRoutingValue`
- package has disposal evidence, such as unrecoverable contamination, forbidden routing value, terminal hazard, or validator-supported destruction rationale
- the rationale distinguishes destruction from quarantine

## Consistency Checks

Before presenting content, check:

- package ID remains in the requested range
- enum names match the current schema
- evidence tags support the selected verdict
- `DeclaredContents` and `ActualContents` create the intended clue relationship
- `PhysicalContents` paths exist under the approved PackIns source
- localization keys use `Package.<PackageId>.*`
- no proposed content requires new scripts, systems, mechanics, or prefabs
