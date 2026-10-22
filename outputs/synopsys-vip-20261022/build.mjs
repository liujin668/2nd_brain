import fs from 'node:fs/promises';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const out = new URL('.', import.meta.url).pathname.replace(/^\/(?:([A-Za-z]):)/, '$1:');
const base = 'https://www.synopsys.com/verification/verification-ip/';
const cat = 'https://www.synopsys.com/zh-cn/verification/verification-ip.html';
const official = '产品页已确认';
const pending = '目录列出，供货待确认';
const data = [];
function add(category,name,scope,notes,path,priority='按芯片接口选购',status=official) {
  data.push([`VIP-${String(data.length+1).padStart(3,'0')}`,category,name,scope,notes,priority,status,'','','','','',null,'','',path.startsWith('http')?path:base+path]);
}
add('片上互连','AMBA CHI','Issue A/B/C/D/E/F/G/H；一致性接口','确认 N2/CMN 实际 CHI revision、RN/SN/monitor及系统检查能力','amba/amba-chi.html','近期优先评估');
add('片上互连','AMBA AXI','AXI3/4/4-Lite/5及J/K/L','需 master/slave/monitor。初期 DDR 替代要求slave memory、预装载与backdoor API','amba/amba-axi.html','近期优先评估');
add('片上互连','AMBA ACE / ACE-Lite','ACE4/5及H/J/K','按设计端口核对一致性功能与AMBA bundle覆盖','amba/amba-ace.html');
add('片上互连','AMBA AHB / AHB-Lite','AHB2/3/5、Multi Layer','按实际AHB端口及IP单测需求选购','amba/amba-ahb.html');
add('片上互连','AMBA APB','APB2/3/4及D/E','若寄存器接口为APB则优先。确认bundle是否包含','amba/amba-apb.html','有APB端口时优先');
add('片上互连','AMBA ATB','Trace 总线','确认trace端口类型与测试角色','amba/amba-atb.html');
add('片上互连','AMBA AXI4-Stream','Stream master/slave/monitor','流接口需求，与AXI memory-mapped分开确认','amba/amba-stream.html');
add('片上互连','AMBA CXS','CXS A/B/C(Lite)/D','确认TX/RX、credit、链路激活与接口revision','amba/amba-cxs.html');
add('片上互连','AMBA CHI C2C','CHI C2C Issue A/B','官方说明依赖另行采购CHI VIP，需确认依赖授权','amba/amba-c2c.html','跨die方案确定后');
add('片上互连','AMBA DTI','DTI-H及向前规范；DTI-TBU/ATS','SMMU场景，确认TBUv5/ATSv5及实际端口支持','https://www.synopsys.com/blogs/chip-design/industry-first-verification-ip-arm-amb-dtih.html','有SMMU/DTI时评估','官方博客已确认');
add('片上互连','AMBA LPI','官方目录列出LPI','要求销售明确P/Q channel等具体支持和交付包',cat,'低功耗阶段评估',pending);
add('片上互连','TileLink','1.8.0/1.8.1；TL-UL/UH/C','按非Arm子系统实际需求','bus-interface/TileLink.html');
add('片上互连','OCP','Open Core Protocol','核实现有交付版本和在售状态','bus-interface/ocp.html');
add('片上互连','NoC 子系统验证方案','官方目录列为子系统项目','非独立标准协议。确认端到端检查、流量与性能方案',cat,'系统集成阶段评估',pending);
add('内存','DDR','DDR2/3/4/5；DIMM、3DS','含UDIMM/RDIMM/LRDIMM等覆盖。确认颗粒、组织方式、速率','memory/ddr5.html','接入真实DDR时');
add('内存','DDR5 MRDIMM / CKD','MRDIMM、MRCD/MDB、CSODIMM/CKD','DDR家族功能需求，不能据此认定独立SKU','memory/ddr5.html','按服务器内存方案');
add('内存','LPDDR','LPDDR2/3/4/5/5X/6','LPDDR6-PIM公开仅列命令采样支持，须明确行为模型边界','memory/ip-lpddr.html');
add('内存','HBM','HBM2/2E/3/4','确认通道、堆叠、容量和器件；HBM5另见待确认事项','memory/hbm-verificationip.html');
add('内存','GDDR6','GDDR6','GDDR7不从本页推断，需销售另证实','memory/gddr6.html');
add('内存','HMC','HMC 2.0','已有公开产品页，采购前确认现售和维护状态','memory/hmc-verification-ip.html');
add('内存','DFI','DFI 5.1/5.2；controller/PHY/monitor','核对DDR/LPDDR/HBM等组合。与DRAM器件VIP验证边界不同','memory/dfi-verification-ip.html','接入DDRC/PHY时');
add('内存','NVDIMM-P','DDR4/DDR5 NVDIMM-P','核实具体器件、revision及供货状态','memory/nvdimm-p.html');
add('内存','NVDIMM-N','官方目录列出','目录复用NVDIMM-P链接，独立支持范围需销售确认',cat,'按内存方案',pending);
add('Flash及卡','eMMC','eMMC 4.41/4.5/5.0/5.1；host/card','SD/UHS-II页面称属于eMMC VIP支持范围，避免重复授权','memory/emmc-verification-ip.html');
add('Flash及卡','SD Host / Card','页面列SD Physical Layer 4.2','eMMC VIP覆盖项；不据此认定SD Express最新版本支持','memory/sd-host-card.html');
add('Flash及卡','UHS-II / SD-TRAN','Host/Card','eMMC VIP覆盖项；核实是否独立选件','memory/uhs-ii-sd-tran.html');
add('Flash及卡','ONFI','页面列至ONFI 5.0','确认厂商器件、NAND组织和时序检查','memory/onfi.html');
add('Flash及卡','ToggleNAND','ToggleNAND 2.0/3.0/4.0','确认具体NAND器件与版本','memory/toggglenand.html');
add('Flash及外设','SPI Bus / Flash / SafeSPI','SPI、Dual/Quad/Octal、SafeSPI','同一产品页。确认Flash模型、xSPI revision及SafeSPI授权','memory/spi-qspi.html','有启动Flash时评估');
add('高速互连','PCI Express','Gen1–7；Gen8 Draft0.3有官方博客','确认RC/EP/PHY/Retimer、PIPE/SerDes、SR-IOV、IDE/DOE及draft release','pcie.html','按PCIe控制器计划');
add('高速互连','M-PCIe','官方旧目录列出','与PCIe页面共用链接，现售、维护及依赖需确认',cat,'有对应接口才考虑',pending);
add('高速互连','CCIX','官方完整方案含VIP；1.0/1.1','确认独立VIP SKU、支持矩阵及当前供货状态','https://www.synopsys.com/designware-ip/interface-ip/ccix.html','有对应接口才考虑','官方方案页已确认');
add('高速互连','CXL','1.1/2.0/3.0/4.0；io/cache/mem','确认Host、Type1/2/3、switch、层次及PCIe依赖授权','subsystems/compute-express-link.html','按CXL设计计划');
add('高速互连','UCIe','1.0/1.1/2.0/3.0；FDI/RDI/PHY','确认Adapter/PHY/full stack及PCIe/CXL/Streaming依赖','subsystems/vc-verification-ip-for-ucie.html','跨die方案确定后');
add('高速互连','UALink','UAL_200 1.0；多协议层','确认UPLI/物理接口、端口规模与交付release','ualink.html');
add('网络','Ethernet','10/100M至1.6T；MAC/PCS/PHY','核对Base-T、USXGMII、FlexE、AVB/TSN、MACsec、MDIO、FEC','ethernet/ethernet-1-6t.html','有以太网时评估');
add('网络','Ethernet AVB / TSN','AVB独立页面；Ethernet家族支持','功能需求，不能直接视为新增独立SKU','ethernet/ethernet-avb.html');
add('网络','Automotive Ethernet','车载以太网','确认100BASE-T1、1000BASE-T1等所需速率与物理接口','automotive/ethernet.html');
add('网络','Ultra Ethernet','公开页明确LLR、CBFC','不能据此推断完整UEC传输层覆盖；要求逐功能矩阵','ethernet/uec.html');
add('网络','Interlaken','1.2；Look-Aside/Retransmit 1.1','核对lane、带宽、角色和错误注入','bus-interface/interlaken.html');
add('网络','Fibre Channel','公开页列至128G','核对Initiator/Target、层次、速率','bus-interface/fibre-channel.html');
add('网络','CPRI','CPRI 7.0；RE/REC','确认串/并行接口、IQ及C&M能力','bus-interface/cpri.html');
add('USB','USB2 / eUSB2','USB2；eUSB2 V1/V2','确认Host/Device/Hub及Repeater/Native Controller','subsystems/verification-ip-usb2.html');
add('USB','USB3','USB3.0/3.1/3.2及USB2覆盖','与USB2授权有重叠，核对Host/Device/PHY/Hub/Retimer','usb/usb.html');
add('USB','USB4','USB4 V1/V2','确认Router/Retimer、USB/PCIe/DP tunneling及依赖包','subsystems/vc-verification-ip-usb4.html');
add('USB','USB Type-C / Power Delivery','PD 1.1/1.3/2.0/3.0/3.1','确认Cable/Receptacle、Source/Sink、Type-C及PD授权组合','usb/usb-power-delivery.html');
add('存储','NVMe','NVMe 1.2/1.3/1.4/2.0','确认PCIe/AXI/User Transport拓扑和所需依赖包','storage/nvme.html');
add('存储','SAS','SPL5；1.5/3/6/12/24G','确认Initiator/Target/Expander及SCSI/STP','storage/sas.html');
add('存储','SATA','Gen1/2/3；Host/Device/Port Multiplier','旧链接可能重定向，请销售确认现有交付版本','storage/sata.html','有对应接口才考虑','官方索引，交付待确认');
add('存储','UFS','UFS 2.x/3.x/4.0/5.0','含UniPro/M-PHY层关系；核实draft revision与独立授权','mipi/ufs.html');
add('MIPI','CSI-2','CSI-2 2.1/3.0/4.0；C/D-PHY','CSE2.0安全扩展已有官方博客，确认可交付版本及许可','mipi/mipi-csi-2.html');
add('MIPI','C-PHY','目录单列，链接至CSI-2页','确认PHY独立license或CSI/DSI组合包','mipi/mipi-csi-2.html');
add('MIPI','D-PHY','串行/PPI、HS、LPDT、ULPS、BTA','核对所需revision及与CSI/DSI授权重叠','mipi/d-phy.html');
add('MIPI','DSI / DSI-2','DSI-2 1.1/2.0、DSE1.1','核对C/D-PHY、Host/Device、DSC及组合包','mipi/mipi-dsi.html');
add('MIPI','I3C','CCC、DAA、Hot-Join、IBI、SDR/HDR','官方另有HDR multi-lane文章；确切revision需确认','mipi/mipi-13c.html');
add('MIPI','RFFE','射频前端控制','核对revision、角色和错误注入','mipi/vc-verification-ip-for-mipi-rffe.html');
add('MIPI','SLIMbus','低引脚数多媒体总线','核对revision及角色','mipi/slimbus.html');
add('MIPI','SoundWire','音频总线','核对revision、端口/通道、时钟与多从设备','mipi/soundwire.html');
add('MIPI','SPMI','系统电源管理接口','核对revision和主从角色','mipi/spmi.html');
add('MIPI','CSI-3','官方目录列出','询价项目，确认现售和可交付范围',cat,'有对应接口才考虑',pending);
add('MIPI','LLI','官方目录列出','询价项目，确认现售和可交付范围',cat,'有对应接口才考虑',pending);
add('MIPI','M-PHY','官方目录单列；UFS也覆盖相关层','确认独立VIP及随UFS授权边界',cat,'按UFS等接口需要',pending);
add('MIPI','UniPro','官方目录单列；UFS也覆盖相关层','确认独立VIP、revision及随UFS授权边界',cat,'按UFS等接口需要',pending);
add('显示','DisplayPort / eDP','DP1.4a/2.0/2.1a；eDP','核对Source/Sink/LTTPR/Branch、HDCP/DSC及USB4隧道','display/displayport.html');
add('显示','HDMI','HDMI1.4/2.0/2.1/2.2','核对HDCP、DSC、CEC、ARC/eARC；以release matrix为准','display/hdmi.html');
add('管理及外设','I2C','I2C','核对模式、速度、多主及错误注入','bus-interface/12c.html','有对应接口时评估');
add('管理及外设','I2S','音频接口、PCM等','核对对齐方式、格式和收发角色','bus-interface/12s.html');
add('管理及外设','SMBus','SMBus3.0、PEC/ARP/SMBALERT','公开页注明不含Host Notify，需复核最新release限制','bus-interface/smbus.html','BMC/管理场景评估');
add('管理及外设','UART','UART串行收发','核对格式、波特率、流控及错误注入','bus-interface/uart.html','有UART时评估');
add('管理及外设','JTAG','IEEE1149.1-2013','核对TAP/IR/DR、自定义指令和scan chain','bus-interface/jtag.html','有调试需求时评估');
add('管理及外设','SWD','Serial Wire Debug 5.0/5.2','核对DP/AP访问、多点调试及Arm调试拓扑','bus-interface/swd.html');
add('管理及外设','AVSBus','官方新文章确认AVSBus2.0','不等同完整PMBus命令层，核对域数与可交付release','https://www.synopsys.com/blogs/chip-design/multi-domain-voltage-control-verification-avsbus-2-vip.html','电源管理场景评估','官方博客已确认');
add('管理及外设','SDIO','SD I/O','核对host/device与SD memory授权边界','bus-interface/sdio.html');
add('汽车','CAN / CAN FD / CAN TT','CAN2.0/FD/TT','CAN XL需单独证实，不能从CAN FD推断','automotive/can20-fd-tt.html');
add('汽车','LIN','LIN2.2A','核对主/从、诊断、睡眠唤醒','automotive/lin-verification-ip.html');
add('汽车','FlexRay','3.0.1；1/2通道','核对2.5/5/10Mbps、角色和故障注入','automotive/flexray.html');

