import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
S = "craps"
SPEC = dict(out="mlc_craps_hit_and_run", credit="",
    hook_lines=["HE PUT $1,100 IN", "A CRAPS MACHINE..."],
    highlight=["niner!", "lot", "$1,100", "five", "ace,", "run", "out", "me?", "happy", "result", "500"],
    drop=["motherfucking"],
    parts=[dict(src=S, a=165.3, b=169.05, x=960, zoom_at=165.4, zoom_len=1.2),
           dict(src=S, a=116.2, b=122.95, x=960, fix={"1100": "$1,100"}),
           dict(src=S, a=161.6, b=172.6, x=960, flash=True),
           dict(src=S, a=175.2, b=178.45, x=960),
           dict(src=S, a=188.25, b=194.65, x=960, zoom_at=189.2, zoom_len=1.4),
           dict(src=S, a=196.95, b=198.4, x=960),
           dict(src=S, a=219.4, b=221.9, x=960),
           dict(src=S, a=260.4, b=265.65, x=960),
           dict(src=S, a=270.6, b=274.4, x=960, drop=["400", "no"])])
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 1.5, 3, 6, 9, 13, 17, 21, 25, 29, 33, 37, tot - 0.4], "work/craps_prev.jpg")
