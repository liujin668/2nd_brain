---
type: reference
status: reviewed
topics: [Neoverse, N2, CPU, architecture]
aliases: ["N2 正文原图表"]
tags: [arm, neoverse, cpu, reference]
sources: ["[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]"]
source_document: "102099_0003_06_en"
source_revision: "r0p3 / Issue 06"
source_date: 2022-10-27
spec_issue: "CHI E"
source_sections: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
evidence: source-derived
verification: source-text-and-figure-index-checked
created: 2026-10-09
updated: 2026-10-10
---

# N2 Core TRM 正文原图表

原文范围 p.26-159。本册收录 92 页截图，覆盖该范围的 119 个编号图表标题，以及跨页续表。

入口：[[N2-Core-TRM-完整中文精读]] · [[N2-Core-TRM-寄存器索引]] · [[Neoverse-MOC]]。

> [!info] 使用方式
> 原页保留完整正文宽度、图表、注释及水印，裁去页眉和页脚空白。图表标题保留英文以便和原文对照；续页若没有新标题，会注明“续表或相关原文”。
> 不含图表的普通说明页请用 PDF 页码链接回查。截图不替代正文中的配置、访问条件和编程步骤。

## 编号图表索引

| 编号与原文标题 | 原页 |
|---|---|
| Figure 1-1: Key to timing diagram conventions | [[#原文第28页\|28]] |
| Figure 2-1: Neoverse™ N2 example configuration | [[#原文第30页\|30]] |
| Table 2-1: Neoverse™ N2 core features that have a dependency on the DSU-110 | [[#原文第32页\|32]] |
| Table 2-2: Armv8.0-A optional feature support in the Neoverse™ N2 core | [[#原文第33页\|33]] |
| Table 2-3: Arm®v8.1-A optional feature support in the Neoverse™ N2 core | [[#原文第33页\|33]] |
| Table 2-4: Arm®v8.2-A optional feature support in the Neoverse™ N2 core | [[#原文第33页\|33]] |
| Table 2-5: Arm®v8.3-A optional feature support in the Neoverse™ N2 core | [[#原文第34页\|34]] |
| Table 2-6: Arm®v8.4-A optional feature support in the Neoverse™ N2 core | [[#原文第35页\|35]] |
| Table 2-7: Arm®v8.5-A optional feature support in the Neoverse™ N2 core | [[#原文第35页\|35]] |
| Table 2-8: Arm®v9.0-A feature support in the Neoverse™ N2 core | [[#原文第35页\|35]] |
| Table 2-9: Other standards and specifications support in the Neoverse™ N2 core | [[#原文第35页\|35]] |
| Table 2-10: Product revisions | [[#原文第38页\|38]] |
| Figure 3-1: Neoverse™ N2 core components | [[#原文第40页\|40]] |
| Figure 5-1: Neoverse™ N2 voltage and power domains | [[#原文第46页\|46]] |
| Figure 5-2: Core power domains in a cluster with one Neoverse™ N2 core | [[#原文第47页\|47]] |
| Table 5-1: Neoverse™ N2 core power modes | [[#原文第50页\|50]] |
| Figure 5-3: Neoverse™ N2 core power mode transitions | [[#原文第51页\|51]] |
| Table 6-1: MMU components | [[#原文第58页\|58]] |
| Figure 6-1: Translation table walks | [[#原文第61页\|61]] |
| Table 6-2: Supported device memory types | [[#原文第63页\|63]] |
| Table 6-3: Shareability for Normal memory | [[#原文第63页\|63]] |
| Table 7-1: L1 instruction memory system features | [[#原文第65页\|65]] |
| Table 8-1: L1 data memory system features | [[#原文第69页\|69]] |
| Table 9-1: L2 memory system features | [[#原文第74页\|74]] |
| Table 9-2: Neoverse™ N2 transaction capabilities | [[#原文第75页\|75]] |
| Table 10-1: System registers used to access internal memory | [[#原文第76页\|76]] |
| Table 10-2: Neoverse™ N2 L1 instruction cache tag location encoding | [[#原文第76页\|76]] |
| Table 10-3: Neoverse™ N2 L1 instruction cache data location encoding | [[#原文第77页\|77]] |
| Table 10-4: Neoverse™ N2 L1 BTB data location encoding | [[#原文第77页\|77]] |
| Table 10-5: Neoverse™ N2 L1 GHB data location encoding | [[#原文第77页\|77]] |
| Table 10-6: Neoverse™ N2 L1 instruction TLB data location encoding | [[#原文第77页\|77]] |
| Table 10-7: Neoverse™ N2 BIM data location encoding | [[#原文第77页\|77]] |
| Table 10-8: Neoverse™ N2 L0 Macro-operation cache data location encoding | [[#原文第78页\|78]] |
| Table 10-9: Neoverse™ N2 L1 data cache tag location encoding | [[#原文第78页\|78]] |
| Table 10-10: Neoverse™ N2 L1 data cache data location encoding | [[#原文第78页\|78]] |
| Table 10-11: Neoverse™ N2 L1 data TLB location encoding | [[#原文第78页\|78]] |
| Table 10-12: L1 instruction cache tag format for Instruction Register 0 | [[#原文第79页\|79]] |
| Table 10-13: L1 instruction cache tag format for Instruction Register 1 | [[#原文第79页\|79]] |
| Table 10-14: L1 instruction cache tag format for Instruction Register 2 | [[#原文第79页\|79]] |
| Table 10-15: L1 instruction cache data format for Instruction Register 0 | [[#原文第79页\|79]] |
| Table 10-16: L1 instruction cache data format for Instruction Register 1 | [[#原文第79页\|79]] |
| Table 10-17: L1 instruction cache data format for Instruction Register 2 | [[#原文第80页\|80]] |
| Table 10-18: L1 BTB cache format for Instruction Register 0 | [[#原文第80页\|80]] |
| Table 10-19: L1 BTB cache format for Instruction Register 1 | [[#原文第80页\|80]] |
| Table 10-20: L1 BTB cache format for Instruction Register 2 | [[#原文第80页\|80]] |
| Table 10-21: L1 GHB cache format for Instruction Register 0 | [[#原文第80页\|80]] |
| Table 10-22: L1 GHB cache format for Instruction Register 1 | [[#原文第80页\|80]] |
| Table 10-23: L1 GHB cache format for Instruction Register 2 | [[#原文第80页\|80]] |
| Table 10-24: L1 BIM cache format for Instruction Register 0 | [[#原文第81页\|81]] |
| Table 10-25: L1 BIM cache format for Instruction Register 1 | [[#原文第81页\|81]] |
| Table 10-26: L1 BIM cache format for Instruction Register 2 | [[#原文第81页\|81]] |
| Table 10-27: L1 instruction TLB format for Instruction Register 0 | [[#原文第81页\|81]] |
| Table 10-28: L1 instruction TLB format for Instruction Register 1 | [[#原文第83页\|83]] |
| Table 10-29: L1 instruction TLB format for Instruction Register 2 | [[#原文第83页\|83]] |
| Table 10-30: L0 MOP cache format for Instruction Register 0 | [[#原文第83页\|83]] |
| Table 10-31: L0 MOP cache format for Instruction Register 1 | [[#原文第83页\|83]] |
| Table 10-32: L0 MOP cache format for Instruction Register 2 | [[#原文第84页\|84]] |
| Table 10-33: L1 data cache tag format for Data Register 0 | [[#原文第84页\|84]] |
| Table 10-34: L1 data cache tag format for Data Register 1 | [[#原文第84页\|84]] |
| Table 10-35: L1 data cache tag format for Data Register 2 | [[#原文第85页\|85]] |
| Table 10-36: L1 data cache data format for Data Register 0 | [[#原文第85页\|85]] |
| Table 10-37: L1 data cache data format for Data Register 1 | [[#原文第85页\|85]] |
| Table 10-38: L1 data cache data format for Data Register 2 | [[#原文第85页\|85]] |
| Table 10-39: L1 data TLB format for Data Register 0 | [[#原文第85页\|85]] |
| Table 10-40: L1 data TLB format for Data Register 1 | [[#原文第87页\|87]] |
| Table 10-41: L1 data TLB format for Data Register 2 | [[#原文第87页\|87]] |
| Table 10-42: Neoverse™ N2 L2 cache tag location encoding for 512KB | [[#原文第87页\|87]] |
| Table 10-43: Neoverse™ N2 L2 cache tag location encoding for 1MB | [[#原文第88页\|88]] |
| Table 10-44: Neoverse™ N2 L2 cache data location encoding for 512KB | [[#原文第88页\|88]] |
| Table 10-45: Neoverse™ N2 L2 cache data location encoding for 1MB | [[#原文第88页\|88]] |
| Table 10-46: Neoverse™ N2 L2 TLB location encoding | [[#原文第89页\|89]] |
| Table 10-47: Neoverse™ N2 L2 victim location encoding | [[#原文第89页\|89]] |
| Table 10-48: L2 tag cache format for Data Register 0 | [[#原文第89页\|89]] |
| Table 10-49: L2 tag cache format for Data Register 1 | [[#原文第90页\|90]] |
| Table 10-50: L2 tag cache format for Data Register 2 | [[#原文第90页\|90]] |
| Table 10-51: L2 tag cache format for Data Register 0 | [[#原文第90页\|90]] |
| Table 10-52: L2 tag cache format for Data Register 1 | [[#原文第91页\|91]] |
| Table 10-53: L2 tag cache format for Data Register 2 | [[#原文第91页\|91]] |
| Table 10-54: L2 data RAM format for Data Register 0 | [[#原文第92页\|92]] |
| Table 10-55: L2 data RAM format for Data Register 1 | [[#原文第92页\|92]] |
| Table 10-56: L2 data RAM format for Data Register 2 | [[#原文第92页\|92]] |
| Table 10-57: L2 TLB format for Instruction Register 0 | [[#原文第92页\|92]] |
| Table 10-58: L2 TLB format for Instruction Register 1 | [[#原文第93页\|93]] |
| Table 10-59: L2 TLB format for Instruction Register 2 | [[#原文第94页\|94]] |
| Table 10-60: Neoverse™ N2 L2 victim format for data register 0 | [[#原文第95页\|95]] |
| Table 10-61: Neoverse™ N2 L2 victim format for data register 1 | [[#原文第95页\|95]] |
| Table 10-62: Neoverse™ N2 L2 victim format for data register 2 | [[#原文第95页\|95]] |
| Table 11-1: RAM cache protection | [[#原文第97页\|97]] |
| Table 11-2: RAS registers summary | [[#原文第100页\|100]] |
| Table 12-1: GIC system registers summary | [[#原文第102页\|102]] |
| Table 15-1: Identification registers summary | [[#原文第107页\|107]] |
| Table 16-1: Random Number Control registers summary | [[#原文第110页\|110]] |
| Figure 17-1: DynamIQ™ cluster debug components | [[#原文第111页\|111]] |
| Figure 17-2: External debug system | [[#原文第112页\|112]] |
| Table 17-1: External access conditions to registers | [[#原文第115页\|115]] |
| Table 17-2: Core ROM table | [[#原文第116页\|116]] |
| Table 17-3: Neoverse™ N2 CoreSight component identification | [[#原文第116页\|116]] |
| Table 17-4: Core CTI register peripheral ID values | [[#原文第117页\|117]] |
| Table 17-5: Debug registers summary | [[#原文第117页\|117]] |
| Table 17-6: Debug registers summary | [[#原文第119页\|119]] |
| Table 17-7: CoreROM registers summary | [[#原文第121页\|121]] |
| Table 18-1: Performance monitors Events | [[#原文第122页\|122]] |
| Table 18-2: Performance Monitors registers summary | [[#原文第133页\|133]] |
| Table 18-3: Performance Monitors registers summary | [[#原文第134页\|134]] |
| Figure 19-1: Trace unit components | [[#原文第137页\|137]] |
| Table 19-1: Trace unit resources | [[#原文第138页\|138]] |
| Table 19-2: Trace unit generation options | [[#原文第139页\|139]] |
| Figure 19-2: Programming trace unit registers using the Debug APB interface | [[#原文第141页\|141]] |
| Figure 19-3: Programming trace registers using the System register interface | [[#原文第142页\|142]] |
| Table 19-3: ETE events | [[#原文第143页\|143]] |
| Table 19-4: Trace unit registers summary | [[#原文第143页\|143]] |
| Table 19-5: Trace unit registers summary | [[#原文第147页\|147]] |
| Table 21-1: Mapping of counters to fixed events | [[#原文第152页\|152]] |
| Table 21-2: Activity Monitors registers summary | [[#原文第153页\|153]] |
| Table 21-3: Activity Monitors registers summary | [[#原文第154页\|154]] |
| Figure 22-1: SPE behavior | [[#原文第156页\|156]] |
| Table 22-1: SPE events packet | [[#原文第157页\|157]] |
| Table 22-2: SPE data source packet | [[#原文第158页\|158]] |
| Table 22-3: Statistical Profiling Extension registers summary | [[#原文第158页\|158]] |

## 第1章 原图表

原文 p.26-29：引言。

### 原文第28页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=28|p.28]]

- Figure 1-1: Key to timing diagram conventions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0028-original.png]]

## 第2章 原图表

原文 p.30-38：N2核。

### 原文第30页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=30|p.30]]

- Figure 2-1: Neoverse™ N2 example configuration

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0030-original.png]]

### 原文第32页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=32|p.32]]

- Table 2-1: Neoverse™ N2 core features that have a dependency on the DSU-110

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0032-original.png]]

### 原文第33页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=33|p.33]]

- Table 2-2: Armv8.0-A optional feature support in the Neoverse™ N2 core
- Table 2-3: Arm®v8.1-A optional feature support in the Neoverse™ N2 core
- Table 2-4: Arm®v8.2-A optional feature support in the Neoverse™ N2 core

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0033-original.png]]

### 原文第34页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=34|p.34]]

- Table 2-5: Arm®v8.3-A optional feature support in the Neoverse™ N2 core

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0034-original.png]]

### 原文第35页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=35|p.35]]

- Table 2-6: Arm®v8.4-A optional feature support in the Neoverse™ N2 core
- Table 2-7: Arm®v8.5-A optional feature support in the Neoverse™ N2 core
- Table 2-8: Arm®v9.0-A feature support in the Neoverse™ N2 core
- Table 2-9: Other standards and specifications support in the Neoverse™ N2 core

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0035-original.png]]

### 原文第36页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=36|p.36]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0036-original.png]]

### 原文第38页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=38|p.38]]

- Table 2-10: Product revisions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0038-original.png]]

## 第3章 原图表

原文 p.39-44：技术总览。

### 原文第40页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=40|p.40]]

- Figure 3-1: Neoverse™ N2 core components

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0040-original.png]]

## 第4章 原图表

原文 p.45-45：时钟与复位。

本章无编号图表；正文请回查 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=45|p.45]]。

## 第5章 原图表

原文 p.46-56：电源管理。

### 原文第46页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=46|p.46]]

- Figure 5-1: Neoverse™ N2 voltage and power domains

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0046-original.png]]

### 原文第47页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=47|p.47]]

- Figure 5-2: Core power domains in a cluster with one Neoverse™ N2 core

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0047-original.png]]

### 原文第50页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=50|p.50]]

- Table 5-1: Neoverse™ N2 core power modes

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0050-original.png]]

### 原文第51页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=51|p.51]]

- Figure 5-3: Neoverse™ N2 core power mode transitions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0051-original.png]]

## 第6章 原图表

原文 p.57-64：内存管理。

### 原文第58页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=58|p.58]]

- Table 6-1: MMU components

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0058-original.png]]

### 原文第61页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=61|p.61]]

- Figure 6-1: Translation table walks

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0061-original.png]]

### 原文第63页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=63|p.63]]

- Table 6-2: Supported device memory types
- Table 6-3: Shareability for Normal memory

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0063-original.png]]

## 第7章 原图表

原文 p.65-68：L1指令存储。

### 原文第65页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=65|p.65]]

- Table 7-1: L1 instruction memory system features

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0065-original.png]]

## 第8章 原图表

原文 p.69-73：L1数据存储。

### 原文第69页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=69|p.69]]

- Table 8-1: L1 data memory system features

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0069-original.png]]

## 第9章 原图表

原文 p.74-75：L2存储。

### 原文第74页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=74|p.74]]

- Table 9-1: L2 memory system features

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0074-original.png]]

### 原文第75页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=75|p.75]]

- Table 9-2: Neoverse™ N2 transaction capabilities

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0075-original.png]]

## 第10章 原图表

原文 p.76-95：内部RAM访问。

### 原文第76页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=76|p.76]]

- Table 10-1: System registers used to access internal memory
- Table 10-2: Neoverse™ N2 L1 instruction cache tag location encoding

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0076-original.png]]

### 原文第77页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=77|p.77]]

- Table 10-3: Neoverse™ N2 L1 instruction cache data location encoding
- Table 10-4: Neoverse™ N2 L1 BTB data location encoding
- Table 10-5: Neoverse™ N2 L1 GHB data location encoding
- Table 10-6: Neoverse™ N2 L1 instruction TLB data location encoding
- Table 10-7: Neoverse™ N2 BIM data location encoding

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0077-original.png]]

### 原文第78页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=78|p.78]]

- Table 10-8: Neoverse™ N2 L0 Macro-operation cache data location encoding
- Table 10-9: Neoverse™ N2 L1 data cache tag location encoding
- Table 10-10: Neoverse™ N2 L1 data cache data location encoding
- Table 10-11: Neoverse™ N2 L1 data TLB location encoding

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0078-original.png]]

### 原文第79页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=79|p.79]]

- Table 10-12: L1 instruction cache tag format for Instruction Register 0
- Table 10-13: L1 instruction cache tag format for Instruction Register 1
- Table 10-14: L1 instruction cache tag format for Instruction Register 2
- Table 10-15: L1 instruction cache data format for Instruction Register 0
- Table 10-16: L1 instruction cache data format for Instruction Register 1

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0079-original.png]]

### 原文第80页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=80|p.80]]

- Table 10-17: L1 instruction cache data format for Instruction Register 2
- Table 10-18: L1 BTB cache format for Instruction Register 0
- Table 10-19: L1 BTB cache format for Instruction Register 1
- Table 10-20: L1 BTB cache format for Instruction Register 2
- Table 10-21: L1 GHB cache format for Instruction Register 0
- Table 10-22: L1 GHB cache format for Instruction Register 1
- Table 10-23: L1 GHB cache format for Instruction Register 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0080-original.png]]

### 原文第81页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=81|p.81]]

- Table 10-24: L1 BIM cache format for Instruction Register 0
- Table 10-25: L1 BIM cache format for Instruction Register 1
- Table 10-26: L1 BIM cache format for Instruction Register 2
- Table 10-27: L1 instruction TLB format for Instruction Register 0

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0081-original.png]]

### 原文第82页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=82|p.82]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0082-original.png]]

### 原文第83页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=83|p.83]]

- Table 10-28: L1 instruction TLB format for Instruction Register 1
- Table 10-29: L1 instruction TLB format for Instruction Register 2
- Table 10-30: L0 MOP cache format for Instruction Register 0
- Table 10-31: L0 MOP cache format for Instruction Register 1

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0083-original.png]]

### 原文第84页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=84|p.84]]

- Table 10-32: L0 MOP cache format for Instruction Register 2
- Table 10-33: L1 data cache tag format for Data Register 0
- Table 10-34: L1 data cache tag format for Data Register 1

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0084-original.png]]

### 原文第85页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=85|p.85]]

- Table 10-35: L1 data cache tag format for Data Register 2
- Table 10-36: L1 data cache data format for Data Register 0
- Table 10-37: L1 data cache data format for Data Register 1
- Table 10-38: L1 data cache data format for Data Register 2
- Table 10-39: L1 data TLB format for Data Register 0

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0085-original.png]]

### 原文第86页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=86|p.86]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0086-original.png]]

### 原文第87页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=87|p.87]]

- Table 10-40: L1 data TLB format for Data Register 1
- Table 10-41: L1 data TLB format for Data Register 2
- Table 10-42: Neoverse™ N2 L2 cache tag location encoding for 512KB

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0087-original.png]]

### 原文第88页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=88|p.88]]

- Table 10-43: Neoverse™ N2 L2 cache tag location encoding for 1MB
- Table 10-44: Neoverse™ N2 L2 cache data location encoding for 512KB
- Table 10-45: Neoverse™ N2 L2 cache data location encoding for 1MB

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0088-original.png]]

### 原文第89页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=89|p.89]]

- Table 10-46: Neoverse™ N2 L2 TLB location encoding
- Table 10-47: Neoverse™ N2 L2 victim location encoding
- Table 10-48: L2 tag cache format for Data Register 0

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0089-original.png]]

### 原文第90页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=90|p.90]]

- Table 10-49: L2 tag cache format for Data Register 1
- Table 10-50: L2 tag cache format for Data Register 2
- Table 10-51: L2 tag cache format for Data Register 0

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0090-original.png]]

### 原文第91页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=91|p.91]]

- Table 10-52: L2 tag cache format for Data Register 1
- Table 10-53: L2 tag cache format for Data Register 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0091-original.png]]

### 原文第92页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=92|p.92]]

- Table 10-54: L2 data RAM format for Data Register 0
- Table 10-55: L2 data RAM format for Data Register 1
- Table 10-56: L2 data RAM format for Data Register 2
- Table 10-57: L2 TLB format for Instruction Register 0

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0092-original.png]]

### 原文第93页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=93|p.93]]

- Table 10-58: L2 TLB format for Instruction Register 1

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0093-original.png]]

### 原文第94页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=94|p.94]]

- Table 10-59: L2 TLB format for Instruction Register 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0094-original.png]]

### 原文第95页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=95|p.95]]

- Table 10-60: Neoverse™ N2 L2 victim format for data register 0
- Table 10-61: Neoverse™ N2 L2 victim format for data register 1
- Table 10-62: Neoverse™ N2 L2 victim format for data register 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0095-original.png]]

## 第11章 原图表

原文 p.96-100：RAS。

### 原文第97页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=97|p.97]]

- Table 11-1: RAM cache protection

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0097-original.png]]

### 原文第100页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=100|p.100]]

- Table 11-2: RAS registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0100-original.png]]

## 第12章 原图表

原文 p.101-104：GIC。

### 原文第102页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=102|p.102]]

- Table 12-1: GIC system registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0102-original.png]]

### 原文第103页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=103|p.103]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0103-original.png]]

### 原文第104页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=104|p.104]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0104-original.png]]

## 第13章 原图表

原文 p.105-105：SIMD与浮点。

本章无编号图表；正文请回查 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=105|p.105]]。

## 第14章 原图表

原文 p.106-106：SVE。

本章无编号图表；正文请回查 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=106|p.106]]。

## 第15章 原图表

原文 p.107-108：系统控制。

### 原文第107页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=107|p.107]]

- Table 15-1: Identification registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0107-original.png]]

### 原文第108页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=108|p.108]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0108-original.png]]

## 第16章 原图表

原文 p.109-110：RNG。

### 原文第110页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=110|p.110]]

- Table 16-1: Random Number Control registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0110-original.png]]

## 第17章 原图表

原文 p.111-121：调试。

### 原文第111页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=111|p.111]]

- Figure 17-1: DynamIQ™ cluster debug components

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0111-original.png]]

### 原文第112页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=112|p.112]]

- Figure 17-2: External debug system

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0112-original.png]]

### 原文第115页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=115|p.115]]

- Table 17-1: External access conditions to registers

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0115-original.png]]

### 原文第116页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=116|p.116]]

- Table 17-2: Core ROM table
- Table 17-3: Neoverse™ N2 CoreSight component identification

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0116-original.png]]

### 原文第117页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=117|p.117]]

- Table 17-4: Core CTI register peripheral ID values
- Table 17-5: Debug registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0117-original.png]]

### 原文第118页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=118|p.118]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0118-original.png]]

### 原文第119页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=119|p.119]]

- Table 17-6: Debug registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0119-original.png]]

### 原文第120页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=120|p.120]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0120-original.png]]

### 原文第121页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=121|p.121]]

- Table 17-7: CoreROM registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0121-original.png]]

## 第18章 原图表

原文 p.122-136：PMU。

### 原文第122页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=122|p.122]]

- Table 18-1: Performance monitors Events

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0122-original.png]]

### 原文第123页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=123|p.123]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0123-original.png]]

### 原文第124页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=124|p.124]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0124-original.png]]

### 原文第125页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=125|p.125]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0125-original.png]]

### 原文第126页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=126|p.126]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0126-original.png]]

### 原文第127页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=127|p.127]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0127-original.png]]

### 原文第128页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=128|p.128]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0128-original.png]]

### 原文第129页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=129|p.129]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0129-original.png]]

### 原文第130页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=130|p.130]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0130-original.png]]

### 原文第131页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=131|p.131]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0131-original.png]]

### 原文第132页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=132|p.132]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0132-original.png]]

### 原文第133页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=133|p.133]]

- Table 18-2: Performance Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0133-original.png]]

### 原文第134页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=134|p.134]]

- Table 18-3: Performance Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0134-original.png]]

### 原文第135页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=135|p.135]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0135-original.png]]

### 原文第136页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=136|p.136]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0136-original.png]]

## 第19章 原图表

原文 p.137-149：ETE。

### 原文第137页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=137|p.137]]

- Figure 19-1: Trace unit components

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0137-original.png]]

### 原文第138页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=138|p.138]]

- Table 19-1: Trace unit resources

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0138-original.png]]

### 原文第139页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=139|p.139]]

- Table 19-2: Trace unit generation options

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0139-original.png]]

### 原文第141页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=141|p.141]]

- Figure 19-2: Programming trace unit registers using the Debug APB interface

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0141-original.png]]

### 原文第142页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=142|p.142]]

- Figure 19-3: Programming trace registers using the System register interface

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0142-original.png]]

### 原文第143页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=143|p.143]]

- Table 19-3: ETE events
- Table 19-4: Trace unit registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0143-original.png]]

### 原文第144页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=144|p.144]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0144-original.png]]

### 原文第145页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=145|p.145]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0145-original.png]]

### 原文第146页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=146|p.146]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0146-original.png]]

### 原文第147页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=147|p.147]]

- Table 19-5: Trace unit registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0147-original.png]]

### 原文第148页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=148|p.148]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0148-original.png]]

### 原文第149页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=149|p.149]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0149-original.png]]

## 第20章 原图表

原文 p.150-150：TRBE。

本章无编号图表；正文请回查 [[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=150|p.150]]。

## 第21章 原图表

原文 p.151-155：AMU。

### 原文第152页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=152|p.152]]

- Table 21-1: Mapping of counters to fixed events

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0152-original.png]]

### 原文第153页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=153|p.153]]

- Table 21-2: Activity Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0153-original.png]]

### 原文第154页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=154|p.154]]

- Table 21-3: Activity Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0154-original.png]]

### 原文第155页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=155|p.155]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0155-original.png]]

## 第22章 原图表

原文 p.156-159：SPE。

### 原文第156页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=156|p.156]]

- Figure 22-1: SPE behavior

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0156-original.png]]

### 原文第157页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=157|p.157]]

- Table 22-1: SPE events packet

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0157-original.png]]

### 原文第158页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=158|p.158]]

- Table 22-2: SPE data source packet
- Table 22-3: Statistical Profiling Extension registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0158-original.png]]

### 原文第159页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=159|p.159]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0159-original.png]]
