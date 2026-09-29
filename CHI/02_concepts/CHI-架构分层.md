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
  - "B1.1.3"
  - "B1.3"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-架构分层

CHI 将通信职责分为 Protocol、Network、Link 三层。

## 三层职责

| 层 | 通信粒度 | 主要职责 |
| --- | --- | --- |
| Protocol | Transaction | 生成与处理请求响应，定义状态转移和事务流，管理协议级流控 |
| Network | Packet | 为消息分包并确定源和目标节点标识 |
| Link | Flit | 相邻网络设备间流控及通道管理 |

以上来自 B1.1.3。理解粒度差异见 [[CHI-通信粒度]]，具体通道见 [[CHI-通道与方向]]。

## 使用边界

分层是职责划分，不能把协议级重试等同于链路发送许可；参见 [[CHI-信用流控与Request-Retry]]。这是基于两层职责的对照解释。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L1081|B1.1.3]]；原始 CHI.md 第 1116 行起。
- [[CHI-Source-IHI0050H#原文 L1081|B1.3]]；原始 CHI.md 第 1178 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
