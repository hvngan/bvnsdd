# BVN-SDD — クイックスタート（1ページ）
# Brycen Viet Nam — Spec-Driven Development

> **コマンドを実行するだけ** — ドキュメントをすべて読む必要はありません。
> 各コマンドは SDD-Installation Pack V04.2 のフェーズに対応し、
> `docs/changes/<チケットID>/` に具体的なアーティファクトファイルを生成します。

## 1. セットアップ（1回だけ）

```bash
bvn-sdd check              # git + Claude Code が利用可能か確認
bvn-sdd init my-project    # プロジェクトを作成（または: bvn-sdd init --here）
```

言語を選択してください: 1=Tiếng Việt / 2=English / 3=日本語

次に **Claude Code でプロジェクトを開き**、すぐに `/sdd-phase0a` を実行します。

## 2. SDD-Installation Pack V04.2 のフェーズ

| フェーズ（V04.2） | Claude Code コマンド | 生成されるもの | あなたが行うこと |
|---|---|---|---|
| **Phase 0-A** Safety Gate | `/sdd-phase0a` | `docs/maintenance/phase0/` + `docs/standards/automation/` — 安全証跡、コンテキストポリシー | **プロジェクトごとに1回。** `bvn-sdd init` 直後、`/sdd-map` 前に実行 |
| **Phase 0-B** Common Base / Source Intelligence | `/sdd-map` | `docs/architecture/` — ソースマップ、ルート、API、DBスキーマ、FE/BEコントラクト、テストカバレッジ | **プロジェクトごとに1回。** 最初のチケット前に実行 |
| **Bootstrap**（Phase 1の前） | `/sdd-new T-001` | `docs/changes/T-001/` + すべての空のアーティファクトファイル | チケットIDを設定 |
| **Phase 1** Investigation / Spec Pack | `/sdd-spec T-001` | `spec-pack.md`、`source-availability.md`、`open-issues.md` | ACが正しいか確認；Open Issuesに回答 |
| **Phase 1** Right-sizing | `/sdd-rightsize T-001` | `mode-decision.md` — モード M1–M5/MX + 適応ワークフロー | **重要:** 続行前にモードを確認 |
| **Phase 2** Ticket Context / Rules | `/sdd-context T-001` | `context.md`、`source-map.md`、`ticket-rules.md` | パターン、実在するメソッド、禁止パターンを確認 *（M1は簡潔に、スキップしない）* |
| **Phase 3** Impact Analysis / Impl Plan | `/sdd-plan T-001` | `impact-analysis.md`、`impl-plan.md` | FE/BE/DBの影響範囲と計画をレビュー *（M1は簡潔に、スキップしない）* |
| **Phase 4+5** Review Checklist + Implementation / AI Review / Human Review | `/sdd-implement T-001` | コード + `review-checklist.md`、`self-review.md` | AIが書いたコードを読む；セルフレビューを確認；**`human-review.md` を記入**して承認 |
| **Phase 6** Test Plan / Test Code | `/sdd-test T-001` | `test-plan.md`、`test-results.md` | テストが実際にPASSするか確認；結果を読む |
| **Phase 7** Black-box Test / Test Data | `/sdd-blackbox T-001` | `blackbox-testcases.md`、`test-data.md`、`blackbox-review-checklist.md` | ユーザー/QAの視点から動作を検証 *（M1は主要ケースのみ、スキップしない）* |
| **Phase 8** Test Results / Final Report | `/sdd-report T-001` | `report.md` | 最終レポートを読む；accepted riskとフォローアップを確認 |
| **Phase 9** Living Docs / Failure Mode Update | `/sdd-learnings T-001` | `promotion-candidates.md` + `docs/maintenance/failure-mode-index.md` 更新 | プロモーション候補をレビュー；プロジェクト標準への追加を承認 |

