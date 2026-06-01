# ウォークスルー：BVN-SDDでWeatherNow（iOS）をゼロから構築する

**シナリオ**: *WeatherNow*という新しいiOS天気アプリをゼロから構築します — 既存のコードベースはありません。  
このウォークスルーでは、すべてのBVN-SDDコマンド、各コマンドが生成する重要なアーティファクトの内容、  
そして各ステップで行う判断を示します。

> これは**ドキュメント例**です — アーティファクトの見た目を示すものであり、実際に実行するSwiftコードではありません。

**アプリ概要**

| | |
|---|---|
| プラットフォーム | iOS 17+、Swift 5.9、SwiftUI |
| アーキテクチャ | MVVM + Clean Architecture |
| このウォークスルーのチケット | **T-001** — 現在の天気画面（位置情報ベース） |
| 外部API | OpenWeatherMap REST API |
| 依存関係管理 | Swift Package Manager |

---

## 0. セットアップ

```bash
bvn-sdd check
# ✓ git 2.44.0
# ✓ claude (Claude Code)

git clone git@github.com:my-org/weathernow-ios.git
cd weathernow-ios

bvn-sdd init --here --lang ja
# ✓ .claude/ 作成済み
# ✓ .bvn-sdd/ 作成済み
# ✓ docs/ 作成済み
```

**Claude Code**でプロジェクトを開き、すぐに実行します:

```
/sdd-phase0a
```

---

## Phase 0-A — Safety Gate

> **仕組み**: `/sdd-phase0a`は「安全環境を監査する」という汎用的な指示をロードするだけです。何を作るかはAIには分かりません。**同じメッセージにアプリの説明を書くことで**、AIがアーティファクトに記録し、以降のフェーズで引き継ぎます。

**Claude Codeで入力するメッセージ**:

```
/sdd-phase0a

プロジェクト: WeatherNow — コードが全くない新規iOS天気アプリ。
プラットフォーム: iOS 17+、SwiftUI、MVVM + Clean Architecture、Swift Package Manager。
外部API: OpenWeatherMap（REST、APIキーで認証）。
オフライン: 最後の成功レスポンスをキャッシュ。「最終更新: X分前」バナーを表示。
```

**AIが行うこと**: リポジトリをスキャン — ソースファイルが見つからない — `project_type = new`を記録。入力した情報をアーティファクトに書き込む。

**生成**: `docs/maintenance/phase0/phase0-plan.md`

```markdown
# Phase 0-A Safety Gate — WeatherNow iOS

## プロジェクトタイプ
new (greenfield) — ソースファイル未検出

## 技術スタック（ユーザーの説明より）
- iOS 17+、Swift 5.9、SwiftUI
- MVVM + Clean Architecture
- Swift Package Manager
- 外部API: OpenWeatherMap REST

## 記録された安全制約
- DENY: .env、APIキー、トークン、PIIの読み取りまたは出力
- DENY: 人間の承認なしでリモートにプッシュ
- DENY: 確認なしの破壊的なgit操作（reset --hard、force-push）
- ASK: ファイル削除前
- ASK: 外部APIを呼び出すコードを書く前（キー処理方法を確認）

## コンテキストポリシー
- 真実の情報源の優先順位: spec-pack.md > アーキテクチャ文書 > AI推測
- 500行を超えるファイルは全内容ロードではなく要約

## /sdd-mapへのオープン質問
1. 希望するモジュール構造（Features/、Data/、Core/ または別の構成）?
2. キャッシュの陳腐化しきい値 — 何分後に「古い」インジケーターを表示?
3. UIデザインドキュメント（Figma、モックアップ）はありますか?
```

**あなた**: `phase0-plan.md`を読む。残りのオープン質問に回答する。

**あなたの回答**:
> Features/Data/Core構成でOK。30分後に陳腐化。Figmaはまだなし。続行。

---

## Phase 0-B — Source Intelligence（グリーンフィールドモード）

**コマンド**: `/sdd-map`

**AIが行うこと**: `phase0-plan.md`を読む（Phase 0-Aで入力した技術スタックが記録されている）→ `project_type = new`を検出 → **グリーンフィールドモード**で実行。アーキテクチャ文書はあなたが提供した情報を元に作成されます — AIが推測するのではありません。スキャンするソースなし — アーキテクチャ*決定*文書を生成。すべてのエントリーは`[PLANNED]`でマーク。

