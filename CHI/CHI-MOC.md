---
type: moc
status: draft
topics:
  - "[[CHI-架构与通信-MOC]]"
aliases:
  - "CHI 知识地图"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections: []
evidence: derived
verification: md-checked
created: 2026-09-09
updated: 2026-09-10
---

# CHI-MOC

以 **Arm IHI0050 Issue H** 为依据的 CHI 学习与查阅入口。中文笔记是有来源的解释层，完整规则仍以原规范为准。

## 文档依据

- [[CHI-Source-IHI0050H]]：保守清洗后的完整来源文本，含原始行号。
- [[CHI/00_spec/CHI.md|CHI 原文件]]：保留不修改。
- [[CHI-版本变化]]：版本敏感内容。
- [[CHI-转换文本疑点]]：待确认事项。

## 建议学习路径

1. [[CHI-架构分层]] → [[CHI-通信粒度]]。
2. [[CHI-节点角色与能力]] → [[CHI-通道与方向]]。
3. [[CHI-Cache状态模型]] → [[CHI-所有权与Dirty责任]]。
4. [[CHI-ReadShared与ReadUnique]] → [[CHI-直接数据传输]]。
5. [[CHI-多副本原子性与Ordering]] → [[CHI-Comp与CompAck]]。
6. [[CHI-信用流控与Request-Retry]] → [[CHI-Resource-Planes]]。

这是编辑建议的学习顺序，不是原文规定。

## 核心主题

- [[CHI-架构与通信-MOC]]
- [[CHI-一致性-MOC]]
- [[CHI-事务与数据路径-MOC]]
- [[CHI-顺序与完成-MOC]]
- [[CHI-流控与链路-MOC]]
- [[CHI-内存管理与隔离-MOC]]
- [[CHI-性能与可靠性-MOC]]

## 理论与方法入口

- 分层模型：[[CHI-架构分层]]。
- 缓存一致性模型：[[CHI-Cache状态模型]]、[[CHI-PoC与PoS]]。
- 顺序模型：[[CHI-多副本原子性与Ordering]]。
- 资源管理方法：[[CHI-信用流控与Request-Retry]]、[[CHI-Resource-Planes]]。
- 数据放置与路径方法：[[CHI-直接数据传输]]、[[CHI-Cache-Stashing]]。
- 独占访问方法：[[CHI-Exclusive访问与Monitor]]。

上述模型和方法已由概念或机制笔记承载，不另建重复的“理论版”笔记。本文未提供值得独立整理的人物材料，因此不建立人物 Note；Arm 作为发布机构记在 Source 中。

## 按问题查阅

- ReturnNID、HomeNID 等 ID 如何理解和记忆？→ [[CHI-如何理解和记忆各种ID]]。

- 256-bit DAT 接口何时只传一拍？→ [[CHI-256bit数据接口何时只传一拍]]。
- RetToSrc 控制什么，为什么需要它？→ [[CHI-RetToSrc的用途与设计原因]]。
- Shared 一定有多个副本吗？→ [[CHI-Cache状态模型]]。
- 没有有效数据还能持有所有权吗？→ [[CHI-所有权与Dirty责任]]。
- 读数据是否必须经过 Home？→ [[CHI-直接数据传输]]。
- 为什么 PCrdGrant 可能先到？→ [[CHI-信用流控与Request-Retry]]。
- 多行请求改变一致性粒度吗？→ [[CHI-Multi-request]]。
- 收到完成响应就能发送下一次 Snoop 吗？→ [[CHI-Comp与CompAck]]、[[CHI-Hazard处理]]。

## 案例与查询

- [[CHI-案例-读数据来源与直接传输]]
- [[CHI-案例-L-Credit逐周期]]
- [[CHI-事务索引]]：C4 全部 68 项摘要入口。
- [[CHI-接口能力参数]]
- [[CHI-知识库维护约定]]

