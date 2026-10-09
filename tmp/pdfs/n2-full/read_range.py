import json, sys, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
p=json.loads((Path(__file__).parent/'pages.json').read_text(encoding='utf-8'))
for spec in sys.argv[1:]:
 a,*b=spec.split('-');start=int(a);end=int(b[0]) if b else start
 for i in range(start-1,end):
  t=p[i].replace('\r','')
  t=re.sub(r'Arm® Neoverse™ N2 Core Technical Reference Manual Document ID: 102099_0003_06_en\s+Issue: 06\s*','',t)
  t=re.sub(r'Copyright © 2020–2022 Arm Limited.*?2026-10-09','',t,flags=re.S)
  t=re.sub(r'\n\s*\n','\n',t)
  print(f'\n===== PAGE {i+1} =====\n{t}')
