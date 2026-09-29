---
type: mechanism
status: draft
topics:
  - "[[CHI-性能与可靠性-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B11.1"
  - "B11.4"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-QoS与MPAM

QoS 与 MPAM 都与资源使用有关，但表达的信息和用途不同。【B11.1、B11.4】

## QoS

规范提供基于优先级以及可使用延迟/吞吐度量的 QoS 描述。相同事务以不同 QoS 再发送时，Completer 必须将其作为多个不同请求处理。【B11.1】

## MPAM

Memory System Resource Partitioning and Monitoring 使用 PartID 和 PerfMonGroup 标识分区与监控组；Home 或 Subordinate 使用这些信息分配资源。【B11.4】

MPAM 字段在 REQ 和 SNP 上适用，其中 SNP 仅 Stash snoop 使用有效 MPAM 值；其他 snoop 使用规定默认值。【B11.4】

## 关联

[[CHI-Cache-Stashing]] 解释相关 Snoop；[[CHI-Resource-Planes]] 解释链路流量独立性。具体仲裁实现不能从这些字段自行推断。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L16321|B11.1]]；原始 CHI.md 第 16417 行起。
- [[CHI-Source-IHI0050H#原文 L16801|B11.4]]；原始 CHI.md 第 16882 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
