import math, os, sys
os.chdir(sys.argv[1])
def w(n,s): open(n,'w',encoding='utf-8').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'+s+'</svg>')
def P(pts): return " ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
ST="#8A949E"; SD="#59626B"; SL="#C3CAD1"; GUN="#3A4148"; RUST="#B5521F"; RL="#D9763B"; SCR="#1B2024"
TOX="#A6E22E"; DARK="#12161A"; TAPE="#C9B98F"; TAPE2="#B3A375"; HAZ="#F2C230"; WIRE="#C2581E"

STEM=[(0,0),(22,0),(22,100),(0,100)]
ARM=[(20,50),(52,0),(78,0),(34,66)]
LEG=[(32,46),(50,36),(82,100),(56,100)]
PIV=(28,58)
def tf(pts,x,y,s): return [(x+px*s,y+py*s) for px,py in pts]
def K(x,y,s,col,droop=None):
    o=f'<polygon points="{P(tf(STEM,x,y,s))}" fill="{col}"/><polygon points="{P(tf(LEG,x,y,s))}" fill="{col}"/>'
    arm=f'<polygon points="{P(tf(ARM,x,y,s))}" fill="{col}"/>'
    if droop is None: return o+arm
    px,py=x+PIV[0]*s,y+PIV[1]*s
    return o+f'<g transform="rotate({droop} {px:.1f} {py:.1f})">{arm}</g>'

def plate(pts,face=ST,shade=SD,d=5):
    sh=[(x+d,y+d) for x,y in pts]
    return f'<polygon points="{P(sh)}" fill="{shade}"/><polygon points="{P(pts)}" fill="{face}"/>'
def rivet(x,y,r=3.5): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SL}"/><circle cx="{x+r*0.3:.1f}" cy="{y+r*0.3:.1f}" r="{r*0.45:.1f}" fill="{SD}"/>'
def screw(x,y,ang,len_=18,col=SL):
    # a loose screw sticking out: head + shaft at an angle
    a=math.radians(ang); ex,ey=x+len_*math.cos(a),y+len_*math.sin(a)
    o=f'<line x1="{x}" y1="{y}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{SD}" stroke-width="4" stroke-linecap="round"/>'
    for k in range(1,4):
        t=k/4; cx,cy=x+(ex-x)*t,y+(ey-y)*t; nx,ny=-math.sin(a)*3,math.cos(a)*3
        o+=f'<line x1="{cx-nx:.1f}" y1="{cy-ny:.1f}" x2="{cx+nx:.1f}" y2="{cy+ny:.1f}" stroke="{SL}" stroke-width="1.2"/>'
    hx,hy=ex+5*math.cos(a),ey+5*math.sin(a)
    o+=f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="6" fill="{col}"/><line x1="{hx-3*math.sin(a):.1f}" y1="{hy+3*math.cos(a):.1f}" x2="{hx+3*math.sin(a):.1f}" y2="{hy-3*math.cos(a):.1f}" stroke="{SD}" stroke-width="2"/>'
    return o
def spring(x0,y0,x1,y1,n=6,amp=6,col=SL):
    dx,dy=x1-x0,y1-y0; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L; nx,ny=-uy,ux
    pts=[(x0,y0)]
    for i in range(1,2*n):
        t=i/(2*n); s=amp if i%2 else -amp
        pts.append((x0+dx*t+nx*s,y0+dy*t+ny*s))
    pts.append((x1,y1))
    return f'<polyline points="{P(pts)}" fill="none" stroke="{col}" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>'
def wire(d,col=WIRE): return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="3" stroke-linecap="round"/>'
def eyes(x,y,s,gap,col=TOX): return K(x,y,s,col)+K(x+gap,y+2,s,col,droop=38)

