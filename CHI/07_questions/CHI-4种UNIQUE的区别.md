---
type: question
status: draft
topics:
  - "[[CHI-一致性-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections: ["B4.2.1", "B4.2.2", "B4.1.1"]
evidence: mixed
verification: md-checked
created: 2026-09-16
updated: 2026-09-16
---

# 4种UNIQUE的区别

## 问题

ReadUnique、MakeReadUnique、CleanUnique 和 MakeUnique 有什么区别？

## 回答

**区别在于是否需要旧数据、是否保证补回数据，以及是否承诺覆盖整行。**

| 请求 | 主要作用 | 数据与权限 |
| --- | --- | --- |
| ReadUnique（RU） | 获取数据和独占写权限 | 返回完整缓存行，数据状态为 UC 或 UD |
| MakeReadUnique（MRU） | 在已有 Shared 副本的基础上获取写权限 | 副本未丢失时保留本地数据；若被失效 snoop 移除，则保证返回数据 |
| CleanUnique（CU） | 获取独占写权限，不请求数据 | 完成响应不带数据；其他缓存的 Dirty 副本必须清理写回 |
| MakeUnique（MU） | 准备覆盖整行时获取写权限 | 必须保证写入整行所有字节；其他缓存的旧 Dirty 数据直接失效，无需传回 |

## 关键区别

MRU 避免获取权限期间副本被失效后，需要重新发请求取数据。HN 根据一致性处理决定是否返回数据；Exclusive 变体还需检查专门规则。

CU 不保证补回数据。如果原有副本在请求完成前被失效，完成时可能进入 **UCE：有独占权限，但没有有效数据字节**。

CU 不要求一定覆盖整行，所以必须保存其他节点的旧脏数据；MU 的整行覆盖承诺允许省去旧数据传输。

## 相关笔记与原文依据

- [[CHI-Cache状态模型]]、[[CHI-所有权与Dirty责任]]、[[CHI-Hazard处理]]。
- [[CHI-Source-IHI0050H]]：B4.2.1 ReadUnique、MakeReadUnique；B4.2.2 CleanUnique、MakeUnique；B4.1.1 空缓存行所有权。

依据 Issue H；详细状态及 Exclusive 变体以对应状态表为准。
