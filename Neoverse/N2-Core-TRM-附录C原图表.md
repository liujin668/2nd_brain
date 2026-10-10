---
type: reference
status: reviewed
topics: [Neoverse, N2, CPU, architecture]
aliases: ["N2 附录C原图表"]
tags: [arm, neoverse, cpu, reference]
sources: ["[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf]]"]
source_document: "102099_0003_06_en"
source_revision: "r0p3 / Issue 06"
source_date: 2022-10-27
spec_issue: "CHI E"
source_sections: ["C"]
evidence: source-derived
verification: source-text-and-figure-index-checked
created: 2026-10-09
updated: 2026-10-10
---

# N2 Core TRM 附录C原图表

原文范围 p.1131-1660。本册收录 473 页截图，覆盖该范围的 647 个编号图表标题，以及跨页续表。

入口：[[N2-Core-TRM-完整中文精读]] · [[N2-Core-TRM-寄存器索引]] · [[Neoverse-MOC]]。

> [!info] 使用方式
> 原页保留完整正文宽度、图表、注释及水印，裁去页眉和页脚空白。图表标题保留英文以便和原文对照；续页若没有新标题，会注明“续表或相关原文”。
> 不含图表的普通说明页请用 PDF 页码链接回查。截图不替代正文中的配置、访问条件和编程步骤。

## 编号图表索引

