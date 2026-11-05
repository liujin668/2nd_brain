from pathlib import Path
import json,re,html,sys,math
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, XPreformatted, Image, KeepTogether, Table, TableStyle
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.enums import TA_LEFT, TA_CENTER

sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parent
WORKSPACE=ROOT.parents[2]
OUTPUT=WORKSPACE/'output/pdf'
OUTPUT.mkdir(parents=True,exist_ok=True)
PDF=OUTPUT/'Easier_UVM_参考指南_中文译本_含Linux_VCS部署.pdf'
for name,path in [('CN',r'C:\Windows\Fonts\msyh.ttc'),('CNBold',r'C:\Windows\Fonts\msyhbd.ttc'),('Mono',r'C:\Windows\Fonts\consola.ttf'),('Symbols',r'C:\Windows\Fonts\seguisym.ttf')]:
    pdfmetrics.registerFont(TTFont(name,path,subfontIndex=0))
pdfmetrics.registerFontFamily('CN',normal='CN',bold='CNBold',italic='CN',boldItalic='CNBold')
NAVY=colors.HexColor('#18364A');BLUE=colors.HexColor('#176B8F');GREY=colors.HexColor('#5B6570');PALE=colors.HexColor('#F2F5F7')
WIDTH,HEIGHT=A4;LEFT=50;RIGHT=50;BODY=WIDTH-LEFT-RIGHT
styles={
 'body':ParagraphStyle('Body',fontName='CN',fontSize=10.2,leading=16.1,spaceAfter=7.4,rightIndent=12,wordWrap='CJK',textColor=NAVY,allowWidows=0,allowOrphans=0),
 'chapter':ParagraphStyle('Chapter',fontName='CNBold',fontSize=16.2,leading=23,spaceBefore=15,spaceAfter=11,keepWithNext=True,wordWrap='CJK',textColor=BLUE),
 'sub':ParagraphStyle('Sub',fontName='CNBold',fontSize=11.7,leading=18,spaceBefore=9,spaceAfter=6,keepWithNext=True,wordWrap='CJK',textColor=NAVY),
 'small':ParagraphStyle('Small',fontName='CN',fontSize=8.4,leading=13.2,spaceAfter=6,wordWrap='CJK',textColor=GREY),
 'caption':ParagraphStyle('Caption',fontName='CNBold',fontSize=9.3,leading=14,spaceBefore=5,spaceAfter=7,alignment=TA_CENTER,wordWrap='CJK',textColor=BLUE),
 'code':ParagraphStyle('Code',fontName='Mono',fontSize=8.0,leading=10.4,spaceBefore=6,spaceAfter=9,leftIndent=7,rightIndent=7,backColor=PALE,borderPadding=5,textColor=NAVY),
 'cover':ParagraphStyle('Cover',fontName='CNBold',fontSize=26,leading=37,spaceAfter=16,textColor=NAVY,wordWrap='CJK'),
 'cover_en':ParagraphStyle('CoverEN',fontName='Helvetica',fontSize=14,leading=20,spaceAfter=28,textColor=GREY),
}
styles['bullet']=ParagraphStyle('Bullet',parent=styles['body'],leftIndent=13,firstLineIndent=-9,spaceAfter=5.5)

DASHES=dict.fromkeys(map(ord,'‐‑‒–—−'),' - ')
def rich(text):
    text=text.translate(DASHES)
    text=re.sub(r'(?: - ){2,}', ' - ', text)
    text=re.sub(r'(?<=[\u4e00-\u9fff])agent', ' agent', text)
    text=re.sub(r'agent(?=[\u4e00-\u9fff])','agent ',text)
    escaped=html.escape(text)
    # Literal SV backticks (e.g. `include) are not Markdown delimiters.
    # Keep prose in the CJK font, whose glyph coverage is verified.
    return escaped
def para(text,style='body'):
    return Paragraph(rich(text),styles[style])
def code(text):
    # Preserve all original code characters. Use a symbol font for tree arrows.
    raw=html.escape(text).replace('↳','<font name="Symbols">↳</font>')
    flow=XPreformatted(raw,styles['code'])
    return flow