add('网络','JESD204','数据转换器串行接口','核对JESD204版本、lane及接口层次','bus-interface/vc-verification-ip-for-jesd204.html');

data.forEach(r => { r[14] = 'Synopsys 官方'; });
const questions = [
 ['商业目录','请提供当前完整VIP SKU及bundle清单','将本表每一行映射至SKU、License Feature及包内范围，补充未列出的可售产品。'],
 ['协议版本','精确规范与release矩阵是什么？','区分正式标准、draft、预览和研发路线图，列出已支持/未支持特性。'],
 ['角色与层次','每个VIP包含哪些角色和接口层？','确认master/slave/monitor，host/device，serial/PIPE/PPI/transaction-level及错误注入。'],
 ['依赖与重叠','哪些需要额外VIP或选件？','特别是CHI C2C→CHI，UFS→UniPro/M-PHY，USB4隧道，以及SD/UHS-II/eMMC、SPI各形态去重。'],
 ['仿真器兼容','VCS、Xcelium和UVM1.2精确组合支持？','要求双方约定版本的release matrix及可执行示例。不要只写“支持主流仿真器”。'],
 ['服务器环境','当前Linux发行版和glibc是否支持？','确认编译器、DPI库、位宽、依赖、安装权限及离线部署流程。'],
 ['并行回归','LSF回归怎样消耗license？','按仿真进程、实例、协议、端口还是token？同一test多个VIP消耗多少？给出并发例子。'],
 ['授权范围','授权期限、地域和项目范围是什么？','确认浮动池、跨服务器/站点、多项目复用、续费及版本升级权益。'],
 ['测试套件','Test Suite和验证计划是否包含？','逐协议确认源码用例、可修改权、coverage plan、错误场景及是否独立收费。'],
 ['系统检查','系统一致性、数据检查和性能组件是否包含？','核对interconnect model、system monitor、scoreboard、traffic profile及调试工具依赖。'],
 ['初期DDR替代','AXI slave memory responder能否满足冒烟？','需要镜像预装载、读写backdoor、字节使能、burst/ID/outstanding、错误和延迟可控。'],
 ['真实内存','DDR/DFI/颗粒模型覆盖哪些边界？','列器件型号、rank/DIMM、training、低功耗和时序检查；不把AXI memory responder当DDR验证。'],
 ['硬件辅助验证','RTL仿真与ZeBu/Palladium支持如何划分？','单独确认transactor/加速方案、平台版本、可综合部分和授权，不能由SV VIP推断可用。'],
 ['交付验收','可否用双方仿真器跑采购验收list？','包含正常/异常、reset、中断/低功耗（适用时）、coverage、monitor与预期失败检查。'],
 ['维护服务','维护、升级及问题响应约定？','确认FAE支持、缺陷修复、版本升级、文档培训和交付时间。'],
 ['报价','请逐项或bundle报价并列商业条件','填写SKU、Feature、并发数、币种、税、维护期、折扣基础及报价有效期，避免重复采购。'],
];
const extra = [
 ['待核实产品','CAN XL','现有CAN2.0/FD/TT不能证明CAN XL支持；请提供官方产品与release信息。',''],
 ['待核实产品','完整PMBus / MCTP','AVSBus不等于PMBus Part I/II或MCTP；服务器管理场景单独询价。',''],
 ['待核实产品','eSPI / LPC','本次未取得足够官方VIP证据，不代表不存在。',''],
 ['待核实产品','RoCE / InfiniBand','不从Ethernet或Ultra Ethernet支持推断完整协议VIP。',''],
 ['待核实产品','MIPI A-PHY','不能从C-PHY/D-PHY产品推断。',''],
 ['待核实产品','GDDR7','本次未核实可交付release和SKU，应由销售说明现有版本或路线图。',''],
 ['官方公告线索','DDR6','官方作者页已有2026-08-14介绍文章；交付release及GA状态待销售确认。','https://www.synopsys.com/authors/gaurav-kumar.html'],
 ['研发路线图','HBM5','官方文章表述正在开发，JEDEC Draft1.0-04；不能列作已确认可售交付。','https://www.synopsys.com/blogs/chip-design/ai-accelerators-hbm5-verification-ip.html'],
 ['配套方案','Synopsys Test Suites','按协议确认是否含源码、是否另售；AMBA与其它协议可能不同。',base+'verification-test-suites.html'],
 ['配套方案','UNH Ethernet Test Suites','官方目录列出，需确认当前提供方式及许可。',cat],
 ['配套方案','VC SoC AutoTestbench / AutoPerformance','环境生成与性能方案，单独询价，不计作独立协议VIP。',base+'amba.html'],
 ['补充版本证据','PCIe8 Draft0.3','官方博客确认草案支持；要求销售对照交付release确认。','https://www.synopsys.com/blogs/chip-design/pcie-8-0-verification-ip-ai-hpc-automotive.html'],
 ['补充功能证据','MIPI CSE2.0','CSI-2安全扩展需求，不能直接推断独立SKU。','https://www.synopsys.com/blogs/chip-design/streamlining-camera-security-validation-framework-using-synopsys-mipi-cse-v20-vip.html'],
 ['补充功能证据','I3C HDR multi-lane','官方博客有覆盖说明；具体规范revision请销售确认。','https://www.synopsys.com/blogs/chip-design/i3c-vip-hdr-multi-lane-verification.html'],
];

