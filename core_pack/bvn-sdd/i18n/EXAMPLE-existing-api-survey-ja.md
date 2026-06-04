# ウォークスルー：既存 API へのフィールド追加（Survey モード、M3）

**シナリオ**：既存の EC バックエンド（Spring Boot）+ Web フロントエンド（React）に
参加します。チケット **T-042** は小さいがコントラクトに触れる変更を求めます：注文
詳細 API が人間可読の `statusLabel` も返し、フロントエンドがステータス文言をハード
コードしないようにします。ソースが存在するため Phase 0-B は **Survey モード**（実
ソースを読む）で実行され、FE/BE コントラクトを変えるためモードは **M3** です。

> これは**ドキュメント例**です — 既存コードベースでのアーティファクトの見え方を示す
> もので、実行すべき実コードではありません。`EXAMPLE-ios-weather-ja.md`（グリーン
> フィールド）と比較すると Survey モードが何を加えるか分かります。
>
> **すべてのフェーズが実行されます。** M3 は深さ（標準 + コントラクト重視）を決め、
> フェーズをスキップしません。停止するのは MX のみ。

**プロジェクト概要**

| | |
|---|---|
| バックエンド | Java 17, Spring Boot 3, JPA/Hibernate, PostgreSQL |
| フロントエンド | React 18, TypeScript, React Query |
| 状態 | **既存**コードベース（ブラウンフィールド） |
| チケット | **T-042** — `GET /api/orders/{id}` 応答に `statusLabel` を追加 |
| モード | **M3**（FE/BE コントラクト変更） |

---

## 0. セットアップ（既存リポジトリ内）

```bash
cd ecommerce-platform          # 既存のモノレポ
bvn-sdd init --here --lang ja
# ✓ .claude/ .bvn-sdd/ docs/ を作成（既存ファイルは決して上書きしません）
```

**Claude Code** で開き、`/sdd-phase0a` を実行。

---

## Phase 0-A — Safety Gate（既存プロジェクト）

```
/sdd-phase0a

Project: ecommerce-platform — 既存の Spring Boot API + React Web。
Stack: Java 17 / Spring Boot 3 / JPA / PostgreSQL; React 18 / TS / React Query.
Constraints: 本番 DB が存在 — ここから破壊的マイグレーションを実行しない。
Secrets: application-prod.yml に DB 認証情報 — 読まない。
```

**AI の動作**：ソースを Glob → `src/main/java/...`、`web/src/...` を発見 →
`project_type = existing` を記録。

**生成**（抜粋）`docs/maintenance/phase0/phase0-plan.md`:
```markdown
## Project Type
existing — ソース検出（Spring Boot バックエンド + React フロントエンド）

## Safety Constraints Recorded
- DENY 読取: application-prod.yml, .env, *.pem
- ASK 前提: Flyway/Liquibase マイグレーション、git push
- 真実の情報源の優先順位: ソースコード > ドキュメント > AI 推論
```

`/sdd-phase0a` は `phase0-decisions.md`、`phase0-execution-log.md`、
`phase0-risk-register.md`、`phase0-review.md`、および 3 つの
`docs/standards/automation/*` ポリシーも生成します。**あなた**は `phase0-review.md`
を確認しサインオフします。

---

## Phase 0-B — Source Intelligence（SURVEY モード）

**コマンド**: `/sdd-map`

**AI の動作**：`project_type = existing` → **Survey モード**。実ソースを*浅く*読み
（全ファイルではない）、**実パス**でマップを生成 — `[PLANNED]` マーカーなし（対照：
グリーンフィールドの iOS 例はすべて `[PLANNED]`）。

**生成** `docs/architecture/system-map.md`（抜粋）:
```markdown
# System Map — ecommerce-platform   (Survey モード — ソースから観測)

## Components
| Component | 責務 | 主な場所 |
|---|---|---|
| Order API | order CRUD + status | src/main/java/com/shop/order/ |
| Order domain | Order, OrderStatus enum | src/main/java/com/shop/order/domain/ |
| Web order page | 注文詳細 UI | web/src/features/orders/ |

## 接続方法
React Query → GET /api/orders/{id} → OrderController → OrderService → OrderRepository → PostgreSQL
```

