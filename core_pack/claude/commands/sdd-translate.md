---
description: BVN-SDD utility — translate key decision artifacts to Vietnamese for internal dev review (never for client delivery).
argument-hint: <TICKET-ID>
allowed-tools: Read, Write, Glob
---

You are producing an **internal Vietnamese review document** for ticket **$ARGUMENTS**.
Work in `docs/changes/$ARGUMENTS/`.

> **Language override for this command only:** Output `vi-review.md` in **Tiếng Việt**
> regardless of the project's configured language. All other artifacts remain in the
> project language. This document is internal — do NOT apply the project language rule to it.

## What to read

Read each of the following artifacts **if it exists** in `docs/changes/$ARGUMENTS/`.
Skip silently if absent:

1. `spec-pack.md`
2. `context.md`
3. `impact-analysis.md`
4. `impl-plan.md`
5. `test-plan.md`
6. `blackbox-testcases.md`
7. `blackbox-review-checklist.md`

Do NOT read `test-data.md`, source code, `self-review.md`, `human-review.md`, or report files.

## What to write

Write (or overwrite) `docs/changes/$ARGUMENTS/vi-review.md` using the structure below.

For each artifact, translate only the **substance** — decisions, scope, acceptance
criteria, risks, implementation steps, test cases. Omit boilerplate headers and
empty template sections. Keep each section concise; reviewers need accuracy, not verbosity.

---

## Template for `vi-review.md`

```markdown
> ⚠️ **NỘI BỘ — KHÔNG GIAO CLIENT**
> Đây là bản dịch tiếng Việt dành cho dev review.
> File gốc (tiếng Nhật) là nguồn chính xác — khi có xung đột, ưu tiên file gốc.
> Cập nhật: {ngày tạo} | Ticket: $ARGUMENTS

---

## Spec Pack (`spec-pack.md`)

### Mục tiêu
{dịch phần mục tiêu / background}

### Phạm vi (Trong scope)
{dịch danh sách in-scope}

### Ngoài phạm vi
{dịch danh sách out-of-scope}

### Acceptance Criteria
{dịch từng AC, giữ nguyên mã ID nếu có}

### Vấn đề mở (`open-issues.md` nếu có đề cập)
{liệt kê các open issue liên quan}

---

## Context (`context.md`)

{Tóm tắt ngắn: hệ thống liên quan, constraints đáng chú ý, quyết định đã xác nhận}

---

## Impact Analysis (`impact-analysis.md`)

### Rủi ro chính
{dịch các risk item}

### Files / module bị ảnh hưởng
{liệt kê files chính}

---

## Implementation Plan (`impl-plan.md`)

### Hướng tiếp cận
{dịch approach / design decision chính}

### Các bước thực hiện
{dịch step list}

### Stop/Ask points
{dịch các điểm cần dừng xác nhận với con người}

---

## Test Plan (`test-plan.md`)

### Test cases chính
{dịch test cases quan trọng}

### Điều kiện pass/fail
{dịch pass/fail criteria}

---

## Blackbox Test (`blackbox-testcases.md` + `blackbox-review-checklist.md`)

### Test cases blackbox
{dịch các test case từ blackbox-testcases.md}

### Checklist review blackbox
{dịch các mục check quan trọng từ blackbox-review-checklist.md}
```

---

## Stop / Ask condition

If any source artifact is missing entirely (all 5 absent), tell the user which
phases have not been run yet and stop — do not produce a partial file.

## When done

Print to the user:
- Path of file written: `docs/changes/$ARGUMENTS/vi-review.md`
- Which source artifacts were found / skipped
- One-line reminder: "File này là nội bộ — không commit vào branch giao client."
