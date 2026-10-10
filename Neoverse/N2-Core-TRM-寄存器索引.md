---
type: reference
status: reviewed
topics: [Neoverse, N2, CPU, architecture]
aliases: ["N2寄存器回查索引"]
tags: [arm, neoverse, cpu, reference]
sources: ["[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]"]
source_document: "102099_0003_06_en"
source_revision: "r0p3 / Issue 06"
source_date: 2022-10-27
spec_issue: "CHI E"
source_sections: ["A", "B", "C"]
evidence: source-derived
verification: source-text-and-figure-index-checked
created: 2026-10-09
updated: 2026-10-10
---

# N2 Core TRM 寄存器索引

按原手册的 30 个功能分组整理。收录 **548 个实际展开说明条目**，并列出各组总表识别到的寄存器名称；只有总表的寄存器不会被补写成具有完整位域说明。

英文寄存器名保留，中文组名帮助定位功能。名称后方是原文章节号和 PDF 页码；数组或成组寄存器可能共用一个展开条目，所以条目数不等于硬件寄存器数量。

阅读入口：[[N2-Core-TRM-完整中文精读#附录B AArch64寄存器]]。需要写寄存器时，必须继续核对原文 Configurations、Reset、Bit descriptions、Accessibility。

## 功能导航

| 原分组 | 功能 | 起始原页 | 展开条目 |
|---|---|---|---|
| A.1 | [[#A1 特殊用途寄存器\|特殊用途寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160\|p.160]] | 0 |
| A.2 | [[#A2 PMU寄存器\|PMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160\|p.160]] | 12 |
| A.3 | [[#A3 通用定时器寄存器\|通用定时器寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207\|p.207]] | 0 |
| A.4 | [[#A4 调试寄存器\|调试寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207\|p.207]] | 0 |
| A.5 | [[#A5 通用系统控制寄存器\|通用系统控制寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208\|p.208]] | 0 |
| A.6 | [[#A6 浮点寄存器\|浮点寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208\|p.208]] | 1 |
| A.7 | [[#A7 AMU寄存器\|AMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213\|p.213]] | 14 |
| B.1 | [[#B1 通用系统控制寄存器\|通用系统控制寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242\|p.242]] | 46 |
| B.2 | [[#B2 调试寄存器\|调试寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351\|p.351]] | 26 |
| B.3 | [[#B3 随机数寄存器\|随机数寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453\|p.453]] | 2 |
| B.4 | [[#B4 系统指令\|系统指令]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=456\|p.456]] | 1 |
| B.5 | [[#B5 识别与能力寄存器\|识别与能力寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458\|p.458]] | 45 |
| B.6 | [[#B6 特殊用途寄存器\|特殊用途寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556\|p.556]] | 0 |
| B.7 | [[#B7 PMU寄存器\|PMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556\|p.556]] | 16 |
| B.8 | [[#B8 GIC寄存器\|GIC寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633\|p.633]] | 14 |
| B.9 | [[#B9 通用定时器寄存器\|通用定时器寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779\|p.779]] | 0 |
| B.10 | [[#B10 其他系统控制寄存器\|其他系统控制寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780\|p.780]] | 0 |
| B.11 | [[#B11 AMU寄存器\|AMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781\|p.781]] | 16 |
| B.12 | [[#B12 ETE寄存器\|ETE寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=816\|p.816]] | 57 |
| B.13 | [[#B13 MPAM寄存器\|MPAM寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048\|p.1048]] | 9 |
| B.14 | [[#B14 RAS寄存器\|RAS寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070\|p.1070]] | 13 |
| B.15 | [[#B15 SPE寄存器\|SPE寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114\|p.1114]] | 3 |
| B.16 | [[#B16 TRBE寄存器\|TRBE寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130\|p.1130]] | 0 |
| C.1 | [[#C1 外部CoreROM寄存器\|外部CoreROM寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131\|p.1131]] | 16 |
| C.2 | [[#C2 外部PPM寄存器\|外部PPM寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151\|p.1151]] | 6 |
| C.3 | [[#C3 外部PMU寄存器\|外部PMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157\|p.1157]] | 60 |
| C.4 | [[#C4 外部CTI寄存器\|外部CTI寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279\|p.1279]] | 23 |
| C.5 | [[#C5 外部调试寄存器\|外部调试寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315\|p.1315]] | 58 |
| C.6 | [[#C6 外部AMU寄存器\|外部AMU寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472\|p.1472]] | 35 |
| C.7 | [[#C7 外部ETE寄存器\|外部ETE寄存器]] | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526\|p.1526]] | 75 |

## 回查方法

- Obsidian 搜索寄存器名，或从下面的功能导航进入相应分组。
- 总表名称包含只有概要、没有单独展开的架构寄存器。其具体位域需结合原文提示查适用的 Arm ARM。
- 同一功能的 AArch32、AArch64、外部接口分别列在 A/B/C；不要将不同访问视图相加为实现数量。
- 位域图和续表位于对应原图表册；访问伪代码等普通页直接用 PDF 页码链接查看。
- 原文标题可能跨行；这里仅保存标题首行，寄存器名与章节号按原文。英文名称的完整展开以原页为准。

## A1 特殊用途寄存器

原分组 A.1，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]；图表回查 [[N2-Core-TRM-附录A原图表#原文第160页]]。

### 总表寄存器名

`DSPSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `DLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]）

本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

## A2 PMU寄存器

原分组 A.2，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]；图表回查 [[N2-Core-TRM-附录A原图表#原文第160页]]。

### 总表寄存器名

`PMCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMCNTENSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMCNTENCLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMOVSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMSWINC`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMSELR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMCEID0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]） · `PMCEID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMCCNTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMXEVTYPER`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMXEVCNTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMUSERENR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMOVSSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMCEID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMCEID3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVCNTR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMEVTYPER5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]） · `PMCCFILTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| A.2.1 | PMEVCNTR0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=162\|p.162]] |
| A.2.2 | PMEVCNTR1, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=165\|p.165]] |
| A.2.3 | PMEVCNTR2, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=168\|p.168]] |
| A.2.4 | PMEVCNTR3, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=171\|p.171]] |
| A.2.5 | PMEVCNTR4, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=174\|p.174]] |
| A.2.6 | PMEVCNTR5, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=178\|p.178]] |
| A.2.7 | PMEVTYPER0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=181\|p.181]] |
| A.2.8 | PMEVTYPER1, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=185\|p.185]] |
| A.2.9 | PMEVTYPER2, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=189\|p.189]] |
| A.2.10 | PMEVTYPER3, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=194\|p.194]] |
| A.2.11 | PMEVTYPER4, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=198\|p.198]] |
| A.2.12 | PMEVTYPER5, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=202\|p.202]] |

## A3 通用定时器寄存器

原分组 A.3，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]；图表回查 [[N2-Core-TRM-附录A原图表#原文第207页]]。

### 总表寄存器名

`CNTFRQ`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTP_TVAL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTP_CTL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTV_TVAL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTV_CTL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTPCT`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTVCT`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTP_CVAL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `CNTV_CVAL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]）

本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

## A4 调试寄存器

原分组 A.4，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]；图表回查 [[N2-Core-TRM-附录A原图表#原文第207页]]。

### 总表寄存器名

`DBGDSCRint`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `DBGDTRRXint`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `DBGDTRTXint`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]）

本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

## A5 通用系统控制寄存器

原分组 A.5，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]；图表回查 [[N2-Core-TRM-附录A原图表#原文第208页]]。

### 总表寄存器名

`TPIDRURW`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]） · `TPIDRURO`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]）

本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

## A6 浮点寄存器

原分组 A.6，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]；图表回查 [[N2-Core-TRM-附录A原图表#原文第208页]]。

### 总表寄存器名

`FPSCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| A.6.1 | FPSCR, Floating-Point Status and Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208\|p.208]] |

## A7 AMU寄存器

原分组 A.7，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]；图表回查 [[N2-Core-TRM-附录A原图表#原文第213页]]。

### 总表寄存器名

`AMCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCFGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCGCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMUSERENR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCNTENCLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCNTENSET0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCNTENCLR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMCNTENSET1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER00`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER01`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER02`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER03`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVTYPER12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]） · `AMEVCNTR00`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR01`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR02`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]） · `AMEVCNTR03`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| A.7.1 | AMEVTYPER00, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214\|p.214]] |
| A.7.2 | AMEVTYPER01, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=216\|p.216]] |
| A.7.3 | AMEVTYPER02, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=218\|p.218]] |
| A.7.4 | AMEVTYPER03, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=220\|p.220]] |
| A.7.5 | AMEVTYPER10, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=222\|p.222]] |
| A.7.6 | AMEVTYPER11, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=223\|p.223]] |
| A.7.7 | AMEVTYPER12, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=225\|p.225]] |
| A.7.8 | AMEVCNTR00, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=227\|p.227]] |
| A.7.9 | AMEVCNTR10, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=229\|p.229]] |
| A.7.10 | AMEVCNTR01, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=231\|p.231]] |
| A.7.11 | AMEVCNTR11, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=233\|p.233]] |
| A.7.12 | AMEVCNTR02, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=235\|p.235]] |
| A.7.13 | AMEVCNTR12, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=237\|p.237]] |
| A.7.14 | AMEVCNTR03, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=239\|p.239]] |

## B1 通用系统控制寄存器

原分组 B.1，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第242页]]。

### 总表寄存器名

`ACTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `RGSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `GCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `TTBR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `TTBR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `TCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APIAKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APIAKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APIBKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APIBKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APDAKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APDAKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APDBKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APDBKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]） · `APGAKeyLo_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `APGAKeyHi_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `SPSel`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `CurrentEL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `PAN`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `UAO`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `AFSR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `AFSR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `ESR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `TFSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `TFSRE0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `FAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `PAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `MAIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `AMAIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LORSA_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LOREA_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LORN_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LORC_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `LORID_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `VBAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `ISR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `CONTEXTIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]） · `TPIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `SCXTNUM_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUECTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUECTLR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUPPMCR3_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUPWRCTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_ATCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR6_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `IMP_CPUACTLR7_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `AIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `NZCV`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `DAIF`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `DIT`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `SSBS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `TCO`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `FPCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `FPSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `TPIDR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]） · `TPIDRRO_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `SCXTNUM_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `ACTLR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `HACR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TTBR0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TTBR1_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VTTBR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VTCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VNCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VSTTBR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VSTCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `AFSR0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `AFSR1_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `ESR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TFSR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `FAR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `HPFAR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `MAIR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `AMAIR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `VBAR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `CONTEXTIDR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `TPIDR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]） · `SCXTNUM_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_ATCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_AVTCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `ACTLR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `SCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `CPTR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `MDCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `TTBR0_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `TCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `AFSR0_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `AFSR1_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `ESR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `TFSR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `FAR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `MAIR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `AMAIR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `VBAR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `RVBAR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `RMR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `TPIDR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `SCXTNUM_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_CPUPPMCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_CPUPPMCR2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]） · `IMP_CPUPPMCR4_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPPMCR5_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPPMCR6_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUACTLR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_ATCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPSELR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPOR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPMR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPOR2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPMR2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]） · `IMP_CPUPFR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.1.1 | ACTLR_EL1, Auxiliary Control Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247\|p.247]] |
| B.1.2 | AFSR0_EL1, Auxiliary Fault Status Register 0 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=249\|p.249]] |
| B.1.3 | AFSR1_EL1, Auxiliary Fault Status Register 1 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=252\|p.252]] |
| B.1.4 | AMAIR_EL1, Auxiliary Memory Attribute Indirection Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=255\|p.255]] |
| B.1.5 | LORID_EL1, LORegionID (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=257\|p.257]] |
| B.1.6 | IMP_CPUACTLR_EL1, CPU Auxiliary Control Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=259\|p.259]] |
| B.1.7 | IMP_CPUACTLR2_EL1, CPU Auxiliary Control Register 2 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=261\|p.261]] |
| B.1.8 | IMP_CPUACTLR3_EL1, CPU Auxiliary Control Register 3 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=263\|p.263]] |
| B.1.9 | IMP_CPUACTLR4_EL1, CPU Auxiliary Control Register 4 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=264\|p.264]] |
| B.1.10 | IMP_CPUECTLR_EL1, CPU Extended Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=266\|p.266]] |
| B.1.11 | IMP_CPUECTLR2_EL1, CPU Extended Control Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=275\|p.275]] |
| B.1.12 | IMP_CPUPPMCR3_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=280\|p.280]] |
| B.1.13 | IMP_CPUPWRCTLR_EL1, CPU Power Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=282\|p.282]] |
| B.1.14 | IMP_ATCR_EL1, CPU Auxiliary Translation Control Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=284\|p.284]] |
| B.1.15 | IMP_CPUACTLR5_EL1, CPU Auxiliary Control Register 5 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=287\|p.287]] |
| B.1.16 | IMP_CPUACTLR6_EL1, CPU Auxiliary Control Register 6 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=288\|p.288]] |
| B.1.17 | IMP_CPUACTLR7_EL1, CPU Auxiliary Control Register 7 (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=290\|p.290]] |
| B.1.18 | AIDR_EL1, Auxiliary ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=292\|p.292]] |
| B.1.19 | FPCR, Floating-point Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=293\|p.293]] |
| B.1.20 | FPSR, Floating-point Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=297\|p.297]] |
| B.1.21 | ACTLR_EL2, Auxiliary Control Register (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=302\|p.302]] |
| B.1.22 | HACR_EL2, Hypervisor Auxiliary Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=305\|p.305]] |
| B.1.23 | AFSR0_EL2, Auxiliary Fault Status Register 0 (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=307\|p.307]] |
| B.1.24 | AFSR1_EL2, Auxiliary Fault Status Register 1 (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=309\|p.309]] |
| B.1.25 | AMAIR_EL2, Auxiliary Memory Attribute Indirection Register (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=312\|p.312]] |
| B.1.26 | IMP_ATCR_EL2, CPU Auxiliary Translation Control Register (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=315\|p.315]] |
| B.1.27 | IMP_AVTCR_EL2, CPU Virtualization Auxiliary Translation Control | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=317\|p.317]] |
| B.1.28 | ACTLR_EL3, Auxiliary Control Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=319\|p.319]] |
| B.1.29 | AFSR0_EL3, Auxiliary Fault Status Register 0 (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=322\|p.322]] |
| B.1.30 | AFSR1_EL3, Auxiliary Fault Status Register 1 (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=324\|p.324]] |
| B.1.31 | AMAIR_EL3, Auxiliary Memory Attribute Indirection Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=325\|p.325]] |
| B.1.32 | RMR_EL3, Reset Management Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=327\|p.327]] |
| B.1.33 | IMP_CPUPPMCR_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=329\|p.329]] |
| B.1.34 | IMP_CPUPPMCR2_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=330\|p.330]] |
| B.1.35 | IMP_CPUPPMCR4_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=332\|p.332]] |
| B.1.36 | IMP_CPUPPMCR5_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=333\|p.333]] |
| B.1.37 | IMP_CPUPPMCR6_EL3, CPU Power Performance Management | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=335\|p.335]] |
| B.1.38 | IMP_CPUACTLR_EL3, CPU Auxiliary Control Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=336\|p.336]] |
| B.1.39 | IMP_ATCR_EL3, CPU Auxiliary Translation Control Register (EL2) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=338\|p.338]] |
| B.1.40 | IMP_CPUPSELR_EL3, Selected Instruction Private Select Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=340\|p.340]] |
| B.1.41 | IMP_CPUPCR_EL3, Selected Instruction Private Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=342\|p.342]] |
| B.1.42 | IMP_CPUPOR_EL3, Selected Instruction Private Opcode Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=343\|p.343]] |
| B.1.43 | IMP_CPUPMR_EL3, Selected Instruction Private Mask Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=345\|p.345]] |
| B.1.44 | IMP_CPUPOR2_EL3, Selected Instruction Private Opcode Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=346\|p.346]] |
| B.1.45 | IMP_CPUPMR2_EL3, Selected Instruction Private Mask Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=348\|p.348]] |
| B.1.46 | IMP_CPUPFR_EL3, Selected Instruction Private Flag Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=349\|p.349]] |

## B2 调试寄存器

原分组 B.2，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第351页]]。

### 总表寄存器名

`OSDTRRX_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWVR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWCR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWVR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWCR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `MDCCINT_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `MDSCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWVR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWCR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `OSDTRTX_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWVR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGWCR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBVR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]） · `DBGBCR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `OSECCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `MDRAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `OSLAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `OSLSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `OSDLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGPRCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGCLAIMSET_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGCLAIMCLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGAUTHSTATUS_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `MDCCSR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGDTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGDTRRX_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `DBGDTRTX_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `TRFCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `MDCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `TRFCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_IDATA0_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_IDATA1_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_IDATA2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_DDATA0_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_DDATA1_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]） · `IMP_DDATA2_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.2.1 | DBGBVR0_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352\|p.352]] |
| B.2.2 | DBGBCR0_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=358\|p.358]] |
| B.2.3 | DBGWVR0_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=363\|p.363]] |
| B.2.4 | DBGWCR0_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=366\|p.366]] |
| B.2.5 | DBGBVR1_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=370\|p.370]] |
| B.2.6 | DBGBCR1_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=376\|p.376]] |
| B.2.7 | DBGWVR1_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=380\|p.380]] |
| B.2.8 | DBGWCR1_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=383\|p.383]] |
| B.2.9 | DBGBVR2_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=387\|p.387]] |
| B.2.10 | DBGBCR2_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=393\|p.393]] |
| B.2.11 | DBGWVR2_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=398\|p.398]] |
| B.2.12 | DBGWCR2_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=401\|p.401]] |
| B.2.13 | DBGBVR3_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=405\|p.405]] |
| B.2.14 | DBGBCR3_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=411\|p.411]] |
| B.2.15 | DBGWVR3_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=416\|p.416]] |
| B.2.16 | DBGWCR3_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=419\|p.419]] |
| B.2.17 | DBGBVR4_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=423\|p.423]] |
| B.2.18 | DBGBCR4_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=429\|p.429]] |
| B.2.19 | DBGBVR5_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=434\|p.434]] |
| B.2.20 | DBGBCR5_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=440\|p.440]] |
| B.2.21 | IMP_IDATA0_EL3, Instruction Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=445\|p.445]] |
| B.2.22 | IMP_IDATA1_EL3, Instruction Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=447\|p.447]] |
| B.2.23 | IMP_IDATA2_EL3, Instruction Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=448\|p.448]] |
| B.2.24 | IMP_DDATA0_EL3, Data Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=449\|p.449]] |
| B.2.25 | IMP_DDATA1_EL3, Data Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=450\|p.450]] |
| B.2.26 | IMP_DDATA2_EL3, Data Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=451\|p.451]] |

## B3 随机数寄存器

原分组 B.3，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453|p.453]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第453页]]。

### 总表寄存器名

`IMP_CPURNDBR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453|p.453]]） · `IMP_CPURNDPEID_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453|p.453]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.3.1 | IMP_CPURNDBR_EL3, CPU Random Number Base Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453\|p.453]] |
| B.3.2 | IMP_CPURNDPEID_EL3, CPU Random Number Packet Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=455\|p.455]] |

## B4 系统指令

原分组 B.4，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=456|p.456]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第456页]]。

### 总表寄存器名

`Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=456|p.456]]） · `SYS_IMP_RAMINDEX`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=457|p.457]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.4.1 | SYS_IMP_RAMINDEX, RAM Index | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=457\|p.457]] |

## B5 识别与能力寄存器

原分组 B.5，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第458页]]。

### 总表寄存器名

`MIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `MPIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `REVIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_PFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_PFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_DFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_AFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_MMFR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_ISAR6_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `MVFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `MVFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `MVFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]） · `ID_PFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_DFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_MMFR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64PFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64PFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64PFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64ZFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64DFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64DFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64AFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64AFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64ISAR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64ISAR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64ISAR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64MMFR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64MMFR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `ID_AA64MMFR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `MPAMIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `IMP_CPUCFR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CCSIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CLIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CCSIDR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `GMID_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CSSELR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `CTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `DCZID_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `VPIDR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]） · `VMPIDR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.5.1 | MIDR_EL1, Main ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459\|p.459]] |
| B.5.2 | MPIDR_EL1, Multiprocessor Affinity Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=461\|p.461]] |
| B.5.3 | REVIDR_EL1, Revision ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=463\|p.463]] |
| B.5.4 | ID_PFR0_EL1, AArch32 Processor Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=464\|p.464]] |
| B.5.5 | ID_PFR1_EL1, AArch32 Processor Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=467\|p.467]] |
| B.5.6 | ID_DFR0_EL1, AArch32 Debug Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=469\|p.469]] |
| B.5.7 | ID_AFR0_EL1, AArch32 Auxiliary Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=471\|p.471]] |
| B.5.8 | ID_MMFR0_EL1, AArch32 Memory Model Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=473\|p.473]] |
| B.5.9 | ID_MMFR1_EL1, AArch32 Memory Model Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=475\|p.475]] |
| B.5.10 | ID_MMFR2_EL1, AArch32 Memory Model Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=477\|p.477]] |
| B.5.11 | ID_MMFR3_EL1, AArch32 Memory Model Feature Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=479\|p.479]] |
| B.5.12 | ID_ISAR0_EL1, AArch32 Instruction Set Attribute Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=482\|p.482]] |
| B.5.13 | ID_ISAR1_EL1, AArch32 Instruction Set Attribute Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=484\|p.484]] |
| B.5.14 | ID_ISAR2_EL1, AArch32 Instruction Set Attribute Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=486\|p.486]] |
| B.5.15 | ID_ISAR3_EL1, AArch32 Instruction Set Attribute Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=488\|p.488]] |
| B.5.16 | ID_ISAR4_EL1, AArch32 Instruction Set Attribute Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=490\|p.490]] |
| B.5.17 | ID_ISAR5_EL1, AArch32 Instruction Set Attribute Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=493\|p.493]] |
| B.5.18 | ID_MMFR4_EL1, AArch32 Memory Model Feature Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=495\|p.495]] |
| B.5.19 | ID_ISAR6_EL1, AArch32 Instruction Set Attribute Register 6 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=497\|p.497]] |
| B.5.20 | MVFR0_EL1, AArch32 Media and VFP Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=500\|p.500]] |
| B.5.21 | MVFR1_EL1, AArch32 Media and VFP Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=502\|p.502]] |
| B.5.22 | MVFR2_EL1, AArch32 Media and VFP Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=504\|p.504]] |
| B.5.23 | ID_PFR2_EL1, AArch32 Processor Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=506\|p.506]] |
| B.5.24 | ID_DFR1_EL1, Debug Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=508\|p.508]] |
| B.5.25 | ID_MMFR5_EL1, AArch32 Memory Model Feature Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=509\|p.509]] |
| B.5.26 | ID_AA64PFR0_EL1, AArch64 Processor Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=511\|p.511]] |
| B.5.27 | ID_AA64PFR1_EL1, AArch64 Processor Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=514\|p.514]] |
| B.5.28 | ID_AA64PFR2_EL1, AArch64 Processor Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=516\|p.516]] |
| B.5.29 | ID_AA64ZFR0_EL1, SVE Feature ID register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=517\|p.517]] |
| B.5.30 | ID_AA64DFR0_EL1, AArch64 Debug Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=520\|p.520]] |
| B.5.31 | ID_AA64DFR1_EL1, AArch64 Debug Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=522\|p.522]] |
| B.5.32 | ID_AA64AFR0_EL1, AArch64 Auxiliary Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=523\|p.523]] |
| B.5.33 | ID_AA64AFR1_EL1, AArch64 Auxiliary Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=525\|p.525]] |
| B.5.34 | ID_AA64ISAR0_EL1, AArch64 Instruction Set Attribute Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=526\|p.526]] |
| B.5.35 | ID_AA64ISAR1_EL1, AArch64 Instruction Set Attribute Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=530\|p.530]] |
| B.5.36 | ID_AA64ISAR2_EL1, AArch64 Instruction Set Attribute Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=533\|p.533]] |
| B.5.37 | ID_AA64MMFR0_EL1, AArch64 Memory Model Feature Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=535\|p.535]] |
| B.5.38 | ID_AA64MMFR1_EL1, AArch64 Memory Model Feature Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=537\|p.537]] |
| B.5.39 | ID_AA64MMFR2_EL1, AArch64 Memory Model Feature Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=540\|p.540]] |
| B.5.40 | MPAMIDR_EL1, MPAM ID Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=543\|p.543]] |
| B.5.41 | IMP_CPUCFR_EL1, CPU Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=545\|p.545]] |
| B.5.42 | CLIDR_EL1, Cache Level ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=546\|p.546]] |
| B.5.43 | GMID_EL1, Multiple tag transfer ID register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=550\|p.550]] |
| B.5.44 | CTR_EL0, Cache Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=552\|p.552]] |
| B.5.45 | DCZID_EL0, Data Cache Zero ID register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=554\|p.554]] |

## B6 特殊用途寄存器

原分组 B.6，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第556页]]。

### 总表寄存器名

`SPSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `ELR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SP_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `DSPSR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `DLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `ELR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SP_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_irq`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_abt`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_und`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_fiq`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SPSR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `ELR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `SP_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]）

本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

## B7 PMU寄存器

原分组 B.7，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第556页]]。

### 总表寄存器名

`PMINTENSET_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `PMINTENCLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]） · `PMMIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCNTENSET_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCNTENCLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMOVSCLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMSWINC_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMSELR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCEID0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCEID1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMCCNTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMXEVTYPER_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMXEVCNTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMUSERENR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMOVSSET_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR2_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR3_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR4_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVCNTR5_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVTYPER0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVTYPER1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVTYPER2_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]） · `PMEVTYPER3_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558|p.558]]） · `PMEVTYPER4_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558|p.558]]） · `PMEVTYPER5_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558|p.558]]） · `PMCCFILTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558|p.558]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.7.1 | PMMIR_EL1, Performance Monitors Machine Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558\|p.558]] |
| B.7.2 | PMCR_EL0, Performance Monitors Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=560\|p.560]] |
| B.7.3 | PMCEID0_EL0, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=566\|p.566]] |
| B.7.4 | PMCEID1_EL0, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=573\|p.573]] |
| B.7.5 | PMEVCNTR0_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=580\|p.580]] |
| B.7.6 | PMEVCNTR1_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=583\|p.583]] |
| B.7.7 | PMEVCNTR2_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=587\|p.587]] |
| B.7.8 | PMEVCNTR3_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=591\|p.591]] |
| B.7.9 | PMEVCNTR4_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=594\|p.594]] |
| B.7.10 | PMEVCNTR5_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=598\|p.598]] |
| B.7.11 | PMEVTYPER0_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=602\|p.602]] |
| B.7.12 | PMEVTYPER1_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=607\|p.607]] |
| B.7.13 | PMEVTYPER2_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=612\|p.612]] |
| B.7.14 | PMEVTYPER3_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=617\|p.617]] |
| B.7.15 | PMEVTYPER4_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=622\|p.622]] |
| B.7.16 | PMEVTYPER5_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=628\|p.628]] |

## B8 GIC寄存器

原分组 B.8，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第633页]]。

### 总表寄存器名

`ICC_PMR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_PMR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_IAR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_IAR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `Register`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_EOIR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_EOIR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_HPPIR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_HPPIR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_BPR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_AP0R0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_AP0R0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_AP1R0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_AP1R0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICC_DIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]） · `ICV_DIR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_RPR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_RPR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_SGI1R_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_ASGI1R_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `Group`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_SGI0R_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_IAR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_IAR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_EOIR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_EOIR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_HPPIR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_HPPIR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_BPR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_BPR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_CTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_CTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_SRE_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_IGRPEN0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_IGRPEN0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_IGRPEN1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICV_IGRPEN1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICH_AP0R0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICH_AP1R0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]） · `ICC_SRE_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_HCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_VTR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_MISR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_EISR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_ELRSR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_VMCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_LR0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_LR1_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_LR2_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICH_LR3_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICC_CTLR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICC_SRE_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]） · `ICC_IGRPEN1_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.8.1 | ICC_AP0R0_EL1, Interrupt Controller Active Priorities Group 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635\|p.635]] |
| B.8.2 | ICV_AP0R0_EL1, Interrupt Controller Virtual Active Priorities Group | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=645\|p.645]] |
| B.8.3 | ICC_AP1R0_EL1, Interrupt Controller Active Priorities Group 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=654\|p.654]] |
| B.8.4 | ICV_AP1R0_EL1, Interrupt Controller Virtual Active Priorities Group | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=669\|p.669]] |
| B.8.5 | ICC_CTLR_EL1, Interrupt Controller Control Register (EL1) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=679\|p.679]] |
| B.8.6 | ICV_CTLR_EL1, Interrupt Controller Virtual Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=683\|p.683]] |
| B.8.7 | ICH_AP0R0_EL2, Interrupt Controller Hyp Active Priorities Group 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=687\|p.687]] |
| B.8.8 | ICH_AP1R0_EL2, Interrupt Controller Hyp Active Priorities Group 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=722\|p.722]] |
| B.8.9 | ICH_VTR_EL2, Interrupt Controller VGIC Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=756\|p.756]] |
| B.8.10 | ICH_LR0_EL2, Interrupt Controller List Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=758\|p.758]] |
| B.8.11 | ICH_LR1_EL2, Interrupt Controller List Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=762\|p.762]] |
| B.8.12 | ICH_LR2_EL2, Interrupt Controller List Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=767\|p.767]] |
| B.8.13 | ICH_LR3_EL2, Interrupt Controller List Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=771\|p.771]] |
| B.8.14 | ICC_CTLR_EL3, Interrupt Controller Control Register (EL3) | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=775\|p.775]] |

## B9 通用定时器寄存器

原分组 B.9，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第779页]]。

### 总表寄存器名

`CNTKCTL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTFRQ_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTPCT_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTVCT_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTP_TVAL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTP_CTL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTP_CVAL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTV_TVAL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTV_CTL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTV_CVAL_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTVOFF_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTHCTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]） · `CNTHP_TVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHP_CTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHP_CVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHV_TVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHV_CTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHV_CVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHVS_TVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHVS_CTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHVS_CVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHPS_TVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHPS_CTL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTHPS_CVAL_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTPS_TVAL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTPS_CTL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CNTPS_CVAL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]）

本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

## B10 其他系统控制寄存器

原分组 B.10，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第780页]]。

### 总表寄存器名

`SCTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `CPACR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `ZCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `SCTLR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]） · `HCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `CPTR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `HSTR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `ZCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `SCTLR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `ZCR_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]）

本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

## B11 AMU寄存器

原分组 B.11，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第781页]]。

### 总表寄存器名

`AMCR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCFGR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCGCR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMUSERENR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCNTENCLR0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCNTENSET0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCNTENCLR1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMCNTENSET1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVCNTR00_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVCNTR01_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVCNTR02_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVCNTR03_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVTYPER00_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]） · `AMEVTYPER01_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER02_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER03_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVCNTR10_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVCNTR11_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVCNTR12_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER10_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER11_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]） · `AMEVTYPER12_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.11.1 | AMCFGR_EL0, Activity Monitors Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782\|p.782]] |
| B.11.2 | AMCGCR_EL0, Activity Monitors Counter Group Configuration | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=784\|p.784]] |
| B.11.3 | AMEVCNTR00_EL0, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=786\|p.786]] |
| B.11.4 | AMEVCNTR01_EL0, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=788\|p.788]] |
| B.11.5 | AMEVCNTR02_EL0, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=790\|p.790]] |
| B.11.6 | AMEVCNTR03_EL0, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=793\|p.793]] |
| B.11.7 | AMEVTYPER00_EL0, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=795\|p.795]] |
| B.11.8 | AMEVTYPER01_EL0, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=797\|p.797]] |
| B.11.9 | AMEVTYPER02_EL0, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=799\|p.799]] |
| B.11.10 | AMEVTYPER03_EL0, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=801\|p.801]] |
| B.11.11 | AMEVCNTR10_EL0, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=804\|p.804]] |
| B.11.12 | AMEVCNTR11_EL0, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=806\|p.806]] |
| B.11.13 | AMEVCNTR12_EL0, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=808\|p.808]] |
| B.11.14 | AMEVTYPER10_EL0, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=810\|p.810]] |
| B.11.15 | AMEVTYPER11_EL0, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=812\|p.812]] |
| B.11.16 | AMEVTYPER12_EL0, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=814\|p.814]] |

