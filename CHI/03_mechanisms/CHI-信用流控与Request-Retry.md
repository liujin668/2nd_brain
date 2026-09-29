---
type: mechanism
status: draft
topics:
  - "[[CHI-流控与链路-MOC]]"
aliases:
  - "Request Retry"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B2.10"
  - "B14.2"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-信用流控与Request-Retry

P-Credit 与 L-Credit 分属协议请求重试和链路传输两类资源管理。【B2.10、B14.2】

| 维度 | P-Credit | L-Credit |
| --- | --- | --- |
| 使用场景 | 请求收到 RetryAck 后重新提交 | 在接口通道发送 Flit |
| 相关信息 | PCrdGrant、PCrdType、AllowRetry | LCRDV 及链路信用计数 |
| 关键约束 | 满足信用分配条件的再次请求保证被接受 | 接收端必须接收已发信用所承诺的 Flit |

## Request Retry

Request Retry 为可选机制，避免 REQ 阻塞；DAT、RSP、SNP 没有对应的 Retry 机制，PrefetchTgt 也不能重试。【B2.10】

PCrdGrant 可能先于 RetryAck 到达，Requester 必须记录信用。获得适用信用后的再次请求通过 AllowRetry=0 表明信用分配。【B2.10】

## L-Credit

传输一个 Flit 消耗一个 L-Credit；收到信用的当周期不能使用该信用。【B14.2.1.1】

[[CHI-Resource-Planes]] 解释流量隔离；[[CHI-案例-L-Credit逐周期]] 给出时序小例。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L7441|B2.10]]；原始 CHI.md 第 7451 行起。
- [[CHI-Source-IHI0050H#原文 L20521|B14.2]]；原始 CHI.md 第 20567 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
