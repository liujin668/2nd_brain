---
type: concept
status: draft
topics:
  - "[[CHI-一致性-MOC]]"
aliases:
  - "缓存一致性状态"
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "B1.1.2"
  - "B1.5"
  - "B4.1"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-Cache状态模型

CHI 以 Valid/Invalid、Unique/Shared、Clean/Dirty、Full/Partial/Empty 等属性描述缓存行，定义七种状态。【B1.5.2、B4.1】

| 状态 | 含义 |
| --- | --- |
| I | Invalid，不持有该缓存行 |
| UC | Unique Clean |
| UCE | Unique Clean Empty，独占但无有效数据字节 |
| UD | Unique Dirty |
| UDP | Unique Dirty Partial，有效字节可以为部分、零或全部 |
| SC | Shared Clean |
| SD | Shared Dirty |

## 容易误读的边界

规范明确支持 MESI 和 MOESI 缓存模型，并提供额外的 Partial 与 Empty 状态。【B1.1.2】本笔记保留 CHI 自身的状态名称，不把七态强行逐项等同于经典模型；若需要完整对应推导，需补充证据，当前待确认。

Shared 表示其他缓存可能有副本，不保证实际存在多个副本。SC 的数据可能与主存不同，但该缓存不承担回写主存责任。【B1.5.2、B4.1】

实现允许只支持状态集合的子集，不能假定每个缓存实现全部七态。【B4.1】

状态中的所有权和字节有效性应分别理解，见 [[CHI-所有权与Dirty责任]]。具体请求不能仅按名字推断终态，见 [[CHI-ReadShared与ReadUnique]]。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L961|B1.1.2]]；原始 CHI.md 的 B1.1.2 Key features。该节跨越后续原文分段，可继续向下阅读。

- [[CHI-Source-IHI0050H#原文 L1441|B1.5]]；原始 CHI.md 第 1444 行起。
- [[CHI-Source-IHI0050H#原文 L7921|B4.1]]；原始 CHI.md 第 7957 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