## B12 ETE寄存器

原分组 B.12，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=816|p.816]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第817页]]。

### 总表寄存器名

`Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=816|p.816]]） · `TRCTRACEIDR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCVICTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQEVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR8`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIMSPEC0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCPRGCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCVIIECTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQEVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR9`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCVISSCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQEVR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSTATR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCCONFIGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCCNTCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCCNTCTLR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCIDR13`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCAUXCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQRSTEVR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCSEQSTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCEVENTCTL0R`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]） · `TRCEXTINSELR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCCNTVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCEVENTCTL1R`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCEXTINSELR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCCNTVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCRSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCEXTINSELR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCEXTINSELR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCTSCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCSYNCPR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCCCCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCBBCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCIDR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCSSCCR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCOSLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCRSCTLR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]） · `TRCRSCTLR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR8`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCSSCSR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR9`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR13`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR14`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCRSCTLR15`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACVR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]） · `TRCACATR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACVR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACATR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACVR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACATR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACVR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCACATR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCCIDCVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCVMIDCVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCCIDCCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCVMIDCCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCCLAIMSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCCLAIMCLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCAUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]） · `TRCDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.12.1 | TRCSEQEVR0, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820\|p.820]] |
| B.12.2 | TRCIDR8, ID Register 8 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=824\|p.824]] |
| B.12.3 | TRCIMSPEC0, IMP DEF Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=826\|p.826]] |
| B.12.4 | TRCSEQEVR1, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=828\|p.828]] |
| B.12.5 | TRCSEQEVR2, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=832\|p.832]] |
| B.12.6 | TRCIDR10, ID Register 10 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=835\|p.835]] |
| B.12.7 | TRCIDR11, ID Register 11 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=837\|p.837]] |
| B.12.8 | TRCCNTCTLR0, Counter Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=838\|p.838]] |
| B.12.9 | TRCIDR12, ID Register 12 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=842\|p.842]] |
| B.12.10 | TRCCNTCTLR1, Counter Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=844\|p.844]] |
| B.12.11 | TRCIDR13, ID Register 13 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=848\|p.848]] |
| B.12.12 | TRCEXTINSELR0, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=849\|p.849]] |
| B.12.13 | TRCCNTVR0, Counter Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=853\|p.853]] |
| B.12.14 | TRCIDR0, ID Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=855\|p.855]] |
| B.12.15 | TRCEXTINSELR1, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=858\|p.858]] |
| B.12.16 | TRCCNTVR1, Counter Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=861\|p.861]] |
| B.12.17 | TRCIDR1, ID Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=863\|p.863]] |
| B.12.18 | TRCEXTINSELR2, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=865\|p.865]] |
| B.12.19 | TRCIDR2, ID Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=868\|p.868]] |
| B.12.20 | TRCEXTINSELR3, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=870\|p.870]] |
| B.12.21 | TRCIDR3, ID Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=873\|p.873]] |
| B.12.22 | TRCIDR4, ID Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=876\|p.876]] |
| B.12.23 | TRCIDR5, ID Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=878\|p.878]] |
| B.12.24 | TRCSSCCR0, Single-shot Comparator Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=880\|p.880]] |
| B.12.25 | TRCRSCTLR2, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=883\|p.883]] |
| B.12.26 | TRCRSCTLR3, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=891\|p.891]] |
| B.12.27 | TRCRSCTLR4, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=897\|p.897]] |
| B.12.28 | TRCRSCTLR5, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=904\|p.904]] |
| B.12.29 | TRCRSCTLR6, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=910\|p.910]] |
| B.12.30 | TRCRSCTLR7, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=917\|p.917]] |
| B.12.31 | TRCRSCTLR8, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=923\|p.923]] |
| B.12.32 | TRCSSCSR0, Single-shot Comparator Control Status Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=930\|p.930]] |
| B.12.33 | TRCRSCTLR9, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=933\|p.933]] |
| B.12.34 | TRCRSCTLR10, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=940\|p.940]] |
| B.12.35 | TRCRSCTLR11, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=947\|p.947]] |
| B.12.36 | TRCRSCTLR12, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=953\|p.953]] |
| B.12.37 | TRCRSCTLR13, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=960\|p.960]] |
| B.12.38 | TRCRSCTLR14, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=966\|p.966]] |
| B.12.39 | TRCRSCTLR15, Resource Selection Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=973\|p.973]] |
| B.12.40 | TRCACVR0, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=979\|p.979]] |
| B.12.41 | TRCACATR0, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=982\|p.982]] |
| B.12.42 | TRCACVR1, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=987\|p.987]] |
| B.12.43 | TRCACATR1, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=990\|p.990]] |
| B.12.44 | TRCACVR2, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=995\|p.995]] |
| B.12.45 | TRCACATR2, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=998\|p.998]] |
| B.12.46 | TRCACVR3, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1003\|p.1003]] |
| B.12.47 | TRCACATR3, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1006\|p.1006]] |
| B.12.48 | TRCACVR4, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1011\|p.1011]] |
| B.12.49 | TRCACATR4, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1014\|p.1014]] |
| B.12.50 | TRCACVR5, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1019\|p.1019]] |
| B.12.51 | TRCACATR5, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1022\|p.1022]] |
| B.12.52 | TRCACVR6, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1027\|p.1027]] |
| B.12.53 | TRCACATR6, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1030\|p.1030]] |
| B.12.54 | TRCACVR7, Address Comparator Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1035\|p.1035]] |
| B.12.55 | TRCACATR7, Address Comparator Access Type Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1038\|p.1038]] |
| B.12.56 | TRCCIDCVR0, Context Identifier Comparator Value Registers <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1043\|p.1043]] |
| B.12.57 | TRCVMIDCVR0, Virtual Context Identifier Comparator Value | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1045\|p.1045]] |

