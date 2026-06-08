# ウォークスルー：WeatherNow に予報画面を追加する（既存の Android + iOS コードベース）

**シナリオ**：*WeatherNow* はすでに **Android と iOS の両方**に存在し、現在の天気画面が
動作しています。BVN-SDD に従って **5 日間の予報画面**（T-001）を両プラットフォームに追加します。

> これは**ドキュメント例**です。**既存コードベース + マルチプラットフォーム**モードでの
> アーティファクトの見え方を示すもので、実際に実行するコードではありません。
> コードベースがない場合との違いは `EXAMPLE-ios-weather-ja.md`（単一プラットフォーム、
> グリーンフィールド）と比較してください。

**プロジェクト概要**

| | |
|---|---|
| プラットフォーム | Android（Kotlin, Jetpack Compose, Hilt）**+** iOS（Swift, SwiftUI, async/await） |
| ステータス | 両プラットフォームが存在：現在の天気画面が動作中 |
| リポジトリ構成 | モノレポ：`android/` + `ios/` + `docs/` |
| 本ウォークスルーのチケット | **T-001** — 5 日間予報画面 |
| 外部 API | OpenWeatherMap REST API（`/data/2.5/forecast`） |

モデルと判断ルールの詳細は `docs/standards/cross-platform.md` を参照してください。

**このウォークスルーの読み方：**  
各フェーズに **「Claude Code に入力するコマンド：」** ブロックがあります — Claude Code ウィンドウに入力する正確なテキストです。  
- ほとんどのコマンドはスラッシュコマンド + チケット ID のみで十分です。Claude が前のアーティファクトを自動的に読み込みます。  
- `/sdd-spec` のみ例外：コマンドと一緒に元の要件（Jira / メールなど）を貼り付けてください。

---

## 0. セットアップ

```bash
bvn-sdd init --here --lang ja
```

`.bvn-sdd/config.yml` を編集して両プラットフォームを宣言します：

```yaml
platforms:
  - android
  - ios

platform_stack:
  shared: "spec-pack が信頼できる唯一の情報源（WHAT）"
  android: "Kotlin, Jetpack Compose, Hilt, StateFlow"
  ios: "Swift, SwiftUI, @Observable, async/await"
```

**Claude Code** でプロジェクトを開き、すぐに `/sdd-phase0a` を実行します。

---

## Phase 0-A — Safety Gate（`/sdd-phase0a`）

**Claude Code に入力するコマンド：**
```
/sdd-phase0a
```
*引数不要 — コマンドがプロジェクト構成と `config.yml` を自動的に読み込みます。*

Phase 0-A は両ネイティブツリーがすでに存在することを検出し、モバイル固有のリスクを記録します。

```markdown
# Phase 0 Plan

## Project Type: existing
android/ と ios/ にソースファイルが見つかりました — SURVEY MODE で実行。

## Tech Stack
- Android: Kotlin, minSdkVersion 26, Jetpack Compose, Hilt, StateFlow
- iOS: Swift 5.9, deployment target iOS 16, SwiftUI, @Observable（iOS 17）

## モバイル プラットフォーム チェック
- android/local.properties: あり（API key 参照 — 値は読まない）
- AndroidManifest.xml パーミッション: INTERNET, ACCESS_FINE_LOCATION
- ios/Info.plist: NSLocationWhenInUseUsageDescription あり
- google-services.json: なし（このプロジェクトで Firebase は未使用）

## リスク登録
| リスク | Severity | 対策 |
|---|---|---|
| local.properties の API キー | Medium | .gitignore に含まれている — コミットなし |
| GPS フォアグラウンドパーミッション | Low | フォアグラウンドのみ；バックグラウンドなし |
```

`docs/maintenance/phase0/phase0-review.md` を確認し、残りの項目をサインオフします。
その後 `/sdd-map` を実行します。

---

## Phase 0-B — ソースインテリジェンス（`/sdd-map`）

**Claude Code に入力するコマンド：**
```
/sdd-map
```
*引数不要 — `phase0-plan.md` から Survey/Green-field モードを検出し、コードベース全体を読み込みます。*

Survey Mode は両ネイティブツリーを読み込み、各プラットフォームの**専用プラットフォームマップ**を
作成します — これがグリーンフィールド実行との主な違いです。

