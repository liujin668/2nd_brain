from pathlib import Path
from html import escape
import re, sys, json
import pypdfium2 as pdfium
from pypdf import PdfReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                               Spacer, Table, TableStyle, Image, PageBreak,
                               KeepTogether)

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parent
SOURCE = Path(r'C:\Users\jinliu01\OneDrive - ARM China\文档\Specs\ARM\arm_neoverse_n2_core_trm_102099_0003_06_en.pdf')
OUT = ROOT / 'output/pdf/Neoverse-N2-Core-TRM-第3章-中文精读.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont('YaHei', r'C:\Windows\Fonts\msyh.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('YaHeiBold', r'C:\Windows\Fonts\msyhbd.ttc', subfontIndex=0))
pdfmetrics.registerFontFamily('YaHei', normal='YaHei', bold='YaHeiBold', italic='YaHei', boldItalic='YaHeiBold')
INK=colors.HexColor('#17304D'); BLUE=colors.HexColor('#17698C')
MUTED=colors.HexColor('#556477'); LIGHT=colors.HexColor('#EDF4F8')
RULE=colors.HexColor('#D6E0E8'); GREEN=colors.HexColor('#EFF6EF')
W,H=595.276,841.890
M=43; CW=W-2*M

S={
 'title': ParagraphStyle('title', fontName='YaHeiBold', fontSize=24, leading=34, textColor=INK, spaceAfter=12, wordWrap='CJK'),
 'sub': ParagraphStyle('sub', fontName='YaHei',fontSize=12,leading=19,textColor=MUTED,spaceAfter=12,wordWrap='CJK'),
 'h1': ParagraphStyle('h1',fontName='YaHeiBold',fontSize=18,leading=26,textColor=INK,spaceAfter=11,wordWrap='CJK'),
 'h2': ParagraphStyle('h2',fontName='YaHeiBold',fontSize=12.5,leading=20,textColor=BLUE,spaceBefore=11,spaceAfter=6,wordWrap='CJK'),
 'body': ParagraphStyle('body',fontName='YaHei',fontSize=10.5,leading=17.6,textColor=INK,spaceAfter=8,wordWrap='CJK'),
 'small': ParagraphStyle('small',fontName='YaHei',fontSize=8.6,leading=13.7,textColor=MUTED,spaceAfter=7,wordWrap='CJK'),
 'cell': ParagraphStyle('cell',fontName='YaHei',fontSize=9.3,leading=15,textColor=INK,wordWrap='CJK'),
 'cellsmall': ParagraphStyle('cellsmall',fontName='YaHei',fontSize=8.6,leading=13.4,textColor=INK,wordWrap='CJK'),
 'headcell': ParagraphStyle('headcell',fontName='YaHeiBold',fontSize=9.4,leading=15,textColor=colors.white,wordWrap='CJK'),
 'call': ParagraphStyle('call',fontName='YaHei',fontSize=10.3,leading=17.5,textColor=INK,wordWrap='CJK'),
}

story=[]
def p(t,style='body'):
    story.append(Paragraph(t,S[style]))
def h(t): p(t,'h2')
def source(t): p('原文定位：'+t,'small')
def call(t,fill=LIGHT):
    tb=Table([[Paragraph(t,S['call'])]],colWidths=[CW])
    tb.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),fill),('BOX',(0,0),(-1,-1),.5,RULE),
                           ('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),11),
                           ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
    story.extend([tb,Spacer(1,10)])
def table(headers,rows,widths=None,small=False):
    widths=widths or [CW/len(headers)]*len(headers)
    cs=S['cellsmall'] if small else S['cell']
    data=[[Paragraph(escape(str(x)),S['headcell']) for x in headers]]
    data += [[Paragraph(escape(str(x)).replace('\n','<br/>'),cs) for x in r] for r in rows]
    t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,LIGHT]),
                          ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
                          ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
                          ('LINEBELOW',(0,0),(-1,0),.5,INK),('LINEBELOW',(0,1),(-1,-1),.35,RULE)]))
    story.extend([t,Spacer(1,9)])
def page(title,loc):
    if story: story.append(PageBreak())
    p(title,'h1');source(loc)