## B13 MPAM寄存器

原分组 B.13，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第1048页]]。

### 总表寄存器名

`MPAM1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAM0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMHCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPMV_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAM2_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM0_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM1_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM2_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM3_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM4_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM5_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM6_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAMVPM7_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]） · `MPAM3_EL3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.13.1 | MPAMVPMV_EL2, MPAM Virtual Partition Mapping Valid Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048\|p.1048]] |
| B.13.2 | MPAMVPM0_EL2, MPAM Virtual PARTID Mapping Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1051\|p.1051]] |
| B.13.3 | MPAMVPM1_EL2, MPAM Virtual PARTID Mapping Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1054\|p.1054]] |
| B.13.4 | MPAMVPM2_EL2, MPAM Virtual PARTID Mapping Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1056\|p.1056]] |
| B.13.5 | MPAMVPM3_EL2, MPAM Virtual PARTID Mapping Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1058\|p.1058]] |
| B.13.6 | MPAMVPM4_EL2, MPAM Virtual PARTID Mapping Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1061\|p.1061]] |
| B.13.7 | MPAMVPM5_EL2, MPAM Virtual PARTID Mapping Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1063\|p.1063]] |
| B.13.8 | MPAMVPM6_EL2, MPAM Virtual PARTID Mapping Register 6 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1066\|p.1066]] |
| B.13.9 | MPAMVPM7_EL2, MPAM Virtual PARTID Mapping Register 7 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1068\|p.1068]] |

