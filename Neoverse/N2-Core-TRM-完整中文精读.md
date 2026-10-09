---
type: guide
status: draft
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
verification: pending
created: 2026-10-09
updated: 2026-10-09
---

# Neoverse N2 Core TRM 完整中文精读

N2 是一个实现 Armv9.0-A 的 CPU 核：前端准备指令，乱序执行单元组织计算，MMU 与缓存共同完成访存；通过 Direct connect DSU-110 接入系统，由电源、RAS、中断、调试和性能监测机制保证可管理、可观察。理解它时，要同时区分**架构行为、N2 实现细节和整个 SoC 的集成配置**。

本文覆盖原手册 **22 章及附录 A-E，共 1668 页**。正文按章解释职责、机制、配置条件和重要限制；寄存器附录按功能解读，另提供本手册逐项寄存器索引与完整原图表回查入口，不把重复的访问伪代码逐页翻译。需要精确编程时，仍需核对原位域、复位值和访问条件。

原文：[本库 PDF](00_sources/arm_neoverse_n2_core_trm_102099_0003_06_en.pdf)；Obsidian 内可用 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]。页码以 PDF 的印刷页码为准，与本文件副本的 PDF 页序一致。副本保持原字节，原文件不修改。

> [!info] 事实与解释
> “原文依据”标明可回查的章节及页码；“理解说明”和“教学示例”解释原理，示例地址、周期和伪结构不代表 N2 的真实测量结果或内部位格式。“待确认”保留原文中的口径问题，不自动补全。
>
> 原图表来自你提供的 PDF 截图，保留水印、标题、图例及跨页续表。为避免丢失条件和脚注，图表册按原页正文区域保存；中文表格是归纳表，不能替代原编码表。

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
- [[#综合理解与学习路线]]
- [[#待确认事项与使用边界]]

配套回查：[[N2-Core-TRM-寄存器索引]] · [[N2-Core-TRM-正文原图表]] · [[N2-Core-TRM-附录A原图表]] · [[N2-Core-TRM-附录B原图表]] · [[N2-Core-TRM-附录C原图表]] · [[N2-Core-TRM-附录DE原图表]]。

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

| 层次 | 谁决定 | 示例 |
|---|---|---|
| Build-time | IP 实现者，RTL 配置与物理实现 | L2 大小、TQ 大小、Crypto、coherent I-cache、RNG、ELA |
| Integration | SoC 集成者，连接和绑带输入 | 外部中断接口、复位行为、RNG 外设关联 |
| Software | 固件、hypervisor、OS | MMU、缓存、预取、电源、PMU 和 SPE 控制 |

L2 512KB/1024KB，TQ 48/56/64 是构建选项，不能假定 OS 可以随意在线变更这些容量。ELA-600 是独立许可产品，ELA ATB FIFO 深度可为 4、8、16、32、64；Crypto 同样需额外许可。L2 RAM 时序也有配置选项。

### 2.3 架构特性应逐项判断

| 类别 | 重要能力或限制 |
|---|---|
| 基本执行 | A32/T32/A64 指令集；AArch32 只在 EL0；AArch64 覆盖 EL0-EL3 |
| 内存 | 48 位 VA/PA；HAFDBS、16 位 VMID、PBHA；不支持 LPA/大 VA 扩展 |
| 虚拟化 | NV/NV2 嵌套虚拟化特性支持，具体行为查架构手册 |
| 安全 | MTE 总是实现；指针认证增强、FPAC；Crypto 与 RNG 受选配条件影响 |
| 数据处理 | SVE/SVE2、BF16、I8MM；F32MM/F64MM 矩阵扩展不支持 |
| 观测 | PMU、AMU、SPE、ETE、TRBE；ELA 可选 |
| 不支持的其他项 | TME；FEAT_ExS；FEAT_VPIPT；LSMAOC；AA32HPD |

“架构可选扩展”与“这个 N2 IP 可以裁剪的组件”不是同一回事。例如 SPE 在架构上是可选扩展，但手册明确说 N2 实现 SPE；是否可裁剪不能仅凭 optional 一词推断。

**待确认**：Table 2-8 使用 `FEAT_SV2` 这一拼写，并列出 SVE 加密指令 Supported；§2.2/§3.1 又说明 Crypto 是选配且单独许可。本文保留两处口径，不据表中 Supported 推断所有芯片都启用加密指令。

全部架构支持原表：[[N2-Core-TRM-正文原图表#第2章 原图表|Tables 2-1 至 2-10，含续表]]。

### 2.4 测试与设计流程

ATPG 测试核逻辑，MBIST 测试 RAM；接口使用细节在集成手册。N2 交付为可综合的 SystemVerilog RTL，实际产品还需配置、加入工艺单元与 RAM、综合和布局布线、集成到 SoC、编写初始化软件。测试接口存在不表示软件自动获得任意内部状态访问权限。

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

若与 DSU 同步共用时钟，或不需要 DVFS，VCORE 与 VCLUSTER 可连接同一供电。原文还有域分布图 Figure 5-2，见 [[N2-Core-TRM-正文原图表#第5章 原图表]]。

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

FULL_RET 还要求 retention timer 到期，且没有临时开钟活动；snoop、maintenance、debug/GIC 访问既可使其退出 retention，也可能仍不让软件退出 WFI/WFE。原模式表 Table 5-1，p.50，见图表册。

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

**原文依据**：§5.4-5.6，p.49-56。全部电源原图表见 [[N2-Core-TRM-正文原图表#第5章 原图表]]。

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

**原文范围：p.65-68，§7.1-7.4。** 前端同时解决“下一条取哪里”“机器码是什么”“能否复用内部操作表示”。

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

所有 **Tables 10-1 至 10-62** 及跨页续表已截入 [[N2-Core-TRM-正文原图表#第10章 原图表]]，实际解码应查看对应原表。

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
