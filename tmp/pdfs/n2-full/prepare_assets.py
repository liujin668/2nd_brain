from pathlib import Path
import json,re,sys,hashlib,shutil
import pypdfium2 as pdfium
from PIL import Image,ImageDraw,ImageFont
sys.stdout.reconfigure(encoding='utf-8')
root=Path(__file__).resolve().parents[3];work=Path(__file__).resolve().parent
src=Path(r'C:\Users\jinliu01\OneDrive - ARM China\文档\Specs\ARM\arm_neoverse_n2_core_trm_102099_0003_06_en.pdf')
asset=root/'Neoverse/01_assets/N2-Core-TRM-r0p3';asset.mkdir(parents=True,exist_ok=True)
dest=root/'Neoverse/00_sources'/src.name
if dest.exists():
    if hashlib.sha256(dest.read_bytes()).digest()!=hashlib.sha256(src.read_bytes()).digest(): raise RuntimeError('Existing source differs')
else: shutil.copy2(src,dest)
pages=json.loads((work/'pages.json').read_text(encoding='utf-8'))
captions=json.loads((work/'captions.json').read_text(encoding='utf-8'))
selected={x['page'] for x in captions}
for i,t in enumerate(pages):
    if i<25:continue
    lines=[l.strip() for l in t.replace('\r','').splitlines() if l.strip()]
    lead='\n'.join(lines[3:14])
    if re.search(r'^(Bits Name|Bit field|Name Op0|Name coproc|Offset Name|Scenario (Behavior|Description)|Change Location|Feature (Status|Description)|Event$|Event number|Standard or)',lead,re.M):selected.add(i+1)
# Complete known long main-body tables, including all their continuation pages.
for a,b in [(33,36),(76,95),(102,104),(107,108),(117,121),(122,136),(143,149),(153,155),(158,159),(1662,1668)]:selected.update(range(a,b+1))
selected={i for i in selected if i>=26}
doc=pdfium.PdfDocument(src);scale=2.25
old_manifest=json.loads((work/'asset-manifest.json').read_text(encoding='utf-8')) if (work/'asset-manifest.json').exists() else {}
rerender=old_manifest.get('crop_version')!=2
for k,n in enumerate(sorted(selected)):
    out=asset/f'p{n:04}-original.png'
    if not out.exists() or rerender:
        p=doc[n-1];im=p.render(scale=scale).to_pil()
        # Preserve the full page body and footnotes, including original watermark.
        im=im.crop(tuple(round(v*scale) for v in (0,60,p.get_width(),741)))
        im.save(out,optimize=True);p.close()
    if (k+1)%100==0:print(f'Rendered {k+1}/{len(selected)} original page screenshots',flush=True)
# Tight original figure used in the main guide; keep the title and legend.
pg=doc[39];im=pg.render(scale=3.4).to_pil();im.crop(tuple(round(v*3.4) for v in (80,76,556,476))).save(asset/'figure-3-1-original.png',optimize=True);pg.close()
manifest={'crop_version':2,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'source_copy':str(dest),'screenshot_pages':sorted(selected),'captions':captions,'asset_dir':str(asset)}
(work/'asset-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
samples=[28,30,40,50,58,63,75,83,84,97,109,111,122,131,137,141,152,156,157,158,242,1114,1662,1667]
thumbs=[]
for n in samples:
    f=asset/f'p{n:04}-original.png'
    if not f.exists():continue
    im=Image.open(f);im.thumbnail((270,360));thumbs.append((n,im.copy()))
sheet=Image.new('RGB',(4*290,((len(thumbs)+3)//4)*395),'#DCE3EB');dr=ImageDraw.Draw(sheet);font=ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc',17)
for i,(n,im) in enumerate(thumbs):
    x=i%4*290+10;y=i//4*395+30;sheet.paste(im,(x,y));dr.text((x,y-23),f'原文 p.{n}',font=font,fill='#17304D')
sheet.save(work/'source-qa-contact.png')
print(json.dumps({'screenshots':len(selected)+1,'asset_bytes':sum(f.stat().st_size for f in asset.glob('*.png')),'source_copy_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},ensure_ascii=False))
