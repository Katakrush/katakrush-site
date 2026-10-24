import math, os, sys
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'round12.py'),encoding='utf-8').read()
exec(src[:src.index('w("fin-1.svg"')])
def final(mouth_col, mouth_w):
    global RUST
    RUST="#A6E22E"
    s=outline()+antenna("nut",x=98,y=56)+thin_head(6)+screen_col(letters)
    s+=f'<polyline points="62,138 75,145 88,138 101,145 114,138" fill="none" stroke="{mouth_col}" stroke-width="{mouth_w}" stroke-linejoin="round" stroke-linecap="round"/>'
    s+=rivet(40,66)+rivet(156,60)+rivet(40,152)
    return s
w("final-dark.svg", final("#2A1A12",6))
w("final-green.svg", final("#A6E22E",5.5))
cells="".join(f"<div style='display:flex;align-items:center;gap:14px;padding:20px;background:{bg}'><img src='{n}.svg' width='260'><img src='{n}.svg' width='64'><img src='{n}.svg' width='40'><img src='{n}.svg' width='24'></div>" for n in ("final-dark","final-green") for bg in ("#15181B","#E6E0D2"))
open("sheet10.html","w").write(f"<html><body style='margin:0;display:grid;grid-template-columns:repeat(2,600px)'>{cells}</body></html>")
