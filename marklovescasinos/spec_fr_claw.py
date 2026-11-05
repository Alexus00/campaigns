import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
# YOUTUBE (IRL, arcade claw machine, no gambling). Dropbox IRL "2026-10-19 VEGAS FREMONT STREAM.mp4" 1165 s -> src/fr_claw.mp4.
# Payoff-first: "it did the exact same thing... that would have won it" then the story. Own audio everywhere (lip sync).
S = "fr_claw"
P = [   # hook = his face + claim; payoff = the near-miss. Own audio everywhere.
    dict(src=S, a=49.90, b=52.25, x=960, zoom_at=50.0, zoom_len=1.0,
         caps=[(0.0, 0.55, "LIKE, THESE ARE"), (0.55, 1.62, "RIGGED."), (1.62, 2.35, "THESE ARE RIGGED.")]),        # face: "like, these are rigged. these are rigged."
    dict(src=S, a=18.75, b=20.90, x=960, flash=True),                        # claw: "I really want to win some Pokemon cards"
    dict(src=S, a=46.45, b=49.85, x=960),                                    # face: "now that I own an arcade game, I know how these work"
    dict(src=S, a=52.35, b=53.95, x=960),                                    # face: "wait, no, I'm gonna win this one"
    dict(src=S, a=68.50, b=71.95, x=960, flash=True),                        # claw: "no, it's rigged. I did not release it"
    dict(src=S, a=94.90, b=99.70, x=960),                                    # "last try... it goes past the target"
    dict(src=S, a=101.25, b=104.05, x=960, zoom_at=102.5, zoom_len=1.5),     # claw: "it literally did the exact same f*cking thing"
    dict(src=S, a=109.20, b=111.60, x=960, flash=True),                      # face: "that would have won it. that would have won it"
]
SPEC = dict(out="yt_claw_rigged", credit="", progress=True,
    hook_lines=["HE OWNS AN ARCADE GAME...", "SO HE KNOWS THE TRICK?"],
    highlight=["exact", "same", "won", "pokemon", "cards", "rigged.", "last", "target."],
    fix={"pokemon": "POKÉMON"}, drop=["y", "'all", "-"], parts=P)
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.0, 1.5, 3.2, 5.0, 7.0, 9.5, 12.0, 14.5, 17.0, 19.5, tot - 0.3], "work/fr_claw_prev.jpg")