# Crop the single original figure. The bounding box includes the original
# figure title, all component boxes, and the optional-component legend.
srcdoc=pdfium.PdfDocument(SOURCE)
srcpage=srcdoc[39]
scale=3.4
raw=srcpage.render(scale=scale).to_pil()
crop=raw.crop(tuple(round(v*scale) for v in (80,76,556,476)))
FIG=WORK/'figure-3-1-original.png'
crop.save(FIG)

# 1 - Overview, source scope, and reading map.
p('Neoverse N2 Core TRM','sub')
p('第 3 章 · 中文精读','title')
p('Technical overview｜从结构图理解 CPU 核如何工作','sub')
call('<b>本章的主线</b><br/>N2 先取得并译码指令，通过重命名与发射组织乱序执行；load/store 由数据存储系统处理，MMU/TLB 提供地址转换；私有 L2 经 CPU bridge 连接 DSU-110。监控、追踪和中断接口为整个执行过程提供观测与控制。')
h('本导读覆盖什么')
p('完整覆盖原文第 3 章的 <b>3.1 Core components、3.2 Interfaces、3.3 Programmers model</b>，对应 PDF 第 39-44 页。按模块职责、协作关系和易混淆点重新组织，不逐句翻译，也不从后续章节引入未经本章支持的微架构参数。')
table(['原文结构','阅读问题','本导读页码'],[
 ('3.1 Core components','结构图里的模块分别负责什么？','2-7'),
 ('3.2 Interfaces','一个 N2 核如何连接到外部 SoC？','6、8'),
 ('3.3 Programmers model','支持哪些执行状态与异常级别？','8'),
 ('综合理解与回查','一次执行怎样贯穿各模块？','9-10'),
], [120, CW-195,75])
h('依据与解释如何区分')
p('<b>原文要点</b>表示本章明确给出的事实；<b>理解说明 / 教学示例</b>用于解释机制，不代表原文公开了对应的详细实现。图 Figure 3-1 使用你提供的 PDF 原图截图，保留完整图例；本导读中的中文表格为重新归纳，本章没有原文表格。')
p('来源：Arm Neoverse N2 Core Technical Reference Manual，r0p3，Issue 06，Document ID 102099_0003_06_en；原文版本日期 2022-10-27。整理日期：2026-10-09。','small')
p('范围提醒：这份资料讲的是 <b>N2 CPU 核</b>。此前的 RD-N2 Reference Design 讲整套参考系统；不要把 RD-N2 的 32 核、CMN-700 或 DDR 配置当成本章对每个 N2 产品的固定要求。','small')

# 2 - Complete original figure and walkthrough.
page('3.1 核心组件：先读原图','§3.1，p.39-43；Figure 3-1，p.40')
story.append(Image(str(FIG),width=CW,height=CW*crop.height/crop.width))
p('<b>原图 Figure 3-1：</b>Neoverse N2 core components。截图来自原文第 40 页；包含标题、核心组件和绿色可选组件图例。','small')
h('按四组模块读图')
p('<b>① 指令前端：</b>左上 L1 instruction memory system；中上 instruction decode、register rename、instruction issue。它们把程序中的指令组织成可执行的内部操作。')
p('<b>② 执行与访存：</b>右上 integer/vector execution；中部 MMU 和 L1 data memory system；下方 L2 memory system。它们分别处理计算、地址转换和数据访问。')
p('<b>③ 观测与事件：</b>底部 trace、TRBE、PMU、ELA、GIC CPU interface。<b>④ 对外连接：</b>最底部 CPU bridge，连接 DSU-110。')
call('<b>读图注意：</b>绿色 Crypto 与 ELA 是图中标出的可选组件。正文还列出 AMU 和 SPE；没有在图中单独画出某个功能块，不能据此判断它不存在。本图是组件图，没有给出逐周期流水线、发射宽度或全部数据通路。')

