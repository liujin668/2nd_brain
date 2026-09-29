---
type: transaction
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "C4.27"
  - "C4.28"
  - "B4.2.1"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-ReadShared与ReadUnique

两种请求都针对 Snoopable 地址区域，区别在于请求意图和允许返回状态。【C4.27–C4.28】

| 请求 | 意图 | 允许的数据返回状态 |
| --- | --- | --- |
| ReadShared | 为 load 读取 cache line | UC、UD、SC、SD |
| ReadUnique | 为 store 获取 cache line | UC、UD |

## 名称不等于最终状态

ReadShared 并不保证最终 Shared。当 Requester 能接受 SD 时，可使用 ReadShared 而非 ReadNotSharedDirty。【C4.27】

完整初态、终态和 peer 状态限制还需查 B4.2.1 对应表；本表不是完整合法性矩阵。

## 阅读路径

先读 [[CHI-Cache状态模型]]，再读 [[CHI-Comp与CompAck]] 和 [[CHI-直接数据传输]]。具体消息字段见 C4 中指向 C1 的索引。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L24961|C4.27]]；原始 CHI.md 第 25050 行起。
- [[CHI-Source-IHI0050H#原文 L24961|C4.28]]；原始 CHI.md 第 25076 行起。
- [[CHI-Source-IHI0050H#原文 L8041|B4.2.1]]；原始 CHI.md 第 8067 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