# S1 tin-can: tilted trapezoid head, rust patch, spring out of the top, bent antenna
s=f'<g transform="rotate(-4 100 110)">'
s+=spring(58,52,44,22,5,5)+f'<circle cx="44" cy="20" r="5" fill="{RUST}"/>'
s+=f'<polyline points="134,52 138,30 152,22" fill="none" stroke="{SD}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/><circle cx="153" cy="21" r="5" fill="{TOX}"/>'
head=[(44,52),(154,48),(166,150),(34,156)]
s+=plate(head)
s+=f'<polygon points="{P([(54,68),(146,66),(150,124),(52,128)])}" fill="{SCR}"/>'
s+=eyes(66,78,0.36,46)
s+=f'<polygon points="{P([(112,132),(160,128),(162,150),(110,152)])}" fill="{RUST}"/>'+rivet(116,136,2.8)+rivet(156,133,2.8)+rivet(116,148,2.8)
s+=f'<line x1="60" y1="140" x2="100" y2="139" stroke="{SD}" stroke-width="4"/>'+''.join(f'<line x1="{x}" y1="134" x2="{x}" y2="146" stroke="{SD}" stroke-width="2.5"/>' for x in (68,78,88))
s+=rivet(50,60)+rivet(148,56)+rivet(42,146)
s+='</g>'+screw(170,92,20)+f'<polygon points="{P([(30,176),(38,172),(36,182)])}" fill="{SL}"/>'
w("s-tincan.svg",s)

# S2 mismatched sockets: square screen + round porthole, dish ear and bolt ear, hanging wire
s=f'<polygon points="{P([(26,72),(14,60),(10,96),(26,88)])}" fill="{SD}"/><ellipse cx="14" cy="78" rx="6" ry="20" fill="{ST}"/>'
s+=f'<rect x="168" y="82" width="16" height="22" fill="{SD}"/><polygon points="{P([(184,86),(192,90),(192,98),(184,102)])}" fill="{SL}"/>'
head=[(28,46),(170,40),(174,148),(168,160),(32,164),(26,152)]
s+=plate(head)
s+=f'<polygon points="{P([(42,62),(96,60),(98,116),(44,118)])}" fill="{SCR}"/>'+K(52,70,0.44,TOX)
s+=f'<circle cx="134" cy="90" r="30" fill="{SD}"/><circle cx="134" cy="90" r="24" fill="{SCR}"/>'+K(118,74,0.36,TOX,droop=38)
s+=''.join(rivet(134+27*math.cos(a),90+27*math.sin(a),2.6) for a in [i*math.pi/3 for i in range(6)])
s+=f'<polygon points="{P([(50,132),(150,128),(150,146),(50,150)])}" fill="{GUN}"/>'+''.join(f'<rect x="{x}" y="132" width="6" height="14" fill="{SCR}"/>' for x in (60,74,88,102,116,130))
s+=wire("M60 158 C58 176 72 178 70 192")+rivet(40,56)+rivet(160,52)
s+=screw(98,40,-100,16)
w("s-sockets.svg",s)

# S3 bucket head: narrower top, dents, crooked handle as antenna, spring out of the side
s=f'<path d="M58 48 Q100 -4 146 50" fill="none" stroke="{SD}" stroke-width="5" stroke-linecap="round"/><circle cx="58" cy="48" r="4" fill="{SL}"/><circle cx="146" cy="50" r="4" fill="{SL}"/>'
head=[(56,46),(148,46),(170,158),(30,158)]
s+=plate(head)
s+=f'<polygon points="{P([(50,58),(156,58),(158,68),(48,68)])}" fill="{SD}"/>'
s+=f'<polygon points="{P([(56,78),(146,78),(154,128),(48,128)])}" fill="{SCR}"/>'+eyes(66,86,0.36,46)
s+=f'<path d="M128 140 q8 -6 14 2 q-6 6 -14 -2 z" fill="{SD}"/><path d="M50 98 q6 -4 8 4 q-6 4 -8 -4 z" fill="{SD}"/>'
s+=f'<polygon points="{P([(30,158),(170,158),(172,168),(28,168)])}" fill="{SD}"/>'
s+=spring(164,106,192,96,4,5)+f'<circle cx="193" cy="95" r="5" fill="{HAZ}"/>'
s+=f'<line x1="84" y1="142" x2="118" y2="140" stroke="{TOX}" stroke-width="4" stroke-linecap="round"/>'
s+=screw(26,120,200,14)
w("s-bucket.svg",s)