# 3 - Front end.
page('3.1 指令前端：取得并理解指令','p.40：L1 instruction memory system、Instruction decode')
h('L1 指令存储系统：不只是一块 I-cache')
p('<b>原文要点：</b>指令存储系统从指令缓存取得指令，并向译码单元提供指令流；它还包含指令 TLB、L0 MOP cache 和动态分支预测器。')
table(['组件','原文明确的配置','作用与理解'],[
 ('L1 instruction cache','64KB；4-way set associative；64-byte cache line','缓存指令字节，减少从更远存储层次取指的需要。'),
 ('L1 instruction TLB','Fully associative；原生支持 4KB、16KB、64KB、2MB 页尺寸','缓存取指所需的地址转换信息；它不缓存指令内容。'),
 ('L0 Macro-OP cache','1536 entries；4-way skewed associative','保存已经译码并优化的内部指令，帮助提高性能。'),
 ('Dynamic branch predictor','本章未提供容量和算法参数','预测控制流走向，帮助前端决定接下来取哪里的指令。'),
], [114,176,CW-290])
p('<b>术语理解：</b>4-way set associative 是“4 路组相联”：一个组内有 4 个候选缓存位置；fully associative 是“全相联”。MOP 的 skewed associative 表示斜向相联组织，本章未说明具体索引规则，不能直接当成普通 4 路组相联。','small')
h('MOP cache 与 I-cache 的关键差别')
p('<b>理解说明：</b>I-cache 保存程序的指令字节；MOP cache 保存已经处理过的内部指令表示。一个常执行的代码片段可从缓存的内部表示中获益。1536 是条目数，不能直接当成字节容量，也不能推定为固定数量的源程序指令。')
h('Instruction decode：转换为内部格式')
p('<b>原文要点：</b>译码单元可将 AArch32 和 AArch64 指令转换成内部格式。<b>理解说明：</b>软件看到的体系结构指令和核内部用于调度、执行的操作不是同一层次；后续重命名和发射针对内部表示工作。')
call('<b>这一部分最值得记住：</b>取到指令、完成地址转换、完成译码是不同工作。I-cache、ITLB 和 MOP cache 分别服务于指令内容、地址映射和已译码表示。')

# 4 - Scheduling and execution.
page('3.1 重命名、发射与执行','p.41：Register rename、Instruction issue、Integer / Vector execute')
h('Register rename：为乱序执行整理依赖')
p('<b>原文要点：</b>重命名单元执行寄存器重命名，以支持 out-of-order execution，并把已译码指令分发到不同 issue queues。')
p('<b>理解说明：</b>体系结构寄存器名称属于软件接口；硬件可以通过重命名减少因名称复用产生的约束。但如果一条指令真正需要前一条指令的计算结果，重命名不能消除这种真实数据依赖。')
h('Instruction issue：决定什么时候执行')
p('<b>原文要点：</b>发射单元控制已译码指令何时送到执行流水线，包含保存待发射指令的 issue queues。<b>理解说明：</b>进入队列不等于已经执行；等待可能涉及操作数、依赖或可用执行资源。本章未给出队列深度与每周期发射数量。')
table(['执行部分','本章列出的能力','需要区分的概念'],[
 ('Integer execute','算术与逻辑数据处理','整数运算属于执行流水线的一部分。'),
 ('Advanced SIMD / FPU','SIMD；单精度、双精度浮点','NEON 是 Advanced SIMD 及相关实现/软件的常用名称。'),
 ('SVE / SVE2','执行 SVE 和 SVE2 指令','SVE 仅在 AArch64 执行状态定义；补充而不替代 Advanced SIMD/FPU。'),
 ('Crypto（可选）','AES；SHA-1/224/256/384/512；SM3/SM4；有限域运算','本章明确为可选扩展，基础产品不包含，需要额外许可。'),
], [123,190,CW-313])
p('<b>用途理解：</b>Advanced SIMD 主要面向音视频、图像、3D 图形和语音等数据并行处理。Crypto 指令加速 AES 加解密、SHA/SM3 哈希、SM4 加解密，以及 GCM、ECC 等算法使用的有限域运算；这些是指令扩展能力，不是独立的通用加密外设。','small')
h('一个依赖例子：为什么不是所有指令都能提前执行')
p('<b>教学示例：</b>“r1 = load(A)”之后的“r2 = r1 + 1”必须等待 load 的结果；而“r3 = r4 + r5”若与它独立，就可能在合适资源可用时先执行。这只说明乱序调度的思想，不是 N2 具体周期或执行端口的描述。')
call('<b>重要边界：</b>乱序执行说的是核内部组织计算的能力。它不能被理解为软件可观察行为任意乱序；本章也没有给出内存顺序规则或退休机制的详细实现。')