## B14 RAS寄存器

原分组 B.14，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070|p.1070]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第1070页]]。

### 总表寄存器名

`ERRIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070|p.1070]]） · `ERRSELR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070|p.1070]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070|p.1070]]） · `ERXFR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXCTLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXSTATUS_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXADDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXPFGF_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXPFGCTL_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXPFGCDN_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXMISC0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXMISC1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXMISC2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `ERXMISC3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `DISR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `VSESR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]） · `VDISR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.14.1 | ERRIDR_EL1, Error Record ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071\|p.1071]] |
| B.14.2 | ERRSELR_EL1, Error Record Select Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1073\|p.1073]] |
| B.14.3 | ERXFR_EL1, Selected Error Record Feature Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1075\|p.1075]] |
| B.14.4 | ERXCTLR_EL1, Selected Error Record Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1078\|p.1078]] |
| B.14.5 | ERXSTATUS_EL1, Selected Error Record Primary Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1081\|p.1081]] |
| B.14.6 | ERXADDR_EL1, Selected Error Record Address Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1087\|p.1087]] |
| B.14.7 | ERXPFGF_EL1, Selected Pseudo-fault Generation Feature register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1090\|p.1090]] |
| B.14.8 | ERXPFGCTL_EL1, Selected Pseudo-fault Generation Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1094\|p.1094]] |
| B.14.9 | ERXPFGCDN_EL1, Selected Pseudo-fault Generation Countdown | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1098\|p.1098]] |
| B.14.10 | ERXMISC0_EL1, Selected Error Record Miscellaneous Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1101\|p.1101]] |
| B.14.11 | ERXMISC1_EL1, Selected Error Record Miscellaneous Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1107\|p.1107]] |
| B.14.12 | ERXMISC2_EL1, Selected Error Record Miscellaneous Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1109\|p.1109]] |
| B.14.13 | ERXMISC3_EL1, Selected Error Record Miscellaneous Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1112\|p.1112]] |

## B15 SPE寄存器

原分组 B.15，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第1114页]]。

### 总表寄存器名

`PMSCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSICR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSIRR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSFCR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSEVFR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]） · `PMSLATFR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMSIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMBLIMITR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMBPTR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMBSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMBIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]） · `PMSCR_EL2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| B.15.1 | PMSEVFR_EL1, Sampling Event Filter Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115\|p.1115]] |
| B.15.2 | PMSIDR_EL1, Sampling Profiling ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1126\|p.1126]] |
| B.15.3 | PMBIDR_EL1, Profiling Buffer ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1128\|p.1128]] |

