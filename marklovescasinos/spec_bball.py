import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
S = "bball"
SPEC = dict(out="mlc_37_points", credit="",
    hook_lines=["HIS GOAL: 37 POINTS", "ON FREMONT STREET..."],
    highlight=["37", "45?", "cooking", "35.", "good", "form?", "shot."],
    drop=["milking", "over", "-under"],
    parts=[dict(src=S, a=44.4, b=52.1, x=900, va=66.0),
           dict(src=S, a=53.0, b=60.0, x=900, flash=True),
           dict(src=S, a=62.2, b=64.0, x=900),
           dict(src=S, a=72.55, b=73.3, x=900, zoom_at=72.6, zoom_len=0.7),
           dict(src=S, a=80.0, b=86.0, x=900),
           dict(src=S, a=93.6, b=97.4, x=900),
           dict(src=S, a=102.5, b=108.0, x=900),
           dict(src=S, a=110.3, b=117.0, x=880, va=113.2, flash=True),
           dict(src=S, a=126.8, b=128.3, x=900)])
YEL, RED, WHT = "&H0000E5FF&", "&H003030FF&", "&H00FFFFFF&"
def lab(t, en, y, txt, col=WHT, fs=64):
    return (t, en, "Hook", f"{{\\\\pos(540,{y})\\\\c{col}\\\\fs{fs}\\\\fscx140\\\\fscy140\\\\t(0,180,\\\\fscx100\\\\fscy100)}}{txt}", 7)
SPEC["extra"] = [lab(0.0, 33.2, 380, "GOAL: 37", YEL, 70), lab(33.2, 40.75, 380, "SCORE: 35", RED, 90), lab(33.4, 40.75, 470, "(GOAL: 37)", WHT, 44)]
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 3, 8, 12, 15.5, 19, 24, 28, 31, 33.5, 36, tot - 0.4], "work/bball_prev.jpg")
