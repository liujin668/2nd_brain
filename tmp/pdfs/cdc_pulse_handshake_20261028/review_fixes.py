from pathlib import Path
import re
work=Path('tmp/pdfs/cdc_pulse_handshake_20261028');bt=chr(96)
p=work/'spec_content.md';s=p.read_text(encoding='utf-8-sig')
s=s.replace('照片是分析依据，不包含对服务器执行操作的授权或指令。','照片是本说明的代码依据。')
s=s.replace('**无丢失使用条件**','**单事件传输的协议前提（数字逻辑层面）**')
s=s.replace(bt+'din'+bt+' 必须先被源时钟采到低电平，之后再被采到高电平，才能识别为下一次事件。','两个相邻事件之间，'+bt+'din'+bt+' 必须先被源时钟采到低电平，之后再被采到高电平，才能识别为下一次事件；复位后的首个事件另见第 8 节。')
s=s.replace(bt+'din & ~din_pipe'+bt,bt+'din && ~din_pipe'+bt)
s=s.replace('正反向同步器各假设为两级、目的时钟上升沿采样、复位值为 0；','正反向同步器各假设为两级，正向由 '+bt+'clk_dst'+bt+' 上升沿采样，回传由 '+bt+'clk_src'+bt+' 上升沿采样，复位值均为 0；')
s=s.replace('结构图、四组说明性时序','一张结构图、三组说明性时序图')
s=s.replace('异步置位、同步释放的复位同步宏说明','异步断言、同步释放的复位同步宏说明')
p.write_text(s,encoding='utf-8')
p=work/'build_spec.py';s=p.read_text(encoding='utf-8')
s=s.replace("['目的域上升沿检测','Q && ~Q_delay','dout 为组合表达式']","['Q_delay <= Q @clk_dst','dout = Q && ~Q_delay','延迟寄存器 + 组合边沿检测']")
s=s.replace("FENCE=chr(96)*3","""FENCE=chr(96)*3
def code_rich(s):
    return re.sub(r'[^\\x00-\\x7f]+',lambda m:'<font name="CN">'+m.group(0)+'</font>',html.escape(s))""")
s=s.replace("XPreformatted(html.escape(raw),st)","XPreformatted(code_rich(raw),st)")
s=s.replace("def wave(name,end,din,R,Q,A,pulses,events,consumers):","""PLOT_DATA={}
def wave(name,end,din,R,Q,A,pulses,events,consumers):
    PLOT_DATA[name]={'end':end,'din':din,'din_store':R,'din_store_sync2dst':Q,'din_store_sync2src':A,'dout':sum(([(a,1),(b,0)] for a,b in pulses),[]),'sampled_in_events':events,'consumer_samples':consumers}""")
validator="""def verify_figures():
    data=json.loads((WORK/'timing_examples.json').read_text(encoding='utf-8-sig'))
    mapping={'02_normal_timing':'normal_single','03_busy_merge':'busy_merge','04_safe_repeat':'rearmed_two'}
    report={}
    for fig,case_name in mapping.items():
        case=next(c for c in data['cases'] if c['name']==case_name)
        plot=PLOT_DATA[fig];end=plot['end']
        for signal in ['din','din_store','din_store_sync2dst','din_store_sync2src','dout']:
            expected=[(v['time_ns'],v['value']) for v in case['transitions'] if v['signal']==signal and v['time_ns']<=end]
            assert plot[signal]==expected,(fig,signal,plot[signal],expected)
        for kind in ['sampled_in_events','consumer_samples']:
            assert plot[kind]==[t for t in case['summary'][kind] if t<=end]
        report[fig]={'matched_independent_model':True,'signals_checked':5,'summary':case['summary']}
    (WORK/'plot_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print('All waveform transitions agree with the independent event model.')
"""
s=s.replace("PAGE_W,PAGE_H=A4;",validator+'\nPAGE_W,PAGE_H=A4;')
s=s.replace("if '--figures-only' in sys.argv:figures();print('Four diagram assets generated.')","if '--figures-only' in sys.argv:figures();verify_figures();print('Four diagram assets generated.')")
p.write_text(s,encoding='utf-8')