```markdown
# System Map — WeatherNow（マルチプラットフォーム、既存コードベース）

## Platforms
| Platform | Tree | Stack | Status |
|---|---|---|---|
| Shared（contract） | docs/, contract | spec-pack SSOT | IMPLEMENTED |
| Android | android/ | Kotlin, Compose, Hilt, MVVM | IMPLEMENTED |
| iOS | ios/ | Swift, SwiftUI, @Observable, MVVM | IMPLEMENTED |

## 共有コントラクト レイヤー（使用中）
- GET /data/2.5/weather → WeatherData { city, tempC, description, iconCode, observedAt }
- 未設定: /data/2.5/forecast エンドポイントのコントラクト

## パリティ ステータス
| 機能 | Android | iOS | 備考 |
|---|---|---|---|
| 現在の天気画面 | ✓ 実装済み | ✓ 実装済み | パリティ intact |
| 5 日間予報画面 | ✗ 未実装 | ✗ 未実装 | 新機能 — T-001 |
→ パリティデットなし。T-001 の前は両プラットフォームが同水準。
```

```markdown
# Platform Android Map — WeatherNow

## アーキテクチャ: MVVM + Clean Architecture（partial）
android/app/src/main/java/com/weathernow/
  ui/current/      — CurrentWeatherViewModel.kt, CurrentWeatherScreen.kt
  data/remote/     — WeatherApiService.kt（Retrofit）, WeatherDto.kt
  data/repository/ — WeatherRepositoryImpl.kt
  domain/model/    — WeatherData.kt
  di/              — NetworkModule.kt（Hilt）

## 状態管理: StateFlow<ViewState>
ViewState: sealed class { Idle | Loading | Loaded(data) | Error(message) }
CurrentWeatherViewModel のパターンがプロジェクト標準 — Forecast でも再利用。

## テストインフラ
- Unit: JUnit 5 + MockK（Mockito は未使用）
- UI: Compose UI テスト（CurrentWeather のテストはまだ未記述）
- 実行: ./gradlew :app:testDebugUnitTest
```

```markdown
# Platform iOS Map — WeatherNow

## アーキテクチャ: MVVM + async/await
ios/WeatherNow/
  Features/CurrentWeather/ — CurrentWeatherViewModel.swift, CurrentWeatherView.swift
  Services/                — WeatherAPIClient.swift, WeatherAPIError.swift
  Models/                  — WeatherData.swift

## 状態管理: @Observable ViewModel（iOS 17）
ViewState: enum { idle, loading, loaded(WeatherData), error(String) }
CurrentWeatherViewModel のパターンがプロジェクト標準 — Forecast でも再利用。

## テストインフラ
- Unit: XCTest + プロトコルベースのモック（外部モックフレームワークなし）
- UI: XCUITest（未記述）
- 実行: xcodebuild test -scheme WeatherNow -destination 'platform=iOS Simulator,name=iPhone 16'
```

---

## T-001 — 5 日間予報画面

### ブートストラップ — `/sdd-new T-001 Forecast screen`

**Claude Code に入力するコマンド：**
```
/sdd-new T-001 5日間予報画面
```
*チケット ID + 短い名前 — `docs/changes/T-001/` とすべての空アーティファクトファイルを作成します。内容は入力しません。*

1 つのチケットフォルダ、1 つの共有スペック。Phase 0-B のプラットフォームマップを
Phase 2 で読み込んで実際のパターンを検証します。

---

### Phase 1 — Spec Pack（`/sdd-spec T-001`）

**Claude Code に入力するコマンド：**
```
/sdd-spec T-001

PM からの要件：
5 日間予報画面を追加する。各日に表示: 曜日名、最高/最低気温（°C）、天気説明、アイコン。
ソース: OpenWeatherMap /data/2.5/forecast。
30 分間キャッシュ；オフライン時はキャッシュを表示。
ネットワーク障害 → エラーメッセージ + 再試行ボタン、クラッシュなし。
```
*Jira / メール / ブリーフの元の要件をコマンドと一緒に貼り付けてください。コマンドは `docs/architecture/`、ソースを読み込み、提供された要件と組み合わせて `spec-pack.md` を生成します。手動入力が必要な唯一のフェーズです。*

スペックは WHAT について**プラットフォーム中立**を保ちます。`Source Availability` は
実際に読んだコードを参照します — `[PLANNED]` エントリはありません。