## B16 TRBE寄存器

原分组 B.16，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]；图表回查 [[N2-Core-TRM-附录B原图表#原文第1130页]]。

### 总表寄存器名

`TRBLIMITR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBPTR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBBASER_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBSR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBMAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBTRG_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `TRBIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]） · `Page`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]）

本组在本手册只有总表，没有单独展开条目；精确架构定义需查适用版 Arm ARM。

## C1 外部CoreROM寄存器

原分组 C.1，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]；图表回查 [[N2-Core-TRM-附录C原图表#原文第1131页]]。

### 总表寄存器名

`COREROM_ROMENTRY0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_ROMENTRY1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_ROMENTRY2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_ROMENTRY3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_AUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_DEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_DEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_PIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_CIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_CIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_CIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]） · `COREROM_CIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| C.1.1 | COREROM_ROMENTRY0, Core ROM table Entry 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131\|p.1131]] |
| C.1.2 | COREROM_ROMENTRY1, Core ROM table Entry 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1133\|p.1133]] |
| C.1.3 | COREROM_ROMENTRY2, Core ROM table Entry 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1134\|p.1134]] |
| C.1.4 | COREROM_ROMENTRY3, Core ROM table Entry 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1135\|p.1135]] |
| C.1.5 | COREROM_AUTHSTATUS, Core ROM table Authentication Status | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1137\|p.1137]] |
| C.1.6 | COREROM_DEVARCH, Core ROM table Device Architecture Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1138\|p.1138]] |
| C.1.7 | COREROM_DEVTYPE, Core ROM table Device Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1139\|p.1139]] |
| C.1.8 | COREROM_PIDR4, Core ROM table Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1140\|p.1140]] |
| C.1.9 | COREROM_PIDR0, Core ROM table Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1142\|p.1142]] |
| C.1.10 | COREROM_PIDR1, Core ROM table Peripheral Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1143\|p.1143]] |
| C.1.11 | COREROM_PIDR2, Core ROM table Peripheral Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1144\|p.1144]] |
| C.1.12 | COREROM_PIDR3, Core ROM table Peripheral Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1145\|p.1145]] |
| C.1.13 | COREROM_CIDR0, Core ROM table Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1146\|p.1146]] |
| C.1.14 | COREROM_CIDR1, Core ROM table Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1147\|p.1147]] |
| C.1.15 | COREROM_CIDR2, Core ROM table Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1149\|p.1149]] |
| C.1.16 | COREROM_CIDR3, Core ROM table Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1150\|p.1150]] |

## C2 外部PPM寄存器

原分组 C.2，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]；图表回查 [[N2-Core-TRM-附录C原图表#原文第1151页]]。

### 总表寄存器名

`CPUPPMCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]） · `CPUPPMCR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| C.2.1 | CPUPPMCR, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151\|p.1151]] |
| C.2.2 | CPUPPMCR2, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1152\|p.1152]] |
| C.2.3 | CPUPPMCR3, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1153\|p.1153]] |
| C.2.4 | CPUPPMCR4, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1154\|p.1154]] |
| C.2.5 | CPUPPMCR5, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1155\|p.1155]] |
| C.2.6 | CPUPPMCR6, Power Performance Management Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1156\|p.1156]] |

## C3 外部PMU寄存器

