"""python3 tools/scanvod.py <master.m3u8> <name> : 160p audio -> wav/<name>.pcm, words/<name>.json (base.en), work/<name>_loud.txt"""
import sys, subprocess, os, json, concurrent.futures as cf, numpy as np
url, name = sys.argv[1], sys.argv[2]; base = url.rsplit("/", 1)[0] + "/160p30"
pl = subprocess.run(["curl", "-s", "-m", "60", f"{base}/playlist.m3u8"], capture_output=True, text=True).stdout.splitlines()
segs = [l for l in pl if l and not l.startswith("#")]; d = f"work/lo_{name}"; os.makedirs(d, exist_ok=True)
def get(i):
    o = f"{d}/{i:05d}.ts"
    if not os.path.exists(o) or os.path.getsize(o) == 0: subprocess.run(["curl", "-s", "-m", "120", "--retry", "4", "-o", o, f"{base}/{segs[i]}"])
with cf.ThreadPoolExecutor(16) as ex: list(ex.map(get, range(len(segs))))
open(f"{d}/list.txt", "w").write("".join(f"file '{i:05d}.ts'\n" for i in range(len(segs))))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{d}/list.txt", "-c", "copy", f"work/{name}_lo.mp4"], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"work/{name}_lo.mp4", "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", f"wav/{name}.pcm"], check=True)
subprocess.run(["rm", "-rf", d])
a = np.memmap(f"wav/{name}.pcm", dtype=np.int16, mode="r"); SR = 16000; n = len(a) // SR
db = np.array([20 * np.log10(np.sqrt(np.mean((a[i*SR:(i+1)*SR].astype(np.float32) / 32768) ** 2)) + 1e-6) for i in range(n)])
sm = np.convolve(db, np.ones(3) / 3, "same"); base_db = np.median(db); picked = []
for i in np.argsort(-sm):
    if all(abs(i - p) > 90 for p in picked): picked.append(int(i))
    if len(picked) >= 25: break
open(f"work/{name}_loud.txt", "w").write("\n".join(f"{p} {sm[p]-base_db:.1f}" for p in sorted(picked)))
print(name, len(segs), "segs; loud peaks saved")
