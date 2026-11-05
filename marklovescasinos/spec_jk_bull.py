import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
# YOUTUBE (IRL Nashville bar, mechanical bull, no gambling). Dropbox IRL "CRAZY JOKER" 4340 s -> src/jk_bull.mp4.
# Abigail SURFS the bull (standing) -> Mark (as the Joker): "why are you flexing on me" -> "I'm not ready" -> falls off. Own audio everywhere.
S = "jk_bull"
P = [
    dict(src=S, a=145.40, b=148.50, x=960, zoom_at=146.0, zoom_len=1.5, caps=[(0.0, 2.45, "HOLY..."), (2.45, 3.1, "F*CK")]),     # Abigail surfing: "HOLY F*CK"
    dict(src=S, a=148.90, b=151.75, x=960),                                  # "why is she showing me up like that"
    dict(src=S, a=167.00, b=171.00, x=960, flash=True),                      # "Abigail, why are you flexing on me like that"
    dict(src=S, a=236.75, b=239.20, x=960),                                  # "and you're gonna make me seem like a fool"
    dict(src=S, a=364.85, b=369.05, x=960, flash=True),                      # on the bull: "oh god, I'm so nervous... I'm not ready"
    dict(src=S, a=418.10, b=423.10, x=960),                                  # "oh my god, what the f*ck is that?"
    dict(src=S, a=432.90, b=434.30, x=960, caps=[(0.0, 1.4, "...")]),        # the bull bucks
    dict(src=S, a=434.30, b=435.90, x=960, slow=1.6, zoom_at=434.6, zoom_len=1.2, caps=[(0.0, 2.56, "DOWN HE GOES")]),  # the fall (slow-mo)
]
SPEC = dict(out="yt_joker_bull", credit="", progress=True,
    hook_lines=["SHE RODE THE BULL...", "THEN THE JOKER TRIED"],
    highlight=["holy", "flexing", "fool", "nervous", "ready", "that"],
    fix={"bowl": "BULL"}, drop=["y", "'all"], parts=P)
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.0, 2.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 21.5, 23.0, tot - 0.2], "work/jk_bull_prev.jpg")