原分组 C.3，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]；图表回查 [[N2-Core-TRM-附录C原图表#原文第1157页]]。

### 总表寄存器名

`PMEVCNTR0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR2_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR3_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR4_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMEVCNTR5_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMCCNTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]） · `PMPCSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCID1SR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMVIDSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCID2SR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER0_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER1_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER2_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER3_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER4_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVTYPER5_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCCFILTR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMPCSSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCIDSSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMSSSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCCNTSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMEVCNTSR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMSSCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCNTENSET_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCNTENCLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMINTENSET_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMINTENCLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMOVSCLR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMSWINC_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMOVSSET_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCFGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCR_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCEID0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCEID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCEID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMCEID3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMMIR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]） · `PMDEVAFF0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMDEVAFF1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMLAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMAUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMDEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMPIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]） · `PMCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| C.3.1 | PMEVCNTR0_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159\|p.1159]] |
| C.3.2 | PMEVCNTR1_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1161\|p.1161]] |
| C.3.3 | PMEVCNTR2_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1163\|p.1163]] |
| C.3.4 | PMEVCNTR3_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1165\|p.1165]] |
| C.3.5 | PMEVCNTR4_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1168\|p.1168]] |
| C.3.6 | PMEVCNTR5_EL0, Performance Monitors Event Count Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1170\|p.1170]] |
| C.3.7 | PMCCNTR_EL0, Performance Monitors Cycle Counter | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1172\|p.1172]] |
| C.3.8 | PMPCSR, Program Counter Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1174\|p.1174]] |
| C.3.9 | PMCID1SR, CONTEXTIDR_EL1 Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1178\|p.1178]] |
| C.3.10 | PMVIDSR, VMID Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1180\|p.1180]] |
| C.3.11 | PMCID2SR, CONTEXTIDR_EL2 Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1182\|p.1182]] |
| C.3.12 | PMEVTYPER0_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1183\|p.1183]] |
| C.3.13 | PMEVTYPER1_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1187\|p.1187]] |
| C.3.14 | PMEVTYPER2_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1190\|p.1190]] |
| C.3.15 | PMEVTYPER3_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1194\|p.1194]] |
| C.3.16 | PMEVTYPER4_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1197\|p.1197]] |
| C.3.17 | PMEVTYPER5_EL0, Performance Monitors Event Type Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1201\|p.1201]] |
| C.3.18 | PMCCFILTR_EL0, Performance Monitors Cycle Counter Filter | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1204\|p.1204]] |
| C.3.19 | PMPCSSR, Snapshot Program Counter Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1207\|p.1207]] |
| C.3.20 | PMCIDSSR, Snapshot CONTEXTIDR_EL1 Sample Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1208\|p.1208]] |
| C.3.21 | PMSSSR, PMU Snapshot Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1209\|p.1209]] |
| C.3.22 | PMCCNTSR, PMU Cycle Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1211\|p.1211]] |
| C.3.23 | PMEVCNTSR0, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1212\|p.1212]] |
| C.3.24 | PMEVCNTSR1, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1213\|p.1213]] |
| C.3.25 | PMEVCNTSR2, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1214\|p.1214]] |
| C.3.26 | PMEVCNTSR3, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1215\|p.1215]] |
| C.3.27 | PMEVCNTSR4, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1216\|p.1216]] |
| C.3.28 | PMEVCNTSR5, PMU Event Counter Snapshot Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1217\|p.1217]] |
| C.3.29 | PMSSCR, PMU Snapshot Capture Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1219\|p.1219]] |
| C.3.30 | PMCNTENSET_EL0, Performance Monitors Count Enable Set | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1220\|p.1220]] |
| C.3.31 | PMCNTENCLR_EL0, Performance Monitors Count Enable Clear | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1222\|p.1222]] |
| C.3.32 | PMINTENSET_EL1, Performance Monitors Interrupt Enable Set | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1224\|p.1224]] |
| C.3.33 | PMINTENCLR_EL1, Performance Monitors Interrupt Enable Clear | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1226\|p.1226]] |
| C.3.34 | PMOVSCLR_EL0, Performance Monitors Overflow Flag Status Clear | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1228\|p.1228]] |
| C.3.35 | PMSWINC_EL0, Performance Monitors Software Increment register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1230\|p.1230]] |
| C.3.36 | PMOVSSET_EL0, Performance Monitors Overflow Flag Status Set | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1231\|p.1231]] |
| C.3.37 | PMCFGR, Performance Monitors Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1233\|p.1233]] |
| C.3.38 | PMCR_EL0, Performance Monitors Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1236\|p.1236]] |
| C.3.39 | PMCEID0, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1238\|p.1238]] |
| C.3.40 | PMCEID1, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1242\|p.1242]] |
| C.3.41 | PMCEID2, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1246\|p.1246]] |
| C.3.42 | PMCEID3, Performance Monitors Common Event Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1250\|p.1250]] |
| C.3.43 | PMMIR, Performance Monitors Machine Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1254\|p.1254]] |
| C.3.44 | PMDEVAFF0, Performance Monitors Device Affinity register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1255\|p.1255]] |
| C.3.45 | PMDEVAFF1, Performance Monitors Device Affinity register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1256\|p.1256]] |
| C.3.46 | PMLAR, Performance Monitors Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1258\|p.1258]] |
| C.3.47 | PMLSR, Performance Monitors Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1259\|p.1259]] |
| C.3.48 | PMAUTHSTATUS, Performance Monitors Authentication Status | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1261\|p.1261]] |
| C.3.49 | PMDEVARCH, Performance Monitors Device Architecture register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1262\|p.1262]] |
| C.3.50 | PMDEVID, Performance Monitors Device ID register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1264\|p.1264]] |
| C.3.51 | PMDEVTYPE, Performance Monitors Device Type register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1265\|p.1265]] |
| C.3.52 | PMPIDR4, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1266\|p.1266]] |
| C.3.53 | PMPIDR0, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1268\|p.1268]] |
| C.3.54 | PMPIDR1, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1269\|p.1269]] |
| C.3.55 | PMPIDR2, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1271\|p.1271]] |
| C.3.56 | PMPIDR3, Performance Monitors Peripheral Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1272\|p.1272]] |
| C.3.57 | PMCIDR0, Performance Monitors Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1274\|p.1274]] |
| C.3.58 | PMCIDR1, Performance Monitors Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1275\|p.1275]] |
| C.3.59 | PMCIDR2, Performance Monitors Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1276\|p.1276]] |
| C.3.60 | PMCIDR3, Performance Monitors Component Identification | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1278\|p.1278]] |

## C4 外部CTI寄存器

