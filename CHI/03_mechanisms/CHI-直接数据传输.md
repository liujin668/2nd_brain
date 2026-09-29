---
type: mechanism
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases:
  - "DMT"
  - "DCT"
  - "DWT"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B1.7"
  - "B5.1"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-直接数据传输

直接传输通过减少数据经过的节点跳数改善延迟和互连带宽利用；不同机制的数据发送者不同。【B1.7】

| 机制 | 数据路径 |
| --- | --- |
| DMT：Direct Memory Transfer | Subordinate → Requester |
| DCT：Direct Cache Transfer | Peer RN-F → Requester |
| DWT：Direct Write-data Transfer | Requester → Subordinate |

DCT 的数据提供方须告知 Home 数据已发送，部分情况下还要向 Home 提供数据副本。【B1.7】

## 边界

数据直达不代表 Home 不再承担协议职责。具体控制消息和状态依流程变化，不能用上表代替完整时序。

## 案例

[[CHI-案例-读数据来源与直接传输]] 比较路径。[[CHI-转换文本疑点]] 记录 D1 术语表与本节的疑似冲突。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L1561|B1.7]]；原始 CHI.md 第 1596 行起。
- [[CHI-Source-IHI0050H#原文 L11881|B5.1]]；原始 CHI.md 第 11974 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
