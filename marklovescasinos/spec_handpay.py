import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
# Source: vegas_928 (IRL VEGAS 9:28, Drive copy) 850 s -> 1250 s  => src/handpay.mp4 (t = source - 850)
# Format: reaction first, win revealed last. Amount hidden until R1.
S = "handpay"
FACE = dict(x=1180, y=430, h=640)          # tight on Mark, keeps jackpot meters on the left out of frame
P = [
    # HOOK (no screen visible)
    dict(src=S, a=187.40, b=188.70, va=203.6, **FACE, zoom_at=187.6, zoom_len=1.0, caps=[(0.0, 1.3, "HOLY!")]),        # "HOLY!"
    dict(src=S, a=195.50, b=197.80, va=204.9, **FACE),                                       # "first hand pay since February"
    # BUILD-UP (chronological)
    dict(src=S, a=14.30, b=16.05, va=33.0, x=960, flash=True),                                       # "can I do a $30 spin?"
    dict(src=S, a=30.05, b=31.95, va=37.75, x=960, flash=True,
         caps=[(0.0, 0.7, "OH MY GOD!"), (0.7, 1.9, "Y'ALL!")]),                              # 6 FREE GAMES
    dict(src=S, a=69.70, b=71.20, x=960),                                                    # "hats hats hats"
    dict(src=S, a=86.00, b=87.40, x=960, zoom_at=86.1, zoom_len=0.9),                       # "free trigger, baby"
    dict(src=S, a=97.80, b=100.05, x=960),                                                   # "forgetting this is a $30 spin"
    dict(src=S, a=139.45, b=143.65, va=143.5, x=960),                                        # "what's a grand? 75,000..."
    dict(src=S, a=168.35, b=169.30, va=163.5, x=760, y=370, h=740),                         # board fills (totals cropped out)
    dict(src=S, a=175.10, b=178.30, x=960, dim=True),                                        # "a thousand f*cking dollars" (screen blurred)
    dict(src=S, a=186.35, b=187.40, va=193.6, x=1000),                                       # "wait, how much is this?" (face)
    # REVEAL
    dict(src=S, a=187.40, b=188.75, va=187.0, x=1380, freeze=True, flash=True, caps=[(0.0, 1.35, "HOLY!")]),              # WIN $2,555.50 on screen
    dict(src=S, a=389.60, b=393.00, va=216.4, x=1100, zoom_at=217.6, zoom_len=2.2),          # attendant: Jackpot Handpay $2,555.50
    dict(src=S, a=395.15, b=396.90, va=212.0, x=1000),                                       # "I will take that all day long, baby"
]
SPEC = dict(out="mlc_handpay_reveal", credit="", progress=True,
    hook_lines=["HIS REACTION WHEN", "THE SLOT PAID OUT..."],
    highlight=["holy!", "hand", "pay", "february,", "$30", "grand?", "75,000.", "trigger,", "thousand", "$2,550", "win.", "long,", "hats"],
    fix={"thirty": "30"}, parts=P)

t, T = 0.0, []
for p in P: T.append(t); t += (p["b"] - p["a"])
END = t
YEL, GRN, WHT, RED = "&H0000E5FF&", "&H0050E650&", "&H00FFFFFF&", "&H003030FF&"
def lab(st, en, x, y, txt, col=WHT, fs=56, pop=True, layer=7):
    anim = "\\fscx140\\fscy140\\t(0,180,\\fscx100\\fscy100)" if pop else ""
    return (st, en, "Hook", f"{{\\pos({x},{y})\\c{col}\\fs{fs}{anim}}}{txt}", layer)
R1 = T[11]
SPEC["extra"] = [
    lab(0.0, R1, 820, 370, "WIN: ???", YEL, 52, pop=False),                 # small hidden badge (whole build-up)
    lab(T[2] + 0.4, R1, 250, 370, "BET: $30", WHT, 52),                       # bet badge from his own line
    lab(T[9], T[10], 540, 760, "WIN: ???", YEL, 120),                          # big teaser over blurred screen
    lab(R1, END, 540, 400, "WIN: $2,555.50", GRN, 96),                        # reveal = number on the machine
]
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 1.5, 3.0, 4.6, 6.6, 8.6, 10.2, 12.4, 15.5, 17.6, 19.5, 22.4, 23.5, 25.5, tot - 0.4], "work/handpay_prev.jpg")
