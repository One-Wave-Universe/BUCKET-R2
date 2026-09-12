# BUCKET-R2

A bucket with opinions.

Grayscale eye. Speaker drum. Guitar in the room. Language loop on a Jetson when you plug one in.

This repo is the **loop**, not the shopping list.

```
see (gray world) → feel the beat → hit the bucket → hear yourself → say a word → see again
```

The word is no longer a CLI toy. Each bar steps the HEX-SPLIT fifths walk (`clock.py`). Mouth says the gray sticker only if the drum hit. Guitar stub lands on Express polarity. Compress bars listen harder.

Sister benches: [GCAC](https://github.com/One-Wave-Universe/GCAC) for the gate that decides *whether* to hit. [HEX-SPLIT](https://github.com/One-Wave-Universe/HEX-SPLIT) for `clock.json` — copy it beside `clock.py` when you want the benches to share one file.

## Run the dry loop (no hardware)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python loop.py
python loop.py --beats 24
```

You get a receipt: fake frames, drum hits, Express/Compress guitar flag, spoken gray sticker. When a camera and a speaker exist, replace the stubs in `senses.py`. `midi` on each slot is waiting for the speaker body.

## Hardware spine (when you kick the actual bucket)

- eye: any USB cam, force grayscale, small frame (160x120 is plenty)
- drum: one speaker on the bucket wall. Not pretty. Coupled.
- guitar: room mic or line-in. Onset, not transcription, first.
- brain: Jetson if you have it; this laptop if you don't. GCAC gate decides hit/hold/listen.
- mouth: espeak / piper / whatever is installed. One gray sticker per earned bar until it earns sentences.

## Rule

Language is learned *on the beat*, not in a quiet corpus. If it cannot drum, it does not get to talk.
