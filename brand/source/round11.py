import math, os, sys
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'round10.py'),encoding='utf-8').read()
exec(src[:src.index('def bot(name,d)')])   # thin_head, smile, antenna, crack_and_tape, K, rivet, screw...

# name: (face, side, top, light, bezel, screen, letters, nut, label)
PALETTES = {
 "c1": ("#8A949E","#59626B","#B4BCC4","#C3CAD1","#3A4148","#1B2024","#A6E22E","#B5521F","Steel · toxic green"),
 "c2": ("#B5521F","#7E3714","#D07A45","#E8A47A","#3A2A22","#1B1714","#A6E22E","#59626B","Rust · toxic green"),
 "c3": ("#6B7A3A","#495427","#8C9A5A","#B2BE86","#2F3420","#161A10","#F2C230","#B5521F","Olive · amber"),
 "c4": ("#F2C230","#B38A12","#F7D86A","#FBE9A6","#2B2B2B","#151515","#FF7A2E","#3A4148","Hazard yellow · orange"),
 "c5": ("#5E7C86","#3F5760","#86A2AB","#B2C7CD","#26343A","#0E1A1E","#FFB23E","#B5521F","Teal steel · amber screen"),
 "c6": ("#2E3338","#1C1F23","#454B52","#6B737B","#121417","#0B0D0F","#A6E22E","#B5521F","Matte black · toxic green"),
 "c7": ("#E6E0D2","#B9B1A0","#F4F0E6","#FFFFFF","#3A4148","#1B2024","#E5483A","#B5521F","Bone white · red"),
 "c8": ("#B8733E","#83502A","#D2925E","#E8B98F","#2E2620","#121716","#3FD6D0","#59626B","Copper · cyan"),
 "c9": ("#8A949E","#59626B","#B4BCC4","#C3CAD1","#3A4148","#1B2024","#FF5FA2","#F2C230","Steel · hot pink"),
}

def screen_col(col):
    o=f'<polygon points="{P([(44,72),(152,66),(154,128),(44,132)])}" fill="{GUN}"/>'
    o+=f'<polygon points="{P([(49,77),(148,71),(149,123),(49,127)])}" fill="{SCR}"/>'
    o+=f'<polygon points="{P([(49,77),(148,71),(148,75),(49,81)])}" fill="#000000" opacity="0.35"/>'
    o+=K(56,82,0.38,col)+K(104,84,0.38,col,droop=38)
    o+=crack_and_tape([(147,74),(140,81),(144,86),(134,94)])
    return o

labels=[]
for name,(face,side,top,light,bezel,scr,letters,nut,label) in PALETTES.items():
    ST,SD,TOP,SL,GUN,SCR,RUST=face,side,top,light,bezel,scr,nut
    s=antenna("nut",x=98,y=56)+thin_head(6)+screen_col(letters)
    s+=f'<polyline points="64,138 76,144 88,138 100,144 112,138" fill="none" stroke="{SD}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
    s+=rivet(40,66)+rivet(156,60)+rivet(40,152)+screw(168,128,-10,16)+screw(24,92,190,12)
    w(f"col-{name}.svg",s)
    labels.append((name,label))

cells="".join(f"<div style='width:400px;height:400px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#ccc;font:14px sans-serif'><img src='col-{n}.svg' width='330' height='330'>{l}</div>" for n,l in labels)
open("sheet8.html","w").write(f"<html><body style='margin:0;background:#15181B;display:grid;grid-template-columns:repeat(3,400px)'>{cells}</body></html>")
