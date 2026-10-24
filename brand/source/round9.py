import math, os, sys
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'round7.py'),encoding='utf-8').read()
exec(src[:src.index('# S1 tin-can')])   # K, plate, rivet, screw, spring, eyes, colours
TOP="#B4BCC4"

def crack_and_tape(pts, tape_at=(0.5,), length=15, width=6):
    o=f'<polyline points="{P(pts)}" fill="none" stroke="{SL}" stroke-width="2" stroke-linejoin="round"/>'
    (x0,y0),(x1,y1)=pts[0],pts[-1]
    ang=math.degrees(math.atan2(y1-y0,x1-x0))+90
    for t in tape_at:
        cx,cy=x0+(x1-x0)*t,y0+(y1-y0)*t
        o+=f'<g transform="rotate({ang:.1f} {cx:.1f} {cy:.1f})"><rect x="{cx-length/2:.1f}" y="{cy-width/2:.1f}" width="{length}" height="{width}" fill="{TAPE}"/><rect x="{cx-length/2:.1f}" y="{cy-width/2:.1f}" width="{length}" height="1.6" fill="{TAPE2}"/></g>'
    return o

def box_head(dx=16, dy=-11):
    """A head with depth: a lighter top, a darker side, the front, and a chamfer light."""
    front=[(36,62),(140,56),(148,64),(148,160),(140,168),(36,170),(28,162),(28,70)]
    if dx>=0:
        side=[(148,64),(140,56),(140+dx,56+dy),(148+dx,64+dy),(148+dx,160+dy),(148,160)]
    else:
        side=[(28,70),(36,62),(36+dx,62+dy),(28+dx,70+dy),(28+dx,162+dy),(28,162)]
    top=[(36,62),(140,56),(140+dx,56+dy),(36+dx,62+dy)]
    o=f'<polygon points="{P(side)}" fill="{SD}"/><polygon points="{P(top)}" fill="{TOP}"/><polygon points="{P(front)}" fill="{ST}"/>'
    o+=f'<polygon points="{P([(36,62),(140,56),(141,60),(37,66)])}" fill="{SL}" opacity="0.6"/>'
    o+=f'<polygon points="{P([(28,162),(36,170),(140,168),(148,160),(148,164),(140,172),(36,174),(28,166)])}" fill="{SD}"/>'
    return o

def screen():
    o=f'<polygon points="{P([(40,74),(138,70),(138,134),(40,138)])}" fill="{GUN}"/>'
    o+=f'<polygon points="{P([(45,79),(133,75),(133,129),(45,133)])}" fill="{SCR}"/>'
    o+=f'<polygon points="{P([(45,79),(133,75),(133,79),(45,83)])}" fill="#000000" opacity="0.35"/>'
    o+=f'<polygon points="{P([(56,79),(72,78),(50,120),(45,120)])}" fill="#FFFFFF" opacity="0.05"/>'
    o+=eyes(54,86,0.34,44)
    # crack only inside the screen, top-right corner, clear of both Ks
    o+=crack_and_tape([(132,78),(126,84),(130,89),(121,96)])
    return o

