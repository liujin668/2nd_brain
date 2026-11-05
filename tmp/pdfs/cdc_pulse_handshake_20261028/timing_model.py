"""Illustrative event model, NOT RTL simulation. See JSON assumptions."""
import csv
import json
from pathlib import Path
OUT = Path(__file__).resolve().parent
SIGNALS = ['din','din_pipe','din_store','forward_ff1','din_store_sync2dst','din_store_sync2dst_pipe','backward_ff1','din_store_sync2src']
def derived(s):
    return {'din_re':s['din'] & (1-s['din_pipe']), 'dout':s['din_store_sync2dst'] & (1-s['din_store_sync2dst_pipe']), 'internal_idle':(1-s['din_store']) & (1-s['din_store_sync2src'])}
def simulate(name, changes, end=240):
    changes = dict(changes)
    src = set(range(0,end+1,10))
    dst = set(range(3,end+1,16))
    assert not src.intersection(dst)
    assert not set(changes).intersection(src|dst)
    s = dict.fromkeys(SIGNALS,0)
    summary = {k:[] for k in ['sampled_in_events','dout_rises','dout_falls','consumer_samples','idle_return']}
    rows=[]
    transitions=[]
    for t in sorted(src|dst|set(changes)):
        old=dict(s)
        pre=derived(old)
        event=[]
        sampled=consumer=0
        if t in changes:
            s['din']=changes[t]
            event.append('din_change')
        if t in src:
            event.append('src_rise')
            sampled=pre['din_re']
            if sampled: summary['sampled_in_events'].append(t)
            s['din_pipe']=old['din']
            s['din_store']=1 if sampled else 0 if old['din_store_sync2src'] else old['din_store']
            s['backward_ff1']=old['din_store_sync2dst']
            s['din_store_sync2src']=old['backward_ff1']
        if t in dst:
            event.append('dst_rise')
            consumer=pre['dout']
            if consumer: summary['consumer_samples'].append(t)
            s['forward_ff1']=old['din_store']
            s['din_store_sync2dst']=old['forward_ff1']
            s['din_store_sync2dst_pipe']=old['din_store_sync2dst']
        post=derived(s)
        if not pre['dout'] and post['dout']: summary['dout_rises'].append(t)
        if pre['dout'] and not post['dout']: summary['dout_falls'].append(t)
        if not pre['internal_idle'] and post['internal_idle']: summary['idle_return'].append(t)
        for key,value in dict(s,**post).items():
            if value != dict(old,**pre)[key]: transitions.append({'time_ns':t,'signal':key,'value':value})
        rows.append(dict(time_ns=t,event='+'.join(event),**s,**post,sampled_in_event=sampled,consumer_sample=consumer))
    summary['sampled_in_event_count']=len(summary['sampled_in_events'])
    summary['dout_pulse_count']=len(summary['dout_rises'])
    return {'name':name,'din_changes':[{'time_ns':t,'value':v} for t,v in sorted(changes.items())],'end_ns':end,'summary':summary,'transitions':transitions,'rows':rows}
def main():
    cases=[simulate('normal_single',[(6,1),(16,0)],160),simulate('busy_merge',[(6,1),(16,0),(26,1),(36,0)],160),simulate('rearmed_two',[(6,1),(16,0),(106,1),(116,0)],240),simulate('unsafe_partial_rearm',[(6,1),(16,0),(66,1),(76,0)],180)]
    result={case['name']:case['summary'] for case in cases}
    assert result['normal_single']['sampled_in_events']==[10]
    assert result['normal_single']['dout_rises']==[35]
    assert result['normal_single']['dout_falls']==[51]
    assert result['normal_single']['consumer_samples']==[51]
    assert result['normal_single']['idle_return']==[100]
    assert result['busy_merge']['sampled_in_events']==[10,30]
    assert result['busy_merge']['dout_rises']==[35]
    assert result['rearmed_two']['sampled_in_events']==[10,110]
    assert result['rearmed_two']['dout_rises']==[35,131]
    assert result['rearmed_two']['consumer_samples']==[51,147]
    assert result['rearmed_two']['idle_return']==[100,190]
    assert result['unsafe_partial_rearm']['sampled_in_events']==[10,70]
    assert result['unsafe_partial_rearm']['dout_rises']==[35]
    data={'model_kind':'illustrative Python event model; NOT RTL simulation or CDC signoff','assumptions':['Each unprovided acs_cdc_capt_sync is modeled as exactly TWO positive-edge flip-flops.','Both active-low resets have already initialized all registers to zero and safely released before t=0.','No metastability, recovery/removal violation, setup/hold violation, reset operation or stopped clock is modeled.','All same-domain registers sample old values and update atomically after the edge (NBA-like).','Noncoincident rising edges; din changes away from clock edges.','internal_idle is explanatory only: the pictured IP has no ready/busy output.','sampled_in_events records source-side din_re detection, NOT successfully queued or delivered transactions.'],'clocks':{'src_period_ns':10,'dst_period_ns':16,'src_first_rise_ns':0,'dst_first_rise_ns':3},'cases':cases,'checks':'All expected event-time assertions passed.'}
    (OUT/'timing_examples.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    for case in cases:
        with (OUT/(case['name']+'.csv')).open('w',encoding='utf-8',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=list(case['rows'][0]))
            writer.writeheader()
            writer.writerows(case['rows'])
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
