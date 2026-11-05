"""python3 tools/tr.py name [model]  -> words/<name>.json + printed transcript with lang check"""
import json, sys, os, numpy as np
from faster_whisper import WhisperModel
n = sys.argv[1]; md = sys.argv[2] if len(sys.argv) > 2 else "small"
m = WhisperModel(md, device="cpu", compute_type="int8", cpu_threads=4)
a = np.fromfile(f"wav/{n}.pcm", dtype=np.int16).astype(np.float32) / 32768
segs, info = m.transcribe(a, word_timestamps=True, beam_size=5, condition_on_previous_text=False, vad_filter=True)
segs = list(segs); os.makedirs("words", exist_ok=True)
json.dump([(round(w.start, 2), round(w.end, 2), w.word.strip()) for s in segs for w in s.words], open(f"words/{n}.json", "w"))
print(n, info.language, round(info.language_probability, 2))
for s in segs: print(f"{int(s.start//60):3d}:{s.start%60:05.2f} {s.text.strip()}")
