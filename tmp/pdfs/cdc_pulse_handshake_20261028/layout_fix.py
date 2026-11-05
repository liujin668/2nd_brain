from pathlib import Path
p=Path('tmp/pdfs/cdc_pulse_handshake_20261028/build_spec.py')
s=p.read_text(encoding='utf-8')
s=s.replace("spaceAfter=7,wordWrap='CJK',textColor=NAVY,allowWidows=0","spaceAfter=7,rightIndent=12,wordWrap='CJK',textColor=NAVY,allowWidows=0")
p.write_text(s,encoding='utf-8')
