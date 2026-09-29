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
  - "B1.6"
  - "C3.1"
  - "C3.2"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-节点角色与能力

节点类型决定协议职责和允许使用的事务子集。【B1.6、C3】

| 类型 | 核心职责 |
| --- | --- |
| RN-F | 带硬件一致性缓存的 Request Node，支持 Snoop |
| RN-D | 无硬件一致性缓存，支持 DVM 的 IO coherent Request Node |
| RN-I | 无硬件一致性缓存，不接收 DVM 的 IO coherent Request Node |
| HN-F | 协调一致性，包含 PoC，预期承担 PoS |
| HN-I | 处理有限的非一致性请求子集，不包含 PoC |
| MN | 处理 DVM 事务 |
| SN-F、SN-I | 接收来自 Home 的请求并完成；具体事务能力见 C3.2 |

以上概括来自 B1.6；不是完整合法性矩阵。

## 边界

HN-F 可以包含目录或 Snoop filter，也可以集成互连缓存；不能把这些都写成必备结构。【B1.6】

[[CHI-PoC与PoS]] 解释协调点；[[CHI-DVM]] 解释 MN 参与的维护流程。精确事务限制仍需查 C2、C3。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L1441|B1.6]]；原始 CHI.md 第 1520 行起。
- [[CHI-Source-IHI0050H#原文 L24121|C3.1]]；原始 CHI.md 第 24155 行起。
- [[CHI-Source-IHI0050H#原文 L24241|C3.2]]；原始 CHI.md 第 24255 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
