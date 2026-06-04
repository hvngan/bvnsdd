# ウォークスルー：単一の共有スペックから Android + iOS の WeatherNow を構築

**シナリオ**：*WeatherNow* を **2 つのネイティブアプリとして同時に**構築します —
Android（Kotlin / Jetpack Compose）と iOS（Swift / SwiftUI）を、**単一の共有スペック**
で駆動します。プラットフォーム固有の作業はアーティファクト内できれいに分離されます。

> これは**ドキュメント例**です — マルチプラットフォームモードでアーティファクトが
> どう見えるかを示すもので、実行すべき実コードではありません。`EXAMPLE-ios-weather-en.md`
>（単一プラットフォーム）と比較すると、分割が何をもたらすかが分かります。

**アプリ概要**

| | |
|---|---|
| プラットフォーム | Android（Kotlin, Jetpack Compose）**+** iOS（Swift, SwiftUI） |
| 信頼できる唯一の情報源 | `spec-pack.md` — WHAT（受け入れ基準、コントラクト） |
| リポジトリ構成 | モノレポ：`android/` + `ios/` + `docs/` |
| 本ウォークスルーのチケット | **T-001** — 現在の天気画面（位置情報ベース） |
| 外部 API | OpenWeatherMap REST API（1 つのコントラクト、両クライアント共通） |

モデルと判断ルールの詳細は `docs/standards/cross-platform.md` を参照してください。

---

## 0. セットアップ — 両プラットフォームを宣言

```bash
bvn-sdd init --here --lang ja
```

次に `.bvn-sdd/config.yml` を編集して両プラットフォームを列挙します — **この 1 行が
すべてのアーティファクトで Shared / Android / iOS の分割を有効化**します：

```yaml
platforms:
  - android
  - ios

platform_stack:
  shared: "spec-pack が信頼できる唯一の情報源（WHAT）"
  android: "Kotlin, Jetpack Compose"
  ios: "Swift, SwiftUI"
```

**Claude Code** でプロジェクトを開き `/sdd-phase0a` を実行し、両ネイティブツリー
（`android/`, `ios/`）と共有 OpenWeatherMap コントラクトを記述します。

---

## Phase 0-B — ソースインテリジェンス（`/sdd-map`）

`platforms:` が 2 つを列挙するため、`system-map.md` は共有スペック/コントラクト
レイヤーに加えて、ネイティブツリーごとのレイヤーを持ちます：

```markdown
# System Map — WeatherNow（マルチプラットフォーム）
## Status: GREEN-FIELD — 全エントリ [PLANNED]

## Platforms
| Platform | Tree | Stack | Status |
|---|---|---|---|
| Shared（spec / contract） | docs/, contract | spec-pack SSOT | [PLANNED] |
| Android | android/ | Kotlin, Jetpack Compose, MVVM | [PLANNED] |
| iOS | ios/ | Swift, SwiftUI, MVVM | [PLANNED] |

## Shared contract layer
- WeatherService.getCurrentWeather(lat, lon) -> WeatherData
  （OpenWeatherMap GET /data/2.5/weather — 両クライアントで同一の request/response）
- WeatherData { city, tempC, description, iconCode, observedAt }
```

---

## T-001 — 現在の天気画面

### ブートストラップ — `/sdd-new T-001 Current weather screen`

1 つのチケットフォルダ、1 つの共有スペック。後続のアーティファクトが
Shared / Android / iOS の分割を持ちます。

---

### Phase 1 — Spec Pack（`/sdd-spec T-001`）

スペックは WHAT について**プラットフォーム中立**を保ちます。プラットフォームは
*サーフェス影響*（§8）としてのみ現れ、コントラクトは単数のまま（§9）です。

```markdown
# Spec Pack — T-001: 現在の天気画面

## 6. Acceptance Criteria        （中立 — ここに Kotlin/Swift は書かない）
- [ ] AC-1: 初回起動時に位置情報の許可を要求する。
- [ ] AC-2: 許可拒否 → 「位置情報へのアクセスが必要」+ OS 設定を開く手段を表示。
- [ ] AC-3: 許可付与 → 共有サービスから天気を取得。
- [ ] AC-4: 都市名、気温（°C）、説明、天気アイコンを表示。
- [ ] AC-5: 取得中はローディング表示。
- [ ] AC-6: キャッシュありのネットワーク障害 → キャッシュ +「X 分前に更新」を表示。
- [ ] AC-7: キャッシュなしのネットワーク障害 →「接続なし」+ 再試行。
- [ ] AC-8: プルして更新で手動リロード。

## 8. Surface impact (per platform)
| Platform | 影響する画面 / サーフェス | 影響する Backend / API | データ / イベント |
|---|---|---|---|
| Shared（contract） | — | OpenWeatherMap GET /weather | WeatherData モデル |
| Android | CurrentWeather Compose 画面 | （共有サービス経由） | ローカルキャッシュ（DataStore） |
| iOS | CurrentWeather SwiftUI 画面 | （共有サービス経由） | ローカルキャッシュ（UserDefaults） |

## 9. Client/Service contract（プラットフォーム中立）
GET /data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}
Response → WeatherData { city: String, tempC: Double, description: String,
           iconCode: String, observedAt: epochSeconds }
Android と iOS は同一に消費する。[android-only]/[ios-only] フィールドなし。

## 15. Complexity Classification
1 つのスペックから 2 つのネイティブツリー → マルチプラットフォーム要因 → M3+ を推奨。
```

