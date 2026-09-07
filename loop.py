#!/usr/bin/env python3
"""See → gate → drum → hear → speak."""
from __future__ import annotations

import argparse

from senses import Drum, Ear, Eye, Mouth

# local tiny gate so this repo runs alone; swap for GCAC.Gate later
DEAD = 0.08


def gate(motion: float, guitar: bool) -> int:
    drive = motion + (0.2 if guitar else 0.0)
    if abs(drive) < DEAD:
        return 0
    return 1 if drive > 0 else -1


def bar(t: int, word: str, eye: Eye, ear: Ear, drum: Drum, mouth: Mouth) -> dict:
    frame = eye.grab(t)
    guitar = (t % 4 == 0)  # stub: guitar hits the downbeat
    decision = gate(frame.motion, guitar)
    hit = drum.hit(frame.motion + 0.25 * decision) if decision >= 0 else False
    heard = ear.hear(hit, guitar)
    spoken = mouth.say(word if hit else "")
    return {
        "t": t,
        "gray": round(frame.mean, 3),
        "motion": round(frame.motion, 3),
        "gate": decision,
        "hit": hit,
        "guitar": guitar,
        "heard": heard["room"],
        "said": spoken,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--beats", type=int, default=8)
    p.add_argument("--word", default="bucket")
    args = p.parse_args()
    eye, ear, drum, mouth = Eye(), Ear(), Drum(), Mouth()
    print("BUCKET-R2 loop")
    print(f"{'t':>3} {'gray':>6} {'mot':>6} {'g':>3} {'hit':>5} {'gtr':>5} {'said'}")
    for t in range(args.beats):
        r = bar(t, args.word, eye, ear, drum, mouth)
        print(
            f"{r['t']:3d} {r['gray']:6.3f} {r['motion']:6.3f} {r['gate']:3d} "
            f"{str(r['hit']):>5} {str(r['guitar']):>5} {r['said']}"
        )


if __name__ == "__main__":
    main()
