import json, glob, os, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=4)
out = {}
for f in sorted(glob.glob("wav/*.pcm")):
    k = os.path.basename(f)[:-4]
    a = np.fromfile(f, dtype=np.int16).astype(np.float32) / 32768
    try:
        segs, _ = m.transcribe(a, word_timestamps=True, beam_size=5, condition_on_previous_text=False)
        out[k] = [(round(w.start,2), round(w.end,2), w.word.strip()) for s in segs for w in s.words]
    except Exception as e:
        out[k] = []
    json.dump(out, open("words.json", "w"))
print("done")
