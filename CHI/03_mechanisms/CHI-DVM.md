---
type: mechanism
status: draft
topics:
  - "[[CHI-内存管理与隔离-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B8.1"
  - "B8.2"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-DVM

Distributed Virtual Memory（DVM）是可选机制，用于传递虚拟内存系统维护消息。【B8.1】

## 操作范围

Non-sync 包含 TLB invalidation、Branch predictor invalidation、Physical/Virtual instruction cache invalidation；Sync 用于同步。【B8.1】

这些操作面向只读结构，因此这里使用失效操作而不是清理脏数据。比请求范围更广的失效在功能上允许，但可能影响性能。【B8.1】

支持能力由 DVM_Support 声明。【B8.1】

## 边界

本笔记不把 DVM 等同于普通数据缓存一致性协议；具体消息打包及 Sync 完成顺序需要结合 B8.2–B8.4。

[[CHI-节点角色与能力]] 说明 MN、RN-D 等参与者；[[CHI-接口能力参数]] 记录配置入口。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L13681|B8.1]]；原始 CHI.md 第 13779 行起。
- [[CHI-Source-IHI0050H#原文 L13801|B8.2]]；原始 CHI.md 第 13801 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
