import sys, subprocess, os; sys.path.insert(0, "tools")
import numpy as np, wave
from irlgen import build, preview
# TEST B — BRAINROT: 5 of Mark's loudest hype moments from vegas_928 (none used in other clips), fast cuts,
# punch-in zoom + flash on every cut, "W" counter, bass-boom SFX on each cut (synthetic, no voice). Own audio everywhere.
# Sources (vegas_928 seconds): br1=3805+ (Frankenstein wager saver), br2=4336+ (coin flip minor), br4=258+ (first bonus),
#                              br5=7745+ (diamond), br6=4965+ (golden spin).
P = [
    dict(src="br4", a=12.35, b=14.45, x=900, zoom_at=12.4, zoom_len=0.9),    # "f*cking bonus, baby. okay, let's go"
    dict(src="br5", a=26.85, b=28.15, x=960, zoom_at=26.9, zoom_len=0.6, flash=True,
         caps=[(0.0, 0.6, "WE GOT A"), (0.6, 0.95, "DIAMOND!"), (0.95, 1.3, "DIAMOND!")]),    # "we got a diamond, we got a diamond"
    dict(src="br6", a=13.35, b=14.95, x=960, zoom_at=13.6, zoom_len=0.8, flash=True),    # "we got the m*f golden spin"
    dict(src="br2", a=18.55, b=21.55, x=960, zoom_at=20.4, zoom_len=1.1, flash=True),    # "we're up. we got the minor, baby. we got the minor"
    dict(src="br1", a=22.15, b=24.65, x=900, zoom_at=22.2, zoom_len=1.0, flash=True),    # "I'm the f*cking wager saver!"
    dict(src="br1", a=25.25, b=26.35, x=900, zoom_at=25.3, zoom_len=1.05, flash=True),   # "HOLY SH*T!"
]
SPEC = dict(out="mlc_vegas_in_12_seconds", credit="", progress=True,
    hook_lines=["3 HOURS OF VEGAS", "IN 12 SECONDS"],
    highlight=["bonus,", "baby.", "diamond,", "diamond.", "golden", "spin.", "miner,", "miner.", "saber!", "holy", "shit!", "go."],
    fix={"miner": "MINOR", "saber": "SAVER!", "motherfucking": "M*THERF*CKING"},
    drop=["okay"], parts=P)

t, T = 0.0, []
for p in P: T.append(t); t += round((p["b"] - p["a"]) * 30) / 30
END = t
YEL, GRN, WHT = "&H0000E5FF&", "&H0050E650&", "&H00FFFFFF&"
def lab(st, en, x, y, txt, col=WHT, fs=56, layer=7):
    return (st, en, "Hook", f"{{\\pos({x},{y})\\c{col}\\fs{fs}\\fscx170\\fscy170\\t(0,140,\\fscx100\\fscy100)}}{txt}", layer)
SPEC["extra"] = [lab(T[i], T[i + 1] if i + 1 < len(T) else END, 540, 440, f"W #{i + 1}", GRN if i < 5 else YEL, 96) for i in range(len(P))]

def boom_track(path, total, times):
    SR = 48000; buf = np.zeros(int((total + 1) * SR))
    tt = np.arange(int(0.45 * SR)) / SR
    boom = np.sin(2 * np.pi * (70 * np.exp(-tt * 4)) * tt * 3) * np.exp(-tt * 9) * 0.55     # deep pitch-drop thump
    click = np.random.default_rng(1).standard_normal(int(0.012 * SR)) * np.exp(-np.arange(int(0.012 * SR)) / 80) * 0.25
    for x in times:
        i = int(x * SR); buf[i:i + len(boom)] += boom[: len(buf) - i]; buf[i:i + len(click)] += click[: len(buf) - i]
    pcm = (np.clip(buf[: int(total * SR)], -1, 1) * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())

if __name__ == "__main__":
    out, tot = build(SPEC)
    sfx = "work/brainrot_sfx.wav"; boom_track(sfx, tot, T)
    tmp = out[:-4] + "_nosfx.mp4"; os.replace(out, tmp)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-i", sfx, "-filter_complex",
                    "[1:a]volume=0.8,aresample=48000[s];[0:a][s]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", out], check=True)
    os.remove(tmp)
    preview(out, [0.0, 1.2, 2.5, 3.6, 5.0, 6.5, 8.0, 9.5, 11.0, 12.3, tot - 0.2], "work/brainrot_prev.jpg")
    print("with sfx:", out)
