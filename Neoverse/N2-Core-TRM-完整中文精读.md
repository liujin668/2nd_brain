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
verification: source-text-and-figure-index-checked
created: 2026-10-09
updated: 2026-10-10
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

原表 Table 11-2 的 RAS 寄存器总表和完整位图入口：[[N2-Core-TRM-正文原图表#第11章 原图表]]、[[N2-Core-TRM-寄存器索引#B14 RAS寄存器]]。

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

原表 Table 12-1 跨 p.102-104，全部保留于 [[N2-Core-TRM-正文原图表#第12章 原图表]]。

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

原表 Table 15-1 跨 p.107-108，见 [[N2-Core-TRM-正文原图表#第15章 原图表]]。

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

原表 Table 16-1 与 B.3 的基地址/PEID 原位图入口：[[N2-Core-TRM-正文原图表#第16章 原图表]]、[[N2-Core-TRM-附录B原图表#原文第454页]]、[[N2-Core-TRM-附录B原图表#原文第455页]]。

## 第17章 调试系统

**原文范围：p.111-121，§17.1-17.10。** 调试分 self-hosted 与 external；DSU DebugBlock 单独供电，使核或 cluster 掉电后仍可保持连接。

### 17.1 调试组件如何连接

DebugBlock 与 cluster 之间通过双向 APB 接口传递多数调试访问和 CTI trigger；每核 trace unit 输出经 funnel 汇聚到 ATB。每核 CTI 位于 DebugBlock，CTM 连接触发网络。

原图 Figure 17-1，p.111：

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0111-original.png]]

**读图边界**：这是通用 DynamIQ 组织图，画出了 SCU、L3、snoop filter；N2 的 Direct connect 配置不能据此增加这些实际组件。

原图 Figure 17-2，p.112 的外部调试链路见 [[N2-Core-TRM-正文原图表#第17章 原图表]]。Debug host 发高层命令，协议转换设备连接目标 SoC，再通过 CoreSight 访问指定核。Self-hosted debug 则由目标核上的 monitor 软件处理，不必依赖另一台主机。

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

全部原图、访问条件表、ROM 表和寄存器总表已保留于 [[N2-Core-TRM-正文原图表#第17章 原图表]]。

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

原始 **Table 18-1，p.122-132** 的整张事件表及全部续页：[[N2-Core-TRM-正文原图表#第18章 原图表]]。

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

全部资源/能力原表、流程图、总表和续页见 [[N2-Core-TRM-正文原图表#第19章 原图表]]。

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

全部原流程、事件/数据来源总表与 register summary：[[N2-Core-TRM-正文原图表#第22章 原图表]]。PMSIDR/PMBIDR 原位图与对应表见 [[N2-Core-TRM-附录B原图表#原文第1126页]] 至 [[N2-Core-TRM-附录B原图表#原文第1129页]]。

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

详细条目见 [[N2-Core-TRM-寄存器索引#A2 PMU寄存器]]、[[N2-Core-TRM-寄存器索引#A6 浮点寄存器]]。全部原位图、编码与续表见 [[N2-Core-TRM-附录A原图表]]。

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

理解说明：把线程标记为不同 PARTID，与“把 N2 私有 L2 强制分成两块固定容量”不是同一个结论。不能只根据本附录推断整个 CMN/SLC 的容量分配策略。原总表与字段见 [[N2-Core-TRM-附录B原图表#原文第1048页]] 起。

### B.7 RAS：选择记录之后才读状态与附加信息

先用 `ERRIDR_EL1` 理解记录能力，通过 `ERRSELR_EL1` 选择记录，再读取 `ERXFR_EL1` 的能力、`ERXSTATUS_EL1` 的状态，按有效位解释 `ERXADDR_EL1/ERXMISC*`。控制/注入类寄存器与读取报告不同，具体清除和写入语义需核对原位域。

不能把 UNKNOWN reset、地址无效或未实现字段解释成“无错误”。也不能根据一个 error status 就忽略第11章中的同步/异步异常、poison、FHI/ERI 与电源状态。对应条目见 [[N2-Core-TRM-寄存器索引#B14 RAS寄存器]]。

### B.8 性能与追踪：按实现能力配置

PMU 的控制/事件类型/计数值对应第18章；ETE 配置对应第19章；AMU 对应第21章；SPE 对应第22章。名称相似的 buffer、counter、filter 不能互换。

SPE 先读 `PMSIDR_EL1/PMBIDR_EL1` 的能力和 buffer 要求，再理解 `PMSIRR_EL1`、`PMSEVFR_EL1`、`PMSLATFR_EL1` 等采样配置。TRBE 的 `TRBBASER_EL1/TRBLIMITR_EL1/TRBPTR_EL1` 记录 ETE 追踪缓冲；SPE 的 `PMB*` 是另一条数据记录路径。

### B.9 逐项条目的阅读顺序

1. 先看 Configurations：是否存在、依赖哪个 FEAT、是否当前执行状态可用。
2. 看 Attributes：宽度、RO/RW/WO 或各字段访问类型。
3. 看 Reset：`x`/UNKNOWN 与 0 不同；Cold/Warm reset 也可能不同。
4. 看 Bit descriptions：RES0/RES1、RAZ/WI、有效位、清除语义必须逐项遵守。
5. 最后看 Accessibility：当前 EL、安全状态、trap/锁等条件，不能只按寄存器名称后缀判断。

有些分组只有总表，没有在本手册内逐项展开。索引会明确标出，并指向原总表；没有的说明不会补写成 N2 的确定行为。入口：[[N2-Core-TRM-寄存器索引]]；完整位图与续表：[[N2-Core-TRM-附录B原图表]]。

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

先从本组 summary 查 offset/width/description，再进入具体条目确认位域与访问条件。原图表保留每组总表、所有编号位图与位域续表，见 [[N2-Core-TRM-附录C原图表]]；名字检索用 [[N2-Core-TRM-寄存器索引]]。

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

全部原行为表及续表见 [[N2-Core-TRM-附录DE原图表]]。

## 附录E 文档版本变化

**原文范围：p.1666-1668，§E.1。** 文档内容变动可能是增补、澄清或自动生成寄存器条目的变化；不能把每条 change 都理解为硬件新增功能或已确认的 silicon erratum。

| 文档版本 | 对应状态 | 对本次学习最重要的变化 |
|---|---|---|
| 0000-02 | r0p0 early access | 增补 SPE、L2 编码和 PMU 事件信息 |
| 0000-03 | r0p0 的后续文档 | 增补 DSU 依赖项、SPE/trace 寄存器；补充电源模式与 write streaming；移除 PMSSRR 条目 |
| 0000-04 | r0p0 的后续文档 | RNG、transaction queue、架构版本、bus port 和 PMU→trace 信息更新 |
| 0001-05 | r0p1 首版 | 更新 full retention、AMU、L2 行为、转换响应和多个字段说明 |
| 0003-06 | r0p3 首版，本次依据 | 更新 feature/转换响应、L1 data tag 位位置和 CoreSight revision；导入新的自动生成寄存器说明 |

读到网络旧资料或不同修订的截图时，先核对产品 revision 与 document issue。第10章的编码、第9章 TQ 数量、第5章 retention、第16章 RNG 等均是历史上修改过的内容，必须引用本版原页。原 change tables：[[N2-Core-TRM-附录DE原图表#原文第1666页]] 起。

## 综合理解与学习路线

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

维护时先核对来源版本，再修改对应章节；新增外部证据应标明来源和与本版差异。图表册与寄存器索引负责回查，中文精读负责解释，入口统一放在 [[Neoverse-MOC]]。
