from pathlib import Path
import json
import pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import Image,ImageDraw,ImageFont

root=Path(__file__).resolve().parent
folder=root/'render'
pdf=pdfium.PdfDocument(str(folder/'template.pdf'))
reader=PdfReader(str(folder/'template.pdf'))
records=[]
for i,page in enumerate(pdf):
    image=page.render(scale=1.5).to_pil()
    image.save(folder/f'page-{i+1}.png')
    text=reader.pages[i].extract_text()
    records.append({'page':i+1,'chars':len(text),'text':text})
pdf.close()
(folder/'page_text.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
for start in range(0,len(records),6):
    sheet=Image.new('RGB',(1200,1740),'#dde3e8')
    draw=ImageDraw.Draw(sheet)
    for k in range(6):
        i=start+k
        if i>=len(records):break
        im=Image.open(folder/f'page-{i+1}.png');im.thumbnail((570,540))
        x=15+(k%2)*600;y=35+(k//2)*580
        sheet.paste(im,(x,y))
        draw.text((x,y-25),f'Page {i+1}',fill='black')
    sheet.save(folder/f'contact-{start+1}.png')
print(json.dumps({'pages':len(records),'low_text_pages':[r['page'] for r in records if r['chars']<100],'characters':sum(r['chars'] for r in records)}))
