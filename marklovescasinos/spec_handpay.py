import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
# Source: vegas_928 (IRL VEGAS 9:28, Drive copy) 850 s -> 1250 s  => src/handpay.mp4 (t = source - 850)
# Format: reaction first, win revealed last. Amount hidden until R1.
S = "handpay"
FACE = dict(x=1180, y=430, h=640)          # tight on Mark, keeps jackpot meters on the left out of frame
P = [   # every shot with Mark's face uses its OWN audio (lip sync); only screen/no-face shots may differ
    # HOOK (no screen visible)
    dict(src=S, a=203.25, b=205.75, **FACE, zoom_at=204.6, zoom_len=1.0,
         caps=[(0.0, 0.16, 'CAN'), (0.16, 0.26, 'YOU'), (0.26, 0.5, 'TEXT'), (0.5, 0.68, 'MY'), (0.68, 0.9, 'DAD'), (0.9, 1.12, 'FOR'), (1.12, 1.26, 'ME'), (1.26, 1.38, 'THAT'), (1.38, 1.5, 'I'), (1.5, 1.6, 'HIT'), (1.6, 1.74, 'A'), (1.74, 1.96, 'HAND'), (1.96, 2.1, 'PAY'), (2.1, 2.44, 'FINALLY?')]),   # word times from words/handpay.json, first pinned to 0.0
    dict(src=S, a=195.50, b=197.85, x=1000),                                                 # arms up: "first hand pay since February"
    # BUILD-UP (chronological)
    dict(src=S, a=14.30, b=16.05, x=1000, flash=True),                                       # "can I do a $30 spin?"
    dict(src=S, a=30.05, b=31.95, x=960, flash=True,
         caps=[(0.0, 0.7, "OH MY GOD!"), (0.7, 1.9, "Y'ALL!")]),                              # 6 FREE GAMES banner
    dict(src=S, a=69.70, b=71.20, x=960),                                                    # "hats hats hats"
    dict(src=S, a=86.00, b=87.40, x=960, zoom_at=86.1, zoom_len=0.9),                       # "free trigger, baby"
    dict(src=S, a=97.80, b=100.05, x=960),                                                   # "forgetting this is a $30 spin"
    dict(src=S, a=142.25, b=143.55, x=960, dim=True),                                        # "if we get the grand" (screen shows MINOR $2,500 meter -> blurred)
    dict(src=S, a=143.55, b=145.20, x=960, y=480, h=960),                                    # face: "what do we do if we get the grand?"
    dict(src=S, a=168.35, b=169.30, x=760, y=370, h=740),                                    # board fills (totals cropped out)
    dict(src=S, a=175.10, b=178.30, x=960, dim=True),                                        # "a thousand f*cking dollars" (screen blurred)
    # REVEAL
    dict(src=S, a=186.35, b=187.90, x=1380, flash=True, zoom_at=187.0, zoom_len=0.9),        # "how much is this? HOLY!" -> WIN $2,555.50
    dict(src=S, a=187.90, b=188.75, x=700, h=900),                                           # his face, end of "HOLY!"
    dict(src=S, a=389.60, b=393.00, x=960),                                                  # "a $2,550 f*cking win"
    dict(src=S, a=395.15, b=396.90, x=960),                                                  # "I will take that all day long, baby"
]
SPEC = dict(out="mlc_handpay_reveal", credit="", progress=True,
    hook_lines=["HIS REACTION WHEN", "THE SLOT PAID OUT..."],
    highlight=["holy!", "hand", "pay", "february,", "$30", "grand?", "75,000.", "trigger,", "thousand", "$2,550", "win.", "long,", "hats"],
    fix={"thirty": "30"}, drop=["morts,", "morts"], parts=P)

t, T = 0.0, []
for p in P: T.append(t); t += round((p["b"] - p["a"]) * 30) / 30
END = t
YEL, GRN, WHT, RED = "&H0000E5FF&", "&H0050E650&", "&H00FFFFFF&", "&H003030FF&"
def lab(st, en, x, y, txt, col=WHT, fs=56, pop=True, layer=7):
    anim = "\\fscx140\\fscy140\\t(0,180,\\fscx100\\fscy100)" if pop else ""
    return (st, en, "Hook", f"{{\\pos({x},{y})\\c{col}\\fs{fs}{anim}}}{txt}", layer)
R1 = T[11] + 0.45
SPEC["extra"] = [
    lab(0.0, R1, 820, 370, "WIN: ???", YEL, 52, pop=False),                 # small hidden badge (whole build-up)
    lab(T[2] + 0.4, R1, 250, 370, "BET: $30", WHT, 52),                       # bet badge from his own line
    lab(T[10], T[11], 540, 760, "WIN: ???", YEL, 120),                          # big teaser over blurred screen
    lab(R1, END, 540, 400, "WIN: $2,555.50", GRN, 96),                        # reveal = number on the machine
]
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 1.5, 3.0, 4.6, 6.6, 8.6, 10.2, 12.4, 15.5, 17.6, 19.5, 22.4, 23.5, 25.5, tot - 0.4], "work/handpay_prev.jpg")