**生成**（いずれも実在、planned ではない）:
- `source-inventory.md` — 主要ファイルと目的
- `route-api-map.md` — `GET /api/orders/{id}`, `OrderController#getOrder`
- `repository-db-map.md` — `orders` テーブル、`OrderStatus` enum 値 `1/2/3/4`
- `fe-be-contract-map.md` — Web が消費する現在の `OrderResponse` の形
- `test-map.md` — `OrderControllerTest`, `OrderServiceTest`, web `orderApi.test.ts`

**あなた**：マップに目を通す；これがすべてのチケットのナビゲーションガイドになる。

---

## T-042: Order 応答に `statusLabel` を追加

### ブートストラップ — `/sdd-new T-042 Order statusLabel`

`docs/changes/T-042/` に 20 個の空アーティファクトを作成。

---

### Phase 1 — Spec Pack（`/sdd-spec T-042`）

```
/sdd-spec T-042

要件: GET /api/orders/{id} は `statusLabel` も返す — 既存の数値 `status`
(1=Pending, 2=Paid, 3=Shipped, 4=Cancelled) の人間可読ラベル。Web 注文ページは
自分で数値をマップせず statusLabel を表示。ラベルは当面英語；i18n は範囲外。
```

**AI が最初に読む**：`docs/architecture/*`（survey マップ）、次に実際の
`OrderController`、`OrderResponse`、`OrderStatus`。**生成** `spec-pack.md`（抜粋）:
```markdown
## 6. Acceptance Criteria
- [ ] AC-1: GET /api/orders/{id} 応答に新しい文字列フィールド `statusLabel` を含む。
- [ ] AC-2: statusLabel は status 1→"Pending", 2→"Paid", 3→"Shipped", 4→"Cancelled"。
- [ ] AC-3: 既存の `status`（数値）は不変 — 追加のみ、後方互換。
- [ ] AC-4: Web 注文ページは statusLabel を表示；ローカルの数値→文言マップを削除。
- [ ] AC-5: 未知の status 値 → statusLabel = "Unknown"（500 を出さない）。

## 9. Client/Service contract（プラットフォーム中立）
OrderResponse に追加: statusLabel: string (non-null)。`status` フィールドは不変。
後方互換: 新フィールドを無視する既存コンシューマはそのまま動作。
```

`source-availability.md` → GREEN（関連ソースすべて読取可能）。`open-issues.md` に
OI-1: 「ラベル文言をプロダクトと確認（Paid か Completed か？）」。

---

### Phase 1-B — ライトサイジング（`/sdd-rightsize T-042`）

```markdown
# Mode Decision — T-042
## Scoring: Reversibility 1 | Uncertainty 1 | Risk 2 | Scope 2  → M3
## 決定: M3 (Plus) — FE/BE コントラクトに触れるため、コントラクトの整合が重要。
## フェーズ別の深さ: 全フェーズを標準の深さで実行；§9 コントラクトを特に重視。
## オンデマンドの深いアーティファクト: fe-be-contract-map.md（チケットレベル）。
```

> 変更は小さくても FE/BE 境界を越える → M1 ではなく M3。全フェーズは依然実行。

---

### Phase 2 — Context（`/sdd-context T-042`）

EXISTING PROJECT MODE — AI は Grep/Read で実ソースに照合。

```markdown
# Context — T-042
## コードベース内の正しい例
- src/main/java/com/shop/order/OrderResponse.java — DTO は Java record；ここに追加。
- web/src/features/orders/orderApi.ts — React Query フック；型は DTO を反映。

## 実在するメソッド/クラス（検証済み）
- enum OrderStatus: PENDING(1), PAID(2), SHIPPED(3), CANCELLED(4)  ← Grep で確認
- OrderMapper.toResponse(Order) — DTO を組み立てる唯一の場所；ここを変更。

## 禁止
- React コンポーネントにラベルロジックを追加しない（AC-4 は FE マップを削除）。
- `status`（数値）のシリアライズを変えない（AC-3）。
```

`source-map.md` は触れる実ファイルを列挙：`OrderResponse.java`、`OrderMapper.java`、
`orderApi.ts`、`OrderStatusBadge.tsx` とそのテスト。

---

### Phase 3 — Plan（`/sdd-plan T-042`）

