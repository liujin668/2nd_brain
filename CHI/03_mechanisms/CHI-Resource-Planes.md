---
type: mechanism
status: draft
topics:
  - "[[CHI-流控与链路-MOC]]"
aliases:
  - "Resource Planes"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B14.2.1.2"
  - "B2.10"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-Resource-Planes

Resource Planes（RP）可用于 REQ 和 SNP 通道，使共享链路上的不同流量具有独立前进能力。【B14.2.1.2】

## 机制

每个 RP 有专用信用，也可以配置共享信用以提高缓冲利用率；一个 RP 缺少信用时，不应阻塞其他 RP 的流量。【B14.2.1.2】

同一链路每周期只允许一个 RP 传输 Flit；不同 RP 的信用允许同周期发放。不能把 RP 理解为自动增加物理传输宽度。【B14.2.1.2】

## 与重试的关系

Request Retry 与 RP 正交，可以独立使用或组合使用。【B2.10】

[[CHI-信用流控与Request-Retry]] 给出信用层次；实现配置应查 [[CHI-接口能力参数]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L20521|B14.2.1.2]]；原始 CHI.md 第 20613 行起。
- [[CHI-Source-IHI0050H#原文 L7441|B2.10]]；原始 CHI.md 第 7451 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
