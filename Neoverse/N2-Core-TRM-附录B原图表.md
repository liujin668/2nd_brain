---
type: reference
status: reviewed
topics: [Neoverse, N2, CPU, architecture]
aliases: ["N2 附录B原图表"]
tags: [arm, neoverse, cpu, reference]
sources: ["[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]"]
source_document: "102099_0003_06_en"
source_revision: "r0p3 / Issue 06"
source_date: 2022-10-27
spec_issue: "CHI E"
source_sections: ["B"]
evidence: source-derived
verification: source-text-and-figure-index-checked
created: 2026-10-09
updated: 2026-10-10
---

# N2 Core TRM 附录B原图表

原文范围 p.242-1130。本册收录 615 页截图，覆盖该范围的 598 个编号图表标题，以及跨页续表。

入口：[[N2-Core-TRM-完整中文精读]] · [[N2-Core-TRM-寄存器索引]] · [[Neoverse-MOC]]。

> [!info] 使用方式
> 原页保留完整正文宽度、图表、注释及水印，裁去页眉和页脚空白。图表标题保留英文以便和原文对照；续页若没有新标题，会注明“续表或相关原文”。
> 不含图表的普通说明页请用 PDF 页码链接回查。截图不替代正文中的配置、访问条件和编程步骤。

## 编号图表索引