**ユーティリティ**（Spec 32 — Long Context / Strategic Compact）:
- `/sdd-compact T-001` → `strategic-compact.md` — セッションスナップショット。新しいセッションの冒頭に貼り付けて、すべてを再読せずに再開できます。

## 3. モード（`/sdd-rightsize` が決定）

> **モードは各フェーズの「深さ」を決めるもので、フェーズをスキップしません。** 単一・
> マルチプラットフォームを問わず、すべてのチケットが全フェーズを実行します。M1 は各
> アーティファクトを簡潔にするだけです。停止するのは **MX** のみ。

| モード | 名前 | 使用時期 | このモードでの深さ |
|---|---|---|---|
| **M1** | Light | テキスト修正、設定、3ファイル未満の小さなバグ | 全フェーズ実行、アーティファクトは簡潔（固有事項がなければ1行）；セルフレビューのみ |
| **M2** | Standard | 通常の機能開発、単一サービス | すべてのアーティファクトを標準の深さで |
| **M3** | Plus | FE+BEコントラクト変更、10〜30ファイル | 標準 + FE/BEコントラクト重視；必要に応じ深いアーティファクト追加（contract-map、codex-review） |
| **M4** | Heavy | アーキテクチャ変更、DBマイグレーション | フル + heavy-source-analysis、security-review、ロールバック/移行計画、独立レビュー |
| **M5** | Critical | セキュリティパッチ、本番インシデント | 最大 + 必須の人間ゲート（脅威モデル、テスト証跡、監査）；人間のリードにエスカレート |
| **MX** | Stop | 要件が不明または高リスク | 停止 — 先にOpen Issuesを解決。作業を止める唯一のモード |

## 4. 5つの必須ルール

1. **コードの前に計画。** AIは常に計画を先に提示します。編集の前に承認してください。
2. **`spec-pack.md` が唯一の真実の情報源。** 不明点は `open-issues.md` へ。推測禁止。
3. **ソースコードがドキュメントに勝る。** ドキュメント（Excel/PDF）とソースコードが矛盾する場合、ソースコードを信頼してください。
4. **シークレットに触れない。** `.env`、キー、トークン、PIIを読み取ったり出力したりしないでください。
5. **最終的な判断者はあなた。** AIのセルフレビュー後も、あなたが読んで承認してください。

## 5. STOP してエスカレーションするタイミング

- 正しく実装するためにソースが不足または読み取り不可
- シークレットや個人情報が露出
- 変更が決済・ログイン/権限・本番DBマイグレーションに影響
- ソースコードと仕様が矛盾している
- AIが存在しないメソッドやファイルを使おうとしている

## 6. ヒント

- すべての結果は `docs/changes/<チケットID>/` にあります — いつでも確認できます。
- 各コマンドの終わりに、AIが次に実行するコマンドを教えてくれます。
- 詳細なルール: `.claude/rules/`。プロジェクト標準: `docs/standards/`。

## 7. ウォークスルー例

**既存の Android + iOS コードベース**両方に対して WeatherNow に機能を追加する完全なウォークスルーは **[EXAMPLE-cross-platform-weather-ja.md](EXAMPLE-cross-platform-weather-ja.md)** を参照してください。

各フェーズで以下を示します:
- 実行する正確なコマンド
- AIが生成する重要なアーティファクトの内容（リアルな抜粋）
- 次のフェーズに進む前に行う判断または承認

既存コードベースの完全なパスをカバー: Phase 0-A → Phase 0-B（Survey Mode、`platform-android-map.md` + `platform-ios-map.md`） → T-001 ブートストラップ → Spec → Rightsize → Context（実際のパターンを検証、[PLANNED] なし） → Plan → Implement → Test → Black-box → Report → Learnings。

単一プラットフォーム ウォークスルー（グリーンフィールド、比較用）:
- **[EXAMPLE-ios-weather-ja.md](EXAMPLE-ios-weather-ja.md)** — iOS のみ、ゼロから構築（M2）。コードベースがない場合との比較。
