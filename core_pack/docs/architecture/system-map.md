# System Map

> Project-level map. Fill this with `/sdd-map`. High-level components and how
> they relate — not an exhaustive file list.

## Components
| Component | Responsibility | Key locations |
|---|---|---|
|  |  |  |

## How they connect
_Describe the main flows between components._

## Platforms
_Multi-platform projects only (`.bvn-sdd/config.yml` `platforms:` > 1). Keep one
row per in-scope native tree plus the shared layer; delete this section for a
single-platform project. See `docs/standards/cross-platform.md`._
| Platform | Tree | Stack | Status |
|---|---|---|---|
| Shared (spec / contract) | docs/, contract | spec-pack is the single source of truth | |
| Android | android/ | Kotlin, Jetpack Compose | |
| iOS | ios/ | Swift, SwiftUI | |

## Shared contract layer
_The client/service contract and data model that every native tree consumes
identically. Both Android and iOS bind to this — it is never forked per platform._
