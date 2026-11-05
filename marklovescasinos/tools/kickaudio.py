"""python3 tools/kickaudio.py <master.m3u8> <start_s> <dur_s> <out.pcm> : 160p HLS audio slice -> 16k mono pcm (for offset matching)"""
import sys, subprocess, os, tempfile
url, st, du, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
base = url.rsplit("/", 1)[0] + "/160p30"
pl = subprocess.run(["curl", "-s", "-m", "60", f"{base}/playlist.m3u8"], capture_output=True, text=True).stdout.splitlines()
t, segs, first = 0.0, [], None
for i, l in enumerate(pl):
    if l.startswith("#EXTINF:"):
        d = float(l[8:].split(",")[0]); name = pl[i + 1]
        if t + d > st and t < st + du:
            segs.append(name); first = t if first is None else first
        t += d
d = tempfile.mkdtemp()
for k, s in enumerate(segs):
    subprocess.run(["curl", "-s", "-m", "120", "--retry", "4", "-o", f"{d}/{k:04d}.ts", f"{base}/{s}"])
open(f"{d}/l.txt", "w").write("".join(f"file '{k:04d}.ts'\n" for k in range(len(segs))))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{d}/l.txt", "-vn", "-ss", f"{st - first}", "-t", f"{du}",
                "-ac", "1", "-ar", "16000", "-f", "s16le", out], check=True)
print(out, "from", st)
