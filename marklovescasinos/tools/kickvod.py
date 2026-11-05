"""python3 tools/kickvod.py <master.m3u8> <name> [quality]  -> src/<name>.mp4 + wav/<name>.pcm"""
import sys, subprocess, os, concurrent.futures as cf
url, name = sys.argv[1], sys.argv[2]; q = sys.argv[3] if len(sys.argv) > 3 else "1080p60"
base = url.rsplit("/", 1)[0] + "/" + q
pl = subprocess.run(["curl", "-s", "-m", "60", f"{base}/playlist.m3u8"], capture_output=True, text=True).stdout.splitlines()
segs = [l for l in pl if l and not l.startswith("#")]
d = f"work/seg_{name}"; os.makedirs(d, exist_ok=True)
def get(i):
    out = f"{d}/{i:05d}.ts"
    if not os.path.exists(out) or os.path.getsize(out) == 0:
        subprocess.run(["curl", "-s", "-m", "180", "--retry", "4", "-o", out, f"{base}/{segs[i]}"])
with cf.ThreadPoolExecutor(12) as ex: list(ex.map(get, range(len(segs))))
open(f"{d}/list.txt", "w").write("".join(f"file '{i:05d}.ts'\n" for i in range(len(segs))))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{d}/list.txt", "-c", "copy", f"src/{name}.mp4"], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"src/{name}.mp4", "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", f"wav/{name}.pcm"], check=True)
subprocess.run(["rm", "-rf", d]); print(name, len(segs), "segments done")
