"""Render the central-square measurements as a self-contained HTML/SVG page (no deps)."""
import glob, math, html

pts = {}
for f in glob.glob('sweep_*.txt'):
    for line in open(f):
        n, s, _ = line.split()
        n, s = int(n), int(s)
        if n >= 30 and s > 0:
            pts[n] = s
pts = sorted(pts.items())
xs = [n for n, _ in pts]; ys = [s for _, s in pts]

# least squares side = a*n + c
N = len(pts); mx = sum(xs)/N; my = sum(ys)/N
a = sum((x-mx)*(y-my) for x, y in pts)/sum((x-mx)**2 for x in xs); c = my - a*mx

W, H = 720, 300; L, R, T, B = 56, 96, 28, 40
def sx(n): return L + (n - 0) / (max(xs)+20) * (W - L - R)
def sy(v, lo, hi): return T + (hi - v) / (hi - lo) * (H - T - B)

def axis(lo, hi, step, fmt, ylab):
    out = []
    v = lo
    while v <= hi + 1e-9:
        y = sy(v, lo, hi)
        out.append(f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" class="grid"/>')
        out.append(f'<text x="{L-6}" y="{y+4:.1f}" class="tick" text-anchor="end">{fmt(v)}</text>')
        v += step
    for n in range(0, max(xs)+1, 100):
        x = sx(n)
        out.append(f'<text x="{x:.1f}" y="{H-B+16}" class="tick" text-anchor="middle">{n}</text>')
    out.append(f'<text x="{(L+W-R)/2:.0f}" y="{H-6}" class="tick" text-anchor="middle">n (Gitterseite)</text>')
    out.append(f'<text x="14" y="{(T+H-B)/2:.0f}" class="tick" text-anchor="middle" transform="rotate(-90 14 {(T+H-B)/2:.0f})">{ylab}</text>')
    return '\n'.join(out)

# chart 1: side vs n, single series, reference line 0.4n
lo1, hi1 = 0, math.ceil(max(ys)/50)*50
c1 = [axis(lo1, hi1, 50, lambda v: f'{v:.0f}', 'Seite des 2er-Quadrats')]
c1.append(f'<line x1="{sx(0):.1f}" y1="{sy(0,lo1,hi1):.1f}" x2="{sx(max(xs)):.1f}" y2="{sy(0.4*max(xs),lo1,hi1):.1f}" class="ref"/>')
c1.append(f'<text x="{sx(max(xs))-4:.1f}" y="{sy(0.4*max(xs),lo1,hi1)+14:.1f}" class="lbl" text-anchor="end">0,4·n</text>')
for n, s in pts:
    c1.append(f'<circle cx="{sx(n):.1f}" cy="{sy(s,lo1,hi1):.1f}" r="2.5" class="s1"><title>n={n}, Seite={s}</title></circle>')

# chart 2: residual side - 0.4n, two series (even/odd), legend + direct labels
res = [(n, s - 0.4*n, n % 2) for n, s in pts]
lo2, hi2 = 0, math.ceil(max(r for _, r, _ in res))
c2 = [axis(lo2, hi2, 1, lambda v: f'{v:.0f}', 'Seite − 0,4·n')]
for n, r, par in res:
    c2.append(f'<circle cx="{sx(n):.1f}" cy="{sy(r,lo2,hi2):.1f}" r="2.5" class="s{par+1}"><title>n={n}, Rest={r:.1f}</title></circle>')
# direct labels near the last point of each parity
for par, name in ((0, 'gerade n'), (1, 'ungerade n')):
    last = [p for p in res if p[2] == par][-1]
    c2.append(f'<text x="{sx(last[0])+6:.1f}" y="{sy(last[1],lo2,hi2)+4:.1f}" class="lbl s{par+1}t">{name}</text>')

page = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sandpile Zentralquadrat</title>
<style>
:root{{--surface:#fcfcfb;--text:#0b0b0b;--text2:#52514e;--grid:#e6e5e1;--s1:#2a78d6;--s2:#eb6834}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--surface:#1a1a19;--text:#fff;--text2:#c3c2b7;--grid:#2e2e2c;--s1:#3987e5;--s2:#d95926}}}}
:root[data-theme="dark"]{{--surface:#1a1a19;--text:#fff;--text2:#c3c2b7;--grid:#2e2e2c;--s1:#3987e5;--s2:#d95926}}
body{{margin:0;padding:16px;background:var(--surface);color:var(--text);font:14px/1.4 system-ui,sans-serif;max-width:760px}}
h1{{font-size:18px;margin:0 0 4px}} h2{{font-size:15px;margin:20px 0 4px}} p{{color:var(--text2);margin:0 0 8px}}
svg{{width:100%;height:auto;display:block}}
.grid{{stroke:var(--grid);stroke-width:1}} .tick,.lbl{{fill:var(--text2);font-size:11px}} .lbl{{font-size:12px}}
.ref{{stroke:var(--text2);stroke-width:1.5;stroke-dasharray:4 3}}
.s1{{fill:var(--s1)}} .s2{{fill:var(--s2)}} .s1t,.s2t{{fill:var(--text)}}
.legend{{display:flex;gap:16px;color:var(--text2);font-size:12px;margin:4px 0}} .sw{{display:inline-block;width:10px;height:10px;border-radius:5px;margin-right:6px;vertical-align:-1px}}
table{{border-collapse:collapse;font-size:12px;margin-top:8px}} td,th{{padding:2px 8px;text-align:right;border-bottom:1px solid var(--grid)}}
details summary{{cursor:pointer;color:var(--text2)}}
</style></head><body>
<h1>Zentrales 2er-Quadrat der Sandhaufen-Identität</h1>
<p>{N} Gittergrößen n = {min(xs)} … {max(xs)}. Lineare Anpassung: Seite ≈ {a:.4f}·n + {c:.2f}.</p>
<h2>Seite gegen n</h2>
<svg viewBox="0 0 {W} {H}" role="img" aria-label="Seite des Zentralquadrats gegen n">{''.join(c1)}</svg>
<h2>Rest gegenüber 0,4·n</h2>
<div class="legend"><span><i class="sw" style="background:var(--s1)"></i>gerade n</span><span><i class="sw" style="background:var(--s2)"></i>ungerade n</span></div>
<svg viewBox="0 0 {W} {H}" role="img" aria-label="Rest Seite minus 0,4 n gegen n">{''.join(c2)}</svg>
<details><summary>Tabelle ({N} Zeilen)</summary><table><tr><th>n</th><th>Seite</th><th>Seite − 0,4·n</th></tr>
{''.join(f"<tr><td>{n}</td><td>{s}</td><td>{s-0.4*n:.1f}</td></tr>" for n,s in pts)}
</table></details>
</body></html>'''
open('sweep.html', 'w').write(page)
print(f'N={N} n∈[{min(xs)},{max(xs)}] fit side = {a:.4f}n + {c:.2f}; wrote sweep.html')
