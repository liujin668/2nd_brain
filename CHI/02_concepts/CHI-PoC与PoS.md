---
type: concept
status: draft
topics:
  - "[[CHI-一致性-MOC]]"
aliases:
  - "Point of Coherence"
  - "Point of Serialization"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B1.3"
  - "B1.6"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-PoC与PoS

Point of Coherence（PoC）是所有能够访问内存的 agent 被保证看到某内存位置同一副本的点；Point of Serialization（PoS）决定不同 agent 请求间的顺序。【B1.3】

## 节点与职责

HN-F 包含 PoC，并预期承担 PoS；HN-I 不包含 PoC，但预期承担面向 IO 请求的 PoS。【B1.6】

所以 PoC 和 PoS 不是同义词，也不能仅因为一个节点负责排序就认定它负责缓存一致性。后一句是对原文节点职责的比较。

## 关联

[[CHI-节点角色与能力]] 描述承担者；[[CHI-多副本原子性与Ordering]] 描述顺序要求。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L1081|B1.3]]；原始 CHI.md 第 1178 行起。
- [[CHI-Source-IHI0050H#原文 L1441|B1.6]]；原始 CHI.md 第 1520 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
