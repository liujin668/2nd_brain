from pathlib import Path
import json, sys, re, hashlib, time
import pypdfium2 as pdfium
sys.stdout.reconfigure(encoding='utf-8')
root=Path(__file__).resolve().parents[3]
work=Path(__file__).resolve().parent
src=Path(r'C:\Users\jinliu01\OneDrive - ARM China\文档\Specs\ARM\arm_neoverse_n2_core_trm_102099_0003_06_en.pdf')
doc=pdfium.PdfDocument(src)
pages=[]
for i in range(len(doc)):
    p=doc[i];tp=p.get_textpage();t=tp.get_text_range()
    pages.append(t)
    tp.close();p.close()
    if (i+1)%200==0: print('Extracted',i+1,flush=True)
(work/'pages.json').write_text(json.dumps(pages,ensure_ascii=False),encoding='utf-8')
(work/'full-text.txt').write_text('\n'.join(f'\n===== PDF PAGE {i+1} =====\n'+t for i,t in enumerate(pages)),encoding='utf-8')
(work/'front-matter.txt').write_text('\n'.join(f'\n===== PDF PAGE {i+1} =====\n'+t for i,t in enumerate(pages[:25])),encoding='utf-8')
captions=[]
for i,t in enumerate(pages):
    for line in t.splitlines():
        if re.match(r'^(Figure|Table) \d|^(Figure|Table) [A-Z]-',line): captions.append({'page':i+1,'caption':line})
(work/'captions.json').write_text(json.dumps(captions,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(pages),'chars':sum(map(len,pages)),'captions':len(captions),'sha256':hashlib.sha256(src.read_bytes()).hexdigest()},ensure_ascii=False))
