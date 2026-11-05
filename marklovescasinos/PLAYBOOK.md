# Mark Loves Casinos — editing playbook (living doc, update after every stats round)

## Pipeline (fast path, ~15–25 min per clip)
1. Source: Kick VOD of a stream that is in the official folder → `tools/scanvod.py <m3u8> <name>` (160p audio + loud peaks) → `tools/tr.py <name> small.en`.
2. Pick moments: loud peaks + keyword minutes (wins, strangers, decisions). Reject: gambling on YT, sexual/violent talk, Mark looking bad, Stake/online casino.
3. HD range: `tools/getrange.py <m3u8> <clip> <a> <b>` → `tools/tr.py <clip> medium.en`.
4. Spec file `spec_<clip>.py` → `tools/irlgen.py` (Kick overlay, captions from 0.0, censor, `extra` graphics, `dim`, `vsrc/va` cutaways, `freeze`, `slow`).
5. QA: preview strip, first frame (caption + strong visual), no dead visuals > 3 s, SAR 1:1, overlay above IG/YT UI, ≥10 s, true header.
6. Cover: `tools/cover.py` (grid-safe 3:4 centre). Caption: line + @marklovescasinos / #Ad / ≤3 tags.

## Formats we have (reuse)
| Format | Example | Graphic |
|---|---|---|
| Result-first + table tracker | mlc_jordan_double | blackjack cards from his own calls |
| Take it or try again | mlc_top_dollar | offer tracker 30·30·30·35 → FINAL |
| Chat decides | mlc_black_or_red | live vote labels |
| Goal vs score | mlc_37_points | GOAL: 37 → SCORE: 35 |
| Iconic-quote costume | mlc_joker_origin | close-up cutaway hook |
| Wholesome stranger | mlc_fan_inspired | quote hook |

## Lessons (update with real stats)
- Nov 5 stats (IG one_scroll_man): jordan_double (result-first: $1,000 + double down, table graphic) 2,418 views/6 h, skip 34%, avg 14 s of 41 s.
  handpay_reveal (reaction-first, amount hidden) 97 views/1 h, skip 52.6%, avg 10 s of 28 s. → Stake/decision + money context in frame 1 beats a mystery reaction. Viewers leave ~10–14 s → aim ≤ 22 s.
- Exact $ / number in first words; one risky decision; payoff on screen (research Nov 5).
- LIP SYNC: a shot where Mark's face/mouth is visible must use its OWN audio (no `va`/`vsrc` J-cut). Borrowed footage only on no-face shots (screens, banners, chips). irlgen now renders parts frame-exact with PCM audio (fixed ~15 ms/part AAC drift on concat, Nov 5).
- Never > 3 s of dead visuals (floor/back of head) → dim + graphic or cutaway.
- Kick overlay at y=1380–1481 (IG/YT UI covers bottom ~20 %).
- Stats log: log/clips_log.csv (views_72h, stayed %, avg viewed %). After every 5 clips: compare formats, double down on the winner.
