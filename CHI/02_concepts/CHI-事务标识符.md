---
type: concept
status: draft
topics:
  - "[[CHI-架构与通信-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B2.4"
  - "B2.5"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-事务标识符

标识符分别解决路由、事务匹配、数据缓冲区匹配及数据包定位等问题，不能把所有 ID 都视为请求的 TxnID。【B2.4】

| 字段 | 用途 |
| --- | --- |
| SrcID、TgtID | 标识源和目标，用于路由 |
| TxnID | 标识给定 Requester 的事务 |
| DBID | Completer 提供的标识，用于规定的数据或确认消息关联 |
| ReturnTxnID、FwdTxnID | 返回或转发路径上的事务关联 |
| DataID、CCID | 数据包及关键块标识 |
| CacheLineID | Multi-request 中的 cache line 标识 |

以上为 B2.4 的用途摘要；每种消息的字段值见 B2.5。

## 重要限制

重试请求不要求沿用原 TxnID。DBID 也不能无条件替换所有返回消息的 TxnID。【B2.4.2–B2.4.3】

路由见 [[CHI-SAM与目标路由]]；多行请求见 [[CHI-Multi-request]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L3961|B2.4]]；原始 CHI.md 第 4061 行起。
- [[CHI-Source-IHI0050H#原文 L4321|B2.5]]；原始 CHI.md 第 4407 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