const wb = Workbook.create();
const sh = wb.worksheets.add('采购目录');
const q = wb.worksheets.add('采购确认');
for(const s of [sh,q]) { s.showGridLines=false; s.getRange('A1:P110').format.font={name:'Arial',size:11,color:'#243047'}; }
sh.tabColor='#253D68'; q.tabColor='#637595';
sh.getRange('A2').values=[['Synopsys VIP 采购候选目录']];
sh.getRange('A2').format.font={name:'Arial',size:16,bold:true,color:'#253D68'};
sh.getRange('A3').values=[['整理日期：2026-10-22。按公开协议/产品家族汇总，非完整商业SKU目录；在售状态、版本及授权以供应商书面确认为准。']];
sh.getRange('A4').values=[['适用项目：Arm N2 + CMN，单die最小系统；初期用AXI slave memory替代DDR。黄色列留给采购/销售回填，行数不等于license数量。']];
sh.getRange('A5').values=[[`目录含 ${data.length} 个采购需求条目。来源为Synopsys官方产品页、目录及博客；新版本/旧目录的证据状态逐项标注。`]];
sh.getRange('A3:P5').format.rowHeight=22;
const headers=['ID','类别','协议 / 家族','公开支持范围','采购关注点','本项目优先级','证据状态','选择采购','销售 SKU','License Feature','并发数','含 Test Suite','报价金额','币种','来源说明','官方来源 URL'];
sh.getRange('A7:P7').values=[headers];
sh.getRange(`A8:P${7+data.length}`).values=data;
const end=7+data.length;
const t=sh.tables.add(`A7:P${end}`,true,'VIPCatalog'); t.showFilterButton=true;
const widths=[11,17,28,44,54,22,23,14,25,26,12,17,18,11,18,75];
for(let i=0;i<widths.length;i++)sh.getRangeByIndexes(6,i,end-6,1).format.columnWidth=widths[i];
sh.getRange(`A8:P${end}`).format.rowHeight=62;
sh.getRange(`A8:P${end}`).format.wrapText=true;
sh.getRange(`A8:P${end}`).format.verticalAlignment='center';
sh.getRange('A7:N7').format={fill:'#253D68',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},horizontalAlignment:'center',verticalAlignment:'center',wrapText:true,rowHeight:33};
sh.getRange('P7').format={font:{name:'Arial',size:11,bold:true,color:'#637595'},wrapText:true};
sh.getRange(`H8:N${end}`).format.fill='#FFF2CC';
sh.getRange(`K8:K${end}`).setNumberFormat('0');
sh.getRange(`M8:M${end}`).setNumberFormat('#,##0.00');
sh.getRange(`H8:H${end}`).dataValidation={rule:{type:'list',values:['采购','不采购','待定']}};
sh.getRange(`L8:L${end}`).dataValidation={rule:{type:'list',values:['含','另购','不提供','待确认']}};
sh.getRange(`K8:K${end}`).dataValidation={rule:{type:'whole',operator:'greaterThanOrEqual',formula1:0}};
sh.getRange(`G8:G${end}`).conditionalFormats.add('containsText',{text:'待确认',format:{fill:'#FCE6CE',font:{color:'#9A5713'}}});
sh.freezePanes.freezeRows(7); sh.freezePanes.freezeColumns(3);

