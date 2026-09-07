# BUCKET-R2

A bucket with opinions.

Grayscale eye. Speaker drum. Guitar in the room. Language loop on a Jetson when you plug one in.

This repo is the **loop**, not the shopping list.

```
see (gray world) → feel the beat → hit the bucket → hear yourself → say a word → see again
```

Sister benches: [GCAC](https://github.com/One-Wave-Universe/GCAC) for the gate that decides *whether* to hit. [HEX-SPLIT](https://github.com/One-Wave-Universe/HEX-SPLIT) for the 12-tone clock the drum can follow.

## Run the dry loop (no hardware)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python loop.py
python loop.py --beats 16 --word hello
```

You get a receipt: fake frames, drum hits, heard onsets, spoken token. When a camera and a speaker exist, replace the stubs in `senses.py`.

## Hardware spine (when you kick the actual bucket)

- eye: any USB cam, force grayscale, small frame (160x120 is plenty)
- drum: one speaker on the bucket wall. Not pretty. Coupled.
- guitar: room mic or line-in. Onset, not transcription, first.
- brain: Jetson if you have it; this laptop if you don't. GCAC gate decides hit/hold/listen.
- mouth: espeak / piper / whatever is installed. One word per bar until it earns sentences.

## Rule

Language is learned *on the beat*, not in a quiet corpus. If it cannot drum, it does not get to talk.
