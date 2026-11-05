import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
# TEST C — "suspense WITH context": same bonus as mlc_big_boss_875 (src/bigboss.mp4 = vegas_928 from 1860 s).
# Post EITHER this OR mlc_big_boss_875 on one_scroll_man, never both (same moment).
# Frame 1 = machine "1 SPIN LEFT" + bet $12.50 (context), amount hidden until the end. Own audio everywhere (lip sync).
S = "bigboss"
P = [
    dict(src=S, a=126.70, b=128.55, x=960, caps=[(0.0, 0.32, "DIAMOND,"), (0.32, 0.72, "DIAMOND,"), (0.72, 1.12, "DIAMOND,"), (1.12, 1.85, "DIAMOND!")]),  # screen: 1 SPIN LEFT
    dict(src=S, a=129.85, b=132.15, x=960),                                  # face: "now we're sweating it on the last spin"
    dict(src=S, a=135.90, b=137.10, x=960, zoom_at=136.0, zoom_len=1.0),     # screen: "what the f*ck?"
    dict(src=S, a=169.80, b=171.90, x=960),                                  # screen LAST SPIN: "we need two diamonds now?"
    dict(src=S, a=172.00, b=173.75, x=960, zoom_at=172.9, zoom_len=0.85),    # screen MINOR: "do it, do it. we got the minor"
    dict(src=S, a=187.45, b=189.15, x=1100, flash=True, zoom_at=187.9, zoom_len=1.2),  # REVEAL screen: WIN $875.00
    dict(src=S, a=201.05, b=201.50, x=960, zoom_at=201.05, zoom_len=0.45),   # face: "HOLY,"
    dict(src=S, a=202.30, b=205.20, x=960),                                  # face: "what the f*ck? this luck is unreal"
]
SPEC = dict(out="mlc_last_free_spin", credit="", progress=True,
    hook_lines=["HIS LAST FREE SPIN...", "HE NEEDS DIAMONDS"],
    highlight=["diamond,", "diamond!", "last", "spin.", "diamonds", "minor.", "miner.", "$875", "holy,", "unreal,"],
    fix={"miner": "MINOR!"}, drop=["man"], parts=P)

t, T = 0.0, []
for p in P: T.append(t); t += round((p["b"] - p["a"]) * 30) / 30
END = t
YEL, GRN, WHT = "&H0000E5FF&", "&H0050E650&", "&H00FFFFFF&"
def lab(st, en, x, y, txt, col=WHT, fs=56, pop=True, layer=7):
    anim = "\\fscx140\\fscy140\\t(0,180,\\fscx100\\fscy100)" if pop else ""
    return (st, en, "Hook", f"{{\\pos({x},{y})\\c{col}\\fs{fs}{anim}}}{txt}", layer)
R = T[5] + 0.3
SPEC["extra"] = [
    lab(0.0, END, 250, 370, "BET: $12.50", WHT, 52, pop=False),
    lab(0.0, R, 820, 370, "WIN: ???", YEL, 52, pop=False),
    lab(R, END, 540, 480, "WIN: $875", GRN, 104),
]
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.0, 1.0, 2.5, 4.3, 5.5, 7.0, 8.6, 9.6, 11.0, 12.5, 14.0, tot - 0.3], "work/lastfree_prev.jpg")
