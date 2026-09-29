---
type: concept
status: draft
topics:
  - "[[CHI-内存管理与隔离-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B10.1"
  - "B10.2"
  - "B2.7.1"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-RME与PAS

Realm Management Extension（RME）通过硬件隔离支持不同 Security state 下执行环境共享系统资源，是 Arm CCA 的组成部分。【B10.1】

## PAS 的协议意义

Physical Address Space（PAS）参与区分地址空间；同一 cache line 地址但不同 PAS，不能在一致性、可观察性和 Hazard 判断中无条件当成同一位置。【B2.7.1、B10.2】

本文只记录 CHI 接口中的含义，不扩展为完整安全架构说明。

## 关联

[[CHI-GDI]] 是 RME 的扩展；[[CHI-多副本原子性与Ordering]] 使用 PAS 判断同一位置。Issue H 的字段变化见 [[CHI-版本变化]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L15601|B10.1]]；原始 CHI.md 第 15706 行起。
- [[CHI-Source-IHI0050H#原文 L15601|B10.2]]；原始 CHI.md 第 15717 行起。
- [[CHI-Source-IHI0050H#原文 L5521|B2.7.1]]；原始 CHI.md 第 5639 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
