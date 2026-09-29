---
type: question
status: draft
topics:
  - "[[CHI-一致性-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections: ["B4.2.2.1", "B4.7.2"]
evidence: mixed
verification: md-checked
created: 2026-09-16
updated: 2026-09-16
---

# CLEANSHARED&CLEANINVALID

## 问题

CleanShared 与 CleanInvalid 分别做什么？Requester 自身需要处于什么状态？

## 回答

**两者都保存脏数据；CleanShared 允许保留 Clean 副本，CleanInvalid 要求移除适用范围内的缓存副本。**

| 请求 | 维护结果 | Requester 发出独立请求时的状态 |
| --- | --- | --- |
| CleanShared | 将适用范围内的副本变为非 Dirty，并完成脏数据写回 | I、SC 或 UC |
| CleanInvalid | 完成脏数据写回，并使适用范围内的副本失效 | I |

适用范围由内存属性和系统配置决定。CleanShared 不意味着所有副本必须变成 SC。

## CleanShared 的用途

让缓存中的修改对需要观察下游数据的设备可见，同时允许缓存保留 Clean 副本。例如，与非一致性 DMA 交接由 CPU 写入、设备读取的数据。

这是对维护语义的应用解释，不是完整 DMA 软件操作序列；维护目标和同步步骤需结合平台确认。

![[Pasted image 20260916181648.png]]

## CleanInvalid 的用途

保存已有修改，并清除旧缓存副本。例如，在平台规定的缓存关闭或缓存使用方式切换流程中，作为必要的维护步骤。

**Requester 发出 CHI CleanInvalid 时必须已经为 I，不代表软件维护操作开始前就没有数据。** 原有本地脏数据和失效需要由相应流程处理。

![[Pasted image 20260916181700.png]]

## 相关笔记与原文依据

- [[CHI-PoC与PoS]]、[[CHI-Cache状态模型]]、[[CHI-所有权与Dirty责任]]。
- [[CHI-Source-IHI0050H]]：B4.2.2.1 Cache Maintenance transactions 的完成保证与适用范围；B4.7.2 Requester 状态要求。

依据 Issue H。具体软件指令映射、DMA 同步与平台维护流程待确认。
