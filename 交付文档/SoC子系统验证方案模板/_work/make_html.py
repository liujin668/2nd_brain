from pathlib import Path
import re, html, base64, json
root=Path(__file__).resolve().parent.parent
source=(root/'SoC子系统验证方案模板.md').read_text(encoding='utf-8')
lines=source.splitlines(); out=[]; inlist=False; i=0; chapter=-1
def inline(s):
    s=html.escape(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    return s
while i<len(lines):
    s=lines[i].strip()
    if not s:
        if inlist:out.append('</ul>');inlist=False
        i+=1;continue
    if s.startswith('|'):
        if inlist:out.append('</ul>');inlist=False
        block=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            block.append([x.strip() for x in lines[i].strip().strip('|').split('|')]);i+=1
        out.append('<table><thead><tr>'+''.join('<th>'+inline(x)+'</th>' for x in block[0])+'</tr></thead><tbody>')
        for row in block[2:]:out.append('<tr>'+''.join('<td>'+inline(x)+'</td>' for x in row)+'</tr>')
        out.append('</tbody></table>');continue
    if s.startswith('!['):
        m=re.match(r'!\[(.*?)\]\((.*?)\)',s)
        if m:
            data=base64.b64encode((root/m[2]).read_bytes()).decode('ascii')
            out.append('<img alt="'+html.escape(m[1],quote=True)+'" src="data:image/png;base64,'+data+'">')
    elif s.startswith('#'):
        m=re.match(r'(#+) (.*)',s);level=len(m[1]);text=m[2]
        if level<=2:
            if chapter>=0:out.append('</section>')
            chapter+=1;out.append('<section class="chapter" id="chapter-'+str(chapter)+'">')
        out.append(f'<h{level}>'+inline(text)+f'</h{level}>')
    elif s.startswith('- '):
        if not inlist:out.append('<ul>');inlist=True
        out.append('<li>'+inline(s[2:])+'</li>')
    else:out.append('<p>'+inline(s)+'</p>')
    i+=1
if inlist:out.append('</ul>')
out.append('</section>')
css='''body{margin:0;background:#edf1f4;color:#111;font-family:"Microsoft YaHei",sans-serif;font-size:16px;line-height:1.75}main{max-width:1100px;margin:24px auto;background:white;padding:48px 56px}h1{font-size:32px;margin:0 0 22px}h2{font-size:26px;margin:38px 0 18px}h3{font-size:21px;margin:28px 0 12px}p{margin:10px 0 15px}ul{padding-left:25px}table{width:100%;border-collapse:collapse;margin:15px 0 26px;table-layout:auto;font-size:14px;line-height:1.65}td,th{border:1px solid #d9d9d9;padding:10px 12px;vertical-align:middle;overflow-wrap:anywhere}th{background:#dce9f0;color:#000;text-align:left}tr:nth-child(even){background:#f5f8fa}img{display:block;width:100%;height:auto;margin:20px auto 10px}code{font-family:Consolas,monospace}section{padding:1px 0 20px}@media print{body{background:white}main{margin:0;padding:0;max-width:none}h2,h3{break-after:avoid}tr,img{break-inside:avoid}}'''
result='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>SoC子系统验证方案模板</title><style>'+css+'</style></head><body><main>'+''.join(out)+'</main></body></html>'
(root/'SoC子系统验证方案模板.html').write_text(result,encoding='utf-8')
print(json.dumps({'sections':chapter+1,'html_bytes':len(result.encode('utf-8'))}))
