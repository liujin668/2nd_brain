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
  - "B9.1.1"
  - "B9.2"
  - "B9.3"
evidence: mixed
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-错误分类与传播

CHI 区分 Data Error（DERR）和 Non-data Error（NDERR）。【B9.1.1】

| 类型 | 典型含义 | Home 行为摘要 |
| --- | --- | --- |
| DERR | 访问了正确地址，但数据损坏 | 对原本要求下传的请求，不得因 DERR 停止向 Subordinate 传播 |
| NDERR | 非数据损坏类错误，如非法访问 | 允许但不要求继续下传，必须向 Requester 返回 NDERR |

以上来自 B9.1.1，不是所有错误情形的穷尽列表。

## 不同粒度

RespErr、Poison、DataCheck 和接口 parity 分别涉及不同错误报告或检测粒度；不能只检查一个字段就宣称覆盖全部错误。【B9.1–B9.3】

相关数据与 tag 操作见 [[CHI-MTE与Tag一致性]]。具体编码表暂保留在 Source，避免复制转换损坏的表格。

## 原文依据

- [[CHI-Source-IHI0050H#原文 L14881|B9.1.1]]；原始 CHI.md 第 14907 行起。
- [[CHI-Source-IHI0050H#原文 L15361|B9.2]]；原始 CHI.md 第 15468 行起。
- [[CHI-Source-IHI0050H#原文 L15481|B9.3]]；原始 CHI.md 第 15537 行起。

本笔记依据 Issue H 转述。未覆盖的条件、表格和例外应回查原文；不是完整实现检查表。
