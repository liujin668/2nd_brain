---
type: case
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B1.7"
  - "B5.1.1"
  - "B5.1.2"
  - "B5.1.3"
  - "B5.1.4"
evidence: mixed
verification: needs-check
created: 2026-09-09
updated: 2026-09-09
---

# CHI-案例-读数据来源与直接传输

本例是规范已有读路径的对照，不是某个真实芯片的测量结果。

## 场景与结果

| 情形 | 数据路径概括 | 来源 |
| --- | --- | --- |
| DMT | Subordinate 直接向 Requester 发送数据 | B1.7、B5.1.1–B5.1.2 |
| DCT | Peer RN-F 直接向 Requester 发送数据 | B1.7、B5.1.3 |
| 不使用 DMT/DCT | 数据通过 Home 转发给 Requester | B1.7、B5.1.4 |

## 可得出的结论

数据来源与是否经过 Home 是不同观察维度；控制职责不能由数据箭头单独推断。

## 待确认

转换文本不能完整保存原图中的条件分支和时序。本例不指定未核实的初态，不补画完整消息顺序，不宣称具体周期收益。

机制定义见 [[CHI-直接数据传输]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L1561|B1.7]]；原始 CHI.md 第 1596 行起。
- [[CHI-Source-IHI0050H#原文 L11881|B5.1.1]]；原始 CHI.md 第 11977 行起。
- [[CHI-Source-IHI0050H#原文 L11881|B5.1.2]]；原始 CHI.md 第 11998 行起。
- [[CHI-Source-IHI0050H#原文 L12001|B5.1.3]]；原始 CHI.md 第 12030 行起。
- [[CHI-Source-IHI0050H#原文 L12121|B5.1.4]]；原始 CHI.md 第 12122 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