```markdown
# Spec Pack — T-001: 5 日間予報画面

## 6. Acceptance Criteria
- [ ] AC-1: アプリが現在地から 5 日間の予報を表示する。
- [ ] AC-2: 各日に表示: 曜日名、最高/最低気温（°C）、説明、アイコン。
- [ ] AC-3: データ取得中はローディング表示。
- [ ] AC-4: ネットワーク障害 → エラーメッセージ + 再試行ボタン；クラッシュしない。
- [ ] AC-5: データを 30 分間キャッシュ；オフライン時はキャッシュを表示。

## 8. Surface impact (per platform)
| Platform | 影響する画面 / サーフェス | 影響する Backend / API | データ / イベント |
|---|---|---|---|
| Shared（contract） | — | OpenWeatherMap GET /forecast | 新しい ForecastData モデル |
| Android | 新しい ForecastScreen（Compose） | WeatherApiService を拡張 | キャッシュ（DataStore） |
| iOS | 新しい ForecastView（SwiftUI） | WeatherAPIClient を拡張 | キャッシュ（UserDefaults） |

## 9. Client/Service contract（プラットフォーム中立）
GET /data/2.5/forecast?lat={lat}&lon={lon}&cnt=40&units=metric&appid={key}
Response → ForecastData {
  days: List<DayForecast>   （5 エントリ、日単位でグループ化）
  DayForecast { date: String, highC: Double, lowC: Double,
                description: String, iconCode: String }
}
Android と iOS は同一に消費する。

## 14. Source Availability Summary
- WeatherApiService.kt / WeatherAPIClient.swift: 存在 ✓、/forecast エンドポイントの追加が必要
- WeatherData モデル: 存在 ✓、新しい ForecastData モデルの追加が必要
- ViewState パターン: CurrentWeather に存在 ✓ — 同じ構造を再利用

## 15. Complexity Classification
2 つのネイティブツリー + 既存コードベース → M3 Plus。
```

---

### Phase 1-B — ライトサイジング（`/sdd-rightsize T-001`）

**Claude Code に入力するコマンド：**
```
/sdd-rightsize T-001
```
*追加入力不要 — `spec-pack.md` と `config.yml`（`platforms:`）を読み込んでスコアを計算し、モードを選択します。*

**マルチプラットフォーム要因**が下限を **M3** に引き上げます：

```markdown
# Mode Decision — T-001

## Scoring
- Reversibility: 1（新機能の追加、既存機能の変更なし）
- Uncertainty: 2（/forecast のコントラクトは明確だがグループ化ロジックの検証が必要）
- Risk: 1（認証、本番 DB、決済への影響なし）
- Scope: 3（1 つのスペックから 2 つのネイティブツリー）

## マルチプラットフォーム要因
platforms: [android, ios] → Scope = 3 → モード下限 M3 を適用。

## 決定: M3（Plus）
## 適応ワークフロー: sdd-context → sdd-plan → sdd-implement → sdd-test → sdd-blackbox → sdd-report → sdd-learnings
```

> 注: モードは各フェーズの「深さ」を決めるもので、どのフェーズを実行するかではありません。
> すべてのチケットは全シーケンスを実行します。停止するのは MX のみ。

---

### Phase 2 — Context（`/sdd-context T-001`）

**Claude Code に入力するコマンド：**
```
/sdd-context T-001
```
*追加入力不要 — Phase 0-B のプラットフォームマップ、`spec-pack.md` を読み込み、Grep でソースを検証します。*

`context.md` は最初に Phase 0-B のプラットフォームマップを読み込み、次に Grep を使って
パターンが**実際にコードベースに存在する**ことを検証します — `[PLANNED]` はここにありません。