原分组 C.4，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]；图表回查 [[N2-Core-TRM-附录C原图表#原文第1279页]]。

### 总表寄存器名

`CTICONTROL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIINTACK`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIAPPSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIAPPCLEAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIAPPPULSE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTITRIGINSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTITRIGOUTSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTICHINSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTICHOUTSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIGATE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `ASICCTL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIDEVCTL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIDEVAFF0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]） · `CTIDEVAFF1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTILAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTILSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIAUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIDEVID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIDEVID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]） · `CTIDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| C.4.1 | CTICONTROL, CTI Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280\|p.1280]] |
| C.4.2 | CTIINTACK, CTI Output Trigger Acknowledge register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1281\|p.1281]] |
| C.4.3 | CTIAPPSET, CTI Application Trigger Set register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1283\|p.1283]] |
| C.4.4 | CTIAPPCLEAR, CTI Application Trigger Clear register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1285\|p.1285]] |
| C.4.5 | CTIAPPPULSE, CTI Application Pulse register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1287\|p.1287]] |
| C.4.6 | CTIINEN<n>, CTI Input Trigger to Output Channel Enable registers, n | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1289\|p.1289]] |
| C.4.7 | CTIOUTEN<n>, CTI Input Channel to Output Trigger Enable registers, | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1291\|p.1291]] |
| C.4.8 | CTITRIGINSTATUS, CTI Trigger In Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1292\|p.1292]] |
| C.4.9 | CTITRIGOUTSTATUS, CTI Trigger Out Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1294\|p.1294]] |
| C.4.10 | CTICHINSTATUS, CTI Channel In Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1295\|p.1295]] |
| C.4.11 | CTICHOUTSTATUS, CTI Channel Out Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1297\|p.1297]] |
| C.4.12 | CTIGATE, CTI Channel Gate Enable register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1298\|p.1298]] |
| C.4.13 | ASICCTL, CTI External Multiplexer Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1300\|p.1300]] |
| C.4.14 | CTIDEVCTL, CTI Device Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1301\|p.1301]] |
| C.4.15 | CTIDEVAFF0, CTI Device Affinity register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1303\|p.1303]] |
| C.4.16 | CTIDEVAFF1, CTI Device Affinity register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1304\|p.1304]] |
| C.4.17 | CTILAR, CTI Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1305\|p.1305]] |
| C.4.18 | CTILSR, CTI Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1306\|p.1306]] |
| C.4.19 | CTIAUTHSTATUS, CTI Authentication Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1308\|p.1308]] |
| C.4.20 | CTIDEVARCH, CTI Device Architecture register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1309\|p.1309]] |
| C.4.21 | CTIDEVID2, CTI Device ID register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1311\|p.1311]] |
| C.4.22 | CTIDEVID1, CTI Device ID register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1312\|p.1312]] |
| C.4.23 | CTIDEVID, CTI Device ID register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1313\|p.1313]] |

## C5 外部调试寄存器

原分组 C.5，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]；图表回查 [[N2-Core-TRM-附录C原图表#原文第1315页]]。

### 总表寄存器名

`EDESR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDECR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDWAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGDTRRX_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDITR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDSCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGDTRTX_EL0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDRCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDECCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `OSLAR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDPRCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `EDPRSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGBVR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGBCR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]） · `DBGBVR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBVR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBVR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBVR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR4_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBVR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGBCR5_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWVR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWCR0_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWVR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWCR1_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWVR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWCR2_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWVR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGWCR3_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `MIDR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPFR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDFR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDAA32PFR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDITCTRL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGCLAIMSET_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGCLAIMCLR_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVAFF0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVAFF1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDLAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `DBGAUTHSTATUS_EL1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDDEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]） · `EDPIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDPIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]） · `EDCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| C.5.1 | EDESR, External Debug Event Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317\|p.1317]] |
| C.5.2 | EDECR, External Debug Execution Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1319\|p.1319]] |
| C.5.3 | EDWAR, External Debug Watchpoint Address Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1320\|p.1320]] |
| C.5.4 | DBGDTRRX_EL0, Debug Data Transfer Register, Receive | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1322\|p.1322]] |
| C.5.5 | EDITR, External Debug Instruction Transfer Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1324\|p.1324]] |
| C.5.6 | EDSCR, External Debug Status and Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1326\|p.1326]] |
| C.5.7 | DBGDTRTX_EL0, Debug Data Transfer Register, Transmit | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1333\|p.1333]] |
| C.5.8 | EDRCR, External Debug Reserve Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1335\|p.1335]] |
| C.5.9 | EDECCR, External Debug Exception Catch Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1336\|p.1336]] |
| C.5.10 | OSLAR_EL1, OS Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1342\|p.1342]] |
| C.5.11 | EDPRCR, External Debug Power/Reset Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1343\|p.1343]] |
| C.5.12 | EDPRSR, External Debug Processor Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1346\|p.1346]] |
| C.5.13 | DBGBVR0_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1353\|p.1353]] |
| C.5.14 | DBGBCR0_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1359\|p.1359]] |
| C.5.15 | DBGBVR1_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1363\|p.1363]] |
| C.5.16 | DBGBCR1_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1368\|p.1368]] |
| C.5.17 | DBGBVR2_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1373\|p.1373]] |
| C.5.18 | DBGBCR2_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1378\|p.1378]] |
| C.5.19 | DBGBVR3_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1383\|p.1383]] |
| C.5.20 | DBGBCR3_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1388\|p.1388]] |
| C.5.21 | DBGBVR4_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1393\|p.1393]] |
| C.5.22 | DBGBCR4_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1398\|p.1398]] |
| C.5.23 | DBGBVR5_EL1, Debug Breakpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1403\|p.1403]] |
| C.5.24 | DBGBCR5_EL1, Debug Breakpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1408\|p.1408]] |
| C.5.25 | DBGWVR0_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1413\|p.1413]] |
| C.5.26 | DBGWCR0_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1414\|p.1414]] |
| C.5.27 | DBGWVR1_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1418\|p.1418]] |
| C.5.28 | DBGWCR1_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1420\|p.1420]] |
| C.5.29 | DBGWVR2_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1423\|p.1423]] |
| C.5.30 | DBGWCR2_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1425\|p.1425]] |
| C.5.31 | DBGWVR3_EL1, Debug Watchpoint Value Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1428\|p.1428]] |
| C.5.32 | DBGWCR3_EL1, Debug Watchpoint Control Registers | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1430\|p.1430]] |
| C.5.33 | MIDR_EL1, Main ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1433\|p.1433]] |
| C.5.34 | EDPFR, External Debug Processor Feature Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1435\|p.1435]] |
| C.5.35 | EDDFR, External Debug Feature Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1437\|p.1437]] |
| C.5.36 | EDAA32PFR, External Debug Auxiliary Processor Feature Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1439\|p.1439]] |
| C.5.37 | EDITCTRL, External Debug Integration mode Control register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1441\|p.1441]] |
| C.5.38 | DBGCLAIMSET_EL1, Debug CLAIM Tag Set register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1442\|p.1442]] |
| C.5.39 | DBGCLAIMCLR_EL1, Debug CLAIM Tag Clear register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1444\|p.1444]] |
| C.5.40 | EDDEVAFF0, External Debug Device Affinity register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1446\|p.1446]] |
| C.5.41 | EDDEVAFF1, External Debug Device Affinity register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1447\|p.1447]] |
| C.5.42 | EDLAR, External Debug Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1448\|p.1448]] |
| C.5.43 | EDLSR, External Debug Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1449\|p.1449]] |
| C.5.44 | DBGAUTHSTATUS_EL1, Debug Authentication Status register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1451\|p.1451]] |
| C.5.45 | EDDEVARCH, External Debug Device Architecture register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1453\|p.1453]] |
| C.5.46 | EDDEVID2, External Debug Device ID register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1454\|p.1454]] |
| C.5.47 | EDDEVID1, External Debug Device ID register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1456\|p.1456]] |
| C.5.48 | EDDEVID, External Debug Device ID register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1457\|p.1457]] |
| C.5.49 | EDDEVTYPE, External Debug Device Type register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1458\|p.1458]] |
| C.5.50 | EDPIDR4, External Debug Peripheral Identification Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1460\|p.1460]] |
| C.5.51 | EDPIDR0, External Debug Peripheral Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1461\|p.1461]] |
| C.5.52 | EDPIDR1, External Debug Peripheral Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1462\|p.1462]] |
| C.5.53 | EDPIDR2, External Debug Peripheral Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1464\|p.1464]] |
| C.5.54 | EDPIDR3, External Debug Peripheral Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1465\|p.1465]] |
| C.5.55 | EDCIDR0, External Debug Component Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1467\|p.1467]] |
| C.5.56 | EDCIDR1, External Debug Component Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1468\|p.1468]] |
| C.5.57 | EDCIDR2, External Debug Component Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1469\|p.1469]] |
| C.5.58 | EDCIDR3, External Debug Component Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1471\|p.1471]] |

## C6 外部AMU寄存器

原分组 C.6，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]；图表回查 [[N2-Core-TRM-附录C原图表#原文第1472页]]。

### 总表寄存器名

`AMEVCNTR00`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR01`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR02`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR03`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVCNTR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVTYPER00`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVTYPER01`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]） · `AMEVTYPER02`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMEVTYPER03`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMEVTYPER10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMEVTYPER11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMEVTYPER12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCNTENSET0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCNTENSET1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCNTENCLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCNTENCLR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCGCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCFGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMIIDR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMDEVAFF0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMDEVAFF1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMDEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMPIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]） · `AMCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| C.6.1 | AMEVCNTR00, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473\|p.1473]] |
| C.6.2 | AMEVCNTR01, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1475\|p.1475]] |
| C.6.3 | AMEVCNTR02, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1477\|p.1477]] |
| C.6.4 | AMEVCNTR03, Activity Monitors Event Counter Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1479\|p.1479]] |
| C.6.5 | AMEVCNTR10, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1480\|p.1480]] |
| C.6.6 | AMEVCNTR11, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1482\|p.1482]] |
| C.6.7 | AMEVCNTR12, Activity Monitors Event Counter Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1484\|p.1484]] |
| C.6.8 | AMEVTYPER00, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1486\|p.1486]] |
| C.6.9 | AMEVTYPER01, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1487\|p.1487]] |
| C.6.10 | AMEVTYPER02, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1489\|p.1489]] |
| C.6.11 | AMEVTYPER03, Activity Monitors Event Type Registers 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1491\|p.1491]] |
| C.6.12 | AMEVTYPER10, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1493\|p.1493]] |
| C.6.13 | AMEVTYPER11, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1494\|p.1494]] |
| C.6.14 | AMEVTYPER12, Activity Monitors Event Type Registers 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1496\|p.1496]] |
| C.6.15 | AMCNTENSET0, Activity Monitors Count Enable Set Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1498\|p.1498]] |
| C.6.16 | AMCNTENSET1, Activity Monitors Count Enable Set Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1499\|p.1499]] |
| C.6.17 | AMCNTENCLR0, Activity Monitors Count Enable Clear Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1501\|p.1501]] |
| C.6.18 | AMCNTENCLR1, Activity Monitors Count Enable Clear Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1502\|p.1502]] |
| C.6.19 | AMCGCR, Activity Monitors Counter Group Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1504\|p.1504]] |
| C.6.20 | AMCFGR, Activity Monitors Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1505\|p.1505]] |
| C.6.21 | AMCR, Activity Monitors Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1507\|p.1507]] |
| C.6.22 | AMIIDR, Activity Monitors Implementation Identification Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1508\|p.1508]] |
| C.6.23 | AMDEVAFF0, Activity Monitors Device Affinity Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1510\|p.1510]] |
| C.6.24 | AMDEVAFF1, Activity Monitors Device Affinity Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1511\|p.1511]] |
| C.6.25 | AMDEVARCH, Activity Monitors Device Architecture Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1512\|p.1512]] |
| C.6.26 | AMDEVTYPE, Activity Monitors Device Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1514\|p.1514]] |
| C.6.27 | AMPIDR4, Activity Monitors Peripheral Identification Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1515\|p.1515]] |
| C.6.28 | AMPIDR0, Activity Monitors Peripheral Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1516\|p.1516]] |
| C.6.29 | AMPIDR1, Activity Monitors Peripheral Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1517\|p.1517]] |
| C.6.30 | AMPIDR2, Activity Monitors Peripheral Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1519\|p.1519]] |
| C.6.31 | AMPIDR3, Activity Monitors Peripheral Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1520\|p.1520]] |
| C.6.32 | AMCIDR0, Activity Monitors Component Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1521\|p.1521]] |
| C.6.33 | AMCIDR1, Activity Monitors Component Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1523\|p.1523]] |
| C.6.34 | AMCIDR2, Activity Monitors Component Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1524\|p.1524]] |
| C.6.35 | AMCIDR3, Activity Monitors Component Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1525\|p.1525]] |

