---
type: question
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
  - "[[CHI-一致性-MOC]]"
aliases: [Return to Source]
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections: ["B4.9", "B13.10.34"]
evidence: mixed
verification: md-checked
created: 2026-09-10
updated: 2026-09-10
---

# CHI-RetToSrc的用途与设计原因

## 问题

RetToSrc 字段有什么用途，为什么这样设计？

## 定义与路径

**RetToSrc（Return to Source）表达 snoop 发起方是否请求 Snoopee 向其返回一份数据。** Src 是 snoop 的发送者，通常为 HN，不是原始读请求的 RN。

```text
RN-A ── Read ──→ HN ── Snoop ──→ RN-B
                 ↑                 │
                 └── 返回数据 ─────┘  RetToSrc 相关路径

若使用 DCT：
RN-B ── CompData ──→ RN-A              直接转发路径
RN-B ── 数据副本 ──→ HN                是否另回一份由相关规则决定
```

**它不是“0 一定无数据、1 一定有数据”的通用开关。** 必须结合 snoop opcode、本地 cache 状态以及实际转发行为判断。不给 HN 数据也不意味着不回 snoop 响应。

## 非 forwarding snoop

Issue H B4.9 对非 forwarding snoop（排除 SnpMakeInvalid）规定：

| 本地状态 | RetToSrc=0 | RetToSrc=1 |
| --- | --- | --- |
| SC | 不得返回数据 | 建议返回，但不强制 |
| UC | 可以返回数据 | 可以返回数据 |
| Dirty | 必须返回数据 | 必须返回数据 |
| I / UCE | 无有效数据可返回 | 无有效数据可返回 |

表中还要叠加 opcode 对 RetToSrc 的合法性约束。特别是 **SnpCleanInvalid 的 RetToSrc 必须为 0，但命中脏副本时仍需返回数据**；0 不能取消脏数据处理义务。

## Forwarding snoop

以允许设置该位的 SnpSharedFwd 为例，若 RN-B 持有 SC 且实际向 RN-A 转发：

| 设置 | 给 RN-A | 给 HN |
| --- | --- | --- |
| RetToSrc=0 | 数据 | 仅 snoop 响应，不回数据 |
| RetToSrc=1 | 数据 | 同时返回数据副本 |

对于实际执行数据转发的 forwarding snoop，RetToSrc=1 时 Clean 或 Dirty 数据均必须回 Home 一份；RetToSrc=0 时 Clean 数据不得回 Home。若脏数据无法转发或保留，仍必须返回 Home，不能丢失。

Issue H 中以下 opcode 的 RetToSrc 不适用且必须为 0：SnpCleanShared、SnpCleanInvalid、SnpMakeInvalid、SnpOnceFwd、SnpUniqueFwd、SnpMakeInvalidStash、SnpStashUnique、SnpStashShared、SnpQuery、SnpDVMOp。

## 为什么这样设计：由规则推导的解释

### 避免多个共享者重复回数据

HN 可能需要 snoop 多个 SC 持有者以完成一致性操作，但不需要所有节点都回相同的 64 B 数据。规范要求：对于同一相关 snoop 操作，Home 只能向一个 RN 发出 RetToSrc=1 的 snoop。其他 SC 节点只回状态，从而节省 DAT 带宽。

### 将一致性动作与数据搬运策略分开

Opcode 表达共享、失效、清理、转发等要求；RetToSrc 进一步表达 Home 对数据副本的需求。DCT 可以让请求方直接收到数据，同时允许 Home 在需要时取得副本，例如用于 Home 侧缓存；不需要副本时便省去这一段传输。具体缓存分配策略属于实现选择。

### 正确性不能被性能提示覆盖

SC 通常不承担回写责任；脏数据则必须遵守保全、转移或清理规则。因此 RetToSrc=0 不能简单阻止所有数据返回。该位与 Dirty 责任正交，不能代替状态机规则。

### 为什么non-forwarding可以在RetToSrc时不回数据，而forwarding必回数据

因为non-forwarding不管怎么样，HN总能得到数据，比如SC RN都没回，可以去SN拿；
而forwarding绕过了HN，所以RetToSrc有效必给，是一个严格的的条件。

## 相关笔记与原文依据

- [[CHI-直接数据传输]]、[[CHI-所有权与Dirty责任]]、[[CHI-Cache状态模型]]。
- [[CHI-Source-IHI0050H#原文 L11761|B4.9 Returning Data with Snoop response]]：原始 CHI.md 第 11815 行起。
- [[CHI-Source-IHI0050H]]：B13.10.34 Return to Source 字段定义；各 opcode 的详细状态表另见 B4.8。

依据 Issue H。其他版本在 SC 返回数据的强制程度和字段适用范围上可能不同，应回查对应版本。
