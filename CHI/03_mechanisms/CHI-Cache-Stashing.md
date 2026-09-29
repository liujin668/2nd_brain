---
type: mechanism
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases:
  - "Cache Stashing"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B7.1"
  - "B7.2"
  - "B7.3"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-Cache-Stashing

Cache Stashing 将数据放置在预计使用点附近的缓存，以改善性能；仅允许用于 Snoopable memory。【B7.1】

## 两种形式

- Write with Stash hint：写入时已知目标，可使用 WriteUniqueFullStash 或 WriteUniquePtlStash。
- Independent Stash request：放置请求与写入分离，可用 Shared 或 Unique 变体表达预期用途。

以上来自 B7.1–B7.3。

## 关键边界

Stashing 是性能提示，接收方允许不执行实际放置行为。不能把发出 Stash 等同于保证目标缓存命中。【B7.1】

目标可以涉及 peer cache、其 LP cache 或下游缓存，选择依赖目标标识。【B7.1、B7.4】

## 关联

节点角色见 [[CHI-节点角色与能力]]；数据标签的配套处理见 [[CHI-MTE与Tag一致性]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L13441|B7.1]]；原始 CHI.md 第 13472 行起。
- [[CHI-Source-IHI0050H#原文 L13441|B7.2]]；原始 CHI.md 第 13542 行起。
- [[CHI-Source-IHI0050H#原文 L13561|B7.3]]；原始 CHI.md 第 13586 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