```markdown
# Context — T-001

## コードベース内の正しい例

### Android パターン
- CurrentWeatherViewModel.kt: @HiltViewModel + StateFlow<ViewState> + viewModelScope.launch
  → これが ForecastViewModel の標準です（Read で検証済み）
- WeatherApiService.kt: @GET + suspend fun + Retrofit インターフェース
  → 同じパターンで getForecast() を追加する

### iOS パターン
- CurrentWeatherViewModel.swift: @Observable final class + enum ViewState + @MainActor func
  → これが ForecastViewModel の標準です（Read で検証済み）
- WeatherAPIClient.swift: func fetch...() async throws → Model
  → 同じパターンで fetchForecast() を追加する

## 許可 vs. 禁止パターン

### Android
- 許可: StateFlow<ViewState> + @HiltViewModel + @Inject constructor
- 許可: DataStore によるキャッシュ（CurrentWeather で既に使用 — 再利用）
- 禁止: LiveData（プロジェクトは完全に StateFlow に移行済み）
- 禁止: @Composable からのネットワーク呼び出し

### iOS
- 許可: @Observable class + @MainActor func load() async
- 許可: 短期キャッシュに UserDefaults（CurrentWeather と同じパターン）
- 禁止: ObservableObject（このコードベースでは @Observable に置き換え済み）
- 禁止: SwiftUI View から直接 URLSession；新規コードでの DispatchQueue.main

## 実際に存在するメソッド / クラス

### Android（Grep で検証）
- WeatherRepositoryImpl.fetchCurrentWeather() — 存在 ✓
- WeatherApiService.getCurrentWeather() — 存在 ✓（getForecast() の追加が必要）
- CurrentWeatherViewModel の StateFlow<ViewState> — 存在 ✓

### iOS（Grep で検証）
- WeatherAPIClient.fetchCurrentWeather() — 存在 ✓
- @Observable CurrentWeatherViewModel — 存在 ✓
- ViewState enum（idle/loading/loaded/error） — 存在 ✓

## パリティギャップ チェック
両プラットフォームとも CurrentWeather を実装済み。T-001 に影響するパリティデットなし。
```

---

### Phase 3 — Plan（`/sdd-plan T-001`）

**Claude Code に入力するコマンド：**
```
/sdd-plan T-001
```
*追加入力不要 — `context.md` と `spec-pack.md` を読み込み、影響分析と実装計画を作成します。*

`impl-plan.md` はネイティブツリーごとに HOW を分割し、パリティチェック表で両プラットフォームが
同じベースラインから始まることを確認します。

```markdown
# Implementation Plan — T-001

## 変更するファイル

### Shared
| ファイル | 理由 | Add / Modify |
|---|---|---|
| docs/changes/T-001/spec-pack.md | ForecastData コントラクトの SSOT | Modify |

### Android
| ファイル | 理由 | Add / Modify |
|---|---|---|
| android/.../data/remote/WeatherApiService.kt | getForecast() エンドポイントの追加 | Modify |
| android/.../data/remote/ForecastDto.kt | /forecast レスポンス用の新しい DTO | Add |
| android/.../domain/model/ForecastData.kt | 新しいドメインモデル | Add |
| android/.../data/repository/WeatherRepositoryImpl.kt | fetchForecast() の実装 | Modify |
| android/.../ui/forecast/ForecastViewModel.kt | 新しい ViewModel（StateFlow<ViewState>） | Add |
| android/.../ui/forecast/ForecastScreen.kt | 新しい Compose 画面 | Add |

### iOS
| ファイル | 理由 | Add / Modify |
|---|---|---|
| ios/.../Services/WeatherAPIClient.swift | fetchForecast() の追加 | Modify |
| ios/.../Models/ForecastData.swift | 新しいモデル | Add |
| ios/.../Features/Forecast/ForecastViewModel.swift | 新しい ViewModel（@Observable） | Add |
| ios/.../Features/Forecast/ForecastView.swift | 新しい SwiftUI 画面 | Add |

## クロスプラットフォーム パリティ チェック
| 共有 AC / 振る舞い | Android impl | iOS impl | 同一? |
|---|---|---|---|
| AC-1 現在地から 5 日間 | ForecastViewModel.loadForecast() | ForecastViewModel.loadForecast() @MainActor | はい |
| AC-3 ローディング | ViewState.Loading → CircularProgressIndicator | ViewState.loading → ProgressView | はい |
| AC-4 ネットワークエラー + 再試行 | ViewState.Error + retry button | ViewState.error + retry button | はい |
| AC-5 30 分キャッシュ | DataStore + タイムスタンプ確認 | UserDefaults + タイムスタンプ確認 | はい（同一閾値） |

## モード チェック
2 つのネイティブツリー、パリティデットなし → M3 確認。
```

---

### Phase 4+5 — 実装（`/sdd-implement T-001`）

**Claude Code に入力するコマンド：**
```
/sdd-implement T-001
```
*追加入力不要 — `impl-plan.md` を読み込み、レビューチェックリストを提示してコードを書く前にあなたの確認を待ちます。各 Stop/Ask ポイントで停止します。*

各ツリーは**既存パターン**から拡張され、それぞれのイディオムで実装されます。

