import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
# TEST A — GAMBLE DECISION / STAKES FIRST. Source: vegas_928 11330 s -> end (src/lastspin.mp4, t = source - 11330).
# Last slot of the night: he states the stakes himself ("if we lose ... a $2,500 loss"), first-ever old-school pinball,
# "last shot", then "we put in 1700, taking out 2400, we are UP on the day" + cash-out voucher. Own audio everywhere.
S = "lastspin"
P = [
    dict(src=S, a=88.35, b=90.25, x=960, zoom_at=89.4, zoom_len=0.85),       # face: "if we lose this"
    dict(src=S, a=93.60, b=95.10, x=960),                                    # face: "a $2,500 loss"
    dict(src=S, a=84.25, b=88.30, x=960),                                    # face: "we win this guys, we will be significantly up on the night"
    dict(src=S, a=41.60, b=44.05, x=960, flash=True),                        # "I've always wanted to hit an old-school pinball"
    dict(src=S, a=188.45, b=189.95, x=960, zoom_at=188.9, zoom_len=1.0),     # "I've never gotten this in my life"
    dict(src=S, a=247.05, b=250.35, x=960),                                  # pinball screen: "one more shot, last shot. make it worth it"
    dict(src=S, a=252.75, b=255.85, x=960, flash=True),                      # "25! okay okay wait, how much of a win is this?"
    dict(src=S, a=272.95, b=279.00, x=960, zoom_at=276.3, zoom_len=2.0),     # voucher + "put in 1700, taking out 2400, UP on the day"
]
SPEC = dict(out="mlc_last_slot_of_the_night", credit="", progress=True,
    hook_lines=["LAST SLOT OF THE NIGHT...", "WIN = UP, LOSE = -$2,500"],
    highlight=["lose", "$2,500", "win", "up", "pinball", "life", "last", "shot.", "25,", "$1,700", "$2,400", "day"],
    fix={"2500": "$2,500", "1700": "$1,700", "2400": "$2,400"}, drop=["hour", "we", "guys"] and ["hour"], parts=P)

t, T = 0.0, []
for p in P: T.append(t); t += round((p["b"] - p["a"]) * 30) / 30
END = t
YEL, GRN, WHT, RED = "&H0000E5FF&", "&H0050E650&", "&H00FFFFFF&", "&H003030FF&"
def lab(st, en, x, y, txt, col=WHT, fs=56, pop=True, layer=7):
    anim = "\\fscx140\\fscy140\\t(0,180,\\fscx100\\fscy100)" if pop else ""
    return (st, en, "Hook", f"{{\\pos({x},{y})\\c{col}\\fs{fs}{anim}}}{txt}", layer)
R = T[7] + 0.15
SPEC["extra"] = [
    lab(T[5], T[7], 540, 470, "LAST SHOT", YEL, 80),
    lab(R, END, 540, 430, "IN: $1,700", WHT, 72),
    lab(R + 1.3, END, 540, 520, "CASHOUT: $2,446", GRN, 84),   # exact amount printed on the voucher
]
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.0, 1.5, 3.0, 5.5, 8.0, 10.5, 13.0, 15.5, 17.5, 19.0, 21.0, tot - 0.3], "work/lastslot_prev.jpg")