q.getRange('A2').values=[['采购确认与待核实项目']];q.getRange('A2').format.font={name:'Arial',size:16,bold:true,color:'#253D68'};
q.getRange('A3').values=[['请供应商填写答复与证据。下方“待核实产品 / 研发路线图”不表示已确认可售。']];
q.getRange('A5:D5').values=[['主题','确认问题','需求 / 验收依据','供应商答复']];
q.getRange(`A6:D${5+questions.length}`).values=questions.map(x=>[...x,'']);
const qend=5+questions.length;
q.tables.add(`A5:D${qend}`,true,'ProcurementQuestions');
q.getRange('A5:D5').format={fill:'#253D68',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},horizontalAlignment:'center',rowHeight:30};
q.getRange(`A6:D${qend}`).format.rowHeight=58;q.getRange(`A6:D${qend}`).format.wrapText=true;
q.getRange(`D6:D${qend}`).format.fill='#FFF2CC';
q.getRange('A24').values=[['待核实项目、配套方案与补充证据']];q.getRange('A24').format.font={name:'Arial',size:14,bold:true,color:'#253D68'};
q.getRange('A26:F26').values=[['类型','项目','当前证据 / 待确认范围','供应商答复','','官方来源 URL']];
q.getRange(`A27:F${26+extra.length}`).values=extra.map(x=>[x[0],x[1],x[2],'','',x[3]]);
q.tables.add(`A26:D${26+extra.length}`,true,'AdditionalItems');
q.getRange('A26:D26').format={fill:'#637595',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},horizontalAlignment:'center',rowHeight:30};
q.getRange(`A27:F${26+extra.length}`).format.rowHeight=62;q.getRange(`A27:F${26+extra.length}`).format.wrapText=true;
q.getRange(`D27:D${26+extra.length}`).format.fill='#FFF2CC';
for(const [col,width] of [['A',20],['B',43],['C',80],['D',58],['E',3],['F',80]])q.getRange(`${col}5:${col}40`).format.columnWidth=width;
q.getRange('A5:F40').format.verticalAlignment='center';
q.freezePanes.freezeRows(5);