# 5 - Data side and MMU.
page('3.1 数据访存与 MMU：内容和地址分开看','p.42：L1 data memory system、Memory Management Unit')
h('L1 data memory system：load、store 和一致性请求')
p('<b>原文要点：</b>数据存储系统执行 load/store，并处理 memory coherency requests。其 L1 D-cache 为 <b>64KB、4-way set associative、64-byte cache line</b>。')
table(['对比','L1 instruction TLB','L1 data TLB'],[
 ('相联方式','Fully associative','Fully associative'),
 ('原生支持的页/块尺寸','4KB、16KB、64KB、2MB','4KB、16KB、64KB 页；2MB、512MB 块'),
 ('服务对象','取指地址转换','load/store 的地址转换'),
], [95, CW/2-47.5,CW/2-47.5])
p('<b>理解说明：</b>cache line 与 page/block 是不同层次：64 字节 cache line 描述数据缓存的存储/访问粒度；页或块尺寸属于地址转换映射。不能把“支持 2MB 映射”理解为一次缓存 2MB 数据。')
h('MMU 与 TLB 怎样配合')
p('<b>原文要点：</b>MMU 依据 translation tables 中的虚拟到物理地址映射和 memory attributes，提供细粒度的内存系统控制；地址转换后的信息保存到 TLB。')
p('<b>理解说明：</b>页表是映射与属性的依据，TLB 是转换结果的缓存。TLB 命中可以减少重新获取转换信息的工作；D-cache 命中说明所需数据可能已经在近端。二者各自命中或缺失，不应混为一次“缓存命中”。')
h('ASID / VMID：识别映射属于谁')
p('原文说明 TLB 条目包含 global、ASID 和 VMID 等信息，以减少上下文或虚拟机切换时的失效需求。<b>理解说明：</b>相同虚拟地址在不同进程/虚拟机中可能指向不同物理内存；标识可以帮助区分条目。它不意味着切换、修改页表或复用标识时永远无需 TLB maintenance。')
call('<b>对 CHI 学习的连接：</b>CPU 私有缓存属于系统一致性参与者。一次 load/store 的地址和权限问题，与缓存副本及最新数据来源问题，都需要正确处理；本章只概括各模块职责，没有逐条规定 CHI 事务。')

# 6 - L2 bridge, interfaces.
page('3.1 私有 L2、CPU bridge 与 DSU-110','p.39、42-43：L2 memory system、CPU bridge；§3.2 Interfaces')
h('L2 是本核私有缓存')
table(['项目','本章结论'],[
 ('归属','Private to the core：属于单个 N2 核。'),
 ('相联方式','8-way set associative。'),
 ('RAM 容量配置','512KB 或 1024KB。'),
 ('对外连接','L2 memory system 通过 CPU bridge 连接 DSU-110。'),
], [140,CW-140])
p('<b>理解说明：</b>“可配置 512KB / 1024KB”是产品集成配置能力，不能从本章推定软件能在运行中任意切换容量。也不能把一个核的 L2 看成所有核共享的统一缓存。')
h('CPU bridge：缓冲和跨时钟同步')
p('<b>原文要点：</b>每个 N2 核与 DSU-110 之间有一个 CPU bridge；桥负责 buffering 与 synchronization。桥采用异步方式，允许各核选择不同频率、功耗和面积实现点；也可配置为同步运行。')
p('原文还说明，把 CPU bridge 配成同步不会改变 debug、trace 等其他接口，它们始终是异步的。<b>理解说明：</b>“桥可同步”不是“整颗芯片所有接口都同步”。')
h('怎样读核与系统之间的边界')
call('<b>本章明确的连接关系：</b><br/>N2 core / L2 memory system → CPU bridge → DSU-110 → 外部存储系统与 SoC<br/><br/>§3.2 说明 DSU-110 管理 N2 核到 SoC 的外部接口。接口细节应查 DSU-110 TRM，不能根据本章的组件图推导完整 CHI 通道、位宽或系统拓扑。')
h('与之前 RD-N2 文档的关系')
p('本章给出 CPU IP 的连接边界；RD-N2 则选择特定 DSU、互连和缓存配置来集成系统。阅读两份资料时，先标明讨论层次：<b>核心组件 → 集群/DSU 接口 → 系统互连与内存</b>。本章没有规定所有 N2 系统必须使用 32 核、CMN-700 或某种 DDR。')