**Android — `ForecastViewModel.kt`（新規、CurrentWeatherViewModel 標準に従う）**
```kotlin
@HiltViewModel
class ForecastViewModel @Inject constructor(
    private val repo: WeatherRepository,
    private val location: LocationService,
) : ViewModel() {
    private val _state = MutableStateFlow<ViewState>(ViewState.Idle)
    val state: StateFlow<ViewState> = _state.asStateFlow()

    fun loadForecast() = viewModelScope.launch {
        _state.value = ViewState.Loading
        runCatching {
            val loc = location.current()
            repo.fetchForecast(loc.lat, loc.lon)
        }.onSuccess { _state.value = ViewState.Loaded(it) }
         .onFailure { _state.value = repo.cachedForecast()?.let(ViewState::Loaded)
                                       ?: ViewState.Error(it.message.orEmpty()) }
    }
}
```

**iOS — `ForecastViewModel.swift`（新規、CurrentWeatherViewModel 標準に従う）**
```swift
@Observable final class ForecastViewModel {
    enum ViewState { case idle, loading, loaded([DayForecast]), error(String) }
    private(set) var state: ViewState = .idle

    @MainActor func loadForecast() async {
        state = .loading
        do {
            let loc = try await location.current()
            state = .loaded(try await apiClient.fetchForecast(lat: loc.lat, lon: loc.lon))
        } catch {
            state = cachedForecast().map(ViewState.loaded) ?? .error(error.localizedDescription)
        }
    }
}
```

両者は AC-1、AC-3、AC-4、AC-5 を同一に満たします。self-review の前に
`review-checklist.md` の **Cross-platform consistency** セクションをチェック：
すべての AC が両プラットフォームで観測可能；ForecastData コントラクトは同一に消費。

---

### Phase 6 — Test（`/sdd-test T-001`）

**Claude Code に入力するコマンド：**
```
/sdd-test T-001
```
*追加入力不要 — `spec-pack.md` と実装済みソースを読み込み、AC マトリクスに従ってテストを書いて実行します。*

AC↔テストマトリクスに **Platform** 列が追加され、コントラクトテストで同じ JSON フィクスチャが
両クライアントで同じモデルを生成することを保証します。

```markdown
## AC ↔ テストマトリクス
| AC | Platform | テスト種別 | テスト名 | 優先度 |
|---|---|---|---|---|
| AC-1 | Android | unit | ForecastViewModelTest.loadForecast_success | H |
| AC-1 | iOS | unit | ForecastViewModelTests.loadForecast_success | H |
| AC-1 | Shared | contract | ForecastContractTest（JSON フィクスチャ → ForecastData） | H |
| AC-4 | Android | unit | ForecastViewModelTest.loadForecast_networkError | H |
| AC-4 | iOS | unit | ForecastViewModelTests.loadForecast_networkError | H |
| AC-5 | Android | unit | ForecastViewModelTest.loadForecast_cacheHit | M |
| AC-5 | iOS | unit | ForecastViewModelTests.loadForecast_cacheHit | M |

## 実行コマンド
# Android
./gradlew :app:testDebugUnitTest --tests "*.ForecastViewModelTest"
# iOS
xcodebuild test -scheme WeatherNow \
  -destination 'platform=iOS Simulator,name=iPhone 16' \
  -only-testing:WeatherNowTests/ForecastViewModelTests
```

---

### Phase 7 — ブラックボックス（`/sdd-blackbox T-001`）

**Claude Code に入力するコマンド：**
```
/sdd-blackbox T-001
```
*追加入力不要 — `spec-pack.md` と `test-results.md` を読み込み、ユーザー/QA 観点からテストケースを生成します。*

ケースは共有スペックのみから導出し、各ケースに `Platform:` を付与。
観測される振る舞いが同一 → 1 つの `Both` ケース。

```markdown
## AC カバレッジマップ
| AC | Platform | Happy path | Error | Cache | Status |
|---|---|---|---|---|---|
| AC-1,2 | Both | TC-1 | — | — | Pending |
| AC-4 | Both | — | TC-2 | — | Pending |
| AC-5 | Both | — | — | TC-3 | Pending |

### TC-1: 5 日間予報の取得成功
AC: AC-1, AC-2
Platform: Both
Input: 位置情報許可付与済み、ネットワーク利用可能、予報画面を開く
Expected output: 5 行；各行に曜日名、最高/最低気温（°C）、説明、アイコンが表示。

### TC-2: ネットワーク障害 — キャッシュなし
AC: AC-4
Platform: Both
Input: 機内モード、キャッシュなし、予報画面を開く
Expected output: エラーメッセージ + 「再試行」ボタンが表示；クラッシュしない。

### TC-3: キャッシュ有効（30 分以内）
AC: AC-5
Platform: Both
Input: 取得成功 → 機内モードをオン → 30 分以内に再び開く
Expected output: キャッシュされたデータが表示；スピナーなし；エラーなし。
```

