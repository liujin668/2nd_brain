---
type: mechanism
status: draft
topics:
  - "[[CHI-内存管理与隔离-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B10.8"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-GDI

Granular Data Isolation（GDI）是 RME 扩展，用于在 RME 系统中隔离非 PE 数据流与 Processing Element。【B10.8】

## MECID 不匹配

对相关 PAS 的 MECID 不匹配处理不得导致不同 Memory Encryption Context 之间的数据机密性丢失；规范允许该处理导致系统一致性丢失。【B10.8.1】

读、部分写、全写以及 Snoop 的处理规则不同，不能把一种处理规则套用到全部消息。【B10.8.1.1–B10.8.1.2】

## 范围

是否适用需要检查 PAS 和相关支持属性。本笔记只概括约束，不代替完整实现规则。

背景见 [[CHI-RME与PAS]]，功能引入见 [[CHI-版本变化]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L16201|B10.8]]；原始 CHI.md 第 16268 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
