---
type: reference
status: reviewed
topics: [Neoverse, N2, CPU, architecture]
aliases: ["N2 附录A原图表"]
tags: [arm, neoverse, cpu, reference]
sources: ["[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]"]
source_document: "102099_0003_06_en"
source_revision: "r0p3 / Issue 06"
source_date: 2022-10-27
spec_issue: "CHI E"
source_sections: ["A"]
evidence: source-derived
verification: source-text-and-figure-index-checked
created: 2026-10-09
updated: 2026-10-10
---

# N2 Core TRM 附录A原图表

原文范围 p.160-241。本册收录 46 页截图，覆盖该范围的 61 个编号图表标题，以及跨页续表。

入口：[[N2-Core-TRM-完整中文精读]] · [[N2-Core-TRM-寄存器索引]] · [[Neoverse-MOC]]。

> [!info] 使用方式
> 原页保留完整正文宽度、图表、注释及水印，裁去页眉和页脚空白。图表标题保留英文以便和原文对照；续页若没有新标题，会注明“续表或相关原文”。
> 不含图表的普通说明页请用 PDF 页码链接回查。截图不替代正文中的配置、访问条件和编程步骤。

## 编号图表索引

| 编号与原文标题 | 原页 |
|---|---|
| Table A-1: Special-purpose registers summary | [[#原文第160页\|160]] |
| Table A-2: Performance Monitors registers summary | [[#原文第160页\|160]] |
| Figure A-1: AArch32_pmevcntr0 bit assignments | [[#原文第162页\|162]] |
| Table A-3: PMEVCNTR0 bit descriptions | [[#原文第162页\|162]] |
| Figure A-2: AArch32_pmevcntr1 bit assignments | [[#原文第165页\|165]] |
| Table A-6: PMEVCNTR1 bit descriptions | [[#原文第166页\|166]] |
| Figure A-3: AArch32_pmevcntr2 bit assignments | [[#原文第169页\|169]] |
| Table A-9: PMEVCNTR2 bit descriptions | [[#原文第169页\|169]] |
| Figure A-4: AArch32_pmevcntr3 bit assignments | [[#原文第172页\|172]] |
| Table A-12: PMEVCNTR3 bit descriptions | [[#原文第172页\|172]] |
| Figure A-5: AArch32_pmevcntr4 bit assignments | [[#原文第175页\|175]] |
| Table A-15: PMEVCNTR4 bit descriptions | [[#原文第175页\|175]] |
| Figure A-6: AArch32_pmevcntr5 bit assignments | [[#原文第178页\|178]] |
| Table A-18: PMEVCNTR5 bit descriptions | [[#原文第179页\|179]] |
| Figure A-7: AArch32_pmevtyper0 bit assignments | [[#原文第182页\|182]] |
| Table A-21: PMEVTYPER0 bit descriptions | [[#原文第182页\|182]] |
| Figure A-8: AArch32_pmevtyper1 bit assignments | [[#原文第186页\|186]] |
| Table A-24: PMEVTYPER1 bit descriptions | [[#原文第186页\|186]] |
| Figure A-9: AArch32_pmevtyper2 bit assignments | [[#原文第190页\|190]] |
| Table A-27: PMEVTYPER2 bit descriptions | [[#原文第190页\|190]] |
| Figure A-10: AArch32_pmevtyper3 bit assignments | [[#原文第194页\|194]] |
| Table A-30: PMEVTYPER3 bit descriptions | [[#原文第195页\|195]] |
| Figure A-11: AArch32_pmevtyper4 bit assignments | [[#原文第199页\|199]] |
| Table A-33: PMEVTYPER4 bit descriptions | [[#原文第199页\|199]] |
| Figure A-12: AArch32_pmevtyper5 bit assignments | [[#原文第203页\|203]] |
| Table A-36: PMEVTYPER5 bit descriptions | [[#原文第203页\|203]] |
| Table A-39: Generic Timer registers summary | [[#原文第207页\|207]] |
| Table A-40: Debug registers summary | [[#原文第207页\|207]] |
| Table A-41: Generic System Control registers summary | [[#原文第208页\|208]] |
| Table A-42: Floating Point registers summary | [[#原文第208页\|208]] |
| Figure A-13: AArch32_fpscr bit assignments | [[#原文第209页\|209]] |
| Table A-43: FPSCR bit descriptions | [[#原文第209页\|209]] |
| Table A-46: Activity Monitors registers summary | [[#原文第213页\|213]] |
| Figure A-14: AArch32_amevtyper00 bit assignments | [[#原文第215页\|215]] |
| Table A-47: AMEVTYPER00 bit descriptions | [[#原文第215页\|215]] |
| Figure A-15: AArch32_amevtyper01 bit assignments | [[#原文第216页\|216]] |
| Table A-49: AMEVTYPER01 bit descriptions | [[#原文第217页\|217]] |
| Figure A-16: AArch32_amevtyper02 bit assignments | [[#原文第218页\|218]] |
| Table A-51: AMEVTYPER02 bit descriptions | [[#原文第218页\|218]] |
| Figure A-17: AArch32_amevtyper03 bit assignments | [[#原文第220页\|220]] |
| Table A-53: AMEVTYPER03 bit descriptions | [[#原文第220页\|220]] |
| Figure A-18: AArch32_amevtyper10 bit assignments | [[#原文第222页\|222]] |
| Table A-55: AMEVTYPER10 bit descriptions | [[#原文第222页\|222]] |
| Figure A-19: AArch32_amevtyper11 bit assignments | [[#原文第224页\|224]] |
| Table A-57: AMEVTYPER11 bit descriptions | [[#原文第224页\|224]] |
| Figure A-20: AArch32_amevtyper12 bit assignments | [[#原文第226页\|226]] |
| Table A-59: AMEVTYPER12 bit descriptions | [[#原文第226页\|226]] |
| Figure A-21: AArch32_amevcntr00 bit assignments | [[#原文第228页\|228]] |
| Table A-61: AMEVCNTR00 bit descriptions | [[#原文第228页\|228]] |
| Figure A-22: AArch32_amevcntr10 bit assignments | [[#原文第230页\|230]] |
| Table A-64: AMEVCNTR10 bit descriptions | [[#原文第230页\|230]] |
| Figure A-23: AArch32_amevcntr01 bit assignments | [[#原文第232页\|232]] |
| Table A-67: AMEVCNTR01 bit descriptions | [[#原文第232页\|232]] |
| Figure A-24: AArch32_amevcntr11 bit assignments | [[#原文第234页\|234]] |
| Table A-70: AMEVCNTR11 bit descriptions | [[#原文第234页\|234]] |
| Figure A-25: AArch32_amevcntr02 bit assignments | [[#原文第236页\|236]] |
| Table A-73: AMEVCNTR02 bit descriptions | [[#原文第236页\|236]] |
| Figure A-26: AArch32_amevcntr12 bit assignments | [[#原文第238页\|238]] |
| Table A-76: AMEVCNTR12 bit descriptions | [[#原文第238页\|238]] |
| Figure A-27: AArch32_amevcntr03 bit assignments | [[#原文第240页\|240]] |
| Table A-79: AMEVCNTR03 bit descriptions | [[#原文第240页\|240]] |

## 原页截图

### 原文第160页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=160|p.160]]

- Table A-1: Special-purpose registers summary
- Table A-2: Performance Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0160-original.png]]

### 原文第161页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=161|p.161]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0161-original.png]]

### 原文第162页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=162|p.162]]

- Figure A-1: AArch32_pmevcntr0 bit assignments
- Table A-3: PMEVCNTR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0162-original.png]]

### 原文第165页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=165|p.165]]

- Figure A-2: AArch32_pmevcntr1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0165-original.png]]

### 原文第166页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=166|p.166]]

- Table A-6: PMEVCNTR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0166-original.png]]

### 原文第169页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=169|p.169]]

- Figure A-3: AArch32_pmevcntr2 bit assignments
- Table A-9: PMEVCNTR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0169-original.png]]

### 原文第172页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=172|p.172]]

- Figure A-4: AArch32_pmevcntr3 bit assignments
- Table A-12: PMEVCNTR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0172-original.png]]

### 原文第175页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=175|p.175]]

- Figure A-5: AArch32_pmevcntr4 bit assignments
- Table A-15: PMEVCNTR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0175-original.png]]

### 原文第178页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=178|p.178]]

- Figure A-6: AArch32_pmevcntr5 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0178-original.png]]

### 原文第179页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=179|p.179]]

- Table A-18: PMEVCNTR5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0179-original.png]]

### 原文第182页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=182|p.182]]

- Figure A-7: AArch32_pmevtyper0 bit assignments
- Table A-21: PMEVTYPER0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0182-original.png]]

### 原文第183页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=183|p.183]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0183-original.png]]

### 原文第186页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=186|p.186]]

- Figure A-8: AArch32_pmevtyper1 bit assignments
- Table A-24: PMEVTYPER1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0186-original.png]]

### 原文第187页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=187|p.187]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0187-original.png]]

### 原文第190页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=190|p.190]]

- Figure A-9: AArch32_pmevtyper2 bit assignments
- Table A-27: PMEVTYPER2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0190-original.png]]

### 原文第191页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=191|p.191]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0191-original.png]]

### 原文第194页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=194|p.194]]

- Figure A-10: AArch32_pmevtyper3 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0194-original.png]]

### 原文第195页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=195|p.195]]

- Table A-30: PMEVTYPER3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0195-original.png]]

### 原文第196页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=196|p.196]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0196-original.png]]

### 原文第199页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=199|p.199]]

- Figure A-11: AArch32_pmevtyper4 bit assignments
- Table A-33: PMEVTYPER4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0199-original.png]]

### 原文第200页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=200|p.200]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0200-original.png]]

### 原文第203页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=203|p.203]]

- Figure A-12: AArch32_pmevtyper5 bit assignments
- Table A-36: PMEVTYPER5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0203-original.png]]

### 原文第204页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=204|p.204]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0204-original.png]]

### 原文第207页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=207|p.207]]

- Table A-39: Generic Timer registers summary
- Table A-40: Debug registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0207-original.png]]

### 原文第208页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=208|p.208]]

- Table A-41: Generic System Control registers summary
- Table A-42: Floating Point registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0208-original.png]]

### 原文第209页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=209|p.209]]

- Figure A-13: AArch32_fpscr bit assignments
- Table A-43: FPSCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0209-original.png]]

### 原文第210页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=210|p.210]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0210-original.png]]

### 原文第211页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=211|p.211]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0211-original.png]]

### 原文第212页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=212|p.212]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0212-original.png]]

### 原文第213页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=213|p.213]]

- Table A-46: Activity Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0213-original.png]]

### 原文第214页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=214|p.214]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0214-original.png]]

### 原文第215页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=215|p.215]]

- Figure A-14: AArch32_amevtyper00 bit assignments
- Table A-47: AMEVTYPER00 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0215-original.png]]

### 原文第216页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=216|p.216]]

- Figure A-15: AArch32_amevtyper01 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0216-original.png]]

### 原文第217页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=217|p.217]]

- Table A-49: AMEVTYPER01 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0217-original.png]]

### 原文第218页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=218|p.218]]

- Figure A-16: AArch32_amevtyper02 bit assignments
- Table A-51: AMEVTYPER02 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0218-original.png]]

### 原文第220页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=220|p.220]]

- Figure A-17: AArch32_amevtyper03 bit assignments
- Table A-53: AMEVTYPER03 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0220-original.png]]

### 原文第222页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=222|p.222]]

- Figure A-18: AArch32_amevtyper10 bit assignments
- Table A-55: AMEVTYPER10 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0222-original.png]]

### 原文第224页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=224|p.224]]

- Figure A-19: AArch32_amevtyper11 bit assignments
- Table A-57: AMEVTYPER11 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0224-original.png]]

### 原文第226页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=226|p.226]]

- Figure A-20: AArch32_amevtyper12 bit assignments
- Table A-59: AMEVTYPER12 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0226-original.png]]

### 原文第228页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=228|p.228]]

- Figure A-21: AArch32_amevcntr00 bit assignments
- Table A-61: AMEVCNTR00 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0228-original.png]]

### 原文第230页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=230|p.230]]

- Figure A-22: AArch32_amevcntr10 bit assignments
- Table A-64: AMEVCNTR10 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0230-original.png]]

### 原文第232页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=232|p.232]]

- Figure A-23: AArch32_amevcntr01 bit assignments
- Table A-67: AMEVCNTR01 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0232-original.png]]

### 原文第234页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=234|p.234]]

- Figure A-24: AArch32_amevcntr11 bit assignments
- Table A-70: AMEVCNTR11 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0234-original.png]]

### 原文第236页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=236|p.236]]

- Figure A-25: AArch32_amevcntr02 bit assignments
- Table A-73: AMEVCNTR02 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0236-original.png]]

### 原文第238页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=238|p.238]]

- Figure A-26: AArch32_amevcntr12 bit assignments
- Table A-76: AMEVCNTR12 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0238-original.png]]

### 原文第240页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=240|p.240]]

- Figure A-27: AArch32_amevcntr03 bit assignments
- Table A-79: AMEVCNTR03 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0240-original.png]]
