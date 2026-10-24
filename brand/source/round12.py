import math, os, sys, random
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'round11.py'),encoding='utf-8').read()
exec(src[:src.index('labels=[]')])   # helpers + PALETTES + screen_col

face,side,top,light,bezel,scr,letters,nut,_=PALETTES["c2"]
ST,SD,TOP,SL,GUN,SCR,RUST=face,side,top,light,bezel,scr,nut
OUT="#2A1A12"

def outline(d=6,width=4):
    ox,oy=d,-d*0.7
    back=[(x+ox,y+oy) for x,y in FRONT]
    st=f'fill="{OUT}" stroke="{OUT}" stroke-width="{width*2}" stroke-linejoin="round"'
    o=f'<polygon points="{P(FRONT)}" {st}/><polygon points="{P(back)}" {st}/>'
    for i in range(len(FRONT)):
        q=[FRONT[i],FRONT[(i+1)%len(FRONT)],back[(i+1)%len(FRONT)],back[i]]
        o+=f'<polygon points="{P(q)}" {st}/>'
    return o

def patina(seed=4):
    random.seed(seed); o=''
    for x,y,r in [(60,152,3),(138,152,4),(150,146,2.5),(34,110,2.5)]:
        o+=f'<ellipse cx="{x}" cy="{y}" rx="{r*1.6:.1f}" ry="{r:.1f}" fill="#7E3714" opacity="0.35"/>'
    return o

def mouth(): return f'<polyline points="64,138 76,144 88,138 100,144 112,138" fill="none" stroke="{SD}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'

def screen_big_crack(col):
    o=f'<polygon points="{P([(44,72),(152,66),(154,128),(44,132)])}" fill="{GUN}"/>'
    o+=f'<polygon points="{P([(49,77),(148,71),(149,123),(49,127)])}" fill="{SCR}"/>'
    o+=f'<polygon points="{P([(49,77),(148,71),(148,75),(49,81)])}" fill="#000000" opacity="0.35"/>'
    o+=K(56,82,0.38,col)+K(104,84,0.38,col,droop=38)
    o+=crack_and_tape([(147,73),(138,82),(143,88),(131,98)],length=18,width=7)
    return o

def head(nut_col=RUST, rivets=True, out=False, pat=False, big_crack=False, antenna_kind="nut"):
    global RUST
    RUST=nut_col
    s=''
    if out: s+=outline()
    s+=antenna(antenna_kind,x=98,y=56)+thin_head(6)
    s+=screen_big_crack(letters) if big_crack else screen_col(letters)
    if pat: s+=patina()
    s+=mouth()
    if rivets: s+=rivet(40,66)+rivet(156,60)+rivet(40,152)
    return s

w("fin-1.svg", head())                                   # C2, no side screws
w("fin-2.svg", head(nut_col="#A6E22E"))                  # green nut to echo the eyes
w("fin-3.svg", head(out=True))                           # dark outline for small sizes
w("fin-4.svg", head(pat=True))                           # a little rust patina
w("fin-5.svg", head(big_crack=True, pat=True))           # bigger crack + patina

# small-size mark: no antenna detail, no crack, no rivets, thicker K
def tiny():
    s=f'<polygon points="{P(FRONT)}" fill="{ST}"/>'
    s+=f'<polygon points="{P([(44,72),(152,66),(154,128),(44,132)])}" fill="{SCR}"/>'
    s+=K(54,80,0.44,letters)+K(106,82,0.44,letters,droop=38)
    s+=f'<polyline points="64,144 80,152 96,144 112,152 128,144" fill="none" stroke="{SD}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'
    s+=f'<rect x="94" y="30" width="8" height="26" fill="{SD}"/>'
    s+=f'<polygon points="{P([(98+11*math.cos(math.pi/3*i),24+11*math.sin(math.pi/3*i)) for i in range(6)])}" fill="#59626B"/>'
    return s
w("fin-tiny.svg", tiny())

names=["fin-1","fin-2","fin-3","fin-4","fin-5","fin-tiny"]
cells="".join(f"<div style='width:400px;height:400px;display:flex;align-items:center;justify-content:center;gap:10px'><img src='{n}.svg' width='300' height='300'><img src='{n}.svg' width='32' height='32'><img src='{n}.svg' width='16' height='16'></div>" for n in names)
open("sheet9.html","w").write(f"<html><body style='margin:0;background:#15181B;display:grid;grid-template-columns:repeat(3,400px)'>{cells}</body></html>")
