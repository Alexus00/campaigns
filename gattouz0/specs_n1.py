import sys
from camgen import build, preview
UM = dict(top=(8, 58, 670, 447), bot=(8, 590, 670, 447))
SPECS = {
 "ronaldo": dict(out="gattouz_talks_like_ronaldo", credit="GATTOUZ0 ON KICK", progress=True, layout=UM,
    hook_lines=["A STRANGER TOLD GATTOUZ0", "HE TALKS LIKE RONALDO..."],
    highlight=["cristiano", "ronaldo", "real", "mannerisms", "wives."], drop=["is", "zippy", "but"],
    parts=[dict(src="n1_ronaldo", a=40.45, b=46.4, zoom="bot", zoom_at=44.0, zoom_len=2.0),
           dict(src="n1_ronaldo", a=55.5, b=58.9, zoom="top", zoom_at=56.5, zoom_len=2.0),
           dict(src="n1_ronaldo", a=61.0, b=69.8, zoom="bot", zoom_at=66.0, zoom_len=1.6)]),
 "date": dict(out="gattouz_first_date_pay", credit="GATTOUZ0 ON KICK", progress=True, layout=UM,
    hook_lines=["GATTOUZ0 ASKED STRANGERS:", "SHOULD THE MAN PAY?"],
    highlight=["pay", "first", "date.", "traditional", "polite,", "coffee", "cinema", "fancy", "investing"],
    drop=["per", "argument"], end_text="COMMENT YOUR ANSWER",
    parts=[dict(src="n1_date", a=35.0, b=41.4),
           dict(src="n1_date", a=41.4, b=43.0),
           dict(src="n1_date", a=49.0, b=51.1, zoom="top", zoom_at=49.2, zoom_len=1.8),
           dict(src="n1_date", a=55.6, b=61.1),
           dict(src="n1_date", a=74.2, b=83.1, zoom="bot", zoom_at=76.5, zoom_len=2.0),
           dict(src="n1_date", a=84.4, b=92.6)]),
 "court": dict(out="gattouz_100m_court", credit="GATTOUZ0 ON KICK", progress=True, layout=UM,
    hook_lines=["THIS STRANGER IS IN COURT", "OVER $100 MILLION..."],
    highlight=["court,", "hundred", "million", "dollars,", "alive.", "money.", "protect", "stress", "gym"],
    fix={"hundred": "$100", "million": "MILLION"},
    parts=[dict(src="n1_court", a=136.0, b=143.4, zoom="top", zoom_at=137.4, zoom_len=1.8, caps=[(0.0, 1.5, "WHEN YOU GO TO COURT"), (1.5, 2.9, "OVER $100 MILLION,"), (2.9, 4.6, "YOU'LL SEE THAT IT"), (4.6, 5.9, "AFFECTS YOUR MENTAL HEALTH"), (5.9, 7.4, "AND PHYSICAL HEALTH.")]),
           dict(src="n1_court", a=144.6, b=162.3, zoom="bot", zoom_at=145.3, zoom_len=1.6),
           dict(src="n1_court", a=171.5, b=175.0),
           dict(src="n1_court", a=177.9, b=184.6),
           dict(src="n1_court", a=187.5, b=192.6, zoom="bot", zoom_at=188.0, zoom_len=1.6)]),
}
if __name__ == "__main__":
    for k in sys.argv[1:]:
        for p in SPECS[k]["parts"]:
            for kk, vv in SPECS[k]["layout"].items(): p.setdefault(kk, vv)
        out, tot = build(SPECS[k])
        preview(out, [0.3] + [round(tot * f, 2) for f in (0.15, 0.3, 0.45, 0.6, 0.75, 0.95)], f"work/{k}_prev.jpg")
