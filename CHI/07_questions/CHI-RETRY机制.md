---
type: question
status: draft
topics:
  - "[[CHI-流控与链路-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections: ["B2.10"]
evidence: mixed
verification: md-checked
created: 2026-09-16
updated: 2026-09-16
---

# RETRY机制

## 问题

CHI Request Retry 如何工作？响应顺序、信用匹配及取消请求有什么要求？

## 回答

**Completer 暂时无法接收可重试请求时，通过 RetryAck 拒收，并通过 Protocol Credit 保证后续重发被接收。**

## 基本流程

1. Requester 首次发送请求，AllowRetry=1。
2. Completer 返回 RetryAck，通过 PCrdType 指明重发所需的信用类型。
3. Completer 通过 PCrdGrant 发放对应信用。
4. Requester 同时具备 RetryAck 和匹配信用后，重发请求，设置 AllowRetry=0，并携带对应 PCrdType。
5. 使用有效匹配信用的重发必须被接受，不能再次收到 RetryAck。

## 信用匹配与响应顺序

- PCrdGrant 可以先于 RetryAck 到达，Requester 必须保存并正确匹配信用，不能假定固定顺序。
- 信用匹配需考虑提供信用的 Completer 及 PCrdType，不能只比较类型数值。
- 信用不绑定原始 TxnID，可在符合条件的待重试请求中选择，但仍需遵守事务顺序和 Resource Plane 等约束。

## 不再需要请求时

若请求允许取消且不再需要重发，应及时通过 PCrdReturn 归还未使用信用。尚未取得信用时不能凭空归还。

例如 CopyBack Write 在等待期间被 snoop 失效，应按对应的取消或无有效数据返回规则处理，不能认定所有请求都可随意取消。

## 适用范围

Request Retry 用于 REQ 请求，不适用于 DAT、RSP 或 SNP 消息。DataPull 隐含在 snoop 响应中，不能使用此重试机制；PrefetchTgt 也不适用。

## 相关笔记与原文依据

- [[CHI-信用流控与Request-Retry]]：机制详解。
- [[CHI-Resource-Planes]]、[[CHI-Hazard处理]]、[[CHI-Cache-Stashing]]。
- [[CHI-Source-IHI0050H]]：B2.10 Request Retry，涵盖 RetryAck、PCrdGrant、重发和信用归还规则。

依据 Issue H。本页保留速记定位，完整条件回查 B2.10，避免与机制笔记重复维护。
