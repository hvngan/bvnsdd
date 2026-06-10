# 例: WeatherNow（iOS）をゼロから構築する

**シナリオ**: *WeatherNow* という新しい iOS 天気アプリをゼロから構築します — 既存のコードベースはありません。

| | |
|---|---|
| プラットフォーム | iOS 17+, Swift 5.9, SwiftUI |
| 状態 | グリーンフィールド — コードなし |
| チケット | **T-001** — 現在の天気画面（位置情報ベース） |

コードベースがすでに存在する場合との違いは `EXAMPLE-cross-platform-weather-ja.md` で確認してください。

---

## 0. セットアップ

```bash
bvn-sdd check
git clone git@github.com:my-org/weathernow-ios.git
cd weathernow-ios
bvn-sdd init --here --lang ja
```

**Claude Code** でプロジェクトを開きます。

---

## Phase 0-A — Safety Gate (`/sdd-phase0a`)

**実行** — ソースが存在しないため、コマンドの直下にプロジェクトを説明します（必須）:
```
/sdd-phase0a

プロジェクト: WeatherNow — 新しいiOS天気アプリ、コードなし。
プラットフォーム: iOS 17+, SwiftUI, MVVM + Clean Architecture, Swift Package Manager。
外部API: OpenWeatherMap（REST、APIキーで認証）。
オフライン: 最後の成功レスポンスをキャッシュ；「最終更新: X分前」バナーを表示。
```

**あなたが行うこと:**
- `docs/maintenance/phase0/phase0-plan.md` を読む
- AI が提起するオープンな質問に回答する（モジュール構造、キャッシュの陳腐化しきい値など）

---

## Phase 0-B — Source Intelligence — グリーンフィールドモード (`/sdd-map`)

**実行:**
```
/sdd-map
```

**あなたが行うこと:**
- `docs/architecture/system-map.md` を読む — これは**アーキテクチャ決定書**であり、すべてのエントリは `[PLANNED]` でマークされます
- 必要に応じてモジュール構造を調整する — このファイルはすべての後続チケットの設計図です
- 最初のチケットを開始する前に承認する

---

## ブートストラップ (`/sdd-new T-001`)

**実行:**
```
/sdd-new T-001 現在の天気画面
```

---

## Phase 1 — Spec Pack (`/sdd-spec T-001`)

**実行** — コマンドの直下に元の要件を貼り付けます:
```
/sdd-spec T-001

[Jira / メール / ブリーフからの要件をここに貼り付け]
```
手動入力が必要なのはこのフェーズのみです。

**あなたが行うこと:**
- ACが正確で完全か確認する
- 次のステップに進む前に `open-issues.md` のすべての項目に回答する

---

## Phase 1 — Right-sizing (`/sdd-rightsize T-001`)

**実行:**
```
/sdd-rightsize T-001
```

**あなたが行うこと:**
- `mode-decision.md` を読み、モード（M1–M5）を確認する
- グリーンフィールドプロジェクトの最初のチケットは、複数レイヤーを同時に作成するため通常 M2–M3

---

## Phase 2 — Context (`/sdd-context T-001`)

**実行:**
```
/sdd-context T-001
```

**あなたが行うこと:**
- 確立されるコンベンションとパターンを確認する（`[PLANNED]` — まだ実際のコードはない）
- `source-map.md` が変更するファイルではなく**新規作成するファイル**を列挙していることを確認する

---

## Phase 3 — Impact & Plan (`/sdd-plan T-001`)

**実行:**
```
/sdd-plan T-001
```

**あなたが行うこと:**
- `impl-plan.md` の実装順序を確認する（依存関係は正しい順序か？）
- AI が実行できない手動ステップをメモする（例: Xcode で Info.plist にキーを追加する）
- **明示的に承認する** — 確認するまで AI はコードを書きません

---

## Phase 4+5 — Implement (`/sdd-implement T-001`)

**実行:**
```
/sdd-implement T-001
```

**あなたが行うこと:**
- AI がコーディングを始める前にレビューチェックリストを承認する（AI は一時停止して待ちます）
- 手動ステップを並行して実行する（例: Xcode で Info.plist 文字列を追加する）
- AI が書いたすべてのコード（diff）を読む
- `human-review.md` を記入する — AI はこのファイルを記入してはいけません

---

## Phase 6 — Test (`/sdd-test T-001`)

**実行:**
```
/sdd-test T-001
```

**あなたが行うこと:**
- `xcodebuild test -scheme WeatherNow -destination 'platform=iOS Simulator,...'` を実行する
- 続行前にすべてのテストが PASS することを確認する

---

## Phase 7 — Black-box Test (`/sdd-blackbox T-001`)

**実行:**
```
/sdd-blackbox T-001
```

**あなたが行うこと:**
- iOS Simulator または実機で `blackbox-testcases.md` の各ケースを手動テストする
- 各ケースに Pass / Fail をマークする
- `test-data.md` に必要なフィクスチャを記入する

---

## Phase 8 — Final Report (`/sdd-report T-001`)

**実行:**
```
/sdd-report T-001
```

**あなたが行うこと:**
- `report.md` を読み、accepted risks とフォローアップチケットを確認する

---

## Phase 9 — Learnings (`/sdd-learnings T-001`)

**実行:**
```
/sdd-learnings T-001
```

**あなたが行うこと:**
- `promotion-candidates.md` を読む
- どのパターンを `docs/standards/` に、どの障害モードを `failure-mode-index.md` に追加するか確認する

---

## T-001 の後: アーキテクチャマップを更新する

**`/sdd-map` を再実行**して `[PLANNED]` エントリを実際のソースパスに置き換えます:
```
/sdd-map
```

T-002 以降、Phase 2 はゼロから設計する代わりに、ソース内の実際のパターンを参照できるようになります。
