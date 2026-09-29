---
type: concept
status: draft
topics:
  - "[[CHI-顺序与完成-MOC]]"
aliases:
  - "Multi-copy atomicity"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B2.7.1"
  - "B2.7.2"
  - "B2.7.5"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-多副本原子性与Ordering

本规范的内存模型要求 Multi-copy atomicity，合规组件必须保证写请求满足该要求。【B2.7.1】

## 两项条件

1. 对同一位置的写被序列化，所有 Requester 按相同顺序观察这些写；某些 Requester 可以没有观察到全部写。
2. 在所有 Requester 观察到一个写之前，读取该位置不能返回该写的值。

以上为 B2.7.1 的转述。

## 范围与边界

就一致性、可观察性和 Hazard 而言，判断同一位置需要同时考虑 cache line 地址和 PAS 属性。【B2.7.1】

完成响应的顺序含义随事务类型和内存属性变化，不应直接概括为“所有事务全局顺序执行”。【B2.7.2、B2.7.5】

[[CHI-PoC与PoS]] 提供序列化背景，[[CHI-Comp与CompAck]] 解释完成消息与后续 Snoop 的关系。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L5521|B2.7.1]]；原始 CHI.md 第 5639 行起。
- [[CHI-Source-IHI0050H#原文 L5641|B2.7.2]]；原始 CHI.md 第 5648 行起。
- [[CHI-Source-IHI0050H#原文 L5881|B2.7.5]]；原始 CHI.md 第 5883 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
