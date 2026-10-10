---
type: guide
status: reviewed
topics: [Neoverse, N2, CPU, MMU, Cache, CHI, RAS, Debug, PMU, SPE]
aliases: ["Neoverse N2 Core TRM中文精读", "N2核技术参考手册中文导读"]
tags: [arm, neoverse, cpu, architecture, reference]
sources: ["[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]"]
source_document: "102099_0003_06_en"
source_revision: "r0p3 / Issue 06"
source_date: 2022-10-27
spec_issue: "CHI E"
source_sections: ["1-22", "A", "B", "C", "D", "E"]
evidence: mixed
verification: consolidated-content-and-links-checked
created: 2026-10-09
updated: 2026-10-10
---

# Neoverse N2 Core TRM 完整中文精读

N2 是一个实现 Armv9.0-A 的 CPU 核：前端准备指令，乱序执行单元组织计算，MMU 与缓存共同完成访存；通过 Direct connect DSU-110 接入系统，由电源、RAS、中断、调试和性能监测机制保证可管理、可观察。理解它时，要同时区分**架构行为、N2 实现细节和整个 SoC 的集成配置**。

本文覆盖原手册 **22 章及附录 A-E，共 1668 页**。正文按章解释职责、机制、配置条件和重要限制；寄存器附录按功能解读，文末提供本手册逐项寄存器索引与完整原图表回查入口，不把重复的访问伪代码逐页翻译。需要精确编程时，仍需核对原位域、复位值和访问条件。

原文：[本库 PDF](00_sources/arm_neoverse_n2_core_trm_102099_0003_06_en.pdf)；Obsidian 内可用 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]。页码以 PDF 的印刷页码为准，与本文件副本的 PDF 页序一致。副本保持原字节，原文件不修改。

> [!info] 事实与解释
> “原文依据”标明可回查的章节及页码；“理解说明”和“教学示例”解释原理，示例地址、周期和伪结构不代表 N2 的真实测量结果或内部位格式。“待确认”保留原文中的口径问题，不自动补全。
>
> 原图表来自你提供的 PDF 截图，保留水印、标题、图例及跨页续表。为避免丢失条件和脚注，截图按原页正文区域保存；中文表格是归纳表，不能替代原编码表。

## 阅读导航

- [[#总览与关键参数]]
- [[#第1章 引言与阅读约定]]
- [[#第2章 N2核的能力与配置]]
- [[#第3章 技术总览与核心组件]]
- [[#第4章 时钟与复位]]
- [[#第5章 电源管理]]
- [[#第6章 内存管理与地址转换]]
- [[#第7章 L1指令存储系统与MOP cache]]
- [[#第8章 L1数据存储系统]]
- [[#第9章 L2存储系统与CHI接口]]
- [[#第10章 内部RAM直接访问]]
- [[#第11章 RAS与错误处理]]
- [[#第12章 GIC CPU接口]]
- [[#第13章 Advanced SIMD与浮点]]
- [[#第14章 SVE与SVE2]]
- [[#第15章 系统控制与能力发现]]
- [[#第16章 随机数指令与外部RNG]]
- [[#第17章 调试系统]]
- [[#第18章 PMU性能监测]]
- [[#第19章 ETE指令流追踪]]
- [[#第20章 TRBE追踪缓冲]]
- [[#第21章 AMU活动监测]]
- [[#第22章 SPE统计采样]]
- [[#附录A AArch32寄存器]]
- [[#附录B AArch64寄存器]]
- [[#附录C 外部寄存器]]
- [[#附录D UNPREDICTABLE行为]]
- [[#附录E 文档版本变化]]
- [[#寄存器回查索引]]
- [[#原图表回查索引]]
- [[#综合理解与学习路线]]
- [[#待确认事项与使用边界]]

文内回查：[[#寄存器回查索引]] · [[#原图表回查索引]]。系统层面的参考设计见 [[RD-N2-Reference-Design-中文精读]]。

### 按目的阅读

| 阅读目标 | 入口 |
|---|---|
| 先了解核的能力、配置、组件与执行模型 | [[#第2章 N2核的能力与配置]]、[[#第3章 技术总览与核心组件]] |
| 时钟、复位、WFI/WFE、掉电和retention | [[#第4章 时钟与复位]]、[[#第5章 电源管理]] |
| 地址转换、TLB与两阶段翻译 | [[#第6章 内存管理与地址转换]] |
| MOP cache、L1/L2、预取与一致性接口 | [[#第7章 L1指令存储系统与MOP cache]] 至 [[#第10章 内部RAM直接访问]] |
| ECC、错误上报、中断与调试 | [[#第11章 RAS与错误处理]]、[[#第12章 GIC CPU接口]]、[[#第17章 调试系统]] |
| SIMD、SVE/SVE2、系统控制与随机数 | [[#第13章 Advanced SIMD与浮点]] 至 [[#第16章 随机数指令与外部RNG]] |
| PMU计数、ETE追踪、TRBE、AMU与SPE | [[#第18章 PMU性能监测]] 至 [[#第22章 SPE统计采样]] |
| 精确寄存器、边界行为和版本差异 | [[#附录A AArch32寄存器]] 至 [[#附录E 文档版本变化]] |
| 根据当前问题选择阅读顺序 | [[#综合理解与学习路线]] |
| 原文疑点、适用范围和维护约定 | [[#待确认事项与使用边界]] |

## 总览与关键参数

| 项目 | 本版 N2 明确给出的能力 | 依据 |
|---|---|---|
| 架构与执行状态 | Armv9.0-A；AArch32 仅 EL0；AArch64 为 EL0-EL3 | §2.1、§3.3，p.30、43 |
| 地址宽度 | 48 位 VA、48 位 PA | §2.1，p.30 |
| 系统连接 | 仅支持 Direct connect；通过 CPU bridge 接 DSU-110 | §2、§9，p.30、74 |
| L1 I-cache / D-cache | 分离的 64KB、4 路、64B cache line | §7、§8，p.65、69 |
| L0 MOP cache | 1536 个 Macro-operations、4 路 skewed associative | §7，p.65 |
| 私有统一 L2 | 512KB 或 1024KB，8 路、2 banks、64B line | §9，p.74 |
| TLB | L1 ITLB 48 项；L1 DTLB 44 项；L2 TLB 1280 项、5 路；TRBE TLB 2 项 | §6.1，p.58 |
| L2 Transaction Queue | 构建时可配置为 48、56 或 64 | §2.2，p.31 |
| CHI | Issue E；读、写 DAT 通道各为 256 位 | §9，p.74 |
| 向量 | Advanced SIMD / 浮点；SVE 与 SVE2；N2 的 SVE 长度为 128 位 | §2.1、§14，p.31、106 |
| 中断 | GICv4.1 CPU interface，需结合系统外部中断组件 | §12，p.101 |
| PMU | 6 个可配置 64 位事件计数器，并支持周期计数、快照 | §18，p.122 |
| AMU | 7 个 64 位计数器，分 4 项与 3 项两组；后三项在事件表标 Reserved | §21，p.151-152 |
| 硬件调试资源 | 6 个 breakpoint，4 个 watchpoint | §17.2.4，p.115 |
| 选配项 | Crypto、coherent I-cache、RNG、ELA 等 | §2.2，p.31-32 |

**重要区别**：核私有 L2、DSU 集群结构、CMN 系统缓存和 DDR 是不同层次。此前的 [[RD-N2-Reference-Design-中文精读]] 展示一个具体系统，不能把其中的核心数量、SLC 容量或 DDR 通道数视为所有 N2 芯片的固定参数。

## 第1章 引言与阅读约定

**原文范围：p.26-29，§1.1-1.4。** 本章帮助读者判断文档的适用版本、术语和配套资料。

### 1.1 产品修订与文档修订

`r0p3` 中，`r` 表示主要修订，`p` 表示次要修订或修改状态。`Issue 06` 是文档版本；二者不能混为一个编号。本手册属于 2022-10-27 的 `102099_0003_06_en`，产品处于 Final 状态。

### 1.2 读图和读信号的规则

时序图只保证明确标出的时序信息。阴影表示值未定义或不影响该过程；不能从图的横向距离估算额外的周期要求。

“asserted”表示有效状态：active-HIGH 信号有效时为高，active-LOW 信号有效时为低；信号名开头或结尾的 `n` 通常表示低有效。

**教学示例**：`nIRQ = 0` 表示中断请求有效，而不是“没有中断”。查看功耗和握手信号时，应先确认有效电平，再讨论事件先后。

原图 Figure 1-1，p.28：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0028-original.png]]

### 1.3 为什么需要其他手册

| 资料 | 用途 |
|---|---|
| N2 Core TRM，本手册 | N2 实现的模块、行为和寄存器差异 |
| N2 Configuration and Integration Manual，102100 | RTL 配置、RAM、实现和集成信号 |
| DSU-110 TRM，101381 | 核到系统的接口、集群、电源和调试组织 |
| Arm ARM，DDI 0487 | 指令、异常、内存模型和通用架构寄存器语义 |
| CHI，IHI 0050 | 一致性事务、消息、状态和协议约束 |
| RAS、MPAM、GIC、CoreSight 架构资料 | 各扩展的完整规则 |

本手册自身说明，寄存器列表并不完整。寄存器不在本文或本手册里，不等于硬件必然没有实现它。

## 第2章 N2核的能力与配置

**原文范围：p.30-38，§2.1-2.7。** 核心问题是“什么是固定能力，什么由构建和集成决定”。

### 2.1 仅支持 Direct connect

N2 在 DSU-110 的 **Direct connect** 配置中使用。Figure 2-1 展示单核 DSU 例子，其中 DSU 不包含 L3 cache、snoop filter 和 SCU 逻辑。本手册明确说 N2 **只支持 Direct connect**。

原图 Figure 2-1，p.30：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0030-original.png]]

**理解说明**：Direct connect 保留核与外部系统之间所需的桥接和管理功能，不能理解为“CPU 绕过所有一致性机制直接连 DDR”。系统级一致性与共享缓存在哪里实现，要看外部互连设计。第 17 章通用 DSU 调试图包含 L3/SCU，不改变本章对 N2 配置的限制。

### 2.2 构建配置、集成配置、软件配置

| 层次          | 谁决定                | 示例                                          |
| ----------- | ------------------ | ------------------------------------------- |
| Build-time  | IP 实现者，RTL 配置与物理实现 | L2 大小、TQ 大小、Crypto、coherent I-cache、RNG、ELA |
| Integration | SoC 集成者，连接和绑带输入    | 外部中断接口、复位行为、RNG 外设关联                        |
| Software    | 固件、hypervisor、OS   | MMU、缓存、预取、电源、PMU 和 SPE 控制                   |

L2 512KB/1024KB，TQ 48/56/64 是构建选项，不能假定 OS 可以随意在线变更这些容量。ELA-600 是独立许可产品，ELA ATB FIFO 深度可为 4、8、16、32、64；Crypto 同样需额外许可。L2 RAM 时序也有配置选项。

### 2.3 架构特性应逐项判断

| 类别      | 重要能力或限制                                           |
| ------- | ------------------------------------------------- |
| 基本执行    | A32/T32/A64 指令集；AArch32 只在 EL0；AArch64 覆盖 EL0-EL3 |
| 内存      | 48 位 VA/PA；HAFDBS、16 位 VMID、PBHA；不支持 LPA/大 VA 扩展  |
| 虚拟化     | NV/NV2 嵌套虚拟化特性支持，具体行为查架构手册                        |
| 安全      | MTE 总是实现；指针认证增强、FPAC；Crypto 与 RNG 受选配条件影响         |
| 数据处理    | SVE/SVE2、BF16、I8MM；F32MM/F64MM 矩阵扩展不支持            |
| 观测      | PMU、AMU、SPE、ETE、TRBE；ELA 可选                       |
| 不支持的其他项 | TME；FEAT_ExS；FEAT_VPIPT；LSMAOC；AA32HPD            |

“架构可选扩展”与“这个 N2 IP 可以裁剪的组件”不是同一回事。例如 SPE 在架构上是可选扩展，但手册明确说 N2 实现 SPE；是否可裁剪不能仅凭 optional 一词推断。

**待确认**：Table 2-8 使用 `FEAT_SV2` 这一拼写，并列出 SVE 加密指令 Supported；§2.2/§3.1 又说明 Crypto 是选配且单独许可。本文保留两处口径，不据表中 Supported 推断所有芯片都启用加密指令。

全部架构支持原表：[[#图表 第2章|Tables 2-1 至 2-10，含续表]]。

### 2.4 测试与设计流程

ATPG 测试核逻辑，MBIST 测试 RAM；接口使用细节在集成手册。N2 交付为可综合的 SystemVerilog RTL，实际产品还需配置、加入工艺单元与 RAM、综合和布局布线、集成到 SoC、编写初始化软件。测试接口存在不表示软件自动获得任意内部状态访问权限。

### 2.5 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第32页：Table 2-1: Neoverse™ N2 core features that have a dependency on the DSU-110
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=32|p.32]]
>
> Table 2-1: Neoverse™ N2 core features that have a dependency on the DSU-110
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0032-original.png]]

> [!quote]- 原文第33页：Table 2-2: Armv8.0-A optional feature support in the Neoverse™ N2 core；Table 2-3: Arm®v8.1-A optional feature support in the Neoverse™ N2 core；Table 2-4: Arm®v8.2-A optional feature support in the Neoverse™ N2 core
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=33|p.33]]
>
> Table 2-2: Armv8.0-A optional feature support in the Neoverse™ N2 core；Table 2-3: Arm®v8.1-A optional feature support in the Neoverse™ N2 core；Table 2-4: Arm®v8.2-A optional feature support in the Neoverse™ N2 core
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0033-original.png]]

> [!quote]- 原文第34页：Table 2-5: Arm®v8.3-A optional feature support in the Neoverse™ N2 core
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=34|p.34]]
>
> Table 2-5: Arm®v8.3-A optional feature support in the Neoverse™ N2 core
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0034-original.png]]

> [!quote]- 原文第35页：Table 2-6: Arm®v8.4-A optional feature support in the Neoverse™ N2 core；Table 2-7: Arm®v8.5-A optional feature support in the Neoverse™ N2 core；Table 2-8: Arm®v9.0-A feature support in the Neoverse™ N2 core；Table 2-9: Other standards and specifications support in the Neoverse™ N2 core
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=35|p.35]]
>
> Table 2-6: Arm®v8.4-A optional feature support in the Neoverse™ N2 core；Table 2-7: Arm®v8.5-A optional feature support in the Neoverse™ N2 core；Table 2-8: Arm®v9.0-A feature support in the Neoverse™ N2 core；Table 2-9: Other standards and specifications support in the Neoverse™ N2 core
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0035-original.png]]

> [!quote]- 原文第36页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=36|p.36]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0036-original.png]]

> [!quote]- 原文第38页：Table 2-10: Product revisions
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=38|p.38]]
>
> Table 2-10: Product revisions
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0038-original.png]]


## 第3章 技术总览与核心组件

**原文范围：p.39-44，§3.1-3.3。** 本章建立整体工作模型；更精确参数以各后续章节为依据。

### 3.1 先读原结构图

原图 Figure 3-1，p.40，完整保留标题及可选组件图例：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/figure-3-1-original.png]]

| 组件组 | 职责 |
|---|---|
| I-cache、ITLB、MOP、branch prediction | 取到正确位置的指令，准备内部操作表示 |
| Decode、rename、issue | 译码，组织依赖，选择可以进入执行流水线的操作 |
| Integer / vector execution | 执行整数、SIMD、浮点、SVE/SVE2；可选 Crypto |
| D-cache、DTLB、MMU、L2 | 地址与权限检查、数据访问、缓存和一致性响应 |
| CPU bridge | 缓冲和同步，连接核与 DSU-110 |
| PMU、AMU、SPE、trace、GIC | 统计、采样、追踪、系统管理和中断 |

绿色 Crypto 与 ELA 是图中标出的可选组件。AMU、SPE 没有单独画出，不表示它们不存在。这张图也没有公开全部流水级、ROB、端口或逐周期路径。

### 3.2 重命名与发射为什么分开

Register rename 支持乱序执行，并将已译码指令送到不同 issue queues。Issue 决定操作何时进入执行流水线。

**教学示例**：

```text
A: r1 = load(address)
B: r2 = r1 + 1
C: r3 = r4 + r5
```

B 依赖 A 返回的数据；C 若独立且资源就绪，可以先执行。寄存器重命名能缓解因名称复用造成的约束，却不能消除 B 对 A 计算结果的真实依赖。乱序执行仍必须保持架构规定的软件可观察行为。

### 3.3 一条load把多个模块连在一起

取指地址通过 ITLB 转换，指令来自 I-cache 或可复用的 MOP 表示；操作经重命名与发射进入数据访问路径；DTLB/MMU 给出地址、权限和属性；数据可能在本核缓存中，也可能需要经 L2、bridge、DSU 和外部系统取得。整个过程可以被 PMU 计数、被 SPE 抽样，也可能与 snoop 或中断交错。

### 3.4 编程模型和接口边界

AArch32 只在 EL0，AArch64 覆盖 EL0-EL3；SVE 仅在 AArch64。执行状态、异常级别、安全状态是三个维度，不能把“64 位”“EL2”“Non-secure”当成同一分类。

核经 CPU bridge 连接 DSU-110，外部 SoC 接口由 DSU-110 管理。每核一个 bridge；默认异步，并可配置同步。将 bridge 配成同步不会把 debug/trace 接口也改成同步，这些接口始终异步。

## 第4章 时钟与复位

**原文范围：p.45。** 每个 N2 核有一个时钟域、一个时钟输入；CPU bridge 中的架构级 clock gate 可控制这个输入。核内部还有 regional 和 local clock gating，分别减少模块、寄存器组的切换。

| 机制 | 作用 | 注意 |
|---|---|---|
| 顶层 clock gate | 大范围停止核时钟 | 开钟/关钟不等于电源移除 |
| Regional / local gating | 停止暂时不工作的块或寄存器 | 减少动态功耗，模块仍可保留状态 |
| Warm reset | 复位主要核状态 | 不复位部分 debug/trace 与 RAS 状态 |
| Cold reset | 复位整个核逻辑 | 包括调试和追踪逻辑 |

**理解说明**：故障后仍能读到 RAS 信息，与部分状态不被 Warm reset 清掉有关。但“暖复位保留一些诊断状态”不能推出“程序和所有缓存内容正常保留”。正常复位、电源保持和 Debug recovery 是不同机制。

时钟/复位整体序列应结合 DSU-110 TRM；具体 RAM/寄存器的复位值还应查附录，不能用一个“Warm reset 不变”的概括替代位域规则。

## 第5章 电源管理

**原文范围：p.46-56，§5.1-5.6。** 最重要的是：关钟、retention 和 Off 不同；低功耗期间仍要服务系统请求；掉电前必须处理一致性和错误中断。

### 5.1 电源与电压域

`PDCORE/VCORE` 包含核逻辑及 bridge 的核侧；`PDCLUSTER/VCLUSTER` 包含 bridge 的系统侧。DSU 的 PPU 控制电源模式转换，每核有独立 PPU，cluster 也有 PPU。核根据 PPU 请求完成关钟、清理缓存、退出一致性等动作，再接受转换。

原图 Figure 5-1，p.46：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0046-original.png]]

若与 DSU 同步共用时钟，或不需要 DVFS，VCORE 与 VCLUSTER 可连接同一供电。原文还有域分布图 Figure 5-2，见 [[#图表 第5章]]。

### 5.2 WFI/WFE不是掉电

WFI/WFE 主要关闭核时钟，电源仍在、状态保留。进入前等待核中指令及显式访存退休，store 已更新缓存或发向下游；这不是“所有数据已经写入 DDR”的保证。若 WFE 执行时 event register 已置位，它清除此标志而不会进入低功耗。

**容易混淆的行为**：WFI/WFE 期间收到 snoop、cache/TLB maintenance、utility bus、GIC 或 debug 访问时，可以临时开钟服务请求，处理后仍保持 WFI/WFE。暂时开钟不一定意味着唤醒软件执行。

**教学示例**：RN0 在 WFI，RN1 请求 RN0 缓存中的最新数据；RN0 可临时开钟处理 snoop，然后继续等待中断。系统一致性不能依赖 RN0 上的软件先醒来。

### 5.3 六种电源模式与合法转换

| 模式 | 状态 | 使用含义 |
|---|---|---|
| ON | 正常供电、运行 | 正常工作状态 |
| FULL_RET | 保留寄存器和 RAM，不运行 | 必须先在 WFI/WFE，满足计时器与其他条件 |
| OFF | 完全掉电、状态丢失 | 进入时自动 clean/invalidate 私有缓存并退出一致性 |
| OFF_EMU | 保持电源/时钟，功能接口模拟 Off | 保留外部调试，用于验证上下电软件 |
| DBG_RECOV | 保留 cache/RAS 便于故障诊断 | 只能调试，不能正常运行使用 |
| WARM_RST | 执行 Warm reset | debug、trace、RAS 中的指定状态保留 |

原图 Figure 5-3，p.51；合法转换应按箭头判断：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0051-original.png]]

FULL_RET 还要求 retention timer 到期，且没有临时开钟活动；snoop、maintenance、debug/GIC 访问既可使其退出 retention，也可能仍不让软件退出 WFI/WFE。原模式表 Table 5-1，p.50，见图表索引。

### 5.4 正常掉电的关键顺序

原文 §5.5，p.54 的软件步骤：

1. 必要时把需要恢复的核状态保存到系统内存。
2. 禁止相应 GIC group interrupt enable，配置 `GICR_WAKER`，确认 `ChildrenAsleep`。
3. 禁止并清理 RAS 中断，或将错误输出重定向给系统错误管理组件。
4. 设置 `IMP_CPUPWRCTLR_EL1.CORE_PWRDN_EN = 1`。
5. 执行 `ISB`。
6. 执行 `WFI`，由 power controller 请求后，硬件清理缓存并退出一致性。

这是特定掉电路径。在 `CORE_PWRDN_EN` 已设置的情况下，WFI 会屏蔽中断和唤醒事件，只能通过 reset 唤醒，不能照搬普通 idle 的“来个中断就醒”理解。

### 5.5 为什么RAS处理是必要步骤

掉电 WFI 是软件不可回头的节点。如果 RAS 错误输出仍有效，硬件可能拒绝掉电，但软件又无法响应中断，形成“电源还 ON、软件不运行”的状态。手册指出这种情况只能通过 cluster reset 重启软件。

全关错误中断也有代价：错误检测/纠正即使继续进行，Off 后记录会丢失；未报告的不可纠正错误可能损害系统。保留不可纠正错误报告时，需要系统设计支持重路由和外部复位处理，不能只改几个寄存器就假定闭环成立。

### 5.6 Debug recovery与debug over powerdown

Debug recovery 在 watchdog 等故障后保留 cache/RAS 信息；未完成访存可能在复位后返回，snoop 可能扰动缓存或造成死锁，因此仅限诊断，可能需要更广系统复位。

Debug over powerdown 则借助 DSU DebugBlock 保持调试连接。DebugBlock 必须持续供电；保持连接不代表已掉电的核 RAM 仍可任意读取。

**原文依据**：§5.4-5.6，p.49-56。全部电源原图表见 [[#图表 第5章]]。

### 5.7 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第47页：Figure 5-2: Core power domains in a cluster with one Neoverse™ N2 core
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=47|p.47]]
>
> Figure 5-2: Core power domains in a cluster with one Neoverse™ N2 core
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0047-original.png]]

> [!quote]- 原文第50页：Table 5-1: Neoverse™ N2 core power modes
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=50|p.50]]
>
> Table 5-1: Neoverse™ N2 core power modes
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0050-original.png]]


## 第6章 内存管理与地址转换

**原文范围：p.57-64，§6.1-6.8。** MMU 负责地址转换、权限、内存属性和缓存策略；TLB 缓存的是转换结果，不是程序数据。

### 6.1 Stage 1与Stage 2

| 模式 | 转换 | 常见理解 |
|---|---|---|
| Stage 1 | VA → PA，或 VA → IPA | OS 管理进程虚拟地址 |
| Stage 2 | IPA → PA | Hypervisor 管理客体物理地址 |
| Combined | VA → IPA → PA | 虚拟机里运行进程时的两阶段转换 |

**教学示例**：虚拟机中的应用读 VA `0x4000`，客体页表将其映射为 IPA `0x8000`，hypervisor 又把 IPA 映射为 PA `0xA000`。数据缓存最终需要识别真实物理地址，不能把 IPA 当成系统 DDR 地址。Stage 2 也可能修改 Stage 1 给出的属性或施加额外限制。

### 6.2 两级TLB和页表预取

| 结构 | 配置 | 缓存的主要内容 |
|---|---|---|
| L1 ITLB | 全相联，48 entries | 4KB、16KB、64KB、2MB 的 VA→PA 转换 |
| L1 DTLB | 全相联，44 entries | 4KB、16KB、64KB、2MB、512MB 的 VA→PA 转换 |
| L1 TRBE TLB | 2 entries | 追踪缓冲写入所用 VA→PA 转换 |
| L2 TLB / MMUTC 路径 | 5 路，1280 entries，指令/数据共用 | 多种 VA→PA、IPA→PA 映射及 table walk 中间信息 |
| Translation table prefetcher | 可通过控制寄存器关闭 | 检测连续页表访问并预取后续内容 |

L2 支持的 VA→PA 块大小包含 4KB、16KB、64KB、2MB、32MB、512MB、1GB；Stage 2 块支持需同时看 translation granule，不能把所有大小当成每种 granule 都可用。

原表 Table 6-1，p.58：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0058-original.png]]

L1 TLB 命中提供单 CLK 周期的转换访问。§6.1 对数据侧 L1 miss / L2 TLB hit 路径给出相对 L1 hit 的 3-cycle penalty，并说明仲裁可增加延迟；不能把它当成所有 table walk 的固定延迟。

### 6.3 命中判断不是只比较VA

TLB entry 包括 VA、PA、内存类型与权限，还关联 translation regime、global/ASID、适用的 VMID。命中必须满足相应上下文条件。Global 条目可忽略 ASID，但不能据此忽略所有 regime 或虚拟机条件。

**理解说明**：进程 A 和 B 的 VA `0x4000` 可以指向不同 PA；ASID 帮助保留并区分这两份转换。VMID 服务类似的虚拟机区分。标识减少切换时整体失效的需要，但修改页表、标识复用等场景仍需按架构做 TLB maintenance。

### 6.4 页表遍历流程

```text
查询对应 L1 TLB
    ├─ hit：返回地址、权限和属性
    └─ miss：查询 L2 TLB
                ├─ hit：利用已有转换
                └─ miss：硬件读取 translation tables
```

原图 Figure 6-1，p.61：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0061-original.png]]

Table walk 描述符经 L2 memory system 读取；页表访问可以设置为 cacheable。**TLB miss 不必然等于 DDR 访问**：L2 TLB 或缓存中的页表内容都可能减少远端访问。

### 6.5 Access flag和dirty state的硬件更新

N2 支持硬件更新 AF 和 dirty state，由 `TCR_ELx`/`VTCR_EL2` 控制，dirty 管理使用 DBM。**页表必须位于 Inner Write-Back 且 Outer Write-Back 的 Normal memory**，否则所请求的硬件更新会产生手册给出的 abort 编码 `0b110001`。

页表 dirty state 描述映射写入管理，与 cache line 的 dirty/coherence 状态不同；不能用“页表 dirty”直接判定应发送哪种 CHI writeback。

### 6.6 Fault、external abort与TLB冲突

MMU 可以报告地址大小、translation、access flag、permission 等 fault。External abort 来自外部接口或不可纠正 ECC，属于另一类问题。§6.6 按 Normal/Device、load/store、atomic、maintenance 等给出同步/异步报告规则，不能统一写成“访存出错总能由当前指令精确报告”。

手册还规定：TLB 冲突由硬件失效冲突项处理，不产生 conflict abort。Contiguous hint 等页表误编程存在特定行为，不能以“没有 fault”推断页表配置有效。

**待确认**：p.62 的异步 Device load 描述写作 “without release semantics”，与前文 load-acquire 分类的术语不一致。本文不擅自改写，编程判断应核对 Arm ARM 和最新勘误。

### 6.7 内存属性会被N2降级

| 软件属性组合 | N2 的重要处理 |
|---|---|
| Inner WB + Outer WB | 可进入 L1 D-cache 与 L2 |
| Inner Write-Through | 降为 Non-cacheable |
| Outer Write-Through 或 Outer Non-cacheable | 即便 Inner 为 WB，也降为 Non-cacheable |
| Device / Non-cacheable | 按表中规则处理为 Outer Shareable |
| Inner Shareable 的相应 Normal memory | 按 Table 6-3 处理为 Outer Shareable |

Allocation hint 也有传播规则：Outer No Allocate 可以向 DSU 传播为 No Allocate，但不能据此说本核完全不分配。以 Table 6-2 的本核行为和外发属性分别判断。

原表 Tables 6-2、6-3，p.63：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0063-original.png]]

### 6.8 PBHA不是统一的架构策略编号

Page-Based Hardware Attributes 可把页表中的最多 4 位属性带到事务，含义由系统设计定义。两阶段都启用时，按位由 Stage 2 的已启用 PBHA 优先；均未启用的位为 0。相同 PA 的不同 VA alias 若给出不同 PBHA，结果为 UNPREDICTABLE。

**教学示例**：系统设计者可能让某一位选择下游策略，但这只是说明用途，不能把某位固定解释为“低延迟”或“高优先级”。PBHA 与 MPAM 也不是同一字段。

## 第7章 L1指令存储系统与MOP cache

**原文范围：p.65-68，§7.1-7.4；MOP 内容的补充依据为 §3.1，p.40。** 前端同时解决“下一条取哪里”“机器码是什么”“能否复用内部操作表示”。

### 7.1 I-cache、ITLB、MOP分别保存什么

| 结构 | 保存内容 | N2 特征 |
|---|---|---|
| I-cache | 指令机器码字节 | 64KB、4 路、64B line；VIPT，行为满足 PIPT；parity |
| ITLB | 取指的地址转换、属性和权限 | 参数见第 6 章 |
| L0 MOP cache | 已译码并优化的内部操作表示 | 1536 MOP、4 路 skewed associative；VIVT，行为满足 PIPT |

表中“behaving as PIPT”是行为保证，不应据此把物理实现索引方式改写成 PIPT。替换策略为 pseudo-LRU。Skewed associative 也不能直接当成普通组相联的固定索引公式。

原表 Table 7-1，p.65：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0065-original.png]]

### 7.2 MOP具体例子

p.40 明确说明 L0 MOP cache 包含 decoded and optimized instructions。以下用两条指令解释这种内部表示与执行数据的区别；具体编码和拆分方式未公开。

```asm
0x1000: ADD X0, X1, X2
0x1004: LDR X3, [X4, #8]
```

I-cache 保存这两条 A64 指令的二进制编码。MOP cache 缓存的内部语义，可以这样示意：

```text
操作 A：整数加法，源为 X1/X2，目标 X0，宽度 64 位
操作 B：读取 64 位数据，地址表达式 X4+8，目标 X3
```

这是**语义示意，不是 N2 的实际 MOP 字段格式**。MOP 不保存这次 X1/X2 的当前数值，不保存 LDR 读取的数据，也不保存上次运算结果。

| 执行次数 | X1 / X2 | ADD 的结果 | X4 | LDR 的地址 |
|---|---|---|---|---|
| 第一次 | 10 / 20 | 30 | 0x3000 | 0x3008 |
| 第二次 | 100 / 200 | 300 | 0x5000 | 0x5008 |

两次可复用同一操作描述，却必须使用每次的新操作数。循环命中 MOP 时可减少重复译码工作，提高取指阶段吞吐与延迟表现，但仍要重命名、调度、计算和访存。**1536 个 MOP 不等于固定 1536 条程序指令，更不能按 A64 指令 4 字节换算容量。**

第 10 章允许读出 MOP RAM 的 104 位原始返回数据，但只命名为 Macro-operation data，没有解释其中具体 opcode/operand 字段，所以不能据此绘制真实编码格式。

### 7.3 取指、复位与推测访问

正常 reset 自动失效 I-cache；Debug recovery 例外，但该模式下 I-cache 不正常工作。I-cache 关闭时，原 cacheable 取指按 non-cacheable 对待，可能不与其他核缓存保持所需的一致性。

取指可推测执行；分支或异常会冲刷已取指令。因此 Device 页必须 XN，设备与代码物理地址空间应分开，尤其在地址转换关闭时避免推测读到读敏感外设。

I-cache miss 可以查询 L1 D-cache，但这不会由取指引起 D-cache refill；相关分配行为需结合 I-cache 使能及数据缓存使能条件，不能套用普通 load 流程。

### 7.4 分支预测

包含 BTB、branch direction predictor、return stack、static predictor 和 indirect predictor。条件分支预测方向与目标；无条件分支主要预测目标。当前 EL 的 MMU 使能会影响 program flow prediction 是否启用。

Return stack 保存返回地址与指令状态，服务函数调用/返回。Exception return 指令 `ERET/ERETAA/ERETAB` 不预测。原文 AArch32 push 列表包含 `MOV pc,r14`，不要自行把它按常识归入另一类，应以具体指令规则回查。

### 7.5 可选的I-cache硬件一致性

`COHERENT_ICACHE=TRUE` 时：

- I-cache 与 L2 **strictly inclusive**，I-cache 中的 line 必须存在于 L2。
- L2 监视写入和一致性失效，必要时失效对应 I-cache 条目。
- I-cache invalidate 指令按 no-op 处理，不引发相应 DVMMsg 广播。
- `CTR_EL0[29]` 为 1，软件可识别这一能力。

一致性域中不能混入需要软件 I-cache maintenance 的 coherent agent。手册建议此配置用 1MB L2；512KB 也允许，原文给出约 1-2% 的特定性能影响说明，不应当成所有应用的必然结果。

**理解说明**：硬件处理 I-cache 一致性，不等于自修改代码可以忽略一切同步要求；指令流同步与 cache invalidate 是不同问题。

## 第8章 L1数据存储系统

**原文范围：p.69-73，§8.1-8.5。** 它处理 load/store，也处理 atomic、cache maintenance、MTE 指令和一致性请求。

### 8.1 参数与cache使能

D-cache 为 64KB、4 路、64B line，VIPT 但行为满足 PIPT，使用 ECC、pseudo-LRU。与整数流水线有 3×64-bit 读路径和 4×64-bit 写路径；与 vector 有 3×128-bit 读、2×128-bit 写路径。**路径数量不等于软件每周期保证退休同样多条 load/store。**

原表 Table 8-1，p.69：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0069-original.png]]

L1 D-cache 和 L2 不能独立禁用：数据缓存关闭后，本核发出的原 cacheable 数据访问不再在这两层缓存；cache maintenance 仍可执行。

没有一条“失效整个 D-cache”的指令；软件须根据几何参数遍历 set/way。N2 的 DCCISW 是 clean+invalidate，`HCR_EL2.SWIO` 不改变其行为。章内用 MESI 说明多核数据一致性；不要把内部 MESI 编码机械等同于所有 CHI 状态编码。

### 8.2 Near atomic与far atomic

Near atomic 倾向在近端缓存处执行，far atomic 向下游传递执行；选择与数据所在位置、系统行为和互连支持有关。L1 hit 时尝试 near，但不保证最终一直 near。手册给出预先 `PLDW`/`PRFM PSTL1KEEP` 以及控制寄存器设置的办法，帮助提高 near atomic 的可能性。

Device 或 Non-cacheable atomic 依赖互连支持；不支持时会 abort。

**待确认**：§8.2 使用“cluster L3 执行 atomic”的通用 DSU 描述，而 §2/§9 要求 N2 Direct connect，示例没有集群 L3。这里保留 near/far 的决策条件，具体 Direct connect 系统执行点需查 DSU/互连实现，不能虚构 N2 自带 L3。

### 8.3 Exclusive monitor与锁

内部 exclusive monitor 为 open/exclusive 两态，处理 Load-Exclusive、Store-Exclusive 和 `CLREX`。被监视的块为 16 words，即一条 64B cache line。

**教学示例**：

```asm
retry:
    LDXR W0, [X1]
    ADD  W0, W0, #1
    STXR W2, W0, [X1]
    CBNZ W2, retry
```

若另一核的操作使 monitor 条件失效，STXR 可失败并重试。示例只解释更新重试，实际同步原语还必须选择所需 acquire/release 或 barrier 语义。**exclusive monitor 的有效，不等于永远持有一条 Unique cache line。**

### 8.4 预取和DC ZVA

PRFM/PLD/PLDW 提示未来地址访问。PRFM miss 且 cacheable 时可启动 linefill，但在 linefill 启动时就可退休，不等待数据回来。因此 `PRFM; LDR` 不保证后续读取一定命中。

Load-side 硬件预取使用 VA，面向 L1/L2；store-side 使用 PA，只面向 L2。PLI 可在后台预取至 L2。预取是性能机制，不替代权限、内存顺序或完成性保证。

`DC ZVA` 对齐清零 64B 内存块；应按地址对齐和权限规则使用，不能把它看成单纯“写某个缓存内部 RAM”。

### 8.5 Write streaming为什么避免无意义读旧值

通常 read/write miss 会分配缓存行。大块 `memset` 连续覆盖整行时，先读取旧数据再全部覆盖会浪费带宽并污染缓存。N2 检测连续若干次“linefill 完成前已覆盖整行”，切换 write streaming。

模式下 load 仍正常查缓存和 refill；store 仍查缓存，**miss 时倾向向 L2/系统写出而不启动本层 linefill**，并非所有 store 都绕开缓存。检测到不满整行的 cacheable write burst，或 load 读取正在写的同一行，可退出模式。

**教学示例**：清零 1MB 缓冲区，连续写满许多 64B line。对旧内容没有需求时，减少 read-for-allocation 有意义；反复修改少量字节的计数器则不符合这个场景。

进一步的连续写可让 L2、SLC 或 DRAM 路径得到 streaming 指示。`WS_THR_L2`、`WS_THR_L3`、`DRAM_WR_THR` 管理阈值，`WS_THR_L4` 无效果。阈值不表示主接口恰好发出这么多次 linefill 后立即切换。

## 第9章 L2存储系统与CHI接口

**原文范围：p.74-75，§9.1-9.3。** L2 是核私有、统一的指令/数据缓存，也服务 table walk 和外部 snoop。

### 9.1 参数、替换和包含关系

L2 为 512KB 或 1024KB、8 路、2 banks、PIPT、64B line、ECC，使用 dynamic biased replacement。它包含在 L2 memory system 中，与 L2 TLB 共处这一层功能组织；**L2 TLB 不是 L2 data cache 的“页表数据区”。**

原表 Table 9-1，p.74：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0074-original.png]]

`COHERENT_ICACHE=FALSE` 时，I-cache/L2 是 weakly inclusive：共同分配不意味着 L2 eviction 一定 back-invalidate I-cache；为 TRUE 时 strictly inclusive，L2 victimization 可以使 I-cache 失效。

### 9.2 内存类型和Transient hint

仅 Inner WB+Outer WB 的相应内存在 L1 D-cache/L2 正常缓存，WT 或 Outer NC 组合降级为 NC。Transient read 仍可分配 L1，但更可能优先被淘汰；L2 淘汰 transient line 时不向下游缓存分配。Hint 影响策略，不保证一条 line 永远在某层保留或从不分配。

### 9.3 CHI通道与outstanding能力

核 L2 与 DSU-110 之间有一个 **CHI Issue E** 接口，读、写 DAT 通道宽度为 256 bits。

**教学计算**：64B line = 512 bits，满行有效负载在 256-bit DAT 通道上通常需要两次 32B 数据传输；这不表示一次 CPU load 固定两周期完成，还涉及事务路径、时钟、握手和响应。

| TQ 构建大小 | read issuing 最大值 | write issuing 最大值 | DVM issuing 最大值 | snoop acceptance 最大值 |
|---|---:|---:|---:|---:|
| 48 | 46 | 46 | 46 | 29 |
| 56 | 54 | 54 | 54 | 33 |
| 64 | 62 | 62 | 62 | 37 |

原表 Table 9-2，p.75：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0075-original.png]]

这些是各类事务的最大可能能力，**不能相加为同时可用的独立总容量**。实际并发还受共享资源、下游信用、retry、顺序和事务类型制约。

### 9.4 与CHI知识库的连接

这章给出 N2 实现的接口与资源上限；[[CHI-节点角色与能力]]、[[CHI-通道与方向]]、[[CHI-Cache状态模型]]、[[CHI-信用流控与Request-Retry]] 解释协议语义。现有 CHI 库以 Issue H 为主，而本 N2 明确为 Issue E，版本扩展不能直接套用。

## 第10章 内部RAM直接访问

**原文范围：p.76-95，§10.1-10.2。** 这是诊断缓存、TLB 和前端状态的接口，**只能读取内部结构，不能用它更新 cache/TLB 内容**；仅 EL3 可用，其他模式执行相应操作会触发 Undefined Instruction。

### 10.1 操作的三个步骤

1. 根据目标 RAM，构造包含 RAMID、index、way/bank 等的选择值。
2. 通过 `SYS_IMP_RAMINDEX` 发出选择/读取操作。
3. 读取 `IMP_IDATA0/1/2_EL3` 或 `IMP_DDATA0/1/2_EL3`，按目标结构解释返回值。

**原文依据**：§10，p.76；B.4.1，p.457。不能把普通 VA/PA 直接填入所有 RAM 的 INDEX；不同 RAM 有不同编码和 XOR 规则。

### 10.2 覆盖的内部结构

| 类别 | 可选择的结构 | 编码/返回说明 |
|---|---|---|
| L1 前端 | I-cache tag/data、BTB、GHB、BIM、ITLB、MOP | §10.1，p.76-84 |
| L1 数据 | D-cache tag/data、DTLB | §10.1，p.78、84-87 |
| L2 | tag/data、TLB、victim/replacement 信息 | §10.2，p.87-95 |

L1 instruction/data 为 4 路，L2 为 8 路；L2 编码还随 512KB/1MB 配置不同。L2 index 使用物理地址位的 XOR 及 way 相关变换，不应按简单的“PA 中间位直接为 set”推断。

所有 **Tables 10-1 至 10-62** 及跨页续表已截入 [[#图表 第10章]]，实际解码应查看对应原表。

### 10.3 从返回数据理解cache line的组成

D-cache tag 除物理地址、Non-secure、MESI 状态外，还有 MTE tag 数据/状态、poison、prefetch/transient 等信息。Data RAM 返回真正的数据，同时单独包含 ECC/poison。**软件数据值、cache coherence state、MTE tag 和错误标记属于不同维度。**

L2 tag 还有 MPAM 的 PARTID/PMG/NS、PBHA、L1 valid 等。Coherent I-cache 开启与关闭时，其位域布局不同；不要用一种布局解另一种配置的 dump。

**教学示例**：某个缓存 line 的数据字节可能正确，但 tag 中的状态、地址或 poison 异常，仍可能导致错误。一致性排查要同时核对 tag、data、状态和 ECC，不能只看十六进制数据是否相同。

### 10.4 MOP RAM返回值能告诉我们多少

Tables 10-30/31/32 将返回值定义为：

```text
IDATA0[63:0] = Macro-operation data[63:0]
IDATA1[39:0] = Macro-operation data[103:64]
IDATA1[63:40] = 0
IDATA2[63:0] = 0
```

原表在 p.83-84：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0083-original.png]]

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0084-original.png]]

这些是诊断读取的拼接方式，没有公开 MOP 内部每一位的操作含义。104 位返回格式不能直接换算整个 MOP cache 的物理 RAM 容量，因为还可能涉及组织、有效信息、保护和打包。

### 10.5 原表中的编码疑点

**待确认**：Table 10-28 的位范围存在重叠，Table 10-58 对 ASID 的范围/宽度表述也有疑点，Table 10-46 写 L2 TLB Way(0-5)，而 Table 6-1 写 5-way。本文不自动修正原编码；调试工具实现应核对该版勘误或更新手册。

### 10.6 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第76页：Table 10-1: System registers used to access internal memory；Table 10-2: Neoverse™ N2 L1 instruction cache tag location encoding
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=76|p.76]]
>
> Table 10-1: System registers used to access internal memory；Table 10-2: Neoverse™ N2 L1 instruction cache tag location encoding
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0076-original.png]]

> [!quote]- 原文第77页：Table 10-3: Neoverse™ N2 L1 instruction cache data location encoding；Table 10-4: Neoverse™ N2 L1 BTB data location encoding；Table 10-5: Neoverse™ N2 L1 GHB data location encoding；Table 10-6: Neoverse™ N2 L1 instruction TLB data location encoding；Table 10-7: Neoverse™ N2 BIM data location encoding
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=77|p.77]]
>
> Table 10-3: Neoverse™ N2 L1 instruction cache data location encoding；Table 10-4: Neoverse™ N2 L1 BTB data location encoding；Table 10-5: Neoverse™ N2 L1 GHB data location encoding；Table 10-6: Neoverse™ N2 L1 instruction TLB data location encoding；Table 10-7: Neoverse™ N2 BIM data location encoding
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0077-original.png]]

> [!quote]- 原文第78页：Table 10-8: Neoverse™ N2 L0 Macro-operation cache data location encoding；Table 10-9: Neoverse™ N2 L1 data cache tag location encoding；Table 10-10: Neoverse™ N2 L1 data cache data location encoding；Table 10-11: Neoverse™ N2 L1 data TLB location encoding
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=78|p.78]]
>
> Table 10-8: Neoverse™ N2 L0 Macro-operation cache data location encoding；Table 10-9: Neoverse™ N2 L1 data cache tag location encoding；Table 10-10: Neoverse™ N2 L1 data cache data location encoding；Table 10-11: Neoverse™ N2 L1 data TLB location encoding
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0078-original.png]]

> [!quote]- 原文第79页：Table 10-12: L1 instruction cache tag format for Instruction Register 0；Table 10-13: L1 instruction cache tag format for Instruction Register 1；Table 10-14: L1 instruction cache tag format for Instruction Register 2；Table 10-15: L1 instruction cache data format for Instruction Register 0；Table 10-16: L1 instruction cache data format for Instruction Register 1
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=79|p.79]]
>
> Table 10-12: L1 instruction cache tag format for Instruction Register 0；Table 10-13: L1 instruction cache tag format for Instruction Register 1；Table 10-14: L1 instruction cache tag format for Instruction Register 2；Table 10-15: L1 instruction cache data format for Instruction Register 0；Table 10-16: L1 instruction cache data format for Instruction Register 1
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0079-original.png]]

> [!quote]- 原文第80页：Table 10-17: L1 instruction cache data format for Instruction Register 2；Table 10-18: L1 BTB cache format for Instruction Register 0；Table 10-19: L1 BTB cache format for Instruction Register 1；Table 10-20: L1 BTB cache format for Instruction Register 2；Table 10-21: L1 GHB cache format for Instruction Register 0；Table 10-22: L1 GHB cache format for Instruction Register 1；Table 10-23: L1 GHB cache format for Instruction Register 2
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=80|p.80]]
>
> Table 10-17: L1 instruction cache data format for Instruction Register 2；Table 10-18: L1 BTB cache format for Instruction Register 0；Table 10-19: L1 BTB cache format for Instruction Register 1；Table 10-20: L1 BTB cache format for Instruction Register 2；Table 10-21: L1 GHB cache format for Instruction Register 0；Table 10-22: L1 GHB cache format for Instruction Register 1；Table 10-23: L1 GHB cache format for Instruction Register 2
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0080-original.png]]

> [!quote]- 原文第81页：Table 10-24: L1 BIM cache format for Instruction Register 0；Table 10-25: L1 BIM cache format for Instruction Register 1；Table 10-26: L1 BIM cache format for Instruction Register 2；Table 10-27: L1 instruction TLB format for Instruction Register 0
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=81|p.81]]
>
> Table 10-24: L1 BIM cache format for Instruction Register 0；Table 10-25: L1 BIM cache format for Instruction Register 1；Table 10-26: L1 BIM cache format for Instruction Register 2；Table 10-27: L1 instruction TLB format for Instruction Register 0
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0081-original.png]]

> [!quote]- 原文第82页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=82|p.82]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0082-original.png]]

> [!quote]- 原文第85页：Table 10-35: L1 data cache tag format for Data Register 2；Table 10-36: L1 data cache data format for Data Register 0；Table 10-37: L1 data cache data format for Data Register 1；Table 10-38: L1 data cache data format for Data Register 2；Table 10-39: L1 data TLB format for Data Register 0
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=85|p.85]]
>
> Table 10-35: L1 data cache tag format for Data Register 2；Table 10-36: L1 data cache data format for Data Register 0；Table 10-37: L1 data cache data format for Data Register 1；Table 10-38: L1 data cache data format for Data Register 2；Table 10-39: L1 data TLB format for Data Register 0
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0085-original.png]]

> [!quote]- 原文第86页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=86|p.86]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0086-original.png]]

> [!quote]- 原文第87页：Table 10-40: L1 data TLB format for Data Register 1；Table 10-41: L1 data TLB format for Data Register 2；Table 10-42: Neoverse™ N2 L2 cache tag location encoding for 512KB
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=87|p.87]]
>
> Table 10-40: L1 data TLB format for Data Register 1；Table 10-41: L1 data TLB format for Data Register 2；Table 10-42: Neoverse™ N2 L2 cache tag location encoding for 512KB
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0087-original.png]]

> [!quote]- 原文第88页：Table 10-43: Neoverse™ N2 L2 cache tag location encoding for 1MB；Table 10-44: Neoverse™ N2 L2 cache data location encoding for 512KB；Table 10-45: Neoverse™ N2 L2 cache data location encoding for 1MB
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=88|p.88]]
>
> Table 10-43: Neoverse™ N2 L2 cache tag location encoding for 1MB；Table 10-44: Neoverse™ N2 L2 cache data location encoding for 512KB；Table 10-45: Neoverse™ N2 L2 cache data location encoding for 1MB
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0088-original.png]]

> [!quote]- 原文第89页：Table 10-46: Neoverse™ N2 L2 TLB location encoding；Table 10-47: Neoverse™ N2 L2 victim location encoding；Table 10-48: L2 tag cache format for Data Register 0
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=89|p.89]]
>
> Table 10-46: Neoverse™ N2 L2 TLB location encoding；Table 10-47: Neoverse™ N2 L2 victim location encoding；Table 10-48: L2 tag cache format for Data Register 0
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0089-original.png]]

> [!quote]- 原文第90页：Table 10-49: L2 tag cache format for Data Register 1；Table 10-50: L2 tag cache format for Data Register 2；Table 10-51: L2 tag cache format for Data Register 0
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=90|p.90]]
>
> Table 10-49: L2 tag cache format for Data Register 1；Table 10-50: L2 tag cache format for Data Register 2；Table 10-51: L2 tag cache format for Data Register 0
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0090-original.png]]

> [!quote]- 原文第91页：Table 10-52: L2 tag cache format for Data Register 1；Table 10-53: L2 tag cache format for Data Register 2
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=91|p.91]]
>
> Table 10-52: L2 tag cache format for Data Register 1；Table 10-53: L2 tag cache format for Data Register 2
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0091-original.png]]

> [!quote]- 原文第92页：Table 10-54: L2 data RAM format for Data Register 0；Table 10-55: L2 data RAM format for Data Register 1；Table 10-56: L2 data RAM format for Data Register 2；Table 10-57: L2 TLB format for Instruction Register 0
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=92|p.92]]
>
> Table 10-54: L2 data RAM format for Data Register 0；Table 10-55: L2 data RAM format for Data Register 1；Table 10-56: L2 data RAM format for Data Register 2；Table 10-57: L2 TLB format for Instruction Register 0
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0092-original.png]]

> [!quote]- 原文第93页：Table 10-58: L2 TLB format for Instruction Register 1
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=93|p.93]]
>
> Table 10-58: L2 TLB format for Instruction Register 1
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0093-original.png]]

> [!quote]- 原文第94页：Table 10-59: L2 TLB format for Instruction Register 2
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=94|p.94]]
>
> Table 10-59: L2 TLB format for Instruction Register 2
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0094-original.png]]

> [!quote]- 原文第95页：Table 10-60: Neoverse™ N2 L2 victim format for data register 0；Table 10-61: Neoverse™ N2 L2 victim format for data register 1；Table 10-62: Neoverse™ N2 L2 victim format for data register 2
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=95|p.95]]
>
> Table 10-60: Neoverse™ N2 L2 victim format for data register 0；Table 10-61: Neoverse™ N2 L2 victim format for data register 1；Table 10-62: Neoverse™ N2 L2 victim format for data register 2
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0095-original.png]]


## 第11章 RAS与错误处理

**原文范围：p.96-100，§11.1-11.6。** RAS 关注 Reliability、Availability、Serviceability，即可靠性、可用性与可维护性。N2 的 Node 0 包含本核私有 L1/L2 memory systems；这个 RAS node 编号不是 CHI NodeID。

### 11.1 为什么dirty数据用ECC，clean结构可用parity

| 保护方式 | 能力 | N2 中的典型结构 |
|---|---|---|
| SED parity | 检测单 bit 错误；不能保证检测同保护粒度双 bit 错误 | I-cache、MOP、MMUTC |
| SECDED ECC | 单 bit 纠正、双 bit 检测 | D-cache tag/data、L2 tag/data、TQ |

原表 Table 11-1，p.97：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0097-original.png]]

**理解说明**：仅存 clean 内容的结构通常能从可信下游重新取得信息；dirty line 可能是最新数据的唯一副本，不能简单丢弃。因此保护需求不同。但 ECC 不等于自动修复任意多 bit 错误，双 bit 检测也不等于双 bit 纠正。

手册保证单 bit 错误时可继续保持正确；多个不同保护粒度中的单 bit 错误也可处理。同一粒度双 bit 错误则依赖 RAM 类别，dirty 数据可能丢失；三 bit 及以上错误是否能检测不能一概保证。

### 11.2 Poison、containment与异常

Detected data error 可用 poison 随数据传播，让消费者识别，避免静默使用。带双 bit 错误的数据 eviction 也可附带 poison。**不可纠正的 L1 D-cache/L2 tag 错误不能 containment**，因为地址和状态信息本身已不可靠。

ESB（Error Synchronization Barrier）让前序相关 SError 被处理或挂入 `DISR_EL1`，有助于界定异步错误范围；它不是一条“修复 ECC”的指令。

### 11.3 Fault报告与错误被消费要分开

| 机制 | 关注点 |
|---|---|
| FHI，Fault Handling Interrupt | 按 FI/CFI 条件报告 deferred、uncorrected、corrected 或计数溢出等 |
| ERI，Error Recovery Interrupt | 按 UI 条件报告未 deferred 的 uncorrected error |
| SEA / AEA | 数据被访问或消费时产生同步/异步 external abort |
| Error record | FR 能力、CTLR 控制、STATUS 状态、ADDR/MISC 定位与计数 |

发现错误、记录错误、发出中断以及软件消费 poisoned data 的时刻可能不同，不能把一次 ECC 检测固定解释为一次立即 Data Abort。

### 11.4 错误注入与验证

支持 corrected、deferred、uncontainable 的伪错误注入，可立即或由 32 位倒计时触发。它用于验证错误处理软件，**不是真正在 RAM bitcell 中制造物理故障**。

**教学示例**：先准备 RAS handler 和记录读取路径，再用 corrected error 注入检查状态、中断与清除流程；不能用一次 corrected 注入通过来证明双 bit tag 错误恢复也正确。

所有检测到的 ECC/parity 错误可触发 PMU `MEMORY_ERROR`，前提是选择并使能对应计数器；Secure 计数另受 `MDCR_EL3.SPME` 等条件约束。RAS 与掉电流程的关联见 [[#第5章 电源管理]]。

原表 Table 11-2 的 RAS 寄存器总表和完整位图入口：[[#图表 第11章]]、[[#寄存器 B14 RAS寄存器]]。

### 11.5 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第100页：Table 11-2: RAS registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=100|p.100]]
>
> Table 11-2: RAS registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0100-original.png]]


## 第12章 GIC CPU接口

**原文范围：p.101-104，§12.1-12.2。** 本核实现 GICv4.1 CPU interface，接外部 distributor，提供中断屏蔽、识别、优先级、应答及虚拟化相关控制。

### 12.1 支持哪些中断能力

包括两种安全状态、Secure virtualization、SGI、message-based interrupts、system register access、优先级与屏蔽、唤醒事件。Group 0 总是 Secure，通过 FIQ；Group 1 可 Secure/Non-secure，经规则选择 IRQ/FIQ。

**理解说明**：CPU interface 决定“当前 PE 接受和处理哪个中断”，外部 GIC 组件还负责分发、路由和中断源状态。GIC CPU interface 不等于整套 GIC 都在 CPU 核中。

### 12.2 典型处理过程

**教学流程**：外部中断到达 → CPU 侧按 group enable 和 priority mask 判断可否呈现 → 软件读相应 IAR 确认中断 → handler 处理设备 → 写 EOIR，必要时按 EOImode 做 deactivation。优先级降低与 active 状态清除不能永远视为同一个步骤，精确流程查 GIC 架构。

虚拟化中 `ICV_*` 是虚拟 CPU 接口视图，`ICH_*` 面向 hypervisor，如 list registers；它们与物理 `ICC_*` 不能混用。寄存器名后的 EL 不表示低 EL 无条件可访问。

### 12.3 禁用集成接口的条件

复位时将 `GICCDISABLE` 拉高可禁用；系统没有符合要求的外部 GIC distributor（至少 GICv3）时，需要禁用这个接口。禁用后外部 GIC 可驱动 nIRQ/nFIQ/nVIRQ/nVFIQ，而 GIC system register access 产生 Undefined Instruction。

启用时，nVIRQ/nVFIQ 应绑高，因为虚拟中断由 CPU interface 自身生成；nIRQ/nFIQ 的处理条件不同，不能全部照搬绑高。

原表 Table 12-1 跨 p.102-104，全部保留于 [[#图表 第12章]]。

### 12.4 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第102页：Table 12-1: GIC system registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=102|p.102]]
>
> Table 12-1: GIC system registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0102-original.png]]

> [!quote]- 原文第103页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=103|p.103]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0103-original.png]]

> [!quote]- 原文第104页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=104|p.104]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0104-original.png]]


## 第13章 Advanced SIMD与浮点

**原文范围：p.105。** N2 支持 A32/T32/A64 中的 Advanced SIMD 与标量浮点，硬件实现标量操作，支持 rounding modes、flush-to-zero、default NaN 等组合；本章说明不支持 floating-point exception trapping。

### 13.1 SIMD与标量的差别

标量加法处理一对数；SIMD 把多个元素打包，在一次向量操作中分别处理。**教学示例**：一个 128-bit 向量可放 4 个 32-bit 元素，向量加法得到 4 个独立和，而不是把它当成一个 128-bit 整数相加。

```text
[1, 2, 3, 4] + [10, 20, 30, 40] → [11, 22, 33, 44]
```

### 13.2 浮点控制为何影响结果

Rounding mode 决定不可精确表示结果怎样舍入；flush-to-zero 和 default NaN 影响特殊值处理。AArch64 中 FPCR 负责控制，FPSR 记录状态；AArch32 的 FPSCR 综合这些职能。

“不支持异常 trapping”不是“没有浮点异常状态”，也不代表除零、NaN 等行为被忽略。算法对特殊值、舍入和跨平台可重复性的需求必须按架构设置核对。

本章没有给出各指令的 latency/throughput，不从“硬件实现”推断固定单周期；性能参数应查匹配修订的 Software Optimization Guide。

## 第14章 SVE与SVE2

**原文范围：p.106。** N2 支持 SVE/SVE2，**实现的 vector length 为 128 bits**；两者补充而不替代 AArch64 Advanced SIMD/FPU。

### 14.1 Scalable不代表N2任意变宽

SVE 的可扩展性体现在架构与软件模型，可写与向量长度无关的代码；N2 这款实现仍是 128-bit，不应据 scalable 推断 N2 有 256/512-bit 向量硬件。SVE 仅在 AArch64，AArch32 应用不能因此获得 SVE 指令执行能力。

### 14.2 Predicate帮助处理尾部元素

**教学示例**：对 10 个 32-bit 元素做运算，128-bit 一组有 4 个元素。前两组处理 8 个；最后一组用 predicate 只使能剩下 2 个 lane。Predicate 表达哪些元素有效，避免把数组外的元素当成合法运算对象，具体 load 和故障规则仍由指令语义决定。

SVE2 提供更多数据处理指令能力；不能因为 SVE 支持就推定所有可选 SVE 扩展也支持。与 BF16/I8MM、Crypto 等的组合应逐项核对第 2 章能力表和 ID 寄存器。

本章没有公开全部向量流水线宽度、执行端口、吞吐和 lane 内部划分，不能由 128-bit vector length 反推这些实现参数。

## 第15章 系统控制与能力发现

**原文范围：p.107-108，§15.1。** 系统寄存器管理 PMU、cache、MMU、GIC 和整体运行状态；有些还可经 external debug/utility bus 访问。

### 15.1 先读能力，再配置行为

| 目标 | 代表性寄存器 | 理解重点 |
|---|---|---|
| 识别核及修订 | MIDR_EL1、REVIDR_EL1 | 核类型与版本，不是运行频率 |
| 识别拓扑/亲和性 | MPIDR_EL1 | Affinity，不是 CHI TxnID |
| 识别指令/内存能力 | ID_AA64ISAR*、ID_AA64MMFR*、ID_AA64PFR*、ID_AA64ZFR0_EL1 | 是否存在相关架构功能 |
| 缓存几何 | CLIDR、CSSELR、CCSIDR、CTR | Cache 层次、尺寸、line 和一致性相关能力 |
| DC ZVA | DCZID_EL0 | 清零块大小与禁止条件 |
| N2 配置 | IMP_CPUCFR_EL1 | 实现相关配置，具体位域回查 |

**教学示例**：做缓存 set/way 操作前，按 CLIDR/CSSELR/CCSIDR 识别实际几何，不能在通用代码中硬编码“所有 CPU 都是同样 1MB L2”。使用 SVE、RNG、Crypto 也应检测实际平台能力。

### 15.2 “寄存器存在”不等于“应用可直接访问”

MRS/MSR 的可访问性由当前 EL、安全状态、trap control、debug 条件等共同决定。低 EL 执行可能 trap 到 EL2/EL3，或者 UNDEFINED；有些访问视图会重定向到虚拟寄存器。访问伪代码在附录，不应只看名字和编码总表。

原表 Table 15-1 跨 p.107-108，见 [[#图表 第15章]]。

### 15.3 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第107页：Table 15-1: Identification registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=107|p.107]]
>
> Table 15-1: Identification registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0107-original.png]]

> [!quote]- 原文第108页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=108|p.108]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0108-original.png]]


## 第16章 随机数指令与外部RNG

**原文范围：p.109-110，§16.1。** 随机数指令可选，N2 期待系统提供符合要求的 **memory-mapped TRNG 与 DRBG 外设**，不是在本核内部自动产生全部熵。

### 16.1 RNDR与RNDRRS

```asm
MRS Xn, RNDR
MRS Xn, RNDRRS
```

两者返回 64-bit random number。RNDRRS 请求按架构要求从 TRNG 为 DRBG reseed；系统需提供带宽、延迟与 QoS 保障，必要时部署多个 RNG 实例。

### 16.2 请求地址如何构造

```text
RNDR   = {CPURNDBR_EL3[47:16], CPURNDPEID_EL3[10:0], 0, 0000}
RNDRRS = {CPURNDBR_EL3[47:16], CPURNDPEID_EL3[10:0], 1, 0000}
```

基地址按 64KB 页配置，地址 [15:5] 标识 PE，[4] 区分 RNDR/RNDRRS。核通过 Device-nGnRnE 的成对读取取回结果。

**教学计算**：若基地址为 `0x80000000`，PEID=3，则 RNDR 地址为 `0x80000060`，RNDRRS 为 `0x80000070`。这仅用于解释拼接，实际地址由 SoC 集成者配置。

外设成功返回时，第一个 64-bit 是随机数，第二个 64-bit 为 1；超出实现规定时间无法提供时，两者为 0。**随机数值本身为 0 不等于失败**，应依据成功状态判断。总线错误导致请求失败，核设置 PSTATE.Z 并发出 SEI。

### 16.3 集成与验证重点

必须核对外设支持、基地址、PEID、Secure/Non-secure 属性、QoS 和失败路径。不能只看到 RNDR instruction supported 就声称随机服务可用。原文给出 SBSA ACS/NIST 测试入口，测试统计性质不能代替整个熵源设计审查。

原表 Table 16-1 与 B.3 的基地址/PEID 原位图入口：[[#图表 第16章]]、[[Neoverse/01_assets/N2-Core-TRM-r0p3/p0454-original.png|原文第454页截图]]、[[Neoverse/01_assets/N2-Core-TRM-r0p3/p0455-original.png|原文第455页截图]]。

### 16.4 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第110页：Table 16-1: Random Number Control registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=110|p.110]]
>
> Table 16-1: Random Number Control registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0110-original.png]]


## 第17章 调试系统

**原文范围：p.111-121，§17.1-17.10。** 调试分 self-hosted 与 external；DSU DebugBlock 单独供电，使核或 cluster 掉电后仍可保持连接。

### 17.1 调试组件如何连接

DebugBlock 与 cluster 之间通过双向 APB 接口传递多数调试访问和 CTI trigger；每核 trace unit 输出经 funnel 汇聚到 ATB。每核 CTI 位于 DebugBlock，CTM 连接触发网络。

原图 Figure 17-1，p.111：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0111-original.png]]

**读图边界**：这是通用 DynamIQ 组织图，画出了 SCU、L3、snoop filter；N2 的 Direct connect 配置不能据此增加这些实际组件。

原图 Figure 17-2，p.112 的外部调试链路见 [[#图表 第17章]]。Debug host 发高层命令，协议转换设备连接目标 SoC，再通过 CoreSight 访问指定核。Self-hosted debug 则由目标核上的 monitor 软件处理，不必依赖另一台主机。

### 17.2 访问路径并不相同

| 功能 | 核内system register | 外部memory-mapped接口 |
|---|---|---|
| Debug / PMU / trace | 支持相应寄存器 | DebugBlock APB |
| SPE | System registers | 本章未列外部 APB 编程接口 |
| ELA | 非本章的 system register 路径 | APB memory-mapped |
| AMU | System registers | Utility bus 的只读计数器访问，见第 21 章 |

外部访问受核供电、OS Lock、外部认证等条件控制。Cold reset 设置 Debug OS Lock，需要按规则清除才能正常调试；有 APB 地址不等于读写必成功。

### 17.3 Breakpoint和watchpoint

N2 支持 **6 个 breakpoint、4 个 watchpoint**。BRP0-3 只做 VA 匹配；BRP4/5 可匹配 VA、Context ID 或 VMID。Watchpoint 可链接 BRP4/5，限制为特定进程/虚拟机上下文。

**教学示例**：某个进程偶尔改坏 `buffer[0]`，设置数据 watchpoint 比只在函数入口设 breakpoint 更能定位实际写入指令；如多个进程共享同 VA，要结合 context 条件，避免抓到别的地址空间。

Watchpoint event 在 N2 中总是 synchronous。但 prefetch/cache hint、部分 CMO 不生成 watchpoint；Store-exclusive 即使失败、CAS 即使比较失败，也可生成 watchpoint。**没有成功写入，不等于一定没有 debug event。** 精确排除列表见 p.115。

### 17.4 ROM table与CoreSight ID

每核 ROM table 给出 core debug、PMU、trace、可选 ELA 的发现入口；DSU 另有 cluster 与 DebugBlock ROM tables。ROM table 是调试组件目录，不是程序启动 ROM 或指令缓存。

Table 17-3 给出 r0p3 的 component ID/peripheral ID/DevArch 等；工具识别需要核对版本。CTI 位于 DSU DebugBlock，相关信号/映射不能仅由本核 TRM 决定。

全部原图、访问条件表、ROM 表和寄存器总表已保留于 [[#图表 第17章]]。

### 17.5 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第112页：Figure 17-2: External debug system
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=112|p.112]]
>
> Figure 17-2: External debug system
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0112-original.png]]

> [!quote]- 原文第115页：Table 17-1: External access conditions to registers
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=115|p.115]]
>
> Table 17-1: External access conditions to registers
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0115-original.png]]

> [!quote]- 原文第116页：Table 17-2: Core ROM table；Table 17-3: Neoverse™ N2 CoreSight component identification
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=116|p.116]]
>
> Table 17-2: Core ROM table；Table 17-3: Neoverse™ N2 CoreSight component identification
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0116-original.png]]

> [!quote]- 原文第117页：Table 17-4: Core CTI register peripheral ID values；Table 17-5: Debug registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=117|p.117]]
>
> Table 17-4: Core CTI register peripheral ID values；Table 17-5: Debug registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0117-original.png]]

> [!quote]- 原文第118页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=118|p.118]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0118-original.png]]

> [!quote]- 原文第119页：Table 17-6: Debug registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=119|p.119]]
>
> Table 17-6: Debug registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0119-original.png]]

> [!quote]- 原文第120页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=120|p.120]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0120-original.png]]

> [!quote]- 原文第121页：Table 17-7: CoreROM registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=121|p.121]]
>
> Table 17-7: CoreROM registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0121-original.png]]


## 第18章 PMU性能监测

**原文范围：p.122-136，§18.1-18.5。** PMU 从其他功能单元收集事件，提供 6 个可配置 64-bit event counters、周期计数、上下文采样快照和溢出中断。可通过 system registers 或外部 Debug APB 编程。

### 18.1 事件名不能代替事件定义

| 编号 | 事件 | 重要计数口径 |
|---|---|---|
| 0x08 | INST_RETIRED | 退休的体系结构指令，包括条件判断不通过的指令 |
| 0x11 | CPU_CYCLES | 核周期；此事件不导出给 trace |
| 0x03 / 0x04 | L1D_CACHE_REFILL / L1D_CACHE | 可包括 load/store 和 table walk，排除项需查原定义 |
| 0x14 | L1I_CACHE | I-cache **或 MOP cache** 的取指访问，不能当成纯 I-cache access |
| 0x16 / 0x17 | L2D_CACHE / L2D_CACHE_REFILL | 来自本核上层的相应 lookup/refill；外部 snoop 等有排除条件 |
| 0x19 | BUS_ACCESS | 按数据传输 beat 计数，不按一整个 CHI transaction 计数 |
| 0x21 / 0x22 | BR_RETIRED / BR_MIS_PRED_RETIRED | 退休分支与导致相应 flush 的预测错误分支 |
| 0x23 / 0x24 | STALL_FRONTEND / STALL_BACKEND | 按事件定义计没有 fetched instruction 或资源阻塞的周期 |
| 0x3A / 0x3B | OP_RETIRED / OP_SPEC | micro-operation，不是体系结构指令 |
| 0x36 / 0x37 | LL_CACHE_RD / LL_CACHE_MISS_RD | 受 CPUECTLR.EXTLLC 与系统实现影响 |
| 0x4000-0x4003 | SAMPLE_* | SPE population、采样、过滤和 collision 统计 |
| 0x8006、0x8074 等 | SVE_* | SVE operation、predicate 等行为 |

原始 **Table 18-1，p.122-132** 的整张事件表及全部续页：[[#图表 第18章]]。

### 18.2 教学例子：CPI与事件比率

假设同一段测量窗口中：退休指令 100 万，核周期 200 万，则 CPI=2，IPC=0.5。这是平均吞吐表现，**不是每条指令都耗时两周期**，乱序与并行使单条 latency 和整体 CPI 不同。

若同窗 L1D_CACHE=10 万，L1D_CACHE_REFILL=2 万，可以按这一计数口径计算 20% 的 refill/access 比例。但它不是自动等于“应用 load 的精确 miss rate”，因为分母/分子可包含 table walk 等，且都有排除项。

**教学例子**：软件 `store` 可能触发 ReadUnique；PMU 某些事务事件按 CHI read transaction 计数。因此“read 事件增长”并不证明源代码执行了同样数量的 load。

### 18.3 Bus、LLC与时钟的三个陷阱

1. `BUS_ACCESS` 是 data beat；完整 64B 数据通常涉及两个 256-bit beat，不应与事务总数直接比较。请求、响应头等也不属于这份数据量计数。
2. 名为 L3/SCU 的事件描述反映数据来源与系统语境，不能据事件名字推定 N2 Direct connect 自带集群 L3。
3. CPU_CYCLES 和 constant-frequency cycles 不同；DVFS 会改变核周期对应的时间，比较性能需要同时明确测量窗口、频率和运行状态。

### 18.4 中断、权限与测量质量

计数器溢出可触发低有效 `nPMUIRQ[n]`。外部访问受供电、OS Lock、External Performance Monitors Access Disable 等限制。短窗口容易受 pipeline effects 影响；事件虽可统计，也必须选择并使能计数器。

6 个事件计数器不意味着只能分析 6 种事件；可分多轮测量，但不同轮负载变化及复用会带来可比性问题。PMU 总量分析之后，可用 SPE 把事件关联到具体被采样操作，或用 trace 看控制流。

### 18.5 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第122页：Table 18-1: Performance monitors Events
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=122|p.122]]
>
> Table 18-1: Performance monitors Events
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0122-original.png]]

> [!quote]- 原文第123页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=123|p.123]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0123-original.png]]

> [!quote]- 原文第124页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=124|p.124]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0124-original.png]]

> [!quote]- 原文第125页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=125|p.125]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0125-original.png]]

> [!quote]- 原文第126页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=126|p.126]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0126-original.png]]

> [!quote]- 原文第127页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=127|p.127]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0127-original.png]]

> [!quote]- 原文第128页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=128|p.128]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0128-original.png]]

> [!quote]- 原文第129页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=129|p.129]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0129-original.png]]

> [!quote]- 原文第130页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=130|p.130]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0130-original.png]]

> [!quote]- 原文第131页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=131|p.131]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0131-original.png]]

> [!quote]- 原文第132页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=132|p.132]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0132-original.png]]

> [!quote]- 原文第133页：Table 18-2: Performance Monitors registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=133|p.133]]
>
> Table 18-2: Performance Monitors registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0133-original.png]]

> [!quote]- 原文第134页：Table 18-3: Performance Monitors registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=134|p.134]]
>
> Table 18-3: Performance Monitors registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0134-original.png]]

> [!quote]- 原文第135页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=135|p.135]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0135-original.png]]

> [!quote]- 原文第136页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=136|p.136]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0136-original.png]]


## 第19章 ETE指令流追踪

**原文范围：p.137-149，§19.1-19.9。** Embedded Trace Extension 生成实时、压缩的程序流追踪；N2 ETE **不实现 data tracing**。

### 19.1 四个主要部分

原图 Figure 19-1，p.137：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0137-original.png]]

| 部分 | 作用 |
|---|---|
| Core interface | 按程序顺序提供分支、异常等 P0 elements |
| Trace generation | 将这些元素编码为 trace packets |
| Filtering / triggering | 限定地址范围、上下文和触发条件，控制输出量 |
| FIFO / trace out | 平滑突发，经 ATB 或 trace buffer 输出 |

FIFO 满时发生 overflow，生成逻辑暂停新 trace 直至 FIFO 排空，导致 debugger 看到追踪缺口。不能假定追踪永远连续完整，也不能把缺口解释成程序停止执行。

### 19.2 N2实现的资源与限制

Table 19-1 给出：8 对 resource selection、4 个 external input selectors、4 个 ETE events、2 个 counters、4 个 sequencer states、1 个 VMID comparator、1 个 Context ID comparator、4 对地址 comparator；不实现 data address/data value comparators。

Table 19-2 给出：8-byte 指令地址、4-byte VMID/Context ID、7-bit Trace ID、64-bit global timestamp；支持 instruction cycle counting、branch broadcast、return stack、SError tracing。不支持 data tracing、load/store 作为 P0 tracing、stall control、overflow avoidance 和低功耗 override。Cycle-counting minimum threshold 为 4。

**教学示例**：异常偶现时，trace 可帮助理解程序从函数 A 进入 B，经哪个分支到故障处理入口；却不能据 N2 的 instruction flow trace 得到“每次 LDR 读到了哪些数据值”。数据来源/地址统计更适合 SPE 或其他观测机制。

### 19.3 两种编程路径的顺序

APB 路径：关闭 `TRCPRGCTLR.EN` → 轮询 `TRCSTATR.Idle=1` → 配好所有相关寄存器 → 开 EN → 轮询 Idle=0。

原图 Figure 19-2，p.141：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0141-original.png]]

System register 路径：EN=0 → ISB → TSB → 配寄存器 → EN=1 → ISB。

原图 Figure 19-3，p.142：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0142-original.png]]

先整体停用再配置，目的是避免部分设置先开始计数/触发，而其他条件还没建立。不能把两个接口的轮询和屏障流程随意交换。

### 19.4 PMU、复位与追踪

4 个扩展输入选择器可独立选择 PMU events，按事件发生周期提供给 trace 条件。Tables 19-3 另列 PMU overflow、TRB trigger 等事件。

Warm reset 可能缺少复位前最后几条指令的 trace；TRBE 在 Warm reset 被禁用，不能用它保证捕获暖复位过程。Trace unit 被 reset 后需重新配置并使能。

全部资源/能力原表、流程图、总表和续页见 [[#图表 第19章]]。

### 19.5 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第138页：Table 19-1: Trace unit resources
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=138|p.138]]
>
> Table 19-1: Trace unit resources
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0138-original.png]]

> [!quote]- 原文第139页：Table 19-2: Trace unit generation options
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=139|p.139]]
>
> Table 19-2: Trace unit generation options
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0139-original.png]]

> [!quote]- 原文第143页：Table 19-3: ETE events；Table 19-4: Trace unit registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=143|p.143]]
>
> Table 19-3: ETE events；Table 19-4: Trace unit registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0143-original.png]]

> [!quote]- 原文第144页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=144|p.144]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0144-original.png]]

> [!quote]- 原文第145页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=145|p.145]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0145-original.png]]

> [!quote]- 原文第146页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=146|p.146]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0146-original.png]]

> [!quote]- 原文第147页：Table 19-5: Trace unit registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=147|p.147]]
>
> Table 19-5: Trace unit registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0147-original.png]]

> [!quote]- 原文第148页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=148|p.148]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0148-original.png]]

> [!quote]- 原文第149页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=149|p.149]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0149-original.png]]


## 第20章 TRBE追踪缓冲

**原文范围：p.150，§20.1-20.2。** TRace Buffer Extension 接受 ETE 生成的 program-flow trace，并直接写向内存系统；它是保存追踪流的机制，不是另一种指令流生成器。

### 20.1 Accept、discard、reject的区别

| 行为 | 后果 |
|---|---|
| Accept | 接收 trace，向 L2 memory system 写入 |
| Discard | 丢弃 trace，这部分数据永久丢失 |
| Reject | 暂时不接收，trace unit 保留待接收数据 |
| TRBE disabled | 忽略本缓冲路径，trace unit 向 ATB 输出 |

Reject 与 discard 不同，但上游 FIFO 有限，因此 reject 也不能无限期保证无丢失；应结合 ETE overflow 行为理解整个缓冲链。

### 20.2 配置与地址

通过 system registers 配置，`TRBLIMITR_EL1.E` 控制使能；需整体完成设置后启用。Base、pointer、limit、memory attributes、status、trigger 等寄存器见 B.16，p.1130 的 Table B-739。

原表 Table B-739：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1130-original.png]]

**教学示例**：追踪程序一段执行路径，ETE 负责产生压缩流，TRBE 把它写入指定 buffer，软件/工具之后解码。Buffer 可写、地址转换、边界和异常处理属于使能前必须成立的条件，不能只打开 E 位就假定可靠记录。

## 第21章 AMU活动监测

**原文范围：p.151-155，§21.1-21.5。** Activity Monitors 更偏向系统管理、功耗策略和持续监测；PMU 更偏向应用性能分析和调试。

### 21.1 实际计数内容

N2 实现 7 个 64-bit wrapping counters：Group 0 四项，Group 1 三项。

| Counter | 事件 | 作用 |
|---|---|---|
| AMEVCNTR00 | CPU_CYCLES，0x0011 | 核频率周期 |
| AMEVCNTR01 | CNT_CYCLES，0x4004 | 恒定频率周期 |
| AMEVCNTR02 | Instructions retired，0x0008 | 架构执行的指令，包括条件不通过的指令 |
| AMEVCNTR03 | STALL_BACKEND_MEM，0x4005 | 核内末级缓存 miss 导致前端无法向后端派发的周期 |
| AMEVCNTR10-12 | Reserved，0x0300-0x0302 | 原表未定义可用业务事件，不自行补充 |

原表 Table 21-1，p.152：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0152-original.png]]

Counter wrap 不产生 overflow status 或 interrupt；Cold reset 清零。频率变化与 WFI/WFE 停钟可影响计数，要比较同一有定义的窗口。

### 21.2 访问与配置

最高已实现 EL 配置主要控制和计数值；运行中主要用读访问。System register 的低 EL 权限还受 AMUSERENR、CPTR_EL2.TAM、CPTR_EL3.TAM 等限制。Utility bus 只提供相应计数器的只读 memory-mapped 访问，基地址为 `0x<n>90000`，n 表示 DSU 内核实例。

### 21.3 管理例子

**教学示例**：同样的工作量，若退休指令变化小而 memory stall cycles 很高，单纯提高核心频率可能收益有限。系统管理软件可结合核周期、恒定频率周期、退休指令和内存阻塞信息评估策略，但要考虑时钟停止、窗口与其他系统瓶颈，不能只用一比值推断完整功耗。

**待确认**：§21.3 引言写 events “fixed or programmable”，但正文与 Table 21-1 将 N2 事件定义为 fixed，辅助三项为 Reserved。本文按具体计数器说明，不把它当成 7 个任意可编程 PMU counters。

### 21.4 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第153页：Table 21-2: Activity Monitors registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=153|p.153]]
>
> Table 21-2: Activity Monitors registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0153-original.png]]

> [!quote]- 原文第154页：Table 21-3: Activity Monitors registers summary
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=154|p.154]]
>
> Table 21-3: Activity Monitors registers summary
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0154-original.png]]

> [!quote]- 原文第155页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=155|p.155]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0155-original.png]]


## 第22章 SPE统计采样

**原文范围：p.156-159，§22.1-22.4；补充位域依据 B.15，p.1114-1129。** Statistical Profiling Extension **抽样跟踪执行中的微操作**，写出样本，再由工具聚合分析。

### 22.1 N2抽样的是micro-operation

原图 Figure 22-1，p.156：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0156-original.png]]

倒计数器按已派发的 speculative micro-operations 递减，归零选择一个；在该微操作生命周期中收集信息，相关指令 retired/aborted/flushed 后写记录。因此采样可覆盖后来被冲刷的操作，不能把所有样本当成已退休指令。

MOP cache 保存已译码表示，SPE 则观察被选中的执行实例；Macro-operation 与 micro-operation 的具体拆分不能假定一一对应。

记录通过 VA 写入 memory buffer，写入本身需要 MMU 转换与内存访问。采样通常扰动较小，但过密会增加开销。N2 建议最小间隔为 **1024 个微操作**；不是每 1024 条 retired instructions，也不是固定 1024 个 cycles。

### 22.2 N2样本中的事件

| 事件位 | 含义或注意 |
|---|---|
| 0 / 1 | Generated exception / Architecturally retired |
| 2 / 3 | L1 data cache access / refill |
| 4 / 5 | TLB access / 页表遍历相关事件；位 5 名称见下方口径说明 |
| 6 / 7 | Not taken / Branch mispredicted |
| 8 / 9 | Last-level cache access / miss |
| 10 / 11 / 12 | Remote access / Data alignment flag / Late prefetch |
| 17 / 18 | Partial predicate / Empty predicate |

原表 Table 22-1，p.157：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0157-original.png]]

**原文口径说明**：Table 22-1 对 bit 5 只写 “L1 data cache Translation Lookaside Buffer (TLB)”，未明确动作；B.15.1 的 E[5] 在 p.1115、1124 明确称为 TLB walk。本文据附录解释这一位，保留主表措辞疑点供回查，不直接当成任意 L1 TLB miss。

### 22.3 数据来源能定位到哪一层

| 编码 | 数据来源 |
|---|---|
| 0x0 | L1 data cache |
| 0x8 | L2 cache |
| 0x9 | Peer core |
| 0xA | Local cluster |
| 0xB | System cache |
| 0xC | Peer cluster |
| 0xD | Remote |
| 0xE | DRAM |

原表 Table 22-2，p.158：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0158-original.png]]

这些是分类，不是 CHI NodeID。Peer core 不标识具体 RN；Local cluster/Peer cluster/Remote 的实际拓扑意义需结合集成。编码存在也不意味着当前系统必然包含每种来源。

### 22.4 Load样本的具体例子

```asm
0x4000: LDR X0, [X0, #8]    // 例如读取链表的 next 指针
```

分析工具解码后的样本可示意为：

```text
PC：0x4000
操作：Load
数据地址：0x90000008
L1 data access：1
L1 data refill：1
Last-level cache miss：1
Data source：DRAM
Total latency：180 cycles
Architecturally retired：1
```

这是**教学样本**，不是原始 packet 格式，地址和 180 cycles 都是假设。N2 的 ID 寄存器支持微操作采样、loaded data source、按类型/事件/延迟过滤；SPE 架构中的地址和 latency packet 定义应查 Arm ARM。Total latency 的范围不能直接当成 DDR 设备本身响应时间。

若在相同过滤条件下，这条 load 的 1000 份样本中 700 份来自 DRAM，就可怀疑其局部性较差，结合链表布局排查。**70% 是这组样本的来源比例，不是全部程序读写的精确 DRAM 比率**。被记录数据也不包括这次 LDR 实际读到的业务数据值。

### 22.5 Branch样本与数据共享例子

条件分支 `B.NE` 的 sample 若带 bit7=1，可将 misprediction 关联到对应 PC；大量样本集中到同一分支，就能检查条件变化和布局。

同一 load 的另一份 sample 若 Data source=Peer core，可以研究共享数据访问。但单个样本不能证明 false sharing，更不能还原 RetToSrc、forwarding、CompAck 等完整 CHI 交换。需要访问地址、缓存行分布、线程行为及更多证据一起判断。

### 22.6 过滤、记录尺寸和饱和

`PMSIDR_EL1` 在本版给出：ArchInst=0（micro-op sampling）、LDS=1、FL/FT/FE 支持；CountSize 为 12-bit saturating，MaxSize 为 64B，Interval 推荐 1024。`PMBIDR_EL1` 规定 pointer 最小对齐为 64B；不能忽略 buffer 权限和边界。

Event filter 是 **AND** 条件。比如 E[3]=1 且 E[5]=1，只保留同时具有 L1 data/unified refill 与 TLB walk 的样本，不是二者满足任一即可。

采样倒计数和随后过滤要分开理解：并不是先找出“所有 cache miss”，再每隔 N 个 miss 采样。原记录会受过滤、collision、缓冲写入及观测窗口影响，不能把 sample count 简单乘 interval 当成无偏精确总量。

### 22.7 PMU、SPE、ETE、AMU的选择

| 想知道的事 | 更适合的机制 |
|---|---|
| 总共多少 cache refill、branch miss、cycles | PMU，注意每个事件口径 |
| 哪条被采样 load 很慢、数据来自哪里 | SPE |
| 运行时经哪些分支/异常走到这里 | ETE，必要时由 TRBE 保存 |
| 系统长期运行、频率和内存阻塞的管理信息 | AMU |

全部原流程、事件/数据来源总表与 register summary：[[#图表 第22章]]。PMSIDR/PMBIDR 原位图与对应表见 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1126-original.png|原文第1126页截图]] 至 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1129-original.png|原文第1129页截图]]。

### 22.8 原图表补充（按需展开）

以下保留本章其余原图表与跨页续表，按需展开查看。

> [!quote]- 原文第159页：续表或相关原文
> [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=159|p.159]]
>
> 续表或相关原文
>
> ![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0159-original.png]]


## 附录A AArch32寄存器

**原文范围：p.160-241，§A.1-A.7。** 这部分是 AArch32 视图的寄存器参考。N2 的 AArch32 仅用于 EL0，附录中架构寄存器的通用访问描述不能推导出 N2 支持 AArch32 EL1/EL2/EL3。原文明确说本手册不是完整架构寄存器清单，必须结合 Arm ARM。

| 分组 | 原文入口 | 理解重点 |
|---|---|---|
| A.1 Special-purpose | p.160 | DSPSR、DLR 是调试保存状态和链接信息 |
| A.2 Performance Monitors | p.160-206 | PMCR、计数器使能/溢出、事件选择、事件计数器及类型；是 PMU 的 AArch32 访问视图 |
| A.3 Generic Timer | p.207 | 区分物理/虚拟 count、compare value、timer value 和 control；部分寄存器为 64 位 |
| A.4 Debug | p.207 | DBGDSCRint、DBGDTRRXint、DBGDTRTXint，是内部调试状态与数据传递视图 |
| A.5 Generic System Control | p.208 | TPIDRURW、TPIDRURO 是软件线程标识，不是 CHI TxnID/NodeID |
| A.6 Floating Point | p.208-212 | FPSCR 同时包含控制字段与累计状态字段，部分位映射到 AArch64 FPSR |
| A.7 Activity Monitors | p.213-241 | AMU 的能力、使能、计数器及事件类型；实际实现数量应回到第21章 |

### A.1 两种访问视图不能当成两套硬件

例如 AArch32 的 FPSCR 与 AArch64 的 FPSR/FPCR 之间存在架构定义的映射。附录中的 `architecturally mapped` 描述用于理解状态之间的对应关系，不意味着可以在任意 EL、任意执行状态下直接访问另一视图。

PMU/AMU 同样要区分**寄存器名称、架构允许的编号范围与 N2 实际计数器数量**。N2 的 PMU 是 6 个事件计数器；不能看到模板化位域中出现更大的编号，就认为 N2 实现了更多计数器。

### A.2 如何读FPSCR

原位图 Figure A-13 与位域表 Table A-43，p.209：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0209-original.png]]

将字段分成四组理解：比较结果 NZCV、Advanced SIMD 累计饱和 QC、舍入/默认 NaN/flush-to-zero 等控制字段、浮点累计异常状态。第13章已说明 N2 不支持浮点异常 trapping；存在状态标志不等于该异常会引发 trap。清除/写入行为必须按对应字段定义，不能把整寄存器未知复位位直接当 0。

详细条目见 [[#寄存器 A2 PMU寄存器]]、[[#寄存器 A6 浮点寄存器]]。全部原位图、编码与续表见 [[#图表 附录A]]。

## 附录B AArch64寄存器

**原文范围：p.242-1130，§B.1-B.16。** 这是编写固件、虚拟化软件、性能工具和调试工具时最常回查的部分。每个展开条目通常包含作用、配置前提、访问属性、复位、位图、位域和访问伪代码。中文功能概括不能替代这些精确条件。

### B.1 功能分组与软件使用场景

| 分组 | 原文入口 | 用来解决的问题 |
|---|---|---|
| B.1 Generic System Control | p.242-350 | 页表和转换配置、内存属性、异常信息、Pointer Authentication、MTE，以及 N2 私有控制 |
| B.2 Debug | p.351-452 | 断点/观察点、调试锁、调试状态、寄存器传递和异常控制 |
| B.3 Random Number Control | p.453-456 | 配置外部 RNG 的基址、安全属性与 PEID；RNDR/RNDRRS 请求构造见第16章 |
| B.4 System instructions | p.456-457 | SYS_IMP_RAMINDEX：内部 RAM 的诊断读取接口，配合第10章 |
| B.5 Identification | p.458-555 | 读取架构能力、缓存属性、处理器身份；决定软件能否使用某项功能 |
| B.6 Special-purpose | p.556 | SPSR/ELR/SP 等保存状态、异常返回和栈指针，以及 DSPSR_EL0、DLR_EL0 调试视图 |
| B.7 Performance Monitors | p.556-632 | PMU 控制、过滤、计数器、事件类型、使能和溢出 |
| B.8 GIC system registers | p.633-778 | ICC 物理接口与 ICH 虚拟化接口，包括优先级、应答、EOI 与虚拟中断状态 |
| B.9 Generic Timer | p.779-780 | 各异常级的物理/虚拟 timer；count 和 compare/control 要分开 |
| B.10 Other system control | p.780-781 | SCTLR、CPACR、HCR、CPTR、ZCR 等控制和 trap 寄存器总表 |
| B.11 Activity Monitors | p.781-815 | AMU 能力、两组计数器和访问控制 |
| B.12 Trace unit | p.816-1047 | ETE 配置、资源选择、过滤、状态和组件识别 |
| B.13 MPAM | p.1048-1069 | 读取分区/监测能力并控制 PARTID/PMG 等分区信息 |
| B.14 RAS | p.1070-1113 | 选择错误记录、读取状态/地址/杂项信息、控制上报和注入 |
| B.15 SPE | p.1114-1129 | 采样间隔、事件/操作/延迟过滤、能力与采样缓冲控制 |
| B.16 TRBE | p.1130 | 追踪 buffer 的 base、limit、pointer、状态等寄存器总表 |

表中的“入口”按分组起止位置归纳；同一页可能同时包含上一组的末尾和下一组的开头。

### B.2 地址转换：基址、配置、属性、故障各司其职

`TTBR0_EL1/TTBR1_EL1` 指向 Stage 1 页表；`TCR_EL1` 控制地址转换相关参数；`MAIR_EL1` 提供属性编码。涉及虚拟化时，再看 `VTTBR_EL2/VTCR_EL2` 的 Stage 2 配置。`ESR_ELx/FAR_ELx` 是故障分析入口，不应拿页表基址寄存器代替 fault address。

理解说明：同一 VA 下出现 TLB miss、translation fault、permission fault 与 external abort，原因不同。先用第6章判断故障属于转换还是数据访问，再查相应寄存器字段。修改页表后是否需要 TLBI、屏障、怎样处理并发，是架构和软件协议问题；本摘要不提供可直接运行的通用页表更新代码。

MTE 的标签控制、种子等条目也在 B.1。标签相关配置不能代替常规地址转换/权限检查；需要同时核对 feature ID、页表属性和对应异常信息。

### B.3 N2私有控制必须与通用架构控制区分

`IMP_CPUACTLR_EL1`、`IMP_CPUECTLR_EL1` 等带 `IMP_` 的条目属于实现相关接口。前文的 write streaming、预取、电源相关设置要回查对应位域。不能把某一版 N2 的私有编码当作所有 Cortex/Neoverse 的通用设置，也不能仅根据 `_EL1` 后缀推定任何 EL1 软件都获准访问。

`SYS_IMP_RAMINDEX` 与第10章配合读取内部 RAM。它用于诊断与编码回查，不能借此向 MOP cache 写入“自定义指令”，也不能把原始 tag/data 位当成常规架构寄存器。

### B.4 能力发现先于功能使用

从 `MIDR_EL1/REVIDR_EL1` 确认实现身份和修订，再看 `ID_AA64*` 等 feature ID。缓存方面由 `CTR_EL0`、`CLIDR_EL1`、`CCSIDR_EL1` 等发现属性，按架构要求选择合法的 cache level/type。

例如 SVE 软件既要确认支持 SVE，也要读取/配置允许的 vector length；N2 128-bit 的实现上限见第14章，不能仅根据 SVE 架构允许更大的向量而假定这颗核实现了它。有关私有 L2 大小、可选 RNG/crypto/coherent I-cache，还需核对实际构建配置。

### B.5 GIC：读到中断编号之后还有状态转换

ICC 系列的 IAR/EOIR 等寄存器控制物理中断应答与优先级状态；虚拟化还需 ICH 系列维护虚拟中断的列表和控制状态。EOI 和 deactivate 是否合并受接口模式影响，不能把“写 EOIR”概括为所有情况下都彻底释放中断。对应行为见第12章与 B.8。

### B.6 MPAM：标识资源分区，不是直接配置核私有缓存容量

MPAM（Memory Partitioning and Monitoring）寄存器描述能力和分区/监测标识，如 PARTID、PMG，以及虚拟化相关控制。它们提供可随访问传播的资源管理信息；共享资源具体如何分配和监测，还要看系统中的接收组件及实现。

理解说明：把线程标记为不同 PARTID，与“把 N2 私有 L2 强制分成两块固定容量”不是同一个结论。不能只根据本附录推断整个 CMN/SLC 的容量分配策略。原总表与字段见 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1048-original.png|原文第1048页截图]] 起。

### B.7 RAS：选择记录之后才读状态与附加信息

先用 `ERRIDR_EL1` 理解记录能力，通过 `ERRSELR_EL1` 选择记录，再读取 `ERXFR_EL1` 的能力、`ERXSTATUS_EL1` 的状态，按有效位解释 `ERXADDR_EL1/ERXMISC*`。控制/注入类寄存器与读取报告不同，具体清除和写入语义需核对原位域。

不能把 UNKNOWN reset、地址无效或未实现字段解释成“无错误”。也不能根据一个 error status 就忽略第11章中的同步/异步异常、poison、FHI/ERI 与电源状态。对应条目见 [[#寄存器 B14 RAS寄存器]]。

### B.8 性能与追踪：按实现能力配置

PMU 的控制/事件类型/计数值对应第18章；ETE 配置对应第19章；AMU 对应第21章；SPE 对应第22章。名称相似的 buffer、counter、filter 不能互换。

SPE 先读 `PMSIDR_EL1/PMBIDR_EL1` 的能力和 buffer 要求，再理解 `PMSIRR_EL1`、`PMSEVFR_EL1`、`PMSLATFR_EL1` 等采样配置。TRBE 的 `TRBBASER_EL1/TRBLIMITR_EL1/TRBPTR_EL1` 记录 ETE 追踪缓冲；SPE 的 `PMB*` 是另一条数据记录路径。

### B.9 逐项条目的阅读顺序

1. 先看 Configurations：是否存在、依赖哪个 FEAT、是否当前执行状态可用。
2. 看 Attributes：宽度、RO/RW/WO 或各字段访问类型。
3. 看 Reset：`x`/UNKNOWN 与 0 不同；Cold/Warm reset 也可能不同。
4. 看 Bit descriptions：RES0/RES1、RAZ/WI、有效位、清除语义必须逐项遵守。
5. 最后看 Accessibility：当前 EL、安全状态、trap/锁等条件，不能只按寄存器名称后缀判断。

有些分组只有总表，没有在本手册内逐项展开。索引会明确标出，并指向原总表；没有的说明不会补写成 N2 的确定行为。入口：[[#寄存器回查索引]]；完整位图与续表：[[#图表 附录B]]。

## 附录C 外部寄存器

**原文范围：p.1131-1660，§C.1-C.7。** 外部寄存器是调试/系统侧通过 memory-mapped 接口看到的组件视图。原表的 Offset 通常是相应组件基址内的偏移，不能当作固定物理地址。

| 分组 | 原文入口 | 主要用途 |
|---|---|---|
| C.1 CoreROM | p.1131-1150 | 发现组件、核对 ROM entry 与组件识别信息 |
| C.2 PPM | p.1151-1156 | Power/Performance Management 寄存器；本版条目 RO，位域 Reserved |
| C.3 Performance Monitors | p.1157-1278 | PMU 的外部访问视图，包含计数、配置、锁和组件识别 |
| C.4 CTI | p.1279-1314 | Cross Trigger Interface，配置触发输入/输出和通道连接 |
| C.5 Debug | p.1315-1471 | 外部调试状态、指令/数据传递、断点/观察点、锁和认证 |
| C.6 Activity Monitors | p.1472-1525 | AMU 外部只读观察及组件相关寄存器 |
| C.7 Trace unit | p.1526-1660 | ETE 的 memory-mapped 配置、状态、资源、锁与识别 |

### C.1 相对偏移与组件发现

Core ROM table 帮助外部调试器找到组件；ROM entry、PIDR、CIDR 等用于发现和识别。第17章的布局与附录 C 的组件内偏移需要一起读。教学例子：若工具已经确定某 PMU 组件基址为 `BASE`，其寄存器地址按 `BASE + offset` 计算；`BASE` 必须来自平台/组件发现，本文不虚构 SoC 的固定基址。

### C.2 外部访问受电源、锁与认证共同约束

某寄存器在 APB 上“能寻址”，不意味着核心掉电、OS Lock/Double Lock 生效或认证未通过时仍可正常读取。第17/18/19/21章分别定义了相关模块的访问限制；位于 DebugBlock 和 Core power domain 的寄存器可能受不同电源状态影响。

同名信息的系统寄存器视图与外部视图通常用于观察同一功能，但不是所有寄存器都严格一一映射，也不能忽略外部接口的数据宽度、访问大小与锁条件。操作系统和调试器若并发配置同一功能，应由软件协调。

### C.3 PPM不能按名称推测写控制能力

原 C.2 的 `CPUPPMCR/CPUPPMCR2-6` 描述开头提到 CPU behavior 控制，但本版 Attributes 是 **RO**，公开位域全部 Reserved。偏移为 0x000、0x010、0x020、0x080、0x088、0x090。可编程控制含义**待确认**，不能仅凭名称编造 DVFS 或功率控制流程。

原表入口 p.1151：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1151-original.png]]

### C.4 CTI连接事件，不搬运追踪数据

CTI 用于将触发事件通过通道进行连接，配合第17章的 CTM。它可以协调调试/追踪组件的触发行为；Trace stream 本身由 ATB/TRBE 等路径处理。CTI 的 trigger channel 和 CHI 的 REQ/RSP/SNP/DAT channel 属于不同系统，不能因都叫 channel 而混用。

### C.5 总表与展开条目一起使用

先从本组 summary 查 offset/width/description，再进入具体条目确认位域与访问条件。原图表保留每组总表、所有编号位图与位域续表，见 [[#图表 附录C]]；名字检索用 [[#寄存器回查索引]]。

## 附录D UNPREDICTABLE行为

**原文范围：p.1661-1665，§D.1-D.4。** 本章记录特定条件下，N2 对架构允许的不确定行为所作的选择或偏离。它是排查异常/调试兼容性问题的依据，不能用来鼓励依赖不可移植的指令用法。

### D.1 R15作为操作数

对于原文指定的、以 R15 为 load/store base 的 UNPREDICTABLE 情形，N2 使用具有通常偏移的 PC；T32 时强制 word alignment。若指令要求 WriteBack，则执行访存但不 WriteBack。其他不合法 R15 使用不能概括为“读 0、写忽略”：原文明确 N2 不采用该策略，而是采取 UNDEFINED exception trap。

### D.2 跨页访问

| 原文限定的跨页情形 | N2记录的行为 |
|---|---|
| Store 跨页 | 不产生该情形的 alignment fault，拆成两个 store，各自采用所在地址的 memory type/shareability |
| Load 跨页，Device→Device 或 Normal→Normal | 不产生该情形的 alignment fault，拆成两个 load，各自使用对应属性 |
| Load 跨页，Device→Normal 或 Normal→Device | 产生 alignment fault |

此表讨论原文列出的 CONSTRAINED UNPREDICTABLE 条件，不表示所有跨页访问都无其他异常，也不保证拆分访问的整体原子性。中文“各自属性”不能替代设备内存访问规则。

### D.3 调试与计数器边界

原 Table D-1（p.1662-1664）包括下列值得记住的情况：

- A32 BKPT/HLT 的 condition code 不为 AL 时，这些列出的情形仍无条件执行。
- 链接到不存在或不具上下文能力的 breakpoint，不产生对应 Breakpoint/Watchpoint event；LBN 读 UNKNOWN。
- Address match breakpoint 的 BAS=0000 时视为 disabled；其他 BAS/MASK 组合需查原表，不能猜测。
- PMU 选择超出可访问/实现计数器范围时，可出现 RES0 或 UNALLOCATED；要区分实际实现数量 N、受虚拟化控制的可访问数量和 selector。
- 调试寄存器映射成 Normal memory，访问可能被重复、合并、拆分或改变大小，效果 UNPREDICTABLE。
- 不符合规定访问大小的外部访问可能读 UNKNOWN 或写成 UNKNOWN；外部写与 reset 同时发生时取 reset value。
- 保留调试/PMU 地址在掉电、锁或访问禁止等条件下，可能返回 Error 或 RES0；具体地址范围和优先条件见 p.1664。

### D.4 其他边界

`CSSELR` 选择不存在的缓存时，读取 CCSIDR 可能成为 NOP、UNDEFINED 或返回 UNKNOWN，不能据此推导出缓存容量为零。AArch32 CRC32/CRC32C 某些不合法 size/condition 编码的行为也有单独记录，不能扩展为正常编程建议。

全部原行为表及续表见 [[#图表 附录D与E]]。

## 附录E 文档版本变化

**原文范围：p.1666-1668，§E.1。** 文档内容变动可能是增补、澄清或自动生成寄存器条目的变化；不能把每条 change 都理解为硬件新增功能或已确认的 silicon erratum。

| 文档版本 | 对应状态 | 对本次学习最重要的变化 |
|---|---|---|
| 0000-02 | r0p0 early access | 增补 SPE、L2 编码和 PMU 事件信息 |
| 0000-03 | r0p0 的后续文档 | 增补 DSU 依赖项、SPE/trace 寄存器；补充电源模式与 write streaming；移除 PMSSRR 条目 |
| 0000-04 | r0p0 的后续文档 | RNG、transaction queue、架构版本、bus port 和 PMU→trace 信息更新 |
| 0001-05 | r0p1 首版 | 更新 full retention、AMU、L2 行为、转换响应和多个字段说明 |
| 0003-06 | r0p3 首版，本次依据 | 更新 feature/转换响应、L1 data tag 位位置和 CoreSight revision；导入新的自动生成寄存器说明 |

读到网络旧资料或不同修订的截图时，先核对产品 revision 与 document issue。第10章的编码、第9章 TQ 数量、第5章 retention、第16章 RNG 等均是历史上修改过的内容，必须引用本版原页。原 change tables：[[Neoverse/01_assets/N2-Core-TRM-r0p3/p1666-original.png|原文第1666页截图]] 起。

## 寄存器回查索引

按原手册的 30 个功能分组整理。收录 **548 个实际展开说明条目**，并列出各组总表识别到的寄存器名称；只有总表的寄存器不会被补写成具有完整位域说明。

英文寄存器名保留，中文组名帮助定位功能。名称后方是原文章节号和 PDF 页码；数组或成组寄存器可能共用一个展开条目，所以条目数不等于硬件寄存器数量。

阅读入口：[[#附录B AArch64寄存器]]。需要写寄存器时，必须继续核对原文 Configurations、Reset、Bit descriptions、Accessibility。

### 寄存器功能导航

| 原分组 | 功能 | 起始原页 | 展开条目 |
|---|---|---|---|
| A.1 | [[#寄存器 A1 特殊用途寄存器\|特殊用途寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160\|p.160]] | 0 |
| A.2 | [[#寄存器 A2 PMU寄存器\|PMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160\|p.160]] | 12 |
| A.3 | [[#寄存器 A3 通用定时器寄存器\|通用定时器寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207\|p.207]] | 0 |
| A.4 | [[#寄存器 A4 调试寄存器\|调试寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207\|p.207]] | 0 |
| A.5 | [[#寄存器 A5 通用系统控制寄存器\|通用系统控制寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208\|p.208]] | 0 |
| A.6 | [[#寄存器 A6 浮点寄存器\|浮点寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208\|p.208]] | 1 |
| A.7 | [[#寄存器 A7 AMU寄存器\|AMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213\|p.213]] | 14 |
| B.1 | [[#寄存器 B1 通用系统控制寄存器\|通用系统控制寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242\|p.242]] | 46 |
| B.2 | [[#寄存器 B2 调试寄存器\|调试寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351\|p.351]] | 26 |
| B.3 | [[#寄存器 B3 随机数寄存器\|随机数寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453\|p.453]] | 2 |
| B.4 | [[#寄存器 B4 系统指令\|系统指令]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=456\|p.456]] | 1 |
| B.5 | [[#寄存器 B5 识别与能力寄存器\|识别与能力寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458\|p.458]] | 45 |
| B.6 | [[#寄存器 B6 特殊用途寄存器\|特殊用途寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556\|p.556]] | 0 |
| B.7 | [[#寄存器 B7 PMU寄存器\|PMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556\|p.556]] | 16 |
| B.8 | [[#寄存器 B8 GIC寄存器\|GIC寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633\|p.633]] | 14 |
| B.9 | [[#寄存器 B9 通用定时器寄存器\|通用定时器寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779\|p.779]] | 0 |
| B.10 | [[#寄存器 B10 其他系统控制寄存器\|其他系统控制寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780\|p.780]] | 0 |
| B.11 | [[#寄存器 B11 AMU寄存器\|AMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781\|p.781]] | 16 |
| B.12 | [[#寄存器 B12 ETE寄存器\|ETE寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=816\|p.816]] | 57 |
| B.13 | [[#寄存器 B13 MPAM寄存器\|MPAM寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048\|p.1048]] | 9 |
| B.14 | [[#寄存器 B14 RAS寄存器\|RAS寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070\|p.1070]] | 13 |
| B.15 | [[#寄存器 B15 SPE寄存器\|SPE寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114\|p.1114]] | 3 |
| B.16 | [[#寄存器 B16 TRBE寄存器\|TRBE寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130\|p.1130]] | 0 |
| C.1 | [[#寄存器 C1 外部CoreROM寄存器\|外部CoreROM寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131\|p.1131]] | 16 |
| C.2 | [[#寄存器 C2 外部PPM寄存器\|外部PPM寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151\|p.1151]] | 6 |
| C.3 | [[#寄存器 C3 外部PMU寄存器\|外部PMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157\|p.1157]] | 60 |
| C.4 | [[#寄存器 C4 外部CTI寄存器\|外部CTI寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279\|p.1279]] | 23 |
| C.5 | [[#寄存器 C5 外部调试寄存器\|外部调试寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315\|p.1315]] | 58 |
| C.6 | [[#寄存器 C6 外部AMU寄存器\|外部AMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472\|p.1472]] | 35 |
| C.7 | [[#寄存器 C7 外部ETE寄存器\|外部ETE寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526\|p.1526]] | 75 |

### 寄存器回查方法

- Obsidian 搜索寄存器名，或从下面的功能导航进入相应分组。
- 总表名称包含只有概要、没有单独展开的架构寄存器。其具体位域需结合原文提示查适用的 Arm ARM。
- 同一功能的 AArch32、AArch64、外部接口分别列在 A/B/C；不要将不同访问视图相加为实现数量。
- 位域图和续表位于文末原图表回查索引；访问伪代码等普通页直接用 PDF 页码链接查看。
- 原文标题可能跨行；这里仅保存标题首行，寄存器名与章节号按原文。英文名称的完整展开以原页为准。

### AArch32寄存器索引

#### 寄存器 A1 特殊用途寄存器

> [!abstract]- 寄存器总表（本手册未逐项展开）
> 原分组 A.1，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0160-original.png|原文第160页截图]]。
>
> ##### 总表寄存器名
>
> `DSPSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `DLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]）
>
> 本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

#### 寄存器 A2 PMU寄存器

> [!abstract]- 总表名称与展开说明（12个展开条目）
> 原分组 A.2，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0160-original.png|原文第160页截图]]。
>
> ##### 总表寄存器名
>
> `PMCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMCNTENSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMCNTENCLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMOVSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMSWINC`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMSELR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMCEID0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMCEID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMCCNTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMXEVTYPER`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMXEVCNTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMUSERENR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMOVSSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMCEID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMCEID3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMCCFILTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | A.2.1 | PMEVCNTR0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=162\|p.162]] |
> | A.2.2 | PMEVCNTR1, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=165\|p.165]] |
> | A.2.3 | PMEVCNTR2, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=168\|p.168]] |
> | A.2.4 | PMEVCNTR3, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=171\|p.171]] |
> | A.2.5 | PMEVCNTR4, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=174\|p.174]] |
> | A.2.6 | PMEVCNTR5, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=178\|p.178]] |
> | A.2.7 | PMEVTYPER0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=181\|p.181]] |
> | A.2.8 | PMEVTYPER1, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=185\|p.185]] |
> | A.2.9 | PMEVTYPER2, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=189\|p.189]] |
> | A.2.10 | PMEVTYPER3, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=194\|p.194]] |
> | A.2.11 | PMEVTYPER4, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=198\|p.198]] |
> | A.2.12 | PMEVTYPER5, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=202\|p.202]] |

#### 寄存器 A3 通用定时器寄存器

> [!abstract]- 寄存器总表（本手册未逐项展开）
> 原分组 A.3，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0207-original.png|原文第207页截图]]。
>
> ##### 总表寄存器名
>
> `CNTFRQ`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTP_TVAL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTP_CTL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTV_TVAL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTV_CTL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTPCT`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTVCT`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTP_CVAL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTV_CVAL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]）
>
> 本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

#### 寄存器 A4 调试寄存器

> [!abstract]- 寄存器总表（本手册未逐项展开）
> 原分组 A.4，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0207-original.png|原文第207页截图]]。
>
> ##### 总表寄存器名
>
> `DBGDSCRint`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `DBGDTRRXint`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `DBGDTRTXint`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]）
>
> 本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

#### 寄存器 A5 通用系统控制寄存器

> [!abstract]- 寄存器总表（本手册未逐项展开）
> 原分组 A.5，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0208-original.png|原文第208页截图]]。
>
> ##### 总表寄存器名
>
> `TPIDRURW`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]） · `TPIDRURO`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]）
>
> 本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

#### 寄存器 A6 浮点寄存器

> [!abstract]- 总表名称与展开说明（1个展开条目）
> 原分组 A.6，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0208-original.png|原文第208页截图]]。
>
> ##### 总表寄存器名
>
> `FPSCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | A.6.1 | FPSCR, Floating-Point Status and Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208\|p.208]] |

#### 寄存器 A7 AMU寄存器

> [!abstract]- 总表名称与展开说明（14个展开条目）
> 原分组 A.7，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0213-original.png|原文第213页截图]]。
>
> ##### 总表寄存器名
>
> `AMCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCFGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCGCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMUSERENR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCNTENCLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCNTENSET0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCNTENCLR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCNTENSET1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER00`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER01`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER02`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER03`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVCNTR00`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR01`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR02`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR03`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | A.7.1 | AMEVTYPER00, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214\|p.214]] |
> | A.7.2 | AMEVTYPER01, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=216\|p.216]] |
> | A.7.3 | AMEVTYPER02, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=218\|p.218]] |
> | A.7.4 | AMEVTYPER03, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=220\|p.220]] |
> | A.7.5 | AMEVTYPER10, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=222\|p.222]] |
> | A.7.6 | AMEVTYPER11, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=223\|p.223]] |
> | A.7.7 | AMEVTYPER12, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=225\|p.225]] |
> | A.7.8 | AMEVCNTR00, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=227\|p.227]] |
> | A.7.9 | AMEVCNTR10, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=229\|p.229]] |
> | A.7.10 | AMEVCNTR01, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=231\|p.231]] |
> | A.7.11 | AMEVCNTR11, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=233\|p.233]] |
> | A.7.12 | AMEVCNTR02, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=235\|p.235]] |
> | A.7.13 | AMEVCNTR12, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=237\|p.237]] |
> | A.7.14 | AMEVCNTR03, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=239\|p.239]] |

### AArch64寄存器索引

#### 寄存器 B1 通用系统控制寄存器

> [!abstract]- 总表名称与展开说明（46个展开条目）
> 原分组 B.1，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0242-original.png|原文第242页截图]]。
>
> ##### 总表寄存器名
>
> `ACTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `RGSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `GCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `TTBR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `TTBR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `TCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APIAKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APIAKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APIBKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APIBKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APDAKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APDAKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APDBKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APDBKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APGAKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `APGAKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `SPSel`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `CurrentEL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `PAN`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `UAO`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `AFSR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `AFSR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `ESR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `TFSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `TFSRE0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `FAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `PAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `MAIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `AMAIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LORSA_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LOREA_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LORN_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LORC_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LORID_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `VBAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `ISR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `CONTEXTIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `TPIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `SCXTNUM_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUECTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUECTLR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUPPMCR3_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUPWRCTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_ATCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR6_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR7_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `AIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `NZCV`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `DAIF`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `DIT`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `SSBS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `TCO`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `FPCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `FPSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `TPIDR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `TPIDRRO_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `SCXTNUM_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `ACTLR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `HACR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TTBR0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TTBR1_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VTTBR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VTCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VNCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VSTTBR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VSTCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `AFSR0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `AFSR1_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `ESR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TFSR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `FAR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `HPFAR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `MAIR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `AMAIR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VBAR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `CONTEXTIDR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TPIDR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `SCXTNUM_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_ATCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_AVTCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `ACTLR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `SCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `CPTR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `MDCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `TTBR0_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `TCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `AFSR0_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `AFSR1_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `ESR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `TFSR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `FAR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `MAIR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `AMAIR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `VBAR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `RVBAR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `RMR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `TPIDR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `SCXTNUM_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_CPUPPMCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_CPUPPMCR2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_CPUPPMCR4_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPPMCR5_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPPMCR6_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUACTLR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_ATCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPSELR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPOR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPMR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPOR2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPMR2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPFR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.1.1 | ACTLR_EL1, Auxiliary Control Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247\|p.247]] |
> | B.1.2 | AFSR0_EL1, Auxiliary Fault Status Register 0 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=249\|p.249]] |
> | B.1.3 | AFSR1_EL1, Auxiliary Fault Status Register 1 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=252\|p.252]] |
> | B.1.4 | AMAIR_EL1, Auxiliary Memory Attribute Indirection Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=255\|p.255]] |
> | B.1.5 | LORID_EL1, LORegionID (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=257\|p.257]] |
> | B.1.6 | IMP_CPUACTLR_EL1, CPU Auxiliary Control Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=259\|p.259]] |
> | B.1.7 | IMP_CPUACTLR2_EL1, CPU Auxiliary Control Register 2 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=261\|p.261]] |
> | B.1.8 | IMP_CPUACTLR3_EL1, CPU Auxiliary Control Register 3 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=263\|p.263]] |
> | B.1.9 | IMP_CPUACTLR4_EL1, CPU Auxiliary Control Register 4 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=264\|p.264]] |
> | B.1.10 | IMP_CPUECTLR_EL1, CPU Extended Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=266\|p.266]] |
> | B.1.11 | IMP_CPUECTLR2_EL1, CPU Extended Control Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=275\|p.275]] |
> | B.1.12 | IMP_CPUPPMCR3_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=280\|p.280]] |
> | B.1.13 | IMP_CPUPWRCTLR_EL1, CPU Power Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=282\|p.282]] |
> | B.1.14 | IMP_ATCR_EL1, CPU Auxiliary Translation Control Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=284\|p.284]] |
> | B.1.15 | IMP_CPUACTLR5_EL1, CPU Auxiliary Control Register 5 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=287\|p.287]] |
> | B.1.16 | IMP_CPUACTLR6_EL1, CPU Auxiliary Control Register 6 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=288\|p.288]] |
> | B.1.17 | IMP_CPUACTLR7_EL1, CPU Auxiliary Control Register 7 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=290\|p.290]] |
> | B.1.18 | AIDR_EL1, Auxiliary ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=292\|p.292]] |
> | B.1.19 | FPCR, Floating-point Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=293\|p.293]] |
> | B.1.20 | FPSR, Floating-point Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=297\|p.297]] |
> | B.1.21 | ACTLR_EL2, Auxiliary Control Register (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=302\|p.302]] |
> | B.1.22 | HACR_EL2, Hypervisor Auxiliary Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=305\|p.305]] |
> | B.1.23 | AFSR0_EL2, Auxiliary Fault Status Register 0 (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=307\|p.307]] |
> | B.1.24 | AFSR1_EL2, Auxiliary Fault Status Register 1 (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=309\|p.309]] |
> | B.1.25 | AMAIR_EL2, Auxiliary Memory Attribute Indirection Register (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=312\|p.312]] |
> | B.1.26 | IMP_ATCR_EL2, CPU Auxiliary Translation Control Register (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=315\|p.315]] |
> | B.1.27 | IMP_AVTCR_EL2, CPU Virtualization Auxiliary Translation Control | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=317\|p.317]] |
> | B.1.28 | ACTLR_EL3, Auxiliary Control Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=319\|p.319]] |
> | B.1.29 | AFSR0_EL3, Auxiliary Fault Status Register 0 (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=322\|p.322]] |
> | B.1.30 | AFSR1_EL3, Auxiliary Fault Status Register 1 (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=324\|p.324]] |
> | B.1.31 | AMAIR_EL3, Auxiliary Memory Attribute Indirection Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=325\|p.325]] |
> | B.1.32 | RMR_EL3, Reset Management Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=327\|p.327]] |
> | B.1.33 | IMP_CPUPPMCR_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=329\|p.329]] |
> | B.1.34 | IMP_CPUPPMCR2_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=330\|p.330]] |
> | B.1.35 | IMP_CPUPPMCR4_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=332\|p.332]] |
> | B.1.36 | IMP_CPUPPMCR5_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=333\|p.333]] |
> | B.1.37 | IMP_CPUPPMCR6_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=335\|p.335]] |
> | B.1.38 | IMP_CPUACTLR_EL3, CPU Auxiliary Control Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=336\|p.336]] |
> | B.1.39 | IMP_ATCR_EL3, CPU Auxiliary Translation Control Register (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=338\|p.338]] |
> | B.1.40 | IMP_CPUPSELR_EL3, Selected Instruction Private Select Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=340\|p.340]] |
> | B.1.41 | IMP_CPUPCR_EL3, Selected Instruction Private Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=342\|p.342]] |
> | B.1.42 | IMP_CPUPOR_EL3, Selected Instruction Private Opcode Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=343\|p.343]] |
> | B.1.43 | IMP_CPUPMR_EL3, Selected Instruction Private Mask Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=345\|p.345]] |
> | B.1.44 | IMP_CPUPOR2_EL3, Selected Instruction Private Opcode Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=346\|p.346]] |
> | B.1.45 | IMP_CPUPMR2_EL3, Selected Instruction Private Mask Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=348\|p.348]] |
> | B.1.46 | IMP_CPUPFR_EL3, Selected Instruction Private Flag Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=349\|p.349]] |

#### 寄存器 B2 调试寄存器

> [!abstract]- 总表名称与展开说明（26个展开条目）
> 原分组 B.2，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0351-original.png|原文第351页截图]]。
>
> ##### 总表寄存器名
>
> `OSDTRRX_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWVR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWCR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWVR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWCR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `MDCCINT_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `MDSCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWVR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWCR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `OSDTRTX_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWVR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWCR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `OSECCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `MDRAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `OSLAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `OSLSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `OSDLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGPRCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGCLAIMSET_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGCLAIMCLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGAUTHSTATUS_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `MDCCSR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGDTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGDTRRX_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGDTRTX_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `TRFCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `MDCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `TRFCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_IDATA0_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_IDATA1_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_IDATA2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_DDATA0_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_DDATA1_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_DDATA2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.2.1 | DBGBVR0_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352\|p.352]] |
> | B.2.2 | DBGBCR0_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=358\|p.358]] |
> | B.2.3 | DBGWVR0_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=363\|p.363]] |
> | B.2.4 | DBGWCR0_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=366\|p.366]] |
> | B.2.5 | DBGBVR1_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=370\|p.370]] |
> | B.2.6 | DBGBCR1_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=376\|p.376]] |
> | B.2.7 | DBGWVR1_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=380\|p.380]] |
> | B.2.8 | DBGWCR1_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=383\|p.383]] |
> | B.2.9 | DBGBVR2_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=387\|p.387]] |
> | B.2.10 | DBGBCR2_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=393\|p.393]] |
> | B.2.11 | DBGWVR2_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=398\|p.398]] |
> | B.2.12 | DBGWCR2_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=401\|p.401]] |
> | B.2.13 | DBGBVR3_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=405\|p.405]] |
> | B.2.14 | DBGBCR3_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=411\|p.411]] |
> | B.2.15 | DBGWVR3_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=416\|p.416]] |
> | B.2.16 | DBGWCR3_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=419\|p.419]] |
> | B.2.17 | DBGBVR4_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=423\|p.423]] |
> | B.2.18 | DBGBCR4_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=429\|p.429]] |
> | B.2.19 | DBGBVR5_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=434\|p.434]] |
> | B.2.20 | DBGBCR5_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=440\|p.440]] |
> | B.2.21 | IMP_IDATA0_EL3, Instruction Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=445\|p.445]] |
> | B.2.22 | IMP_IDATA1_EL3, Instruction Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=447\|p.447]] |
> | B.2.23 | IMP_IDATA2_EL3, Instruction Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=448\|p.448]] |
> | B.2.24 | IMP_DDATA0_EL3, Data Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=449\|p.449]] |
> | B.2.25 | IMP_DDATA1_EL3, Data Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=450\|p.450]] |
> | B.2.26 | IMP_DDATA2_EL3, Data Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=451\|p.451]] |

#### 寄存器 B3 随机数寄存器

> [!abstract]- 总表名称与展开说明（2个展开条目）
> 原分组 B.3，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453|p.453]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0453-original.png|原文第453页截图]]。
>
> ##### 总表寄存器名
>
> `IMP_CPURNDBR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453|p.453]]） · `IMP_CPURNDPEID_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453|p.453]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.3.1 | IMP_CPURNDBR_EL3, CPU Random Number Base Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453\|p.453]] |
> | B.3.2 | IMP_CPURNDPEID_EL3, CPU Random Number Packet Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=455\|p.455]] |

#### 寄存器 B4 系统指令

> [!abstract]- 总表名称与展开说明（1个展开条目）
> 原分组 B.4，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=456|p.456]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0456-original.png|原文第456页截图]]。
>
> ##### 总表寄存器名
>
> `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=456|p.456]]） · `SYS_IMP_RAMINDEX`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=457|p.457]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.4.1 | SYS_IMP_RAMINDEX, RAM Index | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=457\|p.457]] |

#### 寄存器 B5 识别与能力寄存器

> [!abstract]- 总表名称与展开说明（45个展开条目）
> 原分组 B.5，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0458-original.png|原文第458页截图]]。
>
> ##### 总表寄存器名
>
> `MIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `MPIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `REVIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_PFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_PFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_DFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_AFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR6_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `MVFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `MVFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `MVFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_PFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_DFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_MMFR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64PFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64PFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64PFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64ZFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64DFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64DFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64AFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64AFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64ISAR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64ISAR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64ISAR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64MMFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64MMFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64MMFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `MPAMIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `IMP_CPUCFR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CCSIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CLIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CCSIDR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `GMID_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CSSELR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `DCZID_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `VPIDR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `VMPIDR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.5.1 | MIDR_EL1, Main ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459\|p.459]] |
> | B.5.2 | MPIDR_EL1, Multiprocessor Affinity Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=461\|p.461]] |
> | B.5.3 | REVIDR_EL1, Revision ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=463\|p.463]] |
> | B.5.4 | ID_PFR0_EL1, AArch32 Processor Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=464\|p.464]] |
> | B.5.5 | ID_PFR1_EL1, AArch32 Processor Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=467\|p.467]] |
> | B.5.6 | ID_DFR0_EL1, AArch32 Debug Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=469\|p.469]] |
> | B.5.7 | ID_AFR0_EL1, AArch32 Auxiliary Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=471\|p.471]] |
> | B.5.8 | ID_MMFR0_EL1, AArch32 Memory Model Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=473\|p.473]] |
> | B.5.9 | ID_MMFR1_EL1, AArch32 Memory Model Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=475\|p.475]] |
> | B.5.10 | ID_MMFR2_EL1, AArch32 Memory Model Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=477\|p.477]] |
> | B.5.11 | ID_MMFR3_EL1, AArch32 Memory Model Feature Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=479\|p.479]] |
> | B.5.12 | ID_ISAR0_EL1, AArch32 Instruction Set Attribute Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=482\|p.482]] |
> | B.5.13 | ID_ISAR1_EL1, AArch32 Instruction Set Attribute Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=484\|p.484]] |
> | B.5.14 | ID_ISAR2_EL1, AArch32 Instruction Set Attribute Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=486\|p.486]] |
> | B.5.15 | ID_ISAR3_EL1, AArch32 Instruction Set Attribute Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=488\|p.488]] |
> | B.5.16 | ID_ISAR4_EL1, AArch32 Instruction Set Attribute Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=490\|p.490]] |
> | B.5.17 | ID_ISAR5_EL1, AArch32 Instruction Set Attribute Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=493\|p.493]] |
> | B.5.18 | ID_MMFR4_EL1, AArch32 Memory Model Feature Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=495\|p.495]] |
> | B.5.19 | ID_ISAR6_EL1, AArch32 Instruction Set Attribute Register 6 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=497\|p.497]] |
> | B.5.20 | MVFR0_EL1, AArch32 Media and VFP Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=500\|p.500]] |
> | B.5.21 | MVFR1_EL1, AArch32 Media and VFP Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=502\|p.502]] |
> | B.5.22 | MVFR2_EL1, AArch32 Media and VFP Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=504\|p.504]] |
> | B.5.23 | ID_PFR2_EL1, AArch32 Processor Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=506\|p.506]] |
> | B.5.24 | ID_DFR1_EL1, Debug Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=508\|p.508]] |
> | B.5.25 | ID_MMFR5_EL1, AArch32 Memory Model Feature Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=509\|p.509]] |
> | B.5.26 | ID_AA64PFR0_EL1, AArch64 Processor Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=511\|p.511]] |
> | B.5.27 | ID_AA64PFR1_EL1, AArch64 Processor Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=514\|p.514]] |
> | B.5.28 | ID_AA64PFR2_EL1, AArch64 Processor Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=516\|p.516]] |
> | B.5.29 | ID_AA64ZFR0_EL1, SVE Feature ID register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=517\|p.517]] |
> | B.5.30 | ID_AA64DFR0_EL1, AArch64 Debug Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=520\|p.520]] |
> | B.5.31 | ID_AA64DFR1_EL1, AArch64 Debug Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=522\|p.522]] |
> | B.5.32 | ID_AA64AFR0_EL1, AArch64 Auxiliary Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=523\|p.523]] |
> | B.5.33 | ID_AA64AFR1_EL1, AArch64 Auxiliary Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=525\|p.525]] |
> | B.5.34 | ID_AA64ISAR0_EL1, AArch64 Instruction Set Attribute Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=526\|p.526]] |
> | B.5.35 | ID_AA64ISAR1_EL1, AArch64 Instruction Set Attribute Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=530\|p.530]] |
> | B.5.36 | ID_AA64ISAR2_EL1, AArch64 Instruction Set Attribute Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=533\|p.533]] |
> | B.5.37 | ID_AA64MMFR0_EL1, AArch64 Memory Model Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=535\|p.535]] |
> | B.5.38 | ID_AA64MMFR1_EL1, AArch64 Memory Model Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=537\|p.537]] |
> | B.5.39 | ID_AA64MMFR2_EL1, AArch64 Memory Model Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=540\|p.540]] |
> | B.5.40 | MPAMIDR_EL1, MPAM ID Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=543\|p.543]] |
> | B.5.41 | IMP_CPUCFR_EL1, CPU Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=545\|p.545]] |
> | B.5.42 | CLIDR_EL1, Cache Level ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=546\|p.546]] |
> | B.5.43 | GMID_EL1, Multiple tag transfer ID register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=550\|p.550]] |
> | B.5.44 | CTR_EL0, Cache Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=552\|p.552]] |
> | B.5.45 | DCZID_EL0, Data Cache Zero ID register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=554\|p.554]] |

#### 寄存器 B6 特殊用途寄存器

> [!abstract]- 寄存器总表（本手册未逐项展开）
> 原分组 B.6，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0556-original.png|原文第556页截图]]。
>
> ##### 总表寄存器名
>
> `SPSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `ELR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SP_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `DSPSR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `DLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `ELR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SP_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_irq`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_abt`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_und`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_fiq`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `ELR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SP_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]）
>
> 本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

#### 寄存器 B7 PMU寄存器

> [!abstract]- 总表名称与展开说明（16个展开条目）
> 原分组 B.7，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0556-original.png|原文第556页截图]]。
>
> ##### 总表寄存器名
>
> `PMINTENSET_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `PMINTENCLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `PMMIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCNTENSET_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCNTENCLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMOVSCLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMSWINC_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMSELR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCEID0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCEID1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCCNTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMXEVTYPER_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMXEVCNTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMUSERENR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMOVSSET_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR2_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR3_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR4_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR5_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVTYPER0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVTYPER1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVTYPER2_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVTYPER3_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558|p.558]]） · `PMEVTYPER4_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558|p.558]]） · `PMEVTYPER5_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558|p.558]]） · `PMCCFILTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558|p.558]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.7.1 | PMMIR_EL1, Performance Monitors Machine Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558\|p.558]] |
> | B.7.2 | PMCR_EL0, Performance Monitors Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=560\|p.560]] |
> | B.7.3 | PMCEID0_EL0, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=566\|p.566]] |
> | B.7.4 | PMCEID1_EL0, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=573\|p.573]] |
> | B.7.5 | PMEVCNTR0_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=580\|p.580]] |
> | B.7.6 | PMEVCNTR1_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=583\|p.583]] |
> | B.7.7 | PMEVCNTR2_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=587\|p.587]] |
> | B.7.8 | PMEVCNTR3_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=591\|p.591]] |
> | B.7.9 | PMEVCNTR4_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=594\|p.594]] |
> | B.7.10 | PMEVCNTR5_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=598\|p.598]] |
> | B.7.11 | PMEVTYPER0_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=602\|p.602]] |
> | B.7.12 | PMEVTYPER1_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=607\|p.607]] |
> | B.7.13 | PMEVTYPER2_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=612\|p.612]] |
> | B.7.14 | PMEVTYPER3_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=617\|p.617]] |
> | B.7.15 | PMEVTYPER4_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=622\|p.622]] |
> | B.7.16 | PMEVTYPER5_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=628\|p.628]] |

#### 寄存器 B8 GIC寄存器

> [!abstract]- 总表名称与展开说明（14个展开条目）
> 原分组 B.8，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0633-original.png|原文第633页截图]]。
>
> ##### 总表寄存器名
>
> `ICC_PMR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_PMR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_IAR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_IAR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `Register`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_EOIR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_EOIR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_HPPIR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_HPPIR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_BPR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_AP0R0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_AP0R0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_AP1R0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_AP1R0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_DIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_DIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_RPR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_RPR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_SGI1R_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_ASGI1R_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `Group`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_SGI0R_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_IAR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_IAR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_EOIR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_EOIR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_HPPIR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_HPPIR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_BPR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_BPR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_CTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_CTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_SRE_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_IGRPEN0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_IGRPEN0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_IGRPEN1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_IGRPEN1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICH_AP0R0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICH_AP1R0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_SRE_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_HCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_VTR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_MISR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_EISR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_ELRSR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_VMCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_LR0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_LR1_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_LR2_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_LR3_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICC_CTLR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICC_SRE_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICC_IGRPEN1_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.8.1 | ICC_AP0R0_EL1, Interrupt Controller Active Priorities Group 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635\|p.635]] |
> | B.8.2 | ICV_AP0R0_EL1, Interrupt Controller Virtual Active Priorities Group | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=645\|p.645]] |
> | B.8.3 | ICC_AP1R0_EL1, Interrupt Controller Active Priorities Group 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=654\|p.654]] |
> | B.8.4 | ICV_AP1R0_EL1, Interrupt Controller Virtual Active Priorities Group | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=669\|p.669]] |
> | B.8.5 | ICC_CTLR_EL1, Interrupt Controller Control Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=679\|p.679]] |
> | B.8.6 | ICV_CTLR_EL1, Interrupt Controller Virtual Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=683\|p.683]] |
> | B.8.7 | ICH_AP0R0_EL2, Interrupt Controller Hyp Active Priorities Group 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=687\|p.687]] |
> | B.8.8 | ICH_AP1R0_EL2, Interrupt Controller Hyp Active Priorities Group 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=722\|p.722]] |
> | B.8.9 | ICH_VTR_EL2, Interrupt Controller VGIC Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=756\|p.756]] |
> | B.8.10 | ICH_LR0_EL2, Interrupt Controller List Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=758\|p.758]] |
> | B.8.11 | ICH_LR1_EL2, Interrupt Controller List Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=762\|p.762]] |
> | B.8.12 | ICH_LR2_EL2, Interrupt Controller List Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=767\|p.767]] |
> | B.8.13 | ICH_LR3_EL2, Interrupt Controller List Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=771\|p.771]] |
> | B.8.14 | ICC_CTLR_EL3, Interrupt Controller Control Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=775\|p.775]] |

#### 寄存器 B9 通用定时器寄存器

> [!abstract]- 寄存器总表（本手册未逐项展开）
> 原分组 B.9，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0779-original.png|原文第779页截图]]。
>
> ##### 总表寄存器名
>
> `CNTKCTL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTFRQ_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTPCT_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTVCT_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTP_TVAL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTP_CTL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTP_CVAL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTV_TVAL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTV_CTL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTV_CVAL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTVOFF_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTHCTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTHP_TVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHP_CTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHP_CVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHV_TVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHV_CTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHV_CVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHVS_TVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHVS_CTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHVS_CVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHPS_TVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHPS_CTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHPS_CVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTPS_TVAL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTPS_CTL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTPS_CVAL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]）
>
> 本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

#### 寄存器 B10 其他系统控制寄存器

> [!abstract]- 寄存器总表（本手册未逐项展开）
> 原分组 B.10，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0780-original.png|原文第780页截图]]。
>
> ##### 总表寄存器名
>
> `SCTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CPACR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `ZCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `SCTLR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `HCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `CPTR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `HSTR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `ZCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `SCTLR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `ZCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]）
>
> 本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

#### 寄存器 B11 AMU寄存器

> [!abstract]- 总表名称与展开说明（16个展开条目）
> 原分组 B.11，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0781-original.png|原文第781页截图]]。
>
> ##### 总表寄存器名
>
> `AMCR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCFGR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCGCR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMUSERENR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCNTENCLR0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCNTENSET0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCNTENCLR1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCNTENSET1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVCNTR00_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVCNTR01_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVCNTR02_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVCNTR03_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVTYPER00_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVTYPER01_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER02_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER03_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVCNTR10_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVCNTR11_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVCNTR12_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER10_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER11_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER12_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.11.1 | AMCFGR_EL0, Activity Monitors Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782\|p.782]] |
> | B.11.2 | AMCGCR_EL0, Activity Monitors Counter Group Configuration | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=784\|p.784]] |
> | B.11.3 | AMEVCNTR00_EL0, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=786\|p.786]] |
> | B.11.4 | AMEVCNTR01_EL0, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=788\|p.788]] |
> | B.11.5 | AMEVCNTR02_EL0, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=790\|p.790]] |
> | B.11.6 | AMEVCNTR03_EL0, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=793\|p.793]] |
> | B.11.7 | AMEVTYPER00_EL0, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=795\|p.795]] |
> | B.11.8 | AMEVTYPER01_EL0, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=797\|p.797]] |
> | B.11.9 | AMEVTYPER02_EL0, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=799\|p.799]] |
> | B.11.10 | AMEVTYPER03_EL0, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=801\|p.801]] |
> | B.11.11 | AMEVCNTR10_EL0, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=804\|p.804]] |
> | B.11.12 | AMEVCNTR11_EL0, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=806\|p.806]] |
> | B.11.13 | AMEVCNTR12_EL0, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=808\|p.808]] |
> | B.11.14 | AMEVTYPER10_EL0, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=810\|p.810]] |
> | B.11.15 | AMEVTYPER11_EL0, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=812\|p.812]] |
> | B.11.16 | AMEVTYPER12_EL0, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=814\|p.814]] |

#### 寄存器 B12 ETE寄存器

> [!abstract]- 总表名称与展开说明（57个展开条目）
> 原分组 B.12，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=816|p.816]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0817-original.png|原文第817页截图]]。
>
> ##### 总表寄存器名
>
> `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=816|p.816]]） · `TRCTRACEIDR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCVICTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQEVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR8`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIMSPEC0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCPRGCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCVIIECTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQEVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR9`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCVISSCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQEVR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSTATR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCCONFIGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCCNTCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCCNTCTLR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR13`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCAUXCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQRSTEVR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQSTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCEVENTCTL0R`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCEXTINSELR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCCNTVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCEVENTCTL1R`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCEXTINSELR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCCNTVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCRSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCEXTINSELR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCEXTINSELR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCTSCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCSYNCPR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCCCCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCBBCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCSSCCR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCOSLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCRSCTLR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCRSCTLR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR8`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCSSCSR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR9`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR13`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR14`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR15`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACVR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACATR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACVR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACATR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACVR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACATR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCCIDCVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCVMIDCVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCCIDCCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCVMIDCCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCCLAIMSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCCLAIMCLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCAUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.12.1 | TRCSEQEVR0, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820\|p.820]] |
> | B.12.2 | TRCIDR8, ID Register 8 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=824\|p.824]] |
> | B.12.3 | TRCIMSPEC0, IMP DEF Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=826\|p.826]] |
> | B.12.4 | TRCSEQEVR1, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=828\|p.828]] |
> | B.12.5 | TRCSEQEVR2, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=832\|p.832]] |
> | B.12.6 | TRCIDR10, ID Register 10 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=835\|p.835]] |
> | B.12.7 | TRCIDR11, ID Register 11 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=837\|p.837]] |
> | B.12.8 | TRCCNTCTLR0, Counter Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=838\|p.838]] |
> | B.12.9 | TRCIDR12, ID Register 12 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=842\|p.842]] |
> | B.12.10 | TRCCNTCTLR1, Counter Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=844\|p.844]] |
> | B.12.11 | TRCIDR13, ID Register 13 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=848\|p.848]] |
> | B.12.12 | TRCEXTINSELR0, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=849\|p.849]] |
> | B.12.13 | TRCCNTVR0, Counter Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=853\|p.853]] |
> | B.12.14 | TRCIDR0, ID Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=855\|p.855]] |
> | B.12.15 | TRCEXTINSELR1, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=858\|p.858]] |
> | B.12.16 | TRCCNTVR1, Counter Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=861\|p.861]] |
> | B.12.17 | TRCIDR1, ID Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=863\|p.863]] |
> | B.12.18 | TRCEXTINSELR2, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=865\|p.865]] |
> | B.12.19 | TRCIDR2, ID Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=868\|p.868]] |
> | B.12.20 | TRCEXTINSELR3, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=870\|p.870]] |
> | B.12.21 | TRCIDR3, ID Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=873\|p.873]] |
> | B.12.22 | TRCIDR4, ID Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=876\|p.876]] |
> | B.12.23 | TRCIDR5, ID Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=878\|p.878]] |
> | B.12.24 | TRCSSCCR0, Single-shot Comparator Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=880\|p.880]] |
> | B.12.25 | TRCRSCTLR2, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=883\|p.883]] |
> | B.12.26 | TRCRSCTLR3, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=891\|p.891]] |
> | B.12.27 | TRCRSCTLR4, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=897\|p.897]] |
> | B.12.28 | TRCRSCTLR5, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=904\|p.904]] |
> | B.12.29 | TRCRSCTLR6, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=910\|p.910]] |
> | B.12.30 | TRCRSCTLR7, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=917\|p.917]] |
> | B.12.31 | TRCRSCTLR8, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=923\|p.923]] |
> | B.12.32 | TRCSSCSR0, Single-shot Comparator Control Status Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=930\|p.930]] |
> | B.12.33 | TRCRSCTLR9, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=933\|p.933]] |
> | B.12.34 | TRCRSCTLR10, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=940\|p.940]] |
> | B.12.35 | TRCRSCTLR11, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=947\|p.947]] |
> | B.12.36 | TRCRSCTLR12, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=953\|p.953]] |
> | B.12.37 | TRCRSCTLR13, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=960\|p.960]] |
> | B.12.38 | TRCRSCTLR14, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=966\|p.966]] |
> | B.12.39 | TRCRSCTLR15, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=973\|p.973]] |
> | B.12.40 | TRCACVR0, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=979\|p.979]] |
> | B.12.41 | TRCACATR0, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=982\|p.982]] |
> | B.12.42 | TRCACVR1, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=987\|p.987]] |
> | B.12.43 | TRCACATR1, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=990\|p.990]] |
> | B.12.44 | TRCACVR2, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=995\|p.995]] |
> | B.12.45 | TRCACATR2, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=998\|p.998]] |
> | B.12.46 | TRCACVR3, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1003\|p.1003]] |
> | B.12.47 | TRCACATR3, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1006\|p.1006]] |
> | B.12.48 | TRCACVR4, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1011\|p.1011]] |
> | B.12.49 | TRCACATR4, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1014\|p.1014]] |
> | B.12.50 | TRCACVR5, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1019\|p.1019]] |
> | B.12.51 | TRCACATR5, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1022\|p.1022]] |
> | B.12.52 | TRCACVR6, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1027\|p.1027]] |
> | B.12.53 | TRCACATR6, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1030\|p.1030]] |
> | B.12.54 | TRCACVR7, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1035\|p.1035]] |
> | B.12.55 | TRCACATR7, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1038\|p.1038]] |
> | B.12.56 | TRCCIDCVR0, Context Identifier Comparator Value Registers <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1043\|p.1043]] |
> | B.12.57 | TRCVMIDCVR0, Virtual Context Identifier Comparator Value | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1045\|p.1045]] |

#### 寄存器 B13 MPAM寄存器

> [!abstract]- 总表名称与展开说明（9个展开条目）
> 原分组 B.13，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1048-original.png|原文第1048页截图]]。
>
> ##### 总表寄存器名
>
> `MPAM1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAM0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMHCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPMV_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAM2_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM1_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM2_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM3_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM4_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM5_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM6_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM7_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAM3_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.13.1 | MPAMVPMV_EL2, MPAM Virtual Partition Mapping Valid Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048\|p.1048]] |
> | B.13.2 | MPAMVPM0_EL2, MPAM Virtual PARTID Mapping Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1051\|p.1051]] |
> | B.13.3 | MPAMVPM1_EL2, MPAM Virtual PARTID Mapping Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1054\|p.1054]] |
> | B.13.4 | MPAMVPM2_EL2, MPAM Virtual PARTID Mapping Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1056\|p.1056]] |
> | B.13.5 | MPAMVPM3_EL2, MPAM Virtual PARTID Mapping Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1058\|p.1058]] |
> | B.13.6 | MPAMVPM4_EL2, MPAM Virtual PARTID Mapping Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1061\|p.1061]] |
> | B.13.7 | MPAMVPM5_EL2, MPAM Virtual PARTID Mapping Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1063\|p.1063]] |
> | B.13.8 | MPAMVPM6_EL2, MPAM Virtual PARTID Mapping Register 6 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1066\|p.1066]] |
> | B.13.9 | MPAMVPM7_EL2, MPAM Virtual PARTID Mapping Register 7 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1068\|p.1068]] |

#### 寄存器 B14 RAS寄存器

> [!abstract]- 总表名称与展开说明（13个展开条目）
> 原分组 B.14，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070|p.1070]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1070-original.png|原文第1070页截图]]。
>
> ##### 总表寄存器名
>
> `ERRIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070|p.1070]]） · `ERRSELR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070|p.1070]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070|p.1070]]） · `ERXFR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXCTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXSTATUS_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXADDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXPFGF_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXPFGCTL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXPFGCDN_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXMISC0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXMISC1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXMISC2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXMISC3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `DISR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `VSESR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `VDISR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.14.1 | ERRIDR_EL1, Error Record ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071\|p.1071]] |
> | B.14.2 | ERRSELR_EL1, Error Record Select Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1073\|p.1073]] |
> | B.14.3 | ERXFR_EL1, Selected Error Record Feature Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1075\|p.1075]] |
> | B.14.4 | ERXCTLR_EL1, Selected Error Record Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1078\|p.1078]] |
> | B.14.5 | ERXSTATUS_EL1, Selected Error Record Primary Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1081\|p.1081]] |
> | B.14.6 | ERXADDR_EL1, Selected Error Record Address Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1087\|p.1087]] |
> | B.14.7 | ERXPFGF_EL1, Selected Pseudo-fault Generation Feature register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1090\|p.1090]] |
> | B.14.8 | ERXPFGCTL_EL1, Selected Pseudo-fault Generation Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1094\|p.1094]] |
> | B.14.9 | ERXPFGCDN_EL1, Selected Pseudo-fault Generation Countdown | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1098\|p.1098]] |
> | B.14.10 | ERXMISC0_EL1, Selected Error Record Miscellaneous Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1101\|p.1101]] |
> | B.14.11 | ERXMISC1_EL1, Selected Error Record Miscellaneous Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1107\|p.1107]] |
> | B.14.12 | ERXMISC2_EL1, Selected Error Record Miscellaneous Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1109\|p.1109]] |
> | B.14.13 | ERXMISC3_EL1, Selected Error Record Miscellaneous Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1112\|p.1112]] |

#### 寄存器 B15 SPE寄存器

> [!abstract]- 总表名称与展开说明（3个展开条目）
> 原分组 B.15，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1114-original.png|原文第1114页截图]]。
>
> ##### 总表寄存器名
>
> `PMSCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSICR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSIRR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSFCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSEVFR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSLATFR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMSIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMBLIMITR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMBPTR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMBSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMBIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMSCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | B.15.1 | PMSEVFR_EL1, Sampling Event Filter Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115\|p.1115]] |
> | B.15.2 | PMSIDR_EL1, Sampling Profiling ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1126\|p.1126]] |
> | B.15.3 | PMBIDR_EL1, Profiling Buffer ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1128\|p.1128]] |

#### 寄存器 B16 TRBE寄存器

> [!abstract]- 寄存器总表（本手册未逐项展开）
> 原分组 B.16，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1130-original.png|原文第1130页截图]]。
>
> ##### 总表寄存器名
>
> `TRBLIMITR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBPTR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBBASER_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBMAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBTRG_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]）
>
> 本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

### 外部寄存器索引

#### 寄存器 C1 外部CoreROM寄存器

> [!abstract]- 总表名称与展开说明（16个展开条目）
> 原分组 C.1，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1131-original.png|原文第1131页截图]]。
>
> ##### 总表寄存器名
>
> `COREROM_ROMENTRY0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_ROMENTRY1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_ROMENTRY2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_ROMENTRY3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_AUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_DEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_DEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_CIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_CIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_CIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_CIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | C.1.1 | COREROM_ROMENTRY0, Core ROM table Entry 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131\|p.1131]] |
> | C.1.2 | COREROM_ROMENTRY1, Core ROM table Entry 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1133\|p.1133]] |
> | C.1.3 | COREROM_ROMENTRY2, Core ROM table Entry 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1134\|p.1134]] |
> | C.1.4 | COREROM_ROMENTRY3, Core ROM table Entry 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1135\|p.1135]] |
> | C.1.5 | COREROM_AUTHSTATUS, Core ROM table Authentication Status | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1137\|p.1137]] |
> | C.1.6 | COREROM_DEVARCH, Core ROM table Device Architecture Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1138\|p.1138]] |
> | C.1.7 | COREROM_DEVTYPE, Core ROM table Device Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1139\|p.1139]] |
> | C.1.8 | COREROM_PIDR4, Core ROM table Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1140\|p.1140]] |
> | C.1.9 | COREROM_PIDR0, Core ROM table Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1142\|p.1142]] |
> | C.1.10 | COREROM_PIDR1, Core ROM table Peripheral Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1143\|p.1143]] |
> | C.1.11 | COREROM_PIDR2, Core ROM table Peripheral Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1144\|p.1144]] |
> | C.1.12 | COREROM_PIDR3, Core ROM table Peripheral Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1145\|p.1145]] |
> | C.1.13 | COREROM_CIDR0, Core ROM table Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1146\|p.1146]] |
> | C.1.14 | COREROM_CIDR1, Core ROM table Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1147\|p.1147]] |
> | C.1.15 | COREROM_CIDR2, Core ROM table Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1149\|p.1149]] |
> | C.1.16 | COREROM_CIDR3, Core ROM table Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1150\|p.1150]] |

#### 寄存器 C2 外部PPM寄存器

> [!abstract]- 总表名称与展开说明（6个展开条目）
> 原分组 C.2，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1151-original.png|原文第1151页截图]]。
>
> ##### 总表寄存器名
>
> `CPUPPMCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | C.2.1 | CPUPPMCR, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151\|p.1151]] |
> | C.2.2 | CPUPPMCR2, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1152\|p.1152]] |
> | C.2.3 | CPUPPMCR3, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1153\|p.1153]] |
> | C.2.4 | CPUPPMCR4, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1154\|p.1154]] |
> | C.2.5 | CPUPPMCR5, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1155\|p.1155]] |
> | C.2.6 | CPUPPMCR6, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1156\|p.1156]] |

#### 寄存器 C3 外部PMU寄存器

> [!abstract]- 总表名称与展开说明（60个展开条目）
> 原分组 C.3，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1157-original.png|原文第1157页截图]]。
>
> ##### 总表寄存器名
>
> `PMEVCNTR0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR2_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR3_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR4_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR5_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMCCNTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMPCSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCID1SR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMVIDSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCID2SR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER2_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER3_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER4_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER5_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCCFILTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMPCSSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCIDSSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMSSSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCCNTSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMSSCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCNTENSET_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCNTENCLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMINTENSET_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMINTENCLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMOVSCLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMSWINC_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMOVSSET_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCFGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCEID0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCEID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCEID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCEID3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMMIR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMDEVAFF0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMDEVAFF1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMLAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMAUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMDEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | C.3.1 | PMEVCNTR0_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159\|p.1159]] |
> | C.3.2 | PMEVCNTR1_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1161\|p.1161]] |
> | C.3.3 | PMEVCNTR2_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1163\|p.1163]] |
> | C.3.4 | PMEVCNTR3_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1165\|p.1165]] |
> | C.3.5 | PMEVCNTR4_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1168\|p.1168]] |
> | C.3.6 | PMEVCNTR5_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1170\|p.1170]] |
> | C.3.7 | PMCCNTR_EL0, Performance Monitors Cycle Counter | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1172\|p.1172]] |
> | C.3.8 | PMPCSR, Program Counter Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1174\|p.1174]] |
> | C.3.9 | PMCID1SR, CONTEXTIDR_EL1 Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1178\|p.1178]] |
> | C.3.10 | PMVIDSR, VMID Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1180\|p.1180]] |
> | C.3.11 | PMCID2SR, CONTEXTIDR_EL2 Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1182\|p.1182]] |
> | C.3.12 | PMEVTYPER0_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1183\|p.1183]] |
> | C.3.13 | PMEVTYPER1_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1187\|p.1187]] |
> | C.3.14 | PMEVTYPER2_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1190\|p.1190]] |
> | C.3.15 | PMEVTYPER3_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1194\|p.1194]] |
> | C.3.16 | PMEVTYPER4_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1197\|p.1197]] |
> | C.3.17 | PMEVTYPER5_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1201\|p.1201]] |
> | C.3.18 | PMCCFILTR_EL0, Performance Monitors Cycle Counter Filter | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1204\|p.1204]] |
> | C.3.19 | PMPCSSR, Snapshot Program Counter Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1207\|p.1207]] |
> | C.3.20 | PMCIDSSR, Snapshot CONTEXTIDR_EL1 Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1208\|p.1208]] |
> | C.3.21 | PMSSSR, PMU Snapshot Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1209\|p.1209]] |
> | C.3.22 | PMCCNTSR, PMU Cycle Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1211\|p.1211]] |
> | C.3.23 | PMEVCNTSR0, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1212\|p.1212]] |
> | C.3.24 | PMEVCNTSR1, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1213\|p.1213]] |
> | C.3.25 | PMEVCNTSR2, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1214\|p.1214]] |
> | C.3.26 | PMEVCNTSR3, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1215\|p.1215]] |
> | C.3.27 | PMEVCNTSR4, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1216\|p.1216]] |
> | C.3.28 | PMEVCNTSR5, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1217\|p.1217]] |
> | C.3.29 | PMSSCR, PMU Snapshot Capture Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1219\|p.1219]] |
> | C.3.30 | PMCNTENSET_EL0, Performance Monitors Count Enable Set | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1220\|p.1220]] |
> | C.3.31 | PMCNTENCLR_EL0, Performance Monitors Count Enable Clear | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1222\|p.1222]] |
> | C.3.32 | PMINTENSET_EL1, Performance Monitors Interrupt Enable Set | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1224\|p.1224]] |
> | C.3.33 | PMINTENCLR_EL1, Performance Monitors Interrupt Enable Clear | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1226\|p.1226]] |
> | C.3.34 | PMOVSCLR_EL0, Performance Monitors Overflow Flag Status Clear | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1228\|p.1228]] |
> | C.3.35 | PMSWINC_EL0, Performance Monitors Software Increment register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1230\|p.1230]] |
> | C.3.36 | PMOVSSET_EL0, Performance Monitors Overflow Flag Status Set | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1231\|p.1231]] |
> | C.3.37 | PMCFGR, Performance Monitors Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1233\|p.1233]] |
> | C.3.38 | PMCR_EL0, Performance Monitors Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1236\|p.1236]] |
> | C.3.39 | PMCEID0, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1238\|p.1238]] |
> | C.3.40 | PMCEID1, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1242\|p.1242]] |
> | C.3.41 | PMCEID2, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1246\|p.1246]] |
> | C.3.42 | PMCEID3, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1250\|p.1250]] |
> | C.3.43 | PMMIR, Performance Monitors Machine Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1254\|p.1254]] |
> | C.3.44 | PMDEVAFF0, Performance Monitors Device Affinity register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1255\|p.1255]] |
> | C.3.45 | PMDEVAFF1, Performance Monitors Device Affinity register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1256\|p.1256]] |
> | C.3.46 | PMLAR, Performance Monitors Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1258\|p.1258]] |
> | C.3.47 | PMLSR, Performance Monitors Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1259\|p.1259]] |
> | C.3.48 | PMAUTHSTATUS, Performance Monitors Authentication Status | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1261\|p.1261]] |
> | C.3.49 | PMDEVARCH, Performance Monitors Device Architecture register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1262\|p.1262]] |
> | C.3.50 | PMDEVID, Performance Monitors Device ID register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1264\|p.1264]] |
> | C.3.51 | PMDEVTYPE, Performance Monitors Device Type register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1265\|p.1265]] |
> | C.3.52 | PMPIDR4, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1266\|p.1266]] |
> | C.3.53 | PMPIDR0, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1268\|p.1268]] |
> | C.3.54 | PMPIDR1, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1269\|p.1269]] |
> | C.3.55 | PMPIDR2, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1271\|p.1271]] |
> | C.3.56 | PMPIDR3, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1272\|p.1272]] |
> | C.3.57 | PMCIDR0, Performance Monitors Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1274\|p.1274]] |
> | C.3.58 | PMCIDR1, Performance Monitors Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1275\|p.1275]] |
> | C.3.59 | PMCIDR2, Performance Monitors Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1276\|p.1276]] |
> | C.3.60 | PMCIDR3, Performance Monitors Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1278\|p.1278]] |

#### 寄存器 C4 外部CTI寄存器

> [!abstract]- 总表名称与展开说明（23个展开条目）
> 原分组 C.4，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1279-original.png|原文第1279页截图]]。
>
> ##### 总表寄存器名
>
> `CTICONTROL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIINTACK`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIAPPSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIAPPCLEAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIAPPPULSE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTITRIGINSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTITRIGOUTSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTICHINSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTICHOUTSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIGATE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `ASICCTL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIDEVCTL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIDEVAFF0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIDEVAFF1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTILAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTILSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIAUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIDEVID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIDEVID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | C.4.1 | CTICONTROL, CTI Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280\|p.1280]] |
> | C.4.2 | CTIINTACK, CTI Output Trigger Acknowledge register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1281\|p.1281]] |
> | C.4.3 | CTIAPPSET, CTI Application Trigger Set register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1283\|p.1283]] |
> | C.4.4 | CTIAPPCLEAR, CTI Application Trigger Clear register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1285\|p.1285]] |
> | C.4.5 | CTIAPPPULSE, CTI Application Pulse register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1287\|p.1287]] |
> | C.4.6 | CTIINEN<n>, CTI Input Trigger to Output Channel Enable registers, n | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1289\|p.1289]] |
> | C.4.7 | CTIOUTEN<n>, CTI Input Channel to Output Trigger Enable registers, | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1291\|p.1291]] |
> | C.4.8 | CTITRIGINSTATUS, CTI Trigger In Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1292\|p.1292]] |
> | C.4.9 | CTITRIGOUTSTATUS, CTI Trigger Out Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1294\|p.1294]] |
> | C.4.10 | CTICHINSTATUS, CTI Channel In Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1295\|p.1295]] |
> | C.4.11 | CTICHOUTSTATUS, CTI Channel Out Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1297\|p.1297]] |
> | C.4.12 | CTIGATE, CTI Channel Gate Enable register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1298\|p.1298]] |
> | C.4.13 | ASICCTL, CTI External Multiplexer Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1300\|p.1300]] |
> | C.4.14 | CTIDEVCTL, CTI Device Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1301\|p.1301]] |
> | C.4.15 | CTIDEVAFF0, CTI Device Affinity register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1303\|p.1303]] |
> | C.4.16 | CTIDEVAFF1, CTI Device Affinity register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1304\|p.1304]] |
> | C.4.17 | CTILAR, CTI Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1305\|p.1305]] |
> | C.4.18 | CTILSR, CTI Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1306\|p.1306]] |
> | C.4.19 | CTIAUTHSTATUS, CTI Authentication Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1308\|p.1308]] |
> | C.4.20 | CTIDEVARCH, CTI Device Architecture register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1309\|p.1309]] |
> | C.4.21 | CTIDEVID2, CTI Device ID register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1311\|p.1311]] |
> | C.4.22 | CTIDEVID1, CTI Device ID register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1312\|p.1312]] |
> | C.4.23 | CTIDEVID, CTI Device ID register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1313\|p.1313]] |

#### 寄存器 C5 外部调试寄存器

> [!abstract]- 总表名称与展开说明（58个展开条目）
> 原分组 C.5，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1315-original.png|原文第1315页截图]]。
>
> ##### 总表寄存器名
>
> `EDESR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDECR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDWAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGDTRRX_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDITR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDSCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGDTRTX_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDRCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDECCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `OSLAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDPRCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDPRSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGBVR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGBCR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGBVR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBVR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBVR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBVR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBVR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWVR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWCR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWVR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWCR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWVR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWCR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWVR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWCR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `MIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPFR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDFR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDAA32PFR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDITCTRL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGCLAIMSET_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGCLAIMCLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVAFF0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVAFF1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDLAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGAUTHSTATUS_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDPIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | C.5.1 | EDESR, External Debug Event Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317\|p.1317]] |
> | C.5.2 | EDECR, External Debug Execution Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1319\|p.1319]] |
> | C.5.3 | EDWAR, External Debug Watchpoint Address Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1320\|p.1320]] |
> | C.5.4 | DBGDTRRX_EL0, Debug Data Transfer Register, Receive | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1322\|p.1322]] |
> | C.5.5 | EDITR, External Debug Instruction Transfer Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1324\|p.1324]] |
> | C.5.6 | EDSCR, External Debug Status and Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1326\|p.1326]] |
> | C.5.7 | DBGDTRTX_EL0, Debug Data Transfer Register, Transmit | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1333\|p.1333]] |
> | C.5.8 | EDRCR, External Debug Reserve Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1335\|p.1335]] |
> | C.5.9 | EDECCR, External Debug Exception Catch Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1336\|p.1336]] |
> | C.5.10 | OSLAR_EL1, OS Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1342\|p.1342]] |
> | C.5.11 | EDPRCR, External Debug Power/Reset Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1343\|p.1343]] |
> | C.5.12 | EDPRSR, External Debug Processor Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1346\|p.1346]] |
> | C.5.13 | DBGBVR0_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1353\|p.1353]] |
> | C.5.14 | DBGBCR0_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1359\|p.1359]] |
> | C.5.15 | DBGBVR1_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1363\|p.1363]] |
> | C.5.16 | DBGBCR1_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1368\|p.1368]] |
> | C.5.17 | DBGBVR2_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1373\|p.1373]] |
> | C.5.18 | DBGBCR2_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1378\|p.1378]] |
> | C.5.19 | DBGBVR3_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1383\|p.1383]] |
> | C.5.20 | DBGBCR3_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1388\|p.1388]] |
> | C.5.21 | DBGBVR4_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1393\|p.1393]] |
> | C.5.22 | DBGBCR4_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1398\|p.1398]] |
> | C.5.23 | DBGBVR5_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1403\|p.1403]] |
> | C.5.24 | DBGBCR5_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1408\|p.1408]] |
> | C.5.25 | DBGWVR0_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1413\|p.1413]] |
> | C.5.26 | DBGWCR0_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1414\|p.1414]] |
> | C.5.27 | DBGWVR1_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1418\|p.1418]] |
> | C.5.28 | DBGWCR1_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1420\|p.1420]] |
> | C.5.29 | DBGWVR2_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1423\|p.1423]] |
> | C.5.30 | DBGWCR2_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1425\|p.1425]] |
> | C.5.31 | DBGWVR3_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1428\|p.1428]] |
> | C.5.32 | DBGWCR3_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1430\|p.1430]] |
> | C.5.33 | MIDR_EL1, Main ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1433\|p.1433]] |
> | C.5.34 | EDPFR, External Debug Processor Feature Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1435\|p.1435]] |
> | C.5.35 | EDDFR, External Debug Feature Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1437\|p.1437]] |
> | C.5.36 | EDAA32PFR, External Debug Auxiliary Processor Feature Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1439\|p.1439]] |
> | C.5.37 | EDITCTRL, External Debug Integration mode Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1441\|p.1441]] |
> | C.5.38 | DBGCLAIMSET_EL1, Debug CLAIM Tag Set register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1442\|p.1442]] |
> | C.5.39 | DBGCLAIMCLR_EL1, Debug CLAIM Tag Clear register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1444\|p.1444]] |
> | C.5.40 | EDDEVAFF0, External Debug Device Affinity register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1446\|p.1446]] |
> | C.5.41 | EDDEVAFF1, External Debug Device Affinity register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1447\|p.1447]] |
> | C.5.42 | EDLAR, External Debug Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1448\|p.1448]] |
> | C.5.43 | EDLSR, External Debug Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1449\|p.1449]] |
> | C.5.44 | DBGAUTHSTATUS_EL1, Debug Authentication Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1451\|p.1451]] |
> | C.5.45 | EDDEVARCH, External Debug Device Architecture register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1453\|p.1453]] |
> | C.5.46 | EDDEVID2, External Debug Device ID register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1454\|p.1454]] |
> | C.5.47 | EDDEVID1, External Debug Device ID register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1456\|p.1456]] |
> | C.5.48 | EDDEVID, External Debug Device ID register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1457\|p.1457]] |
> | C.5.49 | EDDEVTYPE, External Debug Device Type register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1458\|p.1458]] |
> | C.5.50 | EDPIDR4, External Debug Peripheral Identification Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1460\|p.1460]] |
> | C.5.51 | EDPIDR0, External Debug Peripheral Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1461\|p.1461]] |
> | C.5.52 | EDPIDR1, External Debug Peripheral Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1462\|p.1462]] |
> | C.5.53 | EDPIDR2, External Debug Peripheral Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1464\|p.1464]] |
> | C.5.54 | EDPIDR3, External Debug Peripheral Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1465\|p.1465]] |
> | C.5.55 | EDCIDR0, External Debug Component Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1467\|p.1467]] |
> | C.5.56 | EDCIDR1, External Debug Component Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1468\|p.1468]] |
> | C.5.57 | EDCIDR2, External Debug Component Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1469\|p.1469]] |
> | C.5.58 | EDCIDR3, External Debug Component Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1471\|p.1471]] |

#### 寄存器 C6 外部AMU寄存器

> [!abstract]- 总表名称与展开说明（35个展开条目）
> 原分组 C.6，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1472-original.png|原文第1472页截图]]。
>
> ##### 总表寄存器名
>
> `AMEVCNTR00`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR01`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR02`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR03`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVTYPER00`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVTYPER01`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVTYPER02`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMEVTYPER03`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMEVTYPER10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMEVTYPER11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMEVTYPER12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCNTENSET0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCNTENSET1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCNTENCLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCNTENCLR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCGCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCFGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMIIDR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMDEVAFF0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMDEVAFF1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMDEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | C.6.1 | AMEVCNTR00, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473\|p.1473]] |
> | C.6.2 | AMEVCNTR01, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1475\|p.1475]] |
> | C.6.3 | AMEVCNTR02, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1477\|p.1477]] |
> | C.6.4 | AMEVCNTR03, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1479\|p.1479]] |
> | C.6.5 | AMEVCNTR10, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1480\|p.1480]] |
> | C.6.6 | AMEVCNTR11, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1482\|p.1482]] |
> | C.6.7 | AMEVCNTR12, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1484\|p.1484]] |
> | C.6.8 | AMEVTYPER00, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1486\|p.1486]] |
> | C.6.9 | AMEVTYPER01, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1487\|p.1487]] |
> | C.6.10 | AMEVTYPER02, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1489\|p.1489]] |
> | C.6.11 | AMEVTYPER03, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1491\|p.1491]] |
> | C.6.12 | AMEVTYPER10, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1493\|p.1493]] |
> | C.6.13 | AMEVTYPER11, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1494\|p.1494]] |
> | C.6.14 | AMEVTYPER12, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1496\|p.1496]] |
> | C.6.15 | AMCNTENSET0, Activity Monitors Count Enable Set Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1498\|p.1498]] |
> | C.6.16 | AMCNTENSET1, Activity Monitors Count Enable Set Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1499\|p.1499]] |
> | C.6.17 | AMCNTENCLR0, Activity Monitors Count Enable Clear Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1501\|p.1501]] |
> | C.6.18 | AMCNTENCLR1, Activity Monitors Count Enable Clear Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1502\|p.1502]] |
> | C.6.19 | AMCGCR, Activity Monitors Counter Group Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1504\|p.1504]] |
> | C.6.20 | AMCFGR, Activity Monitors Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1505\|p.1505]] |
> | C.6.21 | AMCR, Activity Monitors Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1507\|p.1507]] |
> | C.6.22 | AMIIDR, Activity Monitors Implementation Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1508\|p.1508]] |
> | C.6.23 | AMDEVAFF0, Activity Monitors Device Affinity Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1510\|p.1510]] |
> | C.6.24 | AMDEVAFF1, Activity Monitors Device Affinity Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1511\|p.1511]] |
> | C.6.25 | AMDEVARCH, Activity Monitors Device Architecture Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1512\|p.1512]] |
> | C.6.26 | AMDEVTYPE, Activity Monitors Device Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1514\|p.1514]] |
> | C.6.27 | AMPIDR4, Activity Monitors Peripheral Identification Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1515\|p.1515]] |
> | C.6.28 | AMPIDR0, Activity Monitors Peripheral Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1516\|p.1516]] |
> | C.6.29 | AMPIDR1, Activity Monitors Peripheral Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1517\|p.1517]] |
> | C.6.30 | AMPIDR2, Activity Monitors Peripheral Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1519\|p.1519]] |
> | C.6.31 | AMPIDR3, Activity Monitors Peripheral Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1520\|p.1520]] |
> | C.6.32 | AMCIDR0, Activity Monitors Component Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1521\|p.1521]] |
> | C.6.33 | AMCIDR1, Activity Monitors Component Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1523\|p.1523]] |
> | C.6.34 | AMCIDR2, Activity Monitors Component Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1524\|p.1524]] |
> | C.6.35 | AMCIDR3, Activity Monitors Component Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1525\|p.1525]] |

#### 寄存器 C7 外部ETE寄存器

> [!abstract]- 总表名称与展开说明（75个展开条目）
> 原分组 C.7，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526|p.1526]]；图表回查 [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1526-original.png|原文第1526页截图]]。
>
> ##### 总表寄存器名
>
> `TRCPRGCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526|p.1526]]） · `TRCSTATR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526|p.1526]]） · `TRCCONFIGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526|p.1526]]） · `TRCAUXCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEVENTCTL0R`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEVENTCTL1R`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCRSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCTSCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSYNCPR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCCCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCBBCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCTRACEIDR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCVICTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCVIIECTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCVISSCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQEVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQEVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQEVR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQRSTEVR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQSTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEXTINSELR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEXTINSELR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEXTINSELR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEXTINSELR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTRLDVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTRLDVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTCTLR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR8`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR9`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR13`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIMSPEC0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCIDR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCOSLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPDCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPDSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDCCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCVMIDCCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCITCTRL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCLAIMSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCLAIMCLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVAFF`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCLAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCAUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]）
>
> ##### 展开说明条目
>
> | 原章节 | 寄存器/原文标题 | 起始原页 |
> |---|---|---|
> | C.7.1 | TRCPRGCTLR, Programming Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528\|p.1528]] |
> | C.7.2 | TRCSTATR, Trace Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1530\|p.1530]] |
> | C.7.3 | TRCCONFIGR, Trace Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1531\|p.1531]] |
> | C.7.4 | TRCAUXCTLR, Auxiliary Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1534\|p.1534]] |
> | C.7.5 | TRCEVENTCTL0R, Event Control 0 Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1535\|p.1535]] |
> | C.7.6 | TRCEVENTCTL1R, Event Control 1 Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1538\|p.1538]] |
> | C.7.7 | TRCRSR, Resources Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1541\|p.1541]] |
> | C.7.8 | TRCTSCTLR, Timestamp Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1543\|p.1543]] |
> | C.7.9 | TRCSYNCPR, Synchronization Period Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1545\|p.1545]] |
> | C.7.10 | TRCCCCTLR, Cycle Count Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1547\|p.1547]] |
> | C.7.11 | TRCBBCTLR, Branch Broadcast Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1548\|p.1548]] |
> | C.7.12 | TRCTRACEIDR, Trace ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1550\|p.1550]] |
> | C.7.13 | TRCVICTLR, ViewInst Main Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1552\|p.1552]] |
> | C.7.14 | TRCVIIECTLR, ViewInst Include/Exclude Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1555\|p.1555]] |
> | C.7.15 | TRCVISSCTLR, ViewInst Start/Stop Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1557\|p.1557]] |
> | C.7.16 | TRCSEQEVR0, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1560\|p.1560]] |
> | C.7.17 | TRCSEQEVR1, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1562\|p.1562]] |
> | C.7.18 | TRCSEQEVR2, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1565\|p.1565]] |
> | C.7.19 | TRCSEQRSTEVR, Sequencer Reset Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1568\|p.1568]] |
> | C.7.20 | TRCSEQSTR, Sequencer State Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1570\|p.1570]] |
> | C.7.21 | TRCEXTINSELR0, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1571\|p.1571]] |
> | C.7.22 | TRCEXTINSELR1, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1574\|p.1574]] |
> | C.7.23 | TRCEXTINSELR2, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1576\|p.1576]] |
> | C.7.24 | TRCEXTINSELR3, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1578\|p.1578]] |
> | C.7.25 | TRCCNTRLDVR0, Counter Reload Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1580\|p.1580]] |
> | C.7.26 | TRCCNTRLDVR1, Counter Reload Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1581\|p.1581]] |
> | C.7.27 | TRCCNTCTLR0, Counter Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1582\|p.1582]] |
> | C.7.28 | TRCCNTCTLR1, Counter Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1585\|p.1585]] |
> | C.7.29 | TRCCNTVR0, Counter Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1588\|p.1588]] |
> | C.7.30 | TRCCNTVR1, Counter Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1590\|p.1590]] |
> | C.7.31 | TRCIDR8, ID Register 8 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1591\|p.1591]] |
> | C.7.32 | TRCIDR9, ID Register 9 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1592\|p.1592]] |
> | C.7.33 | TRCIDR10, ID Register 10 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1594\|p.1594]] |
> | C.7.34 | TRCIDR11, ID Register 11 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1595\|p.1595]] |
> | C.7.35 | TRCIDR12, ID Register 12 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1596\|p.1596]] |
> | C.7.36 | TRCIDR13, ID Register 13 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1597\|p.1597]] |
> | C.7.37 | TRCIMSPEC0, IMP DEF Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1598\|p.1598]] |
> | C.7.38 | TRCIDR0, ID Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1599\|p.1599]] |
> | C.7.39 | TRCIDR1, ID Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1602\|p.1602]] |
> | C.7.40 | TRCIDR2, ID Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1603\|p.1603]] |
> | C.7.41 | TRCIDR3, ID Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1605\|p.1605]] |
> | C.7.42 | TRCIDR4, ID Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1607\|p.1607]] |
> | C.7.43 | TRCIDR5, ID Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1609\|p.1609]] |
> | C.7.44 | TRCIDR6, ID Register 6 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1611\|p.1611]] |
> | C.7.45 | TRCIDR7, ID Register 7 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1612\|p.1612]] |
> | C.7.46 | TRCSSCSR<n>, Single-shot Comparator Control Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1613\|p.1613]] |
> | C.7.47 | TRCOSLSR, Trace OS Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1616\|p.1616]] |
> | C.7.48 | TRCPDCR, PowerDown Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1617\|p.1617]] |
> | C.7.49 | TRCPDSR, PowerDown Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1619\|p.1619]] |
> | C.7.50 | TRCCIDCCTLR0, Context Identifier Comparator Control Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1620\|p.1620]] |
> | C.7.51 | TRCVMIDCCTLR0, Virtual Context Identifier Comparator Control | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1622\|p.1622]] |
> | C.7.52 | TRCITCTRL, Integration Mode Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1624\|p.1624]] |
> | C.7.53 | TRCCLAIMSET, Claim Tag Set Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1626\|p.1626]] |
> | C.7.54 | TRCCLAIMCLR, Claim Tag Clear Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1628\|p.1628]] |
> | C.7.55 | TRCDEVAFF, Device Affinity Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1629\|p.1629]] |
> | C.7.56 | TRCLAR, Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1630\|p.1630]] |
> | C.7.57 | TRCLSR, Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1632\|p.1632]] |
> | C.7.58 | TRCAUTHSTATUS, Authentication Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1633\|p.1633]] |
> | C.7.59 | TRCDEVARCH, Device Architecture Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1637\|p.1637]] |
> | C.7.60 | TRCDEVID2, Device Configuration Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1638\|p.1638]] |
> | C.7.61 | TRCDEVID1, Device Configuration Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1640\|p.1640]] |
> | C.7.62 | TRCDEVID, Device Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1641\|p.1641]] |
> | C.7.63 | TRCDEVTYPE, Device Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1642\|p.1642]] |
> | C.7.64 | TRCPIDR4, Peripheral Identification Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1643\|p.1643]] |
> | C.7.65 | TRCPIDR5, Peripheral Identification Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1645\|p.1645]] |
> | C.7.66 | TRCPIDR6, Peripheral Identification Register 6 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1647\|p.1647]] |
> | C.7.67 | TRCPIDR7, Peripheral Identification Register 7 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1648\|p.1648]] |
> | C.7.68 | TRCPIDR0, Peripheral Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1649\|p.1649]] |
> | C.7.69 | TRCPIDR1, Peripheral Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1650\|p.1650]] |
> | C.7.70 | TRCPIDR2, Peripheral Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1652\|p.1652]] |
> | C.7.71 | TRCPIDR3, Peripheral Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1653\|p.1653]] |
> | C.7.72 | TRCCIDR0, Component Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1655\|p.1655]] |
> | C.7.73 | TRCCIDR1, Component Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1656\|p.1656]] |
> | C.7.74 | TRCCIDR2, Component Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1658\|p.1658]] |
> | C.7.75 | TRCCIDR3, Component Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1659\|p.1659]] |


## 原图表回查索引

这里保留原手册全部 1432 个编号图表标题与跨页续表入口。正文原图已放在对应章节；寄存器位图和大段续表可从下面的折叠目录按需打开。

“查看截图”打开原页图像；PDF 页码打开完整原文。截图保留原水印和正文宽度。无新编号标题的续页以“续表或相关原文”列出。

### 图表 第1章

原文范围 p.26-29。

> [!info]- 1个编号图表 · 1页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Figure 1-1: Key to timing diagram conventions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0028-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=28\|p.28]] |


### 图表 第2章

原文范围 p.30-38。

> [!info]- 11个编号图表 · 7页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Figure 2-1: Neoverse™ N2 example configuration | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0030-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=30\|p.30]] |
> | Table 2-1: Neoverse™ N2 core features that have a dependency on the DSU-110 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0032-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=32\|p.32]] |
> | Table 2-2: Armv8.0-A optional feature support in the Neoverse™ N2 core | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0033-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=33\|p.33]] |
> | Table 2-3: Arm®v8.1-A optional feature support in the Neoverse™ N2 core | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0033-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=33\|p.33]] |
> | Table 2-4: Arm®v8.2-A optional feature support in the Neoverse™ N2 core | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0033-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=33\|p.33]] |
> | Table 2-5: Arm®v8.3-A optional feature support in the Neoverse™ N2 core | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0034-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=34\|p.34]] |
> | Table 2-6: Arm®v8.4-A optional feature support in the Neoverse™ N2 core | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0035-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=35\|p.35]] |
> | Table 2-7: Arm®v8.5-A optional feature support in the Neoverse™ N2 core | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0035-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=35\|p.35]] |
> | Table 2-8: Arm®v9.0-A feature support in the Neoverse™ N2 core | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0035-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=35\|p.35]] |
> | Table 2-9: Other standards and specifications support in the Neoverse™ N2 core | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0035-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=35\|p.35]] |
> | 续表或相关原文（第36页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0036-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=36\|p.36]] |
> | Table 2-10: Product revisions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0038-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=38\|p.38]] |


### 图表 第3章

原文范围 p.39-44。

> [!info]- 1个编号图表 · 1页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Figure 3-1: Neoverse™ N2 core components | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0040-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=40\|p.40]] |


### 图表 第4章

原文范围 p.45-45。

本部分无编号图表；正文入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=45|p.45]]。

### 图表 第5章

原文范围 p.46-56。

> [!info]- 4个编号图表 · 4页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Figure 5-1: Neoverse™ N2 voltage and power domains | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0046-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=46\|p.46]] |
> | Figure 5-2: Core power domains in a cluster with one Neoverse™ N2 core | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0047-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=47\|p.47]] |
> | Table 5-1: Neoverse™ N2 core power modes | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0050-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=50\|p.50]] |
> | Figure 5-3: Neoverse™ N2 core power mode transitions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0051-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=51\|p.51]] |


### 图表 第6章

原文范围 p.57-64。

> [!info]- 4个编号图表 · 3页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 6-1: MMU components | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0058-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=58\|p.58]] |
> | Figure 6-1: Translation table walks | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0061-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=61\|p.61]] |
> | Table 6-2: Supported device memory types | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0063-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=63\|p.63]] |
> | Table 6-3: Shareability for Normal memory | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0063-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=63\|p.63]] |


### 图表 第7章

原文范围 p.65-68。

> [!info]- 1个编号图表 · 1页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 7-1: L1 instruction memory system features | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0065-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=65\|p.65]] |


### 图表 第8章

原文范围 p.69-73。

> [!info]- 1个编号图表 · 1页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 8-1: L1 data memory system features | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0069-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=69\|p.69]] |


### 图表 第9章

原文范围 p.74-75。

> [!info]- 2个编号图表 · 2页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 9-1: L2 memory system features | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0074-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=74\|p.74]] |
> | Table 9-2: Neoverse™ N2 transaction capabilities | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0075-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=75\|p.75]] |


### 图表 第10章

原文范围 p.76-95。

> [!info]- 62个编号图表 · 20页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 10-1: System registers used to access internal memory | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0076-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=76\|p.76]] |
> | Table 10-2: Neoverse™ N2 L1 instruction cache tag location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0076-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=76\|p.76]] |
> | Table 10-3: Neoverse™ N2 L1 instruction cache data location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0077-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=77\|p.77]] |
> | Table 10-4: Neoverse™ N2 L1 BTB data location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0077-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=77\|p.77]] |
> | Table 10-5: Neoverse™ N2 L1 GHB data location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0077-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=77\|p.77]] |
> | Table 10-6: Neoverse™ N2 L1 instruction TLB data location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0077-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=77\|p.77]] |
> | Table 10-7: Neoverse™ N2 BIM data location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0077-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=77\|p.77]] |
> | Table 10-8: Neoverse™ N2 L0 Macro-operation cache data location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0078-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=78\|p.78]] |
> | Table 10-9: Neoverse™ N2 L1 data cache tag location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0078-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=78\|p.78]] |
> | Table 10-10: Neoverse™ N2 L1 data cache data location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0078-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=78\|p.78]] |
> | Table 10-11: Neoverse™ N2 L1 data TLB location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0078-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=78\|p.78]] |
> | Table 10-12: L1 instruction cache tag format for Instruction Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0079-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=79\|p.79]] |
> | Table 10-13: L1 instruction cache tag format for Instruction Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0079-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=79\|p.79]] |
> | Table 10-14: L1 instruction cache tag format for Instruction Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0079-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=79\|p.79]] |
> | Table 10-15: L1 instruction cache data format for Instruction Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0079-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=79\|p.79]] |
> | Table 10-16: L1 instruction cache data format for Instruction Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0079-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=79\|p.79]] |
> | Table 10-17: L1 instruction cache data format for Instruction Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0080-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=80\|p.80]] |
> | Table 10-18: L1 BTB cache format for Instruction Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0080-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=80\|p.80]] |
> | Table 10-19: L1 BTB cache format for Instruction Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0080-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=80\|p.80]] |
> | Table 10-20: L1 BTB cache format for Instruction Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0080-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=80\|p.80]] |
> | Table 10-21: L1 GHB cache format for Instruction Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0080-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=80\|p.80]] |
> | Table 10-22: L1 GHB cache format for Instruction Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0080-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=80\|p.80]] |
> | Table 10-23: L1 GHB cache format for Instruction Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0080-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=80\|p.80]] |
> | Table 10-24: L1 BIM cache format for Instruction Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0081-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=81\|p.81]] |
> | Table 10-25: L1 BIM cache format for Instruction Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0081-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=81\|p.81]] |
> | Table 10-26: L1 BIM cache format for Instruction Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0081-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=81\|p.81]] |
> | Table 10-27: L1 instruction TLB format for Instruction Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0081-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=81\|p.81]] |
> | 续表或相关原文（第82页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0082-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=82\|p.82]] |
> | Table 10-28: L1 instruction TLB format for Instruction Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0083-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=83\|p.83]] |
> | Table 10-29: L1 instruction TLB format for Instruction Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0083-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=83\|p.83]] |
> | Table 10-30: L0 MOP cache format for Instruction Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0083-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=83\|p.83]] |
> | Table 10-31: L0 MOP cache format for Instruction Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0083-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=83\|p.83]] |
> | Table 10-32: L0 MOP cache format for Instruction Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0084-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=84\|p.84]] |
> | Table 10-33: L1 data cache tag format for Data Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0084-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=84\|p.84]] |
> | Table 10-34: L1 data cache tag format for Data Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0084-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=84\|p.84]] |
> | Table 10-35: L1 data cache tag format for Data Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0085-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=85\|p.85]] |
> | Table 10-36: L1 data cache data format for Data Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0085-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=85\|p.85]] |
> | Table 10-37: L1 data cache data format for Data Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0085-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=85\|p.85]] |
> | Table 10-38: L1 data cache data format for Data Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0085-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=85\|p.85]] |
> | Table 10-39: L1 data TLB format for Data Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0085-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=85\|p.85]] |
> | 续表或相关原文（第86页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0086-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=86\|p.86]] |
> | Table 10-40: L1 data TLB format for Data Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0087-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=87\|p.87]] |
> | Table 10-41: L1 data TLB format for Data Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0087-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=87\|p.87]] |
> | Table 10-42: Neoverse™ N2 L2 cache tag location encoding for 512KB | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0087-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=87\|p.87]] |
> | Table 10-43: Neoverse™ N2 L2 cache tag location encoding for 1MB | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0088-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=88\|p.88]] |
> | Table 10-44: Neoverse™ N2 L2 cache data location encoding for 512KB | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0088-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=88\|p.88]] |
> | Table 10-45: Neoverse™ N2 L2 cache data location encoding for 1MB | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0088-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=88\|p.88]] |
> | Table 10-46: Neoverse™ N2 L2 TLB location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0089-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=89\|p.89]] |
> | Table 10-47: Neoverse™ N2 L2 victim location encoding | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0089-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=89\|p.89]] |
> | Table 10-48: L2 tag cache format for Data Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0089-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=89\|p.89]] |
> | Table 10-49: L2 tag cache format for Data Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0090-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=90\|p.90]] |
> | Table 10-50: L2 tag cache format for Data Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0090-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=90\|p.90]] |
> | Table 10-51: L2 tag cache format for Data Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0090-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=90\|p.90]] |
> | Table 10-52: L2 tag cache format for Data Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0091-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=91\|p.91]] |
> | Table 10-53: L2 tag cache format for Data Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0091-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=91\|p.91]] |
> | Table 10-54: L2 data RAM format for Data Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0092-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=92\|p.92]] |
> | Table 10-55: L2 data RAM format for Data Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0092-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=92\|p.92]] |
> | Table 10-56: L2 data RAM format for Data Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0092-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=92\|p.92]] |
> | Table 10-57: L2 TLB format for Instruction Register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0092-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=92\|p.92]] |
> | Table 10-58: L2 TLB format for Instruction Register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0093-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=93\|p.93]] |
> | Table 10-59: L2 TLB format for Instruction Register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0094-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=94\|p.94]] |
> | Table 10-60: Neoverse™ N2 L2 victim format for data register 0 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0095-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=95\|p.95]] |
> | Table 10-61: Neoverse™ N2 L2 victim format for data register 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0095-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=95\|p.95]] |
> | Table 10-62: Neoverse™ N2 L2 victim format for data register 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0095-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=95\|p.95]] |


### 图表 第11章

原文范围 p.96-100。

> [!info]- 2个编号图表 · 2页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 11-1: RAM cache protection | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0097-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=97\|p.97]] |
> | Table 11-2: RAS registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0100-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=100\|p.100]] |


### 图表 第12章

原文范围 p.101-104。

> [!info]- 1个编号图表 · 3页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 12-1: GIC system registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0102-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=102\|p.102]] |
> | 续表或相关原文（第103页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0103-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=103\|p.103]] |
> | 续表或相关原文（第104页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0104-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=104\|p.104]] |


### 图表 第13章

原文范围 p.105-105。

本部分无编号图表；正文入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=105|p.105]]。

### 图表 第14章

原文范围 p.106-106。

本部分无编号图表；正文入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=106|p.106]]。

### 图表 第15章

原文范围 p.107-108。

> [!info]- 1个编号图表 · 2页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 15-1: Identification registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0107-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=107\|p.107]] |
> | 续表或相关原文（第108页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0108-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=108\|p.108]] |


### 图表 第16章

原文范围 p.109-110。

> [!info]- 1个编号图表 · 1页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 16-1: Random Number Control registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0110-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=110\|p.110]] |


### 图表 第17章

原文范围 p.111-121。

> [!info]- 9个编号图表 · 9页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Figure 17-1: DynamIQ™ cluster debug components | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0111-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=111\|p.111]] |
> | Figure 17-2: External debug system | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0112-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=112\|p.112]] |
> | Table 17-1: External access conditions to registers | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0115-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=115\|p.115]] |
> | Table 17-2: Core ROM table | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0116-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=116\|p.116]] |
> | Table 17-3: Neoverse™ N2 CoreSight component identification | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0116-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=116\|p.116]] |
> | Table 17-4: Core CTI register peripheral ID values | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0117-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=117\|p.117]] |
> | Table 17-5: Debug registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0117-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=117\|p.117]] |
> | 续表或相关原文（第118页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0118-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=118\|p.118]] |
> | Table 17-6: Debug registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0119-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=119\|p.119]] |
> | 续表或相关原文（第120页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0120-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=120\|p.120]] |
> | Table 17-7: CoreROM registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0121-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=121\|p.121]] |


### 图表 第18章

原文范围 p.122-136。

> [!info]- 3个编号图表 · 15页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 18-1: Performance monitors Events | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0122-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=122\|p.122]] |
> | 续表或相关原文（第123页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0123-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=123\|p.123]] |
> | 续表或相关原文（第124页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0124-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=124\|p.124]] |
> | 续表或相关原文（第125页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0125-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=125\|p.125]] |
> | 续表或相关原文（第126页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0126-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=126\|p.126]] |
> | 续表或相关原文（第127页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0127-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=127\|p.127]] |
> | 续表或相关原文（第128页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0128-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=128\|p.128]] |
> | 续表或相关原文（第129页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0129-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=129\|p.129]] |
> | 续表或相关原文（第130页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0130-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=130\|p.130]] |
> | 续表或相关原文（第131页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0131-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=131\|p.131]] |
> | 续表或相关原文（第132页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0132-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=132\|p.132]] |
> | Table 18-2: Performance Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0133-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=133\|p.133]] |
> | Table 18-3: Performance Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0134-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=134\|p.134]] |
> | 续表或相关原文（第135页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0135-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=135\|p.135]] |
> | 续表或相关原文（第136页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0136-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=136\|p.136]] |


### 图表 第19章

原文范围 p.137-149。

> [!info]- 8个编号图表 · 12页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Figure 19-1: Trace unit components | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0137-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=137\|p.137]] |
> | Table 19-1: Trace unit resources | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0138-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=138\|p.138]] |
> | Table 19-2: Trace unit generation options | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0139-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=139\|p.139]] |
> | Figure 19-2: Programming trace unit registers using the Debug APB interface | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0141-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=141\|p.141]] |
> | Figure 19-3: Programming trace registers using the System register interface | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0142-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=142\|p.142]] |
> | Table 19-3: ETE events | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0143-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=143\|p.143]] |
> | Table 19-4: Trace unit registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0143-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=143\|p.143]] |
> | 续表或相关原文（第144页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0144-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=144\|p.144]] |
> | 续表或相关原文（第145页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0145-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=145\|p.145]] |
> | 续表或相关原文（第146页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0146-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=146\|p.146]] |
> | Table 19-5: Trace unit registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0147-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=147\|p.147]] |
> | 续表或相关原文（第148页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0148-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=148\|p.148]] |
> | 续表或相关原文（第149页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0149-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=149\|p.149]] |


### 图表 第20章

原文范围 p.150-150。

本部分无编号图表；正文入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=150|p.150]]。

### 图表 第21章

原文范围 p.151-155。

> [!info]- 3个编号图表 · 4页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table 21-1: Mapping of counters to fixed events | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0152-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=152\|p.152]] |
> | Table 21-2: Activity Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0153-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=153\|p.153]] |
> | Table 21-3: Activity Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0154-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=154\|p.154]] |
> | 续表或相关原文（第155页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0155-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=155\|p.155]] |


### 图表 第22章

原文范围 p.156-159。

> [!info]- 4个编号图表 · 4页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Figure 22-1: SPE behavior | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0156-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=156\|p.156]] |
> | Table 22-1: SPE events packet | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0157-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=157\|p.157]] |
> | Table 22-2: SPE data source packet | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0158-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=158\|p.158]] |
> | Table 22-3: Statistical Profiling Extension registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0158-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=158\|p.158]] |
> | 续表或相关原文（第159页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0159-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=159\|p.159]] |


### 图表 附录A

原文范围 p.160-241。

> [!info]- 61个编号图表 · 46页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table A-1: Special-purpose registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0160-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160\|p.160]] |
> | Table A-2: Performance Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0160-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160\|p.160]] |
> | 续表或相关原文（第161页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0161-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161\|p.161]] |
> | Figure A-1: AArch32_pmevcntr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0162-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=162\|p.162]] |
> | Table A-3: PMEVCNTR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0162-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=162\|p.162]] |
> | Figure A-2: AArch32_pmevcntr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0165-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=165\|p.165]] |
> | Table A-6: PMEVCNTR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0166-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=166\|p.166]] |
> | Figure A-3: AArch32_pmevcntr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0169-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=169\|p.169]] |
> | Table A-9: PMEVCNTR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0169-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=169\|p.169]] |
> | Figure A-4: AArch32_pmevcntr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0172-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=172\|p.172]] |
> | Table A-12: PMEVCNTR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0172-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=172\|p.172]] |
> | Figure A-5: AArch32_pmevcntr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0175-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=175\|p.175]] |
> | Table A-15: PMEVCNTR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0175-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=175\|p.175]] |
> | Figure A-6: AArch32_pmevcntr5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0178-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=178\|p.178]] |
> | Table A-18: PMEVCNTR5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0179-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=179\|p.179]] |
> | Figure A-7: AArch32_pmevtyper0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0182-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=182\|p.182]] |
> | Table A-21: PMEVTYPER0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0182-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=182\|p.182]] |
> | 续表或相关原文（第183页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0183-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=183\|p.183]] |
> | Figure A-8: AArch32_pmevtyper1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0186-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=186\|p.186]] |
> | Table A-24: PMEVTYPER1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0186-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=186\|p.186]] |
> | 续表或相关原文（第187页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0187-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=187\|p.187]] |
> | Figure A-9: AArch32_pmevtyper2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0190-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=190\|p.190]] |
> | Table A-27: PMEVTYPER2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0190-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=190\|p.190]] |
> | 续表或相关原文（第191页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0191-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=191\|p.191]] |
> | Figure A-10: AArch32_pmevtyper3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0194-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=194\|p.194]] |
> | Table A-30: PMEVTYPER3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0195-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=195\|p.195]] |
> | 续表或相关原文（第196页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0196-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=196\|p.196]] |
> | Figure A-11: AArch32_pmevtyper4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0199-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=199\|p.199]] |
> | Table A-33: PMEVTYPER4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0199-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=199\|p.199]] |
> | 续表或相关原文（第200页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0200-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=200\|p.200]] |
> | Figure A-12: AArch32_pmevtyper5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0203-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=203\|p.203]] |
> | Table A-36: PMEVTYPER5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0203-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=203\|p.203]] |
> | 续表或相关原文（第204页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0204-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=204\|p.204]] |
> | Table A-39: Generic Timer registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0207-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207\|p.207]] |
> | Table A-40: Debug registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0207-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207\|p.207]] |
> | Table A-41: Generic System Control registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0208-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208\|p.208]] |
> | Table A-42: Floating Point registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0208-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208\|p.208]] |
> | Figure A-13: AArch32_fpscr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0209-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=209\|p.209]] |
> | Table A-43: FPSCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0209-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=209\|p.209]] |
> | 续表或相关原文（第210页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0210-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=210\|p.210]] |
> | 续表或相关原文（第211页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0211-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=211\|p.211]] |
> | 续表或相关原文（第212页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0212-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=212\|p.212]] |
> | Table A-46: Activity Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0213-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213\|p.213]] |
> | 续表或相关原文（第214页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0214-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214\|p.214]] |
> | Figure A-14: AArch32_amevtyper00 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0215-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=215\|p.215]] |
> | Table A-47: AMEVTYPER00 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0215-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=215\|p.215]] |
> | Figure A-15: AArch32_amevtyper01 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0216-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=216\|p.216]] |
> | Table A-49: AMEVTYPER01 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0217-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=217\|p.217]] |
> | Figure A-16: AArch32_amevtyper02 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0218-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=218\|p.218]] |
> | Table A-51: AMEVTYPER02 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0218-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=218\|p.218]] |
> | Figure A-17: AArch32_amevtyper03 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0220-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=220\|p.220]] |
> | Table A-53: AMEVTYPER03 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0220-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=220\|p.220]] |
> | Figure A-18: AArch32_amevtyper10 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0222-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=222\|p.222]] |
> | Table A-55: AMEVTYPER10 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0222-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=222\|p.222]] |
> | Figure A-19: AArch32_amevtyper11 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0224-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=224\|p.224]] |
> | Table A-57: AMEVTYPER11 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0224-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=224\|p.224]] |
> | Figure A-20: AArch32_amevtyper12 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0226-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=226\|p.226]] |
> | Table A-59: AMEVTYPER12 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0226-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=226\|p.226]] |
> | Figure A-21: AArch32_amevcntr00 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0228-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=228\|p.228]] |
> | Table A-61: AMEVCNTR00 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0228-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=228\|p.228]] |
> | Figure A-22: AArch32_amevcntr10 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0230-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=230\|p.230]] |
> | Table A-64: AMEVCNTR10 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0230-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=230\|p.230]] |
> | Figure A-23: AArch32_amevcntr01 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0232-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=232\|p.232]] |
> | Table A-67: AMEVCNTR01 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0232-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=232\|p.232]] |
> | Figure A-24: AArch32_amevcntr11 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0234-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=234\|p.234]] |
> | Table A-70: AMEVCNTR11 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0234-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=234\|p.234]] |
> | Figure A-25: AArch32_amevcntr02 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0236-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=236\|p.236]] |
> | Table A-73: AMEVCNTR02 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0236-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=236\|p.236]] |
> | Figure A-26: AArch32_amevcntr12 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0238-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=238\|p.238]] |
> | Table A-76: AMEVCNTR12 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0238-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=238\|p.238]] |
> | Figure A-27: AArch32_amevcntr03 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0240-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=240\|p.240]] |
> | Table A-79: AMEVCNTR03 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0240-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=240\|p.240]] |


### 图表 附录B

原文范围 p.242-1130。

> [!info]- 598个编号图表 · 615页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table B-1: Generic System Control registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0242-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242\|p.242]] |
> | 续表或相关原文（第243页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0243-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243\|p.243]] |
> | 续表或相关原文（第244页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0244-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244\|p.244]] |
> | 续表或相关原文（第245页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0245-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245\|p.245]] |
> | 续表或相关原文（第246页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0246-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246\|p.246]] |
> | 续表或相关原文（第247页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0247-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247\|p.247]] |
> | Figure B-1: AArch64_actlr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0248-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=248\|p.248]] |
> | Table B-2: ACTLR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0248-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=248\|p.248]] |
> | Figure B-2: AArch64_afsr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0250-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=250\|p.250]] |
> | Table B-5: AFSR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0250-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=250\|p.250]] |
> | Figure B-3: AArch64_afsr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0252-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=252\|p.252]] |
> | Table B-10: AFSR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0253-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=253\|p.253]] |
> | Figure B-4: AArch64_amair_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0255-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=255\|p.255]] |
> | Table B-15: AMAIR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0255-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=255\|p.255]] |
> | Figure B-5: AArch64_lorid_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0258-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=258\|p.258]] |
> | Table B-20: LORID_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0258-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=258\|p.258]] |
> | Figure B-6: AArch64_imp_cpuactlr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0260-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=260\|p.260]] |
> | Table B-22: IMP_CPUACTLR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0260-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=260\|p.260]] |
> | Figure B-7: AArch64_imp_cpuactlr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0261-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=261\|p.261]] |
> | Table B-25: IMP_CPUACTLR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0262-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=262\|p.262]] |
> | Figure B-8: AArch64_imp_cpuactlr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0263-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=263\|p.263]] |
> | Table B-28: IMP_CPUACTLR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0263-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=263\|p.263]] |
> | Figure B-9: AArch64_imp_cpuactlr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0265-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=265\|p.265]] |
> | Table B-31: IMP_CPUACTLR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0265-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=265\|p.265]] |
> | Figure B-10: AArch64_imp_cpuectlr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0267-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=267\|p.267]] |
> | Table B-34: IMP_CPUECTLR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0267-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=267\|p.267]] |
> | 续表或相关原文（第268页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0268-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=268\|p.268]] |
> | 续表或相关原文（第269页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0269-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=269\|p.269]] |
> | 续表或相关原文（第270页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0270-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=270\|p.270]] |
> | 续表或相关原文（第271页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0271-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=271\|p.271]] |
> | 续表或相关原文（第272页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0272-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=272\|p.272]] |
> | 续表或相关原文（第273页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0273-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=273\|p.273]] |
> | 续表或相关原文（第274页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0274-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=274\|p.274]] |
> | Figure B-11: AArch64_imp_cpuectlr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0276-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=276\|p.276]] |
> | Table B-37: IMP_CPUECTLR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0276-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=276\|p.276]] |
> | 续表或相关原文（第277页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0277-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=277\|p.277]] |
> | 续表或相关原文（第278页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0278-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=278\|p.278]] |
> | 续表或相关原文（第279页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0279-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=279\|p.279]] |
> | Figure B-12: AArch64_imp_cpuppmcr3_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0281-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=281\|p.281]] |
> | Table B-40: IMP_CPUPPMCR3_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0281-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=281\|p.281]] |
> | Figure B-13: AArch64_imp_cpupwrctlr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0282-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=282\|p.282]] |
> | Table B-43: IMP_CPUPWRCTLR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0282-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=282\|p.282]] |
> | 续表或相关原文（第283页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0283-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=283\|p.283]] |
> | Figure B-14: AArch64_imp_atcr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0285-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=285\|p.285]] |
> | Table B-46: IMP_ATCR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0285-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=285\|p.285]] |
> | 续表或相关原文（第286页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0286-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=286\|p.286]] |
> | Figure B-15: AArch64_imp_cpuactlr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0287-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=287\|p.287]] |
> | Table B-49: IMP_CPUACTLR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0287-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=287\|p.287]] |
> | Figure B-16: AArch64_imp_cpuactlr6_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0289-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=289\|p.289]] |
> | Table B-52: IMP_CPUACTLR6_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0289-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=289\|p.289]] |
> | Figure B-17: AArch64_imp_cpuactlr7_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0291-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=291\|p.291]] |
> | Table B-55: IMP_CPUACTLR7_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0291-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=291\|p.291]] |
> | Figure B-18: AArch64_aidr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0293-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=293\|p.293]] |
> | Table B-58: AIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0293-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=293\|p.293]] |
> | Figure B-19: AArch64_fpcr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0294-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=294\|p.294]] |
> | Table B-60: FPCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0294-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=294\|p.294]] |
> | 续表或相关原文（第295页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0295-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=295\|p.295]] |
> | Figure B-20: AArch64_fpsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0298-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=298\|p.298]] |
> | Table B-63: FPSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0298-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=298\|p.298]] |
> | 续表或相关原文（第299页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0299-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=299\|p.299]] |
> | 续表或相关原文（第300页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0300-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=300\|p.300]] |
> | Figure B-21: AArch64_actlr_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0303-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=303\|p.303]] |
> | Table B-66: ACTLR_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0303-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=303\|p.303]] |
> | 续表或相关原文（第304页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0304-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=304\|p.304]] |
> | Figure B-22: AArch64_hacr_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0306-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=306\|p.306]] |
> | Table B-69: HACR_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0306-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=306\|p.306]] |
> | Figure B-23: AArch64_afsr0_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0307-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=307\|p.307]] |
> | Table B-72: AFSR0_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0307-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=307\|p.307]] |
> | Figure B-24: AArch64_afsr1_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0310-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=310\|p.310]] |
> | Table B-77: AFSR1_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0310-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=310\|p.310]] |
> | Figure B-25: AArch64_amair_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0313-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=313\|p.313]] |
> | Table B-82: AMAIR_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0313-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=313\|p.313]] |
> | Figure B-26: AArch64_imp_atcr_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0315-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=315\|p.315]] |
> | Table B-87: IMP_ATCR_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0315-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=315\|p.315]] |
> | 续表或相关原文（第316页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0316-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=316\|p.316]] |
> | Figure B-27: AArch64_imp_avtcr_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0318-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=318\|p.318]] |
> | Table B-90: IMP_AVTCR_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0318-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=318\|p.318]] |
> | Figure B-28: AArch64_actlr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0320-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=320\|p.320]] |
> | Table B-93: ACTLR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0320-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=320\|p.320]] |
> | 续表或相关原文（第321页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0321-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=321\|p.321]] |
> | Figure B-29: AArch64_afsr0_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0323-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=323\|p.323]] |
> | Table B-96: AFSR0_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0323-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=323\|p.323]] |
> | Figure B-30: AArch64_afsr1_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0324-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=324\|p.324]] |
> | Table B-99: AFSR1_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0324-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=324\|p.324]] |
> | Figure B-31: AArch64_amair_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0326-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=326\|p.326]] |
> | Table B-102: AMAIR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0326-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=326\|p.326]] |
> | Figure B-32: AArch64_rmr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0328-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=328\|p.328]] |
> | Table B-105: RMR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0328-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=328\|p.328]] |
> | Figure B-33: AArch64_imp_cpuppmcr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0329-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=329\|p.329]] |
> | Table B-108: IMP_CPUPPMCR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0329-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=329\|p.329]] |
> | Figure B-34: AArch64_imp_cpuppmcr2_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0331-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=331\|p.331]] |
> | Table B-111: IMP_CPUPPMCR2_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0331-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=331\|p.331]] |
> | Figure B-35: AArch64_imp_cpuppmcr4_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0332-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=332\|p.332]] |
> | Table B-114: IMP_CPUPPMCR4_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0332-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=332\|p.332]] |
> | Figure B-36: AArch64_imp_cpuppmcr5_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0334-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=334\|p.334]] |
> | Table B-117: IMP_CPUPPMCR5_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0334-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=334\|p.334]] |
> | Figure B-37: AArch64_imp_cpuppmcr6_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0335-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=335\|p.335]] |
> | Table B-120: IMP_CPUPPMCR6_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0336-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=336\|p.336]] |
> | Figure B-38: AArch64_imp_cpuactlr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0337-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=337\|p.337]] |
> | Table B-123: IMP_CPUACTLR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0337-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=337\|p.337]] |
> | Figure B-39: AArch64_imp_atcr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0339-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=339\|p.339]] |
> | Table B-126: IMP_ATCR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0339-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=339\|p.339]] |
> | Figure B-40: AArch64_imp_cpupselr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0341-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=341\|p.341]] |
> | Table B-129: IMP_CPUPSELR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0341-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=341\|p.341]] |
> | Figure B-41: AArch64_imp_cpupcr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0342-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=342\|p.342]] |
> | Table B-132: IMP_CPUPCR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0342-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=342\|p.342]] |
> | Figure B-42: AArch64_imp_cpupor_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0344-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=344\|p.344]] |
> | Table B-135: IMP_CPUPOR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0344-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=344\|p.344]] |
> | Figure B-43: AArch64_imp_cpupmr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0345-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=345\|p.345]] |
> | Table B-138: IMP_CPUPMR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0345-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=345\|p.345]] |
> | Figure B-44: AArch64_imp_cpupor2_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0347-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=347\|p.347]] |
> | Table B-141: IMP_CPUPOR2_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0347-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=347\|p.347]] |
> | Figure B-45: AArch64_imp_cpupmr2_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0348-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=348\|p.348]] |
> | Table B-144: IMP_CPUPMR2_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0348-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=348\|p.348]] |
> | Figure B-46: AArch64_imp_cpupfr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0350-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=350\|p.350]] |
> | Table B-147: IMP_CPUPFR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0350-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=350\|p.350]] |
> | Table B-150: Debug registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0351-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351\|p.351]] |
> | 续表或相关原文（第352页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0352-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352\|p.352]] |
> | Figure B-47: AArch64_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0353-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=353\|p.353]] |
> | Table B-151: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0354-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=354\|p.354]] |
> | Figure B-48: AArch64_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0354-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=354\|p.354]] |
> | Table B-152: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0354-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=354\|p.354]] |
> | Figure B-49: AArch64_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0354-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=354\|p.354]] |
> | Table B-153: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0355-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=355\|p.355]] |
> | Figure B-50: AArch64_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0355-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=355\|p.355]] |
> | Table B-154: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0355-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=355\|p.355]] |
> | Figure B-51: AArch64_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0355-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=355\|p.355]] |
> | Table B-155: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0355-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=355\|p.355]] |
> | Figure B-52: AArch64_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0356-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=356\|p.356]] |
> | Table B-156: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0356-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=356\|p.356]] |
> | Figure B-53: AArch64_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0356-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=356\|p.356]] |
> | Table B-157: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0356-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=356\|p.356]] |
> | Figure B-54: AArch64_dbgbcr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0358-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=358\|p.358]] |
> | Table B-160: DBGBCR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0359-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=359\|p.359]] |
> | 续表或相关原文（第360页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0360-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=360\|p.360]] |
> | 续表或相关原文（第361页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0361-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=361\|p.361]] |
> | Table B-161: BAS description | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0362-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=362\|p.362]] |
> | Figure B-55: AArch64_dbgwvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0364-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=364\|p.364]] |
> | Table B-164: DBGWVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0364-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=364\|p.364]] |
> | Figure B-56: AArch64_dbgwcr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0366-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=366\|p.366]] |
> | Table B-167: DBGWCR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0366-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=366\|p.366]] |
> | 续表或相关原文（第367页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0367-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=367\|p.367]] |
> | Table B-168: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0368-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=368\|p.368]] |
> | Table B-169: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0368-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=368\|p.368]] |
> | Figure B-57: AArch64_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0371-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=371\|p.371]] |
> | Table B-172: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0371-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=371\|p.371]] |
> | Figure B-58: AArch64_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0372-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=372\|p.372]] |
> | Table B-173: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0372-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=372\|p.372]] |
> | Figure B-59: AArch64_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0372-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=372\|p.372]] |
> | Table B-174: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0372-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=372\|p.372]] |
> | Figure B-60: AArch64_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0373-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=373\|p.373]] |
> | Table B-175: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0373-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=373\|p.373]] |
> | Figure B-61: AArch64_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0373-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=373\|p.373]] |
> | Table B-176: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0373-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=373\|p.373]] |
> | Figure B-62: AArch64_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0374-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=374\|p.374]] |
> | Table B-177: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0374-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=374\|p.374]] |
> | Figure B-63: AArch64_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0374-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=374\|p.374]] |
> | Table B-178: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0374-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=374\|p.374]] |
> | Figure B-64: AArch64_dbgbcr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0376-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=376\|p.376]] |
> | Table B-181: DBGBCR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0376-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=376\|p.376]] |
> | 续表或相关原文（第377页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0377-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=377\|p.377]] |
> | 续表或相关原文（第378页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0378-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=378\|p.378]] |
> | Table B-182: BAS description | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0379-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=379\|p.379]] |
> | Figure B-65: AArch64_dbgwvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0381-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=381\|p.381]] |
> | Table B-185: DBGWVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0381-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=381\|p.381]] |
> | Figure B-66: AArch64_dbgwcr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0383-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=383\|p.383]] |
> | Table B-188: DBGWCR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0384-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=384\|p.384]] |
> | Table B-189: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0385-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=385\|p.385]] |
> | Table B-190: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0385-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=385\|p.385]] |
> | Figure B-67: AArch64_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0388-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=388\|p.388]] |
> | Table B-193: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0389-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=389\|p.389]] |
> | Figure B-68: AArch64_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0389-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=389\|p.389]] |
> | Table B-194: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0389-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=389\|p.389]] |
> | Figure B-69: AArch64_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0389-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=389\|p.389]] |
> | Table B-195: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0390-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=390\|p.390]] |
> | Figure B-70: AArch64_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0390-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=390\|p.390]] |
> | Table B-196: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0390-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=390\|p.390]] |
> | Figure B-71: AArch64_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0390-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=390\|p.390]] |
> | Table B-197: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0390-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=390\|p.390]] |
> | Figure B-72: AArch64_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0391-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=391\|p.391]] |
> | Table B-198: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0391-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=391\|p.391]] |
> | Figure B-73: AArch64_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0391-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=391\|p.391]] |
> | Table B-199: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0391-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=391\|p.391]] |
> | Figure B-74: AArch64_dbgbcr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0393-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=393\|p.393]] |
> | Table B-202: DBGBCR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0394-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=394\|p.394]] |
> | 续表或相关原文（第395页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0395-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=395\|p.395]] |
> | 续表或相关原文（第396页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0396-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=396\|p.396]] |
> | Table B-203: BAS description | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0397-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=397\|p.397]] |
> | Figure B-75: AArch64_dbgwvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0399-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=399\|p.399]] |
> | Table B-206: DBGWVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0399-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=399\|p.399]] |
> | Figure B-76: AArch64_dbgwcr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0401-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=401\|p.401]] |
> | Table B-209: DBGWCR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0402-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=402\|p.402]] |
> | Table B-210: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0403-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=403\|p.403]] |
> | Table B-211: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0403-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=403\|p.403]] |
> | Figure B-77: AArch64_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0406-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=406\|p.406]] |
> | Table B-214: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0407-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=407\|p.407]] |
> | Figure B-78: AArch64_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0407-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=407\|p.407]] |
> | Table B-215: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0407-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=407\|p.407]] |
> | Figure B-79: AArch64_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0407-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=407\|p.407]] |
> | Table B-216: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0408-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=408\|p.408]] |
> | Figure B-80: AArch64_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0408-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=408\|p.408]] |
> | Table B-217: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0408-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=408\|p.408]] |
> | Figure B-81: AArch64_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0408-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=408\|p.408]] |
> | Table B-218: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0408-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=408\|p.408]] |
> | Figure B-82: AArch64_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0409-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=409\|p.409]] |
> | Table B-219: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0409-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=409\|p.409]] |
> | Figure B-83: AArch64_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0409-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=409\|p.409]] |
> | Table B-220: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0409-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=409\|p.409]] |
> | Figure B-84: AArch64_dbgbcr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0411-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=411\|p.411]] |
> | Table B-223: DBGBCR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0412-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=412\|p.412]] |
> | 续表或相关原文（第413页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0413-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=413\|p.413]] |
> | 续表或相关原文（第414页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0414-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=414\|p.414]] |
> | Table B-224: BAS description | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0415-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=415\|p.415]] |
> | Figure B-85: AArch64_dbgwvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0417-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=417\|p.417]] |
> | Table B-227: DBGWVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0417-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=417\|p.417]] |
> | Figure B-86: AArch64_dbgwcr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0419-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=419\|p.419]] |
> | Table B-230: DBGWCR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0420-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=420\|p.420]] |
> | Table B-231: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0421-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=421\|p.421]] |
> | Table B-232: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0421-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=421\|p.421]] |
> | Figure B-87: AArch64_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0424-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=424\|p.424]] |
> | Table B-235: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0425-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=425\|p.425]] |
> | Figure B-88: AArch64_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0425-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=425\|p.425]] |
> | Table B-236: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0425-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=425\|p.425]] |
> | Figure B-89: AArch64_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0425-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=425\|p.425]] |
> | Table B-237: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0426-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=426\|p.426]] |
> | Figure B-90: AArch64_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0426-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=426\|p.426]] |
> | Table B-238: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0426-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=426\|p.426]] |
> | Figure B-91: AArch64_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0426-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=426\|p.426]] |
> | Table B-239: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0426-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=426\|p.426]] |
> | Figure B-92: AArch64_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0427-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=427\|p.427]] |
> | Table B-240: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0427-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=427\|p.427]] |
> | Figure B-93: AArch64_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0427-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=427\|p.427]] |
> | Table B-241: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0427-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=427\|p.427]] |
> | Figure B-94: AArch64_dbgbcr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0429-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=429\|p.429]] |
> | Table B-244: DBGBCR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0430-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=430\|p.430]] |
> | 续表或相关原文（第431页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0431-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=431\|p.431]] |
> | 续表或相关原文（第432页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0432-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=432\|p.432]] |
> | Table B-245: BAS description | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0433-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=433\|p.433]] |
> | Figure B-95: AArch64_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0436-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=436\|p.436]] |
> | Table B-248: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0436-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=436\|p.436]] |
> | Figure B-96: AArch64_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0436-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=436\|p.436]] |
> | Table B-249: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0436-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=436\|p.436]] |
> | Figure B-97: AArch64_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0437-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=437\|p.437]] |
> | Table B-250: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0437-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=437\|p.437]] |
> | Figure B-98: AArch64_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0437-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=437\|p.437]] |
> | Table B-251: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0437-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=437\|p.437]] |
> | Figure B-99: AArch64_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0438-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=438\|p.438]] |
> | Table B-252: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0438-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=438\|p.438]] |
> | Figure B-100: AArch64_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0438-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=438\|p.438]] |
> | Table B-253: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0438-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=438\|p.438]] |
> | Figure B-101: AArch64_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0439-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=439\|p.439]] |
> | Table B-254: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0439-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=439\|p.439]] |
> | Figure B-102: AArch64_dbgbcr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0441-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=441\|p.441]] |
> | Table B-257: DBGBCR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0441-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=441\|p.441]] |
> | 续表或相关原文（第442页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0442-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=442\|p.442]] |
> | 续表或相关原文（第443页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0443-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=443\|p.443]] |
> | Table B-258: BAS description | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0444-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=444\|p.444]] |
> | Figure B-103: AArch64_imp_idata0_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0446-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=446\|p.446]] |
> | Table B-261: IMP_IDATA0_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0446-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=446\|p.446]] |
> | Figure B-104: AArch64_imp_idata1_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0447-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=447\|p.447]] |
> | Table B-263: IMP_IDATA1_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0447-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=447\|p.447]] |
> | Figure B-105: AArch64_imp_idata2_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0448-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=448\|p.448]] |
> | Table B-265: IMP_IDATA2_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0449-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=449\|p.449]] |
> | Figure B-106: AArch64_imp_ddata0_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0450-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=450\|p.450]] |
> | Table B-267: IMP_DDATA0_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0450-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=450\|p.450]] |
> | Figure B-107: AArch64_imp_ddata1_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0451-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=451\|p.451]] |
> | Table B-269: IMP_DDATA1_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0451-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=451\|p.451]] |
> | Figure B-108: AArch64_imp_ddata2_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0452-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=452\|p.452]] |
> | Table B-271: IMP_DDATA2_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0452-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=452\|p.452]] |
> | Table B-273: Random Number Control registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0453-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453\|p.453]] |
> | Figure B-109: AArch64_imp_cpurndbr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0454-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=454\|p.454]] |
> | Table B-274: IMP_CPURNDBR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0454-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=454\|p.454]] |
> | Figure B-110: AArch64_imp_cpurndpeid_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0455-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=455\|p.455]] |
> | Table B-277: IMP_CPURNDPEID_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0455-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=455\|p.455]] |
> | 续表或相关原文（第456页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0456-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=456\|p.456]] |
> | Table B-280: System instructions summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0457-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=457\|p.457]] |
> | Figure B-111: AArch64_sys_imp_ramindex bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0457-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=457\|p.457]] |
> | Table B-281: SYS_IMP_RAMINDEX bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0457-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=457\|p.457]] |
> | Table B-283: Identification registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0458-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458\|p.458]] |
> | 续表或相关原文（第459页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0459-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459\|p.459]] |
> | Figure B-112: AArch64_midr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0460-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=460\|p.460]] |
> | Table B-284: MIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0460-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=460\|p.460]] |
> | 续表或相关原文（第461页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0461-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=461\|p.461]] |
> | Figure B-113: AArch64_mpidr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0462-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=462\|p.462]] |
> | Table B-286: MPIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0462-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=462\|p.462]] |
> | Figure B-114: AArch64_revidr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0464-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=464\|p.464]] |
> | Table B-288: REVIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0464-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=464\|p.464]] |
> | Figure B-115: AArch64_id_pfr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0465-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=465\|p.465]] |
> | Table B-290: ID_PFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0465-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=465\|p.465]] |
> | 续表或相关原文（第466页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0466-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=466\|p.466]] |
> | Figure B-116: AArch64_id_pfr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0467-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=467\|p.467]] |
> | Table B-292: ID_PFR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0467-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=467\|p.467]] |
> | 续表或相关原文（第468页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0468-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=468\|p.468]] |
> | Figure B-117: AArch64_id_dfr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0470-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=470\|p.470]] |
> | Table B-294: ID_DFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0470-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=470\|p.470]] |
> | 续表或相关原文（第471页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0471-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=471\|p.471]] |
> | Figure B-118: AArch64_id_afr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0472-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=472\|p.472]] |
> | Table B-296: ID_AFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0472-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=472\|p.472]] |
> | Figure B-119: AArch64_id_mmfr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0473-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=473\|p.473]] |
> | Table B-298: ID_MMFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0473-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=473\|p.473]] |
> | 续表或相关原文（第474页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0474-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=474\|p.474]] |
> | Figure B-120: AArch64_id_mmfr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0475-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=475\|p.475]] |
> | Table B-300: ID_MMFR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0476-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=476\|p.476]] |
> | Figure B-121: AArch64_id_mmfr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0478-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=478\|p.478]] |
> | Table B-302: ID_MMFR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0478-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=478\|p.478]] |
> | 续表或相关原文（第479页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0479-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=479\|p.479]] |
> | Figure B-122: AArch64_id_mmfr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0480-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=480\|p.480]] |
> | Table B-304: ID_MMFR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0480-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=480\|p.480]] |
> | 续表或相关原文（第481页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0481-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=481\|p.481]] |
> | Figure B-123: AArch64_id_isar0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0482-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=482\|p.482]] |
> | Table B-306: ID_ISAR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0483-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=483\|p.483]] |
> | Figure B-124: AArch64_id_isar1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0484-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=484\|p.484]] |
> | Table B-308: ID_ISAR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0485-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=485\|p.485]] |
> | Figure B-125: AArch64_id_isar2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0487-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=487\|p.487]] |
> | Table B-310: ID_ISAR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0487-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=487\|p.487]] |
> | 续表或相关原文（第488页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0488-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=488\|p.488]] |
> | Figure B-126: AArch64_id_isar3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0489-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=489\|p.489]] |
> | Table B-312: ID_ISAR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0489-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=489\|p.489]] |
> | 续表或相关原文（第490页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0490-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=490\|p.490]] |
> | Figure B-127: AArch64_id_isar4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0491-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=491\|p.491]] |
> | Table B-314: ID_ISAR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0491-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=491\|p.491]] |
> | 续表或相关原文（第492页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0492-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=492\|p.492]] |
> | Figure B-128: AArch64_id_isar5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0493-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=493\|p.493]] |
> | Table B-316: ID_ISAR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0493-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=493\|p.493]] |
> | 续表或相关原文（第494页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0494-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=494\|p.494]] |
> | Figure B-129: AArch64_id_mmfr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0496-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=496\|p.496]] |
> | Table B-318: ID_MMFR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0496-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=496\|p.496]] |
> | 续表或相关原文（第497页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0497-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=497\|p.497]] |
> | Figure B-130: AArch64_id_isar6_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0498-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=498\|p.498]] |
> | Table B-320: ID_ISAR6_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0498-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=498\|p.498]] |
> | 续表或相关原文（第499页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0499-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=499\|p.499]] |
> | Figure B-131: AArch64_mvfr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0500-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=500\|p.500]] |
> | Table B-322: MVFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0501-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=501\|p.501]] |
> | Figure B-132: AArch64_mvfr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0503-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=503\|p.503]] |
> | Table B-324: MVFR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0503-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=503\|p.503]] |
> | 续表或相关原文（第504页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0504-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=504\|p.504]] |
> | Figure B-133: AArch64_mvfr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0505-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=505\|p.505]] |
> | Table B-326: MVFR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0505-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=505\|p.505]] |
> | Figure B-134: AArch64_id_pfr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0507-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=507\|p.507]] |
> | Table B-328: ID_PFR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0507-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=507\|p.507]] |
> | Figure B-135: AArch64_id_dfr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0508-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=508\|p.508]] |
> | Table B-330: ID_DFR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0508-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=508\|p.508]] |
> | Figure B-136: AArch64_id_mmfr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0510-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=510\|p.510]] |
> | Table B-332: ID_MMFR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0510-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=510\|p.510]] |
> | Figure B-137: AArch64_id_aa64pfr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0511-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=511\|p.511]] |
> | Table B-334: ID_AA64PFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0512-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=512\|p.512]] |
> | 续表或相关原文（第513页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0513-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=513\|p.513]] |
> | Figure B-138: AArch64_id_aa64pfr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0514-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=514\|p.514]] |
> | Table B-336: ID_AA64PFR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0514-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=514\|p.514]] |
> | 续表或相关原文（第515页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0515-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=515\|p.515]] |
> | Figure B-139: AArch64_id_aa64pfr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0516-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=516\|p.516]] |
> | Table B-338: ID_AA64PFR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0516-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=516\|p.516]] |
> | Figure B-140: AArch64_id_aa64zfr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0518-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=518\|p.518]] |
> | Table B-340: ID_AA64ZFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0518-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=518\|p.518]] |
> | 续表或相关原文（第519页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0519-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=519\|p.519]] |
> | Figure B-141: AArch64_id_aa64dfr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0520-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=520\|p.520]] |
> | Table B-342: ID_AA64DFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0521-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=521\|p.521]] |
> | Figure B-142: AArch64_id_aa64dfr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0523-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=523\|p.523]] |
> | Table B-344: ID_AA64DFR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0523-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=523\|p.523]] |
> | Figure B-143: AArch64_id_aa64afr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0524-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=524\|p.524]] |
> | Table B-346: ID_AA64AFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0524-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=524\|p.524]] |
> | Figure B-144: AArch64_id_aa64afr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0525-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=525\|p.525]] |
> | Table B-348: ID_AA64AFR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0526-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=526\|p.526]] |
> | Figure B-145: AArch64_id_aa64isar0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0527-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=527\|p.527]] |
> | Table B-350: ID_AA64ISAR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0527-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=527\|p.527]] |
> | 续表或相关原文（第528页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0528-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=528\|p.528]] |
> | 续表或相关原文（第529页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0529-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=529\|p.529]] |
> | Figure B-146: AArch64_id_aa64isar1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0531-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=531\|p.531]] |
> | Table B-352: ID_AA64ISAR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0531-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=531\|p.531]] |
> | 续表或相关原文（第532页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0532-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=532\|p.532]] |
> | Figure B-147: AArch64_id_aa64isar2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0534-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=534\|p.534]] |
> | Table B-354: ID_AA64ISAR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0534-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=534\|p.534]] |
> | Figure B-148: AArch64_id_aa64mmfr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0535-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=535\|p.535]] |
> | Table B-356: ID_AA64MMFR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0535-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=535\|p.535]] |
> | 续表或相关原文（第536页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0536-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=536\|p.536]] |
> | Figure B-149: AArch64_id_aa64mmfr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0538-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=538\|p.538]] |
> | Table B-358: ID_AA64MMFR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0538-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=538\|p.538]] |
> | 续表或相关原文（第539页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0539-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=539\|p.539]] |
> | Figure B-150: AArch64_id_aa64mmfr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0541-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=541\|p.541]] |
> | Table B-360: ID_AA64MMFR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0541-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=541\|p.541]] |
> | 续表或相关原文（第542页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0542-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=542\|p.542]] |
> | Figure B-151: AArch64_mpamidr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0543-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=543\|p.543]] |
> | Table B-362: MPAMIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0544-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=544\|p.544]] |
> | Figure B-152: AArch64_imp_cpucfr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0545-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=545\|p.545]] |
> | Table B-364: IMP_CPUCFR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0545-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=545\|p.545]] |
> | 续表或相关原文（第546页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0546-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=546\|p.546]] |
> | Figure B-153: AArch64_clidr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0547-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=547\|p.547]] |
> | Table B-366: CLIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0547-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=547\|p.547]] |
> | 续表或相关原文（第548页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0548-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=548\|p.548]] |
> | 续表或相关原文（第549页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0549-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=549\|p.549]] |
> | 续表或相关原文（第550页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0550-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=550\|p.550]] |
> | Figure B-154: AArch64_gmid_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0551-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=551\|p.551]] |
> | Table B-368: GMID_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0551-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=551\|p.551]] |
> | Figure B-155: AArch64_ctr_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0552-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=552\|p.552]] |
> | Table B-370: CTR_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0553-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=553\|p.553]] |
> | Figure B-156: AArch64_dczid_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0555-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=555\|p.555]] |
> | Table B-372: DCZID_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0555-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=555\|p.555]] |
> | Table B-374: Special-purpose registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0556-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556\|p.556]] |
> | Table B-375: Performance Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0556-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556\|p.556]] |
> | 续表或相关原文（第557页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0557-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557\|p.557]] |
> | Figure B-157: AArch64_pmmir_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0558-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558\|p.558]] |
> | Table B-376: PMMIR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0559-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=559\|p.559]] |
> | 续表或相关原文（第560页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0560-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=560\|p.560]] |
> | Figure B-158: AArch64_pmcr_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0561-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=561\|p.561]] |
> | Table B-378: PMCR_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0561-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=561\|p.561]] |
> | 续表或相关原文（第562页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0562-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=562\|p.562]] |
> | 续表或相关原文（第563页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0563-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=563\|p.563]] |
> | 续表或相关原文（第564页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0564-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=564\|p.564]] |
> | Figure B-159: AArch64_pmceid0_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0567-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=567\|p.567]] |
> | Table B-381: PMCEID0_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0567-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=567\|p.567]] |
> | 续表或相关原文（第568页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0568-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=568\|p.568]] |
> | 续表或相关原文（第569页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0569-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=569\|p.569]] |
> | 续表或相关原文（第570页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0570-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=570\|p.570]] |
> | 续表或相关原文（第571页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0571-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=571\|p.571]] |
> | 续表或相关原文（第572页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0572-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=572\|p.572]] |
> | Figure B-160: AArch64_pmceid1_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0574-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=574\|p.574]] |
> | Table B-383: PMCEID1_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0574-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=574\|p.574]] |
> | 续表或相关原文（第575页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0575-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=575\|p.575]] |
> | 续表或相关原文（第576页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0576-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=576\|p.576]] |
> | 续表或相关原文（第577页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0577-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=577\|p.577]] |
> | 续表或相关原文（第578页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0578-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=578\|p.578]] |
> | 续表或相关原文（第579页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0579-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=579\|p.579]] |
> | Figure B-161: AArch64_pmevcntr0_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0580-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=580\|p.580]] |
> | Table B-385: PMEVCNTR0_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0580-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=580\|p.580]] |
> | Figure B-162: AArch64_pmevcntr1_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0584-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=584\|p.584]] |
> | Table B-388: PMEVCNTR1_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0584-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=584\|p.584]] |
> | Figure B-163: AArch64_pmevcntr2_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0588-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=588\|p.588]] |
> | Table B-391: PMEVCNTR2_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0588-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=588\|p.588]] |
> | Figure B-164: AArch64_pmevcntr3_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0591-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=591\|p.591]] |
> | Table B-394: PMEVCNTR3_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0591-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=591\|p.591]] |
> | Figure B-165: AArch64_pmevcntr4_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0595-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=595\|p.595]] |
> | Table B-397: PMEVCNTR4_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0595-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=595\|p.595]] |
> | Figure B-166: AArch64_pmevcntr5_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0599-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=599\|p.599]] |
> | Table B-400: PMEVCNTR5_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0599-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=599\|p.599]] |
> | Figure B-167: AArch64_pmevtyper0_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0602-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=602\|p.602]] |
> | Table B-403: PMEVTYPER0_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0602-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=602\|p.602]] |
> | 续表或相关原文（第603页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0603-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=603\|p.603]] |
> | 续表或相关原文（第604页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0604-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=604\|p.604]] |
> | Figure B-168: AArch64_pmevtyper1_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0607-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=607\|p.607]] |
> | Table B-406: PMEVTYPER1_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0608-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=608\|p.608]] |
> | 续表或相关原文（第609页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0609-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=609\|p.609]] |
> | Figure B-169: AArch64_pmevtyper2_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0613-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=613\|p.613]] |
> | Table B-409: PMEVTYPER2_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0613-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=613\|p.613]] |
> | 续表或相关原文（第614页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0614-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=614\|p.614]] |
> | Figure B-170: AArch64_pmevtyper3_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0618-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=618\|p.618]] |
> | Table B-412: PMEVTYPER3_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0618-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=618\|p.618]] |
> | 续表或相关原文（第619页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0619-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=619\|p.619]] |
> | Figure B-171: AArch64_pmevtyper4_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0623-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=623\|p.623]] |
> | Table B-415: PMEVTYPER4_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0623-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=623\|p.623]] |
> | 续表或相关原文（第624页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0624-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=624\|p.624]] |
> | 续表或相关原文（第625页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0625-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=625\|p.625]] |
> | Figure B-172: AArch64_pmevtyper5_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0628-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=628\|p.628]] |
> | Table B-418: PMEVTYPER5_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0628-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=628\|p.628]] |
> | 续表或相关原文（第629页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0629-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=629\|p.629]] |
> | 续表或相关原文（第630页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0630-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=630\|p.630]] |
> | Table B-421: GIC system registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0633-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633\|p.633]] |
> | 续表或相关原文（第634页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0634-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634\|p.634]] |
> | 续表或相关原文（第635页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0635-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635\|p.635]] |
> | Figure B-173: AArch64_icc_ap0r0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0636-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=636\|p.636]] |
> | Table B-422: ICC_AP0R0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0636-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=636\|p.636]] |
> | 续表或相关原文（第637页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0637-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=637\|p.637]] |
> | 续表或相关原文（第638页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0638-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=638\|p.638]] |
> | 续表或相关原文（第639页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0639-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=639\|p.639]] |
> | 续表或相关原文（第640页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0640-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=640\|p.640]] |
> | 续表或相关原文（第641页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0641-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=641\|p.641]] |
> | 续表或相关原文（第642页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0642-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=642\|p.642]] |
> | Figure B-174: AArch64_icv_ap0r0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0646-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=646\|p.646]] |
> | Table B-425: ICV_AP0R0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0646-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=646\|p.646]] |
> | 续表或相关原文（第647页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0647-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=647\|p.647]] |
> | 续表或相关原文（第648页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0648-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=648\|p.648]] |
> | 续表或相关原文（第649页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0649-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=649\|p.649]] |
> | 续表或相关原文（第650页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0650-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=650\|p.650]] |
> | 续表或相关原文（第651页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0651-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=651\|p.651]] |
> | 续表或相关原文（第652页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0652-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=652\|p.652]] |
> | Figure B-175: AArch64_icc_ap1r0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0655-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=655\|p.655]] |
> | Table B-428: ICC_AP1R0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0655-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=655\|p.655]] |
> | 续表或相关原文（第656页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0656-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=656\|p.656]] |
> | 续表或相关原文（第657页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0657-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=657\|p.657]] |
> | 续表或相关原文（第658页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0658-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=658\|p.658]] |
> | 续表或相关原文（第659页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0659-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=659\|p.659]] |
> | 续表或相关原文（第660页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0660-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=660\|p.660]] |
> | 续表或相关原文（第661页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0661-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=661\|p.661]] |
> | 续表或相关原文（第662页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0662-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=662\|p.662]] |
> | 续表或相关原文（第663页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0663-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=663\|p.663]] |
> | 续表或相关原文（第664页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0664-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=664\|p.664]] |
> | 续表或相关原文（第665页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0665-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=665\|p.665]] |
> | 续表或相关原文（第666页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0666-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=666\|p.666]] |
> | Figure B-176: AArch64_icv_ap1r0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0670-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=670\|p.670]] |
> | Table B-431: ICV_AP1R0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0670-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=670\|p.670]] |
> | 续表或相关原文（第671页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0671-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=671\|p.671]] |
> | 续表或相关原文（第672页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0672-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=672\|p.672]] |
> | 续表或相关原文（第673页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0673-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=673\|p.673]] |
> | 续表或相关原文（第674页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0674-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=674\|p.674]] |
> | 续表或相关原文（第675页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0675-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=675\|p.675]] |
> | 续表或相关原文（第676页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0676-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=676\|p.676]] |
> | Figure B-177: AArch64_icc_ctlr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0679-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=679\|p.679]] |
> | Table B-434: ICC_CTLR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0679-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=679\|p.679]] |
> | 续表或相关原文（第680页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0680-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=680\|p.680]] |
> | 续表或相关原文（第681页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0681-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=681\|p.681]] |
> | Figure B-178: AArch64_icv_ctlr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0684-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=684\|p.684]] |
> | Table B-437: ICV_CTLR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0684-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=684\|p.684]] |
> | 续表或相关原文（第685页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0685-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=685\|p.685]] |
> | Figure B-179: AArch64_ich_ap0r0_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0687-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=687\|p.687]] |
> | Table B-440: ICH_AP0R0_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0688-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=688\|p.688]] |
> | 续表或相关原文（第689页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0689-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=689\|p.689]] |
> | 续表或相关原文（第690页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0690-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=690\|p.690]] |
> | 续表或相关原文（第691页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0691-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=691\|p.691]] |
> | 续表或相关原文（第692页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0692-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=692\|p.692]] |
> | 续表或相关原文（第693页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0693-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=693\|p.693]] |
> | 续表或相关原文（第694页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0694-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=694\|p.694]] |
> | 续表或相关原文（第695页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0695-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=695\|p.695]] |
> | 续表或相关原文（第696页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0696-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=696\|p.696]] |
> | 续表或相关原文（第697页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0697-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=697\|p.697]] |
> | 续表或相关原文（第698页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0698-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=698\|p.698]] |
> | 续表或相关原文（第699页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0699-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=699\|p.699]] |
> | 续表或相关原文（第700页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0700-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=700\|p.700]] |
> | 续表或相关原文（第701页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0701-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=701\|p.701]] |
> | 续表或相关原文（第702页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0702-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=702\|p.702]] |
> | 续表或相关原文（第703页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0703-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=703\|p.703]] |
> | 续表或相关原文（第704页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0704-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=704\|p.704]] |
> | 续表或相关原文（第705页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0705-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=705\|p.705]] |
> | 续表或相关原文（第706页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0706-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=706\|p.706]] |
> | 续表或相关原文（第707页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0707-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=707\|p.707]] |
> | 续表或相关原文（第708页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0708-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=708\|p.708]] |
> | 续表或相关原文（第709页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0709-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=709\|p.709]] |
> | 续表或相关原文（第710页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0710-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=710\|p.710]] |
> | 续表或相关原文（第711页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0711-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=711\|p.711]] |
> | 续表或相关原文（第712页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0712-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=712\|p.712]] |
> | 续表或相关原文（第713页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0713-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=713\|p.713]] |
> | 续表或相关原文（第714页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0714-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=714\|p.714]] |
> | 续表或相关原文（第715页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0715-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=715\|p.715]] |
> | 续表或相关原文（第716页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0716-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=716\|p.716]] |
> | 续表或相关原文（第717页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0717-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=717\|p.717]] |
> | 续表或相关原文（第718页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0718-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=718\|p.718]] |
> | 续表或相关原文（第719页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0719-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=719\|p.719]] |
> | Figure B-180: AArch64_ich_ap1r0_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0722-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=722\|p.722]] |
> | Table B-443: ICH_AP1R0_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0723-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=723\|p.723]] |
> | 续表或相关原文（第724页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0724-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=724\|p.724]] |
> | 续表或相关原文（第725页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0725-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=725\|p.725]] |
> | 续表或相关原文（第726页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0726-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=726\|p.726]] |
> | 续表或相关原文（第727页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0727-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=727\|p.727]] |
> | 续表或相关原文（第728页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0728-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=728\|p.728]] |
> | 续表或相关原文（第729页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0729-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=729\|p.729]] |
> | 续表或相关原文（第730页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0730-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=730\|p.730]] |
> | 续表或相关原文（第731页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0731-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=731\|p.731]] |
> | 续表或相关原文（第732页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0732-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=732\|p.732]] |
> | 续表或相关原文（第733页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0733-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=733\|p.733]] |
> | 续表或相关原文（第734页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0734-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=734\|p.734]] |
> | 续表或相关原文（第735页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0735-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=735\|p.735]] |
> | 续表或相关原文（第736页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0736-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=736\|p.736]] |
> | 续表或相关原文（第737页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0737-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=737\|p.737]] |
> | 续表或相关原文（第738页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0738-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=738\|p.738]] |
> | 续表或相关原文（第739页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0739-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=739\|p.739]] |
> | 续表或相关原文（第740页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0740-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=740\|p.740]] |
> | 续表或相关原文（第741页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0741-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=741\|p.741]] |
> | 续表或相关原文（第742页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0742-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=742\|p.742]] |
> | 续表或相关原文（第743页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0743-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=743\|p.743]] |
> | 续表或相关原文（第744页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0744-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=744\|p.744]] |
> | 续表或相关原文（第745页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0745-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=745\|p.745]] |
> | 续表或相关原文（第746页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0746-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=746\|p.746]] |
> | 续表或相关原文（第747页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0747-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=747\|p.747]] |
> | 续表或相关原文（第748页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0748-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=748\|p.748]] |
> | 续表或相关原文（第749页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0749-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=749\|p.749]] |
> | 续表或相关原文（第750页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0750-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=750\|p.750]] |
> | 续表或相关原文（第751页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0751-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=751\|p.751]] |
> | 续表或相关原文（第752页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0752-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=752\|p.752]] |
> | 续表或相关原文（第753页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0753-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=753\|p.753]] |
> | 续表或相关原文（第754页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0754-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=754\|p.754]] |
> | Figure B-181: AArch64_ich_vtr_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0757-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=757\|p.757]] |
> | Table B-446: ICH_VTR_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0757-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=757\|p.757]] |
> | 续表或相关原文（第758页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0758-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=758\|p.758]] |
> | Figure B-182: AArch64_ich_lr0_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0759-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=759\|p.759]] |
> | Table B-448: ICH_LR0_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0759-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=759\|p.759]] |
> | 续表或相关原文（第760页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0760-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=760\|p.760]] |
> | 续表或相关原文（第761页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0761-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=761\|p.761]] |
> | Figure B-183: AArch64_ich_lr1_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0763-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=763\|p.763]] |
> | Table B-451: ICH_LR1_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0764-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=764\|p.764]] |
> | 续表或相关原文（第765页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0765-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=765\|p.765]] |
> | Figure B-184: AArch64_ich_lr2_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0767-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=767\|p.767]] |
> | Table B-454: ICH_LR2_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0768-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=768\|p.768]] |
> | 续表或相关原文（第769页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0769-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=769\|p.769]] |
> | Figure B-185: AArch64_ich_lr3_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0771-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=771\|p.771]] |
> | Table B-457: ICH_LR3_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0772-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=772\|p.772]] |
> | 续表或相关原文（第773页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0773-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=773\|p.773]] |
> | Figure B-186: AArch64_icc_ctlr_el3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0775-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=775\|p.775]] |
> | Table B-460: ICC_CTLR_EL3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0775-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=775\|p.775]] |
> | 续表或相关原文（第776页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0776-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=776\|p.776]] |
> | 续表或相关原文（第777页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0777-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=777\|p.777]] |
> | 续表或相关原文（第778页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0778-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=778\|p.778]] |
> | Table B-463: Generic Timer registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0779-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779\|p.779]] |
> | Table B-464: Other system control registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0780-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780\|p.780]] |
> | Table B-465: Activity Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0781-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781\|p.781]] |
> | 续表或相关原文（第782页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0782-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782\|p.782]] |
> | Figure B-187: AArch64_amcfgr_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0783-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=783\|p.783]] |
> | Table B-466: AMCFGR_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0783-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=783\|p.783]] |
> | Figure B-188: AArch64_amcgcr_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0785-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=785\|p.785]] |
> | Table B-468: AMCGCR_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0785-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=785\|p.785]] |
> | Figure B-189: AArch64_amevcntr00_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0787-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=787\|p.787]] |
> | Table B-470: AMEVCNTR00_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0787-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=787\|p.787]] |
> | Figure B-190: AArch64_amevcntr01_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0789-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=789\|p.789]] |
> | Table B-473: AMEVCNTR01_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0789-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=789\|p.789]] |
> | Figure B-191: AArch64_amevcntr02_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0791-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=791\|p.791]] |
> | Table B-476: AMEVCNTR02_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0791-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=791\|p.791]] |
> | Figure B-192: AArch64_amevcntr03_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0793-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=793\|p.793]] |
> | Table B-479: AMEVCNTR03_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0793-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=793\|p.793]] |
> | Figure B-193: AArch64_amevtyper00_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0795-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=795\|p.795]] |
> | Table B-482: AMEVTYPER00_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0796-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=796\|p.796]] |
> | Figure B-194: AArch64_amevtyper01_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0798-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=798\|p.798]] |
> | Table B-484: AMEVTYPER01_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0798-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=798\|p.798]] |
> | Figure B-195: AArch64_amevtyper02_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0800-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=800\|p.800]] |
> | Table B-486: AMEVTYPER02_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0800-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=800\|p.800]] |
> | Figure B-196: AArch64_amevtyper03_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0802-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=802\|p.802]] |
> | Table B-488: AMEVTYPER03_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0802-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=802\|p.802]] |
> | Figure B-197: AArch64_amevcntr10_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0804-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=804\|p.804]] |
> | Table B-490: AMEVCNTR10_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0804-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=804\|p.804]] |
> | Figure B-198: AArch64_amevcntr11_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0806-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=806\|p.806]] |
> | Table B-493: AMEVCNTR11_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0806-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=806\|p.806]] |
> | Figure B-199: AArch64_amevcntr12_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0808-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=808\|p.808]] |
> | Table B-496: AMEVCNTR12_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0809-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=809\|p.809]] |
> | Figure B-200: AArch64_amevtyper10_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0811-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=811\|p.811]] |
> | Table B-499: AMEVTYPER10_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0811-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=811\|p.811]] |
> | Figure B-201: AArch64_amevtyper11_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0813-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=813\|p.813]] |
> | Table B-501: AMEVTYPER11_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0813-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=813\|p.813]] |
> | Figure B-202: AArch64_amevtyper12_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0815-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=815\|p.815]] |
> | Table B-503: AMEVTYPER12_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0815-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=815\|p.815]] |
> | Table B-505: Trace unit registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0817-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817\|p.817]] |
> | 续表或相关原文（第818页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0818-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818\|p.818]] |
> | 续表或相关原文（第819页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0819-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819\|p.819]] |
> | 续表或相关原文（第820页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0820-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820\|p.820]] |
> | Figure B-203: AArch64_trcseqevr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0821-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=821\|p.821]] |
> | Table B-506: TRCSEQEVR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0821-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=821\|p.821]] |
> | 续表或相关原文（第822页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0822-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=822\|p.822]] |
> | Figure B-204: AArch64_trcidr8 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0825-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=825\|p.825]] |
> | Table B-509: TRCIDR8 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0825-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=825\|p.825]] |
> | Figure B-205: AArch64_trcimspec0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0826-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=826\|p.826]] |
> | Table B-511: TRCIMSPEC0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0826-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=826\|p.826]] |
> | Figure B-206: AArch64_trcseqevr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0829-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=829\|p.829]] |
> | Table B-514: TRCSEQEVR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0829-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=829\|p.829]] |
> | 续表或相关原文（第830页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0830-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=830\|p.830]] |
> | Figure B-207: AArch64_trcseqevr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0832-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=832\|p.832]] |
> | Table B-517: TRCSEQEVR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0832-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=832\|p.832]] |
> | 续表或相关原文（第833页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0833-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=833\|p.833]] |
> | 续表或相关原文（第834页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0834-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=834\|p.834]] |
> | Figure B-208: AArch64_trcidr10 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0836-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=836\|p.836]] |
> | Table B-520: TRCIDR10 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0836-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=836\|p.836]] |
> | Figure B-209: AArch64_trcidr11 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0837-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=837\|p.837]] |
> | Table B-522: TRCIDR11 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0838-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=838\|p.838]] |
> | Figure B-210: AArch64_trccntctlr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0839-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=839\|p.839]] |
> | Table B-524: TRCCNTCTLR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0839-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=839\|p.839]] |
> | 续表或相关原文（第840页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0840-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=840\|p.840]] |
> | 续表或相关原文（第841页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0841-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=841\|p.841]] |
> | Figure B-211: AArch64_trcidr12 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0843-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=843\|p.843]] |
> | Table B-527: TRCIDR12 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0843-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=843\|p.843]] |
> | Figure B-212: AArch64_trccntctlr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0845-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=845\|p.845]] |
> | Table B-529: TRCCNTCTLR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0845-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=845\|p.845]] |
> | 续表或相关原文（第846页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0846-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=846\|p.846]] |
> | Figure B-213: AArch64_trcidr13 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0848-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=848\|p.848]] |
> | Table B-532: TRCIDR13 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0849-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=849\|p.849]] |
> | Figure B-214: AArch64_trcextinselr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0850-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=850\|p.850]] |
> | Table B-534: TRCEXTINSELR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0850-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=850\|p.850]] |
> | 续表或相关原文（第851页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0851-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=851\|p.851]] |
> | Figure B-215: AArch64_trccntvr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0853-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=853\|p.853]] |
> | Table B-537: TRCCNTVR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0853-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=853\|p.853]] |
> | Figure B-216: AArch64_trcidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0856-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=856\|p.856]] |
> | Table B-540: TRCIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0856-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=856\|p.856]] |
> | 续表或相关原文（第857页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0857-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=857\|p.857]] |
> | Figure B-217: AArch64_trcextinselr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0858-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=858\|p.858]] |
> | Table B-542: TRCEXTINSELR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0859-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=859\|p.859]] |
> | Figure B-218: AArch64_trccntvr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0861-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=861\|p.861]] |
> | Table B-545: TRCCNTVR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0861-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=861\|p.861]] |
> | Figure B-219: AArch64_trcidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0864-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=864\|p.864]] |
> | Table B-548: TRCIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0864-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=864\|p.864]] |
> | Figure B-220: AArch64_trcextinselr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0866-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=866\|p.866]] |
> | Table B-550: TRCEXTINSELR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0866-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=866\|p.866]] |
> | Figure B-221: AArch64_trcidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0869-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=869\|p.869]] |
> | Table B-553: TRCIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0869-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=869\|p.869]] |
> | Figure B-222: AArch64_trcextinselr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0871-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=871\|p.871]] |
> | Table B-555: TRCEXTINSELR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0871-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=871\|p.871]] |
> | Figure B-223: AArch64_trcidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0874-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=874\|p.874]] |
> | Table B-558: TRCIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0874-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=874\|p.874]] |
> | 续表或相关原文（第875页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0875-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=875\|p.875]] |
> | Figure B-224: AArch64_trcidr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0876-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=876\|p.876]] |
> | Table B-560: TRCIDR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0877-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=877\|p.877]] |
> | Figure B-225: AArch64_trcidr5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0879-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=879\|p.879]] |
> | Table B-562: TRCIDR5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0879-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=879\|p.879]] |
> | Figure B-226: AArch64_trcssccr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0881-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=881\|p.881]] |
> | Table B-564: TRCSSCCR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0881-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=881\|p.881]] |
> | 续表或相关原文（第882页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0882-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=882\|p.882]] |
> | Figure B-227: AArch64_trcrsctlr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0884-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=884\|p.884]] |
> | Table B-567: TRCRSCTLR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0884-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=884\|p.884]] |
> | 续表或相关原文（第885页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0885-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=885\|p.885]] |
> | 续表或相关原文（第886页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0886-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=886\|p.886]] |
> | 续表或相关原文（第887页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0887-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=887\|p.887]] |
> | Figure B-228: AArch64_trcrsctlr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0891-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=891\|p.891]] |
> | Table B-570: TRCRSCTLR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0891-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=891\|p.891]] |
> | 续表或相关原文（第892页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0892-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=892\|p.892]] |
> | 续表或相关原文（第893页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0893-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=893\|p.893]] |
> | Figure B-229: AArch64_trcrsctlr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0897-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=897\|p.897]] |
> | Table B-573: TRCRSCTLR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0897-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=897\|p.897]] |
> | 续表或相关原文（第898页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0898-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=898\|p.898]] |
> | 续表或相关原文（第899页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0899-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=899\|p.899]] |
> | 续表或相关原文（第900页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0900-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=900\|p.900]] |
> | Figure B-230: AArch64_trcrsctlr5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0904-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=904\|p.904]] |
> | Table B-576: TRCRSCTLR5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0904-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=904\|p.904]] |
> | 续表或相关原文（第905页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0905-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=905\|p.905]] |
> | 续表或相关原文（第906页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0906-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=906\|p.906]] |
> | Figure B-231: AArch64_trcrsctlr6 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0910-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=910\|p.910]] |
> | Table B-579: TRCRSCTLR6 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0910-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=910\|p.910]] |
> | 续表或相关原文（第911页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0911-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=911\|p.911]] |
> | 续表或相关原文（第912页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0912-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=912\|p.912]] |
> | 续表或相关原文（第913页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0913-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=913\|p.913]] |
> | Figure B-232: AArch64_trcrsctlr7 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0917-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=917\|p.917]] |
> | Table B-582: TRCRSCTLR7 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0917-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=917\|p.917]] |
> | 续表或相关原文（第918页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0918-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=918\|p.918]] |
> | 续表或相关原文（第919页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0919-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=919\|p.919]] |
> | Figure B-233: AArch64_trcrsctlr8 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0923-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=923\|p.923]] |
> | Table B-585: TRCRSCTLR8 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0923-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=923\|p.923]] |
> | 续表或相关原文（第924页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0924-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=924\|p.924]] |
> | 续表或相关原文（第925页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0925-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=925\|p.925]] |
> | 续表或相关原文（第926页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0926-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=926\|p.926]] |
> | Figure B-234: AArch64_trcsscsr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0930-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=930\|p.930]] |
> | Table B-588: TRCSSCSR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0930-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=930\|p.930]] |
> | 续表或相关原文（第931页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0931-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=931\|p.931]] |
> | 续表或相关原文（第932页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0932-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=932\|p.932]] |
> | Figure B-235: AArch64_trcrsctlr9 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0934-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=934\|p.934]] |
> | Table B-591: TRCRSCTLR9 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0934-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=934\|p.934]] |
> | 续表或相关原文（第935页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0935-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=935\|p.935]] |
> | 续表或相关原文（第936页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0936-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=936\|p.936]] |
> | Figure B-236: AArch64_trcrsctlr10 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0940-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=940\|p.940]] |
> | Table B-594: TRCRSCTLR10 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0940-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=940\|p.940]] |
> | 续表或相关原文（第941页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0941-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=941\|p.941]] |
> | 续表或相关原文（第942页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0942-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=942\|p.942]] |
> | 续表或相关原文（第943页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0943-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=943\|p.943]] |
> | Figure B-237: AArch64_trcrsctlr11 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0947-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=947\|p.947]] |
> | Table B-597: TRCRSCTLR11 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0947-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=947\|p.947]] |
> | 续表或相关原文（第948页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0948-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=948\|p.948]] |
> | 续表或相关原文（第949页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0949-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=949\|p.949]] |
> | Figure B-238: AArch64_trcrsctlr12 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0953-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=953\|p.953]] |
> | Table B-600: TRCRSCTLR12 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0953-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=953\|p.953]] |
> | 续表或相关原文（第954页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0954-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=954\|p.954]] |
> | 续表或相关原文（第955页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0955-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=955\|p.955]] |
> | 续表或相关原文（第956页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0956-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=956\|p.956]] |
> | Figure B-239: AArch64_trcrsctlr13 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0960-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=960\|p.960]] |
> | Table B-603: TRCRSCTLR13 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0960-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=960\|p.960]] |
> | 续表或相关原文（第961页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0961-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=961\|p.961]] |
> | 续表或相关原文（第962页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0962-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=962\|p.962]] |
> | Figure B-240: AArch64_trcrsctlr14 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0966-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=966\|p.966]] |
> | Table B-606: TRCRSCTLR14 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0966-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=966\|p.966]] |
> | 续表或相关原文（第967页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0967-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=967\|p.967]] |
> | 续表或相关原文（第968页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0968-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=968\|p.968]] |
> | 续表或相关原文（第969页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0969-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=969\|p.969]] |
> | Figure B-241: AArch64_trcrsctlr15 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0973-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=973\|p.973]] |
> | Table B-609: TRCRSCTLR15 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0973-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=973\|p.973]] |
> | 续表或相关原文（第974页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0974-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=974\|p.974]] |
> | 续表或相关原文（第975页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0975-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=975\|p.975]] |
> | Figure B-242: AArch64_trcacvr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0979-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=979\|p.979]] |
> | Table B-612: TRCACVR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0980-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=980\|p.980]] |
> | Figure B-243: AArch64_trcacatr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0983-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=983\|p.983]] |
> | Table B-615: TRCACATR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0983-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=983\|p.983]] |
> | 续表或相关原文（第984页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0984-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=984\|p.984]] |
> | Figure B-244: AArch64_trcacvr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0987-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=987\|p.987]] |
> | Table B-618: TRCACVR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0988-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=988\|p.988]] |
> | Figure B-245: AArch64_trcacatr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0991-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=991\|p.991]] |
> | Table B-621: TRCACATR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0991-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=991\|p.991]] |
> | 续表或相关原文（第992页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0992-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=992\|p.992]] |
> | Figure B-246: AArch64_trcacvr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0995-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=995\|p.995]] |
> | Table B-624: TRCACVR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0996-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=996\|p.996]] |
> | Figure B-247: AArch64_trcacatr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0999-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=999\|p.999]] |
> | Table B-627: TRCACATR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p0999-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=999\|p.999]] |
> | 续表或相关原文（第1000页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1000-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1000\|p.1000]] |
> | Figure B-248: AArch64_trcacvr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1003-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1003\|p.1003]] |
> | Table B-630: TRCACVR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1004-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1004\|p.1004]] |
> | Figure B-249: AArch64_trcacatr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1007-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1007\|p.1007]] |
> | Table B-633: TRCACATR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1007-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1007\|p.1007]] |
> | 续表或相关原文（第1008页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1008-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1008\|p.1008]] |
> | Figure B-250: AArch64_trcacvr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1011-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1011\|p.1011]] |
> | Table B-636: TRCACVR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1012-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1012\|p.1012]] |
> | Figure B-251: AArch64_trcacatr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1015-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1015\|p.1015]] |
> | Table B-639: TRCACATR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1015-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1015\|p.1015]] |
> | 续表或相关原文（第1016页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1016-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1016\|p.1016]] |
> | Figure B-252: AArch64_trcacvr5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1019-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1019\|p.1019]] |
> | Table B-642: TRCACVR5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1020-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1020\|p.1020]] |
> | Figure B-253: AArch64_trcacatr5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1023-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1023\|p.1023]] |
> | Table B-645: TRCACATR5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1023-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1023\|p.1023]] |
> | 续表或相关原文（第1024页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1024-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1024\|p.1024]] |
> | Figure B-254: AArch64_trcacvr6 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1027-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1027\|p.1027]] |
> | Table B-648: TRCACVR6 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1028-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1028\|p.1028]] |
> | Figure B-255: AArch64_trcacatr6 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1031-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1031\|p.1031]] |
> | Table B-651: TRCACATR6 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1031-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1031\|p.1031]] |
> | 续表或相关原文（第1032页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1032-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1032\|p.1032]] |
> | Figure B-256: AArch64_trcacvr7 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1035-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1035\|p.1035]] |
> | Table B-654: TRCACVR7 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1036-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1036\|p.1036]] |
> | Figure B-257: AArch64_trcacatr7 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1039-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1039\|p.1039]] |
> | Table B-657: TRCACATR7 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1039-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1039\|p.1039]] |
> | 续表或相关原文（第1040页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1040-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1040\|p.1040]] |
> | Figure B-258: AArch64_trccidcvr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1043-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1043\|p.1043]] |
> | Table B-660: TRCCIDCVR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1043-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1043\|p.1043]] |
> | Figure B-259: AArch64_trcvmidcvr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1046-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1046\|p.1046]] |
> | Table B-663: TRCVMIDCVR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1046-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1046\|p.1046]] |
> | Table B-666: Memory Partitioning and Monitoring registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1048-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048\|p.1048]] |
> | Figure B-260: AArch64_mpamvpmv_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1049-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1049\|p.1049]] |
> | Table B-667: MPAMVPMV_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1049-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1049\|p.1049]] |
> | 续表或相关原文（第1050页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1050-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1050\|p.1050]] |
> | Figure B-261: AArch64_mpamvpm0_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1052-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1052\|p.1052]] |
> | Table B-670: MPAMVPM0_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1052-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1052\|p.1052]] |
> | Figure B-262: AArch64_mpamvpm1_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1054-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1054\|p.1054]] |
> | Table B-673: MPAMVPM1_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1055-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1055\|p.1055]] |
> | Figure B-263: AArch64_mpamvpm2_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1057-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1057\|p.1057]] |
> | Table B-676: MPAMVPM2_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1057-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1057\|p.1057]] |
> | Figure B-264: AArch64_mpamvpm3_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1059-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1059\|p.1059]] |
> | Table B-679: MPAMVPM3_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1059-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1059\|p.1059]] |
> | Figure B-265: AArch64_mpamvpm4_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1062-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1062\|p.1062]] |
> | Table B-682: MPAMVPM4_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1062-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1062\|p.1062]] |
> | Figure B-266: AArch64_mpamvpm5_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1064-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1064\|p.1064]] |
> | Table B-685: MPAMVPM5_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1064-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1064\|p.1064]] |
> | Figure B-267: AArch64_mpamvpm6_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1066-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1066\|p.1066]] |
> | Table B-688: MPAMVPM6_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1067-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1067\|p.1067]] |
> | Figure B-268: AArch64_mpamvpm7_el2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1069-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1069\|p.1069]] |
> | Table B-691: MPAMVPM7_EL2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1069-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1069\|p.1069]] |
> | Table B-694: RAS registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1070-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070\|p.1070]] |
> | 续表或相关原文（第1071页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1071-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071\|p.1071]] |
> | Figure B-269: AArch64_erridr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1072-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1072\|p.1072]] |
> | Table B-695: ERRIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1072-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1072\|p.1072]] |
> | Figure B-270: AArch64_errselr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1073-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1073\|p.1073]] |
> | Table B-697: ERRSELR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1073-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1073\|p.1073]] |
> | Figure B-271: AArch64_erxfr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1075-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1075\|p.1075]] |
> | Table B-700: ERXFR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1075-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1075\|p.1075]] |
> | 续表或相关原文（第1076页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1076-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1076\|p.1076]] |
> | 续表或相关原文（第1077页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1077-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1077\|p.1077]] |
> | Figure B-272: AArch64_erxctlr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1078-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1078\|p.1078]] |
> | Table B-702: ERXCTLR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1078-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1078\|p.1078]] |
> | 续表或相关原文（第1079页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1079-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1079\|p.1079]] |
> | 续表或相关原文（第1080页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1080-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1080\|p.1080]] |
> | Figure B-273: AArch64_erxstatus_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1082-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1082\|p.1082]] |
> | Table B-705: ERXSTATUS_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1082-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1082\|p.1082]] |
> | 续表或相关原文（第1083页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1083-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1083\|p.1083]] |
> | 续表或相关原文（第1084页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1084-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1084\|p.1084]] |
> | 续表或相关原文（第1085页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1085-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1085\|p.1085]] |
> | Figure B-274: AArch64_erxaddr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1088-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1088\|p.1088]] |
> | Table B-708: ERXADDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1088-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1088\|p.1088]] |
> | Figure B-275: AArch64_erxpfgf_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1090-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1090\|p.1090]] |
> | Table B-711: ERXPFGF_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1091-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1091\|p.1091]] |
> | 续表或相关原文（第1092页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1092-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1092\|p.1092]] |
> | Figure B-276: AArch64_erxpfgctl_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1095-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1095\|p.1095]] |
> | Table B-713: ERXPFGCTL_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1095-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1095\|p.1095]] |
> | 续表或相关原文（第1096页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1096-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1096\|p.1096]] |
> | Figure B-277: AArch64_erxpfgcdn_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1099-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1099\|p.1099]] |
> | Table B-716: ERXPFGCDN_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1099-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1099\|p.1099]] |
> | Figure B-278: AArch64_erxmisc0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1102-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1102\|p.1102]] |
> | Table B-719: ERXMISC0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1102-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1102\|p.1102]] |
> | 续表或相关原文（第1103页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1103-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1103\|p.1103]] |
> | 续表或相关原文（第1104页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1104-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1104\|p.1104]] |
> | 续表或相关原文（第1105页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1105-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1105\|p.1105]] |
> | Figure B-279: AArch64_erxmisc1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1108-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1108\|p.1108]] |
> | Table B-722: ERXMISC1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1108-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1108\|p.1108]] |
> | Figure B-280: AArch64_erxmisc2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1110-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1110\|p.1110]] |
> | Table B-725: ERXMISC2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1110-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1110\|p.1110]] |
> | Figure B-281: AArch64_erxmisc3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1112-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1112\|p.1112]] |
> | Table B-728: ERXMISC3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1113-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1113\|p.1113]] |
> | Table B-731: Statistical Profiling Extension registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1114-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114\|p.1114]] |
> | 续表或相关原文（第1115页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1115-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115\|p.1115]] |
> | Figure B-282: AArch64_pmsevfr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1116-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1116\|p.1116]] |
> | Table B-732: PMSEVFR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1116-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1116\|p.1116]] |
> | 续表或相关原文（第1117页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1117-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1117\|p.1117]] |
> | 续表或相关原文（第1118页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1118-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1118\|p.1118]] |
> | 续表或相关原文（第1119页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1119-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1119\|p.1119]] |
> | 续表或相关原文（第1120页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1120-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1120\|p.1120]] |
> | 续表或相关原文（第1121页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1121-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1121\|p.1121]] |
> | 续表或相关原文（第1122页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1122-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1122\|p.1122]] |
> | 续表或相关原文（第1123页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1123-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1123\|p.1123]] |
> | 续表或相关原文（第1124页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1124-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1124\|p.1124]] |
> | 续表或相关原文（第1125页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1125-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1125\|p.1125]] |
> | Figure B-283: AArch64_pmsidr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1126-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1126\|p.1126]] |
> | Table B-735: PMSIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1127-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1127\|p.1127]] |
> | Figure B-284: AArch64_pmbidr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1129-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1129\|p.1129]] |
> | Table B-737: PMBIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1129-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1129\|p.1129]] |
> | Table B-739: Trace Buffer Extension registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1130-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130\|p.1130]] |


### 图表 附录C

原文范围 p.1131-1660。

> [!info]- 647个编号图表 · 473页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table C-1: CoreROM registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1131-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131\|p.1131]] |
> | Figure C-1: ext_corerom_romentry0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1132-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1132\|p.1132]] |
> | Table C-2: COREROM_ROMENTRY0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1132-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1132\|p.1132]] |
> | Figure C-2: ext_corerom_romentry1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1133-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1133\|p.1133]] |
> | Table C-3: COREROM_ROMENTRY1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1134-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1134\|p.1134]] |
> | Figure C-3: ext_corerom_romentry2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1135-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1135\|p.1135]] |
> | Table C-4: COREROM_ROMENTRY2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1135-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1135\|p.1135]] |
> | Figure C-4: ext_corerom_romentry3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1136-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1136\|p.1136]] |
> | Table C-5: COREROM_ROMENTRY3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1136-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1136\|p.1136]] |
> | Figure C-5: ext_corerom_authstatus bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1137-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1137\|p.1137]] |
> | Table C-6: COREROM_AUTHSTATUS bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1137-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1137\|p.1137]] |
> | 续表或相关原文（第1138页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1138-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1138\|p.1138]] |
> | Figure C-6: ext_corerom_devarch bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1139-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1139\|p.1139]] |
> | Table C-7: COREROM_DEVARCH bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1139-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1139\|p.1139]] |
> | Figure C-7: ext_corerom_devtype bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1140-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1140\|p.1140]] |
> | Table C-8: COREROM_DEVTYPE bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1140-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1140\|p.1140]] |
> | Figure C-8: ext_corerom_pidr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1141-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1141\|p.1141]] |
> | Table C-9: COREROM_PIDR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1141-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1141\|p.1141]] |
> | Figure C-9: ext_corerom_pidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1142-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1142\|p.1142]] |
> | Table C-10: COREROM_PIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1142-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1142\|p.1142]] |
> | Figure C-10: ext_corerom_pidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1143-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1143\|p.1143]] |
> | Table C-11: COREROM_PIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1143-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1143\|p.1143]] |
> | Figure C-11: ext_corerom_pidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1144-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1144\|p.1144]] |
> | Table C-12: COREROM_PIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1145-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1145\|p.1145]] |
> | Figure C-12: ext_corerom_pidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1146-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1146\|p.1146]] |
> | Table C-13: COREROM_PIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1146-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1146\|p.1146]] |
> | Figure C-13: ext_corerom_cidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1147-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1147\|p.1147]] |
> | Table C-14: COREROM_CIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1147-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1147\|p.1147]] |
> | Figure C-14: ext_corerom_cidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1148-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1148\|p.1148]] |
> | Table C-15: COREROM_CIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1148-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1148\|p.1148]] |
> | Figure C-15: ext_corerom_cidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1149-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1149\|p.1149]] |
> | Table C-16: COREROM_CIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1149-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1149\|p.1149]] |
> | Figure C-16: ext_corerom_cidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1150-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1150\|p.1150]] |
> | Table C-17: COREROM_CIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1150-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1150\|p.1150]] |
> | Table C-18: PPM registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1151-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151\|p.1151]] |
> | Figure C-17: ext_cpuppmcr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1152-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1152\|p.1152]] |
> | Table C-19: CPUPPMCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1152-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1152\|p.1152]] |
> | Figure C-18: ext_cpuppmcr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1153-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1153\|p.1153]] |
> | Table C-20: CPUPPMCR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1153-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1153\|p.1153]] |
> | Figure C-19: ext_cpuppmcr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1154-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1154\|p.1154]] |
> | Table C-21: CPUPPMCR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1154-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1154\|p.1154]] |
> | Figure C-20: ext_cpuppmcr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1155-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1155\|p.1155]] |
> | Table C-22: CPUPPMCR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1155-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1155\|p.1155]] |
> | Figure C-21: ext_cpuppmcr5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1156-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1156\|p.1156]] |
> | Table C-23: CPUPPMCR5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1156-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1156\|p.1156]] |
> | Figure C-22: ext_cpuppmcr6 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1157-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157\|p.1157]] |
> | Table C-24: CPUPPMCR6 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1157-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157\|p.1157]] |
> | Table C-25: Performance Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1157-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157\|p.1157]] |
> | 续表或相关原文（第1158页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1158-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158\|p.1158]] |
> | 续表或相关原文（第1159页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1159-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159\|p.1159]] |
> | Figure C-23: ext_pmevcntr0_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1160-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1160\|p.1160]] |
> | Table C-26: PMEVCNTR0_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1160-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1160\|p.1160]] |
> | Figure C-24: ext_pmevcntr1_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1162-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1162\|p.1162]] |
> | Table C-28: PMEVCNTR1_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1162-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1162\|p.1162]] |
> | Figure C-25: ext_pmevcntr2_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1164-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1164\|p.1164]] |
> | Table C-30: PMEVCNTR2_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1164-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1164\|p.1164]] |
> | Figure C-26: ext_pmevcntr3_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1166-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1166\|p.1166]] |
> | Table C-32: PMEVCNTR3_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1166-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1166\|p.1166]] |
> | Figure C-27: ext_pmevcntr4_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1168-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1168\|p.1168]] |
> | Table C-34: PMEVCNTR4_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1168-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1168\|p.1168]] |
> | Figure C-28: ext_pmevcntr5_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1170-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1170\|p.1170]] |
> | Table C-36: PMEVCNTR5_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1171-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1171\|p.1171]] |
> | Figure C-29: ext_pmccntr_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1173-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1173\|p.1173]] |
> | Table C-38: PMCCNTR_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1173-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1173\|p.1173]] |
> | Figure C-30: ext_pmpcsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1175-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1175\|p.1175]] |
> | Table C-41: PMPCSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1175-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1175\|p.1175]] |
> | 续表或相关原文（第1176页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1176-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1176\|p.1176]] |
> | Figure C-31: ext_pmcid1sr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1178-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1178\|p.1178]] |
> | Table C-46: PMCID1SR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1179-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1179\|p.1179]] |
> | Figure C-32: ext_pmvidsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1180-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1180\|p.1180]] |
> | Table C-49: PMVIDSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1180-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1180\|p.1180]] |
> | 续表或相关原文（第1181页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1181-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1181\|p.1181]] |
> | Figure C-33: ext_pmcid2sr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1182-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1182\|p.1182]] |
> | Table C-51: PMCID2SR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1183-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1183\|p.1183]] |
> | Figure C-34: ext_pmevtyper0_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1184-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1184\|p.1184]] |
> | Table C-53: PMEVTYPER0_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1184-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1184\|p.1184]] |
> | 续表或相关原文（第1185页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1185-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1185\|p.1185]] |
> | 续表或相关原文（第1186页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1186-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1186\|p.1186]] |
> | Figure C-35: ext_pmevtyper1_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1187-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1187\|p.1187]] |
> | Table C-55: PMEVTYPER1_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1187-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1187\|p.1187]] |
> | 续表或相关原文（第1188页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1188-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1188\|p.1188]] |
> | 续表或相关原文（第1189页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1189-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1189\|p.1189]] |
> | Figure C-36: ext_pmevtyper2_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1191-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1191\|p.1191]] |
> | Table C-57: PMEVTYPER2_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1191-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1191\|p.1191]] |
> | 续表或相关原文（第1192页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1192-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1192\|p.1192]] |
> | 续表或相关原文（第1193页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1193-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1193\|p.1193]] |
> | Figure C-37: ext_pmevtyper3_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1194-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1194\|p.1194]] |
> | Table C-59: PMEVTYPER3_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1194-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1194\|p.1194]] |
> | 续表或相关原文（第1195页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1195-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1195\|p.1195]] |
> | 续表或相关原文（第1196页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1196-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1196\|p.1196]] |
> | Figure C-38: ext_pmevtyper4_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1198-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1198\|p.1198]] |
> | Table C-61: PMEVTYPER4_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1198-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1198\|p.1198]] |
> | 续表或相关原文（第1199页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1199-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1199\|p.1199]] |
> | 续表或相关原文（第1200页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1200-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1200\|p.1200]] |
> | Figure C-39: ext_pmevtyper5_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1201-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1201\|p.1201]] |
> | Table C-63: PMEVTYPER5_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1201-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1201\|p.1201]] |
> | 续表或相关原文（第1202页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1202-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1202\|p.1202]] |
> | 续表或相关原文（第1203页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1203-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1203\|p.1203]] |
> | Figure C-40: ext_pmccfiltr_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1205-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1205\|p.1205]] |
> | Table C-65: PMCCFILTR_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1205-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1205\|p.1205]] |
> | 续表或相关原文（第1206页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1206-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1206\|p.1206]] |
> | Figure C-41: ext_pmpcssr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1207-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1207\|p.1207]] |
> | Table C-67: PMPCSSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1208-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1208\|p.1208]] |
> | Figure C-42: ext_pmcidssr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1209-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1209\|p.1209]] |
> | Table C-68: PMCIDSSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1209-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1209\|p.1209]] |
> | Figure C-43: ext_pmsssr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1210-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1210\|p.1210]] |
> | Table C-69: PMSSSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1210-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1210\|p.1210]] |
> | Figure C-44: ext_pmccntsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1211-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1211\|p.1211]] |
> | Table C-70: PMCCNTSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1211-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1211\|p.1211]] |
> | Figure C-45: ext_pmevcntsr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1212-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1212\|p.1212]] |
> | Table C-71: PMEVCNTSR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1213-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1213\|p.1213]] |
> | Figure C-46: ext_pmevcntsr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1214-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1214\|p.1214]] |
> | Table C-73: PMEVCNTSR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1214-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1214\|p.1214]] |
> | Figure C-47: ext_pmevcntsr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1215-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1215\|p.1215]] |
> | Table C-75: PMEVCNTSR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1215-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1215\|p.1215]] |
> | Figure C-48: ext_pmevcntsr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1216-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1216\|p.1216]] |
> | Table C-77: PMEVCNTSR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1216-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1216\|p.1216]] |
> | Figure C-49: ext_pmevcntsr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1217-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1217\|p.1217]] |
> | Table C-79: PMEVCNTSR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1217-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1217\|p.1217]] |
> | Figure C-50: ext_pmevcntsr5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1218-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1218\|p.1218]] |
> | Table C-81: PMEVCNTSR5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1218-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1218\|p.1218]] |
> | Figure C-51: ext_pmsscr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1219-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1219\|p.1219]] |
> | Table C-83: PMSSCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1219-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1219\|p.1219]] |
> | Figure C-52: ext_pmcntenset_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1220-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1220\|p.1220]] |
> | Table C-84: PMCNTENSET_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1221-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1221\|p.1221]] |
> | Figure C-53: ext_pmcntenclr_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1222-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1222\|p.1222]] |
> | Table C-86: PMCNTENCLR_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1223-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1223\|p.1223]] |
> | Figure C-54: ext_pmintenset_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1224-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1224\|p.1224]] |
> | Table C-88: PMINTENSET_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1225-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1225\|p.1225]] |
> | Figure C-55: ext_pmintenclr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1226-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1226\|p.1226]] |
> | Table C-90: PMINTENCLR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1227-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1227\|p.1227]] |
> | Figure C-56: ext_pmovsclr_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1228-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1228\|p.1228]] |
> | Table C-92: PMOVSCLR_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1229-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1229\|p.1229]] |
> | Figure C-57: ext_pmswinc_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1230-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1230\|p.1230]] |
> | Table C-94: PMSWINC_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1231-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1231\|p.1231]] |
> | Figure C-58: ext_pmovsset_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1232-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1232\|p.1232]] |
> | Table C-96: PMOVSSET_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1232-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1232\|p.1232]] |
> | 续表或相关原文（第1233页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1233-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1233\|p.1233]] |
> | Figure C-59: ext_pmcfgr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1234-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1234\|p.1234]] |
> | Table C-98: PMCFGR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1234-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1234\|p.1234]] |
> | 续表或相关原文（第1235页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1235-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1235\|p.1235]] |
> | Figure C-60: ext_pmcr_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1236-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1236\|p.1236]] |
> | Table C-100: PMCR_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1236-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1236\|p.1236]] |
> | 续表或相关原文（第1237页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1237-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1237\|p.1237]] |
> | Figure C-61: ext_pmceid0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1239-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1239\|p.1239]] |
> | Table C-102: PMCEID0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1239-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1239\|p.1239]] |
> | 续表或相关原文（第1240页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1240-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1240\|p.1240]] |
> | 续表或相关原文（第1241页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1241-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1241\|p.1241]] |
> | Figure C-62: ext_pmceid1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1243-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1243\|p.1243]] |
> | Table C-104: PMCEID1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1243-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1243\|p.1243]] |
> | 续表或相关原文（第1244页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1244-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1244\|p.1244]] |
> | 续表或相关原文（第1245页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1245-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1245\|p.1245]] |
> | Figure C-63: ext_pmceid2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1247-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1247\|p.1247]] |
> | Table C-106: PMCEID2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1247-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1247\|p.1247]] |
> | 续表或相关原文（第1248页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1248-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1248\|p.1248]] |
> | 续表或相关原文（第1249页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1249-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1249\|p.1249]] |
> | Figure C-64: ext_pmceid3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1251-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1251\|p.1251]] |
> | Table C-108: PMCEID3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1251-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1251\|p.1251]] |
> | 续表或相关原文（第1252页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1252-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1252\|p.1252]] |
> | 续表或相关原文（第1253页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1253-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1253\|p.1253]] |
> | Figure C-65: ext_pmmir bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1254-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1254\|p.1254]] |
> | Table C-110: PMMIR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1254-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1254\|p.1254]] |
> | 续表或相关原文（第1255页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1255-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1255\|p.1255]] |
> | Figure C-66: ext_pmdevaff0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1256-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1256\|p.1256]] |
> | Table C-112: PMDEVAFF0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1256-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1256\|p.1256]] |
> | Figure C-67: ext_pmdevaff1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1257-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1257\|p.1257]] |
> | Table C-114: PMDEVAFF1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1257-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1257\|p.1257]] |
> | Figure C-68: ext_pmlar bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1258-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1258\|p.1258]] |
> | Table C-116: PMLAR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1259-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1259\|p.1259]] |
> | Figure C-69: ext_pmlsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1260-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1260\|p.1260]] |
> | Table C-118: PMLSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1260-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1260\|p.1260]] |
> | Figure C-70: ext_pmauthstatus bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1261-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1261\|p.1261]] |
> | Table C-120: PMAUTHSTATUS bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1261-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1261\|p.1261]] |
> | 续表或相关原文（第1262页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1262-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1262\|p.1262]] |
> | Figure C-71: ext_pmdevarch bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1263-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1263\|p.1263]] |
> | Table C-122: PMDEVARCH bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1263-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1263\|p.1263]] |
> | Figure C-72: ext_pmdevid bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1265-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1265\|p.1265]] |
> | Table C-124: PMDEVID bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1265-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1265\|p.1265]] |
> | Figure C-73: ext_pmdevtype bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1266-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1266\|p.1266]] |
> | Table C-126: PMDEVTYPE bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1266-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1266\|p.1266]] |
> | Figure C-74: ext_pmpidr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1267-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1267\|p.1267]] |
> | Table C-128: PMPIDR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1267-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1267\|p.1267]] |
> | Figure C-75: ext_pmpidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1269-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1269\|p.1269]] |
> | Table C-130: PMPIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1269-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1269\|p.1269]] |
> | Figure C-76: ext_pmpidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1270-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1270\|p.1270]] |
> | Table C-132: PMPIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1270-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1270\|p.1270]] |
> | Figure C-77: ext_pmpidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1271-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1271\|p.1271]] |
> | Table C-134: PMPIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1272-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1272\|p.1272]] |
> | Figure C-78: ext_pmpidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1273-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1273\|p.1273]] |
> | Table C-136: PMPIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1273-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1273\|p.1273]] |
> | Figure C-79: ext_pmcidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1274-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1274\|p.1274]] |
> | Table C-138: PMCIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1274-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1274\|p.1274]] |
> | 续表或相关原文（第1275页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1275-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1275\|p.1275]] |
> | Figure C-80: ext_pmcidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1276-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1276\|p.1276]] |
> | Table C-140: PMCIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1276-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1276\|p.1276]] |
> | Figure C-81: ext_pmcidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1277-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1277\|p.1277]] |
> | Table C-142: PMCIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1277-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1277\|p.1277]] |
> | Figure C-82: ext_pmcidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1278-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1278\|p.1278]] |
> | Table C-144: PMCIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1279-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279\|p.1279]] |
> | Table C-146: CTI registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1279-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279\|p.1279]] |
> | Figure C-83: ext_cticontrol bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1280-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280\|p.1280]] |
> | Table C-147: CTICONTROL bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1281-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1281\|p.1281]] |
> | Figure C-84: ext_ctiintack bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1282-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1282\|p.1282]] |
> | Table C-149: CTIINTACK bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1283-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1283\|p.1283]] |
> | Figure C-85: ext_ctiappset bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1284-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1284\|p.1284]] |
> | Table C-151: CTIAPPSET bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1285-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1285\|p.1285]] |
> | Figure C-86: ext_ctiappclear bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1286-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1286\|p.1286]] |
> | Table C-153: CTIAPPCLEAR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1286-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1286\|p.1286]] |
> | Figure C-87: ext_ctiapppulse bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1288-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1288\|p.1288]] |
> | Table C-155: CTIAPPPULSE bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1288-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1288\|p.1288]] |
> | Figure C-88: ext_ctiinen_n_ bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1290-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1290\|p.1290]] |
> | Table C-157: CTIINEN<n> bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1290-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1290\|p.1290]] |
> | Figure C-89: ext_ctiouten_n_ bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1291-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1291\|p.1291]] |
> | Table C-159: CTIOUTEN<n> bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1292-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1292\|p.1292]] |
> | Figure C-90: ext_ctitriginstatus bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1293-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1293\|p.1293]] |
> | Table C-161: CTITRIGINSTATUS bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1293-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1293\|p.1293]] |
> | Figure C-91: ext_ctitrigoutstatus bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1294-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1294\|p.1294]] |
> | Table C-163: CTITRIGOUTSTATUS bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1295-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1295\|p.1295]] |
> | Figure C-92: ext_ctichinstatus bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1296-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1296\|p.1296]] |
> | Table C-165: CTICHINSTATUS bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1296-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1296\|p.1296]] |
> | Figure C-93: ext_ctichoutstatus bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1297-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1297\|p.1297]] |
> | Table C-167: CTICHOUTSTATUS bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1298-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1298\|p.1298]] |
> | Figure C-94: ext_ctigate bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1299-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1299\|p.1299]] |
> | Table C-169: CTIGATE bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1299-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1299\|p.1299]] |
> | Figure C-95: ext_asicctl bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1301-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1301\|p.1301]] |
> | Table C-171: ASICCTL bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1301-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1301\|p.1301]] |
> | Figure C-96: ext_ctidevctl bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1302-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1302\|p.1302]] |
> | Table C-173: CTIDEVCTL bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1302-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1302\|p.1302]] |
> | Figure C-97: ext_ctidevaff0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1303-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1303\|p.1303]] |
> | Table C-175: CTIDEVAFF0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1304-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1304\|p.1304]] |
> | Figure C-98: ext_ctidevaff1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1305-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1305\|p.1305]] |
> | Table C-177: CTIDEVAFF1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1305-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1305\|p.1305]] |
> | Figure C-99: ext_ctilar bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1306-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1306\|p.1306]] |
> | Table C-179: CTILAR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1306-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1306\|p.1306]] |
> | Figure C-100: ext_ctilsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1307-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1307\|p.1307]] |
> | Table C-181: CTILSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1307-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1307\|p.1307]] |
> | 续表或相关原文（第1308页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1308-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1308\|p.1308]] |
> | Figure C-101: ext_ctiauthstatus bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1309-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1309\|p.1309]] |
> | Table C-183: CTIAUTHSTATUS bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1309-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1309\|p.1309]] |
> | Figure C-102: ext_ctidevarch bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1310-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1310\|p.1310]] |
> | Table C-185: CTIDEVARCH bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1310-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1310\|p.1310]] |
> | 续表或相关原文（第1311页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1311-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1311\|p.1311]] |
> | Figure C-103: ext_ctidevid2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1312-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1312\|p.1312]] |
> | Table C-187: CTIDEVID2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1312-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1312\|p.1312]] |
> | Figure C-104: ext_ctidevid1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1313-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1313\|p.1313]] |
> | Table C-189: CTIDEVID1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1313-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1313\|p.1313]] |
> | Figure C-105: ext_ctidevid bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1314-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1314\|p.1314]] |
> | Table C-191: CTIDEVID bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1314-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1314\|p.1314]] |
> | Table C-193: Debug registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1315-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315\|p.1315]] |
> | 续表或相关原文（第1316页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1316-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316\|p.1316]] |
> | Figure C-106: ext_edesr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1317-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317\|p.1317]] |
> | Table C-194: EDESR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1318-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1318\|p.1318]] |
> | Figure C-107: ext_edecr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1319-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1319\|p.1319]] |
> | Table C-196: EDECR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1319-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1319\|p.1319]] |
> | 续表或相关原文（第1320页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1320-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1320\|p.1320]] |
> | Figure C-108: ext_edwar bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1321-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1321\|p.1321]] |
> | Table C-198: EDWAR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1321-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1321\|p.1321]] |
> | Figure C-109: ext_dbgdtrrx_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1322-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1322\|p.1322]] |
> | Table C-201: DBGDTRRX_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1323-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1323\|p.1323]] |
> | Figure C-110: ext_editr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1324-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1324\|p.1324]] |
> | Table C-203: EDITR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1325-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1325\|p.1325]] |
> | Figure C-111: ext_editr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1325-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1325\|p.1325]] |
> | Table C-204: EDITR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1325-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1325\|p.1325]] |
> | Figure C-112: ext_edscr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1327-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1327\|p.1327]] |
> | Table C-206: EDSCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1327-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1327\|p.1327]] |
> | 续表或相关原文（第1328页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1328-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1328\|p.1328]] |
> | 续表或相关原文（第1329页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1329-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1329\|p.1329]] |
> | 续表或相关原文（第1330页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1330-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1330\|p.1330]] |
> | 续表或相关原文（第1331页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1331-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1331\|p.1331]] |
> | 续表或相关原文（第1332页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1332-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1332\|p.1332]] |
> | Figure C-113: ext_dbgdtrtx_el0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1333-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1333\|p.1333]] |
> | Table C-208: DBGDTRTX_EL0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1334-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1334\|p.1334]] |
> | Figure C-114: ext_edrcr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1335-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1335\|p.1335]] |
> | Table C-210: EDRCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1335-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1335\|p.1335]] |
> | 续表或相关原文（第1336页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1336-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1336\|p.1336]] |
> | Figure C-115: ext_edeccr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1337-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1337\|p.1337]] |
> | Table C-212: EDECCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1337-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1337\|p.1337]] |
> | 续表或相关原文（第1338页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1338-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1338\|p.1338]] |
> | 续表或相关原文（第1339页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1339-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1339\|p.1339]] |
> | 续表或相关原文（第1340页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1340-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1340\|p.1340]] |
> | 续表或相关原文（第1341页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1341-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1341\|p.1341]] |
> | Figure C-116: ext_oslar_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1342-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1342\|p.1342]] |
> | Table C-214: OSLAR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1343-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1343\|p.1343]] |
> | Figure C-117: ext_edprcr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1344-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1344\|p.1344]] |
> | Table C-216: EDPRCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1344-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1344\|p.1344]] |
> | 续表或相关原文（第1345页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1345-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1345\|p.1345]] |
> | Figure C-118: ext_edprsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1347-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1347\|p.1347]] |
> | Table C-218: EDPRSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1347-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1347\|p.1347]] |
> | 续表或相关原文（第1348页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1348-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1348\|p.1348]] |
> | 续表或相关原文（第1349页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1349-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1349\|p.1349]] |
> | 续表或相关原文（第1350页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1350-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1350\|p.1350]] |
> | 续表或相关原文（第1351页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1351-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1351\|p.1351]] |
> | 续表或相关原文（第1352页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1352-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1352\|p.1352]] |
> | Figure C-119: ext_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1355-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1355\|p.1355]] |
> | Table C-220: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1355-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1355\|p.1355]] |
> | Figure C-120: ext_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1355-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1355\|p.1355]] |
> | Table C-221: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1355-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1355\|p.1355]] |
> | Figure C-121: ext_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1356-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1356\|p.1356]] |
> | Table C-222: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1356-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1356\|p.1356]] |
> | Figure C-122: ext_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1356-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1356\|p.1356]] |
> | Table C-223: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1356-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1356\|p.1356]] |
> | Figure C-123: ext_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1357-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1357\|p.1357]] |
> | Table C-224: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1357-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1357\|p.1357]] |
> | Figure C-124: ext_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1357-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1357\|p.1357]] |
> | Table C-225: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1358-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1358\|p.1358]] |
> | Figure C-125: ext_dbgbvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1358-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1358\|p.1358]] |
> | Table C-226: DBGBVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1358-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1358\|p.1358]] |
> | Figure C-126: ext_dbgbcr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1359-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1359\|p.1359]] |
> | Table C-228: DBGBCR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1359-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1359\|p.1359]] |
> | 续表或相关原文（第1360页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1360-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1360\|p.1360]] |
> | 续表或相关原文（第1361页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1361-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1361\|p.1361]] |
> | Table C-229: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1362-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1362\|p.1362]] |
> | Table C-230: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1362-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1362\|p.1362]] |
> | Figure C-127: ext_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1364-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1364\|p.1364]] |
> | Table C-232: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1364-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1364\|p.1364]] |
> | Figure C-128: ext_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1365-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1365\|p.1365]] |
> | Table C-233: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1365-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1365\|p.1365]] |
> | Figure C-129: ext_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1365-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1365\|p.1365]] |
> | Table C-234: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1365-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1365\|p.1365]] |
> | Figure C-130: ext_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1365-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1365\|p.1365]] |
> | Table C-235: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1366-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1366\|p.1366]] |
> | Figure C-131: ext_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1366-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1366\|p.1366]] |
> | Table C-236: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1366-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1366\|p.1366]] |
> | Figure C-132: ext_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1367-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1367\|p.1367]] |
> | Table C-237: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1367-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1367\|p.1367]] |
> | Figure C-133: ext_dbgbvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1367-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1367\|p.1367]] |
> | Table C-238: DBGBVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1367-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1367\|p.1367]] |
> | Figure C-134: ext_dbgbcr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1369-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1369\|p.1369]] |
> | Table C-240: DBGBCR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1369-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1369\|p.1369]] |
> | 续表或相关原文（第1370页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1370-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1370\|p.1370]] |
> | 续表或相关原文（第1371页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1371-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1371\|p.1371]] |
> | Table C-241: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1372-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1372\|p.1372]] |
> | Table C-242: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1372-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1372\|p.1372]] |
> | Figure C-135: ext_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1374-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1374\|p.1374]] |
> | Table C-244: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1374-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1374\|p.1374]] |
> | Figure C-136: ext_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1375-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1375\|p.1375]] |
> | Table C-245: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1375-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1375\|p.1375]] |
> | Figure C-137: ext_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1375-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1375\|p.1375]] |
> | Table C-246: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1375-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1375\|p.1375]] |
> | Figure C-138: ext_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1375-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1375\|p.1375]] |
> | Table C-247: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1376-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1376\|p.1376]] |
> | Figure C-139: ext_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1376-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1376\|p.1376]] |
> | Table C-248: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1376-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1376\|p.1376]] |
> | Figure C-140: ext_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1377-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1377\|p.1377]] |
> | Table C-249: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1377-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1377\|p.1377]] |
> | Figure C-141: ext_dbgbvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1377-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1377\|p.1377]] |
> | Table C-250: DBGBVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1377-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1377\|p.1377]] |
> | Figure C-142: ext_dbgbcr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1379-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1379\|p.1379]] |
> | Table C-252: DBGBCR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1379-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1379\|p.1379]] |
> | 续表或相关原文（第1380页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1380-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1380\|p.1380]] |
> | 续表或相关原文（第1381页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1381-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1381\|p.1381]] |
> | Table C-253: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1382-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1382\|p.1382]] |
> | Table C-254: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1382-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1382\|p.1382]] |
> | Figure C-143: ext_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1384-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1384\|p.1384]] |
> | Table C-256: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1384-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1384\|p.1384]] |
> | Figure C-144: ext_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1385-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1385\|p.1385]] |
> | Table C-257: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1385-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1385\|p.1385]] |
> | Figure C-145: ext_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1385-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1385\|p.1385]] |
> | Table C-258: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1385-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1385\|p.1385]] |
> | Figure C-146: ext_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1385-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1385\|p.1385]] |
> | Table C-259: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1386-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1386\|p.1386]] |
> | Figure C-147: ext_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1386-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1386\|p.1386]] |
> | Table C-260: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1386-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1386\|p.1386]] |
> | Figure C-148: ext_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1387-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1387\|p.1387]] |
> | Table C-261: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1387-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1387\|p.1387]] |
> | Figure C-149: ext_dbgbvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1387-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1387\|p.1387]] |
> | Table C-262: DBGBVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1387-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1387\|p.1387]] |
> | Figure C-150: ext_dbgbcr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1389-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1389\|p.1389]] |
> | Table C-264: DBGBCR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1389-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1389\|p.1389]] |
> | 续表或相关原文（第1390页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1390-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1390\|p.1390]] |
> | 续表或相关原文（第1391页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1391-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1391\|p.1391]] |
> | Table C-265: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1392-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1392\|p.1392]] |
> | Table C-266: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1392-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1392\|p.1392]] |
> | Figure C-151: ext_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1394-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1394\|p.1394]] |
> | Table C-268: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1394-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1394\|p.1394]] |
> | Figure C-152: ext_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1395-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1395\|p.1395]] |
> | Table C-269: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1395-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1395\|p.1395]] |
> | Figure C-153: ext_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1395-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1395\|p.1395]] |
> | Table C-270: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1395-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1395\|p.1395]] |
> | Figure C-154: ext_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1395-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1395\|p.1395]] |
> | Table C-271: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1396-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1396\|p.1396]] |
> | Figure C-155: ext_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1396-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1396\|p.1396]] |
> | Table C-272: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1396-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1396\|p.1396]] |
> | Figure C-156: ext_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1397-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1397\|p.1397]] |
> | Table C-273: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1397-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1397\|p.1397]] |
> | Figure C-157: ext_dbgbvr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1397-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1397\|p.1397]] |
> | Table C-274: DBGBVR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1397-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1397\|p.1397]] |
> | Figure C-158: ext_dbgbcr4_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1399-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1399\|p.1399]] |
> | Table C-276: DBGBCR4_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1399-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1399\|p.1399]] |
> | 续表或相关原文（第1400页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1400-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1400\|p.1400]] |
> | 续表或相关原文（第1401页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1401-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1401\|p.1401]] |
> | Table C-277: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1402-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1402\|p.1402]] |
> | Table C-278: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1402-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1402\|p.1402]] |
> | Figure C-159: ext_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1404-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1404\|p.1404]] |
> | Table C-280: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1404-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1404\|p.1404]] |
> | Figure C-160: ext_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1405-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1405\|p.1405]] |
> | Table C-281: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1405-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1405\|p.1405]] |
> | Figure C-161: ext_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1405-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1405\|p.1405]] |
> | Table C-282: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1405-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1405\|p.1405]] |
> | Figure C-162: ext_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1405-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1405\|p.1405]] |
> | Table C-283: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1406-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1406\|p.1406]] |
> | Figure C-163: ext_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1406-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1406\|p.1406]] |
> | Table C-284: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1406-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1406\|p.1406]] |
> | Figure C-164: ext_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1407-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1407\|p.1407]] |
> | Table C-285: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1407-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1407\|p.1407]] |
> | Figure C-165: ext_dbgbvr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1407-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1407\|p.1407]] |
> | Table C-286: DBGBVR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1407-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1407\|p.1407]] |
> | Figure C-166: ext_dbgbcr5_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1409-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1409\|p.1409]] |
> | Table C-288: DBGBCR5_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1409-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1409\|p.1409]] |
> | 续表或相关原文（第1410页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1410-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1410\|p.1410]] |
> | 续表或相关原文（第1411页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1411-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1411\|p.1411]] |
> | Table C-289: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1412-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1412\|p.1412]] |
> | Table C-290: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1412-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1412\|p.1412]] |
> | Figure C-167: ext_dbgwvr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1413-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1413\|p.1413]] |
> | Table C-292: DBGWVR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1414-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1414\|p.1414]] |
> | Figure C-168: ext_dbgwcr0_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1415-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1415\|p.1415]] |
> | Table C-294: DBGWCR0_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1415-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1415\|p.1415]] |
> | 续表或相关原文（第1416页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1416-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1416\|p.1416]] |
> | Table C-295: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1417-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1417\|p.1417]] |
> | Table C-296: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1417-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1417\|p.1417]] |
> | Figure C-169: ext_dbgwvr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1419-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1419\|p.1419]] |
> | Table C-298: DBGWVR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1419-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1419\|p.1419]] |
> | Figure C-170: ext_dbgwcr1_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1420-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1420\|p.1420]] |
> | Table C-300: DBGWCR1_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1421-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1421\|p.1421]] |
> | Table C-301: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1422-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1422\|p.1422]] |
> | Table C-302: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1422-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1422\|p.1422]] |
> | Figure C-171: ext_dbgwvr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1424-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1424\|p.1424]] |
> | Table C-304: DBGWVR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1424-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1424\|p.1424]] |
> | Figure C-172: ext_dbgwcr2_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1426-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1426\|p.1426]] |
> | Table C-306: DBGWCR2_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1426-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1426\|p.1426]] |
> | Table C-307: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1427-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1427\|p.1427]] |
> | Table C-308: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1427-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1427\|p.1427]] |
> | Figure C-173: ext_dbgwvr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1429-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1429\|p.1429]] |
> | Table C-310: DBGWVR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1429-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1429\|p.1429]] |
> | Figure C-174: ext_dbgwcr3_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1431-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1431\|p.1431]] |
> | Table C-312: DBGWCR3_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1431-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1431\|p.1431]] |
> | Table C-313: BAS description table 1 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1432-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1432\|p.1432]] |
> | Table C-314: BAS description table 2 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1432-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1432\|p.1432]] |
> | Figure C-175: ext_midr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1434-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1434\|p.1434]] |
> | Table C-316: MIDR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1434-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1434\|p.1434]] |
> | Figure C-176: ext_edpfr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1435-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1435\|p.1435]] |
> | Table C-318: EDPFR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1435-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1435\|p.1435]] |
> | 续表或相关原文（第1436页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1436-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1436\|p.1436]] |
> | Figure C-177: ext_eddfr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1438-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1438\|p.1438]] |
> | Table C-321: EDDFR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1438-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1438\|p.1438]] |
> | 续表或相关原文（第1439页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1439-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1439\|p.1439]] |
> | Figure C-178: ext_edaa32pfr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1440-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1440\|p.1440]] |
> | Table C-324: EDAA32PFR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1440-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1440\|p.1440]] |
> | 续表或相关原文（第1441页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1441-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1441\|p.1441]] |
> | Figure C-179: ext_editctrl bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1442-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1442\|p.1442]] |
> | Table C-326: EDITCTRL bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1442-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1442\|p.1442]] |
> | Figure C-180: ext_dbgclaimset_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1443-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1443\|p.1443]] |
> | Table C-328: DBGCLAIMSET_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1443-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1443\|p.1443]] |
> | 续表或相关原文（第1444页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1444-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1444\|p.1444]] |
> | Figure C-181: ext_dbgclaimclr_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1445-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1445\|p.1445]] |
> | Table C-330: DBGCLAIMCLR_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1445-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1445\|p.1445]] |
> | Figure C-182: ext_eddevaff0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1446-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1446\|p.1446]] |
> | Table C-332: EDDEVAFF0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1446-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1446\|p.1446]] |
> | Figure C-183: ext_eddevaff1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1447-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1447\|p.1447]] |
> | Table C-334: EDDEVAFF1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1448-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1448\|p.1448]] |
> | Figure C-184: ext_edlar bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1449-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1449\|p.1449]] |
> | Table C-336: EDLAR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1449-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1449\|p.1449]] |
> | Figure C-185: ext_edlsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1450-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1450\|p.1450]] |
> | Table C-338: EDLSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1450-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1450\|p.1450]] |
> | 续表或相关原文（第1451页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1451-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1451\|p.1451]] |
> | Figure C-186: ext_dbgauthstatus_el1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1452-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1452\|p.1452]] |
> | Table C-340: DBGAUTHSTATUS_EL1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1452-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1452\|p.1452]] |
> | Figure C-187: ext_eddevarch bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1453-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1453\|p.1453]] |
> | Table C-342: EDDEVARCH bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1454-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1454\|p.1454]] |
> | Figure C-188: ext_eddevid2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1455-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1455\|p.1455]] |
> | Table C-344: EDDEVID2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1455-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1455\|p.1455]] |
> | Figure C-189: ext_eddevid1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1456-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1456\|p.1456]] |
> | Table C-346: EDDEVID1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1456-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1456\|p.1456]] |
> | Figure C-190: ext_eddevid bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1458-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1458\|p.1458]] |
> | Table C-348: EDDEVID bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1458-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1458\|p.1458]] |
> | Figure C-191: ext_eddevtype bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1459-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1459\|p.1459]] |
> | Table C-350: EDDEVTYPE bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1459-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1459\|p.1459]] |
> | Figure C-192: ext_edpidr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1460-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1460\|p.1460]] |
> | Table C-352: EDPIDR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1461-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1461\|p.1461]] |
> | Figure C-193: ext_edpidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1462-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1462\|p.1462]] |
> | Table C-354: EDPIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1462-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1462\|p.1462]] |
> | Figure C-194: ext_edpidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1463-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1463\|p.1463]] |
> | Table C-356: EDPIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1463-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1463\|p.1463]] |
> | Figure C-195: ext_edpidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1464-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1464\|p.1464]] |
> | Table C-358: EDPIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1465-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1465\|p.1465]] |
> | Figure C-196: ext_edpidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1466-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1466\|p.1466]] |
> | Table C-360: EDPIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1466-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1466\|p.1466]] |
> | Figure C-197: ext_edcidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1467-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1467\|p.1467]] |
> | Table C-362: EDCIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1467-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1467\|p.1467]] |
> | Figure C-198: ext_edcidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1469-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1469\|p.1469]] |
> | Table C-364: EDCIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1469-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1469\|p.1469]] |
> | Figure C-199: ext_edcidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1470-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1470\|p.1470]] |
> | Table C-366: EDCIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1470-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1470\|p.1470]] |
> | Figure C-200: ext_edcidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1471-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1471\|p.1471]] |
> | Table C-368: EDCIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1471-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1471\|p.1471]] |
> | Table C-370: Activity Monitors registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1472-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472\|p.1472]] |
> | 续表或相关原文（第1473页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1473-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473\|p.1473]] |
> | Figure C-201: ext_amevcntr00 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1474-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1474\|p.1474]] |
> | Table C-371: AMEVCNTR00 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1474-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1474\|p.1474]] |
> | Figure C-202: ext_amevcntr01 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1476-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1476\|p.1476]] |
> | Table C-374: AMEVCNTR01 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1476-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1476\|p.1476]] |
> | Figure C-203: ext_amevcntr02 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1477-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1477\|p.1477]] |
> | Table C-377: AMEVCNTR02 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1478-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1478\|p.1478]] |
> | Figure C-204: ext_amevcntr03 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1479-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1479\|p.1479]] |
> | Table C-380: AMEVCNTR03 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1479-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1479\|p.1479]] |
> | Figure C-205: ext_amevcntr10 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1481-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1481\|p.1481]] |
> | Table C-383: AMEVCNTR10 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1481-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1481\|p.1481]] |
> | Figure C-206: ext_amevcntr11 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1483-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1483\|p.1483]] |
> | Table C-386: AMEVCNTR11 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1483-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1483\|p.1483]] |
> | Figure C-207: ext_amevcntr12 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1484-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1484\|p.1484]] |
> | Table C-389: AMEVCNTR12 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1485-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1485\|p.1485]] |
> | Figure C-208: ext_amevtyper00 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1486-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1486\|p.1486]] |
> | Table C-392: AMEVTYPER00 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1486-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1486\|p.1486]] |
> | 续表或相关原文（第1487页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1487-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1487\|p.1487]] |
> | Figure C-209: ext_amevtyper01 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1488-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1488\|p.1488]] |
> | Table C-394: AMEVTYPER01 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1488-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1488\|p.1488]] |
> | Figure C-210: ext_amevtyper02 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1490-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1490\|p.1490]] |
> | Table C-396: AMEVTYPER02 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1490-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1490\|p.1490]] |
> | Figure C-211: ext_amevtyper03 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1492-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1492\|p.1492]] |
> | Table C-398: AMEVTYPER03 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1492-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1492\|p.1492]] |
> | Figure C-212: ext_amevtyper10 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1493-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1493\|p.1493]] |
> | Table C-400: AMEVTYPER10 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1493-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1493\|p.1493]] |
> | 续表或相关原文（第1494页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1494-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1494\|p.1494]] |
> | Figure C-213: ext_amevtyper11 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1495-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1495\|p.1495]] |
> | Table C-402: AMEVTYPER11 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1495-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1495\|p.1495]] |
> | Figure C-214: ext_amevtyper12 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1497-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1497\|p.1497]] |
> | Table C-404: AMEVTYPER12 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1497-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1497\|p.1497]] |
> | Figure C-215: ext_amcntenset0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1498-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1498\|p.1498]] |
> | Table C-406: AMCNTENSET0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1498-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1498\|p.1498]] |
> | 续表或相关原文（第1499页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1499-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1499\|p.1499]] |
> | Figure C-216: ext_amcntenset1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1500-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1500\|p.1500]] |
> | Table C-408: AMCNTENSET1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1500-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1500\|p.1500]] |
> | Figure C-217: ext_amcntenclr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1502-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1502\|p.1502]] |
> | Table C-410: AMCNTENCLR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1502-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1502\|p.1502]] |
> | Figure C-218: ext_amcntenclr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1503-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1503\|p.1503]] |
> | Table C-412: AMCNTENCLR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1503-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1503\|p.1503]] |
> | Figure C-219: ext_amcgcr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1505-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1505\|p.1505]] |
> | Table C-414: AMCGCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1505-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1505\|p.1505]] |
> | Figure C-220: ext_amcfgr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1506-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1506\|p.1506]] |
> | Table C-416: AMCFGR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1506-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1506\|p.1506]] |
> | 续表或相关原文（第1507页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1507-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1507\|p.1507]] |
> | Figure C-221: ext_amcr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1508-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1508\|p.1508]] |
> | Table C-418: AMCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1508-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1508\|p.1508]] |
> | Figure C-222: ext_amiidr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1509-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1509\|p.1509]] |
> | Table C-420: AMIIDR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1509-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1509\|p.1509]] |
> | 续表或相关原文（第1510页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1510-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1510\|p.1510]] |
> | Figure C-223: ext_amdevaff0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1511-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1511\|p.1511]] |
> | Table C-422: AMDEVAFF0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1511-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1511\|p.1511]] |
> | Figure C-224: ext_amdevaff1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1512-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1512\|p.1512]] |
> | Table C-424: AMDEVAFF1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1512-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1512\|p.1512]] |
> | Figure C-225: ext_amdevarch bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1513-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1513\|p.1513]] |
> | Table C-426: AMDEVARCH bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1513-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1513\|p.1513]] |
> | Figure C-226: ext_amdevtype bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1514-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1514\|p.1514]] |
> | Table C-428: AMDEVTYPE bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1514-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1514\|p.1514]] |
> | 续表或相关原文（第1515页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1515-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1515\|p.1515]] |
> | Figure C-227: ext_ampidr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1516-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1516\|p.1516]] |
> | Table C-430: AMPIDR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1516-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1516\|p.1516]] |
> | Figure C-228: ext_ampidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1517-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1517\|p.1517]] |
> | Table C-432: AMPIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1517-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1517\|p.1517]] |
> | Figure C-229: ext_ampidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1518-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1518\|p.1518]] |
> | Table C-434: AMPIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1518-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1518\|p.1518]] |
> | Figure C-230: ext_ampidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1519-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1519\|p.1519]] |
> | Table C-436: AMPIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1520-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1520\|p.1520]] |
> | Figure C-231: ext_ampidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1521-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1521\|p.1521]] |
> | Table C-438: AMPIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1521-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1521\|p.1521]] |
> | Figure C-232: ext_amcidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1522-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1522\|p.1522]] |
> | Table C-440: AMCIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1522-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1522\|p.1522]] |
> | Figure C-233: ext_amcidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1523-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1523\|p.1523]] |
> | Table C-442: AMCIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1523-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1523\|p.1523]] |
> | 续表或相关原文（第1524页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1524-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1524\|p.1524]] |
> | Figure C-234: ext_amcidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1525-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1525\|p.1525]] |
> | Table C-444: AMCIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1525-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1525\|p.1525]] |
> | Figure C-235: ext_amcidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1526-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526\|p.1526]] |
> | Table C-446: AMCIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1526-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526\|p.1526]] |
> | Table C-448: Trace unit registers summary | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1526-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526\|p.1526]] |
> | 续表或相关原文（第1527页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1527-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527\|p.1527]] |
> | 续表或相关原文（第1528页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1528-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528\|p.1528]] |
> | Figure C-236: ext_trcprgctlr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1529-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1529\|p.1529]] |
> | Table C-449: TRCPRGCTLR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1529-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1529\|p.1529]] |
> | Figure C-237: ext_trcstatr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1530-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1530\|p.1530]] |
> | Table C-451: TRCSTATR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1530-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1530\|p.1530]] |
> | 续表或相关原文（第1531页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1531-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1531\|p.1531]] |
> | Figure C-238: ext_trcconfigr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1532-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1532\|p.1532]] |
> | Table C-453: TRCCONFIGR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1532-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1532\|p.1532]] |
> | 续表或相关原文（第1533页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1533-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1533\|p.1533]] |
> | Figure C-239: ext_trcauxctlr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1534-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1534\|p.1534]] |
> | Table C-455: TRCAUXCTLR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1534-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1534\|p.1534]] |
> | Figure C-240: ext_trceventctl0r bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1535-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1535\|p.1535]] |
> | Table C-457: TRCEVENTCTL0R bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1536-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1536\|p.1536]] |
> | 续表或相关原文（第1537页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1537-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1537\|p.1537]] |
> | 续表或相关原文（第1538页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1538-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1538\|p.1538]] |
> | Figure C-241: ext_trceventctl1r bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1539-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1539\|p.1539]] |
> | Table C-459: TRCEVENTCTL1R bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1539-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1539\|p.1539]] |
> | 续表或相关原文（第1540页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1540-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1540\|p.1540]] |
> | Figure C-242: ext_trcrsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1541-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1541\|p.1541]] |
> | Table C-461: TRCRSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1541-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1541\|p.1541]] |
> | 续表或相关原文（第1542页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1542-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1542\|p.1542]] |
> | Figure C-243: ext_trctsctlr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1543-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1543\|p.1543]] |
> | Table C-463: TRCTSCTLR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1543-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1543\|p.1543]] |
> | 续表或相关原文（第1544页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1544-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1544\|p.1544]] |
> | Figure C-244: ext_trcsyncpr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1545-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1545\|p.1545]] |
> | Table C-465: TRCSYNCPR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1545-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1545\|p.1545]] |
> | 续表或相关原文（第1546页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1546-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1546\|p.1546]] |
> | Figure C-245: ext_trcccctlr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1547-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1547\|p.1547]] |
> | Table C-467: TRCCCCTLR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1548-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1548\|p.1548]] |
> | Figure C-246: ext_trcbbctlr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1549-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1549\|p.1549]] |
> | Table C-469: TRCBBCTLR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1549-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1549\|p.1549]] |
> | 续表或相关原文（第1550页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1550-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1550\|p.1550]] |
> | Figure C-247: ext_trctraceidr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1551-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1551\|p.1551]] |
> | Table C-471: TRCTRACEIDR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1551-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1551\|p.1551]] |
> | Figure C-248: ext_trcvictlr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1552-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1552\|p.1552]] |
> | Table C-473: TRCVICTLR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1553-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1553\|p.1553]] |
> | 续表或相关原文（第1554页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1554-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1554\|p.1554]] |
> | 续表或相关原文（第1555页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1555-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1555\|p.1555]] |
> | Figure C-249: ext_trcviiectlr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1556-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1556\|p.1556]] |
> | Table C-475: TRCVIIECTLR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1556-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1556\|p.1556]] |
> | 续表或相关原文（第1557页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1557-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1557\|p.1557]] |
> | Figure C-250: ext_trcvissctlr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1558-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1558\|p.1558]] |
> | Table C-477: TRCVISSCTLR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1559-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1559\|p.1559]] |
> | Figure C-251: ext_trcseqevr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1560-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1560\|p.1560]] |
> | Table C-479: TRCSEQEVR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1560-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1560\|p.1560]] |
> | 续表或相关原文（第1561页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1561-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1561\|p.1561]] |
> | 续表或相关原文（第1562页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1562-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1562\|p.1562]] |
> | Figure C-252: ext_trcseqevr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1563-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1563\|p.1563]] |
> | Table C-481: TRCSEQEVR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1563-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1563\|p.1563]] |
> | 续表或相关原文（第1564页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1564-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1564\|p.1564]] |
> | Figure C-253: ext_trcseqevr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1566-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1566\|p.1566]] |
> | Table C-483: TRCSEQEVR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1566-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1566\|p.1566]] |
> | 续表或相关原文（第1567页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1567-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1567\|p.1567]] |
> | Figure C-254: ext_trcseqrstevr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1568-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1568\|p.1568]] |
> | Table C-485: TRCSEQRSTEVR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1568-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1568\|p.1568]] |
> | 续表或相关原文（第1569页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1569-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1569\|p.1569]] |
> | Figure C-255: ext_trcseqstr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1570-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1570\|p.1570]] |
> | Table C-487: TRCSEQSTR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1570-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1570\|p.1570]] |
> | 续表或相关原文（第1571页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1571-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1571\|p.1571]] |
> | Figure C-256: ext_trcextinselr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1572-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1572\|p.1572]] |
> | Table C-489: TRCEXTINSELR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1572-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1572\|p.1572]] |
> | 续表或相关原文（第1573页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1573-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1573\|p.1573]] |
> | Figure C-257: ext_trcextinselr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1574-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1574\|p.1574]] |
> | Table C-491: TRCEXTINSELR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1574-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1574\|p.1574]] |
> | 续表或相关原文（第1575页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1575-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1575\|p.1575]] |
> | Figure C-258: ext_trcextinselr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1576-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1576\|p.1576]] |
> | Table C-493: TRCEXTINSELR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1576-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1576\|p.1576]] |
> | 续表或相关原文（第1577页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1577-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1577\|p.1577]] |
> | Figure C-259: ext_trcextinselr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1578-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1578\|p.1578]] |
> | Table C-495: TRCEXTINSELR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1578-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1578\|p.1578]] |
> | 续表或相关原文（第1579页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1579-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1579\|p.1579]] |
> | Figure C-260: ext_trccntrldvr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1580-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1580\|p.1580]] |
> | Table C-497: TRCCNTRLDVR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1580-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1580\|p.1580]] |
> | Figure C-261: ext_trccntrldvr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1582-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1582\|p.1582]] |
> | Table C-499: TRCCNTRLDVR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1582-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1582\|p.1582]] |
> | Figure C-262: ext_trccntctlr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1583-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1583\|p.1583]] |
> | Table C-501: TRCCNTCTLR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1583-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1583\|p.1583]] |
> | 续表或相关原文（第1584页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1584-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1584\|p.1584]] |
> | 续表或相关原文（第1585页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1585-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1585\|p.1585]] |
> | Figure C-263: ext_trccntctlr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1586-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1586\|p.1586]] |
> | Table C-503: TRCCNTCTLR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1586-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1586\|p.1586]] |
> | 续表或相关原文（第1587页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1587-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1587\|p.1587]] |
> | 续表或相关原文（第1588页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1588-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1588\|p.1588]] |
> | Figure C-264: ext_trccntvr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1589-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1589\|p.1589]] |
> | Table C-505: TRCCNTVR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1589-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1589\|p.1589]] |
> | Figure C-265: ext_trccntvr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1590-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1590\|p.1590]] |
> | Table C-507: TRCCNTVR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1591-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1591\|p.1591]] |
> | Figure C-266: ext_trcidr8 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1592-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1592\|p.1592]] |
> | Table C-509: TRCIDR8 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1592-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1592\|p.1592]] |
> | Figure C-267: ext_trcidr9 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1593-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1593\|p.1593]] |
> | Table C-511: TRCIDR9 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1593-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1593\|p.1593]] |
> | Figure C-268: ext_trcidr10 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1594-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1594\|p.1594]] |
> | Table C-513: TRCIDR10 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1594-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1594\|p.1594]] |
> | Figure C-269: ext_trcidr11 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1595-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1595\|p.1595]] |
> | Table C-515: TRCIDR11 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1595-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1595\|p.1595]] |
> | Figure C-270: ext_trcidr12 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1596-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1596\|p.1596]] |
> | Table C-517: TRCIDR12 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1596-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1596\|p.1596]] |
> | Figure C-271: ext_trcidr13 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1597-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1597\|p.1597]] |
> | Table C-519: TRCIDR13 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1598-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1598\|p.1598]] |
> | Figure C-272: ext_trcimspec0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1599-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1599\|p.1599]] |
> | Table C-521: TRCIMSPEC0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1599-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1599\|p.1599]] |
> | Figure C-273: ext_trcidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1600-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1600\|p.1600]] |
> | Table C-523: TRCIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1600-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1600\|p.1600]] |
> | 续表或相关原文（第1601页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1601-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1601\|p.1601]] |
> | Figure C-274: ext_trcidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1602-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1602\|p.1602]] |
> | Table C-525: TRCIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1602-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1602\|p.1602]] |
> | 续表或相关原文（第1603页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1603-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1603\|p.1603]] |
> | Figure C-275: ext_trcidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1604-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1604\|p.1604]] |
> | Table C-527: TRCIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1604-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1604\|p.1604]] |
> | Figure C-276: ext_trcidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1605-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1605\|p.1605]] |
> | Table C-529: TRCIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1606-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1606\|p.1606]] |
> | 续表或相关原文（第1607页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1607-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1607\|p.1607]] |
> | Figure C-277: ext_trcidr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1608-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1608\|p.1608]] |
> | Table C-531: TRCIDR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1608-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1608\|p.1608]] |
> | Figure C-278: ext_trcidr5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1610-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1610\|p.1610]] |
> | Table C-533: TRCIDR5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1610-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1610\|p.1610]] |
> | Figure C-279: ext_trcidr6 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1611-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1611\|p.1611]] |
> | Table C-535: TRCIDR6 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1611-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1611\|p.1611]] |
> | Figure C-280: ext_trcidr7 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1612-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1612\|p.1612]] |
> | Table C-537: TRCIDR7 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1613-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1613\|p.1613]] |
> | Figure C-281: ext_trcsscsr_n_ bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1614-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1614\|p.1614]] |
> | Table C-539: TRCSSCSR<n> bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1614-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1614\|p.1614]] |
> | 续表或相关原文（第1615页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1615-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1615\|p.1615]] |
> | Figure C-282: ext_trcoslsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1616-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1616\|p.1616]] |
> | Table C-541: TRCOSLSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1616-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1616\|p.1616]] |
> | 续表或相关原文（第1617页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1617-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1617\|p.1617]] |
> | Figure C-283: ext_trcpdcr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1618-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1618\|p.1618]] |
> | Table C-543: TRCPDCR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1618-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1618\|p.1618]] |
> | Figure C-284: ext_trcpdsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1619-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1619\|p.1619]] |
> | Table C-545: TRCPDSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1619-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1619\|p.1619]] |
> | 续表或相关原文（第1620页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1620-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1620\|p.1620]] |
> | Figure C-285: ext_trccidcctlr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1621-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1621\|p.1621]] |
> | Table C-547: TRCCIDCCTLR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1621-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1621\|p.1621]] |
> | Figure C-286: ext_trcvmidcctlr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1623-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1623\|p.1623]] |
> | Table C-549: TRCVMIDCCTLR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1623-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1623\|p.1623]] |
> | Figure C-287: ext_trcitctrl bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1625-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1625\|p.1625]] |
> | Table C-551: TRCITCTRL bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1625-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1625\|p.1625]] |
> | Figure C-288: ext_trcclaimset bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1627-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1627\|p.1627]] |
> | Table C-553: TRCCLAIMSET bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1627-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1627\|p.1627]] |
> | Figure C-289: ext_trcclaimclr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1628-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1628\|p.1628]] |
> | Table C-555: TRCCLAIMCLR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1629-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1629\|p.1629]] |
> | Figure C-290: ext_trcdevaff bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1630-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1630\|p.1630]] |
> | Table C-557: TRCDEVAFF bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1630-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1630\|p.1630]] |
> | Figure C-291: ext_trclar bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1631-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1631\|p.1631]] |
> | Table C-559: TRCLAR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1631-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1631\|p.1631]] |
> | Figure C-292: ext_trclsr bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1632-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1632\|p.1632]] |
> | Table C-561: TRCLSR bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1633-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1633\|p.1633]] |
> | Figure C-293: ext_trcauthstatus bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1634-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1634\|p.1634]] |
> | Table C-563: TRCAUTHSTATUS bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1634-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1634\|p.1634]] |
> | 续表或相关原文（第1635页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1635-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1635\|p.1635]] |
> | 续表或相关原文（第1636页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1636-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1636\|p.1636]] |
> | Figure C-294: ext_trcdevarch bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1637-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1637\|p.1637]] |
> | Table C-565: TRCDEVARCH bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1638-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1638\|p.1638]] |
> | Figure C-295: ext_trcdevid2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1639-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1639\|p.1639]] |
> | Table C-567: TRCDEVID2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1639-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1639\|p.1639]] |
> | Figure C-296: ext_trcdevid1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1640-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1640\|p.1640]] |
> | Table C-569: TRCDEVID1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1640-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1640\|p.1640]] |
> | Figure C-297: ext_trcdevid bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1641-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1641\|p.1641]] |
> | Table C-571: TRCDEVID bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1642-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1642\|p.1642]] |
> | Figure C-298: ext_trcdevtype bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1643-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1643\|p.1643]] |
> | Table C-573: TRCDEVTYPE bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1643-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1643\|p.1643]] |
> | Figure C-299: ext_trcpidr4 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1644-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1644\|p.1644]] |
> | Table C-575: TRCPIDR4 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1644-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1644\|p.1644]] |
> | 续表或相关原文（第1645页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1645-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1645\|p.1645]] |
> | Figure C-300: ext_trcpidr5 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1646-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1646\|p.1646]] |
> | Table C-577: TRCPIDR5 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1646-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1646\|p.1646]] |
> | Figure C-301: ext_trcpidr6 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1647-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1647\|p.1647]] |
> | Table C-579: TRCPIDR6 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1647-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1647\|p.1647]] |
> | Figure C-302: ext_trcpidr7 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1648-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1648\|p.1648]] |
> | Table C-581: TRCPIDR7 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1649-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1649\|p.1649]] |
> | Figure C-303: ext_trcpidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1650-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1650\|p.1650]] |
> | Table C-583: TRCPIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1650-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1650\|p.1650]] |
> | Figure C-304: ext_trcpidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1651-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1651\|p.1651]] |
> | Table C-585: TRCPIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1651-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1651\|p.1651]] |
> | Figure C-305: ext_trcpidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1652-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1652\|p.1652]] |
> | Table C-587: TRCPIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1653-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1653\|p.1653]] |
> | Figure C-306: ext_trcpidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1654-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1654\|p.1654]] |
> | Table C-589: TRCPIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1654-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1654\|p.1654]] |
> | 续表或相关原文（第1655页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1655-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1655\|p.1655]] |
> | Figure C-307: ext_trccidr0 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1656-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1656\|p.1656]] |
> | Table C-591: TRCCIDR0 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1656-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1656\|p.1656]] |
> | Figure C-308: ext_trccidr1 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1657-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1657\|p.1657]] |
> | Table C-593: TRCCIDR1 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1657-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1657\|p.1657]] |
> | Figure C-309: ext_trccidr2 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1658-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1658\|p.1658]] |
> | Table C-595: TRCCIDR2 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1659-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1659\|p.1659]] |
> | Figure C-310: ext_trccidr3 bit assignments | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1660-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1660\|p.1660]] |
> | Table C-597: TRCCIDR3 bit descriptions | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1660-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1660\|p.1660]] |


### 图表 附录D与E

原文范围 p.1661-1668。

> [!info]- 7个编号图表 · 7页截图（含续页）
> | 原文编号与标题 | 原页截图 | PDF |
> |---|---|---|
> | Table D-1: Armv8 Debug UNPREDICTABLE behaviors | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1662-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1662\|p.1662]] |
> | 续表或相关原文（第1663页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1663-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1663\|p.1663]] |
> | Table D-2: Other UNPREDICTABLE behaviors | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1664-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1664\|p.1664]] |
> | 续表或相关原文（第1665页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1665-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1665\|p.1665]] |
> | Table E-1: Issue 0000-02 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1666-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1666\|p.1666]] |
> | Table E-2: Differences between Issue 0000-02 and Issue 0000-03 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1666-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1666\|p.1666]] |
> | Table E-3: Differences between Issue 0000-03 and 0000-04 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1666-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1666\|p.1666]] |
> | Table E-4: Differences between Issue 0000-04 and 0001-05 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1667-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1667\|p.1667]] |
> | Table E-5: Differences between Issue 0001-05 and 0003-06 | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1667-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1667\|p.1667]] |
> | 续表或相关原文（第1668页） | [[Neoverse/01_assets/N2-Core-TRM-r0p3/p1668-original.png\|查看截图]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1668\|p.1668]] |


## 综合理解与学习路线

N2 第8/9章解释缓存体系和 CHI 接口实现；事务和协议规则继续从 [[CHI-节点角色与能力]]、[[CHI-通道与方向]]、[[CHI-Cache状态模型]]、[[CHI-信用流控与Request-Retry]] 阅读。TRM 的实现参数不能取代 CHI 规范中的完整事务条件。

### 先建立一条完整的数据路径

```text
分支预测/取指 → L1 I-cache 或 L0 MOP cache → decode/rename/乱序执行
                                            ↓ load/store
                       VA → L1 TLB →（miss）L2 TLB/页表遍历
                                            ↓ PA + 属性
                       L1 D-cache → 私有 L2 → CPU bridge / CHI
                                            ↓
                                    DSU-110 → 系统一致性与内存
```

这是理解关系的概念路径，不是周期精确流水图；MOP 命中可避开重复译码，TLB miss 和 cache miss 是不同的等待原因。请求可能被其他缓存满足，不是所有 L2 miss 都必然读 DDR。

### 按问题串联章节

| 问题 | 阅读顺序 |
|---|---|
| L0 MOP cache 存什么、如何减少前端工作 | 第3→7→10章，注意第10章原始编码公开边界 |
| 一条 load 为什么慢 | 第6→8→9章，再用第18/22章观察 |
| 写大数组为什么未必反复填入L1 | 第8章 write streaming，结合第9章缓存分配 |
| RN 一致性事务如何经过CPU缓存体系 | 第8/9章，再看 [[CHI-Cache状态模型]] 与 [[CHI-节点角色与能力]] |
| WFI、retention、掉电分别保留什么 | 第4→5章，再看第11/17/19章的错误与调试影响 |
| ECC纠错、poison、SError和错误中断的关系 | 第11章→附录 B.14；不要只看一个 status bit |
| 想知道“多少”“哪条慢”“走到哪” | 第18 PMU→22 SPE→19 ETE/20 TRBE，AMU 用于长期管理 |
| 给系统做性能或调试工具 | 第15/17章发现能力→功能章→附录 B/C 精确访问定义 |
| 理解整个平台而非单核 | 本文第2/9章→[[RD-N2-Reference-Design-中文精读]] |

学习完成后应能区分四组经常混淆的概念：MOP 内容与机器码/数据、translation 与 cache lookup、coherence 与内存可观察/顺序、计数与采样/追踪。阅读参数时同时记住“固定实现能力、构建选项、运行配置、系统集成条件”各属于哪一层。

## 待确认事项与使用边界

下列疑点保留原文，不擅自修订。实际编程应核对后续正式勘误、适用版 Arm ARM 或你的平台文档。

| 项目 | 疑点与处理 | 原文回查 |
|---|---|---|
| L2 TLB相联路数与way编码 | 功能描述为5路，RAM诊断编码列出的way范围存在口径疑点；不扩写为6路TLB | §6.1、§10.2.3，p.58、92 |
| 内部RAM字段 | 个别字段位区间/宽度说明有疑点；原编码图表保留，未自行修正 | 第10章，尤其相关L1/L2 TLB表 |
| 外部abort的Device措辞 | 原文条件含容易混淆的 acquire/release 用语；同步/异步分类按原表回查，不推导新规则 | §6.6，p.61-63 |
| Direct connect与L3通用表述 | N2明确仅Direct connect，但个别缓存/调试/PMU段落仍含L3或通用DSU示意；不据此认定N2具有DSU L3 | 第2/8/17/18章 |
| AMU辅助组 | 描述包含辅助/programmable字样，但实现事件表列Reserved；不虚构三种可用事件 | 第21章，p.151-152 |
| SPE事件bit5 | 正文表标题与寄存器字段描述口径需一起核对；过滤解释采用位域中TLB walk说明 | p.157、1115、1124 |
| PPM可编程含义 | 名称/引言提到控制CPU，但公开接口RO、位域Reserved | §C.2，p.1151-1156 |
| MOP具体二进制语义 | 有RAM返回宽度/读取接口，未公开足以把每个entry还原成指令的完整格式；示例仅概念解释 | §7、§10 |

本文没有依据本手册推断具体 SoC 的主频、IPC、DDR 延迟、CHIE 的所有事务细节、Linux 工具版本或后续 N2 修订能力。需要这些信息时应另附可验证来源，不能回填为本版 TRM 原文结论。

维护时先核对来源版本，再修改对应章节；新增外部证据应标明来源和与本版差异。本文的章节负责解释，文末索引负责回查；通过 [[#阅读导航]] 在同一文件内跳转。
