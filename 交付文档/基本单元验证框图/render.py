from pathlib import Path
from html import escape
import math
from PIL import Image, ImageDraw, ImageFont
OUT=Path(__file__).resolve().parent
W,H,S=1500,650,2
INK,LINE,FILL,MUTED='#213a49','#3c6278','#eef4f7','#647985'
im=Image.new('RGB',(W*S,H*S),'white')
d=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">','<title>逻辑门与时钟单元验证框图</title>','<desc>激励驱动并列的逻辑与时钟单元。参考模型使用实际输入产生期望结果，与监测输出比较。</desc>','<rect width="100%" height="100%" fill="white"/>']
def box(x,y,w,h,fill=FILL):
 d.rounded_rectangle((x*S,y*S,(x+w)*S,(y+h)*S),radius=9*S,fill=fill,outline=LINE,width=4)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{LINE}" stroke-width="1.8"/>')
def txt(x,y,t,size=23,bold=False,anchor='middle',color=INK):
 font=ImageFont.truetype('C:/Windows/Fonts/msyhbd.ttc' if bold else 'C:/Windows/Fonts/msyh.ttc',size*S)
 d.text((x*S,y*S),t,font=font,fill=color,anchor={'middle':'mm','start':'lm'}[anchor])
 svg.append(f'<text x="{x}" y="{y}" font-family="Microsoft YaHei,Noto Sans CJK SC,sans-serif" font-size="{size}" font-weight="{600 if bold else 400}" text-anchor="{anchor}" dominant-baseline="central" fill="{color}">{escape(t)}</text>')
def line(p,arrow=False):
 d.line([(int(x*S),int(y*S)) for x,y in p],fill=LINE,width=4,joint='curve')
 svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in p)+f'" fill="none" stroke="{LINE}" stroke-width="1.9" stroke-linejoin="round"/>')
 if arrow:
  x,y=p[-1];px,py=p[-2];a=math.atan2(y-py,x-px);ll,hh=10,4.5
  tri=[(x,y),(x-ll*math.cos(a)+hh*math.sin(a),y-ll*math.sin(a)-hh*math.cos(a)),(x-ll*math.cos(a)-hh*math.sin(a),y-ll*math.sin(a)+hh*math.cos(a))]
  d.polygon([(int(xx*S),int(yy*S)) for xx,yy in tri],fill=LINE)
  svg.append('<polygon points="'+' '.join(f'{xx:.2f},{yy:.2f}' for xx,yy in tri)+f'" fill="{LINE}"/>')
def dot(x,y):
 d.ellipse(((x-3.5)*S,(y-3.5)*S,(x+3.5)*S,(y+3.5)*S),fill=LINE)
 svg.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="{LINE}"/>')
txt(750,43,'逻辑门与时钟单元验证框图',32,True)
box(390,115,460,325,'white')
txt(411,141,'DUT 边界 | 基本单元',24,True,'start')
box(440,180,350,105)
txt(615,205,'组合逻辑单元',25)
txt(615,239,'AND / OR / XOR / NAND / NOR',18)
txt(615,264,'XNOR / MUX / BUF / INV',18)
box(440,315,350,100)
txt(615,340,'时钟单元',25)
txt(615,373,'CLK BUF / INV / AND / OR',18)
txt(615,396,'GATE / MUX',18)
box(60,215,225,160)
txt(172.5,250,'激励发生器',27)
txt(172.5,296,'穷举 / 随机逻辑向量',20)
txt(172.5,331,'时钟 / 使能 / 选择',20)
box(920,230,180,130)
txt(1010,265,'输出监测',27)
txt(1010,307,'数据 / 边沿',21)
txt(1010,337,'脉宽 / 时间戳',20)
box(1210,230,220,130)
txt(1320,263,'比对与检查',27)
txt(1320,306,'功能 / 时钟行为',22)
txt(1320,337,'Checker / SVA',20)
box(440,475,350,110)
txt(615,503,'参考模型',26)
txt(615,540,'逻辑真值表 / 时钟行为',21)
txt(615,570,'独立计算期望结果',20)
box(1210,455,220,110)
txt(1320,485,'结果与覆盖率',25)
txt(1320,523,'PASS / FAIL',22)
txt(1320,551,'日志 / 波形 / 覆盖率',18)
line([(285,295),(350,295)])
line([(350,295),(350,232),(440,232)],True)
line([(350,295),(350,365),(440,365)],True)
dot(350,295)
line([(315,295),(315,530),(440,530)],True)
dot(315,295)
txt(324,491,'实际输入',19,anchor='start',color=MUTED)
line([(790,232),(885,232),(885,270),(920,270)],True)
line([(790,365),(885,365),(885,325),(920,325)],True)
line([(1100,275),(1210,275)],True)
txt(1155,252,'实际输出',18,color=MUTED)
line([(790,530),(1160,530),(1160,330),(1210,330)],True)
txt(975,509,'期望输出 / 预期边沿',20,color=MUTED)
line([(1320,360),(1320,455)],True)
txt(1334,408,'检查结果',19,anchor='start',color=MUTED)
txt(60,620,'注：各单元并列验证；毛刺、脉宽和切换规则按具体单元规格检查。',20,anchor='start',color=MUTED)
svg.append('</svg>')
base=OUT/'逻辑门与时钟单元验证框图'
base.with_suffix('.svg').write_text('\n'.join(svg),encoding='utf-8')
im.save(base.with_suffix('.png'),dpi=(220,220))
print(base.with_suffix('.png'))
print(base.with_suffix('.svg'))
print(im.size)

