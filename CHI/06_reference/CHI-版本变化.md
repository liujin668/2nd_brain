---
type: reference
status: draft
topics:
  - "[[CHI-架构与通信-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "C5.11"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-版本变化

本库以 IHI0050 Issue H 为依据；不宣称它是当前最新规范。

## G.b 到 H 的已记录变化

- 新增 GDI 及相关属性。
- PAS 字段替代此前的 NS、NSE 字段。
- 增加 NodeID_Width 支持范围。
- 新增 Multi-request 及相关支持属性。
- 增加 RP 相关属性以及 Retry_Support。

以上均来自 C5.11；属性新增不自动等价于所有相关机制都在 H 首次提出。

## 维护规则

新版本进入时保留旧 Source，逐条比较受影响结论；仅对有证据的条目填写 introduced_in。

重点关联：[[CHI-GDI]]、[[CHI-RME与PAS]]、[[CHI-Multi-request]]、[[CHI-Resource-Planes]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L26881|C5.11]]；原始 CHI.md 第 26905 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