| 编号与原文标题 | 原页 |
|---|---|
| Table B-1: Generic System Control registers summary | [[#原文第242页\|242]] |
| Figure B-1: AArch64_actlr_el1 bit assignments | [[#原文第248页\|248]] |
| Table B-2: ACTLR_EL1 bit descriptions | [[#原文第248页\|248]] |
| Figure B-2: AArch64_afsr0_el1 bit assignments | [[#原文第250页\|250]] |
| Table B-5: AFSR0_EL1 bit descriptions | [[#原文第250页\|250]] |
| Figure B-3: AArch64_afsr1_el1 bit assignments | [[#原文第252页\|252]] |
| Table B-10: AFSR1_EL1 bit descriptions | [[#原文第253页\|253]] |
| Figure B-4: AArch64_amair_el1 bit assignments | [[#原文第255页\|255]] |
| Table B-15: AMAIR_EL1 bit descriptions | [[#原文第255页\|255]] |
| Figure B-5: AArch64_lorid_el1 bit assignments | [[#原文第258页\|258]] |
| Table B-20: LORID_EL1 bit descriptions | [[#原文第258页\|258]] |
| Figure B-6: AArch64_imp_cpuactlr_el1 bit assignments | [[#原文第260页\|260]] |
| Table B-22: IMP_CPUACTLR_EL1 bit descriptions | [[#原文第260页\|260]] |
| Figure B-7: AArch64_imp_cpuactlr2_el1 bit assignments | [[#原文第261页\|261]] |
| Table B-25: IMP_CPUACTLR2_EL1 bit descriptions | [[#原文第262页\|262]] |
| Figure B-8: AArch64_imp_cpuactlr3_el1 bit assignments | [[#原文第263页\|263]] |
| Table B-28: IMP_CPUACTLR3_EL1 bit descriptions | [[#原文第263页\|263]] |
| Figure B-9: AArch64_imp_cpuactlr4_el1 bit assignments | [[#原文第265页\|265]] |
| Table B-31: IMP_CPUACTLR4_EL1 bit descriptions | [[#原文第265页\|265]] |
| Figure B-10: AArch64_imp_cpuectlr_el1 bit assignments | [[#原文第267页\|267]] |
| Table B-34: IMP_CPUECTLR_EL1 bit descriptions | [[#原文第267页\|267]] |
| Figure B-11: AArch64_imp_cpuectlr2_el1 bit assignments | [[#原文第276页\|276]] |
| Table B-37: IMP_CPUECTLR2_EL1 bit descriptions | [[#原文第276页\|276]] |
| Figure B-12: AArch64_imp_cpuppmcr3_el3 bit assignments | [[#原文第281页\|281]] |
| Table B-40: IMP_CPUPPMCR3_EL3 bit descriptions | [[#原文第281页\|281]] |
| Figure B-13: AArch64_imp_cpupwrctlr_el1 bit assignments | [[#原文第282页\|282]] |
| Table B-43: IMP_CPUPWRCTLR_EL1 bit descriptions | [[#原文第282页\|282]] |
| Figure B-14: AArch64_imp_atcr_el1 bit assignments | [[#原文第285页\|285]] |
| Table B-46: IMP_ATCR_EL1 bit descriptions | [[#原文第285页\|285]] |
| Figure B-15: AArch64_imp_cpuactlr5_el1 bit assignments | [[#原文第287页\|287]] |
| Table B-49: IMP_CPUACTLR5_EL1 bit descriptions | [[#原文第287页\|287]] |
| Figure B-16: AArch64_imp_cpuactlr6_el1 bit assignments | [[#原文第289页\|289]] |
| Table B-52: IMP_CPUACTLR6_EL1 bit descriptions | [[#原文第289页\|289]] |
| Figure B-17: AArch64_imp_cpuactlr7_el1 bit assignments | [[#原文第291页\|291]] |
| Table B-55: IMP_CPUACTLR7_EL1 bit descriptions | [[#原文第291页\|291]] |
| Figure B-18: AArch64_aidr_el1 bit assignments | [[#原文第293页\|293]] |
| Table B-58: AIDR_EL1 bit descriptions | [[#原文第293页\|293]] |
| Figure B-19: AArch64_fpcr bit assignments | [[#原文第294页\|294]] |
| Table B-60: FPCR bit descriptions | [[#原文第294页\|294]] |
| Figure B-20: AArch64_fpsr bit assignments | [[#原文第298页\|298]] |
| Table B-63: FPSR bit descriptions | [[#原文第298页\|298]] |
| Figure B-21: AArch64_actlr_el2 bit assignments | [[#原文第303页\|303]] |
| Table B-66: ACTLR_EL2 bit descriptions | [[#原文第303页\|303]] |
| Figure B-22: AArch64_hacr_el2 bit assignments | [[#原文第306页\|306]] |
| Table B-69: HACR_EL2 bit descriptions | [[#原文第306页\|306]] |
| Figure B-23: AArch64_afsr0_el2 bit assignments | [[#原文第307页\|307]] |
| Table B-72: AFSR0_EL2 bit descriptions | [[#原文第307页\|307]] |
| Figure B-24: AArch64_afsr1_el2 bit assignments | [[#原文第310页\|310]] |
| Table B-77: AFSR1_EL2 bit descriptions | [[#原文第310页\|310]] |
| Figure B-25: AArch64_amair_el2 bit assignments | [[#原文第313页\|313]] |
| Table B-82: AMAIR_EL2 bit descriptions | [[#原文第313页\|313]] |
| Figure B-26: AArch64_imp_atcr_el2 bit assignments | [[#原文第315页\|315]] |
| Table B-87: IMP_ATCR_EL2 bit descriptions | [[#原文第315页\|315]] |
| Figure B-27: AArch64_imp_avtcr_el2 bit assignments | [[#原文第318页\|318]] |
| Table B-90: IMP_AVTCR_EL2 bit descriptions | [[#原文第318页\|318]] |
| Figure B-28: AArch64_actlr_el3 bit assignments | [[#原文第320页\|320]] |
| Table B-93: ACTLR_EL3 bit descriptions | [[#原文第320页\|320]] |
| Figure B-29: AArch64_afsr0_el3 bit assignments | [[#原文第323页\|323]] |
| Table B-96: AFSR0_EL3 bit descriptions | [[#原文第323页\|323]] |
| Figure B-30: AArch64_afsr1_el3 bit assignments | [[#原文第324页\|324]] |
| Table B-99: AFSR1_EL3 bit descriptions | [[#原文第324页\|324]] |
| Figure B-31: AArch64_amair_el3 bit assignments | [[#原文第326页\|326]] |
| Table B-102: AMAIR_EL3 bit descriptions | [[#原文第326页\|326]] |
| Figure B-32: AArch64_rmr_el3 bit assignments | [[#原文第328页\|328]] |
| Table B-105: RMR_EL3 bit descriptions | [[#原文第328页\|328]] |
| Figure B-33: AArch64_imp_cpuppmcr_el3 bit assignments | [[#原文第329页\|329]] |
| Table B-108: IMP_CPUPPMCR_EL3 bit descriptions | [[#原文第329页\|329]] |
| Figure B-34: AArch64_imp_cpuppmcr2_el3 bit assignments | [[#原文第331页\|331]] |
| Table B-111: IMP_CPUPPMCR2_EL3 bit descriptions | [[#原文第331页\|331]] |
| Figure B-35: AArch64_imp_cpuppmcr4_el3 bit assignments | [[#原文第332页\|332]] |
| Table B-114: IMP_CPUPPMCR4_EL3 bit descriptions | [[#原文第332页\|332]] |
| Figure B-36: AArch64_imp_cpuppmcr5_el3 bit assignments | [[#原文第334页\|334]] |
| Table B-117: IMP_CPUPPMCR5_EL3 bit descriptions | [[#原文第334页\|334]] |
| Figure B-37: AArch64_imp_cpuppmcr6_el3 bit assignments | [[#原文第335页\|335]] |
| Table B-120: IMP_CPUPPMCR6_EL3 bit descriptions | [[#原文第336页\|336]] |
| Figure B-38: AArch64_imp_cpuactlr_el3 bit assignments | [[#原文第337页\|337]] |
| Table B-123: IMP_CPUACTLR_EL3 bit descriptions | [[#原文第337页\|337]] |
| Figure B-39: AArch64_imp_atcr_el3 bit assignments | [[#原文第339页\|339]] |
| Table B-126: IMP_ATCR_EL3 bit descriptions | [[#原文第339页\|339]] |
| Figure B-40: AArch64_imp_cpupselr_el3 bit assignments | [[#原文第341页\|341]] |
| Table B-129: IMP_CPUPSELR_EL3 bit descriptions | [[#原文第341页\|341]] |
| Figure B-41: AArch64_imp_cpupcr_el3 bit assignments | [[#原文第342页\|342]] |
| Table B-132: IMP_CPUPCR_EL3 bit descriptions | [[#原文第342页\|342]] |
| Figure B-42: AArch64_imp_cpupor_el3 bit assignments | [[#原文第344页\|344]] |
| Table B-135: IMP_CPUPOR_EL3 bit descriptions | [[#原文第344页\|344]] |
| Figure B-43: AArch64_imp_cpupmr_el3 bit assignments | [[#原文第345页\|345]] |
| Table B-138: IMP_CPUPMR_EL3 bit descriptions | [[#原文第345页\|345]] |
| Figure B-44: AArch64_imp_cpupor2_el3 bit assignments | [[#原文第347页\|347]] |
| Table B-141: IMP_CPUPOR2_EL3 bit descriptions | [[#原文第347页\|347]] |
| Figure B-45: AArch64_imp_cpupmr2_el3 bit assignments | [[#原文第348页\|348]] |
| Table B-144: IMP_CPUPMR2_EL3 bit descriptions | [[#原文第348页\|348]] |
| Figure B-46: AArch64_imp_cpupfr_el3 bit assignments | [[#原文第350页\|350]] |
| Table B-147: IMP_CPUPFR_EL3 bit descriptions | [[#原文第350页\|350]] |
| Table B-150: Debug registers summary | [[#原文第351页\|351]] |
| Figure B-47: AArch64_dbgbvr0_el1 bit assignments | [[#原文第353页\|353]] |
| Table B-151: DBGBVR0_EL1 bit descriptions | [[#原文第354页\|354]] |
| Figure B-48: AArch64_dbgbvr0_el1 bit assignments | [[#原文第354页\|354]] |
| Table B-152: DBGBVR0_EL1 bit descriptions | [[#原文第354页\|354]] |
| Figure B-49: AArch64_dbgbvr0_el1 bit assignments | [[#原文第354页\|354]] |
| Table B-153: DBGBVR0_EL1 bit descriptions | [[#原文第355页\|355]] |
| Figure B-50: AArch64_dbgbvr0_el1 bit assignments | [[#原文第355页\|355]] |
| Table B-154: DBGBVR0_EL1 bit descriptions | [[#原文第355页\|355]] |
| Figure B-51: AArch64_dbgbvr0_el1 bit assignments | [[#原文第355页\|355]] |
| Table B-155: DBGBVR0_EL1 bit descriptions | [[#原文第355页\|355]] |
| Figure B-52: AArch64_dbgbvr0_el1 bit assignments | [[#原文第356页\|356]] |
| Table B-156: DBGBVR0_EL1 bit descriptions | [[#原文第356页\|356]] |
| Figure B-53: AArch64_dbgbvr0_el1 bit assignments | [[#原文第356页\|356]] |
| Table B-157: DBGBVR0_EL1 bit descriptions | [[#原文第356页\|356]] |
| Figure B-54: AArch64_dbgbcr0_el1 bit assignments | [[#原文第358页\|358]] |
| Table B-160: DBGBCR0_EL1 bit descriptions | [[#原文第359页\|359]] |
| Table B-161: BAS description | [[#原文第362页\|362]] |
| Figure B-55: AArch64_dbgwvr0_el1 bit assignments | [[#原文第364页\|364]] |
| Table B-164: DBGWVR0_EL1 bit descriptions | [[#原文第364页\|364]] |
| Figure B-56: AArch64_dbgwcr0_el1 bit assignments | [[#原文第366页\|366]] |
| Table B-167: DBGWCR0_EL1 bit descriptions | [[#原文第366页\|366]] |
| Table B-168: BAS description table 1 | [[#原文第368页\|368]] |
| Table B-169: BAS description table 2 | [[#原文第368页\|368]] |
| Figure B-57: AArch64_dbgbvr1_el1 bit assignments | [[#原文第371页\|371]] |
| Table B-172: DBGBVR1_EL1 bit descriptions | [[#原文第371页\|371]] |
| Figure B-58: AArch64_dbgbvr1_el1 bit assignments | [[#原文第372页\|372]] |
| Table B-173: DBGBVR1_EL1 bit descriptions | [[#原文第372页\|372]] |
| Figure B-59: AArch64_dbgbvr1_el1 bit assignments | [[#原文第372页\|372]] |
| Table B-174: DBGBVR1_EL1 bit descriptions | [[#原文第372页\|372]] |
| Figure B-60: AArch64_dbgbvr1_el1 bit assignments | [[#原文第373页\|373]] |
| Table B-175: DBGBVR1_EL1 bit descriptions | [[#原文第373页\|373]] |
| Figure B-61: AArch64_dbgbvr1_el1 bit assignments | [[#原文第373页\|373]] |
| Table B-176: DBGBVR1_EL1 bit descriptions | [[#原文第373页\|373]] |
| Figure B-62: AArch64_dbgbvr1_el1 bit assignments | [[#原文第374页\|374]] |
| Table B-177: DBGBVR1_EL1 bit descriptions | [[#原文第374页\|374]] |
| Figure B-63: AArch64_dbgbvr1_el1 bit assignments | [[#原文第374页\|374]] |
| Table B-178: DBGBVR1_EL1 bit descriptions | [[#原文第374页\|374]] |
| Figure B-64: AArch64_dbgbcr1_el1 bit assignments | [[#原文第376页\|376]] |
| Table B-181: DBGBCR1_EL1 bit descriptions | [[#原文第376页\|376]] |
| Table B-182: BAS description | [[#原文第379页\|379]] |
| Figure B-65: AArch64_dbgwvr1_el1 bit assignments | [[#原文第381页\|381]] |
| Table B-185: DBGWVR1_EL1 bit descriptions | [[#原文第381页\|381]] |
| Figure B-66: AArch64_dbgwcr1_el1 bit assignments | [[#原文第383页\|383]] |
| Table B-188: DBGWCR1_EL1 bit descriptions | [[#原文第384页\|384]] |
| Table B-189: BAS description table 1 | [[#原文第385页\|385]] |
| Table B-190: BAS description table 2 | [[#原文第385页\|385]] |
| Figure B-67: AArch64_dbgbvr2_el1 bit assignments | [[#原文第388页\|388]] |
| Table B-193: DBGBVR2_EL1 bit descriptions | [[#原文第389页\|389]] |
| Figure B-68: AArch64_dbgbvr2_el1 bit assignments | [[#原文第389页\|389]] |
| Table B-194: DBGBVR2_EL1 bit descriptions | [[#原文第389页\|389]] |
| Figure B-69: AArch64_dbgbvr2_el1 bit assignments | [[#原文第389页\|389]] |
| Table B-195: DBGBVR2_EL1 bit descriptions | [[#原文第390页\|390]] |
| Figure B-70: AArch64_dbgbvr2_el1 bit assignments | [[#原文第390页\|390]] |
| Table B-196: DBGBVR2_EL1 bit descriptions | [[#原文第390页\|390]] |
| Figure B-71: AArch64_dbgbvr2_el1 bit assignments | [[#原文第390页\|390]] |
| Table B-197: DBGBVR2_EL1 bit descriptions | [[#原文第390页\|390]] |
| Figure B-72: AArch64_dbgbvr2_el1 bit assignments | [[#原文第391页\|391]] |
| Table B-198: DBGBVR2_EL1 bit descriptions | [[#原文第391页\|391]] |
| Figure B-73: AArch64_dbgbvr2_el1 bit assignments | [[#原文第391页\|391]] |
| Table B-199: DBGBVR2_EL1 bit descriptions | [[#原文第391页\|391]] |
| Figure B-74: AArch64_dbgbcr2_el1 bit assignments | [[#原文第393页\|393]] |
| Table B-202: DBGBCR2_EL1 bit descriptions | [[#原文第394页\|394]] |
| Table B-203: BAS description | [[#原文第397页\|397]] |
| Figure B-75: AArch64_dbgwvr2_el1 bit assignments | [[#原文第399页\|399]] |
| Table B-206: DBGWVR2_EL1 bit descriptions | [[#原文第399页\|399]] |
| Figure B-76: AArch64_dbgwcr2_el1 bit assignments | [[#原文第401页\|401]] |
| Table B-209: DBGWCR2_EL1 bit descriptions | [[#原文第402页\|402]] |
| Table B-210: BAS description table 1 | [[#原文第403页\|403]] |
| Table B-211: BAS description table 2 | [[#原文第403页\|403]] |
| Figure B-77: AArch64_dbgbvr3_el1 bit assignments | [[#原文第406页\|406]] |
| Table B-214: DBGBVR3_EL1 bit descriptions | [[#原文第407页\|407]] |
| Figure B-78: AArch64_dbgbvr3_el1 bit assignments | [[#原文第407页\|407]] |
| Table B-215: DBGBVR3_EL1 bit descriptions | [[#原文第407页\|407]] |
| Figure B-79: AArch64_dbgbvr3_el1 bit assignments | [[#原文第407页\|407]] |
| Table B-216: DBGBVR3_EL1 bit descriptions | [[#原文第408页\|408]] |
| Figure B-80: AArch64_dbgbvr3_el1 bit assignments | [[#原文第408页\|408]] |
| Table B-217: DBGBVR3_EL1 bit descriptions | [[#原文第408页\|408]] |
| Figure B-81: AArch64_dbgbvr3_el1 bit assignments | [[#原文第408页\|408]] |
| Table B-218: DBGBVR3_EL1 bit descriptions | [[#原文第408页\|408]] |
| Figure B-82: AArch64_dbgbvr3_el1 bit assignments | [[#原文第409页\|409]] |
| Table B-219: DBGBVR3_EL1 bit descriptions | [[#原文第409页\|409]] |
| Figure B-83: AArch64_dbgbvr3_el1 bit assignments | [[#原文第409页\|409]] |
| Table B-220: DBGBVR3_EL1 bit descriptions | [[#原文第409页\|409]] |
| Figure B-84: AArch64_dbgbcr3_el1 bit assignments | [[#原文第411页\|411]] |
| Table B-223: DBGBCR3_EL1 bit descriptions | [[#原文第412页\|412]] |
| Table B-224: BAS description | [[#原文第415页\|415]] |
| Figure B-85: AArch64_dbgwvr3_el1 bit assignments | [[#原文第417页\|417]] |
| Table B-227: DBGWVR3_EL1 bit descriptions | [[#原文第417页\|417]] |
| Figure B-86: AArch64_dbgwcr3_el1 bit assignments | [[#原文第419页\|419]] |
| Table B-230: DBGWCR3_EL1 bit descriptions | [[#原文第420页\|420]] |
| Table B-231: BAS description table 1 | [[#原文第421页\|421]] |
| Table B-232: BAS description table 2 | [[#原文第421页\|421]] |
| Figure B-87: AArch64_dbgbvr4_el1 bit assignments | [[#原文第424页\|424]] |
| Table B-235: DBGBVR4_EL1 bit descriptions | [[#原文第425页\|425]] |
| Figure B-88: AArch64_dbgbvr4_el1 bit assignments | [[#原文第425页\|425]] |
| Table B-236: DBGBVR4_EL1 bit descriptions | [[#原文第425页\|425]] |
| Figure B-89: AArch64_dbgbvr4_el1 bit assignments | [[#原文第425页\|425]] |
| Table B-237: DBGBVR4_EL1 bit descriptions | [[#原文第426页\|426]] |
| Figure B-90: AArch64_dbgbvr4_el1 bit assignments | [[#原文第426页\|426]] |
| Table B-238: DBGBVR4_EL1 bit descriptions | [[#原文第426页\|426]] |
| Figure B-91: AArch64_dbgbvr4_el1 bit assignments | [[#原文第426页\|426]] |
| Table B-239: DBGBVR4_EL1 bit descriptions | [[#原文第426页\|426]] |
| Figure B-92: AArch64_dbgbvr4_el1 bit assignments | [[#原文第427页\|427]] |
| Table B-240: DBGBVR4_EL1 bit descriptions | [[#原文第427页\|427]] |
| Figure B-93: AArch64_dbgbvr4_el1 bit assignments | [[#原文第427页\|427]] |
| Table B-241: DBGBVR4_EL1 bit descriptions | [[#原文第427页\|427]] |
| Figure B-94: AArch64_dbgbcr4_el1 bit assignments | [[#原文第429页\|429]] |
| Table B-244: DBGBCR4_EL1 bit descriptions | [[#原文第430页\|430]] |
| Table B-245: BAS description | [[#原文第433页\|433]] |
| Figure B-95: AArch64_dbgbvr5_el1 bit assignments | [[#原文第436页\|436]] |
| Table B-248: DBGBVR5_EL1 bit descriptions | [[#原文第436页\|436]] |
| Figure B-96: AArch64_dbgbvr5_el1 bit assignments | [[#原文第436页\|436]] |
| Table B-249: DBGBVR5_EL1 bit descriptions | [[#原文第436页\|436]] |
| Figure B-97: AArch64_dbgbvr5_el1 bit assignments | [[#原文第437页\|437]] |
| Table B-250: DBGBVR5_EL1 bit descriptions | [[#原文第437页\|437]] |
| Figure B-98: AArch64_dbgbvr5_el1 bit assignments | [[#原文第437页\|437]] |
| Table B-251: DBGBVR5_EL1 bit descriptions | [[#原文第437页\|437]] |
| Figure B-99: AArch64_dbgbvr5_el1 bit assignments | [[#原文第438页\|438]] |
| Table B-252: DBGBVR5_EL1 bit descriptions | [[#原文第438页\|438]] |
| Figure B-100: AArch64_dbgbvr5_el1 bit assignments | [[#原文第438页\|438]] |
| Table B-253: DBGBVR5_EL1 bit descriptions | [[#原文第438页\|438]] |
| Figure B-101: AArch64_dbgbvr5_el1 bit assignments | [[#原文第439页\|439]] |
| Table B-254: DBGBVR5_EL1 bit descriptions | [[#原文第439页\|439]] |
| Figure B-102: AArch64_dbgbcr5_el1 bit assignments | [[#原文第441页\|441]] |
| Table B-257: DBGBCR5_EL1 bit descriptions | [[#原文第441页\|441]] |
| Table B-258: BAS description | [[#原文第444页\|444]] |
| Figure B-103: AArch64_imp_idata0_el3 bit assignments | [[#原文第446页\|446]] |
| Table B-261: IMP_IDATA0_EL3 bit descriptions | [[#原文第446页\|446]] |
| Figure B-104: AArch64_imp_idata1_el3 bit assignments | [[#原文第447页\|447]] |
| Table B-263: IMP_IDATA1_EL3 bit descriptions | [[#原文第447页\|447]] |
| Figure B-105: AArch64_imp_idata2_el3 bit assignments | [[#原文第448页\|448]] |
| Table B-265: IMP_IDATA2_EL3 bit descriptions | [[#原文第449页\|449]] |
| Figure B-106: AArch64_imp_ddata0_el3 bit assignments | [[#原文第450页\|450]] |
| Table B-267: IMP_DDATA0_EL3 bit descriptions | [[#原文第450页\|450]] |
| Figure B-107: AArch64_imp_ddata1_el3 bit assignments | [[#原文第451页\|451]] |
| Table B-269: IMP_DDATA1_EL3 bit descriptions | [[#原文第451页\|451]] |
| Figure B-108: AArch64_imp_ddata2_el3 bit assignments | [[#原文第452页\|452]] |
| Table B-271: IMP_DDATA2_EL3 bit descriptions | [[#原文第452页\|452]] |
| Table B-273: Random Number Control registers summary | [[#原文第453页\|453]] |
| Figure B-109: AArch64_imp_cpurndbr_el3 bit assignments | [[#原文第454页\|454]] |
| Table B-274: IMP_CPURNDBR_EL3 bit descriptions | [[#原文第454页\|454]] |
| Figure B-110: AArch64_imp_cpurndpeid_el3 bit assignments | [[#原文第455页\|455]] |
| Table B-277: IMP_CPURNDPEID_EL3 bit descriptions | [[#原文第455页\|455]] |
| Table B-280: System instructions summary | [[#原文第457页\|457]] |
| Figure B-111: AArch64_sys_imp_ramindex bit assignments | [[#原文第457页\|457]] |
| Table B-281: SYS_IMP_RAMINDEX bit descriptions | [[#原文第457页\|457]] |
| Table B-283: Identification registers summary | [[#原文第458页\|458]] |
| Figure B-112: AArch64_midr_el1 bit assignments | [[#原文第460页\|460]] |
| Table B-284: MIDR_EL1 bit descriptions | [[#原文第460页\|460]] |
| Figure B-113: AArch64_mpidr_el1 bit assignments | [[#原文第462页\|462]] |
| Table B-286: MPIDR_EL1 bit descriptions | [[#原文第462页\|462]] |
| Figure B-114: AArch64_revidr_el1 bit assignments | [[#原文第464页\|464]] |
| Table B-288: REVIDR_EL1 bit descriptions | [[#原文第464页\|464]] |
| Figure B-115: AArch64_id_pfr0_el1 bit assignments | [[#原文第465页\|465]] |
| Table B-290: ID_PFR0_EL1 bit descriptions | [[#原文第465页\|465]] |
| Figure B-116: AArch64_id_pfr1_el1 bit assignments | [[#原文第467页\|467]] |
| Table B-292: ID_PFR1_EL1 bit descriptions | [[#原文第467页\|467]] |
| Figure B-117: AArch64_id_dfr0_el1 bit assignments | [[#原文第470页\|470]] |
| Table B-294: ID_DFR0_EL1 bit descriptions | [[#原文第470页\|470]] |
| Figure B-118: AArch64_id_afr0_el1 bit assignments | [[#原文第472页\|472]] |
| Table B-296: ID_AFR0_EL1 bit descriptions | [[#原文第472页\|472]] |
| Figure B-119: AArch64_id_mmfr0_el1 bit assignments | [[#原文第473页\|473]] |
| Table B-298: ID_MMFR0_EL1 bit descriptions | [[#原文第473页\|473]] |
| Figure B-120: AArch64_id_mmfr1_el1 bit assignments | [[#原文第475页\|475]] |
| Table B-300: ID_MMFR1_EL1 bit descriptions | [[#原文第476页\|476]] |
| Figure B-121: AArch64_id_mmfr2_el1 bit assignments | [[#原文第478页\|478]] |
| Table B-302: ID_MMFR2_EL1 bit descriptions | [[#原文第478页\|478]] |
| Figure B-122: AArch64_id_mmfr3_el1 bit assignments | [[#原文第480页\|480]] |
| Table B-304: ID_MMFR3_EL1 bit descriptions | [[#原文第480页\|480]] |
| Figure B-123: AArch64_id_isar0_el1 bit assignments | [[#原文第482页\|482]] |
| Table B-306: ID_ISAR0_EL1 bit descriptions | [[#原文第483页\|483]] |
| Figure B-124: AArch64_id_isar1_el1 bit assignments | [[#原文第484页\|484]] |
| Table B-308: ID_ISAR1_EL1 bit descriptions | [[#原文第485页\|485]] |
| Figure B-125: AArch64_id_isar2_el1 bit assignments | [[#原文第487页\|487]] |
| Table B-310: ID_ISAR2_EL1 bit descriptions | [[#原文第487页\|487]] |
| Figure B-126: AArch64_id_isar3_el1 bit assignments | [[#原文第489页\|489]] |
| Table B-312: ID_ISAR3_EL1 bit descriptions | [[#原文第489页\|489]] |
| Figure B-127: AArch64_id_isar4_el1 bit assignments | [[#原文第491页\|491]] |
| Table B-314: ID_ISAR4_EL1 bit descriptions | [[#原文第491页\|491]] |
| Figure B-128: AArch64_id_isar5_el1 bit assignments | [[#原文第493页\|493]] |
| Table B-316: ID_ISAR5_EL1 bit descriptions | [[#原文第493页\|493]] |
| Figure B-129: AArch64_id_mmfr4_el1 bit assignments | [[#原文第496页\|496]] |
| Table B-318: ID_MMFR4_EL1 bit descriptions | [[#原文第496页\|496]] |
| Figure B-130: AArch64_id_isar6_el1 bit assignments | [[#原文第498页\|498]] |
| Table B-320: ID_ISAR6_EL1 bit descriptions | [[#原文第498页\|498]] |
| Figure B-131: AArch64_mvfr0_el1 bit assignments | [[#原文第500页\|500]] |
| Table B-322: MVFR0_EL1 bit descriptions | [[#原文第501页\|501]] |
| Figure B-132: AArch64_mvfr1_el1 bit assignments | [[#原文第503页\|503]] |
| Table B-324: MVFR1_EL1 bit descriptions | [[#原文第503页\|503]] |
| Figure B-133: AArch64_mvfr2_el1 bit assignments | [[#原文第505页\|505]] |
| Table B-326: MVFR2_EL1 bit descriptions | [[#原文第505页\|505]] |
| Figure B-134: AArch64_id_pfr2_el1 bit assignments | [[#原文第507页\|507]] |
| Table B-328: ID_PFR2_EL1 bit descriptions | [[#原文第507页\|507]] |
| Figure B-135: AArch64_id_dfr1_el1 bit assignments | [[#原文第508页\|508]] |
| Table B-330: ID_DFR1_EL1 bit descriptions | [[#原文第508页\|508]] |
| Figure B-136: AArch64_id_mmfr5_el1 bit assignments | [[#原文第510页\|510]] |
| Table B-332: ID_MMFR5_EL1 bit descriptions | [[#原文第510页\|510]] |
| Figure B-137: AArch64_id_aa64pfr0_el1 bit assignments | [[#原文第511页\|511]] |
| Table B-334: ID_AA64PFR0_EL1 bit descriptions | [[#原文第512页\|512]] |
| Figure B-138: AArch64_id_aa64pfr1_el1 bit assignments | [[#原文第514页\|514]] |
| Table B-336: ID_AA64PFR1_EL1 bit descriptions | [[#原文第514页\|514]] |
| Figure B-139: AArch64_id_aa64pfr2_el1 bit assignments | [[#原文第516页\|516]] |
| Table B-338: ID_AA64PFR2_EL1 bit descriptions | [[#原文第516页\|516]] |
| Figure B-140: AArch64_id_aa64zfr0_el1 bit assignments | [[#原文第518页\|518]] |
| Table B-340: ID_AA64ZFR0_EL1 bit descriptions | [[#原文第518页\|518]] |
| Figure B-141: AArch64_id_aa64dfr0_el1 bit assignments | [[#原文第520页\|520]] |
| Table B-342: ID_AA64DFR0_EL1 bit descriptions | [[#原文第521页\|521]] |
| Figure B-142: AArch64_id_aa64dfr1_el1 bit assignments | [[#原文第523页\|523]] |
| Table B-344: ID_AA64DFR1_EL1 bit descriptions | [[#原文第523页\|523]] |
| Figure B-143: AArch64_id_aa64afr0_el1 bit assignments | [[#原文第524页\|524]] |
| Table B-346: ID_AA64AFR0_EL1 bit descriptions | [[#原文第524页\|524]] |
| Figure B-144: AArch64_id_aa64afr1_el1 bit assignments | [[#原文第525页\|525]] |
| Table B-348: ID_AA64AFR1_EL1 bit descriptions | [[#原文第526页\|526]] |
| Figure B-145: AArch64_id_aa64isar0_el1 bit assignments | [[#原文第527页\|527]] |
| Table B-350: ID_AA64ISAR0_EL1 bit descriptions | [[#原文第527页\|527]] |
| Figure B-146: AArch64_id_aa64isar1_el1 bit assignments | [[#原文第531页\|531]] |
| Table B-352: ID_AA64ISAR1_EL1 bit descriptions | [[#原文第531页\|531]] |
| Figure B-147: AArch64_id_aa64isar2_el1 bit assignments | [[#原文第534页\|534]] |
| Table B-354: ID_AA64ISAR2_EL1 bit descriptions | [[#原文第534页\|534]] |
| Figure B-148: AArch64_id_aa64mmfr0_el1 bit assignments | [[#原文第535页\|535]] |
| Table B-356: ID_AA64MMFR0_EL1 bit descriptions | [[#原文第535页\|535]] |
| Figure B-149: AArch64_id_aa64mmfr1_el1 bit assignments | [[#原文第538页\|538]] |
| Table B-358: ID_AA64MMFR1_EL1 bit descriptions | [[#原文第538页\|538]] |
| Figure B-150: AArch64_id_aa64mmfr2_el1 bit assignments | [[#原文第541页\|541]] |
| Table B-360: ID_AA64MMFR2_EL1 bit descriptions | [[#原文第541页\|541]] |
| Figure B-151: AArch64_mpamidr_el1 bit assignments | [[#原文第543页\|543]] |
| Table B-362: MPAMIDR_EL1 bit descriptions | [[#原文第544页\|544]] |
| Figure B-152: AArch64_imp_cpucfr_el1 bit assignments | [[#原文第545页\|545]] |
| Table B-364: IMP_CPUCFR_EL1 bit descriptions | [[#原文第545页\|545]] |
| Figure B-153: AArch64_clidr_el1 bit assignments | [[#原文第547页\|547]] |
| Table B-366: CLIDR_EL1 bit descriptions | [[#原文第547页\|547]] |
| Figure B-154: AArch64_gmid_el1 bit assignments | [[#原文第551页\|551]] |
| Table B-368: GMID_EL1 bit descriptions | [[#原文第551页\|551]] |
| Figure B-155: AArch64_ctr_el0 bit assignments | [[#原文第552页\|552]] |
| Table B-370: CTR_EL0 bit descriptions | [[#原文第553页\|553]] |
| Figure B-156: AArch64_dczid_el0 bit assignments | [[#原文第555页\|555]] |
| Table B-372: DCZID_EL0 bit descriptions | [[#原文第555页\|555]] |
| Table B-374: Special-purpose registers summary | [[#原文第556页\|556]] |
| Table B-375: Performance Monitors registers summary | [[#原文第556页\|556]] |
| Figure B-157: AArch64_pmmir_el1 bit assignments | [[#原文第558页\|558]] |
| Table B-376: PMMIR_EL1 bit descriptions | [[#原文第559页\|559]] |
| Figure B-158: AArch64_pmcr_el0 bit assignments | [[#原文第561页\|561]] |
| Table B-378: PMCR_EL0 bit descriptions | [[#原文第561页\|561]] |
| Figure B-159: AArch64_pmceid0_el0 bit assignments | [[#原文第567页\|567]] |
| Table B-381: PMCEID0_EL0 bit descriptions | [[#原文第567页\|567]] |
| Figure B-160: AArch64_pmceid1_el0 bit assignments | [[#原文第574页\|574]] |
| Table B-383: PMCEID1_EL0 bit descriptions | [[#原文第574页\|574]] |
| Figure B-161: AArch64_pmevcntr0_el0 bit assignments | [[#原文第580页\|580]] |
| Table B-385: PMEVCNTR0_EL0 bit descriptions | [[#原文第580页\|580]] |
| Figure B-162: AArch64_pmevcntr1_el0 bit assignments | [[#原文第584页\|584]] |
| Table B-388: PMEVCNTR1_EL0 bit descriptions | [[#原文第584页\|584]] |
| Figure B-163: AArch64_pmevcntr2_el0 bit assignments | [[#原文第588页\|588]] |
| Table B-391: PMEVCNTR2_EL0 bit descriptions | [[#原文第588页\|588]] |
| Figure B-164: AArch64_pmevcntr3_el0 bit assignments | [[#原文第591页\|591]] |
| Table B-394: PMEVCNTR3_EL0 bit descriptions | [[#原文第591页\|591]] |
| Figure B-165: AArch64_pmevcntr4_el0 bit assignments | [[#原文第595页\|595]] |
| Table B-397: PMEVCNTR4_EL0 bit descriptions | [[#原文第595页\|595]] |
| Figure B-166: AArch64_pmevcntr5_el0 bit assignments | [[#原文第599页\|599]] |
| Table B-400: PMEVCNTR5_EL0 bit descriptions | [[#原文第599页\|599]] |
| Figure B-167: AArch64_pmevtyper0_el0 bit assignments | [[#原文第602页\|602]] |
| Table B-403: PMEVTYPER0_EL0 bit descriptions | [[#原文第602页\|602]] |
| Figure B-168: AArch64_pmevtyper1_el0 bit assignments | [[#原文第607页\|607]] |
| Table B-406: PMEVTYPER1_EL0 bit descriptions | [[#原文第608页\|608]] |
| Figure B-169: AArch64_pmevtyper2_el0 bit assignments | [[#原文第613页\|613]] |
| Table B-409: PMEVTYPER2_EL0 bit descriptions | [[#原文第613页\|613]] |
| Figure B-170: AArch64_pmevtyper3_el0 bit assignments | [[#原文第618页\|618]] |
| Table B-412: PMEVTYPER3_EL0 bit descriptions | [[#原文第618页\|618]] |
| Figure B-171: AArch64_pmevtyper4_el0 bit assignments | [[#原文第623页\|623]] |
| Table B-415: PMEVTYPER4_EL0 bit descriptions | [[#原文第623页\|623]] |
| Figure B-172: AArch64_pmevtyper5_el0 bit assignments | [[#原文第628页\|628]] |
| Table B-418: PMEVTYPER5_EL0 bit descriptions | [[#原文第628页\|628]] |
| Table B-421: GIC system registers summary | [[#原文第633页\|633]] |
| Figure B-173: AArch64_icc_ap0r0_el1 bit assignments | [[#原文第636页\|636]] |
| Table B-422: ICC_AP0R0_EL1 bit descriptions | [[#原文第636页\|636]] |
| Figure B-174: AArch64_icv_ap0r0_el1 bit assignments | [[#原文第646页\|646]] |
| Table B-425: ICV_AP0R0_EL1 bit descriptions | [[#原文第646页\|646]] |
| Figure B-175: AArch64_icc_ap1r0_el1 bit assignments | [[#原文第655页\|655]] |
| Table B-428: ICC_AP1R0_EL1 bit descriptions | [[#原文第655页\|655]] |
| Figure B-176: AArch64_icv_ap1r0_el1 bit assignments | [[#原文第670页\|670]] |
| Table B-431: ICV_AP1R0_EL1 bit descriptions | [[#原文第670页\|670]] |
| Figure B-177: AArch64_icc_ctlr_el1 bit assignments | [[#原文第679页\|679]] |
| Table B-434: ICC_CTLR_EL1 bit descriptions | [[#原文第679页\|679]] |
| Figure B-178: AArch64_icv_ctlr_el1 bit assignments | [[#原文第684页\|684]] |
| Table B-437: ICV_CTLR_EL1 bit descriptions | [[#原文第684页\|684]] |
| Figure B-179: AArch64_ich_ap0r0_el2 bit assignments | [[#原文第687页\|687]] |
| Table B-440: ICH_AP0R0_EL2 bit descriptions | [[#原文第688页\|688]] |
| Figure B-180: AArch64_ich_ap1r0_el2 bit assignments | [[#原文第722页\|722]] |
| Table B-443: ICH_AP1R0_EL2 bit descriptions | [[#原文第723页\|723]] |
| Figure B-181: AArch64_ich_vtr_el2 bit assignments | [[#原文第757页\|757]] |
| Table B-446: ICH_VTR_EL2 bit descriptions | [[#原文第757页\|757]] |
| Figure B-182: AArch64_ich_lr0_el2 bit assignments | [[#原文第759页\|759]] |
| Table B-448: ICH_LR0_EL2 bit descriptions | [[#原文第759页\|759]] |
| Figure B-183: AArch64_ich_lr1_el2 bit assignments | [[#原文第763页\|763]] |
| Table B-451: ICH_LR1_EL2 bit descriptions | [[#原文第764页\|764]] |
| Figure B-184: AArch64_ich_lr2_el2 bit assignments | [[#原文第767页\|767]] |
| Table B-454: ICH_LR2_EL2 bit descriptions | [[#原文第768页\|768]] |
| Figure B-185: AArch64_ich_lr3_el2 bit assignments | [[#原文第771页\|771]] |
| Table B-457: ICH_LR3_EL2 bit descriptions | [[#原文第772页\|772]] |
| Figure B-186: AArch64_icc_ctlr_el3 bit assignments | [[#原文第775页\|775]] |
| Table B-460: ICC_CTLR_EL3 bit descriptions | [[#原文第775页\|775]] |
| Table B-463: Generic Timer registers summary | [[#原文第779页\|779]] |
| Table B-464: Other system control registers summary | [[#原文第780页\|780]] |
| Table B-465: Activity Monitors registers summary | [[#原文第781页\|781]] |
| Figure B-187: AArch64_amcfgr_el0 bit assignments | [[#原文第783页\|783]] |
| Table B-466: AMCFGR_EL0 bit descriptions | [[#原文第783页\|783]] |
| Figure B-188: AArch64_amcgcr_el0 bit assignments | [[#原文第785页\|785]] |
| Table B-468: AMCGCR_EL0 bit descriptions | [[#原文第785页\|785]] |
| Figure B-189: AArch64_amevcntr00_el0 bit assignments | [[#原文第787页\|787]] |
| Table B-470: AMEVCNTR00_EL0 bit descriptions | [[#原文第787页\|787]] |
| Figure B-190: AArch64_amevcntr01_el0 bit assignments | [[#原文第789页\|789]] |
| Table B-473: AMEVCNTR01_EL0 bit descriptions | [[#原文第789页\|789]] |
| Figure B-191: AArch64_amevcntr02_el0 bit assignments | [[#原文第791页\|791]] |
| Table B-476: AMEVCNTR02_EL0 bit descriptions | [[#原文第791页\|791]] |
| Figure B-192: AArch64_amevcntr03_el0 bit assignments | [[#原文第793页\|793]] |
| Table B-479: AMEVCNTR03_EL0 bit descriptions | [[#原文第793页\|793]] |
| Figure B-193: AArch64_amevtyper00_el0 bit assignments | [[#原文第795页\|795]] |
| Table B-482: AMEVTYPER00_EL0 bit descriptions | [[#原文第796页\|796]] |
| Figure B-194: AArch64_amevtyper01_el0 bit assignments | [[#原文第798页\|798]] |
| Table B-484: AMEVTYPER01_EL0 bit descriptions | [[#原文第798页\|798]] |
| Figure B-195: AArch64_amevtyper02_el0 bit assignments | [[#原文第800页\|800]] |
| Table B-486: AMEVTYPER02_EL0 bit descriptions | [[#原文第800页\|800]] |
| Figure B-196: AArch64_amevtyper03_el0 bit assignments | [[#原文第802页\|802]] |
| Table B-488: AMEVTYPER03_EL0 bit descriptions | [[#原文第802页\|802]] |
| Figure B-197: AArch64_amevcntr10_el0 bit assignments | [[#原文第804页\|804]] |
| Table B-490: AMEVCNTR10_EL0 bit descriptions | [[#原文第804页\|804]] |
| Figure B-198: AArch64_amevcntr11_el0 bit assignments | [[#原文第806页\|806]] |
| Table B-493: AMEVCNTR11_EL0 bit descriptions | [[#原文第806页\|806]] |
| Figure B-199: AArch64_amevcntr12_el0 bit assignments | [[#原文第808页\|808]] |
| Table B-496: AMEVCNTR12_EL0 bit descriptions | [[#原文第809页\|809]] |
| Figure B-200: AArch64_amevtyper10_el0 bit assignments | [[#原文第811页\|811]] |
| Table B-499: AMEVTYPER10_EL0 bit descriptions | [[#原文第811页\|811]] |
| Figure B-201: AArch64_amevtyper11_el0 bit assignments | [[#原文第813页\|813]] |
| Table B-501: AMEVTYPER11_EL0 bit descriptions | [[#原文第813页\|813]] |
| Figure B-202: AArch64_amevtyper12_el0 bit assignments | [[#原文第815页\|815]] |
| Table B-503: AMEVTYPER12_EL0 bit descriptions | [[#原文第815页\|815]] |
| Table B-505: Trace unit registers summary | [[#原文第817页\|817]] |
| Figure B-203: AArch64_trcseqevr0 bit assignments | [[#原文第821页\|821]] |
| Table B-506: TRCSEQEVR0 bit descriptions | [[#原文第821页\|821]] |
| Figure B-204: AArch64_trcidr8 bit assignments | [[#原文第825页\|825]] |
| Table B-509: TRCIDR8 bit descriptions | [[#原文第825页\|825]] |
| Figure B-205: AArch64_trcimspec0 bit assignments | [[#原文第826页\|826]] |
| Table B-511: TRCIMSPEC0 bit descriptions | [[#原文第826页\|826]] |
| Figure B-206: AArch64_trcseqevr1 bit assignments | [[#原文第829页\|829]] |
| Table B-514: TRCSEQEVR1 bit descriptions | [[#原文第829页\|829]] |
| Figure B-207: AArch64_trcseqevr2 bit assignments | [[#原文第832页\|832]] |
| Table B-517: TRCSEQEVR2 bit descriptions | [[#原文第832页\|832]] |
| Figure B-208: AArch64_trcidr10 bit assignments | [[#原文第836页\|836]] |
| Table B-520: TRCIDR10 bit descriptions | [[#原文第836页\|836]] |
| Figure B-209: AArch64_trcidr11 bit assignments | [[#原文第837页\|837]] |
| Table B-522: TRCIDR11 bit descriptions | [[#原文第838页\|838]] |
| Figure B-210: AArch64_trccntctlr0 bit assignments | [[#原文第839页\|839]] |
| Table B-524: TRCCNTCTLR0 bit descriptions | [[#原文第839页\|839]] |
| Figure B-211: AArch64_trcidr12 bit assignments | [[#原文第843页\|843]] |
| Table B-527: TRCIDR12 bit descriptions | [[#原文第843页\|843]] |
| Figure B-212: AArch64_trccntctlr1 bit assignments | [[#原文第845页\|845]] |
| Table B-529: TRCCNTCTLR1 bit descriptions | [[#原文第845页\|845]] |
| Figure B-213: AArch64_trcidr13 bit assignments | [[#原文第848页\|848]] |
| Table B-532: TRCIDR13 bit descriptions | [[#原文第849页\|849]] |
| Figure B-214: AArch64_trcextinselr0 bit assignments | [[#原文第850页\|850]] |
| Table B-534: TRCEXTINSELR0 bit descriptions | [[#原文第850页\|850]] |
| Figure B-215: AArch64_trccntvr0 bit assignments | [[#原文第853页\|853]] |
| Table B-537: TRCCNTVR0 bit descriptions | [[#原文第853页\|853]] |
| Figure B-216: AArch64_trcidr0 bit assignments | [[#原文第856页\|856]] |
| Table B-540: TRCIDR0 bit descriptions | [[#原文第856页\|856]] |
| Figure B-217: AArch64_trcextinselr1 bit assignments | [[#原文第858页\|858]] |
| Table B-542: TRCEXTINSELR1 bit descriptions | [[#原文第859页\|859]] |
| Figure B-218: AArch64_trccntvr1 bit assignments | [[#原文第861页\|861]] |
| Table B-545: TRCCNTVR1 bit descriptions | [[#原文第861页\|861]] |
| Figure B-219: AArch64_trcidr1 bit assignments | [[#原文第864页\|864]] |
| Table B-548: TRCIDR1 bit descriptions | [[#原文第864页\|864]] |
| Figure B-220: AArch64_trcextinselr2 bit assignments | [[#原文第866页\|866]] |
| Table B-550: TRCEXTINSELR2 bit descriptions | [[#原文第866页\|866]] |
| Figure B-221: AArch64_trcidr2 bit assignments | [[#原文第869页\|869]] |
| Table B-553: TRCIDR2 bit descriptions | [[#原文第869页\|869]] |
| Figure B-222: AArch64_trcextinselr3 bit assignments | [[#原文第871页\|871]] |
| Table B-555: TRCEXTINSELR3 bit descriptions | [[#原文第871页\|871]] |
| Figure B-223: AArch64_trcidr3 bit assignments | [[#原文第874页\|874]] |
| Table B-558: TRCIDR3 bit descriptions | [[#原文第874页\|874]] |
| Figure B-224: AArch64_trcidr4 bit assignments | [[#原文第876页\|876]] |
| Table B-560: TRCIDR4 bit descriptions | [[#原文第877页\|877]] |
| Figure B-225: AArch64_trcidr5 bit assignments | [[#原文第879页\|879]] |
| Table B-562: TRCIDR5 bit descriptions | [[#原文第879页\|879]] |
| Figure B-226: AArch64_trcssccr0 bit assignments | [[#原文第881页\|881]] |
| Table B-564: TRCSSCCR0 bit descriptions | [[#原文第881页\|881]] |
| Figure B-227: AArch64_trcrsctlr2 bit assignments | [[#原文第884页\|884]] |
| Table B-567: TRCRSCTLR2 bit descriptions | [[#原文第884页\|884]] |
| Figure B-228: AArch64_trcrsctlr3 bit assignments | [[#原文第891页\|891]] |
| Table B-570: TRCRSCTLR3 bit descriptions | [[#原文第891页\|891]] |
| Figure B-229: AArch64_trcrsctlr4 bit assignments | [[#原文第897页\|897]] |
| Table B-573: TRCRSCTLR4 bit descriptions | [[#原文第897页\|897]] |
| Figure B-230: AArch64_trcrsctlr5 bit assignments | [[#原文第904页\|904]] |
| Table B-576: TRCRSCTLR5 bit descriptions | [[#原文第904页\|904]] |
| Figure B-231: AArch64_trcrsctlr6 bit assignments | [[#原文第910页\|910]] |
| Table B-579: TRCRSCTLR6 bit descriptions | [[#原文第910页\|910]] |
| Figure B-232: AArch64_trcrsctlr7 bit assignments | [[#原文第917页\|917]] |
| Table B-582: TRCRSCTLR7 bit descriptions | [[#原文第917页\|917]] |
| Figure B-233: AArch64_trcrsctlr8 bit assignments | [[#原文第923页\|923]] |
| Table B-585: TRCRSCTLR8 bit descriptions | [[#原文第923页\|923]] |
| Figure B-234: AArch64_trcsscsr0 bit assignments | [[#原文第930页\|930]] |
| Table B-588: TRCSSCSR0 bit descriptions | [[#原文第930页\|930]] |
| Figure B-235: AArch64_trcrsctlr9 bit assignments | [[#原文第934页\|934]] |
| Table B-591: TRCRSCTLR9 bit descriptions | [[#原文第934页\|934]] |
| Figure B-236: AArch64_trcrsctlr10 bit assignments | [[#原文第940页\|940]] |
| Table B-594: TRCRSCTLR10 bit descriptions | [[#原文第940页\|940]] |
| Figure B-237: AArch64_trcrsctlr11 bit assignments | [[#原文第947页\|947]] |
| Table B-597: TRCRSCTLR11 bit descriptions | [[#原文第947页\|947]] |
| Figure B-238: AArch64_trcrsctlr12 bit assignments | [[#原文第953页\|953]] |
| Table B-600: TRCRSCTLR12 bit descriptions | [[#原文第953页\|953]] |
| Figure B-239: AArch64_trcrsctlr13 bit assignments | [[#原文第960页\|960]] |
| Table B-603: TRCRSCTLR13 bit descriptions | [[#原文第960页\|960]] |
| Figure B-240: AArch64_trcrsctlr14 bit assignments | [[#原文第966页\|966]] |
| Table B-606: TRCRSCTLR14 bit descriptions | [[#原文第966页\|966]] |
| Figure B-241: AArch64_trcrsctlr15 bit assignments | [[#原文第973页\|973]] |
| Table B-609: TRCRSCTLR15 bit descriptions | [[#原文第973页\|973]] |
| Figure B-242: AArch64_trcacvr0 bit assignments | [[#原文第979页\|979]] |
| Table B-612: TRCACVR0 bit descriptions | [[#原文第980页\|980]] |
| Figure B-243: AArch64_trcacatr0 bit assignments | [[#原文第983页\|983]] |
| Table B-615: TRCACATR0 bit descriptions | [[#原文第983页\|983]] |
| Figure B-244: AArch64_trcacvr1 bit assignments | [[#原文第987页\|987]] |
| Table B-618: TRCACVR1 bit descriptions | [[#原文第988页\|988]] |
| Figure B-245: AArch64_trcacatr1 bit assignments | [[#原文第991页\|991]] |
| Table B-621: TRCACATR1 bit descriptions | [[#原文第991页\|991]] |
| Figure B-246: AArch64_trcacvr2 bit assignments | [[#原文第995页\|995]] |
| Table B-624: TRCACVR2 bit descriptions | [[#原文第996页\|996]] |
| Figure B-247: AArch64_trcacatr2 bit assignments | [[#原文第999页\|999]] |
| Table B-627: TRCACATR2 bit descriptions | [[#原文第999页\|999]] |
| Figure B-248: AArch64_trcacvr3 bit assignments | [[#原文第1003页\|1003]] |
| Table B-630: TRCACVR3 bit descriptions | [[#原文第1004页\|1004]] |
| Figure B-249: AArch64_trcacatr3 bit assignments | [[#原文第1007页\|1007]] |
| Table B-633: TRCACATR3 bit descriptions | [[#原文第1007页\|1007]] |
| Figure B-250: AArch64_trcacvr4 bit assignments | [[#原文第1011页\|1011]] |
| Table B-636: TRCACVR4 bit descriptions | [[#原文第1012页\|1012]] |
| Figure B-251: AArch64_trcacatr4 bit assignments | [[#原文第1015页\|1015]] |
| Table B-639: TRCACATR4 bit descriptions | [[#原文第1015页\|1015]] |
| Figure B-252: AArch64_trcacvr5 bit assignments | [[#原文第1019页\|1019]] |
| Table B-642: TRCACVR5 bit descriptions | [[#原文第1020页\|1020]] |
| Figure B-253: AArch64_trcacatr5 bit assignments | [[#原文第1023页\|1023]] |
| Table B-645: TRCACATR5 bit descriptions | [[#原文第1023页\|1023]] |
| Figure B-254: AArch64_trcacvr6 bit assignments | [[#原文第1027页\|1027]] |
| Table B-648: TRCACVR6 bit descriptions | [[#原文第1028页\|1028]] |
| Figure B-255: AArch64_trcacatr6 bit assignments | [[#原文第1031页\|1031]] |
| Table B-651: TRCACATR6 bit descriptions | [[#原文第1031页\|1031]] |
| Figure B-256: AArch64_trcacvr7 bit assignments | [[#原文第1035页\|1035]] |
| Table B-654: TRCACVR7 bit descriptions | [[#原文第1036页\|1036]] |
| Figure B-257: AArch64_trcacatr7 bit assignments | [[#原文第1039页\|1039]] |
| Table B-657: TRCACATR7 bit descriptions | [[#原文第1039页\|1039]] |
| Figure B-258: AArch64_trccidcvr0 bit assignments | [[#原文第1043页\|1043]] |
| Table B-660: TRCCIDCVR0 bit descriptions | [[#原文第1043页\|1043]] |
| Figure B-259: AArch64_trcvmidcvr0 bit assignments | [[#原文第1046页\|1046]] |
| Table B-663: TRCVMIDCVR0 bit descriptions | [[#原文第1046页\|1046]] |
| Table B-666: Memory Partitioning and Monitoring registers summary | [[#原文第1048页\|1048]] |
| Figure B-260: AArch64_mpamvpmv_el2 bit assignments | [[#原文第1049页\|1049]] |
| Table B-667: MPAMVPMV_EL2 bit descriptions | [[#原文第1049页\|1049]] |
| Figure B-261: AArch64_mpamvpm0_el2 bit assignments | [[#原文第1052页\|1052]] |
| Table B-670: MPAMVPM0_EL2 bit descriptions | [[#原文第1052页\|1052]] |
| Figure B-262: AArch64_mpamvpm1_el2 bit assignments | [[#原文第1054页\|1054]] |
| Table B-673: MPAMVPM1_EL2 bit descriptions | [[#原文第1055页\|1055]] |
| Figure B-263: AArch64_mpamvpm2_el2 bit assignments | [[#原文第1057页\|1057]] |
| Table B-676: MPAMVPM2_EL2 bit descriptions | [[#原文第1057页\|1057]] |
| Figure B-264: AArch64_mpamvpm3_el2 bit assignments | [[#原文第1059页\|1059]] |
| Table B-679: MPAMVPM3_EL2 bit descriptions | [[#原文第1059页\|1059]] |
| Figure B-265: AArch64_mpamvpm4_el2 bit assignments | [[#原文第1062页\|1062]] |
| Table B-682: MPAMVPM4_EL2 bit descriptions | [[#原文第1062页\|1062]] |
| Figure B-266: AArch64_mpamvpm5_el2 bit assignments | [[#原文第1064页\|1064]] |
| Table B-685: MPAMVPM5_EL2 bit descriptions | [[#原文第1064页\|1064]] |
| Figure B-267: AArch64_mpamvpm6_el2 bit assignments | [[#原文第1066页\|1066]] |
| Table B-688: MPAMVPM6_EL2 bit descriptions | [[#原文第1067页\|1067]] |
| Figure B-268: AArch64_mpamvpm7_el2 bit assignments | [[#原文第1069页\|1069]] |
| Table B-691: MPAMVPM7_EL2 bit descriptions | [[#原文第1069页\|1069]] |
| Table B-694: RAS registers summary | [[#原文第1070页\|1070]] |
| Figure B-269: AArch64_erridr_el1 bit assignments | [[#原文第1072页\|1072]] |
| Table B-695: ERRIDR_EL1 bit descriptions | [[#原文第1072页\|1072]] |
| Figure B-270: AArch64_errselr_el1 bit assignments | [[#原文第1073页\|1073]] |
| Table B-697: ERRSELR_EL1 bit descriptions | [[#原文第1073页\|1073]] |
| Figure B-271: AArch64_erxfr_el1 bit assignments | [[#原文第1075页\|1075]] |
| Table B-700: ERXFR_EL1 bit descriptions | [[#原文第1075页\|1075]] |
| Figure B-272: AArch64_erxctlr_el1 bit assignments | [[#原文第1078页\|1078]] |
| Table B-702: ERXCTLR_EL1 bit descriptions | [[#原文第1078页\|1078]] |
| Figure B-273: AArch64_erxstatus_el1 bit assignments | [[#原文第1082页\|1082]] |
| Table B-705: ERXSTATUS_EL1 bit descriptions | [[#原文第1082页\|1082]] |
| Figure B-274: AArch64_erxaddr_el1 bit assignments | [[#原文第1088页\|1088]] |
| Table B-708: ERXADDR_EL1 bit descriptions | [[#原文第1088页\|1088]] |
| Figure B-275: AArch64_erxpfgf_el1 bit assignments | [[#原文第1090页\|1090]] |
| Table B-711: ERXPFGF_EL1 bit descriptions | [[#原文第1091页\|1091]] |
| Figure B-276: AArch64_erxpfgctl_el1 bit assignments | [[#原文第1095页\|1095]] |
| Table B-713: ERXPFGCTL_EL1 bit descriptions | [[#原文第1095页\|1095]] |
| Figure B-277: AArch64_erxpfgcdn_el1 bit assignments | [[#原文第1099页\|1099]] |
| Table B-716: ERXPFGCDN_EL1 bit descriptions | [[#原文第1099页\|1099]] |
| Figure B-278: AArch64_erxmisc0_el1 bit assignments | [[#原文第1102页\|1102]] |
| Table B-719: ERXMISC0_EL1 bit descriptions | [[#原文第1102页\|1102]] |
| Figure B-279: AArch64_erxmisc1_el1 bit assignments | [[#原文第1108页\|1108]] |
| Table B-722: ERXMISC1_EL1 bit descriptions | [[#原文第1108页\|1108]] |
| Figure B-280: AArch64_erxmisc2_el1 bit assignments | [[#原文第1110页\|1110]] |
| Table B-725: ERXMISC2_EL1 bit descriptions | [[#原文第1110页\|1110]] |
| Figure B-281: AArch64_erxmisc3_el1 bit assignments | [[#原文第1112页\|1112]] |
| Table B-728: ERXMISC3_EL1 bit descriptions | [[#原文第1113页\|1113]] |
| Table B-731: Statistical Profiling Extension registers summary | [[#原文第1114页\|1114]] |
| Figure B-282: AArch64_pmsevfr_el1 bit assignments | [[#原文第1116页\|1116]] |
| Table B-732: PMSEVFR_EL1 bit descriptions | [[#原文第1116页\|1116]] |
| Figure B-283: AArch64_pmsidr_el1 bit assignments | [[#原文第1126页\|1126]] |
| Table B-735: PMSIDR_EL1 bit descriptions | [[#原文第1127页\|1127]] |
| Figure B-284: AArch64_pmbidr_el1 bit assignments | [[#原文第1129页\|1129]] |
| Table B-737: PMBIDR_EL1 bit descriptions | [[#原文第1129页\|1129]] |
| Table B-739: Trace Buffer Extension registers summary | [[#原文第1130页\|1130]] |

## 原页截图

### 原文第242页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=242|p.242]]

- Table B-1: Generic System Control registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0242-original.png]]

### 原文第243页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=243|p.243]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0243-original.png]]

### 原文第244页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=244|p.244]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0244-original.png]]

### 原文第245页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=245|p.245]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0245-original.png]]

### 原文第246页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=246|p.246]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0246-original.png]]

### 原文第247页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=247|p.247]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0247-original.png]]

### 原文第248页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=248|p.248]]

- Figure B-1: AArch64_actlr_el1 bit assignments
- Table B-2: ACTLR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0248-original.png]]

### 原文第250页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=250|p.250]]

- Figure B-2: AArch64_afsr0_el1 bit assignments
- Table B-5: AFSR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0250-original.png]]

### 原文第252页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=252|p.252]]

- Figure B-3: AArch64_afsr1_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0252-original.png]]

### 原文第253页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=253|p.253]]

- Table B-10: AFSR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0253-original.png]]

### 原文第255页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=255|p.255]]

- Figure B-4: AArch64_amair_el1 bit assignments
- Table B-15: AMAIR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0255-original.png]]

### 原文第258页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=258|p.258]]

- Figure B-5: AArch64_lorid_el1 bit assignments
- Table B-20: LORID_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0258-original.png]]

### 原文第260页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=260|p.260]]

- Figure B-6: AArch64_imp_cpuactlr_el1 bit assignments
- Table B-22: IMP_CPUACTLR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0260-original.png]]

### 原文第261页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=261|p.261]]

- Figure B-7: AArch64_imp_cpuactlr2_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0261-original.png]]

### 原文第262页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=262|p.262]]

- Table B-25: IMP_CPUACTLR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0262-original.png]]

### 原文第263页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=263|p.263]]

- Figure B-8: AArch64_imp_cpuactlr3_el1 bit assignments
- Table B-28: IMP_CPUACTLR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0263-original.png]]

### 原文第265页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=265|p.265]]

- Figure B-9: AArch64_imp_cpuactlr4_el1 bit assignments
- Table B-31: IMP_CPUACTLR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0265-original.png]]

### 原文第267页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=267|p.267]]

- Figure B-10: AArch64_imp_cpuectlr_el1 bit assignments
- Table B-34: IMP_CPUECTLR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0267-original.png]]

### 原文第268页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=268|p.268]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0268-original.png]]

### 原文第269页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=269|p.269]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0269-original.png]]

### 原文第270页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=270|p.270]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0270-original.png]]

### 原文第271页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=271|p.271]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0271-original.png]]

### 原文第272页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=272|p.272]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0272-original.png]]

### 原文第273页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=273|p.273]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0273-original.png]]

### 原文第274页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=274|p.274]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0274-original.png]]

### 原文第276页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=276|p.276]]

- Figure B-11: AArch64_imp_cpuectlr2_el1 bit assignments
- Table B-37: IMP_CPUECTLR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0276-original.png]]

### 原文第277页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=277|p.277]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0277-original.png]]

### 原文第278页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=278|p.278]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0278-original.png]]

### 原文第279页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=279|p.279]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0279-original.png]]

### 原文第281页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=281|p.281]]

- Figure B-12: AArch64_imp_cpuppmcr3_el3 bit assignments
- Table B-40: IMP_CPUPPMCR3_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0281-original.png]]

### 原文第282页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=282|p.282]]

- Figure B-13: AArch64_imp_cpupwrctlr_el1 bit assignments
- Table B-43: IMP_CPUPWRCTLR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0282-original.png]]

### 原文第283页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=283|p.283]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0283-original.png]]

### 原文第285页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=285|p.285]]

- Figure B-14: AArch64_imp_atcr_el1 bit assignments
- Table B-46: IMP_ATCR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0285-original.png]]

### 原文第286页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=286|p.286]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0286-original.png]]

### 原文第287页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=287|p.287]]

- Figure B-15: AArch64_imp_cpuactlr5_el1 bit assignments
- Table B-49: IMP_CPUACTLR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0287-original.png]]

### 原文第289页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=289|p.289]]

- Figure B-16: AArch64_imp_cpuactlr6_el1 bit assignments
- Table B-52: IMP_CPUACTLR6_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0289-original.png]]

### 原文第291页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=291|p.291]]

- Figure B-17: AArch64_imp_cpuactlr7_el1 bit assignments
- Table B-55: IMP_CPUACTLR7_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0291-original.png]]

### 原文第293页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=293|p.293]]

- Figure B-18: AArch64_aidr_el1 bit assignments
- Table B-58: AIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0293-original.png]]

### 原文第294页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=294|p.294]]

- Figure B-19: AArch64_fpcr bit assignments
- Table B-60: FPCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0294-original.png]]

### 原文第295页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=295|p.295]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0295-original.png]]

### 原文第298页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=298|p.298]]

- Figure B-20: AArch64_fpsr bit assignments
- Table B-63: FPSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0298-original.png]]

### 原文第299页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=299|p.299]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0299-original.png]]

### 原文第300页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=300|p.300]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0300-original.png]]

### 原文第303页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=303|p.303]]

- Figure B-21: AArch64_actlr_el2 bit assignments
- Table B-66: ACTLR_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0303-original.png]]

### 原文第304页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=304|p.304]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0304-original.png]]

### 原文第306页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=306|p.306]]

- Figure B-22: AArch64_hacr_el2 bit assignments
- Table B-69: HACR_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0306-original.png]]

### 原文第307页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=307|p.307]]

- Figure B-23: AArch64_afsr0_el2 bit assignments
- Table B-72: AFSR0_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0307-original.png]]

### 原文第310页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=310|p.310]]

- Figure B-24: AArch64_afsr1_el2 bit assignments
- Table B-77: AFSR1_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0310-original.png]]

### 原文第313页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=313|p.313]]

- Figure B-25: AArch64_amair_el2 bit assignments
- Table B-82: AMAIR_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0313-original.png]]

### 原文第315页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=315|p.315]]

- Figure B-26: AArch64_imp_atcr_el2 bit assignments
- Table B-87: IMP_ATCR_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0315-original.png]]

### 原文第316页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=316|p.316]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0316-original.png]]

### 原文第318页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=318|p.318]]

- Figure B-27: AArch64_imp_avtcr_el2 bit assignments
- Table B-90: IMP_AVTCR_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0318-original.png]]

### 原文第320页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=320|p.320]]

- Figure B-28: AArch64_actlr_el3 bit assignments
- Table B-93: ACTLR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0320-original.png]]

### 原文第321页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=321|p.321]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0321-original.png]]

### 原文第323页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=323|p.323]]

- Figure B-29: AArch64_afsr0_el3 bit assignments
- Table B-96: AFSR0_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0323-original.png]]

### 原文第324页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=324|p.324]]

- Figure B-30: AArch64_afsr1_el3 bit assignments
- Table B-99: AFSR1_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0324-original.png]]

### 原文第326页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=326|p.326]]

- Figure B-31: AArch64_amair_el3 bit assignments
- Table B-102: AMAIR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0326-original.png]]

### 原文第328页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=328|p.328]]

- Figure B-32: AArch64_rmr_el3 bit assignments
- Table B-105: RMR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0328-original.png]]

### 原文第329页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=329|p.329]]

- Figure B-33: AArch64_imp_cpuppmcr_el3 bit assignments
- Table B-108: IMP_CPUPPMCR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0329-original.png]]

### 原文第331页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=331|p.331]]

- Figure B-34: AArch64_imp_cpuppmcr2_el3 bit assignments
- Table B-111: IMP_CPUPPMCR2_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0331-original.png]]

### 原文第332页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=332|p.332]]

- Figure B-35: AArch64_imp_cpuppmcr4_el3 bit assignments
- Table B-114: IMP_CPUPPMCR4_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0332-original.png]]

### 原文第334页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=334|p.334]]

- Figure B-36: AArch64_imp_cpuppmcr5_el3 bit assignments
- Table B-117: IMP_CPUPPMCR5_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0334-original.png]]

### 原文第335页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=335|p.335]]

- Figure B-37: AArch64_imp_cpuppmcr6_el3 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0335-original.png]]

### 原文第336页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=336|p.336]]

- Table B-120: IMP_CPUPPMCR6_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0336-original.png]]

### 原文第337页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=337|p.337]]

- Figure B-38: AArch64_imp_cpuactlr_el3 bit assignments
- Table B-123: IMP_CPUACTLR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0337-original.png]]

### 原文第339页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=339|p.339]]

- Figure B-39: AArch64_imp_atcr_el3 bit assignments
- Table B-126: IMP_ATCR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0339-original.png]]

### 原文第341页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=341|p.341]]

- Figure B-40: AArch64_imp_cpupselr_el3 bit assignments
- Table B-129: IMP_CPUPSELR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0341-original.png]]

### 原文第342页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=342|p.342]]

- Figure B-41: AArch64_imp_cpupcr_el3 bit assignments
- Table B-132: IMP_CPUPCR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0342-original.png]]

### 原文第344页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=344|p.344]]

- Figure B-42: AArch64_imp_cpupor_el3 bit assignments
- Table B-135: IMP_CPUPOR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0344-original.png]]

### 原文第345页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=345|p.345]]

- Figure B-43: AArch64_imp_cpupmr_el3 bit assignments
- Table B-138: IMP_CPUPMR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0345-original.png]]

### 原文第347页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=347|p.347]]

- Figure B-44: AArch64_imp_cpupor2_el3 bit assignments
- Table B-141: IMP_CPUPOR2_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0347-original.png]]

### 原文第348页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=348|p.348]]

- Figure B-45: AArch64_imp_cpupmr2_el3 bit assignments
- Table B-144: IMP_CPUPMR2_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0348-original.png]]

### 原文第350页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=350|p.350]]

- Figure B-46: AArch64_imp_cpupfr_el3 bit assignments
- Table B-147: IMP_CPUPFR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0350-original.png]]

### 原文第351页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=351|p.351]]

- Table B-150: Debug registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0351-original.png]]

### 原文第352页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=352|p.352]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0352-original.png]]

### 原文第353页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=353|p.353]]

- Figure B-47: AArch64_dbgbvr0_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0353-original.png]]

### 原文第354页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=354|p.354]]

- Table B-151: DBGBVR0_EL1 bit descriptions
- Figure B-48: AArch64_dbgbvr0_el1 bit assignments
- Table B-152: DBGBVR0_EL1 bit descriptions
- Figure B-49: AArch64_dbgbvr0_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0354-original.png]]

### 原文第355页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=355|p.355]]

- Table B-153: DBGBVR0_EL1 bit descriptions
- Figure B-50: AArch64_dbgbvr0_el1 bit assignments
- Table B-154: DBGBVR0_EL1 bit descriptions
- Figure B-51: AArch64_dbgbvr0_el1 bit assignments
- Table B-155: DBGBVR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0355-original.png]]

### 原文第356页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=356|p.356]]

- Figure B-52: AArch64_dbgbvr0_el1 bit assignments
- Table B-156: DBGBVR0_EL1 bit descriptions
- Figure B-53: AArch64_dbgbvr0_el1 bit assignments
- Table B-157: DBGBVR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0356-original.png]]

### 原文第358页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=358|p.358]]

- Figure B-54: AArch64_dbgbcr0_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0358-original.png]]

### 原文第359页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=359|p.359]]

- Table B-160: DBGBCR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0359-original.png]]

### 原文第360页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=360|p.360]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0360-original.png]]

### 原文第361页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=361|p.361]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0361-original.png]]

### 原文第362页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=362|p.362]]

- Table B-161: BAS description

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0362-original.png]]

### 原文第364页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=364|p.364]]

- Figure B-55: AArch64_dbgwvr0_el1 bit assignments
- Table B-164: DBGWVR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0364-original.png]]

### 原文第366页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=366|p.366]]

- Figure B-56: AArch64_dbgwcr0_el1 bit assignments
- Table B-167: DBGWCR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0366-original.png]]

### 原文第367页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=367|p.367]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0367-original.png]]

### 原文第368页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=368|p.368]]

- Table B-168: BAS description table 1
- Table B-169: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0368-original.png]]

### 原文第371页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=371|p.371]]

- Figure B-57: AArch64_dbgbvr1_el1 bit assignments
- Table B-172: DBGBVR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0371-original.png]]

### 原文第372页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=372|p.372]]

- Figure B-58: AArch64_dbgbvr1_el1 bit assignments
- Table B-173: DBGBVR1_EL1 bit descriptions
- Figure B-59: AArch64_dbgbvr1_el1 bit assignments
- Table B-174: DBGBVR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0372-original.png]]

### 原文第373页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=373|p.373]]

- Figure B-60: AArch64_dbgbvr1_el1 bit assignments
- Table B-175: DBGBVR1_EL1 bit descriptions
- Figure B-61: AArch64_dbgbvr1_el1 bit assignments
- Table B-176: DBGBVR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0373-original.png]]

### 原文第374页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=374|p.374]]

- Figure B-62: AArch64_dbgbvr1_el1 bit assignments
- Table B-177: DBGBVR1_EL1 bit descriptions
- Figure B-63: AArch64_dbgbvr1_el1 bit assignments
- Table B-178: DBGBVR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0374-original.png]]

### 原文第376页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=376|p.376]]

- Figure B-64: AArch64_dbgbcr1_el1 bit assignments
- Table B-181: DBGBCR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0376-original.png]]

### 原文第377页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=377|p.377]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0377-original.png]]

### 原文第378页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=378|p.378]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0378-original.png]]

### 原文第379页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=379|p.379]]

- Table B-182: BAS description

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0379-original.png]]

### 原文第381页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=381|p.381]]

- Figure B-65: AArch64_dbgwvr1_el1 bit assignments
- Table B-185: DBGWVR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0381-original.png]]

### 原文第383页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=383|p.383]]

- Figure B-66: AArch64_dbgwcr1_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0383-original.png]]

### 原文第384页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=384|p.384]]

- Table B-188: DBGWCR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0384-original.png]]

### 原文第385页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=385|p.385]]

- Table B-189: BAS description table 1
- Table B-190: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0385-original.png]]

### 原文第388页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=388|p.388]]

- Figure B-67: AArch64_dbgbvr2_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0388-original.png]]

### 原文第389页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=389|p.389]]

- Table B-193: DBGBVR2_EL1 bit descriptions
- Figure B-68: AArch64_dbgbvr2_el1 bit assignments
- Table B-194: DBGBVR2_EL1 bit descriptions
- Figure B-69: AArch64_dbgbvr2_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0389-original.png]]

### 原文第390页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=390|p.390]]

- Table B-195: DBGBVR2_EL1 bit descriptions
- Figure B-70: AArch64_dbgbvr2_el1 bit assignments
- Table B-196: DBGBVR2_EL1 bit descriptions
- Figure B-71: AArch64_dbgbvr2_el1 bit assignments
- Table B-197: DBGBVR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0390-original.png]]

### 原文第391页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=391|p.391]]

- Figure B-72: AArch64_dbgbvr2_el1 bit assignments
- Table B-198: DBGBVR2_EL1 bit descriptions
- Figure B-73: AArch64_dbgbvr2_el1 bit assignments
- Table B-199: DBGBVR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0391-original.png]]

### 原文第393页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=393|p.393]]

- Figure B-74: AArch64_dbgbcr2_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0393-original.png]]

### 原文第394页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=394|p.394]]

- Table B-202: DBGBCR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0394-original.png]]

### 原文第395页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=395|p.395]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0395-original.png]]

### 原文第396页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=396|p.396]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0396-original.png]]

### 原文第397页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=397|p.397]]

- Table B-203: BAS description

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0397-original.png]]

### 原文第399页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=399|p.399]]

- Figure B-75: AArch64_dbgwvr2_el1 bit assignments
- Table B-206: DBGWVR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0399-original.png]]

### 原文第401页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=401|p.401]]

- Figure B-76: AArch64_dbgwcr2_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0401-original.png]]

### 原文第402页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=402|p.402]]

- Table B-209: DBGWCR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0402-original.png]]

### 原文第403页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=403|p.403]]

- Table B-210: BAS description table 1
- Table B-211: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0403-original.png]]

### 原文第406页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=406|p.406]]

- Figure B-77: AArch64_dbgbvr3_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0406-original.png]]

### 原文第407页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=407|p.407]]

- Table B-214: DBGBVR3_EL1 bit descriptions
- Figure B-78: AArch64_dbgbvr3_el1 bit assignments
- Table B-215: DBGBVR3_EL1 bit descriptions
- Figure B-79: AArch64_dbgbvr3_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0407-original.png]]

### 原文第408页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=408|p.408]]

- Table B-216: DBGBVR3_EL1 bit descriptions
- Figure B-80: AArch64_dbgbvr3_el1 bit assignments
- Table B-217: DBGBVR3_EL1 bit descriptions
- Figure B-81: AArch64_dbgbvr3_el1 bit assignments
- Table B-218: DBGBVR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0408-original.png]]

### 原文第409页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=409|p.409]]

- Figure B-82: AArch64_dbgbvr3_el1 bit assignments
- Table B-219: DBGBVR3_EL1 bit descriptions
- Figure B-83: AArch64_dbgbvr3_el1 bit assignments
- Table B-220: DBGBVR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0409-original.png]]

### 原文第411页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=411|p.411]]

- Figure B-84: AArch64_dbgbcr3_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0411-original.png]]

### 原文第412页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=412|p.412]]

- Table B-223: DBGBCR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0412-original.png]]

### 原文第413页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=413|p.413]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0413-original.png]]

### 原文第414页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=414|p.414]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0414-original.png]]

### 原文第415页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=415|p.415]]

- Table B-224: BAS description

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0415-original.png]]

### 原文第417页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=417|p.417]]

- Figure B-85: AArch64_dbgwvr3_el1 bit assignments
- Table B-227: DBGWVR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0417-original.png]]

### 原文第419页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=419|p.419]]

- Figure B-86: AArch64_dbgwcr3_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0419-original.png]]

### 原文第420页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=420|p.420]]

- Table B-230: DBGWCR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0420-original.png]]

### 原文第421页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=421|p.421]]

- Table B-231: BAS description table 1
- Table B-232: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0421-original.png]]

### 原文第424页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=424|p.424]]

- Figure B-87: AArch64_dbgbvr4_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0424-original.png]]

### 原文第425页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=425|p.425]]

- Table B-235: DBGBVR4_EL1 bit descriptions
- Figure B-88: AArch64_dbgbvr4_el1 bit assignments
- Table B-236: DBGBVR4_EL1 bit descriptions
- Figure B-89: AArch64_dbgbvr4_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0425-original.png]]

### 原文第426页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=426|p.426]]

- Table B-237: DBGBVR4_EL1 bit descriptions
- Figure B-90: AArch64_dbgbvr4_el1 bit assignments
- Table B-238: DBGBVR4_EL1 bit descriptions
- Figure B-91: AArch64_dbgbvr4_el1 bit assignments
- Table B-239: DBGBVR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0426-original.png]]

### 原文第427页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=427|p.427]]

- Figure B-92: AArch64_dbgbvr4_el1 bit assignments
- Table B-240: DBGBVR4_EL1 bit descriptions
- Figure B-93: AArch64_dbgbvr4_el1 bit assignments
- Table B-241: DBGBVR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0427-original.png]]

### 原文第429页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=429|p.429]]

- Figure B-94: AArch64_dbgbcr4_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0429-original.png]]

### 原文第430页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=430|p.430]]

- Table B-244: DBGBCR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0430-original.png]]

### 原文第431页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=431|p.431]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0431-original.png]]

### 原文第432页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=432|p.432]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0432-original.png]]

### 原文第433页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=433|p.433]]

- Table B-245: BAS description

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0433-original.png]]

### 原文第436页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=436|p.436]]

- Figure B-95: AArch64_dbgbvr5_el1 bit assignments
- Table B-248: DBGBVR5_EL1 bit descriptions
- Figure B-96: AArch64_dbgbvr5_el1 bit assignments
- Table B-249: DBGBVR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0436-original.png]]

### 原文第437页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=437|p.437]]

- Figure B-97: AArch64_dbgbvr5_el1 bit assignments
- Table B-250: DBGBVR5_EL1 bit descriptions
- Figure B-98: AArch64_dbgbvr5_el1 bit assignments
- Table B-251: DBGBVR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0437-original.png]]

### 原文第438页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=438|p.438]]

- Figure B-99: AArch64_dbgbvr5_el1 bit assignments
- Table B-252: DBGBVR5_EL1 bit descriptions
- Figure B-100: AArch64_dbgbvr5_el1 bit assignments
- Table B-253: DBGBVR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0438-original.png]]

### 原文第439页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=439|p.439]]

- Figure B-101: AArch64_dbgbvr5_el1 bit assignments
- Table B-254: DBGBVR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0439-original.png]]

### 原文第441页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=441|p.441]]

- Figure B-102: AArch64_dbgbcr5_el1 bit assignments
- Table B-257: DBGBCR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0441-original.png]]

### 原文第442页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=442|p.442]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0442-original.png]]

### 原文第443页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=443|p.443]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0443-original.png]]

### 原文第444页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=444|p.444]]

- Table B-258: BAS description

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0444-original.png]]

### 原文第446页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=446|p.446]]

- Figure B-103: AArch64_imp_idata0_el3 bit assignments
- Table B-261: IMP_IDATA0_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0446-original.png]]

### 原文第447页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=447|p.447]]

- Figure B-104: AArch64_imp_idata1_el3 bit assignments
- Table B-263: IMP_IDATA1_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0447-original.png]]

### 原文第448页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=448|p.448]]

- Figure B-105: AArch64_imp_idata2_el3 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0448-original.png]]

### 原文第449页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=449|p.449]]

- Table B-265: IMP_IDATA2_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0449-original.png]]

### 原文第450页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=450|p.450]]

- Figure B-106: AArch64_imp_ddata0_el3 bit assignments
- Table B-267: IMP_DDATA0_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0450-original.png]]

### 原文第451页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=451|p.451]]

- Figure B-107: AArch64_imp_ddata1_el3 bit assignments
- Table B-269: IMP_DDATA1_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0451-original.png]]

### 原文第452页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=452|p.452]]

- Figure B-108: AArch64_imp_ddata2_el3 bit assignments
- Table B-271: IMP_DDATA2_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0452-original.png]]

### 原文第453页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=453|p.453]]

- Table B-273: Random Number Control registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0453-original.png]]

### 原文第454页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=454|p.454]]

- Figure B-109: AArch64_imp_cpurndbr_el3 bit assignments
- Table B-274: IMP_CPURNDBR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0454-original.png]]

### 原文第455页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=455|p.455]]

- Figure B-110: AArch64_imp_cpurndpeid_el3 bit assignments
- Table B-277: IMP_CPURNDPEID_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0455-original.png]]

### 原文第456页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=456|p.456]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0456-original.png]]

### 原文第457页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=457|p.457]]

- Table B-280: System instructions summary
- Figure B-111: AArch64_sys_imp_ramindex bit assignments
- Table B-281: SYS_IMP_RAMINDEX bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0457-original.png]]

### 原文第458页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=458|p.458]]

- Table B-283: Identification registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0458-original.png]]

### 原文第459页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=459|p.459]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0459-original.png]]

### 原文第460页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=460|p.460]]

- Figure B-112: AArch64_midr_el1 bit assignments
- Table B-284: MIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0460-original.png]]

### 原文第461页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=461|p.461]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0461-original.png]]

### 原文第462页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=462|p.462]]

- Figure B-113: AArch64_mpidr_el1 bit assignments
- Table B-286: MPIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0462-original.png]]

### 原文第464页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=464|p.464]]

- Figure B-114: AArch64_revidr_el1 bit assignments
- Table B-288: REVIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0464-original.png]]

### 原文第465页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=465|p.465]]

- Figure B-115: AArch64_id_pfr0_el1 bit assignments
- Table B-290: ID_PFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0465-original.png]]

### 原文第466页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=466|p.466]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0466-original.png]]

### 原文第467页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=467|p.467]]

- Figure B-116: AArch64_id_pfr1_el1 bit assignments
- Table B-292: ID_PFR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0467-original.png]]

### 原文第468页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=468|p.468]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0468-original.png]]

### 原文第470页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=470|p.470]]

- Figure B-117: AArch64_id_dfr0_el1 bit assignments
- Table B-294: ID_DFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0470-original.png]]

### 原文第471页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=471|p.471]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0471-original.png]]

### 原文第472页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=472|p.472]]

- Figure B-118: AArch64_id_afr0_el1 bit assignments
- Table B-296: ID_AFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0472-original.png]]

### 原文第473页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=473|p.473]]

- Figure B-119: AArch64_id_mmfr0_el1 bit assignments
- Table B-298: ID_MMFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0473-original.png]]

### 原文第474页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=474|p.474]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0474-original.png]]

### 原文第475页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=475|p.475]]

- Figure B-120: AArch64_id_mmfr1_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0475-original.png]]

### 原文第476页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=476|p.476]]

- Table B-300: ID_MMFR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0476-original.png]]

### 原文第478页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=478|p.478]]

- Figure B-121: AArch64_id_mmfr2_el1 bit assignments
- Table B-302: ID_MMFR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0478-original.png]]

### 原文第479页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=479|p.479]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0479-original.png]]

### 原文第480页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=480|p.480]]

- Figure B-122: AArch64_id_mmfr3_el1 bit assignments
- Table B-304: ID_MMFR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0480-original.png]]

### 原文第481页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=481|p.481]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0481-original.png]]

### 原文第482页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=482|p.482]]

- Figure B-123: AArch64_id_isar0_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0482-original.png]]

### 原文第483页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=483|p.483]]

- Table B-306: ID_ISAR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0483-original.png]]

### 原文第484页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=484|p.484]]

- Figure B-124: AArch64_id_isar1_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0484-original.png]]

### 原文第485页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=485|p.485]]

- Table B-308: ID_ISAR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0485-original.png]]

### 原文第487页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=487|p.487]]

- Figure B-125: AArch64_id_isar2_el1 bit assignments
- Table B-310: ID_ISAR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0487-original.png]]

### 原文第488页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=488|p.488]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0488-original.png]]

### 原文第489页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=489|p.489]]

- Figure B-126: AArch64_id_isar3_el1 bit assignments
- Table B-312: ID_ISAR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0489-original.png]]

### 原文第490页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=490|p.490]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0490-original.png]]

### 原文第491页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=491|p.491]]

- Figure B-127: AArch64_id_isar4_el1 bit assignments
- Table B-314: ID_ISAR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0491-original.png]]

### 原文第492页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=492|p.492]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0492-original.png]]

### 原文第493页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=493|p.493]]

- Figure B-128: AArch64_id_isar5_el1 bit assignments
- Table B-316: ID_ISAR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0493-original.png]]

### 原文第494页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=494|p.494]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0494-original.png]]

### 原文第496页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=496|p.496]]

- Figure B-129: AArch64_id_mmfr4_el1 bit assignments
- Table B-318: ID_MMFR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0496-original.png]]

### 原文第497页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=497|p.497]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0497-original.png]]

### 原文第498页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=498|p.498]]

- Figure B-130: AArch64_id_isar6_el1 bit assignments
- Table B-320: ID_ISAR6_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0498-original.png]]

### 原文第499页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=499|p.499]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0499-original.png]]

### 原文第500页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=500|p.500]]

- Figure B-131: AArch64_mvfr0_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0500-original.png]]

### 原文第501页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=501|p.501]]

- Table B-322: MVFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0501-original.png]]

### 原文第503页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=503|p.503]]

- Figure B-132: AArch64_mvfr1_el1 bit assignments
- Table B-324: MVFR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0503-original.png]]

### 原文第504页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=504|p.504]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0504-original.png]]

### 原文第505页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=505|p.505]]

- Figure B-133: AArch64_mvfr2_el1 bit assignments
- Table B-326: MVFR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0505-original.png]]

### 原文第507页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=507|p.507]]

- Figure B-134: AArch64_id_pfr2_el1 bit assignments
- Table B-328: ID_PFR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0507-original.png]]

### 原文第508页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=508|p.508]]

- Figure B-135: AArch64_id_dfr1_el1 bit assignments
- Table B-330: ID_DFR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0508-original.png]]

### 原文第510页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=510|p.510]]

- Figure B-136: AArch64_id_mmfr5_el1 bit assignments
- Table B-332: ID_MMFR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0510-original.png]]

### 原文第511页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=511|p.511]]

- Figure B-137: AArch64_id_aa64pfr0_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0511-original.png]]

### 原文第512页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=512|p.512]]

- Table B-334: ID_AA64PFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0512-original.png]]

### 原文第513页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=513|p.513]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0513-original.png]]

### 原文第514页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=514|p.514]]

- Figure B-138: AArch64_id_aa64pfr1_el1 bit assignments
- Table B-336: ID_AA64PFR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0514-original.png]]

### 原文第515页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=515|p.515]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0515-original.png]]

### 原文第516页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=516|p.516]]

- Figure B-139: AArch64_id_aa64pfr2_el1 bit assignments
- Table B-338: ID_AA64PFR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0516-original.png]]

### 原文第518页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=518|p.518]]

- Figure B-140: AArch64_id_aa64zfr0_el1 bit assignments
- Table B-340: ID_AA64ZFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0518-original.png]]

### 原文第519页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=519|p.519]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0519-original.png]]

### 原文第520页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=520|p.520]]

- Figure B-141: AArch64_id_aa64dfr0_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0520-original.png]]

### 原文第521页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=521|p.521]]

- Table B-342: ID_AA64DFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0521-original.png]]

### 原文第523页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=523|p.523]]

- Figure B-142: AArch64_id_aa64dfr1_el1 bit assignments
- Table B-344: ID_AA64DFR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0523-original.png]]

### 原文第524页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=524|p.524]]

- Figure B-143: AArch64_id_aa64afr0_el1 bit assignments
- Table B-346: ID_AA64AFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0524-original.png]]

### 原文第525页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=525|p.525]]

- Figure B-144: AArch64_id_aa64afr1_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0525-original.png]]

### 原文第526页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=526|p.526]]

- Table B-348: ID_AA64AFR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0526-original.png]]

### 原文第527页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=527|p.527]]

- Figure B-145: AArch64_id_aa64isar0_el1 bit assignments
- Table B-350: ID_AA64ISAR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0527-original.png]]

### 原文第528页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=528|p.528]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0528-original.png]]

### 原文第529页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=529|p.529]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0529-original.png]]

### 原文第531页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=531|p.531]]

- Figure B-146: AArch64_id_aa64isar1_el1 bit assignments
- Table B-352: ID_AA64ISAR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0531-original.png]]

### 原文第532页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=532|p.532]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0532-original.png]]

### 原文第534页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=534|p.534]]

- Figure B-147: AArch64_id_aa64isar2_el1 bit assignments
- Table B-354: ID_AA64ISAR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0534-original.png]]

### 原文第535页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=535|p.535]]

- Figure B-148: AArch64_id_aa64mmfr0_el1 bit assignments
- Table B-356: ID_AA64MMFR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0535-original.png]]

### 原文第536页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=536|p.536]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0536-original.png]]

### 原文第538页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=538|p.538]]

- Figure B-149: AArch64_id_aa64mmfr1_el1 bit assignments
- Table B-358: ID_AA64MMFR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0538-original.png]]

### 原文第539页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=539|p.539]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0539-original.png]]

### 原文第541页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=541|p.541]]

- Figure B-150: AArch64_id_aa64mmfr2_el1 bit assignments
- Table B-360: ID_AA64MMFR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0541-original.png]]

### 原文第542页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=542|p.542]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0542-original.png]]

### 原文第543页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=543|p.543]]

- Figure B-151: AArch64_mpamidr_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0543-original.png]]

### 原文第544页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=544|p.544]]

- Table B-362: MPAMIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0544-original.png]]

### 原文第545页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=545|p.545]]

- Figure B-152: AArch64_imp_cpucfr_el1 bit assignments
- Table B-364: IMP_CPUCFR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0545-original.png]]

### 原文第546页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=546|p.546]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0546-original.png]]

### 原文第547页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=547|p.547]]

- Figure B-153: AArch64_clidr_el1 bit assignments
- Table B-366: CLIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0547-original.png]]

### 原文第548页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=548|p.548]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0548-original.png]]

### 原文第549页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=549|p.549]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0549-original.png]]

### 原文第550页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=550|p.550]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0550-original.png]]

### 原文第551页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=551|p.551]]

- Figure B-154: AArch64_gmid_el1 bit assignments
- Table B-368: GMID_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0551-original.png]]

### 原文第552页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=552|p.552]]

- Figure B-155: AArch64_ctr_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0552-original.png]]

### 原文第553页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=553|p.553]]

- Table B-370: CTR_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0553-original.png]]

### 原文第555页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=555|p.555]]

- Figure B-156: AArch64_dczid_el0 bit assignments
- Table B-372: DCZID_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0555-original.png]]

### 原文第556页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=556|p.556]]

- Table B-374: Special-purpose registers summary
- Table B-375: Performance Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0556-original.png]]

### 原文第557页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=557|p.557]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0557-original.png]]

### 原文第558页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=558|p.558]]

- Figure B-157: AArch64_pmmir_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0558-original.png]]

### 原文第559页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=559|p.559]]

- Table B-376: PMMIR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0559-original.png]]

### 原文第560页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=560|p.560]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0560-original.png]]

### 原文第561页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=561|p.561]]

- Figure B-158: AArch64_pmcr_el0 bit assignments
- Table B-378: PMCR_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0561-original.png]]

### 原文第562页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=562|p.562]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0562-original.png]]

### 原文第563页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=563|p.563]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0563-original.png]]

### 原文第564页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=564|p.564]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0564-original.png]]

### 原文第567页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=567|p.567]]

- Figure B-159: AArch64_pmceid0_el0 bit assignments
- Table B-381: PMCEID0_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0567-original.png]]

### 原文第568页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=568|p.568]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0568-original.png]]

### 原文第569页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=569|p.569]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0569-original.png]]

### 原文第570页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=570|p.570]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0570-original.png]]

### 原文第571页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=571|p.571]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0571-original.png]]

### 原文第572页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=572|p.572]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0572-original.png]]

### 原文第574页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=574|p.574]]

- Figure B-160: AArch64_pmceid1_el0 bit assignments
- Table B-383: PMCEID1_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0574-original.png]]

### 原文第575页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=575|p.575]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0575-original.png]]

### 原文第576页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=576|p.576]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0576-original.png]]

### 原文第577页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=577|p.577]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0577-original.png]]

### 原文第578页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=578|p.578]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0578-original.png]]

### 原文第579页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=579|p.579]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0579-original.png]]

### 原文第580页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=580|p.580]]

- Figure B-161: AArch64_pmevcntr0_el0 bit assignments
- Table B-385: PMEVCNTR0_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0580-original.png]]

### 原文第584页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=584|p.584]]

- Figure B-162: AArch64_pmevcntr1_el0 bit assignments
- Table B-388: PMEVCNTR1_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0584-original.png]]

### 原文第588页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=588|p.588]]

- Figure B-163: AArch64_pmevcntr2_el0 bit assignments
- Table B-391: PMEVCNTR2_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0588-original.png]]

### 原文第591页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=591|p.591]]

- Figure B-164: AArch64_pmevcntr3_el0 bit assignments
- Table B-394: PMEVCNTR3_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0591-original.png]]

### 原文第595页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=595|p.595]]

- Figure B-165: AArch64_pmevcntr4_el0 bit assignments
- Table B-397: PMEVCNTR4_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0595-original.png]]

### 原文第599页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=599|p.599]]

- Figure B-166: AArch64_pmevcntr5_el0 bit assignments
- Table B-400: PMEVCNTR5_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0599-original.png]]

### 原文第602页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=602|p.602]]

- Figure B-167: AArch64_pmevtyper0_el0 bit assignments
- Table B-403: PMEVTYPER0_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0602-original.png]]

### 原文第603页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=603|p.603]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0603-original.png]]

### 原文第604页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=604|p.604]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0604-original.png]]

### 原文第607页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=607|p.607]]

- Figure B-168: AArch64_pmevtyper1_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0607-original.png]]

### 原文第608页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=608|p.608]]

- Table B-406: PMEVTYPER1_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0608-original.png]]

### 原文第609页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=609|p.609]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0609-original.png]]

### 原文第613页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=613|p.613]]

- Figure B-169: AArch64_pmevtyper2_el0 bit assignments
- Table B-409: PMEVTYPER2_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0613-original.png]]

### 原文第614页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=614|p.614]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0614-original.png]]

### 原文第618页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=618|p.618]]

- Figure B-170: AArch64_pmevtyper3_el0 bit assignments
- Table B-412: PMEVTYPER3_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0618-original.png]]

### 原文第619页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=619|p.619]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0619-original.png]]

### 原文第623页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=623|p.623]]

- Figure B-171: AArch64_pmevtyper4_el0 bit assignments
- Table B-415: PMEVTYPER4_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0623-original.png]]

### 原文第624页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=624|p.624]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0624-original.png]]

### 原文第625页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=625|p.625]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0625-original.png]]

### 原文第628页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=628|p.628]]

- Figure B-172: AArch64_pmevtyper5_el0 bit assignments
- Table B-418: PMEVTYPER5_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0628-original.png]]

### 原文第629页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=629|p.629]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0629-original.png]]

### 原文第630页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=630|p.630]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0630-original.png]]

### 原文第633页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=633|p.633]]

- Table B-421: GIC system registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0633-original.png]]

### 原文第634页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=634|p.634]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0634-original.png]]

### 原文第635页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=635|p.635]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0635-original.png]]

### 原文第636页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=636|p.636]]

- Figure B-173: AArch64_icc_ap0r0_el1 bit assignments
- Table B-422: ICC_AP0R0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0636-original.png]]

### 原文第637页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=637|p.637]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0637-original.png]]

### 原文第638页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=638|p.638]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0638-original.png]]

### 原文第639页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=639|p.639]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0639-original.png]]

### 原文第640页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=640|p.640]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0640-original.png]]

### 原文第641页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=641|p.641]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0641-original.png]]

### 原文第642页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=642|p.642]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0642-original.png]]

### 原文第646页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=646|p.646]]

- Figure B-174: AArch64_icv_ap0r0_el1 bit assignments
- Table B-425: ICV_AP0R0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0646-original.png]]

### 原文第647页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=647|p.647]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0647-original.png]]

### 原文第648页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=648|p.648]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0648-original.png]]

### 原文第649页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=649|p.649]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0649-original.png]]

### 原文第650页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=650|p.650]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0650-original.png]]

### 原文第651页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=651|p.651]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0651-original.png]]

### 原文第652页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=652|p.652]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0652-original.png]]

### 原文第655页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=655|p.655]]

- Figure B-175: AArch64_icc_ap1r0_el1 bit assignments
- Table B-428: ICC_AP1R0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0655-original.png]]

### 原文第656页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=656|p.656]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0656-original.png]]

### 原文第657页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=657|p.657]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0657-original.png]]

### 原文第658页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=658|p.658]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0658-original.png]]

### 原文第659页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=659|p.659]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0659-original.png]]

### 原文第660页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=660|p.660]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0660-original.png]]

### 原文第661页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=661|p.661]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0661-original.png]]

### 原文第662页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=662|p.662]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0662-original.png]]

### 原文第663页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=663|p.663]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0663-original.png]]

### 原文第664页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=664|p.664]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0664-original.png]]

### 原文第665页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=665|p.665]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0665-original.png]]

### 原文第666页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=666|p.666]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0666-original.png]]

### 原文第670页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=670|p.670]]

- Figure B-176: AArch64_icv_ap1r0_el1 bit assignments
- Table B-431: ICV_AP1R0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0670-original.png]]

### 原文第671页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=671|p.671]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0671-original.png]]

### 原文第672页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=672|p.672]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0672-original.png]]

### 原文第673页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=673|p.673]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0673-original.png]]

### 原文第674页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=674|p.674]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0674-original.png]]

### 原文第675页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=675|p.675]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0675-original.png]]

### 原文第676页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=676|p.676]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0676-original.png]]

### 原文第679页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=679|p.679]]

- Figure B-177: AArch64_icc_ctlr_el1 bit assignments
- Table B-434: ICC_CTLR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0679-original.png]]

### 原文第680页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=680|p.680]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0680-original.png]]

### 原文第681页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=681|p.681]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0681-original.png]]

### 原文第684页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=684|p.684]]

- Figure B-178: AArch64_icv_ctlr_el1 bit assignments
- Table B-437: ICV_CTLR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0684-original.png]]

### 原文第685页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=685|p.685]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0685-original.png]]

### 原文第687页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=687|p.687]]

- Figure B-179: AArch64_ich_ap0r0_el2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0687-original.png]]

### 原文第688页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=688|p.688]]

- Table B-440: ICH_AP0R0_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0688-original.png]]

### 原文第689页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=689|p.689]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0689-original.png]]

### 原文第690页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=690|p.690]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0690-original.png]]

### 原文第691页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=691|p.691]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0691-original.png]]

### 原文第692页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=692|p.692]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0692-original.png]]

### 原文第693页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=693|p.693]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0693-original.png]]

### 原文第694页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=694|p.694]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0694-original.png]]

### 原文第695页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=695|p.695]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0695-original.png]]

### 原文第696页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=696|p.696]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0696-original.png]]

### 原文第697页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=697|p.697]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0697-original.png]]

### 原文第698页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=698|p.698]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0698-original.png]]

### 原文第699页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=699|p.699]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0699-original.png]]

### 原文第700页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=700|p.700]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0700-original.png]]

### 原文第701页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=701|p.701]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0701-original.png]]

### 原文第702页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=702|p.702]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0702-original.png]]

### 原文第703页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=703|p.703]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0703-original.png]]

### 原文第704页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=704|p.704]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0704-original.png]]

### 原文第705页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=705|p.705]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0705-original.png]]

### 原文第706页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=706|p.706]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0706-original.png]]

### 原文第707页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=707|p.707]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0707-original.png]]

### 原文第708页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=708|p.708]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0708-original.png]]

### 原文第709页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=709|p.709]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0709-original.png]]

### 原文第710页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=710|p.710]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0710-original.png]]

### 原文第711页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=711|p.711]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0711-original.png]]

### 原文第712页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=712|p.712]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0712-original.png]]

### 原文第713页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=713|p.713]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0713-original.png]]

### 原文第714页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=714|p.714]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0714-original.png]]

### 原文第715页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=715|p.715]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0715-original.png]]

### 原文第716页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=716|p.716]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0716-original.png]]

### 原文第717页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=717|p.717]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0717-original.png]]

### 原文第718页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=718|p.718]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0718-original.png]]

### 原文第719页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=719|p.719]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0719-original.png]]

### 原文第722页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=722|p.722]]

- Figure B-180: AArch64_ich_ap1r0_el2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0722-original.png]]

### 原文第723页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=723|p.723]]

- Table B-443: ICH_AP1R0_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0723-original.png]]

### 原文第724页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=724|p.724]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0724-original.png]]

### 原文第725页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=725|p.725]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0725-original.png]]

### 原文第726页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=726|p.726]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0726-original.png]]

### 原文第727页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=727|p.727]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0727-original.png]]

### 原文第728页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=728|p.728]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0728-original.png]]

### 原文第729页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=729|p.729]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0729-original.png]]

### 原文第730页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=730|p.730]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0730-original.png]]

### 原文第731页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=731|p.731]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0731-original.png]]

### 原文第732页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=732|p.732]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0732-original.png]]

### 原文第733页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=733|p.733]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0733-original.png]]

### 原文第734页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=734|p.734]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0734-original.png]]

### 原文第735页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=735|p.735]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0735-original.png]]

### 原文第736页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=736|p.736]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0736-original.png]]

### 原文第737页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=737|p.737]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0737-original.png]]

### 原文第738页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=738|p.738]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0738-original.png]]

### 原文第739页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=739|p.739]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0739-original.png]]

### 原文第740页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=740|p.740]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0740-original.png]]

### 原文第741页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=741|p.741]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0741-original.png]]

### 原文第742页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=742|p.742]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0742-original.png]]

### 原文第743页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=743|p.743]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0743-original.png]]

### 原文第744页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=744|p.744]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0744-original.png]]

### 原文第745页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=745|p.745]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0745-original.png]]

### 原文第746页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=746|p.746]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0746-original.png]]

### 原文第747页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=747|p.747]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0747-original.png]]

### 原文第748页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=748|p.748]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0748-original.png]]

### 原文第749页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=749|p.749]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0749-original.png]]

### 原文第750页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=750|p.750]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0750-original.png]]

### 原文第751页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=751|p.751]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0751-original.png]]

### 原文第752页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=752|p.752]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0752-original.png]]

### 原文第753页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=753|p.753]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0753-original.png]]

### 原文第754页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=754|p.754]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0754-original.png]]

### 原文第757页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=757|p.757]]

- Figure B-181: AArch64_ich_vtr_el2 bit assignments
- Table B-446: ICH_VTR_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0757-original.png]]

### 原文第758页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=758|p.758]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0758-original.png]]

### 原文第759页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=759|p.759]]

- Figure B-182: AArch64_ich_lr0_el2 bit assignments
- Table B-448: ICH_LR0_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0759-original.png]]

### 原文第760页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=760|p.760]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0760-original.png]]

### 原文第761页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=761|p.761]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0761-original.png]]

### 原文第763页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=763|p.763]]

- Figure B-183: AArch64_ich_lr1_el2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0763-original.png]]

### 原文第764页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=764|p.764]]

- Table B-451: ICH_LR1_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0764-original.png]]

### 原文第765页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=765|p.765]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0765-original.png]]

### 原文第767页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=767|p.767]]

- Figure B-184: AArch64_ich_lr2_el2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0767-original.png]]

### 原文第768页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=768|p.768]]

- Table B-454: ICH_LR2_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0768-original.png]]

### 原文第769页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=769|p.769]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0769-original.png]]

### 原文第771页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=771|p.771]]

- Figure B-185: AArch64_ich_lr3_el2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0771-original.png]]

### 原文第772页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=772|p.772]]

- Table B-457: ICH_LR3_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0772-original.png]]

### 原文第773页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=773|p.773]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0773-original.png]]

### 原文第775页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=775|p.775]]

- Figure B-186: AArch64_icc_ctlr_el3 bit assignments
- Table B-460: ICC_CTLR_EL3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0775-original.png]]

### 原文第776页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=776|p.776]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0776-original.png]]

### 原文第777页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=777|p.777]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0777-original.png]]

### 原文第778页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=778|p.778]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0778-original.png]]

### 原文第779页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=779|p.779]]

- Table B-463: Generic Timer registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0779-original.png]]

### 原文第780页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=780|p.780]]

- Table B-464: Other system control registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0780-original.png]]

### 原文第781页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=781|p.781]]

- Table B-465: Activity Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0781-original.png]]

### 原文第782页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=782|p.782]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0782-original.png]]

### 原文第783页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=783|p.783]]

- Figure B-187: AArch64_amcfgr_el0 bit assignments
- Table B-466: AMCFGR_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0783-original.png]]

### 原文第785页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=785|p.785]]

- Figure B-188: AArch64_amcgcr_el0 bit assignments
- Table B-468: AMCGCR_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0785-original.png]]

### 原文第787页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=787|p.787]]

- Figure B-189: AArch64_amevcntr00_el0 bit assignments
- Table B-470: AMEVCNTR00_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0787-original.png]]

### 原文第789页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=789|p.789]]

- Figure B-190: AArch64_amevcntr01_el0 bit assignments
- Table B-473: AMEVCNTR01_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0789-original.png]]

### 原文第791页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=791|p.791]]

- Figure B-191: AArch64_amevcntr02_el0 bit assignments
- Table B-476: AMEVCNTR02_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0791-original.png]]

### 原文第793页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=793|p.793]]

- Figure B-192: AArch64_amevcntr03_el0 bit assignments
- Table B-479: AMEVCNTR03_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0793-original.png]]

### 原文第795页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=795|p.795]]

- Figure B-193: AArch64_amevtyper00_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0795-original.png]]

### 原文第796页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=796|p.796]]

- Table B-482: AMEVTYPER00_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0796-original.png]]

### 原文第798页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=798|p.798]]

- Figure B-194: AArch64_amevtyper01_el0 bit assignments
- Table B-484: AMEVTYPER01_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0798-original.png]]

### 原文第800页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=800|p.800]]

- Figure B-195: AArch64_amevtyper02_el0 bit assignments
- Table B-486: AMEVTYPER02_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0800-original.png]]

### 原文第802页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=802|p.802]]

- Figure B-196: AArch64_amevtyper03_el0 bit assignments
- Table B-488: AMEVTYPER03_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0802-original.png]]

### 原文第804页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=804|p.804]]

- Figure B-197: AArch64_amevcntr10_el0 bit assignments
- Table B-490: AMEVCNTR10_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0804-original.png]]

### 原文第806页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=806|p.806]]

- Figure B-198: AArch64_amevcntr11_el0 bit assignments
- Table B-493: AMEVCNTR11_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0806-original.png]]

### 原文第808页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=808|p.808]]

- Figure B-199: AArch64_amevcntr12_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0808-original.png]]

### 原文第809页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=809|p.809]]

- Table B-496: AMEVCNTR12_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0809-original.png]]

### 原文第811页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=811|p.811]]

- Figure B-200: AArch64_amevtyper10_el0 bit assignments
- Table B-499: AMEVTYPER10_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0811-original.png]]

### 原文第813页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=813|p.813]]

- Figure B-201: AArch64_amevtyper11_el0 bit assignments
- Table B-501: AMEVTYPER11_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0813-original.png]]

### 原文第815页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=815|p.815]]

- Figure B-202: AArch64_amevtyper12_el0 bit assignments
- Table B-503: AMEVTYPER12_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0815-original.png]]

### 原文第817页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=817|p.817]]

- Table B-505: Trace unit registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0817-original.png]]

### 原文第818页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=818|p.818]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0818-original.png]]

### 原文第819页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=819|p.819]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0819-original.png]]

### 原文第820页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=820|p.820]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0820-original.png]]

### 原文第821页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=821|p.821]]

- Figure B-203: AArch64_trcseqevr0 bit assignments
- Table B-506: TRCSEQEVR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0821-original.png]]

### 原文第822页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=822|p.822]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0822-original.png]]

### 原文第825页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=825|p.825]]

- Figure B-204: AArch64_trcidr8 bit assignments
- Table B-509: TRCIDR8 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0825-original.png]]

### 原文第826页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=826|p.826]]

- Figure B-205: AArch64_trcimspec0 bit assignments
- Table B-511: TRCIMSPEC0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0826-original.png]]

### 原文第829页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=829|p.829]]

- Figure B-206: AArch64_trcseqevr1 bit assignments
- Table B-514: TRCSEQEVR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0829-original.png]]

### 原文第830页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=830|p.830]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0830-original.png]]

### 原文第832页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=832|p.832]]

- Figure B-207: AArch64_trcseqevr2 bit assignments
- Table B-517: TRCSEQEVR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0832-original.png]]

### 原文第833页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=833|p.833]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0833-original.png]]

### 原文第834页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=834|p.834]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0834-original.png]]

### 原文第836页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=836|p.836]]

- Figure B-208: AArch64_trcidr10 bit assignments
- Table B-520: TRCIDR10 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0836-original.png]]

### 原文第837页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=837|p.837]]

- Figure B-209: AArch64_trcidr11 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0837-original.png]]

### 原文第838页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=838|p.838]]

- Table B-522: TRCIDR11 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0838-original.png]]

### 原文第839页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=839|p.839]]

- Figure B-210: AArch64_trccntctlr0 bit assignments
- Table B-524: TRCCNTCTLR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0839-original.png]]

### 原文第840页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=840|p.840]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0840-original.png]]

### 原文第841页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=841|p.841]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0841-original.png]]

### 原文第843页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=843|p.843]]

- Figure B-211: AArch64_trcidr12 bit assignments
- Table B-527: TRCIDR12 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0843-original.png]]

### 原文第845页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=845|p.845]]

- Figure B-212: AArch64_trccntctlr1 bit assignments
- Table B-529: TRCCNTCTLR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0845-original.png]]

### 原文第846页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=846|p.846]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0846-original.png]]

### 原文第848页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=848|p.848]]

- Figure B-213: AArch64_trcidr13 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0848-original.png]]

### 原文第849页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=849|p.849]]

- Table B-532: TRCIDR13 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0849-original.png]]

### 原文第850页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=850|p.850]]

- Figure B-214: AArch64_trcextinselr0 bit assignments
- Table B-534: TRCEXTINSELR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0850-original.png]]

### 原文第851页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=851|p.851]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0851-original.png]]

### 原文第853页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=853|p.853]]

- Figure B-215: AArch64_trccntvr0 bit assignments
- Table B-537: TRCCNTVR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0853-original.png]]

### 原文第856页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=856|p.856]]

- Figure B-216: AArch64_trcidr0 bit assignments
- Table B-540: TRCIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0856-original.png]]

### 原文第857页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=857|p.857]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0857-original.png]]

### 原文第858页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=858|p.858]]

- Figure B-217: AArch64_trcextinselr1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0858-original.png]]

### 原文第859页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=859|p.859]]

- Table B-542: TRCEXTINSELR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0859-original.png]]

### 原文第861页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=861|p.861]]

- Figure B-218: AArch64_trccntvr1 bit assignments
- Table B-545: TRCCNTVR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0861-original.png]]

### 原文第864页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=864|p.864]]

- Figure B-219: AArch64_trcidr1 bit assignments
- Table B-548: TRCIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0864-original.png]]

### 原文第866页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=866|p.866]]

- Figure B-220: AArch64_trcextinselr2 bit assignments
- Table B-550: TRCEXTINSELR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0866-original.png]]

### 原文第869页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=869|p.869]]

- Figure B-221: AArch64_trcidr2 bit assignments
- Table B-553: TRCIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0869-original.png]]

### 原文第871页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=871|p.871]]

- Figure B-222: AArch64_trcextinselr3 bit assignments
- Table B-555: TRCEXTINSELR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0871-original.png]]

### 原文第874页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=874|p.874]]

- Figure B-223: AArch64_trcidr3 bit assignments
- Table B-558: TRCIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0874-original.png]]

### 原文第875页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=875|p.875]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0875-original.png]]

### 原文第876页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=876|p.876]]

- Figure B-224: AArch64_trcidr4 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0876-original.png]]

### 原文第877页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=877|p.877]]

- Table B-560: TRCIDR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0877-original.png]]

### 原文第879页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=879|p.879]]

- Figure B-225: AArch64_trcidr5 bit assignments
- Table B-562: TRCIDR5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0879-original.png]]

### 原文第881页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=881|p.881]]

- Figure B-226: AArch64_trcssccr0 bit assignments
- Table B-564: TRCSSCCR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0881-original.png]]

### 原文第882页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=882|p.882]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0882-original.png]]

### 原文第884页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=884|p.884]]

- Figure B-227: AArch64_trcrsctlr2 bit assignments
- Table B-567: TRCRSCTLR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0884-original.png]]

### 原文第885页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=885|p.885]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0885-original.png]]

### 原文第886页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=886|p.886]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0886-original.png]]

### 原文第887页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=887|p.887]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0887-original.png]]

### 原文第891页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=891|p.891]]

- Figure B-228: AArch64_trcrsctlr3 bit assignments
- Table B-570: TRCRSCTLR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0891-original.png]]

### 原文第892页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=892|p.892]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0892-original.png]]

### 原文第893页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=893|p.893]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0893-original.png]]

### 原文第897页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=897|p.897]]

- Figure B-229: AArch64_trcrsctlr4 bit assignments
- Table B-573: TRCRSCTLR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0897-original.png]]

### 原文第898页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=898|p.898]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0898-original.png]]

### 原文第899页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=899|p.899]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0899-original.png]]

### 原文第900页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=900|p.900]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0900-original.png]]

### 原文第904页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=904|p.904]]

- Figure B-230: AArch64_trcrsctlr5 bit assignments
- Table B-576: TRCRSCTLR5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0904-original.png]]

### 原文第905页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=905|p.905]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0905-original.png]]

### 原文第906页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=906|p.906]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0906-original.png]]

### 原文第910页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=910|p.910]]

- Figure B-231: AArch64_trcrsctlr6 bit assignments
- Table B-579: TRCRSCTLR6 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0910-original.png]]

### 原文第911页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=911|p.911]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0911-original.png]]

### 原文第912页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=912|p.912]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0912-original.png]]

### 原文第913页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=913|p.913]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0913-original.png]]

### 原文第917页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=917|p.917]]

- Figure B-232: AArch64_trcrsctlr7 bit assignments
- Table B-582: TRCRSCTLR7 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0917-original.png]]

### 原文第918页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=918|p.918]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0918-original.png]]

### 原文第919页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=919|p.919]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0919-original.png]]

### 原文第923页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=923|p.923]]

- Figure B-233: AArch64_trcrsctlr8 bit assignments
- Table B-585: TRCRSCTLR8 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0923-original.png]]

### 原文第924页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=924|p.924]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0924-original.png]]

### 原文第925页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=925|p.925]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0925-original.png]]

### 原文第926页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=926|p.926]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0926-original.png]]

### 原文第930页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=930|p.930]]

- Figure B-234: AArch64_trcsscsr0 bit assignments
- Table B-588: TRCSSCSR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0930-original.png]]

### 原文第931页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=931|p.931]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0931-original.png]]

### 原文第932页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=932|p.932]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0932-original.png]]

### 原文第934页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=934|p.934]]

- Figure B-235: AArch64_trcrsctlr9 bit assignments
- Table B-591: TRCRSCTLR9 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0934-original.png]]

### 原文第935页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=935|p.935]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0935-original.png]]

### 原文第936页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=936|p.936]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0936-original.png]]

### 原文第940页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=940|p.940]]

- Figure B-236: AArch64_trcrsctlr10 bit assignments
- Table B-594: TRCRSCTLR10 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0940-original.png]]

### 原文第941页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=941|p.941]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0941-original.png]]

### 原文第942页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=942|p.942]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0942-original.png]]

### 原文第943页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=943|p.943]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0943-original.png]]

### 原文第947页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=947|p.947]]

- Figure B-237: AArch64_trcrsctlr11 bit assignments
- Table B-597: TRCRSCTLR11 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0947-original.png]]

### 原文第948页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=948|p.948]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0948-original.png]]

### 原文第949页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=949|p.949]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0949-original.png]]

### 原文第953页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=953|p.953]]

- Figure B-238: AArch64_trcrsctlr12 bit assignments
- Table B-600: TRCRSCTLR12 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0953-original.png]]

### 原文第954页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=954|p.954]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0954-original.png]]

### 原文第955页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=955|p.955]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0955-original.png]]

### 原文第956页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=956|p.956]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0956-original.png]]

### 原文第960页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=960|p.960]]

- Figure B-239: AArch64_trcrsctlr13 bit assignments
- Table B-603: TRCRSCTLR13 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0960-original.png]]

### 原文第961页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=961|p.961]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0961-original.png]]

### 原文第962页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=962|p.962]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0962-original.png]]

### 原文第966页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=966|p.966]]

- Figure B-240: AArch64_trcrsctlr14 bit assignments
- Table B-606: TRCRSCTLR14 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0966-original.png]]

### 原文第967页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=967|p.967]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0967-original.png]]

### 原文第968页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=968|p.968]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0968-original.png]]

### 原文第969页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=969|p.969]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0969-original.png]]

### 原文第973页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=973|p.973]]

- Figure B-241: AArch64_trcrsctlr15 bit assignments
- Table B-609: TRCRSCTLR15 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0973-original.png]]

### 原文第974页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=974|p.974]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0974-original.png]]

### 原文第975页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=975|p.975]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0975-original.png]]

### 原文第979页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=979|p.979]]

- Figure B-242: AArch64_trcacvr0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0979-original.png]]

### 原文第980页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=980|p.980]]

- Table B-612: TRCACVR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0980-original.png]]

### 原文第983页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=983|p.983]]

- Figure B-243: AArch64_trcacatr0 bit assignments
- Table B-615: TRCACATR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0983-original.png]]

### 原文第984页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=984|p.984]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0984-original.png]]

### 原文第987页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=987|p.987]]

- Figure B-244: AArch64_trcacvr1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0987-original.png]]

### 原文第988页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=988|p.988]]

- Table B-618: TRCACVR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0988-original.png]]

### 原文第991页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=991|p.991]]

- Figure B-245: AArch64_trcacatr1 bit assignments
- Table B-621: TRCACATR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0991-original.png]]

### 原文第992页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=992|p.992]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0992-original.png]]

### 原文第995页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=995|p.995]]

- Figure B-246: AArch64_trcacvr2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0995-original.png]]

### 原文第996页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=996|p.996]]

- Table B-624: TRCACVR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0996-original.png]]

### 原文第999页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=999|p.999]]

- Figure B-247: AArch64_trcacatr2 bit assignments
- Table B-627: TRCACATR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p0999-original.png]]

### 原文第1000页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1000|p.1000]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1000-original.png]]

### 原文第1003页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1003|p.1003]]

- Figure B-248: AArch64_trcacvr3 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1003-original.png]]

### 原文第1004页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1004|p.1004]]

- Table B-630: TRCACVR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1004-original.png]]

### 原文第1007页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1007|p.1007]]

- Figure B-249: AArch64_trcacatr3 bit assignments
- Table B-633: TRCACATR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1007-original.png]]

### 原文第1008页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1008|p.1008]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1008-original.png]]

### 原文第1011页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1011|p.1011]]

- Figure B-250: AArch64_trcacvr4 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1011-original.png]]

### 原文第1012页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1012|p.1012]]

- Table B-636: TRCACVR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1012-original.png]]

### 原文第1015页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1015|p.1015]]

- Figure B-251: AArch64_trcacatr4 bit assignments
- Table B-639: TRCACATR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1015-original.png]]

### 原文第1016页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1016|p.1016]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1016-original.png]]

### 原文第1019页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1019|p.1019]]

- Figure B-252: AArch64_trcacvr5 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1019-original.png]]

### 原文第1020页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1020|p.1020]]

- Table B-642: TRCACVR5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1020-original.png]]

### 原文第1023页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1023|p.1023]]

- Figure B-253: AArch64_trcacatr5 bit assignments
- Table B-645: TRCACATR5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1023-original.png]]

### 原文第1024页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1024|p.1024]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1024-original.png]]

### 原文第1027页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1027|p.1027]]

- Figure B-254: AArch64_trcacvr6 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1027-original.png]]

### 原文第1028页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1028|p.1028]]

- Table B-648: TRCACVR6 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1028-original.png]]

### 原文第1031页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1031|p.1031]]

- Figure B-255: AArch64_trcacatr6 bit assignments
- Table B-651: TRCACATR6 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1031-original.png]]

### 原文第1032页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1032|p.1032]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1032-original.png]]

### 原文第1035页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1035|p.1035]]

- Figure B-256: AArch64_trcacvr7 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1035-original.png]]

### 原文第1036页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1036|p.1036]]

- Table B-654: TRCACVR7 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1036-original.png]]

### 原文第1039页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1039|p.1039]]

- Figure B-257: AArch64_trcacatr7 bit assignments
- Table B-657: TRCACATR7 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1039-original.png]]

### 原文第1040页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1040|p.1040]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1040-original.png]]

### 原文第1043页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1043|p.1043]]

- Figure B-258: AArch64_trccidcvr0 bit assignments
- Table B-660: TRCCIDCVR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1043-original.png]]

### 原文第1046页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1046|p.1046]]

- Figure B-259: AArch64_trcvmidcvr0 bit assignments
- Table B-663: TRCVMIDCVR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1046-original.png]]

### 原文第1048页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1048|p.1048]]

- Table B-666: Memory Partitioning and Monitoring registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1048-original.png]]

### 原文第1049页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1049|p.1049]]

- Figure B-260: AArch64_mpamvpmv_el2 bit assignments
- Table B-667: MPAMVPMV_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1049-original.png]]

### 原文第1050页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1050|p.1050]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1050-original.png]]

### 原文第1052页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1052|p.1052]]

- Figure B-261: AArch64_mpamvpm0_el2 bit assignments
- Table B-670: MPAMVPM0_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1052-original.png]]

### 原文第1054页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1054|p.1054]]

- Figure B-262: AArch64_mpamvpm1_el2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1054-original.png]]

### 原文第1055页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1055|p.1055]]

- Table B-673: MPAMVPM1_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1055-original.png]]

### 原文第1057页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1057|p.1057]]

- Figure B-263: AArch64_mpamvpm2_el2 bit assignments
- Table B-676: MPAMVPM2_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1057-original.png]]

### 原文第1059页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1059|p.1059]]

- Figure B-264: AArch64_mpamvpm3_el2 bit assignments
- Table B-679: MPAMVPM3_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1059-original.png]]

### 原文第1062页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1062|p.1062]]

- Figure B-265: AArch64_mpamvpm4_el2 bit assignments
- Table B-682: MPAMVPM4_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1062-original.png]]

### 原文第1064页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1064|p.1064]]

- Figure B-266: AArch64_mpamvpm5_el2 bit assignments
- Table B-685: MPAMVPM5_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1064-original.png]]

### 原文第1066页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1066|p.1066]]

- Figure B-267: AArch64_mpamvpm6_el2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1066-original.png]]

### 原文第1067页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1067|p.1067]]

- Table B-688: MPAMVPM6_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1067-original.png]]

### 原文第1069页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1069|p.1069]]

- Figure B-268: AArch64_mpamvpm7_el2 bit assignments
- Table B-691: MPAMVPM7_EL2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1069-original.png]]

### 原文第1070页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1070|p.1070]]

- Table B-694: RAS registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1070-original.png]]

### 原文第1071页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1071|p.1071]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1071-original.png]]

### 原文第1072页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1072|p.1072]]

- Figure B-269: AArch64_erridr_el1 bit assignments
- Table B-695: ERRIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1072-original.png]]

### 原文第1073页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1073|p.1073]]

- Figure B-270: AArch64_errselr_el1 bit assignments
- Table B-697: ERRSELR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1073-original.png]]

### 原文第1075页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1075|p.1075]]

- Figure B-271: AArch64_erxfr_el1 bit assignments
- Table B-700: ERXFR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1075-original.png]]

### 原文第1076页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1076|p.1076]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1076-original.png]]

### 原文第1077页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1077|p.1077]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1077-original.png]]

### 原文第1078页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1078|p.1078]]

- Figure B-272: AArch64_erxctlr_el1 bit assignments
- Table B-702: ERXCTLR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1078-original.png]]

### 原文第1079页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1079|p.1079]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1079-original.png]]

### 原文第1080页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1080|p.1080]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1080-original.png]]

### 原文第1082页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1082|p.1082]]

- Figure B-273: AArch64_erxstatus_el1 bit assignments
- Table B-705: ERXSTATUS_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1082-original.png]]

### 原文第1083页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1083|p.1083]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1083-original.png]]

### 原文第1084页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1084|p.1084]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1084-original.png]]

### 原文第1085页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1085|p.1085]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1085-original.png]]

### 原文第1088页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1088|p.1088]]

- Figure B-274: AArch64_erxaddr_el1 bit assignments
- Table B-708: ERXADDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1088-original.png]]

### 原文第1090页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1090|p.1090]]

- Figure B-275: AArch64_erxpfgf_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1090-original.png]]

### 原文第1091页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1091|p.1091]]

- Table B-711: ERXPFGF_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1091-original.png]]

### 原文第1092页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1092|p.1092]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1092-original.png]]

### 原文第1095页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1095|p.1095]]

- Figure B-276: AArch64_erxpfgctl_el1 bit assignments
- Table B-713: ERXPFGCTL_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1095-original.png]]

### 原文第1096页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1096|p.1096]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1096-original.png]]

### 原文第1099页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1099|p.1099]]

- Figure B-277: AArch64_erxpfgcdn_el1 bit assignments
- Table B-716: ERXPFGCDN_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1099-original.png]]

### 原文第1102页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1102|p.1102]]

- Figure B-278: AArch64_erxmisc0_el1 bit assignments
- Table B-719: ERXMISC0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1102-original.png]]

### 原文第1103页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1103|p.1103]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1103-original.png]]

### 原文第1104页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1104|p.1104]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1104-original.png]]

### 原文第1105页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1105|p.1105]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1105-original.png]]

### 原文第1108页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1108|p.1108]]

- Figure B-279: AArch64_erxmisc1_el1 bit assignments
- Table B-722: ERXMISC1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1108-original.png]]

### 原文第1110页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1110|p.1110]]

- Figure B-280: AArch64_erxmisc2_el1 bit assignments
- Table B-725: ERXMISC2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1110-original.png]]

### 原文第1112页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1112|p.1112]]

- Figure B-281: AArch64_erxmisc3_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1112-original.png]]

### 原文第1113页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1113|p.1113]]

- Table B-728: ERXMISC3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1113-original.png]]

### 原文第1114页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1114|p.1114]]

- Table B-731: Statistical Profiling Extension registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1114-original.png]]

### 原文第1115页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1115|p.1115]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1115-original.png]]

### 原文第1116页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1116|p.1116]]

- Figure B-282: AArch64_pmsevfr_el1 bit assignments
- Table B-732: PMSEVFR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1116-original.png]]

### 原文第1117页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1117|p.1117]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1117-original.png]]

### 原文第1118页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1118|p.1118]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1118-original.png]]

### 原文第1119页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1119|p.1119]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1119-original.png]]

### 原文第1120页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1120|p.1120]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1120-original.png]]

### 原文第1121页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1121|p.1121]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1121-original.png]]

### 原文第1122页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1122|p.1122]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1122-original.png]]

### 原文第1123页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1123|p.1123]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1123-original.png]]

### 原文第1124页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1124|p.1124]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1124-original.png]]

### 原文第1125页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1125|p.1125]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1125-original.png]]

### 原文第1126页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1126|p.1126]]

- Figure B-283: AArch64_pmsidr_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1126-original.png]]

### 原文第1127页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1127|p.1127]]

- Table B-735: PMSIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1127-original.png]]

### 原文第1129页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1129|p.1129]]

- Figure B-284: AArch64_pmbidr_el1 bit assignments
- Table B-737: PMBIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1129-original.png]]

### 原文第1130页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1130|p.1130]]

- Table B-739: Trace Buffer Extension registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1130-original.png]]