---

### Phase 1-B — ライトサイジング（`/sdd-rightsize T-001`）

**マルチプラットフォーム要因**が下限を **M3** に引き上げます：

```markdown
# Mode Decision — T-001

## Scoring
- Reversibility: 2 | Uncertainty: 2 | Risk: 1 | Scope: 3（1 スペックから 2 ネイティブツリー）

## マルチプラットフォーム要因
platforms: [android, ios] → Scope = 3 寄与 → モード下限 M3 を適用。

## 決定: M3（Plus）
## 適応ワークフロー: sdd-context → sdd-plan → sdd-implement → sdd-test → sdd-blackbox → sdd-report
```

> 注: モードは各フェーズの「深さ」を決めるもので、どのフェーズを実行するかではありま
> せん。すべてのチケットは上記の全シーケンスを実行します。軽いモード（例: M1）でも各
> アーティファクトを簡潔にするだけで、全フェーズを実行します。停止するのは MX のみ。

---

### Phase 2 — Context（`/sdd-context T-001`）

`context.md` と `source-map.md` はネイティブツリーごとに分割し、コントラクト/
データモデルは共有のまま保ちます。

```markdown
# Context — T-001

## Allowed vs. forbidden patterns
### Shared
- 許可: WeatherData コントラクトを両クライアントで同一にマップ。
- 禁止: プラットフォームごとにフィールド名や単位をフォーク。
### Android patterns
- 許可: Jetpack ViewModel + StateFlow による @Observable 風 ViewModel；Compose の state hoisting。
- 禁止: @Composable からのネットワーク呼び出し。
### iOS patterns
- 許可: @Observable ViewModel（iOS 17）、@MainActor での state 変更。
- 禁止: SwiftUI View からの URLSession 呼び出し；新規コードでの DispatchQueue.main。

## DTO / Entity / Table mappings
_プラットフォーム間で共有 — 両クライアントは同一の WeatherData コントラクトにマップする。_
```

```markdown
# Source Map — T-001

## Files likely to change
### Shared
| File | 想定変更 |
| docs/changes/T-001/spec-pack.md (contract) | 唯一の WeatherData コントラクト |
### Android (android/…)
| android/.../CurrentWeatherViewModel.kt | 新規 — StateFlow<ViewState> |
| android/.../CurrentWeatherScreen.kt | 新規 — Compose 画面 |
### iOS (ios/…)
| ios/.../CurrentWeatherViewModel.swift | 新規 — @Observable ViewModel |
| ios/.../CurrentWeatherView.swift | 新規 — SwiftUI 画面 |
```

---

### Phase 3 — Plan（`/sdd-plan T-001`）

`impl-plan.md` は HOW を分割し、**Cross-platform parity check** を追加します。

```markdown
# Implementation Plan — T-001

## Classes / functions / methods
### Android
- CurrentWeatherViewModel.loadWeather(): ViewState.Loading を設定 → 共有サービス呼び出し → Loaded/Error。
- CurrentWeatherScreen: when(state) → Loading / Loaded / PermissionDenied / Error。
### iOS
- CurrentWeatherViewModel.loadWeather() @MainActor: .loading → 共有サービス → .loaded/.error。
- CurrentWeatherView: switch state → ProgressView / コンテンツ / denied / error。

## Cross-platform parity check
| 共有 AC / 振る舞い | Android impl | iOS impl | 同一? |
|---|---|---|---|
| AC-3 許可時の fetch | 初回コンポジションで loadWeather() | .task 内で loadWeather() | はい |
| AC-6 古いキャッシュバナー | DataStore キャッシュ + バナー | UserDefaults キャッシュ + バナー | はい（同一テキスト/閾値） |
| AC-2 設定を開く | Intent → アプリ設定 | UIApplication openSettingsURL | サーフェス相違（OI-1） |

## Mode check
スコープに 2 つのネイティブツリー → モード M3 を確認。
```

意図的な相違（AC-2 のディープリンク手段）は `open-issues.md` に OI-1 として記録 —
観測される結果は同一（「ユーザーが OS 設定に到達」）、ネイティブ API は異なる。

