# ウォークスルー：Heavy な DB マイグレーション（M4、既存システム）

**シナリオ**：同じ EC バックエンドで **`orders.customer_name` 列を
`orders.customer_id` + 新しい `customers` テーブルに分割**する — バックフィルを伴い、
本番データを持つシステム上での破壊的傾向のスキーマ変更。これは **M4（Heavy）**：
フルの深さ、オンデマンドの深いアーティファクト（heavy source analysis、security
review、独立レビュー）、明示的な expand-contract ロールバック計画 — そして
**どのフェーズもスキップしません**。

> これは**ドキュメント例**です。**テスト FAIL → 修正** サイクルと、**オンデマンドで
> 作成**される M4 専用の深いアーティファクト（既定の 20 ファイルスキャフォールドの
> 一部ではない）を意図的に示し、「Core は軽く、オプションは深く」を表します。
>
> モードは**深さ**を上げ、フェーズをスキップしません。停止するのは MX のみ。

**チケット概要**

| | |
|---|---|
| チケット | **T-077** — 顧客データ正規化: `customer_name` → `customer_id` + `customers` |
| Stack | Spring Boot 3, JPA, **Flyway** マイグレーション, PostgreSQL（本番データ） |
| モード | **M4（Heavy）** — スキーマ移行、バックフィル、多層影響 |
| 深いアーティファクト（オンデマンド） | `heavy-source-analysis.md`, `security-review.md`, `codex-review.md` |

---

## Phase 0-A / 0-B（このリポジトリでは実施済み）

`project_type = existing` は記録済み；`/sdd-map` の survey マップが存在（survey 例
参照）。M4 チケットでは計画前に**影響領域で `/sdd-map` を再実行**し、
`repository-db-map.md` と `route-api-map.md` を更新します。

---

## T-077 ブートストラップ — `/sdd-new T-077 Normalise customer data`

---

### Phase 1 — Spec Pack（`/sdd-spec T-077`）

```markdown
## 6. Acceptance Criteria
- [ ] AC-1: 新 `customers` テーブル (id, name, created_at)；移行中は name に unique。
- [ ] AC-2: `orders.customer_id` FK → customers.id、expand 中は nullable。
- [ ] AC-3: 既存の全注文を customer 行へバックフィル（データ損失なし）。
- [ ] AC-4: クライアントへの API/応答挙動は不変（customer_name を引き続き返す）。
- [ ] AC-5: マイグレーションは contract 段階まで可逆；ロールバックを文書化。
- [ ] AC-6: バックフィル中に PII（customer_name）をログに書かない。

## 11. Security / Privacy
customer_name は PII。バックフィルは名前をログしない；アクセスは既存スコープ内。
```

`source-availability.md` → GREEN。`open-issues.md` OI-1:「重複名 — マージするか別顧客
として保持するか？」（blocking — 人間の判断が必要）。

---

### Phase 1-B — ライトサイジング（`/sdd-rightsize T-077`）

```markdown
# Mode Decision — T-077
## Scoring: Reversibility 3 | Uncertainty 2 | Risk 3 | Scope 3  → M4
## 決定: M4 (Heavy) — 本番データ上の破壊的傾向スキーマ変更 + バックフィル。
## フェーズ別の深さ: すべてのフェーズをフルの深さで実行（スキップなし）。
## 本チケットで必要なオンデマンド深いアーティファクト:
##   - heavy-source-analysis.md  (customer_name の使用箇所)
##   - security-review.md        (バックフィル/ログの PII)
##   - codex-review.md           (マージ前の独立レビュー)
## 人間ゲート: OI-1 を Phase 3 前に解決；マージ前にロールバックを検証。
```

**Stop/Ask**: OI-1 は blocking → AI は停止して質問。**あなた**が判断：「unique な名前
ごとに別顧客を保持；重複は当面許容」。

---

### Phase 2 — Context（`/sdd-context T-077`）

フルの深さ + オンデマンドの **heavy source analysis**:
```markdown
# heavy-source-analysis.md — T-077  (M4 深いアーティファクト、オンデマンド作成)
## customer_name の読み書き箇所（Grep で検証）
- OrderEntity.customerName            (JPA フィールド)   — 書き込み経路
- OrderMapper.toResponse              (name を読む)      — AC-4 で返し続ける
- OrderSearchRepository.byCustomer    (name に LIKE)     — join に切替必要
- ReportJob.exportCustomers           (バッチ、毎晩)     — リスク: name を一括読込
## リスク領域
- ReportJob は毎晩実行 → デプロイ中にマイグレーションが壊さないこと（expand-contract）。
- 名前検索は index 使用 → customers(name) に代替 index を計画。
```
`context.md` は禁止パターンを記録：**`customerName` を決してログしない**（AC-6）。

---

### Phase 3 — Plan（`/sdd-plan T-077`）

