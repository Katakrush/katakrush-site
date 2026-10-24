import math, os, sys
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'round9.py'),encoding='utf-8').read()
exec(src[:src.index('def bot(name')])   # K, eyes, rivet, screw, antenna, crack_and_tape, colours

FRONT=[(36,58),(150,52),(168,70),(166,152),(150,166),(34,162),(26,144),(28,66)]

def thin_head(d):
    """S4's angular head as one solid piece: a thin top and side, not a second sheet behind it."""
    o=''
    n=len(FRONT)
    # the depth: for every edge facing up or right, a thin face pushed back by (d, -d*0.7)
    ox,oy=d,-d*0.7
    for i in range(n):
        (x0,y0),(x1,y1)=FRONT[i],FRONT[(i+1)%n]
        nx,ny=(y1-y0),-(x1-x0)                     # outward normal (points are clockwise)
        if nx*ox+ny*oy>0:
            col=TOP if ny<0 and abs(ny)>abs(nx) else SD
            o+=f'<polygon points="{P([(x0,y0),(x1,y1),(x1+ox,y1+oy),(x0+ox,y0+oy)])}" fill="{col}"/>'
    o+=f'<polygon points="{P(FRONT)}" fill="{ST}"/>'
    o+=f'<polygon points="{P([(36,58),(150,52),(152,56),(37,62)])}" fill="{SL}" opacity="0.55"/>'
    return o

def screen():
    o=f'<polygon points="{P([(44,72),(152,66),(154,128),(44,132)])}" fill="{GUN}"/>'
    o+=f'<polygon points="{P([(49,77),(148,71),(149,123),(49,127)])}" fill="{SCR}"/>'
    o+=f'<polygon points="{P([(49,77),(148,71),(148,75),(49,81)])}" fill="#000000" opacity="0.35"/>'
    o+=eyes(56,82,0.38,48)
    o+=crack_and_tape([(147,74),(140,81),(144,86),(134,94)])
    return o

def smile():
    # S4's zigzag, turned over: the ends now go up
    return f'<polyline points="64,138 76,144 88,138 100,144 112,138" fill="none" stroke="{SD}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'

def bot(name,d):
    s=antenna("nut",x=98,y=56)+thin_head(d)+screen()+smile()
    s+=rivet(40,66)+rivet(156,60)+rivet(40,152)
    s+=screw(168,128,-10,16)+screw(24,92,190,12)
    w(name,s)

bot("f-d3.svg",3)
bot("f-d6.svg",6)
bot("f-d9.svg",9)
names=["f-d3","f-d6","f-d9"]
cells="".join(f"<div style='width:400px;height:400px;display:flex;align-items:center;justify-content:center'><img src='{n}.svg' width='360' height='360'></div>" for n in names)
open("sheet7.html","w").write(f"<html><body style='margin:0;background:#15181B;display:grid;grid-template-columns:repeat(3,400px)'>{cells}</body></html>")