# 7 - Monitoring, trace, GIC.
page('3.1 监测、追踪与中断','p.39、42-43：Trace / TRBE、PMU、SPE、AMU、GIC CPU interface')
table(['模块','原文要点','理解时关注'],[
 ('PMU','6 个可配置的性能监测器，可统计核与内存系统运行情况。','主要帮助回答某类事件发生多少次。不要据此推定全部计数器和事件的详细组织。'),
 ('SPE','N2 实现可选的 Statistical Profiling Extension，提供已执行指令的统计性能视图。','侧重采样分析；“optional”修饰架构扩展，本章明确写 N2 implements，不能直接视为图中绿色可裁剪块。'),
 ('ETE / TRBE','Embedded Trace Extension（嵌入式追踪扩展）与 Trace Buffer Extension（追踪缓冲扩展）；支持 trace unit 和 trace buffer。','用于观察执行相关信息，追踪格式、过滤和保存方式由后续章节规定。'),
 ('CoreSight ROM table','调试器可发现已实现的 CoreSight 组件。','ROM table 是组件发现机制，不是普通程序的代码缓存。'),
 ('ELA','Figure 3-1 标为可选；细节见 Configuration and Integration Manual。','不把未公开的 ELA 能力或连接方式填入本章。'),
 ('AMU','在本章主模块列表中列出 Activity Monitors Unit（活动监测单元）。','本章没有展开计数器定义；进一步查第 21 章。'),
 ('GIC CPU interface','配合外部 distributor，支持和管理 cluster 中断。','这是 CPU 侧接口，不等于把完整系统 GIC 都包含在核里。'),
], [100,205,CW-305],small=True)
h('它们为什么不能相互替代')
p('<b>理解说明：</b>PMU 更偏向事件统计；SPE 更偏向抽样定位；trace 更偏向执行路径观测；中断接口则处理事件通知与响应。看到“代码慢”，可能先用统计判断大类，再用采样或追踪缩小问题范围；收到中断本身不是一次性能分析。')
call('<b>边界提醒：</b>本章介绍“有这些能力”，并未给出事件编码、采样精度、trace 带宽、全部寄存器和中断状态机。相关细节应回查本导读第 10 页的原文索引。')

# 8 - Original 3.2 and 3.3.
page('3.2 接口与 3.3 编程模型','§3.2-3.3，p.43-44')
h('3.2 Interfaces：外部接口由 DSU-110 管理')
p('本节非常简短，核心结论是：<b>DSU-110 管理 N2 core 对 SoC 的外部接口</b>。原文将详细接口说明指向 DSU-110 TRM 的 Technical overview。第三章结构图中的 CPU bridge 是理解这个边界的入口。')
h('3.3 Programmers model：软件看到什么')
p('<b>原文要点：</b>N2 实现 Armv9.0-A。原文说明 Armv9.0-A 扩展了 Armv8-A 体系中截至 Armv8.5-A 定义的架构。本章给出执行状态和异常级别支持范围，详细编程模型由 A-profile Architecture Reference Manual 定义；通用定时器等架构功能遵循 §2.4 所列标准。')
table(['执行状态','本章明确支持的范围','直接含义'],[
 ('AArch32','EL0','可以支持 32 位用户态执行；不代表支持 32 位内核或 32 位 hypervisor。'),
 ('AArch64','EL0、EL1、EL2、EL3','64 位执行状态覆盖用户态与更高特权级软件。'),
], [105,130,CW-235])
table(['异常级别','常见用途：帮助理解，不是全部规则'],[
 ('EL0','用户态应用。'),
 ('EL1','操作系统内核等特权软件。'),
 ('EL2','Hypervisor / 虚拟化相关软件。'),
 ('EL3','最高特权的安全监控与固件相关功能。'),
], [105,CW-105])
h('三组概念不要混用')
p('<b>AArch32 / AArch64</b>描述执行状态；<b>EL0-EL3</b>描述异常级别；<b>Secure / Non-secure</b>属于安全状态维度。它们不是同一组标签。本章支持范围不能替代架构手册中对异常路由、切换和权限的具体规定。')
call('<b>与向量扩展一起记：</b>AArch32 支持只到 EL0；SVE 在 AArch64 执行状态中定义。不能因为 N2 能译码 AArch32，就认为 32 位程序可以直接执行 SVE 指令。')

