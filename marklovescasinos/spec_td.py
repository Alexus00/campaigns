import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
S = "topdollar"
P = [dict(src=S, a=183.85, b=188.95, x=960, zoom_at=184.0, zoom_len=1.0),       # hook: "that's 30... try again... I need your help"
     dict(src=S, a=23.7, b=25.55, x=960, flash=True),                            # "we burnt $500"
     dict(src=S, a=27.6, b=29.95, x=960),                                        # "positive vibes"
     dict(src=S, a=117.9, b=122.4, x=960),                                       # "this might be our last spin"
     dict(src=S, a=133.6, b=135.75, x=960),                                      # "manifesting a top dollar"
     dict(src=S, a=178.0, b=179.8, x=960, flash=True),                           # "we just hit a bonus"
     dict(src=S, a=207.1, b=209.95, x=960),                                      # "first ever top dollar"
     dict(src=S, a=202.4, b=204.4, x=960, va=196.0),                             # "30 again, try again"
     dict(src=S, a=228.6, b=230.95, x=960, zoom_at=229.0, zoom_len=1.2),         # "that's a 35"
     dict(src=S, a=237.75, b=238.95, x=960),                                     # "try again"
     dict(src=S, a=254.4, b=256.7, x=960),                                       # "what would 35 have been?"
     dict(src=S, a=262.1, b=266.8, x=960, zoom_at=265.0, zoom_len=1.6),          # "650 bucks... are you f*cking me?"
     dict(src=S, a=282.0, b=284.0, x=960, flash=True),                           # "$300 win"
     dict(src=S, a=285.3, b=286.95, x=960)]                                      # "it won nonetheless"
SPEC = dict(out="mlc_top_dollar", credit="",
    hook_lines=["$1,000 IN TOP DOLLAR...", "TAKE IT OR TRY AGAIN?"],
    highlight=["30.", "again.", "$500", "last", "spin,", "bonus", "first", "35", "35.", "650", "$300", "won"],
    fix={"went": "WON"}, drop=["we", "have", "now"] and [], parts=P)
t, T = 0.0, []
for p in P: T.append(t); t += p["b"] - p["a"]
END = t
YEL, RED, GRN, WHT = "&H0000E5FF&", "&H003030FF&", "&H0050E650&", "&H00FFFFFF&"
def lab(st, en, y, txt, col=WHT, fs=56):
    return (st, en, "Hook", f"{{\\\\pos(540,{y})\\\\c{col}\\\\fs{fs}\\\\fscx140\\\\fscy140\\\\t(0,180,\\\\fscx100\\\\fscy100)}}{txt}", 7)
off = lambda i, s: T[i] + s
SPEC["extra"] = [lab(off(0, 0.55), T[1], 380, "OFFER: 30 CREDITS", YEL, 60), lab(off(0, 1.7), T[1], 460, "TRY AGAIN?", WHT, 54),
                 lab(T[1], T[5], 380, "DOWN $500", RED, 64),
                 lab(off(5, 0.1), END, 380, "TOP DOLLAR HIT", GRN, 60),
                 lab(T[7], END, 460, "OFFER 1-3: 30 · 30 · 30", WHT, 44), lab(T[8] + 0.5, END, 530, "OFFER 4: 35", YEL, 52),
                 lab(T[9], END, 610, "TRY AGAIN...", RED, 52), lab(T[12] + 0.3, END, 700, "FINAL: $300", GRN, 72)]
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 2, 4.5, 6, 8.5, 12, 14.5, 17, 20, 23, 26, 29, 32, tot - 0.4], "work/td_prev.jpg")
