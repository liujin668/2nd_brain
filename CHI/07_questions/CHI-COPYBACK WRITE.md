---
type: question
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections: ["B2.3.2.3", "B2.8.8", "B4.2.3.2", "B4.7.3"]
evidence: mixed
verification: md-checked
created: 2026-09-16
updated: 2026-09-16
---

# COPYBACK WRITE

## 问题

WriteBack、WriteClean 和 WriteEvictOrEvict 有什么区别？HN 如何决定是否接收数据？

## 回答

| 请求                           | 主要作用                      | Requester 的副本                 |
| ---------------------------- | ------------------------- | ----------------------------- |
| WriteBackFull / WriteBackPtl | 将脏数据写回下一级缓存或内存            | 最终失效                          |
| WriteCleanFull               | 写回完整脏数据                   | 通常保留 Clean 副本；并发 snoop 可能使其失效 |
| WriteEvictOrEvict            | 驱逐 Clean 副本，由 HN 决定是否接收数据 | 最终失效                          |

## WriteEvictOrEvict 的两条路径

**HN 通过响应 Opcode 决定是否要数据。**

| HN 响应        | RN 的动作                    | 是否单独发送 CompAck |
| ------------ | ------------------------- | -------------- |
| Comp         | 不发送数据，回复 CompAck          | 必须发送           |
| CompDBIDResp | 收到响应后发送 CopyBackWriteData | 不另发 CompAck    |

无数据分支的 CompAck 必须在收到 Comp 后发送，不受原请求 ExpCompAck 值影响。有数据分支必须等到 CompDBIDResp 后才能发送数据。

即使 CAH=0，WriteEvictOrEvict 也允许 HN 选择不接收数据。具体缓存分配与保留策略属于实现。

## 状态与并发限制

等待响应期间可能收到 snoop，因此 CopyBackWriteData 或 CompAck 必须反映协议允许的状态变化，不能固定假设始终是 UC。

Clean 副本不承担保存脏数据的责任，但 SC 不意味着 DDR 一定最新；系统中可能有其他节点承担 Dirty 责任。

## 相关笔记与原文依据

- [[CHI-所有权与Dirty责任]]、[[CHI-Comp与CompAck]]、[[CHI-Hazard处理]]。
- [[CHI-Source-IHI0050H]]：B2.3.2.3 CopyBack Write 流程；B2.8.8 CAH 规则；B4.2.3.2 请求定义；B4.7.3 状态转换。

依据 Issue H；简表概括主要用途，消息与状态细节以原文为准。
