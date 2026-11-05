import sys; sys.path.insert(0, "tools")
from irlgen import build, preview
S = "jordan"
SPEC = dict(out="mlc_jordan_double", credit="",
    hook_lines=["HE BET $1,000 ON ONE HAND", "AND DOUBLED DOWN..."],
    highlight=["four", "$2,000", "permission,", "$1,000", "double.", "jordan", "jordan!", "god!", "savior.", "walking"],
    parts=[dict(src=S, a=179.4, b=185.1, x=960, zoom_at=181.2, zoom_len=1.4, fix={"two": "$2,000"}, drop=["thousand", "dollars"]),
           dict(src=S, a=23.1, b=25.9, x=960, flash=True, drop=["correct,"]),
           dict(src=S, a=62.0, b=70.6, x=960, fix={"thousand": "$1,000"}, drop=["our", "it"]),
           dict(src=S, a=96.9, b=99.4, x=960, fix={"thousand": "$1,000"}, drop=["-hour"]),
           dict(src=S, a=118.8, b=130.6, x=960),
           dict(src=S, a=133.6, b=139.0, x=960, flash=True),
           dict(src=S, a=145.4, b=149.75, x=960)])
END = 41.15
def card(t, x, y, txt, col="&H00000000&", back=False):
    w, h = 150, 210
    fill = "&H00A05020&" if back else "&H00FFFFFF&"
    box = f"m {x} {y} l {x+w} {y} {x+w} {y+h} {x} {y+h}"
    ev = [(t, END, "Bar", f"{{\\pos(0,0)\\an7\\c{fill}\\bord4\\3c&H00FFFFFF&\\fad(120,0)\\t(0,150,\\fscx100)}}{{\\p1}}{box}{{\\p0}}", 6)]
    ev.append((t, END, "Hook", f"{{\\pos({x + w//2},{y + h//2})\\c{col}\\bord0\\shad0\\fs120\\fad(120,0)}}{txt}", 7))
    return ev
def label(t, x, y, txt, col="&H00FFFFFF&", fs=48, end=END, extra=""):
    return [(t, end, "Hook", f"{{\\pos({x},{y})\\c{col}\\fs{fs}\\fad(150,0){extra}}}{txt}", 7)]
YEL, GRN, RED = "&H0000E5FF&", "&H0050E650&", "&H003030E0&"
EXTRA = (label(8.6, 540, 345, "DEALER", fs=44) + label(8.6, 540, 895, "MARK", fs=44)
         + label(5.75, 540, 780, "CAMERA DOWN · NO FILMING AT THE TABLE", fs=40, end=11.5)
         + card(11.64, 385, 925, "A") + card(13.04, 545, 925, "4", RED)
         + card(16.16, 465, 375, "3", RED)
         + label(14.6, 540, 650, "DOUBLE DOWN · $1,000", YEL, 56, extra="\\fscx130\\fscy130\\t(0,200,\\fscx100\\fscy100)")
         + card(20.9, 705, 925, "?", "&H00FFFFFF&", back=True)
         + label(22.62, 540, 770, "JORDAN?", YEL, 80, end=31.4, extra="\\t(0,400,\\fscx115\\fscy115)\\t(400,800,\\fscx100\\fscy100)")
         + label(31.55, 540, 770, "HE WON", GRN, 110, extra="\\fscx160\\fscy160\\t(0,180,\\fscx100\\fscy100)"))
SPEC["extra"] = EXTRA
for i in (1, 2, 3, 4, 5, 6): SPEC["parts"][i]["dim"] = True

if __name__ == "__main__":
    out, tot = build(SPEC)
    preview(out, [0.1, 1.5, 3.0, 6.5, 10, 16, 20, 26, 31, 36, tot - 0.5], "work/jordan_prev.jpg")
