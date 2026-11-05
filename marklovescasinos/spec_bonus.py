import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
S = "bonus"
SPEC = dict(out="mlc_bonus_in_bonus", credit="",
    hook_lines=["A BONUS INSIDE A BONUS", "ON A $25 SPIN..."],
    highlight=["bonus,", "bonus!", "million", "nothing.", "mini.", "grand", "going.", "bonus.", "$1,775"],
    drop=["motherfucking", "y", "'all"],
    parts=[dict(src=S, a=102.1, b=106.6, x=960, va=192.0, zoom_at=104.0, zoom_len=1.2),
           dict(src=S, a=93.3, b=97.2, x=960),
           dict(src=S, a=156.8, b=167.6, x=960, zoom_at=163.3, zoom_len=1.5),
           dict(src=S, a=185.7, b=191.0, x=960),
           dict(src=S, a=241.3, b=247.9, x=960, flash=True),
           dict(src=S, a=268.9, b=274.6, x=1150, zoom_at=271.3, zoom_len=3.0,
                fix={"one": "$1,775"}, drop=["thousand", "seven", "hundred", "seventy", "five", "dollar"])])
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 2.5, 5, 8, 12, 16, 21, 25, 29, 33, tot - 0.4], "work/bonus_prev.jpg")
