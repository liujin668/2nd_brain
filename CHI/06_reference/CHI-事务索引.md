---
type: reference
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections:
  - "C4"
evidence: paraphrase
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-事务索引

C4 共有 68 项事务摘要。本表保留完整原文入口；未单独整理的事务直接回到 Source，不创建空壳 Note。

| 编号 | 事务 | 原文入口 |
| --- | --- | --- |
| C4.1 | AtomicCompare | [[CHI-Source-IHI0050H#原文 L24361|原文 L24361]] |
| C4.2 | AtomicLoad | [[CHI-Source-IHI0050H#原文 L24361|原文 L24396]] |
| C4.3 | AtomicStore | [[CHI-Source-IHI0050H#原文 L24361|原文 L24428]] |
| C4.4 | AtomicSwap | [[CHI-Source-IHI0050H#原文 L24361|原文 L24461]] |
| C4.5 | CleanInvalid | [[CHI-Source-IHI0050H#原文 L24481|原文 L24493]] |
| C4.6 | CleanInvalidPoPA | [[CHI-Source-IHI0050H#原文 L24481|原文 L24518]] |
| C4.7 | CleanInvalidStorage | [[CHI-Source-IHI0050H#原文 L24481|原文 L24545]] |
| C4.8 | CleanShared | [[CHI-Source-IHI0050H#原文 L24481|原文 L24570]] |
| C4.9 | CleanSharedPersist | [[CHI-Source-IHI0050H#原文 L24481|原文 L24595]] |
| C4.10 | CleanSharedPersistSep | [[CHI-Source-IHI0050H#原文 L24601|原文 L24620]] |
| C4.11 | CleanUnique | [[CHI-Source-IHI0050H#原文 L24601|原文 L24650]] |
| C4.12 | DVMOp | [[CHI-Source-IHI0050H#原文 L24601|原文 L24676]] |
| C4.13 | Evict | [[CHI-Source-IHI0050H#原文 L24601|原文 L24700]] |
| C4.14 | MakeInvalid | [[CHI-Source-IHI0050H#原文 L24721|原文 L24722]] |
| C4.15 | MakeReadUnique | [[CHI-Source-IHI0050H#原文 L24721|原文 L24747]] |
| C4.16 | MakeUnique | [[CHI-Source-IHI0050H#原文 L24721|原文 L24773]] |
| C4.17 | PCrdReturn | [[CHI-Source-IHI0050H#原文 L24721|原文 L24798]] |
| C4.18 | PrefetchTgt | [[CHI-Source-IHI0050H#原文 L24721|原文 L24821]] |
| C4.19 | ReadClean | [[CHI-Source-IHI0050H#原文 L24841|原文 L24855]] |
| C4.20 | ReadNoSnp | [[CHI-Source-IHI0050H#原文 L24841|原文 L24879]] |
| C4.21 | ReadNoSnpSep | [[CHI-Source-IHI0050H#原文 L24841|原文 L24902]] |
| C4.22 | ReadNotSharedDirty | [[CHI-Source-IHI0050H#原文 L24841|原文 L24926]] |
| C4.23 | ReadOnce | [[CHI-Source-IHI0050H#原文 L24841|原文 L24951]] |
| C4.24 | ReadOnceCleanInvalid | [[CHI-Source-IHI0050H#原文 L24961|原文 L24973]] |
| C4.25 | ReadOnceMakeInvalid | [[CHI-Source-IHI0050H#原文 L24961|原文 L24997]] |
| C4.26 | ReadPreferUnique | [[CHI-Source-IHI0050H#原文 L24961|原文 L25022]] |
| C4.27 | ReadShared | [[CHI-Source-IHI0050H#原文 L24961|原文 L25050]] |
| C4.28 | ReadUnique | [[CHI-Source-IHI0050H#原文 L24961|原文 L25076]] |
| C4.29 | ReqLCrdReturn | [[CHI-Source-IHI0050H#原文 L25081|原文 L25099]] |
| C4.30 | StashOnceSepShared | [[CHI-Source-IHI0050H#原文 L25081|原文 L25120]] |
| C4.31 | StashOnceSepUnique | [[CHI-Source-IHI0050H#原文 L25081|原文 L25148]] |
| C4.32 | StashOnceShared | [[CHI-Source-IHI0050H#原文 L25081|原文 L25178]] |
| C4.33 | StashOnceUnique | [[CHI-Source-IHI0050H#原文 L25201|原文 L25206]] |
| C4.34 | WriteBackFull | [[CHI-Source-IHI0050H#原文 L25201|原文 L25235]] |
| C4.35 | WriteBackFullCleanInv | [[CHI-Source-IHI0050H#原文 L25201|原文 L25258]] |
| C4.36 | WriteBackFullCleanInvPoPA | [[CHI-Source-IHI0050H#原文 L25201|原文 L25285]] |
| C4.37 | WriteBackFullCleanInvStrg | [[CHI-Source-IHI0050H#原文 L25201|原文 L25312]] |
| C4.38 | WriteBackFullCleanSh | [[CHI-Source-IHI0050H#原文 L25321|原文 L25339]] |
| C4.39 | WriteBackFullCleanShPerSep | [[CHI-Source-IHI0050H#原文 L25321|原文 L25366]] |
| C4.40 | WriteBackPtl | [[CHI-Source-IHI0050H#原文 L25321|原文 L25393]] |
| C4.41 | WriteCleanFull | [[CHI-Source-IHI0050H#原文 L25321|原文 L25416]] |
| C4.42 | WriteCleanFullCleanSh | [[CHI-Source-IHI0050H#原文 L25321|原文 L25439]] |
| C4.43 | WriteCleanFullCleanShPerSep | [[CHI-Source-IHI0050H#原文 L25441|原文 L25466]] |
| C4.44 | WriteEvictFull | [[CHI-Source-IHI0050H#原文 L25441|原文 L25493]] |
| C4.45 | WriteEvictOrEvict | [[CHI-Source-IHI0050H#原文 L25441|原文 L25517]] |
| C4.46 | WriteNoSnpDef | [[CHI-Source-IHI0050H#原文 L25441|原文 L25543]] |
| C4.47 | WriteNoSnpFull | [[CHI-Source-IHI0050H#原文 L25561|原文 L25568]] |
| C4.48 | WriteNoSnpFullCleanInv | [[CHI-Source-IHI0050H#原文 L25561|原文 L25591]] |
| C4.49 | WriteNoSnpFullCleanInvPoPA | [[CHI-Source-IHI0050H#原文 L25561|原文 L25617]] |
| C4.50 | WriteNoSnpFullCleanInvStrg | [[CHI-Source-IHI0050H#原文 L25561|原文 L25643]] |
| C4.51 | WriteNoSnpFullCleanSh | [[CHI-Source-IHI0050H#原文 L25561|原文 L25669]] |
| C4.52 | WriteNoSnpFullCleanShPerSep | [[CHI-Source-IHI0050H#原文 L25681|原文 L25695]] |
| C4.53 | WriteNoSnpPtl | [[CHI-Source-IHI0050H#原文 L25681|原文 L25721]] |
| C4.54 | WriteNoSnpPtlCleanInv | [[CHI-Source-IHI0050H#原文 L25681|原文 L25745]] |
| C4.55 | WriteNoSnpPtlCleanInvPoPA | [[CHI-Source-IHI0050H#原文 L25681|原文 L25771]] |
| C4.56 | WriteNoSnpPtlCleanSh | [[CHI-Source-IHI0050H#原文 L25681|原文 L25797]] |
| C4.57 | WriteNoSnpPtlCleanShPerSep | [[CHI-Source-IHI0050H#原文 L25801|原文 L25823]] |
| C4.58 | WriteNoSnpZero | [[CHI-Source-IHI0050H#原文 L25801|原文 L25849]] |
| C4.59 | WriteUniqueFull | [[CHI-Source-IHI0050H#原文 L25801|原文 L25872]] |
| C4.60 | WriteUniqueFullCleanInvStrg | [[CHI-Source-IHI0050H#原文 L25801|原文 L25895]] |
| C4.61 | WriteUniqueFullCleanSh | [[CHI-Source-IHI0050H#原文 L25921|原文 L25922]] |
| C4.62 | WriteUniqueFullCleanShPerSep | [[CHI-Source-IHI0050H#原文 L25921|原文 L25949]] |
| C4.63 | WriteUniqueFullStash | [[CHI-Source-IHI0050H#原文 L25921|原文 L25976]] |
| C4.64 | WriteUniquePtl | [[CHI-Source-IHI0050H#原文 L25921|原文 L26000]] |
| C4.65 | WriteUniquePtlCleanSh | [[CHI-Source-IHI0050H#原文 L25921|原文 L26024]] |
| C4.66 | WriteUniquePtlCleanShPerSep | [[CHI-Source-IHI0050H#原文 L26041|原文 L26051]] |
| C4.67 | WriteUniquePtlStash | [[CHI-Source-IHI0050H#原文 L26041|原文 L26078]] |
| C4.68 | WriteUniqueZero | [[CHI-Source-IHI0050H#原文 L26041|原文 L26103]] |

## 已整理的事务与机制

- [[CHI-ReadShared与ReadUnique]]
- [[CHI-Atomic事务族]]
- [[CHI-Cache-Stashing]]
- [[CHI-DVM]]

## 查阅顺序

从 C4 摘要查找 B2 的事务结构、B4 的语义和状态、C1 的字段映射以及 C3 的节点事务子集。不要仅用摘要代替完整规则。
