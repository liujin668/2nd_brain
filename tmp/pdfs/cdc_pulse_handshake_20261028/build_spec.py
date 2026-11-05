from pathlib import Path
import re, json, html, shutil, hashlib, zipfile, sys, math
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Rect, Line, String, Polygon, PolyLine
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, XPreformatted, Image, KeepTogether
import pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import Image as PILImage, ImageDraw
sys.stdout.reconfigure(encoding='utf-8')
WORK=Path(__file__).resolve().parent
ROOT=WORK.parents[2]
OUT=ROOT/'output/pdf/acs_cdc_pulse_handshake_20261028'
ASSETS=OUT/'assets'
ASSETS.mkdir(parents=True,exist_ok=True)
for n,p in [('CN',r'C:\Windows\Fonts\msyh.ttc'),('CNB',r'C:\Windows\Fonts\msyhbd.ttc'),('Mono',r'C:\Windows\Fonts\consola.ttf')]:
    pdfmetrics.registerFont(TTFont(n,p,subfontIndex=0))
pdfmetrics.registerFontFamily('CN',normal='CN',bold='CNB',italic='CN',boldItalic='CNB')
NAVY=colors.HexColor('#17374B'); BLUE=colors.HexColor('#146F91'); TEAL=colors.HexColor('#15786F')
ORANGE=colors.HexColor('#BD6422'); RED=colors.HexColor('#A33C3C'); GREY=colors.HexColor('#60727D')
LIGHT=colors.HexColor('#F0F5F8'); WHITE=colors.white
def text(d,x,y,s,size=13,font='CN',color=NAVY,anchor='start'):
    d.add(String(x,y,s,fontName=font,fontSize=size,fillColor=color,textAnchor=anchor))
def multiline(d,x,y,lines,size=14,leading=21,font='CN',color=NAVY,anchor='middle'):
    for k,s in enumerate(lines):text(d,x,y-k*leading,s,size,font,color,anchor)
def rect(d,x,y,w,h,fill=LIGHT,stroke=BLUE):
    d.add(Rect(x,y,w,h,rx=8,ry=8,fillColor=fill,strokeColor=stroke,strokeWidth=1.4))
def arrow(d,points,color=BLUE,width=1.7):
    d.add(PolyLine([v for p in points for v in p],strokeColor=color,strokeWidth=width,fillColor=None))
    x,y=points[-1]; px,py=points[-2];a=math.atan2(y-py,x-px);size=8
    d.add(Polygon([x,y,x-size*math.cos(a-.45),y-size*math.sin(a-.45),x-size*math.cos(a+.45),y-size*math.sin(a+.45)],fillColor=color,strokeColor=color))
def save_drawing(d,name):
    p=WORK/(name+'.pdf');renderPDF.drawToFile(d,str(p))
    pd=pdfium.PdfDocument(str(p));pd[0].render(scale=2.4).to_pil().save(ASSETS/(name+'.png'));pd.close()