**生成**: `docs/architecture/system-map.md`

```markdown
# System Map — WeatherNow iOS
## ステータス: GREEN-FIELD — すべてのエントリー [PLANNED]

## レイヤー概要
| レイヤー | 技術 | ステータス |
|---|---|---|
| Presentation | SwiftUI Views | [PLANNED] |
| State / ViewModel | @Observable (iOS 17) | [PLANNED] |
| Domain (Use Cases) | Pure Swift structs | [PLANNED] |
| Data (Repository) | Protocol + URLSession実装 | [PLANNED] |
| Location | CoreLocation async wrapper | [PLANNED] |
| Cache | UserDefaults（シンプルJSON） | [PLANNED] |

## モジュール構造 [PLANNED]
WeatherNow/
├── App/
│   └── WeatherNowApp.swift          # エントリーポイント、DIルート
├── Features/
│   └── CurrentWeather/
│       ├── View/                    # SwiftUI Views
│       ├── ViewModel/               # @Observable ViewModels
│       └── Model/                   # ドメインモデル（WeatherDataなど）
├── Data/
│   ├── Repository/                  # WeatherRepositoryプロトコル + 実装
│   ├── Network/                     # URLSession wrapper + Codable DTO
│   └── Location/                    # CLLocationManager async/await wrapper
└── Core/
    └── Config/                      # AppConfig — Info.plistからキー読み取り

## 計画されたAPIコントラクト
- WeatherRepository.fetchCurrentWeather(lat:lon:) async throws -> WeatherData
- LocationService.requestCurrentLocation() async throws -> CLLocationCoordinate2D

## 外部API [PLANNED]
- OpenWeatherMap: GET /data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric
- 認証: クエリパラメーターのAPIキー（Info.plistに保存、ソースにハードコードしない）
```

**追加生成**: `docs/architecture/api-contracts.md` *（すべて`[PLANNED]`）*  
**追加生成**: `docs/architecture/db-schema.md` *（UserDefaultsキャッシュスキーマを`[PLANNED]`でマーク）*

**あなた**: モジュール構造を確認。必要に応じて調整。この文書はすべてのチケットが参照するアーキテクチャ設計図。

**あなたの確認**: 承認。最初のチケットに進む。

---

## T-001: 現在の天気画面

### ブートストラップ

**入力するコマンド**（短いタイトルを付けると便利）:

```
/sdd-new T-001 現在の天気画面
```

```
✓ docs/changes/T-001/ 作成済み
✓ 20個の空のアーティファクトファイル準備完了:
    spec-pack.md, source-availability.md, open-issues.md
    mode-decision.md, context.md, source-map.md, ticket-rules.md
    impact-analysis.md, impl-plan.md, review-checklist.md
    self-review.md, human-review.md, test-plan.md, test-results.md
    blackbox-testcases.md, test-data.md, blackbox-review-checklist.md
    report.md, promotion-candidates.md, strategic-compact.md
```

---

### Phase 1 — Spec Pack

> **AIはT-001の要件をどこから知るのか?**  
> `/sdd-spec`には汎用的な指示しか含まれていません — 「入力された要件からspec-packを書く」というものです。チケット固有の要件は**同じメッセージのコマンドの下に書いてください**。AIはその入力とPhase 0-Bの`docs/architecture/system-map.md`を組み合わせて完全なspecを作成します。

**Claude Codeで入力するメッセージ**（コマンド + 要件を一緒に）:

```
/sdd-spec T-001

T-001の要件 — 現在の天気画面:

目標: アプリを開く → 現在のGPS位置の天気をすぐに表示する。

表示: 都市名、気温（°C）、短い説明（例: "Partly cloudy"）、天気アイコン。

位置情報の許可フロー:
- 初回起動 → 位置情報の許可をリクエスト
- ユーザーが拒否 → 「位置情報へのアクセスが必要です」+ 「設定を開く」ボタン
- 許可された場合 → 自動的に天気を取得

ローディング状態:
- API処理中 → ローディングインジケーター
- ネットワークエラー + キャッシュあり → 古いデータ + 「最終更新: X分前」バナー
- ネットワークエラー + キャッシュなし → 「接続なし」空の状態 + 再試行ボタン

操作: 手動再読み込みのためのプルトゥリフレッシュ。

T-001のスコープ外: 時間別/日別予報、複数の位置、設定画面、プッシュ通知。

オープン質問: APIキーの保存 — Info.plist（シンプル）またはKeychain（安全）? open-issuesに記録。
```

