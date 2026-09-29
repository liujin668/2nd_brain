---
type: mechanism
status: draft
topics:
  - "[[CHI-一致性-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B4.11"
  - "B5.6"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-Hazard处理

Hazard 规则约束在途请求、Snoop 和数据相互作用时的前向进展，必须分别考察 RN-F 和 HN-F。【B4.11】

## HN-F 的一条核心约束

HN-F 必须收到某 Snoopee 的 Snoop 响应后，才能对该 Snoopee 同一 cache line 发起另一 Snoop。【B4.11.2】

Home 接收部分 Data message 后，必须能够接收剩余包，不能依赖其他请求或响应的前向进展。【B4.11.2】

发送完成后的下一次 Snoop 还受事务对应的数据或确认到达条件限制，不是一个通用固定延迟。【B4.11.2】

## 案例与限制

B5.6 提供 Snoop、Request、Read/Dataless 和 Race hazard 示例。其图形时间线在转换文本中不完整，精确事件顺序标为待确认，暂不重绘。

相关确认机制见 [[CHI-Comp与CompAck]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L11761|B4.11]]；原始 CHI.md 第 11856 行起。
- [[CHI-Source-IHI0050H#原文 L12721|B5.6]]；原始 CHI.md 第 12839 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
