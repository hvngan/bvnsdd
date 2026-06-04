# Context & Rules — <TICKET>

> The concrete facts the implementation must respect, verified against source.
> The patterns below are split per platform. If `.bvn-sdd/config.yml`
> `platforms:` lists one platform, keep only that subsection and delete the
> others.

## Correct examples in the codebase
_Existing implementations to follow (file path + why it's a good model)._

### Shared
_Examples that apply regardless of platform (contract usage, shared rules)._

### Android patterns
_Kotlin / Jetpack Compose models to follow, verified against `android/`._

### iOS patterns
_Swift / SwiftUI models to follow, verified against `ios/`._

## Allowed vs. forbidden patterns

### Shared
- Allowed:
- Forbidden:

### Android patterns
- Allowed:
- Forbidden:

### iOS patterns
- Allowed:
- Forbidden:

## Methods / classes that actually exist
_Confirmed available (do not invent APIs). Note any that must NOT be used._

### Shared
_Contract / shared types confirmed available._

### Android patterns
_Confirmed available in `android/` (verify with Grep/Read)._

### iOS patterns
_Confirmed available in `ios/` (verify with Grep/Read)._

## DTO / Entity / Table mappings
_Shared across platforms — both native clients map to the same contract._
| Concept | DTO | Entity | Table |
|---|---|---|---|
|  |  |  |  |

## Master data / code-value mappings
_Shared across platforms. Enumerations, status codes, lookup values relevant to
this ticket._

## Encoding / multi-language notes
_Shared across platforms. Character set, full-width handling, i18n concerns._