def page_frame(c,doc):
    if doc.page==1:return
    c.saveState();c.setStrokeColor(colors.HexColor('#CBD5DC'));c.setLineWidth(.5)
    c.line(LEFT,HEIGHT-38,WIDTH-RIGHT,HEIGHT-38)
    c.setFont('CN',8);c.setFillColor(GREY)
    c.drawString(LEFT,HEIGHT-29,'Easier UVM 代码生成器参考指南 | 中文译本')
    c.line(LEFT,36,WIDTH-RIGHT,36)
    c.drawString(LEFT,24,'原文：Doulos  |  实施附录：Linux + VCS')
    c.drawRightString(WIDTH-RIGHT,24,str(doc.page))
    c.restoreState()

class Document(BaseDocTemplate):
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw)
        self.addPageTemplates(PageTemplate(id='main',frames=[Frame(LEFT,49,BODY,HEIGHT-101,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page_frame))
    def afterFlowable(self,flow):
        if isinstance(flow,Paragraph) and hasattr(flow,'toc_key'):
            self.canv.bookmarkPage(flow.toc_key)
            self.canv.addOutlineEntry(flow.getPlainText(),flow.toc_key,0,False)
            self.notify('TOCEntry',(0,flow.getPlainText(),self.page,flow.toc_key))

blocks=json.loads((ROOT/'blocks.json').read_text(encoding='utf-8'))
zh={}
for n in range(1,4):zh.update(json.loads((ROOT/f'part{n}_zh.json').read_text(encoding='utf-8')))
expected={b['id'] for b in blocks if b['type'] not in ['code','image']}
assert set(zh)==expected
assert sum(b['type']=='code' for b in blocks)==140
assert sum(b['type']=='image' for b in blocks)==3
source_pages={'b0000':'1-3','b0025':'3-4','b0033':'4-5','b0046':'5-17','b0191':'17-19','b0201':'19-26','b0293':'26-29','b0312':'29-30','b0324':'30-31','b0333':'31-35','b0345':'35-36','b0361':'36-37','b0367':'37','b0372':'37-38','b0375':'38-40','b0383':'40-41','b0390':'41','b0399':'42'}
legends={
 'b0009':'图内术语：Input Files = 输入文件；Interface Template File = 接口模板文件；Common Template File = 通用模板文件；Pin List File = 引脚列表文件；DUT Directory = DUT 源目录；Include Directory = 用户包含文件目录；Code Generator = 代码生成器；Output Files = 输出文件；Simulation scripts = 仿真脚本。目录名和类名保持英文。',
 'b0295':'图内术语：Top-level env = 顶层环境；Scoreboard = 记分板；Configuration object = 配置对象；Queues = 队列；Producers = 产生源；Reference Model = 参考模型。DUT 队列保存实际响应，REF 队列保存预期响应；ref_model_input/ref_model_output 是模板设置名。',
 'b0335':'图内术语：Test = 测试；Env = 环境；Config = 配置；Subscriber = 订阅器；Scoreboard = 记分板；Virtual sequence = 虚拟序列；Register layer = 寄存器层；Sequence = 序列；Seqr = 序列仲裁器；Monitor = 监视器；Driver = 驱动器；Test harness = 测试支架；Interface = 接口。'}
story=[]
story += [Spacer(1,60),para('Easier UVM\n代码生成器参考指南'.replace('\n',' '),'cover'),Paragraph('Easier UVM Code Generator<br/>Reference Guide',styles['cover_en']),para('中文全译本 + Linux / VCS 实施附录','sub'),Spacer(1,22)]
for text in ['原作：Doulos','对应原网页版本：2016-04-18；用户提供的打印件：42 页','译文整理日期：2026-10-26','译文包含全部 264 条正文、标题与列表条目，保留 140 段代码/命令和 3 幅原图。']:
    story.append(para(text))
story += [Spacer(1,26),para('正文为原文翻译；末尾“实施附录”是针对 Linux + VCS 的补充建议，单独标识，不属于原文。代码、参数名、文件名、取值和版本日期保留英文；原图下方提供中文术语对照。','small')]
story += [PageBreak(),para('阅读说明','chapter')]
for text in [
 '原件由网页打印为图片型 PDF。本译本对 42 页逐页进行了文字识别，并与对应的 Doulos 官方参考页交叉核对，以恢复代码、参数和长段说明。译文重新排版，页码与原文不同；各节注明原件页码范围。',
 '代码和命令按原文保留，包括英文注释，以便与原发行包核对。层次图中的箭头由支持该字形的字体呈现；代码中的缩进和声明顺序保留。',
 '正文忠实保留 2016 年文档使用的工具名和安装方式。原文要求以 root 安装 Perl 模块的内容只作为翻译保留；你的 Linux 工作服务器建议优先使用现有公司环境或用户目录，参见实施附录。',
 '原文几处标识符或措辞存在疑点：trans_var_enum、req_seq_inc、agent_has env，以及 top_env_generate_methods_inside/after_class 的合写形式。译文保留原写法；实际配置应与所下载版本的脚本、帮助和示例核对，不能把这些疑点直接当成新选项。',
 '原文对 reg_cover_inc 的覆盖组包含位置有历史说明；其后又明确要求包含名为 m_cov 的完整覆盖组。应以实际生成代码及对应版本示例为准。']:
    story.append(para(text))
terms=[['英文','统一译法'],['agent / env','agent 组件 / 环境'],['transaction / sequence','事务 / 序列'],['sequencer','序列仲裁器'],['driver / monitor','驱动器 / 监视器'],['reference model / scoreboard','参考模型 / 记分板'],['test harness / covergroup','测试支架 / 覆盖组']]
t=Table([[para(cell,'small') for cell in row] for row in terms],colWidths=[200,BODY-200],hAlign='LEFT')
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#C7D1D9')),('BOTTOMPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5)]))
story += [t,Spacer(1,12),Paragraph('原文对照：<link href="https://www.doulos.com/knowhow/systemverilog/uvm/easier-uvm/easier-uvm-code-generator/easier-uvm-code-generator-reference-guide" color="#176B8F">Doulos 官方参考指南</link>',styles['small']),PageBreak(),para('目录','chapter')]
toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC0',fontName='CN',fontSize=10,leading=15.4,firstLineIndent=0,leftIndent=0,rightIndent=18,spaceBefore=4,textColor=NAVY,wordWrap='CJK')]
story += [toc,PageBreak()]
major={'b0000','b0046','b0201','b0293','b0333'}
chapter_index=0
for i,b in enumerate(blocks):
    typ=b['type'];bid=b['id']
    if typ=='h1':
        if bid in major and i>0:story.append(PageBreak())
        chapter_index+=1
        title=f'{chapter_index:02d}  {zh[bid]}'
        p=para(title,'chapter');p.toc_key=bid;story.append(p)
        story.append(para('原件页码：'+source_pages[bid],'small'))
    elif typ=='h2':story.append(para(zh[bid].lstrip('☆ ').strip(),'sub'))
    elif typ=='bullet':story.append(para('• '+zh[bid],'bullet'))
    elif typ=='code':
        c=code(b['text'])
        story.append(KeepTogether([c]) if len(b['text'].splitlines())>20 else c)
    elif typ=='image':
        image=Image(str(ROOT/(bid+'.png')))
        ratio=min(BODY/image.imageWidth,490/image.imageHeight)
        image.drawWidth=image.imageWidth*ratio;image.drawHeight=image.imageHeight*ratio
        story.append(KeepTogether([image,Spacer(1,5),para(legends[bid],'small')]))
    elif b['text'].startswith('Figure:'):story.append(para(zh[bid],'caption'))
    else:story.append(para(zh[bid]))

# Editorial implementation appendix, deliberately separate from the translation.
story.append(PageBreak())
p=para('附录 A  在 Linux + VCS 工作服务器上落地','chapter');p.toc_key='appendix-linux-vcs';story.append(p)
story.append(para('本附录为实施建议，不属于原文翻译。已知条件是 Linux + VCS；具体 VCS release、UVM 版本及公司工具环境脚本尚未提供，所以下列路径和示例模板名需要替换为实际值。'))
appendix=[
 ('sub','A.1  先确定三种不同的“成功”'),
 ('bullet','生成成功：Perl 生成器读取模板、include 和 DUT 输入，产生 SV 骨架与仿真脚本。此步骤本身不需要 VCS 仿真许可证。'),
 ('bullet','骨架跑通：VCS 能编译、启动 UVM 测试并按预期结束，说明编译链和基本连接可用。'),
 ('bullet','真实 DUT 验证成功：driver 真正驱动协议，monitor 正确还原事务，scoreboard/断言能够识别故意注入的错误。默认示例打印 transaction 不能代替这些工作。'),
 ('sub','A.2  获取和保存官方生成器'),
 ('p','从 Doulos 官方 Easier UVM 页面进入下载入口。当前入口要求填写登记信息；应由你本人按公司流程下载，不假设存在稳定的公开 ZIP 直链。将原始发行包、版本说明及校验值保存在受版本管理的工具目录。无外网服务器可通过公司批准的渠道接收发行包及离线 Perl 依赖。'),
 ('p','建议目录职责：tools/ 保存生成器；templates/ 保存 .tpl 和 pinlist；rtl_input/ 保存所需 RTL 与 files.f；include/ 保存用户代码；生成目录只作为可重复构建产物。首次先使用官方发行包中的 minimal 示例，目录名称以解压后实物为准。'),
 ('sub','A.3  加载公司工具环境，检查前提'),
 ('p','先运行你们已有的 VCS 环境设置脚本或工具模块命令。不要另造许可证地址，也不要在不清楚原配置时覆盖公司环境。以下命令只用于检查：'),
 ('code',"command -v perl vcs vlogan gcc g++ make\nperl -e 'require 5.008; print \"Perl $^V\\n\"'\nperl -MFile::Copy::Recursive -e 1\nperl -MFile::stat -e 1\nvcs -ID"),
 ('p','Perl 要求至少 5.8.0。File::Copy::Recursive 是需要核对的非核心依赖；现代 Perl 中 File::stat 通常属于核心模块，缺失时先排查 Perl 版本和 @INC。原文虽在安装段开头列出 Time::Piece，随后又明确指出 2015-06 之后不再要求它，因此只作为旧版兼容检查。vcs -ID 不能证明仿真许可证已经成功签出，仍需实际编译和运行。'),
 ('sub','A.4  无 root 安装 Perl 模块'),
 ('p','优先使用公司已经提供的 Perl 模块。如果已有 cpanm 且允许联网，可安装到自己的用户目录：'),
 ('code','cpanm --local-lib="$HOME/perl5" local::lib File::Copy::Recursive\neval "$(perl -I\"$HOME/perl5/lib/perl5\" -Mlocal::lib=\"$HOME/perl5\")"\nperl -MFile::Copy::Recursive -MFile::stat -e \'print "Perl modules OK\\n"\''),
 ('p','如果没有 cpanm 或服务器不能联网，请让 IT 提供本地 Perl 库或离线模块包，并按公司约定配置 PERL5LIB。不要把原文的 root 安装命令直接当成普通工作账号的操作前提。'),
 ('sub','A.5  先运行官方最小示例'),
 ('p','将 minimal 示例复制到自己的可写工作目录。在模板所在目录运行生成器；下面的 /path/to/... 是占位路径，clkndata.tpl 是文档入门示例名，要按实际包中的文件替换：'),
 ('code','perl /path/to/easier_uvm_gen.pl -h\nperl /path/to/easier_uvm_gen.pl -m common.tpl clkndata.tpl'),
 ('p','-t 可省略。common.tpl 默认名为 common.tpl；prefix 默认 top；project 默认 generated_tb。project 必须是简单目录名，而不是带斜杠的路径。先 cd 到合适工作目录，再生成。初次调通不要用 -c 自动跳过所有警告；先逐条弄清警告原因。'),
 ('p','每次重新生成都会更新生成目录。长期修改要保存在模板、include 文件或可重复的后处理脚本中，避免仅手改生成结果。可以使用 Git 保存输入及发行包版本。'),
 ('sub','A.6  检查并运行生成的 VCS 脚本'),
 ('code','cd generated_tb/sim\nhead -n 1 compile_vcs.sh\ngrep -nE \'vcs|vlogan|uvm|UVM|ntb_opts|simv|files\' compile_vcs.sh\n./compile_vcs.sh'),
 ('p','原文的 VCS 入口是 <project>/sim/compile_vcs.sh。先查看脚本使用哪种 shell、如何选择 UVM、是否已同时编译并启动 simv，再运行。旧发行包可能依赖 csh/tcsh；按脚本 shebang 和公司平台处理，不要无条件用 bash 硬跑。2016 年脚本的工具开关不能假定与所有当前 VCS release 一致。'),
 ('p','UVM 只选择一套：优先采用公司已经验证的 VCS/UVM 组合。使用 VCS 内建 UVM 时，根据本地 vcs -help 和公司 flow 选择对应选项；常见示意为 -ntb_opts uvm-1.2，但实际可用版本要核对。如果使用外部 UVM，则按公司 flow 编译它。不要同时选择内建 UVM 并再手动编译另一份 uvm_pkg.sv。'),
 ('sub','A.7  再替换为真实 DUT'),
 ('bullet','common.tpl：填写真实 DUT 模块名 dut_top、相对当前生成工作目录的 dut_source_path、inc_path、dut_pfile，以及 prefix/project 等设置。'),
 ('bullet','RTL/filelist：准备完整依赖与编译顺序。生成器会复制 dut_source_path 下的文件；其中 files.f 只列 DUT 及所需选项，不要再列一份 UVM 基类库。嵌套 include 或外部 package 的路径需单独核对。'),
 ('bullet','每类接口一份 .tpl：定义 agent_name、trans_item、trans_var、if_port、时钟/复位标识以及 agent 模式。pinlist 将接口变量映射到真实 DUT 端口。'),
 ('bullet','用户代码：实现 driver 的 do_drive 或 run_phase、monitor 的 do_mon 或 run_phase，以及 sequence。默认 driver 打印收到的事务不意味着已经驱动 DUT。'),
 ('bullet','检查与覆盖：接入记分板/参考模型、断言、覆盖率和异常场景。Syosil scoreboard 是可选额外依赖，最小骨架 smoke 不必引入它。'),
 ('p','先调通一个接口和一个最小测试，再增加多 agent、多实例、寄存器层和复杂参考模型。你之前生成的 DV_SVA_ASSERT 库可以通过 interface/assertion module 或 bind 方式加入，不会由 Easier UVM 自动理解并生成协议断言。'),
 ('sub','A.8  调通的验收清单'),
 ('bullet','生成阶段：没有未处理的模板警告；生成目录结构和 DUT 实例端口映射与预期相符。'),
 ('bullet','编译阶段：无 package 重复定义、无缺失 include/模块/类，UVM 版本和工具链一致，许可证可正常签出。'),
 ('bullet','基础运行：选中的 UVM test 确实启动；run_phase、sequence、driver/monitor 的基本连接可观察；测试能按预期结束。'),
 ('bullet','真实协议：波形上时钟/复位正确、接口确实活动；monitor 还原的事务与驱动一致；检查器对正确场景通过、对故意违规失败；覆盖点确实被触发。'),
 ('sub','A.9  接入真实工程还需准备的信息'),
 ('p','VCS 的具体版本及公司 UVM 选型；DUT 顶层模块和端口声明；时钟/复位极性与时序；需要几个接口/agent；事务字段与握手协议；RTL files.f；可用的参考模型或期望结果。缺少这些输入时可以生成学习骨架，但不能替你完成真实协议驱动和功能检查。'),
 ('p','本译本没有连接或修改你的工作服务器，没有下载执行生成器，也没有运行 VCS。以上步骤和原文提供的脚本入口应在你们的实际工具环境中进行 smoke 验证。'),
 ('sub','实施参考来源'),
 ('p','Doulos 官方下载入口：https://www.doulos.com/knowhow/systemverilog/uvm/easier-uvm/easier-uvm-coding-guidelines/download-the-easier-uvm-coding-guidelines-and-code-generator/'),
 ('p','Doulos 入门教程：https://www.doulos.com/knowhow/systemverilog/uvm/easier-uvm/easier-uvm-code-generator/easier-uvm-code-generator-tutorial-1/'),
 ('p','用户目录 Perl 模块安装参考：https://metacpan.org/pod/App::cpanminus 与 https://metacpan.org/pod/local::lib。VCS 具体版本开关以公司安装版本的帮助和支持文档为准。'),
]
for typ,text in appendix:
    if typ=='code':story.append(code(text))
    elif typ=='bullet':story.append(para('• '+text,'bullet'))
    else:story.append(para(text,typ if typ in styles else 'body'))

# Check glyph availability before authoring, including all translated text.
for text in zh.values():
    missing={c for c in text if ord(c)>127 and ord(c) not in pdfmetrics.getFont('CN').face.charToGlyph and not c.isspace()}
    assert not missing,('Missing CJK glyphs',missing)
doc=Document(str(PDF),pagesize=A4,title='Easier UVM 代码生成器参考指南 - 中文译本与 Linux VCS 实施附录',author='中文译文整理',subject='Doulos Reference Guide 2016-04-18 的中文翻译')
doc.multiBuild(story)
from pypdf import PdfReader
r=PdfReader(PDF)
assert len(r.pages)>20
text='\n'.join(p.extract_text() or '' for p in r.pages)
for word in ['File::Copy::Recursive','ref_model_output','do_drive','Linux','VCS','附录 A']:
    assert word in text,word
manifest={'pdf':str(PDF),'source_pages':42,'translated_blocks':len(zh),'code_blocks':140,'figures':3,'output_pages':len(r.pages),'pdf_bytes':PDF.stat().st_size,'all_translation_ids_present':True}
(ROOT/'translation_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(manifest,ensure_ascii=False,indent=2))