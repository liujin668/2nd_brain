---
type: concept
status: draft
topics:
  - "[[CHI-架构与通信-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B1.3"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-通信粒度

Transaction 执行一次操作；Message 是协议层交换单位；Packet 是端点之间的传输单位；Flit 是最小流控单位；Phit 是相邻设备间一次物理传输单位。【B1.3】

## 不同粒度的关系

一个 Message 可以包含多个 Packet。一般术语定义允许一个 Packet 包含多个 Flit，但本规范明确说明：CHI 的一个 Packet 由一个 Flit 构成，一个 Flit 由一个 Phit 构成。【B1.3】

不要将一般网络术语中的可能关系直接当作本规范的实际配置。

## 关联

层次职责见 [[CHI-架构分层]]；链路传输许可见 [[CHI-信用流控与Request-Retry]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L1081|B1.3]]；原始 CHI.md 第 1178 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
