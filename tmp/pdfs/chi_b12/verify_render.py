from pathlib import Path
import json
import re
import math
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
manifest = json.loads((BASE/'build_manifest.json').read_text(encoding='utf-8'))
path = Path(manifest['pdf'])
reader = PdfReader(path)
text = '\n'.join(p.extract_text() for p in reader.pages)
assert '\ufffd' not in text, 'Replacement characters found'
assert set(manifest['source_pages']) == set(range(429,452))
assert all(f'B12.{i} ' in text or f'B12.{i}\n' in text for i in range(1,14))
assert len(reader.outline) == 13, len(reader.outline)
assert all(len(p.extract_text()) > 100 for p in reader.pages)
for token in ['TagGroupID','ReturnNID','TraceTag','MTE_Support','WriteDataCancel',
              'ReadOnceCleanInvalid','SnpPreferUniqueFwd','Comp_UC','Comp_SC',
              'DatLCrdReturn','B16.24','B13.10.46','B9.1.4','B4.38',
              'Data_Width/32','Data_Width/128']:
    assert token in text.replace(' ','').replace('\n',''), token

qa = BASE/'qa'
qa.mkdir(exist_ok=True)
doc = pdfium.PdfDocument(str(path))
thumbs = []
for i in range(len(doc)):
    page = doc[i]
    image = page.render(scale=1.6).to_pil().convert('RGB')
    image.save(qa/f'page_{i+1:02}.png')
    thumb = image.copy()
    thumb.thumbnail((595,842))
    thumbs.append(thumb)
font = ImageFont.truetype('C:/Windows/Fonts/consola.ttf',18)
for start in range(0,len(thumbs),6):
    sheet = Image.new('RGB',(1240,2670),'#dbe2e8')
    draw = ImageDraw.Draw(sheet)
    for k, thumb in enumerate(thumbs[start:start+6]):
        x = 15+(k%2)*620
        y = 32+(k//2)*890
        draw.text((x,y-24),f'PDF page {start+k+1}',fill='#183040',font=font)
        sheet.paste(thumb,(x,y))
    sheet.save(qa/f'contact_{start//6+1:02}.jpg',quality=90)

report = {
    'pdf':str(path), 'pages':len(reader.pages), 'outlines':len(reader.outline),
    'source_pages':manifest['source_pages'], 'replacement_characters':0,
    'text_characters':len(text), 'bytes':path.stat().st_size,
    'page_characters':[len(p.extract_text()) for p in reader.pages],
    'contact_sheets':[str(p) for p in sorted(qa.glob('contact_*.jpg'))],
}
(qa/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(qa/'pdf_text.txt').write_text(text,encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