def structure():
    d=Drawing(820,510)
    rect(d,15,18,380,475,colors.HexColor('#EEF5FC'),colors.HexColor('#A9C9E0'))
    rect(d,425,18,380,475,colors.HexColor('#ECF7F3'),colors.HexColor('#A4CFBF'))
    text(d,205,465,'源时钟域 / clk_src',19,'CNB',BLUE,'middle')
    text(d,615,465,'目的时钟域 / clk_dst',19,'CNB',TEAL,'middle')
    rect(d,110,370,220,65,WHITE);multiline(d,220,410,['上升事件检测','din && ~din_pipe'],14,22)
    text(d,43,397,'din',16,'Mono');arrow(d,[(72,402),(110,402)])
    rect(d,110,260,220,75,WHITE);multiline(d,220,309,['请求寄存器 R','din_store','复位 > set > clear'],14,21)
    arrow(d,[(220,370),(220,335)]);text(d,232,348,'set',12,'Mono')
    rect(d,455,260,285,75,colors.HexColor('#FFF6E9'),ORANGE)
    multiline(d,597,309,['正向同步器','acs_cdc_capt_sync','内部级数与实现待核实'],13,21,color=ORANGE)
    arrow(d,[(330,298),(455,298)]);text(d,390,311,'R',14,'Mono',BLUE,'middle')
    arrow(d,[(740,298),(776,298),(776,178),(740,178)],TEAL);text(d,769,245,'Q',15,'Mono',TEAL,'middle')
    rect(d,455,140,285,75,WHITE,TEAL);multiline(d,597,189,['Q_delay <= Q @clk_dst','dout = Q && ~Q_delay','延迟寄存器 + 组合边沿检测'],13,21,color=TEAL)
    arrow(d,[(597,140),(597,108)],TEAL);text(d,617,107,'dout',16,'Mono',TEAL)
    rect(d,110,45,220,75,colors.HexColor('#FFF6E9'),ORANGE)
    multiline(d,220,94,['回传同步器','acs_cdc_capt_sync','内部级数与实现待核实'],12.5,21,color=ORANGE)
    arrow(d,[(776,298),(791,298),(791,78),(330,78)],ORANGE)
    text(d,540,55,'回传 Q：确认同步路径已看到请求',12,'CN',ORANGE,'middle')
    arrow(d,[(110,82),(67,82),(67,279),(110,279)],ORANGE)
    text(d,50,195,'A',15,'Mono',ORANGE,'middle');text(d,50,174,'clear',11,'Mono',ORANGE,'middle')
    text(d,205,31,'rstn_src 控制源域寄存器与回传实例',11,'CN',GREY,'middle')
    text(d,615,31,'rstn_dst 控制目的域寄存器与正向实例',11,'CN',GREY,'middle')
    save_drawing(d,'01_structure')
def clock_changes(period,phase,end):
    x=[];t=phase
    while t<=end:
        x.append((t,1))
        if t+period/2<=end:x.append((t+period/2,0))
        t+=period
    return x
PLOT_DATA={}
def wave(name,end,din,R,Q,A,pulses,events,consumers):
    PLOT_DATA[name]={'end':end,'din':din,'din_store':R,'din_store_sync2dst':Q,'din_store_sync2src':A,'dout':sum(([(a,1),(b,0)] for a,b in pulses),[]),'sampled_in_events':events,'consumer_samples':consumers}
    d=Drawing(900,420);left=158;right=875;top=350;step=35;lowhigh=17;scale=(right-left)/end
    tick=10 if end<=115 else 20
    for t in range(0,int(end)+1,tick):
        x=left+t*scale;d.add(Line(x,63,x,374,strokeColor=colors.HexColor('#DCE6EC'),strokeWidth=.7))
        text(d,x,46,str(t),11,'Mono',GREY,'middle')
    text(d,875,25,'时间 / ns',12,'CN',GREY,'end')
    idle=[]; rstate=0; astate=0; oldidle=1
    for t in sorted(set(t for t,v in R+A)):
        rstate=next((v for x,v in reversed(R) if x<=t),0);astate=next((v for x,v in reversed(A) if x<=t),0)
        newidle=int(not(rstate or astate))
        if newidle!=oldidle:idle.append((t,newidle));oldidle=newidle
    rows=[('clk_src',clock_changes(10,0,end),GREY),('clk_dst',clock_changes(16,3,end),GREY),('din',din,BLUE),
          ('R / din_store',R,BLUE),('Q / dst_sync',Q,TEAL),('dout',sum(([(a,1),(b,0)] for a,b in pulses),[]),RED),
          ('A / src_ack',A,ORANGE),('idle*',idle,GREY)]
    for i,(label,trans,color) in enumerate(rows):
        y=top-i*step;text(d,14,y+5,label,13,'Mono',color);state=1 if label=='idle*' else 0
        pts=[left,y+lowhigh*state]
        for t,value in sorted(trans):
            if t>end:continue
            x=left+t*scale;pts.extend([x,y+lowhigh*state,x,y+lowhigh*value]);state=value
        pts.extend([right,y+lowhigh*state]);d.add(PolyLine(pts,strokeColor=color,strokeWidth=1.7,fillColor=None))
    for t in events:
        x=left+t*scale;d.add(Polygon([x-4,392,x+4,392,x,381],fillColor=BLUE,strokeColor=BLUE))
        text(d,x,400,str(t),11,'Mono',BLUE,'middle')
    for t in consumers:
        x=left+t*scale;d.add(Polygon([x-4,69,x+4,69,x,80],fillColor=RED,strokeColor=RED))
        text(d,x,57,str(t),10,'Mono',RED,'middle')
    text(d,16,383,'蓝标：源采样识别事件',11,'CN',BLUE)
    text(d,16,21,'红标：下游 FF 采到 dout；idle* 为解释信号，原 IP 无此端口',11,'CN',GREY)
    save_drawing(d,name)
