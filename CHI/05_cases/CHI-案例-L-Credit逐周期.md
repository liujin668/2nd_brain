---
type: case
status: draft
topics:
  - "[[CHI-流控与链路-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B14.2.1.1"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-案例-L-Credit逐周期

场景为无 Resource Planes 的通道，发送端初始无信用。本例转述 B14.2.1.1 的文字步骤。

| 周期 | 动作 |
| --- | --- |
| 0 | 发送端没有信用，无事件 |
| 1 | 接收端授予一个信用 |
| 2 | 发送端用该信用发送一次传输 |
| 3 | 接收端授予一个信用 |
| 4 | 接收端再授予一个信用 |
| 5 | 发送端传输，同时接收端授予一个信用 |

## 解释

信用不能在收到的同周期使用。以上只是规范示例，不意味着必须等待这些固定周期才能授信或发送。【B14.2.1.1】

机制见 [[CHI-信用流控与Request-Retry]]；RP 扩展见 [[CHI-Resource-Planes]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L20521|B14.2.1.1]]；原始 CHI.md 第 20574 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
