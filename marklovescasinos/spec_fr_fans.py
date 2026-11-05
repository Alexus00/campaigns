import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
# YOUTUBE (IRL, no gambling). Dropbox IRL folder: "2026-10-19 VEGAS FREMONT STREAM.mp4" 1425 s -> src/fr_zach.mp4 (t = source - 1425).
# Fan Zach came to Vegas for his birthday, saw Mark was in town on Instagram, found him at the Fremont arcade.
# NOTE "could find you" = Whisper heard "teach you" (boosted audio, Zach is quiet); meaning is clear from context.
S = "fr_zach"; Z = dict(x=1150)
P = [
    dict(src=S, a=7.85, b=12.05, **Z),                                     # "I came out here for my birthday... he's coming to town"
    dict(src=S, a=16.90, b=21.40, **Z),                                    # "I look on Instagram... he's f*cking here"
    dict(src=S, a=23.10, b=28.75, **Z, zoom_at=26.5, zoom_len=1.5),        # Mark: "of course dude... what's your name" / "I'm Zach"
    dict(src=S, a=58.50, b=63.55, x=1100, flash=True),                     # Mark: "it always makes me so happy when I meet a friend..."
]
SPEC = dict(out="yt_fan_birthday_vegas", credit="", progress=True,
    hook_lines=["BIRTHDAY TRIP TO VEGAS...", "AND MARK WAS IN TOWN"],
    highlight=["birthday", "town.", "instagram", "here.", "zach.", "happy", "smile"],
    fix={"fontainebleau.": "FONTAINEBLEAU."}, parts=P)
if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.0, 2.0, 4.5, 7.0, 9.5, 12.0, 14.0, 16.0, tot - 0.3], "work/fr_fans_prev.jpg")
