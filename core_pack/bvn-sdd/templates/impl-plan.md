# Implementation Plan — <TICKET>

> A skeleton, not full code. Make the intent clear before writing. The HOW is
> split per native tree below. If `.bvn-sdd/config.yml` `platforms:` lists one
> platform, keep only that subsection and delete the others.

## Files to change

### Shared
| File | Reason | Add / Modify |
|---|---|---|
|  |  |  |

### Android
| File | Reason | Add / Modify |
|---|---|---|
|  |  |  |

### iOS
| File | Reason | Add / Modify |
|---|---|---|
|  |  |  |

## Classes / functions / methods
_What to add or modify, with intended input/output._

### Shared

### Android

### iOS

## Data / SQL intent
_Shared by default — both clients use the same data model / contract. For each
query: target table, where-conditions, expected volume, performance risk. Do not
paste full SQL unless necessary._

_Optional `### Android-local` / `### iOS-local` subsections only for on-device
cache differences (e.g. Room vs Core Data)._

## Validation / error / logging approach
_How errors are handled and what gets logged._

### Shared

### Android

### iOS

## Test approach
_What kinds of tests, what they will assert (full detail goes in test-plan.md)._

### Shared

### Android

### iOS

## Migration / rollback approach
_DB or data migration steps and how to roll back. If none, say so._

## Cross-platform parity check
_Behaviors that MUST be identical across platforms, and how each native impl
satisfies the same shared AC. Flag any intentional divergence and link it to an
open issue._
| Shared AC / behavior | Android impl | iOS impl | Identical? |
|---|---|---|---|
|  |  |  |  |

## Mode check
_Does this still fit the recommended mode? If DB/contract changes appeared,
recommend escalation. If two native trees are in scope, confirm mode is M3+._