# 9 - Integrative example and comprehension questions.
page('综合理解：把组件连成一次工作过程','教学解释，依据 §3.1-3.3 的模块职责；不表示逐周期实现')
h('示例：循环读取数组，计算后写回')
table(['阶段','可能参与的模块','这一阶段解决什么'],[
 ('1. 决定取指位置','动态分支预测；指令存储系统','循环和分支使下一取指地址需要控制流判断。'),
 ('2. 获得指令及内部表示','ITLB、I-cache、MOP cache、decode','分别处理取指地址、指令内容和内部表示；不要求每次都走全部路径。'),
 ('3. 组织待执行工作','Register rename、issue queues、instruction issue','记录依赖，安排可执行操作进入相应流水线。'),
 ('4. 读取数组数据','L1 data memory system、DTLB、MMU、缓存层次','确认地址映射与属性，并取得所需数据。'),
 ('5. 进行计算','Integer / Vector execute','使用相应执行能力；标量循环不会自动等同于 SVE 执行。'),
 ('6. 保存结果与处理系统交互','数据存储系统、私有 L2、bridge / DSU（按需）','访问是否到更远层次取决于缓存和事务情况；不等于每次 store 都写到 DDR。'),
 ('7. 观测或处理中断','PMU、SPE、trace、GIC CPU interface','统计、采样、追踪或响应事件，各有不同职责。'),
], [100,180,CW-280],small=True)
h('用五个问题检查自己是否看懂')
p('① I-cache 与 MOP cache 保存的内容有什么不同？<br/>② ITLB / DTLB 命中为什么不等于指令或数据 cache 命中？<br/>③ 重命名为什么不能消除 load 结果被后续加法真正使用的依赖？<br/>④ private L2、CPU bridge 和 DSU-110 分别解决哪一层问题？<br/>⑤ N2 支持 AArch32 为什么不意味着它支持 32 位内核？')
call('<b>答案提要：</b>指令字节 / 已译码表示；地址转换 / 内容缓存；真实结果依赖仍存在；本核缓存 / 缓冲同步 / 系统接入；AArch32 的支持范围仅为 EL0。')

