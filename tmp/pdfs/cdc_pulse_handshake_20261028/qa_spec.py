from pathlib import Path
import re,json,html,hashlib,zipfile
import pdfplumber
from pypdf import PdfReader
w=Path('tmp/pdfs/cdc_pulse_handshake_20261028')
out=Path('output/pdf/acs_cdc_pulse_handshake_20261028')
md=(out/'acs_cdc_pulse_handshake_设计说明.md').read_text(encoding='utf-8')
pdf=out/'acs_cdc_pulse_handshake_设计说明.pdf'
reader=PdfReader(str(pdf));texts=[p.extract_text() or '' for p in reader.pages]
norm=lambda s:re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff]','',s)
alltext=norm('\n'.join(texts))
missing=[]
for n,line in enumerate(md.splitlines(),1):
    s=line.strip()
    if not s or s.startswith('<!--') or s.startswith(chr(96)*3):continue
    if s.startswith('|') and re.fullmatch(r'[\s|:\-]+',s):continue
    s=re.sub(r'!\[([^]]*)\]\([^)]+\)',r'\1',s)
    s=re.sub(r'\[([^]]*)\]\([^)]+\)',r'\1',s)
    token=norm(s)
    if token and token not in alltext:missing.append({'line':n,'text':s})
bounds=[]
with pdfplumber.open(str(pdf)) as p:
    for n,page in enumerate(p.pages,1):
        for ch in page.chars:
            if not (44<ch['top']<page.height-44):continue
            if ch['x0']<45 or ch['x1']>page.width-45 or ch['bottom']>page.height-44:
                bounds.append({'page':n,'text':ch['text'],'x0':round(ch['x0'],1),'x1':round(ch['x1'],1),'bottom':round(ch['bottom'],1)})
assets=re.findall(r'!\[[^]]*\]\(([^)]+)\)',md)
assert all((out/p).exists() for p in assets)
assert not missing,missing
assert not bounds,bounds
assert len(texts)==13
assert all('\ufffd' not in t for t in texts)
zp=out.parent/'acs_cdc_pulse_handshake_文档包_20261028.zip'
with zipfile.ZipFile(zp) as z:
    assert z.testzip() is None
    zcount=len(z.namelist())
result={'pages':len(texts),'md_nonempty_lines_matched':sum(bool(l.strip()) for l in md.splitlines()),'missing_text_lines':missing,'body_bounds_violations':bounds,'relative_image_links_ok':len(assets),'zip_files':zcount,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'illustrative_model':'4 cases checked by model assertions; 3 plotted cases match all 5 plotted data signals and event/consumer times','rtl_simulation_run':False}
(w/'final_qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