def figures():
    structure()
    wave('02_normal_timing',110,[(6,1),(16,0)],[(10,1),(60,0)],[(35,1),(83,0)],[(50,1),(100,0)],[(35,51)],[10],[51])
    wave('03_busy_merge',110,[(6,1),(16,0),(26,1),(36,0)],[(10,1),(60,0)],[(35,1),(83,0)],[(50,1),(100,0)],[(35,51)],[10,30],[51])
    wave('04_safe_repeat',205,[(6,1),(16,0),(106,1),(116,0)],[(10,1),(60,0),(110,1),(160,0)],[(35,1),(83,0),(131,1),(179,0)],[(50,1),(100,0),(150,1),(190,0)],[(35,51),(131,147)],[10,110],[51,147])
def verify_figures():
    data=json.loads((WORK/'timing_examples.json').read_text(encoding='utf-8-sig'))
    mapping={'02_normal_timing':'normal_single','03_busy_merge':'busy_merge','04_safe_repeat':'rearmed_two'}
    report={}
    for fig,case_name in mapping.items():
        case=next(c for c in data['cases'] if c['name']==case_name)
        plot=PLOT_DATA[fig];end=plot['end']
        for signal in ['din','din_store','din_store_sync2dst','din_store_sync2src','dout']:
            expected=[(v['time_ns'],v['value']) for v in case['transitions'] if v['signal']==signal and v['time_ns']<=end]
            assert plot[signal]==expected,(fig,signal,plot[signal],expected)
        for kind in ['sampled_in_events','consumer_samples']:
            assert plot[kind]==[t for t in case['summary'][kind] if t<=end]
        report[fig]={'matched_independent_model':True,'signals_checked':5,'summary':case['summary']}
    (WORK/'plot_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print('All waveform transitions agree with the independent event model.')

PAGE_W,PAGE_H=A4;LEFT=46;RIGHT=46;BODY=PAGE_W-LEFT-RIGHT
styles={
 'body':ParagraphStyle('Body',fontName='CN',fontSize=10,leading=16.2,spaceAfter=7,rightIndent=12,wordWrap='CJK',textColor=NAVY,allowWidows=0,allowOrphans=0),
 'title':ParagraphStyle('Title',fontName='CNB',fontSize=22,leading=31,spaceAfter=16,wordWrap='CJK',textColor=NAVY),
 'h2':ParagraphStyle('H2',fontName='CNB',fontSize=16,leading=23,spaceAfter=12,spaceBefore=5,keepWithNext=True,wordWrap='CJK',textColor=BLUE),
 'h3':ParagraphStyle('H3',fontName='CNB',fontSize=11.2,leading=17,spaceAfter=6,spaceBefore=8,keepWithNext=True,wordWrap='CJK',textColor=NAVY),
 'small':ParagraphStyle('Small',fontName='CN',fontSize=8.2,leading=12.8,spaceAfter=6,wordWrap='CJK',textColor=GREY),
 'cell':ParagraphStyle('Cell',fontName='CN',fontSize=8.6,leading=13.2,spaceAfter=0,wordWrap='CJK',textColor=NAVY),
 'code':ParagraphStyle('Code',fontName='Mono',fontSize=7.5,leading=10,spaceAfter=8,spaceBefore=5,leftIndent=7,rightIndent=7,borderPadding=6,backColor=LIGHT,textColor=NAVY),
 'caption':ParagraphStyle('Caption',fontName='CN',fontSize=8.3,leading=13,spaceAfter=9,alignment=1,wordWrap='CJK',textColor=GREY)}
FENCE=chr(96)*3
def code_rich(s):
    return re.sub(r'[^\x00-\x7f]+',lambda m:'<font name="CN">'+m.group(0)+'</font>',html.escape(s))
def rich(s):
    s=html.escape(s);s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(chr(96)+r'([^'+chr(96)+r']+)'+chr(96),r'\1',s)
    return re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<link href="\2" color="#146F91">\1</link>',s)
def P(s,kind='body'):return Paragraph(rich(s),styles[kind])
def frame(c,doc):
    c.saveState();c.setStrokeColor(colors.HexColor('#CAD8E1'));c.setLineWidth(.5)
    c.line(LEFT,PAGE_H-36,PAGE_W-RIGHT,PAGE_H-36);c.setFillColor(GREY);c.setFont('CN',8)
    c.drawString(LEFT,PAGE_H-27,'acs_cdc_pulse_handshake | IP 设计与接口说明')
    c.drawRightString(PAGE_W-RIGHT,PAGE_H-27,'2026-10-28 / v1.0')
    c.line(LEFT,36,PAGE_W-RIGHT,36);c.drawString(LEFT,24,'基于提供的代码照片；同步器内部实现待确认')
    c.drawRightString(PAGE_W-RIGHT,24,str(doc.page));c.restoreState()
class Doc(BaseDocTemplate):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.addPageTemplates(PageTemplate(id='main',frames=[Frame(LEFT,49,BODY,PAGE_H-98,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=frame))
    def afterFlowable(self,flow):
        if hasattr(flow,'bookmark'):
            self.canv.bookmarkPage(flow.bookmark);self.canv.addOutlineEntry(flow.getPlainText(),flow.bookmark,0,False)
def boundary(s):
    return s.startswith(('#','|','![','>','- ','<!--',FENCE)) or bool(re.match(r'^[0-9]+\.\s',s))
def parse_md(md):
    lines=md.splitlines();story=[];i=0;hnum=0
    while i<len(lines):
        s=lines[i].strip()
        if not s:i+=1;continue
        if s=='<!-- PAGE -->':story.append(PageBreak());i+=1;continue
        if s.startswith(FENCE):
            buf=[];i+=1
            while i<len(lines) and not lines[i].strip().startswith(FENCE):buf.append(lines[i]);i+=1
            raw='\n'.join(buf);longest=max([len(x) for x in buf] or [1]);st=ParagraphStyle('Code'+str(i),parent=styles['code'])
            st.fontSize=min(7.5,(BODY-28)/(longest*.60));st.leading=st.fontSize*1.34
            story.append(XPreformatted(code_rich(raw),st));i+=1;continue
        m=re.match(r'!\[([^\]]*)\]\(([^)]+)\)',s)
        if m:
            p=OUT/m.group(2);im=Image(str(p));sc=min(BODY/im.imageWidth,345/im.imageHeight)
            im.drawWidth=im.imageWidth*sc;im.drawHeight=im.imageHeight*sc
            story.append(KeepTogether([im,P(m.group(1),'caption')]));i+=1;continue
        if s.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=[t.strip() for t in lines[i].strip().strip('|').split('|')]
                if not all(re.match(r'^:?-+:?$',t.replace(' ','')) for t in row):rows.append(row)
                i+=1
            n=max(map(len,rows));weights=[1/n]*n
            if n==2:weights=[.31,.69]
            elif n==3:weights=[.22,.22,.56]
            elif n==4:weights=[.21,.17,.20,.42]
            elif n==5:weights=[.12,.16,.16,.16,.40]
            cells=[[P(v,'cell') for v in row]+[P('','cell')]*(n-len(row)) for row in rows]
            t=Table(cells,colWidths=[BODY*w for w in weights],hAlign='LEFT',repeatRows=1)
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),LIGHT),('VALIGN',(0,0),(-1,-1),'TOP'),
                ('LINEBELOW',(0,0),(-1,0),.8,colors.HexColor('#B8CDDA')),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#DFE7EC')),
                ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
            story.extend([t,Spacer(1,8)]);continue
        if s.startswith('### '):story.append(P(s[4:],'h3'));i+=1;continue
        if s.startswith('## '):
            hnum+=1;p=P(s[3:],'h2');p.bookmark='sec'+str(hnum);story.append(p);i+=1;continue
        if s.startswith('# '):
            story.extend([P(s[2:],'title'),P('设计说明 / 接口时序 / 集成与验证要点','h3'),P('版本 v1.0    整理日期 2026-10-28    阅读对象：RTL / DV / SoC 集成人员','small')])
            i+=1;continue
        if s.startswith('> '):story.append(P(s[2:],'small'));i+=1;continue
        if s.startswith('- ') or re.match(r'^\d+\.\s',s):story.append(P(s));i+=1;continue
        buf=[s];i+=1
        while i<len(lines) and lines[i].strip() and not boundary(lines[i].strip()):buf.append(lines[i].strip());i+=1
        story.append(P(' '.join(buf)))
    return story
def build():
    md=(WORK/'spec_content.md').read_text(encoding='utf-8-sig')
    for c in '\u2011\u2013\u2014\u2212':md=md.replace(c,'-')
    mdpath=OUT/'acs_cdc_pulse_handshake_设计说明.md';mdpath.write_text(md,encoding='utf-8')
    pdfpath=OUT/'acs_cdc_pulse_handshake_设计说明.pdf'
    doc=Doc(str(pdfpath),pagesize=A4,title='acs_cdc_pulse_handshake IP设计与接口说明',author='基于用户提供RTL照片整理',subject='CDC pulse handshake design and timing specification')
    doc.build(parse_md(md));rd=PdfReader(str(pdfpath));text_all='\n'.join(p.extract_text() or '' for p in rd.pages)
    assert all(s in text_all for s in ['din_store_sync2dst','din_store_sync2src','clk_src','clk_dst','dout','2026-10-28'])
    renderdir=WORK/'rendered';renderdir.mkdir(exist_ok=True);pd=pdfium.PdfDocument(str(pdfpath))
    for j in range(len(pd)):pd[j].render(scale=1.5).to_pil().save(renderdir/f'page-{j+1:02d}.png')
    pd.close()
    for start in range(0,len(rd.pages),6):
        canvas=PILImage.new('RGB',(1260,1800),'#dce3e9');dr=ImageDraw.Draw(canvas)
        for k in range(6):
            j=start+k;p=renderdir/f'page-{j+1:02d}.png'
            if not p.exists():break
            im=PILImage.open(p);im.thumbnail((400,840));x=10+(k%3)*420;y=28+(k//3)*890
            canvas.paste(im,(x,y));dr.text((x,y-17),f'Page {j+1}',fill='black')
        canvas.save(renderdir/f'contact-{start//6+1}.png')
    for filename in ['timing_model.py','timing_examples.json','normal_single.csv','busy_merge.csv','rearmed_two.csv','unsafe_partial_rearm.csv']:
        source=WORK/filename
        if source.exists():
            target=OUT/'timing_model'/filename;target.parent.mkdir(exist_ok=True);shutil.copy2(source,target)
    manifest={'date':'2026-10-28','pages':len(rd.pages),'pdf_bytes':pdfpath.stat().st_size,'pdf_sha256':hashlib.sha256(pdfpath.read_bytes()).hexdigest(),'markdown_chars':len(md),'figures':4,'rtl_simulation_run':False,'scope':'Visible RTL lines 23-93; synchronizer internals unavailable.'}
    (OUT/'交付说明.txt').write_text('PDF与Markdown内容对应，Markdown图片位于assets目录，搬移时请保留目录结构。\n时序模型位于timing_model目录，仅为明确假设下的说明性Python模型，不是RTL仿真。\n本次未运行VCS，未完成CDC/RDC/STA签核；acs_cdc_capt_sync内部实现尚未提供。\n'+json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (WORK/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    zip_path=OUT.parent/'acs_cdc_pulse_handshake_文档包_20261028.zip'
    with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(OUT.rglob('*')):
            if p.is_file():z.write(p,p.relative_to(OUT.parent))
    print(json.dumps(manifest,ensure_ascii=False));print(str(pdfpath));print(str(mdpath));print(str(zip_path))
if __name__=='__main__':
    if '--figures-only' in sys.argv:figures();verify_figures();print('Four diagram assets generated.')
    else:build()
