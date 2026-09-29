---
type: transaction
status: draft
topics:
  - "[[CHI-顺序与完成-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B2.7.2"
  - "B2.3.3"
  - "B4.2.5"
  - "C4.1"
  - "C4.2"
  - "C4.3"
  - "C4.4"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-Atomic事务族

CHI 的 Atomic 事务族包括 AtomicCompare、AtomicLoad、AtomicStore 和 AtomicSwap。【C4.1–C4.4】

## 学习与查阅方式

B2.3.3 给出事务结构，B4.2.5 给出请求语义，B5.4 给出流程；阅读时必须结合具体操作类别，不能仅因名称含 Atomic 就套用同一返回流程。

组件只能在保证所有观察者看到原子操作结果时给出 Comp 或 CompDBIDResp。【B2.7.2】

## 边界

Atomic 与 [[CHI-Exclusive访问与Monitor]] 不等价；前者是事务操作族，后者围绕独占序列和监控成功/失败。

操作数布局、大小和对齐详细表暂不转写；需要使用时回查 B2.9.6。规则背景见 [[CHI-多副本原子性与Ordering]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L5641|B2.7.2]]；原始 CHI.md 的 B2.7.2 Completion response and ordering，原子完成条件位于该节后部。

- [[CHI-Source-IHI0050H#原文 L3241|B2.3.3]]；原始 CHI.md 第 3347 行起。
- [[CHI-Source-IHI0050H#原文 L9001|B4.2.5]]；原始 CHI.md 第 9105 行起。
- [[CHI-Source-IHI0050H#原文 L24361|C4.1]]；原始 CHI.md 第 24361 行起。
- [[CHI-Source-IHI0050H#原文 L24361|C4.2]]；原始 CHI.md 第 24396 行起。
- [[CHI-Source-IHI0050H#原文 L24361|C4.3]]；原始 CHI.md 第 24428 行起。
- [[CHI-Source-IHI0050H#原文 L24361|C4.4]]；原始 CHI.md 第 24461 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