if(new Set(data.map(x=>x[0])).size!==data.length)throw Error('Duplicate IDs');
if(new Set(data.map(x=>x[2])).size!==data.length)throw Error('Duplicate names');
if(data.some(x=>!x[15].startsWith('https://www.synopsys.com/')))throw Error('Nonofficial URL');
wb.recalculate();
console.log((await wb.inspect({kind:'region',sheetId:'采购目录',range:'A7:G11',maxChars:2200,tableMaxCellChars:65})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},summary:'Formula error scan'})).ndjson);
await fs.writeFile(new URL('catalog-preview.png',import.meta.url),new Uint8Array(await (await wb.render({sheetName:'采购目录',range:'A1:G13',scale:1,format:'png'})).arrayBuffer()));
await fs.writeFile(new URL('questions-preview.png',import.meta.url),new Uint8Array(await (await wb.render({sheetName:'采购确认',range:'A1:D11',scale:1,format:'png'})).arrayBuffer()));
await fs.writeFile(new URL('extras-preview.png',import.meta.url),new Uint8Array(await (await wb.render({sheetName:'采购确认',range:'A24:D32',scale:1,format:'png'})).arrayBuffer()));
const file = await SpreadsheetFile.exportXlsx(wb);
await file.save(decodeURIComponent(new URL('Synopsys_VIP采购清单_20261022.xlsx',import.meta.url).pathname.replace(/^\/(?:([A-Za-z]):)/,'$1:')));
await fs.writeFile(new URL('inventory.json',import.meta.url),JSON.stringify({headers,data,questions,extra},null,2));
console.log(JSON.stringify({rows:data.length,statusCounts:data.reduce((a,r)=>(a[r[6]]=(a[r[6]]||0)+1,a),{}),file:'Synopsys_VIP采购清单_20261022.xlsx'}));