```markdown
# Impl Plan — T-077  (expand → migrate → contract)
## Phase A (expand、可逆):
  V12__create_customers.sql        — 新テーブル、orders.customer_id は nullable
  name + customer_id を DUAL-WRITE するアプリをデプロイ
## Phase B (backfill):
  V13__backfill_customers.sql      — distinct name → customers に挿入; orders.customer_id を設定
  バッチでバックフィル；name をログしない（AC-6）
## Phase C (contract、後続チケット): 全リーダー移行後に orders.customer_name を drop

## Migration / rollback
- Phase A/B 可逆: customer_id + customers を drop（データは customer_name に保持）。
- ロールバックスクリプト: V13_rollback.sql を文書化しステージングでテスト。
- 後戻り不能点: Phase C（別チケット、別承認）。
```

---

### Phase 4+5 — Implement + レビュー（`/sdd-implement T-077`）

Dual-write 実装 + Flyway スクリプト。続いて**2 つのレビュー**（M4 の深さ）:

```markdown
# self-review.md (Claude)
- [x] Dual-write が customer_name を維持（AC-4 後方互換）
- [x] バックフィルはバッチ；ログに name なし（AC-6）
- [ ] WARN: unique(name) 制約は既存の重複名で失敗 → テスト参照

# codex-review.md (独立、M4 オンデマンド)
Verdict: NEEDS_FIX
- [Major] V12 は UNIQUE(name) を追加するが本番に重複名あり → マイグレーションが中断。
  Fix: 移行用 unique を partial/deferred にする、または name でなく id で重複排除。
```

独立レビューがマージ前に実在の欠陥を捕捉。

---

### Phase 6 — Test（`/sdd-test T-077`）— FAIL → 修正

```markdown
# test-results.md — Run 1
FAIL  MigrationTest.backfillPreservesAllOrders
  → V12 UNIQUE(name) 違反: "John Smith" の既存 2 行。
  根本原因: 本番相当データに重複名（codex-review の Major と一致）。

# 適用した修正
- V12: UNIQUE(name) を UNIQUE(id) に置換；移行中は重複名を許容
  （OI-1 の判断と一致: 行ごとに別顧客を保持）。
- バックフィル再実行: 各注文 → 独自の customer 行。

# test-results.md — Run 2
PASS  MigrationTest.backfillPreservesAllOrders   (注文損失 0; 1:1 マッピング)
PASS  MigrationTest.rollbackRestoresState
PASS  OrderApiContractTest.customerNameStillReturned   (AC-4)
PASS  BackfillLoggingTest.noPiiInLogs                  (AC-6)
```

> この FAIL→修正 サイクルが要点：M4 の深さ（独立レビュー + 実マイグレーション
> テスト）が、happy path では見逃す本番データの危険を捕捉した。

---

### Phase 7 — Black-box（`/sdd-blackbox T-077`）

```markdown
### TC-1: 既存注文が依然読める
Input: GET /api/orders/9001 (マイグレーション前に作成)
Expected: customer_name は従来どおり返る（AC-4）；今は customer_id にもリンク。

### TC-2: ロールバック訓練（ステージング）
Steps: V12+V13 を適用、文書化したロールバックを実行。
Expected: スキーマ + データがマイグレーション前へ復帰；注文損失なし（AC-5）。

### TC-3: バックフィルのログ検査
Steps: debug ログ有効でバックフィル実行。
Expected: どのログ行にも顧客名文字列が現れない（AC-6）。
```

---

### Phase 8 — Report（`/sdd-report T-077`）

```markdown
# Final Report — T-077   Status: COMPLETE（expand + backfill 段階）
expand-contract で顧客データを正規化。Dual-write が API を安定維持（AC-4）。
独立レビュー + マイグレーションテストがマージ前に重複名中断を捕捉。
テスト: Run 1 FAIL（重複名）→ 修正 → Run 2 全 PASS。

## Accepted risks
- AR-1: contract チケット（T-09x）まで orders.customer_name を維持 — 意図的。
## Security
- security-review.md: PASS — ログに PII なし；アクセススコープ不変。
## Follow-up
- T-09x: contract 段階（customer_name を drop）— 別チケット + 承認（後戻り不能点）。
```

---

### Phase 9 — Learnings（`/sdd-learnings T-077`）

```markdown
# Promotion Candidates — T-077
## PC-1 → docs/maintenance/failure-mode-index.md
Failure: マイグレーション中に列が unique と仮定。本番データに重複名があった。
Prevention: dedupe/移行計画なしに自由テキストへ UNIQUE を追加しない。
## PC-2 → docs/standards/database.md
常に expand → backfill → contract を別デプロイで；各ステップを可逆に保つ。
```

---

## まとめ — M4（Heavy）が加えるもの、フェーズはスキップしない

| 観点 | M2/M3 | **M4（本例）** |
|---|---|---|
| 実行フェーズ | すべて | すべて（フルの深さ） |
| ソース分析 | 標準マップ | + `heavy-source-analysis.md`（使用箇所、バッチリスク） |
| レビュー | self（+ 任意の codex） | self **+ 独立 `codex-review.md`**（欠陥を捕捉） |
| セキュリティ | インライン | + 専用 `security-review.md`（バックフィルの PII） |
| マイグレーション | 通常なし | expand→backfill→contract + テスト済みロールバック |
| テスト | PASS | 本番相当データで **FAIL→修正**、その後 PASS |

上記の深いアーティファクトは **M4 のためオンデマンドで作成** — すべてのチケットには
スキャフォールドされず、M1/M2 の作業では core を軽く保ちます。
