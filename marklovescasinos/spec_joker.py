import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
S = "jk_origin"
SPEC = dict(out="mlc_joker_origin", credit="",
    hook_lines=["HE DRESSED UP AS THE JOKER", "AND TOLD HIS ORIGIN STORY..."],
    highlight=["smiles,", "joker.", "batman.", "batman?", "brother", "sports.", "frown.", "improved", "better", "smile."],
    parts=[dict(src=S, a=35.5, b=38.95, x=960, vsrc="jk_street", va=2.2),
           dict(src="jk_street", a=6.85, b=11.75, x=960),
           dict(src=S, a=12.6, b=17.35, x=1000, flash=True),
           dict(src=S, a=23.7, b=30.95, x=1000),
           dict(src=S, a=39.3, b=45.1, x=1080),
           dict(src=S, a=49.1, b=62.55, x=1080),
           dict(src=S, a=62.7, b=69.6, x=1080, zoom_at=65.6, zoom_len=3.6)])
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 2, 5, 9, 13, 17, 21, 25, 29, 32, 36, tot - 0.4], "work/joker_prev.jpg")
