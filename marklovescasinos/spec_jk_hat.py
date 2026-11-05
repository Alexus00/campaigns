import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
# YOUTUBE (IRL Nashville, no gambling). Dropbox IRL "2026-10-30 - CRAZY JOKER - NASHVILLE HALLOWEEKEND.mp4" 6130 s -> src/jk_hat.mp4.
# Mark dressed as the Joker in a Nashville boot/hat store: $1,000 hat, can't try it on (green hair), buys a $90 one. Own audio everywhere.
S = "jk_hat"
P = [
    dict(src=S, a=40.40, b=42.30, x=960, zoom_at=40.5, zoom_len=1.8),        # seller: "this one's actually a $1,000 hat right here"
    dict(src=S, a=43.10, b=45.20, x=960),                                    # "is it a $1,000 hat?"
    dict(src=S, a=46.25, b=50.35, x=960, flash=True),                        # "can I try it on?" "no, not with the green hair" "not with the green hair, okay"
    dict(src=S, a=67.25, b=71.05, x=960),                                    # "I gotta see if y'all are vibing with me buying a $1,000 hat"
    dict(src=S, a=162.20, b=165.95, x=960),                                  # "I'm not buying a thousand dollar, I'm copping it for 3 to 400"
    dict(src=S, a=222.50, b=223.90, x=960, flash=True),                      # "how much is this one?"
    dict(src=S, a=226.85, b=228.05, x=960),                                  # "no, this is 90, my bad"
    dict(src=S, a=229.45, b=231.85, x=960, zoom_at=230.9, zoom_len=0.9),     # "90 dollars? F*CK YEAH"
    dict(src=S, a=259.95, b=262.45, x=960),                                  # "now I bought it. I'm a cowboy now."
]
SPEC = dict(out="yt_joker_1000_hat", credit="", progress=True,
    hook_lines=["HE WALKED IN AS THE JOKER...", "THE HAT WAS $1,000"],
    highlight=["$1,000", "green", "hair", "thousand", "90", "cowboy"],
    fix={"three": "300", "y": "Y'ALL"}, drop=["'all"], parts=P)
t, T = 0.0, []
for p in P: T.append(t); t += round((p["b"] - p["a"]) * 30) / 30
END = t
YEL, GRN, WHT, RED = "&H0000E5FF&", "&H0050E650&", "&H00FFFFFF&", "&H003030FF&"
def lab(st, en, x, y, txt, col=WHT, fs=56, layer=7):
    return (st, en, "Hook", f"{{\\pos({x},{y})\\c{col}\\fs{fs}\\fscx140\\fscy140\\t(0,180,\\fscx100\\fscy100)}}{txt}", layer)
SPEC["extra"] = [lab(0.0, T[6], 540, 420, "PRICE: $1,000", RED, 80), lab(T[6], END, 540, 420, "PRICE: $90", GRN, 80)]
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.0, 2.0, 4.0, 6.0, 8.5, 11.0, 14.0, 16.5, 18.5, 20.0, tot - 0.3], "work/jk_hat_prev.jpg")