**`spec-pack.md`を書く前にAIが読むもの**:
1. `.claude/CLAUDE.md`、`.claude/rules/*` — プロジェクトルール
2. `docs/architecture/system-map.md` — Phase 0-BでのiOS/SwiftUI/MVVMアーキテクチャ決定
3. **上記に書いた要件** — 受け入れ基準とopen issuesの主要ソース

**生成**: `docs/changes/T-001/spec-pack.md`

```markdown
# Spec Pack — T-001: 現在の天気画面

## 概要
ユーザーのGPS位置に基づいた現在の天気状況を表示する。

## 受け入れ基準
1. 初回起動時に位置情報の許可をリクエスト。
2. 拒否された場合 → 「位置情報へのアクセスが必要です」メッセージ + 「設定を開く」ボタンを表示。
3. 許可された場合 → OpenWeatherMapから天気データを取得。
4. 表示: 都市名、気温（°C）、天気の説明、天気アイコン。
5. 取得中はローディングインジケーターを表示。
6. ネットワーク障害時はエラー状態を表示、「再試行」ボタン付き。
7. プルトゥリフレッシュに対応。
8. キャッシュデータがあってネットワーク障害の場合 → 「最終更新: X分前」バナー付きでキャッシュを表示。

## スコープ外（T-001）
- 時間別/日別予報
- 複数の保存済み位置
- 設定画面（単位、テーマ）
- プッシュ通知

## ソースの可用性
- OpenWeatherMap API: openweathermap.org/api で文書化 — キー必要
- CoreLocation: Apple SDK、常に利用可能
- 再利用できる既存のSwiftコードなし
```

**生成**: `docs/changes/T-001/open-issues.md`

```markdown
# Open Issues — T-001

OI-001: APIキーの保存戦略
  選択肢: (a) Info.plist — シンプルだがバイナリからキーが読み取り可能
          (b) Keychain — より安全だが最初のチケットには複雑
  → Phase 4前に決定が必要。

OI-002: 位置精度のしきい値
  CLLocation.horizontalAccuracy > 5000mの場合はどうする?
  → 警告を表示? 黙って受け入れる?

OI-003: オフラインモード — 空の状態またはキャッシュデータ?
  ネットワークなし かつ キャッシュなし → ユーザーは何を見る?
```

**あなた**: `/sdd-rightsize`を実行する前にオープン質問に回答する。

**あなたの回答**（`open-issues.md`に書くかチャットで回答）:
- OI-001 → 当面はInfo.plist。AR-001として技術的負債を記録。App Store前にプロキシに移行。
- OI-002 → 任意の精度を受け入れ。2km超の場合は「おおよその位置」ラベルを表示。
- OI-003 → 「接続なし — ネットワークを確認してください」空の状態 + 再試行ボタンを表示。

---

### Phase 1 — ライトサイジング

**コマンド**: `/sdd-rightsize T-001`

**生成**: `docs/changes/T-001/mode-decision.md`

```markdown
# Mode Decision — T-001

## 評価
- 新規プロジェクト: 再利用できる既存パターンなし、すべてのレイヤーをゼロから作成。
- 影響するレイヤー: UI（SwiftUI）、ViewModel（@Observable）、Repository（プロトコル）、
  Network（URLSession）、Location（CoreLocation）、Cache（UserDefaults）。
- 新規ファイル数の見積もり: 12〜14。
- 複雑さ: 中〜高 — async/awaitチェーン、エラー状態マシン、許可フロー。

## 決定: モードM3（Plus）

理由: 複数のアーキテクチャレイヤーを同時に確立する。
「フロントエンド/バックエンドコントラクト」（View ↔ ViewModel ↔ Repository）は
コードを書く前にPhase 2〜3で明示的に定義する必要がある。
グリーンフィールドプロジェクトでPhase 2〜3をスキップすると実装順序が不定になる。

## 適応されたワークフロー
すべてのフェーズを適用（スキップなし）。
Phase 4開始前にPhase 3で完全なファイルリストを生成すること。
```

