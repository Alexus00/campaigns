import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
S = "profit"
SPEC = dict(out="mlc_fan_inspired", credit="",
    hook_lines=["HE SPOTTED MARK'S STREAM", "IN VEGAS AND SAID THIS..."],
    highlight=["inspired", "stream", "everyone", "family", "world", "noticed", "goat.", "love", "luca's"],
    drop=["like", "like,"],
    parts=[dict(src=S, a=177.25, b=179.45, x=960),
           dict(src=S, a=214.2, b=216.35, x=960, flash=True),
           dict(src=S, a=217.5, b=218.45, x=960),
           dict(src=S, a=167.4, b=171.65, x=960),
           dict(src=S, a=173.55, b=177.0, x=960),
           dict(src=S, a=181.2, b=183.05, x=960),
           dict(src=S, a=192.8, b=195.55, x=960, zoom_at=193.4, zoom_len=2.0),
           dict(src=S, a=260.55, b=264.35, x=960, flash=True),
           dict(src=S, a=288.1, b=300.1, x=960, va=260.8)])
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 1.5, 3, 5, 8, 11, 14, 17, 20, 24, 28, tot - 0.4], "work/luca_prev.jpg")
