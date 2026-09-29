---
type: mechanism
status: draft
topics:
  - "[[CHI-内存管理与隔离-MOC]]"
aliases:
  - "Memory Tagging Extension"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B12.1"
  - "B12.3"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-MTE与Tag一致性

Memory Tagging Extension（MTE）将 Allocation Tag 与数据关联，并在规定访问中与 Physical Tag 比较。【B12.1】

## 基本单位与限制

每个对齐的 16-byte 数据区域关联一个 4-bit tag；memory tagging 仅允许用于 Normal WriteBack memory 请求。【B12.1】

读取取回 tag 时由 Requester 检查；携带 Physical Tag 的写检查由 Completer 执行。Tag 的传递、更新和检查依事务类别区分。【B12.1】

需要获取 tag 的读请求不能使用 Forwarding snoops；CMO 必须作用于数据及相应 memory tags。【B12.1】

## 关联

[[CHI-直接数据传输]] 的路径不能忽略 MTE 条件；[[CHI-Cache-Stashing]] 也有相关 tag 行为。Tag coherence 的完整状态组合仍应核对 B12.3 及后续各类事务规则。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L17161|B12.1]]；原始 CHI.md 第 17165 行起。
- [[CHI-Source-IHI0050H#原文 L17161|B12.3]]；原始 CHI.md 第 17237 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
