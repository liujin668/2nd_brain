---
type: concept
status: draft
topics:
  - "[[CHI-架构与通信-MOC]]"
aliases:
  - "System Address Map"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B3.1"
  - "B3.2"
  - "B3.3"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-SAM与目标路由

System Address Map（SAM）用于确定请求的 TgtID；Requester 可以是 Request Node，也可以是 Home Node。【B3.1】

## 规则与实现边界

SAM 必须覆盖整个地址空间，但其具体格式和结构属于 IMPLEMENTATION DEFINED。最简单的映射可以将所有请求导向一个固定节点。【B3.1】

NodeID 用于标识通信源和目的地。一个 Port 可具有多个 NodeID，一个 NodeID 只能分配给一个 Port。【B3.2】

不同消息的目标确定规则有差异，DVMOp、PrefetchTgt 和使用预分配信用的请求不能无条件套用普通地址映射。【B3.3】

## 关联

[[CHI-事务标识符]] 区分路由 ID 与事务 ID；[[CHI-DVM]] 是特殊目标选择的相关机制。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L7561|B3.1]]；原始 CHI.md 第 7676 行起。
- [[CHI-Source-IHI0050H#原文 L7681|B3.2]]；原始 CHI.md 第 7689 行起。
- [[CHI-Source-IHI0050H#原文 L7681|B3.3]]；原始 CHI.md 第 7704 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