# 10 - complete source map and boundaries.
page('精华回查：参数、来源与阅读边界','第三章 p.39-44；后续章节页码来自本手册目录/相关信息')
table(['记忆锚点','原文依据'],[
 ('L1 I-cache：64KB / 4-way / 64B line；MOP：1536 entries / 4-way skewed associative','p.40'),
 ('重命名支持乱序执行；issue queues 保存待发射指令；整数与向量执行职责','p.41'),
 ('Crypto 可选；SVE 仅 AArch64，补充 Advanced SIMD/FPU','p.41-42'),
 ('L1 D-cache：64KB / 4-way / 64B line；数据 TLB 支持 2MB、512MB 块','p.42'),
 ('L2：本核私有 / 8-way / 512KB 或 1024KB','p.42'),
 ('CPU bridge 可异步或配置同步；debug、trace 保持异步','p.43'),
 ('外部接口由 DSU-110 管理；AArch32 仅 EL0；AArch64 为 EL0-EL3','p.43'),
], [CW-85,85],small=True)
h('想继续深入时，去哪里查')
table(['主题','本手册位置'],[
 ('MMU / TLB；L1 指令；L1 数据；L2','第 6 / 7 / 8 / 9 章：p.57 / 65 / 69 / 74'),
 ('GIC CPU interface；PMU','第 12 / 18 章：p.101 / 122'),
 ('ETE / TRBE；AMU；SPE','第 19 / 20 / 21 / 22 章：p.137 / 150 / 151 / 156'),
 ('外部接口、DSU 组织','DSU-110 TRM；本章 §3.2 的相关文档入口'),
 ('EL、执行状态、架构行为','A-profile Architecture Reference Manual'),
], [205,CW-205],small=True)
h('本章没有给出的参数：保持空白，不自行填数')
p('未给出译码/发射宽度、ROB 或 issue queue 容量、执行端口数、指令周期、分支预测器容量、MOP 命中/填充细节、具体 TLB 条目数、全部 CHI 对外参数与 SoC 配置。也不能从本章推定具体芯片频率、IPC、功耗或跑分。','small')
p('固定组织与可选项：章首描述主要功能块的组织，Figure 3-1 用绿色单独标出 Crypto 与 ELA 的可选性；SPE 在正文中有自身的架构扩展描述。应分别保留原文口径，不能笼统写成“图中所有模块永远不可选”或“所有扩展都默认裁剪”。','small')
p('图片溯源：本导读第 2 页仅使用原文 Figure 3-1 的截图；本章无原文表格。其他中文表格与教学例子均为本导读的归纳解释。','small')

class Doc(BaseDocTemplate):
    def afterFlowable(self,flowable):
        if isinstance(flowable,Paragraph) and flowable.style.name in ('title','h1'):
            title=flowable.getPlainText(); key='s'+str(self.page)
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title,key,level=0,closed=False)

def chrome(canvas,doc):
    canvas.saveState()
    canvas.setFillColor(INK);canvas.rect(0,H-8,W,8,fill=1,stroke=0)
    canvas.setFont('YaHei',8.3);canvas.setFillColor(MUTED)
    if doc.page>1:
        canvas.drawString(M,H-30,'Neoverse N2 Core TRM  |  第 3 章中文精读')
        canvas.drawRightString(W-M,H-30,'r0p3 · Issue 06')
    canvas.setStrokeColor(RULE);canvas.line(M,39,W-M,39)
    canvas.setFont('YaHei',8);canvas.drawString(M,24,'原文 102099_0003_06_en · 第 39-44 页  |  中文学习导读')
    canvas.drawRightString(W-M,24,f'{doc.page}')
    canvas.restoreState()

doc=Doc(str(OUT),pagesize=(W,H),leftMargin=M,rightMargin=M,topMargin=53,bottomMargin=52,
        title='Neoverse N2 Core TRM - 第3章中文精读',author='中文技术导读',
        subject='Technical overview：核心组件、接口与编程模型')
doc.addPageTemplates([PageTemplate(id='main',frames=[Frame(M,52,CW,H-105,id='f',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=chrome)])
doc.build(story)

# Render every final page for QA. Store a contact sheet as a quick overview.
final=pdfium.PdfDocument(OUT)
from PIL import Image as PILImage, ImageDraw, ImageFont
thumbs=[]
for i in range(len(final)):
    img=final[i].render(scale=1.5).to_pil();img.save(WORK/f'qa-{i+1:02}.png')
    th=img.copy();th.thumbnail((285,420));thumbs.append(th)
cols=4; rows=(len(thumbs)+cols-1)//cols
sheet=PILImage.new('RGB',(cols*310,rows*465),'#DCE3EB');dr=ImageDraw.Draw(sheet)
ft=ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc',18)
for i,th in enumerate(thumbs):
    x=(i%cols)*310+12;y=(i//cols)*465+30;sheet.paste(th,(x,y));dr.text((x,y-25),f'PAGE {i+1}',font=ft,fill='#17304D')
sheet.save(WORK/'qa-contact.png')
reader=PdfReader(OUT)
print(json.dumps({'output':str(OUT),'pages':len(reader.pages),'bytes':OUT.stat().st_size,'original_figure':str(FIG),'qa_contact':str(WORK/'qa-contact.png')},ensure_ascii=False))
