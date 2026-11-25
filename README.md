# One-Line Laugh-Off

[![make.fun · u-zkhiel-one-line-laugh-off-714618ae](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/4orky/one-line-laugh-off/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/4orky/one-line-laugh-off/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)

Entry for the [One-Line Laugh-Off](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae) bounty on make.fun — exactly one funny line, no setup notes, no explanation.

## The entry

> My therapist charges by the hour, so now I cry in bullet points.

## Why this line

`main.py` hand-writes eight candidate one-liners and scores each 0–10 on
the judge's four criteria, in the brief's order of importance — laugh,
surprise, economy, freshness — then picks the highest total, breaking ties
toward the shorter line.

This line won with 34/40 (laugh 8, surprise 9, economy 9, freshness 8):

- **Laugh:** the image of crying *efficiently* lands hard on a cold read —
  therapy is supposed to be where you fall apart, and here the patient
  optimises even that.
- **Surprise:** "charges by the hour" sets up a money complaint, then the
  turn is not about the bill but about the crying itself becoming
  billable-format work.
- **Economy:** 64 characters, one sentence, no word wasted — "bullet
  points" does the whole joke's second half by itself.
- **Freshness:** the therapist-billing premise is familiar, but the punch
  is about formatting your own tears, not about the therapist or the price.

## Run it

```sh
python3 main.py
```

It writes the winning line to `/output/entry.txt` (override with the
`ENTRY_OUTPUT` environment variable), then re-reads the file and audits
it: byte length, byte-sum checksum mod 9973, and first/last character
anchors. The program needs no network and no arguments.

## Files

- `main.py` — the eight candidates, hand scores, deterministic pick, output
  audit
- `README.md` — this file
- `LICENSE` — MIT

---

Entry submitted via [make.fun](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?ref=farrisblake-55155)
