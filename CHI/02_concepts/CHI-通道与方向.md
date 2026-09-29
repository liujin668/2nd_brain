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
  - "B2.1"
  - "B13.4"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-通道与方向

CHI 使用 REQ、RSP、SNP、DAT 类通道承载请求、响应、Snoop 请求和数据。【B2.1、B13.4】

## 方向以接口为参照

B2.1 在 Request Node 侧使用 TXREQ、TXDAT、TXRSP、RXRSP、RXDAT、RXSNP 等命名。TX/RX 不是全系统固定方向，必须说明观察的是哪个接口。

WDAT、RDAT、SRSP、CRSP 是事务描述中的简写，不应再推导为四种新增的独立协议通道类型。【B2.1】

## 使用方式

阅读事务时同时记录消息名、所在通道、发送者和接收者。节点职责见 [[CHI-节点角色与能力]]；报文关联见 [[CHI-事务标识符]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L1561|B2.1]]；原始 CHI.md 第 1655 行起。
- [[CHI-Source-IHI0050H#原文 L17881|B13.4]]；原始 CHI.md 第 17959 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
