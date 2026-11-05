# Mark Loves Casinos — status (Nov 5 2026)

## Accounts
- Instagram: **one_scroll_man** (main IG for this campaign). Owner also posted 1 reel on another IG account while on a Mumbai VPN (audience risk; advised delete+repost if not submitted). Rule: NO VPN.
- YouTube: **@WhyNotTop-3** (IRL only).

## Clips made (videos are NOT in git — rebuild with spec_*.py after re-downloading sources)
| Clip | Platform | Spec | Posted? |
|---|---|---|---|
| mlc_jordan_double ($1,000 double, blackjack graphic) | IG | spec_jordan.py | posted Nov 5 |
| mlc_bonus_in_bonus ($25 Dragon Link, $1,775) | IG | spec_bonus.py | posted (other account, Mumbai VPN) |
| mlc_top_dollar (take it or try again, offer tracker) | IG | spec_td.py | not yet (post next) |
| mlc_craps_hit_and_run ($1,100 bubble craps) | IG | spec_craps.py | not yet |
| mlc_black_or_red (gamble feature, chat vote) | IG | spec_gb.py | not yet |
| mlc_fan_inspired (fan Luca: "this guy inspired me") | YT | spec_luca.py | not yet |
| mlc_37_points (Fremont arcade basketball) | YT | spec_bball.py | not yet |
| mlc_joker_origin (Joker costume, wholesome origin) | YT | spec_joker.py | not yet |
| mlc_handpay_reveal ($30 spin → $2,555.50 hand pay, reaction first / win last) | IG | spec_handpay.py | not yet (made Nov 5) |
Captions for all: CAPTIONS.md. Ask owner for 24h/72h stats → clips_log.csv.

## Sources (only streams that are in the official folders)
- Drive IRL folder 12FFsKvbUW4dSvl_UWduhiEcUUrcOcVfi / Gambling 1VWFQ95eDWOZ3FW_Cledxb0PkPDXH4GWD → usually "Quota exceeded".
- Owner's Drive copy (works): folder 162XLZ-208-o1PDuV70VENAqGubC1pPdn → IRL VEGAS 9:28 (id 1gUKoGvGoocpVmmDiqto_gFj2OLPQT1j9, 5.7 GB, 3h14) + Nashville Part 7. Download: tools/gdl.sh <id> <name>.
- Kick VODs of the same IRL streams (owner asked Clipping Culture to confirm): irl_vods.txt, kick_vods.txt (Fremont 133254715, Crazy Joker 135166268, Nashville 135003697, Vegas $5k 133107875). HD range: tools/getrange.py <m3u8> <name> <a> <b>.
- Source-time map of segments used (vegas_928 seconds): jordan 8830+, bonus 2250+, profit 10330+, craps 9560+, gamblebonus 6780+, diamond 6060+, bonus32 1860+, topdollar 6170+, handpay 850-1250 (src/handpay.mp4 = vegas_928 from 850 s); fremont bball 1290+; joker jk_origin 805+, jk_street 165+.

## Unused moments worth checking next
- vegas_928: 0:31 "we just did a bonus, big boss" (bonus32, $12.50 spin → $875 on screen 34:00), 1:03 Frankenstein "it's alive / wager saver" ($24 spin → MINOR $450, WIN $468), 3:11 last spin of night, first-ever old-school pinball ("put in 1700, taking out 2400"), 1:42 triple-diamond near hand-pay (diamond).
- vegas_928 0:14–0:21 hand pay = USED (mlc_handpay_reveal).
- Fremont (IRL/YT): 20:00 claw machine "these are rigged", 23:48 fan Zach came for his birthday and found Mark.
- Crazy Joker (IRL): 1:13 Abigail "you're intimidating me", 1:27 impersonations, 0:09 "you're Batman" bar banter. AVOID 16:00–19:00 (veteran talks about rape — banned content) and the "pencil trick"/"kitchen drawer" lines (violent).
- Nashville Just Landed (transcripts/nash_tr.txt): not reviewed yet. Vegas $5k at casino (transcripts/vegas5k_tr.txt): transcribed, not reviewed yet.

## Open questions
- Clipping Culture: OK to use Kick VODs of the same streams? (owner asked)
- frame.io overlay link: one file or separate IRL/Gambling overlays?
- one_scroll_man audience countries (Tier 1–2 needed).

## Setup in a fresh container
pip install faster-whisper pillow numpy yt-dlp ; ffmpeg needed. Fonts: ../fonts (symlink in this folder). Work dirs src/ wav/ work/ out/ are git-ignored — create them.
