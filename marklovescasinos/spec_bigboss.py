import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
# Source: vegas_928 (IRL VEGAS 9:28, Drive copy) 1860 s -> 2110 s => src/bigboss.mp4 (t = source - 1860)
# Format: RESULT FIRST (like mlc_jordan_double, our best: skip 34%) -> exact $ in frame 1, then the story, ~21 s.
# Lip-sync rule: every part uses its OWN audio (no va/vsrc).
# Avoid: 174-176 (Spooky Link $40,022 GRAND meter on the next machine).
S = "bigboss"
P = [
    dict(src=S, a=187.45, b=189.15, x=1100, zoom_at=187.9, zoom_len=1.2, caps=[(0.0, 1.7, "AN $875")]),               # screen: WIN $875.00 / "an $875 one"
    dict(src=S, a=201.05, b=201.50, x=960, zoom_at=201.05, zoom_len=0.45),              # face: "HOLY,"
    dict(src=S, a=202.30, b=205.20, x=960),                                             # face: "what the f*ck? this luck is unreal"
    dict(src=S, a=42.90, b=44.50, x=960, flash=True),                                   # "okay, 12.50 is spent"
    dict(src=S, a=57.90, b=59.60, x=960),                                               # "unleash the beast"
    dict(src=S, a=60.25, b=63.00, x=960, zoom_at=60.4, zoom_len=1.2),                   # face: "we just did a m*therf*cking bonus, baby"
    dict(src=S, a=84.15, b=85.95, x=960, flash=True),                                   # screen: YOU'VE WON MO'SYMBOLS
    dict(src=S, a=126.70, b=128.55, x=960),                                             # screen: 1 SPIN LEFT "diamond x6"
    dict(src=S, a=129.85, b=132.15, x=960),                                             # face: "now we're sweating it on the last spin"
    dict(src=S, a=177.75, b=178.95, x=960),                                             # face: "how much is all this?" -> loops to frame 1
]
SPEC = dict(out="mlc_big_boss_875", credit="", progress=True,
    hook_lines=["$12.50 A SPIN...", "THEN THE BONUS PAID THIS"],
    highlight=["$875", "holy,", "unreal,", "unreal.", "1250", "beast", "bonus,", "symbols,", "symbols.", "last", "spin.", "this?"],
    fix={"1250": "$12.50", "motherfucking": "M*THERF*CKING"}, parts=P)

t, T = 0.0, []
for p in P: T.append(t); t += round((p["b"] - p["a"]) * 30) / 30
END = t
YEL, GRN, WHT = "&H0000E5FF&", "&H0050E650&", "&H00FFFFFF&"
def lab(st, en, x, y, txt, col=WHT, fs=56, pop=True, layer=7):
    anim = "\\fscx140\\fscy140\\t(0,180,\\fscx100\\fscy100)" if pop else ""
    return (st, en, "Hook", f"{{\\pos({x},{y})\\c{col}\\fs{fs}{anim}}}{txt}", layer)
SPEC["extra"] = [
    lab(0.0, T[3], 540, 480, "WIN: $875", GRN, 104),                  # result first, from the machine screen
    lab(T[3], END, 820, 370, "WIN: $875", GRN, 52, pop=False),         # stays small during the story
    lab(0.0, END, 250, 370, "BET: $12.50", WHT, 52, pop=False),
    lab(T[8], T[9], 540, 470, "LAST SPIN", YEL, 72),   # only on his face (screen already says 1 SPIN LEFT)
]
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.0, 1.0, 2.2, 3.5, 5.0, 6.5, 8.0, 9.5, 11.0, 13.0, 15.0, 17.0, 19.0, tot - 0.3], "work/bigboss_prev.jpg")
