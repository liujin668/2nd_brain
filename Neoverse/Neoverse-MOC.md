---
type: moc
status: reviewed
topics: [Neoverse, N2, CPU, architecture]
aliases: ["Neoverse知识地图", "Neoverse目录"]
tags: [arm, neoverse, moc]
sources: ["[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]"]
source_document: "102099_0003_06_en"
source_revision: "r0p3 / Issue 06"
source_date: 2022-10-27
spec_issue: "CHI E"
source_sections: ["1-22", "A", "B", "C", "D", "E"]
evidence: mixed
verification: source-text-and-figure-index-checked
created: 2026-10-10
updated: 2026-10-10
---

# Neoverse 知识地图

从 CPU 核到完整平台分两层阅读：核的实现机制看 [[N2-Core-TRM-完整中文精读]]，参考设计的系统组织看 [[RD-N2-Reference-Design-中文精读]]。核固定参数、构建选项、运行配置与平台集成条件要分别理解。

## N2核：完整中文精读

[[N2-Core-TRM-完整中文精读]] 覆盖 Core TRM r0p3 / Issue 06 的 22 章和附录 A-E。每章注明原页范围，重要图表直接嵌入，更多原位图与续表放在回查册。

| 阅读目标 | 入口 |
|---|---|
| 先了解核的能力、配置、组件与执行模型 | [[N2-Core-TRM-完整中文精读#第2章 N2核的能力与配置]]、[[N2-Core-TRM-完整中文精读#第3章 技术总览与核心组件]] |
| 时钟、复位、WFI/WFE、掉电和retention | [[N2-Core-TRM-完整中文精读#第4章 时钟与复位]]、[[N2-Core-TRM-完整中文精读#第5章 电源管理]] |
| 地址转换、TLB与两阶段翻译 | [[N2-Core-TRM-完整中文精读#第6章 内存管理与地址转换]] |
| MOP cache、L1/L2、预取与一致性接口 | [[N2-Core-TRM-完整中文精读#第7章 L1指令存储系统与MOP cache]] 至 [[N2-Core-TRM-完整中文精读#第10章 内部RAM直接访问]] |
| ECC、错误上报、中断与调试 | [[N2-Core-TRM-完整中文精读#第11章 RAS与错误处理]]、[[N2-Core-TRM-完整中文精读#第12章 GIC CPU接口]]、[[N2-Core-TRM-完整中文精读#第17章 调试系统]] |
| SIMD、SVE/SVE2、系统控制与随机数 | [[N2-Core-TRM-完整中文精读#第13章 Advanced SIMD与浮点]] 至 [[N2-Core-TRM-完整中文精读#第16章 随机数指令与外部RNG]] |
| PMU计数、ETE追踪、TRBE、AMU与SPE | [[N2-Core-TRM-完整中文精读#第18章 PMU性能监测]] 至 [[N2-Core-TRM-完整中文精读#第22章 SPE统计采样]] |
| 精确寄存器、边界行为和版本差异 | [[N2-Core-TRM-完整中文精读#附录A AArch32寄存器]] 至 [[N2-Core-TRM-完整中文精读#附录E 文档版本变化]] |
| 根据当前问题选择阅读顺序 | [[N2-Core-TRM-完整中文精读#综合理解与学习路线]] |
| 原文疑点、适用范围和维护约定 | [[N2-Core-TRM-完整中文精读#待确认事项与使用边界]] |

## 精确回查

- [[N2-Core-TRM-寄存器索引]]：按 30 个功能分组检索，包含 548 个展开条目及总表名称入口。
- [[N2-Core-TRM-正文原图表]]：第1-22章的编号图表和续页。
- [[N2-Core-TRM-附录A原图表]]：AArch32 寄存器。
- [[N2-Core-TRM-附录B原图表]]：AArch64 系统、调试、性能与追踪寄存器。
- [[N2-Core-TRM-附录C原图表]]：外部调试/监测组件及相对偏移。
- [[N2-Core-TRM-附录DE原图表]]：UNPREDICTABLE 行为、调试边界和文档变化。
- [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]：原 PDF 的本库副本，完整普通说明页和访问伪代码以此为准。

## 与CHI知识库的连接

N2 第8/9章解释缓存体系和 CHI 接口实现；事务和协议规则继续从 [[CHI-节点角色与能力]]、[[CHI-通道与方向]]、[[CHI-Cache状态模型]]、[[CHI-信用流控与Request-Retry]] 阅读。TRM 的实现参数不能取代 CHI 规范中的完整事务条件。

## 维护约定

原 PDF 放在 `00_sources`，原图截图放在 `01_assets/N2-Core-TRM-r0p3`。中文精读解释机制，索引帮助查名字，原图表册保留精确字段。新资料先记录版本和来源；遇到与本版不一致的内容，在相应章节标记差异或“待确认”。

尽量向现有主题章补充内容；只有能独立解释且会被反复引用的主题才另建 Note，避免重复摘录同一组寄存器位域。
