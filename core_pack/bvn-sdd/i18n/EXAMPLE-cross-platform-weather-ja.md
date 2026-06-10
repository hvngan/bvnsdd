# 例: WeatherNow に予報画面を追加する（既存 Android + iOS コードベース）

**シナリオ**: *WeatherNow* は Android と iOS の両方にすでに存在し、現在の天気画面が動作しています。
BVN-SDD に従って **5日間予報画面**（T-001）を両プラットフォームに追加します。

| | |
|---|---|
| プラットフォーム | Android (Kotlin, Compose, Hilt) **+** iOS (Swift, SwiftUI, async/await) |
| 状態 | 既存コードベース — 現在の天気画面は動作済み |
| リポジトリ | monorepo: `android/` + `ios/` + `docs/` |

コードベースがない場合との違いは `EXAMPLE-ios-weather-ja.md` で確認してください。

---

## 0. セットアップ

```bash
bvn-sdd init --here --lang ja
```

`.bvn-sdd/config.yml` を編集して両プラットフォームを宣言します:

```yaml
platforms:
  - android
  - ios
platform_stack:
  android: "Kotlin, Jetpack Compose, Hilt, StateFlow"
  ios: "Swift, SwiftUI, @Observable, async/await"
```

**Claude Code** でプロジェクトを開きます。

---

## Phase 0-A — Safety Gate (`/sdd-phase0a`)

**実行:**
```
/sdd-phase0a
```
引数不要 — コマンドはプロジェクト構造と `config.yml` を自動的に読み取ります。

**あなたが行うこと:**
- `docs/maintenance/phase0/phase0-review.md` を読む
- 保留中の項目を確認・承認する

---

## Phase 0-B — Source Intelligence (`/sdd-map`)

**実行:**
```
/sdd-map
```

**あなたが行うこと:**
- `docs/architecture/system-map.md` を読む — §Parity Status を確認（両プラットフォームのベースラインが同じか？）
- `docs/architecture/platform-android-map.md` と `platform-ios-map.md` を読む
- AIが構造を誤解している場合は修正してから最初のチケットに進む

---

## ブートストラップ (`/sdd-new T-001`)

**実行:**
```
/sdd-new T-001 5日間予報画面
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
- specがプラットフォーム中立（WHAT であり HOW ではない）であることを確認する
- 次のステップに進む前に `open-issues.md` のすべての項目に回答する

---

## Phase 1 — Right-sizing (`/sdd-rightsize T-001`)

**実行:**
```
/sdd-rightsize T-001
```

**あなたが行うこと:**
- `mode-decision.md` を読み、モード（M1–M5）を確認する
- 注意: モードは各フェーズの**深さ**を設定するものであり、フェーズをスキップしません

---

## Phase 2 — Context (`/sdd-context T-001`)

**実行:**
```
/sdd-context T-001
```

**あなたが行うこと:**
- パターンとメソッドがコードベースに実際に存在することを確認する
- パリティギャップを確認する — 一方のプラットフォームに必要なベースライン機能がない場合、続行前に解決する

---

## Phase 3 — Impact & Plan (`/sdd-plan T-001`)

**実行:**
```
/sdd-plan T-001
```

**あなたが行うこと:**
- `impact-analysis.md` と `impl-plan.md` を読む
- クロスプラットフォームパリティ表を確認する（Android と iOS が同一の動作をするか？）
- **明示的に承認する** — 確認するまで AI はコードを書きません

---

## Phase 4+5 — Implement (`/sdd-implement T-001`)

**実行:**
```
/sdd-implement T-001
```

**あなたが行うこと:**
- AI がコーディングを始める前にレビューチェックリストを承認する（AI は一時停止して待ちます）
- AI が書いたすべてのコード（diff）を読む
- `human-review.md` を記入する — AI はこのファイルを記入してはいけません

---

## Phase 6 — Test (`/sdd-test T-001`)

**実行:**
```
/sdd-test T-001
```

**あなたが行うこと:**
- 両プラットフォームでテストを実行して PASS を確認する
- Android: `./gradlew :app:testDebugUnitTest`
- iOS: `xcodebuild test -scheme WeatherNow -destination '...'`

---

## Phase 7 — Black-box Test (`/sdd-blackbox T-001`)

**実行:**
```
/sdd-blackbox T-001
```

**あなたが行うこと:**
- `blackbox-testcases.md` の各ケースを**両プラットフォームで**手動テストする
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

## グリーンフィールドとの主な違い

| 既存コードベース（この例） | グリーンフィールド |
|---|---|
| Phase 0-A: プロジェクト説明不要 — AI がソースを読む | Phase 0-A: メッセージにプロジェクトを説明する必要あり |
| Phase 0-B: Surveyモード — 実際のソースを読む | Phase 0-B: グリーンフィールドモード — すべて `[PLANNED]` |
| context.md: 既存パターンを検証する | context.md: 新しいパターンを設計し `[PLANNED]` でマーク |
| source-map.md: 変更するファイル + 新規ファイル | source-map.md: 新規作成するファイル |
| パリティチェック: 両プラットフォームのベースラインを検証 | 最初からパリティ負債なし |
| 最初のチケット後: `/sdd-map` の再実行不要 | 最初のチケット後: **`/sdd-map` を再実行**して `[PLANNED]` を置換 |
