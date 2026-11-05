import sys
from irlgen import build, preview
SPECS = {
 "nms": dict(out="jason_nms_boxing_chaos", credit="JASONTHEWEEN · NMS BOXING 5",
    hook_lines=["NMS BOXING 5", "WAS PURE CHAOS"],
    highlight=["jason!", "jason", "dumbest", "stop", "god!", "ground?", "scripting"],
    parts=[
        dict(src="b03", a=5.9, b=6.95, x=960, h=960, label="JASONTHEWEEN · NMS BOXING 5"),
        dict(src="b06", a=3.4, b=9.2, x=960, h=960, label="#5 THE TKO", zoom_at=6.3, zoom_len=1.2),
        dict(src="b04", a=1.0, b=6.4, x=960, h=960, label="#4 SCRIPTED??", drop=["let's", "just", "watch", "i", "didn't", "see", "look", "for"]),
        dict(src="b01", a=0.0, b=7.2, x=960, h=960, label="#3 NINJA"),
        dict(src="b02", a=0.0, b=9.9, x=960, h=960, label="#2 AURA", zoom_at=5.3, zoom_len=1.4),
        dict(src="b03", a=0.0, b=11.7, x=960, h=960, label="#1 HOW DID HE FALL?!", drop=["just", "said."]),
    ]),
 "viral": dict(out="jason_most_viral_ranked", credit="JASONTHEWEEN",
    hook_lines=["JASONTHEWEEN'S", "MOST VIRAL MOMENTS"],
    highlight=["aura", "world", "magazine", "exploded", "evacuate", "court", "sorry!", "god"],
    parts=[
        dict(src="a01", a=4.0, b=5.2, x=960, label="JASONTHEWEEN"),
        dict(src="a02", a=0.0, b=7.4, x=960, label="#5 EYES ON THE BALL", caps=[(5.9, 6.9, "I'M SORRY!")]),
        dict(src="a08", a=0.0, b=9.6, x=960, label="#4 EVACUATE THE COURT"),
        dict(src="a04", a=12.8, b=20.5, x=960, label="#3 THE MAGAZINE EXPLODED", zoom_at=17.0, zoom_len=1.2, caps=[(2.1, 3.4, "THE"), (3.4, 4.9, "MAGAZINE"), (4.9, 6.5, "EXPLODED")]),
        dict(src="a07", a=0.0, b=9.5, x=960, label="#2 100K SUBS", caps=[]),
        dict(src="a01", a=0.0, b=11.0, x=960, label="#1 INCREASE YOUR AURA", zoom_at=4.2, zoom_len=1.6),
    ]),
 "jutsu": dict(out="jason_fire_jutsu", credit="JASONTHEWEEN",
    hook_lines=["JASONTHEWEEN'S", "CARD TRICK..."],
    highlight=["focus,", "focus.", "whoa!", "card?", "f*ck"],
    parts=[
        dict(src="r06", a=0.0, b=11.79, x=960, h=940, zoom_at=6.0, zoom_len=1.5),
    ]),
}
if __name__ == "__main__":
    for k in sys.argv[1:]:
        out, tot = build(SPECS[k])
        preview(out, [0.2] + [round(tot * f, 2) for f in (0.15, 0.3, 0.45, 0.6, 0.75, 0.95)], f"work/{k}_prev.jpg")
