---
type: mechanism
status: draft
topics:
  - "[[CHI-顺序与完成-MOC]]"
aliases:
  - "Exclusive Access"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B6.1"
  - "B6.2"
  - "B6.3"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-Exclusive访问与Monitor

Exclusive sequence 由 Exclusive Load、计算和 Exclusive Store 组成；若其他 Logical Processor 在两次访问之间更新该位置，Exclusive Store 必须失败且不更新数据。【B6.1】

## 指令动作与接口事务

并非每次 Exclusive Load 或 Exclusive Store 都产生对应接口事务；本地缓存与监控状态会影响是否需要协议交互。【B6.1】

Exclusive 支持 Snoopable 和 Non-snoopable 位置，监控和完成规则需要按目标类别区分。【B6.1–B6.3】

## 使用边界

这里描述 CHI 支持机制，不推导任何特定 CPU 的微架构实现。

[[CHI-Atomic事务族]] 是另一类原子更新机制，二者不要合并成同一个协议流程。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L12961|B6.1]]；原始 CHI.md 第 13069 行起。
- [[CHI-Source-IHI0050H#原文 L13081|B6.2]]；原始 CHI.md 第 13107 行起。
- [[CHI-Source-IHI0050H#原文 L13201|B6.3]]；原始 CHI.md 第 13217 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
