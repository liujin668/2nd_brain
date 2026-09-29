---
type: concept
status: draft
topics:
  - "[[CHI-一致性-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B1.5"
  - "B4.1"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-所有权与Dirty责任

唯一所有权、有效数据和回写责任是不同维度。【B1.5.2、B4.1】

## 所有权不等于已持有数据

UCE 可以持有唯一所有权而没有有效数据；UDP 也允许没有有效字节。获得空行所有权可以服务于随后写入，而不必先获取完整旧数据。【B4.1.1】

## Dirty 责任

UD、SD 的逐出需要向下一级缓存或内存回写；UDP 逐出还涉及与下级数据合并以恢复完整有效行。【B4.1】

主存不必始终保持最新副本，规范要求在不再由任何缓存持有该位置副本之前更新主存。【B1.5.1】

## 关联

状态总表见 [[CHI-Cache状态模型]]；数据获取路径见 [[CHI-直接数据传输]]。不要将 Clean 一概改写为“必然与主存一致”。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L1441|B1.5]]；原始 CHI.md 第 1444 行起。
- [[CHI-Source-IHI0050H#原文 L7921|B4.1]]；原始 CHI.md 第 7957 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
