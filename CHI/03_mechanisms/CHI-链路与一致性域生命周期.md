---
type: mechanism
status: draft
topics:
  - "[[CHI-流控与链路-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B14.5"
  - "B15.1"
  - "B15.2"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-链路与一致性域生命周期

链路激活/停用与加入/退出系统一致性域是不同控制机制，应分开判断状态。【B14.5、B15】

## 一致性域握手

Request Node 使用 SYSCOREQ 请求加入或退出，互连用 SYSCOACK 确认。SYSCOREQ 仅能在两者逻辑值相同时改变，SYSCOACK 仅能在两者逻辑值不同时改变。【B15.2】

Request Node 拉高 SYSCOREQ 时必须能服务 Snoop；在采样 SYSCOACK 为高之前，不能发出允许缓存 coherent location 的事务。【B15.2.1】

退出前需完成规定的缓存相关事务，完整条件以 B15.2.1 为准，不能简化成“没有新请求即可关机”。

## 关联

[[CHI-信用流控与Request-Retry]] 解释链路发送资源；[[CHI-节点角色与能力]] 说明 RN-F/RN-D。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L20641|B14.5]]；原始 CHI.md 第 20753 行起。
- [[CHI-Source-IHI0050H#原文 L21361|B15.1]]；原始 CHI.md 第 21464 行起。
- [[CHI-Source-IHI0050H#原文 L21481|B15.2]]；原始 CHI.md 第 21481 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
