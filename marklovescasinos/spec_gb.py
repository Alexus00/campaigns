import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
S = "gamblebonus"
SPEC = dict(out="mlc_black_or_red", credit="",
    hook_lines=["HE GAMBLED HIS BONUS...", "BLACK OR RED?"],
    highlight=["black", "red", "gamble", "$117", "doubled", "win.", "go."],
    drop=["motherfucking", "y", "'all"],
    parts=[dict(src=S, a=93.9, b=98.3, x=960, zoom_at=94.5, zoom_len=1.6),
           dict(src=S, a=66.7, b=69.4, x=960),
           dict(src=S, a=83.15, b=87.05, x=960, fix={"117": "$117"}),
           dict(src=S, a=103.2, b=111.0, x=960, va=88.6),
           dict(src=S, a=111.0, b=118.95, x=960),
           dict(src=S, a=124.35, b=125.75, x=960, va=120.6, flash=True),
           dict(src=S, a=141.0, b=146.95, x=960),
           dict(src=S, a=147.7, b=153.95, x=960, flash=True)])
YEL, WHT = "&H0000E5FF&", "&H00FFFFFF&"
def lab(t, y, txt, col=WHT, fs=54, end=26.85):
    return (t, end, "Hook", f"{{\\pos(540,{y})\\c{col}\\fs{fs}\\fscx140\\fscy140\\t(0,180,\\fscx100\\fscy100)}}{txt}", 7)
SPEC["extra"] = [lab(11.0, 380, "CHAT IS VOTING...", YEL, 50), lab(14.75, 460, "IFRIT: BLACK"), lab(16.0, 540, "SHEEN: BLACK"),
                 lab(21.0, 620, "HE PICKS...", YEL, 60)]
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 2, 4.5, 8, 11, 14, 18, 22, 25, 28, 31, 34, tot - 0.4], "work/gb_prev.jpg")
