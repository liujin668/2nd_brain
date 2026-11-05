from pathlib import Path
p=Path('tmp/pdfs/cdc_pulse_handshake_20261028/build_spec.py')
s=p.read_text(encoding='utf-8-sig')
s=s.replace("'din & ~din_pipe'","'din && ~din_pipe'").replace("'Q & ~Q_delay'","'Q && ~Q_delay'")
s=s.replace("rows=[('clk_src'", """idle=[]; rstate=0; astate=0; oldidle=1
    for t in sorted(set(t for t,v in R+A)):
        rstate=next((v for x,v in reversed(R) if x<=t),0);astate=next((v for x,v in reversed(A) if x<=t),0)
        newidle=int(not(rstate or astate))
        if newidle!=oldidle:idle.append((t,newidle));oldidle=newidle
    rows=[('clk_src'""")
s=s.replace("('idle*',[(0,1)]+sum(([(a,0),(b,1)] for a,b in zip([10,110],[100,190]) if a<=end),[]),GREY)","('idle*',idle,GREY)")
p.write_text(s,encoding='utf-8')