**あなた**: M3を確認。異議なし → 続行。

---

### Phase 2 — チケットコンテキスト & ルール

**コマンド**: `/sdd-context T-001`

**生成**: `docs/changes/T-001/context.md`

```markdown
# Context — T-001

## 適用中のアーキテクチャ決定（system-map.mdより）
- @Observable（iOS 17 Observationフレームワーク）を使用。ObservableObject/Publishedは使わない。
- Repositoryパターン: ViewModelをモックでテストできるようにプロトコルファースト。
- Network: プレーンなURLSession + async/await。サードパーティのネットワークライブラリは使わない。
- エラー処理: 型付きenum（WeatherError、LocationError）、汎用的なError文字列ではない。

## 依存性注入パターン
- ViewModelは依存関係をinitで渡して初期化（シングルトンなし）。
- WeatherNowApp.swiftでルートインジェクション。

## Async / スレッディングルール
- ViewModelのすべての状態変更は@MainActor経由。
- 新しいコードではDispatchQueue.main.asyncを絶対に使わない — @MainActorを使用。
- LocationServiceはasync/await継続で返す。
```

**生成**: `docs/changes/T-001/ticket-rules.md`

```markdown
# Ticket Rules — T-001

## 禁止パターン
- SwiftUI ViewからURLSessionを直接呼び出さない。
- ソースファイルにAPIキーやベースURLをハードコードしない。
- ネットワークレスポンスのOptionalフィールドに強制アンラップ（!）を使わない。

## 必須パターン
- ViewModel内のすべてのasync関数はawaitの前にstate = .loadingを設定すること。
- すべてのエラーケースをキャッチしてViewStateに保存すること — クラッシュや無視は禁止。
- キャッシュ書き込みはネットワークからの成功レスポンス後に行う（アプリ起動時ではない）。
```

**生成**: `docs/changes/T-001/source-map.md`

```markdown
# Source Map — T-001 [すべて新規作成 — グリーンフィールド]

| ファイル | 目的 |
|---|---|
| WeatherNow/Core/Config/AppConfig.swift | Info.plistからWEATHER_API_KEYを読み取る |
| WeatherNow/Features/CurrentWeather/Model/WeatherData.swift | ドメインモデル |
| WeatherNow/Data/Network/WeatherDTO.swift | Codable OpenWeatherMapレスポンスDTO |
| WeatherNow/Data/Network/WeatherAPIClient.swift | URLSession wrapper + エラーマッピング |
| WeatherNow/Data/Repository/WeatherRepository.swift | プロトコル定義 |
| WeatherNow/Data/Repository/WeatherRepositoryImpl.swift | 実装: APIClient + UserDefaultsキャッシュ |
| WeatherNow/Data/Location/LocationService.swift | CoreLocation async/await wrapper |
| WeatherNow/Features/CurrentWeather/ViewModel/CurrentWeatherViewModel.swift | @Observable ViewModel |
| WeatherNow/Features/CurrentWeather/View/WeatherIconView.swift | アイコンサブコンポーネント |
| WeatherNow/Features/CurrentWeather/View/CurrentWeatherView.swift | メイン画面SwiftUI View |
| WeatherNow/App/WeatherNowApp.swift | エントリーポイント + DIルート |
| WeatherNowTests/CurrentWeatherViewModelTests.swift | ViewModelユニットテスト |
| WeatherNowTests/WeatherAPIClientTests.swift | ネットワークレイヤーテスト |
```

---

### Phase 3 — インパクト分析 & 実装計画

**コマンド**: `/sdd-plan T-001`

**生成**: `docs/changes/T-001/impl-plan.md`