| 编号与原文标题 | 原页 |
|---|---|
| Table C-1: CoreROM registers summary | [[#原文第1131页\|1131]] |
| Figure C-1: ext_corerom_romentry0 bit assignments | [[#原文第1132页\|1132]] |
| Table C-2: COREROM_ROMENTRY0 bit descriptions | [[#原文第1132页\|1132]] |
| Figure C-2: ext_corerom_romentry1 bit assignments | [[#原文第1133页\|1133]] |
| Table C-3: COREROM_ROMENTRY1 bit descriptions | [[#原文第1134页\|1134]] |
| Figure C-3: ext_corerom_romentry2 bit assignments | [[#原文第1135页\|1135]] |
| Table C-4: COREROM_ROMENTRY2 bit descriptions | [[#原文第1135页\|1135]] |
| Figure C-4: ext_corerom_romentry3 bit assignments | [[#原文第1136页\|1136]] |
| Table C-5: COREROM_ROMENTRY3 bit descriptions | [[#原文第1136页\|1136]] |
| Figure C-5: ext_corerom_authstatus bit assignments | [[#原文第1137页\|1137]] |
| Table C-6: COREROM_AUTHSTATUS bit descriptions | [[#原文第1137页\|1137]] |
| Figure C-6: ext_corerom_devarch bit assignments | [[#原文第1139页\|1139]] |
| Table C-7: COREROM_DEVARCH bit descriptions | [[#原文第1139页\|1139]] |
| Figure C-7: ext_corerom_devtype bit assignments | [[#原文第1140页\|1140]] |
| Table C-8: COREROM_DEVTYPE bit descriptions | [[#原文第1140页\|1140]] |
| Figure C-8: ext_corerom_pidr4 bit assignments | [[#原文第1141页\|1141]] |
| Table C-9: COREROM_PIDR4 bit descriptions | [[#原文第1141页\|1141]] |
| Figure C-9: ext_corerom_pidr0 bit assignments | [[#原文第1142页\|1142]] |
| Table C-10: COREROM_PIDR0 bit descriptions | [[#原文第1142页\|1142]] |
| Figure C-10: ext_corerom_pidr1 bit assignments | [[#原文第1143页\|1143]] |
| Table C-11: COREROM_PIDR1 bit descriptions | [[#原文第1143页\|1143]] |
| Figure C-11: ext_corerom_pidr2 bit assignments | [[#原文第1144页\|1144]] |
| Table C-12: COREROM_PIDR2 bit descriptions | [[#原文第1145页\|1145]] |
| Figure C-12: ext_corerom_pidr3 bit assignments | [[#原文第1146页\|1146]] |
| Table C-13: COREROM_PIDR3 bit descriptions | [[#原文第1146页\|1146]] |
| Figure C-13: ext_corerom_cidr0 bit assignments | [[#原文第1147页\|1147]] |
| Table C-14: COREROM_CIDR0 bit descriptions | [[#原文第1147页\|1147]] |
| Figure C-14: ext_corerom_cidr1 bit assignments | [[#原文第1148页\|1148]] |
| Table C-15: COREROM_CIDR1 bit descriptions | [[#原文第1148页\|1148]] |
| Figure C-15: ext_corerom_cidr2 bit assignments | [[#原文第1149页\|1149]] |
| Table C-16: COREROM_CIDR2 bit descriptions | [[#原文第1149页\|1149]] |
| Figure C-16: ext_corerom_cidr3 bit assignments | [[#原文第1150页\|1150]] |
| Table C-17: COREROM_CIDR3 bit descriptions | [[#原文第1150页\|1150]] |
| Table C-18: PPM registers summary | [[#原文第1151页\|1151]] |
| Figure C-17: ext_cpuppmcr bit assignments | [[#原文第1152页\|1152]] |
| Table C-19: CPUPPMCR bit descriptions | [[#原文第1152页\|1152]] |
| Figure C-18: ext_cpuppmcr2 bit assignments | [[#原文第1153页\|1153]] |
| Table C-20: CPUPPMCR2 bit descriptions | [[#原文第1153页\|1153]] |
| Figure C-19: ext_cpuppmcr3 bit assignments | [[#原文第1154页\|1154]] |
| Table C-21: CPUPPMCR3 bit descriptions | [[#原文第1154页\|1154]] |
| Figure C-20: ext_cpuppmcr4 bit assignments | [[#原文第1155页\|1155]] |
| Table C-22: CPUPPMCR4 bit descriptions | [[#原文第1155页\|1155]] |
| Figure C-21: ext_cpuppmcr5 bit assignments | [[#原文第1156页\|1156]] |
| Table C-23: CPUPPMCR5 bit descriptions | [[#原文第1156页\|1156]] |
| Figure C-22: ext_cpuppmcr6 bit assignments | [[#原文第1157页\|1157]] |
| Table C-24: CPUPPMCR6 bit descriptions | [[#原文第1157页\|1157]] |
| Table C-25: Performance Monitors registers summary | [[#原文第1157页\|1157]] |
| Figure C-23: ext_pmevcntr0_el0 bit assignments | [[#原文第1160页\|1160]] |
| Table C-26: PMEVCNTR0_EL0 bit descriptions | [[#原文第1160页\|1160]] |
| Figure C-24: ext_pmevcntr1_el0 bit assignments | [[#原文第1162页\|1162]] |
| Table C-28: PMEVCNTR1_EL0 bit descriptions | [[#原文第1162页\|1162]] |
| Figure C-25: ext_pmevcntr2_el0 bit assignments | [[#原文第1164页\|1164]] |
| Table C-30: PMEVCNTR2_EL0 bit descriptions | [[#原文第1164页\|1164]] |
| Figure C-26: ext_pmevcntr3_el0 bit assignments | [[#原文第1166页\|1166]] |
| Table C-32: PMEVCNTR3_EL0 bit descriptions | [[#原文第1166页\|1166]] |
| Figure C-27: ext_pmevcntr4_el0 bit assignments | [[#原文第1168页\|1168]] |
| Table C-34: PMEVCNTR4_EL0 bit descriptions | [[#原文第1168页\|1168]] |
| Figure C-28: ext_pmevcntr5_el0 bit assignments | [[#原文第1170页\|1170]] |
| Table C-36: PMEVCNTR5_EL0 bit descriptions | [[#原文第1171页\|1171]] |
| Figure C-29: ext_pmccntr_el0 bit assignments | [[#原文第1173页\|1173]] |
| Table C-38: PMCCNTR_EL0 bit descriptions | [[#原文第1173页\|1173]] |
| Figure C-30: ext_pmpcsr bit assignments | [[#原文第1175页\|1175]] |
| Table C-41: PMPCSR bit descriptions | [[#原文第1175页\|1175]] |
| Figure C-31: ext_pmcid1sr bit assignments | [[#原文第1178页\|1178]] |
| Table C-46: PMCID1SR bit descriptions | [[#原文第1179页\|1179]] |
| Figure C-32: ext_pmvidsr bit assignments | [[#原文第1180页\|1180]] |
| Table C-49: PMVIDSR bit descriptions | [[#原文第1180页\|1180]] |
| Figure C-33: ext_pmcid2sr bit assignments | [[#原文第1182页\|1182]] |
| Table C-51: PMCID2SR bit descriptions | [[#原文第1183页\|1183]] |
| Figure C-34: ext_pmevtyper0_el0 bit assignments | [[#原文第1184页\|1184]] |
| Table C-53: PMEVTYPER0_EL0 bit descriptions | [[#原文第1184页\|1184]] |
| Figure C-35: ext_pmevtyper1_el0 bit assignments | [[#原文第1187页\|1187]] |
| Table C-55: PMEVTYPER1_EL0 bit descriptions | [[#原文第1187页\|1187]] |
| Figure C-36: ext_pmevtyper2_el0 bit assignments | [[#原文第1191页\|1191]] |
| Table C-57: PMEVTYPER2_EL0 bit descriptions | [[#原文第1191页\|1191]] |
| Figure C-37: ext_pmevtyper3_el0 bit assignments | [[#原文第1194页\|1194]] |
| Table C-59: PMEVTYPER3_EL0 bit descriptions | [[#原文第1194页\|1194]] |
| Figure C-38: ext_pmevtyper4_el0 bit assignments | [[#原文第1198页\|1198]] |
| Table C-61: PMEVTYPER4_EL0 bit descriptions | [[#原文第1198页\|1198]] |
| Figure C-39: ext_pmevtyper5_el0 bit assignments | [[#原文第1201页\|1201]] |
| Table C-63: PMEVTYPER5_EL0 bit descriptions | [[#原文第1201页\|1201]] |
| Figure C-40: ext_pmccfiltr_el0 bit assignments | [[#原文第1205页\|1205]] |
| Table C-65: PMCCFILTR_EL0 bit descriptions | [[#原文第1205页\|1205]] |
| Figure C-41: ext_pmpcssr bit assignments | [[#原文第1207页\|1207]] |
| Table C-67: PMPCSSR bit descriptions | [[#原文第1208页\|1208]] |
| Figure C-42: ext_pmcidssr bit assignments | [[#原文第1209页\|1209]] |
| Table C-68: PMCIDSSR bit descriptions | [[#原文第1209页\|1209]] |
| Figure C-43: ext_pmsssr bit assignments | [[#原文第1210页\|1210]] |
| Table C-69: PMSSSR bit descriptions | [[#原文第1210页\|1210]] |
| Figure C-44: ext_pmccntsr bit assignments | [[#原文第1211页\|1211]] |
| Table C-70: PMCCNTSR bit descriptions | [[#原文第1211页\|1211]] |
| Figure C-45: ext_pmevcntsr0 bit assignments | [[#原文第1212页\|1212]] |
| Table C-71: PMEVCNTSR0 bit descriptions | [[#原文第1213页\|1213]] |
| Figure C-46: ext_pmevcntsr1 bit assignments | [[#原文第1214页\|1214]] |
| Table C-73: PMEVCNTSR1 bit descriptions | [[#原文第1214页\|1214]] |
| Figure C-47: ext_pmevcntsr2 bit assignments | [[#原文第1215页\|1215]] |
| Table C-75: PMEVCNTSR2 bit descriptions | [[#原文第1215页\|1215]] |
| Figure C-48: ext_pmevcntsr3 bit assignments | [[#原文第1216页\|1216]] |
| Table C-77: PMEVCNTSR3 bit descriptions | [[#原文第1216页\|1216]] |
| Figure C-49: ext_pmevcntsr4 bit assignments | [[#原文第1217页\|1217]] |
| Table C-79: PMEVCNTSR4 bit descriptions | [[#原文第1217页\|1217]] |
| Figure C-50: ext_pmevcntsr5 bit assignments | [[#原文第1218页\|1218]] |
| Table C-81: PMEVCNTSR5 bit descriptions | [[#原文第1218页\|1218]] |
| Figure C-51: ext_pmsscr bit assignments | [[#原文第1219页\|1219]] |
| Table C-83: PMSSCR bit descriptions | [[#原文第1219页\|1219]] |
| Figure C-52: ext_pmcntenset_el0 bit assignments | [[#原文第1220页\|1220]] |
| Table C-84: PMCNTENSET_EL0 bit descriptions | [[#原文第1221页\|1221]] |
| Figure C-53: ext_pmcntenclr_el0 bit assignments | [[#原文第1222页\|1222]] |
| Table C-86: PMCNTENCLR_EL0 bit descriptions | [[#原文第1223页\|1223]] |
| Figure C-54: ext_pmintenset_el1 bit assignments | [[#原文第1224页\|1224]] |
| Table C-88: PMINTENSET_EL1 bit descriptions | [[#原文第1225页\|1225]] |
| Figure C-55: ext_pmintenclr_el1 bit assignments | [[#原文第1226页\|1226]] |
| Table C-90: PMINTENCLR_EL1 bit descriptions | [[#原文第1227页\|1227]] |
| Figure C-56: ext_pmovsclr_el0 bit assignments | [[#原文第1228页\|1228]] |
| Table C-92: PMOVSCLR_EL0 bit descriptions | [[#原文第1229页\|1229]] |
| Figure C-57: ext_pmswinc_el0 bit assignments | [[#原文第1230页\|1230]] |
| Table C-94: PMSWINC_EL0 bit descriptions | [[#原文第1231页\|1231]] |
| Figure C-58: ext_pmovsset_el0 bit assignments | [[#原文第1232页\|1232]] |
| Table C-96: PMOVSSET_EL0 bit descriptions | [[#原文第1232页\|1232]] |
| Figure C-59: ext_pmcfgr bit assignments | [[#原文第1234页\|1234]] |
| Table C-98: PMCFGR bit descriptions | [[#原文第1234页\|1234]] |
| Figure C-60: ext_pmcr_el0 bit assignments | [[#原文第1236页\|1236]] |
| Table C-100: PMCR_EL0 bit descriptions | [[#原文第1236页\|1236]] |
| Figure C-61: ext_pmceid0 bit assignments | [[#原文第1239页\|1239]] |
| Table C-102: PMCEID0 bit descriptions | [[#原文第1239页\|1239]] |
| Figure C-62: ext_pmceid1 bit assignments | [[#原文第1243页\|1243]] |
| Table C-104: PMCEID1 bit descriptions | [[#原文第1243页\|1243]] |
| Figure C-63: ext_pmceid2 bit assignments | [[#原文第1247页\|1247]] |
| Table C-106: PMCEID2 bit descriptions | [[#原文第1247页\|1247]] |
| Figure C-64: ext_pmceid3 bit assignments | [[#原文第1251页\|1251]] |
| Table C-108: PMCEID3 bit descriptions | [[#原文第1251页\|1251]] |
| Figure C-65: ext_pmmir bit assignments | [[#原文第1254页\|1254]] |
| Table C-110: PMMIR bit descriptions | [[#原文第1254页\|1254]] |
| Figure C-66: ext_pmdevaff0 bit assignments | [[#原文第1256页\|1256]] |
| Table C-112: PMDEVAFF0 bit descriptions | [[#原文第1256页\|1256]] |
| Figure C-67: ext_pmdevaff1 bit assignments | [[#原文第1257页\|1257]] |
| Table C-114: PMDEVAFF1 bit descriptions | [[#原文第1257页\|1257]] |
| Figure C-68: ext_pmlar bit assignments | [[#原文第1258页\|1258]] |
| Table C-116: PMLAR bit descriptions | [[#原文第1259页\|1259]] |
| Figure C-69: ext_pmlsr bit assignments | [[#原文第1260页\|1260]] |
| Table C-118: PMLSR bit descriptions | [[#原文第1260页\|1260]] |
| Figure C-70: ext_pmauthstatus bit assignments | [[#原文第1261页\|1261]] |
| Table C-120: PMAUTHSTATUS bit descriptions | [[#原文第1261页\|1261]] |
| Figure C-71: ext_pmdevarch bit assignments | [[#原文第1263页\|1263]] |
| Table C-122: PMDEVARCH bit descriptions | [[#原文第1263页\|1263]] |
| Figure C-72: ext_pmdevid bit assignments | [[#原文第1265页\|1265]] |
| Table C-124: PMDEVID bit descriptions | [[#原文第1265页\|1265]] |
| Figure C-73: ext_pmdevtype bit assignments | [[#原文第1266页\|1266]] |
| Table C-126: PMDEVTYPE bit descriptions | [[#原文第1266页\|1266]] |
| Figure C-74: ext_pmpidr4 bit assignments | [[#原文第1267页\|1267]] |
| Table C-128: PMPIDR4 bit descriptions | [[#原文第1267页\|1267]] |
| Figure C-75: ext_pmpidr0 bit assignments | [[#原文第1269页\|1269]] |
| Table C-130: PMPIDR0 bit descriptions | [[#原文第1269页\|1269]] |
| Figure C-76: ext_pmpidr1 bit assignments | [[#原文第1270页\|1270]] |
| Table C-132: PMPIDR1 bit descriptions | [[#原文第1270页\|1270]] |
| Figure C-77: ext_pmpidr2 bit assignments | [[#原文第1271页\|1271]] |
| Table C-134: PMPIDR2 bit descriptions | [[#原文第1272页\|1272]] |
| Figure C-78: ext_pmpidr3 bit assignments | [[#原文第1273页\|1273]] |
| Table C-136: PMPIDR3 bit descriptions | [[#原文第1273页\|1273]] |
| Figure C-79: ext_pmcidr0 bit assignments | [[#原文第1274页\|1274]] |
| Table C-138: PMCIDR0 bit descriptions | [[#原文第1274页\|1274]] |
| Figure C-80: ext_pmcidr1 bit assignments | [[#原文第1276页\|1276]] |
| Table C-140: PMCIDR1 bit descriptions | [[#原文第1276页\|1276]] |
| Figure C-81: ext_pmcidr2 bit assignments | [[#原文第1277页\|1277]] |
| Table C-142: PMCIDR2 bit descriptions | [[#原文第1277页\|1277]] |
| Figure C-82: ext_pmcidr3 bit assignments | [[#原文第1278页\|1278]] |
| Table C-144: PMCIDR3 bit descriptions | [[#原文第1279页\|1279]] |
| Table C-146: CTI registers summary | [[#原文第1279页\|1279]] |
| Figure C-83: ext_cticontrol bit assignments | [[#原文第1280页\|1280]] |
| Table C-147: CTICONTROL bit descriptions | [[#原文第1281页\|1281]] |
| Figure C-84: ext_ctiintack bit assignments | [[#原文第1282页\|1282]] |
| Table C-149: CTIINTACK bit descriptions | [[#原文第1283页\|1283]] |
| Figure C-85: ext_ctiappset bit assignments | [[#原文第1284页\|1284]] |
| Table C-151: CTIAPPSET bit descriptions | [[#原文第1285页\|1285]] |
| Figure C-86: ext_ctiappclear bit assignments | [[#原文第1286页\|1286]] |
| Table C-153: CTIAPPCLEAR bit descriptions | [[#原文第1286页\|1286]] |
| Figure C-87: ext_ctiapppulse bit assignments | [[#原文第1288页\|1288]] |
| Table C-155: CTIAPPPULSE bit descriptions | [[#原文第1288页\|1288]] |
| Figure C-88: ext_ctiinen_n_ bit assignments | [[#原文第1290页\|1290]] |
| Table C-157: CTIINEN<n> bit descriptions | [[#原文第1290页\|1290]] |
| Figure C-89: ext_ctiouten_n_ bit assignments | [[#原文第1291页\|1291]] |
| Table C-159: CTIOUTEN<n> bit descriptions | [[#原文第1292页\|1292]] |
| Figure C-90: ext_ctitriginstatus bit assignments | [[#原文第1293页\|1293]] |
| Table C-161: CTITRIGINSTATUS bit descriptions | [[#原文第1293页\|1293]] |
| Figure C-91: ext_ctitrigoutstatus bit assignments | [[#原文第1294页\|1294]] |
| Table C-163: CTITRIGOUTSTATUS bit descriptions | [[#原文第1295页\|1295]] |
| Figure C-92: ext_ctichinstatus bit assignments | [[#原文第1296页\|1296]] |
| Table C-165: CTICHINSTATUS bit descriptions | [[#原文第1296页\|1296]] |
| Figure C-93: ext_ctichoutstatus bit assignments | [[#原文第1297页\|1297]] |
| Table C-167: CTICHOUTSTATUS bit descriptions | [[#原文第1298页\|1298]] |
| Figure C-94: ext_ctigate bit assignments | [[#原文第1299页\|1299]] |
| Table C-169: CTIGATE bit descriptions | [[#原文第1299页\|1299]] |
| Figure C-95: ext_asicctl bit assignments | [[#原文第1301页\|1301]] |
| Table C-171: ASICCTL bit descriptions | [[#原文第1301页\|1301]] |
| Figure C-96: ext_ctidevctl bit assignments | [[#原文第1302页\|1302]] |
| Table C-173: CTIDEVCTL bit descriptions | [[#原文第1302页\|1302]] |
| Figure C-97: ext_ctidevaff0 bit assignments | [[#原文第1303页\|1303]] |
| Table C-175: CTIDEVAFF0 bit descriptions | [[#原文第1304页\|1304]] |
| Figure C-98: ext_ctidevaff1 bit assignments | [[#原文第1305页\|1305]] |
| Table C-177: CTIDEVAFF1 bit descriptions | [[#原文第1305页\|1305]] |
| Figure C-99: ext_ctilar bit assignments | [[#原文第1306页\|1306]] |
| Table C-179: CTILAR bit descriptions | [[#原文第1306页\|1306]] |
| Figure C-100: ext_ctilsr bit assignments | [[#原文第1307页\|1307]] |
| Table C-181: CTILSR bit descriptions | [[#原文第1307页\|1307]] |
| Figure C-101: ext_ctiauthstatus bit assignments | [[#原文第1309页\|1309]] |
| Table C-183: CTIAUTHSTATUS bit descriptions | [[#原文第1309页\|1309]] |
| Figure C-102: ext_ctidevarch bit assignments | [[#原文第1310页\|1310]] |
| Table C-185: CTIDEVARCH bit descriptions | [[#原文第1310页\|1310]] |
| Figure C-103: ext_ctidevid2 bit assignments | [[#原文第1312页\|1312]] |
| Table C-187: CTIDEVID2 bit descriptions | [[#原文第1312页\|1312]] |
| Figure C-104: ext_ctidevid1 bit assignments | [[#原文第1313页\|1313]] |
| Table C-189: CTIDEVID1 bit descriptions | [[#原文第1313页\|1313]] |
| Figure C-105: ext_ctidevid bit assignments | [[#原文第1314页\|1314]] |
| Table C-191: CTIDEVID bit descriptions | [[#原文第1314页\|1314]] |
| Table C-193: Debug registers summary | [[#原文第1315页\|1315]] |
| Figure C-106: ext_edesr bit assignments | [[#原文第1317页\|1317]] |
| Table C-194: EDESR bit descriptions | [[#原文第1318页\|1318]] |
| Figure C-107: ext_edecr bit assignments | [[#原文第1319页\|1319]] |
| Table C-196: EDECR bit descriptions | [[#原文第1319页\|1319]] |
| Figure C-108: ext_edwar bit assignments | [[#原文第1321页\|1321]] |
| Table C-198: EDWAR bit descriptions | [[#原文第1321页\|1321]] |
| Figure C-109: ext_dbgdtrrx_el0 bit assignments | [[#原文第1322页\|1322]] |
| Table C-201: DBGDTRRX_EL0 bit descriptions | [[#原文第1323页\|1323]] |
| Figure C-110: ext_editr bit assignments | [[#原文第1324页\|1324]] |
| Table C-203: EDITR bit descriptions | [[#原文第1325页\|1325]] |
| Figure C-111: ext_editr bit assignments | [[#原文第1325页\|1325]] |
| Table C-204: EDITR bit descriptions | [[#原文第1325页\|1325]] |
| Figure C-112: ext_edscr bit assignments | [[#原文第1327页\|1327]] |
| Table C-206: EDSCR bit descriptions | [[#原文第1327页\|1327]] |
| Figure C-113: ext_dbgdtrtx_el0 bit assignments | [[#原文第1333页\|1333]] |
| Table C-208: DBGDTRTX_EL0 bit descriptions | [[#原文第1334页\|1334]] |
| Figure C-114: ext_edrcr bit assignments | [[#原文第1335页\|1335]] |
| Table C-210: EDRCR bit descriptions | [[#原文第1335页\|1335]] |
| Figure C-115: ext_edeccr bit assignments | [[#原文第1337页\|1337]] |
| Table C-212: EDECCR bit descriptions | [[#原文第1337页\|1337]] |
| Figure C-116: ext_oslar_el1 bit assignments | [[#原文第1342页\|1342]] |
| Table C-214: OSLAR_EL1 bit descriptions | [[#原文第1343页\|1343]] |
| Figure C-117: ext_edprcr bit assignments | [[#原文第1344页\|1344]] |
| Table C-216: EDPRCR bit descriptions | [[#原文第1344页\|1344]] |
| Figure C-118: ext_edprsr bit assignments | [[#原文第1347页\|1347]] |
| Table C-218: EDPRSR bit descriptions | [[#原文第1347页\|1347]] |
| Figure C-119: ext_dbgbvr0_el1 bit assignments | [[#原文第1355页\|1355]] |
| Table C-220: DBGBVR0_EL1 bit descriptions | [[#原文第1355页\|1355]] |
| Figure C-120: ext_dbgbvr0_el1 bit assignments | [[#原文第1355页\|1355]] |
| Table C-221: DBGBVR0_EL1 bit descriptions | [[#原文第1355页\|1355]] |
| Figure C-121: ext_dbgbvr0_el1 bit assignments | [[#原文第1356页\|1356]] |
| Table C-222: DBGBVR0_EL1 bit descriptions | [[#原文第1356页\|1356]] |
| Figure C-122: ext_dbgbvr0_el1 bit assignments | [[#原文第1356页\|1356]] |
| Table C-223: DBGBVR0_EL1 bit descriptions | [[#原文第1356页\|1356]] |
| Figure C-123: ext_dbgbvr0_el1 bit assignments | [[#原文第1357页\|1357]] |
| Table C-224: DBGBVR0_EL1 bit descriptions | [[#原文第1357页\|1357]] |
| Figure C-124: ext_dbgbvr0_el1 bit assignments | [[#原文第1357页\|1357]] |
| Table C-225: DBGBVR0_EL1 bit descriptions | [[#原文第1358页\|1358]] |
| Figure C-125: ext_dbgbvr0_el1 bit assignments | [[#原文第1358页\|1358]] |
| Table C-226: DBGBVR0_EL1 bit descriptions | [[#原文第1358页\|1358]] |
| Figure C-126: ext_dbgbcr0_el1 bit assignments | [[#原文第1359页\|1359]] |
| Table C-228: DBGBCR0_EL1 bit descriptions | [[#原文第1359页\|1359]] |
| Table C-229: BAS description table 1 | [[#原文第1362页\|1362]] |
| Table C-230: BAS description table 2 | [[#原文第1362页\|1362]] |
| Figure C-127: ext_dbgbvr1_el1 bit assignments | [[#原文第1364页\|1364]] |
| Table C-232: DBGBVR1_EL1 bit descriptions | [[#原文第1364页\|1364]] |
| Figure C-128: ext_dbgbvr1_el1 bit assignments | [[#原文第1365页\|1365]] |
| Table C-233: DBGBVR1_EL1 bit descriptions | [[#原文第1365页\|1365]] |
| Figure C-129: ext_dbgbvr1_el1 bit assignments | [[#原文第1365页\|1365]] |
| Table C-234: DBGBVR1_EL1 bit descriptions | [[#原文第1365页\|1365]] |
| Figure C-130: ext_dbgbvr1_el1 bit assignments | [[#原文第1365页\|1365]] |
| Table C-235: DBGBVR1_EL1 bit descriptions | [[#原文第1366页\|1366]] |
| Figure C-131: ext_dbgbvr1_el1 bit assignments | [[#原文第1366页\|1366]] |
| Table C-236: DBGBVR1_EL1 bit descriptions | [[#原文第1366页\|1366]] |
| Figure C-132: ext_dbgbvr1_el1 bit assignments | [[#原文第1367页\|1367]] |
| Table C-237: DBGBVR1_EL1 bit descriptions | [[#原文第1367页\|1367]] |
| Figure C-133: ext_dbgbvr1_el1 bit assignments | [[#原文第1367页\|1367]] |
| Table C-238: DBGBVR1_EL1 bit descriptions | [[#原文第1367页\|1367]] |
| Figure C-134: ext_dbgbcr1_el1 bit assignments | [[#原文第1369页\|1369]] |
| Table C-240: DBGBCR1_EL1 bit descriptions | [[#原文第1369页\|1369]] |
| Table C-241: BAS description table 1 | [[#原文第1372页\|1372]] |
| Table C-242: BAS description table 2 | [[#原文第1372页\|1372]] |
| Figure C-135: ext_dbgbvr2_el1 bit assignments | [[#原文第1374页\|1374]] |
| Table C-244: DBGBVR2_EL1 bit descriptions | [[#原文第1374页\|1374]] |
| Figure C-136: ext_dbgbvr2_el1 bit assignments | [[#原文第1375页\|1375]] |
| Table C-245: DBGBVR2_EL1 bit descriptions | [[#原文第1375页\|1375]] |
| Figure C-137: ext_dbgbvr2_el1 bit assignments | [[#原文第1375页\|1375]] |
| Table C-246: DBGBVR2_EL1 bit descriptions | [[#原文第1375页\|1375]] |
| Figure C-138: ext_dbgbvr2_el1 bit assignments | [[#原文第1375页\|1375]] |
| Table C-247: DBGBVR2_EL1 bit descriptions | [[#原文第1376页\|1376]] |
| Figure C-139: ext_dbgbvr2_el1 bit assignments | [[#原文第1376页\|1376]] |
| Table C-248: DBGBVR2_EL1 bit descriptions | [[#原文第1376页\|1376]] |
| Figure C-140: ext_dbgbvr2_el1 bit assignments | [[#原文第1377页\|1377]] |
| Table C-249: DBGBVR2_EL1 bit descriptions | [[#原文第1377页\|1377]] |
| Figure C-141: ext_dbgbvr2_el1 bit assignments | [[#原文第1377页\|1377]] |
| Table C-250: DBGBVR2_EL1 bit descriptions | [[#原文第1377页\|1377]] |
| Figure C-142: ext_dbgbcr2_el1 bit assignments | [[#原文第1379页\|1379]] |
| Table C-252: DBGBCR2_EL1 bit descriptions | [[#原文第1379页\|1379]] |
| Table C-253: BAS description table 1 | [[#原文第1382页\|1382]] |
| Table C-254: BAS description table 2 | [[#原文第1382页\|1382]] |
| Figure C-143: ext_dbgbvr3_el1 bit assignments | [[#原文第1384页\|1384]] |
| Table C-256: DBGBVR3_EL1 bit descriptions | [[#原文第1384页\|1384]] |
| Figure C-144: ext_dbgbvr3_el1 bit assignments | [[#原文第1385页\|1385]] |
| Table C-257: DBGBVR3_EL1 bit descriptions | [[#原文第1385页\|1385]] |
| Figure C-145: ext_dbgbvr3_el1 bit assignments | [[#原文第1385页\|1385]] |
| Table C-258: DBGBVR3_EL1 bit descriptions | [[#原文第1385页\|1385]] |
| Figure C-146: ext_dbgbvr3_el1 bit assignments | [[#原文第1385页\|1385]] |
| Table C-259: DBGBVR3_EL1 bit descriptions | [[#原文第1386页\|1386]] |
| Figure C-147: ext_dbgbvr3_el1 bit assignments | [[#原文第1386页\|1386]] |
| Table C-260: DBGBVR3_EL1 bit descriptions | [[#原文第1386页\|1386]] |
| Figure C-148: ext_dbgbvr3_el1 bit assignments | [[#原文第1387页\|1387]] |
| Table C-261: DBGBVR3_EL1 bit descriptions | [[#原文第1387页\|1387]] |
| Figure C-149: ext_dbgbvr3_el1 bit assignments | [[#原文第1387页\|1387]] |
| Table C-262: DBGBVR3_EL1 bit descriptions | [[#原文第1387页\|1387]] |
| Figure C-150: ext_dbgbcr3_el1 bit assignments | [[#原文第1389页\|1389]] |
| Table C-264: DBGBCR3_EL1 bit descriptions | [[#原文第1389页\|1389]] |
| Table C-265: BAS description table 1 | [[#原文第1392页\|1392]] |
| Table C-266: BAS description table 2 | [[#原文第1392页\|1392]] |
| Figure C-151: ext_dbgbvr4_el1 bit assignments | [[#原文第1394页\|1394]] |
| Table C-268: DBGBVR4_EL1 bit descriptions | [[#原文第1394页\|1394]] |
| Figure C-152: ext_dbgbvr4_el1 bit assignments | [[#原文第1395页\|1395]] |
| Table C-269: DBGBVR4_EL1 bit descriptions | [[#原文第1395页\|1395]] |
| Figure C-153: ext_dbgbvr4_el1 bit assignments | [[#原文第1395页\|1395]] |
| Table C-270: DBGBVR4_EL1 bit descriptions | [[#原文第1395页\|1395]] |
| Figure C-154: ext_dbgbvr4_el1 bit assignments | [[#原文第1395页\|1395]] |
| Table C-271: DBGBVR4_EL1 bit descriptions | [[#原文第1396页\|1396]] |
| Figure C-155: ext_dbgbvr4_el1 bit assignments | [[#原文第1396页\|1396]] |
| Table C-272: DBGBVR4_EL1 bit descriptions | [[#原文第1396页\|1396]] |
| Figure C-156: ext_dbgbvr4_el1 bit assignments | [[#原文第1397页\|1397]] |
| Table C-273: DBGBVR4_EL1 bit descriptions | [[#原文第1397页\|1397]] |
| Figure C-157: ext_dbgbvr4_el1 bit assignments | [[#原文第1397页\|1397]] |
| Table C-274: DBGBVR4_EL1 bit descriptions | [[#原文第1397页\|1397]] |
| Figure C-158: ext_dbgbcr4_el1 bit assignments | [[#原文第1399页\|1399]] |
| Table C-276: DBGBCR4_EL1 bit descriptions | [[#原文第1399页\|1399]] |
| Table C-277: BAS description table 1 | [[#原文第1402页\|1402]] |
| Table C-278: BAS description table 2 | [[#原文第1402页\|1402]] |
| Figure C-159: ext_dbgbvr5_el1 bit assignments | [[#原文第1404页\|1404]] |
| Table C-280: DBGBVR5_EL1 bit descriptions | [[#原文第1404页\|1404]] |
| Figure C-160: ext_dbgbvr5_el1 bit assignments | [[#原文第1405页\|1405]] |
| Table C-281: DBGBVR5_EL1 bit descriptions | [[#原文第1405页\|1405]] |
| Figure C-161: ext_dbgbvr5_el1 bit assignments | [[#原文第1405页\|1405]] |
| Table C-282: DBGBVR5_EL1 bit descriptions | [[#原文第1405页\|1405]] |
| Figure C-162: ext_dbgbvr5_el1 bit assignments | [[#原文第1405页\|1405]] |
| Table C-283: DBGBVR5_EL1 bit descriptions | [[#原文第1406页\|1406]] |
| Figure C-163: ext_dbgbvr5_el1 bit assignments | [[#原文第1406页\|1406]] |
| Table C-284: DBGBVR5_EL1 bit descriptions | [[#原文第1406页\|1406]] |
| Figure C-164: ext_dbgbvr5_el1 bit assignments | [[#原文第1407页\|1407]] |
| Table C-285: DBGBVR5_EL1 bit descriptions | [[#原文第1407页\|1407]] |
| Figure C-165: ext_dbgbvr5_el1 bit assignments | [[#原文第1407页\|1407]] |
| Table C-286: DBGBVR5_EL1 bit descriptions | [[#原文第1407页\|1407]] |
| Figure C-166: ext_dbgbcr5_el1 bit assignments | [[#原文第1409页\|1409]] |
| Table C-288: DBGBCR5_EL1 bit descriptions | [[#原文第1409页\|1409]] |
| Table C-289: BAS description table 1 | [[#原文第1412页\|1412]] |
| Table C-290: BAS description table 2 | [[#原文第1412页\|1412]] |
| Figure C-167: ext_dbgwvr0_el1 bit assignments | [[#原文第1413页\|1413]] |
| Table C-292: DBGWVR0_EL1 bit descriptions | [[#原文第1414页\|1414]] |
| Figure C-168: ext_dbgwcr0_el1 bit assignments | [[#原文第1415页\|1415]] |
| Table C-294: DBGWCR0_EL1 bit descriptions | [[#原文第1415页\|1415]] |
| Table C-295: BAS description table 1 | [[#原文第1417页\|1417]] |
| Table C-296: BAS description table 2 | [[#原文第1417页\|1417]] |
| Figure C-169: ext_dbgwvr1_el1 bit assignments | [[#原文第1419页\|1419]] |
| Table C-298: DBGWVR1_EL1 bit descriptions | [[#原文第1419页\|1419]] |
| Figure C-170: ext_dbgwcr1_el1 bit assignments | [[#原文第1420页\|1420]] |
| Table C-300: DBGWCR1_EL1 bit descriptions | [[#原文第1421页\|1421]] |
| Table C-301: BAS description table 1 | [[#原文第1422页\|1422]] |
| Table C-302: BAS description table 2 | [[#原文第1422页\|1422]] |
| Figure C-171: ext_dbgwvr2_el1 bit assignments | [[#原文第1424页\|1424]] |
| Table C-304: DBGWVR2_EL1 bit descriptions | [[#原文第1424页\|1424]] |
| Figure C-172: ext_dbgwcr2_el1 bit assignments | [[#原文第1426页\|1426]] |
| Table C-306: DBGWCR2_EL1 bit descriptions | [[#原文第1426页\|1426]] |
| Table C-307: BAS description table 1 | [[#原文第1427页\|1427]] |
| Table C-308: BAS description table 2 | [[#原文第1427页\|1427]] |
| Figure C-173: ext_dbgwvr3_el1 bit assignments | [[#原文第1429页\|1429]] |
| Table C-310: DBGWVR3_EL1 bit descriptions | [[#原文第1429页\|1429]] |
| Figure C-174: ext_dbgwcr3_el1 bit assignments | [[#原文第1431页\|1431]] |
| Table C-312: DBGWCR3_EL1 bit descriptions | [[#原文第1431页\|1431]] |
| Table C-313: BAS description table 1 | [[#原文第1432页\|1432]] |
| Table C-314: BAS description table 2 | [[#原文第1432页\|1432]] |
| Figure C-175: ext_midr_el1 bit assignments | [[#原文第1434页\|1434]] |
| Table C-316: MIDR_EL1 bit descriptions | [[#原文第1434页\|1434]] |
| Figure C-176: ext_edpfr bit assignments | [[#原文第1435页\|1435]] |
| Table C-318: EDPFR bit descriptions | [[#原文第1435页\|1435]] |
| Figure C-177: ext_eddfr bit assignments | [[#原文第1438页\|1438]] |
| Table C-321: EDDFR bit descriptions | [[#原文第1438页\|1438]] |
| Figure C-178: ext_edaa32pfr bit assignments | [[#原文第1440页\|1440]] |
| Table C-324: EDAA32PFR bit descriptions | [[#原文第1440页\|1440]] |
| Figure C-179: ext_editctrl bit assignments | [[#原文第1442页\|1442]] |
| Table C-326: EDITCTRL bit descriptions | [[#原文第1442页\|1442]] |
| Figure C-180: ext_dbgclaimset_el1 bit assignments | [[#原文第1443页\|1443]] |
| Table C-328: DBGCLAIMSET_EL1 bit descriptions | [[#原文第1443页\|1443]] |
| Figure C-181: ext_dbgclaimclr_el1 bit assignments | [[#原文第1445页\|1445]] |
| Table C-330: DBGCLAIMCLR_EL1 bit descriptions | [[#原文第1445页\|1445]] |
| Figure C-182: ext_eddevaff0 bit assignments | [[#原文第1446页\|1446]] |
| Table C-332: EDDEVAFF0 bit descriptions | [[#原文第1446页\|1446]] |
| Figure C-183: ext_eddevaff1 bit assignments | [[#原文第1447页\|1447]] |
| Table C-334: EDDEVAFF1 bit descriptions | [[#原文第1448页\|1448]] |
| Figure C-184: ext_edlar bit assignments | [[#原文第1449页\|1449]] |
| Table C-336: EDLAR bit descriptions | [[#原文第1449页\|1449]] |
| Figure C-185: ext_edlsr bit assignments | [[#原文第1450页\|1450]] |
| Table C-338: EDLSR bit descriptions | [[#原文第1450页\|1450]] |
| Figure C-186: ext_dbgauthstatus_el1 bit assignments | [[#原文第1452页\|1452]] |
| Table C-340: DBGAUTHSTATUS_EL1 bit descriptions | [[#原文第1452页\|1452]] |
| Figure C-187: ext_eddevarch bit assignments | [[#原文第1453页\|1453]] |
| Table C-342: EDDEVARCH bit descriptions | [[#原文第1454页\|1454]] |
| Figure C-188: ext_eddevid2 bit assignments | [[#原文第1455页\|1455]] |
| Table C-344: EDDEVID2 bit descriptions | [[#原文第1455页\|1455]] |
| Figure C-189: ext_eddevid1 bit assignments | [[#原文第1456页\|1456]] |
| Table C-346: EDDEVID1 bit descriptions | [[#原文第1456页\|1456]] |
| Figure C-190: ext_eddevid bit assignments | [[#原文第1458页\|1458]] |
| Table C-348: EDDEVID bit descriptions | [[#原文第1458页\|1458]] |
| Figure C-191: ext_eddevtype bit assignments | [[#原文第1459页\|1459]] |
| Table C-350: EDDEVTYPE bit descriptions | [[#原文第1459页\|1459]] |
| Figure C-192: ext_edpidr4 bit assignments | [[#原文第1460页\|1460]] |
| Table C-352: EDPIDR4 bit descriptions | [[#原文第1461页\|1461]] |
| Figure C-193: ext_edpidr0 bit assignments | [[#原文第1462页\|1462]] |
| Table C-354: EDPIDR0 bit descriptions | [[#原文第1462页\|1462]] |
| Figure C-194: ext_edpidr1 bit assignments | [[#原文第1463页\|1463]] |
| Table C-356: EDPIDR1 bit descriptions | [[#原文第1463页\|1463]] |
| Figure C-195: ext_edpidr2 bit assignments | [[#原文第1464页\|1464]] |
| Table C-358: EDPIDR2 bit descriptions | [[#原文第1465页\|1465]] |
| Figure C-196: ext_edpidr3 bit assignments | [[#原文第1466页\|1466]] |
| Table C-360: EDPIDR3 bit descriptions | [[#原文第1466页\|1466]] |
| Figure C-197: ext_edcidr0 bit assignments | [[#原文第1467页\|1467]] |
| Table C-362: EDCIDR0 bit descriptions | [[#原文第1467页\|1467]] |
| Figure C-198: ext_edcidr1 bit assignments | [[#原文第1469页\|1469]] |
| Table C-364: EDCIDR1 bit descriptions | [[#原文第1469页\|1469]] |
| Figure C-199: ext_edcidr2 bit assignments | [[#原文第1470页\|1470]] |
| Table C-366: EDCIDR2 bit descriptions | [[#原文第1470页\|1470]] |
| Figure C-200: ext_edcidr3 bit assignments | [[#原文第1471页\|1471]] |
| Table C-368: EDCIDR3 bit descriptions | [[#原文第1471页\|1471]] |
| Table C-370: Activity Monitors registers summary | [[#原文第1472页\|1472]] |
| Figure C-201: ext_amevcntr00 bit assignments | [[#原文第1474页\|1474]] |
| Table C-371: AMEVCNTR00 bit descriptions | [[#原文第1474页\|1474]] |
| Figure C-202: ext_amevcntr01 bit assignments | [[#原文第1476页\|1476]] |
| Table C-374: AMEVCNTR01 bit descriptions | [[#原文第1476页\|1476]] |
| Figure C-203: ext_amevcntr02 bit assignments | [[#原文第1477页\|1477]] |
| Table C-377: AMEVCNTR02 bit descriptions | [[#原文第1478页\|1478]] |
| Figure C-204: ext_amevcntr03 bit assignments | [[#原文第1479页\|1479]] |
| Table C-380: AMEVCNTR03 bit descriptions | [[#原文第1479页\|1479]] |
| Figure C-205: ext_amevcntr10 bit assignments | [[#原文第1481页\|1481]] |
| Table C-383: AMEVCNTR10 bit descriptions | [[#原文第1481页\|1481]] |
| Figure C-206: ext_amevcntr11 bit assignments | [[#原文第1483页\|1483]] |
| Table C-386: AMEVCNTR11 bit descriptions | [[#原文第1483页\|1483]] |
| Figure C-207: ext_amevcntr12 bit assignments | [[#原文第1484页\|1484]] |
| Table C-389: AMEVCNTR12 bit descriptions | [[#原文第1485页\|1485]] |
| Figure C-208: ext_amevtyper00 bit assignments | [[#原文第1486页\|1486]] |
| Table C-392: AMEVTYPER00 bit descriptions | [[#原文第1486页\|1486]] |
| Figure C-209: ext_amevtyper01 bit assignments | [[#原文第1488页\|1488]] |
| Table C-394: AMEVTYPER01 bit descriptions | [[#原文第1488页\|1488]] |
| Figure C-210: ext_amevtyper02 bit assignments | [[#原文第1490页\|1490]] |
| Table C-396: AMEVTYPER02 bit descriptions | [[#原文第1490页\|1490]] |
| Figure C-211: ext_amevtyper03 bit assignments | [[#原文第1492页\|1492]] |
| Table C-398: AMEVTYPER03 bit descriptions | [[#原文第1492页\|1492]] |
| Figure C-212: ext_amevtyper10 bit assignments | [[#原文第1493页\|1493]] |
| Table C-400: AMEVTYPER10 bit descriptions | [[#原文第1493页\|1493]] |
| Figure C-213: ext_amevtyper11 bit assignments | [[#原文第1495页\|1495]] |
| Table C-402: AMEVTYPER11 bit descriptions | [[#原文第1495页\|1495]] |
| Figure C-214: ext_amevtyper12 bit assignments | [[#原文第1497页\|1497]] |
| Table C-404: AMEVTYPER12 bit descriptions | [[#原文第1497页\|1497]] |
| Figure C-215: ext_amcntenset0 bit assignments | [[#原文第1498页\|1498]] |
| Table C-406: AMCNTENSET0 bit descriptions | [[#原文第1498页\|1498]] |
| Figure C-216: ext_amcntenset1 bit assignments | [[#原文第1500页\|1500]] |
| Table C-408: AMCNTENSET1 bit descriptions | [[#原文第1500页\|1500]] |
| Figure C-217: ext_amcntenclr0 bit assignments | [[#原文第1502页\|1502]] |
| Table C-410: AMCNTENCLR0 bit descriptions | [[#原文第1502页\|1502]] |
| Figure C-218: ext_amcntenclr1 bit assignments | [[#原文第1503页\|1503]] |
| Table C-412: AMCNTENCLR1 bit descriptions | [[#原文第1503页\|1503]] |
| Figure C-219: ext_amcgcr bit assignments | [[#原文第1505页\|1505]] |
| Table C-414: AMCGCR bit descriptions | [[#原文第1505页\|1505]] |
| Figure C-220: ext_amcfgr bit assignments | [[#原文第1506页\|1506]] |
| Table C-416: AMCFGR bit descriptions | [[#原文第1506页\|1506]] |
| Figure C-221: ext_amcr bit assignments | [[#原文第1508页\|1508]] |
| Table C-418: AMCR bit descriptions | [[#原文第1508页\|1508]] |
| Figure C-222: ext_amiidr bit assignments | [[#原文第1509页\|1509]] |
| Table C-420: AMIIDR bit descriptions | [[#原文第1509页\|1509]] |
| Figure C-223: ext_amdevaff0 bit assignments | [[#原文第1511页\|1511]] |
| Table C-422: AMDEVAFF0 bit descriptions | [[#原文第1511页\|1511]] |
| Figure C-224: ext_amdevaff1 bit assignments | [[#原文第1512页\|1512]] |
| Table C-424: AMDEVAFF1 bit descriptions | [[#原文第1512页\|1512]] |
| Figure C-225: ext_amdevarch bit assignments | [[#原文第1513页\|1513]] |
| Table C-426: AMDEVARCH bit descriptions | [[#原文第1513页\|1513]] |
| Figure C-226: ext_amdevtype bit assignments | [[#原文第1514页\|1514]] |
| Table C-428: AMDEVTYPE bit descriptions | [[#原文第1514页\|1514]] |
| Figure C-227: ext_ampidr4 bit assignments | [[#原文第1516页\|1516]] |
| Table C-430: AMPIDR4 bit descriptions | [[#原文第1516页\|1516]] |
| Figure C-228: ext_ampidr0 bit assignments | [[#原文第1517页\|1517]] |
| Table C-432: AMPIDR0 bit descriptions | [[#原文第1517页\|1517]] |
| Figure C-229: ext_ampidr1 bit assignments | [[#原文第1518页\|1518]] |
| Table C-434: AMPIDR1 bit descriptions | [[#原文第1518页\|1518]] |
| Figure C-230: ext_ampidr2 bit assignments | [[#原文第1519页\|1519]] |
| Table C-436: AMPIDR2 bit descriptions | [[#原文第1520页\|1520]] |
| Figure C-231: ext_ampidr3 bit assignments | [[#原文第1521页\|1521]] |
| Table C-438: AMPIDR3 bit descriptions | [[#原文第1521页\|1521]] |
| Figure C-232: ext_amcidr0 bit assignments | [[#原文第1522页\|1522]] |
| Table C-440: AMCIDR0 bit descriptions | [[#原文第1522页\|1522]] |
| Figure C-233: ext_amcidr1 bit assignments | [[#原文第1523页\|1523]] |
| Table C-442: AMCIDR1 bit descriptions | [[#原文第1523页\|1523]] |
| Figure C-234: ext_amcidr2 bit assignments | [[#原文第1525页\|1525]] |
| Table C-444: AMCIDR2 bit descriptions | [[#原文第1525页\|1525]] |
| Figure C-235: ext_amcidr3 bit assignments | [[#原文第1526页\|1526]] |
| Table C-446: AMCIDR3 bit descriptions | [[#原文第1526页\|1526]] |
| Table C-448: Trace unit registers summary | [[#原文第1526页\|1526]] |
| Figure C-236: ext_trcprgctlr bit assignments | [[#原文第1529页\|1529]] |
| Table C-449: TRCPRGCTLR bit descriptions | [[#原文第1529页\|1529]] |
| Figure C-237: ext_trcstatr bit assignments | [[#原文第1530页\|1530]] |
| Table C-451: TRCSTATR bit descriptions | [[#原文第1530页\|1530]] |
| Figure C-238: ext_trcconfigr bit assignments | [[#原文第1532页\|1532]] |
| Table C-453: TRCCONFIGR bit descriptions | [[#原文第1532页\|1532]] |
| Figure C-239: ext_trcauxctlr bit assignments | [[#原文第1534页\|1534]] |
| Table C-455: TRCAUXCTLR bit descriptions | [[#原文第1534页\|1534]] |
| Figure C-240: ext_trceventctl0r bit assignments | [[#原文第1535页\|1535]] |
| Table C-457: TRCEVENTCTL0R bit descriptions | [[#原文第1536页\|1536]] |
| Figure C-241: ext_trceventctl1r bit assignments | [[#原文第1539页\|1539]] |
| Table C-459: TRCEVENTCTL1R bit descriptions | [[#原文第1539页\|1539]] |
| Figure C-242: ext_trcrsr bit assignments | [[#原文第1541页\|1541]] |
| Table C-461: TRCRSR bit descriptions | [[#原文第1541页\|1541]] |
| Figure C-243: ext_trctsctlr bit assignments | [[#原文第1543页\|1543]] |
| Table C-463: TRCTSCTLR bit descriptions | [[#原文第1543页\|1543]] |
| Figure C-244: ext_trcsyncpr bit assignments | [[#原文第1545页\|1545]] |
| Table C-465: TRCSYNCPR bit descriptions | [[#原文第1545页\|1545]] |
| Figure C-245: ext_trcccctlr bit assignments | [[#原文第1547页\|1547]] |
| Table C-467: TRCCCCTLR bit descriptions | [[#原文第1548页\|1548]] |
| Figure C-246: ext_trcbbctlr bit assignments | [[#原文第1549页\|1549]] |
| Table C-469: TRCBBCTLR bit descriptions | [[#原文第1549页\|1549]] |
| Figure C-247: ext_trctraceidr bit assignments | [[#原文第1551页\|1551]] |
| Table C-471: TRCTRACEIDR bit descriptions | [[#原文第1551页\|1551]] |
| Figure C-248: ext_trcvictlr bit assignments | [[#原文第1552页\|1552]] |
| Table C-473: TRCVICTLR bit descriptions | [[#原文第1553页\|1553]] |
| Figure C-249: ext_trcviiectlr bit assignments | [[#原文第1556页\|1556]] |
| Table C-475: TRCVIIECTLR bit descriptions | [[#原文第1556页\|1556]] |
| Figure C-250: ext_trcvissctlr bit assignments | [[#原文第1558页\|1558]] |
| Table C-477: TRCVISSCTLR bit descriptions | [[#原文第1559页\|1559]] |
| Figure C-251: ext_trcseqevr0 bit assignments | [[#原文第1560页\|1560]] |
| Table C-479: TRCSEQEVR0 bit descriptions | [[#原文第1560页\|1560]] |
| Figure C-252: ext_trcseqevr1 bit assignments | [[#原文第1563页\|1563]] |
| Table C-481: TRCSEQEVR1 bit descriptions | [[#原文第1563页\|1563]] |
| Figure C-253: ext_trcseqevr2 bit assignments | [[#原文第1566页\|1566]] |
| Table C-483: TRCSEQEVR2 bit descriptions | [[#原文第1566页\|1566]] |
| Figure C-254: ext_trcseqrstevr bit assignments | [[#原文第1568页\|1568]] |
| Table C-485: TRCSEQRSTEVR bit descriptions | [[#原文第1568页\|1568]] |
| Figure C-255: ext_trcseqstr bit assignments | [[#原文第1570页\|1570]] |
| Table C-487: TRCSEQSTR bit descriptions | [[#原文第1570页\|1570]] |
| Figure C-256: ext_trcextinselr0 bit assignments | [[#原文第1572页\|1572]] |
| Table C-489: TRCEXTINSELR0 bit descriptions | [[#原文第1572页\|1572]] |
| Figure C-257: ext_trcextinselr1 bit assignments | [[#原文第1574页\|1574]] |
| Table C-491: TRCEXTINSELR1 bit descriptions | [[#原文第1574页\|1574]] |
| Figure C-258: ext_trcextinselr2 bit assignments | [[#原文第1576页\|1576]] |
| Table C-493: TRCEXTINSELR2 bit descriptions | [[#原文第1576页\|1576]] |
| Figure C-259: ext_trcextinselr3 bit assignments | [[#原文第1578页\|1578]] |
| Table C-495: TRCEXTINSELR3 bit descriptions | [[#原文第1578页\|1578]] |
| Figure C-260: ext_trccntrldvr0 bit assignments | [[#原文第1580页\|1580]] |
| Table C-497: TRCCNTRLDVR0 bit descriptions | [[#原文第1580页\|1580]] |
| Figure C-261: ext_trccntrldvr1 bit assignments | [[#原文第1582页\|1582]] |
| Table C-499: TRCCNTRLDVR1 bit descriptions | [[#原文第1582页\|1582]] |
| Figure C-262: ext_trccntctlr0 bit assignments | [[#原文第1583页\|1583]] |
| Table C-501: TRCCNTCTLR0 bit descriptions | [[#原文第1583页\|1583]] |
| Figure C-263: ext_trccntctlr1 bit assignments | [[#原文第1586页\|1586]] |
| Table C-503: TRCCNTCTLR1 bit descriptions | [[#原文第1586页\|1586]] |
| Figure C-264: ext_trccntvr0 bit assignments | [[#原文第1589页\|1589]] |
| Table C-505: TRCCNTVR0 bit descriptions | [[#原文第1589页\|1589]] |
| Figure C-265: ext_trccntvr1 bit assignments | [[#原文第1590页\|1590]] |
| Table C-507: TRCCNTVR1 bit descriptions | [[#原文第1591页\|1591]] |
| Figure C-266: ext_trcidr8 bit assignments | [[#原文第1592页\|1592]] |
| Table C-509: TRCIDR8 bit descriptions | [[#原文第1592页\|1592]] |
| Figure C-267: ext_trcidr9 bit assignments | [[#原文第1593页\|1593]] |
| Table C-511: TRCIDR9 bit descriptions | [[#原文第1593页\|1593]] |
| Figure C-268: ext_trcidr10 bit assignments | [[#原文第1594页\|1594]] |
| Table C-513: TRCIDR10 bit descriptions | [[#原文第1594页\|1594]] |
| Figure C-269: ext_trcidr11 bit assignments | [[#原文第1595页\|1595]] |
| Table C-515: TRCIDR11 bit descriptions | [[#原文第1595页\|1595]] |
| Figure C-270: ext_trcidr12 bit assignments | [[#原文第1596页\|1596]] |
| Table C-517: TRCIDR12 bit descriptions | [[#原文第1596页\|1596]] |
| Figure C-271: ext_trcidr13 bit assignments | [[#原文第1597页\|1597]] |
| Table C-519: TRCIDR13 bit descriptions | [[#原文第1598页\|1598]] |
| Figure C-272: ext_trcimspec0 bit assignments | [[#原文第1599页\|1599]] |
| Table C-521: TRCIMSPEC0 bit descriptions | [[#原文第1599页\|1599]] |
| Figure C-273: ext_trcidr0 bit assignments | [[#原文第1600页\|1600]] |
| Table C-523: TRCIDR0 bit descriptions | [[#原文第1600页\|1600]] |
| Figure C-274: ext_trcidr1 bit assignments | [[#原文第1602页\|1602]] |
| Table C-525: TRCIDR1 bit descriptions | [[#原文第1602页\|1602]] |
| Figure C-275: ext_trcidr2 bit assignments | [[#原文第1604页\|1604]] |
| Table C-527: TRCIDR2 bit descriptions | [[#原文第1604页\|1604]] |
| Figure C-276: ext_trcidr3 bit assignments | [[#原文第1605页\|1605]] |
| Table C-529: TRCIDR3 bit descriptions | [[#原文第1606页\|1606]] |
| Figure C-277: ext_trcidr4 bit assignments | [[#原文第1608页\|1608]] |
| Table C-531: TRCIDR4 bit descriptions | [[#原文第1608页\|1608]] |
| Figure C-278: ext_trcidr5 bit assignments | [[#原文第1610页\|1610]] |
| Table C-533: TRCIDR5 bit descriptions | [[#原文第1610页\|1610]] |
| Figure C-279: ext_trcidr6 bit assignments | [[#原文第1611页\|1611]] |
| Table C-535: TRCIDR6 bit descriptions | [[#原文第1611页\|1611]] |
| Figure C-280: ext_trcidr7 bit assignments | [[#原文第1612页\|1612]] |
| Table C-537: TRCIDR7 bit descriptions | [[#原文第1613页\|1613]] |
| Figure C-281: ext_trcsscsr_n_ bit assignments | [[#原文第1614页\|1614]] |
| Table C-539: TRCSSCSR<n> bit descriptions | [[#原文第1614页\|1614]] |
| Figure C-282: ext_trcoslsr bit assignments | [[#原文第1616页\|1616]] |
| Table C-541: TRCOSLSR bit descriptions | [[#原文第1616页\|1616]] |
| Figure C-283: ext_trcpdcr bit assignments | [[#原文第1618页\|1618]] |
| Table C-543: TRCPDCR bit descriptions | [[#原文第1618页\|1618]] |
| Figure C-284: ext_trcpdsr bit assignments | [[#原文第1619页\|1619]] |
| Table C-545: TRCPDSR bit descriptions | [[#原文第1619页\|1619]] |
| Figure C-285: ext_trccidcctlr0 bit assignments | [[#原文第1621页\|1621]] |
| Table C-547: TRCCIDCCTLR0 bit descriptions | [[#原文第1621页\|1621]] |
| Figure C-286: ext_trcvmidcctlr0 bit assignments | [[#原文第1623页\|1623]] |
| Table C-549: TRCVMIDCCTLR0 bit descriptions | [[#原文第1623页\|1623]] |
| Figure C-287: ext_trcitctrl bit assignments | [[#原文第1625页\|1625]] |
| Table C-551: TRCITCTRL bit descriptions | [[#原文第1625页\|1625]] |
| Figure C-288: ext_trcclaimset bit assignments | [[#原文第1627页\|1627]] |
| Table C-553: TRCCLAIMSET bit descriptions | [[#原文第1627页\|1627]] |
| Figure C-289: ext_trcclaimclr bit assignments | [[#原文第1628页\|1628]] |
| Table C-555: TRCCLAIMCLR bit descriptions | [[#原文第1629页\|1629]] |
| Figure C-290: ext_trcdevaff bit assignments | [[#原文第1630页\|1630]] |
| Table C-557: TRCDEVAFF bit descriptions | [[#原文第1630页\|1630]] |
| Figure C-291: ext_trclar bit assignments | [[#原文第1631页\|1631]] |
| Table C-559: TRCLAR bit descriptions | [[#原文第1631页\|1631]] |
| Figure C-292: ext_trclsr bit assignments | [[#原文第1632页\|1632]] |
| Table C-561: TRCLSR bit descriptions | [[#原文第1633页\|1633]] |
| Figure C-293: ext_trcauthstatus bit assignments | [[#原文第1634页\|1634]] |
| Table C-563: TRCAUTHSTATUS bit descriptions | [[#原文第1634页\|1634]] |
| Figure C-294: ext_trcdevarch bit assignments | [[#原文第1637页\|1637]] |
| Table C-565: TRCDEVARCH bit descriptions | [[#原文第1638页\|1638]] |
| Figure C-295: ext_trcdevid2 bit assignments | [[#原文第1639页\|1639]] |
| Table C-567: TRCDEVID2 bit descriptions | [[#原文第1639页\|1639]] |
| Figure C-296: ext_trcdevid1 bit assignments | [[#原文第1640页\|1640]] |
| Table C-569: TRCDEVID1 bit descriptions | [[#原文第1640页\|1640]] |
| Figure C-297: ext_trcdevid bit assignments | [[#原文第1641页\|1641]] |
| Table C-571: TRCDEVID bit descriptions | [[#原文第1642页\|1642]] |
| Figure C-298: ext_trcdevtype bit assignments | [[#原文第1643页\|1643]] |
| Table C-573: TRCDEVTYPE bit descriptions | [[#原文第1643页\|1643]] |
| Figure C-299: ext_trcpidr4 bit assignments | [[#原文第1644页\|1644]] |
| Table C-575: TRCPIDR4 bit descriptions | [[#原文第1644页\|1644]] |
| Figure C-300: ext_trcpidr5 bit assignments | [[#原文第1646页\|1646]] |
| Table C-577: TRCPIDR5 bit descriptions | [[#原文第1646页\|1646]] |
| Figure C-301: ext_trcpidr6 bit assignments | [[#原文第1647页\|1647]] |
| Table C-579: TRCPIDR6 bit descriptions | [[#原文第1647页\|1647]] |
| Figure C-302: ext_trcpidr7 bit assignments | [[#原文第1648页\|1648]] |
| Table C-581: TRCPIDR7 bit descriptions | [[#原文第1649页\|1649]] |
| Figure C-303: ext_trcpidr0 bit assignments | [[#原文第1650页\|1650]] |
| Table C-583: TRCPIDR0 bit descriptions | [[#原文第1650页\|1650]] |
| Figure C-304: ext_trcpidr1 bit assignments | [[#原文第1651页\|1651]] |
| Table C-585: TRCPIDR1 bit descriptions | [[#原文第1651页\|1651]] |
| Figure C-305: ext_trcpidr2 bit assignments | [[#原文第1652页\|1652]] |
| Table C-587: TRCPIDR2 bit descriptions | [[#原文第1653页\|1653]] |
| Figure C-306: ext_trcpidr3 bit assignments | [[#原文第1654页\|1654]] |
| Table C-589: TRCPIDR3 bit descriptions | [[#原文第1654页\|1654]] |
| Figure C-307: ext_trccidr0 bit assignments | [[#原文第1656页\|1656]] |
| Table C-591: TRCCIDR0 bit descriptions | [[#原文第1656页\|1656]] |
| Figure C-308: ext_trccidr1 bit assignments | [[#原文第1657页\|1657]] |
| Table C-593: TRCCIDR1 bit descriptions | [[#原文第1657页\|1657]] |
| Figure C-309: ext_trccidr2 bit assignments | [[#原文第1658页\|1658]] |
| Table C-595: TRCCIDR2 bit descriptions | [[#原文第1659页\|1659]] |
| Figure C-310: ext_trccidr3 bit assignments | [[#原文第1660页\|1660]] |
| Table C-597: TRCCIDR3 bit descriptions | [[#原文第1660页\|1660]] |

## 原页截图

### 原文第1131页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1131|p.1131]]

- Table C-1: CoreROM registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1131-original.png]]

### 原文第1132页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1132|p.1132]]

- Figure C-1: ext_corerom_romentry0 bit assignments
- Table C-2: COREROM_ROMENTRY0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1132-original.png]]

### 原文第1133页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1133|p.1133]]

- Figure C-2: ext_corerom_romentry1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1133-original.png]]

### 原文第1134页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1134|p.1134]]

- Table C-3: COREROM_ROMENTRY1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1134-original.png]]

### 原文第1135页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1135|p.1135]]

- Figure C-3: ext_corerom_romentry2 bit assignments
- Table C-4: COREROM_ROMENTRY2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1135-original.png]]

### 原文第1136页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1136|p.1136]]

- Figure C-4: ext_corerom_romentry3 bit assignments
- Table C-5: COREROM_ROMENTRY3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1136-original.png]]

### 原文第1137页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1137|p.1137]]

- Figure C-5: ext_corerom_authstatus bit assignments
- Table C-6: COREROM_AUTHSTATUS bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1137-original.png]]

### 原文第1138页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1138|p.1138]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1138-original.png]]

### 原文第1139页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1139|p.1139]]

- Figure C-6: ext_corerom_devarch bit assignments
- Table C-7: COREROM_DEVARCH bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1139-original.png]]

### 原文第1140页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1140|p.1140]]

- Figure C-7: ext_corerom_devtype bit assignments
- Table C-8: COREROM_DEVTYPE bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1140-original.png]]

### 原文第1141页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1141|p.1141]]

- Figure C-8: ext_corerom_pidr4 bit assignments
- Table C-9: COREROM_PIDR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1141-original.png]]

### 原文第1142页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1142|p.1142]]

- Figure C-9: ext_corerom_pidr0 bit assignments
- Table C-10: COREROM_PIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1142-original.png]]

### 原文第1143页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1143|p.1143]]

- Figure C-10: ext_corerom_pidr1 bit assignments
- Table C-11: COREROM_PIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1143-original.png]]

### 原文第1144页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1144|p.1144]]

- Figure C-11: ext_corerom_pidr2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1144-original.png]]

### 原文第1145页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1145|p.1145]]

- Table C-12: COREROM_PIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1145-original.png]]

### 原文第1146页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1146|p.1146]]

- Figure C-12: ext_corerom_pidr3 bit assignments
- Table C-13: COREROM_PIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1146-original.png]]

### 原文第1147页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1147|p.1147]]

- Figure C-13: ext_corerom_cidr0 bit assignments
- Table C-14: COREROM_CIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1147-original.png]]

### 原文第1148页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1148|p.1148]]

- Figure C-14: ext_corerom_cidr1 bit assignments
- Table C-15: COREROM_CIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1148-original.png]]

### 原文第1149页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1149|p.1149]]

- Figure C-15: ext_corerom_cidr2 bit assignments
- Table C-16: COREROM_CIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1149-original.png]]

### 原文第1150页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1150|p.1150]]

- Figure C-16: ext_corerom_cidr3 bit assignments
- Table C-17: COREROM_CIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1150-original.png]]

### 原文第1151页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1151|p.1151]]

- Table C-18: PPM registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1151-original.png]]

### 原文第1152页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1152|p.1152]]

- Figure C-17: ext_cpuppmcr bit assignments
- Table C-19: CPUPPMCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1152-original.png]]

### 原文第1153页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1153|p.1153]]

- Figure C-18: ext_cpuppmcr2 bit assignments
- Table C-20: CPUPPMCR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1153-original.png]]

### 原文第1154页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1154|p.1154]]

- Figure C-19: ext_cpuppmcr3 bit assignments
- Table C-21: CPUPPMCR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1154-original.png]]

### 原文第1155页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1155|p.1155]]

- Figure C-20: ext_cpuppmcr4 bit assignments
- Table C-22: CPUPPMCR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1155-original.png]]

### 原文第1156页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1156|p.1156]]

- Figure C-21: ext_cpuppmcr5 bit assignments
- Table C-23: CPUPPMCR5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1156-original.png]]

### 原文第1157页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1157|p.1157]]

- Figure C-22: ext_cpuppmcr6 bit assignments
- Table C-24: CPUPPMCR6 bit descriptions
- Table C-25: Performance Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1157-original.png]]

### 原文第1158页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1158|p.1158]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1158-original.png]]

### 原文第1159页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1159|p.1159]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1159-original.png]]

### 原文第1160页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1160|p.1160]]

- Figure C-23: ext_pmevcntr0_el0 bit assignments
- Table C-26: PMEVCNTR0_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1160-original.png]]

### 原文第1162页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1162|p.1162]]

- Figure C-24: ext_pmevcntr1_el0 bit assignments
- Table C-28: PMEVCNTR1_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1162-original.png]]

### 原文第1164页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1164|p.1164]]

- Figure C-25: ext_pmevcntr2_el0 bit assignments
- Table C-30: PMEVCNTR2_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1164-original.png]]

### 原文第1166页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1166|p.1166]]

- Figure C-26: ext_pmevcntr3_el0 bit assignments
- Table C-32: PMEVCNTR3_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1166-original.png]]

### 原文第1168页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1168|p.1168]]

- Figure C-27: ext_pmevcntr4_el0 bit assignments
- Table C-34: PMEVCNTR4_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1168-original.png]]

### 原文第1170页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1170|p.1170]]

- Figure C-28: ext_pmevcntr5_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1170-original.png]]

### 原文第1171页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1171|p.1171]]

- Table C-36: PMEVCNTR5_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1171-original.png]]

### 原文第1173页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1173|p.1173]]

- Figure C-29: ext_pmccntr_el0 bit assignments
- Table C-38: PMCCNTR_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1173-original.png]]

### 原文第1175页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1175|p.1175]]

- Figure C-30: ext_pmpcsr bit assignments
- Table C-41: PMPCSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1175-original.png]]

### 原文第1176页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1176|p.1176]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1176-original.png]]

### 原文第1178页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1178|p.1178]]

- Figure C-31: ext_pmcid1sr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1178-original.png]]

### 原文第1179页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1179|p.1179]]

- Table C-46: PMCID1SR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1179-original.png]]

### 原文第1180页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1180|p.1180]]

- Figure C-32: ext_pmvidsr bit assignments
- Table C-49: PMVIDSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1180-original.png]]

### 原文第1181页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1181|p.1181]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1181-original.png]]

### 原文第1182页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1182|p.1182]]

- Figure C-33: ext_pmcid2sr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1182-original.png]]

### 原文第1183页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1183|p.1183]]

- Table C-51: PMCID2SR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1183-original.png]]

### 原文第1184页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1184|p.1184]]

- Figure C-34: ext_pmevtyper0_el0 bit assignments
- Table C-53: PMEVTYPER0_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1184-original.png]]

### 原文第1185页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1185|p.1185]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1185-original.png]]

### 原文第1186页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1186|p.1186]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1186-original.png]]

### 原文第1187页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1187|p.1187]]

- Figure C-35: ext_pmevtyper1_el0 bit assignments
- Table C-55: PMEVTYPER1_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1187-original.png]]

### 原文第1188页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1188|p.1188]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1188-original.png]]

### 原文第1189页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1189|p.1189]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1189-original.png]]

### 原文第1191页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1191|p.1191]]

- Figure C-36: ext_pmevtyper2_el0 bit assignments
- Table C-57: PMEVTYPER2_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1191-original.png]]

### 原文第1192页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1192|p.1192]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1192-original.png]]

### 原文第1193页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1193|p.1193]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1193-original.png]]

### 原文第1194页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1194|p.1194]]

- Figure C-37: ext_pmevtyper3_el0 bit assignments
- Table C-59: PMEVTYPER3_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1194-original.png]]

### 原文第1195页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1195|p.1195]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1195-original.png]]

### 原文第1196页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1196|p.1196]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1196-original.png]]

### 原文第1198页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1198|p.1198]]

- Figure C-38: ext_pmevtyper4_el0 bit assignments
- Table C-61: PMEVTYPER4_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1198-original.png]]

### 原文第1199页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1199|p.1199]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1199-original.png]]

### 原文第1200页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1200|p.1200]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1200-original.png]]

### 原文第1201页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1201|p.1201]]

- Figure C-39: ext_pmevtyper5_el0 bit assignments
- Table C-63: PMEVTYPER5_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1201-original.png]]

### 原文第1202页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1202|p.1202]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1202-original.png]]

### 原文第1203页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1203|p.1203]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1203-original.png]]

### 原文第1205页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1205|p.1205]]

- Figure C-40: ext_pmccfiltr_el0 bit assignments
- Table C-65: PMCCFILTR_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1205-original.png]]

### 原文第1206页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1206|p.1206]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1206-original.png]]

### 原文第1207页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1207|p.1207]]

- Figure C-41: ext_pmpcssr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1207-original.png]]

### 原文第1208页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1208|p.1208]]

- Table C-67: PMPCSSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1208-original.png]]

### 原文第1209页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1209|p.1209]]

- Figure C-42: ext_pmcidssr bit assignments
- Table C-68: PMCIDSSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1209-original.png]]

### 原文第1210页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1210|p.1210]]

- Figure C-43: ext_pmsssr bit assignments
- Table C-69: PMSSSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1210-original.png]]

### 原文第1211页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1211|p.1211]]

- Figure C-44: ext_pmccntsr bit assignments
- Table C-70: PMCCNTSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1211-original.png]]

### 原文第1212页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1212|p.1212]]

- Figure C-45: ext_pmevcntsr0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1212-original.png]]

### 原文第1213页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1213|p.1213]]

- Table C-71: PMEVCNTSR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1213-original.png]]

### 原文第1214页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1214|p.1214]]

- Figure C-46: ext_pmevcntsr1 bit assignments
- Table C-73: PMEVCNTSR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1214-original.png]]

### 原文第1215页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1215|p.1215]]

- Figure C-47: ext_pmevcntsr2 bit assignments
- Table C-75: PMEVCNTSR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1215-original.png]]

### 原文第1216页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1216|p.1216]]

- Figure C-48: ext_pmevcntsr3 bit assignments
- Table C-77: PMEVCNTSR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1216-original.png]]

### 原文第1217页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1217|p.1217]]

- Figure C-49: ext_pmevcntsr4 bit assignments
- Table C-79: PMEVCNTSR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1217-original.png]]

### 原文第1218页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1218|p.1218]]

- Figure C-50: ext_pmevcntsr5 bit assignments
- Table C-81: PMEVCNTSR5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1218-original.png]]

### 原文第1219页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1219|p.1219]]

- Figure C-51: ext_pmsscr bit assignments
- Table C-83: PMSSCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1219-original.png]]

### 原文第1220页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1220|p.1220]]

- Figure C-52: ext_pmcntenset_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1220-original.png]]

### 原文第1221页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1221|p.1221]]

- Table C-84: PMCNTENSET_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1221-original.png]]

### 原文第1222页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1222|p.1222]]

- Figure C-53: ext_pmcntenclr_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1222-original.png]]

### 原文第1223页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1223|p.1223]]

- Table C-86: PMCNTENCLR_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1223-original.png]]

### 原文第1224页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1224|p.1224]]

- Figure C-54: ext_pmintenset_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1224-original.png]]

### 原文第1225页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1225|p.1225]]

- Table C-88: PMINTENSET_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1225-original.png]]

### 原文第1226页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1226|p.1226]]

- Figure C-55: ext_pmintenclr_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1226-original.png]]

### 原文第1227页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1227|p.1227]]

- Table C-90: PMINTENCLR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1227-original.png]]

### 原文第1228页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1228|p.1228]]

- Figure C-56: ext_pmovsclr_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1228-original.png]]

### 原文第1229页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1229|p.1229]]

- Table C-92: PMOVSCLR_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1229-original.png]]

### 原文第1230页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1230|p.1230]]

- Figure C-57: ext_pmswinc_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1230-original.png]]

### 原文第1231页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1231|p.1231]]

- Table C-94: PMSWINC_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1231-original.png]]

### 原文第1232页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1232|p.1232]]

- Figure C-58: ext_pmovsset_el0 bit assignments
- Table C-96: PMOVSSET_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1232-original.png]]

### 原文第1233页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1233|p.1233]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1233-original.png]]

### 原文第1234页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1234|p.1234]]

- Figure C-59: ext_pmcfgr bit assignments
- Table C-98: PMCFGR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1234-original.png]]

### 原文第1235页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1235|p.1235]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1235-original.png]]

### 原文第1236页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1236|p.1236]]

- Figure C-60: ext_pmcr_el0 bit assignments
- Table C-100: PMCR_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1236-original.png]]

### 原文第1237页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1237|p.1237]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1237-original.png]]

### 原文第1239页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1239|p.1239]]

- Figure C-61: ext_pmceid0 bit assignments
- Table C-102: PMCEID0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1239-original.png]]

### 原文第1240页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1240|p.1240]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1240-original.png]]

### 原文第1241页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1241|p.1241]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1241-original.png]]

### 原文第1243页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1243|p.1243]]

- Figure C-62: ext_pmceid1 bit assignments
- Table C-104: PMCEID1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1243-original.png]]

### 原文第1244页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1244|p.1244]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1244-original.png]]

### 原文第1245页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1245|p.1245]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1245-original.png]]

### 原文第1247页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1247|p.1247]]

- Figure C-63: ext_pmceid2 bit assignments
- Table C-106: PMCEID2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1247-original.png]]

### 原文第1248页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1248|p.1248]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1248-original.png]]

### 原文第1249页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1249|p.1249]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1249-original.png]]

### 原文第1251页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1251|p.1251]]

- Figure C-64: ext_pmceid3 bit assignments
- Table C-108: PMCEID3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1251-original.png]]

### 原文第1252页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1252|p.1252]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1252-original.png]]

### 原文第1253页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1253|p.1253]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1253-original.png]]

### 原文第1254页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1254|p.1254]]

- Figure C-65: ext_pmmir bit assignments
- Table C-110: PMMIR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1254-original.png]]

### 原文第1255页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1255|p.1255]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1255-original.png]]

### 原文第1256页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1256|p.1256]]

- Figure C-66: ext_pmdevaff0 bit assignments
- Table C-112: PMDEVAFF0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1256-original.png]]

### 原文第1257页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1257|p.1257]]

- Figure C-67: ext_pmdevaff1 bit assignments
- Table C-114: PMDEVAFF1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1257-original.png]]

### 原文第1258页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1258|p.1258]]

- Figure C-68: ext_pmlar bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1258-original.png]]

### 原文第1259页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1259|p.1259]]

- Table C-116: PMLAR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1259-original.png]]

### 原文第1260页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1260|p.1260]]

- Figure C-69: ext_pmlsr bit assignments
- Table C-118: PMLSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1260-original.png]]

### 原文第1261页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1261|p.1261]]

- Figure C-70: ext_pmauthstatus bit assignments
- Table C-120: PMAUTHSTATUS bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1261-original.png]]

### 原文第1262页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1262|p.1262]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1262-original.png]]

### 原文第1263页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1263|p.1263]]

- Figure C-71: ext_pmdevarch bit assignments
- Table C-122: PMDEVARCH bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1263-original.png]]

### 原文第1265页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1265|p.1265]]

- Figure C-72: ext_pmdevid bit assignments
- Table C-124: PMDEVID bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1265-original.png]]

### 原文第1266页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1266|p.1266]]

- Figure C-73: ext_pmdevtype bit assignments
- Table C-126: PMDEVTYPE bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1266-original.png]]

### 原文第1267页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1267|p.1267]]

- Figure C-74: ext_pmpidr4 bit assignments
- Table C-128: PMPIDR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1267-original.png]]

### 原文第1269页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1269|p.1269]]

- Figure C-75: ext_pmpidr0 bit assignments
- Table C-130: PMPIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1269-original.png]]

### 原文第1270页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1270|p.1270]]

- Figure C-76: ext_pmpidr1 bit assignments
- Table C-132: PMPIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1270-original.png]]

### 原文第1271页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1271|p.1271]]

- Figure C-77: ext_pmpidr2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1271-original.png]]

### 原文第1272页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1272|p.1272]]

- Table C-134: PMPIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1272-original.png]]

### 原文第1273页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1273|p.1273]]

- Figure C-78: ext_pmpidr3 bit assignments
- Table C-136: PMPIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1273-original.png]]

### 原文第1274页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1274|p.1274]]

- Figure C-79: ext_pmcidr0 bit assignments
- Table C-138: PMCIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1274-original.png]]

### 原文第1275页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1275|p.1275]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1275-original.png]]

### 原文第1276页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1276|p.1276]]

- Figure C-80: ext_pmcidr1 bit assignments
- Table C-140: PMCIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1276-original.png]]

### 原文第1277页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1277|p.1277]]

- Figure C-81: ext_pmcidr2 bit assignments
- Table C-142: PMCIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1277-original.png]]

### 原文第1278页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1278|p.1278]]

- Figure C-82: ext_pmcidr3 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1278-original.png]]

### 原文第1279页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1279|p.1279]]

- Table C-144: PMCIDR3 bit descriptions
- Table C-146: CTI registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1279-original.png]]

### 原文第1280页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1280|p.1280]]

- Figure C-83: ext_cticontrol bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1280-original.png]]

### 原文第1281页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1281|p.1281]]

- Table C-147: CTICONTROL bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1281-original.png]]

### 原文第1282页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1282|p.1282]]

- Figure C-84: ext_ctiintack bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1282-original.png]]

### 原文第1283页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1283|p.1283]]

- Table C-149: CTIINTACK bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1283-original.png]]

### 原文第1284页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1284|p.1284]]

- Figure C-85: ext_ctiappset bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1284-original.png]]

### 原文第1285页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1285|p.1285]]

- Table C-151: CTIAPPSET bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1285-original.png]]

### 原文第1286页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1286|p.1286]]

- Figure C-86: ext_ctiappclear bit assignments
- Table C-153: CTIAPPCLEAR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1286-original.png]]

### 原文第1288页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1288|p.1288]]

- Figure C-87: ext_ctiapppulse bit assignments
- Table C-155: CTIAPPPULSE bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1288-original.png]]

### 原文第1290页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1290|p.1290]]

- Figure C-88: ext_ctiinen_n_ bit assignments
- Table C-157: CTIINEN<n> bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1290-original.png]]

### 原文第1291页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1291|p.1291]]

- Figure C-89: ext_ctiouten_n_ bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1291-original.png]]

### 原文第1292页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1292|p.1292]]

- Table C-159: CTIOUTEN<n> bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1292-original.png]]

### 原文第1293页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1293|p.1293]]

- Figure C-90: ext_ctitriginstatus bit assignments
- Table C-161: CTITRIGINSTATUS bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1293-original.png]]

### 原文第1294页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1294|p.1294]]

- Figure C-91: ext_ctitrigoutstatus bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1294-original.png]]

### 原文第1295页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1295|p.1295]]

- Table C-163: CTITRIGOUTSTATUS bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1295-original.png]]

### 原文第1296页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1296|p.1296]]

- Figure C-92: ext_ctichinstatus bit assignments
- Table C-165: CTICHINSTATUS bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1296-original.png]]

### 原文第1297页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1297|p.1297]]

- Figure C-93: ext_ctichoutstatus bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1297-original.png]]

### 原文第1298页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1298|p.1298]]

- Table C-167: CTICHOUTSTATUS bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1298-original.png]]

### 原文第1299页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1299|p.1299]]

- Figure C-94: ext_ctigate bit assignments
- Table C-169: CTIGATE bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1299-original.png]]

### 原文第1301页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1301|p.1301]]

- Figure C-95: ext_asicctl bit assignments
- Table C-171: ASICCTL bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1301-original.png]]

### 原文第1302页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1302|p.1302]]

- Figure C-96: ext_ctidevctl bit assignments
- Table C-173: CTIDEVCTL bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1302-original.png]]

### 原文第1303页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1303|p.1303]]

- Figure C-97: ext_ctidevaff0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1303-original.png]]

### 原文第1304页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1304|p.1304]]

- Table C-175: CTIDEVAFF0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1304-original.png]]

### 原文第1305页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1305|p.1305]]

- Figure C-98: ext_ctidevaff1 bit assignments
- Table C-177: CTIDEVAFF1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1305-original.png]]

### 原文第1306页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1306|p.1306]]

- Figure C-99: ext_ctilar bit assignments
- Table C-179: CTILAR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1306-original.png]]

### 原文第1307页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1307|p.1307]]

- Figure C-100: ext_ctilsr bit assignments
- Table C-181: CTILSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1307-original.png]]

### 原文第1308页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1308|p.1308]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1308-original.png]]

### 原文第1309页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1309|p.1309]]

- Figure C-101: ext_ctiauthstatus bit assignments
- Table C-183: CTIAUTHSTATUS bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1309-original.png]]

### 原文第1310页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1310|p.1310]]

- Figure C-102: ext_ctidevarch bit assignments
- Table C-185: CTIDEVARCH bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1310-original.png]]

### 原文第1311页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1311|p.1311]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1311-original.png]]

### 原文第1312页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1312|p.1312]]

- Figure C-103: ext_ctidevid2 bit assignments
- Table C-187: CTIDEVID2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1312-original.png]]

### 原文第1313页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1313|p.1313]]

- Figure C-104: ext_ctidevid1 bit assignments
- Table C-189: CTIDEVID1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1313-original.png]]

### 原文第1314页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1314|p.1314]]

- Figure C-105: ext_ctidevid bit assignments
- Table C-191: CTIDEVID bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1314-original.png]]

### 原文第1315页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1315|p.1315]]

- Table C-193: Debug registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1315-original.png]]

### 原文第1316页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1316|p.1316]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1316-original.png]]

### 原文第1317页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1317|p.1317]]

- Figure C-106: ext_edesr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1317-original.png]]

### 原文第1318页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1318|p.1318]]

- Table C-194: EDESR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1318-original.png]]

### 原文第1319页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1319|p.1319]]

- Figure C-107: ext_edecr bit assignments
- Table C-196: EDECR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1319-original.png]]

### 原文第1320页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1320|p.1320]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1320-original.png]]

### 原文第1321页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1321|p.1321]]

- Figure C-108: ext_edwar bit assignments
- Table C-198: EDWAR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1321-original.png]]

### 原文第1322页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1322|p.1322]]

- Figure C-109: ext_dbgdtrrx_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1322-original.png]]

### 原文第1323页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1323|p.1323]]

- Table C-201: DBGDTRRX_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1323-original.png]]

### 原文第1324页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1324|p.1324]]

- Figure C-110: ext_editr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1324-original.png]]

### 原文第1325页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1325|p.1325]]

- Table C-203: EDITR bit descriptions
- Figure C-111: ext_editr bit assignments
- Table C-204: EDITR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1325-original.png]]

### 原文第1327页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1327|p.1327]]

- Figure C-112: ext_edscr bit assignments
- Table C-206: EDSCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1327-original.png]]

### 原文第1328页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1328|p.1328]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1328-original.png]]

### 原文第1329页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1329|p.1329]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1329-original.png]]

### 原文第1330页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1330|p.1330]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1330-original.png]]

### 原文第1331页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1331|p.1331]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1331-original.png]]

### 原文第1332页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1332|p.1332]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1332-original.png]]

### 原文第1333页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1333|p.1333]]

- Figure C-113: ext_dbgdtrtx_el0 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1333-original.png]]

### 原文第1334页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1334|p.1334]]

- Table C-208: DBGDTRTX_EL0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1334-original.png]]

### 原文第1335页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1335|p.1335]]

- Figure C-114: ext_edrcr bit assignments
- Table C-210: EDRCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1335-original.png]]

### 原文第1336页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1336|p.1336]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1336-original.png]]

### 原文第1337页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1337|p.1337]]

- Figure C-115: ext_edeccr bit assignments
- Table C-212: EDECCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1337-original.png]]

### 原文第1338页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1338|p.1338]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1338-original.png]]

### 原文第1339页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1339|p.1339]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1339-original.png]]

### 原文第1340页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1340|p.1340]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1340-original.png]]

### 原文第1341页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1341|p.1341]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1341-original.png]]

### 原文第1342页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1342|p.1342]]

- Figure C-116: ext_oslar_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1342-original.png]]

### 原文第1343页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1343|p.1343]]

- Table C-214: OSLAR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1343-original.png]]

### 原文第1344页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1344|p.1344]]

- Figure C-117: ext_edprcr bit assignments
- Table C-216: EDPRCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1344-original.png]]

### 原文第1345页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1345|p.1345]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1345-original.png]]

### 原文第1347页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1347|p.1347]]

- Figure C-118: ext_edprsr bit assignments
- Table C-218: EDPRSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1347-original.png]]

### 原文第1348页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1348|p.1348]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1348-original.png]]

### 原文第1349页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1349|p.1349]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1349-original.png]]

### 原文第1350页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1350|p.1350]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1350-original.png]]

### 原文第1351页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1351|p.1351]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1351-original.png]]

### 原文第1352页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1352|p.1352]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1352-original.png]]

### 原文第1355页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1355|p.1355]]

- Figure C-119: ext_dbgbvr0_el1 bit assignments
- Table C-220: DBGBVR0_EL1 bit descriptions
- Figure C-120: ext_dbgbvr0_el1 bit assignments
- Table C-221: DBGBVR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1355-original.png]]

### 原文第1356页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1356|p.1356]]

- Figure C-121: ext_dbgbvr0_el1 bit assignments
- Table C-222: DBGBVR0_EL1 bit descriptions
- Figure C-122: ext_dbgbvr0_el1 bit assignments
- Table C-223: DBGBVR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1356-original.png]]

### 原文第1357页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1357|p.1357]]

- Figure C-123: ext_dbgbvr0_el1 bit assignments
- Table C-224: DBGBVR0_EL1 bit descriptions
- Figure C-124: ext_dbgbvr0_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1357-original.png]]

### 原文第1358页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1358|p.1358]]

- Table C-225: DBGBVR0_EL1 bit descriptions
- Figure C-125: ext_dbgbvr0_el1 bit assignments
- Table C-226: DBGBVR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1358-original.png]]

### 原文第1359页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1359|p.1359]]

- Figure C-126: ext_dbgbcr0_el1 bit assignments
- Table C-228: DBGBCR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1359-original.png]]

### 原文第1360页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1360|p.1360]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1360-original.png]]

### 原文第1361页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1361|p.1361]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1361-original.png]]

### 原文第1362页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1362|p.1362]]

- Table C-229: BAS description table 1
- Table C-230: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1362-original.png]]

### 原文第1364页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1364|p.1364]]

- Figure C-127: ext_dbgbvr1_el1 bit assignments
- Table C-232: DBGBVR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1364-original.png]]

### 原文第1365页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1365|p.1365]]

- Figure C-128: ext_dbgbvr1_el1 bit assignments
- Table C-233: DBGBVR1_EL1 bit descriptions
- Figure C-129: ext_dbgbvr1_el1 bit assignments
- Table C-234: DBGBVR1_EL1 bit descriptions
- Figure C-130: ext_dbgbvr1_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1365-original.png]]

### 原文第1366页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1366|p.1366]]

- Table C-235: DBGBVR1_EL1 bit descriptions
- Figure C-131: ext_dbgbvr1_el1 bit assignments
- Table C-236: DBGBVR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1366-original.png]]

### 原文第1367页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1367|p.1367]]

- Figure C-132: ext_dbgbvr1_el1 bit assignments
- Table C-237: DBGBVR1_EL1 bit descriptions
- Figure C-133: ext_dbgbvr1_el1 bit assignments
- Table C-238: DBGBVR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1367-original.png]]

### 原文第1369页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1369|p.1369]]

- Figure C-134: ext_dbgbcr1_el1 bit assignments
- Table C-240: DBGBCR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1369-original.png]]

### 原文第1370页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1370|p.1370]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1370-original.png]]

### 原文第1371页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1371|p.1371]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1371-original.png]]

### 原文第1372页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1372|p.1372]]

- Table C-241: BAS description table 1
- Table C-242: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1372-original.png]]

### 原文第1374页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1374|p.1374]]

- Figure C-135: ext_dbgbvr2_el1 bit assignments
- Table C-244: DBGBVR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1374-original.png]]

### 原文第1375页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1375|p.1375]]

- Figure C-136: ext_dbgbvr2_el1 bit assignments
- Table C-245: DBGBVR2_EL1 bit descriptions
- Figure C-137: ext_dbgbvr2_el1 bit assignments
- Table C-246: DBGBVR2_EL1 bit descriptions
- Figure C-138: ext_dbgbvr2_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1375-original.png]]

### 原文第1376页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1376|p.1376]]

- Table C-247: DBGBVR2_EL1 bit descriptions
- Figure C-139: ext_dbgbvr2_el1 bit assignments
- Table C-248: DBGBVR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1376-original.png]]

### 原文第1377页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1377|p.1377]]

- Figure C-140: ext_dbgbvr2_el1 bit assignments
- Table C-249: DBGBVR2_EL1 bit descriptions
- Figure C-141: ext_dbgbvr2_el1 bit assignments
- Table C-250: DBGBVR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1377-original.png]]

### 原文第1379页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1379|p.1379]]

- Figure C-142: ext_dbgbcr2_el1 bit assignments
- Table C-252: DBGBCR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1379-original.png]]

### 原文第1380页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1380|p.1380]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1380-original.png]]

### 原文第1381页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1381|p.1381]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1381-original.png]]

### 原文第1382页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1382|p.1382]]

- Table C-253: BAS description table 1
- Table C-254: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1382-original.png]]

### 原文第1384页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1384|p.1384]]

- Figure C-143: ext_dbgbvr3_el1 bit assignments
- Table C-256: DBGBVR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1384-original.png]]

### 原文第1385页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1385|p.1385]]

- Figure C-144: ext_dbgbvr3_el1 bit assignments
- Table C-257: DBGBVR3_EL1 bit descriptions
- Figure C-145: ext_dbgbvr3_el1 bit assignments
- Table C-258: DBGBVR3_EL1 bit descriptions
- Figure C-146: ext_dbgbvr3_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1385-original.png]]

### 原文第1386页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1386|p.1386]]

- Table C-259: DBGBVR3_EL1 bit descriptions
- Figure C-147: ext_dbgbvr3_el1 bit assignments
- Table C-260: DBGBVR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1386-original.png]]

### 原文第1387页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1387|p.1387]]

- Figure C-148: ext_dbgbvr3_el1 bit assignments
- Table C-261: DBGBVR3_EL1 bit descriptions
- Figure C-149: ext_dbgbvr3_el1 bit assignments
- Table C-262: DBGBVR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1387-original.png]]

### 原文第1389页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1389|p.1389]]

- Figure C-150: ext_dbgbcr3_el1 bit assignments
- Table C-264: DBGBCR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1389-original.png]]

### 原文第1390页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1390|p.1390]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1390-original.png]]

### 原文第1391页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1391|p.1391]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1391-original.png]]

### 原文第1392页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1392|p.1392]]

- Table C-265: BAS description table 1
- Table C-266: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1392-original.png]]

### 原文第1394页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1394|p.1394]]

- Figure C-151: ext_dbgbvr4_el1 bit assignments
- Table C-268: DBGBVR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1394-original.png]]

### 原文第1395页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1395|p.1395]]

- Figure C-152: ext_dbgbvr4_el1 bit assignments
- Table C-269: DBGBVR4_EL1 bit descriptions
- Figure C-153: ext_dbgbvr4_el1 bit assignments
- Table C-270: DBGBVR4_EL1 bit descriptions
- Figure C-154: ext_dbgbvr4_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1395-original.png]]

### 原文第1396页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1396|p.1396]]

- Table C-271: DBGBVR4_EL1 bit descriptions
- Figure C-155: ext_dbgbvr4_el1 bit assignments
- Table C-272: DBGBVR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1396-original.png]]

### 原文第1397页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1397|p.1397]]

- Figure C-156: ext_dbgbvr4_el1 bit assignments
- Table C-273: DBGBVR4_EL1 bit descriptions
- Figure C-157: ext_dbgbvr4_el1 bit assignments
- Table C-274: DBGBVR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1397-original.png]]

### 原文第1399页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1399|p.1399]]

- Figure C-158: ext_dbgbcr4_el1 bit assignments
- Table C-276: DBGBCR4_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1399-original.png]]

### 原文第1400页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1400|p.1400]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1400-original.png]]

### 原文第1401页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1401|p.1401]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1401-original.png]]

### 原文第1402页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1402|p.1402]]

- Table C-277: BAS description table 1
- Table C-278: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1402-original.png]]

### 原文第1404页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1404|p.1404]]

- Figure C-159: ext_dbgbvr5_el1 bit assignments
- Table C-280: DBGBVR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1404-original.png]]

### 原文第1405页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1405|p.1405]]

- Figure C-160: ext_dbgbvr5_el1 bit assignments
- Table C-281: DBGBVR5_EL1 bit descriptions
- Figure C-161: ext_dbgbvr5_el1 bit assignments
- Table C-282: DBGBVR5_EL1 bit descriptions
- Figure C-162: ext_dbgbvr5_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1405-original.png]]

### 原文第1406页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1406|p.1406]]

- Table C-283: DBGBVR5_EL1 bit descriptions
- Figure C-163: ext_dbgbvr5_el1 bit assignments
- Table C-284: DBGBVR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1406-original.png]]

### 原文第1407页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1407|p.1407]]

- Figure C-164: ext_dbgbvr5_el1 bit assignments
- Table C-285: DBGBVR5_EL1 bit descriptions
- Figure C-165: ext_dbgbvr5_el1 bit assignments
- Table C-286: DBGBVR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1407-original.png]]

### 原文第1409页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1409|p.1409]]

- Figure C-166: ext_dbgbcr5_el1 bit assignments
- Table C-288: DBGBCR5_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1409-original.png]]

### 原文第1410页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1410|p.1410]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1410-original.png]]

### 原文第1411页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1411|p.1411]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1411-original.png]]

### 原文第1412页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1412|p.1412]]

- Table C-289: BAS description table 1
- Table C-290: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1412-original.png]]

### 原文第1413页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1413|p.1413]]

- Figure C-167: ext_dbgwvr0_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1413-original.png]]

### 原文第1414页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1414|p.1414]]

- Table C-292: DBGWVR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1414-original.png]]

### 原文第1415页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1415|p.1415]]

- Figure C-168: ext_dbgwcr0_el1 bit assignments
- Table C-294: DBGWCR0_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1415-original.png]]

### 原文第1416页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1416|p.1416]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1416-original.png]]

### 原文第1417页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1417|p.1417]]

- Table C-295: BAS description table 1
- Table C-296: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1417-original.png]]

### 原文第1419页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1419|p.1419]]

- Figure C-169: ext_dbgwvr1_el1 bit assignments
- Table C-298: DBGWVR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1419-original.png]]

### 原文第1420页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1420|p.1420]]

- Figure C-170: ext_dbgwcr1_el1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1420-original.png]]

### 原文第1421页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1421|p.1421]]

- Table C-300: DBGWCR1_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1421-original.png]]

### 原文第1422页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1422|p.1422]]

- Table C-301: BAS description table 1
- Table C-302: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1422-original.png]]

### 原文第1424页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1424|p.1424]]

- Figure C-171: ext_dbgwvr2_el1 bit assignments
- Table C-304: DBGWVR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1424-original.png]]

### 原文第1426页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1426|p.1426]]

- Figure C-172: ext_dbgwcr2_el1 bit assignments
- Table C-306: DBGWCR2_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1426-original.png]]

### 原文第1427页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1427|p.1427]]

- Table C-307: BAS description table 1
- Table C-308: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1427-original.png]]

### 原文第1429页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1429|p.1429]]

- Figure C-173: ext_dbgwvr3_el1 bit assignments
- Table C-310: DBGWVR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1429-original.png]]

### 原文第1431页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1431|p.1431]]

- Figure C-174: ext_dbgwcr3_el1 bit assignments
- Table C-312: DBGWCR3_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1431-original.png]]

### 原文第1432页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1432|p.1432]]

- Table C-313: BAS description table 1
- Table C-314: BAS description table 2

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1432-original.png]]

### 原文第1434页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1434|p.1434]]

- Figure C-175: ext_midr_el1 bit assignments
- Table C-316: MIDR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1434-original.png]]

### 原文第1435页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1435|p.1435]]

- Figure C-176: ext_edpfr bit assignments
- Table C-318: EDPFR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1435-original.png]]

### 原文第1436页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1436|p.1436]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1436-original.png]]

### 原文第1438页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1438|p.1438]]

- Figure C-177: ext_eddfr bit assignments
- Table C-321: EDDFR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1438-original.png]]

### 原文第1439页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1439|p.1439]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1439-original.png]]

### 原文第1440页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1440|p.1440]]

- Figure C-178: ext_edaa32pfr bit assignments
- Table C-324: EDAA32PFR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1440-original.png]]

### 原文第1441页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1441|p.1441]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1441-original.png]]

### 原文第1442页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1442|p.1442]]

- Figure C-179: ext_editctrl bit assignments
- Table C-326: EDITCTRL bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1442-original.png]]

### 原文第1443页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1443|p.1443]]

- Figure C-180: ext_dbgclaimset_el1 bit assignments
- Table C-328: DBGCLAIMSET_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1443-original.png]]

### 原文第1444页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1444|p.1444]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1444-original.png]]

### 原文第1445页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1445|p.1445]]

- Figure C-181: ext_dbgclaimclr_el1 bit assignments
- Table C-330: DBGCLAIMCLR_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1445-original.png]]

### 原文第1446页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1446|p.1446]]

- Figure C-182: ext_eddevaff0 bit assignments
- Table C-332: EDDEVAFF0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1446-original.png]]

### 原文第1447页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1447|p.1447]]

- Figure C-183: ext_eddevaff1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1447-original.png]]

### 原文第1448页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1448|p.1448]]

- Table C-334: EDDEVAFF1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1448-original.png]]

### 原文第1449页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1449|p.1449]]

- Figure C-184: ext_edlar bit assignments
- Table C-336: EDLAR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1449-original.png]]

### 原文第1450页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1450|p.1450]]

- Figure C-185: ext_edlsr bit assignments
- Table C-338: EDLSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1450-original.png]]

### 原文第1451页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1451|p.1451]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1451-original.png]]

### 原文第1452页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1452|p.1452]]

- Figure C-186: ext_dbgauthstatus_el1 bit assignments
- Table C-340: DBGAUTHSTATUS_EL1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1452-original.png]]

### 原文第1453页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1453|p.1453]]

- Figure C-187: ext_eddevarch bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1453-original.png]]

### 原文第1454页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1454|p.1454]]

- Table C-342: EDDEVARCH bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1454-original.png]]

### 原文第1455页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1455|p.1455]]

- Figure C-188: ext_eddevid2 bit assignments
- Table C-344: EDDEVID2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1455-original.png]]

### 原文第1456页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1456|p.1456]]

- Figure C-189: ext_eddevid1 bit assignments
- Table C-346: EDDEVID1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1456-original.png]]

### 原文第1458页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1458|p.1458]]

- Figure C-190: ext_eddevid bit assignments
- Table C-348: EDDEVID bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1458-original.png]]

### 原文第1459页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1459|p.1459]]

- Figure C-191: ext_eddevtype bit assignments
- Table C-350: EDDEVTYPE bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1459-original.png]]

### 原文第1460页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1460|p.1460]]

- Figure C-192: ext_edpidr4 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1460-original.png]]

### 原文第1461页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1461|p.1461]]

- Table C-352: EDPIDR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1461-original.png]]

### 原文第1462页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1462|p.1462]]

- Figure C-193: ext_edpidr0 bit assignments
- Table C-354: EDPIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1462-original.png]]

### 原文第1463页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1463|p.1463]]

- Figure C-194: ext_edpidr1 bit assignments
- Table C-356: EDPIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1463-original.png]]

### 原文第1464页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1464|p.1464]]

- Figure C-195: ext_edpidr2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1464-original.png]]

### 原文第1465页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1465|p.1465]]

- Table C-358: EDPIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1465-original.png]]

### 原文第1466页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1466|p.1466]]

- Figure C-196: ext_edpidr3 bit assignments
- Table C-360: EDPIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1466-original.png]]

### 原文第1467页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1467|p.1467]]

- Figure C-197: ext_edcidr0 bit assignments
- Table C-362: EDCIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1467-original.png]]

### 原文第1469页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1469|p.1469]]

- Figure C-198: ext_edcidr1 bit assignments
- Table C-364: EDCIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1469-original.png]]

### 原文第1470页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1470|p.1470]]

- Figure C-199: ext_edcidr2 bit assignments
- Table C-366: EDCIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1470-original.png]]

### 原文第1471页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1471|p.1471]]

- Figure C-200: ext_edcidr3 bit assignments
- Table C-368: EDCIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1471-original.png]]

### 原文第1472页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1472|p.1472]]

- Table C-370: Activity Monitors registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1472-original.png]]

### 原文第1473页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1473|p.1473]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1473-original.png]]

### 原文第1474页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1474|p.1474]]

- Figure C-201: ext_amevcntr00 bit assignments
- Table C-371: AMEVCNTR00 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1474-original.png]]

### 原文第1476页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1476|p.1476]]

- Figure C-202: ext_amevcntr01 bit assignments
- Table C-374: AMEVCNTR01 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1476-original.png]]

### 原文第1477页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1477|p.1477]]

- Figure C-203: ext_amevcntr02 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1477-original.png]]

### 原文第1478页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1478|p.1478]]

- Table C-377: AMEVCNTR02 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1478-original.png]]

### 原文第1479页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1479|p.1479]]

- Figure C-204: ext_amevcntr03 bit assignments
- Table C-380: AMEVCNTR03 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1479-original.png]]

### 原文第1481页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1481|p.1481]]

- Figure C-205: ext_amevcntr10 bit assignments
- Table C-383: AMEVCNTR10 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1481-original.png]]

### 原文第1483页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1483|p.1483]]

- Figure C-206: ext_amevcntr11 bit assignments
- Table C-386: AMEVCNTR11 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1483-original.png]]

### 原文第1484页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1484|p.1484]]

- Figure C-207: ext_amevcntr12 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1484-original.png]]

### 原文第1485页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1485|p.1485]]

- Table C-389: AMEVCNTR12 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1485-original.png]]

### 原文第1486页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1486|p.1486]]

- Figure C-208: ext_amevtyper00 bit assignments
- Table C-392: AMEVTYPER00 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1486-original.png]]

### 原文第1487页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1487|p.1487]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1487-original.png]]

### 原文第1488页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1488|p.1488]]

- Figure C-209: ext_amevtyper01 bit assignments
- Table C-394: AMEVTYPER01 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1488-original.png]]

### 原文第1490页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1490|p.1490]]

- Figure C-210: ext_amevtyper02 bit assignments
- Table C-396: AMEVTYPER02 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1490-original.png]]

### 原文第1492页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1492|p.1492]]

- Figure C-211: ext_amevtyper03 bit assignments
- Table C-398: AMEVTYPER03 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1492-original.png]]

### 原文第1493页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1493|p.1493]]

- Figure C-212: ext_amevtyper10 bit assignments
- Table C-400: AMEVTYPER10 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1493-original.png]]

### 原文第1494页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1494|p.1494]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1494-original.png]]

### 原文第1495页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1495|p.1495]]

- Figure C-213: ext_amevtyper11 bit assignments
- Table C-402: AMEVTYPER11 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1495-original.png]]

### 原文第1497页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1497|p.1497]]

- Figure C-214: ext_amevtyper12 bit assignments
- Table C-404: AMEVTYPER12 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1497-original.png]]

### 原文第1498页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1498|p.1498]]

- Figure C-215: ext_amcntenset0 bit assignments
- Table C-406: AMCNTENSET0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1498-original.png]]

### 原文第1499页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1499|p.1499]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1499-original.png]]

### 原文第1500页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1500|p.1500]]

- Figure C-216: ext_amcntenset1 bit assignments
- Table C-408: AMCNTENSET1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1500-original.png]]

### 原文第1502页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1502|p.1502]]

- Figure C-217: ext_amcntenclr0 bit assignments
- Table C-410: AMCNTENCLR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1502-original.png]]

### 原文第1503页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1503|p.1503]]

- Figure C-218: ext_amcntenclr1 bit assignments
- Table C-412: AMCNTENCLR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1503-original.png]]

### 原文第1505页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1505|p.1505]]

- Figure C-219: ext_amcgcr bit assignments
- Table C-414: AMCGCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1505-original.png]]

### 原文第1506页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1506|p.1506]]

- Figure C-220: ext_amcfgr bit assignments
- Table C-416: AMCFGR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1506-original.png]]

### 原文第1507页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1507|p.1507]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1507-original.png]]

### 原文第1508页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1508|p.1508]]

- Figure C-221: ext_amcr bit assignments
- Table C-418: AMCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1508-original.png]]

### 原文第1509页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1509|p.1509]]

- Figure C-222: ext_amiidr bit assignments
- Table C-420: AMIIDR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1509-original.png]]

### 原文第1510页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1510|p.1510]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1510-original.png]]

### 原文第1511页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1511|p.1511]]

- Figure C-223: ext_amdevaff0 bit assignments
- Table C-422: AMDEVAFF0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1511-original.png]]

### 原文第1512页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1512|p.1512]]

- Figure C-224: ext_amdevaff1 bit assignments
- Table C-424: AMDEVAFF1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1512-original.png]]

### 原文第1513页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1513|p.1513]]

- Figure C-225: ext_amdevarch bit assignments
- Table C-426: AMDEVARCH bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1513-original.png]]

### 原文第1514页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1514|p.1514]]

- Figure C-226: ext_amdevtype bit assignments
- Table C-428: AMDEVTYPE bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1514-original.png]]

### 原文第1515页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1515|p.1515]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1515-original.png]]

### 原文第1516页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1516|p.1516]]

- Figure C-227: ext_ampidr4 bit assignments
- Table C-430: AMPIDR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1516-original.png]]

### 原文第1517页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1517|p.1517]]

- Figure C-228: ext_ampidr0 bit assignments
- Table C-432: AMPIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1517-original.png]]

### 原文第1518页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1518|p.1518]]

- Figure C-229: ext_ampidr1 bit assignments
- Table C-434: AMPIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1518-original.png]]

### 原文第1519页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1519|p.1519]]

- Figure C-230: ext_ampidr2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1519-original.png]]

### 原文第1520页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1520|p.1520]]

- Table C-436: AMPIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1520-original.png]]

### 原文第1521页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1521|p.1521]]

- Figure C-231: ext_ampidr3 bit assignments
- Table C-438: AMPIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1521-original.png]]

### 原文第1522页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1522|p.1522]]

- Figure C-232: ext_amcidr0 bit assignments
- Table C-440: AMCIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1522-original.png]]

### 原文第1523页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1523|p.1523]]

- Figure C-233: ext_amcidr1 bit assignments
- Table C-442: AMCIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1523-original.png]]

### 原文第1524页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1524|p.1524]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1524-original.png]]

### 原文第1525页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1525|p.1525]]

- Figure C-234: ext_amcidr2 bit assignments
- Table C-444: AMCIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1525-original.png]]

### 原文第1526页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1526|p.1526]]

- Figure C-235: ext_amcidr3 bit assignments
- Table C-446: AMCIDR3 bit descriptions
- Table C-448: Trace unit registers summary

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1526-original.png]]

### 原文第1527页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1527|p.1527]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1527-original.png]]

### 原文第1528页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1528|p.1528]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1528-original.png]]

### 原文第1529页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1529|p.1529]]

- Figure C-236: ext_trcprgctlr bit assignments
- Table C-449: TRCPRGCTLR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1529-original.png]]

### 原文第1530页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1530|p.1530]]

- Figure C-237: ext_trcstatr bit assignments
- Table C-451: TRCSTATR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1530-original.png]]

### 原文第1531页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1531|p.1531]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1531-original.png]]

### 原文第1532页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1532|p.1532]]

- Figure C-238: ext_trcconfigr bit assignments
- Table C-453: TRCCONFIGR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1532-original.png]]

### 原文第1533页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1533|p.1533]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1533-original.png]]

### 原文第1534页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1534|p.1534]]

- Figure C-239: ext_trcauxctlr bit assignments
- Table C-455: TRCAUXCTLR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1534-original.png]]

### 原文第1535页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1535|p.1535]]

- Figure C-240: ext_trceventctl0r bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1535-original.png]]

### 原文第1536页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1536|p.1536]]

- Table C-457: TRCEVENTCTL0R bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1536-original.png]]

### 原文第1537页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1537|p.1537]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1537-original.png]]

### 原文第1538页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1538|p.1538]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1538-original.png]]

### 原文第1539页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1539|p.1539]]

- Figure C-241: ext_trceventctl1r bit assignments
- Table C-459: TRCEVENTCTL1R bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1539-original.png]]

### 原文第1540页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1540|p.1540]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1540-original.png]]

### 原文第1541页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1541|p.1541]]

- Figure C-242: ext_trcrsr bit assignments
- Table C-461: TRCRSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1541-original.png]]

### 原文第1542页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1542|p.1542]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1542-original.png]]

### 原文第1543页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1543|p.1543]]

- Figure C-243: ext_trctsctlr bit assignments
- Table C-463: TRCTSCTLR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1543-original.png]]

### 原文第1544页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1544|p.1544]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1544-original.png]]

### 原文第1545页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1545|p.1545]]

- Figure C-244: ext_trcsyncpr bit assignments
- Table C-465: TRCSYNCPR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1545-original.png]]

### 原文第1546页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1546|p.1546]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1546-original.png]]

### 原文第1547页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1547|p.1547]]

- Figure C-245: ext_trcccctlr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1547-original.png]]

### 原文第1548页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1548|p.1548]]

- Table C-467: TRCCCCTLR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1548-original.png]]

### 原文第1549页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1549|p.1549]]

- Figure C-246: ext_trcbbctlr bit assignments
- Table C-469: TRCBBCTLR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1549-original.png]]

### 原文第1550页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1550|p.1550]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1550-original.png]]

### 原文第1551页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1551|p.1551]]

- Figure C-247: ext_trctraceidr bit assignments
- Table C-471: TRCTRACEIDR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1551-original.png]]

### 原文第1552页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1552|p.1552]]

- Figure C-248: ext_trcvictlr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1552-original.png]]

### 原文第1553页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1553|p.1553]]

- Table C-473: TRCVICTLR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1553-original.png]]

### 原文第1554页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1554|p.1554]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1554-original.png]]

### 原文第1555页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1555|p.1555]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1555-original.png]]

### 原文第1556页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1556|p.1556]]

- Figure C-249: ext_trcviiectlr bit assignments
- Table C-475: TRCVIIECTLR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1556-original.png]]

### 原文第1557页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1557|p.1557]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1557-original.png]]

### 原文第1558页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1558|p.1558]]

- Figure C-250: ext_trcvissctlr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1558-original.png]]

### 原文第1559页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1559|p.1559]]

- Table C-477: TRCVISSCTLR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1559-original.png]]

### 原文第1560页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1560|p.1560]]

- Figure C-251: ext_trcseqevr0 bit assignments
- Table C-479: TRCSEQEVR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1560-original.png]]

### 原文第1561页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1561|p.1561]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1561-original.png]]

### 原文第1562页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1562|p.1562]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1562-original.png]]

### 原文第1563页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1563|p.1563]]

- Figure C-252: ext_trcseqevr1 bit assignments
- Table C-481: TRCSEQEVR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1563-original.png]]

### 原文第1564页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1564|p.1564]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1564-original.png]]

### 原文第1566页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1566|p.1566]]

- Figure C-253: ext_trcseqevr2 bit assignments
- Table C-483: TRCSEQEVR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1566-original.png]]

### 原文第1567页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1567|p.1567]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1567-original.png]]

### 原文第1568页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1568|p.1568]]

- Figure C-254: ext_trcseqrstevr bit assignments
- Table C-485: TRCSEQRSTEVR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1568-original.png]]

### 原文第1569页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1569|p.1569]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1569-original.png]]

### 原文第1570页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1570|p.1570]]

- Figure C-255: ext_trcseqstr bit assignments
- Table C-487: TRCSEQSTR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1570-original.png]]

### 原文第1571页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1571|p.1571]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1571-original.png]]

### 原文第1572页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1572|p.1572]]

- Figure C-256: ext_trcextinselr0 bit assignments
- Table C-489: TRCEXTINSELR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1572-original.png]]

### 原文第1573页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1573|p.1573]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1573-original.png]]

### 原文第1574页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1574|p.1574]]

- Figure C-257: ext_trcextinselr1 bit assignments
- Table C-491: TRCEXTINSELR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1574-original.png]]

### 原文第1575页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1575|p.1575]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1575-original.png]]

### 原文第1576页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1576|p.1576]]

- Figure C-258: ext_trcextinselr2 bit assignments
- Table C-493: TRCEXTINSELR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1576-original.png]]

### 原文第1577页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1577|p.1577]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1577-original.png]]

### 原文第1578页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1578|p.1578]]

- Figure C-259: ext_trcextinselr3 bit assignments
- Table C-495: TRCEXTINSELR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1578-original.png]]

### 原文第1579页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1579|p.1579]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1579-original.png]]

### 原文第1580页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1580|p.1580]]

- Figure C-260: ext_trccntrldvr0 bit assignments
- Table C-497: TRCCNTRLDVR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1580-original.png]]

### 原文第1582页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1582|p.1582]]

- Figure C-261: ext_trccntrldvr1 bit assignments
- Table C-499: TRCCNTRLDVR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1582-original.png]]

### 原文第1583页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1583|p.1583]]

- Figure C-262: ext_trccntctlr0 bit assignments
- Table C-501: TRCCNTCTLR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1583-original.png]]

### 原文第1584页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1584|p.1584]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1584-original.png]]

### 原文第1585页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1585|p.1585]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1585-original.png]]

### 原文第1586页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1586|p.1586]]

- Figure C-263: ext_trccntctlr1 bit assignments
- Table C-503: TRCCNTCTLR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1586-original.png]]

### 原文第1587页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1587|p.1587]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1587-original.png]]

### 原文第1588页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1588|p.1588]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1588-original.png]]

### 原文第1589页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1589|p.1589]]

- Figure C-264: ext_trccntvr0 bit assignments
- Table C-505: TRCCNTVR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1589-original.png]]

### 原文第1590页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1590|p.1590]]

- Figure C-265: ext_trccntvr1 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1590-original.png]]

### 原文第1591页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1591|p.1591]]

- Table C-507: TRCCNTVR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1591-original.png]]

### 原文第1592页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1592|p.1592]]

- Figure C-266: ext_trcidr8 bit assignments
- Table C-509: TRCIDR8 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1592-original.png]]

### 原文第1593页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1593|p.1593]]

- Figure C-267: ext_trcidr9 bit assignments
- Table C-511: TRCIDR9 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1593-original.png]]

### 原文第1594页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1594|p.1594]]

- Figure C-268: ext_trcidr10 bit assignments
- Table C-513: TRCIDR10 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1594-original.png]]

### 原文第1595页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1595|p.1595]]

- Figure C-269: ext_trcidr11 bit assignments
- Table C-515: TRCIDR11 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1595-original.png]]

### 原文第1596页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1596|p.1596]]

- Figure C-270: ext_trcidr12 bit assignments
- Table C-517: TRCIDR12 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1596-original.png]]

### 原文第1597页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1597|p.1597]]

- Figure C-271: ext_trcidr13 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1597-original.png]]

### 原文第1598页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1598|p.1598]]

- Table C-519: TRCIDR13 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1598-original.png]]

### 原文第1599页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1599|p.1599]]

- Figure C-272: ext_trcimspec0 bit assignments
- Table C-521: TRCIMSPEC0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1599-original.png]]

### 原文第1600页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1600|p.1600]]

- Figure C-273: ext_trcidr0 bit assignments
- Table C-523: TRCIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1600-original.png]]

### 原文第1601页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1601|p.1601]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1601-original.png]]

### 原文第1602页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1602|p.1602]]

- Figure C-274: ext_trcidr1 bit assignments
- Table C-525: TRCIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1602-original.png]]

### 原文第1603页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1603|p.1603]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1603-original.png]]

### 原文第1604页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1604|p.1604]]

- Figure C-275: ext_trcidr2 bit assignments
- Table C-527: TRCIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1604-original.png]]

### 原文第1605页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1605|p.1605]]

- Figure C-276: ext_trcidr3 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1605-original.png]]

### 原文第1606页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1606|p.1606]]

- Table C-529: TRCIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1606-original.png]]

### 原文第1607页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1607|p.1607]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1607-original.png]]

### 原文第1608页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1608|p.1608]]

- Figure C-277: ext_trcidr4 bit assignments
- Table C-531: TRCIDR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1608-original.png]]

### 原文第1610页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1610|p.1610]]

- Figure C-278: ext_trcidr5 bit assignments
- Table C-533: TRCIDR5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1610-original.png]]

### 原文第1611页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1611|p.1611]]

- Figure C-279: ext_trcidr6 bit assignments
- Table C-535: TRCIDR6 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1611-original.png]]

### 原文第1612页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1612|p.1612]]

- Figure C-280: ext_trcidr7 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1612-original.png]]

### 原文第1613页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1613|p.1613]]

- Table C-537: TRCIDR7 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1613-original.png]]

### 原文第1614页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1614|p.1614]]

- Figure C-281: ext_trcsscsr_n_ bit assignments
- Table C-539: TRCSSCSR<n> bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1614-original.png]]

### 原文第1615页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1615|p.1615]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1615-original.png]]

### 原文第1616页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1616|p.1616]]

- Figure C-282: ext_trcoslsr bit assignments
- Table C-541: TRCOSLSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1616-original.png]]

### 原文第1617页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1617|p.1617]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1617-original.png]]

### 原文第1618页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1618|p.1618]]

- Figure C-283: ext_trcpdcr bit assignments
- Table C-543: TRCPDCR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1618-original.png]]

### 原文第1619页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1619|p.1619]]

- Figure C-284: ext_trcpdsr bit assignments
- Table C-545: TRCPDSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1619-original.png]]

### 原文第1620页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1620|p.1620]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1620-original.png]]

### 原文第1621页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1621|p.1621]]

- Figure C-285: ext_trccidcctlr0 bit assignments
- Table C-547: TRCCIDCCTLR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1621-original.png]]

### 原文第1623页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1623|p.1623]]

- Figure C-286: ext_trcvmidcctlr0 bit assignments
- Table C-549: TRCVMIDCCTLR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1623-original.png]]

### 原文第1625页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1625|p.1625]]

- Figure C-287: ext_trcitctrl bit assignments
- Table C-551: TRCITCTRL bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1625-original.png]]

### 原文第1627页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1627|p.1627]]

- Figure C-288: ext_trcclaimset bit assignments
- Table C-553: TRCCLAIMSET bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1627-original.png]]

### 原文第1628页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1628|p.1628]]

- Figure C-289: ext_trcclaimclr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1628-original.png]]

### 原文第1629页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1629|p.1629]]

- Table C-555: TRCCLAIMCLR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1629-original.png]]

### 原文第1630页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1630|p.1630]]

- Figure C-290: ext_trcdevaff bit assignments
- Table C-557: TRCDEVAFF bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1630-original.png]]

### 原文第1631页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1631|p.1631]]

- Figure C-291: ext_trclar bit assignments
- Table C-559: TRCLAR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1631-original.png]]

### 原文第1632页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1632|p.1632]]

- Figure C-292: ext_trclsr bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1632-original.png]]

### 原文第1633页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1633|p.1633]]

- Table C-561: TRCLSR bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1633-original.png]]

### 原文第1634页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1634|p.1634]]

- Figure C-293: ext_trcauthstatus bit assignments
- Table C-563: TRCAUTHSTATUS bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1634-original.png]]

### 原文第1635页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1635|p.1635]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1635-original.png]]

### 原文第1636页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1636|p.1636]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1636-original.png]]

### 原文第1637页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1637|p.1637]]

- Figure C-294: ext_trcdevarch bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1637-original.png]]

### 原文第1638页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1638|p.1638]]

- Table C-565: TRCDEVARCH bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1638-original.png]]

### 原文第1639页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1639|p.1639]]

- Figure C-295: ext_trcdevid2 bit assignments
- Table C-567: TRCDEVID2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1639-original.png]]

### 原文第1640页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1640|p.1640]]

- Figure C-296: ext_trcdevid1 bit assignments
- Table C-569: TRCDEVID1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1640-original.png]]

### 原文第1641页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1641|p.1641]]

- Figure C-297: ext_trcdevid bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1641-original.png]]

### 原文第1642页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1642|p.1642]]

- Table C-571: TRCDEVID bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1642-original.png]]

### 原文第1643页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1643|p.1643]]

- Figure C-298: ext_trcdevtype bit assignments
- Table C-573: TRCDEVTYPE bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1643-original.png]]

### 原文第1644页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1644|p.1644]]

- Figure C-299: ext_trcpidr4 bit assignments
- Table C-575: TRCPIDR4 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1644-original.png]]

### 原文第1645页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1645|p.1645]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1645-original.png]]

### 原文第1646页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1646|p.1646]]

- Figure C-300: ext_trcpidr5 bit assignments
- Table C-577: TRCPIDR5 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1646-original.png]]

### 原文第1647页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1647|p.1647]]

- Figure C-301: ext_trcpidr6 bit assignments
- Table C-579: TRCPIDR6 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1647-original.png]]

### 原文第1648页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1648|p.1648]]

- Figure C-302: ext_trcpidr7 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1648-original.png]]

### 原文第1649页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1649|p.1649]]

- Table C-581: TRCPIDR7 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1649-original.png]]

### 原文第1650页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1650|p.1650]]

- Figure C-303: ext_trcpidr0 bit assignments
- Table C-583: TRCPIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1650-original.png]]

### 原文第1651页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1651|p.1651]]

- Figure C-304: ext_trcpidr1 bit assignments
- Table C-585: TRCPIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1651-original.png]]

### 原文第1652页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1652|p.1652]]

- Figure C-305: ext_trcpidr2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1652-original.png]]

### 原文第1653页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1653|p.1653]]

- Table C-587: TRCPIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1653-original.png]]

### 原文第1654页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1654|p.1654]]

- Figure C-306: ext_trcpidr3 bit assignments
- Table C-589: TRCPIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1654-original.png]]

### 原文第1655页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1655|p.1655]]

续表或相关原文；请结合上一页标题与本页条件。

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1655-original.png]]

### 原文第1656页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1656|p.1656]]

- Figure C-307: ext_trccidr0 bit assignments
- Table C-591: TRCCIDR0 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1656-original.png]]

### 原文第1657页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1657|p.1657]]

- Figure C-308: ext_trccidr1 bit assignments
- Table C-593: TRCCIDR1 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1657-original.png]]

### 原文第1658页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1658|p.1658]]

- Figure C-309: ext_trccidr2 bit assignments

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1658-original.png]]

### 原文第1659页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1659|p.1659]]

- Table C-595: TRCCIDR2 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1659-original.png]]

### 原文第1660页

[[arm_neoverse_n2_core_trm_102099_0003_06_en.pdf#page=1660|p.1660]]

- Figure C-310: ext_trccidr3 bit assignments
- Table C-597: TRCCIDR3 bit descriptions

![[Neoverse/01_assets/N2-Core-TRM-r0p3/p1660-original.png]]