# S4 taped screen: angular head, cracked screen taped over the drooping side, screws out
head=[(36,50),(150,44),(168,62),(166,150),(150,162),(34,158),(26,140),(28,62)]
s=f'<rect x="92" y="18" width="7" height="30" fill="{SD}" transform="rotate(8 95 48)"/><circle cx="99" cy="18" r="6" fill="{RUST}"/>'
s+=plate(head)
s+=f'<polygon points="{P([(46,66),(150,62),(152,122),(46,126)])}" fill="{SCR}"/>'+eyes(56,74,0.38,50)
s+=f'<polyline points="152,64 140,78 148,86 134,100" fill="none" stroke="{SL}" stroke-width="2.2" stroke-linejoin="round"/>'
s+=f'<g transform="rotate(-42 144 80)"><rect x="124" y="74" width="44" height="12" fill="{TAPE}"/><rect x="124" y="74" width="44" height="3" fill="{TAPE2}"/></g>'
s+=f'<polyline points="64,140 76,134 88,140 100,134 112,140" fill="none" stroke="{SD}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
s+=rivet(40,62)+rivet(158,58)+rivet(40,148)+screw(166,128,-10,16)+screw(24,92,190,12)
w("s-taped.svg",s)

# S5 jaw unhinged: head + jaw hanging on one side by a spring
head=[(34,40),(162,36),(170,118),(30,122)]
s=f'<polygon points="{P([(150,38),(170,6),(176,10),(158,40)])}" fill="{SD}"/>'
s+=plate(head)
s+=f'<polygon points="{P([(46,52),(152,50),(156,106),(44,108)])}" fill="{SCR}"/>'+eyes(58,58,0.4,52)
s+=rivet(40,48)+rivet(158,44)
jaw=[(36,128),(162,124),(164,150),(40,154)]
s+=f'<g transform="rotate(14 40 130)">{plate(jaw,ST,SD,4)}'+''.join(f'<rect x="{x}" y="128" width="8" height="10" fill="{SL}"/>' for x in (54,72,90,108,126))+'</g>'
s+=f'<circle cx="40" cy="126" r="5" fill="{SL}"/>'+spring(160,120,150,160,4,5)
s+=screw(24,72,200,14)
w("s-jaw.svg",s)

# S6 goblin-ear scrap bot: one long fin ear, one broken stub, patch, spring and screw out
head=[(40,50),(150,46),(164,68),(160,156),(44,160),(32,136)]
s=f'<polygon points="{P([(40,80),(2,52),(10,74),(40,106)])}" fill="{SD}"/><polygon points="{P([(40,84),(12,64),(14,72),(40,98)])}" fill="{ST}"/>'
s+=f'<polygon points="{P([(160,88),(176,80),(172,92),(184,96),(162,106)])}" fill="{SD}"/>'
s+=plate(head)
s+=f'<polygon points="{P([(50,64),(148,62),(150,120),(52,122)])}" fill="{SCR}"/>'+eyes(60,72,0.38,48)
s+=f'<polygon points="{P([(48,128),(96,126),(98,152),(50,154)])}" fill="{RUST}"/>'+rivet(54,132,2.6)+rivet(90,131,2.6)+rivet(55,148,2.6)
s+=''.join(f'<line x1="{x}" y1="132" x2="{x}" y2="150" stroke="{SD}" stroke-width="3"/>' for x in (112,122,132,142))
s+=spring(96,48,86,14,5,5)+f'<circle cx="85" cy="12" r="5" fill="{TOX}"/>'+screw(150,46,-60,14)
w("s-goblin.svg",s)

names=["s-tincan","s-sockets","s-bucket","s-taped","s-jaw","s-goblin"]
cells="".join(f"<div style='width:400px;height:400px;display:flex;align-items:center;justify-content:center'><img src='{n}.svg' width='360' height='360'></div>" for n in names)
open("sheet4.html","w").write(f"<html><body style='margin:0;background:#15181B;display:grid;grid-template-columns:repeat(3,400px)'>{cells}</body></html>")