```markdown
# Implementation Plan — T-001

## 実装順序（依存関係安全）
1. AppConfig.swift               — 依存関係なし
2. WeatherData.swift             — ドメインモデル、依存関係なし
3. WeatherDTO.swift              — Codable DTO、依存関係なし
4. WeatherRepository.swift       — プロトコルのみ、まだ実装なし
5. LocationService.swift         — CoreLocation wrapper、スタンドアロン
6. WeatherAPIClient.swift        — AppConfig + WeatherDTOを使用
7. WeatherRepositoryImpl.swift   — APIClient + UserDefaultsを使用
8. CurrentWeatherViewModel.swift — Repository + LocationServiceを使用
9. WeatherIconView.swift         — 純粋UIコンポーネント、依存関係なし
10. CurrentWeatherView.swift      — ViewModelを使用
11. WeatherNowApp.swift           — すべてを繋ぐ
12. テスト                        — 実装完了後

## 主なリスク
- RISK-01: Info.plistのキー保存 — コンパイル済みバイナリからキーが読み取り可能。
  開発フェーズでは許容。App Store前に解決必須（AR-001）。
- RISK-02: NSLocationWhenInUseUsageDescriptionをXcodeでInfo.plistに設定必須
  （AIはXcodeプロジェクトファイルを直接編集できない — 人間の手順が必要）。
- RISK-03: ネットワークタイムアウト時のリトライロジックなし — M3スコープでは許容、
  フォローアップチケットで追加。
```

**あなた**: 計画を確認。AIがコードを書く前にファイルリストと順序を承認する。

**あなたの確認**:
> 承認。`NSLocationWhenInUseUsageDescription`はXcodeで手動でInfo.plistに追加します。

---

### Phase 4+5 — 実装 & レビュー

**コマンド**: `/sdd-implement T-001`

AIは`impl-plan.md`で指定された順序でファイルを作成。主要ファイルの抜粋:

---

**`WeatherRepository.swift`** — プロトコル定義:
```swift
// WeatherNow/Data/Repository/WeatherRepository.swift
protocol WeatherRepository {
    func fetchCurrentWeather(lat: Double, lon: Double) async throws -> WeatherData
    func cachedWeather() -> CachedWeather?
}
```

---

**`CurrentWeatherViewModel.swift`** — コア状態マシン:
```swift
// WeatherNow/Features/CurrentWeather/ViewModel/CurrentWeatherViewModel.swift
@Observable
final class CurrentWeatherViewModel {

    enum ViewState {
        case idle
        case loading
        case loaded(WeatherData)
        case locationPermissionDenied
        case error(String)
    }

    private(set) var state: ViewState = .idle
    private let repository: WeatherRepository
    private let locationService: LocationService

    init(repository: WeatherRepository, locationService: LocationService) {
        self.repository = repository
        self.locationService = locationService
    }

    @MainActor
    func loadWeather() async {
        state = .loading
        do {
            let location = try await locationService.requestCurrentLocation()
            let weather = try await repository.fetchCurrentWeather(
                lat: location.latitude,
                lon: location.longitude
            )
            state = .loaded(weather)
        } catch LocationError.permissionDenied {
            state = .locationPermissionDenied
        } catch {
            if let cached = repository.cachedWeather() {
                state = .loaded(cached.weather)   // バナー付きで古いデータを表示
            } else {
                state = .error(error.localizedDescription)
            }
        }
    }
}
```

---

**生成**: `docs/changes/T-001/self-review.md`

```markdown
# AI Self-Review — T-001

## チェックリスト
- [x] ソースファイルにAPIキーのハードコードなし（AppConfigがInfo.plistから読み取り）
- [x] すべての状態変更に@MainActorを使用 — DispatchQueue.mainなし
- [x] プロトコルファーストのRepository — ViewModelをモックでテスト可能
- [x] すべてのエラー状態を処理: 位置情報拒否、ネットワークエラー、デコードエラー
- [x] すべてのawait前にローディング状態を設定
- [x] ネットワーク障害時にキャッシュを表示（OI-003解決済み）
- [ ] 警告: Info.plistのキー保存 — AR-001技術的負債として許容
- [ ] 警告: NSLocationWhenInUseUsageDescription — Xcodeで手動設定が必要

## 人間のレビューが必要な項目
1. Info.plist（Xcodeプロジェクトファイル）にNSLocationWhenInUseUsageDescriptionを設定。
2. 実行前にInfo.plistにWEATHER_API_KEY値を追加。
3. キャッシュデータ表示時に「最終更新」バナーが正しく表示されることを確認。
```

**あなた**: 生成されたすべてのSwiftファイルを読む。その後`human-review.md`に記入する。