## C7 外部ETE寄存器

原分组 C.7，总表入口 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526|p.1526]]；图表回查 [[N2-Core-TRM-附录C原图表#原文第1526页]]。

### 总表寄存器名

`TRCPRGCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526|p.1526]]） · `TRCSTATR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526|p.1526]]） · `TRCCONFIGR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526|p.1526]]） · `TRCAUXCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEVENTCTL0R`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEVENTCTL1R`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCRSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCTSCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSYNCPR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCCCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCBBCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCTRACEIDR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCVICTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCVIIECTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCVISSCTLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQEVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQEVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQEVR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQRSTEVR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCSEQSTR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEXTINSELR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEXTINSELR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEXTINSELR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCEXTINSELR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTRLDVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTRLDVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTCTLR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTVR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCCNTVR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR8`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR9`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR10`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR11`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR12`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR13`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIMSPEC0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]） · `TRCIDR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCIDR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCOSLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPDCR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPDSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDCCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCVMIDCCTLR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCITCTRL`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCLAIMSET`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCLAIMCLR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVAFF`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCLAR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCLSR`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCAUTHSTATUS`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVARCH`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVID2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVID1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVID`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCDEVTYPE`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR4`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR5`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR6`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR7`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCPIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDR0`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDR1`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDR2`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]） · `TRCCIDR3`（[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]）

### 展开说明条目

| 原章节 | 寄存器/原文标题 | 起始原页 |
|---|---|---|
| C.7.1 | TRCPRGCTLR, Programming Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528\|p.1528]] |
| C.7.2 | TRCSTATR, Trace Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1530\|p.1530]] |
| C.7.3 | TRCCONFIGR, Trace Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1531\|p.1531]] |
| C.7.4 | TRCAUXCTLR, Auxiliary Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1534\|p.1534]] |
| C.7.5 | TRCEVENTCTL0R, Event Control 0 Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1535\|p.1535]] |
| C.7.6 | TRCEVENTCTL1R, Event Control 1 Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1538\|p.1538]] |
| C.7.7 | TRCRSR, Resources Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1541\|p.1541]] |
| C.7.8 | TRCTSCTLR, Timestamp Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1543\|p.1543]] |
| C.7.9 | TRCSYNCPR, Synchronization Period Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1545\|p.1545]] |
| C.7.10 | TRCCCCTLR, Cycle Count Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1547\|p.1547]] |
| C.7.11 | TRCBBCTLR, Branch Broadcast Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1548\|p.1548]] |
| C.7.12 | TRCTRACEIDR, Trace ID Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1550\|p.1550]] |
| C.7.13 | TRCVICTLR, ViewInst Main Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1552\|p.1552]] |
| C.7.14 | TRCVIIECTLR, ViewInst Include/Exclude Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1555\|p.1555]] |
| C.7.15 | TRCVISSCTLR, ViewInst Start/Stop Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1557\|p.1557]] |
| C.7.16 | TRCSEQEVR0, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1560\|p.1560]] |
| C.7.17 | TRCSEQEVR1, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1562\|p.1562]] |
| C.7.18 | TRCSEQEVR2, Sequencer State Transition Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1565\|p.1565]] |
| C.7.19 | TRCSEQRSTEVR, Sequencer Reset Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1568\|p.1568]] |
| C.7.20 | TRCSEQSTR, Sequencer State Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1570\|p.1570]] |
| C.7.21 | TRCEXTINSELR0, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1571\|p.1571]] |
| C.7.22 | TRCEXTINSELR1, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1574\|p.1574]] |
| C.7.23 | TRCEXTINSELR2, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1576\|p.1576]] |
| C.7.24 | TRCEXTINSELR3, External Input Select Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1578\|p.1578]] |
| C.7.25 | TRCCNTRLDVR0, Counter Reload Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1580\|p.1580]] |
| C.7.26 | TRCCNTRLDVR1, Counter Reload Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1581\|p.1581]] |
| C.7.27 | TRCCNTCTLR0, Counter Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1582\|p.1582]] |
| C.7.28 | TRCCNTCTLR1, Counter Control Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1585\|p.1585]] |
| C.7.29 | TRCCNTVR0, Counter Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1588\|p.1588]] |
| C.7.30 | TRCCNTVR1, Counter Value Register <n> | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1590\|p.1590]] |
| C.7.31 | TRCIDR8, ID Register 8 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1591\|p.1591]] |
| C.7.32 | TRCIDR9, ID Register 9 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1592\|p.1592]] |
| C.7.33 | TRCIDR10, ID Register 10 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1594\|p.1594]] |
| C.7.34 | TRCIDR11, ID Register 11 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1595\|p.1595]] |
| C.7.35 | TRCIDR12, ID Register 12 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1596\|p.1596]] |
| C.7.36 | TRCIDR13, ID Register 13 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1597\|p.1597]] |
| C.7.37 | TRCIMSPEC0, IMP DEF Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1598\|p.1598]] |
| C.7.38 | TRCIDR0, ID Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1599\|p.1599]] |
| C.7.39 | TRCIDR1, ID Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1602\|p.1602]] |
| C.7.40 | TRCIDR2, ID Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1603\|p.1603]] |
| C.7.41 | TRCIDR3, ID Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1605\|p.1605]] |
| C.7.42 | TRCIDR4, ID Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1607\|p.1607]] |
| C.7.43 | TRCIDR5, ID Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1609\|p.1609]] |
| C.7.44 | TRCIDR6, ID Register 6 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1611\|p.1611]] |
| C.7.45 | TRCIDR7, ID Register 7 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1612\|p.1612]] |
| C.7.46 | TRCSSCSR<n>, Single-shot Comparator Control Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1613\|p.1613]] |
| C.7.47 | TRCOSLSR, Trace OS Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1616\|p.1616]] |
| C.7.48 | TRCPDCR, PowerDown Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1617\|p.1617]] |
| C.7.49 | TRCPDSR, PowerDown Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1619\|p.1619]] |
| C.7.50 | TRCCIDCCTLR0, Context Identifier Comparator Control Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1620\|p.1620]] |
| C.7.51 | TRCVMIDCCTLR0, Virtual Context Identifier Comparator Control | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1622\|p.1622]] |
| C.7.52 | TRCITCTRL, Integration Mode Control Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1624\|p.1624]] |
| C.7.53 | TRCCLAIMSET, Claim Tag Set Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1626\|p.1626]] |
| C.7.54 | TRCCLAIMCLR, Claim Tag Clear Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1628\|p.1628]] |
| C.7.55 | TRCDEVAFF, Device Affinity Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1629\|p.1629]] |
| C.7.56 | TRCLAR, Lock Access Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1630\|p.1630]] |
| C.7.57 | TRCLSR, Lock Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1632\|p.1632]] |
| C.7.58 | TRCAUTHSTATUS, Authentication Status Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1633\|p.1633]] |
| C.7.59 | TRCDEVARCH, Device Architecture Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1637\|p.1637]] |
| C.7.60 | TRCDEVID2, Device Configuration Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1638\|p.1638]] |
| C.7.61 | TRCDEVID1, Device Configuration Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1640\|p.1640]] |
| C.7.62 | TRCDEVID, Device Configuration Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1641\|p.1641]] |
| C.7.63 | TRCDEVTYPE, Device Type Register | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1642\|p.1642]] |
| C.7.64 | TRCPIDR4, Peripheral Identification Register 4 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1643\|p.1643]] |
| C.7.65 | TRCPIDR5, Peripheral Identification Register 5 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1645\|p.1645]] |
| C.7.66 | TRCPIDR6, Peripheral Identification Register 6 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1647\|p.1647]] |
| C.7.67 | TRCPIDR7, Peripheral Identification Register 7 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1648\|p.1648]] |
| C.7.68 | TRCPIDR0, Peripheral Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1649\|p.1649]] |
| C.7.69 | TRCPIDR1, Peripheral Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1650\|p.1650]] |
| C.7.70 | TRCPIDR2, Peripheral Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1652\|p.1652]] |
| C.7.71 | TRCPIDR3, Peripheral Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1653\|p.1653]] |
| C.7.72 | TRCCIDR0, Component Identification Register 0 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1655\|p.1655]] |
| C.7.73 | TRCCIDR1, Component Identification Register 1 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1656\|p.1656]] |
| C.7.74 | TRCCIDR2, Component Identification Register 2 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1658\|p.1658]] |
| C.7.75 | TRCCIDR3, Component Identification Register 3 | [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1659\|p.1659]] |
