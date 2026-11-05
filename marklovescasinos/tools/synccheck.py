"""python3 tools/synccheck.py spec_x.py : per-part audio offset (ms) of out/<name>.mp4 vs source wav/<src>.pcm (0 = lip sync OK)"""
import sys, subprocess, numpy as np
src = open(sys.argv[1]).read(); g = {}
exec(src.split('if __name__')[0].replace("from irlgen import build, preview", ""), g)
P, out = g["P"] if "P" in g else g["SPEC"]["parts"], g["SPEC"]["out"]
raw = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", f"out/{out}.mp4", "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
f = np.frombuffer(raw, np.int16).astype(np.float32); SR = 16000
env = lambda x: np.abs(x[:len(x) // 160 * 160]).reshape(-1, 160).mean(1)
t, res = 0.0, []
for p in P:
    s = np.fromfile(f"wav/{p['src']}.pcm", np.int16).astype(np.float32); dur = p["b"] - p["a"] - 0.1
    fe = env(f[int((t + .05) * SR):int((t + .05 + dur) * SR)]); best = None
    for lag in range(-30, 31):
        st = int((p["a"] + .05) * SR) + lag * 160; se = env(s[st:st + int(dur * SR)]); n = min(len(fe), len(se))
        c = np.corrcoef(fe[:n], se[:n])[0, 1]
        if best is None or c > best[1]: best = (lag * 10, c)
    res.append(best[0]); t += round((p["b"] - p["a"]) * 30) / 30
print(out, "sync ms:", res)