**`docs/changes/T-001/human-review.md`**（あなたが記入）:
```markdown
# Human Review — T-001

レビュアー: @hv_ngan
日付: 2026-06-01

## 判定: 注記付きで承認

## 発見事項
1. ViewModelのロジックはクリーン。async/awaitチェーンは正確で読みやすい。
2. エラーenumはすべての予想される失敗シナリオをカバー。
3. エラー時のキャッシュ動作がOI-003の決定と一致。 ✓
4. XcodeでNSLocationWhenInUseUsageDescriptionをInfo.plistに追加済み。 ✓
5. Info.plistにWEATHER_API_KEY追加済み。 ✓

## 受け入れたリスク
- AR-001: Info.plistのAPIキー — App Store前にサーバーサイドプロキシに移行予定。
```

---

### Phase 6 — テスト計画 & 結果

**コマンド**: `/sdd-test T-001`

**生成**: `docs/changes/T-001/test-plan.md`（抜粋）

```markdown
# Test Plan — T-001

## ユニットテスト: CurrentWeatherViewModel
| テスト | シナリオ | 期待される結果 |
|---|---|---|
| test_loadWeather_success | 位置情報許可済み、APIが有効なデータを返す | state == .loaded(weather) |
| test_loadWeather_locationDenied | LocationServiceが.permissionDeniedをスロー | state == .locationPermissionDenied |
| test_loadWeather_networkError_withCache | URLErrorスロー、キャッシュあり | state == .loaded(cachedWeather) |
| test_loadWeather_networkError_noCache | URLErrorスロー、キャッシュなし | state == .error("...") |
| test_loadWeather_setsLoadingFirst | awaitの間 | state == .loading（最初） |

## ユニットテスト: WeatherAPIClient
| テスト | シナリオ | 期待される結果 |
|---|---|---|
| test_fetch_parsesValidJSON | 有効なフィクスチャJSON | 正しいWeatherDataを返す |
| test_fetch_throws_on404 | HTTP 404レスポンス | WeatherError.notFoundをスロー |
| test_fetch_throws_onDecodeError | 不正なJSON | WeatherError.decodingFailedをスロー |
```

**生成**: `docs/changes/T-001/test-results.md`

```markdown
# Test Results — T-001

実行日: 2026-06-01
全8テスト PASSED ✓

カバレッジ:
  CurrentWeatherViewModel:  94%
  WeatherAPIClient:         88%
  LocationService:          71%（許可フローはユニットテストが困難 — ブラックボックスでカバー）
```

**あなた**: Xcodeでテストを実行（`Cmd + U`）。続行前にパスを確認する。

---

### Phase 7 — ブラックボックステスト

**コマンド**: `/sdd-blackbox T-001`

**生成**: `docs/changes/T-001/blackbox-testcases.md`

```markdown
# Black-box Test Cases — T-001

## TC-001: 初回起動 — 許可ダイアログ
前提条件: フレッシュインストール（事前許可なし）。
手順: アプリを起動。
期待値: 使用説明文付きのiOS位置情報許可ダイアログが表示される。
合否: [ ]

## TC-002: 位置情報拒否
前提条件: ダイアログまたは設定で位置情報を拒否。
手順: アプリを開く。
期待値: 「位置情報へのアクセスが必要です」メッセージが表示。
       「設定を開く」ボタンがiOS設定 → WeatherNowを開く。
合否: [ ]

## TC-003: 天気の読み込み成功
前提条件: 位置情報許可済み、ネットワーク利用可能。
手順: アプリを起動。
期待値: 都市名、気温（°C）、説明、アイコンがすべて表示。
       スピナーなし。エラーメッセージなし。
合否: [ ]

## TC-004: オフライン — キャッシュなし
前提条件: 機内モードを有効化。アプリデータを消去（フレッシュインストール）。
手順: アプリを起動。
期待値: 「接続なし — ネットワークを確認してください」空の状態 + 再試行ボタン。
合否: [ ]

## TC-005: オフライン — キャッシュあり
前提条件: 一度天気を正常に読み込む。機内モードを有効化。
手順: プルトゥリフレッシュ。
期待値: 古い天気データが表示。「最終更新 X分前」バナーが表示。
合否: [ ]

## TC-006: プルトゥリフレッシュ
前提条件: 天気が正常に読み込まれている。
手順: 画面を引き下げる。
期待値: ローディングインジケーターが表示され、その後最新データで天気が更新される。
合否: [ ]

## TC-007: 低精度の位置情報
前提条件: シミュレーターで低精度を強制（都市レベルの精度）。
手順: 天気を読み込む。
期待値: 天気が表示。「おおよその位置」ラベルが表示。
合否: [ ]
```

