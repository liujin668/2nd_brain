---
type: mechanism
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B2.6"
  - "B2.4.16"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-Multi-request

Multi-request 允许单个请求面向最多 64 条连续 cache line，以减少请求通道带宽开销。【B2.6】

## 不改变一致性粒度

响应仍按 cache line 约束，64-byte 一致性粒度保持不变。中间节点允许将一个 Multi-request 拆成较小请求。【B2.6】

起始地址必须按 cache line 对齐，事务不能跨越 4KB 边界；广播或其他控制还可能施加额外限制。【B2.6】

支持范围取决于 MultiReq_Support，并只适用于本节列出的事务集合，不能推广到所有请求。【B2.6】

CacheLineID 标识响应或数据属于其中哪条 cache line。【B2.4.16】

## 关联

字段背景见 [[CHI-事务标识符]]；引入版本见 [[CHI-版本变化]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L5281|B2.6]]；原始 CHI.md 第 5365 行起。
- [[CHI-Source-IHI0050H#原文 L4321|B2.4.16]]；原始 CHI.md 第 4394 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