---

### Phase 4+5 — 実装（`/sdd-implement T-001`）

各ツリーは**同一スペック**から、それぞれのイディオムで実装 — 混入なし。

**Android — `android/.../CurrentWeatherViewModel.kt`**
```kotlin
class CurrentWeatherViewModel(
    private val repo: WeatherRepository,
    private val location: LocationService,
) : ViewModel() {
    private val _state = MutableStateFlow<ViewState>(ViewState.Idle)
    val state: StateFlow<ViewState> = _state.asStateFlow()

    fun loadWeather() = viewModelScope.launch {
        _state.value = ViewState.Loading
        runCatching {
            val loc = location.current()
            repo.fetchCurrentWeather(loc.lat, loc.lon)
        }.onSuccess { _state.value = ViewState.Loaded(it) }
         .onFailure { _state.value = repo.cached()?.let(ViewState::Loaded)
                                       ?: ViewState.Error(it.message.orEmpty()) }
    }
}
```

**iOS — `ios/.../CurrentWeatherViewModel.swift`**
```swift
@Observable final class CurrentWeatherViewModel {
    enum ViewState { case idle, loading, loaded(WeatherData), denied, error(String) }
    private(set) var state: ViewState = .idle

    @MainActor func loadWeather() async {
        state = .loading
        do {
            let loc = try await location.current()
            state = .loaded(try await repo.fetchCurrentWeather(lat: loc.lat, lon: loc.lon))
        } catch {
            state = repo.cached().map(ViewState.loaded) ?? .error(error.localizedDescription)
        }
    }
}
```

両者は AC-3、AC-5、AC-6 を同一に満たす。self-review の前に `review-checklist.md`
の **Cross-platform consistency** セクションをチェックする。

---

### Phase 6 — Test（`/sdd-test T-001`）

AC↔test マトリクスに **Platform** 列が加わり、parity テストが同一入力に対する
同一出力を保証します。

```markdown
## AC ↔ test matrix
| AC | Platform | テスト種別 | テスト名 / 場所 | 優先度 |
| AC-3 | Android | unit | CurrentWeatherViewModelTest.loadSuccess | H |
| AC-3 | iOS | unit | CurrentWeatherViewModelTests.loadSuccess | H |
| AC-3 | Shared | contract | WeatherContractTest（fixture JSON → WeatherData） | H |
| AC-6 | Android | unit | ...networkError_withCache | H |
| AC-6 | iOS | unit | ...networkError_withCache | H |

## Run commands
# Android
./gradlew :app:testDebugUnitTest
# iOS
xcodebuild test -scheme WeatherNow -destination 'platform=iOS Simulator,name=iPhone 15'
```

---

### Phase 7 — ブラックボックス（`/sdd-blackbox T-001`）

ケースは共有スペックのみから導出し、各ケースに `Platform:` を付与。観測される
振る舞いが同一 → 1 つの `Both` ケース；サーフェスが異なる → プラットフォーム
ごとに 1 ケース。

```markdown
## AC coverage map
| AC | Platform | Happy path | Boundary | Permission | Error | Status |
| AC-3 | Both | TC-1 | — | — | — | Pending |
| AC-2 | Android | — | — | TC-2a | — | Pending |
| AC-2 | iOS | — | — | TC-2b | — | Pending |

### TC-1: 天気の取得成功
**AC:** AC-3
**Platform:** Both  _（Android と iOS で観測される振る舞いが同一）_
**Input:** 許可付与済み、ネットワーク利用可能、アプリ起動
**Expected output:** 都市名、気温（°C）、説明、アイコンを表示；スピナーなし、エラーなし。

### TC-2a: 許可拒否 → 設定を開く（Android）
**AC:** AC-2
**Platform:** Android
**Expected output:** 「位置情報へのアクセスが必要」；ボタンタップで Android のアプリ設定画面を開く。

### TC-2b: 許可拒否 → 設定を開く（iOS）
**AC:** AC-2
**Platform:** iOS
**Expected output:** 「位置情報へのアクセスが必要」；ボタンタップで iOS 設定 → WeatherNow を開く。
```

---

## まとめ — 分割がもたらすもの

| 分割なし | `platforms: [android, ios]` あり |
|---|---|
| 暗黙の単一コードベース | 1 つの共有スペック、明確に分離された 2 つのネイティブツリー |
| スペックにプラットフォームが混入 | スペックは中立；HOW は Shared/Android/iOS サブセクションに |
| パリティは記憶頼み | 明示的なパリティ表 + cross-platform consistency チェックリスト |
| 相違が隠れる | 意図的な相違は open issue として記録 |

単一プラットフォームのプロジェクト（`platforms:` が 1 エントリ）は、すべての
サブセクションが 1 つに畳まれます — 必要ないときは分割のコストはゼロです。
