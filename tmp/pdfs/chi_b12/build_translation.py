from pathlib import Path
import json
import re
from collections import Counter
from xml.sax.saxutils import escape

from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, Flowable, HRFlowable,
)
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
OUT = ROOT / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / 'AMBA_CHI_IHI0050H_B12_内存标签_中文译文.pdf'

pdfmetrics.registerFont(TTFont('CJK', 'C:/Windows/Fonts/msyh.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('CJKB', 'C:/Windows/Fonts/msyhbd.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('Mono', 'C:/Windows/Fonts/consola.ttf'))
pdfmetrics.registerFontFamily('CJK', normal='CJK', bold='CJKB', italic='CJK', boldItalic='CJKB')

INK = colors.HexColor('#192A3A')
ACCENT = colors.HexColor('#174D70')
MUTED = colors.HexColor('#596977')
PALE = colors.HexColor('#EDF3F7')
RULE = colors.HexColor('#CFDAE3')
PAGE_W, PAGE_H = A4
LEFT = RIGHT = 43
TOP, BOTTOM = 48, 44
WIDTH = PAGE_W - LEFT - RIGHT

STYLES = {
    'title': ParagraphStyle('title', fontName='CJKB', fontSize=20, leading=29, textColor=INK, spaceAfter=12, wordWrap='CJK'),
    'subtitle': ParagraphStyle('subtitle', fontName='CJK', fontSize=10, leading=16, textColor=MUTED, spaceAfter=8, wordWrap='CJK'),
    'body': ParagraphStyle('body', fontName='CJK', fontSize=9.7, leading=16, textColor=INK, spaceAfter=6, wordWrap='CJK', splitLongWords=1),
    'note': ParagraphStyle('note', fontName='CJK', fontSize=9.0, leading=14.5, textColor=MUTED, spaceBefore=3, spaceAfter=6, leftIndent=10, borderPadding=5, wordWrap='CJK'),
    'source': ParagraphStyle('source', fontName='CJK', fontSize=8.0, leading=12, textColor=MUTED, spaceBefore=10, spaceAfter=7, keepWithNext=True, wordWrap='CJK'),
    'caption': ParagraphStyle('caption', fontName='CJKB', fontSize=9, leading=14, textColor=ACCENT, spaceBefore=8, spaceAfter=5, keepWithNext=True, wordWrap='CJK'),
    'cell': ParagraphStyle('cell', fontName='CJK', fontSize=8.0, leading=12, textColor=INK, wordWrap='CJK', splitLongWords=1),
    'th': ParagraphStyle('th', fontName='CJKB', fontSize=8, leading=12, textColor=colors.white, wordWrap='CJK', splitLongWords=1),
    'footnote': ParagraphStyle('footnote', fontName='CJK', fontSize=8, leading=12.5, textColor=MUTED, spaceAfter=5, wordWrap='CJK'),
}
for level, size, leading in [(1,16,23),(2,13,20),(3,11,18),(4,10,17)]:
    STYLES[f'h{level}'] = ParagraphStyle(f'h{level}', fontName='CJKB', fontSize=size, leading=leading,
        textColor=ACCENT, spaceBefore=12, spaceAfter=7, keepWithNext=True, wordWrap='CJK')


def markup(value):
    text = str(value)
    text = re.sub(r'([\u4e00-\u9fff])([A-Za-z0-9])', r'\1 \2', text)
    text = re.sub(r'([A-Za-z0-9])([\u4e00-\u9fff])', r'\1 \2', text)
    text = escape(text)
    # Respect explicit lightweight emphasis in translator inputs.
    text = re.sub(r'`([^`]+)`', r'<font name="Mono">\1</font>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    # Preserve literal wildcard opcodes such as Atomic* and SnpStash*.
    # TagOp enumeration values are italicized; cache states stay roman.
    text = re.sub(r'(?<![A-Za-z])(Transfer|Update|Fetch)(?![A-Za-z])', r'<font name="Helvetica-Oblique">\1</font>', text)
    text = re.sub(r'(?<!Tag )(?<![A-Za-z])(Match)(?![A-Za-z])', r'<font name="Helvetica-Oblique">\1</font>', text)
    text = re.sub(r'(TagOp[^。；，：:\n<>]{0,18}?)(Invalid)', r'\1<font name="Helvetica-Oblique">\2</font>', text)
    text = re.sub(r'^(Invalid)(?=[：:])', r'<font name="Helvetica-Oblique">\1</font>', text)
    text = re.sub(r'(值为\s*)(Invalid)(\s*的\s*TagOp)', r'\1<font name="Helvetica-Oblique">\2</font>\3', text)
    return text.replace('\n', '<br/>')


def para(text, style='body'):
    selected = STYLES[style]
    if style == 'body' and str(text).rstrip().endswith(('：', ':')):
        selected = ParagraphStyle('lead_in', parent=selected, keepWithNext=True)
    return Paragraph(markup(text), selected)


class Heading(Paragraph):
    def __init__(self, text, level, key):
        super().__init__(markup(text), STYLES[f'h{min(max(level,1),4)}'])
        self.outline_text = text
        self.outline_level = level
        self.outline_key = key


class TranslationDoc(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Heading):
            self.canv.bookmarkPage(flowable.outline_key)
            # Only main sections enter the PDF navigation outline.
            if re.match(r'^B12\.\d+\s', flowable.outline_text):
                self.canv.addOutlineEntry(flowable.outline_text, flowable.outline_key, level=0, closed=False)


def page_frame(c, doc):
    c.saveState()
    c.setStrokeColor(RULE)
    c.setLineWidth(.5)
    c.line(LEFT, PAGE_H-32, PAGE_W-RIGHT, PAGE_H-32)
    c.setFont('CJK', 8)
    c.setFillColor(MUTED)
    c.drawString(LEFT, PAGE_H-24, 'AMBA CHI · ARM IHI 0050 Issue H')
    c.drawRightString(PAGE_W-RIGHT, PAGE_H-24, 'B12  内存标签 | 中文译文')
    c.line(LEFT, 29, PAGE_W-RIGHT, 29)
    c.setFont('CJK', 7.4)
    c.drawString(LEFT, 17, '非官方译文 · 原文页码见正文 · 原文 © Arm Limited or its affiliates')
    c.drawRightString(PAGE_W-RIGHT, 17, f'译文第 {doc.page} 页')
    c.restoreState()


def table_widths(columns, rows):
    n = len(columns)
    if n == 6:  # TagOp matrix: one opcode column and five concise statuses.
        return [WIDTH*.47] + [WIDTH*.53/5]*5
    if n == 4:
        # Distinguish the signal field table from the cache-state table.
        head = ' '.join(columns)
        if 'Request' in head or '请求' in head:
            return [WIDTH*.31, WIDTH*.23, WIDTH*.21, WIDTH*.25]
        return [WIDTH*.17, WIDTH*.17, WIDTH*.20, WIDTH*.46]
    if n == 3:
        return [WIDTH*.23, WIDTH*.24, WIDTH*.53]
    if n == 2:
        return [WIDTH*.30, WIDTH*.70]
    return [WIDTH/n]*n


segments = []
for filename in ['translation_1_4.json', 'translation_5_9.json', 'translation_10_13.json']:
    segment = json.loads((BASE/filename).read_text(encoding='utf-8-sig'))
    assert isinstance(segment['blocks'], list), filename
    segments.append(segment)

blocks = [b for segment in segments for b in segment['blocks']]
story = [
    para('B12 内存标签\nMemory Tagging', 'title'),
    para('Arm AMBA CHI Architecture Specification\nARM IHI 0050 · Issue H · 原文第 429–451 页', 'subtitle'),
    HRFlowable(width='100%', thickness=1.2, color=ACCENT, spaceAfter=12),
    para('译文说明', 'caption'),
    para('本文件是所提供规格书 B12 全章的非官方中文译文。保留原章节编号、表格编号、协议字段、操作码及状态值；文中的章节和表格交叉引用均指向原规格书。正文标注原文页码，译文独立分页。', 'note'),
    para('表格中的合并单元格按明确的条件组合展开；续表仍保留原表号。必须、不得、允许、建议分别用于区分原文的强制要求、禁止事项、许可和推荐。标为“译注”的文字属于翻译说明。', 'note'),
    para('原文版权：Copyright © 2014, 2017–2025 Arm Limited or its affiliates. All rights reserved. Non-confidential.', 'footnote'),
]
last_source = None
counts = Counter()
all_text = []
table_counts = []

for i, block in enumerate(blocks):
    kind = block['type']
    source = block.get('source_page')
    if source != last_source and source is not None:
        story.append(para(f'原文第 {source} 页', 'source'))
        last_source = source
    counts[kind] += 1
    if kind == 'heading':
        title = block.get('title', block.get('text', ''))
        level = int(block.get('level', 2))
        story.append(Heading(title, level, f'sec_{i}'))
        all_text.append(title)
    elif kind == 'p':
        story.append(para(block['text']))
        all_text.append(block['text'])
    elif kind in ('note','translator_note'):
        value = block['text']
        if kind == 'note' and not value.startswith(('注','译注')):
            value = '注：' + value
        story.append(para(value, 'note'))
        all_text.append(value)
    elif kind == 'bullet':
        indent = int(block.get('indent', 0))
        style = ParagraphStyle(f'bullet_{i}', parent=STYLES['body'], leftIndent=12+indent*12,
            firstLineIndent=0, bulletIndent=indent*12, spaceAfter=4,
            keepWithNext=block['text'].rstrip().endswith(('：', ':')))
        story.append(Paragraph(markup(block['text']), style, bulletText='•' if indent == 0 else '–'))
        all_text.append(block['text'])
    elif kind == 'table':
        caption = block.get('caption','')
        columns = block['columns']
        rows = block['rows']
        assert all(len(row) == len(columns) for row in rows), caption
        if caption:
            story.append(para(caption, 'caption'))
        data = [[para(cell, 'th') for cell in columns]]
        for row in rows:
            rendered = []
            for j, cell in enumerate(row):
                value = markup(cell)
                if (j == 1 and ('TagOp' in columns[j] or 'B12.1' in caption)):
                    value = value.replace('Invalid', '<font name="Helvetica-Oblique">Invalid</font>')
                rendered.append(Paragraph(value, STYLES['cell']))
            data.append(rendered)
        table = Table(data, colWidths=table_widths(columns, rows), repeatRows=1,
                      hAlign='LEFT', splitByRow=1, spaceAfter=7)
        table.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,0),ACCENT),
            ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LINEBELOW',(0,0),(-1,0),.7,ACCENT),
            ('LINEBELOW',(0,1),(-1,-1),.3,RULE),
            ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
            ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
        ]))
        story.append(table)
        for footnote in block.get('footnotes',[]):
            story.append(para(footnote, 'footnote'))
        all_text.extend([caption] + columns + [str(c) for row in rows for c in row] + block.get('footnotes',[]))
        table_counts.append({'caption':caption,'rows':len(rows),'columns':len(columns),'source_page':source})
    else:
        raise ValueError(f'Unsupported block type: {kind}')

doc = TranslationDoc(str(PDF), pagesize=A4, rightMargin=RIGHT, leftMargin=LEFT,
    topMargin=TOP, bottomMargin=BOTTOM, title='AMBA CHI Issue H — B12 内存标签（完整中文译文）',
    author='中文翻译；原文 Arm Limited or its affiliates',
    subject='ARM IHI 0050H B12 Memory Tagging, source pages 429–451', pageCompression=1)
doc.build(story, onFirstPage=page_frame, onLaterPages=page_frame)
(BASE/'translation_flat.txt').write_text('\n'.join(all_text), encoding='utf-8')
(BASE/'build_manifest.json').write_text(json.dumps({'pdf':str(PDF), 'blocks':dict(counts), 'tables':table_counts,
    'source_pages': sorted({b['source_page'] for b in blocks if 'source_page' in b})}, ensure_ascii=False, indent=2),encoding='utf-8')
print(json.dumps({'pdf':str(PDF),'blocks':dict(counts),'tables':table_counts},ensure_ascii=False))
