---
type: reference
status: draft
topics:
  - "[[CHI-流控与链路-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B16.1"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-接口能力参数

规范的 interface property 用于声明能力，与本知识库的 YAML Properties 是两回事。【B16.1】

## 常用查阅入口

| 能力 | 规范属性 |
| --- | --- |
| DVM | DVM_Support |
| MTE | MTE_Support |
| DMT/DCT | Direct_Memory_Transfer、Direct_Cache_Transfer |
| 重试 | Retry_Support |
| 多请求 | MultiReq_Support |
| RP | Num_RP_REQ、Num_RP_SNP 及相关 shared credit 属性 |
| 数据宽度与节点 ID | Data_Width、NodeID_Width |

字段名来自 B16.1，精确取值和依赖仍查相应子节。

## 使用规则

解释可选功能前先核对声明，不能由“规范包含”推导为“所有实现支持”。

相关机制：[[CHI-DVM]]、[[CHI-MTE与Tag一致性]]、[[CHI-Multi-request]]、[[CHI-Resource-Planes]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L21601|B16.1]]；原始 CHI.md 第 21609 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