**あなた**: iOSシミュレーターや実機で手動テスト。各ケースの合否を記入する。

---

### Phase 8 — 最終レポート

**コマンド**: `/sdd-report T-001`

**生成**: `docs/changes/T-001/report.md`

```markdown
# Final Report — T-001: 現在の天気画面

ステータス: 完了 ✓
完了日: 2026-06-01

## 概要
WeatherNow iOSの現在の天気画面をゼロから実装した。
MVVM + Clean Architectureの完全な基盤を確立。
13個のSwiftファイルを作成。ユニットテスト全パス（8/8）。ブラックボックステスト全パス（7/7）。

## 確立されたアーキテクチャ（次のチケットで再利用可能）
- 型付きViewState enumを持つ@Observable ViewModelパターン
- Repositoryプロトコル + URLSession実装（テストでモック可能）
- CoreLocation async/await wrapper
- 鮮度メタデータ付きUserDefaultsキャッシュレイヤー
- アプリエントリーポイントでの依存性注入

## 受け入れたリスク
- AR-001: Info.plistのAPIキー — App Store前にサーバーサイドプロキシに移行（T-003）。

## 推奨されるフォローアップチケット
- T-002: 時間別予報画面（WeatherRepository、LocationServiceを再利用）
- T-003: APIキーサーバープロキシ（公開前にAR-001を解決）
- T-004: ホーム画面ウィジェット（ホーム画面に現在気温のウィジェット）
- T-005: ネットワークタイムアウト時のリトライロジック追加
```

---

### Phase 9 — ラーニング & リビングドキュメント

**コマンド**: `/sdd-learnings T-001`

**生成**: `docs/changes/T-001/promotion-candidates.md`

```markdown
# Promotion Candidates — T-001

## PC-001: @Observable ViewModelパターン
→ プロモート先: docs/standards/coding-conventions.md
内容: すべてのViewModelは@Observable + 型付きViewState enumを使用。
状態変更は@MainActor経由のみ。依存関係はinitで注入。

## PC-002: Repositoryプロトコルパターン
→ プロモート先: docs/standards/coding-conventions.md
内容: すべてのデータソースはSwiftプロトコルで定義。
具体的な実装は注入 — ViewModelの内部でインスタンス化しない。

## PC-003: Info.plistのAPIキー保存（障害モード）
→ プロモート先: docs/maintenance/failure-mode-index.md
障害: Info.plistのAPIキーはコンパイル済みバイナリから読み取り可能。
解決策: 公開配布前にサーバーサイドプロキシエンドポイントを使用。
優先度: 高 — App Store提出前に解決必須。
```

**あなた**: プロモートする候補を承認する。AIは承認されたパターンで`docs/standards/`と`docs/maintenance/failure-mode-index.md`を更新。

---

## T-001後に変わること

最初のチケット完了後、`/sdd-map`を再実行して`[PLANNED]`エントリーを実際のソースパスに置き換える:

```
/sdd-map
```

アーキテクチャドキュメントが以下で更新される:
- 実際のファイルパス（`[PLANNED]`でなくなる）
- 実際のメソッドシグネチャ（ソースから確認済み）
- テストカバレッジマップ

**T-002: 時間別予報**を開始するとき、Phase 2（`/sdd-context`）はゼロから計画する代わりに、ソースコードの実際のパターンを参照できる。

---

## まとめ: グリーンフィールドプロジェクトの重要ポイント

| ポイント | 注意すべきこと |
|---|---|
| Phase 0-Bの出力は`[PLANNED]` | 正しい — ソーススキャンではなくアーキテクチャ決定 |
| 最初のチケットでM3が一般的 | 複数レイヤーを同時に作成 → 常にPhase 2+3が必要 |
| AIができない手動ステップ | Info.plistへの文字列追加、Xcodeプロジェクト設定 |
| T-001後に`/sdd-map`を再実行 | 計画されたアーキテクチャをT-002+の実際のソースマップに変換 |
| AR-001の受け入れたリスク | 公開リリース前に追跡して解決すること |