```markdown
# Impact Analysis — T-042
| Area | Affected? | 詳細 |
| Shared contract | Yes | OrderResponse +statusLabel（追加のみ、後方互換） |
| BE / API | Yes | OrderMapper が enum→ラベルをマップ |
| Web FE | Yes | statusLabel を消費；OrderStatusBadge.tsx のローカルマップ削除 |
| DB | No | スキーマ変更なし — 既存 status から導出 |
| Test | Yes | BE mapper テスト、contract テスト、web component テスト |

# Impl Plan — T-042
## BE: OrderResponse に statusLabel 追加；OrderMapper で OrderStatus → ラベルを switch；既定 "Unknown"。
## FE: orderApi.ts 型 +statusLabel；OrderStatusBadge.tsx は statusLabel を描画、numberToText() 削除。
## fe-be-contract-map.md: フィールド、型、null 可否、4 行の enum→ラベル + Unknown を記録。
```

---

### Phase 4+5 — Implement（`/sdd-implement T-042`）

```java
// OrderResponse.java — 追加フィールド（status は不変 → AC-3）
public record OrderResponse(Long id, int status, String statusLabel, /* ... */) {}

// OrderMapper.java
static String label(OrderStatus s) {
    return switch (s) {
        case PENDING -> "Pending";
        case PAID -> "Paid";
        case SHIPPED -> "Shipped";
        case CANCELLED -> "Cancelled";
    }; // enum は網羅的；防御的 "Unknown" は status をパースする箇所で処理（AC-5）
}
```
```tsx
// OrderStatusBadge.tsx — サーバーのラベルを信頼（AC-4）
export function OrderStatusBadge({ statusLabel }: { statusLabel: string }) {
  return <span className="badge">{statusLabel}</span>;
}
```

`self-review.md` で確認：status 不変（AC-3 ✓）、FE マップ削除（AC-4 ✓）、Unknown
経路（AC-5 ✓）。**あなた**が `human-review.md` を記入。

---

### Phase 6 — Test（`/sdd-test T-042`）

```markdown
# Test Plan — T-042
| AC | テスト種別 | テスト名 | 優先度 |
| AC-2 | BE unit | OrderMapperTest.labelsEachStatus | H |
| AC-3 | contract | OrderResponseContractTest.statusStillNumeric | H |
| AC-5 | BE unit | OrderMapperTest.unknownStatusLabel | M |
| AC-4 | web unit | OrderStatusBadge.test.tsx.rendersServerLabel | H |

## Run commands
./gradlew test
cd web && npm test
```
`test-results.md`: 4 PASS。後方互換 contract テストが既存コンシューマへの無影響を確認。

---

### Phase 7 — Black-box（`/sdd-blackbox T-042`）

```markdown
### TC-1: Paid 注文がラベルを表示
Input: GET /api/orders/1001  (DB で status=2)
Expected: response.statusLabel == "Paid"; response.status == 2 も依然存在。

### TC-2: 後方互換
Input: 未知フィールドを無視する旧クライアントが GET /api/orders/1001 を呼ぶ
Expected: 依然パース可能；`status` 数値は不変。

### TC-3: Web ページ
Input: /orders/1001 を開く
Expected: バッジが API 由来の "Paid" を表示（クライアント側マッピングなし）。
```

---

### Phase 8 — Report（`/sdd-report T-042`）

```markdown
# Final Report — T-042   Status: COMPLETE
追加の `statusLabel` を出荷；数値 `status` は不変（後方互換）。
BE 3 ファイル、FE 2 ファイル。テスト 4/4 PASS（後方互換 contract を含む）。
Accepted risk: なし。Open issue OI-1（文言）はプロダクトと合意：「Paid」を維持。
```

---

### Phase 9 — Learnings（`/sdd-learnings T-042`）

```markdown
# Promotion Candidates — T-042
## PC-1 → docs/standards/api-contract.md
人間可読ラベルはサーバーが所有；クライアントはローカルで enum→text を再マップしない。
## PC-2 → docs/maintenance/pattern-library.md
追加フィールドパターン: DTO を拡張 + 旧フィールド維持 → 既定で後方互換。
```

T-042 の後、コントラクトマップを更新する必要があれば `/sdd-map` を再実行。

---

## まとめ — Survey モードがグリーンフィールドに加えるもの

| | グリーンフィールド（iOS 例） | Survey モード（本例） |
|---|---|---|
| Phase 0-B ソースマップ | `[PLANNED]` 決定 | **実パス**、ソースから観測 |
| Phase 2 コンテキスト | 計画 API を設計 | Grep で実メソッド/enum を**検証** |
| リスクの焦点 | アーキテクチャ確立 | 既存コントラクトの**後方互換** |
| 実行フェーズ | すべて | すべて（M3 — 深さであり、スキップではない） |