def antenna(kind, x=96, y=58):
    rod=lambda pts: f'<polyline points="{P(pts)}" fill="none" stroke="{SD}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>'
    if kind=="nut":
        o=rod([(x,y),(x+2,y-20),(x+12,y-30)])
        hexp=[(x+12+8*math.cos(math.pi/3*i),y-34+8*math.sin(math.pi/3*i)) for i in range(6)]
        return o+f'<polygon points="{P(hexp)}" fill="{RUST}"/><polygon points="{P([(x+12+3.5*math.cos(math.pi/3*i),y-34+3.5*math.sin(math.pi/3*i)) for i in range(6)])}" fill="{SD}"/>'
    if kind=="light":
        o=rod([(x,y),(x-2,y-26)])
        return o+f'<rect x="{x-10}" y="{y-40}" width="16" height="12" fill="{GUN}"/><rect x="{x-7}" y="{y-37}" width="10" height="6" fill="{TOX}"/>'
    if kind=="bolt":
        o=rod([(x,y),(x+4,y-18)])
        b=[(x+10,y-46),(x-2,y-28),(x+5,y-28),(x-1,y-14),(x+13,y-34),(x+6,y-34),(x+12,y-46)]
        return o+f'<polygon points="{P(b)}" fill="{HAZ}"/>'
    if kind=="flag":
        o=rod([(x,y),(x,y-36)])
        return o+f'<polygon points="{P([(x+2,y-36),(x+22,y-30),(x+2,y-24)])}" fill="{RUST}"/>'
    if kind=="washers":
        o=rod([(x,y),(x,y-12)])
        return o+''.join(f'<rect x="{x-9+k}" y="{y-16-k*6}" width="{18-2*k}" height="4" fill="{SL if k%2 else SD}"/>' for k in range(4))
    if kind=="fork":
        o=rod([(x,y),(x+6,y-22)])
        return o+rod([(x+6,y-22),(x,y-36)])+rod([(x+6,y-22),(x+16,y-34)])+f'<rect x="{x-3}" y="{y-39}" width="6" height="5" fill="{TOX}"/><rect x="{x+13}" y="{y-37}" width="6" height="5" fill="{TOX}"/>'
    return ''

def mouth(kind):
    if kind=="grill":
        o=''
        for i in range(6):
            t=i/5; x=58+t*64; y=138+8*(1-(2*t-1)**2)
            o+=f'<rect x="{x-3:.1f}" y="{y:.1f}" width="6" height="11" rx="1" fill="{SCR}"/>'
        return o
    if kind=="smirk":
        return f'<path d="M58 146 Q90 158 122 144" fill="none" stroke="{SCR}" stroke-width="5" stroke-linecap="round"/>'
    if kind=="zig":
        pts=[]
        for i in range(9):
            t=i/8; x=58+t*64; base=150-10*(1-(2*t-1)**2)*-1
            pts.append((x, 154-8*(2*t-1)**2 + (3 if i%2 else -3)))
        return f'<polyline points="{P(pts)}" fill="none" stroke="{SCR}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
    if kind=="slot":
        return f'<path d="M60 142 L120 142 Q118 158 90 158 Q62 158 60 142 Z" fill="{SCR}"/>'+''.join(f'<rect x="{x}" y="142" width="7" height="6" fill="{SL}"/>' for x in (70,82,94,106))
    if kind=="straight":
        return f'<path d="M60 148 L116 148 L124 141" fill="none" stroke="{SCR}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    return ''

def bot(name, ant, mth, dx=16, dy=-11, extra=''):
    s=antenna(ant)+box_head(dx,dy)+screen()+mouth(mth)
    s+=rivet(36,72,3)+rivet(140,66,3)+rivet(36,158,3)+rivet(140,156,3)
    s+=screw(24,100,190,12)+extra
    w(name,s)

bot("u1.svg","nut","grill")
bot("u2.svg","light","smirk")
bot("u3.svg","bolt","zig")
bot("u4.svg","flag","slot",dx=-16,dy=-11,extra=screw(150,112,-10,12))
bot("u5.svg","washers","straight")
bot("u6.svg","fork","grill",dx=20,dy=-14,extra=f'<polygon points="{P([(170,176),(178,172),(176,182)])}" fill="{SL}"/>')

names=["u1","u2","u3","u4","u5","u6"]
cells="".join(f"<div style='width:400px;height:400px;display:flex;align-items:center;justify-content:center'><img src='{n}.svg' width='360' height='360'></div>" for n in names)
open("sheet6.html","w").write(f"<html><body style='margin:0;background:#15181B;display:grid;grid-template-columns:repeat(3,400px)'>{cells}</body></html>")