---

### Phase 8 — レポート（`/sdd-report T-001`）

**Claude Code に入力するコマンド：**
```
/sdd-report T-001
```
*追加入力不要 — 作成されたすべてのアーティファクトを集約して最終レポートを作成します。*

```markdown
# Final Report — T-001: 5 日間予報画面

## Acceptance Criteria — 完了状況
| AC | Android | iOS | 備考 |
|---|---|---|---|
| AC-1 5 日間の表示 | PASS | PASS | 両者とも同じ ForecastData コントラクトから |
| AC-2 各日のコンテンツ | PASS | PASS | 曜日名、気温、説明、アイコンが存在 |
| AC-3 ローディング | PASS | PASS | プラットフォーム標準のプログレス表示 |
| AC-4 ネットワークエラー + 再試行 | PASS | PASS | 正しいメッセージと再試行 |
| AC-5 30 分キャッシュ | PASS | PASS | 同一閾値；DataStore vs UserDefaults |

## クロスプラットフォーム パリティ サマリー
全 5 AC が両プラットフォームで達成。T-001 では意図的な相違なし。

## 受け入れたリスク
- 異なるキャッシュストレージ（DataStore vs UserDefaults）— 受け入れ、これはプラットフォームイディオム。

## フォローアップ
- T-002：日別詳細画面（予報リストからのタップスルー）。
```

---

### Phase 9 — Learnings（`/sdd-learnings T-001`）

**Claude Code に入力するコマンド：**
```
/sdd-learnings T-001
```
*追加入力不要 — すべてのチケットアーティファクトを読み込み、プロモーション候補を提案し、`failure-mode-index.md` を更新します。*

```markdown
# Promotion Candidates — T-001

## プロモーション候補 → docs/standards/cross-platform.md
- **ViewModel パターン再利用**: 既存コードベースに新機能を追加するとき、新しいパターンを
  設計するのではなく、既存 ViewModel の構造（Android は StateFlow/ViewState；
  iOS は @Observable/ViewState）を複製する。フィーチャー間の一貫性を維持できる。
- **コンテキストの前にプラットフォームマップ**: context.md を記入する前に
  docs/architecture/platform-android-map.md と platform-ios-map.md を読む必要がある
  — 実際のツリーに存在しないパターンを spec する事態を防ぐ。

## パリティ チェック結果 — T-001
T-001 の前にパリティデットなし。impl-plan.md のパリティ表：4/4 の振る舞いが同一；
意図的な相違 0 件。

## 追加するフェイルモード → docs/maintenance/failure-mode-index.md
FM-08：一方のプラットフォームにのみ機能を追加 — チケット間でパリティデットが蓄積。
  原因：パリティギャップを記録せずに 1 プラットフォームのみにスコープしたチケット。
  検出：system-map.md の §Parity Status；impl-plan.md のパリティ表。
  対処：すべてのマルチプラットフォームチケットはパリティ表を完全に記入する。
```

---

## まとめ — コードベースが既に存在する場合の違い

| グリーンフィールド（`[PLANNED]`） | 既存コードベース（本ウォークスルー） |
|---|---|
| system-map.md はすべて `[PLANNED]` | system-map.md が実際のステータス + §Parity Status を表示 |
| Phase 0-B はプラットフォームマップなし | Phase 0-B が `platform-android-map.md` + `platform-ios-map.md` を作成 |
| context.md がパターンを設計する | context.md が既存パターンを検証（Grep/Read） |
| source-map.md が作成するファイルを列挙 | source-map.md が変更するファイル + 新規ファイルを列挙 |
| パリティチェック: ゼロからのベースライン | パリティチェック: spec 前に現在のベースラインを検証 |

単一プラットフォームのプロジェクト（`platforms:` が 1 エントリ）は、すべての
サブセクションが 1 つに畳まれます — 必要ないときは分割のコストはゼロです。
