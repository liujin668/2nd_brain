---
type: mechanism
status: draft
topics:
  - "[[CHI-顺序与完成-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B2.7.2"
  - "B2.7.3"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-Comp与CompAck

完成响应与完成确认是不同协议动作。CompAck 用来约束 Requester 事务与其他请求引发的后续 Snoop 之间的相对顺序。【B2.7.3】

## 关键规则

对 B2.7.3 规定的读事务，HN-F 等待 CompAck 后才向同一地址发送后续 Snoop；ReadNoSnp 和 ReadOnce* 有例外。CopyBack 中 WriteData 可以起隐式 CompAck 的作用。【B2.7.3】

是否使用 CompAck 要结合节点类型、事务和 ExpCompAck 规则判断。不能给所有事务统一加上 CompAck。【B2.7.3】

Comp 的可观察性含义依事务而异；取消写的 Comp 仅表示事务环路完成，不能据此宣称其一致性动作完成。【B2.7.2】

## 关联

[[CHI-ReadShared与ReadUnique]] 是阅读入口；[[CHI-Hazard处理]] 解释并发约束。完整发送时点和例外仍以本节原文为准。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L5641|B2.7.2]]；原始 CHI.md 第 5648 行起。
- [[CHI-Source-IHI0050H#原文 L5641|B2.7.3]]；原始 CHI.md 第 5756 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
